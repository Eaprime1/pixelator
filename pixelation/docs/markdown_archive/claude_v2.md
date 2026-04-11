# PIXEL Domos - Claude Code Context

## Project Overview

**PIXEL Domos** is a unified ecosystem for pixel-related projects with an entangled internal/external architecture.

### Core Concept
- **pixel8 (internal)**: `/data/data/com.termux/files/home/pixelation` - Private development workspace
- **pixel8a (external)**: `/data/data/com.termux/files/home/storage/shared/pixelate` - Public shared space
- **Entanglement**: Bidirectional sync creates quantum-inspired relationship

---

## Architecture

### Directory Structure

```
pixelation/ (internal - you are here)
├── .claude/          # Your configuration
├── .eric/            # Personal notes (private)
├── docs/             # Documentation
├── projects/         # Active projects
│   ├── pixel8/       # Internal-only
│   ├── pixel8a/      # External projects
│   ├── experimental/ # Experiments (private)
│   └── shared/       # Bidirectionally synced
├── assets/           # Media resources
├── tools/            # Development utilities (private)
├── archive/          # Historical content
└── .sync/            # Sync configuration
```

### Sync Rules

**Bidirectional** (syncs both ways):
- `projects/shared/`
- `docs/public/` (when exists)
- `assets/shared/`

**Internal-only** (never synced out):
- `.claude/`, `.eric/`, `tools/`, `projects/experimental/`, `projects/pixel8/`

**External-only** (lives in pixel8a):
- `published/`, `releases/`

Full rules: `.sync/rules.yaml`

---

## Workflow

### Development
1. Work in appropriate folders based on privacy needs
2. Internal-only → `projects/pixel8/` or `projects/experimental/`
3. Shared work → `projects/shared/`
4. External-facing → coordinate with pixel8a

### Syncing
```bash
# Run sync
./tools/sync/basic-sync.sh

# Check sync status
cat .sync/sync.log

# Review sync state
cat .sync/last-sync.json
```

### Content Organization
- **Duplicates** → `/data/data/com.termux/files/home/PIXEL_DUPLICATES/` (outside PIXEL)
- **Large files** → Review with `./tools/utilities/find-large-files.sh`
- **Archive** → `archive/sorted/` or `archive/legacy/`

---

## Key Files

### Planning & Documentation
- `PIXEL_DOMOS_MASTER_PLAN.md` - Complete architecture and vision
- `PIXEL_TODO.md` - Task tracking
- `PIXEL_PROCEDURE.md` - Step-by-step procedures
- `RESTRUCTURE_LOG.md` - Detailed change history
- `README.md` - Project overview

### Configuration
- `.sync/rules.yaml` - Sync configuration
- `.sync/exclude.txt` - Exclusion patterns
- `claude.md` - This file (your context)

### Tools
- `tools/sync/basic-sync.sh` - Bidirectional sync
- `tools/utilities/find-duplicates.sh` - Duplicate finder
- `tools/utilities/find-large-files.sh` - Large file finder

---

## Important Guidelines

### File Operations
1. **Check location first** - Is this internal-only or should it sync?
2. **Watch for duplicates** - Use find-duplicates.sh regularly
3. **Monitor large files** - Keep external repo lean
4. **Document changes** - Update RESTRUCTURE_LOG.md for structural changes

### Sync Safety
1. Review `.sync/sync.log` after sync operations
2. Check conflicts in `.sync/last-sync.json`
3. Don't manually edit sync metadata
4. Test with dry_run first for major changes

### Privacy
- `.eric/` is personal - never sync
- `.claude/` stays internal
- `tools/` remain private
- Experimental work stays in `projects/experimental/`

---

## Git Integration

### External Repository (pixel8a)
The external repo uses git with branches:
- `main` - Stable synchronized state
- `pixel8-dev` - Development from internal
- `pixel8a-dev` - Development from external
- Feature branches as needed

### Workflow
1. Work internally in pixelation
2. Sync to external
3. Commit in external repository
4. Push to remote (if configured)

---

## Quick Reference

### Find Things
- Your notes: `.eric/notes/`
- Documentation: `docs/`
- Active projects: `projects/`
- Tools: `tools/`
- Archives: `archive/`

### Common Tasks
```bash
# Sync internal/external
./tools/sync/basic-sync.sh

# Find duplicates
./tools/utilities/find-duplicates.sh

# Find large files
./tools/utilities/find-large-files.sh

# Check sync status
cat .sync/last-sync.json
```

---

## Notes for Claude

- This is a **living ecosystem** - structure evolves with needs
- **Respect privacy boundaries** - know what syncs and what doesn't
- **Log structural changes** - update RESTRUCTURE_LOG.md
- **Watch for duplicates and large files** - they go outside PIXEL
- **Understand entanglement** - internal and external are related but distinct

---

**Version**: 1.0
**Last Updated**: 2026-02-04
**Status**: Active Development

For detailed architecture, see `PIXEL_DOMOS_MASTER_PLAN.md`
