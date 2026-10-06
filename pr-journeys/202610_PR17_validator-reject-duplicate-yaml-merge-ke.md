# PR Journey: #17 — validator: reject duplicate YAML merge keys (adopted from custos)

**Repository:** Eaprime1/pixelator  
**prima-clock:** 202610061005  
**Branch:** `claude/adopt-validator-fix-t2203p` → `main`  
**Author:** @Eaprime1  
**State:** FINALIZED  

## Intent

Bring custos's validator fix (custos #408) into pixelator so the two copies of `tools/validate_json_yaml.sh` match again.

## What Arrived

The validator now rejects a mapping with two literal `<<` merge keys. One `<<` (including a list of anchors) and a local override still pass. Checked in a scratch directory: two `<<` exits 1, one `<<` with an override exits 0.

## Resonance

*matched*

## The Arc

| Event | prima-clock | Actor |
|---|---|---|
| Opened | 202610060927 | @Eaprime1 |
| Finalized | 202610061005 | @Eaprime1 |

## CI Record

| Check | Result |
|---|---|
| copilot-pull-request-reviewer | ✅ |
| claude-review | ✅ |
| custos-speaks | ✅ |
| Codacy Static Code Analysis | ✅ |
| Vercel Preview Comments | ✅ |
| GitGuardian Security Checks | ✅ |
| label | ✅ |
| claude-review | ✅ |
| validate | ✅ |
| custos-speaks | ✅ |
| dependency-review | ✅ |
| scan | ✅ |
| Terraform | ✅ |
| build | ✅ |
| build | ✅ |

## DeepSource Record

*Not configured for this repo.*

## Review Scores

| Dimension | Score | Note |
|---|---|---|
| Correctness | 5/5 | 15 CI check(s) — all passed |
| Consistency | 5/5 | Template complete · ethics 5/5 |
| Scope | 5/5 | 1 file(s) changed |
| Verification | 5/5 | 15 check run(s) completed |
| **Valuation** | **High** | 20/20 |

## Ethics Check

- ✅ Entity agency respected (human, AI, concept — all contributors credited)
- ✅ Free to fork, remix, echo — no hidden ownership
- ✅ `bash tools/scan_lexeme.sh` run — distressed lexemes addressed or intentional
- ✅ No unintended harm surface in tools or scripts
- ✅ Shell inputs validated where applicable

## What Door Does This Open?

Which repo should hold the canonical copy of the validator, so the next fix lands once?

## Witnesses

- @Eaprime1 · 202610061005 · sealed at finalize

---
**prima-clock:** 202610061005  
**witnessed:** true — 1 witness, sealed 202610061005 by @Eaprime1  
*Pixelator — the gateway seals the crossing · ∰*