"""Quantitative fundamentals and options aggregator (Module A)."""

from __future__ import annotations

import logging
from typing import Any

import pandas as pd
import yfinance as yf

logger = logging.getLogger(__name__)


def _safe_get(series_or_df: Any, *keys: str) -> float | None:
    """Pull first available numeric field from a yfinance statement frame."""
    if series_or_df is None:
        return None
    frame = series_or_df
    if isinstance(frame, pd.DataFrame):
        if frame.empty:
            return None
        col = frame.columns[0]
        for key in keys:
            if key in frame.index:
                val = frame.loc[key, col]
                try:
                    return float(val)
                except (TypeError, ValueError):
                    return None
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


def fetch_fundamentals(ticker: str) -> dict[str, Any]:
    """Pull ~4 years of statements and derived ratios via yfinance."""
    t = yf.Ticker(ticker)
    info = t.info or {}
    income = t.financials
    balance = t.balance_sheet
    cashflow = t.cashflow

    ebit = _safe_get(income, "EBIT", "Operating Income")
    total_debt = _safe_get(balance, "Total Debt", "Long Term Debt")
    equity = _safe_get(balance, "Stockholders Equity", "Total Stockholder Equity", "Common Stock Equity")
    cash = _safe_get(balance, "Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments")
    operating_cf = _safe_get(cashflow, "Operating Cash Flow", "Total Cash From Operating Activities")
    capex = _safe_get(cashflow, "Capital Expenditure", "Capital Expenditures")
    market_cap = info.get("marketCap")

    profile = {
        "ticker": ticker.upper(),
        "company_name": info.get("shortName") or info.get("longName"),
        "currency": info.get("currency"),
        "market_cap": market_cap,
        "price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "ratios": {
            "roic": compute_roic(ebit, total_debt, equity, cash),
            "fcf_yield": compute_fcf_yield(operating_cf, capex, market_cap),
            "debt_to_equity": compute_debt_to_equity(total_debt, equity),
        },
        "raw_inputs": {
            "ebit": ebit,
            "total_debt": total_debt,
            "equity": equity,
            "cash": cash,
            "operating_cf": operating_cf,
            "capex": capex,
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

    return {
        "ticker": ticker.upper(),
        "spot": spot,
        "expiration": selected_exp,
        "dte": selected_dte,
        "candidates": candidates[:25],
        "iv_rank": None,  # requires historical IV archive; filled in later phases
        "note": "Delta band approximated via % OTM when greeks are unavailable",
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
