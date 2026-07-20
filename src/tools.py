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

    def __init__(self, ticker: str, evidence: EvidenceStore, progress: ProgressCb) -> None:
        self.ticker = ticker.upper()
        self.evidence = evidence
        self.progress = progress
        self.fundamentals: dict[str, Any] | None = None
        self.options: dict[str, Any] | None = None
        self.sections: dict[str, Any] | None = None
        self.nlp_1a: dict[str, Any] | None = None
        self.nlp_7: dict[str, Any] | None = None
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
    summary = f"Expiration {opts.get('expiration')} (DTE {opts.get('dte')}): {n} candidates"
    if opts.get("error"):
        summary = f"Error: {opts['error']}"
    elif opts.get("note"):
        summary = f"{summary}. {opts['note']}"
    ctx.evidence.add(
        source="yfinance_options",
        title=f"{ctx.ticker} put screen",
        summary=summary,
        meta={"candidate_count": n, "expiration": opts.get("expiration")},
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


TOOL_REGISTRY: dict[str, Callable[[ToolContext], Any]] = {
    "get_fundamentals": tool_get_fundamentals,
    "screen_puts": tool_screen_puts,
    "fetch_10k": tool_fetch_10k,
    "summarize_item_1a": tool_summarize_item_1a,
    "summarize_item_7": tool_summarize_item_7,
}
