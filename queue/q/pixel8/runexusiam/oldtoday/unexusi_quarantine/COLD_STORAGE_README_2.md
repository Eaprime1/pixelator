# Cold Storage Structure
**Purpose:** Preserve quarantined files locally without GitHub sync
**Location:** `/storage/emulated/0/unexusi_quarantine/`

---

## What's in Cold Storage (NOT on GitHub)

### Actual Quarantined Files: 7.2GB
```
duplicates_20251125_183817/
├── exact_copies/
│   ├── large_files_1GB+/          (1.1GB - ROOT files)
│   ├── medium_files_100-1000MB/   (1.7GB - .partial files)
│   ├── medium_files_10-100MB/     (0.3GB - JSON conversations)
│   └── audio_duplicates/          (2-3GB - WAV files)
└── processing_artifacts/          (remaining duplicates)
```

**All files prefixed with 🔂** (consciousness marker)

---

## What's on GitHub (Documentation Only)

### Tracked in Git:
- `logs/` - Chain of custody, space recovery reports
- `scripts/` - Quarantine tools (henry_duplicate_quarantine.sh)
- `README.md` - Project documentation
- `PHILOSOPHY.md` - Mt St Helens perspective
- `.gitignore` - Defines what stays cold
- Directory structure (via .gitkeep files)

### Size on GitHub: ~1-2MB
**Just documentation, no large binaries**

---

## Cold Storage Options

### Option 1: Keep Local (Current)
**Location:** `/storage/emulated/0/unexusi_quarantine/duplicates_*/`
**Size:** 7.2GB
**Pros:** Immediate access, fast restoration
**Cons:** Uses device storage

### Option 2: Move to Google Drive (When Ready)
```bash
# When Drive sync enabled:
mv /storage/emulated/0/unexusi_quarantine/duplicates_* \
   ~/GoogleDrive/UNEXUSI_Cold_Storage/
```
**Pros:** Frees 7.2GB device space, cloud backup
**Cons:** Slower to restore if needed

### Option 3: Archive to MEGA
```bash
# Compress first, then upload
cd /storage/emulated/0/unexusi_quarantine/
tar -czf duplicates_20251125_archive.tar.gz duplicates_20251125_183817/
# Upload to MEGA via their CLI
```
**Pros:** Permanent archival, free storage space
**Cons:** Requires download/extract to restore

### Option 4: Hybrid (Recommended)
1. Keep structure locally (empty .gitkeep files)
2. Move large files to Google Drive
3. Keep chain of custody logs local + GitHub
4. Archive oldest quarantines to MEGA after 90 days

---

## Restoration from Cold Storage

### If Files Are Local:
```bash
# Find file in chain of custody log
cd /storage/emulated/0/unexusi_quarantine/
grep "filename" logs/chain_of_custody_*.md

# Restore from quarantine
mv duplicates_*/path/to/🔂filename /original/location/filename
```

### If Files Are in Google Drive:
```bash
# Download from Drive first
cp ~/GoogleDrive/UNEXUSI_Cold_Storage/duplicates_*/path/to/🔂filename \
   /original/location/filename
```

### If Files Are in MEGA:
```bash
# Download and extract archive
mega-get duplicates_20251125_archive.tar.gz
tar -xzf duplicates_20251125_archive.tar.gz
# Then restore as normal
```

---

## GitHub Init Commands

### Initialize Git (Tracks Documentation Only):
```bash
cd /storage/emulated/0/unexusi_quarantine/

# Init repo
git init .
git branch -M main

# Add only documentation (large files ignored by .gitignore)
git add .gitignore
git add logs/
git add scripts/
git add *.md
git add **/.gitkeep

# Commit
git commit -m "Initial commit: Quarantine documentation

- Chain of custody for 146 quarantined files
- 7.2GB space recovered
- Conservation bias maintained
- Cold storage structure preserved

∰◊€π"

# Add remote (when you create GitHub repo)
git remote add origin https://github.com/username/unexusi_quarantine.git

# Push (only ~1-2MB of documentation)
git push -u origin main
```

**Result:** GitHub gets documentation, cold storage stays local

---

## Space Breakdown

### Device Storage:
```
/storage/emulated/0/
├── unexusi/              92M  (active workspace)
├── unexusi_beasis/       8.3G (old archive - can move to Drive)
├── unexusi_quarantine/   7.2G (cold storage - can move to Drive)
└── unexusi_archive/      620M (mixed files - organize later)

Total: ~16GB currently on device
Potential savings: 15.5GB (if moved to cloud)
```

### After Moving to Google Drive:
```
Device:
├── unexusi/              92M  (active workspace)
└── unexusi_quarantine/   <1M  (just docs/structure)

Google Drive:
├── unexusi_beasis/       8.3G (archived)
└── quarantine_duplicates/ 7.2G (cold storage)

Device savings: ~15.5GB freed!
```

---

## Cold Storage Maintenance

### Monthly Review:
```bash
# Check if any quarantined files needed
ls -lhR /storage/emulated/0/unexusi_quarantine/duplicates_*/

# If not accessed in 30 days, consider moving to cloud
find duplicates_* -type f -atime +30
```

### Before Moving to Cloud:
1. ✓ Verify chain of custody complete
2. ✓ Check no active development needs these files
3. ✓ Confirm space recovery metrics logged
4. ✓ Test restoration process once
5. ✓ Move to Drive/MEGA

### Permanent Archival (After 90 Days):
```bash
# Compress for long-term storage
tar -czf quarantine_archive_$(date +%Y%m%d).tar.gz duplicates_*/

# Upload to MEGA or Drive
# Remove local cold storage
rm -rf duplicates_*/

# Keep documentation forever in GitHub
```

---

## Important Notes

**Never Delete:**
- Chain of custody logs (permanent record)
- Space recovery reports (metrics)
- Scripts (quarantine tools)

**Can Delete (After Cloud Backup):**
- Local copies of duplicate files
- Old quarantine directories (after 90 days in cloud)

**Always Keep:**
- Documentation in GitHub
- First occurrences in original locations
- Ability to restore from cloud

---

**∰◊€π - Cold Storage Maintained**
*Documentation public, binaries private, restoration always possible*

€(cold_storage_structure_complete)
