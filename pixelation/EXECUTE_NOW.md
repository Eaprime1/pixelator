# Execute PIXEL Domos - Quick Command Reference

**Run these commands in order** to bring your PIXEL domos to life!

---

## 🚀 Method 1: All-In-One Discovery

Run all audit tools at once:

```bash
cd /data/data/com.termux/files/home/pixelation
chmod +x run-all-discovery.sh
./run-all-discovery.sh
```

This runs:
1. Content audit (analyzes everything)
2. Duplicate finder (finds duplicate files)
3. Large file finder (identifies large files)

---

## 🔍 Method 2: Step-by-Step

### Step 1: Make Scripts Executable

```bash
cd /data/data/com.termux/files/home/pixelation
chmod +x tools/sync/basic-sync.sh
chmod +x tools/utilities/*.sh
chmod +x run-audit.sh
chmod +x run-all-discovery.sh
```

### Step 2: Run Content Audit

```bash
./tools/utilities/content-audit.sh
```

**What it does**: Scans all content and generates a comprehensive report
**Output**: `.sync/content-audit-[timestamp].md`

### Step 3: Find Duplicates

```bash
./tools/utilities/find-duplicates.sh
```

**What it does**: Identifies duplicate files
**Output**: Console output and/or duplicate report
**Note**: Moves duplicates to `/data/data/com.termux/files/home/PIXEL_DUPLICATES/`

### Step 4: Find Large Files

```bash
./tools/utilities/find-large-files.sh
```

**What it does**: Identifies files over size thresholds
**Output**: `PIXEL_DUPLICATES/large-files-report.txt`
**Thresholds**:
- Images: >10MB
- Videos: >50MB
- Archives: >25MB
- Docs: >5MB
- Code: >1MB

---

## 🔄 Run the Sync

After discovery, test the sync system:

```bash
./tools/sync/basic-sync.sh
```

**What it does**:
- Syncs `projects/shared/` bidirectionally
- Syncs `assets/shared/` bidirectionally
- Syncs `docs/public/` if it exists
- Pulls external-only content (published/, releases/)
- Logs everything to `.sync/sync.log`
- Updates `.sync/last-sync.json`

---

## 🌳 Initialize Git (External)

Set up version control in the external repo:

```bash
cd /data/data/com.termux/files/home/storage/shared/pixelate
chmod +x git-init.sh
chmod +x setup-branches.sh
./git-init.sh
./setup-branches.sh
```

**What it does**:
1. Initializes git repository
2. Creates initial commit
3. Sets up branches (main, pixel8-dev, pixel8a-dev)

---

## 📊 Check Status

### Sync Status
```bash
cat .sync/last-sync.json
```

### Sync Log
```bash
cat .sync/sync.log
```

### Git Status (External)
```bash
cd /data/data/com.termux/files/home/storage/shared/pixelate
git status
git log --oneline --graph --all
```

### View Audit Report
```bash
# Find latest audit
ls -lt .sync/content-audit-*.md | head -1

# View it
cat .sync/content-audit-*.md
```

---

## 🛠 Interactive Organization

Use the migration helper for guided content organization:

```bash
./tools/utilities/migration-helper.sh
```

**Interactive menu** lets you:
- Move files to proper locations
- Archive old content
- Handle duplicates
- Batch rename
- View structure

---

## ⚡ Quick Copy-Paste Commands

**Complete setup in one go:**

```bash
# Navigate to pixelation
cd /data/data/com.termux/files/home/pixelation

# Make everything executable
chmod +x run-all-discovery.sh run-audit.sh tools/sync/basic-sync.sh tools/utilities/*.sh

# Run discovery suite
./run-all-discovery.sh

# Run sync
./tools/sync/basic-sync.sh

# Initialize git (external)
cd /data/data/com.termux/files/home/storage/shared/pixelate
chmod +x git-init.sh setup-branches.sh
./git-init.sh
./setup-branches.sh

# Back to pixelation
cd /data/data/com.termux/files/home/pixelation

# Check everything
echo "=== Sync Status ===" && cat .sync/last-sync.json
echo "" && echo "=== Git Status ==="
cd /data/data/com.termux/files/home/storage/shared/pixelate && git status
```

---

## 🎯 What to Expect

### Content Audit Output
- Total file count
- Total size
- Directory structure
- File type distribution
- Large files list
- Recent files
- Oldest files
- Recommendations

### Duplicate Finder Output
- List of duplicate file groups
- Option to review or auto-move
- Logged to PIXEL_DUPLICATES/DUPLICATE_LOG.md

### Large File Finder Output
- Files categorized by type
- Sorted by size
- Saved to report file
- Top 20 largest displayed

### Sync Output
- Files synced
- Sync direction
- Any conflicts
- Completion status
- Timestamp and size info

---

## 🚨 Troubleshooting

### Permission Denied
```bash
chmod +x script-name.sh
```

### Script Not Found
```bash
# Make sure you're in pixelation directory
cd /data/data/com.termux/files/home/pixelation
pwd  # Verify location
```

### rsync Not Found
```bash
pkg install rsync
```

### fdupes Not Found (for duplicates)
```bash
pkg install fdupes
# Or the script will use md5sum fallback
```

### Git Not Found
```bash
pkg install git
```

---

## 📝 Notes

- **First run may take time** depending on content volume
- **Review reports** before making changes
- **Sync is bidirectional** - changes go both ways
- **Git is in external only** - internal uses sync, not git
- **Duplicates go outside** - to PIXEL_DUPLICATES, not in main structure

---

**Ready to execute?** Start with the quick copy-paste commands above!

🌟 **The PIXEL domos is ready for you.**
