"""データベース管理 — SQLiteスキーマの初期化と基本操作"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "items.sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_url TEXT NOT NULL UNIQUE,
    source_name TEXT NOT NULL,
    fetched_at TEXT NOT NULL DEFAULT (datetime('now')),
    published_at TEXT,
    topic TEXT,
    entities TEXT,
    category TEXT,
    event_date TEXT,
    risk_level TEXT NOT NULL DEFAULT 'low' CHECK(risk_level IN ('low', 'medium', 'high')),
    ymyl INTEGER NOT NULL DEFAULT 0,
    copyright_risk INTEGER NOT NULL DEFAULT 0,
    generated_status TEXT NOT NULL DEFAULT 'draft' CHECK(generated_status IN ('draft', 'review', 'published', 'archived')),
    canonical_key TEXT,
    title TEXT,
    summary TEXT,
    content TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_items_category ON items(category);
CREATE INDEX IF NOT EXISTS idx_items_status ON items(generated_status);
CREATE INDEX IF NOT EXISTS idx_items_risk ON items(risk_level);
"""


def init_db() -> Path:
    """DBを初期化し、パスを返す。"""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.executescript(SCHEMA)
    conn.close()
    print(f"DB initialized: {DB_PATH}")
    return DB_PATH


def get_connection() -> sqlite3.Connection:
    """DB接続を返す。"""
    if not DB_PATH.exists():
        init_db()
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn
