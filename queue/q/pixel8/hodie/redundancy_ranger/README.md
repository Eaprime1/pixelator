# Redundancy Ranger 🤠

**Gravity Well Training Edition**

Hunt duplicates. Designate prime. Shadow the rest.

## What It Does

When Redundancy Ranger finds 6 duplicates of the same file:
1. **Prime** - One file stays (renamed to `filename_6.ext`)
2. **Shadows** - The other 5 go to shadow realm
3. **Queue** - Prime goes to gravity well queue for processing

## Quick Start

```bash
# Test mode (dry run) - first 5 duplicate groups
python3 REDUNDANCY_RANGER.py /path/to/source/directory

# Process for real
# (edit the script and set dry_run=False)
```

## Directory Structure

```
source_directory/          # Files to scan
gravity_well_queue/        # Primes go here (with count)
shadow_realm/              # Shadows banished here
redundancy_report.json     # Detailed report
```

## The Process

### 1. Scan
Ranger scans all files, calculates hashes, groups duplicates

### 2. Designate Prime
From each duplicate group, selects prime by:
- Shortest filename (likely original)
- No numeric suffixes
- Oldest modification time

### 3. Add Count
Prime gets count added: `document.txt` → `document_6.txt`
(The number tells you how many were consolidated)

### 4. Queue & Shadow
- Prime → `gravity_well_queue/` (for further processing)
- Shadows → `shadow_realm/` (review before deleting)

## One Hertz Philosophy

Default: Process 5 groups at a time
- Review results
- Verify logic
- Adjust if needed
- Then process more

## Example Output

```
Group 1: 6 duplicates
  ✓ Prime: important_doc_6.txt
  ○ Shadow: important_doc_1.txt
  ○ Shadow: important_doc_2.txt
  ○ Shadow: important_doc (1).txt
  ... and 2 more shadows

Files scanned:      847
Duplicate groups:   23
Primes designated:  23
Shadows marked:     89
Space saved:        143.2 MB
```

## Safety Features

- **Dry run by default** - No moves until you approve
- **Shadow realm** - Shadows aren't deleted, just moved
- **Detailed report** - JSON log of every decision
- **Name conflict handling** - Never overwrites
- **One hertz batches** - Small, verifiable groups

## Integration with Restored Files

After restoring from trash:

```bash
# Sort by type first
python3 ../restored_sorted/FILE_SORTER.py restored_files/

# Then deduplicate each category
python3 REDUNDANCY_RANGER.py ../restored_sorted/duplicates/
python3 REDUNDANCY_RANGER.py ../restored_sorted/review/
```

## Advanced Usage

```python
from REDUNDANCY_RANGER import RedundancyRanger

# Create ranger
ranger = RedundancyRanger(source_dir="./my_files")

# Scan
ranger.scan_for_duplicates()

# Process (dry run)
results = ranger.process_all_duplicates(dry_run=True, limit=10)

# Review results
ranger.print_stats()

# Process for real (no limit)
results = ranger.process_all_duplicates(dry_run=False, limit=None)

# Save report
ranger.save_report(results)
```

## What Goes Where

### Gravity Well Queue
Files ready for final organization:
- Have count in name (`file_6.txt`)
- Verified as prime
- Deduplicated
- Ready for project folders

### Shadow Realm
Duplicate files marked for deletion:
- Review before permanent delete
- Can restore if prime was wrong
- Can delete all once verified

## Recovery

If you need to undo:
1. Shadow realm has all "deleted" duplicates
2. Report JSON has full mapping
3. Can manually restore any shadow
4. Prime selection logged for review

## Tips

- Run on small batches first
- Review shadow realm before deleting
- Check a few primes manually
- Use dry_run until confident
- Save reports for audit trail

---

**Remember:** Ranger finds, prime stays, shadows marked. You decide when to delete shadows.

Enjoy the journey! 🚀
