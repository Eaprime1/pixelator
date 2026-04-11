# Domos - Domain Models
**Stage**: DOMAIN KNOWLEDGE
**Purpose**: Domos (domain models/documents) with built-in vetting submission
**Date**: 2026-02-14

---

## What is a Domos?

A **domos** is a domain model - a document, folder, or entity that represents a defined domain of knowledge or responsibility within the pixelator ecosystem.

All domos require vetting before they are considered authoritative.

## Structure

```
domos/
├── vetting/            ← SUBMISSION FOLDER (Drive shortcut compatible)
│   ├── inbox/          ← Drop domos here to submit for vetting
│   └── reports/        ← Vetting reports returned here
│
├── [domos_name]/       ← Individual domos folders
│   ├── README.md       ← Domos definition and purpose
│   ├── vetting/        ← This domos's own vetting history
│   └── [content]
│
└── approved/           ← Vetted and approved domos
```

## Vetting Submission Flow

```
Domos created
     ↓
Added to domos/vetting/inbox/  (or Drive shortcut)
     ↓
Vetting system picks up
     ↓
Report generated with file ID
     ↓
Decision: APPROVED → domos/approved/
         NEEDS WORK → returned to creator
     ↓
Incentive earned by submitter
```

## Google Drive Integration

The `domos/vetting/inbox/` folder works as a **Drive shortcut destination**:
- In Google Drive, create a shortcut pointing here
- Drop domos files into the Drive shortcut
- They appear in `inbox/` on the phone
- Vetting processes them
- Reports sync back

This creates a **two-way interaction** between Drive and phone.

## Vetting Incentive Economy

When a domos is submitted for vetting:
- **Submitter earns** vetting incentive reward
- **Reviewer earns** review reward
- **Report generated** with full details
- **File ID logged** for interaction tracking
- **Ownership transfers** on approval

---

∰◊€π¿🌌∞
€(domos_vetting_submission)
*Every domos earns its place through vetting*
