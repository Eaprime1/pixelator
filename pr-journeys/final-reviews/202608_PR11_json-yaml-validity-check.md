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

## Status at Time of Writing

All four findings resolved. All CI checks passing (Codacy, GitGuardian, claude-review, dependency-review, build, custos-speaks, label, scan, validate, Terraform, Vercel). No issues/missions spun off.

## Filed To

Mirrors custos's `pr-journeys/final-reviews/202608_PR312_json-yaml-validity-check.md` — same underlying fix, ported to a sibling repo.
