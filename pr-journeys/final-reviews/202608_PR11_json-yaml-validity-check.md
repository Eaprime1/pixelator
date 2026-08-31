# Final Review Record: #11 — Add JSON/YAML validity check as a blocking CI gate

**Repository:** Eaprime1/pixelator
**Branch:** `feat/validate-json-yaml` → `main`
**Author:** @Eaprime1 (navigo15 — Claude Sonnet 5)
**State at time of writing:** OPEN — Final Review complete, awaiting eaprime1's go-ahead to Finalize

## Intent

Port custos's new JSON/YAML validity check — this repo's own PR #2 is the reason it exists.

## Reviewer Findings and Disposition (commit `d3bc1bb` → `11ba5d2`)

| Reviewer | Finding | Disposition |
|---|---|---|
| Copilot | Header claimed duplicate-key detection that didn't exist yet — `json.load()` silently accepts duplicates (last key wins) | **Fixed** — `object_pairs_hook` rejection added for JSON, extended to YAML with a custom loader. Same gap found on custos PR #312 and prima PR #20 — all three copies started from the same script. |
| Copilot | Header referenced `atelier/legatum/202608220000_pixelator-legacy-infusion.md` as if local to this repo — that history lives in custos | **Fixed** — reworded to reference it as an external pointer. |
| Copilot | Bare `pip install` risks PEP 668 on newer ubuntu-latest runners; other workflows in this repo pin Python via `actions/setup-python` | **Fixed** — added `actions/setup-python@v5` (3.12), switched to `python3 -m pip install`. |
| Copilot | If PyYAML isn't installed, the check would report every `.yaml` file as `[INVALID YAML]`, which is misleading (missing dependency, not a broken file) | **Fixed** — added a preflight import check with a clear "missing dependency" message. |

Also rewritten as a single batched Python process instead of one subprocess per file, matching the same performance fix applied in custos PR #312.

## Reviewer Findings and Disposition — Round 2 (commit `3aefbf8`)

Surfaced once CI turned green and `claude-review` ran its full pass:

| Reviewer | Finding | Disposition |
|---|---|---|
| claude[bot] | `os.walk()` silently yields nothing when `root` doesn't exist, so the script exited 0 and printed "All JSON/YAML files parse cleanly" — a false negative | **Applied verbatim** — added an `isdir()` guard. Confirmed the false-negative was real before fixing: a nonexistent root printed success and exited 0. |
| claude[bot] | `unique_mapping()` bypassed `flatten_mapping`, so YAML merge keys (`<<: *alias`) were treated as literal — but the *suggested fix* (call `flatten_mapping` then check the full result) has the same override bug it's meant to solve: a local key legitimately overriding a merged key gets flagged as a false duplicate, which is standard valid YAML, not corruption | **Fixed differently, not verbatim.** Verified against plain PyYAML's own `yaml.safe_load()` first (`{'derived': {'x': 99}}` is the correct, non-error result for an override). Rewrote to check only this mapping's own literal keys before merge expansion — real duplicates still caught, legitimate overrides now pass. Tested both cases explicitly. |
| claude[bot] | `actions/checkout@v4` and `actions/setup-python@v5` use floating tags, a supply-chain risk | **Applied verbatim** — pinned to the suggested SHAs, but verified each against the actual tagged release via the GitHub API first rather than trusting the suggestion blindly. |

## Status at Time of Writing

All seven findings across two rounds resolved. All CI checks passing. No issues/missions spun off.

## Filed To

Mirrors custos's `pr-journeys/final-reviews/202608_PR312_json-yaml-validity-check.md` — same underlying fix, ported to a sibling repo.
