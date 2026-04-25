# pixelator

**Device:** Pixel 8a
**Owner:** [Eaprime1](https://github.com/eaprime1) / [DeviceHaven](https://github.com/devicehaven) org
**Platform:** PIXEL8 | Marrowing of Primoris | PRIME 2026

Mobile workspace automation running on a Pixel 8a via Termux.
The pixelator is one leg of the **PIXEL Triad**:

| Component | Role | Location |
|---|---|---|
| **pixelator** | Entity terminal home — file routing, queue management | `~/pixelator` |
| **pixelshard** | Shard/fragment entity | `~/pixelshard` |
| **pixelspace** | Narrative universe space | `~/pixelspace` |

These three converge toward PIXEL at prime launch.

---

## Documentation

| Doc | Purpose |
|---|---|
| [`PIXELATOR_README.md`](PIXELATOR_README.md) | Full agent documentation |
| [`MISSION_NOTES.md`](MISSION_NOTES.md) | Living strategic notes |
| [`PERSPECTIVE_REQUEST_001_CARBONITE_MAW.md`](PERSPECTIVE_REQUEST_001_CARBONITE_MAW.md) | Open perspective request |
| [`docs/concepts/PINNACLE_REFINEMENT_WORKFLOW.md`](docs/concepts/PINNACLE_REFINEMENT_WORKFLOW.md) | Refinement workflow reference |

---

## Setup (Termux — run once)

```bash
git clone https://github.com/devicehaven/pixelator
cd pixelator
chmod +x termux_proc.sh
```

---

## termux_proc.sh — Procedure Tracker

Handles multi-step procedures without copy-paste chaos on mobile.
Generates short **verification certificates** you can paste back to Claude.

```bash
bash termux_proc.sh
```

| Option | Action |
|--------|--------|
| 1 | Start / resume a procedure |
| 2 | Complete a step — generates cert |
| 3 | Show last cert (if you scrolled away) |
| 4 | View recent log |
| 5 | Save a quick note |
| 6 | Quit |

### Certificate format

```
CERT|STEP-procedure_name-step_desc|20260327-143022|a3f9c1b2
```

Paste this one line to Claude to verify a step. No long scrolling needed.

### Data stored

All logs and certs saved to `~/.pixelator/` on your phone.

---

## DeviceHaven organization structure

```
github.com/devicehaven/
├── pixelator        ← this repo (Pixel 8a)
├── hodie            ← (transfer when ready)
├── runexusiam       ← (transfer when ready)
└── ...
```

Each device/project is its own repo — flat, no nesting.
