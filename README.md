# pixelator

**Device:** Pixel 8a
**Owner:** [DeviceHaven](https://github.com/devicehaven) org
**Repo:** `github.com/devicehaven/pixelator`

Mobile workspace running on a Pixel 8a via Termux.
Part of the [DeviceHaven](https://github.com/devicehaven) organization.

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
| 6 | Roll D12 insight (timestamp + random icon) |
| 7 | Quit |

### Certificate format

```
CERT|STEP-procedure_name-step_desc|20260327-143022|a3f9c1b2
```

Paste this one line to Claude to verify a step. No long scrolling needed.

### Data stored

All logs and certs saved to `~/.pixelator/` on your phone.

### D12 insight roll

Option 6 populates a D12 dice pool (`1..12`), rolls once, and prints a timestamped insight:

`YYYY-MM-DD HH:MM:SS TZ | D12=<roll> <random dice-related icon> | <insight text>`

This uses random icon output in place of lexeme-style wording.

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
