"""公開処理 — low-risk記事のみ content/sites/ へ配置する（MVP skeleton）"""

from pathlib import Path

DRAFTS_DIR = Path(__file__).resolve().parent.parent / "content" / "drafts"
SITES_DIR = Path(__file__).resolve().parent.parent / "content" / "sites"


def publish_drafts() -> None:
    """drafts/ からlow-riskの記事を sites/ に移動する（MVP skeleton）。"""
    if not DRAFTS_DIR.exists():
        print("[publisher] No drafts directory found.")
        return

    import yaml

    for md_file in DRAFTS_DIR.glob("*.md"):
        raw = md_file.read_text()
        if not raw.startswith("---"):
            continue
        end = raw.index("---", 3)
        meta = yaml.safe_load(raw[3:end])
        if not meta:
            continue

        risk = meta.get("risk_level", "high")
        category = meta.get("category", "misc")

        if risk != "low":
            print(f"[publisher] SKIP (risk={risk}): {md_file.name}")
            continue
        if meta.get("ymyl"):
            print(f"[publisher] SKIP (YMYL): {md_file.name}")
            continue
        if meta.get("copyright_risk"):
            print(f"[publisher] SKIP (copyright_risk): {md_file.name}")
            continue

        dest_dir = SITES_DIR / category / "posts"
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / md_file.name
        md_file.rename(dest)
        print(f"[publisher] Published: {dest}")
