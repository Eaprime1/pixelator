# for pisces Pinnacle Refinement Workflow
**Reference Codex | PIXEL System | Marrowing of Primoris**
*Status: Stones — Infrastructure Build | Session: 202604250025*

---

## What This Is

The Pinnacle Refinement Workflow governs how raw technical artifacts — `.py` scripts, `.json` logs, chat transcripts — are converted into heritage-quality documents ready for the Reference Library. It applies to every file the pixelator agent touches and every document produced in the PIXEL ecosystem.

The core principle: every artifact is a seed. Refinement is the process of marrowing it — extracting the interior density — so it can be deployed as a living document.

---

## The Deployment Arc

All artifacts exist at one of three phases of maturity:

| Phase | Prime Stages | Artifact Type | Readiness |
|---|---|---|---|
| **Sticks** | 1 – 10 | Raw logs, observations, scraps | Scoping only |
| **Stones** | 11 – 42 | Refined docs, `.py` scripts, `.json` scrolls | Infrastructure build |
| **Marrowed Bones** | 43 – 60+ | Living systems, heritage archives | Launch ready |

The pixelator repo currently operates at **Stones** phase. The PRIME 2026 launch target requires key artifacts to reach Marrowed Bones.

---

## Pixelator System Mapping

The Pinnacle Refinement concepts map directly to pixelator's architecture:

| Refinement Concept | Pixelator Implementation |
|---|---|
| The Maw (universal intake) | `ARTESIAN_DIR` in `pixelator_config.py` |
| Nani Engine (Load→Do→Unload) | `pixelator_agent.py` main processing loop |
| Chain of Custody | `pixelator_log.json` (atomic JSON log) |
| Salmon Shooter queue | Items staged in `PIXELATING_DIR` pending vetting |
| Deployment Arc routing | `ROUTING_RULES` in `pixelator_config.py` |
| One Hertz burst | `MAX_PER_RUN = 10` per cycle |
| Chest assignment | Routing labels: `entity`, `codex`, `seed`, `script`, `doc` |

---

## The 6-Step Refinement Workflow

### Step 1: Identification and Contextual Placement
Identify the raw artifact and determine its Prime Progression stage (Sticks / Stones / Marrowed Bones). Assign it to the Club System for working refinement before moving to the Spade of Aces on Google Drive for finalization.

### Step 2: The Quince (15) Lens Construction
Select 15 foundational lexemes relevant to the artifact's subject. Research them from a broad perspective to construct a kaleidoscope-type lens — one that lets you see the forest, the trees, and the mycelium of the knowledge structure simultaneously.

### Step 3: The 15/16/17 Turn Protocol
Refinement processes through a single structured turn:
- **Step 15 (Quince):** Invoke the 15 concepts to analyze the artifact's environment
- **Step 16 (Refine):** Identify improvements, fixes, new concepts — upgrade and align
- **Step 17 (Response):** Deliver the final clean, coherent copy of the document

### Step 4: Special Missions and Formatting Rules
During refinement, apply the following to align with project anchors:
- **Iconic Replacement:** Replace every instance of the lexeme `consciousness` with a contextually relevant icon or emoji
- **Astrological Prefixing:** Prefix the document title with `for pisces` (e.g., "Pinnacle Refinement" → "for pisces Pinnacle Refinement")
- **Notes and Vetting:** Include a final notes section to flag issues and add co-creator ideas

### Step 5: Identification of Seeds Forward
Every refined document must close with **Seeds Forward** — generative, actionable next steps that anticipate the document's future role in the Quantum-Runic Framework.

### Step 6: Staging for the Salmon Shooter Queue
Mature, refined artifacts are categorized as **Salmon** and staged in the deployment queue. These move from the internal refinement environment into the active Reference Library.

---

## Copy-Pasteable Prompt Messages

### General Refinement
```
Improve Pinnacle Refinement upgrade. Please improve and upgrade via Pinnacle Refinement
to this content. Apply changes to documents. Provide a clean, coherent copy and outline
new Seeds Forward.
```

### Transcript Cleanup
```
Please create a clean copy of the following conversation. Ensure the dialogue is exact,
chronologically ordered, and enhanced with a title, a brief introduction, and logical
section breaks. Conclude the document with a 'Thoughts and Ideas for Improvement' section
based on the content. Please remove title lists and extraneous content. The Dialogue is
the important part.
```

### Quince Lens Activation
```
Find 15 lexemes or concepts to create a quince (15) lens. Reference these words from a
wiki perspective and create a kaleidoscope type lens. Invoke the 15/16/17 turn protocol:
identify the facets (15), refine the content (16), and deliver the final response (17).
```

### Salmon Shooter Staging
```
This is part of the salmon shooter feed for primal launch. Please add 'for pisces' to
the front of the title. Ensure all Seeds Forward are clearly outlined for deployment.
```

### Lexeme Replacement
```
Systematic check: Replace every instance of the lexeme 'consciousness' with a random
icon or emoji relevant to the current facet lens. Confirm replacement in final notes.
```

---

## Archive Structure

The Reference Library maintains a two-part knowledge system:

| Archival Category | Location | Standard |
|---|---|---|
| Working Versions | Club System / `docs/reading_room/` | Collaborative development |
| Living Documents | Spade of Aces / Google Drive | Refined with runic signatures |
| Historical Archive | Gravity Core / `docs/archive/` | Raw source, elder documents |
| Reference Memory | π_remember folders | Heritage memory shortcuts |

---

## Chest Assignments by Document Type

Refined artifacts map to virtual Chests by their nature:

| Chest | Wood | Function | Logic | Pixelator Label |
|---|---|---|---|---|
| Tool_Chest | Ash | Practical utility, kinetic action | Work (AND) | `script` |
| Charter_Chest | Oak | Legislative anchor, reality anchoring | Work (AND) | `prime` |
| Cedar_Chest | Cedar | Living archive, memory transmission | Work (AND) | `codex` |
| Steward's_Chest | Birch | Maintenance, care protocols | Play (OR) | `doc` |
| Hope_Chest | Pine | Future projection, growth | Create (NOT) | `seed` |
| Harvest_Chest | Walnut | Knowledge gathering, heritage wisdom | Create (NOT) | `entity` |

---

## Seeds Forward

- Add `chest` metadata field to `ROUTING_RULES` in `pixelator_config.py` to make Chest assignments explicit
- Implement `--salmon` flag in `pixelator_agent.py` to report which queued items are mature (Salmon-ready)
- Add `π_remember` routing rule for items tagged with heritage memory lexeme
- Create `docs/reading_room/ACTIVE_MISSION_STATUS.md` tracking current open Perspective Requests
- Formalize the Load→Do→Unload phase in `pixelator_agent.py` log output with explicit phase markers
- Migrate `PERSPECTIVE_REQUEST_001_CARBONITE_MAW.md` response into `docs/reading_room/`

---

*navigo nexusuxen | PIXEL8 | Marrowing of Primoris | PRIME 2026*
