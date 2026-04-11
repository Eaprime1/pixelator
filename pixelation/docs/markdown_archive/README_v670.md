# PIXEL Domos - Internal Repository (pixel8)

Welcome to **pixelation** - the internal development workspace of the PIXEL domos ecosystem.

## 🌟 Overview

This is **pixel8** (internal) - the private development side of the PIXEL ecosystem that syncs selectively with **pixel8a** (external).

### Location
- **Internal (pixel8)**: `/data/data/com.termux/files/home/pixelation` (this workspace)
- **External (pixel8a)**: `/data/data/com.termux/files/home/storage/shared/pixelate`

### Relationship
These two locations form an **entangled system** - specific directories sync bidirectionally while others remain private or public.

---

## 📁 Structure

```
pixelation/ (pixel8 - internal)
├── .claude/                    # Claude Code configuration
│   ├── memory/                 # Persistent AI memory
│   └── plugins/                # Custom plugins
│
├── .eric/                      # Personal workspace
│   ├── notes/                  # Development notes
│   ├── ideas/                  # Idea capture
│   └── config/                 # Personal settings
│
├── docs/                       # Documentation
│   ├── architecture/           # System design
│   ├── guides/                 # How-to guides
│   ├── api/                    # API documentation
│   └── vision/                 # Vision & planning
│
├── projects/                   # Active projects
│   ├── pixel8/                 # Internal-only projects
│   ├── pixel8a/                # External projects
│   ├── experimental/           # Experiments (internal-only)
│   └── shared/                 # Bidirectionally synced
│
├── assets/                     # Media resources
│   ├── images/
│   ├── videos/
│   ├── audio/
│   ├── data/
│   └── shared/                 # Synced assets
│
├── tools/                      # Development tools (internal-only)
│   ├── sync/                   # Sync utilities
│   ├── automation/             # Automation scripts
│   └── utilities/              # General utilities
│
├── archive/                    # Historical content
│   ├── sorted/                 # Archived sorted content
│   └── legacy/                 # Legacy projects
│
├── .sync/                      # Sync configuration
│   ├── rules.yaml              # Sync rules
│   ├── exclude.txt             # Exclusion patterns
│   └── last-sync.json          # Sync state
│
├── PIXEL_DOMOS_MASTER_PLAN.md  # Architecture & vision
├── PIXEL_TODO.md               # Task tracking
├── PIXEL_PROCEDURE.md          # Procedures
├── RESTRUCTURE_LOG.md          # Change log
└── README.md                   # This file
```

---

## 🔄 Sync Model

### Bidirectional Sync (Both Ways)
- `projects/shared/` - Shared projects
- `docs/public/` - Public documentation (when created)
- `assets/shared/` - Shared media

### Internal-Only (Never Synced Out)
- `.claude/` - AI configuration
- `.eric/` - Personal notes
- `tools/` - Development utilities
- `projects/experimental/` - Experiments
- `projects/pixel8/` - Internal projects

### External-Only (Lives in pixel8a)
- `published/` - Published releases
- `releases/` - Release artifacts

See `.sync/rules.yaml` for complete sync configuration.

---

## 🚀 Quick Start

### Daily Workflow
1. Work in appropriate project folders
2. Run sync when ready to share: `./tools/sync/basic-sync.sh`
3. Review sync log: `cat .sync/sync.log`
4. Commit changes in external if needed

### Finding Content
- **Your notes**: `.eric/notes/`
- **Active projects**: `projects/`
- **Documentation**: `docs/`
- **Tools & scripts**: `tools/`

---

## 🛠 Tools

### Sync Tools
- `tools/sync/basic-sync.sh` - Run bidirectional sync
- `.sync/rules.yaml` - Configure sync behavior

### Utilities
- `tools/utilities/find-duplicates.sh` - Find duplicate files
- `tools/utilities/find-large-files.sh` - Find large files

---

## 📖 Documentation

- **Master Plan**: `PIXEL_DOMOS_MASTER_PLAN.md` - Complete architecture
- **Procedures**: `PIXEL_PROCEDURE.md` - Step-by-step guides
- **TODO**: `PIXEL_TODO.md` - Task tracking
- **Change Log**: `RESTRUCTURE_LOG.md` - All changes

---

## 🎯 Purpose

**pixelation** serves as:
- **Development workspace** for all PIXEL projects
- **Private creative space** with personal notes
- **Tool repository** for automation and utilities
- **Sync hub** for managing internal/external relationship

---

## 🔗 Related

- **External Repository (pixel8a)**: `/data/data/com.termux/files/home/storage/shared/pixelate`
- **Duplicate Storage**: `/data/data/com.termux/files/home/PIXEL_DUPLICATES` (temporary)

---

## ⚡ Git Branches

The external repository (pixel8a) uses branches:
- `main` - Stable, synchronized state
- `pixel8-dev` - Development from internal
- `pixel8a-dev` - Development from external
- Feature branches as needed

See external repo for git workflow details.

---

**Created**: 2026-02-04
**Version**: 1.0
**Status**: Active Development

---

*Part of the PIXEL domos ecosystem - where pixel8 (internal) and pixel8a (external) exist in entangled harmony.*
