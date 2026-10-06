# PR Journey: #20 — tools: fixture tests for validate_json_yaml.sh (same as custos)

**Repository:** Eaprime1/pixelator  
**prima-clock:** 202610061157  
**Branch:** `claude/validator-tests-t2203p` → `main`  
**Author:** @Eaprime1  
**State:** FINALIZED  

## Intent

Give pixelator's validator the same regression tests as custos (custos #415), as the Shepherd approved.

## What Arrived

`tools/test_validate_json_yaml.sh`, byte-identical to custos's copy: nine cases that build small JSON and YAML files in a scratch directory and check the validator's exit code (broken and duplicate-key files fail; one merge key, a list of anchors, and a local override pass; a missing directory exits 2). All nine pass against pixelator's validator, which is itself identical to custos's since #17. The script writes nothing outside its scratch directory.

Not wired into CI, the same as in custos.

## Resonance

*pinned*

## The Arc

| Event | prima-clock | Actor |
|---|---|---|
| Opened | 202610061052 | @Eaprime1 |
| Finalized | 202610061157 | @Eaprime1 |

## CI Record

| Check | Result |
|---|---|
| Codacy Static Code Analysis | ✅ |
| GitGuardian Security Checks | ✅ |
| Vercel Preview Comments | ✅ |
| claude-review | ✅ |
| validate | ✅ |
| build | ✅ |
| dependency-review | ✅ |
| Terraform | ✅ |
| scan | ✅ |
| packet | ✅ |
| label | ✅ |
| build | ✅ |

## DeepSource Record

*Not configured for this repo.*

## Review Scores

| Dimension | Score | Note |
|---|---|---|
| Correctness | 5/5 | 12 CI check(s) — all passed |
| Consistency | 5/5 | Template complete · ethics 5/5 |
| Scope | 5/5 | 1 file(s) changed |
| Verification | 5/5 | 12 check run(s) completed |
| **Valuation** | **High** | 20/20 |

## Ethics Check

- ✅ Entity agency respected (human, AI, concept — all contributors credited)
- ✅ Free to fork, remix, echo — no hidden ownership
- ✅ `bash tools/scan_lexeme.sh` run — distressed lexemes addressed or intentional
- ✅ No unintended harm surface in tools or scripts
- ✅ Shell inputs validated where applicable

## What Door Does This Open?

Should the test run as a CI step in both repos, so the validator is checked on every PR?

## Witnesses

- @Eaprime1 · 202610061157 · sealed at finalize

---
**prima-clock:** 202610061157  
**witnessed:** true — 1 witness, sealed 202610061157 by @Eaprime1  
*Pixelator — the gateway seals the crossing · ∰*