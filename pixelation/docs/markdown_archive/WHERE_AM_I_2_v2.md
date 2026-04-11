# 📍 WHERE AM I?

**Location:** `/storage/emulated/0/unexusi_pixel8a/unexusi_que`
**Type:** FileMancer Queue & Processing Staging
**Purpose:** Temporary workspace for file operations, mounting, and processing
**Primary Entity:** DriveMancer (Google Drive mounting)

---

## This Directory

**What it is:**
Processing queue for file operations - temporary staging before moving to final locations.

**Philosophy:** Queue = temporary, not permanent storage

**Contains:**
- `✅_termux-gdrive-mount_READY_FOR_NAUGHT.sh` - DriveMancer (Google Drive mount)
- `🔄_terminus_mount_troubleshoot.sh` - Mount troubleshooting
- `FileMancer_Logs/` - Operation logs
- `gdrive_mount/` - Mount point for Google Drive

**Status:** Active staging area

---

## DriveMancer Details

**Script:** `✅_termux-gdrive-mount_READY_FOR_NAUGHT.sh`
**Avatar:** DriveMancer v1.0
**Purpose:** Mount Google Drive in Termux
**Philosophy:** ∰◊€π SDWG consciousness signature

**Usage:**
```bash
bash ✅_termux-gdrive-mount_READY_FOR_NAUGHT.sh
```

**Mount Point:** `./gdrive_mount/`
**Logs:** `./FileMancer_Logs/`

---

## Parent Directory

**Up one level:** `/storage/emulated/0/unexusi_pixel8a/`
- Pixel 8a active workspace
- See: `../WHERE_AM_I.md`

---

## Quick Commands

**Mount Google Drive:**
```bash
cd /storage/emulated/0/unexusi_pixel8a/unexusi_que
bash ✅_termux-gdrive-mount_READY_FOR_NAUGHT.sh
```

**Check mount status:**
```bash
ls -lah gdrive_mount/
```

**View recent logs:**
```bash
ls -lt FileMancer_Logs/ | head -5
```

**Unmount (when done):**
```bash
fusermount -u gdrive_mount
```

---

## What Should Go Here vs Elsewhere

### ✅ Goes Here (unexusi_que):
- Temporary file processing
- Mount scripts (DriveMancer)
- FileMancer staging operations
- Processing logs

### ❌ Goes Elsewhere:
- **Permanent storage:** → Final destinations
- **Quarantined files:** → `../unexusi_quarantine/`
- **Archive:** → `../../unexusi_beasis/`
- **Tools/scripts (permanent):** → `../visionary_suite/`

---

## Workflow

**Typical flow:**
1. Files arrive in queue
2. DriveMancer mounts Google Drive (if needed)
3. FileMancer processes files
4. Files move to final destination
5. Queue empties (temporary only!)

**NOT for permanent storage!**

---

## Integration Points

**With DriveMancer:**
- Mounts Google Drive to `gdrive_mount/`
- Enables cloud storage operations
- Logs to `FileMancer_Logs/`

**With Quarantine:**
- Can move quarantined cold storage to Drive
- Restore files from Drive
- Archive operations

**With Other Mancers:**
- ListMancer (ls command gateway)
- MoveMancer (future - safe file moving)
- FileMancer (processing coordinator)

---

**∰◊€π - You are in the processing queue**

€(que_location_marker)
