"""Optional phone / desktop push via ntfy.sh."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Optional, Sequence

import requests

from src.config import ROOT_DIR

logger = logging.getLogger(__name__)


def send_ntfy(
    *,
    title: str,
    message: str,
    priority: int = 4,
    tags: Optional[str] = None,
    click: Optional[str] = None,
    actions: Optional[str] = None,
) -> bool:
    topic = (os.getenv("NTFY_TOPIC") or "").strip()
    if not topic:
        logger.debug("ntfy skipped: NTFY_TOPIC not set")
        return False
    server = (os.getenv("NTFY_SERVER") or "https://ntfy.sh").rstrip("/")
    headers = {
        "Title": title[:200],
        "Priority": str(max(1, min(int(priority), 5))),
    }
    if tags:
        headers["Tags"] = tags
    if click:
        headers["Click"] = click
    if actions:
        headers["Actions"] = actions
    token = (os.getenv("NTFY_TOKEN") or "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        resp = requests.post(
            f"{server}/{topic}",
            data=message.encode("utf-8"),
            headers=headers,
            timeout=8,
        )
        resp.raise_for_status()
        return True
    except Exception:  # noqa: BLE001
        logger.exception("ntfy publish failed")
        return False


def build_http_actions(actions: Sequence[tuple[str, str]]) -> str:
    parts: list[str] = []
    for label, target in actions:
        label = (label or "").replace(",", " ").strip() or "Action"
        target = (target or "").strip()
        if not target:
            continue
        parts.append(f"http, {label}, {target}, method=POST, clear=true")
    return "; ".join(parts)


def resolve_public_base_url(default: str = "http://127.0.0.1:8000") -> str:
    configured = (os.getenv("QUEUE_PUBLIC_BASE_URL") or os.getenv("PUBLIC_BASE_URL") or "").strip().rstrip("/")
    if configured:
        return configured
    tunnel = ROOT_DIR / "data" / "tunnel_url.txt"
    try:
        if tunnel.is_file():
            url = tunnel.read_text(encoding="utf-8").strip().rstrip("/")
            if url.startswith("http"):
                return url
    except OSError:
        pass
    return default.rstrip("/")
