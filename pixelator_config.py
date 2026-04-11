"""
pixelator_config.py
PIXEL8 Pixelator Agent — Configuration
User: Eric Pace (@eaprime1)
Entity: navigo suxenexus (Eric) / navigo nexusuxen (Claude)

Configure feeds, routing rules, and pressure settings here.
The agent reads this file on every run — edit anytime.
"""

import os

# ─── Base Paths ───────────────────────────────────────────────────────────────
BASE = "/storage/emulated/0/pixel8a"

PIXELATOR_ROOT   = f"{BASE}/pixelator"
PIXELATE_DIR     = f"{PIXELATOR_ROOT}/pixelate"       # active jobs, missions
PIXELATING_DIR   = f"{PIXELATOR_ROOT}/pixelating"     # sorting queue (default landing)
VETTING_INBOX    = f"{PIXELATOR_ROOT}/vetting/inbox"  # quality gate
VETTING_APPROVED = f"{PIXELATOR_ROOT}/vetting/approved"
DOMOS_DIR        = f"{PIXELATOR_ROOT}/domos"

Q_DIR            = f"{BASE}/Q"
HODIE_DIR        = f"{Q_DIR}/hodie"
PLEXUS_DIR       = f"{HODIE_DIR}/plexus"
ERIC_REQUESTS    = f"{Q_DIR}/.eric"                   # external creation requests
VISIONHAVEN_DIR  = f"{BASE}/visionhaven"

# ─── Artesian Feed ────────────────────────────────────────────────────────────
# Universal project feed. Natural head pressure. Everything flows through here.
# Drop anything into artesian/ — Pixelator routes it to the right destination.
ARTESIAN_DIR = f"{PIXELATOR_ROOT}/artesian"

# ─── Feed Directories ─────────────────────────────────────────────────────────
# These are the SOURCE directories Pixelator watches for new content.
# Artesian is the universal intake — highest priority, checked first.
FEEDS = [
    ARTESIAN_DIR,                     # ← UNIVERSAL FEED (artesian well, natural pressure)
    f"{BASE}/pixelate",               # top-level pixelate (outside pixelator/)
    f"{PIXELATOR_ROOT}/pixelating",   # sorting queue
    f"{VETTING_INBOX}",               # vetting inbox
    f"{ERIC_REQUESTS}",               # Eric's external creation requests
    # Add more feeds here:
    # f"{BASE}/qdrive",               # Google Drive landing zone
]

# ─── Routing Rules ────────────────────────────────────────────────────────────
# Format: {pattern: destination}
# Patterns match filename (case-insensitive). First match wins.
# Use "*" as catch-all at the end.
ROUTING_RULES = [
    # Vetting → approved items go to pixelate (ready to work)
    {"pattern": "approved_",        "dest": PIXELATE_DIR,    "label": "pre-approved"},

    # Entity/consciousness files → Q entity folders
    {"pattern": "entity",           "dest": f"{HODIE_DIR}/quanta", "label": "entity"},
    {"pattern": "consciousness",    "dest": f"{HODIE_DIR}/quanta", "label": "entity"},

    # CODEX files → codex hub
    {"pattern": "codex",            "dest": f"{Q_DIR}/codex_consolidated", "label": "codex"},
    {"pattern": "prime",            "dest": f"{Q_DIR}/runexusiam/PRIME",   "label": "prime"},

    # Conversations / seeds → visionhaven
    {"pattern": "conversation",     "dest": VISIONHAVEN_DIR, "label": "seed"},
    {"pattern": "seed",             "dest": VISIONHAVEN_DIR, "label": "seed"},

    # Scripts → Q scripts hub (if exists)
    {"pattern": ".py",              "dest": f"{Q_DIR}/AI-Projects", "label": "script"},

    # Markdown docs → pixelating for review first
    {"pattern": ".md",              "dest": PIXELATING_DIR,  "label": "doc"},

    # Default catch-all → pixelating (sorting queue)
    {"pattern": "*",                "dest": PIXELATING_DIR,  "label": "unsorted"},
]

# ─── Queue Pressure Settings ──────────────────────────────────────────────────
# ONE HERTZ philosophy: controlled, deliberate releases.
# MAX_PER_RUN: max files processed per invocation (pressure valve)
# PRESSURE_THRESHOLD: queue depth that triggers an alert
MAX_PER_RUN        = 10      # one hertz burst size
PRESSURE_THRESHOLD = 50      # alert if queue exceeds this

# ─── Trigger Mode ─────────────────────────────────────────────────────────────
# "manual"   → run with: python3 pixelator_agent.py
# "interval" → run with: python3 pixelator_agent.py --interval 60  (seconds)
# "watch"    → continuous file-system watch (requires: pip install watchdog)
TRIGGER_MODE = "manual"
DEFAULT_INTERVAL = 60  # seconds (used if TRIGGER_MODE = "interval")

# ─── Chain of Custody ─────────────────────────────────────────────────────────
LOG_FILE         = f"{PIXELATOR_ROOT}/pixelator_log.json"
QUEUE_MANIFEST   = f"{PIXELATOR_ROOT}/pixelator_queue.json"
CHAIN_OF_CUSTODY = True   # always log moves — never silent

# ─── Safety Settings ──────────────────────────────────────────────────────────
DRY_RUN     = False    # True = show what WOULD happen, don't actually move
COPY_NOT_MOVE = False  # True = copy files (conservation bias), False = move
SKIP_HIDDEN = True     # skip dotfiles and hidden directories
