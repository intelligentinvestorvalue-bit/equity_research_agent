"""Run every research template for one equity into a single pack result."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any, Callable

from src.config import OUTPUT_DIR
from src.plan_runner import run_planned_research
from src.plan_templates import PACK_TEMPLATE_IDS, TEMPLATES, default_goal_for_template
from src.planner import generate_plan

logger = logging.getLogger(__name__)

ProgressCb = Callable[[str, str], None]
ThinkCb = Callable[[str, str], None]


def _noop_progress(stage: str, message: str) -> None:
    logger.info("[%s] %s", stage, message)


def _noop_think(kind: str, message: str) -> None:
    logger.info("think/%s: %s", kind, message)


def _slim_pack_child(result: dict[str, Any], template_id: str) -> dict[str, Any]:
    label = (TEMPLATES.get(template_id) or {}).get("label") or template_id
    return {
        "id": template_id,
        "label": label,
        "status": "completed",
        "report_markdown": result.get("report_markdown") or "",
        "charts": ((result.get("charts") or {}).get("charts") or []),
        "plan": result.get("plan"),
        "critique": result.get("critique"),
        "error": None,
    }


def run_research_pack(
    ticker: str,
    *,
    goal: str = "",
    mode: str = "deep",
    template_ids: list[str] | None = None,
    progress: ProgressCb | None = None,
    think: ThinkCb | None = None,
    on_child_done: Callable[[dict[str, Any]], None] | None = None,
) -> dict[str, Any]:
    """
    Sequentially execute each pack template (no interactive plan approval).
    Returns a pack payload with per-template reports for tabbed UI.
    """
    progress = progress or _noop_progress
    think = think or _noop_think
    ticker = ticker.upper().strip()
    started = datetime.now(timezone.utc).isoformat()
    ids = list(template_ids or PACK_TEMPLATE_IDS)
    reports: list[dict[str, Any]] = []
    total = len(ids)

    think("think", f"Starting full template pack for {ticker} ({total} templates).")
    progress("pack", f"Starting full pack ({total} templates)")

    for i, tid in enumerate(ids, start=1):
        label = (TEMPLATES.get(tid) or {}).get("label") or tid
        progress("pack", f"Running {label} ({i}/{total})")
        think("act", f"Pack step {i}/{total}: template `{tid}`")
        child_goal = default_goal_for_template(tid, goal)
        try:
            plan = generate_plan(ticker, mode=mode if tid != "fast" else "fast", goal=child_goal, template=tid)
            # Ensure charts don't overwrite across templates
            result = run_planned_research(
                plan,
                progress=lambda s, m, _tid=tid: progress(s, f"[{_tid}] {m}"),
                think=think,
            )
            child = _slim_pack_child(result, tid)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Pack template %s failed for %s", tid, ticker)
            think("gap", f"Template `{tid}` failed: {exc}")
            child = {
                "id": tid,
                "label": label,
                "status": "failed",
                "report_markdown": f"## {label}\n\n**Error:** {exc}\n",
                "charts": [],
                "plan": None,
                "critique": None,
                "error": str(exc),
            }
        reports.append(child)
        if on_child_done:
            try:
                on_child_done({"template_reports": list(reports), "current": tid, "index": i, "total": total})
            except Exception:  # noqa: BLE001
                logger.debug("on_child_done failed", exc_info=True)

    # Combined markdown for download
    parts = [
        f"# {ticker} — Full research pack",
        "",
        "> Not investment advice. Local research draft only.",
        "",
        f"**Templates:** {', '.join(ids)}",
        f"**Generated:** {started}",
        "",
    ]
    for r in reports:
        parts.append(f"\n\n---\n\n# Template: {r.get('label')} (`{r.get('id')}`)\n")
        if r.get("status") == "failed":
            parts.append(f"\n**Failed:** {r.get('error')}\n")
        parts.append(r.get("report_markdown") or "")
    combined = "\n".join(parts)
    report_path = OUTPUT_DIR / f"{ticker}_pack_analysis_report.md"
    report_path.write_text(combined, encoding="utf-8")

    progress("done", "Full pack complete")
    think("done", f"Pack finished for {ticker}: {sum(1 for r in reports if r.get('status')=='completed')}/{total} ok.")

    return {
        "kind": "pack",
        "ticker": ticker,
        "mode": mode,
        "template": "all",
        "generated_at": started,
        "goal": goal,
        "template_reports": reports,
        "report_markdown": combined,
        "report_path": str(report_path),
        "charts": {"charts": []},  # charts live per template child
        "pack_progress": {"index": total, "total": total, "current": None},
    }
