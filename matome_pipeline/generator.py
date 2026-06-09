"""記事生成 — Markdown下書きの生成（MVP skeleton）"""

from pathlib import Path

DRAFTS_DIR = Path(__file__).resolve().parent.parent / "content" / "drafts"


def generate_draft(item: dict) -> Path:
    """itemからMarkdown下書きを生成する（MVP skeleton）。"""
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    slug = item.get("slug", "untitled")
    category = item.get("category", "misc")
    path = DRAFTS_DIR / f"{category}-{slug}.md"

    frontmatter = f"""---
title: "{item.get('title', 'Untitled')}"
summary: "{item.get('summary', '')}"
source_url: "{item.get('source_url', '')}"
source_name: "{item.get('source_name', '')}"
published_at: "{item.get('published_at', '')}"
checked_at: "{item.get('checked_at', '')}"
risk_level: "{item.get('risk_level', 'medium')}"
ymyl: {str(item.get('ymyl', False)).lower()}
copyright_risk: {str(item.get('copyright_risk', False)).lower()}
category: "{category}"
slug: "{slug}"
---

## {item.get('title', 'Untitled')}

{item.get('summary', '')}

---

**一次ソース:** [{item.get('source_name', '')}]({item.get('source_url', '')})
**確認日:** {item.get('checked_at', '')}
**免責:** 本記事は公式発表に基づく要約です。正確な情報は一次ソースをご確認ください。
"""
    path.write_text(frontmatter)
    print(f"[generator] Draft created: {path}")
    return path
