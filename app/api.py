"""FastAPI app: LAN UI + collaborative plan + research job API."""

from __future__ import annotations

import logging
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from src.config import OUTPUT_DIR, settings
from src.jobs import job_store
from src.nlp_engine import ollama_available
from src.orchestrator import run_research, run_with_plan
from src.plan_schema import ResearchPlan
from src.plan_templates import list_templates
from src.planner import apply_plan_edits, generate_plan
from src.report_tabs import build_report_tabs, job_href
from src.research_queue import QueueWorker, queue_store
import src.research_queue as research_queue_mod
from src.sync_store import export_all_completed, export_job_id, import_all_sync_jobs

logger = logging.getLogger(__name__)

APP_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(APP_DIR / "templates"))

app = FastAPI(title="Equity Research Agent", version="0.2.0")
app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")
(OUTPUT_DIR / "charts").mkdir(parents=True, exist_ok=True)
app.mount("/charts", StaticFiles(directory=str(OUTPUT_DIR / "charts")), name="charts")


@app.on_event("startup")
def _sync_on_startup() -> None:
    """Pull git-tracked research packs into local SQLite (cloud ↔ local)."""
    try:
        stats = import_all_sync_jobs(job_store)
        if any(stats.get(k, 0) for k in ("inserted", "updated")):
            logger.info("Startup sync: %s", stats)
    except Exception:  # noqa: BLE001
        logger.exception("Startup sync import failed")

    # Daemon worker threads die with the process; mark in-flight jobs failed so the UI is not stuck.
    try:
        n = _fail_orphaned_jobs()
        if n:
            logger.info("Marked %s orphaned in-flight job(s) as failed on startup", n)
    except Exception:  # noqa: BLE001
        logger.exception("Orphan job cleanup failed")

    # Re-queue interrupted overnight items, then start the sequential worker.
    try:
        rq = queue_store.reset_interrupted()
        if rq:
            logger.info("Re-queued %s interrupted research-queue item(s)", rq)
        research_queue_mod.queue_worker = QueueWorker(
            queue_store,
            start_job=_start_job_flow,
            get_job=job_store.get,
            poll_seconds=5.0,
        )
        research_queue_mod.queue_worker.start()
    except Exception:  # noqa: BLE001
        logger.exception("Research queue worker failed to start")


def _fail_orphaned_jobs() -> int:
    """Fail jobs left in running/planning/queued after a process restart."""
    now = datetime.now(timezone.utc).isoformat()
    count = 0
    for j in job_store.list_recent(200):
        if j.status not in {"running", "planning", "queued"}:
            continue
        msg = (
            f"Interrupted by app restart while {j.status}"
            + (f" ({j.stage}: {j.message})" if j.stage or j.message else "")
            + ". Re-run the ticker to continue."
        )
        job_store.update(
            j.id,
            status="failed",
            stage="error",
            message=msg,
            error=msg,
            finished_at=now,
        )
        try:
            job_store.append_thought(j.id, "gap", msg)
        except Exception:  # noqa: BLE001
            pass
        _export_job_sync(j.id)
        count += 1
    return count


def _export_job_sync(job_id: str) -> None:
    try:
        export_job_id(job_store, job_id)
    except Exception:  # noqa: BLE001
        logger.exception("Job sync export failed for %s", job_id)

class ResearchRequest(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=12)
    mode: str = Field(default="deep", pattern="^(fast|deep|comprehensive)$")
    goal: str = ""
    template: str = "auto"
    collaborative: bool = True
    from_scratch: bool = False
    pin: str | None = None


class ApproveRequest(BaseModel):
    goal: str | None = None
    sections: list[dict[str, Any]] | None = None
    assumptions: dict[str, Any] | None = None
    multiples: dict[str, Any] | None = None
    pin: str | None = None


def _check_pin(pin: str | None) -> None:
    if settings.access_pin and (pin or "") != settings.access_pin:
        raise HTTPException(status_code=401, detail="Invalid PIN")


def _slim_result(result: dict[str, Any]) -> dict[str, Any]:
    if result.get("kind") == "pack":
        return {
            "kind": "pack",
            "ticker": result.get("ticker"),
            "mode": result.get("mode"),
            "template": "all",
            "generated_at": result.get("generated_at"),
            "goal": result.get("goal"),
            "template_reports": result.get("template_reports") or [],
            "report_markdown": result.get("report_markdown"),
            "report_path": result.get("report_path"),
            "charts": result.get("charts") or {"charts": []},
            "pack_progress": result.get("pack_progress"),
        }
    return {
        "ticker": result.get("ticker"),
        "mode": result.get("mode"),
        "generated_at": result.get("generated_at"),
        "financials_path": result.get("financials_path"),
        "report_path": result.get("report_path"),
        "report_markdown": result.get("report_markdown"),
        "sections": result.get("sections"),
        "nlp": result.get("nlp"),
        "plan": result.get("plan"),
        "evidence": result.get("evidence"),
        "valuation": result.get("valuation"),
        "web": result.get("web"),
        "loop": result.get("loop"),
        "critique": result.get("critique"),
        "charts": result.get("charts"),
        "quant_summary": {
            "ratios": ((result.get("quant") or {}).get("fundamentals") or {}).get("ratios"),
            "options_candidates": len(
                (((result.get("quant") or {}).get("options") or {}).get("candidates") or [])
            ),
        },
    }


def _fail_job(job_id: str, exc: Exception) -> None:
    job_store.update(
        job_id,
        status="failed",
        stage="error",
        message=str(exc),
        error=str(exc),
        finished_at=datetime.now(timezone.utc).isoformat(),
    )

def _plan_job(job_id: str) -> None:
    job = job_store.get(job_id)
    if not job:
        return
    try:
        job_store.update(job_id, status="planning", stage="planning", message="Drafting research plan…")
        plan = generate_plan(job.ticker, mode=job.mode, goal=job.goal, template=job.template)
        job_store.update(
            job_id,
            status="awaiting_approval",
            stage="awaiting_approval",
            message="Review and approve the plan",
            plan=plan.to_public_dict(),
        )
    except Exception as exc:  # noqa: BLE001
        _fail_job(job_id, exc)
        _export_job_sync(job_id)


def _run_job(job_id: str, *, use_plan_path: bool = True) -> None:
    job = job_store.get(job_id)
    if not job:
        return

    def progress(stage: str, message: str) -> None:
        job_store.update(job_id, status="running", stage=stage, message=message)

    def think(kind: str, message: str) -> None:
        job_store.append_thought(job_id, kind, message)

    try:
        job_store.update(job_id, status="running", stage="starting", message="Job started")
        think("think", f"Job started for {job.ticker} ({job.template or job.mode}).")
        if use_plan_path and job.plan:
            result = run_with_plan(job.plan, progress=progress, think=think)
        else:
            result = run_research(
                job.ticker,
                job.mode,
                progress=progress,
                goal=job.goal,
                template=job.template,
                use_plan=True,
            )
        job_store.update(
            job_id,
            status="completed",
            stage="done",
            message="Complete",
            result=_slim_result(result),
            plan=result.get("plan") or job.plan,
            finished_at=datetime.now(timezone.utc).isoformat(),
        )
        _export_job_sync(job_id)
    except Exception as exc:  # noqa: BLE001
        _fail_job(job_id, exc)
        _export_job_sync(job_id)


def _run_pack_job(job_id: str) -> None:
    from src.pack_runner import run_research_pack
    from src.plan_templates import PACK_TEMPLATE_IDS, TEMPLATES

    job = job_store.get(job_id)
    if not job:
        return

    def progress(stage: str, message: str) -> None:
        job_store.update(job_id, status="running", stage=stage, message=message)

    def think(kind: str, message: str) -> None:
        job_store.append_thought(job_id, kind, message)

    def on_child(partial: dict[str, Any]) -> None:
        reports = partial.get("template_reports") or []
        cur = partial.get("current")
        idx = partial.get("index") or 0
        total = partial.get("total") or len(PACK_TEMPLATE_IDS)
        job_store.update(
            job_id,
            status="running",
            stage="pack",
            message=f"Finished {TEMPLATES.get(cur, {}).get('label', cur)} ({idx}/{total})",
            result={
                "kind": "pack",
                "ticker": job.ticker,
                "template": "all",
                "template_reports": reports,
                "pack_progress": {"index": idx, "total": total, "current": cur},
                "report_markdown": "",
            },
        )

    try:
        job_store.update(
            job_id,
            status="running",
            stage="pack",
            message=f"Starting full pack ({len(PACK_TEMPLATE_IDS)} templates)",
            result={
                "kind": "pack",
                "ticker": job.ticker,
                "template": "all",
                "template_reports": [],
                "pack_progress": {"index": 0, "total": len(PACK_TEMPLATE_IDS), "current": None},
            },
        )
        think("think", f"Full pack started for {job.ticker}.")
        result = run_research_pack(
            job.ticker,
            goal=job.goal or "",
            mode=job.mode,
            progress=progress,
            think=think,
            on_child_done=on_child,
        )
        job_store.update(
            job_id,
            status="completed",
            stage="done",
            message="Full pack complete",
            result=_slim_result(result),
            finished_at=datetime.now(timezone.utc).isoformat(),
        )
        _export_job_sync(job_id)
    except Exception as exc:  # noqa: BLE001
        _fail_job(job_id, exc)
        _export_job_sync(job_id)


def _start_job_flow(
    ticker: str,
    mode: str,
    goal: str,
    collaborative: bool,
    template: str = "auto",
    from_scratch: bool = False,
) -> str:
    mode = "fast" if mode == "fast" else "deep"
    from src.plan_templates import resolve_template_id

    ticker = (ticker or "").upper().strip()
    scratch_note = ""
    if from_scratch:
        from src.fresh_run import clear_ticker_cache

        cleared = clear_ticker_cache(ticker)
        scratch_note = f"From scratch: cleared {cleared.get('count', 0)} cached file(s). "
        logger.info("from_scratch %s → %s", ticker, cleared)

    tid = resolve_template_id(template, goal=goal, mode=mode)
    # Full pack always auto-runs (no multi-plan approval UX)
    if tid == "all":
        job = job_store.create(ticker, mode, goal=goal, collaborative=False, template="all")
        if scratch_note:
            job_store.update(job.id, message=scratch_note + "Starting full pack…", stage="queued")
        threading.Thread(target=_run_pack_job, args=(job.id,), daemon=True).start()
        return job.id

    collab = collaborative and tid != "fast"
    job = job_store.create(
        ticker, mode, goal=goal, collaborative=collab, template=template or "auto"
    )
    if scratch_note:
        job_store.update(
            job.id,
            message=scratch_note + ("Planning…" if collab else "Starting…"),
            stage="queued",
        )
    if collab:
        _plan_job(job.id)
    else:
        threading.Thread(target=_run_job, args=(job.id,), daemon=True).start()
    return job.id


def _job_card(j: Any) -> dict[str, Any]:
    return {
        "id": j.id,
        "ticker": j.ticker,
        "status": j.status,
        "mode": j.mode,
        "template": j.template,
        "goal": j.goal or "",
        "created_at": j.created_at,
        "finished_at": j.finished_at,
        "href": job_href(j),
        "error": j.error,
    }


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, ticker: str = "", from_scratch: str = "") -> Any:
    recent = [_job_card(j) for j in job_store.list_recent(8)]
    scratch = (from_scratch or "").lower() in {"1", "true", "yes", "on"}
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "ollama_up": ollama_available(),
            "model": settings.ollama_model,
            "pin_required": bool(settings.access_pin),
            "templates": list_templates(),
            "recent_jobs": recent,
            "active_nav": "research",
            "prefill_ticker": (ticker or "").strip().upper(),
            "from_scratch": scratch,
        },
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    ticker: str = "",
    status: str = "",
) -> Any:
    ticker_q = (ticker or "").strip().upper()
    status_q = (status or "").strip().lower()
    if status_q and status_q not in {
        "queued",
        "planning",
        "awaiting_approval",
        "running",
        "completed",
        "failed",
    }:
        status_q = ""
    jobs = [
        _job_card(j)
        for j in job_store.list_recent(
            100,
            ticker=ticker_q or None,
            status=status_q or None,
        )
    ]
    total = job_store.count_jobs(ticker=ticker_q or None, status=status_q or None)
    # Latest completed per ticker for quick browse
    by_ticker: dict[str, dict[str, Any]] = {}
    for j in job_store.list_recent(100, status="completed"):
        if j.ticker not in by_ticker:
            card = _job_card(j)
            card["equity_href"] = f"/equities/{j.ticker}"
            by_ticker[j.ticker] = card
    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "jobs": jobs,
            "total": total,
            "ticker_q": ticker_q,
            "status_q": status_q,
            "tickers": sorted(by_ticker.values(), key=lambda x: x["ticker"]),
            "active_nav": "dashboard",
        },
    )


class QueueAddRequest(BaseModel):
    tickers: str = Field(..., min_length=1, description="Tickers separated by newline, comma, or space")
    template: str = "memo"
    mode: str = Field(default="deep", pattern="^(fast|deep|comprehensive)$")
    goal: str = ""
    from_scratch: bool = False
    # prompt_now: ntfy + auto-start after ~60s unless deferred
    # overnight: add only; run when Start overnight / resume deferred
    start_policy: str = Field(default="prompt_now", pattern="^(prompt_now|overnight)$")
    confirm_seconds: int = Field(default=60, ge=0, le=600)
    pin: str | None = None


class QueueControlRequest(BaseModel):
    pin: str | None = None


def _queue_kick() -> None:
    w = research_queue_mod.queue_worker
    if w:
        w.kick()


@app.get("/queue", response_class=HTMLResponse)
async def queue_page(request: Request) -> Any:
    return templates.TemplateResponse(
        request,
        "queue.html",
        {
            "ollama_up": ollama_available(),
            "model": settings.ollama_model,
            "pin_required": bool(settings.access_pin),
            "templates": list_templates(),
            "summary": queue_store.summary(),
            "items": [i.to_dict() for i in queue_store.list_items(limit=200)],
            "active_nav": "queue",
        },
    )


@app.get("/api/queue")
async def api_queue_status() -> dict[str, Any]:
    return {
        "summary": queue_store.summary(),
        "items": [i.to_dict() for i in queue_store.list_items(limit=200)],
    }


@app.post("/api/queue")
async def api_queue_add(body: QueueAddRequest) -> dict[str, Any]:
    _check_pin(body.pin)
    result = queue_store.add_tickers(
        body.tickers,
        template=body.template or "memo",
        mode=body.mode,
        goal=body.goal or "",
        from_scratch=body.from_scratch,
        skip_existing=True,
        start_policy=body.start_policy or "prompt_now",
        confirm_seconds=int(body.confirm_seconds),
    )
    created = result["created"]
    skipped = result["skipped"]
    if not created and not skipped:
        raise HTTPException(status_code=400, detail="No valid tickers found")
    if created:
        from src.queue_notify import notify_prompt_now

        if (body.start_policy or "prompt_now") == "prompt_now":
            notify_prompt_now(created, confirm_seconds=int(body.confirm_seconds))
            # Do not kick yet — hold_until gates claim_next; worker poll releases holds.
            if queue_store.get_paused():
                queue_store.set_paused(False)
            _queue_kick()
        else:
            # Overnight: leave deferred; do not start until Start overnight.
            pass
    return {
        "added": len(created),
        "tickers": [c.ticker for c in created],
        "created": [c.to_dict() for c in created],
        "skipped": skipped,
        "start_policy": body.start_policy,
        "summary": queue_store.summary(),
        "items": [i.to_dict() for i in queue_store.list_items(limit=200)],
    }


@app.post("/queue", response_class=HTMLResponse)
async def queue_add_form(
    request: Request,
    tickers: str = Form(...),
    template: str = Form("memo"),
    mode: str = Form("deep"),
    goal: str = Form(""),
    from_scratch: str | None = Form(None),
    start_policy: str = Form("prompt_now"),
    pin: str | None = Form(None),
) -> Any:
    try:
        _check_pin(pin)
        policy = (start_policy or "prompt_now").strip().lower()
        if policy not in {"prompt_now", "overnight"}:
            policy = "prompt_now"
        result = queue_store.add_tickers(
            tickers,
            template=template or "memo",
            mode=mode,
            goal=goal or "",
            from_scratch=(from_scratch or "").lower() in {"on", "1", "true", "yes"},
            skip_existing=True,
            start_policy=policy,
            confirm_seconds=60,
        )
        created = result["created"]
        if not created and not result["skipped"]:
            raise HTTPException(status_code=400, detail="No valid tickers found")
        if created:
            from src.queue_notify import notify_prompt_now

            if policy == "prompt_now":
                notify_prompt_now(created, confirm_seconds=60)
                if queue_store.get_paused():
                    queue_store.set_paused(False)
                _queue_kick()
    except HTTPException as exc:
        return templates.TemplateResponse(
            request,
            "queue.html",
            {
                "ollama_up": ollama_available(),
                "model": settings.ollama_model,
                "pin_required": bool(settings.access_pin),
                "templates": list_templates(),
                "summary": queue_store.summary(),
                "items": [i.to_dict() for i in queue_store.list_items(limit=200)],
                "active_nav": "queue",
                "error": exc.detail,
            },
            status_code=exc.status_code,
        )
    return RedirectResponse(url="/queue", status_code=303)


@app.post("/api/queue/pause")
async def api_queue_pause(body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    queue_store.set_paused(True)
    return {"summary": queue_store.summary()}


@app.post("/api/queue/resume")
async def api_queue_resume(body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    queue_store.set_paused(False)
    _queue_kick()
    return {"summary": queue_store.summary()}


@app.post("/api/queue/cancel-pending")
async def api_queue_cancel_pending(body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    n = queue_store.cancel_all_pending()
    return {"cancelled": n, "summary": queue_store.summary(), "items": [i.to_dict() for i in queue_store.list_items(limit=200)]}


@app.post("/api/queue/clear-finished")
async def api_queue_clear_finished(body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    n = queue_store.clear_finished()
    return {"cleared": n, "summary": queue_store.summary(), "items": [i.to_dict() for i in queue_store.list_items(limit=200)]}


@app.post("/api/queue/{item_id}/cancel")
async def api_queue_cancel_item(item_id: str, body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    ok = queue_store.cancel(item_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Pending item not found")
    return {"cancelled": True, "summary": queue_store.summary()}


@app.post("/api/queue/{item_id}/start-now")
async def api_queue_start_now(item_id: str, body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    item = queue_store.confirm_start_now(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Pending item not found")
    if queue_store.get_paused():
        queue_store.set_paused(False)
    _queue_kick()
    return {"ok": True, "item": item.to_dict(), "summary": queue_store.summary()}


@app.post("/api/queue/{item_id}/defer")
async def api_queue_defer(item_id: str, body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    item = queue_store.defer_to_overnight(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Pending item not found")
    return {"ok": True, "item": item.to_dict(), "summary": queue_store.summary()}


@app.post("/api/queue/start-now")
async def api_queue_start_all_prompts(body: QueueControlRequest | None = None) -> dict[str, Any]:
    """Clear holds on all pending prompt_now items and start the worker."""
    pin = body.pin if body else None
    _check_pin(pin)
    n = 0
    for item in queue_store.list_items(include_done=False):
        if item.status == "pending" and item.start_policy == "prompt_now":
            if queue_store.confirm_start_now(item.id):
                n += 1
    if queue_store.get_paused():
        queue_store.set_paused(False)
    _queue_kick()
    return {"ok": True, "started": n, "summary": queue_store.summary()}


@app.post("/api/queue/defer-pending-prompts")
async def api_queue_defer_prompts(body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    n = 0
    for item in queue_store.list_items(include_done=False):
        if item.status == "pending" and item.hold_until and not item.deferred:
            if queue_store.defer_to_overnight(item.id):
                n += 1
    return {"ok": True, "deferred": n, "summary": queue_store.summary()}


@app.post("/api/queue/start-overnight")
async def api_queue_start_overnight(body: QueueControlRequest | None = None) -> dict[str, Any]:
    """Release deferred/overnight items and run the queue now."""
    pin = body.pin if body else None
    _check_pin(pin)
    n = queue_store.start_overnight()
    if queue_store.get_paused():
        queue_store.set_paused(False)
    _queue_kick()
    return {"ok": True, "released": n, "summary": queue_store.summary()}


@app.delete("/api/queue/ticker/{ticker}")
@app.post("/api/queue/ticker/{ticker}/remove")
async def api_queue_remove_ticker(ticker: str, body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    n = queue_store.remove_ticker(ticker)
    return {
        "ok": True,
        "removed": n,
        "ticker": ticker.upper().strip(),
        "summary": queue_store.summary(),
        "items": [i.to_dict() for i in queue_store.list_items(limit=200)],
    }


@app.post("/api/queue/{item_id}/remove")
async def api_queue_remove_item(item_id: str, body: QueueControlRequest | None = None) -> dict[str, Any]:
    pin = body.pin if body else None
    _check_pin(pin)
    ok = queue_store.remove_item(item_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Pending item not found")
    return {"ok": True, "removed": True, "summary": queue_store.summary()}


@app.post("/queue/pause")
async def queue_pause_form(pin: str | None = Form(None)) -> RedirectResponse:
    _check_pin(pin)
    queue_store.set_paused(True)
    return RedirectResponse(url="/queue", status_code=303)


@app.post("/queue/resume")
async def queue_resume_form(pin: str | None = Form(None)) -> RedirectResponse:
    _check_pin(pin)
    queue_store.set_paused(False)
    _queue_kick()
    return RedirectResponse(url="/queue", status_code=303)


@app.post("/queue/cancel-pending")
async def queue_cancel_pending_form(pin: str | None = Form(None)) -> RedirectResponse:
    _check_pin(pin)
    queue_store.cancel_all_pending()
    return RedirectResponse(url="/queue", status_code=303)


@app.post("/queue/clear-finished")
async def queue_clear_finished_form(pin: str | None = Form(None)) -> RedirectResponse:
    _check_pin(pin)
    queue_store.clear_finished()
    return RedirectResponse(url="/queue", status_code=303)


@app.post("/queue/start-overnight")
async def queue_start_overnight_form(pin: str | None = Form(None)) -> RedirectResponse:
    _check_pin(pin)
    queue_store.start_overnight()
    if queue_store.get_paused():
        queue_store.set_paused(False)
    _queue_kick()
    return RedirectResponse(url="/queue", status_code=303)


@app.post("/queue/remove")
async def queue_remove_form(
    ticker: str = Form(...),
    pin: str | None = Form(None),
) -> RedirectResponse:
    _check_pin(pin)
    queue_store.remove_ticker(ticker)
    return RedirectResponse(url="/queue", status_code=303)


@app.get("/health")
async def health() -> dict[str, Any]:
    from src.sync_store import JOBS_DIR, ensure_sync_dirs

    ensure_sync_dirs()
    sync_files = len(list(JOBS_DIR.glob("*.json")))
    return {
        "ok": True,
        "ollama_up": ollama_available(),
        "model": settings.ollama_model,
        "sync_jobs": sync_files,
        "db_jobs": job_store.count_jobs(),
    }


@app.post("/api/sync/import")
async def sync_import() -> dict[str, Any]:
    """Import git-tracked data/sync jobs into local SQLite."""
    stats = import_all_sync_jobs(job_store)
    return {"ok": True, "stats": stats}


@app.post("/api/sync/export")
async def sync_export() -> dict[str, Any]:
    """Export all completed local jobs into data/sync for git commit/push."""
    n = export_all_completed(job_store)
    return {"ok": True, "exported": n}


@app.post("/api/research")
async def start_research(body: ResearchRequest) -> dict[str, Any]:
    _check_pin(body.pin)
    from src.ticker_status import ticker_status

    status = ticker_status(body.ticker)
    # Reuse in-flight work instead of spawning a duplicate job.
    if status.get("queued_or_active") and status.get("active_jobs"):
        existing = status["active_jobs"][0]
        return {
            "job_id": existing["id"],
            "status": existing["status"],
            "collaborative": False,
            "from_scratch": bool(body.from_scratch),
            "reused": True,
            "message": f"Reused active job ({existing['status']})",
        }
    if status.get("in_overnight_queue"):
        return {
            "job_id": None,
            "status": "queued",
            "collaborative": False,
            "from_scratch": bool(body.from_scratch),
            "reused": True,
            "in_overnight_queue": True,
            "queue_items": status.get("queue_items") or [],
            "message": status.get("skip_reason") or "Already in overnight queue",
        }
    if status.get("has_research") and not body.from_scratch:
        raise HTTPException(
            status_code=409,
            detail={
                "message": status.get("skip_reason") or "Ticker already researched",
                "ticker": status.get("ticker"),
                "latest_completed": status.get("latest_completed"),
                "sync_reports": status.get("sync_reports"),
                "hint": "Pass from_scratch=true to re-run",
            },
        )

    job_id = _start_job_flow(
        body.ticker,
        body.mode,
        body.goal or "",
        body.collaborative,
        template=body.template or "auto",
        from_scratch=bool(body.from_scratch),
    )
    job = job_store.get(job_id)
    assert job
    return {
        "job_id": job.id,
        "status": job.status,
        "collaborative": job.collaborative,
        "from_scratch": bool(body.from_scratch),
        "reused": False,
    }


@app.get("/api/tickers/{ticker}/status")
async def api_ticker_status(ticker: str) -> dict[str, Any]:
    """Whether a ticker is already queued, running, or has research documents."""
    from src.ticker_status import ticker_status

    return ticker_status(ticker)


@app.post("/research", response_class=HTMLResponse)
async def start_research_form(
    request: Request,
    ticker: str = Form(...),
    mode: str = Form("deep"),
    goal: str = Form(""),
    template: str = Form("auto"),
    collaborative: str | None = Form(None),
    from_scratch: str | None = Form(None),
    pin: str = Form(""),
) -> Any:
    try:
        _check_pin(pin or None)
    except HTTPException:
        return templates.TemplateResponse(
            request,
            "index.html",
            {
                "error": "Invalid PIN",
                "ollama_up": ollama_available(),
                "model": settings.ollama_model,
                "pin_required": bool(settings.access_pin),
                "templates": list_templates(),
                "recent_jobs": [],
                "active_nav": "research",
                "prefill_ticker": (ticker or "").strip().upper(),
                "from_scratch": (from_scratch or "").lower() in {"on", "true", "1", "yes"},
            },
            status_code=401,
        )
    # Checkbox omitted from POST when unchecked
    collab = (collaborative or "").lower() in {"on", "true", "1", "yes"}
    scratch = (from_scratch or "").lower() in {"on", "true", "1", "yes"}
    job_id = _start_job_flow(
        ticker, mode, goal, collab, template=template or "auto", from_scratch=scratch
    )
    job = job_store.get(job_id)
    assert job
    if job.collaborative:
        return RedirectResponse(url=f"/jobs/{job.id}/plan", status_code=303)
    return templates.TemplateResponse(
        request,
        "job.html",
        {"job_id": job.id, "ticker": job.ticker, "mode": job.mode},
    )


@app.get("/api/jobs/{job_id}")
async def job_status(job_id: str) -> dict[str, Any]:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    pack_progress = None
    pack_reports = None
    if job.result and job.result.get("kind") == "pack":
        pack_progress = job.result.get("pack_progress")
        pack_reports = [
            {
                "id": r.get("id"),
                "label": r.get("label"),
                "status": r.get("status"),
                "error": r.get("error"),
            }
            for r in (job.result.get("template_reports") or [])
        ]
    return {
        "id": job.id,
        "ticker": job.ticker,
        "mode": job.mode,
        "goal": job.goal,
        "template": job.template,
        "collaborative": job.collaborative,
        "status": job.status,
        "stage": job.stage,
        "message": job.message,
        "created_at": job.created_at,
        "finished_at": job.finished_at,
        "error": job.error,
        "has_plan": bool(job.plan),
        "has_report": bool(job.result and job.result.get("report_markdown")),
        "is_pack": job.template == "all" or (job.result or {}).get("kind") == "pack",
        "pack_progress": pack_progress,
        "pack_reports": pack_reports,
        "thoughts": job.thoughts[-40:],
        "thought_count": len(job.thoughts),
    }


@app.get("/api/jobs/{job_id}/plan")
async def job_plan_json(job_id: str) -> JSONResponse:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if not job.plan:
        raise HTTPException(status_code=409, detail="Plan not ready")
    return JSONResponse(job.plan)


@app.get("/jobs/{job_id}/plan", response_class=HTMLResponse)
async def job_plan_page(request: Request, job_id: str) -> Any:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.status == "completed":
        return RedirectResponse(url=f"/jobs/{job.id}/report", status_code=303)
    if job.status in {"running", "queued"} and not job.collaborative:
        return RedirectResponse(url=f"/jobs/{job.id}", status_code=303)
    return templates.TemplateResponse(
        request,
        "plan.html",
        {
            "job_id": job.id,
            "ticker": job.ticker,
            "mode": job.mode,
            "goal": job.goal,
            "status": job.status,
            "pin_required": bool(settings.access_pin),
        },
    )


@app.post("/api/jobs/{job_id}/approve")
async def approve_plan_api(job_id: str, body: ApproveRequest) -> dict[str, Any]:
    _check_pin(body.pin)
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.status not in {"awaiting_approval", "planning"}:
        if job.status == "running":
            return {"job_id": job.id, "status": job.status}
        raise HTTPException(status_code=409, detail=f"Cannot approve in status {job.status}")
    if not job.plan:
        raise HTTPException(status_code=409, detail="Plan not ready yet")

    plan = ResearchPlan.model_validate(job.plan)
    edits: dict[str, Any] = {}
    if body.goal is not None:
        edits["goal"] = body.goal
    if body.sections is not None:
        edits["sections"] = body.sections
    if body.assumptions is not None:
        edits["assumptions"] = body.assumptions
    if body.multiples is not None:
        edits["multiples"] = body.multiples
    plan = apply_plan_edits(plan, edits or None)
    job_store.update(job_id, plan=plan.to_public_dict(), goal=plan.goal)
    threading.Thread(target=_run_job, args=(job.id,), kwargs={"use_plan_path": True}, daemon=True).start()
    return {"job_id": job.id, "status": "running"}


@app.post("/jobs/{job_id}/approve", response_class=HTMLResponse)
async def approve_plan_form(
    request: Request,
    job_id: str,
    goal: str = Form(""),
    pin: str = Form(""),
) -> Any:
    try:
        _check_pin(pin or None)
    except HTTPException:
        return templates.TemplateResponse(
            request,
            "plan.html",
            {
                "job_id": job_id,
                "ticker": "",
                "mode": "",
                "goal": goal,
                "status": "awaiting_approval",
                "error": "Invalid PIN",
                "pin_required": True,
            },
            status_code=401,
        )

    job = job_store.get(job_id)
    if not job or not job.plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    form = await request.form()
    section_edits: list[dict[str, Any]] = []
    for sec in job.plan.get("sections") or []:
        sid = sec["id"]
        enabled = form.get(f"enabled_{sid}") is not None
        notes = form.get(f"notes_{sid}")
        section_edits.append(
            {
                "id": sid,
                "enabled": enabled,
                "notes": str(notes) if notes is not None else sec.get("notes", ""),
            }
        )

    def _pct_field(name: str) -> float | None:
        raw = form.get(name)
        if raw is None or str(raw).strip() == "":
            return None
        try:
            # UI uses percent points (8 = 8%)
            return float(str(raw)) / 100.0
        except ValueError:
            return None

    years_raw = form.get("explicit_years")
    try:
        years = int(str(years_raw)) if years_raw not in (None, "") else None
    except ValueError:
        years = None

    assumption_edits: dict[str, Any] = {"user_edited": True}
    if years is not None:
        assumption_edits["explicit_years"] = years
    for scen in ("base", "bull", "bear"):
        patch: dict[str, Any] = {}
        for field, form_key in (
            ("revenue_growth", f"{scen}_growth"),
            ("fcf_margin", f"{scen}_fcf_margin"),
            ("wacc", f"{scen}_wacc"),
            ("terminal_growth", f"{scen}_terminal_growth"),
        ):
            val = _pct_field(form_key)
            if val is not None:
                patch[field] = val
        if years is not None:
            patch["explicit_years"] = years
        if patch:
            assumption_edits[scen] = patch

    def _num_field(name: str) -> float | None:
        raw = form.get(name)
        if raw is None or str(raw).strip() == "":
            return None
        try:
            return float(str(raw))
        except ValueError:
            return None

    def _ebitda_field(name: str) -> float | None:
        """UI enters EBITDA in $B; convert to absolute dollars when magnitude looks like billions."""
        v = _num_field(name)
        if v is None:
            return None
        # If user enters 3.3 treat as $3.3B; if already huge keep as-is
        if abs(v) < 1e6:
            return v * 1e9
        return v

    multiples_edits: dict[str, Any] = {"user_edited": True}
    for scen in ("base", "bull", "bear"):
        patch_m: dict[str, Any] = {"label": scen}
        ebitda = _ebitda_field(f"m_{scen}_ebitda")
        multiple = _num_field(f"m_{scen}_multiple")
        if ebitda is not None:
            patch_m["ebitda"] = ebitda
        if multiple is not None:
            patch_m["multiple"] = multiple
        if len(patch_m) > 1:
            multiples_edits[scen] = patch_m

    plan = apply_plan_edits(
        ResearchPlan.model_validate(job.plan),
        {
            "goal": goal,
            "sections": section_edits,
            "assumptions": assumption_edits,
            "multiples": multiples_edits,
        },
    )
    job_store.update(job_id, plan=plan.to_public_dict(), goal=plan.goal)
    threading.Thread(target=_run_job, args=(job.id,), kwargs={"use_plan_path": True}, daemon=True).start()
    return RedirectResponse(url=f"/jobs/{job.id}", status_code=303)


@app.get("/jobs/{job_id}", response_class=HTMLResponse)
async def job_page(request: Request, job_id: str) -> Any:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.status in {"planning", "awaiting_approval"}:
        return RedirectResponse(url=f"/jobs/{job.id}/plan", status_code=303)
    return templates.TemplateResponse(
        request,
        "job.html",
        {"job_id": job.id, "ticker": job.ticker, "mode": job.mode},
    )


@app.get("/api/jobs/{job_id}/report")
async def job_report_json(job_id: str) -> JSONResponse:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.status != "completed" or not job.result:
        raise HTTPException(status_code=409, detail="Report not ready")
    return JSONResponse(job.result)


@app.get("/jobs/{job_id}/report", response_class=HTMLResponse)
async def job_report_page(request: Request, job_id: str) -> Any:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.status != "completed" or not job.result:
        return templates.TemplateResponse(
            request,
            "job.html",
            {"job_id": job.id, "ticker": job.ticker, "mode": job.mode, "waiting": True},
        )

    is_pack = job.result.get("kind") == "pack" or job.template == "all"
    if is_pack:
        pack_reports = []
        for r in job.result.get("template_reports") or []:
            md = r.get("report_markdown") or ""
            charts = r.get("charts") or []
            pack_reports.append(
                {
                    "id": r.get("id"),
                    "label": r.get("label") or r.get("id"),
                    "status": r.get("status") or "completed",
                    "error": r.get("error"),
                    "markdown": md,
                    "charts": charts,
                    "tabs": build_report_tabs(md, charts),
                }
            )
        return templates.TemplateResponse(
            request,
            "report.html",
            {
                "ticker": job.ticker,
                "mode": job.mode,
                "template": "all",
                "goal": job.goal,
                "markdown": job.result.get("report_markdown") or "",
                "charts": [],
                "tabs": [],
                "is_pack": True,
                "pack_reports": pack_reports,
                "job_id": job.id,
                "created_at": job.created_at,
                "active_nav": "dashboard",
            },
        )

    md = job.result.get("report_markdown") or ""
    charts = ((job.result.get("charts") or {}).get("charts") or [])
    tabs = build_report_tabs(md, charts)
    return templates.TemplateResponse(
        request,
        "report.html",
        {
            "ticker": job.ticker,
            "mode": job.mode,
            "template": job.template,
            "goal": job.goal,
            "markdown": md,
            "charts": charts,
            "tabs": tabs,
            "is_pack": False,
            "pack_reports": [],
            "job_id": job.id,
            "created_at": job.created_at,
            "active_nav": "dashboard",
        },
    )


@app.get("/equities/{ticker}", response_class=HTMLResponse)
async def equity_dossier(request: Request, ticker: str) -> Any:
    """Per-equity menu: latest completed report for each template + latest full pack."""
    from src.plan_templates import PACK_TEMPLATE_IDS, TEMPLATES

    ticker = ticker.upper().strip()
    jobs = job_store.list_recent(100, ticker=ticker)
    latest_pack = next(
        (j for j in jobs if j.status == "completed" and (j.template == "all" or (j.result or {}).get("kind") == "pack")),
        None,
    )
    by_template: dict[str, Any] = {}
    for j in jobs:
        if j.status != "completed" or not j.result:
            continue
        if j.template == "all" or (j.result or {}).get("kind") == "pack":
            continue
        tid = j.template or "deep"
        if tid == "auto":
            tid = ((j.result.get("plan") or {}).get("template")) or "deep"
        if tid not in by_template:
            by_template[tid] = _job_card(j)

    menu = []
    if latest_pack:
        menu.append(
            {
                "id": "all",
                "label": "Full pack (all templates)",
                "href": f"/jobs/{latest_pack.id}/report",
                "status": "completed",
                "created_at": latest_pack.created_at,
            }
        )
    for tid in PACK_TEMPLATE_IDS:
        if tid in by_template:
            j = by_template[tid]
            menu.append(
                {
                    "id": tid,
                    "label": (TEMPLATES.get(tid) or {}).get("label") or tid,
                    "href": j["href"],
                    "status": j["status"],
                    "created_at": j["created_at"],
                }
            )
        else:
            menu.append(
                {
                    "id": tid,
                    "label": (TEMPLATES.get(tid) or {}).get("label") or tid,
                    "href": None,
                    "status": "missing",
                    "created_at": None,
                }
            )

    return templates.TemplateResponse(
        request,
        "equity.html",
        {
            "ticker": ticker,
            "menu": menu,
            "latest_pack_id": latest_pack.id if latest_pack else None,
            "jobs": [_job_card(j) for j in jobs[:30]],
            "active_nav": "dashboard",
        },
    )


@app.get("/jobs/{job_id}/report.md", response_class=PlainTextResponse)
async def job_report_md(job_id: str) -> str:
    job = job_store.get(job_id)
    if not job or job.status != "completed" or not job.result:
        raise HTTPException(status_code=404, detail="Report not ready")
    return job.result.get("report_markdown") or ""
