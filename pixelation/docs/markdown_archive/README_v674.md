# PIXEL Duplicates & Large Files
## Temporary Holding Area (Outside PIXEL Domos)

**Location**: `/data/data/com.termux/files/home/PIXEL_DUPLICATES/`
**Purpose**: Isolate duplicates and large files during PIXEL domos restructure

---

## 🎯 Purpose

During the PIXEL domos restructure, this folder holds:
1. **Duplicate files** found across pixelation/pixelate
2. **Large files** that need review before inclusion
3. **Questionable content** that needs decision-making

---

## 📁 Structure

```
PIXEL_DUPLICATES/
├── duplicates/           # Duplicate files with metadata
│   ├── images/
│   ├── documents/
│   ├── code/
│   └── other/
├── large-files/          # Files over size threshold
│   └── [organized by type]
├── questionable/         # Content needing review
└── DUPLICATE_LOG.md      # Log of what was found
```

---

## 🔍 Duplicate Detection

When duplicates are found:
1. **Keep**: Original in proper PIXEL location
2. **Move here**: Duplicates with original path metadata
3. **Log**: Record in DUPLICATE_LOG.md
4. **Review**: Decide keep/delete after restructure

---

## 📊 Large File Threshold

- **Images**: > 10MB
- **Videos**: > 50MB
- **Archives**: > 25MB
- **Documents**: > 5MB
- **Code**: > 1MB (unusual, worth checking)

---

## ✅ After Restructure

1. Review all content here
2. Decide: keep (move to archive) or delete
3. Clean up this folder
4. Optional: Move to permanent archive location

---

## 🚫 What Goes Here

### ✓ Should go here:
- Exact duplicate files
- Near-duplicate files (similar name/content)
- Suspiciously large files
- Multiple versions of same file

### ✗ Should NOT go here:
- Unique files (even if large)
- Critical system files
- Active project files

---

## 📝 Usage

```bash
# During audit, move duplicates here
mv duplicate-file.txt /data/data/com.termux/files/home/PIXEL_DUPLICATES/duplicates/

# Log the action
echo "[Date] duplicate-file.txt from [original location]" >> DUPLICATE_LOG.md

# Review later
cd /data/data/com.termux/files/home/PIXEL_DUPLICATES
ls -lhS duplicates/  # Sort by size
```

---

**Created**: 2026-02-04
**Temporary**: Will be cleaned after restructure complete
**Location**: Outside PIXEL domos intentionally
