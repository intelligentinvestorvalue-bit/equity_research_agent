"""Persistent multi-ticker research queue (run one after another overnight)."""

from __future__ import annotations

import logging
import threading
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

from src.db import connect

logger = logging.getLogger(__name__)

StartJobFn = Callable[..., str]  # returns job_id


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_tickers(raw: str) -> list[str]:
    """Accept newlines, commas, spaces, or mixed lists."""
    text = (raw or "").upper().replace(",", " ").replace(";", " ").replace("\t", " ")
    out: list[str] = []
    seen: set[str] = set()
    for part in text.replace("\n", " ").split():
        t = "".join(ch for ch in part if ch.isalnum() or ch in {".", "-"})
        t = t.strip(".-")
        if not t or len(t) > 12:
            continue
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


@dataclass
class QueueItem:
    id: str
    ticker: str
    template: str = "memo"
    mode: str = "deep"
    goal: str = ""
    from_scratch: bool = False
    status: str = "pending"  # pending | running | completed | failed | cancelled
    position: int = 0
    job_id: str | None = None
    error: str | None = None
    created_at: str = field(default_factory=_now)
    started_at: str | None = None
    finished_at: str | None = None
    # prompt_now: notify laptop, auto-start after hold_until unless deferred
    # overnight: stay pending until Start overnight / resume deferred
    start_policy: str = "prompt_now"
    hold_until: str | None = None
    deferred: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "ticker": self.ticker,
            "template": self.template,
            "mode": self.mode,
            "goal": self.goal,
            "from_scratch": self.from_scratch,
            "status": self.status,
            "position": self.position,
            "job_id": self.job_id,
            "error": self.error,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "job_href": f"/jobs/{self.job_id}" if self.job_id else None,
            "start_policy": self.start_policy,
            "hold_until": self.hold_until,
            "deferred": bool(self.deferred),
        }


def _row_val(row: Any, key: str, default: Any = None) -> Any:
    try:
        return row[key]
    except (KeyError, IndexError):
        return default


def _row_to_item(row: Any) -> QueueItem:
    return QueueItem(
        id=row["id"],
        ticker=row["ticker"],
        template=row["template"] or "memo",
        mode=row["mode"] or "deep",
        goal=row["goal"] or "",
        from_scratch=bool(row["from_scratch"]),
        status=row["status"],
        position=int(row["position"] or 0),
        job_id=row["job_id"],
        error=row["error"],
        created_at=row["created_at"],
        started_at=row["started_at"],
        finished_at=row["finished_at"],
        start_policy=(_row_val(row, "start_policy") or "prompt_now"),
        hold_until=_row_val(row, "hold_until"),
        deferred=bool(_row_val(row, "deferred") or 0),
    )


class ResearchQueueStore:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._init_db()

    def _init_db(self) -> None:
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS research_queue (
                        id TEXT PRIMARY KEY,
                        ticker TEXT NOT NULL,
                        template TEXT DEFAULT 'memo',
                        mode TEXT DEFAULT 'deep',
                        goal TEXT DEFAULT '',
                        from_scratch INTEGER DEFAULT 0,
                        status TEXT NOT NULL,
                        position INTEGER DEFAULT 0,
                        job_id TEXT,
                        error TEXT,
                        created_at TEXT NOT NULL,
                        started_at TEXT,
                        finished_at TEXT
                    )
                    """
                )
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS research_queue_meta (
                        key TEXT PRIMARY KEY,
                        value TEXT NOT NULL
                    )
                    """
                )
                conn.execute(
                    "CREATE INDEX IF NOT EXISTS idx_rq_status_pos ON research_queue(status, position, created_at)"
                )
                # Default paused=0 (running)
                conn.execute(
                    "INSERT OR IGNORE INTO research_queue_meta(key, value) VALUES ('paused', '0')"
                )
                # Lightweight column ensure (no Alembic)
                cols = {r[1] for r in conn.execute("PRAGMA table_info(research_queue)").fetchall()}
                if "start_policy" not in cols:
                    conn.execute(
                        "ALTER TABLE research_queue ADD COLUMN start_policy TEXT DEFAULT 'prompt_now'"
                    )
                if "hold_until" not in cols:
                    conn.execute("ALTER TABLE research_queue ADD COLUMN hold_until TEXT")
                if "deferred" not in cols:
                    conn.execute(
                        "ALTER TABLE research_queue ADD COLUMN deferred INTEGER DEFAULT 0"
                    )
                conn.commit()
            finally:
                conn.close()

    def get_paused(self) -> bool:
        with self._lock:
            conn = connect()
            try:
                row = conn.execute(
                    "SELECT value FROM research_queue_meta WHERE key='paused'"
                ).fetchone()
                return bool(row and row["value"] in {"1", "true", "yes"})
            finally:
                conn.close()

    def set_paused(self, paused: bool) -> None:
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    "INSERT INTO research_queue_meta(key, value) VALUES ('paused', ?) "
                    "ON CONFLICT(key) DO UPDATE SET value=excluded.value",
                    ("1" if paused else "0",),
                )
                conn.commit()
            finally:
                conn.close()

    def _next_position(self, conn: Any) -> int:
        row = conn.execute("SELECT COALESCE(MAX(position), 0) AS m FROM research_queue").fetchone()
        return int(row["m"] or 0) + 1

    def add_tickers(
        self,
        tickers: list[str] | str,
        *,
        template: str = "memo",
        mode: str = "deep",
        goal: str = "",
        from_scratch: bool = False,
        skip_existing: bool = True,
        start_policy: str = "prompt_now",
        confirm_seconds: int = 60,
    ) -> dict[str, Any]:
        """Enqueue tickers. Returns created items and skip reasons.

        start_policy:
          - prompt_now: hold for confirm_seconds, ntfy laptop, then auto-start
            unless deferred to overnight
          - overnight: stay pending/deferred until Start overnight / resume

        When skip_existing is True (default), tickers already pending/running in
        the overnight queue, already running as jobs, or already researched
        (completed job / sync reports / local output) are skipped — unless
        from_scratch is True (then only active queue/job duplicates are skipped).
        """
        if isinstance(tickers, str):
            tickers = _parse_tickers(tickers)
        else:
            tickers = _parse_tickers(" ".join(tickers))
        if not tickers:
            return {"created": [], "skipped": []}

        template = (template or "memo").strip().lower()
        mode = "fast" if mode == "fast" else "deep"
        policy = (start_policy or "prompt_now").strip().lower()
        if policy not in {"prompt_now", "overnight"}:
            policy = "prompt_now"
        hold_seconds = max(0, int(confirm_seconds))
        created: list[QueueItem] = []
        skipped: list[dict[str, str]] = []

        from src.ticker_status import ticker_status

        accepted: list[str] = []
        for ticker in tickers:
            if skip_existing:
                status = ticker_status(ticker)
                if status.get("in_overnight_queue") or status.get("queued_or_active"):
                    skipped.append(
                        {
                            "ticker": ticker,
                            "reason": status.get("skip_reason") or "already active",
                        }
                    )
                    continue
                if not from_scratch and status.get("has_research"):
                    skipped.append(
                        {
                            "ticker": ticker,
                            "reason": status.get("skip_reason") or "already researched",
                        }
                    )
                    continue
            accepted.append(ticker)

        if not accepted:
            return {"created": created, "skipped": skipped}

        with self._lock:
            conn = connect()
            try:
                for ticker in accepted:
                    # Re-check active queue under lock to avoid races.
                    if skip_existing:
                        row = conn.execute(
                            "SELECT id, status FROM research_queue "
                            "WHERE UPPER(ticker)=? AND status IN ('pending','running') LIMIT 1",
                            (ticker,),
                        ).fetchone()
                        if row:
                            skipped.append(
                                {
                                    "ticker": ticker,
                                    "reason": f"already in overnight queue ({row['status']})",
                                }
                            )
                            continue
                    pos = self._next_position(conn)
                    hold_until = None
                    deferred = 0
                    if policy == "prompt_now" and hold_seconds > 0:
                        from datetime import timedelta

                        hold_until = (
                            datetime.now(timezone.utc) + timedelta(seconds=hold_seconds)
                        ).isoformat()
                    elif policy == "overnight":
                        deferred = 1

                    item = QueueItem(
                        id=str(uuid.uuid4()),
                        ticker=ticker,
                        template=template,
                        mode=mode,
                        goal=goal or "",
                        from_scratch=from_scratch,
                        status="pending",
                        position=pos,
                        start_policy=policy,
                        hold_until=hold_until,
                        deferred=bool(deferred),
                    )
                    conn.execute(
                        """
                        INSERT INTO research_queue (
                            id, ticker, template, mode, goal, from_scratch, status, position,
                            job_id, error, created_at, started_at, finished_at,
                            start_policy, hold_until, deferred
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, ?, NULL, NULL, ?, ?, ?)
                        """,
                        (
                            item.id,
                            item.ticker,
                            item.template,
                            item.mode,
                            item.goal,
                            1 if item.from_scratch else 0,
                            item.status,
                            item.position,
                            item.created_at,
                            item.start_policy,
                            item.hold_until,
                            1 if item.deferred else 0,
                        ),
                    )
                    created.append(item)
                conn.commit()
            finally:
                conn.close()
        return {"created": created, "skipped": skipped}

    def list_items(self, *, limit: int = 200, include_done: bool = True) -> list[QueueItem]:
        with self._lock:
            conn = connect()
            try:
                if not include_done:
                    rows = conn.execute(
                        "SELECT * FROM research_queue WHERE status IN ('pending','running') "
                        "ORDER BY position ASC, created_at ASC LIMIT ?",
                        (limit,),
                    ).fetchall()
                    return [_row_to_item(r) for r in rows]

                # Always include active rows first so a long finished history cannot hide pending.
                active = conn.execute(
                    "SELECT * FROM research_queue WHERE status IN ('pending','running') "
                    "ORDER BY position ASC, created_at ASC"
                ).fetchall()
                remain = max(0, limit - len(active))
                done = []
                if remain:
                    done = conn.execute(
                        "SELECT * FROM research_queue WHERE status NOT IN ('pending','running') "
                        "ORDER BY position ASC, created_at ASC LIMIT ?",
                        (remain,),
                    ).fetchall()
                # Active first (by position), then finished
                return [_row_to_item(r) for r in list(active) + list(done)]
            finally:
                conn.close()

    def get(self, item_id: str) -> QueueItem | None:
        with self._lock:
            conn = connect()
            try:
                row = conn.execute(
                    "SELECT * FROM research_queue WHERE id=?", (item_id,)
                ).fetchone()
                return _row_to_item(row) if row else None
            finally:
                conn.close()

    def summary(self) -> dict[str, Any]:
        with self._lock:
            conn = connect()
            try:
                rows = conn.execute(
                    "SELECT status, COUNT(*) AS n FROM research_queue GROUP BY status"
                ).fetchall()
                counts = {r["status"]: int(r["n"]) for r in rows}
                return {
                    "paused": self.get_paused(),
                    "pending": counts.get("pending", 0),
                    "running": counts.get("running", 0),
                    "completed": counts.get("completed", 0),
                    "failed": counts.get("failed", 0),
                    "cancelled": counts.get("cancelled", 0),
                    "total": sum(counts.values()),
                }
            finally:
                conn.close()

    def claim_next(self) -> QueueItem | None:
        """Atomically mark the next eligible pending item as running and return it."""
        with self._lock:
            if self.get_paused():
                return None
            conn = connect()
            try:
                now = _now()
                row = conn.execute(
                    """
                    SELECT * FROM research_queue
                    WHERE status='pending'
                      AND COALESCE(deferred, 0)=0
                      AND (hold_until IS NULL OR hold_until <= ?)
                    ORDER BY position ASC, created_at ASC
                    LIMIT 1
                    """,
                    (now,),
                ).fetchone()
                if not row:
                    return None
                started = now
                conn.execute(
                    "UPDATE research_queue SET status='running', started_at=?, error=NULL, "
                    "hold_until=NULL WHERE id=?",
                    (started, row["id"]),
                )
                conn.commit()
                item = _row_to_item(row)
                item.status = "running"
                item.started_at = started
                item.hold_until = None
                return item
            finally:
                conn.close()

    def release_holds_due(self) -> int:
        """Clear expired hold_until on non-deferred pending items so worker can claim them."""
        with self._lock:
            conn = connect()
            try:
                now = _now()
                cur = conn.execute(
                    """
                    UPDATE research_queue
                    SET hold_until=NULL
                    WHERE status='pending'
                      AND COALESCE(deferred, 0)=0
                      AND hold_until IS NOT NULL
                      AND hold_until <= ?
                    """,
                    (now,),
                )
                conn.commit()
                return cur.rowcount
            finally:
                conn.close()

    def confirm_start_now(self, item_id: str) -> QueueItem | None:
        """User confirmed: clear hold/deferred and make immediately runnable."""
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    "UPDATE research_queue SET hold_until=NULL, deferred=0, "
                    "start_policy='prompt_now' WHERE id=? AND status='pending'",
                    (item_id,),
                )
                conn.commit()
                row = conn.execute(
                    "SELECT * FROM research_queue WHERE id=?", (item_id,)
                ).fetchone()
                return _row_to_item(row) if row else None
            finally:
                conn.close()

    def defer_to_overnight(self, item_id: str) -> QueueItem | None:
        """Cancel immediate start — keep in overnight queue until manual/overnight start."""
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    "UPDATE research_queue SET deferred=1, hold_until=NULL, "
                    "start_policy='overnight', "
                    "error='Deferred to overnight queue' "
                    "WHERE id=? AND status='pending'",
                    (item_id,),
                )
                conn.commit()
                row = conn.execute(
                    "SELECT * FROM research_queue WHERE id=?", (item_id,)
                ).fetchone()
                return _row_to_item(row) if row else None
            finally:
                conn.close()

    def start_overnight(self) -> int:
        """Make all deferred/overnight pending items eligible and clear holds."""
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    """
                    UPDATE research_queue
                    SET deferred=0, hold_until=NULL, error=NULL
                    WHERE status='pending' AND (
                        COALESCE(deferred, 0)=1 OR start_policy='overnight'
                    )
                    """
                )
                conn.commit()
                return cur.rowcount
            finally:
                conn.close()

    def remove_ticker(self, ticker: str) -> int:
        """Cancel pending items for a ticker (remove from overnight queue)."""
        t = (ticker or "").upper().strip()
        if not t:
            return 0
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    "UPDATE research_queue SET status='cancelled', finished_at=?, "
                    "error='Removed from queue' "
                    "WHERE UPPER(ticker)=? AND status='pending'",
                    (_now(), t),
                )
                conn.commit()
                return cur.rowcount
            finally:
                conn.close()

    def remove_item(self, item_id: str) -> bool:
        """Cancel one pending queue item by id."""
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    "UPDATE research_queue SET status='cancelled', finished_at=?, "
                    "error='Removed from queue' "
                    "WHERE id=? AND status='pending'",
                    (_now(), item_id),
                )
                conn.commit()
                return cur.rowcount > 0
            finally:
                conn.close()

    def attach_job(self, item_id: str, job_id: str) -> None:
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    "UPDATE research_queue SET job_id=? WHERE id=?",
                    (job_id, item_id),
                )
                conn.commit()
            finally:
                conn.close()

    def finish(self, item_id: str, *, ok: bool, error: str | None = None) -> None:
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    "UPDATE research_queue SET status=?, error=?, finished_at=? WHERE id=?",
                    (
                        "completed" if ok else "failed",
                        error,
                        _now(),
                        item_id,
                    ),
                )
                conn.commit()
            finally:
                conn.close()

    def cancel(self, item_id: str) -> bool:
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    "UPDATE research_queue SET status='cancelled', finished_at=? "
                    "WHERE id=? AND status='pending'",
                    (_now(), item_id),
                )
                conn.commit()
                return cur.rowcount > 0
            finally:
                conn.close()

    def cancel_all_pending(self) -> int:
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    "UPDATE research_queue SET status='cancelled', finished_at=? WHERE status='pending'",
                    (_now(),),
                )
                conn.commit()
                return cur.rowcount
            finally:
                conn.close()

    def clear_finished(self) -> int:
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    "DELETE FROM research_queue WHERE status IN ('completed','failed','cancelled')"
                )
                conn.commit()
                return cur.rowcount
            finally:
                conn.close()

    def reset_interrupted(self) -> int:
        """After app restart: put running queue items back to pending for retry."""
        with self._lock:
            conn = connect()
            try:
                cur = conn.execute(
                    "UPDATE research_queue SET status='pending', job_id=NULL, started_at=NULL, "
                    "error='Interrupted by app restart — re-queued' WHERE status='running'"
                )
                conn.commit()
                return cur.rowcount
            finally:
                conn.close()


class QueueWorker:
    """Background loop: start one queued research job at a time, wait, then next."""

    def __init__(
        self,
        store: ResearchQueueStore,
        start_job: StartJobFn,
        get_job: Callable[[str], Any],
        *,
        poll_seconds: float = 5.0,
    ) -> None:
        self.store = store
        self.start_job = start_job
        self.get_job = get_job
        self.poll_seconds = poll_seconds
        self._thread: threading.Thread | None = None
        self._stop = threading.Event()
        self._wake = threading.Event()

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, name="research-queue-worker", daemon=True)
        self._thread.start()
        logger.info("Research queue worker started")

    def stop(self) -> None:
        self._stop.set()
        self._wake.set()

    def kick(self) -> None:
        """Wake the worker after new items are enqueued or pause cleared."""
        self._wake.set()

    def _loop(self) -> None:
        while not self._stop.is_set():
            try:
                self._tick()
            except Exception:  # noqa: BLE001
                logger.exception("Queue worker tick failed")
            self._wake.wait(timeout=self.poll_seconds)
            self._wake.clear()

    def _any_inflight_job(self) -> bool:
        """True if a research job is still active (manual or queue)."""
        list_fn = getattr(getattr(self.get_job, "__self__", None), "list_recent", None)
        if not callable(list_fn):
            return False
        for j in list_fn(40):
            if j.status in {"running", "planning", "queued", "awaiting_approval"}:
                return True
        return False

    def _tick(self) -> None:
        # Release expired prompt holds so claim_next can pick them up.
        try:
            released = self.store.release_holds_due()
            if released:
                logger.info("Released %s expired queue hold(s)", released)
        except Exception:  # noqa: BLE001
            logger.exception("release_holds_due failed")

        # Always settle the current running item first — even when paused —
        # so "Pause after current" still marks that job completed/failed.
        running = [i for i in self.store.list_items(include_done=False) if i.status == "running"]
        if running:
            item = running[0]
            if item.job_id:
                job = self.get_job(item.job_id)
                if job is None:
                    self.store.finish(item.id, ok=False, error="Linked job missing after restart")
                    self.kick()
                    return
                if job.status in {"completed"}:
                    self.store.finish(item.id, ok=True)
                    self.kick()
                    return
                if job.status in {"failed"}:
                    self.store.finish(
                        item.id, ok=False, error=job.error or getattr(job, "message", None) or "Job failed"
                    )
                    self.kick()
                    return
                if job.status in {"awaiting_approval"}:
                    # Queue runs must not block overnight on plan approval.
                    self.store.finish(
                        item.id,
                        ok=False,
                        error="Job waiting for plan approval — queue runs use auto-start (collaborative off)",
                    )
                    self.kick()
                    return
                # still running/planning/queued
                return
            if self.store.get_paused():
                return
            # running without job_id — start now
            self._launch(item)
            return

        if self.store.get_paused():
            return

        # Do not start the next queued ticker while a manual (or other) job is in flight.
        if self._any_inflight_job():
            return

        item = self.store.claim_next()
        if not item:
            return
        self._launch(item)

    def _launch(self, item: QueueItem) -> None:
        logger.info(
            "Queue launching %s template=%s from_scratch=%s",
            item.ticker,
            item.template,
            item.from_scratch,
        )
        try:
            job_id = self.start_job(
                item.ticker,
                item.mode,
                item.goal or "",
                False,  # never collaborative in queue
                template=item.template,
                from_scratch=item.from_scratch,
            )
            self.store.attach_job(item.id, job_id)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Queue failed to start %s", item.ticker)
            self.store.finish(item.id, ok=False, error=str(exc))
            self.kick()


# Process-wide singletons (wired from app.api)
queue_store = ResearchQueueStore()
queue_worker: QueueWorker | None = None
