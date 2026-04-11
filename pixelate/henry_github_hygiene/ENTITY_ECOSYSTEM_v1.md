# ENTITY ECOSYSTEM — Extended Architecture
**Born**: 20260301185500000
**Session**: SESSION_20260301183500000
**Extends**: FRAGGLE_DOOSER_ARCHITECTURE.md
**Status**: DESIGN EXPANSION — Sphincter Aperture + Mancers

∰◊€π¿🌌∞

---

## Full Entity Ecosystem Map

```
                    ┌──────────────────────┐
                    │   SPHINCTER          │
                    │   APERTURE           │  ← intake gate
                    │   (open = liminal)   │  ← controls what enters
                    └──────────┬───────────┘
                               │ content flows in
                               ▼
          ╔═══════════════════════════════════════╗
          ║         LIMINAL SPACE                 ║
          ║    (fluid, between states)            ║
          ║                                       ║
          ║   ┌───────────┐   ┌───────────┐       ║
          ║   │  FRAGGLE  │   │  MANCERS  │       ║
          ║   │ (fluid)   │   │ (fluid)   │       ║
          ║   └─────┬─────┘   └─────┬─────┘       ║
          ║         │               │              ║
          ╚═════════╪═══════════════╪══════════════╝
                    │  deploy       │  deploy
                    ▼               ▼
          ┌─────────────┐   ┌─────────────┐
          │  DOOSERS    │   │  MANCER     │
          │  (solid)    │   │  INSTANCES  │
          │  builders   │   │  (solid)    │
          └─────────────┘   └─────────────┘
                    ▲               ▲
                    └───────┬───────┘
                            │ reports + returns
                    ┌───────┴───────┐
                    │    HENRY      │
                    │  (assessor)   │
                    └───────────────┘
```

---

## SPHINCTER APERTURE

### Concept
The **sphincter** already exists in the platform:
`Q/gather(all)_sphincter/` — the gathering mechanism

The **aperture** is its state:
- **Open** (aperture) → liminal mode → content flows in → entities receive
- **Closed** → solid/momentum → no new intake → mission in progress

### Role in the Ecosystem
```
Sphincter OPEN (aperture state):
  → Henry reports enter
  → New missions arrive
  → Mancers receive queries
  → Fraggle receives content
  → All entities in LIMINAL / FLUID

Sphincter CLOSED (solid state):
  → Doosers working
  → Mancers executing
  → No new intake until mission complete
  → One hertz — one mission at a time
```

### Integration with Fraggle
```python
# Fraggle checks sphincter before entering liminal
if sphincter.is_open():
    fraggle.enter_liminal()
    fraggle.receive(henry_report)
    fraggle.select_dooser(mission_type)
    fraggle.close_sphincter()
    fraggle.launch_dooser()
    fraggle.enter_solid()
```

---

## MANCERS — The Parallel Entity Class

### Origin in Platform
`lsmancer` — already exists as a bash alias (custom list/read command)
Mancers are already native to PIXEL8 platform consciousness.

### Mancer Identity
```python
mancer_template = {
    "name": "[domain]mancer",
    "class": "Mancer",
    "nature": "practitioner",     # one who works through a domain
    "state": "fluid",             # fluid in liminal
    "deploy": "self",             # mancers ARE the instance
    "scope": "domain-specific",   # each mancer owns one domain
    "conservation_bias": True,
    "chain_of_custody": True,
}
```

### Mancers vs Doosers — The Key Difference
```
DOOSER:
  - Small, simple, one task
  - Deployed BY Fraggle
  - Executes one specific change
  - Returns home after mission

MANCER:
  - Domain expert practitioner
  - Self-deploys from liminal
  - Reads, interprets, transforms domain knowledge
  - Can spawn sub-mancers or Doosers
  - Fluid until engaged, solid while working
```

### Mancer Types (GitHub + Platform)
```
lsmancer          ← already exists — lists/reads structure
pathmancer        ← path analysis, deep path detection
trackmancer       ← tracking, chain of custody ledger
diffmancer        ← git diff analysis, change detection
commitmancer      ← commit message formatting + linting
repomancer        ← repository health + structure analysis
symbolmancer      ← consciousness symbol detection + mapping
floatmancer       ← liminal state management (meta-mancer)
```

### Mancer-Dooser Collaboration
```
repomancer scans → identifies Dooser missions
  → sends to Fraggle liminal
  → Fraggle deploys correct Dooser class
  → Dooser executes
  → trackmancer logs CoC entry
  → repomancer updates health score
```

---

## Fluid in Liminal — The Shared Property

Both **Fraggle** and **Mancers** share this core property:

### What "Fluid in Liminal" Means
```
LIMINAL = the threshold state
  (from Latin 'limen' = threshold, doorway)

FLUID = no fixed form
  → can become any shape needed
  → can route to any mission type
  → can carry any Dooser

When FLUID IN LIMINAL:
  → entity is RECEPTIVE (sphincter open)
  → entity is ADAPTIVE (can take any mission)
  → entity is POTENTIAL (not yet committed)
  → entity AWAITS signal to solidify

When signal received:
  → entity SOLIDIFIES (commits to one form)
  → sphincter CLOSES
  → mission BEGINS (one hertz)
  → entity becomes BEDROCK for that mission
```

### The Liminal Loop
```
FLUID (receive) → SOLID (execute) → FLUID (return) → ...

Each cycle = one hertz
Each hertz = one mission complete
Chain of custody = the thread through all cycles
```

---

## Complete Entity Class Table

| Class    | Name(s)        | Nature         | State        | Deploys      |
|----------|----------------|----------------|--------------|--------------|
| Henry    | henry_*        | Scanner/Reporter| Assessment  | Reports only |
| Fraggle  | fraggle        | Pinnacle/Carrier| Liminal→Solid| Doosers     |
| Dooser   | dooser_*       | Executor/Builder| Solid (work)| Changes      |
| Mancer   | *mancer        | Practitioner    | Liminal→Solid| Self/Doosers |
| Sphincter| sphincter      | Gate/Membrane   | Open/Closed  | Flow control |

---

## Build Sequence (Updated)

```
PHASE 1 — Foundation
  [ ] henry_core.py          scanner/reporter
  [ ] sphincter.py           aperture gate control
  [ ] fraggle.py             pinnacle + liminal state machine

PHASE 2 — Doosers (CLASS A first — whitespace)
  [ ] dooser_trailing_space.py
  [ ] dooser_crlf.py
  [ ] dooser_trailing_newline.py

PHASE 3 — Mancers
  [ ] lsmancer.py            (already exists as alias — formalize)
  [ ] repomancer.py          repo health analysis
  [ ] trackmancer.py         CoC ledger management
  [ ] diffmancer.py          git diff + change detection

PHASE 4 — Integration
  [ ] fraggle_ledger.json    live CoC tracking
  [ ] ecosystem_runner.py    orchestration entry point
```

---

## CoC Entry

```
COC-ECO-001
Timestamp  : 20260301185500000
Action     : Entity ecosystem expanded
Additions  : Sphincter Aperture + Mancer class + fluid-liminal model
Session    : SESSION_20260301183500000
Status     : DESIGN COMPLETE
Next       : Begin build phase — henry_core.py first
```

---

**∰◊€π¿🌌∞**
€(entity_ecosystem_v1)
*Status: ECOSYSTEM_DESIGNED*
*Sphincter: OPEN (we are in liminal)*
*Fraggle: FLUID — receiving design*
*Doosers: READY IN ROCK*
*Mancers: FLUID — awaiting domain assignment*

---
CoC-ECO-001: 20260301185500000 | DESIGN | entity_ecosystem_v1
