"""Git-friendly sync of research jobs between Cursor Cloud and local.

Completed jobs are written under data/sync/ (tracked by git). On startup,
those files are imported into the local SQLite DB so both environments share
the same reports after git pull / push.
"""

from __future__ import annotations

import json
import logging
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.config import OUTPUT_DIR, ROOT_DIR
from src.jobs import Job, JobStore

logger = logging.getLogger(__name__)

SYNC_DIR = ROOT_DIR / "data" / "sync"
JOBS_DIR = SYNC_DIR / "jobs"
CHARTS_DIR = SYNC_DIR / "charts"
REPORTS_DIR = SYNC_DIR / "reports"


def ensure_sync_dirs() -> None:
    JOBS_DIR.mkdir(parents=True, exist_ok=True)
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def _iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _chart_paths_from_result(result: dict[str, Any] | None) -> list[Path]:
    """Collect local chart file paths referenced by a job result."""
    if not result:
        return []
    paths: list[Path] = []
    charts_root = OUTPUT_DIR / "charts"

    def add_list(items: list[Any] | None) -> None:
        for c in items or []:
            if not isinstance(c, dict):
                continue
            name = c.get("filename") or (Path(c["path"]).name if c.get("path") else None)
            if not name:
                url = c.get("url") or ""
                if url.startswith("/charts/"):
                    name = url.split("/charts/", 1)[-1]
            if name:
                paths.append(charts_root / name)

    add_list(((result.get("charts") or {}).get("charts")) if isinstance(result.get("charts"), dict) else result.get("charts"))
    for tr in result.get("template_reports") or []:
        if isinstance(tr, dict):
            add_list(tr.get("charts"))
    # de-dupe
    seen: set[str] = set()
    out: list[Path] = []
    for p in paths:
        key = str(p.resolve()) if p.exists() else str(p)
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out


def _copy_charts_for_export(result: dict[str, Any] | None) -> list[str]:
    ensure_sync_dirs()
    copied: list[str] = []
    for src in _chart_paths_from_result(result):
        if not src.exists():
            continue
        dest = CHARTS_DIR / src.name
        try:
            shutil.copy2(src, dest)
            copied.append(src.name)
        except OSError as exc:
            logger.warning("Could not sync chart %s: %s", src, exc)
    return copied


def _restore_charts_from_sync(chart_names: list[str] | None) -> int:
    ensure_sync_dirs()
    (OUTPUT_DIR / "charts").mkdir(parents=True, exist_ok=True)
    n = 0
    for name in chart_names or []:
        src = CHARTS_DIR / name
        if not src.exists():
            continue
        dest = OUTPUT_DIR / "charts" / name
        try:
            shutil.copy2(src, dest)
            n += 1
        except OSError as exc:
            logger.warning("Could not restore chart %s: %s", name, exc)
    return n


def job_to_sync_payload(job: Job) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "exported_at": _iso_now(),
        "job": {
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
            "plan": job.plan,
            "result": job.result,
            "error": job.error,
            "thoughts": job.thoughts[-80:] if job.thoughts else [],
        },
    }


def export_job(job: Job) -> Path | None:
    """Write a completed/failed job into data/sync for git sharing."""
    if job.status not in {"completed", "failed"}:
        return None
    ensure_sync_dirs()
    payload = job_to_sync_payload(job)
    charts = _copy_charts_for_export(job.result)
    payload["charts"] = charts

    path = JOBS_DIR / f"{job.id}.json"
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")

    md = (job.result or {}).get("report_markdown") or ""
    if md:
        safe_ticker = "".join(c for c in (job.ticker or "UNK") if c.isalnum() or c in "-_")[:12]
        report_path = REPORTS_DIR / f"{safe_ticker}_{job.id[:8]}_{job.template or 'job'}.md"
        report_path.write_text(md, encoding="utf-8")
        payload["report_file"] = report_path.name
        path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")

    logger.info("Synced job %s (%s %s) → %s", job.id[:8], job.ticker, job.template, path)
    return path


def export_job_id(store: JobStore, job_id: str) -> Path | None:
    job = store.get(job_id)
    if not job:
        return None
    return export_job(job)


def _should_replace(existing: Job, incoming: Job) -> bool:
    """Prefer completed packs; then newer finished_at; then newer created_at."""
    if existing.status != "completed" and incoming.status == "completed":
        return True
    if existing.status == "completed" and incoming.status != "completed":
        return False
    ef = existing.finished_at or existing.created_at or ""
    inf = incoming.finished_at or incoming.created_at or ""
    if inf > ef:
        return True
    if inf < ef:
        return False
    # Same timestamp: replace if incoming has richer report
    ex_md = len(((existing.result or {}).get("report_markdown")) or "")
    in_md = len(((incoming.result or {}).get("report_markdown")) or "")
    return in_md > ex_md


def payload_to_job(payload: dict[str, Any]) -> Job | None:
    raw = payload.get("job") if isinstance(payload.get("job"), dict) else payload
    if not isinstance(raw, dict) or not raw.get("id"):
        return None
    thoughts = raw.get("thoughts") or []
    if not isinstance(thoughts, list):
        thoughts = []
    return Job(
        id=str(raw["id"]),
        ticker=str(raw.get("ticker") or "").upper(),
        mode=str(raw.get("mode") or "deep"),
        goal=str(raw.get("goal") or ""),
        template=str(raw.get("template") or "auto"),
        collaborative=bool(raw.get("collaborative", True)),
        status=str(raw.get("status") or "completed"),
        stage=str(raw.get("stage") or "done"),
        message=str(raw.get("message") or ""),
        created_at=str(raw.get("created_at") or _iso_now()),
        finished_at=raw.get("finished_at"),
        plan=raw.get("plan") if isinstance(raw.get("plan"), dict) else None,
        result=raw.get("result") if isinstance(raw.get("result"), dict) else None,
        error=raw.get("error"),
        thoughts=thoughts,
    )


def import_sync_file(store: JobStore, path: Path) -> str:
    """Import one sync JSON. Returns inserted|updated|skipped|error."""
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        logger.warning("Bad sync file %s: %s", path, exc)
        return "error"

    job = payload_to_job(payload)
    if not job or not job.ticker:
        return "error"

    _restore_charts_from_sync(payload.get("charts") if isinstance(payload, dict) else None)

    existing = store.get(job.id)
    if existing is None:
        store.upsert(job)
        return "inserted"
    if not _should_replace(existing, job):
        return "skipped"
    store.upsert(job)
    return "updated"


def import_all_sync_jobs(store: JobStore) -> dict[str, int]:
    """Load every data/sync/jobs/*.json into SQLite."""
    ensure_sync_dirs()
    stats = {"inserted": 0, "updated": 0, "skipped": 0, "error": 0}
    files = sorted(JOBS_DIR.glob("*.json"))
    for path in files:
        action = import_sync_file(store, path)
        stats[action] = stats.get(action, 0) + 1
    if files:
        logger.info(
            "Sync import: %s files → inserted=%s updated=%s skipped=%s errors=%s",
            len(files),
            stats["inserted"],
            stats["updated"],
            stats["skipped"],
            stats["error"],
        )
    return stats


def export_all_completed(store: JobStore) -> int:
    """Re-export all completed/failed jobs (e.g. after local-only runs)."""
    n = 0
    for job in store.list_recent(200):
        if job.status in {"completed", "failed"}:
            if export_job(job):
                n += 1
    return n
