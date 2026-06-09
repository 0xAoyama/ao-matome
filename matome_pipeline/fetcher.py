"""ソース取得 — RSS/Atomフィードを取得してDBに保存（MVP skeleton）"""

from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "sources.yaml"


def load_sources(category: str | None = None) -> dict:
    """sources.yamlを読み込む。"""
    with open(CONFIG_PATH) as f:
        sources = yaml.safe_load(f)
    if category:
        return {category: sources.get(category, [])}
    return sources


def fetch(category: str | None = None) -> None:
    """ソースを取得する（MVP: skeleton）。"""
    sources = load_sources(category)
    for cat, entries in sources.items():
        print(f"[fetch] {cat}: {len(entries)} sources")
        for entry in entries:
            print(f"  - {entry['name']} ({entry['type']}): {entry['url']}")
    print("[fetch] MVP skeleton — 実際の取得は未実装です。")
