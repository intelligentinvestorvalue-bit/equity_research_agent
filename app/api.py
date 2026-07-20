"""FastAPI app: LAN UI + collaborative plan + research job API."""

from __future__ import annotations

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

APP_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(APP_DIR / "templates"))

app = FastAPI(title="Equity Research Agent", version="0.2.0")
app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")
(OUTPUT_DIR / "charts").mkdir(parents=True, exist_ok=True)
app.mount("/charts", StaticFiles(directory=str(OUTPUT_DIR / "charts")), name="charts")


class ResearchRequest(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=12)
    mode: str = Field(default="deep", pattern="^(fast|deep|comprehensive)$")
    goal: str = ""
    template: str = "auto"
    collaborative: bool = True
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
    except Exception as exc:  # noqa: BLE001
        _fail_job(job_id, exc)


def _start_job_flow(
    ticker: str,
    mode: str,
    goal: str,
    collaborative: bool,
    template: str = "auto",
) -> str:
    mode = "fast" if mode == "fast" else "deep"
    from src.plan_templates import resolve_template_id

    tid = resolve_template_id(template, goal=goal, mode=mode)
    collab = collaborative and tid != "fast"
    job = job_store.create(
        ticker, mode, goal=goal, collaborative=collab, template=template or "auto"
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
async def home(request: Request) -> Any:
    recent = [_job_card(j) for j in job_store.list_recent(8)]
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
            by_ticker[j.ticker] = _job_card(j)
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


@app.get("/health")
async def health() -> dict[str, Any]:
    return {
        "ok": True,
        "ollama_up": ollama_available(),
        "model": settings.ollama_model,
    }


@app.post("/api/research")
async def start_research(body: ResearchRequest) -> dict[str, Any]:
    _check_pin(body.pin)
    job_id = _start_job_flow(
        body.ticker, body.mode, body.goal or "", body.collaborative, template=body.template or "auto"
    )
    job = job_store.get(job_id)
    assert job
    return {"job_id": job.id, "status": job.status, "collaborative": job.collaborative}


@app.post("/research", response_class=HTMLResponse)
async def start_research_form(
    request: Request,
    ticker: str = Form(...),
    mode: str = Form("deep"),
    goal: str = Form(""),
    template: str = Form("auto"),
    collaborative: str | None = Form(None),
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
            },
            status_code=401,
        )
    # Checkbox omitted from POST when unchecked
    collab = (collaborative or "").lower() in {"on", "true", "1", "yes"}
    job_id = _start_job_flow(ticker, mode, goal, collab, template=template or "auto")
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
            "job_id": job.id,
            "created_at": job.created_at,
            "active_nav": "dashboard",
        },
    )


@app.get("/jobs/{job_id}/report.md", response_class=PlainTextResponse)
async def job_report_md(job_id: str) -> str:
    job = job_store.get(job_id)
    if not job or job.status != "completed" or not job.result:
        raise HTTPException(status_code=404, detail="Report not ready")
    return job.result.get("report_markdown") or ""
