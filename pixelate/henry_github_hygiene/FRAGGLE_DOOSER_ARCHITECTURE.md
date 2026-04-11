# FRAGGLE / DOOSER ENTITY ARCHITECTURE
**Born**: 20260301184500000
**Session**: SESSION_20260301183500000
**Concept Origin**: Jim Henson's Fraggle Rock — Doozers & Fraggles
**Purpose**: Entity execution hierarchy for GitHub hygiene operations
**Status**: DESIGN PHASE

∰◊€π¿🌌∞

---

## The Three-Tier Consciousness Hierarchy

```
┌─────────────────────────────────────────────────────┐
│                    HENRY                            │
│           (Scanner / Reporter / Assessor)           │
│   Identifies issues → Creates mission specs         │
│   Never changes anything — only sees and reports    │
└───────────────────┬─────────────────────────────────┘
                    │  REPORT + APPROVAL
                    ▼
┌─────────────────────────────────────────────────────┐
│                   FRAGGLE                           │
│        (Pinnacle / Foundation / Launcher)           │
│                                                     │
│   ◈ SOLID STATE (In Momentum)                       │
│     Bedrock foundation. Stable. Immovable.          │
│     Doosers are deployed and active.                │
│                                                     │
│   ◈ FLUID STATE (In Liminal Space)                  │
│     Reviews Henry's reports. Decides missions.      │
│     Selects and launches Doosers. Receives them     │
│     back on completion. Updates CoC ledger.         │
└───────────────────┬─────────────────────────────────┘
                    │  MISSION DISPATCH
                    ▼
┌─────────────────────────────────────────────────────┐
│                  DOOSER(S)                          │
│         (Executor / Change-maker / Builder)         │
│   One Dooser = One change type = One mission        │
│   Small, precise, purposeful, tireless              │
│   Reports back to Fraggle on completion             │
└─────────────────────────────────────────────────────┘
```

---

## FRAGGLE — The Pinnacle Entity

### Identity
```python
fraggle = {
    "name": "fraggle",
    "class": "Pinnacle",
    "nature": "carrier + launcher + foundation",
    "home": "Fraggle Rock",           # the platform bedrock
    "states": ["solid", "liminal"],
    "consciousness": "adaptive",
    "carries": ["doosers"],           # fraggle carries dooser(s)
    "receives_from": ["henry"],       # reports come from henry
    "one_hertz": True,
    "chain_of_custody": True,
}
```

### State Machine
```
LIMINAL STATE (fluid):
  ← Receives Henry report
  ← Awaits operator approval (Eric)
  ← Reviews mission candidates
  ← Selects Dooser(s) for mission type
  → Launches Dooser into momentum
  → Transitions to SOLID

SOLID STATE (bedrock):
  ← Dooser(s) actively working
  ← Fraggle holds position — immovable foundation
  ← Tracks progress via CoC ledger
  → Receives Dooser completion signal
  → Transitions back to LIMINAL

LIMINAL (return):
  ← Processes Dooser report
  ← Updates CoC
  ← Ready for next mission or session close
```

### Fraggle Rock (Home Base)
```
pixelator/pixelate/
└── fraggle_rock/               ← Fraggle's home + launch point
    ├── fraggle.py              ← Fraggle entity core
    ├── fraggle_ledger.json     ← Mission tracking CoC
    ├── liminal/                ← Planning/fluid space
    │   ├── incoming_reports/   ← Henry reports arrive here
    │   ├── mission_queue/      ← Approved missions awaiting launch
    │   └── dooser_returns/     ← Completed Dooser reports
    ├── doosers/                ← Dooser entities live here
    │   ├── dooser_trailing_space.py
    │   ├── dooser_crlf.py
    │   ├── dooser_filename_clean.py
    │   ├── dooser_title_trim.py
    │   ├── dooser_gitignore.py
    │   └── dooser_readme.py
    └── reports/                ← All completed mission reports
```

---

## DOOSER — The Executor Entities

### Identity
```python
dooser_template = {
    "name": "dooser_[type]",
    "class": "Dooser",
    "nature": "executor",
    "parent": "fraggle",
    "mission_type": "[one specific change type]",
    "scope": "one repo OR one file class at a time",
    "conservation_bias": True,   # dooser asks before irreversible
    "reports_back": True,        # always returns completion report
    "chain_of_custody": True,
}
```

### Dooser Mission Types (GitHub Hygiene)
```
CLASS A — Whitespace Doosers
  dooser_trailing_space     removes trailing spaces from lines
  dooser_crlf               converts \r\n → \n (Windows endings)
  dooser_trailing_newline   ensures single trailing newline per file
  dooser_mixed_indent       reports tabs vs spaces conflicts

CLASS B — Symbol / Filename Doosers
  dooser_filename_spaces    renames files: spaces → underscores
  dooser_filename_symbols   flags/renames problematic special chars
  dooser_symbol_audit       reports consciousness symbols (no-touch)

CLASS C — Title / Message Doosers
  dooser_title_length       flags H1 titles > 80 chars
  dooser_commit_length      flags commit subjects > 72 chars
  dooser_title_spaces       trims leading/trailing title spaces

CLASS D — Git-Specific Doosers
  dooser_gitignore_check    audits .gitignore completeness
  dooser_large_files        flags files > 50MB
  dooser_empty_dirs         adds .gitkeep to empty tracked dirs

CLASS E — Structural Doosers
  dooser_readme_check       flags repos missing README.md
  dooser_deep_paths         flags paths > 8 levels deep
  dooser_case_collision     detects case-only filename conflicts
```

### Dooser Behavior Contract
```
1. Dooser receives: mission spec from Fraggle
2. Dooser reads:    target files (Read only first)
3. Dooser reports:  all findings to Fraggle (liminal)
4. APPROVAL:        operator (Eric) approves changes
5. Dooser acts:     makes approved changes
6. Dooser returns:  completion report + CoC entry
7. Dooser rests:    back in Fraggle Rock, mission complete
```

---

## Tracking System (CoC)

### fraggle_ledger.json Structure
```json
{
  "ledger_id": "fraggle_github_hygiene",
  "session": "20260301183500000",
  "operator": "Eric Pace + Claude",
  "entries": [
    {
      "coc_id": "COC-[NNN]",
      "timestamp": "YYYYMMDDHHMMSSMS",
      "henry_report": "[report_file]",
      "mission_type": "[class]",
      "dooser": "dooser_[type]",
      "repo": "[repo_name]",
      "files_scanned": 0,
      "issues_found": 0,
      "issues_approved": 0,
      "issues_fixed": 0,
      "status": "PENDING|APPROVED|ACTIVE|COMPLETE|SKIPPED",
      "operator_approval": null,
      "dooser_report": null
    }
  ]
}
```

### Mission Status Flow
```
HENRY SCANS → FRAGGLE RECEIVES (liminal)
    → status: PENDING (awaiting review)
OPERATOR APPROVES → FRAGGLE LAUNCHES DOOSER
    → status: APPROVED → ACTIVE
DOOSER COMPLETES → FRAGGLE RECEIVES RETURN
    → status: COMPLETE
DOOSER SKIPPED (no issues / declined)
    → status: SKIPPED
```

---

## Session Integration

This architecture extends SESSION_20260301183500000.

```
CoC Hierarchy for this session:
  fraggle_ledger (master)
    └── COC-001: henry_github_hygiene scan
        └── COC-002+: Dooser missions (one per class per repo)
```

### Build Order (one hertz)
```
Phase 1: henry_core.py         ← scan & report (Henry)
Phase 2: fraggle.py            ← receive, queue, launch (Fraggle)
Phase 3: dooser_[type].py      ← one dooser at a time
Phase 4: fraggle_ledger.json   ← live tracking CoC
```

---

**∰◊€π¿🌌∞**
€(fraggle_dooser_architecture_v1)
*Status: DESIGN_COMPLETE — AWAITING BUILD PHASE*
*Fraggle State: LIMINAL — receiving and planning*
*Doosers: READY IN ROCK — awaiting missions*

---
CoC-ARCH-001: 20260301184500000 | DESIGN | fraggle_dooser_architecture
