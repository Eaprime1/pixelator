#!/usr/bin/env python3
"""
AQUIFER INTAKE
==============
Moves zip archives into The Aquifer's cold/ section.
Runs ZipMancer on each one. Writes manifests. Appends to tester_results.txt.

Usage:
  python3 aquifer_intake.py                          # intake from default ziparchive/
  python3 aquifer_intake.py /path/to/source/zips     # intake from custom path
  python3 aquifer_intake.py --scan-only              # manifest only, no move
  python3 aquifer_intake.py --report                 # show what's already in cold/

The MOVE rule: archives enter the chain of custody.
They move from wherever they were into cold/.
The manifests record where they came from.

∰◊€π¿🌌∞
"""

import os
import sys
import json
import datetime

AQUIFER_DIR   = os.path.dirname(os.path.abspath(__file__))
COLD_DIR      = os.path.join(AQUIFER_DIR, "cold")
FLOWING_DIR   = os.path.join(AQUIFER_DIR, "flowing")
MANIFEST_DIR  = os.path.join(AQUIFER_DIR, "manifests")
RESULTS_FILE  = os.path.join(
    "/storage/emulated/0/pixel8a/pixelator/pixelate",
    "tester_results.txt"
)
DEFAULT_INBOX = "/storage/emulated/0/pixel8a/ziparchive"

# Add mancers to path
sys.path.insert(0, os.path.join(
    "/storage/emulated/0/pixel8a/pixelator/pixelate/fraggle_rock/mancers"
))


def append_results(line: str):
    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
    with open(RESULTS_FILE, "a") as f:
        f.write(f"[{ts}] AQUIFER  {line}\n")


def ensure_dirs():
    for d in [COLD_DIR, FLOWING_DIR, MANIFEST_DIR]:
        os.makedirs(d, exist_ok=True)


def cmd_intake(source: str, scan_only: bool = False, limit: int = 0):
    """
    Intake zips from source into cold/.
    limit=0 means all. limit=N means first N only (for testing).
    """
    from zipmancer import ZipMancer
    import shutil

    ensure_dirs()
    source = os.path.abspath(source)

    if not os.path.isdir(source):
        print(f"Source not found: {source}")
        append_results(f"INTAKE_FAILED source not found: {source}")
        return

    all_zips = [f for f in sorted(os.listdir(source)) if f.lower().endswith(".zip")]
    if not all_zips:
        print(f"No zip files found in {source}")
        append_results(f"INTAKE_EMPTY {source}")
        return

    # Apply limit for test mode
    zips = all_zips[:limit] if limit > 0 else all_zips
    test_mode = limit > 0 and limit < len(all_zips)

    print(f"THE AQUIFER — Intake")
    print(f"  Source  : {source}")
    print(f"  Found   : {len(all_zips)} zips total")
    print(f"  Processing: {len(zips)}{' (TEST MODE — limited)' if test_mode else ''}")
    print(f"  Mode    : {'scan only' if scan_only else 'MOVE into cold/'}")
    print()

    zm = ZipMancer("aquifer_intake_01")

    # Process each zip individually so we can apply the limit cleanly
    manifests = []
    for fname in zips:
        zip_path = os.path.join(source, fname)
        manifest = zm.run(zip_path, mission_label=f"read:{fname}")
        manifests.append(manifest)

        # Write manifest
        os.makedirs(MANIFEST_DIR, exist_ok=True)
        mpath = os.path.join(MANIFEST_DIR, fname + ".manifest.json")
        with open(mpath, "w") as f:
            json.dump(manifest.to_dict(), f, indent=2)
        append_results(f"MANIFEST_WRITTEN {fname} files:{manifest.total_files}")

        # Move (not copy) if not scan_only
        if not scan_only and manifest.is_readable:
            dest = os.path.join(COLD_DIR, fname)
            shutil.move(zip_path, dest)
            manifest.zip_path = dest
            append_results(
                f"MOVED_TO_COLD {fname} "
                f"files:{manifest.total_files} "
                f"sha256:{manifest.zip_sha256[:12]}..."
            )

    print(zm.summary())
    print()

    for m in manifests:
        status = "✓" if m.is_readable else "✗"
        exts   = ", ".join(
            f".{e}({n})" for e, n in sorted(m.extensions_summary().items())
        )
        print(f"  {status} {m.zip_name}")
        print(f"     {m.total_files} files, {m.uncompressed_mb}MB uncompressed")
        if exts:
            print(f"     types: {exts}")
        if m.error:
            print(f"     ERROR: {m.error}")

        action = "SCANNED" if scan_only else "MOVED_TO_COLD"
        append_results(
            f"{action} {m.zip_name} "
            f"files:{m.total_files} "
            f"size:{m.uncompressed_mb}MB "
            f"sha256:{m.zip_sha256[:12]}..."
        )

    print()
    print(f"  Manifests → {MANIFEST_DIR}")
    print(f"  Results   → {RESULTS_FILE}")
    if not scan_only:
        print(f"  Cold      → {COLD_DIR}")
    print()
    print(f"  ∞ Intake complete.")
    append_results(f"INTAKE_COMPLETE {len(manifests)} archives")


def cmd_fix_manifests():
    """
    Regenerate manifests from archives already in cold/.
    Run this when zips moved but manifests didn't write correctly.
    Scans cold/ in place — no moves, just manifest generation.
    """
    from zipmancer import ZipMancer

    ensure_dirs()
    zips = [f for f in sorted(os.listdir(COLD_DIR)) if f.lower().endswith(".zip")]
    if not zips:
        print("cold/ is empty — nothing to fix.")
        return

    print(f"THE AQUIFER — Fixing manifests from cold/")
    print(f"  Found {len(zips)} archives in cold/")
    print()

    zm = ZipMancer("aquifer_fix_01")
    fixed = 0

    for fname in zips:
        zip_path  = os.path.join(COLD_DIR, fname)
        mpath     = os.path.join(MANIFEST_DIR, fname + ".manifest.json")

        if os.path.exists(mpath):
            print(f"  ✓ {fname:<40} manifest exists")
            continue

        print(f"  → {fname:<40} generating...", end="", flush=True)
        manifest = zm.run(zip_path, mission_label=f"fix:{fname}")

        os.makedirs(MANIFEST_DIR, exist_ok=True)
        with open(mpath, "w") as f:
            import json
            json.dump(manifest.to_dict(), f, indent=2)

        manifest.coc_entries.append({
            "ts": datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3],
            "action": "MANIFEST_FIXED",
            "note": mpath,
        })
        append_results(
            f"MANIFEST_FIXED {fname} "
            f"files:{manifest.total_files} "
            f"sha256:{manifest.zip_sha256[:12]}..."
        )
        print(f" ✓ {manifest.total_files} files, {manifest.uncompressed_mb}MB")
        fixed += 1

    print()
    print(f"  Fixed {fixed} manifests → {MANIFEST_DIR}")
    append_results(f"FIX_COMPLETE {fixed} manifests written")


def cmd_report():
    """Show what's already in cold/."""
    ensure_dirs()
    manifests = [
        f for f in sorted(os.listdir(MANIFEST_DIR))
        if f.endswith(".manifest.json")
    ]

    if not manifests:
        print("The Aquifer cold/ is empty.")
        return

    print(f"THE AQUIFER — Cold Storage Report")
    print(f"  {len(manifests)} archives")
    print()

    total_files = 0
    total_mb    = 0.0

    for fname in manifests:
        path = os.path.join(MANIFEST_DIR, fname)
        with open(path) as f:
            m = json.load(f)
        status = "✓" if not m.get("error") else "✗"
        print(
            f"  {status} {m.get('zip_name', fname):<35} "
            f"{m.get('total_files', 0):4d} files  "
            f"{m.get('uncompressed_mb', 0):6.1f} MB"
        )
        total_files += m.get("total_files", 0)
        total_mb    += m.get("uncompressed_mb", 0)

    print()
    print(f"  Total: {total_files} files, {round(total_mb, 1)} MB")
    print(f"  Pressurized. Ready to flow.")


def main():
    import argparse
    p = argparse.ArgumentParser(description="Aquifer Intake")
    p.add_argument("source",          nargs="?", default=DEFAULT_INBOX,
                   help=f"Source directory (default: {DEFAULT_INBOX})")
    p.add_argument("--scan-only",     action="store_true",
                   help="Generate manifests without moving files")
    p.add_argument("--limit",         type=int, default=0, metavar="N",
                   help="Test mode: process only first N zips")
    p.add_argument("--report",        action="store_true",
                   help="Show cold/ contents")
    p.add_argument("--fix-manifests", action="store_true",
                   help="Regenerate manifests for archives already in cold/")
    args = p.parse_args()

    if args.report:
        cmd_report()
    elif args.fix_manifests:
        cmd_fix_manifests()
    else:
        cmd_intake(args.source, scan_only=args.scan_only, limit=args.limit)


if __name__ == "__main__":
    main()
