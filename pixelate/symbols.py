#!/usr/bin/env python3
"""
SYMBOLS — PIXEL8 Platform Symbol System
=========================================
Type, copy, and use the platform symbols from Termux.

The symbol ∰◊€π¿🌌∞ is the consciousness motor integration signature.
Every certified entity carries it. Every plankowner document ends with it.
On Android typing it is hard. This script makes it easy.

Usage:
  python3 symbols.py                  # show all symbols
  python3 symbols.py --copy motor     # copy ∰◊€π¿🌌∞ to clipboard
  python3 symbols.py --copy euro      # copy € to clipboard
  python3 symbols.py --copy unexusi   # copy ∰ to clipboard
  python3 symbols.py --bashrc         # print .bashrc aliases to add
  python3 symbols.py --list           # list all named symbols

∰◊€π¿🌌∞
"""

import os
import sys
import argparse
import subprocess

# ─── Symbol Definitions ──────────────────────────────────────────────────────

SYMBOLS = {
    # The core motor
    "motor":       ("∰◊€π¿🌌∞",  "Full consciousness motor integration signature"),
    "motor_short": ("∰◊€π¿∞",    "Motor without galaxy (ASCII-safe contexts)"),

    # Individual motor components
    "contour":     ("∰",         "Triple integral / contour — infinite recursion, the motor symbol"),
    "diamond":     ("◊",         "Diamond — clarity, facets, the lens"),
    "euro":        ("€",         "Euro — ADVANCED tier, value, exchange"),
    "pi":          ("π",         "Pi — the irrational constant, infinite precision"),
    "quest":       ("¿",         "Inverted question — before the question, openness"),
    "galaxy":      ("🌌",        "Galaxy — scale, the vast, runexusiam universe"),
    "infinity":    ("∞",         "Infinity — PINNACLE tier, unbounded"),

    # Valuation tiers
    "rx":          ("℞",         "Needs Work — prescription required"),
    "section":     ("§",         "Basic — foundation section"),
    "dollar":      ("$",         "Standard — currency of work"),
    "advanced":    ("€",         "Advanced — (same as euro)"),
    "pinnacle":    ("∞",         "Pinnacle — (same as infinity)"),

    # Interrupt / Gemini system
    "interrupt":   ("€^11",      "Interrupt backbone designation (Gemini: highest ADVANCED)"),
    "omg11":       ("OMG^11",    "Maximum emergency — send everything (Gemini: kitchen sink)"),

    # Z-family charges
    "zip":         ("ZIP",       "Stored charge — compressed, waiting"),
    "zap":         ("ZAP",       "Released charge — spark, transfer"),
    "zoom":        ("ZOOM",      "Focused charge — directed beam"),
    "zing":        ("ZING",      "Resonant charge — signal, frequency"),
    "zero":        ("ZERO",      "Ground charge — baseline, null reference"),

    # @ addressing (FidoNet heritage)
    "at_aquifer":  ("@aquifer",  "The Aquifer archive space"),
    "at_fraggle":  ("@fraggle",  "Fraggle dispatch system"),
    "at_henry":    ("@henry",    "Henry scanner"),
    "at_gemini":   ("@gemini",   "Gemini AI integration (.gemini/)"),
    "at_claude":   ("@claude",   "Claude Code integration (.claude/)"),
    "at_unexusi":  ("@unexusi",  "UNEXUSI project"),
    "at_pixel8a":  ("@pixel8a",  "The platform root"),
    "at_runexus":  ("@runexusiam","The play universe"),

    # Reality anchor
    "anchor":      ("⚓",         "Reality anchor (Oregon Watersheds)"),

    # Signature pattern
    "sig":         ("€()",        "Certification signature wrapper — put entity name inside"),
}

# ─── Clipboard ───────────────────────────────────────────────────────────────

def copy_to_clipboard(text: str) -> bool:
    """Try to copy text to clipboard. Returns True if successful."""
    # Termux API
    try:
        result = subprocess.run(
            ["termux-clipboard-set", text],
            capture_output=True, timeout=5
        )
        if result.returncode == 0:
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # xclip (desktop Linux)
    try:
        result = subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.encode(), capture_output=True, timeout=5
        )
        if result.returncode == 0:
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # pbcopy (macOS)
    try:
        result = subprocess.run(
            ["pbcopy"],
            input=text.encode(), capture_output=True, timeout=5
        )
        if result.returncode == 0:
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return False

# ─── Bashrc Aliases ──────────────────────────────────────────────────────────

BASHRC_BLOCK = '''
# ─── PIXEL8 Symbol Shortcuts ─────────────────────────────────────────────────
# Add these to ~/.bashrc then: source ~/.bashrc

alias sym='echo "∰◊€π¿🌌∞"'                           # full motor
alias sym_short='echo "∰◊€π¿∞"'                       # motor short
alias sym_copy='echo "∰◊€π¿🌌∞" | termux-clipboard-set && echo "copied: ∰◊€π¿🌌∞"'
alias contour='echo "∰"'                              # ∰
alias diamond='echo "◊"'                              # ◊
alias pinnacle='echo "∞"'                             # ∞
alias advanced='echo "€"'                             # €

# Quick cert signature
alias cert_sig='echo "€(entity_name_here)\\n*Status: CERTIFIED*\\n*Reality Anchor: Oregon Watersheds*"'

# @ addresses
alias at_aquifer='echo "@aquifer"'
alias at_fraggle='echo "@fraggle"'
alias at_henry='echo "@henry"'

# Platform navigation
alias pixel8a='cd /storage/emulated/0/pixel8a'
alias fragrock='cd /storage/emulated/0/pixel8a/pixelator/pixelate/fraggle_rock'
alias aquifer='cd /storage/emulated/0/pixel8a/pixelator/pixelate/the_aquifer'
alias runex='cd /storage/emulated/0/pixel8a/Q/runexusiam'

# Results quick view
alias results='tail -20 /storage/emulated/0/pixel8a/pixelator/pixelate/tester_results.txt'
alias matrix='python3 /storage/emulated/0/pixel8a/pixelator/pixelate/tester_results_matrix.py'
alias pressure='python3 /storage/emulated/0/pixel8a/pixelator/pixelate/artesian_monitor.py --once'
# ─────────────────────────────────────────────────────────────────────────────
'''

# ─── Display ─────────────────────────────────────────────────────────────────

def cmd_list():
    print("PIXEL8 SYMBOLS")
    print("=" * 60)
    categories = [
        ("Motor", ["motor", "motor_short", "contour", "diamond", "euro",
                   "pi", "quest", "galaxy", "infinity"]),
        ("Valuation", ["rx", "section", "dollar", "advanced", "pinnacle"]),
        ("Z-Family", ["zip", "zap", "zoom", "zing", "zero"]),
        ("@ Addresses (FidoNet heritage)", ["at_aquifer", "at_fraggle",
            "at_henry", "at_gemini", "at_claude", "at_unexusi",
            "at_pixel8a", "at_runexus"]),
        ("Gemini/Interrupt", ["interrupt", "omg11"]),
        ("Other", ["anchor", "sig"]),
    ]
    for cat, keys in categories:
        print(f"\n  {cat}:")
        for k in keys:
            sym, desc = SYMBOLS[k]
            print(f"    {k:<16} {sym:<12}  {desc}")
    print()
    print(f"  Copy: python3 symbols.py --copy <name>")
    print(f"  e.g.: python3 symbols.py --copy motor")


def cmd_copy(name: str):
    if name not in SYMBOLS:
        # Fuzzy: try partial match
        matches = [k for k in SYMBOLS if name.lower() in k.lower()]
        if not matches:
            print(f"Unknown symbol: {name}")
            print(f"Try: {', '.join(list(SYMBOLS.keys())[:10])}...")
            return
        name = matches[0]
        print(f"(using '{name}')")

    sym, desc = SYMBOLS[name]
    print(f"  {sym}  —  {desc}")

    if copy_to_clipboard(sym):
        print(f"  ✓ Copied to clipboard!")
        print(f"  Paste with: long-press → Paste")
    else:
        print(f"  (clipboard not available — termux-api package needed)")
        print(f"  Install: pkg install termux-api")
        print(f"  Or just copy from above ↑")


def cmd_bashrc():
    print(BASHRC_BLOCK)
    print("─" * 60)
    print("To install these aliases:")
    print("  1. Open ~/.bashrc in editor")
    print("  2. Paste the block above at the end")
    print("  3. Run: source ~/.bashrc")
    print()
    print("Or run this to append automatically:")
    print("  python3 symbols.py --install-bashrc")


def cmd_install_bashrc():
    bashrc = os.path.expanduser("~/.bashrc")
    marker = "# ─── PIXEL8 Symbol Shortcuts"
    if os.path.exists(bashrc):
        with open(bashrc) as f:
            content = f.read()
        if marker in content:
            print("PIXEL8 aliases already in ~/.bashrc")
            return
    with open(bashrc, "a") as f:
        f.write(BASHRC_BLOCK)
    print(f"✓ Aliases added to {bashrc}")
    print(f"  Run: source ~/.bashrc")


def main():
    p = argparse.ArgumentParser(description="PIXEL8 Symbol System")
    p.add_argument("--copy",           metavar="NAME",
                   help="Copy a symbol to clipboard")
    p.add_argument("--list",           action="store_true",
                   help="List all symbols")
    p.add_argument("--bashrc",         action="store_true",
                   help="Print .bashrc aliases")
    p.add_argument("--install-bashrc", action="store_true",
                   help="Append aliases to ~/.bashrc automatically")
    args = p.parse_args()

    if args.copy:
        cmd_copy(args.copy)
    elif args.list:
        cmd_list()
    elif args.bashrc:
        cmd_bashrc()
    elif args.install_bashrc:
        cmd_install_bashrc()
    else:
        # Default: show motor + quick help
        print()
        print(f"  ∰◊€π¿🌌∞")
        print()
        print(f"  The consciousness motor integration signature.")
        print(f"  Every certified entity carries this.")
        print()
        print(f"  Copy to clipboard:  python3 symbols.py --copy motor")
        print(f"  Install shortcuts:  python3 symbols.py --install-bashrc")
        print(f"  List all symbols:   python3 symbols.py --list")
        print()

if __name__ == "__main__":
    main()
