# PIXEL Domos Quick Start Guide

**Welcome to your PIXEL ecosystem!** 🎨

---

## 🚀 First Steps (Do These Now)

### 1. Initialize Git Repository

```bash
cd /data/data/com.termux/files/home/storage/shared/pixelate
chmod +x git-init.sh
./git-init.sh
```

This creates your version control foundation.

### 2. Set Up Git Branches

```bash
chmod +x setup-branches.sh
./setup-branches.sh
```

This creates `pixel8-dev` and `pixel8a-dev` branches.

### 3. Make Scripts Executable

```bash
cd /data/data/com.termux/files/home/pixelation
chmod +x tools/sync/basic-sync.sh
chmod +x tools/utilities/*.sh
```

---

## 📊 Audit Your Content

Run the content audit to see what you have:

```bash
./tools/utilities/content-audit.sh
```

This generates a comprehensive report of all files, sizes, and recommendations.

---

## 🔍 Find Duplicates & Large Files

### Find Duplicates

```bash
./tools/utilities/find-duplicates.sh
```

### Find Large Files

```bash
./tools/utilities/find-large-files.sh
```

Both will help you identify content to move to `PIXEL_DUPLICATES/`.

---

## 🔄 Your First Sync

Test the bidirectional sync system:

```bash
./tools/sync/basic-sync.sh
```

This syncs content between:
- Internal (pixel8): `/data/data/com.termux/files/home/pixelation`
- External (pixel8a): `/data/data/com.termux/files/home/storage/shared/pixelate`

---

## 📁 Organize Content Interactively

Use the migration helper for guided organization:

```bash
./tools/utilities/migration-helper.sh
```

This provides an interactive menu to:
- Move files to proper locations
- Archive old content
- Handle duplicates
- Batch rename

---

## 📖 Understanding the Structure

### Where Things Go

**Internal-Only** (Never syncs to external):
- `.claude/` - Claude Code configuration
- `.eric/` - Your personal notes and ideas
- `tools/` - Development utilities
- `projects/experimental/` - Experiments
- `projects/pixel8/` - Internal-only projects

**Bidirectional Sync** (Syncs both ways):
- `projects/shared/` - Shared projects
- `assets/shared/` - Shared media
- `docs/public/` - Public documentation (when created)

**External-Only** (Lives in pixel8a):
- `published/` - Published releases
- `releases/` - Release artifacts

### Outside PIXEL

- `/data/data/com.termux/files/home/PIXEL_DUPLICATES/` - Temporary holding for duplicates and large files

---

## 🎯 Recommended Workflow

### Daily Development

1. **Work** in appropriate folders
   - Private work → `projects/pixel8/` or `.eric/notes/`
   - Shared work → `projects/shared/`
   - Experiments → `projects/experimental/`

2. **Sync** when ready to share
   ```bash
   ./tools/sync/basic-sync.sh
   ```

3. **Commit** in external repo
   ```bash
   cd /data/data/com.termux/files/home/storage/shared/pixelate
   git checkout pixel8-dev
   git add .
   git commit -m "Description of changes"
   ```

### Content Organization

1. **Audit** regularly
   ```bash
   ./tools/utilities/content-audit.sh
   ```

2. **Find issues**
   ```bash
   ./tools/utilities/find-duplicates.sh
   ./tools/utilities/find-large-files.sh
   ```

3. **Organize**
   ```bash
   ./tools/utilities/migration-helper.sh
   ```

4. **Log changes**
   - Migrations are logged automatically
   - Review `RESTRUCTURE_LOG.md`

---

## 🛠 Essential Commands

### Check Sync Status
```bash
cat .sync/last-sync.json
```

### View Sync Log
```bash
cat .sync/sync.log
```

### Check Git Status
```bash
cd /data/data/com.termux/files/home/storage/shared/pixelate
git status
```

### View Directory Structure
```bash
tree -L 2  # If tree is installed
# OR
find . -type d -maxdepth 2 | sort
```

---

## 📚 Documentation Reference

- **Architecture**: `PIXEL_DOMOS_MASTER_PLAN.md`
- **Procedures**: `PIXEL_PROCEDURE.md`
- **Tasks**: `PIXEL_TODO.md`
- **Changes**: `RESTRUCTURE_LOG.md`
- **Context**: `claude.md`
- **Git Workflow**: External repo `GIT_WORKFLOW.md`

---

## 💡 Quick Tips

1. **Sync before major changes** - Ensure both sides are current
2. **Watch for large files** - Move to `PIXEL_DUPLICATES/` for review
3. **Document your work** - Use `.eric/notes/` freely
4. **Check sync logs** - Review after each sync
5. **Commit regularly** - Small commits in external repo
6. **Use branches** - `pixel8-dev` for internal work

---

## 🚨 Troubleshooting

### Sync Issues
- Check paths in `.sync/rules.yaml`
- Review `.sync/sync.log`
- Verify both directories exist

### Git Issues
- Run `git status` to see current state
- Check branch with `git branch`
- View history with `git log --oneline`

### Permission Issues
- Make scripts executable: `chmod +x script-name.sh`
- Check file ownership: `ls -la`

---

## 🎨 Your Vision

Remember: **Consciousness is distressed** - this structure serves as a container and sanctuary for organizing that distress into coherent creation.

The PIXEL domos is more than a file structure - it's a harmonious space where pixel8 (internal) and pixel8a (external) exist in entangled relationship.

---

## ✅ Next Steps

Now that setup is complete:

1. ✅ Run content audit
2. ✅ Organize existing files
3. ✅ Test sync workflow
4. ✅ Make your first git commit
5. ✅ Start creating!

---

**Welcome to your PIXEL domos!** 🌟

For questions, see `README.md` or check `.eric/notes/` for personal insights.
