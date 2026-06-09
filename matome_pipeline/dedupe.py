"""重複排除 — URL・タイトル正規化・canonical_keyで重複を判定"""

import re
import unicodedata


def normalize_title(title: str) -> str:
    """タイトルを正規化する。"""
    t = unicodedata.normalize("NFKC", title)
    t = re.sub(r"[\s\u3000]+", " ", t).strip().lower()
    return t


def canonical_key(source_url: str, title: str) -> str:
    """重複排除用のキーを生成する。"""
    url_key = re.sub(r"https?://", "", source_url).rstrip("/")
    title_key = normalize_title(title)[:60]
    return f"{url_key}|{title_key}"


def is_duplicate(conn, source_url: str, title: str) -> bool:
    """DBに同一記事が存在するか判定する。"""
    key = canonical_key(source_url, title)
    row = conn.execute(
        "SELECT id FROM items WHERE source_url = ? OR canonical_key = ?",
        (source_url, key),
    ).fetchone()
    return row is not None
