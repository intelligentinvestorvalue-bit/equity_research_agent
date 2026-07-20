"""FastAPI app: LAN UI + research job API."""

from __future__ import annotations

import threading
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from src.config import settings
from src.jobs import job_store
from src.nlp_engine import ollama_available
from src.orchestrator import run_research

APP_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(APP_DIR / "templates"))

app = FastAPI(title="Equity Research Agent", version="0.1.0")
app.mount("/static", StaticFiles(directory=str(APP_DIR / "static")), name="static")


class ResearchRequest(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=12)
    mode: str = Field(default="deep", pattern="^(fast|deep|comprehensive)$")
    pin: str | None = None


def _check_pin(pin: str | None) -> None:
    if settings.access_pin and (pin or "") != settings.access_pin:
        raise HTTPException(status_code=401, detail="Invalid PIN")


def _run_job(job_id: str) -> None:
    job = job_store.get(job_id)
    if not job:
        return

    def progress(stage: str, message: str) -> None:
        job_store.update(job_id, status="running", stage=stage, message=message)

    try:
        job_store.update(job_id, status="running", stage="starting", message="Job started")
        result = run_research(job.ticker, job.mode, progress=progress)
        # Don't keep huge filing text in memory via result; report markdown is enough
        slim = {
            "ticker": result.get("ticker"),
            "mode": result.get("mode"),
            "generated_at": result.get("generated_at"),
            "financials_path": result.get("financials_path"),
            "report_path": result.get("report_path"),
            "report_markdown": result.get("report_markdown"),
            "sections": result.get("sections"),
            "nlp": result.get("nlp"),
            "quant_summary": {
                "ratios": ((result.get("quant") or {}).get("fundamentals") or {}).get("ratios"),
                "options_candidates": len((((result.get("quant") or {}).get("options") or {}).get("candidates") or [])),
            },
        }
        from datetime import datetime, timezone

        job_store.update(
            job_id,
            status="completed",
            stage="done",
            message="Complete",
            result=slim,
            finished_at=datetime.now(timezone.utc).isoformat(),
        )
    except Exception as exc:  # noqa: BLE001
        from datetime import datetime, timezone

        job_store.update(
            job_id,
            status="failed",
            stage="error",
            message=str(exc),
            error=str(exc),
            finished_at=datetime.now(timezone.utc).isoformat(),
        )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> Any:
    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "ollama_up": ollama_available(),
            "model": settings.ollama_model,
            "pin_required": bool(settings.access_pin),
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
    job = job_store.create(body.ticker, body.mode)
    threading.Thread(target=_run_job, args=(job.id,), daemon=True).start()
    return {"job_id": job.id, "status": job.status}


@app.post("/research", response_class=HTMLResponse)
async def start_research_form(
    request: Request,
    ticker: str = Form(...),
    mode: str = Form("deep"),
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
            },
            status_code=401,
        )
    job = job_store.create(ticker, mode)
    threading.Thread(target=_run_job, args=(job.id,), daemon=True).start()
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
        "status": job.status,
        "stage": job.stage,
        "message": job.message,
        "created_at": job.created_at,
        "finished_at": job.finished_at,
        "error": job.error,
        "has_report": bool(job.result and job.result.get("report_markdown")),
    }


@app.get("/jobs/{job_id}", response_class=HTMLResponse)
async def job_page(request: Request, job_id: str) -> Any:
    job = job_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
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
    return templates.TemplateResponse(
        request,
        "report.html",
        {
            "ticker": job.ticker,
            "mode": job.mode,
            "markdown": job.result.get("report_markdown") or "",
            "job_id": job.id,
        },
    )


@app.get("/jobs/{job_id}/report.md", response_class=PlainTextResponse)
async def job_report_md(job_id: str) -> str:
    job = job_store.get(job_id)
    if not job or job.status != "completed" or not job.result:
        raise HTTPException(status_code=404, detail="Report not ready")
    return job.result.get("report_markdown") or ""
