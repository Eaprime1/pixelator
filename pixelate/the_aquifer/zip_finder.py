#!/usr/bin/env python3
"""
ZIP FINDER
==========
Discovers all .zip files anywhere under pixel8a.
Shows size, location, whether already in The Aquifer's cold/.
Does NOT move anything — pure discovery.

Run this first to understand the full zip landscape before any intake.

Usage:
  python3 zip_finder.py              # find all zips, full report
  python3 zip_finder.py --summary    # totals only, no file list
  python3 zip_finder.py --unknown    # only zips NOT yet in cold/

Results appended to tester_results.txt.

∰◊€π¿🌌∞
"""

import os
import sys
import datetime
import argparse

PIXEL8A_ROOT   = "/storage/emulated/0/pixel8a"
COLD_DIR       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cold")
RESULTS_FILE   = os.path.join(
    "/storage/emulated/0/pixel8a/pixelator/pixelate", "tester_results.txt"
)

# Directories to skip — too large, irrelevant, or already processed
SKIP_DIRS = {
    ".git", "__pycache__", "node_modules",
    "cold",      # already in The Aquifer
    "flowing",   # already extracted
}

MAX_DEPTH = 8


def append_results(line: str):
    os.makedirs(os.path.dirname(RESULTS_FILE), exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
    with open(RESULTS_FILE, "a") as f:
        f.write(f"[{ts}] ZIP_FINDER   {line}\n")


def find_zips(root: str) -> list:
    """Walk root and return list of (path, size_bytes, depth)."""
    results = []
    root = os.path.abspath(root)

    for dirpath, dirnames, filenames in os.walk(root):
        depth = dirpath[len(root):].count(os.sep)
        if depth >= MAX_DEPTH:
            dirnames.clear()
            continue

        # Prune skip dirs in-place
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        for fname in filenames:
            if fname.lower().endswith(".zip"):
                full = os.path.join(dirpath, fname)
                try:
                    size = os.path.getsize(full)
                except OSError:
                    size = 0
                rel  = full[len(root):].lstrip("/")
                results.append({
                    "path":     full,
                    "rel":      rel,
                    "name":     fname,
                    "size":     size,
                    "size_kb":  round(size / 1024, 1),
                    "size_mb":  round(size / (1024 * 1024), 2),
                    "in_cold":  os.path.exists(os.path.join(COLD_DIR, fname)),
                })

    results.sort(key=lambda r: r["path"])
    return results


def group_by_dir(zips: list) -> dict:
    groups = {}
    for z in zips:
        d = os.path.dirname(z["rel"])
        if d not in groups:
            groups[d] = []
        groups[d].append(z)
    return groups


def cmd_find(summary_only: bool = False, unknown_only: bool = False):
    print("ZIP FINDER — Platform Survey")
    print(f"  Root: {PIXEL8A_ROOT}")
    print()

    all_zips = find_zips(PIXEL8A_ROOT)

    if unknown_only:
        zips = [z for z in all_zips if not z["in_cold"]]
        label = "not yet in cold/"
    else:
        zips = all_zips
        label = "total"

    in_cold    = sum(1 for z in all_zips if z["in_cold"])
    not_in_cold = len(all_zips) - in_cold
    total_mb   = round(sum(z["size_mb"] for z in zips), 1)

    print(f"  Found        : {len(all_zips)} zip files")
    print(f"  In cold/     : {in_cold}")
    print(f"  Not in cold/ : {not_in_cold}  ← candidates for intake")
    print(f"  Showing      : {len(zips)} ({label})")
    print(f"  Total size   : {total_mb} MB")
    print()

    if not summary_only and zips:
        groups = group_by_dir(zips)
        for dirrel, group in sorted(groups.items()):
            dir_mb = round(sum(z["size_mb"] for z in group), 1)
            print(f"  📁 {dirrel or '(root)'}  [{len(group)} zips, {dir_mb}MB]")
            for z in group:
                cold_mark = "✓cold" if z["in_cold"] else "     "
                print(f"     {cold_mark}  {z['name']:<40}  {z['size_kb']:8.1f} KB")
        print()

    # Recommendation
    if not_in_cold > 0:
        print(f"  Recommendation:")
        print(f"    {not_in_cold} zips not yet in The Aquifer.")
        if not_in_cold <= 5:
            print(f"    Small batch — run intake directly.")
        elif not_in_cold <= 20:
            print(f"    Medium batch — test with --limit 3 first, then full intake.")
        else:
            print(f"    Large batch ({not_in_cold}) — run --limit 5 to test,")
            print(f"    then intake by directory to keep it manageable.")
        print()
        print(f"    Test run:  python3 aquifer_intake.py <dir> --limit 3 --scan-only")
        print(f"    Full move: python3 aquifer_intake.py <dir> --limit 5")

    append_results(
        f"SURVEY total:{len(all_zips)} "
        f"in_cold:{in_cold} "
        f"candidates:{not_in_cold} "
        f"size_mb:{total_mb}"
    )


def main():
    p = argparse.ArgumentParser(description="Zip Finder — Platform Survey")
    p.add_argument("--summary", action="store_true",
                   help="Totals only, no file listing")
    p.add_argument("--unknown", action="store_true",
                   help="Show only zips not yet in cold/")
    args = p.parse_args()
    cmd_find(summary_only=args.summary, unknown_only=args.unknown)


if __name__ == "__main__":
    main()
