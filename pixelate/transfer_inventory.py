#!/usr/bin/env python3
"""
transfer_inventory.py
Chain-of-custody transfer: _pixelator/ → pixelator/

Philosophy: copy not move, full manifest, archive originals.

Usage:
    python3 transfer_inventory.py          # scan only (safe)
    python3 transfer_inventory.py --run    # execute transfer
    python3 transfer_inventory.py --status # show what's been transferred
"""

import os
import shutil
import json
import uuid
import hashlib
import argparse
from pathlib import Path
from datetime import datetime

SRC  = Path("/storage/emulated/0/pixel8a/_pixelator")
DST  = Path("/storage/emulated/0/pixel8a/pixelator")
MANIFEST_FILE = DST / "pixelate" / "transfer_manifest.json"

SKIP_PATTERNS = {".git", "__pycache__", ".DS_Store", "*.pyc"}

# ── helpers ────────────────────────────────────────────────────

def file_hash(path):
    """SHA256 of file content"""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()[:16]
    except Exception:
        return "unreadable"

def should_skip(path):
    for pat in SKIP_PATTERNS:
        if pat.startswith("*"):
            if path.name.endswith(pat[1:]):
                return True
        elif path.name == pat:
            return True
    return False

def scan_source():
    """Walk _pixelator/ and catalogue everything"""
    items = []
    if not SRC.exists():
        print(f"  ERROR: Source not found: {SRC}")
        return items

    for root, dirs, files in os.walk(SRC):
        # Skip hidden/system dirs in place
        dirs[:] = [d for d in dirs
                   if not should_skip(Path(root) / d)]

        for fname in files:
            fpath = Path(root) / fname
            if should_skip(fpath):
                continue

            rel = fpath.relative_to(SRC)
            dst_path = DST / rel

            items.append({
                "src":       str(fpath),
                "dst":       str(dst_path),
                "rel":       str(rel),
                "size":      fpath.stat().st_size,
                "hash":      file_hash(fpath),
                "exists_at_dst": dst_path.exists(),
                "status":    "pending"
            })

    return items

def load_manifest():
    if MANIFEST_FILE.exists():
        return json.loads(MANIFEST_FILE.read_text())
    return None

def save_manifest(manifest):
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))

# ── actions ────────────────────────────────────────────────────

def do_scan():
    print(f"\n{'='*60}")
    print(f"  TRANSFER INVENTORY SCAN")
    print(f"  Source: {SRC}")
    print(f"  Target: {DST}")
    print(f"{'='*60}\n")

    items = scan_source()
    if not items:
        print("  Nothing found in source.")
        return

    new_files     = [i for i in items if not i["exists_at_dst"]]
    exist_files   = [i for i in items if i["exists_at_dst"]]

    print(f"  Total files in _pixelator/:  {len(items)}")
    print(f"  New (not yet in pixelator/): {len(new_files)}")
    print(f"  Already exist at dst:        {len(exist_files)}")
    print()

    if new_files:
        print("  NEW FILES TO TRANSFER:")
        for item in new_files:
            size_kb = item["size"] / 1024
            print(f"    + {item['rel']}  ({size_kb:.1f}KB)")
    else:
        print("  All files already present at destination.")

    if exist_files:
        print("\n  ALREADY AT DESTINATION (will skip):")
        for item in exist_files[:10]:
            print(f"    = {item['rel']}")
        if len(exist_files) > 10:
            print(f"    ... and {len(exist_files)-10} more")

    print(f"\n  Run with --run to execute transfer")
    print(f"  Manifest will be saved to: {MANIFEST_FILE}")

    # Save scan manifest
    manifest = {
        "manifest_id": str(uuid.uuid4()),
        "created":     datetime.now().isoformat(),
        "source":      str(SRC),
        "destination": str(DST),
        "scanned_at":  datetime.now().isoformat(),
        "total":       len(items),
        "new":         len(new_files),
        "existing":    len(exist_files),
        "items":       items,
        "transferred": False
    }
    save_manifest(manifest)
    print(f"\n  Manifest saved. ✓")


def do_transfer():
    print(f"\n{'='*60}")
    print(f"  EXECUTING TRANSFER (chain of custody)")
    print(f"{'='*60}\n")

    manifest = load_manifest()
    if not manifest:
        print("  No manifest found. Run scan first (no --run flag)")
        return

    items    = manifest["items"]
    new_items = [i for i in items if not i["exists_at_dst"]]

    if not new_items:
        print("  Nothing to transfer — all files already at destination.")
        return

    transferred = []
    skipped     = []
    errors      = []

    for item in new_items:
        src_path = Path(item["src"])
        dst_path = Path(item["dst"])

        try:
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)

            # Verify copy
            dst_hash = file_hash(dst_path)
            if dst_hash == item["hash"]:
                item["status"] = "transferred"
                item["transferred_at"] = datetime.now().isoformat()
                item["verified"] = True
                transferred.append(item)
                print(f"  ✓ {item['rel']}")
            else:
                item["status"] = "hash_mismatch"
                item["verified"] = False
                errors.append(item)
                print(f"  ✗ HASH MISMATCH: {item['rel']}")

        except Exception as e:
            item["status"] = f"error: {e}"
            errors.append(item)
            print(f"  ✗ ERROR: {item['rel']} — {e}")

    # Update manifest
    manifest["transferred"]      = True
    manifest["transfer_run_at"]  = datetime.now().isoformat()
    manifest["transfer_count"]   = len(transferred)
    manifest["transfer_errors"]  = len(errors)
    manifest["items"]            = items
    save_manifest(manifest)

    print(f"\n{'='*60}")
    print(f"  TRANSFER COMPLETE")
    print(f"  Transferred: {len(transferred)} files")
    print(f"  Errors:      {len(errors)} files")
    print(f"  Manifest:    {MANIFEST_FILE}")
    print(f"\n  Originals preserved in: {SRC}")
    print(f"  To archive source when ready:")
    print(f"    mv {SRC} {SRC}.archived")
    print(f"\n  Next: git add . && git commit in pixelator/")
    print(f"{'='*60}")


def do_status():
    manifest = load_manifest()
    if not manifest:
        print("  No manifest found. Run scan first.")
        return

    print(f"\n  TRANSFER STATUS")
    print(f"  Manifest:    {manifest['manifest_id'][:8]}...")
    print(f"  Scanned:     {manifest.get('scanned_at','unknown')}")
    print(f"  Transferred: {manifest.get('transferred', False)}")
    if manifest.get("transferred"):
        print(f"  Run at:      {manifest.get('transfer_run_at','?')}")
        print(f"  Files moved: {manifest.get('transfer_count','?')}")
        print(f"  Errors:      {manifest.get('transfer_errors','?')}")
    print(f"  Total items: {manifest.get('total','?')}")
    print(f"  New items:   {manifest.get('new','?')}")


# ── main ───────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Chain-of-custody transfer: _pixelator → pixelator"
    )
    parser.add_argument("--run",    action="store_true",
                        help="Execute the transfer (default: scan only)")
    parser.add_argument("--status", action="store_true",
                        help="Show manifest status")
    args = parser.parse_args()

    print("\n∰◊€π¿🌌∞  Pixelator Transfer — Chain of Custody")

    if args.status:
        do_status()
    elif args.run:
        do_transfer()
    else:
        do_scan()
