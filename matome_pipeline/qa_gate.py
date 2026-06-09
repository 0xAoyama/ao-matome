"""品質ゲート — 公開可否を判定する

基本思想:
- risk_level=low のみ自動公開を許可
- risk_level=medium は人間レビュー後に公開（draftに留める）
- risk_level=high は自動公開しない（炎上、人物、YMYL事故回避）
- source_url がない記事は公開しない
- copyright_risk=true の記事は公開しない
"""

from pathlib import Path
from typing import TextIO

import yaml
import sys


class QAResult:
    def __init__(self):
        self.passed: list[str] = []
        self.blocked: list[str] = []

    @property
    def ok(self) -> bool:
        return len(self.blocked) == 0

    def report(self, out: TextIO = sys.stdout) -> None:
        out.write(f"QA result: {'PASS' if self.ok else 'BLOCKED'}\n")
        for msg in self.passed:
            out.write(f"  [PASS] {msg}\n")
        for msg in self.blocked:
            out.write(f"  [BLOCK] {msg}\n")


def check_post(meta: dict) -> QAResult:
    """記事メタデータの公開可否を判定する。"""
    result = QAResult()

    # 一次ソースURL必須
    if meta.get("source_url"):
        result.passed.append("source_url あり")
    else:
        result.blocked.append("source_url がありません — 公式ソースなしの記事は公開できません")

    # リスクレベル判定
    risk = meta.get("risk_level", "high")
    if risk == "low":
        result.passed.append(f"risk_level={risk} — 自動公開OK")
    elif risk == "medium":
        result.blocked.append(f"risk_level={risk} — 人間レビューが必要です")
    else:
        result.blocked.append(f"risk_level={risk} — 自動公開禁止（炎上/人物/YMYL事故回避）")

    # YMYL判定
    if meta.get("ymyl"):
        result.blocked.append("YMYL記事 — 専門家レビューなしでは公開できません")
    else:
        result.passed.append("YMYL=false")

    # 著作権リスク判定
    if meta.get("copyright_risk"):
        result.blocked.append("copyright_risk=true — 著作権リスクがある記事は公開できません")
    else:
        result.passed.append("copyright_risk=false")

    return result


def qa_all_posts() -> bool:
    """content/sites/ 配下の全記事をQAチェックする。"""
    content_dir = Path(__file__).resolve().parent.parent / "content" / "sites"
    all_ok = True
    count = 0

    for md_file in sorted(content_dir.rglob("*.md")):
        raw = md_file.read_text()
        # 簡易frontmatterパース
        if not raw.startswith("---"):
            continue
        end = raw.index("---", 3)
        meta = yaml.safe_load(raw[3:end])
        if not meta:
            continue

        count += 1
        result = check_post(meta)
        status = "PASS" if result.ok else "BLOCKED"
        print(f"[{status}] {md_file.relative_to(content_dir)}: {meta.get('title', '?')}")
        if not result.ok:
            for msg in result.blocked:
                print(f"         {msg}")
            all_ok = False

    print(f"\nTotal: {count} posts checked")
    return all_ok
