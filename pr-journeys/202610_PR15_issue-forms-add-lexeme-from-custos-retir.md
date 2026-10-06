# PR Journey: #15 — issue forms: add lexeme (from custos), retire bounty

**Repository:** Eaprime1/pixelator  
**prima-clock:** 202610061012  
**Branch:** `claude/pixelator-issue-forms-t2203p` → `main`  
**Author:** @Eaprime1  
**State:** FINALIZED  

## Intent

Do what the Shepherd decided on peer review Run 0 finding PC-5: bring custos's `lexeme` issue form to pixelator and retire `bounty`.

## What Arrived

- `.github/ISSUE_TEMPLATE/lexeme.yml` (new), adapted from custos: notes go to `docs/lexemes/<slug>.md`, "read first" points at this repo's files, and a term from custos's compiled weighted list is routed by `pixelate/ROUTING.md` (when unsure, to maw) instead of being rewritten here.
- `.github/ISSUE_TEMPLATE/bounty.yml` removed. Custos retired the word and pays no monetary rewards; `mission` and `upgrade` stay as they are.

## Resonance

*retired, borrowed*

## The Arc

| Event | prima-clock | Actor |
|---|---|---|
| Opened | 202610060918 | @Eaprime1 |
| Finalized | 202610061012 | @Eaprime1 |

## CI Record

| Check | Result |
|---|---|
| Codacy Static Code Analysis | ✅ |
| Vercel Preview Comments | ✅ |
| build | ✅ |
| Terraform | ✅ |
| claude-review | ✅ |
| dependency-review | ✅ |
| scan | ✅ |
| validate | ✅ |
| GitGuardian Security Checks | ✅ |
| packet | ✅ |
| label | ✅ |
| analyze-documents | ✅ |
| build | ✅ |

## DeepSource Record

*Not configured for this repo.*

## Review Scores

| Dimension | Score | Note |
|---|---|---|
| Correctness | 5/5 | 13 CI check(s) — all passed |
| Consistency | 5/5 | Template complete · ethics 5/5 |
| Scope | 5/5 | 4 file(s) changed |
| Verification | 5/5 | 13 check run(s) completed |
| **Valuation** | **High** | 20/20 |

## Ethics Check

- ✅ Entity agency respected (human, AI, concept — all contributors credited)
- ✅ Free to fork, remix, echo — no hidden ownership
- ✅ `bash tools/scan_lexeme.sh` run — distressed lexemes addressed or intentional
- ✅ No unintended harm surface in tools or scripts
- ✅ Shell inputs validated where applicable

## What Door Does This Open?

Pixelator's label list (`.github/sovran-labels.yml`) defines none of `lexeme`, `mission`, `upgrade` or `open`. Should it carry the same labels as custos?

## Witnesses

- @Eaprime1 · 202610061012 · sealed at finalize

---
**prima-clock:** 202610061012  
**witnessed:** true — 1 witness, sealed 202610061012 by @Eaprime1  
*Pixelator — the gateway seals the crossing · ∰*