# Google Drive Trash Restoration Plan
**Date:** 2026-01-09 20:53
**Strategy:** Restore all → Deduplicate locally → Keep control

## Why Restore First?
✅ Safer - nothing gets permanently lost
✅ Can deduplicate with your proven local tools
✅ Full control over what stays/goes
✅ Can verify everything before final cleanup

---

## Step 1: Access Trash (Web Interface)

### Desktop (Recommended for bulk operations):
1. Go to: https://drive.google.com/drive/trash
2. You'll see all 1.191 GiB of trashed items

### Mobile (Pixel 8):
1. Open Google Drive app
2. Menu ☰ → Trash

---

## Step 2: Restore Options

### Option A: Restore Everything at Once (Fastest)
**Best if:** You have space and want everything back

1. In trash view, click checkbox at top to "Select all"
2. Click "Restore" button (↶ icon)
3. Files return to their original locations
4. Wait for "Restored X items" confirmation

⚠️ **Note:** Files go back to where they were before deletion!

### Option B: Selective Restore
**Best if:** You want to review first

1. Sort trash by Name or Date
2. Select groups of files
3. Restore in batches
4. Good for "one hertz" approach!

### Option C: Restore to New Folder (Organized)
**Best if:** You want restored files separate

1. Create new folder in Drive: "RESTORED_FROM_TRASH_20260109"
2. In trash, select files
3. Restore them
4. Move them to the new folder
   - Or use Drive's "Move to" after restore

---

## Step 3: Download Restored Files (If Needed)

### Using rclone:
```bash
# Download restored folder to local
rclone copy \\
    gdrive_terminal:"RESTORED_FROM_TRASH_20260109" \\
    ~/pixel8/Q/restored_trash/ \\
    --progress \\
    --transfers 4
```

### Using Google Drive Sync:
- If you have Drive desktop app
- Or use "Download" from web interface

---

## Step 4: Local Deduplication

You already have experience with this! Use your existing approach:

```bash
# Your proven deduplication method
cd ~/pixel8/Q/

# Compare restored files with existing
# Use your deduplicate_v2.py or similar
python3 deduplicate_v2.py --source restored_trash/ --check
```

---

## Space Considerations

**Current Status:**
- Google Drive used: 9.264 GiB
- Trash size: 1.191 GiB
- After restore: ~10.5 GiB used
- Your Drive total: 2 TiB (plenty of room!)

**Local Space:**
```bash
# Check available space
df -h $HOME
```

If space is tight locally:
- Restore to Drive but don't download yet
- Or download in batches
- Or deduplicate in-place on Drive using rclone

---

## Recommended Workflow

### **"One Hertz Restore & Verify"**

**Phase 1: Restore (5 minutes)**
1. Open Drive trash on desktop browser
2. Select all items
3. Click Restore
4. Confirm success message

**Phase 2: Organize (10 minutes)**
1. Create folder: "TRASH_RESTORED_20260109"
2. Move restored items there for review
3. This keeps them separate from active work

**Phase 3: Download (time varies)**
```bash
# Create local staging area
mkdir -p ~/pixel8/Q/trash_restored_staging

# Download restored items
rclone copy \\
    gdrive_terminal:"TRASH_RESTORED_20260109" \\
    ~/pixel8/Q/trash_restored_staging/ \\
    --progress
```

**Phase 4: Deduplicate (30 min - 1 hour)**
```bash
# Compare with your existing gravity_well
# Your proven scripts will handle this!
cd ~/pixel8/Q/
python3 compare_and_dedupe.py \\
    --restored trash_restored_staging/ \\
    --existing Q_pixel8/gravity_well/ \\
    --action report  # Just report first!
```

---

## Safety Checklist

Before starting:
- [ ] Confirmed Google Drive has space (yes - 2TB free!)
- [ ] Local space check (if downloading)
- [ ] Backup of critical current files
- [ ] Know original location of trashed files

During restore:
- [ ] Note how many items restored
- [ ] Check a few files opened correctly
- [ ] Verify original folder structure

After restore:
- [ ] Verify file count matches expectation
- [ ] Spot-check content of random files
- [ ] Compare against local inventory

---

## Quick Commands Reference

```bash
# Check Drive trash size
rclone about gdrive_terminal:

# Create restoration folder on Drive
rclone mkdir gdrive_terminal:"TRASH_RESTORED_20260109"

# Download specific folder
rclone copy gdrive_terminal:"FolderName" ~/local/path/

# Get file count
rclone ls gdrive_terminal:"FolderName" | wc -l

# Check local space
df -h $HOME
```

---

## What Happens Next?

1. **You restore** from trash (web interface)
2. **You organize** restored files on Drive
3. **We download** if needed (or work on Drive directly)
4. **We deduplicate** using your proven methods
5. **We verify** everything is safe
6. **We cleanup** duplicates locally
7. **We celebrate** successful document rescue! 🎉

---

## Notes / Observations

Write here as you go:
- Time started restore:
- Number of items in trash:
- Any errors encountered:
- Interesting findings:
- Next steps decided:

---

Ready to start? Just open that trash view and hit restore! 🚀
