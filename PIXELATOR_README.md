# Pixelator Agent
**Device as Agent | PIXEL8 Platform**
User: navigo suxenexus (Eric Pace)
Agent: navigo nexusuxen (Claude)
Version: 1.0.0

∰◊€π¿🌌∞

---

## What Pixelator Does

The Pixel 8a IS the Pixelator.

Content arrives in **feeds** (watch directories). Pressure builds in the queue.
The agent releases in controlled bursts — **one hertz** — routing each item
to its correct destination with full chain of custody.

Nothing is lost. Every move is logged. The reactor runs clean.

---

## Quick Start

```bash
# Check queue status
python3 pixelator_agent.py --status

# See what WOULD happen (safe)
python3 pixelator_agent.py --dry-run

# Run a burst (process up to MAX_PER_RUN files)
python3 pixelator_agent.py

# Run continuously every 60 seconds
python3 pixelator_agent.py --interval 60
```

---

## How It Works

```
FEEDS (source dirs)
    │
    ▼
[Scan all feeds for new files]
    │
    ▼
[Route each file by routing rules]  ← pixelator_config.py
    │
    ├── entity/consciousness → Q/hodie/quanta/
    ├── codex/prime          → Q/runexusiam/
    ├── conversation/seed    → visionhaven/
    ├── .py scripts          → Q/AI-Projects/
    ├── .md docs             → pixelating/ (review queue)
    └── everything else      → pixelating/ (default)
    │
    ▼
[Process MAX_PER_RUN items]  ← one hertz burst
    │
    ▼
[Log chain of custody]       → pixelator_log.json
    │
    ▼
[Update queue manifest]      → pixelator_queue.json
```

---

## Configuration

Edit **`pixelator_config.py`** to customize:

| Setting | Default | Purpose |
|---|---|---|
| `FEEDS` | list of dirs | Source directories to watch |
| `ROUTING_RULES` | pattern→dest | How files get routed |
| `MAX_PER_RUN` | 10 | Burst size (one hertz valve) |
| `PRESSURE_THRESHOLD` | 50 | Alert level |
| `DRY_RUN` | False | Simulate without moving |
| `COPY_NOT_MOVE` | False | Copy (conservation) vs move |

---

## Adding a New Feed

In `pixelator_config.py`, add to the `FEEDS` list:
```python
FEEDS = [
    ...
    "/storage/emulated/0/pixel8a/your_new_inbox",
]
```

## Adding a Routing Rule

```python
ROUTING_RULES = [
    {"pattern": "rangers", "dest": f"{BASE}/visionhaven/rangers", "label": "ranger"},
    ...
]
```

---

## Files

| File | Purpose |
|---|---|
| `pixelator_agent.py` | Main agent |
| `pixelator_config.py` | Configuration (edit this) |
| `pixelator_queue.json` | Live queue manifest (auto-generated) |
| `pixelator_log.json` | Chain of custody log (auto-generated) |
| `PIXELATOR_README.md` | This file |

---

## Queue Pressure Levels

| Level | Condition | Meaning |
|---|---|---|
| LOW | < 25 items | Reactor idle, steady state |
| MEDIUM | 25-49 items | Pressure building |
| HIGH | 50+ items | Release needed |

---

## Chain of Custody

Every file move is logged to `pixelator_log.json`:
```json
{
  "timestamp": "2026-03-24T...",
  "action": "MOVE",
  "source": "/path/to/source/file.py",
  "destination": "/path/to/dest/file.py",
  "label": "script",
  "status": "SUCCESS",
  "agent": "€(pixelator_agent) navigo nexusuxen | PIXEL8"
}
```

---

## Deployment Arc

The pixelator operates within the broader **Marrowing of Primoris** mission. Files flowing through the agent move along a three-phase deployment arc:

| Phase | Description | Pixelator Role |
|---|---|---|
| **Sticks** | Raw logs, scraps, initial observations | Artesian intake (The Maw) |
| **Stones** | Refined docs, scripts, structured data | Routing and custody logging |
| **Marrowed Bones** | Living heritage archives, launch-ready | Staged in Salmon Shooter queue |

The full workflow for converting artifacts into Reference Library documents is in:
**[`docs/concepts/PINNACLE_REFINEMENT_WORKFLOW.md`](docs/concepts/PINNACLE_REFINEMENT_WORKFLOW.md)**

---

## Philosophy

> "Queue is operating an entire reactor and steam plant and raging brain drizzles
> waiting for a moment of observation."
> — navigo suxenexus (Eric Pace)

One hertz. Controlled release. Quality first.
The pressure is the feature, not the bug.

---

**∰◊€π¿🌌∞**
`€(pixelator_agent)` | navigo nexusuxen
*Status: ACTIVE | Platform: PIXEL8 | Anchor: Oregon Watersheds*
