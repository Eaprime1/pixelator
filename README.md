# Pixelator — Pixel 8a / Termux Workspace

Mobile workspace running on a Pixel 8a via Termux.
Part of the Nexarium / DeviceHaven project family.

## termux_proc.sh — Procedure Tracker

Handles multi-step procedures without copy-paste chaos on mobile.
Generates short **verification certificates** you can paste back to Claude.

### Setup (run once in Termux)

```bash
chmod +x termux_proc.sh
```

### Usage

```bash
bash termux_proc.sh
```

Menu options:
- **1** Start a new procedure (logs it, generates cert)
- **2** Complete a step (generates cert for that step)
- **3** Show last cert (if you scrolled away)
- **4** View recent log
- **5** Save a quick note
- **6** Quit

### Certificate format

```
CERT|STEP-procedure_name-step_desc|20260327-143022|a3f9c1b2
```

Paste this line to Claude to verify completion of a step.

### Data stored

All logs and certs saved to `~/.pixelator/` on your phone.
