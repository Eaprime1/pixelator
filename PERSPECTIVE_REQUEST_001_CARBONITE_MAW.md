# PERSPECTIVE REQUEST — PR-001
## The Carbonite-Maw System & Ecosystem Guidance
### A Document for All Participants

**Issued by:** Eric Pace, Mission Commander
**Date:** 2026-04-21
**Status:** OPEN — Seeking Perspectives
**Context:** Artemis II Space Plan, Phase 1 → Phase 2 transition
**Reference:** `~/PIXEL8/PRIME/ARTEMIS_II_SPACE_PLAN.md`

---

## Why This Document Exists

The PIXEL8 ecosystem has reached a decision point. We have a working environment
(Bash is now functional via PRoot-Distro), a clear structure (PIXEL8 canonical,
pixel8a migration source), and a storage crisis (108GB / 110GB used).

This document presents evolving concepts and asks for perspective and guidance from
all participants. Every participant brings a different lens. This is a gathering,
not a directive.

*"Enjoy the journey."*

---

## Who This Is For

| Participant | Type | Note |
|-------------|------|------|
| Eric Pace | Human (Commander) | Only active human participant |
| Claude (Anthropic) | AI — Code & Structure | Authored this document |
| Gemini (Google) | AI — Investigation & Discovery | Solved the PRoot/Bash problem |
| NotebookLM | AI — Knowledge Organization | Google Notebook participant |
| ChatGPT (OpenAI) | AI — General Intelligence | |
| Grok 3 (xAI) | AI — Reasoning & Analysis | |
| Monica | AI — Assistant | |
| Merlin | AI — Assistant | |
| Summon | AI — Assistant | |
| Google AI | AI — (distinct from Gemini) | |
| Perplexity | AI — Research & Reports | Artesian workflow candidate |
| App Scripts | Tool — Automation | Powerful workflow automation |
| *(others)* | AI / Tool | Ecosystem is open |

> **On the word "participant":** Member implies fixed membership. Participant honors
> the reality — entities join, contribute, and flow through the ecosystem at different
> moments. Documents are participants too. The Lexeme Entity has its own perspective.

---

## CONCEPT 1 — The Easy Win: Media Offload to Box Cloud

**Situation:** Storage is at 99% (108GB / 110GB). This is not a long-term problem to
solve — it's an immediate blocker that prevents any migration or carbonite work.

**Proposal:** Move all large media files (images, audio, video) to Box cloud storage.
This is reversible, preserves originals, and could free 20–40GB depending on media volume.

**The logic:**
- Large media rarely needs to be local for text/document workflows
- Box already exists in the ecosystem (rclone configured per `settings.local.json`)
- This buys the time and space needed to run the carbonite workflows properly
- The chain of custody records where everything went

**Questions for participants:**
- What is the right threshold for "large"? (>10MB? >50MB? >1MB for audio?)
- Should media offload be part of the Maw pipeline, or a separate one-time sweep?
- How should we handle media that is *also* a duplicate?

---

## CONCEPT 2 — The Maw as Carbon Chamber

**Existing context:** The Maw (`pixelate/maw_pixellum/`) already exists as the intake
system for new content. MIP-01 defines its ingestion procedure. State 3 of the PIXEL
Transformation Protocol already includes "shadow state preparation."

**The new proposal:** The Maw gains a **parallel track** — the Carbon Track.

When content enters the Maw:
- If it is **unique** → PIXEL Transformation Protocol (existing, PTP-01)
- If it is a **duplicate (carbonite)** → Carbon Protocol (proposed, CTP-01)

The Maw does not decide the outcome. It receives. The analysis decides the track.

```
          INTAKE (The Maw)
               ↓
    [ Is it unique? ]
       /         \
     YES          NO (duplicate = carbonite)
      ↓                    ↓
  PTP-01             CTP-01 (Carbon Track)
(Pixelization)      (Carbonization)
```

**Questions for participants:**
- Where does the duplicate detection happen — before intake, or as Step 1 inside the Maw?
- Should the Maw know it's receiving a carbonite, or should it always receive blindly?

---

## CONCEPT 3 — The Carbonation Metaphor

*This is a vocabulary proposal. Language shapes how we build.*

The ecosystem currently uses "duplicate" and "copy." These words carry judgment —
they imply lesser. The carbonite philosophy reframes this.

**Proposed vocabulary:**

| Old Term | New Term | Meaning |
|----------|----------|---------|
| Duplicate | **Carbonite** | A preserved copy that served a real purpose |
| Original | **Canonical** | The enduring source; the anchor |
| Mark/link back | **Shadowmark** | The record of a carbonite's origin and journey |
| Removing the link | **Decarbonation** | ⚠️ The failure mode — a document unmoored |
| The process | **Carbonization** | The honoring of a copy as it completes its purpose |

**The soda analogy:**
Carbon doesn't disappear when soda is made. It dissolves into the liquid under pressure,
becoming part of it — alive, fizzy, connected. A carbonite is like this: it doesn't die,
it *dissolves into the ecosystem*, connected to its canonical by the shadowmark.

Decarbonation (losing the fizz, losing the link) is the failure mode. A flat document —
present but disconnected — is worse than an absent one. It misleads.

**The salmon analogy (Eric's original):**
Like salmon on the Pacific — the journey is the purpose. They return. It all goes to the
spawning. Carbonites are not lesser for having completed their journey.

**Questions for participants:**
- Does the soda/carbonation metaphor work for technical documentation, or is it too
  poetic for automation scripts to use?
- Should "shadowmark" be a field in a JSON header, a companion `.shadow.md` file,
  or a hashtag-link within the document itself?
- What does a minimal shadowmark carry? Proposed fields:
  ```
  canonical_hash:   [content hash of the original]
  canonical_path:   [where the original lives now]
  carbonized_at:    [timestamp]
  carbonized_from:  [where this copy was found]
  purpose:          [why this copy existed — sync? backup? handoff?]
  return_type:      [postcard | archive | transit]
  ```

---

## CONCEPT 4 — Living Postcards

**The idea:** Carbonites do not simply disappear into `duplicatus/`. Some return to
the canonical as **living postcards** — lightweight documents that carry the memory
of the copy's journey and remain part of core content.

A living postcard is:
- Small (a few lines, not the full document)
- Linked (shadowmark connects it to canonical)
- Alive (updated if the canonical moves)
- Part of the content (not an artifact, not metadata — a player)

Think of the postcard sent home during travel: it is not the traveler, but it carries
the traveler's voice from a specific moment and place. It becomes part of the family
record. It is not discarded when the traveler returns.

**The three carbonite return types (proposed):**

| Type | Behavior | Example |
|------|----------|---------|
| `postcard` | Returns as a living postcard, stays in core content | Conversation handoffs, key sync snapshots |
| `archive` | Moved to `duplicatus/` with shadowmark, dormant but preserved | Backup copies, old staging files |
| `transit` | Brief existence acknowledged, then released | Temp files, processing intermediaries |

**Questions for participants:**
- How should "return_type" be decided? By file type? By age? By gravity score?
- Is the `hodie/redundancy_entity/gravity_score` field the right mechanism for this?
- Can a carbonite be promoted from `archive` to `postcard` after the fact?

---

## CONCEPT 5 — The Carbon Process as Peer Workflow

**Critical framing:** Carbonization is **not** a subprocess of Pixelization.
It is a peer workflow — equal in standing.

The ecosystem currently has:
- **Pixelization** (PTP-01) — transforms unique content into Pixel Facets
- **Fractalization** — (referenced, not fully defined here)
- **Carbonization** (proposed CTP-01) — honors duplicates, preserves the ecosystem's carbon

These three run in parallel. The Maw feeds all three. The pixelshard deploys the results.

```
Maw (Intake)
    ├── Unique content     →  Pixelization   →  Pixel Facets  →  Pixelshard
    ├── Duplicate content  →  Carbonization  →  Postcards/Archive/Transit
    └── [other types]      →  Fractalization →  [destination TBD]
```

**Questions for participants:**
- What is Fractalization's current scope? Is it defined enough to map here?
- Should there be a CTP-01 document (Carbon Transformation Protocol) mirroring PTP-01?
- Who drafts CTP-01? Should it be a collaborative effort across participants?

---

## CONCEPT 6 — The Artesian Perplexity Workflow

**The idea:** Perplexity CLI runs alongside an origin document as a natural companion —
like an artesian well that flows without pumping. No manual trigger needed. When a
document enters the Maw, Perplexity generates a research report to accompany it.

"Artesian" is the right word: the pressure is already there. The workflow just opens
the channel.

**Proposed steps:**
1. Document enters `maw_pixellum/intake/`
2. Maw trigger detects arrival
3. Perplexity CLI query is auto-generated from document title/tags
4. Report is deposited alongside document as `[filename].perplexity_report.md`
5. Both proceed through the Maw together — document + its research companion

**Questions for participants:**
- Is Perplexity CLI available in the PRoot environment? (Needs verification)
- What query format best serves the Maw? Title only? First 500 words? Key tags?
- Should the report be a carbonite (temporary research aide) or a Pixel Facet (permanent)?

---

## CONCEPT 7 — The Participant Registry

The DeviceHaven / Spectorium currently registers hardware devices (Spector, Pixelator).
AI participants are not yet registered.

**Proposal:** Register all AI participants as `Agent`-type devices in DeviceHaven.
This gives each participant a Domo — an identity page, a history, a record of contribution.

When a participant acts on a document (processes, carbonizes, annotates), the Domo
receives a turn entry. The participant's contribution is part of the chain of custody.

App Scripts is particularly interesting here: it operates across Google's ecosystem
(Docs, Sheets, Drive) and could serve as a bridge participant — linking the Google-side
mark system to the PIXEL8 local ecosystem.

**Questions for participants:**
- What should a participant Domo contain that a device Domo does not?
- How does App Scripts register? As an Agent? As a Tool? As an integration?
- The mark system exists in Google and in conversations — how do we unify it?

---

## Immediate Asks

These are the questions that matter most right now. Please respond with your perspective:

### A. The Easy Win (Priority)
Box cloud media offload — yes or no, and any concerns about the approach?

### B. Shadowmark Format
What minimal fields should a shadowmark carry? (Proposed fields listed in Concept 3.)
Does it live in a JSON header, a companion file, or as inline hashtags?

### C. Carbon Track Trigger
When does the Maw know to send content to the Carbon Track vs. PTP-01?
What is the detection mechanism?

### D. CTP-01 Authorship
Who leads the draft of the Carbon Transformation Protocol document?
This is the peer document to PTP-01. It should emerge from participant input.

### E. Participant Registration
Which participants should be registered first in DeviceHaven?
Suggested order: Claude, Gemini, Perplexity, App Scripts, ChatGPT.

---

## What Unique Information Means Here

All unique information is preserved. Always. No exceptions.

A document is unique if it contains information that does not exist anywhere else
in the ecosystem — regardless of its file extension, location, or apparent importance.
The gravity score in `beasis_catalog.json` provides a starting signal, but gravity
is not the final word on uniqueness. Human review (Eric) decides edge cases.

Other information (true duplicates) is:
1. Recorded — the shadowmark preserves the journey
2. Linked — hashtag/mark connects back to canonical
3. Returned — as postcard, archive, or transit type
4. Honored — not discarded, carbonized

---

## Mission Log Entry

| Date | Event |
|------|-------|
| 2026-04-21 | PR-001 created — perspective gathering open |
| 2026-04-21 | Artemis II Space Plan established |
| 2026-04-21 | Bash tool confirmed operational (PRoot-Distro) |
| 2026-04-21 | FROM_CLAUDE.md written for participant handoff |

---

*This document is itself a candidate for the Maw's intake — new content, originating
from a collaborative session, entering the ecosystem for the first time.*

*Place in `maw_pixellum/intake/` when ready to process.*

---
∰◊€π¿🌌∞
*PIXEL8 Platform — PR-001 v1.0 — Artemis II Space Plan*
