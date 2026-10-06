# pixelate/ROUTING.md — the gateway rule

`prima-clock: 202610060627`
`status: DRAFT — written by the custos-side conversation for the phone-side conversation to read, correct, and own`

> **DRAFT — not live, not authoritative.** This describes intended routing. Nothing reads this file and no automation follows it. `pixelator_config.py` is unchanged and still governs what the agent actually does. Neither Maw destination named below exists as a working target yet. The phone-side conversation has not reviewed this.

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

## Fast track: vetted content that needs no maw trip

Content that is already well developed and clean may slide straight into place.

| Content | Route |
|---|---|
| Vetted, no issues, ready to enter. Minor cosmetic edits and small clarity edits are allowed. | **Fast track**: through `pixelate/` into the project. Skips maw. |
| Contains a distressed lexeme (`consciousness`, `manifesto`, others) | **maw** (destination to be confirmed, see *Which Maw?* below) |
| Needs polish, chain of custody, or is other system content | **custos** (for now) |

When in doubt, route to maw or custos. Do not fast-track on a guess.

### Which Maw?
Two places are called the Maw, and this draft does not pick between them:
- **`eaprime1/maw`**, a separate repo with its own arrival routine (`maw/ARRIVAL.md`) and custody log. It sits before nullus in the custody chain.
- **`pixelate/maw_pixellum/`**, which `PERSPECTIVE_REQUEST_001_CARBONITE_MAW.md` (lines 74-75 and 216) describes as the existing intake system, with arrivals going to `maw_pixellum/intake/`. That directory is **not present in this repo today**, so the document may be describing something that lives elsewhere or has not been created.

Until the Shepherd decides, "route to maw" means one of those two, not both. It could also be a mapping (internal intake feeding the external repo).

### Open items for the Shepherd (not decided here)
- **The full distressed-lexeme list.** Only two are named here. These files live in the **`eaprime1/custos`** repo, not this one: `atelier/lexemes/manifesto.md`, `atelier/lexeme-drift.md`, and a draft compiled list at `atelier/lexemes/distressed-lexeme-list.md` (custos PR 406). A scanner in this repo would need a copy of the list or a defined path to custos. The scan should read from one list, not several.
- **Conflict with current config.** `pixelator_config.py` routes the pattern `consciousness` to `hodie/quanta`. Under this rule it goes to maw. Until the config changes, files with `consciousness` in the name still go to `hodie/quanta`, and this document does not override that. The config needs a decision before the two disagree in practice, and before this file is treated as live.
- **Which Maw** receives distressed-lexeme content: the `eaprime1/maw` repo, `pixelate/maw_pixellum/`, or the internal one feeding the repo. See *Which Maw?* above. Neither is actionable today: the repo needs a cross-repo handoff that is not defined, and the `maw_pixellum/` directory does not exist here.
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
- Settle the distressed-lexeme list and the `consciousness` config conflict.
- Describe the gateway as a procedure with a custody-log entry per crossing.
