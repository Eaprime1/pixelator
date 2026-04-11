# Visionary Duplicate Mancer - Quick Reference
**∰◊€π - Rapid Github Preparation Tool**

## **One-Line Mission**
Rapid-but-careful duplicate quarantine with full chain of custody and conservation bias.

---

## **Usage**

### **Scan Entire UNEXUSI**
```bash
bash visionary_dup_mancer.sh
```

### **Scan Specific Directory**
```bash
bash visionary_dup_mancer.sh /storage/emulated/0/unexusi/target_folder
```

---

## **What It Does**

1. **Detects** duplicates via SHA-256 hash (content-based)
2. **Preserves** first occurrence in original location
3. **Quarantines** subsequent matches to `/unexusi_quarantine/`
4. **Marks** quarantined files with 🔂 prefix
5. **Documents** everything in consciousness logs

---

## **Key Symbols**

| Symbol | Meaning |
|--------|---------|
| 🔂 | Quarantined duplicate (consciousness marker) |
| ✓ | Successfully quarantined |
| ⚠ | Warning/skip |
| ∰◊€π | SDWG Archival consciousness signature |

---

## **Output Locations**

```
/storage/emulated/0/unexusi_quarantine/
├── consciousness_logs/
│   ├── scan_manifest_TIMESTAMP.md       (operation summary)
│   ├── chain_of_custody_TIMESTAMP.md    (every file tracked)
│   └── quarantine_registry.md           (historical log)
└── duplicates_TIMESTAMP/
    └── [original_structure]/
        └── 🔂[filename]
```

---

## **Conservation Bias**

✓ **Preserves** first occurrence  
✓ **Quarantines** (never deletes) duplicates  
✓ **Skips** inaccessible files  
✓ **Documents** everything  

**Philosophy**: Duplicates tell developmental story.

---

## **Quick Checks**

### **How Many Quarantined?**
```bash
cat /storage/emulated/0/unexusi_quarantine/consciousness_logs/scan_manifest_*.md | grep "Files for Quarantine"
```

### **Last Operation**
```bash
tail -20 /storage/emulated/0/unexusi_quarantine/consciousness_logs/quarantine_registry.md
```

### **Specific File Location**
```bash
grep "filename" /storage/emulated/0/unexusi_quarantine/consciousness_logs/chain_of_custody_*.md
```

---

## **Restoration (If Needed)**

```bash
# Find file in chain of custody
cat chain_of_custody_TIMESTAMP.md | grep "filename"

# Move back (remove 🔂 prefix)
mv quarantine_location/🔂filename original_location/filename
```

**Note**: Manual restoration prevents accidental re-introduction of duplicates.

---

## **Henry vs. Visionary**

| Aspect | Henry (Standard) | Visionary (This) |
|--------|------------------|------------------|
| Purpose | Daily collaboration | Github prep |
| Mode | Verbose/exploratory | Rapid/succinct |
| Focus | Internal development | External manifestation |
| Output | Interactive dialogue | Brief confirmation + logs |

---

## **Mancer Architecture**

```
MANCER (Orchestrator)
├── hash_henry      → Duplicate detection
├── quarantine_henry → File movement
├── logger_henry    → Documentation
└── report_henry    → Summary generation
```

**ONE HERTZ Principle**: One Script, One Mission, Infinite Vision

---

## **Status Indicators**

During execution, you'll see:
- `⚡ entity awakening...` - Henry starting work
- `🔍 Analyzing...` - Detection phase
- `✓ 🔂 filename` - File quarantined
- `✨ No duplicates detected` - Clean scan
- `€(one_hertz_mission_complete)` - Operation finished

---

## **Emergency**

**Files Missing?**  
→ Check quarantine directory first (likely moved, not deleted)

**Unexpected Results?**  
→ Review chain_of_custody before running again

**Need to Undo?**  
→ Use restoration protocol (see full guide)

---

**∰◊€π** - Consciousness Archaeology Active  
*Conservation Bias: MAINTAINED*

€(quick_reference_complete)
