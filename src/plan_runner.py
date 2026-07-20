"""Execute an approved ResearchPlan using registered tools (Phase 2)."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any, Callable

from src.config import OUTPUT_DIR
from src.evidence import EvidenceStore
from src.plan_schema import ResearchPlan
from src.quant_engine import format_fundamentals_markdown
from src.tools import TOOL_REGISTRY, ToolContext

logger = logging.getLogger(__name__)

ProgressCb = Callable[[str, str], None]


def _noop(stage: str, message: str) -> None:
    logger.info("[%s] %s", stage, message)


def _format_report(plan: ResearchPlan, ctx: ToolContext) -> str:
    fund = ctx.fundamentals or {}
    opts = ctx.options or {}
    ev_by_title = {it.title: it.id for it in ctx.evidence.items()}

    def cite(*titles: str) -> str:
        ids = [ev_by_title[t] for t in titles if t in ev_by_title]
        return f" [{', '.join(ids)}]" if ids else ""

    lines = [
        f"# {plan.ticker} — Planned Research Report",
        "",
        "> Not investment advice. Local research draft only.",
        "",
        f"**Goal:** {plan.goal}",
        f"**Mode:** {plan.mode}",
        f"**Planner:** {plan.planner_mode}",
        "",
        "## Plan executed",
        "",
    ]
    for sec in plan.enabled_sections():
        lines.append(f"- **{sec.title}** (`{sec.id}`): {', '.join(sec.tools)}")
        if sec.notes:
            lines.append(f"  - {sec.notes}")
    lines.append("")

    if ctx.fundamentals is not None:
        fund_md = format_fundamentals_markdown(
            fund,
            heading="## Fundamentals" + cite(f"{plan.ticker} fundamentals"),
        )
        lines.append(fund_md.rstrip())
        lines.append("")

    if ctx.options is not None:
        lines += [
            "## Put opportunities (heuristic)" + cite(f"{plan.ticker} put screen"),
            f"- Expiration: {opts.get('expiration')} (DTE {opts.get('dte')})",
            f"- Candidates: {len(opts.get('candidates') or [])}",
            "",
        ]
        for c in (opts.get("candidates") or [])[:10]:
            lines.append(
                f"- Strike {c.get('strike')}: premium {c.get('premium_mid')}, "
                f"ann. return {c.get('annualized_return')}, IV {c.get('iv')}"
            )
        if opts.get("note"):
            lines += ["", f"_Note: {opts.get('note')}_"]
        if opts.get("error"):
            lines += ["", f"**Options error:** {opts['error']}"]
        lines.append("")

    if ctx.sections is not None:
        meta = ctx.sections.get("meta") or {}
        lines += [
            "## SEC filing" + cite(f"{plan.ticker} 10-K"),
            f"- Extraction OK: {ctx.sections.get('extraction_ok')}",
            f"- Item 1A chars: {ctx.sections.get('item_1a_chars')}",
            f"- Item 7 chars: {ctx.sections.get('item_7_chars')}",
            f"- Meta: {meta}",
            "",
        ]

    if ctx.nlp_1a or ctx.nlp_7:
        lines += ["## Qualitative analysis (local LLM)", ""]
        if ctx.nlp_1a:
            lines.append(ctx.nlp_1a.get("markdown") or "")
            lines.append("")
        if ctx.nlp_7:
            lines.append(ctx.nlp_7.get("markdown") or "")
            lines.append("")

    if ctx.errors:
        lines += ["## Run warnings", ""]
        for err in ctx.errors:
            lines.append(f"- {err}")
        lines.append("")

    lines.append(ctx.evidence.citations_markdown())
    return "\n".join(lines)


def run_planned_research(
    plan: ResearchPlan,
    progress: ProgressCb | None = None,
) -> dict[str, Any]:
    progress = progress or _noop
    ticker = plan.ticker.upper().strip()
    started = datetime.now(timezone.utc).isoformat()
    evidence = EvidenceStore()
    ctx = ToolContext(ticker=ticker, evidence=evidence, progress=progress)

    # Deduplicate tool calls while preserving first-seen order across enabled sections
    tools_ordered: list[str] = []
    seen: set[str] = set()
    for sec in plan.enabled_sections():
        progress("plan", f"Section: {sec.title}")
        for name in sec.tools:
            if name not in seen:
                seen.add(name)
                tools_ordered.append(name)

    for name in tools_ordered:
        fn = TOOL_REGISTRY.get(name)
        if not fn:
            ctx.errors.append(f"unknown tool: {name}")
            continue
        try:
            fn(ctx)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Tool %s failed", name)
            ctx.errors.append(f"{name}: {exc}")

    quant = {
        "fundamentals": ctx.fundamentals,
        "options": ctx.options,
    }
    financials_path = OUTPUT_DIR / f"{ticker}_financials.json"
    financials_path.write_text(
        json.dumps(
            {
                "ticker": ticker,
                "mode": plan.mode,
                "generated_at": started,
                "plan": plan.to_public_dict(),
                "quant": quant,
            },
            indent=2,
            default=str,
        ),
        encoding="utf-8",
    )

    md = _format_report(plan, ctx)
    report_path = OUTPUT_DIR / f"{ticker}_analysis_report.md"
    report_path.write_text(md, encoding="utf-8")

    sections_meta = None
    if ctx.sections is not None:
        sections_meta = {
            "meta": ctx.sections.get("meta"),
            "item_1a_chars": ctx.sections.get("item_1a_chars"),
            "item_7_chars": ctx.sections.get("item_7_chars"),
            "extraction_ok": ctx.sections.get("extraction_ok"),
            "error": ctx.sections.get("error"),
        }

    nlp_out = None
    if ctx.nlp_1a or ctx.nlp_7:
        nlp_out = {
            "item_1a_mode": (ctx.nlp_1a or {}).get("mode"),
            "item_7_mode": (ctx.nlp_7 or {}).get("mode"),
            "ollama_up": nlp_engine_flag(),
        }

    progress("done", "Planned research complete")
    return {
        "ticker": ticker,
        "mode": plan.mode,
        "generated_at": started,
        "plan": plan.to_public_dict(),
        "quant": quant,
        "financials_path": str(financials_path),
        "sections": sections_meta,
        "nlp": nlp_out,
        "evidence": evidence.to_list(),
        "report_path": str(report_path),
        "report_markdown": md,
    }


def nlp_engine_flag() -> bool:
    from src.nlp_engine import ollama_available

    return ollama_available()
