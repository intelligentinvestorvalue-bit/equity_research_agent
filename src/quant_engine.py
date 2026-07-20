"""Quantitative fundamentals and options aggregator (Module A)."""

from __future__ import annotations

import logging
import math
from typing import Any

import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


def _safe_get(series_or_df: Any, *keys: str) -> float | None:
    """Pull first available numeric field from a yfinance statement frame (latest col)."""
    history = _row_history(series_or_df, *keys, max_periods=1)
    return history[0]["value"] if history else None


def _to_float(val: Any) -> float | None:
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return None
    try:
        if pd.isna(val):
            return None
    except (TypeError, ValueError):
        pass
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def _row_history(series_or_df: Any, *keys: str, max_periods: int = 5) -> list[dict[str, Any]]:
    """
    Extract a named row across statement columns (newest → oldest).
    Returns [{period, value}, ...] with period as YYYY-MM-DD string when possible.
    """
    if series_or_df is None or not isinstance(series_or_df, pd.DataFrame) or series_or_df.empty:
        return []
    row_key = None
    for key in keys:
        if key in series_or_df.index:
            row_key = key
            break
    if row_key is None:
        return []
    out: list[dict[str, Any]] = []
    for col in list(series_or_df.columns)[:max_periods]:
        val = _to_float(series_or_df.loc[row_key, col])
        if val is None:
            continue
        period = col.strftime("%Y-%m-%d") if hasattr(col, "strftime") else str(col)[:10]
        out.append({"period": period, "value": val})
    return out


def _fcf_history(cashflow: Any, max_periods: int = 5) -> list[dict[str, Any]]:
    """Free cash flow ≈ operating CF − |capex| per period."""
    if cashflow is None or not isinstance(cashflow, pd.DataFrame) or cashflow.empty:
        return []
    ocf_key = next(
        (k for k in ("Operating Cash Flow", "Total Cash From Operating Activities") if k in cashflow.index),
        None,
    )
    capex_key = next(
        (k for k in ("Capital Expenditure", "Capital Expenditures") if k in cashflow.index),
        None,
    )
    if ocf_key is None:
        return []
    out: list[dict[str, Any]] = []
    for col in list(cashflow.columns)[:max_periods]:
        ocf = _to_float(cashflow.loc[ocf_key, col])
        if ocf is None:
            continue
        capex = _to_float(cashflow.loc[capex_key, col]) if capex_key else 0.0
        period = col.strftime("%Y-%m-%d") if hasattr(col, "strftime") else str(col)[:10]
        out.append({"period": period, "value": ocf - abs(capex or 0.0)})
    return out


def _yoy_growth(history: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """YoY growth between consecutive periods (newest first)."""
    growth: list[dict[str, Any]] = []
    for i in range(len(history) - 1):
        newer, older = history[i], history[i + 1]
        base = older["value"]
        if base in (None, 0):
            rate = None
        else:
            rate = (newer["value"] - base) / abs(base)
        growth.append(
            {
                "from_period": older["period"],
                "to_period": newer["period"],
                "rate": rate,
            }
        )
    return growth


def _cagr(history: list[dict[str, Any]]) -> float | None:
    """CAGR from oldest to newest point in history (newest-first list)."""
    if len(history) < 2:
        return None
    newest = history[0]["value"]
    oldest = history[-1]["value"]
    years = len(history) - 1
    if oldest in (None, 0) or newest is None or years <= 0:
        return None
    if oldest < 0 or newest < 0:
        # CAGR not meaningful across sign changes / negatives
        return None
    try:
        return (newest / oldest) ** (1.0 / years) - 1.0
    except (ZeroDivisionError, ValueError, OverflowError):
        return None


def compute_roic(ebit: float | None, total_debt: float | None, equity: float | None, cash: float | None) -> float | None:
    if ebit is None or equity is None:
        return None
    invested = (total_debt or 0.0) + equity - (cash or 0.0)
    if invested == 0:
        return None
    return ebit / invested


def compute_fcf_yield(operating_cf: float | None, capex: float | None, market_cap: float | None) -> float | None:
    if operating_cf is None or market_cap in (None, 0):
        return None
    fcf = operating_cf - abs(capex or 0.0)
    return fcf / market_cap


def compute_debt_to_equity(total_debt: float | None, equity: float | None) -> float | None:
    if total_debt is None or equity in (None, 0):
        return None
    return total_debt / equity


def _history_map(history: list[dict[str, Any]]) -> dict[str, float]:
    return {row["period"]: float(row["value"]) for row in history if row.get("value") is not None}


def _build_kpi_table(
    periods: list[str],
    series: dict[str, dict[str, float]],
) -> list[dict[str, Any]]:
    """Rows newest→oldest with aligned KPI columns."""
    rows: list[dict[str, Any]] = []
    for period in periods:
        row: dict[str, Any] = {"period": period, "year": (period or "")[:4]}
        for key, mp in series.items():
            row[key] = mp.get(period)
        ocf = row.get("operating_cash_flow")
        capex = row.get("capex")
        if row.get("free_cash_flow") is None and ocf is not None:
            row["free_cash_flow"] = ocf - abs(capex or 0.0)
        debt = row.get("long_term_debt")
        cash = row.get("cash")
        if debt is not None or cash is not None:
            row["net_debt"] = (debt or 0.0) - (cash or 0.0)
        ebitda = row.get("ebitda")
        nd = row.get("net_debt")
        if ebitda not in (None, 0) and nd is not None:
            row["net_debt_to_ebitda"] = nd / ebitda
        rows.append(row)
    return rows


def _align_periods(*histories: list[dict[str, Any]], max_periods: int = 6) -> list[str]:
    periods: list[str] = []
    seen: set[str] = set()
    for hist in histories:
        for row in hist:
            p = row.get("period")
            if p and p not in seen:
                seen.add(p)
                periods.append(p)
    return periods[:max_periods]


def fetch_fundamentals(ticker: str) -> dict[str, Any]:
    """Pull statements + richer metrics: revenue, FCF history, shares, growth rates."""
    t = yf.Ticker(ticker)
    info = t.info or {}
    income = t.financials
    balance = t.balance_sheet
    cashflow = t.cashflow

    ebit = _safe_get(income, "EBIT", "Operating Income")
    ebitda = _safe_get(income, "EBITDA", "Normalized EBITDA")
    if ebitda is None:
        ebitda = _to_float(info.get("ebitda"))
    operating_income = _safe_get(income, "Operating Income", "EBIT")
    total_debt = _safe_get(balance, "Total Debt", "Long Term Debt")
    lt_debt = _safe_get(balance, "Long Term Debt", "LongTermDebt")
    st_debt = _safe_get(
        balance,
        "Current Debt",
        "Current Debt And Capital Lease Obligation",
        "Short Long Term Debt",
    )
    if total_debt is None and (lt_debt is not None or st_debt is not None):
        total_debt = (lt_debt or 0.0) + (st_debt or 0.0)
    if lt_debt is None and total_debt is not None:
        lt_debt = total_debt - (st_debt or 0.0)
    equity = _safe_get(balance, "Stockholders Equity", "Total Stockholder Equity", "Common Stock Equity")
    cash = _safe_get(balance, "Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments")
    operating_cf = _safe_get(cashflow, "Operating Cash Flow", "Total Cash From Operating Activities")
    capex = _safe_get(cashflow, "Capital Expenditure", "Capital Expenditures")
    market_cap = _to_float(info.get("marketCap"))
    price = _to_float(info.get("currentPrice") or info.get("regularMarketPrice"))
    enterprise_value = _to_float(info.get("enterpriseValue"))
    book_value = _to_float(info.get("bookValue"))
    beta = _to_float(info.get("beta"))
    fifty_two_high = _to_float(info.get("fiftyTwoWeekHigh"))
    fifty_two_low = _to_float(info.get("fiftyTwoWeekLow"))
    target_mean = _to_float(info.get("targetMeanPrice"))
    target_high = _to_float(info.get("targetHighPrice"))
    target_low = _to_float(info.get("targetLowPrice"))
    recommendation = info.get("recommendationKey") or info.get("recommendationMean")

    revenue_hist = _row_history(income, "Total Revenue", "Operating Revenue", max_periods=6)
    fcf_hist = _fcf_history(cashflow, max_periods=6)
    op_inc_hist = _row_history(income, "Operating Income", "EBIT", max_periods=6)
    net_inc_hist = _row_history(income, "Net Income", "Net Income Common Stockholders", max_periods=6)
    ebitda_hist = _row_history(income, "EBITDA", "Normalized EBITDA", max_periods=6)
    ocf_hist = _row_history(
        cashflow, "Operating Cash Flow", "Total Cash From Operating Activities", max_periods=6
    )
    capex_hist = _row_history(cashflow, "Capital Expenditure", "Capital Expenditures", max_periods=6)
    # Capex often stored negative; normalize to absolute outflow for display
    capex_hist_abs = [
        {"period": r["period"], "value": abs(r["value"])} for r in capex_hist if r.get("value") is not None
    ]
    lt_debt_hist = _row_history(balance, "Long Term Debt", "LongTermDebt", max_periods=6)
    if not lt_debt_hist:
        lt_debt_hist = _row_history(balance, "Total Debt", max_periods=6)
    cash_hist = _row_history(
        balance,
        "Cash And Cash Equivalents",
        "Cash Cash Equivalents And Short Term Investments",
        max_periods=6,
    )

    periods = _align_periods(
        revenue_hist, fcf_hist, ocf_hist, ebitda_hist, lt_debt_hist, net_inc_hist, max_periods=6
    )
    kpi_table = _build_kpi_table(
        periods,
        {
            "revenue": _history_map(revenue_hist),
            "operating_cash_flow": _history_map(ocf_hist),
            "capex": _history_map(capex_hist_abs),
            "free_cash_flow": _history_map(fcf_hist),
            "ebitda": _history_map(ebitda_hist),
            "long_term_debt": _history_map(lt_debt_hist),
            "cash": _history_map(cash_hist),
            "net_income": _history_map(net_inc_hist),
            "operating_income": _history_map(op_inc_hist),
        },
    )

    revenue = revenue_hist[0]["value"] if revenue_hist else None
    fcf = fcf_hist[0]["value"] if fcf_hist else (
        (operating_cf - abs(capex or 0.0)) if operating_cf is not None else None
    )
    shares = (
        _to_float(info.get("sharesOutstanding"))
        or _to_float(info.get("impliedSharesOutstanding"))
        or _to_float(info.get("floatShares"))
    )
    operating_margin = None
    if operating_income is not None and revenue not in (None, 0):
        operating_margin = operating_income / revenue

    net_debt = None
    if total_debt is not None or cash is not None:
        net_debt = (total_debt or 0.0) - (cash or 0.0)
    if enterprise_value is None and market_cap is not None and net_debt is not None:
        enterprise_value = market_cap + net_debt

    ev_ebitda = None
    if enterprise_value is not None and ebitda not in (None, 0):
        ev_ebitda = enterprise_value / ebitda
    net_debt_ebitda = None
    if net_debt is not None and ebitda not in (None, 0):
        net_debt_ebitda = net_debt / ebitda
    book_equity = equity
    if book_equity is None and book_value is not None and shares not in (None, 0):
        book_equity = book_value * shares

    revenue_yoy = _yoy_growth(revenue_hist)
    fcf_yoy = _yoy_growth(fcf_hist)

    snapshot = {
        "price": price,
        "market_cap": market_cap,
        "enterprise_value": enterprise_value,
        "shares_outstanding": shares,
        "fifty_two_week_high": fifty_two_high,
        "fifty_two_week_low": fifty_two_low,
        "beta": beta,
        "book_equity": book_equity,
        "book_value_per_share": book_value,
        "ebitda": ebitda,
        "ev_to_ebitda": ev_ebitda,
        "target_mean_price": target_mean,
        "target_high_price": target_high,
        "target_low_price": target_low,
        "recommendation": recommendation,
        "sector": info.get("sector"),
        "industry": info.get("industry"),
    }

    capital_structure = {
        "cash": cash,
        "short_term_debt": st_debt,
        "long_term_debt": lt_debt,
        "total_debt": total_debt,
        "net_debt": net_debt,
        "book_equity": book_equity,
        "ebitda": ebitda,
        "net_debt_to_ebitda": net_debt_ebitda,
        "debt_to_equity": compute_debt_to_equity(total_debt, equity),
    }

    profile = {
        "ticker": ticker.upper(),
        "company_name": info.get("shortName") or info.get("longName"),
        "currency": info.get("currency"),
        "market_cap": market_cap,
        "price": price,
        "shares_outstanding": shares,
        "revenue": revenue,
        "free_cash_flow": fcf,
        "operating_income": operating_income,
        "operating_margin": operating_margin,
        "ebitda": ebitda,
        "snapshot": snapshot,
        "capital_structure": capital_structure,
        "kpi_table": kpi_table,
        "history": {
            "revenue": revenue_hist,
            "free_cash_flow": fcf_hist,
            "operating_income": op_inc_hist,
            "net_income": net_inc_hist,
            "ebitda": ebitda_hist,
            "operating_cash_flow": ocf_hist,
            "capex": capex_hist_abs,
            "long_term_debt": lt_debt_hist,
            "cash": cash_hist,
        },
        "growth": {
            "revenue_cagr": _cagr(revenue_hist),
            "fcf_cagr": _cagr(fcf_hist),
            "revenue_yoy": revenue_yoy,
            "fcf_yoy": fcf_yoy,
            "latest_revenue_yoy": revenue_yoy[0]["rate"] if revenue_yoy else None,
            "latest_fcf_yoy": fcf_yoy[0]["rate"] if fcf_yoy else None,
        },
        "ratios": {
            "roic": compute_roic(ebit, total_debt, equity, cash),
            "fcf_yield": compute_fcf_yield(operating_cf, capex, market_cap),
            "debt_to_equity": compute_debt_to_equity(total_debt, equity),
            "operating_margin": operating_margin,
            "fcf_per_share": (fcf / shares) if fcf is not None and shares not in (None, 0) else None,
            "revenue_per_share": (revenue / shares) if revenue is not None and shares not in (None, 0) else None,
            "ev_to_ebitda": ev_ebitda,
            "net_debt_to_ebitda": net_debt_ebitda,
        },
        "raw_inputs": {
            "ebit": ebit,
            "ebitda": ebitda,
            "total_debt": total_debt,
            "long_term_debt": lt_debt,
            "short_term_debt": st_debt,
            "equity": equity,
            "cash": cash,
            "net_debt": net_debt,
            "operating_cf": operating_cf,
            "capex": capex,
            "enterprise_value": enterprise_value,
        },
        "statements_available": {
            "income_cols": list(income.columns.astype(str)) if isinstance(income, pd.DataFrame) and not income.empty else [],
            "balance_cols": list(balance.columns.astype(str)) if isinstance(balance, pd.DataFrame) and not balance.empty else [],
            "cashflow_cols": list(cashflow.columns.astype(str)) if isinstance(cashflow, pd.DataFrame) and not cashflow.empty else [],
        },
    }
    return profile


def _approx_delta_otm_puts(chain: pd.DataFrame, spot: float, low_pct: float = 0.05, high_pct: float = 0.20) -> pd.DataFrame:
    """Fallback when delta is missing: keep puts roughly 5–20% OTM."""
    if chain.empty or not spot:
        return chain.iloc[0:0]
    otm = chain[(chain["strike"] < spot * (1 - low_pct)) & (chain["strike"] >= spot * (1 - high_pct))]
    return otm.copy()


def _annualized_put_return(premium: float, strike: float, dte: float) -> float | None:
    if strike <= 0 or dte <= 0 or premium is None:
        return None
    return (premium / strike) * (365.0 / dte)


def fetch_put_opportunities(ticker: str, target_dte_low: int = 30, target_dte_high: int = 60) -> dict[str, Any]:
    """
    Near-term put screen for ~10–15% annualized premium in an OTM band.
    Delta filtering is best-effort; yfinance often lacks greeks → % OTM fallback.
    """
    t = yf.Ticker(ticker)
    spot = (t.info or {}).get("currentPrice") or (t.info or {}).get("regularMarketPrice")
    expirations = list(t.options or [])
    if not expirations:
        return {"ticker": ticker.upper(), "spot": spot, "candidates": [], "note": "No options chain available"}

    import datetime as dt

    today = dt.date.today()
    selected_exp = None
    selected_dte = None
    for exp in expirations:
        exp_date = dt.date.fromisoformat(exp)
        dte = (exp_date - today).days
        if target_dte_low <= dte <= target_dte_high:
            selected_exp = exp
            selected_dte = dte
            break

    if selected_exp is None:
        # nearest expiration as fallback
        selected_exp = expirations[0]
        selected_dte = (dt.date.fromisoformat(selected_exp) - today).days

    chain = t.option_chain(selected_exp).puts
    if "impliedVolatility" not in chain.columns:
        chain["impliedVolatility"] = None

    puts = _approx_delta_otm_puts(chain, float(spot or 0))
    candidates: list[dict[str, Any]] = []
    for _, row in puts.iterrows():
        mid = None
        if pd.notna(row.get("bid")) and pd.notna(row.get("ask")):
            mid = (float(row["bid"]) + float(row["ask"])) / 2.0
        elif pd.notna(row.get("lastPrice")):
            mid = float(row["lastPrice"])
        ann = _annualized_put_return(mid or 0.0, float(row["strike"]), float(selected_dte or 1))
        if ann is None:
            continue
        if 0.10 <= ann <= 0.15:
            candidates.append(
                {
                    "expiration": selected_exp,
                    "dte": selected_dte,
                    "strike": float(row["strike"]),
                    "premium_mid": mid,
                    "annualized_return": ann,
                    "iv": float(row["impliedVolatility"]) if pd.notna(row.get("impliedVolatility")) else None,
                }
            )

    from src.iv_store import iv_rank_bundle

    iv_info = iv_rank_bundle(ticker, chain, float(spot or 0))
    notes = ["Delta band approximated via % OTM when greeks are unavailable"]
    notes.extend(iv_info.get("notes") or [])

    return {
        "ticker": ticker.upper(),
        "spot": spot,
        "expiration": selected_exp,
        "dte": selected_dte,
        "candidates": candidates[:25],
        "current_iv": iv_info.get("current_iv"),
        "iv_rank": iv_info.get("iv_rank"),
        "iv_samples": iv_info.get("iv_samples"),
        "iv_low": iv_info.get("iv_low"),
        "iv_high": iv_info.get("iv_high"),
        "hv_rank": iv_info.get("hv_rank"),
        "hv_current": iv_info.get("hv_current"),
        "note": "; ".join(notes),
    }


def run_quant(ticker: str) -> dict[str, Any]:
    try:
        fundamentals = fetch_fundamentals(ticker)
    except Exception as exc:  # noqa: BLE001 — surface soft failure to orchestrator
        logger.exception("Fundamentals failed for %s", ticker)
        fundamentals = {"ticker": ticker.upper(), "error": str(exc)}

    try:
        options = fetch_put_opportunities(ticker)
    except Exception as exc:  # noqa: BLE001
        logger.exception("Options failed for %s", ticker)
        options = {"ticker": ticker.upper(), "error": str(exc), "candidates": []}

    return {"fundamentals": fundamentals, "options": options}


def _fmt_money(val: float | None) -> str:
    if val is None:
        return "—"
    abs_v = abs(val)
    sign = "-" if val < 0 else ""
    if abs_v >= 1e9:
        return f"{sign}${abs_v / 1e9:.2f}B"
    if abs_v >= 1e6:
        return f"{sign}${abs_v / 1e6:.2f}M"
    if abs_v >= 1e3:
        return f"{sign}${abs_v / 1e3:.2f}K"
    return f"{sign}${abs_v:.2f}"


def _fmt_pct(val: float | None) -> str:
    if val is None:
        return "—"
    return f"{val * 100:.1f}%"


def _fmt_multiple(val: float | None, digits: int = 1) -> str:
    if val is None:
        return "—"
    return f"{val:.{digits}f}x"


def _fmt_shares(val: float | None) -> str:
    if val is None:
        return "—"
    if val >= 1e9:
        return f"{val / 1e9:.2f}B"
    if val >= 1e6:
        return f"{val / 1e6:.2f}M"
    return f"{val:,.0f}"


def format_fundamentals_markdown(fund: dict[str, Any], heading: str = "## Fundamentals") -> str:
    """Render richer fundamentals block for reports."""
    if fund.get("error"):
        return f"{heading}\n\n**Fundamentals error:** {fund['error']}\n"

    ratios = fund.get("ratios") or {}
    growth = fund.get("growth") or {}
    history = fund.get("history") or {}
    snap = fund.get("snapshot") or {}
    cap = fund.get("capital_structure") or {}
    lines = [
        heading,
        f"- Company: {fund.get('company_name')}",
        f"- Sector / industry: {snap.get('sector') or '—'} / {snap.get('industry') or '—'}",
        f"- Price: {fund.get('price')}",
        f"- 52-week range: {_fmt_money(_to_float(snap.get('fifty_two_week_low')))} – {_fmt_money(_to_float(snap.get('fifty_two_week_high')))}",
        f"- Market cap: {_fmt_money(_to_float(fund.get('market_cap')))}",
        f"- Enterprise value: {_fmt_money(_to_float(snap.get('enterprise_value')))}",
        f"- Shares outstanding: {_fmt_shares(_to_float(fund.get('shares_outstanding')))}",
        f"- Beta: {snap.get('beta') if snap.get('beta') is not None else '—'}",
        f"- Book equity: {_fmt_money(_to_float(cap.get('book_equity') or snap.get('book_equity')))}",
        f"- Revenue (latest): {_fmt_money(_to_float(fund.get('revenue')))}",
        f"- EBITDA (latest): {_fmt_money(_to_float(fund.get('ebitda')))}",
        f"- Free cash flow (latest): {_fmt_money(_to_float(fund.get('free_cash_flow')))}",
        f"- Operating income: {_fmt_money(_to_float(fund.get('operating_income')))}",
        f"- Operating margin: {_fmt_pct(_to_float(fund.get('operating_margin')))}",
        f"- EV / EBITDA: {_fmt_multiple(_to_float(ratios.get('ev_to_ebitda')))}",
        f"- ROIC: {_fmt_pct(_to_float(ratios.get('roic')))}",
        f"- FCF yield: {_fmt_pct(_to_float(ratios.get('fcf_yield')))}",
        f"- Debt / Equity: {ratios.get('debt_to_equity') if ratios.get('debt_to_equity') is not None else '—'}",
        f"- FCF / share: {_fmt_money(_to_float(ratios.get('fcf_per_share')))}",
        f"- Revenue / share: {_fmt_money(_to_float(ratios.get('revenue_per_share')))}",
        "",
        "### Capital structure",
        f"- Cash: {_fmt_money(_to_float(cap.get('cash')))}",
        f"- Short-term debt: {_fmt_money(_to_float(cap.get('short_term_debt')))}",
        f"- Long-term debt: {_fmt_money(_to_float(cap.get('long_term_debt')))}",
        f"- Total debt: {_fmt_money(_to_float(cap.get('total_debt')))}",
        f"- Net debt: {_fmt_money(_to_float(cap.get('net_debt')))}",
        f"- Net debt / EBITDA: {_fmt_multiple(_to_float(cap.get('net_debt_to_ebitda')))}",
        "",
        "### Growth",
        f"- Revenue CAGR: {_fmt_pct(_to_float(growth.get('revenue_cagr')))}",
        f"- FCF CAGR: {_fmt_pct(_to_float(growth.get('fcf_cagr')))}",
        f"- Latest revenue YoY: {_fmt_pct(_to_float(growth.get('latest_revenue_yoy')))}",
        f"- Latest FCF YoY: {_fmt_pct(_to_float(growth.get('latest_fcf_yoy')))}",
        "",
    ]

    if snap.get("target_mean_price") is not None or snap.get("recommendation") is not None:
        lines += [
            "### Market expectations (yfinance, sparse)",
            f"- Mean target: {_fmt_money(_to_float(snap.get('target_mean_price')))}",
            f"- Target range: {_fmt_money(_to_float(snap.get('target_low_price')))} – {_fmt_money(_to_float(snap.get('target_high_price')))}",
            f"- Recommendation: {snap.get('recommendation') or '—'}",
            "",
            "_Consensus revenue/EBITDA forecasts are often unavailable via free feeds; treat targets as point-in-time only._",
            "",
        ]

    kpi = fund.get("kpi_table") or []
    if kpi:
        lines.append("### Historical KPIs (multi-year)")
        lines.append("")
        lines.append(
            "| Year | Revenue | OCF | Capex | FCF | EBITDA | LT debt | Cash | Net debt | Net income |"
        )
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
        for row in kpi:
            lines.append(
                "| {year} | {rev} | {ocf} | {capex} | {fcf} | {ebitda} | {ltd} | {cash} | {nd} | {ni} |".format(
                    year=row.get("year") or (row.get("period") or "")[:4],
                    rev=_fmt_money(_to_float(row.get("revenue"))),
                    ocf=_fmt_money(_to_float(row.get("operating_cash_flow"))),
                    capex=_fmt_money(_to_float(row.get("capex"))),
                    fcf=_fmt_money(_to_float(row.get("free_cash_flow"))),
                    ebitda=_fmt_money(_to_float(row.get("ebitda"))),
                    ltd=_fmt_money(_to_float(row.get("long_term_debt"))),
                    cash=_fmt_money(_to_float(row.get("cash"))),
                    nd=_fmt_money(_to_float(row.get("net_debt"))),
                    ni=_fmt_money(_to_float(row.get("net_income"))),
                )
            )
        lines.append("")

    rev_hist = history.get("revenue") or []
    if rev_hist and not kpi:
        lines.append("### Revenue history")
        for row in rev_hist:
            lines.append(f"- {row.get('period')}: {_fmt_money(_to_float(row.get('value')))}")
        lines.append("")

    fcf_hist = history.get("free_cash_flow") or []
    if fcf_hist and not kpi:
        lines.append("### Free cash flow history")
        for row in fcf_hist:
            lines.append(f"- {row.get('period')}: {_fmt_money(_to_float(row.get('value')))}")
        lines.append("")

    return "\n".join(lines) + "\n"


def fetch_earnings_history(ticker: str, limit: int = 12) -> dict[str, Any]:
    """
    Earnings surprise vs next-day price move (best-effort via yfinance).
    Missing estimates/prices → rows skipped; never invent consensus.
    """
    import datetime as dt

    t = yf.Ticker(ticker)
    notes: list[str] = []
    rows: list[dict[str, Any]] = []

    try:
        ed = t.get_earnings_dates(limit=max(limit + 4, 16))
    except Exception as exc:  # noqa: BLE001
        logger.warning("earnings dates failed for %s: %s", ticker, exc)
        return {"ticker": ticker.upper(), "rows": [], "notes": [str(exc)], "ok": False}

    if ed is None or (isinstance(ed, pd.DataFrame) and ed.empty):
        return {
            "ticker": ticker.upper(),
            "rows": [],
            "notes": ["No earnings dates available from yfinance"],
            "ok": False,
        }

    df = ed.copy()
    # Columns vary: Earnings Date index, EPS Estimate, Reported EPS, Surprise(%)
    colmap = {c.lower().replace(" ", ""): c for c in df.columns}

    def _col(*names: str) -> str | None:
        for n in names:
            key = n.lower().replace(" ", "")
            if key in colmap:
                return colmap[key]
        return None

    est_c = _col("EPS Estimate", "epsestimate")
    act_c = _col("Reported EPS", "reportedeps", "epsactual")
    sur_c = _col("Surprise(%)", "surprise(%)", "surprise")

    try:
        hist = t.history(period="5y")
    except Exception:  # noqa: BLE001
        hist = pd.DataFrame()

    for idx, row in df.iterrows():
        if len(rows) >= limit:
            break
        try:
            if hasattr(idx, "to_pydatetime"):
                d = idx.to_pydatetime().date()
            elif isinstance(idx, dt.datetime):
                d = idx.date()
            else:
                d = dt.date.fromisoformat(str(idx)[:10])
        except Exception:  # noqa: BLE001
            continue
        est = _to_float(row[est_c]) if est_c else None
        act = _to_float(row[act_c]) if act_c else None
        surprise = None
        if est is not None and act is not None:
            surprise = act - est
        else:
            raw_sur = _to_float(row[sur_c]) if sur_c else None
            # yfinance Surprise(%) is percent points; convert to absolute only if we have estimate
            if raw_sur is not None and est not in (None, 0):
                surprise = est * (raw_sur / 100.0)
            else:
                surprise = raw_sur
        move = None
        if hist is not None and not hist.empty:
            try:
                # Align to trading calendar: close on/after earnings → next close
                idx_dates = hist.index.tz_localize(None) if hist.index.tz is not None else hist.index
                day_ts = pd.Timestamp(d)
                after = hist.loc[idx_dates >= day_ts]
                if len(after) >= 2:
                    c0 = float(after["Close"].iloc[0])
                    c1 = float(after["Close"].iloc[1])
                    if c0:
                        move = (c1 - c0) / c0
            except Exception:  # noqa: BLE001
                move = None
        if act is None and est is None:
            continue
        rows.append(
            {
                "date": d.isoformat(),
                "eps_estimate": est,
                "eps_actual": act,
                "eps_surprise": surprise,
                "one_day_move": move,
            }
        )

    # Soft correlation EPS surprise vs move
    corr = None
    pairs = [
        (r["eps_surprise"], r["one_day_move"])
        for r in rows
        if r.get("eps_surprise") is not None and r.get("one_day_move") is not None
    ]
    if len(pairs) >= 5:
        from src.drivers import pearson_corr

        xs = [p[0] for p in pairs]
        ys = [p[1] for p in pairs]
        corr = pearson_corr(xs, ys)
        notes.append(
            f"EPS surprise vs 1-day move Pearson r={corr.get('r')} (n={corr.get('n')}, p≈{corr.get('p')}); "
            "treat as suggestive only."
        )
    else:
        notes.append("Insufficient paired earnings/move observations for correlation.")

    next_earn = None
    try:
        cal = t.calendar
        if isinstance(cal, dict):
            ne = cal.get("Earnings Date") or cal.get("EarningsDate")
            if isinstance(ne, (list, tuple)) and ne:
                next_earn = str(ne[0])[:10]
            elif ne is not None:
                next_earn = str(ne)[:10]
        elif isinstance(cal, pd.DataFrame) and not cal.empty:
            next_earn = str(cal.values.flatten()[0])[:10]
    except Exception:  # noqa: BLE001
        pass

    return {
        "ticker": ticker.upper(),
        "rows": rows,
        "correlation": corr,
        "next_earnings": next_earn,
        "notes": notes,
        "ok": bool(rows),
    }


def format_earnings_markdown(earnings: dict[str, Any]) -> str:
    lines = ["## Earnings, guidance & revision catalysts", ""]
    if earnings.get("next_earnings"):
        lines.append(f"- Next earnings (calendar): {earnings.get('next_earnings')}")
        lines.append("")
    rows = earnings.get("rows") or []
    if not rows:
        lines.append("_No earnings surprise history available from yfinance._")
        lines.append("")
        for n in earnings.get("notes") or []:
            lines.append(f"- {n}")
        return "\n".join(lines) + "\n"

    lines.append("| Date | EPS est | EPS actual | Surprise | 1-day move |")
    lines.append("|---|---:|---:|---:|---:|")
    for r in rows[:12]:
        sur = r.get("eps_surprise")
        move = r.get("one_day_move")
        lines.append(
            "| {d} | {e} | {a} | {s} | {m} |".format(
                d=r.get("date"),
                e=f"{r['eps_estimate']:.2f}" if r.get("eps_estimate") is not None else "—",
                a=f"{r['eps_actual']:.2f}" if r.get("eps_actual") is not None else "—",
                s=f"{sur:.2f}" if sur is not None else "—",
                m=f"{move * 100:.1f}%" if move is not None else "—",
            )
        )
    lines.append("")
    for n in earnings.get("notes") or []:
        lines.append(f"_{n}_")
    lines.append("")
    lines.append(
        "_Guidance vs Street and adjusted EBITDA are often missing from free feeds; "
        "use web/SEC sections for narrative guidance._"
    )
    lines.append("")
    return "\n".join(lines) + "\n"

