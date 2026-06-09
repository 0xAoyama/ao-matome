"""CLIエントリポイント — python -m matome_pipeline <command>"""

import sys


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python -m matome_pipeline <command>")
        print("Commands:")
        print("  db init           — Initialize SQLite database")
        print("  sources validate  — Validate config/sources.yaml")
        print("  qa                — Run QA gate on all published posts")
        print("  run               — Run full pipeline (MVP skeleton)")
        print("  fetch             — Fetch sources (MVP skeleton)")
        print("  publish           — Publish low-risk drafts")
        sys.exit(1)

    cmd = args[0]

    if cmd == "db" and len(args) > 1 and args[1] == "init":
        from .db import init_db
        init_db()

    elif cmd == "sources" and len(args) > 1 and args[1] == "validate":
        from .fetcher import load_sources
        sources = load_sources()
        total = 0
        for cat, entries in sources.items():
            print(f"{cat}: {len(entries)} sources")
            for entry in entries:
                if not entry.get("url"):
                    print(f"  ERROR: {entry.get('name', '?')} has no URL")
                    sys.exit(1)
                if not entry.get("name"):
                    print(f"  ERROR: entry has no name")
                    sys.exit(1)
                total += 1
        print(f"All {total} sources valid.")

    elif cmd == "qa":
        from .qa_gate import qa_all_posts
        ok = qa_all_posts()
        sys.exit(0 if ok else 1)

    elif cmd == "run":
        print("[run] MVP pipeline skeleton")
        from .fetcher import fetch
        from .qa_gate import qa_all_posts
        fetch()
        qa_all_posts()
        print("[run] Done.")

    elif cmd == "fetch":
        from .fetcher import fetch
        category = args[1] if len(args) > 1 else None
        fetch(category)

    elif cmd == "publish":
        from .publisher import publish_drafts
        publish_drafts()

    else:
        print(f"Unknown command: {' '.join(args)}")
        sys.exit(1)
