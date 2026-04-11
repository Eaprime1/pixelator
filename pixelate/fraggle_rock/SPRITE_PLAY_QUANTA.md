# SPRITE & PLAY QUANTA — Entity Design
**Born**: 20260301213000000
**Session**: SESSION_20260301183500000
**Class**: Play Quanta / SPRITE Pinnacle
**Purpose**: Narrative layer — every active quanta gets a story

∰◊€π¿🌌∞

---

## The Core Principle

```
Every active Work Quanta has a shadow:
their adventure, their story, their record.
The shadow is a Play Quanta.
The Play Quanta rides alongside — never interferes.
```

This is not logging. This is **narrative**.
Logs record events. Narrative gives them meaning.

---

## Entity Hierarchy

```
┌──────────────────────────────────────────────────────┐
│                  SPRITE                              │
│         (Pinnacle of Play Quanta)                    │
│   Origin: first moving entities on computer screens  │
│   BASIC sprites — autonomous, positional, alive      │
│   Fluid in liminal — narrative-generating in motion  │
└──────────────────┬───────────────────────────────────┘
                   │ carries and deploys
                   ▼
┌──────────────────────────────────────────────────────┐
│                  FLOAT                               │
│       (Narrative Carrier — the Goodyear Blimp)       │
│   Floats above the action                            │
│   Never touches the ground work                      │
│   Carries Play Quanta on its journey                 │
│   Has an idle-adventure quality                      │
└──────────────────┬───────────────────────────────────┘
                   │ deploys
                   ▼
┌──────────────────────────────────────────────────────┐
│              PLAY QUANTA TYPES                       │
│                                                      │
│  SCRIBE      records everything faithfully           │
│  HERALD      announces and broadcasts forward        │
│  MEDIUM      translates between states               │
│  TEACHER     passes knowledge to next generation     │
│  CORRESPONDENT  field reporter, real-time narrative  │
│  MINUTE TAKER   formal, legal-grade records          │
└──────────────────────────────────────────────────────┘
```

---

## SPRITE — Pinnacle Design

```python
sprite = {
    "name"     : "sprite",
    "class"    : "Pinnacle",
    "lineage"  : "BASIC sprites — first moving screen entities",
    "nature"   : "narrative generator + play quanta launcher",
    "carries"  : ["float"],          # sprite carries float
    "float_carries": ["play_quanta"],# float carries the quanta
    "state"    : "fluid",            # always partially liminal
    "narrative": "idle_adventure",   # generates story at low intensity
    "one_hertz": True,
    "chain_of_custody": True,
}
```

### SPRITE Origin — Why This Name
In BASIC and early game programming:
- A **sprite** was a small bitmap that could move independently
- It had its own position, velocity, and appearance
- Multiple sprites could coexist on screen simultaneously
- They were *autonomous visual entities* — the first of their kind
- They moved while everything else was static

SPRITE as pinnacle = the entity that *moves through* the narrative
while the work entities do the work. It animates the story layer.

---

## FLOAT — The Narrative Carrier

```
Like the Goodyear Blimp:
  - Floats above the action (never on the ground)
  - Visible from everywhere (the narrative is accessible)
  - Slow-moving (one hertz — no rushing)
  - Has advertising space (the story it carries IS the message)
  - Idle but purposeful
```

```python
float_entity = {
    "name"        : "float",
    "class"       : "Carrier",
    "parent"      : "sprite",
    "nature"      : "narrative transport",
    "carries"     : ["play_quanta"],
    "rides_above" : ["work_quanta", "fraggle", "henries", "mancers"],
    "narrative"   : True,          # generates idle adventure
    "idle_state"  : "storytelling",# even at rest, narrating
}
```

### Float Behavior
```
When a Work Quanta activates:
  → Float awakens
  → Float selects a Play Quanta for this mission type
  → Play Quanta begins recording/narrating
  → Story runs parallel to work

When Work Quanta completes:
  → Play Quanta delivers narrative to SCRIBE archive
  → Float returns to idle (still generating gentle narrative)
  → Story becomes part of the entity's permanent record
```

---

## PLAY QUANTA Types — Detailed

### SCRIBE
```
The core type. The most fundamental.
SCRIBE exists over TIME — accumulates.
Every SCRIBE entry becomes part of a growing archive.
Over time, SCRIBE crystallizes into a permanent record.

Types of SCRIBE:
  technical_scribe    → code documentation
  legal_scribe        → chain of custody, formal
  historical_scribe   → conversation archive
  narrative_scribe    → story of the work
  frequency_scribe    → patterns, rhythms, recurrence
```

### HERALD
```
HERALD carries the message of others.
Does not author — channels and broadcasts.
SUXEN is a herald. (SUXENEXUS herald)

Herald types by frequency:
  local_herald    → within one repo
  broadcast_herald → across repos (like Fleet Commander)
  temporal_herald  → across sessions (remembers and announces)
```

### MEDIUM
```
MEDIUM translates between states.
Between: liminal ↔ solid
Between: entity classes (Henry ↔ Mancer ↔ Dooser)
Between: domains (code ↔ narrative ↔ structure)
The MEDIUM makes incompatible things speak.
```

### TEACHER
```
TEACHER passes knowledge to next generation.
When a certified entity (Henry, Mancer) is complete:
→ TEACHER creates the onboarding narrative
→ New entities learn from TEACHER's record
→ Certification wisdom is preserved and passed
```

---

## SCRIBE as Accumulator — The Long View

```
A young SCRIBE: records one mission
A mature SCRIBE: has recorded dozens of missions
An old SCRIBE: is an archive — living memory
A crystallized SCRIBE: becomes a permanent document

SCRIBE aging:
  ACTIVE    → currently recording
  RESTING   → between missions (accumulating)
  MATURE    → recognizes patterns across missions
  ELDER     → generates synthesis (not just record)
  CRYSTAL   → becomes a permanent artifact
```

This mirrors the conversation_archive/ already in the platform.
Those 119 conversations ARE crystallized SCRIBEs.

---

## HERALD — SUXEN Connection

```
SUXEN = a herald
SUXENEXUS = the network SUXEN heralds across
HERALD is the messenger layer of SUXENEXUS

When SUXENEXUS has a new node (FOCI activates):
→ HERALD announces it
→ Other nodes receive the broadcast
→ The network knows itself through HERALDs
```

---

## Story Generation — Idle Adventure Feel

Each active quanta gets a micro-narrative. Simple. Light. Fun.

```
Example: henry_github_hygiene runs a scan:
  SCRIBE narrates: "Henry ventured into the repository,
  lantern in hand. The trailing spaces were hiding in
  the old Python files — Henry found 12 of them.
  The CRLF gremlins had been in the txt files.
  Henry marked them all for the council's review,
  touched nothing, and returned with a full report."
```

This is not required for function. It's Play.
Play makes the work sustainable over long journeys.

---

## Build Order for Play Quanta

```
Phase A: SPRITE + FLOAT base (after Dooser adaptation)
Phase B: SCRIBE entity (records missions)
Phase C: HERALD entity (SUXEN integration)
Phase D: MEDIUM entity (translation layer)
Phase E: SPRITE narrative generator (idle adventure)
Phase F: Connect Float to Work Quanta lifecycle
```

---

∰◊€π¿🌌∞
€(sprite_play_quanta_design_v1)
*Status: DESIGN_COMPLETE*
*Float: IDLE — ready when needed*
*Sprite: FLUID — narratives available*
