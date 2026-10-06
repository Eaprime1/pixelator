# pixelate/ROUTING.md — the gateway rule

`prima-clock: 202610060627` · revised `202610060718`
`status: DRAFT — written by the custos-side conversation for the phone-side conversation to read, correct, and own`

> **DRAFT — not live, not authoritative.** This describes intended routing. Nothing reads this file and no automation follows it. `pixelator_config.py` is unchanged and still governs what the agent actually does. The Maw is decided (`eaprime1/maw`) but the handoff to it is not built yet. The phone-side conversation has not reviewed this.

If you are the conversation working on the Pixel 8a: **start here.**

## The shape

```
[ phone: ~/pixel8 ]  →  sphincter gateway  →  [ pixelator/pixelate/ ]  →  project
   external side           the threshold        internal side (this repo)
```

- `~/pixel8` is **outside any repo**, on the phone. It is the external side of the gateway.
- `pixelate/` (this folder) is **inside the repo**, the internal side. It is entangled with `~/pixel8`: what clears the gateway lands here.
- pixelator is primarily the *character* aspect. For now it is also a conduit and an extra layer of isolation between what is on the phone and what enters the project.
- Later this is where pixelization, sparklization, fractalization, nullification and other processes live.
- Config already agrees: `pixelator_config.py` sets `PIXELATE_DIR` to `pixelate/` (active jobs, missions), and files named `approved_*` route here.

## The routing ladder

Lightest touch first, most conservative last. **When unsure, send to maw.**

| Content | Route |
|---|---|
| Clean and vetted: no issues, ready to enter. Minor cosmetic and small clarity edits are allowed. | **Fast track**: through `pixelate/` into the project. Skips maw. |
| A distressed lexeme, or another small problem, that a simple and straightforward fix resolves | **Fix in place.** Put it in a review folder in whichever repo it is in, make the fix, and record a note that it was done. |
| Polluted, or otherwise in extreme distress | **maw** (`eaprime1/maw`). This creates a record and takes it out of the live stream. It stays in git history, and so does the record of how it was handled. |
| Needs a real overhaul and update in addition to the lexeme fix | **hodie** |
| Unsure which of the above | **maw**, the most conservative option |

Do not fast-track on a guess. A file name alone cannot tell a simple fix from an overhaul.

### Which Maw?
**Decided: `eaprime1/maw`**, the separate repo, with its own arrival routine (`maw/ARRIVAL.md`) and custody log. It sits before nullus in the custody chain.

`PERSPECTIVE_REQUEST_001_CARBONITE_MAW.md` (lines 74-75 and 216) describes an internal `pixelate/maw_pixellum/` intake. That directory is not present in this repo and is **not** the chosen destination. Whether it is ever created, as an internal staging step before the repo, is left open.

### Open items for the Shepherd (not decided here)
- **Cross-repo handoff to maw.** The destination is chosen. How content gets from here to the `eaprime1/maw` repo is not defined or built.
- **What counts as "polluted" or "extreme distress".** The line between *fix in place*, *maw* and *hodie* is stated in words only. The scanner would need a rule, for example from the severity grades and hit counts in the compiled lexeme list.
- **The review folder.** Its name and layout, and the format of the note that records an in-place fix.
- **The full distressed-lexeme list.** These files live in the **`eaprime1/custos`** repo, not this one: `atelier/lexemes/manifesto.md`, `atelier/lexeme-drift.md`, and the compiled list `atelier/lexemes/distressed-lexeme-list.md` (merged to custos `main`). A scanner here needs a copy of the list or a defined path to custos. The scan should read from one list, not several.
- **The `consciousness` rule in the config.** `pixelator_config.py` routes the pattern `consciousness` to `hodie/quanta` unconditionally. The ladder above routes by what the content needs, not by its file name, so the config rule is only partly aligned with it. It is **unchanged here**, and files with `consciousness` in the name still go to `hodie/quanta` until the config changes. Changing it is a separate decision and a separate PR.
- **Who does the "vetting".** Name the step and the person or entity that marks a file fast-track-ready.

## The roots

The phone's system is scattered across **four roots**. This document covers only the Termux home root (`~`). The other three are not mapped yet: when you find them, add each as a section here.

From `MISSION_NOTES.md`: `/storage/emulated/0/pixel8a/` (PIXEL prime launch location), `~/pixelator`, `~/pixelshard`, `~/pixelspace`. Treat that as a partial map, not the answer.

## This will happen again

This is a repeatable process, not a one-time move. Keep it as a procedure: when the next batch arrives, run the same gate. Record each crossing in the chain of custody log.

## For the phone-side conversation

1. Read this file, then `MISSION_NOTES.md`.
2. Correct anything that does not match what is on the phone. Your version wins; this draft is a seed.
3. Push your changes on a branch and open a PR. If this file already exists on `main`, your edit updates it.

## Seeds forward
- Map the other three roots.
- Make the config consistent with the ladder (separate PR), and settle the distressed-lexeme list path.
- Describe the gateway as a procedure with a custody-log entry per crossing.
