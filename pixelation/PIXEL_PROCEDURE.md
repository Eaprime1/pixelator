# PIXEL Domos Implementation Procedures
## Step-by-Step Guide

**Version**: 1.0
**Last Updated**: 2026-02-04

---

## 📖 Table of Contents

1. [Foundation Setup](#foundation-setup)
2. [Git Repository Initialization](#git-repository-initialization)
3. [Sync System Setup](#sync-system-setup)
4. [Content Audit & Migration](#content-audit--migration)
5. [Documentation Updates](#documentation-updates)
6. [Testing & Validation](#testing--validation)
7. [Maintenance Procedures](#maintenance-procedures)

---

## 1. Foundation Setup

### 1.1 Create Directory Structure

```bash
# Navigate to pixelation (internal)
cd /data/data/com.termux/files/home/pixelation

# Create core directories
mkdir -p .claude/{memory,plugins}
mkdir -p .eric/{notes,ideas,config}
mkdir -p docs/{architecture,guides,api,vision}
mkdir -p projects/{pixel8,pixel8a,experimental}
mkdir -p assets/{images,videos,audio,data}
mkdir -p tools/{sync,automation,utilities}
mkdir -p archive/{sorted,legacy}
mkdir -p .sync

# Create external shared structure
mkdir -p /data/data/com.termux/files/home/storage/shared/pixelate
```

### 1.2 Create Configuration Files

```bash
# Create sync rules
cat > .sync/rules.yaml << 'EOF'
# Sync Rules Configuration
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

exclude_patterns:
  - "*.tmp"
  - "*.log"
  - ".DS_Store"
  - "node_modules/"
  - ".git/"
EOF

# Create sync exclude list
cat > .sync/exclude.txt << 'EOF'
.git/
node_modules/
*.tmp
*.log
.DS_Store
*.swp
*~
EOF
```

---

## 2. Git Repository Initialization

### 2.1 Initialize External Repository

```bash
# Navigate to external shared location
cd /data/data/com.termux/files/home/storage/shared/pixelate

# Initialize git
git init

# Create .gitignore
cat > .gitignore << 'EOF'
# Temporary files
*.tmp
*.log
*.swp
*~

# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.sublime-*

# Build outputs
dist/
build/
*.pyc
__pycache__/

# Dependencies
node_modules/
vendor/

# Sensitive
.env
*.key
*.pem
secrets/

# Sync metadata
.sync/last-sync.json
EOF

# Initial commit
git add .
git commit -m "Initial commit: PIXEL domos structure"
```

### 2.2 Set Up Remote (Optional)

```bash
# If using GitHub/GitLab
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

---

## 3. Sync System Setup

### 3.1 Create Basic Sync Script

```bash
# Create sync utility
cat > tools/sync/basic-sync.sh << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos Basic Sync Script
# Syncs between internal (pixelation) and external (pixelate)

INTERNAL="/data/data/com.termux/files/home/pixelation"
EXTERNAL="/data/data/com.termux/files/home/storage/shared/pixelate"
EXCLUDE_FILE="${INTERNAL}/.sync/exclude.txt"
LOG_FILE="${INTERNAL}/.sync/sync.log"

# Timestamp
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting sync..." >> "$LOG_FILE"

# Bidirectional sync
# Internal -> External
rsync -avz --delete --exclude-from="$EXCLUDE_FILE" \
  "$INTERNAL/" "$EXTERNAL/" >> "$LOG_FILE" 2>&1

# External -> Internal
rsync -avz --exclude-from="$EXCLUDE_FILE" \
  "$EXTERNAL/" "$INTERNAL/" >> "$LOG_FILE" 2>&1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] Sync completed." >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"
EOF

chmod +x tools/sync/basic-sync.sh
```

### 3.2 Test Sync

```bash
# Run initial sync
./tools/sync/basic-sync.sh

# Check log
cat .sync/sync.log
```

---

## 4. Content Audit & Migration

### 4.1 Audit Current Content

```bash
# Create content inventory
cd /data/data/com.termux/files/home/pixelation

# List all directories
find . -type d -not -path '*/\.*' > .sync/directory-inventory.txt

# List all files with sizes
find . -type f -not -path '*/\.*' -exec ls -lh {} \; > .sync/file-inventory.txt

# Identify "sort" folders
find . -type d -name '*sort*' -o -name '*temp*' -o -name '*tmp*'
```

### 4.2 Categorize Content

Create a categorization plan:

1. **Keep & Move**: Content to keep in proper location
2. **Archive**: Old but potentially useful content
3. **Delete**: Truly unnecessary content

### 4.3 Execute Migration

```bash
# Example: Move content from sort folder
# Adjust paths as needed

# Move to appropriate location
mv old-sort-folder/project-name projects/pixel8/

# Archive old content
mv old-project/ archive/legacy/old-project-$(date +%Y%m%d)

# Delete unnecessary
rm -rf truly-unnecessary-folder/
```

### 4.4 Document Changes

```bash
# Create restructure log entry
cat >> RESTRUCTURE_LOG.md << 'EOF'
## [2026-02-04] Content Migration

### Moved
- old-sort-folder/project-name -> projects/pixel8/project-name

### Archived
- old-project -> archive/legacy/old-project-20260204

### Deleted
- truly-unnecessary-folder/

### Reason
Part of PIXEL domos restructure initiative.
EOF
```

---

## 5. Documentation Updates

### 5.1 Update claude.md

```bash
# Edit claude.md to include new structure
cat > claude.md << 'EOF'
# PIXEL Domos - Claude Code Context

## Project Overview
This is the PIXEL domos - a unified ecosystem for all pixel-related projects and development.

## Structure
- **pixelation** (internal): /data/data/com.termux/files/home/pixelation
- **pixelate** (external): /data/data/com.termux/files/home/storage/shared/pixelate
- **Relationship**: Bidirectionally synced, entangled system

## Key Directories
- `.claude/` - Claude Code configuration
- `.eric/` - Personal notes and preferences
- `projects/` - Active projects (pixel8, pixel8a, experimental)
- `docs/` - Documentation
- `assets/` - Media resources
- `tools/` - Utilities and scripts

## Workflow
1. Develop in pixelation (internal)
2. Sync to pixelate (external) for sharing
3. Changes sync bidirectionally

## Important Notes
- Always check sync status before major changes
- Use provided tools for common tasks
- Document significant changes in RESTRUCTURE_LOG.md

For detailed information, see PIXEL_DOMOS_MASTER_PLAN.md
EOF
```

### 5.2 Create .eric Notes

```bash
# Create personal notes structure
cat > .eric/notes/vision.md << 'EOF'
# PIXEL Vision - Personal Notes

## Core Concept
[Your vision and thoughts here]

## Goals
- Goal 1
- Goal 2

## Ideas
- Idea 1
- Idea 2
EOF
```

### 5.3 Create README.md

```bash
cat > README.md << 'EOF'
# PIXEL Domos

Welcome to the PIXEL domos - your unified ecosystem for pixel8 and pixel8a projects.

## Quick Start

1. **Explore**: Browse projects/ to see active work
2. **Sync**: Run `./tools/sync/basic-sync.sh` to sync internal/external
3. **Document**: Update relevant docs/ as you work
4. **Enjoy**: Create and build amazing things!

## Structure

See `PIXEL_DOMOS_MASTER_PLAN.md` for complete architecture.

## Contact

For questions or ideas, check `.eric/notes/`
EOF
```

---

## 6. Testing & Validation

### 6.1 Verify Structure

```bash
# Check that all directories exist
tree -L 2 -d

# Verify permissions
ls -la

# Check sync configuration
cat .sync/rules.yaml
```

### 6.2 Test Sync

```bash
# Create test file in internal
echo "Test sync" > test-sync.txt

# Run sync
./tools/sync/basic-sync.sh

# Verify in external
cat /data/data/com.termux/files/home/storage/shared/pixelate/test-sync.txt

# Cleanup
rm test-sync.txt
./tools/sync/basic-sync.sh
```

### 6.3 Validate Git

```bash
cd /data/data/com.termux/files/home/storage/shared/pixelate
git status
git log
```

---

## 7. Maintenance Procedures

### 7.1 Regular Sync

```bash
# Run sync manually
./tools/sync/basic-sync.sh

# Or set up automatic sync (optional)
# Add to crontab or use file watchers
```

### 7.2 Periodic Cleanup

```bash
# Weekly: Review and clean archive
cd archive/
ls -lht

# Monthly: Review and update docs
cd docs/
# Update relevant documentation

# Quarterly: Full audit
# Review entire structure and optimize
```

### 7.3 Backup Verification

```bash
# Verify git commits
cd /data/data/com.termux/files/home/storage/shared/pixelate
git log --oneline -10

# Check sync logs
tail -50 .sync/sync.log

# Verify critical files exist
ls -lh PIXEL_DOMOS_MASTER_PLAN.md
ls -lh claude.md
```

---

## 🎯 Next Steps

After completing these procedures:

1. ✅ Verify all structure is in place
2. ✅ Test sync functionality
3. ✅ Begin content migration
4. ✅ Update documentation continuously
5. ✅ Establish regular sync cadence

---

## 📞 Troubleshooting

### Sync Issues
- Check permissions: `ls -la`
- Verify paths in sync script
- Review .sync/sync.log

### Git Issues
- Check git status: `git status`
- Review git log: `git log`
- Verify remote: `git remote -v`

### Permission Issues
- Fix permissions: `chmod -R u+rw directory/`
- Check ownership: `ls -la`

---

*Follow these procedures systematically for successful PIXEL domos implementation.*
