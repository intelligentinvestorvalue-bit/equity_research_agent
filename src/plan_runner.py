"""Execute an approved ResearchPlan using registered tools (Phase 2)."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any, Callable

from src.chart_engine import charts_markdown, generate_research_charts
from src.config import OUTPUT_DIR
from src.critique import critique_report
from src.evidence import EvidenceStore
from src.plan_schema import ResearchPlan
from src.quant_engine import format_fundamentals_markdown
from src.research_loop import run_research_loop
from src.thinking import ThinkCb, _noop_think
from src.tools import TOOL_REGISTRY, ToolContext
from src.valuation import format_valuation_markdown
from src.web_engine import format_web_markdown

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
        f"**Template:** {getattr(plan, 'template', '')}",
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

    # Charts inserted after fundamentals / before valuation when available
    charts_md = getattr(ctx, "_charts_markdown", "") or ""
    if charts_md:
        lines.append(charts_md.rstrip())
        lines.append("")

    if ctx.valuation is not None:
        val_md = format_valuation_markdown(ctx.valuation)
        # Attach citation if present
        cite_bit = cite(f"{plan.ticker} DCF valuation")
        if cite_bit:
            val_md = val_md.replace(
                "## DCF valuation (base / bull / bear)",
                "## DCF valuation (base / bull / bear)" + cite_bit,
                1,
            )
        lines.append(val_md.rstrip())
        lines.append("")

    if ctx.multiples is not None:
        from src.multiples import format_multiples_markdown

        mult_md = ctx.multiples.get("report_markdown") or format_multiples_markdown(ctx.multiples)
        cite_bit = cite(f"{plan.ticker} EV/EBITDA valuation")
        if cite_bit:
            mult_md = mult_md.replace(
                "## Valuation — EV/EBITDA scenarios",
                "## Valuation — EV/EBITDA scenarios" + cite_bit,
                1,
            )
        lines.append(mult_md.rstrip())
        lines.append("")

    if ctx.peers is not None:
        from src.peers import format_peer_comps_markdown

        peer_md = ctx.peers.get("report_markdown") or format_peer_comps_markdown(ctx.peers)
        lines.append(peer_md.rstrip())
        lines.append("")

    if ctx.earnings is not None:
        from src.quant_engine import format_earnings_markdown

        earn_md = ctx.earnings.get("report_markdown") or format_earnings_markdown(ctx.earnings)
        lines.append(earn_md.rstrip())
        lines.append("")

    if ctx.filings_extra is not None:
        from src.sec_engine import format_recent_filings_markdown

        fil_md = ctx.filings_extra.get("report_markdown") or format_recent_filings_markdown(
            ctx.filings_extra
        )
        lines.append(fil_md.rstrip())
        lines.append("")

    if ctx.drivers is not None:
        from src.drivers import format_drivers_markdown

        drv_md = ctx.drivers.get("report_markdown") or format_drivers_markdown(ctx.drivers)
        lines.append(drv_md.rstrip())
        lines.append("")

    if ctx.memo is not None and ctx.memo.get("markdown"):
        lines.append(ctx.memo["markdown"].rstrip())
        lines.append("")

    if ctx.web is not None:
        # Prefer per-section reports when multiple web passes ran
        if ctx.web_reports:
            for wr in ctx.web_reports:
                sid = wr.get("section_id") or "web"
                lines.append(f"## Web research — {sid}")
                lines.append("")
                body = wr.get("report_markdown") or format_web_markdown(
                    wr, wr.get("summary_markdown") or ""
                )
                # Drop duplicate top heading from format_web_markdown
                body = body.replace("## Web / news research\n\n", "", 1)
                lines.append(body.rstrip())
                lines.append("")
        else:
            web_md = ctx.web.get("report_markdown") or format_web_markdown(
                ctx.web, (ctx.web_summary or {}).get("markdown") or ""
            )
            lines.append(web_md.rstrip())
            lines.append("")

    if ctx.options is not None:
        def _pct(v: Any) -> str:
            try:
                return f"{float(v) * 100:.1f}%" if v is not None else "—"
            except (TypeError, ValueError):
                return "—"

        lines += [
            "## Put opportunities (heuristic)" + cite(f"{plan.ticker} put screen"),
            f"- Expiration: {opts.get('expiration')} (DTE {opts.get('dte')})",
            f"- Candidates: {len(opts.get('candidates') or [])}",
            f"- ATM IV (est.): {_pct(opts.get('current_iv'))}",
            f"- IV rank: {_pct(opts.get('iv_rank'))} ({opts.get('iv_samples') or 0} local samples)",
            f"- HV rank (20d realized): {_pct(opts.get('hv_rank'))}",
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

    loop = getattr(ctx, "loop_result", None) or {}
    steps = loop.get("steps") or []
    if steps:
        lines += ["## Research loop (think → act)", ""]
        for i, step in enumerate(steps, start=1):
            lines.append(f"{i}. _{step.get('mode', 'heuristic')}_ — {step.get('thought', '')}")
            for a in step.get("actions") or []:
                lines.append(
                    f"   - act `{a.get('tool')}`: {a.get('reason') or ''} "
                    f"{('· ' + ', '.join(a.get('queries') or [])) if a.get('queries') else ''}"
                )
        lines.append("")

    lines.append(ctx.evidence.citations_markdown())
    return "\n".join(lines)


def run_planned_research(
    plan: ResearchPlan,
    progress: ProgressCb | None = None,
    think: ThinkCb | None = None,
) -> dict[str, Any]:
    progress = progress or _noop
    think = think or _noop_think
    ticker = plan.ticker.upper().strip()
    started = datetime.now(timezone.utc).isoformat()
    evidence = EvidenceStore()
    plan_queries: list[str] = []
    for sec in plan.enabled_sections():
        plan_queries.extend(sec.queries or [])
    ctx = ToolContext(
        ticker=ticker,
        evidence=evidence,
        progress=progress,
        plan_assumptions=plan.assumptions.model_dump() if plan.assumptions else None,
        plan_multiples=plan.multiples.model_dump() if getattr(plan, "multiples", None) else None,
        plan_goal=plan.goal or "",
        plan_queries=plan_queries,
    )

    think("think", f"Executing approved plan for {ticker} ({plan.template}).")

    # Run tools section-by-section so search_web can use per-section queries
    seen: set[str] = set()
    for sec in plan.enabled_sections():
        progress("plan", f"Section: {sec.title}")
        think("act", f"Running section `{sec.id}`: {sec.title}")
        ctx.active_section_id = sec.id
        ctx.active_section_queries = list(sec.queries or [])
        for name in sec.tools:
            # Dedupe non-web tools; allow search_web multiple times
            if name != "search_web" and name in seen:
                continue
            if name != "search_web":
                seen.add(name)
            fn = TOOL_REGISTRY.get(name)
            if not fn:
                ctx.errors.append(f"unknown tool: {name}")
                continue
            try:
                fn(ctx)
            except Exception as exc:  # noqa: BLE001
                logger.exception("Tool %s failed", name)
                ctx.errors.append(f"{name}: {exc}")
                think("gap", f"Tool `{name}` failed: {exc}")
    ctx.active_section_id = None
    ctx.active_section_queries = []

    # Iterative gap-fill (Gemini-style think → act)
    loop_result = run_research_loop(plan, ctx, progress=progress, think=think)
    ctx.loop_result = loop_result  # type: ignore[attr-defined]

    progress("charts", "Rendering charts")
    think("act", "Building revenue/FCF, valuation, and peer charts.")
    charts_meta = generate_research_charts(
        ticker,
        ctx.fundamentals,
        ctx.valuation,
        multiples=ctx.multiples,
        peers=ctx.peers,
    )
    ctx._charts_markdown = charts_markdown(charts_meta)  # type: ignore[attr-defined]
    think("think", f"Generated {len(charts_meta.get('charts') or [])} chart(s).")

    quant = {
        "fundamentals": ctx.fundamentals,
        "options": ctx.options,
        "earnings": ctx.earnings,
        "peers": {
            "peers": (ctx.peers or {}).get("peers"),
            "rows": (ctx.peers or {}).get("rows"),
            "notes": (ctx.peers or {}).get("notes"),
        }
        if ctx.peers
        else None,
        "drivers": ctx.drivers,
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
                "valuation": ctx.valuation,
                "multiples": ctx.multiples,
                "memo": {"mode": (ctx.memo or {}).get("mode")} if ctx.memo else None,
                "loop": loop_result,
                "charts": charts_meta,
                "web": {
                    "queries": (ctx.web or {}).get("queries"),
                    "hit_count": (ctx.web or {}).get("hit_count"),
                    "fetched_ok": (ctx.web or {}).get("fetched_ok"),
                    "hits": (ctx.web or {}).get("hits"),
                }
                if ctx.web
                else None,
            },
            indent=2,
            default=str,
        ),
        encoding="utf-8",
    )

    md = _format_report(plan, ctx)
    progress("critique", "Self-critique pass")
    think("think", "Reviewing draft for unsupported claims and fragile assumptions.")
    critique = critique_report(md, plan, ctx)
    md = critique.get("final_markdown") or md
    think(
        "done" if not critique.get("issues") else "gap",
        f"Self-critique ({critique.get('mode')}): {critique.get('issue_count', 0)} issue(s) flagged.",
    )
    report_path = OUTPUT_DIR / f"{ticker}_analysis_report.md"
    report_path.write_text(md, encoding="utf-8")

    # Persist critique alongside financials payload
    try:
        payload = json.loads(financials_path.read_text(encoding="utf-8"))
        payload["critique"] = {
            "mode": critique.get("mode"),
            "issues": critique.get("issues"),
            "issue_count": critique.get("issue_count"),
        }
        financials_path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    except Exception:  # noqa: BLE001
        logger.debug("Could not append critique to financials JSON", exc_info=True)

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
    think("done", "Research run finished.")
    return {
        "ticker": ticker,
        "mode": plan.mode,
        "generated_at": started,
        "plan": plan.to_public_dict(),
        "quant": quant,
        "valuation": ctx.valuation,
        "multiples": {
            "ok": (ctx.multiples or {}).get("ok"),
            "scenarios": (ctx.multiples or {}).get("scenarios"),
        }
        if ctx.multiples
        else None,
        "loop": loop_result,
        "critique": {
            "mode": critique.get("mode"),
            "issues": critique.get("issues"),
            "issue_count": critique.get("issue_count"),
        },
        "charts": charts_meta,
        "web": {
            "queries": (ctx.web or {}).get("queries"),
            "hit_count": (ctx.web or {}).get("hit_count"),
            "fetched_ok": (ctx.web or {}).get("fetched_ok"),
            "summary_mode": (ctx.web_summary or {}).get("mode"),
        }
        if ctx.web
        else None,
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
