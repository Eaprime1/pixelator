# CLAUDE.md

`prima-clock: 202610061006` (UTC)

Guidance for Claude Code when working in this repository.

## What this repository is

**pixelator** is the Pixel 8a's entity terminal home: automation that routes files from watch directories to their destinations with a chain of custody, plus the governance pipeline ported from `eaprime1/custos`.

- A Python agent (`pixelator_agent.py`) driven by `pixelator_config.py`, a Termux procedure tracker (`termux_proc.sh`), and `pixelator_automate.sh`.
- `pixelate/` is the **internal** side of the gateway between `~/pixel8` on the phone (external, outside any repo) and this repo. `pixelate/ROUTING.md` is the routing ladder (still a DRAFT); `pixelate/CUSTODY_LOG.md` records crossings.
- It is also a conduit and an extra layer of isolation between what is on the phone and what enters the project. Pixelization, sparklization and the other processes will live here later.
- No build pipeline. Python 3 standard library only.

## Commands

```bash
python3 pixelator_agent.py --status      # queue status
python3 pixelator_agent.py --dry-run     # what would happen (safe)
python3 pixelator_agent.py               # one burst (up to MAX_PER_RUN files)
python3 pixelator_agent.py --pressure    # pressure report
python3 pixelator_agent.py --interval 60 # run every 60 seconds (Ctrl+C to stop)

# one-time setup, not part of each pass: python3 -m pip install flake8 pytest pyyaml
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics   # what CI runs first
pytest                                    # tests mock the config, so they run off-device

bash tools/scan_lexeme.sh                 # unfinished markers (TODO, TBD, ...); advisory
bash tools/validate_json_yaml.sh .        # JSON/YAML must parse; blocking in CI
bash tools/prime_check.sh                 # prime state, if a .prime file exists

bash termux_proc.sh                       # step-by-step procedure tracker for the phone
```

`pixelator_config.py` hard-codes Pixel 8a paths (`/storage/emulated/0/pixel8a/...`). Change it only in a PR of its own, and keep the `consciousness` rule as it is until the Shepherd decides (see `pixelate/ROUTING.md`, open items).

## Routing

`pixelate/ROUTING.md` (a draft) sets out where content goes, lightest touch first: fast track for clean, vetted content; fix in place (a review folder and a note) for a distressed lexeme or another small problem a simple fix resolves; `eaprime1/maw` for polluted or extremely distressed content; `eaprime1/hodie` where it needs a real overhaul; and **when unsure, maw**. Record each crossing in `pixelate/CUSTODY_LOG.md`.

## Governance pipeline (`.github/workflows/`)

Ported from custos and adapted (pixelator PR #13). `finalize-pr.yml` seals on `@claude finalize` or `@claude ultima probatio`; `latin-cue-record.yml`, `review-packet.yml` and `witness-pr.yml` log cues, summarise the PR and keep the witness list.

- `finalize-pr.yml`: seals a PR when the owner comments `@claude finalize` (or `@claude ultima probatio`). A comment that carries the Claude Code footer never seals, and quoted cues are ignored.
- `latin-cue-record.yml`: logs each owner cue and the PR's state in one comment (UTC stamps).
- `review-packet.yml`: no-API summary of every PR; runs under `pull_request_target`, no checkout.
- `witness-pr.yml`: `witnessed` comments build the witness list; finalize seals it.
- `scan-lexeme.yml`, `validate-json-yaml.yml`, `python-app.yml`, `dependency-review.yml`, `claude-code-review.yml` and others.

In PR comments a navigo describes the seal cue in words and does not post it, unless the owner asks. A navigo merges only when the owner asks, in the conversation or on the PR.

## Conventions

- **Branches:** `claude/<topic>` for AI-authored work, one topic per branch. PRs open as drafts.
- **PR template:** Intent, What Arrived, Resonance, Ethics Check, What Door Does This Open?
- **prima-clock stamps:** `YYYYMMDDHHMM`. The Shepherd's own stamps use local time. The seal, the cue record and custody logs are UTC (`date -u '+%Y%m%d%H%M'`), so official records do not depend on where the Shepherd is.
- **No bounties, no cash.** The `bounty` issue form is retired and removed (custos did the same). Rewards are XP and credit.
- **Issue forms:** `mission`, `upgrade`, `lexeme`. The `lexeme` form needs the `lexeme` and `open` labels, which `.github/sovran-labels.yml` defines and the label sync creates.
- **Distressed words:** some words are weighted (custos keeps the compiled list, `atelier/lexemes/distressed-lexeme-list.md`). Do not rewrite them in place; route them by the ladder.
- Anything that needs the Shepherd's judgment is held and asked, not guessed. Report outcomes as they are: if a check fails, say so.

## Related repositories

`eaprime1/custos` (the hub and origin mold), `eaprime1/maw` (arrival and custody for polluted content), `eaprime1/hodie`.

## Known stale content

- `README.md` lines 4 and 85 still point at the `devicehaven` org; the Shepherd says `devicehaven` is now the spectorium repo. Only the clone line has been corrected so far, and the other two mentions wait for the Shepherd.

These are recorded in custos's `queue/future-forward/pixelator.md`, not fixed here.
