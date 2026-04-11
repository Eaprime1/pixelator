#!/usr/bin/env python3
"""
ARTESIAN MONITOR
================
One Hertz system pressure logger for PIXEL8 platform.

Concept:
  An artesian well has head pressure from depth + geology.
  This system has head pressure from active processes + memory load.
  The monitor reads pressure at one hertz and logs it.

  Low pressure   = system is breathing
  Rising pressure = load building
  High pressure  = caution, reduce parallel ops
  Overflow       = something needs to yield

Usage:
  python3 artesian_monitor.py              # run until Ctrl+C
  python3 artesian_monitor.py --once       # single reading
  python3 artesian_monitor.py --tail 20   # show last 20 log entries
  python3 artesian_monitor.py --status    # current pressure + summary

Output: pixel8a/Q/hodie/quanta/one_hertz_collective/pressure_log.jsonl

€(artesian_monitor_v1)
Status: ACTIVE ENTITY
Reality Anchor: Oregon Watersheds
"""

import json
import os
import sys
import time
import datetime
import argparse

# ─── Configuration ───────────────────────────────────────────────────────────

LOG_PATH     = "/storage/emulated/0/pixel8a/Q/hodie/quanta/one_hertz_collective/pressure_log.jsonl"
RESULTS_PATH = "/storage/emulated/0/pixel8a/pixelator/pixelate/tester_results.txt"
MEMINFO      = "/proc/meminfo"
STAT         = "/proc/stat"

# Pressure thresholds (0–100 score)
THRESHOLD_CAUTION  = 60
THRESHOLD_HIGH     = 80
THRESHOLD_OVERFLOW = 95

# ─── Memory Reading ───────────────────────────────────────────────────────────

def read_meminfo():
    """Read /proc/meminfo and return key fields in MB."""
    fields = {}
    try:
        with open(MEMINFO, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2:
                    key = parts[0].rstrip(":")
                    val = int(parts[1])  # kB
                    fields[key] = val
    except Exception:
        return {}

    total     = fields.get("MemTotal", 0)
    available = fields.get("MemAvailable", 0)
    used      = total - available

    return {
        "total_mb":     round(total / 1024, 1),
        "used_mb":      round(used / 1024, 1),
        "available_mb": round(available / 1024, 1),
        "used_pct":     round((used / total * 100) if total else 0, 1),
    }

# ─── CPU Reading ─────────────────────────────────────────────────────────────

_last_cpu = None

def read_cpu_pct():
    """Return CPU usage % since last call (delta-based, like top)."""
    global _last_cpu
    try:
        with open(STAT, "r") as f:
            line = f.readline()
        parts = line.split()
        # user, nice, system, idle, iowait, irq, softirq
        vals = [int(x) for x in parts[1:8]]
        idle    = vals[3] + vals[4]   # idle + iowait
        total   = sum(vals)

        if _last_cpu is None:
            _last_cpu = (total, idle)
            return 0.0

        prev_total, prev_idle = _last_cpu
        _last_cpu = (total, idle)

        d_total = total - prev_total
        d_idle  = idle  - prev_idle

        if d_total == 0:
            return 0.0
        return round((1.0 - d_idle / d_total) * 100, 1)
    except Exception:
        return 0.0

# ─── Process Count ────────────────────────────────────────────────────────────

def count_python_procs():
    """Count running Python processes via /proc."""
    count = 0
    try:
        for pid in os.listdir("/proc"):
            if not pid.isdigit():
                continue
            cmdline_path = f"/proc/{pid}/cmdline"
            try:
                with open(cmdline_path, "rb") as f:
                    cmd = f.read().replace(b"\x00", b" ").decode(errors="ignore")
                if "python" in cmd.lower():
                    count += 1
            except Exception:
                continue
    except Exception:
        pass
    return count

# ─── Pressure Score ──────────────────────────────────────────────────────────

def compute_pressure(mem, cpu_pct, py_procs):
    """
    Pressure score 0–100.
    Weighted: memory 50%, CPU 35%, process count 15%.
    """
    mem_score  = mem.get("used_pct", 0)            # already 0-100
    cpu_score  = min(cpu_pct, 100)
    proc_score = min(py_procs * 10, 100)            # 10 procs = 100

    score = (mem_score * 0.50) + (cpu_score * 0.35) + (proc_score * 0.15)
    return round(score, 1)

def pressure_label(score):
    if score >= THRESHOLD_OVERFLOW:  return "OVERFLOW"
    if score >= THRESHOLD_HIGH:      return "HIGH"
    if score >= THRESHOLD_CAUTION:   return "CAUTION"
    return "BREATHING"

def pressure_symbol(score):
    if score >= THRESHOLD_OVERFLOW:  return "∰"   # overflow
    if score >= THRESHOLD_HIGH:      return "¿"   # high
    if score >= THRESHOLD_CAUTION:   return "€"   # caution
    return "◊"                                    # breathing

# ─── Reading ─────────────────────────────────────────────────────────────────

def take_reading():
    """Take one pressure reading and return as dict."""
    mem       = read_meminfo()
    cpu_pct   = read_cpu_pct()
    py_procs  = count_python_procs()
    pressure  = compute_pressure(mem, cpu_pct, py_procs)
    label     = pressure_label(pressure)

    return {
        "ts":         datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3],
        "pressure":   pressure,
        "label":      label,
        "symbol":     pressure_symbol(pressure),
        "mem_used_pct":   mem.get("used_pct", 0),
        "mem_used_mb":    mem.get("used_mb", 0),
        "mem_total_mb":   mem.get("total_mb", 0),
        "cpu_pct":        cpu_pct,
        "python_procs":   py_procs,
    }

# ─── Display ─────────────────────────────────────────────────────────────────

def display_reading(r, verbose=True):
    sym  = r["symbol"]
    p    = r["pressure"]
    lbl  = r["label"]
    bar_filled = int(p / 5)
    bar  = "█" * bar_filled + "░" * (20 - bar_filled)

    if verbose:
        print(f"\r{sym} [{bar}] {p:5.1f}  {lbl:<10}  "
              f"MEM:{r['mem_used_pct']:4.1f}%  "
              f"CPU:{r['cpu_pct']:4.1f}%  "
              f"PY:{r['python_procs']:2d}", end="", flush=True)
    else:
        print(f"{sym} {p:5.1f} {lbl}")

# ─── Logging ─────────────────────────────────────────────────────────────────

def ensure_log_dir():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

def write_log(r):
    ensure_log_dir()
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(r) + "\n")

def write_results(r, label: str = "reading"):
    """
    Append a human-readable line to tester_results.txt.
    History builds here — each run adds to the record, never overwrites.
    """
    os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)
    ts   = r.get("ts", "?")
    sym  = r.get("symbol", "?")
    p    = r.get("pressure", 0)
    lbl  = r.get("label", "?")
    mem  = r.get("mem_used_pct", 0)
    cpu  = r.get("cpu_pct", 0)
    py   = r.get("python_procs", 0)
    line = (
        f"[{ts}] {label:<12} {sym} {p:5.1f} {lbl:<10} "
        f"MEM:{mem:4.1f}% CPU:{cpu:4.1f}% PY:{py}\n"
    )
    with open(RESULTS_PATH, "a") as f:
        f.write(line)

# ─── Commands ────────────────────────────────────────────────────────────────

def cmd_once():
    """Single reading, print and log."""
    # Warm the CPU delta
    read_cpu_pct()
    time.sleep(0.5)
    r = take_reading()
    display_reading(r, verbose=False)
    write_log(r)
    write_results(r, label="once")

def cmd_tail(n=20):
    """Show last N log entries."""
    ensure_log_dir()
    if not os.path.exists(LOG_PATH):
        print("No log yet.")
        return
    with open(LOG_PATH, "r") as f:
        lines = f.readlines()
    for line in lines[-n:]:
        try:
            r = json.loads(line.strip())
            ts   = r.get("ts", "?")
            sym  = r.get("symbol", "?")
            p    = r.get("pressure", 0)
            lbl  = r.get("label", "?")
            mem  = r.get("mem_used_pct", 0)
            cpu  = r.get("cpu_pct", 0)
            py   = r.get("python_procs", 0)
            print(f"  {ts}  {sym} {p:5.1f}  {lbl:<10}  MEM:{mem:4.1f}%  CPU:{cpu:4.1f}%  PY:{py}")
        except Exception:
            print(f"  {line.strip()}")

def cmd_status():
    """Current reading + log summary."""
    print("PIXEL8 ARTESIAN MONITOR")
    print("─" * 50)

    # current
    read_cpu_pct()
    time.sleep(0.5)
    r = take_reading()
    print(f"  Pressure : {r['symbol']} {r['pressure']} — {r['label']}")
    print(f"  Memory   : {r['mem_used_mb']}MB / {r['mem_total_mb']}MB ({r['mem_used_pct']}%)")
    print(f"  CPU      : {r['cpu_pct']}%")
    print(f"  Python   : {r['python_procs']} processes")
    write_log(r)

    # log summary
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            lines = f.readlines()
        if lines:
            entries = [json.loads(l) for l in lines if l.strip()]
            labels = [e.get("label") for e in entries]
            write_results(r, label="status")
            print(f"\n  Log      : {len(entries)} readings")
            for lbl in ["OVERFLOW", "HIGH", "CAUTION", "BREATHING"]:
                c = labels.count(lbl)
                if c:
                    pct = round(c / len(labels) * 100)
                    print(f"  {lbl:<12}: {c:4d}  ({pct}%)")
            print(f"  Since    : {entries[0].get('ts', '?')}")

def cmd_run():
    """Continuous one-hertz monitor until Ctrl+C."""
    print("PIXEL8 ARTESIAN MONITOR  (Ctrl+C to stop)")
    print("  ◊ BREATHING  €CAUTION  ¿HIGH  ∰OVERFLOW")
    print()

    # Warm CPU
    read_cpu_pct()
    time.sleep(1)

    readings_since_log = 0

    try:
        while True:
            r = take_reading()
            display_reading(r)
            readings_since_log += 1

            # Log every 60 readings (1/minute) or on CAUTION+
            if readings_since_log >= 60 or r["pressure"] >= THRESHOLD_CAUTION:
                write_log(r)
                write_results(r, label="monitor")
                readings_since_log = 0

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nMonitor stopped. ◊")

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="PIXEL8 Artesian Monitor")
    parser.add_argument("--once",   action="store_true", help="Single reading")
    parser.add_argument("--tail",   type=int, metavar="N", help="Show last N log entries")
    parser.add_argument("--status", action="store_true", help="Status + summary")
    args = parser.parse_args()

    if args.once:
        cmd_once()
    elif args.tail is not None:
        cmd_tail(args.tail)
    elif args.status:
        cmd_status()
    else:
        cmd_run()

if __name__ == "__main__":
    main()
