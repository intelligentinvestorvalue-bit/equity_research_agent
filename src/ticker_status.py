"""Per-ticker coverage: active jobs, overnight queue, completed research / docs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.config import OUTPUT_DIR
from src.jobs import Job, job_store
from src.research_queue import queue_store
from src.sync_store import REPORTS_DIR, ensure_sync_dirs

ACTIVE_JOB_STATUSES = frozenset({"queued", "planning", "awaiting_approval", "running"})
ACTIVE_QUEUE_STATUSES = frozenset({"pending", "running"})


def _job_brief(job: Job) -> dict[str, Any]:
    return {
        "id": job.id,
        "status": job.status,
        "template": job.template,
        "mode": job.mode,
        "created_at": job.created_at,
        "finished_at": job.finished_at,
        "href": f"/jobs/{job.id}",
    }


def sync_report_names(ticker: str) -> list[str]:
    ensure_sync_dirs()
    t = ticker.upper().strip()
    if not t or not REPORTS_DIR.exists():
        return []
    return sorted(p.name for p in REPORTS_DIR.glob(f"{t}_*.md"))


def local_output_flags(ticker: str) -> dict[str, bool]:
    t = ticker.upper().strip()
    out = Path(OUTPUT_DIR)
    return {
        "analysis_report": (out / f"{t}_analysis_report.md").exists(),
        "pack_report": (out / f"{t}_pack_analysis_report.md").exists(),
        "financials": (out / f"{t}_financials.json").exists(),
    }


def ticker_status(ticker: str) -> dict[str, Any]:
    """Return whether a ticker is queued, running, or already researched."""
    t = (ticker or "").upper().strip()
    if not t:
        return {
            "ticker": "",
            "queued_or_active": False,
            "in_overnight_queue": False,
            "has_research": False,
            "should_skip": False,
            "skip_reason": None,
        }

    jobs = job_store.list_recent(100, ticker=t)
    active_jobs = [j for j in jobs if j.status in ACTIVE_JOB_STATUSES]
    completed_jobs = [j for j in jobs if j.status == "completed"]

    queue_items = [
        i
        for i in queue_store.list_items(limit=200, include_done=False)
        if i.ticker.upper() == t and i.status in ACTIVE_QUEUE_STATUSES
    ]

    reports = sync_report_names(t)
    local = local_output_flags(t)
    has_docs = bool(reports) or any(local.values())
    has_research = bool(completed_jobs) or has_docs

    skip_reason: str | None = None
    if active_jobs:
        skip_reason = f"active job {active_jobs[0].id} ({active_jobs[0].status})"
    elif queue_items:
        skip_reason = f"already in overnight queue ({queue_items[0].status})"
    elif completed_jobs:
        skip_reason = f"already researched (job {completed_jobs[0].id})"
    elif has_docs:
        skip_reason = "research documents already on disk (sync/output)"

    return {
        "ticker": t,
        "queued_or_active": bool(active_jobs),
        "active_jobs": [_job_brief(j) for j in active_jobs],
        "in_overnight_queue": bool(queue_items),
        "queue_items": [i.to_dict() for i in queue_items],
        "has_research": has_research,
        "completed_count": len(completed_jobs),
        "latest_completed": _job_brief(completed_jobs[0]) if completed_jobs else None,
        "sync_reports": reports,
        "local_output": local,
        "should_skip": skip_reason is not None,
        "skip_reason": skip_reason,
    }
