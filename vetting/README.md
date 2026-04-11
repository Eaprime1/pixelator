# Vetting - Project-Wide Quality Queue
**Stage**: VETTING
**Purpose**: Quality review, approval, and transfer of ownership
**Date**: 2026-02-14

---

## What is Vetting?

The **quality gate** for the pixelator system. When a document or folder is submitted here, it enters the vetting economy - a transfer of responsibility and ownership through quality review.

## What Gets Vetted?

- All domos folders (required)
- Important documents before promotion
- Content before Drive sync
- Anything needing quality sign-off
- Submissions from pixelate/ ready for approval

## The Vetting Economy

### Submission = Incentive

When a domos or document submits to vetting:
1. **Submission logged** with file ID
2. **Vetting incentive** earned (reward for participating)
3. **Reviewer assigned** (or self-review)
4. **Vetting report generated**:
   - Decision: APPROVED / NEEDS WORK / REJECTED
   - Information: What was reviewed
   - File ID: For interaction logging
   - Incentive: Reward amount
5. **Ownership transfers** based on decision

### Why the Economy?

Vetting creates value by:
- Maintaining quality standards
- Rewarding participation
- Creating interaction records
- Building trust in content
- Enabling Drive integration

## Vetting Folder Structure

```
vetting/
├── inbox/          ← New submissions arrive here
├── in_review/      ← Currently being reviewed
├── approved/       ← Passed vetting
├── needs_work/     ← Returned for revision
└── reports/        ← All vetting reports (chain of custody)
```

## Vetting Report Format

Each submission generates a report:
```json
{
  "vetting_id": "UUID",
  "submission_date": "2026-02-14T...",
  "file_id": "Google Drive File ID or local path",
  "submitter": "domos_name or folder_name",
  "reviewer": "entity_name",
  "decision": "APPROVED | NEEDS_WORK | REJECTED",
  "incentive_earned": 1,
  "information": {
    "content_reviewed": "...",
    "quality_notes": "...",
    "next_steps": "..."
  }
}
```

## Google Drive Integration

Vetting folders are **Drive shortcut compatible**:
- Create a Drive shortcut to `vetting/inbox/`
- Submit documents by adding them to the shortcut
- Reports sync back to Drive

---

∰◊€π¿🌌∞
€(vetting_economy)
*Quality through incentive, ownership through trust*
