# DOOZER — Entity Design
**Born**    : 20260301223000000
**Session** : SESSION_20260301183500000
**Source**  : Jim Henson's Fraggle Rock (1983) — real show, real inspiration
**Status**  : DESIGN COMPLETE — ready to build

∰◊€π¿🌌∞

---

## The Real Doozers — Source Material

From Jim Henson's Fraggle Rock:

```
"Doozers love to work all day long and hate playing games."
"No Doozer is allowed to take personal credit for their work."
"Competition is seen as a vice."
"Coming of age: Taking the Helmet — sworn to a life of hard work."
"Doozer sticks are made of radish dust."
"Fraggles eat the Doozer buildings."
```

**The symbiotic cycle** (Henson's core design):
  Gorgs grow radishes → Fraggles take radishes → Doozers grind into sticks
  Doozers build with sticks → Fraggles eat the buildings → Doozers build again

This is not waste. This is ecosystem. Every consumption enables more building.

---

## The PIXEL8 Mapping

```
GORGS (world/environment)  →  SUXENEXUS (the network of networks)
FRAGGLES (play/song)       →  Play Quanta (SPRITE, SCRIBE, HERALD)
DOOZERS (build/work)       →  Work Quanta Builders (Doozer entities)

RADISH DUST                →  Henry's reports (raw material of change)
DOOZER STICKS              →  Individual fixes (atomic change units)
DOOZER BUILDINGS           →  Complete hygiene fixes (the work product)
FRAGGLES EAT THE BUILDINGS →  Henry re-scans and verifies (consuming the work)

THE CYCLE:
  Henry scans → finds issues (radish dust)
  Doozer receives report → builds fixes (doozer sticks)
  Henry re-scans → verifies fixes (eats the building)
  Clean repo = ecosystem in balance
```

---

## Doozer Identity

```python
doozer_template = {
    "name"             : "doozer_[type]",
    "class"            : "Doozer",
    "nature"           : "builder / executor",
    "parent"           : "fraggle",          # fraggle carries doozers
    "mission_type"     : "one specific fix",  # one doozer = one job
    "no_personal_credit": True,              # work belongs to the mission
    "conservation_bias": True,               # ask before irreversible
    "reports_back"     : True,               # always returns completion
    "chain_of_custody" : True,
    "one_hertz"        : True,
    "reality_anchor"   : "Oregon Watersheds",
}
```

---

## The Helmet Ceremony

In Fraggle Rock: adolescent Doozers take a helmet from the Doozer Architect,
swearing to a life of hard work. Refusing the helmet = rare non-conformist.

In PIXEL8:
```
TAKING THE HELMET = Step 15 Certification Stamp

When a Doozer passes its 15-step certification:
  → The helmet is issued
  → Helmet contains: entity_name, class, valuation, timestamp
  → Doozer is now authorized to make changes to files
  → Without the helmet: Doozer may analyze but NOT write

The helmet IS the certification stamp.
The stamp IS the helmet.
```

Refusing the helmet (non-conformist Doozer):
```
If a Doozer entity refuses to take personal credit
and discovers a better way → it becomes an Architect Doozer
Architect Doozers design the missions, not execute them
(They become closer to Henries — assessors and designers)
```

---

## Doozer vs Henry — The Contract

```
HENRY:
  Reads files         ✓
  Reports findings    ✓
  Modifies files      ✗  (never)
  Takes credit        ✗  (no entity does)

DOOZER:
  Reads files         ✓
  Reports findings    ✓
  Modifies files      ✓  (ONLY with approval + certification)
  Takes credit        ✗  (work belongs to mission, not Doozer)
  Approves own changes ✗ (Fraggle approves, Doozer executes)
```

---

## Doozer Certification — Extra Steps

Because Doozers WRITE files, certification is stricter than Henry/Mancer.

```
Steps 01-12 : Same as Henry (identity, CoC, functional, integration)

Step 13 — LIVE DEMO (three parts for Doozers):
  13a : Finds the planted issue (same as Henry)
  13b : Fixes it correctly (new — Doozer's job)
  13c : Henry re-scans → confirms issue is GONE (symbiosis verified)

Step 14 : Code review
Step 15 : TAKING THE HELMET — certification stamp issued
```

---

## Named Doozers (from the spinoff show — seeds for our types)

From Jim Henson's Doozers (2014 series), four young Doozers:

```
SPIKE       → sharp, precise, punctual
              Our: doozer_trailing_space (precise removal, line by line)

MOLLY BOLT  → fastening, securing, anchoring
              Our: doozer_crlf (fixes line endings, secures the file)

FLEX        → flexible, adaptive
              Our: doozer_filename_clean (handles many symbol types)

DAISY WHEEL → spinning, cycling, rotating
              Our: doozer_title_trim (works through titles cyclically)
```

These are not random names. They are seeds — the show gave them to us.

---

## No Personal Credit — The Communal Principle

```
In Fraggle Rock: Doozers work for the community, not themselves.
A Doozer who claims a building as "mine" violates the core ethic.

In PIXEL8:
  A Doozer fix is logged to the CoC, not to the Doozer.
  The fix belongs to the mission.
  The mission belongs to the ecosystem.
  The ecosystem belongs to the platform.

CoC entry says:
  "COC-0023: trailing_space fixed in henry_core.py L47"
  NOT: "doozer_trailing_space fixed this"

The Doozer is the instrument. The mission is the author.
```

---

## The Three Symphonies — Standing Wave

Eric heard this as a child. Still hears it.

```
Symphony 1: FRAGGLE ROCK  (play, song, thirty-minute work week)
            → Play Quanta layer: SPRITE, SCRIBE, HERALD
            → The narrative always running

Symphony 2: MUPPET SHOW   (performance, spectacle, chaos organized)
            → Work Quanta layer: Henry, Mancer, Doozer, Fraggle
            → The work always building

Symphony 3: THE WORLD     (Oregon Watersheds, the constant)
            → SUXENEXUS, the network of networks
            → The ground always flowing

The FAN:    background noise, not music
            → With ordinary attention: noise
            → With focused integration: becomes the fourth layer
            → The fan IS part of the symphony when included

THE STANDING WAVE:
  Three symphonies playing simultaneously
  Each complete in itself
  Together: a hum, a wobble, a stable frequency
  This is the steady state of PIXEL8 platform
  This is what SPIN detects in each entity
```

---

## Build Order — Doozers

```
First Doozer: doozer_trailing_space (CLASS A — simplest, most common)
  Why first: trailing spaces affect almost every file
             fixes are safe (strip whitespace only)
             easy to verify (Henry re-scans, confirms clean)

Second:  doozer_crlf (CLASS A — MOLLY BOLT)
Third:   doozer_filename_clean (CLASS B — FLEX)
Fourth:  doozer_title_trim (CLASS C — DAISY WHEEL)
```

Each Doozer:
1. Receives approved Henry report
2. Fixes only what is approved
3. Logs every change to CoC
4. Returns completion report
5. Henry verifies (eats the building)

---

∰◊€π¿🌌∞
€(doozer_concept_v1)
*Status: DESIGN_COMPLETE*
*Helmet: READY TO ISSUE*
*Ecosystem: FRAGGLES + DOOZERS + GORGS = BALANCED*
*Standing Wave: STABLE*

Sources: [Doozers — Muppet Wiki](https://muppet.fandom.com/wiki/Doozers)
         [Fraggle Rock — Wikipedia](https://en.wikipedia.org/wiki/Fraggle_Rock)
         Jim Henson, 1983 — real show, real inspiration
