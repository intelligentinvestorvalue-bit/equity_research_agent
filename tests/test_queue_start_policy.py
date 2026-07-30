"""Tests for queue start_policy hold / defer / overnight."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import src.db as db_mod
from src.research_queue import ResearchQueueStore


def _fresh_store(tmp_path, monkeypatch):
    db_path = tmp_path / "queue_test.db"
    monkeypatch.setattr(db_mod, "DB_PATH", db_path)
    return ResearchQueueStore()


def test_prompt_now_hold_then_release(tmp_path, monkeypatch):
    store = _fresh_store(tmp_path, monkeypatch)
    result = store.add_tickers(
        "HOLDT1",
        template="all",
        skip_existing=False,
        start_policy="prompt_now",
        confirm_seconds=60,
    )
    assert len(result["created"]) == 1
    item = result["created"][0]
    assert item.hold_until is not None
    assert item.deferred is False
    assert store.claim_next() is None  # still holding

    past = (datetime.now(timezone.utc) - timedelta(seconds=5)).isoformat()
    with store._lock:
        conn = db_mod.connect()
        try:
            conn.execute(
                "UPDATE research_queue SET hold_until=? WHERE id=?",
                (past, item.id),
            )
            conn.commit()
        finally:
            conn.close()
    assert store.release_holds_due() >= 1
    claimed = store.claim_next()
    assert claimed is not None
    assert claimed.ticker == "HOLDT1"


def test_overnight_deferred_until_start(tmp_path, monkeypatch):
    store = _fresh_store(tmp_path, monkeypatch)
    result = store.add_tickers(
        "OVNT1",
        template="memo",
        skip_existing=False,
        start_policy="overnight",
    )
    item = result["created"][0]
    assert item.deferred is True
    assert store.claim_next() is None
    assert store.start_overnight() >= 1
    claimed = store.claim_next()
    assert claimed is not None
    assert claimed.ticker == "OVNT1"


def test_defer_and_remove(tmp_path, monkeypatch):
    store = _fresh_store(tmp_path, monkeypatch)
    result = store.add_tickers(
        "DEFR1",
        skip_existing=False,
        start_policy="prompt_now",
        confirm_seconds=30,
    )
    item = result["created"][0]
    deferred = store.defer_to_overnight(item.id)
    assert deferred is not None
    assert deferred.deferred is True
    assert store.claim_next() is None
    assert store.remove_ticker("DEFR1") >= 1
