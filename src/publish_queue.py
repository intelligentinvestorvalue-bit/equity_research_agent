"""Request a debounced git publish of data/sync + docs/ after research exports.

The local scheduled task (scripts/publish_sync.ps1) picks up the flag and
rebuilds GitHub Pages + pushes — no manual commit needed.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parents[1]
FLAG_PATH = ROOT_DIR / "data" / "publish_requested"


def request_publish(reason: str = "") -> None:
    """Mark that sync artifacts should be pushed (idempotent / debounced)."""
    try:
        FLAG_PATH.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).isoformat()
        line = f"{stamp}\t{reason}".strip() + "\n"
        FLAG_PATH.write_text(line, encoding="utf-8")
        logger.info("Publish requested (%s)", reason or "sync")
    except OSError as exc:
        logger.warning("Could not write publish flag: %s", exc)


def clear_publish_request() -> None:
    try:
        if FLAG_PATH.exists():
            FLAG_PATH.unlink()
    except OSError as exc:
        logger.warning("Could not clear publish flag: %s", exc)


def publish_requested() -> bool:
    return FLAG_PATH.exists()
