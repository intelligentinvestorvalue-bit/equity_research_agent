"""Peer comps via yfinance (free local data)."""

from __future__ import annotations

import logging
import math
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)

# Industry / sector keyword → peer tickers (best-effort defaults)
_PEER_MAP: list[tuple[tuple[str, ...], list[str]]] = [
    (("telecom", "telephone", "communication services"), ["T", "VZ", "TMUS", "EQIX", "CCI"]),
    (("software", "internet", "information technology"), ["MSFT", "ORCL", "ADBE", "CRM", "NOW"]),
    (("semiconductor",), ["NVDA", "AMD", "AVGO", "TSM", "INTC"]),
    (("bank", "financial"), ["JPM", "BAC", "WFC", "C", "GS"]),
    (("oil", "gas", "energy"), ["XOM", "CVX", "COP", "SLB", "EOG"]),
    (("retail", "consumer cyclical"), ["AMZN", "WMT", "TGT", "COST", "HD"]),
    (("biotech", "pharma", "healthcare"), ["PFE", "JNJ", "MRK", "LLY", "ABBV"]),
    (("mining", "uranium", "metal"), ["CCJ", "UEC", "NXE", "UUUU", "FCX"]),
    (("utility", "electric"), ["NEE", "DUK", "SO", "D", "AEP"]),
]


def _to_float(val: Any) -> float | None:
    if val is None:
        return None
    try:
        if isinstance(val, float) and math.isnan(val):
            return None
        return float(val)
    except (TypeError, ValueError):
        return None


def suggest_peers(ticker: str, sector: str | None = None, industry: str | None = None) -> list[str]:
    blob = f"{sector or ''} {industry or ''}".lower()
    peers: list[str] = []
    for keys, tickers in _PEER_MAP:
        if any(k in blob for k in keys):
            peers = list(tickers)
            break
    t = ticker.upper()
    return [p for p in peers if p != t][:5]


def _price_return(hist: pd.DataFrame, years: float) -> float | None:
    if hist is None or hist.empty or "Close" not in hist.columns:
        return None
    try:
        closes = hist["Close"].dropna()
        if closes.empty:
            return None
        end = float(closes.iloc[-1])
        # approx trading days
        n = int(years * 252)
        if len(closes) <= n:
            start = float(closes.iloc[0])
        else:
            start = float(closes.iloc[-n])
        if start == 0:
            return None
        return (end / start) - 1.0
    except Exception:  # noqa: BLE001
        return None


def _ann_vol(hist: pd.DataFrame) -> float | None:
    if hist is None or hist.empty or "Close" not in hist.columns:
        return None
    try:
        rets = hist["Close"].pct_change().dropna()
        if len(rets) < 20:
            return None
        return float(rets.std() * math.sqrt(252))
    except Exception:  # noqa: BLE001
        return None


def _snapshot_ticker(sym: str) -> dict[str, Any]:
    t = yf.Ticker(sym)
    info = t.info or {}
    try:
        hist = t.history(period="5y")
    except Exception:  # noqa: BLE001
        hist = pd.DataFrame()
    mcap = _to_float(info.get("marketCap"))
    ebitda = _to_float(info.get("ebitda"))
    ev = _to_float(info.get("enterpriseValue"))
    total_debt = _to_float(info.get("totalDebt"))
    cash = _to_float(info.get("totalCash"))
    net_debt = None
    if total_debt is not None or cash is not None:
        net_debt = (total_debt or 0.0) - (cash or 0.0)
    ev_ebitda = (ev / ebitda) if ev is not None and ebitda not in (None, 0) else _to_float(info.get("enterpriseToEbitda"))
    nd_ebitda = (net_debt / ebitda) if net_debt is not None and ebitda not in (None, 0) else None
    return {
        "ticker": sym.upper(),
        "name": info.get("shortName") or info.get("longName"),
        "price": _to_float(info.get("currentPrice") or info.get("regularMarketPrice")),
        "market_cap": mcap,
        "enterprise_value": ev,
        "ebitda": ebitda,
        "ev_to_ebitda": ev_ebitda,
        "net_debt_to_ebitda": nd_ebitda,
        "beta": _to_float(info.get("beta")),
        "return_1y": _price_return(hist, 1.0),
        "return_5y": _price_return(hist, 5.0),
        "volatility": _ann_vol(hist),
        "history": hist,
    }


def fetch_peer_comps(
    ticker: str,
    peers: list[str] | None = None,
    fund: dict[str, Any] | None = None,
) -> dict[str, Any]:
    ticker = ticker.upper()
    fund = fund or {}
    snap = fund.get("snapshot") or {}
    sector = snap.get("sector") or fund.get("sector")
    industry = snap.get("industry") or fund.get("industry")
    if not peers:
        peers = suggest_peers(ticker, sector=sector, industry=industry)
    notes: list[str] = []
    if not peers:
        notes.append("No industry peer map match; comps limited to the subject ticker.")
    else:
        notes.append(f"Peer set (heuristic by sector/industry): {', '.join(peers)}")

    universe = [ticker, *[p.upper() for p in peers if p.upper() != ticker]]
    rows: list[dict[str, Any]] = []
    histories: dict[str, pd.DataFrame] = {}
    for sym in universe:
        try:
            row = _snapshot_ticker(sym)
            histories[sym] = row.pop("history", pd.DataFrame())
            rows.append(row)
        except Exception as exc:  # noqa: BLE001
            logger.warning("peer %s failed: %s", sym, exc)
            notes.append(f"{sym}: {exc}")

    # Beta vs first peer if available
    subject_beta_vs_peer = None
    if len(universe) >= 2 and ticker in histories and universe[1] in histories:
        try:
            a = histories[ticker]["Close"].pct_change().dropna()
            b = histories[universe[1]]["Close"].pct_change().dropna()
            joined = pd.concat([a, b], axis=1, join="inner").dropna()
            if len(joined) > 60:
                cov = np.cov(joined.iloc[:, 0], joined.iloc[:, 1])
                var = cov[1, 1]
                if var:
                    subject_beta_vs_peer = float(cov[0, 1] / var)
                    notes.append(f"Beta vs {universe[1]} (daily, ~5y overlap): {subject_beta_vs_peer:.2f}")
        except Exception as exc:  # noqa: BLE001
            logger.debug("beta vs peer failed: %s", exc)

    return {
        "ticker": ticker,
        "peers": peers,
        "sector": sector,
        "industry": industry,
        "rows": rows,
        "beta_vs_peer": subject_beta_vs_peer,
        "beta_vs_peer_symbol": universe[1] if len(universe) >= 2 else None,
        "notes": notes,
        "histories": {k: v for k, v in histories.items() if v is not None and not v.empty},
        "ok": bool(rows),
    }


def format_peer_comps_markdown(comps: dict[str, Any]) -> str:
    lines = [
        "## Peer & factor comps",
        "",
        f"- Sector / industry: {comps.get('sector') or '—'} / {comps.get('industry') or '—'}",
        f"- Peers: {', '.join(comps.get('peers') or []) or '—'}",
        "",
    ]
    rows = comps.get("rows") or []
    if not rows:
        lines.append("_No peer data available._")
        lines.append("")
        return "\n".join(lines) + "\n"

    def _m(v: Any) -> str:
        if v is None:
            return "—"
        v = float(v)
        sign = "-" if v < 0 else ""
        a = abs(v)
        if a >= 1e9:
            return f"{sign}${a / 1e9:.1f}B"
        if a >= 1e6:
            return f"{sign}${a / 1e6:.1f}M"
        return f"{sign}${a:,.0f}"

    def _pct(v: Any) -> str:
        return f"{float(v) * 100:.1f}%" if v is not None else "—"

    def _x(v: Any) -> str:
        return f"{float(v):.1f}x" if v is not None else "—"

    lines.append("| Ticker | Mkt cap | EV/EBITDA | ND/EBITDA | Beta | 1y | 5y | Vol |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for r in rows:
        lines.append(
            "| {t} | {mc} | {ev} | {nd} | {b} | {r1} | {r5} | {v} |".format(
                t=r.get("ticker"),
                mc=_m(r.get("market_cap")),
                ev=_x(r.get("ev_to_ebitda")),
                nd=_x(r.get("net_debt_to_ebitda")),
                b=f"{float(r['beta']):.2f}" if r.get("beta") is not None else "—",
                r1=_pct(r.get("return_1y")),
                r5=_pct(r.get("return_5y")),
                v=_pct(r.get("volatility")),
            )
        )
    lines.append("")
    for n in comps.get("notes") or []:
        lines.append(f"- {n}")
    lines.append("")
    lines.append("_Price returns are price-only (dividends ignored). Peer set is heuristic, not a formal comps universe._")
    lines.append("")
    return "\n".join(lines) + "\n"
