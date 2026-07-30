"""Notify laptop when queue items are waiting for start confirmation."""

from __future__ import annotations

import logging
import os
from typing import Iterable

from src.ntfy import build_http_actions, resolve_public_base_url, send_ntfy
from src.research_queue import QueueItem

logger = logging.getLogger(__name__)


def notify_prompt_now(items: Iterable[QueueItem], *, confirm_seconds: int = 60) -> None:
    items = [i for i in items if i.start_policy == "prompt_now"]
    if not items:
        return
    if os.getenv("QUEUE_NTFY_ENABLED", "1").strip().lower() in {"0", "false", "no", "off"}:
        return

    base = resolve_public_base_url()
    tickers = ", ".join(i.ticker for i in items[:8])
    extra = f" (+{len(items) - 8} more)" if len(items) > 8 else ""
    # Actions on the first item (batch starts together via worker)
    first = items[0]
    actions = build_http_actions(
        [
            ("Start now", f"{base}/api/queue/{first.id}/start-now"),
            ("Overnight instead", f"{base}/api/queue/{first.id}/defer"),
        ]
    )
    # If multiple, also offer start-all / defer-all
    if len(items) > 1:
        actions = build_http_actions(
            [
                ("Start queue now", f"{base}/api/queue/start-now"),
                ("Keep overnight", f"{base}/api/queue/defer-pending-prompts"),
            ]
        )

    send_ntfy(
        title="Equity queue — start deep dive?",
        message=(
            f"{tickers}{extra} added. Auto-starts in ~{confirm_seconds}s. "
            f"Tap Start now, or Overnight to wait for overnight/manual start. "
            f"No browser needed."
        ),
        priority=4,
        tags="hourglass_flowing_sand,chart_with_upwards_trend",
        click=f"{base}/queue",
        actions=actions,
    )
    logger.info("Queue start prompt ntfy sent for %s", tickers)
