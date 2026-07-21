"""Institutional memo thesis sections (Ollama + rule-based fallback)."""

from __future__ import annotations

import logging
import re
from typing import Any

from src.nlp_engine import ollama_available, summarize_text

logger = logging.getLogger(__name__)

MEMO_PROMPT = """You are drafting sections of an equity research memo (NOT investment advice; no buy/sell rating).
Use ONLY the facts in the context. If something is unknown, say so.

Write markdown with these exact headings (##):
## Executive summary
## Company setup & business model
## Variant perception
## Catalysts & monitoring
## Falsification triggers
## Source quality & limitations

Under Company setup & business model: write a thorough overview (ideally 400–800 words) grounded in the
10-K Item 1 Business summary when provided — cover what the company does, products/segments, customers,
competitive position, geography/operations, and strategic focus. Do not invent details absent from context.
Under Variant perception include short bull / bear / consensus framing.
Under Falsification triggers use a short bullet list of invalidation rules.
Under Source quality & limitations note free-data limits (yfinance/SEC/web) and that figures may be incomplete.

Context:
{chunk}
"""


def _money(v: Any) -> str:
    if v is None:
        return "—"
    try:
        v = float(v)
    except (TypeError, ValueError):
        return "—"
    sign = "-" if v < 0 else ""
    a = abs(v)
    if a >= 1e9:
        return f"{sign}${a / 1e9:.2f}B"
    if a >= 1e6:
        return f"{sign}${a / 1e6:.2f}M"
    return f"{sign}${a:,.0f}"


def _build_context(
    ticker: str,
    fund: dict[str, Any] | None,
    valuation: dict[str, Any] | None,
    multiples: dict[str, Any] | None,
    peers: dict[str, Any] | None,
    web: dict[str, Any] | None,
    nlp_business: dict[str, Any] | None,
    nlp_1a: dict[str, Any] | None,
    nlp_7: dict[str, Any] | None,
    earnings: dict[str, Any] | None,
    filings_extra: dict[str, Any] | None,
    goal: str = "",
) -> str:
    fund = fund or {}
    snap = fund.get("snapshot") or {}
    cap = fund.get("capital_structure") or {}
    parts = [
        f"Ticker: {ticker}",
        f"Company: {fund.get('company_name')}",
        f"Goal: {goal or 'Institutional deep-dive memo'}",
        f"Price: {fund.get('price')}, Mkt cap: {_money(fund.get('market_cap'))}, EV: {_money(snap.get('enterprise_value'))}",
        f"Sector/Industry: {snap.get('sector')} / {snap.get('industry')}",
        f"Revenue: {_money(fund.get('revenue'))}, EBITDA: {_money(fund.get('ebitda'))}, FCF: {_money(fund.get('free_cash_flow'))}",
        f"Net debt: {_money(cap.get('net_debt'))}, ND/EBITDA: {cap.get('net_debt_to_ebitda')}, Book equity: {_money(cap.get('book_equity'))}",
        f"52w: {snap.get('fifty_two_week_low')} – {snap.get('fifty_two_week_high')}, beta={snap.get('beta')}",
        f"Street (sparse): target mean={snap.get('target_mean_price')}, rec={snap.get('recommendation')}",
    ]
    if multiples and multiples.get("scenarios"):
        for k, sc in (multiples.get("scenarios") or {}).items():
            parts.append(
                f"EV/EBITDA {k}: ebitda={sc.get('ebitda')}, mult={sc.get('multiple')}, px={sc.get('share_price')}"
            )
    if valuation and valuation.get("scenarios"):
        for k, sc in (valuation.get("scenarios") or {}).items():
            parts.append(f"DCF {k} share_price={sc.get('share_price')}")
    if peers:
        parts.append(f"Peers: {', '.join(peers.get('peers') or [])}")
        for r in (peers.get("rows") or [])[:6]:
            parts.append(
                f"Peer {r.get('ticker')}: EV/EBITDA={r.get('ev_to_ebitda')}, 1y={r.get('return_1y')}, vol={r.get('volatility')}"
            )
    if earnings:
        parts.append(f"Next earnings: {earnings.get('next_earnings')}")
        for r in (earnings.get("rows") or [])[:4]:
            parts.append(
                f"Earnings {r.get('date')}: est={r.get('eps_estimate')} act={r.get('eps_actual')} move={r.get('one_day_move')}"
            )
    if filings_extra:
        for f in (filings_extra.get("recent") or [])[:8]:
            parts.append(f"Filing {f.get('form')} {f.get('filing_date')}: {f.get('description') or f.get('accession')}")
    if nlp_business:
        parts.append("Item 1 Business summary (primary for Company setup):\n" + ((nlp_business.get("markdown") or "")[:6000]))
    if nlp_1a:
        parts.append("Item 1A summary:\n" + ((nlp_1a.get("markdown") or "")[:1800]))
    if nlp_7:
        parts.append("Item 7 summary:\n" + ((nlp_7.get("markdown") or "")[:1800]))
    if web:
        for h in (web.get("hits") or [])[:8]:
            parts.append(f"Web: {h.get('title')} — {(h.get('snippet') or '')[:220]}")
        for p in (web.get("pages") or [])[:3]:
            if p.get("ok"):
                parts.append(f"Page {p.get('title')}: {(p.get('text') or '')[:500]}")
    return "\n".join(parts)


def _rule_memo(
    ticker: str,
    fund: dict[str, Any] | None,
    multiples: dict[str, Any] | None,
    peers: dict[str, Any] | None,
    earnings: dict[str, Any] | None,
    filings_extra: dict[str, Any] | None,
    goal: str = "",
    nlp_business: dict[str, Any] | None = None,
) -> str:
    fund = fund or {}
    snap = fund.get("snapshot") or {}
    cap = fund.get("capital_structure") or {}
    name = fund.get("company_name") or ticker
    base_px = ((multiples or {}).get("scenarios") or {}).get("base", {}).get("share_price")
    bear_px = ((multiples or {}).get("scenarios") or {}).get("bear", {}).get("share_price")
    bull_px = ((multiples or {}).get("scenarios") or {}).get("bull", {}).get("share_price")
    peer_list = ", ".join((peers or {}).get("peers") or []) or "n/a"
    next_e = (earnings or {}).get("next_earnings") or "unconfirmed"
    recent = (filings_extra or {}).get("recent") or []

    lines = [
        "## Executive summary",
        "",
        f"{name} ({ticker}) trades near {fund.get('price')} with market cap {_money(fund.get('market_cap'))} "
        f"and EV {_money(snap.get('enterprise_value'))}. Net debt is {_money(cap.get('net_debt'))} "
        f"(ND/EBITDA {cap.get('net_debt_to_ebitda') if cap.get('net_debt_to_ebitda') is not None else '—'}). "
        f"Latest revenue {_money(fund.get('revenue'))}, EBITDA {_money(fund.get('ebitda'))}, FCF {_money(fund.get('free_cash_flow'))}.",
        "",
        f"**Goal focus:** {goal or 'institutional deep-dive structure'}.",
        "",
        "What matters most (framework): balance-sheet trajectory, cash generation vs leverage, "
        "and whether market expectations (sparse free-data targets) already price execution risk.",
        "",
        f"EV/EBITDA implied prices — bear {f'${bear_px:.2f}' if bear_px is not None else '—'} / "
        f"base {f'${base_px:.2f}' if base_px is not None else '—'} / "
        f"bull {f'${bull_px:.2f}' if bull_px is not None else '—'}.",
        "",
        "## Company setup & business model",
        "",
    ]
    biz_md = ((nlp_business or {}).get("markdown") or "").strip()
    if biz_md:
        # Drop a redundant top ### heading if present; keep subsections
        biz_body = re.sub(r"^###\s+Item 1[^\n]*\n+", "", biz_md, count=1, flags=re.I).strip()
        lines.append(biz_body)
        lines.append("")
        lines.append("_Source: latest 10-K Item 1 (Business), summarized locally._")
        lines.append("")
    else:
        lines += [
            f"Sector/industry: {snap.get('sector') or '—'} / {snap.get('industry') or '—'}. "
            "Run `summarize_item_1` on the latest 10-K to populate a full business overview from Item 1.",
            "",
        ]
    lines += [
        "## Variant perception",
        "",
        f"- **Consensus frame (sparse):** recommendation={snap.get('recommendation') or '—'}, "
        f"mean target={snap.get('target_mean_price') or '—'}.",
        "- **Bear:** leverage and execution risk dominate; cash generation fails to cover refinancing / reinvestment needs; "
        "equity remains constrained by net debt.",
        "- **Bull:** cash-flow and strategic optionality re-rate the equity as leverage falls and growth/mix improves.",
        "- **Middle:** returns may track free-cash-flow more than headline revenue — verify with driver analysis tab.",
        "",
        "## Catalysts & monitoring",
        "",
        f"- Next earnings window (calendar): {next_e}",
        f"- Peer tape to watch: {peer_list}",
        "- Monitor: FCF vs net debt, leverage (ND/EBITDA), refinancing headlines, and material 8-K strategy updates.",
    ]
    for f in recent[:5]:
        lines.append(f"- Recent filing: {f.get('form')} on {f.get('filing_date')} — {f.get('description') or ''}")
    lines += [
        "",
        "## Falsification triggers",
        "",
        "- Leverage (net debt/EBITDA) re-rises sustainably above prior repaired levels without offsetting EBITDA growth.",
        "- Underlying FCF (ex one-times, when identifiable) trends below levels needed to service debt and fund required capex.",
        "- Strategic thesis KPIs (from filings/web) stall for consecutive reporting periods.",
        "- Distressed refinancing, covenant stress, or major customer/contract loss headlines.",
        "",
        "## Source quality & limitations",
        "",
        "- Quantitative data from yfinance (statements, prices, sparse targets); qualitative from SEC + public web.",
        "- Consensus revenue/EBITDA estimates and adjusted metrics are often unavailable — do not treat missing fields as zero.",
        "- Peer sets are heuristic by sector/industry keyword maps.",
        "- This is a local research draft only — not investment advice and not a rating.",
        "",
    ]
    return "\n".join(lines)


def _extract_proxy_rows(web: dict[str, Any] | None, ticker: str) -> list[dict[str, str]]:
    """Heuristic proxy tracker rows from web snippets."""
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    patterns = [
        (r"guidance|outlook|forecast", "Guidance / outlook", "Forward cash/earnings path"),
        (r"debt|refinanc|leverage|maturity", "Leverage / refinancing", "Balance-sheet repair"),
        (r"contract|backlog|customer|hyperscaler|partnership", "Contract / backlog", "Demand durability"),
        (r"capex|buildout|capacity|miles", "Capex / capacity", "Leading indicator of future revenue"),
        (r"margin|ebitda", "Margin / EBITDA", "Mix and operating leverage"),
    ]
    texts: list[tuple[str, str]] = []
    for h in (web or {}).get("hits") or []:
        texts.append((h.get("title") or "", f"{h.get('title') or ''} {h.get('snippet') or ''}"))
    for p in (web or {}).get("pages") or []:
        if p.get("ok"):
            texts.append((p.get("title") or "", (p.get("text") or "")[:800]))

    for title, blob in texts:
        low = blob.lower()
        for pat, proxy, why in patterns:
            if re.search(pat, low) and proxy not in seen:
                seen.add(proxy)
                snippet = re.sub(r"\s+", " ", blob).strip()[:180]
                rows.append(
                    {
                        "proxy": proxy,
                        "why": why,
                        "signal": snippet or title or "See web sources",
                        "source": title or ticker,
                    }
                )
    if not rows:
        rows = [
            {
                "proxy": "Free cash flow",
                "why": "Cash generation vs leverage",
                "signal": "Track quarterly FCF and one-time adjustments in filings",
                "source": "financials",
            },
            {
                "proxy": "Net debt / EBITDA",
                "why": "Balance-sheet repair",
                "signal": "Watch leverage trend in capital structure section",
                "source": "financials",
            },
        ]
    return rows[:8]


def format_proxy_tracker_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "## Early proxy tracker",
        "",
        "| Proxy | Why it matters | Current signal | Source |",
        "|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r.get('proxy', '')} | {r.get('why', '')} | {r.get('signal', '').replace('|', '/')} | {r.get('source', '')} |"
        )
    lines.append("")
    lines.append("_Proxies are heuristic extractions from public web/SEC context; verify against primary filings._")
    lines.append("")
    return "\n".join(lines) + "\n"


def format_catalyst_calendar_markdown(
    earnings: dict[str, Any] | None,
    filings_extra: dict[str, Any] | None,
    web: dict[str, Any] | None,
) -> str:
    lines = [
        "## Catalyst calendar",
        "",
        "| Window | Catalyst | Notes |",
        "|---|---|---|",
    ]
    if earnings and earnings.get("next_earnings"):
        lines.append(f"| {earnings['next_earnings']} | Earnings | Next report date from yfinance calendar |")
    for f in (filings_extra or {}).get("recent") or []:
        if f.get("form") in {"8-K", "10-Q", "10-K"}:
            lines.append(
                f"| {f.get('filing_date')} | {f.get('form')} | {(f.get('description') or '')[:120]} |"
            )
    # dated-ish web headlines
    date_re = re.compile(r"\b(20\d{2}[-/]\d{1,2}[-/]\d{1,2}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+20\d{2})", re.I)
    for h in (web or {}).get("hits") or []:
        title = h.get("title") or ""
        m = date_re.search(f"{title} {h.get('snippet') or ''}")
        if m:
            lines.append(f"| {m.group(0)} | Web event | {title[:140]} |")
    if len(lines) <= 4:
        lines.append("| Near term | Monitor filings & earnings | No dated catalysts extracted |")
    lines.append("")
    return "\n".join(lines) + "\n"


def draft_memo_sections(
    ticker: str,
    *,
    fund: dict[str, Any] | None = None,
    valuation: dict[str, Any] | None = None,
    multiples: dict[str, Any] | None = None,
    peers: dict[str, Any] | None = None,
    web: dict[str, Any] | None = None,
    nlp_business: dict[str, Any] | None = None,
    nlp_1a: dict[str, Any] | None = None,
    nlp_7: dict[str, Any] | None = None,
    earnings: dict[str, Any] | None = None,
    filings_extra: dict[str, Any] | None = None,
    goal: str = "",
) -> dict[str, Any]:
    ctx = _build_context(
        ticker,
        fund,
        valuation,
        multiples,
        peers,
        web,
        nlp_business,
        nlp_1a,
        nlp_7,
        earnings,
        filings_extra,
        goal=goal,
    )
    mode = "rules"
    body = ""
    if ollama_available():
        try:
            result = summarize_text(ctx, "Memo sections", prompt_template=MEMO_PROMPT)
            body = (result.get("markdown") or "").strip()
            mode = result.get("mode") or "ollama"
            # Ensure required headings exist
            if "## Executive summary" not in body:
                body = ""
            # Prefer the dedicated Item 1 summary for Company setup when Ollama stays thin
            elif nlp_business and (nlp_business.get("markdown") or "").strip():
                biz = (nlp_business.get("markdown") or "").strip()
                biz_body = re.sub(r"^###\s+Item 1[^\n]*\n+", "", biz, count=1, flags=re.I).strip()
                body = _replace_section(
                    body,
                    "## Company setup & business model",
                    "## Company setup & business model\n\n"
                    + biz_body
                    + "\n\n_Source: latest 10-K Item 1 (Business), summarized locally._\n",
                )
        except Exception as exc:  # noqa: BLE001
            logger.warning("memo ollama failed: %s", exc)
            body = ""

    if not body:
        body = _rule_memo(
            ticker,
            fund,
            multiples,
            peers,
            earnings,
            filings_extra,
            goal=goal,
            nlp_business=nlp_business,
        )
        mode = "rules"

    proxy_rows = _extract_proxy_rows(web, ticker)
    proxy_md = format_proxy_tracker_markdown(proxy_rows)
    calendar_md = format_catalyst_calendar_markdown(earnings, filings_extra, web)

    full = body.rstrip() + "\n\n" + proxy_md + calendar_md
    return {
        "ticker": ticker.upper(),
        "mode": mode,
        "markdown": full,
        "proxy_rows": proxy_rows,
        "ok": True,
    }


def _replace_section(markdown: str, heading: str, replacement: str) -> str:
    """Replace a ## section through the next ## heading (or EOF)."""
    pattern = re.compile(
        rf"(^{re.escape(heading)}\s*\n)(.*?)(?=^## |\Z)",
        re.M | re.S,
    )
    if not pattern.search(markdown):
        return markdown.rstrip() + "\n\n" + replacement.strip() + "\n"
    return pattern.sub(replacement.rstrip() + "\n\n", markdown, count=1)
