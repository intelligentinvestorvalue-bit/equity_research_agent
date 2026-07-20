"""Quarterly driver correlations (suggestive; small-n caveats)."""

from __future__ import annotations

import logging
import math
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


def _to_float(val: Any) -> float | None:
    if val is None:
        return None
    try:
        if isinstance(val, float) and math.isnan(val):
            return None
        return float(val)
    except (TypeError, ValueError):
        return None


def pearson_corr(xs: list[float], ys: list[float]) -> dict[str, Any]:
    n = min(len(xs), len(ys))
    if n < 3:
        return {"r": None, "p": None, "n": n}
    x = np.array(xs[:n], dtype=float)
    y = np.array(ys[:n], dtype=float)
    if np.std(x) == 0 or np.std(y) == 0:
        return {"r": None, "p": None, "n": n}
    r = float(np.corrcoef(x, y)[0, 1])
    # two-sided p via t-approx
    if abs(r) >= 1.0:
        p = 0.0
    else:
        t = r * math.sqrt((n - 2) / (1 - r * r))
        # crude survival using erfc for normal approx of t when n large; for small n use same
        p = float(math.erfc(abs(t) / math.sqrt(2)))
    return {"r": round(r, 3), "p": round(p, 3), "n": n}


def spearman_corr(xs: list[float], ys: list[float]) -> dict[str, Any]:
    n = min(len(xs), len(ys))
    if n < 3:
        return {"rho": None, "p": None, "n": n}
    xr = pd.Series(xs[:n]).rank().to_numpy()
    yr = pd.Series(ys[:n]).rank().to_numpy()
    base = pearson_corr(list(xr), list(yr))
    return {"rho": base.get("r"), "p": base.get("p"), "n": base.get("n")}


def _quarterly_metric(df: pd.DataFrame, *keys: str) -> pd.Series:
    if df is None or not isinstance(df, pd.DataFrame) or df.empty:
        return pd.Series(dtype=float)
    row_key = next((k for k in keys if k in df.index), None)
    if row_key is None:
        return pd.Series(dtype=float)
    s = df.loc[row_key].apply(_to_float)
    s.index = pd.to_datetime(s.index)
    return s.dropna().sort_index()


def _quarterly_returns(ticker: str) -> pd.Series:
    t = yf.Ticker(ticker)
    hist = t.history(period="6y", interval="1d")
    if hist is None or hist.empty:
        return pd.Series(dtype=float)
    closes = hist["Close"].copy()
    if closes.index.tz is not None:
        closes.index = closes.index.tz_localize(None)
    q = closes.resample("QE").last().dropna()
    return q.pct_change().dropna()


def analyze_drivers(ticker: str) -> dict[str, Any]:
    """
    Correlate quarterly stock returns with FCF, revenue growth, OCF, debt, EBITDA.
    Results are suggestive only — especially with n < 20.
    """
    ticker = ticker.upper()
    notes: list[str] = [
        "Correlations describe association, not causation.",
        "Small samples (especially regime splits) are directional only.",
    ]
    t = yf.Ticker(ticker)
    try:
        q_income = t.quarterly_financials
        q_cash = t.quarterly_cashflow
        q_bal = t.quarterly_balance_sheet
    except Exception as exc:  # noqa: BLE001
        return {"ticker": ticker, "ok": False, "drivers": [], "notes": [str(exc)]}

    rev = _quarterly_metric(q_income, "Total Revenue", "Operating Revenue")
    ebitda = _quarterly_metric(q_income, "EBITDA", "Normalized EBITDA")
    ocf = _quarterly_metric(q_cash, "Operating Cash Flow", "Total Cash From Operating Activities")
    capex = _quarterly_metric(q_cash, "Capital Expenditure", "Capital Expenditures").abs()
    fcf = (ocf - capex).dropna() if not ocf.empty else pd.Series(dtype=float)
    debt = _quarterly_metric(q_bal, "Long Term Debt", "Total Debt")
    rets = _quarterly_returns(ticker)

    rev_yoy = rev.pct_change(4) if len(rev) >= 5 else pd.Series(dtype=float)
    fcf_margin = (fcf / rev.replace(0, np.nan)).dropna() if not fcf.empty and not rev.empty else pd.Series(dtype=float)

    series_map = {
        "Revenue growth (YoY)": rev_yoy,
        "Free cash flow": fcf,
        "FCF margin": fcf_margin,
        "Operating cash flow": ocf,
        "Long-term debt level": debt,
        "EBITDA": ebitda,
        "Capex (abs)": capex,
    }

    drivers: list[dict[str, Any]] = []
    for name, series in series_map.items():
        if series is None or series.empty or rets.empty:
            drivers.append({"driver": name, "pearson": None, "spearman": None, "n": 0})
            continue
        joined = pd.concat([rets.rename("ret"), series.rename("x")], axis=1, join="inner").dropna()
        n = len(joined)
        if n < 5:
            drivers.append({"driver": name, "pearson": None, "spearman": None, "n": n})
            continue
        xs = joined["x"].tolist()
        ys = joined["ret"].tolist()
        drivers.append(
            {
                "driver": name,
                "pearson": pearson_corr(xs, ys),
                "spearman": spearman_corr(xs, ys),
                "n": n,
            }
        )

    # Simple regime split: pre/post median date of return sample
    regime: list[dict[str, Any]] = []
    if len(rets) >= 12 and not fcf.empty:
        mid = rets.index[len(rets) // 2]
        for label, mask in (("earlier", rets.index <= mid), ("later", rets.index > mid)):
            sub_rets = rets.loc[mask]
            joined = pd.concat([sub_rets.rename("ret"), fcf.rename("x")], axis=1, join="inner").dropna()
            if len(joined) < 5:
                continue
            regime.append(
                {
                    "regime": label,
                    "driver": "Free cash flow",
                    "pearson": pearson_corr(joined["x"].tolist(), joined["ret"].tolist()),
                    "n": len(joined),
                }
            )
        notes.append(f"Regime split at {mid.date()} (sample midpoint); directional only.")

    ok = any((d.get("pearson") or {}).get("r") is not None for d in drivers)
    if not ok:
        notes.append("Insufficient quarterly overlap for driver correlations.")
    return {
        "ticker": ticker,
        "ok": ok,
        "drivers": drivers,
        "regime": regime,
        "notes": notes,
    }


def format_drivers_markdown(result: dict[str, Any]) -> str:
    lines = [
        "## Key driver analysis (quarterly)",
        "",
        "Pearson / Spearman correlations of quarterly stock returns with fundamentals.",
        "",
    ]
    drivers = result.get("drivers") or []
    if not drivers:
        lines.append("_No driver statistics available._")
        lines.append("")
        return "\n".join(lines) + "\n"

    lines.append("| Driver | Pearson r | p | n | Spearman ρ | p |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for d in drivers:
        p = d.get("pearson") or {}
        s = d.get("spearman") or {}

        def _fmt(v: Any) -> str:
            return f"{v:.3f}" if isinstance(v, (int, float)) else "—"

        lines.append(
            f"| {d.get('driver')} | {_fmt(p.get('r'))} | {_fmt(p.get('p'))} | {d.get('n') or p.get('n') or '—'} | "
            f"{_fmt(s.get('rho'))} | {_fmt(s.get('p'))} |"
        )
    lines.append("")
    if result.get("regime"):
        lines.append("### Regime check (FCF)")
        lines.append("")
        for r in result["regime"]:
            pr = r.get("pearson") or {}
            lines.append(
                f"- {r.get('regime')}: r={pr.get('r')} (n={r.get('n')}, p≈{pr.get('p')})"
            )
        lines.append("")
    for n in result.get("notes") or []:
        lines.append(f"- {n}")
    lines.append("")
    return "\n".join(lines) + "\n"
