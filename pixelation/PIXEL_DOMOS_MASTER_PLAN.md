# PIXEL Domos Master Plan
## Vision: Unified Quantum-Inspired PIXEL Ecosystem

**Last Updated**: 2026-02-04

---

## 🎯 Core Concept

Create an entangled, bidirectional ecosystem where:
- **pixelation** (internal) = Development workspace, creative studio, processing center
- **pixelate** (external shared) = Public interface, shared artifacts, distribution point
- **Entanglement** = Bidirectional sync ensuring both spaces reflect each other's state

---

## 📐 Architecture

### Primary Locations
```
Internal (pixel8):  /data/data/com.termux/files/home/pixelation
External (pixel8a): /data/data/com.termux/files/home/storage/shared/pixelate
```

### Domos Structure

```
pixelation/
├── .claude/                    # Claude Code configuration
│   ├── memory/                 # Persistent memory across sessions
│   ├── plugins/                # Custom plugins
│   └── keybindings.json        # Custom keybindings
│
├── .eric/                      # Eric's personal notes & preferences
│   ├── notes/                  # Personal development notes
│   ├── ideas/                  # Idea capture
│   └── config/                 # Personal configurations
│
├── docs/                       # Documentation hub
│   ├── architecture/           # System design & architecture
│   ├── guides/                 # How-to guides
│   ├── api/                    # API documentation
│   └── vision/                 # Vision & planning documents
│
├── projects/                   # Active project development
│   ├── pixel8/                 # Internal pixel8 projects
│   ├── pixel8a/                # External pixel8a projects
│   └── experimental/           # Experimental work
│
├── assets/                     # Media & resources
│   ├── images/                 # Image assets
│   ├── videos/                 # Video assets
│   ├── audio/                  # Audio assets
│   └── data/                   # Data files
│
├── tools/                      # Development tools & scripts
│   ├── sync/                   # Sync utilities
│   ├── automation/             # Automation scripts
│   └── utilities/              # General utilities
│
├── archive/                    # Historical & archived content
│   ├── sorted/                 # Previously sorted content
│   └── legacy/                 # Legacy projects
│
├── .sync/                      # Sync metadata & configuration
│   ├── rules.yaml              # Sync rules
│   ├── exclude.txt             # Files to exclude from sync
│   └── last-sync.json          # Last sync state
│
├── claude.md                   # Claude Code project context
├── README.md                   # Project overview
└── CHANGELOG.md                # Change log
```

---

## 🔄 Sync Strategy

### Bidirectional Entanglement

**Philosophy**: Changes in either space should reflect in the other, creating a quantum-like entangled state.

### Sync Rules

1. **Selective Sync**: Not all folders sync both ways
   - Some folders are internal-only
   - Some folders are external-only
   - Some folders bidirectionally sync

2. **Sync Configuration**:
   ```yaml
   bidirectional:
     - projects/shared/
     - docs/public/
     - assets/shared/

   internal_only:
     - .claude/
     - .eric/
     - projects/experimental/
     - tools/

   external_only:
     - published/
     - releases/
   ```

3. **Conflict Resolution**:
   - Timestamp-based (most recent wins)
   - Manual review for critical files
   - Log all conflicts for review

---

## 🚀 Implementation Phases

### Phase 1: Foundation (Quick Wins)
- [ ] Create core directory structure
- [ ] Initialize git repository in pixelate
- [ ] Set up basic sync script
- [ ] Update claude.md with new structure
- [ ] Create .eric/ personal space

### Phase 2: Content Migration
- [ ] Audit existing content
- [ ] Sort "sort" folders
- [ ] Move developed folders
- [ ] Archive outdated content
- [ ] Update all documentation references

### Phase 3: Automation
- [ ] Implement robust bidirectional sync
- [ ] Add conflict resolution
- [ ] Create automation scripts
- [ ] Set up git hooks
- [ ] Add monitoring & logging

### Phase 4: Enhancement
- [ ] Advanced sync features
- [ ] Cloud backup integration
- [ ] Cross-device sync
- [ ] Performance optimization
- [ ] Analytics & insights

---

## 📋 Priority Actions

### Immediate (Today)
1. Create directory structure
2. Initialize git repo
3. Basic sync setup
4. Document current state

### Short-term (This Week)
1. Content audit & sort
2. Move existing projects
3. Update all docs
4. Test sync workflow

### Long-term (This Month)
1. Advanced automation
2. Backup strategy
3. Performance tuning
4. Team collaboration features

---

## 🎨 Naming Conventions

- **pixel8** = Internal development (pixelation)
- **pixel8a** = External shared (pixelate)
- **PIXEL** = Overarching concept/brand
- **Domos** = Home/hub for all PIXEL activities

---

## 📝 Change Log Strategy

All structural changes will be logged in:
- `CHANGELOG.md` - User-facing changes
- `RESTRUCTURE_LOG.md` - Detailed restructuring actions
- `.sync/sync.log` - Sync operations log

---

## 🔧 Tools & Technologies

### Sync Mechanisms (Options)
1. **rsync** - Traditional file sync
2. **syncthing** - Continuous sync
3. **git** - Version control
4. **Custom script** - Tailored solution

### Automation
- Bash scripts
- Python utilities
- Git hooks
- Cron jobs (if needed)

---

## 💡 Quick Wins Identified

1. **Immediate Organization**: Create folder structure now
2. **Git Init**: Version control from day one
3. **Simple Sync**: Basic rsync script for immediate sync
4. **Documentation**: Update claude.md to guide Claude
5. **Personal Space**: .eric/ for your notes and ideas

---

## 🎯 Success Metrics

- [ ] All content organized into logical structure
- [ ] Sync working bidirectionally
- [ ] Documentation up to date
- [ ] Git repository initialized
- [ ] No orphaned files in "sort" folders
- [ ] Clear understanding of pixel8 vs pixel8a distinction

---

## 🤔 Key Decisions Needed

1. **Sync Frequency**: Real-time, on-demand, or scheduled?
2. **Conflict Strategy**: Auto-resolve or manual review?
3. **Backup Approach**: Cloud, local, or both?
4. **Access Control**: Any restrictions between internal/external?

---

## 📚 Related Documents

- `claude.md` - Claude Code context
- `.eric/notes/vision.md` - Personal vision notes
- `docs/architecture/sync-design.md` - Detailed sync design
- `RESTRUCTURE_LOG.md` - Detailed change log

---

*This is a living document - update as the vision evolves.*
