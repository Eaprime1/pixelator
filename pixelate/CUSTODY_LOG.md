# pixelate/CUSTODY_LOG.md — crossings at the gateway

`status: DRAFT — opened by the custos-side conversation; the phone-side conversation reads it, corrects it and owns it`

Chain of custody for what crosses the gateway from `~/pixel8` into this repo (the routing ladder in `ROUTING.md`). Append only: new entries go at the bottom; past entries are never edited. A correction is a new entry that names the one it corrects.

This is a different record from `pixelator_log.json`. That file is the agent's own log of every file move it makes. This file records the **decisions**: what crossed, which rung of the ladder it took, and who judged it. For what happens after a send to maw, the record continues in maw's own log (`eaprime1/maw`, `maw/registry/custody_log.md`).

`ROUTING.md` is still a draft, so this log is too: it records intent until the phone side confirms the procedure.

## Entry format

One fenced block per entry:

```yaml
prima_clock: YYYYMMDDHHMM    # UTC: date -u '+%Y%m%d%H%M'
event:       cross | fast-track | fix-in-place | send-to-maw | hold | correction
item:        <path or batch name, as it arrived>
from:        <where it was: ~/pixel8/... , a repo path, or a named source such as a conversation or PR>
to:          <where it went: a path here, maw, hodie, or held>
by:          <who judged it: e.g. eaprime1, nav1>
note:        <one line: why this rung>
```

- `fast-track`: vetted content, straight in.
- `fix-in-place`: a polish or small edit made here, with a review folder and a note of what changed.
- `send-to-maw`: sent to `eaprime1/maw` (distressed words, or when unsure).
- `hold`: left outside until a decision is made.

## Entries

```yaml
prima_clock: 202610060918
event:       cross
item:        pixelate/ROUTING.md (draft of the gateway rule)
from:        custos-side conversation, via pixelator PR #12
to:          pixelate/ROUTING.md
by:          eaprime1, nav1
note:        first item recorded; the log itself opens with this entry
```
