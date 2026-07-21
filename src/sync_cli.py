"""CLI: python -m src.sync_cli import|export|status"""

from __future__ import annotations

import argparse
import json
import sys

from src.jobs import job_store
from src.sync_store import JOBS_DIR, ensure_sync_dirs, export_all_completed, import_all_sync_jobs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Sync research jobs between cloud and local via data/sync/")
    parser.add_argument("command", choices=["import", "export", "status"])
    args = parser.parse_args(argv)

    ensure_sync_dirs()
    if args.command == "import":
        stats = import_all_sync_jobs(job_store)
        print(json.dumps({"ok": True, "stats": stats}, indent=2))
        return 0
    if args.command == "export":
        n = export_all_completed(job_store)
        print(json.dumps({"ok": True, "exported": n, "dir": str(JOBS_DIR)}, indent=2))
        return 0
    # status
    files = list(JOBS_DIR.glob("*.json"))
    print(
        json.dumps(
            {
                "sync_dir": str(JOBS_DIR),
                "sync_jobs": len(files),
                "db_jobs": job_store.count_jobs(),
                "db_completed": job_store.count_jobs(status="completed"),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
