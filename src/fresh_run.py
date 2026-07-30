"""Clear local caches so a ticker can be researched from scratch."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from src.config import FILINGS_DIR, OUTPUT_DIR

logger = logging.getLogger(__name__)


def clear_ticker_cache(ticker: str) -> dict[str, Any]:
    """
    Remove cached SEC extracts and local output artifacts for a ticker.

    Does not delete SQLite job history or data/sync packs — those remain as
    prior runs. The next research job re-downloads the 10-K and regenerates
    reports/charts.
    """
    ticker = (ticker or "").upper().strip()
    if not ticker:
        return {"ticker": "", "removed": [], "count": 0}

    removed: list[str] = []
    patterns = [
        FILINGS_DIR.glob(f"{ticker}_*"),
        OUTPUT_DIR.glob(f"{ticker}_*"),
        (OUTPUT_DIR / "charts").glob(f"{ticker}_*"),
    ]
    for group in patterns:
        for path in group:
            try:
                if path.is_file():
                    path.unlink()
                    removed.append(str(path))
            except OSError as exc:
                logger.warning("Could not remove %s: %s", path, exc)

    logger.info("Cleared %s cache file(s) for %s", len(removed), ticker)
    return {"ticker": ticker, "removed": removed, "count": len(removed)}
