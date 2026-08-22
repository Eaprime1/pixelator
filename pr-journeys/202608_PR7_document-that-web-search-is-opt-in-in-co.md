# PR Journey: #7 — Document that web search is opt-in in .codex/AGENTS.md

**Repository:** Eaprime1/pixelator  
**prima-clock:** 202608220645  
**Branch:** `docs/codex-agents-websearch-note` → `main`  
**Author:** @Eaprime1  
**State:** FINALIZED  

## Intent

Rebase the doc improvement from copilot/repair-and-improve-pixelator onto current main.

## What Arrived

.codex/AGENTS.md now states explicitly that live web search is off by default (matching config.toml's web_search = "off" from PR #2) and must be opted into per-user.

## Resonance

*clarity

---*

## The Arc

| Event | prima-clock | Actor |
|---|---|---|
| Opened | 202608220620 | @Eaprime1 |
| Finalized | 202608220645 | @Eaprime1 |

## CI Record

| Check | Result |
|---|---|
| Codacy Static Code Analysis | ✅ |
| copilot-pull-request-reviewer | ✅ |
| Vercel Preview Comments | ✅ |
| claude-review | ✅ |
| dependency-review | ✅ |
| scan | ✅ |
| label | ✅ |
| custos-speaks | ✅ |
| build | ✅ |
| GitGuardian Security Checks | ✅ |

## DeepSource Record

*Not configured for this repo.*

## Review Scores

| Dimension | Score | Note |
|---|---|---|
| Correctness | 5/5 | 10 CI check(s) — all passed |
| Consistency | 5/5 | Template complete · ethics 5/5 |
| Scope | 5/5 | 1 file(s) changed |
| Verification | 5/5 | 10 check run(s) completed |
| **Valuation** | **High** | 20/20 |

## Ethics Check

- ✅ Entity agency respected
- ✅ Free to fork, remix, echo — no hidden ownership
- ✅ `bash tools/scan_lexeme.sh` run
- ✅ No unintended harm surface
- ✅ Shell inputs validated where applicable

## What Door Does This Open?

None — doc-only.

---
**prima-clock:** 202608220645  
**witnessed:** true  
*🌿 Custos — the shepherd closes the fold · ∰🌿*