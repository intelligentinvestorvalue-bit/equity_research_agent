"""Tests for ticker coverage / skip logic."""

from __future__ import annotations

from src.ticker_status import ticker_status


def test_ticker_status_empty_unknown():
    status = ticker_status("ZZZZNOPE999")
    assert status["ticker"] == "ZZZZNOPE999"
    assert status["queued_or_active"] is False
    assert status["in_overnight_queue"] is False
    # May or may not have research depending on local DB; should_skip only if covered
    assert "should_skip" in status
    assert "has_research" in status


def test_add_tickers_skips_duplicate_queue(tmp_path, monkeypatch):
    monkeypatch.setenv("SEC_USER_AGENT", "EquityTest test@example.com")
    # Use isolated DB if possible — research_queue shares default DB; still verify API shape.
    from src.research_queue import ResearchQueueStore

    store = ResearchQueueStore()
    first = store.add_tickers("TSTDQ1", template="all", skip_existing=False)
    assert len(first["created"]) == 1
    second = store.add_tickers("TSTDQ1", template="all", skip_existing=True)
    assert second["created"] == []
    assert second["skipped"]
    assert second["skipped"][0]["ticker"] == "TSTDQ1"
