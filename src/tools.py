"""Tool adapters for plan-driven research (Phase 2)."""

from __future__ import annotations

import logging
from typing import Any, Callable

from src import nlp_engine, quant_engine, sec_engine
from src.evidence import EvidenceStore

logger = logging.getLogger(__name__)

ProgressCb = Callable[[str, str], None]


class ToolContext:
    """Shared state across tool calls within one planned run."""

    def __init__(
        self,
        ticker: str,
        evidence: EvidenceStore,
        progress: ProgressCb,
        plan_assumptions: dict[str, Any] | None = None,
        plan_goal: str = "",
        plan_queries: list[str] | None = None,
    ) -> None:
        self.ticker = ticker.upper()
        self.evidence = evidence
        self.progress = progress
        self.plan_assumptions = plan_assumptions
        self.plan_goal = plan_goal or ""
        self.plan_queries = list(plan_queries or [])
        self.fundamentals: dict[str, Any] | None = None
        self.options: dict[str, Any] | None = None
        self.sections: dict[str, Any] | None = None
        self.nlp_1a: dict[str, Any] | None = None
        self.nlp_7: dict[str, Any] | None = None
        self.valuation: dict[str, Any] | None = None
        self.web: dict[str, Any] | None = None
        self.web_summary: dict[str, Any] | None = None
        self.web_reports: list[dict[str, Any]] = []
        self.active_section_id: str | None = None
        self.active_section_queries: list[str] = []
        self.errors: list[str] = []


def tool_get_fundamentals(ctx: ToolContext) -> dict[str, Any]:
    ctx.progress("quant", f"Fetching fundamentals for {ctx.ticker}")
    try:
        fund = quant_engine.fetch_fundamentals(ctx.ticker)
    except Exception as exc:  # noqa: BLE001
        logger.exception("fundamentals failed")
        fund = {"ticker": ctx.ticker, "error": str(exc)}
        ctx.errors.append(f"fundamentals: {exc}")
    ctx.fundamentals = fund
    ratios = fund.get("ratios") or {}
    growth = fund.get("growth") or {}
    summary = (
        f"{fund.get('company_name') or ctx.ticker}: price={fund.get('price')}, "
        f"rev={fund.get('revenue')}, fcf={fund.get('free_cash_flow')}, "
        f"shares={fund.get('shares_outstanding')}, "
        f"rev_cagr={growth.get('revenue_cagr')}, "
        f"ROIC={ratios.get('roic')}, FCF yield={ratios.get('fcf_yield')}"
    )
    if fund.get("error"):
        summary = f"Error: {fund['error']}"
    ctx.evidence.add(
        source="yfinance",
        title=f"{ctx.ticker} fundamentals",
        summary=summary,
        meta={
            "ratios": ratios,
            "growth": growth,
            "revenue": fund.get("revenue"),
            "free_cash_flow": fund.get("free_cash_flow"),
            "shares_outstanding": fund.get("shares_outstanding"),
        },
    )
    return fund


def tool_screen_puts(ctx: ToolContext) -> dict[str, Any]:
    ctx.progress("quant", f"Screening puts for {ctx.ticker}")
    try:
        opts = quant_engine.fetch_put_opportunities(ctx.ticker)
    except Exception as exc:  # noqa: BLE001
        logger.exception("options failed")
        opts = {"ticker": ctx.ticker, "error": str(exc), "candidates": []}
        ctx.errors.append(f"options: {exc}")
    ctx.options = opts
    n = len(opts.get("candidates") or [])
    summary = (
        f"Expiration {opts.get('expiration')} (DTE {opts.get('dte')}): {n} candidates; "
        f"IV={opts.get('current_iv')}, IV rank={opts.get('iv_rank')}, HV rank={opts.get('hv_rank')}"
    )
    if opts.get("error"):
        summary = f"Error: {opts['error']}"
    elif opts.get("note"):
        summary = f"{summary}. {opts['note']}"
    ctx.evidence.add(
        source="yfinance_options",
        title=f"{ctx.ticker} put screen",
        summary=summary,
        meta={
            "candidate_count": n,
            "expiration": opts.get("expiration"),
            "current_iv": opts.get("current_iv"),
            "iv_rank": opts.get("iv_rank"),
            "hv_rank": opts.get("hv_rank"),
        },
    )
    return opts


def tool_fetch_10k(ctx: ToolContext) -> dict[str, Any]:
    ctx.progress("sec", f"Fetching 10-K for {ctx.ticker}")
    try:
        sections = sec_engine.fetch_10k_sections(ctx.ticker)
        sec_engine.save_section_blocks(sections)
    except Exception as exc:  # noqa: BLE001
        logger.exception("SEC failed")
        sections = {"ticker": ctx.ticker, "item_1a": None, "item_7": None, "error": str(exc), "extraction_ok": False}
        ctx.errors.append(f"sec: {exc}")
    ctx.sections = sections
    meta = sections.get("meta") or {}
    summary = (
        f"Item 1A chars={sections.get('item_1a_chars', 0)}, "
        f"Item 7 chars={sections.get('item_7_chars', 0)}, "
        f"ok={sections.get('extraction_ok')}, source={meta.get('source')}"
    )
    if sections.get("error"):
        summary = f"Error: {sections['error']}"
    url = meta.get("url")
    ctx.evidence.add(
        source="sec",
        title=f"{ctx.ticker} 10-K",
        summary=summary,
        url=url if isinstance(url, str) else None,
        meta={"filing_date": meta.get("filing_date"), "accession": meta.get("accession_number")},
    )
    return sections


def tool_summarize_item_1a(ctx: ToolContext) -> dict[str, Any]:
    if ctx.sections is None:
        tool_fetch_10k(ctx)
    ctx.progress("nlp", "Summarizing Item 1A")
    text = (ctx.sections or {}).get("item_1a")
    result = nlp_engine.summarize_section(text, "Item 1A — Risk Factors")
    ctx.nlp_1a = result
    ctx.evidence.add(
        source="nlp",
        title="Item 1A summary",
        summary=(result.get("markdown") or "")[:500],
        meta={"mode": result.get("mode")},
    )
    return result


def tool_summarize_item_7(ctx: ToolContext) -> dict[str, Any]:
    if ctx.sections is None:
        tool_fetch_10k(ctx)
    ctx.progress("nlp", "Summarizing Item 7")
    text = (ctx.sections or {}).get("item_7")
    result = nlp_engine.summarize_section(text, "Item 7 — MD&A")
    ctx.nlp_7 = result
    ctx.evidence.add(
        source="nlp",
        title="Item 7 summary",
        summary=(result.get("markdown") or "")[:500],
        meta={"mode": result.get("mode")},
    )
    return result


def tool_run_dcf(ctx: ToolContext) -> dict[str, Any]:
    from src.valuation import merge_assumptions, run_dcf

    if ctx.fundamentals is None:
        tool_get_fundamentals(ctx)
    ctx.progress("valuation", f"Running base/bull/bear DCF for {ctx.ticker}")
    fund = ctx.fundamentals or {}
    assumptions = merge_assumptions(fund, ctx.plan_assumptions)
    result = run_dcf(fund, assumptions)
    ctx.valuation = result
    if not result.get("ok"):
        ctx.errors.append("dcf: " + "; ".join(result.get("errors") or ["failed"]))
        summary = "DCF failed: " + "; ".join(result.get("errors") or [])
    else:
        base = (result.get("scenarios") or {}).get("base") or {}
        summary = (
            f"Base share price={base.get('share_price')}, "
            f"bull={(result.get('scenarios') or {}).get('bull', {}).get('share_price')}, "
            f"bear={(result.get('scenarios') or {}).get('bear', {}).get('share_price')}"
        )
    ctx.evidence.add(
        source="dcf",
        title=f"{ctx.ticker} DCF valuation",
        summary=summary,
        meta={
            "ok": result.get("ok"),
            "base_share_price": ((result.get("scenarios") or {}).get("base") or {}).get("share_price"),
        },
    )
    return result


def tool_search_web(ctx: ToolContext) -> dict[str, Any]:
    from src.web_engine import (
        WEB_SUMMARY_PROMPT,
        build_research_queries,
        corpus_from_web,
        format_web_markdown,
        search_and_read,
    )

    label = ctx.active_section_id or "web"
    ctx.progress("web", f"Searching news/web for {ctx.ticker} ({label})")
    company = None
    if ctx.fundamentals:
        company = ctx.fundamentals.get("company_name")
    elif ctx.fundamentals is None:
        try:
            tool_get_fundamentals(ctx)
            company = (ctx.fundamentals or {}).get("company_name")
        except Exception:  # noqa: BLE001
            company = None

    section_queries = list(ctx.active_section_queries or [])
    if section_queries:
        queries = section_queries
    else:
        queries = build_research_queries(
            ctx.ticker,
            company_name=company,
            goal=ctx.plan_goal,
            extra_queries=ctx.plan_queries,
        )
    try:
        web = search_and_read(queries, max_results_per_query=4, max_pages_to_fetch=3)
    except Exception as exc:  # noqa: BLE001
        logger.exception("web search failed")
        web = {
            "queries": queries,
            "hits": [],
            "pages": [],
            "errors": [str(exc)],
            "hit_count": 0,
            "fetched_ok": 0,
        }
        ctx.errors.append(f"search_web: {exc}")

    web["section_id"] = label
    corpus = corpus_from_web(web)
    ctx.progress("web", f"Summarizing web findings ({label})")
    summary = nlp_engine.summarize_text(
        corpus or None,
        f"Web synthesis — {label}",
        prompt_template=WEB_SUMMARY_PROMPT,
    )
    web["summary_markdown"] = summary.get("markdown") or ""
    web["report_markdown"] = format_web_markdown(web, web["summary_markdown"])

    # Merge across multiple search_web sections (analysts + drivers)
    if ctx.web:
        merged_hits = {(h.get("url") or ""): h for h in (ctx.web.get("hits") or [])}
        for h in web.get("hits") or []:
            merged_hits[h.get("url") or ""] = h
        ctx.web = {
            "queries": list(dict.fromkeys([*(ctx.web.get("queries") or []), *(web.get("queries") or [])])),
            "hits": [h for u, h in merged_hits.items() if u],
            "pages": [*(ctx.web.get("pages") or []), *(web.get("pages") or [])],
            "errors": [*(ctx.web.get("errors") or []), *(web.get("errors") or [])],
            "hit_count": len([u for u in merged_hits if u]),
            "fetched_ok": sum(1 for p in [*(ctx.web.get("pages") or []), *(web.get("pages") or [])] if p.get("ok")),
            "sections": [*(ctx.web.get("sections") or []), label],
        }
    else:
        web["sections"] = [label]
        ctx.web = web

    ctx.web_reports.append(web)
    ctx.web_summary = summary

    for h in (web.get("hits") or [])[:8]:
        ctx.evidence.add(
            source="web",
            title=h.get("title") or h.get("url") or "web hit",
            summary=(h.get("snippet") or "")[:400],
            url=h.get("url"),
            meta={"kind": h.get("kind"), "query": h.get("query"), "section": label},
        )
    for p in web.get("pages") or []:
        if not p.get("ok"):
            continue
        ctx.evidence.add(
            source="web_page",
            title=p.get("title") or p.get("search_title") or p.get("url") or "page",
            summary=(p.get("text") or "")[:400],
            url=p.get("url"),
            meta={"section": label},
        )

    return web


TOOL_REGISTRY: dict[str, Callable[[ToolContext], Any]] = {
    "get_fundamentals": tool_get_fundamentals,
    "screen_puts": tool_screen_puts,
    "fetch_10k": tool_fetch_10k,
    "summarize_item_1a": tool_summarize_item_1a,
    "summarize_item_7": tool_summarize_item_7,
    "run_dcf": tool_run_dcf,
    "search_web": tool_search_web,
}
