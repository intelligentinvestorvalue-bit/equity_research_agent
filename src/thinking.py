"""Thinking / research-loop event helpers."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Callable


ThinkCb = Callable[[str, str], None]  # kind, message


def _noop_think(kind: str, message: str) -> None:
    return None


def thought_event(kind: str, message: str, **extra: Any) -> dict[str, Any]:
    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "kind": kind,  # think | act | gap | done
        "message": message,
        **extra,
    }
