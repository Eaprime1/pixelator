#!/usr/bin/env python3
"""
TESTER RESULTS MATRIX
=====================
Gathers all tester_results.txt files across the PIXEL8 platform,
aggregates them into a unified view, shows trends and pressure history.

Runs on command or at intervals (--watch N seconds).

Sources: finds all tester_results.txt anywhere under pixel8a/
Each line format: [TIMESTAMP] LABEL  SYMBOL PRESSURE STATUS  MEM:x CPU:x PY:x

Usage:
  python3 tester_results_matrix.py              # one-shot report
  python3 tester_results_matrix.py --watch 30   # refresh every 30s
  python3 tester_results_matrix.py --tail 20    # last 20 entries only
  python3 tester_results_matrix.py --find       # locate all results files
  python3 tester_results_matrix.py --since 1h   # last hour only

Output: appends summary to tester_results.txt (the matrix IS also a tester)

∰◊€π¿🌌∞
€(tester_results_matrix_v1)
"""

import os
import sys
import time
import json
import re
import datetime
import argparse
from collections import defaultdict
from typing import List, Dict, Optional, Tuple

PIXEL8A_ROOT   = "/storage/emulated/0/pixel8a"
RESULTS_FNAME  = "tester_results.txt"
PRIMARY_RESULT = os.path.join(PIXEL8A_ROOT, "pixelator/pixelate", RESULTS_FNAME)

# Search roots — where to look for results files
SEARCH_ROOTS = [
    PIXEL8A_ROOT,
]

MAX_DEPTH = 6   # don't recurse too deep (huge directories)

# Labels from artesian_monitor / aquifer_intake / other tools
KNOWN_LABELS = {
    "once":            "artesian_monitor --once",
    "status":          "artesian_monitor --status",
    "monitor":         "artesian_monitor continuous",
    "AQUIFER":         "aquifer_intake",
    "INTAKE_COMPLETE": "aquifer_intake complete",
    "MANIFEST_FIXED":  "manifest fix",
    "FIX_COMPLETE":    "manifest fix complete",
    "MATRIX":          "tester_results_matrix",
}

# ─── Entry Parsing ────────────────────────────────────────────────────────────

def parse_line(line: str, source_file: str) -> Optional[dict]:
    """
    Parse one line from a tester_results.txt file.
    Format: [TIMESTAMP] LABEL  SYMBOL PRESSURE STATUS  MEM:x CPU:x PY:x
    Also handles plain AQUIFER/INTAKE lines without pressure data.
    """
    line = line.strip()
    if not line:
        return None

    # Extract timestamp
    ts_match = re.match(r'\[(\d{17,20})\]\s+(.+)', line)
    if not ts_match:
        return None

    ts   = ts_match.group(1)
    rest = ts_match.group(2).strip()

    entry = {
        "ts":       ts,
        "raw":      line,
        "source":   source_file,
        "label":    "",
        "symbol":   "",
        "pressure": None,
        "status":   "",
        "mem":      None,
        "cpu":      None,
        "py":       None,
    }

    # Try to parse pressure line (artesian_monitor format)
    # LABEL  SYMBOL PRESSURE STATUS  MEM:x CPU:x PY:x
    pressure_re = re.compile(
        r'(\S+)\s+'                           # label
        r'([∰¿€◊℞§$∞])\s+'                   # symbol
        r'([\d.]+)\s+'                         # pressure
        r'(\S+)'                               # status
        r'(?:\s+MEM:([\d.]+)%)?'              # MEM optional
        r'(?:\s+CPU:([\d.]+)%)?'              # CPU optional
        r'(?:\s+PY:(\d+))?'                   # PY optional
    )
    m = pressure_re.match(rest)
    if m:
        entry["label"]    = m.group(1)
        entry["symbol"]   = m.group(2)
        entry["pressure"] = float(m.group(3))
        entry["status"]   = m.group(4)
        entry["mem"]      = float(m.group(5)) if m.group(5) else None
        entry["cpu"]      = float(m.group(6)) if m.group(6) else None
        entry["py"]       = int(m.group(7))   if m.group(7) else None
    else:
        # Non-pressure entry (aquifer events etc)
        parts = rest.split(None, 1)
        entry["label"] = parts[0] if parts else rest
        entry["status"] = parts[1] if len(parts) > 1 else ""

    return entry


def load_file(path: str) -> List[dict]:
    entries = []
    try:
        with open(path, "r", errors="replace") as f:
            for line in f:
                e = parse_line(line, path)
                if e:
                    entries.append(e)
    except Exception:
        pass
    return entries


# ─── File Discovery ───────────────────────────────────────────────────────────

def find_results_files() -> List[str]:
    """Walk SEARCH_ROOTS to find all tester_results.txt files."""
    found = []
    for root in SEARCH_ROOTS:
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            # Limit depth
            depth = dirpath[len(root):].count(os.sep)
            if depth >= MAX_DEPTH:
                dirnames.clear()
                continue
            # Skip hidden and large dirs
            dirnames[:] = [
                d for d in dirnames
                if not d.startswith(".") and d not in ("__pycache__",)
            ]
            if RESULTS_FNAME in filenames:
                found.append(os.path.join(dirpath, RESULTS_FNAME))
    return sorted(found)


# ─── Analysis ────────────────────────────────────────────────────────────────

def since_cutoff(since_str: str) -> Optional[str]:
    """Convert '1h', '30m', '2d' to a timestamp string for comparison."""
    now = datetime.datetime.now()
    m = re.match(r'^(\d+)([mhd])$', since_str.lower())
    if not m:
        return None
    n, unit = int(m.group(1)), m.group(2)
    delta = {"m": datetime.timedelta(minutes=n),
             "h": datetime.timedelta(hours=n),
             "d": datetime.timedelta(days=n)}[unit]
    cutoff = now - delta
    return cutoff.strftime("%Y%m%d%H%M%S000")


def analyze(entries: List[dict]) -> dict:
    """Summarize a list of parsed entries."""
    pressure_entries = [e for e in entries if e["pressure"] is not None]
    event_entries    = [e for e in entries if e["pressure"] is None]

    stats = {
        "total":          len(entries),
        "pressure_count": len(pressure_entries),
        "event_count":    len(event_entries),
        "by_label":       defaultdict(int),
        "by_status":      defaultdict(int),
        "pressure_max":   None,
        "pressure_min":   None,
        "pressure_avg":   None,
        "overflow_count": 0,
        "high_count":     0,
        "caution_count":  0,
        "breathing_count":0,
        "first_ts":       entries[0]["ts"]  if entries else None,
        "last_ts":        entries[-1]["ts"] if entries else None,
    }

    for e in entries:
        stats["by_label"][e["label"]] += 1
        if e["status"]:
            stats["by_status"][e["status"]] += 1

    if pressure_entries:
        pressures = [e["pressure"] for e in pressure_entries]
        stats["pressure_max"] = max(pressures)
        stats["pressure_min"] = min(pressures)
        stats["pressure_avg"] = round(sum(pressures) / len(pressures), 1)
        for e in pressure_entries:
            p = e["pressure"]
            if p >= 95:   stats["overflow_count"]  += 1
            elif p >= 80: stats["high_count"]       += 1
            elif p >= 60: stats["caution_count"]    += 1
            else:         stats["breathing_count"]  += 1

    return stats


# ─── Display ─────────────────────────────────────────────────────────────────

PRESSURE_BARS = {
    "OVERFLOW":  "∰",
    "HIGH":      "¿",
    "CAUTION":   "€",
    "BREATHING": "◊",
}

def pressure_bar(value: Optional[float], width: int = 20) -> str:
    if value is None:
        return "─" * width
    filled = int((value / 100) * width)
    return "█" * filled + "░" * (width - filled)


def format_ts(ts: str) -> str:
    """20260326142233000 → 2026-03-26 14:22:33"""
    if len(ts) >= 14:
        return f"{ts[0:4]}-{ts[4:6]}-{ts[6:8]} {ts[8:10]}:{ts[10:12]}:{ts[12:14]}"
    return ts


def print_matrix(all_entries: List[dict], stats: dict, sources: List[str], tail: int = 0):
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║          PIXEL8  TESTER RESULTS MATRIX               ║")
    print(f"║  {now_str}                              ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()

    # Sources
    print(f"  Sources ({len(sources)}):")
    for s in sources:
        rel = s.replace(PIXEL8A_ROOT + "/", "")
        count = sum(1 for e in all_entries if e["source"] == s)
        print(f"    {rel:<55} {count:4d} entries")
    print()

    # Pressure summary
    if stats["pressure_count"] > 0:
        avg = stats["pressure_avg"]
        sym = "∰" if avg >= 95 else "¿" if avg >= 80 else "€" if avg >= 60 else "◊"
        bar = pressure_bar(avg)
        print(f"  Pressure  {sym} [{bar}] avg:{avg}  "
              f"max:{stats['pressure_max']}  min:{stats['pressure_min']}")
        print(f"            ∰ overflow:{stats['overflow_count']}  "
              f"¿ high:{stats['high_count']}  "
              f"€ caution:{stats['caution_count']}  "
              f"◊ breathing:{stats['breathing_count']}")
        print()

    # Events summary
    if stats["event_count"] > 0:
        print(f"  Events    {stats['event_count']} non-pressure entries")
        for label, count in sorted(stats["by_label"].items()):
            desc = KNOWN_LABELS.get(label, "")
            print(f"    {label:<20} {count:4d}  {desc}")
        print()

    # Timespan
    if stats["first_ts"] and stats["last_ts"]:
        print(f"  Span      {format_ts(stats['first_ts'])} → {format_ts(stats['last_ts'])}")
        print(f"  Total     {stats['total']} entries")
        print()

    # Recent entries
    entries_to_show = all_entries[-tail:] if tail > 0 else all_entries[-30:]
    if entries_to_show:
        print(f"  Recent entries (last {len(entries_to_show)}):")
        print(f"  {'TIMESTAMP':<19} {'LABEL':<14} {'SYM'} {'PRESSURE':>8}  STATUS")
        print(f"  {'─'*19} {'─'*14} {'─'*3} {'─'*8}  {'─'*12}")
        for e in entries_to_show:
            ts_fmt   = format_ts(e["ts"])
            label    = e["label"][:13]
            sym      = e.get("symbol", " ")
            pressure = f"{e['pressure']:6.1f}" if e["pressure"] is not None else "      "
            status   = e.get("status", "")[:20]
            print(f"  {ts_fmt:<19} {label:<14} {sym}  {pressure}  {status}")
    print()


# ─── Results Append ──────────────────────────────────────────────────────────

def write_matrix_result(stats: dict):
    """Matrix writes its own summary to tester_results.txt."""
    os.makedirs(os.path.dirname(PRIMARY_RESULT), exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]
    avg_str = str(stats["pressure_avg"]) if stats["pressure_avg"] else "n/a"
    line = (
        f"[{ts}] MATRIX       matrix_run "
        f"total:{stats['total']} "
        f"pressure_avg:{avg_str} "
        f"overflow:{stats['overflow_count']} "
        f"high:{stats['high_count']}\n"
    )
    with open(PRIMARY_RESULT, "a") as f:
        f.write(line)


# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_find():
    files = find_results_files()
    print(f"Found {len(files)} tester_results.txt files:")
    for f in files:
        rel = f.replace(PIXEL8A_ROOT + "/", "")
        try:
            size = os.path.getsize(f)
            with open(f) as fh:
                lines = sum(1 for _ in fh)
            print(f"  {rel:<60} {lines:5d} lines  {size:7d} bytes")
        except Exception:
            print(f"  {rel}")


def cmd_report(tail: int = 30, since: str = None):
    files   = find_results_files()
    cutoff  = since_cutoff(since) if since else None

    all_entries = []
    for f in files:
        entries = load_file(f)
        if cutoff:
            entries = [e for e in entries if e["ts"] >= cutoff]
        all_entries.extend(entries)

    all_entries.sort(key=lambda e: e["ts"])
    stats = analyze(all_entries)
    print_matrix(all_entries, stats, files, tail=tail)
    write_matrix_result(stats)


def cmd_watch(interval: int, tail: int = 20, since: str = None):
    print(f"Matrix watching — refresh every {interval}s (Ctrl+C to stop)")
    try:
        while True:
            os.system("clear")
            cmd_report(tail=tail, since=since)
            print(f"  Next refresh in {interval}s...")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMatrix stopped. ◊")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="PIXEL8 Tester Results Matrix")
    p.add_argument("--watch",  type=int, metavar="SEC",
                   help="Refresh every N seconds")
    p.add_argument("--tail",   type=int, default=30, metavar="N",
                   help="Show last N entries (default 30)")
    p.add_argument("--find",   action="store_true",
                   help="Find all tester_results.txt files")
    p.add_argument("--since",  metavar="PERIOD",
                   help="Filter to recent period: 30m, 2h, 1d")
    args = p.parse_args()

    if args.find:
        cmd_find()
    elif args.watch:
        cmd_watch(args.watch, tail=args.tail, since=args.since)
    else:
        cmd_report(tail=args.tail, since=args.since)


if __name__ == "__main__":
    main()
