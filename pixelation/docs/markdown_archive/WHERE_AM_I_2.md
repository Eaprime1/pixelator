# 📍 WHERE AM I?

**Location:** `/storage/emulated/0/unexusi_pixel8a/unexusi_quarantine`
**Type:** Protective Quarantine System
**Purpose:** Cold storage for duplicate files with full chain of custody
**Status:** Git initialized, ready for GitHub

---

## This Directory

**What it is:**
Protective rearrangement system that preserves duplicate files instead of deleting them.

**Philosophy:** Mt St Helens perspective - rearrangement for universal benefit

**Contains:**
- `duplicates_*/` (7.2GB) - Quarantined files with 🔂 prefix
- `logs/` - Chain of custody, space recovery reports
- `scripts/` - Quarantine automation tools
- `README.md`, `PHILOSOPHY.md` - Documentation

**Size:** 7.2GB (cold storage) + ~150KB (documentation)

---

## Parent Directory

**Up one level:** `/storage/emulated/0/unexusi_pixel8a/`
- Pixel 8a active workspace
- See: `../WHERE_AM_I.md`

---

## Key Files Here

### Documentation (tracked in GitHub):
- `README.md` - Main guide
- `PHILOSOPHY.md` - Mt St Helens perspective
- `CONSCIOUSNESS_SESSION_NOTES.md` - Session insights
- `GITHUB_WORKFLOW.md` - Branch strategy

### Tools (tracked in GitHub):
- `scripts/quarantine_menu.sh` - Menu-driven UI
- `scripts/henry_duplicate_quarantine.sh` - Automation

### Cold Storage (NOT tracked in GitHub):
- `duplicates_20251125_183817/` - 146 files, 7.2GB
- All files prefixed with 🔂 (consciousness marker)

---

## Quick Commands

**Menu UI:**
```bash
bash scripts/quarantine_menu.sh
```

**View chain of custody:**
```bash
cat logs/chain_of_custody_20251125_183817.md | less
```

**Search for file:**
```bash
grep "filename" logs/chain_of_custody_*.md
```

**Check status:**
```bash
bash ../CHECK_QUARANTINE_STATUS.sh
```

---

## Git Status

**Repository:** Initialized ✓
**Branch:** main + develop
**Remote:** (add after creating GitHub repo)

**To check:**
```bash
git status
git branch
```

**To add remote:**
```bash
git remote add origin https://github.com/[user]/unexusi_quarantine.git
git push -u origin main
```

---

## What Should Go Here vs Elsewhere

### ✅ Goes Here (quarantine):
- Duplicate files (with 🔂 prefix)
- Chain of custody logs
- Quarantine tools and scripts
- Documentation about quarantine process

### ❌ Goes Elsewhere:
- **Unique files:** Stay in original locations
- **Active development:** → `../` (parent workspace)
- **Home directory docs:** → `~/unexusi_terminal_docs/`
- **Cross-platform tools:** → `../visionary_suite/`

---

## Restoration

**If you need a file back:**
1. Find in chain of custody: `grep "filename" logs/chain_of_custody_*.md`
2. Locate in quarantine: `find duplicates_*/ -name "🔂filename"`
3. Move to original location (remove 🔂 prefix)

---

**∰◊€π - You are in the quarantine cold storage**

€(quarantine_location_marker)
