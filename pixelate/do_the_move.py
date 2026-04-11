#!/usr/bin/env python3
"""
do_the_move.py — Pixelator MOVE phase (Duplicatus Edition)
Stage 01 chain-of-custody: move originals to duplicatus after verified copy

Policy (per Gemini session 2026-03-29):
  - Verified originals go to DUPLICATUS — NOT deleted
  - If a copy was necessary (file ID changed), log the previous path
  - Delete from duplicatus only when consciously decided later
  - Conservation bias: archive, don't delete

Reads transfer_manifest.json and moves _pixelator/ originals to duplicatus/
only where status == "transferred" and verified == True.

Usage:
    python3 do_the_move.py              # dry run (safe, shows what WOULD move)
    python3 do_the_move.py --run        # execute moves to duplicatus
    python3 do_the_move.py --status     # summary counts only

∰◊€π¿🌌∞
€(do_the_move_v2_duplicatus)
"""

import json
import os
import shutil
import sys
from datetime import datetime

MANIFEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transfer_manifest.json")
MOVE_LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "move_log.json")

# Duplicatus — where originals go to orbit until consciously deleted
DUPLICATUS_ROOT = "/storage/emulated/0/pixel8a/Q/hodie/duplicatus/_pixelator"


def load_manifest():
    with open(MANIFEST_PATH, "r") as f:
        return json.load(f)


def run(execute=False, status_only=False):
    manifest = load_manifest()
    items = manifest.get("items", [])

    total    = len(items)
    safe     = [i for i in items if i.get("status") == "transferred" and i.get("verified") is True]
    pending  = [i for i in items if i.get("status") == "pending"]
    skipped  = [i for i in items if i.get("status") not in ("transferred", "pending")]

    print(f"\n── Pixelator Move → Duplicatus ─────────────────")
    print(f"  Manifest  : {manifest['manifest_id']}")
    print(f"  Source    : {manifest['source']}")
    print(f"  Dest copy : {manifest['destination']}")
    print(f"  Duplicatus: {DUPLICATUS_ROOT}")
    print(f"  Total     : {total:,}")
    print(f"  ✓ Safe to move (verified copies)    : {len(safe):,}")
    print(f"  ⏳ Pending (not yet transferred)    : {len(pending):,}")
    print(f"  ? Other status                      : {len(skipped):,}")
    print(f"────────────────────────────────────────────────\n")

    if status_only:
        return

    mode = "DRY RUN" if not execute else "LIVE MOVE → DUPLICATUS"
    print(f"  Mode: {mode}\n")

    if pending:
        print(f"  ⚠  {len(pending):,} files not yet transferred — skipping those originals.\n")

    moved   = []
    errors  = []
    missing = []

    for item in safe:
        src = item["src"]
        rel = item["rel"]

        # Destination in duplicatus mirrors relative path
        dup_dst = os.path.join(DUPLICATUS_ROOT, rel)

        # Verify copy exists before touching original
        dst = item["dst"]
        if not os.path.exists(dst):
            errors.append({"src": src, "reason": "verified copy missing at dst"})
            print(f"  [!] COPY MISSING — keeping original: {rel}")
            continue

        if not os.path.exists(src):
            missing.append(src)
            continue  # already moved, fine

        if execute:
            try:
                os.makedirs(os.path.dirname(dup_dst), exist_ok=True)
                shutil.move(src, dup_dst)
                moved.append({
                    "rel": rel,
                    "previous_path": src,
                    "duplicatus_path": dup_dst,
                    "copy_at_dst": dst,
                    "moved_at": datetime.now().isoformat(),
                    "note": "original → duplicatus; copy verified before move"
                })
            except Exception as e:
                errors.append({"src": src, "reason": str(e)})
                print(f"  [!] ERROR moving {rel}: {e}")
        else:
            # Dry run — list first 20
            if len(moved) < 20:
                print(f"  [dry] {rel}")
                print(f"        {src}")
                print(f"        → {dup_dst}")
            elif len(moved) == 20:
                print(f"  [dry] ... and {len(safe) - 20:,} more\n")
            moved.append(src)

    print(f"\n── Results ─────────────────────────────────────")
    if execute:
        print(f"  Moved to duplicatus : {len(moved):,}")
        print(f"  Errors              : {len(errors):,}")
        print(f"  Already gone        : {len(missing):,}")

        log = {
            "move_id": manifest["manifest_id"],
            "executed_at": datetime.now().isoformat(),
            "policy": "originals → duplicatus, not deleted",
            "duplicatus_root": DUPLICATUS_ROOT,
            "moved_count": len(moved),
            "error_count": len(errors),
            "already_gone": len(missing),
            "errors": errors,
            "moves": moved,
        }
        with open(MOVE_LOG_PATH, "w") as f:
            json.dump(log, f, indent=2)
        print(f"  Log saved : {MOVE_LOG_PATH}")
        print(f"\n  Originals are in duplicatus — delete consciously when ready.")
    else:
        print(f"  Would move  : {len(moved):,} originals → duplicatus")
        print(f"  Skipped     : {len(pending):,} pending")
        print(f"\n  Run with --run to execute.")

    print(f"────────────────────────────────────────────────\n")


if __name__ == "__main__":
    if "--run" in sys.argv:
        print("\n  Moving originals to duplicatus (NOT deleting).")
        confirm = input("  Type 'yes' to continue: ").strip().lower()
        if confirm == "yes":
            run(execute=True)
        else:
            print("  Aborted.")
    elif "--status" in sys.argv:
        run(status_only=True)
    else:
        run(execute=False)
