# Restored Files → Clean Files Workflow

**Date:** 2026-01-09
**Goal:** Process laptop trash restore → organized, deduplicated files

## The Pipeline

```
Laptop Trash
    ↓
[RESTORE] ← You're doing this now!
    ↓
Restored Files (unsorted)
    ↓
[FILE_SORTER] ← Step 1: Categorize
    ↓
├─ metadata/
├─ entangled/
├─ duplicates/
└─ review/
    ↓
[REDUNDANCY_RANGER] ← Step 2: Deduplicate each
    ↓
├─ gravity_well_queue/  (primes with counts)
└─ shadow_realm/        (duplicates to review)
    ↓
[YOU VERIFY] ← Step 3: Check results
    ↓
Delete shadows → Keep primes → Organize to projects
```

## Step-by-Step Guide

### Phase 1: Restore (NOW - In Progress)
**You're doing:** Restoring from laptop trash
**Wait for:** Restore to complete
**Creates:** Pile of unsorted files

### Phase 2: Sort by Type
**Tool:** `FILE_SORTER.py`
**Where:** `Q_pixel8/restored_sorted/`

```bash
# When restore is done
cd ~/pixel8/Q/Q_pixel8/restored_sorted
python3 FILE_SORTER.py /path/to/restored/files

# Result: Files sorted into categories
```

**Output folders:**
- `metadata/` - JSON, config, map files
- `entangled/` - Quantum-named files, consciousness patterns
- `duplicates/` - Files with dup_, _1, _2 patterns
- `review/` - Everything else (check manually)

### Phase 3: Deduplicate Each Category
**Tool:** `REDUNDANCY_RANGER.py`
**Where:** `Q_pixel8/hodie/redundancy_ranger/`

```bash
cd ~/pixel8/Q/Q_pixel8/hodie/redundancy_ranger

# Test on duplicates folder first (dry run)
python3 REDUNDANCY_RANGER.py ../../restored_sorted/duplicates/

# Review results, then run for real
# (set dry_run=False in script)

# Then process other categories
python3 REDUNDANCY_RANGER.py ../../restored_sorted/review/
python3 REDUNDANCY_RANGER.py ../../restored_sorted/metadata/
# (entangled might need manual review - skip ranger for now)
```

**Creates:**
- `gravity_well_queue/` - Primes (one per group, with count)
- `shadow_realm/` - Duplicates (review before delete)
- `redundancy_report.json` - Full audit trail

### Phase 4: Verify & Clean
**You do:**

1. **Check primes** in `gravity_well_queue/`
   - Random spot checks
   - Verify counts make sense
   - Open a few to confirm content

2. **Review shadows** in `shadow_realm/`
   - Quick browse
   - Any files you recognize as unique?
   - If all look like true duplicates → delete

3. **Handle special cases**
   - `metadata/` - Might need version comparison
   - `entangled/` - Probably need manual review
   - `review/` - Check for treasures

### Phase 5: Organize Primes
**Final step:** Move from gravity_well_queue to projects

```bash
# Organize by project/topic
mv gravity_well_queue/PRIME_*.md ~/projects/prime_docs/
mv gravity_well_queue/*quantum* ~/projects/quantum_work/
# etc.
```

## One Hertz Checkpoints

✅ **After Restore:** Count files, note total size
✅ **After Sort:** Check each category makes sense
✅ **After Dedup:** Review stats, spot-check primes
✅ **Before Delete:** Final review of shadow realm
✅ **After Organize:** Verify projects have what they need

## If Something Goes Wrong

- **Wrong prime selected?** → Restore from shadow_realm
- **Lost a file?** → Check `redundancy_report.json`
- **Need to undo?** → Shadow realm has everything
- **Sorted wrong?** → Move between category folders

## Testing Strategy

1. **Test FILE_SORTER** on 20 files (built-in limit)
2. **Test RANGER** on 5 groups (built-in limit)
3. **Review** results carefully
4. **Adjust** patterns if needed
5. **Process** larger batches
6. **Verify** each batch before next

## While Waiting for Restore

✅ Setup complete!
✅ Tools ready:
   - FILE_SORTER.py
   - REDUNDANCY_RANGER.py
   - Documentation

⏳ Waiting for: Laptop trash restore to complete

## Next Action

When restore finishes, tell me:
- How many files restored
- Where they are
- Any immediate patterns you notice

Then we'll start Phase 2 (sorting)!

---

**Current Status:**
- ✅ Folders created
- ✅ Ranger built
- ✅ Documentation ready
- ⏳ Waiting for restore
- ⏸️  Ready to test when you are

Enjoy the journey! 🚀
