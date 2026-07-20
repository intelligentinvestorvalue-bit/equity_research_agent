"""End-to-end research orchestration."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from src.config import OUTPUT_DIR
from src import nlp_engine, quant_engine, sec_engine

logger = logging.getLogger(__name__)

ProgressCb = Callable[[str, str], None]


def _noop_progress(stage: str, message: str) -> None:
    logger.info("[%s] %s", stage, message)


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")


def run_research(
    ticker: str,
    mode: str = "deep",
    progress: ProgressCb | None = None,
) -> dict[str, Any]:
    """
    mode:
      - fast: quant only
      - deep / comprehensive: quant + SEC + NLP
    """
    progress = progress or _noop_progress
    ticker = ticker.upper().strip()
    mode = mode.lower().strip()
    if mode == "comprehensive":
        mode = "deep"
    if mode not in {"fast", "deep"}:
        raise ValueError(f"Unknown mode: {mode}")

    started = datetime.now(timezone.utc).isoformat()
    progress("quant", f"Fetching fundamentals/options for {ticker}")
    quant = quant_engine.run_quant(ticker)

    financials_path = OUTPUT_DIR / f"{ticker}_financials.json"
    _write_json(
        financials_path,
        {"ticker": ticker, "mode": mode, "generated_at": started, "quant": quant},
    )

    result: dict[str, Any] = {
        "ticker": ticker,
        "mode": mode,
        "generated_at": started,
        "quant": quant,
        "financials_path": str(financials_path),
        "sections": None,
        "nlp": None,
        "report_path": None,
        "report_markdown": None,
    }

    if mode == "fast":
        md = _format_fast_report(ticker, quant)
        report_path = OUTPUT_DIR / f"{ticker}_analysis_report.md"
        report_path.write_text(md, encoding="utf-8")
        result["report_path"] = str(report_path)
        result["report_markdown"] = md
        progress("done", "Fast research complete")
        return result

    progress("sec", "Fetching latest 10-K and extracting sections")
    try:
        sections = sec_engine.fetch_10k_sections(ticker)
        sec_engine.save_section_blocks(sections)
        result["sections"] = {
            "meta": sections.get("meta"),
            "item_1a_chars": sections.get("item_1a_chars"),
            "item_7_chars": sections.get("item_7_chars"),
            "extraction_ok": sections.get("extraction_ok"),
        }
    except Exception as exc:  # noqa: BLE001
        logger.exception("SEC failed for %s", ticker)
        sections = {"ticker": ticker, "item_1a": None, "item_7": None, "error": str(exc)}
        result["sections"] = {"error": str(exc), "extraction_ok": False}

    progress("nlp", "Running local LLM / fallback summarizer")
    nlp = nlp_engine.run_nlp(sections)
    result["nlp"] = {
        "ollama_up": nlp.get("ollama_up"),
        "item_1a_mode": nlp.get("item_1a", {}).get("mode"),
        "item_7_mode": nlp.get("item_7", {}).get("mode"),
    }

    md = _format_deep_report(ticker, quant, result.get("sections"), nlp)
    report_path = OUTPUT_DIR / f"{ticker}_analysis_report.md"
    report_path.write_text(md, encoding="utf-8")
    result["report_path"] = str(report_path)
    result["report_markdown"] = md
    progress("done", "Deep research complete")
    return result


def _format_fast_report(ticker: str, quant: dict[str, Any]) -> str:
    fund = quant.get("fundamentals") or {}
    ratios = fund.get("ratios") or {}
    opts = quant.get("options") or {}
    lines = [
        f"# {ticker} — Fast Research Report",
        "",
        "> Not investment advice. Local research draft only.",
        "",
        "## Fundamentals",
        f"- Company: {fund.get('company_name')}",
        f"- Price: {fund.get('price')}",
        f"- Market cap: {fund.get('market_cap')}",
        f"- ROIC: {ratios.get('roic')}",
        f"- FCF yield: {ratios.get('fcf_yield')}",
        f"- Debt / Equity: {ratios.get('debt_to_equity')}",
        "",
        "## Put opportunities (heuristic)",
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
    if fund.get("error"):
        lines += ["", f"**Fundamentals error:** {fund['error']}"]
    if opts.get("error"):
        lines += ["", f"**Options error:** {opts['error']}"]
    return "\n".join(lines) + "\n"


def _format_deep_report(
    ticker: str,
    quant: dict[str, Any],
    sections_meta: dict[str, Any] | None,
    nlp: dict[str, Any],
) -> str:
    base = _format_fast_report(ticker, quant).replace("Fast Research Report", "Deep Research Report")
    sec_bits = [
        "",
        "## SEC filing",
        f"- Extraction OK: {(sections_meta or {}).get('extraction_ok')}",
        f"- Item 1A chars: {(sections_meta or {}).get('item_1a_chars')}",
        f"- Item 7 chars: {(sections_meta or {}).get('item_7_chars')}",
        f"- Meta: {(sections_meta or {}).get('meta')}",
        "",
        "## Qualitative analysis (local LLM)",
        f"- Ollama up: {nlp.get('ollama_up')}",
        "",
        nlp.get("markdown") or "_No NLP output._",
        "",
    ]
    return base + "\n".join(sec_bits)
