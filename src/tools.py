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
        plan_multiples: dict[str, Any] | None = None,
    ) -> None:
        self.ticker = ticker.upper()
        self.evidence = evidence
        self.progress = progress
        self.plan_assumptions = plan_assumptions
        self.plan_multiples = plan_multiples
        self.plan_goal = plan_goal or ""
        self.plan_queries = list(plan_queries or [])
        self.fundamentals: dict[str, Any] | None = None
        self.options: dict[str, Any] | None = None
        self.sections: dict[str, Any] | None = None
        self.nlp_business: dict[str, Any] | None = None
        self.nlp_1a: dict[str, Any] | None = None
        self.nlp_7: dict[str, Any] | None = None
        self.valuation: dict[str, Any] | None = None
        self.multiples: dict[str, Any] | None = None
        self.peers: dict[str, Any] | None = None
        self.earnings: dict[str, Any] | None = None
        self.filings_extra: dict[str, Any] | None = None
        self.drivers: dict[str, Any] | None = None
        self.memo: dict[str, Any] | None = None
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
        sections = {
            "ticker": ctx.ticker,
            "item_1": None,
            "item_1a": None,
            "item_7": None,
            "error": str(exc),
            "extraction_ok": False,
        }
        ctx.errors.append(f"sec: {exc}")
    ctx.sections = sections
    meta = sections.get("meta") or {}
    summary = (
        f"Item 1 chars={sections.get('item_1_chars', 0)}, "
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


def tool_summarize_item_1(ctx: ToolContext) -> dict[str, Any]:
    if ctx.sections is None:
        tool_fetch_10k(ctx)
    ctx.progress("nlp", "Summarizing Item 1 Business")
    text = (ctx.sections or {}).get("item_1")
    result = nlp_engine.summarize_business(text)
    ctx.nlp_business = result
    ctx.evidence.add(
        source="nlp",
        title="Item 1 Business summary",
        summary=(result.get("markdown") or "")[:500],
        meta={"mode": result.get("mode")},
    )
    return result


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


def tool_run_ev_ebitda(ctx: ToolContext) -> dict[str, Any]:
    from src.multiples import format_multiples_markdown, merge_multiples, run_ev_ebitda

    if ctx.fundamentals is None:
        tool_get_fundamentals(ctx)
    ctx.progress("valuation", f"Running EV/EBITDA scenarios for {ctx.ticker}")
    fund = ctx.fundamentals or {}
    assumptions = merge_multiples(fund, ctx.plan_multiples)
    result = run_ev_ebitda(fund, assumptions)
    result["report_markdown"] = format_multiples_markdown(result)
    ctx.multiples = result
    if not result.get("ok"):
        ctx.errors.append("ev_ebitda: " + "; ".join(result.get("errors") or ["failed"]))
    base = (result.get("scenarios") or {}).get("base") or {}
    ctx.evidence.add(
        source="multiples",
        title=f"{ctx.ticker} EV/EBITDA valuation",
        summary=f"Base implied price={base.get('share_price')}, multiple={base.get('multiple')}",
        meta={"ok": result.get("ok"), "base_share_price": base.get("share_price")},
    )
    return result


def tool_get_peer_comps(ctx: ToolContext) -> dict[str, Any]:
    from src.peers import fetch_peer_comps, format_peer_comps_markdown

    if ctx.fundamentals is None:
        tool_get_fundamentals(ctx)
    ctx.progress("peers", f"Building peer comps for {ctx.ticker}")
    try:
        comps = fetch_peer_comps(ctx.ticker, fund=ctx.fundamentals)
    except Exception as exc:  # noqa: BLE001
        logger.exception("peers failed")
        comps = {"ticker": ctx.ticker, "rows": [], "peers": [], "ok": False, "notes": [str(exc)]}
        ctx.errors.append(f"peers: {exc}")
    # Drop heavy histories from ctx persistence path — keep for charts via attribute
    hist = comps.pop("histories", {})
    comps["report_markdown"] = format_peer_comps_markdown(comps)
    comps["_histories"] = hist
    ctx.peers = comps
    ctx.evidence.add(
        source="peers",
        title=f"{ctx.ticker} peer comps",
        summary=f"Peers: {', '.join(comps.get('peers') or [])}; rows={len(comps.get('rows') or [])}",
        meta={"peers": comps.get("peers")},
    )
    return comps


def tool_get_earnings(ctx: ToolContext) -> dict[str, Any]:
    from src.quant_engine import fetch_earnings_history, format_earnings_markdown

    ctx.progress("earnings", f"Fetching earnings history for {ctx.ticker}")
    try:
        earnings = fetch_earnings_history(ctx.ticker)
    except Exception as exc:  # noqa: BLE001
        logger.exception("earnings failed")
        earnings = {"ticker": ctx.ticker, "rows": [], "ok": False, "notes": [str(exc)]}
        ctx.errors.append(f"earnings: {exc}")
    earnings["report_markdown"] = format_earnings_markdown(earnings)
    ctx.earnings = earnings
    ctx.evidence.add(
        source="earnings",
        title=f"{ctx.ticker} earnings history",
        summary=f"rows={len(earnings.get('rows') or [])}; next={earnings.get('next_earnings')}",
        meta={"ok": earnings.get("ok")},
    )
    return earnings


def tool_fetch_recent_filings(ctx: ToolContext) -> dict[str, Any]:
    ctx.progress("sec", f"Listing recent 10-Q/8-K for {ctx.ticker}")
    try:
        filings = sec_engine.fetch_recent_filings(ctx.ticker)
    except Exception as exc:  # noqa: BLE001
        logger.exception("recent filings failed")
        filings = {"ticker": ctx.ticker, "recent": [], "ok": False, "error": str(exc)}
        ctx.errors.append(f"recent_filings: {exc}")
    filings["report_markdown"] = sec_engine.format_recent_filings_markdown(filings)
    ctx.filings_extra = filings
    for f in (filings.get("recent") or [])[:8]:
        ctx.evidence.add(
            source="sec",
            title=f"{ctx.ticker} {f.get('form')} {f.get('filing_date')}",
            summary=f.get("description") or "",
            url=f.get("url"),
            meta={"form": f.get("form"), "accession": f.get("accession")},
        )
    return filings


def tool_analyze_drivers(ctx: ToolContext) -> dict[str, Any]:
    from src.drivers import analyze_drivers, format_drivers_markdown

    ctx.progress("drivers", f"Computing driver correlations for {ctx.ticker}")
    try:
        result = analyze_drivers(ctx.ticker)
    except Exception as exc:  # noqa: BLE001
        logger.exception("drivers failed")
        result = {"ticker": ctx.ticker, "ok": False, "drivers": [], "notes": [str(exc)]}
        ctx.errors.append(f"drivers: {exc}")
    result["report_markdown"] = format_drivers_markdown(result)
    ctx.drivers = result
    ctx.evidence.add(
        source="drivers",
        title=f"{ctx.ticker} driver analysis",
        summary=f"ok={result.get('ok')}; drivers={len(result.get('drivers') or [])}",
        meta={"ok": result.get("ok")},
    )
    return result


def tool_draft_memo_sections(ctx: ToolContext) -> dict[str, Any]:
    from src.memo_engine import draft_memo_sections

    # Ensure inputs that memo benefits from
    if ctx.fundamentals is None:
        tool_get_fundamentals(ctx)
    ctx.progress("memo", f"Drafting memo thesis sections for {ctx.ticker}")
    result = draft_memo_sections(
        ctx.ticker,
        fund=ctx.fundamentals,
        valuation=ctx.valuation,
        multiples=ctx.multiples,
        peers=ctx.peers,
        web=ctx.web,
        nlp_business=ctx.nlp_business,
        nlp_1a=ctx.nlp_1a,
        nlp_7=ctx.nlp_7,
        earnings=ctx.earnings,
        filings_extra=ctx.filings_extra,
        goal=ctx.plan_goal,
    )
    ctx.memo = result
    ctx.evidence.add(
        source="memo",
        title=f"{ctx.ticker} memo sections",
        summary=f"mode={result.get('mode')}; proxies={len(result.get('proxy_rows') or [])}",
        meta={"mode": result.get("mode")},
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
    "summarize_item_1": tool_summarize_item_1,
    "summarize_item_1a": tool_summarize_item_1a,
    "summarize_item_7": tool_summarize_item_7,
    "run_dcf": tool_run_dcf,
    "run_ev_ebitda": tool_run_ev_ebitda,
    "get_peer_comps": tool_get_peer_comps,
    "get_earnings": tool_get_earnings,
    "fetch_recent_filings": tool_fetch_recent_filings,
    "analyze_drivers": tool_analyze_drivers,
    "draft_memo_sections": tool_draft_memo_sections,
    "search_web": tool_search_web,
}
