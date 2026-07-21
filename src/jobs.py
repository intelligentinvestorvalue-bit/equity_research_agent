"""Persistent job store (SQLite) for research jobs that survive restarts."""

from __future__ import annotations

import json
import threading
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from src.db import connect


@dataclass
class Job:
    id: str
    ticker: str
    mode: str
    goal: str = ""
    template: str = "auto"
    collaborative: bool = True
    status: str = "queued"  # queued | planning | awaiting_approval | running | completed | failed
    stage: str = "queued"
    message: str = ""
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    finished_at: str | None = None
    plan: dict[str, Any] | None = None
    result: dict[str, Any] | None = None
    error: str | None = None
    thoughts: list[dict[str, Any]] = field(default_factory=list)


def _dumps(obj: Any) -> str | None:
    if obj is None:
        return None
    return json.dumps(obj, default=str)


def _loads(raw: str | None) -> Any:
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return None


def _row_to_job(row: Any) -> Job:
    thoughts = _loads(row["thoughts_json"]) or []
    if not isinstance(thoughts, list):
        thoughts = []
    return Job(
        id=row["id"],
        ticker=row["ticker"],
        mode=row["mode"],
        goal=row["goal"] or "",
        template=row["template"] or "auto",
        collaborative=bool(row["collaborative"]),
        status=row["status"],
        stage=row["stage"] or "",
        message=row["message"] or "",
        created_at=row["created_at"],
        finished_at=row["finished_at"],
        plan=_loads(row["plan_json"]),
        result=_loads(row["result_json"]),
        error=row["error"],
        thoughts=thoughts,
    )


class JobStore:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._init_db()

    def _init_db(self) -> None:
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS jobs (
                        id TEXT PRIMARY KEY,
                        ticker TEXT NOT NULL,
                        mode TEXT NOT NULL,
                        goal TEXT DEFAULT '',
                        template TEXT DEFAULT 'auto',
                        collaborative INTEGER DEFAULT 1,
                        status TEXT NOT NULL,
                        stage TEXT DEFAULT '',
                        message TEXT DEFAULT '',
                        created_at TEXT NOT NULL,
                        finished_at TEXT,
                        plan_json TEXT,
                        result_json TEXT,
                        error TEXT,
                        thoughts_json TEXT DEFAULT '[]'
                    )
                    """
                )
                conn.execute(
                    "CREATE INDEX IF NOT EXISTS idx_jobs_created ON jobs(created_at DESC)"
                )
                conn.commit()
            finally:
                conn.close()

    def create(
        self,
        ticker: str,
        mode: str,
        goal: str = "",
        collaborative: bool = True,
        template: str = "auto",
    ) -> Job:
        job = Job(
            id=str(uuid.uuid4()),
            ticker=ticker.upper(),
            mode=mode,
            goal=goal or "",
            template=template or "auto",
            collaborative=collaborative,
        )
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    """
                    INSERT INTO jobs (
                        id, ticker, mode, goal, template, collaborative,
                        status, stage, message, created_at, finished_at,
                        plan_json, result_json, error, thoughts_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        job.id,
                        job.ticker,
                        job.mode,
                        job.goal,
                        job.template,
                        1 if job.collaborative else 0,
                        job.status,
                        job.stage,
                        job.message,
                        job.created_at,
                        job.finished_at,
                        None,
                        None,
                        None,
                        "[]",
                    ),
                )
                conn.commit()
            finally:
                conn.close()
        return job

    def upsert(self, job: Job) -> None:
        """Insert or fully replace a job row (used by cloud/local sync import)."""
        with self._lock:
            conn = connect()
            try:
                conn.execute(
                    """
                    INSERT INTO jobs (
                        id, ticker, mode, goal, template, collaborative,
                        status, stage, message, created_at, finished_at,
                        plan_json, result_json, error, thoughts_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        ticker=excluded.ticker,
                        mode=excluded.mode,
                        goal=excluded.goal,
                        template=excluded.template,
                        collaborative=excluded.collaborative,
                        status=excluded.status,
                        stage=excluded.stage,
                        message=excluded.message,
                        created_at=excluded.created_at,
                        finished_at=excluded.finished_at,
                        plan_json=excluded.plan_json,
                        result_json=excluded.result_json,
                        error=excluded.error,
                        thoughts_json=excluded.thoughts_json
                    """,
                    (
                        job.id,
                        job.ticker,
                        job.mode,
                        job.goal,
                        job.template,
                        1 if job.collaborative else 0,
                        job.status,
                        job.stage,
                        job.message,
                        job.created_at,
                        job.finished_at,
                        _dumps(job.plan),
                        _dumps(job.result),
                        job.error,
                        _dumps(job.thoughts) or "[]",
                    ),
                )
                conn.commit()
            finally:
                conn.close()

    def get(self, job_id: str) -> Job | None:
        with self._lock:
            conn = connect()
            try:
                row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
                return _row_to_job(row) if row else None
            finally:
                conn.close()

    def update(self, job_id: str, **kwargs: Any) -> None:
        if not kwargs:
            return
        allowed = {
            "ticker",
            "mode",
            "goal",
            "template",
            "collaborative",
            "status",
            "stage",
            "message",
            "finished_at",
            "plan",
            "result",
            "error",
            "thoughts",
        }
        cols: list[str] = []
        vals: list[Any] = []
        for k, v in kwargs.items():
            if k not in allowed:
                continue
            if k == "plan":
                cols.append("plan_json = ?")
                vals.append(_dumps(v))
            elif k == "result":
                cols.append("result_json = ?")
                vals.append(_dumps(v))
            elif k == "thoughts":
                cols.append("thoughts_json = ?")
                vals.append(_dumps(v) or "[]")
            elif k == "collaborative":
                cols.append("collaborative = ?")
                vals.append(1 if v else 0)
            else:
                cols.append(f"{k} = ?")
                vals.append(v)
        if not cols:
            return
        vals.append(job_id)
        with self._lock:
            conn = connect()
            try:
                conn.execute(f"UPDATE jobs SET {', '.join(cols)} WHERE id = ?", vals)
                conn.commit()
            finally:
                conn.close()

    def append_thought(self, job_id: str, kind: str, message: str) -> None:
        from src.thinking import thought_event

        with self._lock:
            job = self.get(job_id)
            if not job:
                return
            thoughts = list(job.thoughts or [])
            thoughts.append(thought_event(kind, message))
            if len(thoughts) > 200:
                thoughts = thoughts[-200:]
            self.update(job_id, thoughts=thoughts)

    def list_recent(
        self,
        limit: int = 20,
        *,
        ticker: str | None = None,
        status: str | None = None,
        offset: int = 0,
    ) -> list[Job]:
        clauses: list[str] = []
        params: list[Any] = []
        if ticker:
            clauses.append("UPPER(ticker) = ?")
            params.append(ticker.strip().upper())
        if status:
            clauses.append("status = ?")
            params.append(status.strip().lower())
        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        params.extend([max(1, min(int(limit), 200)), max(0, int(offset))])
        with self._lock:
            conn = connect()
            try:
                rows = conn.execute(
                    f"SELECT * FROM jobs {where} ORDER BY created_at DESC LIMIT ? OFFSET ?",
                    params,
                ).fetchall()
                return [_row_to_job(r) for r in rows]
            finally:
                conn.close()

    def count_jobs(self, *, ticker: str | None = None, status: str | None = None) -> int:
        clauses: list[str] = []
        params: list[Any] = []
        if ticker:
            clauses.append("UPPER(ticker) = ?")
            params.append(ticker.strip().upper())
        if status:
            clauses.append("status = ?")
            params.append(status.strip().lower())
        where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
        with self._lock:
            conn = connect()
            try:
                row = conn.execute(f"SELECT COUNT(*) AS n FROM jobs {where}", params).fetchone()
                return int(row["n"]) if row else 0
            finally:
                conn.close()


job_store = JobStore()
