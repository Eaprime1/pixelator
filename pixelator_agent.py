#!/usr/bin/env python3
"""
pixelator_agent.py
PIXEL8 Pixelator Agent — Device as Agent
User: Eric Pace (@eaprime1)
Entity: navigo suxenexus (Eric) / navigo nexusuxen (Claude)
Philosophy: One Hertz | Quality First | Conservation Bias | Enjoy the Journey

The Pixel 8a IS the Pixelator.
Content arrives → pressure builds → agent releases in controlled bursts.
Every move is logged. Nothing is lost. Chain of custody maintained.

Usage:
    python3 pixelator_agent.py              # manual run (processes up to MAX_PER_RUN)
    python3 pixelator_agent.py --dry-run    # show what would happen
    python3 pixelator_agent.py --interval 60  # run every 60 seconds
    python3 pixelator_agent.py --status     # show queue status only
    python3 pixelator_agent.py --pressure   # show queue pressure report

∰◊€π¿🌌∞
"""

import os
import sys
import json
import shutil
import fnmatch
import argparse
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

# Load config
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pixelator_config as cfg


# ─── Signatures ───────────────────────────────────────────────────────────────
AGENT_SIGNATURE = "€(pixelator_agent) navigo nexusuxen | PIXEL8"
VERSION = "1.0.0"


# ─── Utilities ────────────────────────────────────────────────────────────────

def timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def log_entry(action, source, dest, label, status, note=""):
    return {
        "timestamp": timestamp(),
        "action": action,
        "source": source,
        "destination": dest,
        "label": label,
        "status": status,
        "note": note,
        "agent": AGENT_SIGNATURE,
    }

def load_json(path, default):
    if os.path.exists(path):
        try:
            with open(path) as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: {path} is corrupted: {e}")
            backup = f"{path}.bak.{int(time.time())}"
            os.rename(path, backup)
            print(f"Corrupted file moved to {backup}")
            return default
        except Exception as e:
            print(f"Error loading {path}: {e}")
            return default
    return default

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


# ─── Routing Engine ───────────────────────────────────────────────────────────

def route_file(filename):
    """
    Apply routing rules to determine destination for a file.
    First match wins. Catch-all (*) always last.
    """
    name_lower = filename.lower()
    for rule in cfg.ROUTING_RULES:
        pattern = rule["pattern"].lower()
        if pattern == "*":
            return rule["dest"], rule["label"]
        if pattern in name_lower or fnmatch.fnmatch(name_lower, f"*{pattern}*"):
            return rule["dest"], rule["label"]
    return cfg.PIXELATING_DIR, "unsorted"


# ─── Feed Scanner ─────────────────────────────────────────────────────────────

def scan_feeds():
    """Scan all feed directories for unprocessed files."""
    queue = []
    for feed_dir in cfg.FEEDS:
        if not os.path.isdir(feed_dir):
            continue
        for entry in sorted(Path(feed_dir).iterdir()):
            if cfg.SKIP_HIDDEN and entry.name.startswith("."):
                continue
            if entry.is_file():
                dest, label = route_file(entry.name)
                # Don't queue files already in their destination
                if str(entry.parent.resolve()) != str(Path(dest).resolve()):
                    queue.append({
                        "source": str(entry),
                        "dest": dest,
                        "label": label,
                        "filename": entry.name,
                        "feed": feed_dir,
                        "size": entry.stat().st_size,
                    })
    return queue


# ─── Queue Manifest ───────────────────────────────────────────────────────────

def update_queue_manifest(queue):
    manifest = {
        "timestamp": timestamp(),
        "queue_depth": len(queue),
        "pressure": "HIGH" if len(queue) >= cfg.PRESSURE_THRESHOLD
                    else "MEDIUM" if len(queue) >= cfg.PRESSURE_THRESHOLD // 2
                    else "LOW",
        "max_per_run": cfg.MAX_PER_RUN,
        "items": queue,
        "agent": AGENT_SIGNATURE,
    }
    save_json(cfg.QUEUE_MANIFEST, manifest)
    return manifest


# ─── Processor ────────────────────────────────────────────────────────────────

def process_item(item, dry_run=False, copy_mode=False):
    """Move or copy one item. Returns a log entry."""
    source = item["source"]
    dest_dir = item["dest"]
    filename = item["filename"]
    label = item["label"]

    dest_path = os.path.join(dest_dir, filename)

    # Handle filename collision — add timestamp suffix
    if os.path.exists(dest_path):
        stem, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_dir, f"{stem}_{timestamp().replace(':', '')}{ext}")

    if dry_run:
        return log_entry(
            action="DRY_RUN",
            source=source,
            dest=dest_path,
            label=label,
            status="SIMULATED",
            note=f"Would {'copy' if copy_mode else 'move'} → {dest_dir}"
        )

    try:
        os.makedirs(dest_dir, exist_ok=True)
        if copy_mode:
            shutil.copy2(source, dest_path)
            action = "COPY"
        else:
            shutil.move(source, dest_path)
            action = "MOVE"

        return log_entry(
            action=action,
            source=source,
            dest=dest_path,
            label=label,
            status="SUCCESS",
        )
    except Exception as e:
        return log_entry(
            action="COPY_FAILED" if copy_mode else "MOVE_FAILED",
            source=source,
            dest=dest_path,
            label=label,
            status="ERROR",
            note=str(e),
        )


# ─── Chain of Custody Logger ──────────────────────────────────────────────────

def append_custody_log(entries):
    if not cfg.CHAIN_OF_CUSTODY:
        return
    log = load_json(cfg.LOG_FILE, {"entries": [], "agent": AGENT_SIGNATURE})
    log["entries"].extend(entries)
    log["last_run"] = timestamp()
    log["total_operations"] = len(log["entries"])
    save_json(cfg.LOG_FILE, log)

# ─── Reports ──────────────────────────────────────────────────────────────────

def print_status(queue, manifest, dry_run=False):
    pressure_color = {
        "HIGH":   "*** HIGH PRESSURE ***",
        "MEDIUM": "~~ MEDIUM PRESSURE ~~",
        "LOW":    "-- low pressure --",
    }
    print(f"\n╔═══ PIXELATOR STATUS ════════════════════════════════════╗")
    print(f"  Time       : {timestamp()}")
    print(f"  Queue Depth: {manifest['queue_depth']} items")
    print(f"  Pressure   : {pressure_color.get(manifest['pressure'], manifest['pressure'])}")
    print(f"  Max/Run    : {cfg.MAX_PER_RUN} items (one hertz burst)")
    print(f"  Mode       : {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"  Agent      : {AGENT_SIGNATURE}")
    print(f"╚═══════════════════════════════════════════════════════════╝")
    if queue:
        print(f"\n  Pending items (first 10):")
        for item in queue[:10]:
            src_short = item["source"].replace("/storage/emulated/0/pixel8a/", "~/")
            dst_short = item["dest"].replace("/storage/emulated/0/pixel8a/", "~/")
            print(f"    [{item['label']:12s}] {item['filename']}")
            print(f"                  {src_short}")
            print(f"              →   {dst_short}")
    print()


def print_pressure_report(queue, manifest):
    """Dedicated pressure report: breakdown by label and feed, with queue preview."""
    pressure_color = {
        "HIGH":   "*** HIGH PRESSURE ***",
        "MEDIUM": "~~ MEDIUM PRESSURE ~~",
        "LOW":    "-- low pressure --",
    }
    total    = manifest["queue_depth"]
    capacity = cfg.MAX_PER_RUN
    cycles   = -(-total // capacity) if total else 0          # ceiling div
    held     = max(total - capacity, 0)
    by_label = Counter(item["label"] for item in queue)
    by_feed  = Counter(item["feed"]  for item in queue)

    print(f"\n╔═══ PIXELATOR PRESSURE REPORT ══════════════════════════╗")
    print(f"  Time         : {timestamp()}")
    print(f"  Queue Depth  : {total} item(s)")
    print(f"  Pressure     : {pressure_color.get(manifest['pressure'], manifest['pressure'])}")
    print(f"  Threshold    : {cfg.PRESSURE_THRESHOLD} (HIGH above this)")
    print(f"  Capacity/Run : {capacity} item(s)")
    print(f"  Runs to Clear: ~{cycles} burst(s)")
    print(f"  Held/Burst   : {held} item(s) remain after one run")
    print(f"")
    print(f"  By Label:")
    if by_label:
        for label, count in sorted(by_label.items(), key=lambda x: -x[1]):
            bar = "█" * min(count, 30)
            print(f"    {label:15s} {count:4d}  {bar}")
    else:
        print("    (queue is empty)")
    print(f"")
    print(f"  By Feed:")
    for feed, count in sorted(by_feed.items(), key=lambda x: -x[1]):
        feed_short = feed.replace("/storage/emulated/0/pixel8a/", "~/")
        print(f"    {count:4d}  {feed_short}")
    if total:
        preview = ", ".join(item.get("filename", "?") for item in queue[:3])
        print(f"")
        print(f"  Queue head   : {preview}")
        if total > 3:
            print(f"  Queue tail   : ... +{total - 3} more item(s)")
    print(f"╚═══════════════════════════════════════════════════════════╝")
    print()


def print_run_summary(entries, copy_mode=False):
    success = sum(1 for e in entries if e["status"] == "SUCCESS")
    errors  = sum(1 for e in entries if e["status"] == "ERROR")
    dry     = sum(1 for e in entries if e["status"] == "SIMULATED")
    verb = "copied" if copy_mode else "moved"
    print(f"\n  ✓ Processed : {success} items {verb}")
    if dry:
        print(f"  ~ Simulated : {dry} items (dry run)")
    if errors:
        print(f"  ✗ Errors    : {errors} items failed")
    print(f"  Log         : {cfg.LOG_FILE}")
    print(f"\n  ∰◊€π¿🌌∞  Quality First. Enjoy the Journey.\n")


# ─── Main Run ─────────────────────────────────────────────────────────────────

def run_cycle(dry_run=False, status_only=False, pressure_only=False):
    print(f"\n  PIXELATOR AGENT v{VERSION} — navigo nexusuxen")
    print(f"  PIXEL8 Platform | Eric Pace (@eaprime1)")
    print(f"  {'─' * 52}")

    # Scan
    queue = scan_feeds()
    manifest = update_queue_manifest(queue)

    if pressure_only:
        print_pressure_report(queue, manifest)
        return

    if status_only:
        print_status(queue, manifest, dry_run=dry_run)
        return

    print_status(queue, manifest, dry_run=dry_run)

    if not queue:
        print("  Queue is empty. All feeds clear. 🌌\n")
        return

    # Process up to MAX_PER_RUN (one hertz burst)
    batch = queue[:cfg.MAX_PER_RUN]
    remaining = len(queue) - len(batch)

    print(f"  Processing {len(batch)} item(s)"
          f"{' (dry run)' if dry_run else ''}...\n")

    custody_entries = []
    for item in batch:
        entry = process_item(item, dry_run=dry_run, copy_mode=cfg.COPY_NOT_MOVE)
        custody_entries.append(entry)
        status_icon = {"SUCCESS": "✓", "SIMULATED": "~", "ERROR": "✗"}.get(entry["status"], "?")
        print(f"  {status_icon} [{entry['label']:12s}] {item['filename']}")

    if remaining > 0:
        print(f"\n  ↓ {remaining} item(s) remain in queue (pressure held — run again to release)")

    # Log chain of custody
    append_custody_log(custody_entries)

    # Update manifest with remaining queue
    update_queue_manifest(queue[cfg.MAX_PER_RUN:])

    print_run_summary(custody_entries, copy_mode=cfg.COPY_NOT_MOVE)


# ─── Entry Point ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="PIXEL8 Pixelator Agent — Device as Agent"
    )
    parser.add_argument("--dry-run",    action="store_true", help="Simulate only, no moves")
    parser.add_argument("--status",     action="store_true", help="Show queue status and exit")
    parser.add_argument("--pressure",   action="store_true", help="Show pressure report and exit")
    parser.add_argument("--interval",   type=int, default=None,
                        help="Run every N seconds (overrides TRIGGER_MODE)")
    args = parser.parse_args()

    dry_run = args.dry_run or cfg.DRY_RUN

    if args.interval:
        print(f"\n  Pixelator running on {args.interval}s interval. Ctrl+C to stop.")
        try:
            while True:
                run_cycle(dry_run=dry_run)
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n  Pixelator stopped. Sails furled. ∰\n")
    else:
        run_cycle(dry_run=dry_run, status_only=args.status, pressure_only=args.pressure)


if __name__ == "__main__":
    main()
