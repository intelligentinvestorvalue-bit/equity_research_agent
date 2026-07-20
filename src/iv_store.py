"""Local IV history cache and IV / HV rank helpers."""

from __future__ import annotations

import logging
import math
from datetime import date, datetime, timezone
from typing import Any

import pandas as pd

from src.db import connect

logger = logging.getLogger(__name__)


def _init_iv_table() -> None:
    conn = connect()
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS iv_daily (
                ticker TEXT NOT NULL,
                asof TEXT NOT NULL,
                iv REAL NOT NULL,
                source TEXT DEFAULT 'chain_atm',
                PRIMARY KEY (ticker, asof)
            )
            """
        )
        conn.execute("CREATE INDEX IF NOT EXISTS idx_iv_ticker_asof ON iv_daily(ticker, asof DESC)")
        conn.commit()
    finally:
        conn.close()


_init_iv_table()


def _today() -> str:
    return date.today().isoformat()


def record_iv(ticker: str, iv: float, asof: str | None = None, source: str = "chain_atm") -> None:
    if iv is None or not math.isfinite(iv) or iv <= 0:
        return
    ticker = ticker.upper().strip()
    asof = asof or _today()
    conn = connect()
    try:
        conn.execute(
            """
            INSERT INTO iv_daily (ticker, asof, iv, source) VALUES (?, ?, ?, ?)
            ON CONFLICT(ticker, asof) DO UPDATE SET iv = excluded.iv, source = excluded.source
            """,
            (ticker, asof, float(iv), source),
        )
        conn.commit()
    finally:
        conn.close()


def load_iv_history(ticker: str, lookback_days: int = 365) -> list[dict[str, Any]]:
    ticker = ticker.upper().strip()
    conn = connect()
    try:
        rows = conn.execute(
            """
            SELECT asof, iv, source FROM iv_daily
            WHERE ticker = ?
            ORDER BY asof DESC
            LIMIT ?
            """,
            (ticker, max(lookback_days, 30)),
        ).fetchall()
        return [{"asof": r["asof"], "iv": float(r["iv"]), "source": r["source"]} for r in rows]
    finally:
        conn.close()


def compute_rank(current: float, series: list[float]) -> float | None:
    """Percentile rank of current within [min, max] of series (inclusive)."""
    vals = [v for v in series if v is not None and math.isfinite(v)]
    if current is None or not math.isfinite(current) or len(vals) < 5:
        return None
    lo, hi = min(vals), max(vals)
    if hi <= lo:
        return 0.5
    return max(0.0, min(1.0, (current - lo) / (hi - lo)))


def atm_iv_from_puts(chain: pd.DataFrame, spot: float) -> float | None:
    """Median IV of puts nearest ATM (within ~10% of spot)."""
    if chain is None or chain.empty or not spot:
        return None
    if "impliedVolatility" not in chain.columns or "strike" not in chain.columns:
        return None
    band = chain[
        (chain["strike"] >= spot * 0.90)
        & (chain["strike"] <= spot * 1.05)
        & chain["impliedVolatility"].notna()
    ]
    if band.empty:
        # fall back to closest 5 strikes by distance to spot
        tmp = chain.dropna(subset=["impliedVolatility"]).copy()
        if tmp.empty:
            return None
        tmp["dist"] = (tmp["strike"] - spot).abs()
        band = tmp.nsmallest(5, "dist")
    try:
        return float(band["impliedVolatility"].median())
    except (TypeError, ValueError):
        return None


def realized_vol_rank(ticker: str, window: int = 20, lookback_days: int = 252) -> dict[str, Any]:
    """
    HV rank: where today's N-day realized vol sits vs ~1y history of that HV.
    Useful proxy when local IV history is thin.
    """
    import yfinance as yf

    try:
        hist = yf.Ticker(ticker).history(period="2y")
    except Exception as exc:  # noqa: BLE001
        return {"hv_rank": None, "hv_current": None, "error": str(exc)}
    if hist is None or hist.empty or "Close" not in hist.columns:
        return {"hv_rank": None, "hv_current": None, "error": "no price history"}

    close = hist["Close"].dropna()
    if len(close) < window + 5:
        return {"hv_rank": None, "hv_current": None, "error": "insufficient history"}

    log_ret = (close / close.shift(1)).apply(lambda x: math.log(x) if x and x > 0 else float("nan"))
    hv = log_ret.rolling(window).std() * math.sqrt(252.0)
    hv = hv.dropna()
    if hv.empty:
        return {"hv_rank": None, "hv_current": None, "error": "hv empty"}

    series = hv.tail(lookback_days).tolist()
    current = float(series[-1])
    rank = compute_rank(current, series)
    return {
        "hv_rank": rank,
        "hv_current": current,
        "hv_window": window,
        "hv_samples": len(series),
        "hv_low": min(series) if series else None,
        "hv_high": max(series) if series else None,
    }


def iv_rank_bundle(
    ticker: str,
    chain: pd.DataFrame,
    spot: float,
    *,
    min_iv_samples: int = 20,
) -> dict[str, Any]:
    """
    Record today's ATM IV, compute IV rank from local cache when possible,
    and always attempt HV rank as a complementary / fallback metric.
    """
    ticker = ticker.upper().strip()
    current_iv = atm_iv_from_puts(chain, float(spot or 0))
    if current_iv is not None:
        record_iv(ticker, current_iv)

    history = load_iv_history(ticker, lookback_days=400)
    iv_series = [h["iv"] for h in history]
    # Ensure current is in series for rank calc
    if current_iv is not None and (not iv_series or abs(iv_series[0] - current_iv) > 1e-9):
        iv_series = [current_iv] + iv_series

    iv_rank = compute_rank(current_iv, iv_series) if current_iv is not None and len(iv_series) >= min_iv_samples else None
    hv = realized_vol_rank(ticker)

    notes = []
    if current_iv is None:
        notes.append("Could not estimate ATM IV from the option chain.")
    if iv_rank is None:
        notes.append(
            f"IV rank needs ~{min_iv_samples}+ local daily IV samples "
            f"(have {len(history)}); run the options screen over time to build history."
        )
    if hv.get("hv_rank") is not None:
        notes.append("HV rank is realized-vol rank (20d HV vs ~1y); useful when IV history is thin.")

    return {
        "current_iv": current_iv,
        "iv_rank": iv_rank,
        "iv_samples": len(history),
        "iv_low": min(iv_series) if len(iv_series) >= 2 else None,
        "iv_high": max(iv_series) if len(iv_series) >= 2 else None,
        "hv_rank": hv.get("hv_rank"),
        "hv_current": hv.get("hv_current"),
        "hv_samples": hv.get("hv_samples"),
        "asof": _today(),
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "notes": notes,
    }
