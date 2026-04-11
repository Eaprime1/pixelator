# Google Drive Trash Verification Guide
**Date:** 2026-01-09
**Goal:** Verify 40,000 files in Google Drive trash are duplicates before permanent deletion

## Current Status
- **Trash Size:** 1.191 GiB (per rclone)
- **Active Drive Used:** 9.264 GiB
- **Remote:** gdrive_terminal
- **Local Work:** Q_pixel8/gravity_well (contains deduplicated files)

---

## Step 1: Access Google Drive Trash (Web Interface)

### On Desktop Browser:
1. Open: https://drive.google.com/drive/trash
2. You'll see all trashed items with:
   - File names
   - Original location
   - Deletion date
   - File type

### On Mobile (Pixel 8):
1. Open Google Drive app
2. Tap ☰ menu (top left)
3. Tap "Trash"
4. View all trashed items

---

## Step 2: Document Trash Contents

### Option A: Quick Visual Check (Fast)
**Good for:** Confirming suspicions about duplicates

1. In trash, click sort by "Name"
2. Look for patterns:
   - Files with `_1`, `_2`, `_3` suffixes (duplicates)
   - Multiple copies of same filename
   - Files you recognize from local `gravity_well/`
3. Note approximate count and types

### Option B: Export Trash List (Thorough)
**Good for:** Detailed comparison with local files

#### Using Browser Console (Desktop):
```javascript
// In Chrome/Firefox, press F12, go to Console tab, paste this:
let files = [];
document.querySelectorAll('[data-id]').forEach(el => {
    let name = el.querySelector('[data-tooltip]');
    if (name) files.push(name.innerText);
});
console.log(files.join('\\n'));
// Copy the output
```

#### Manual Method:
1. Select all (Ctrl+A or Cmd+A)
2. Take screenshots
3. Or manually type/copy notable filenames into a text file

---

## Step 3: Save Trash Inventory

Create a file: `gdrive_trash_manual_inventory.txt`

**Include:**
- Total file count
- Sample filenames (at least 50-100)
- Date ranges
- File types observed
- Any folders in trash

**Template:**
```
Google Drive Trash Inventory (Manual)
Date: 2026-01-09
Method: Web Interface

Total Items: ~XXXXX files + XX folders
Trash Size: 1.191 GiB

Sample Files (sorted by name):
1. filename1.txt
2. filename2_1.md
3. filename2_2.md
...

Observations:
- [ ] Many duplicates with _1, _2 suffixes
- [ ] Matches files in local gravity_well/
- [ ] Recent deletion dates (Dec 2025)
- [ ] Mostly .md, .txt, .pdf, .docx types
```

---

## Step 4: Compare with Local Files

Once you have the trash list, we'll run a comparison script:

```bash
# We'll create this after you get the trash list
python3 compare_trash_to_local.py \\
    gdrive_trash_manual_inventory.txt \\
    Q_pixel8/inventory_gravity_well.md
```

This will show:
- ✅ Files in trash that ARE in local (safe to delete)
- ⚠️  Files in trash that are NOT in local (review carefully!)
- 📊 Statistics and duplicate analysis

---

## Safety Checklist

Before emptying trash:
- [ ] Confirmed most files have local copies
- [ ] Checked a few random files for matches
- [ ] Reviewed any unique files not found locally
- [ ] Made backup of critical local files
- [ ] Comfortable with "one hertz" verification approach

---

## Next Steps After This Guide

1. **You**: Access web trash and create inventory
2. **Claude**: Create comparison script
3. **Together**: Review results and decide on safe deletions
4. **You**: Empty trash (or restore unique files first)

---

## Notes
- Google Drive trash auto-deletes after 30 days
- You can select "Delete forever" for confirmed duplicates
- Or "Restore" for any files you want to keep
- The 1.191 GiB suggests thousands of files, not quite 40k unless they're very small

---

## Questions to Answer While Reviewing Trash

1. Are most files from a specific date range?
2. Do you see entire folder structures or just files?
3. Are there any project-critical files you recognize?
4. What's the mix of file types (.txt vs .md vs .pdf etc)?

Write your observations here as you go!
