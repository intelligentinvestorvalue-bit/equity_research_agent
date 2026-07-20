"""Shared SQLite paths for jobs and IV history."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from src.config import ROOT_DIR

DATA_DIR = ROOT_DIR / "data"
DB_PATH = DATA_DIR / "research.db"


def connect() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False, timeout=30)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    return conn
