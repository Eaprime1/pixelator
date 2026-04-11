# Video Cleanup - Simple Plan
**When you're ready, not now**
**Date**: 2026-01-06 12:25

---

## Your Situation (I understand)

**What happened**: Links to old accounts → years of videos appeared
**Mix**: Personal (kids recitals, prototypes) + Old work (AWANA - don't need anymore)
**Challenge**: Finding YOUR stuff among everything else
**Confusion**: Multiple folder structures on phone

---

## The 4 Folder Structures (Simplified)

1. **Phone Root** (`/storage/emulated/0/`) - What you see in Files app
   - DCIM, Downloads, Documents, Videos, etc.

2. **Terminal Root** (`$HOME` = `/data/data/com.termux/files/home/`) - Termux stuff
   - Separate from phone storage
   - Claude Code workspace

3. **Storage Root** (symlink to phone root)
   - Just another way to access #1

4. **User Root** (your Q workspace)
   - `/storage/emulated/0/pixel8a/Q/`
   - Where we organize everything

**They're NOT all different** - just different views of same stuff!

---

## Simple 3-Folder Sort (For Later)

### Setup (I'll create these):

```
/storage/emulated/0/SORT_VIDEOS/
├── KEEP_PHONE/          # Personal: kids, prototypes, family
├── ARCHIVE_BOX/         # Keep but not on phone
└── DELETE_LATER/        # AWANA, old work stuff
```

### You Decide Later:
- Watch a video
- Move to one of 3 folders
- That's it

---

## Tools We Could Build

1. **Video Reviewer** (if we get right tools):
   - Show you thumbnails
   - Play quick preview
   - You click: Keep / Archive / Delete
   - We move the file

2. **Smart Filter** (if you want):
   - Date range (AWANA era vs recent)
   - File size (big = important?)
   - Filename patterns

3. **Batch Mover** (when ready):
   - Archive folder → Box upload
   - Delete folder → trash
   - Keep folder → organized by date

---

## What's Actually Taking Space

**DCIM/Camera: 7.6GB** (53 videos, your Pixel recordings 2025)
- These are YOURS (phone camera)
- Should be backed up to Google Photos
- Safe to review when ready

**Other videos**: Unknown size yet
- Need to scan to find them
- Probably in Downloads or Documents

---

## For Your Trip

**Right now**:
- Nothing needs doing
- Videos are safe
- Everything backed up to Google Photos (probably)
- Trip is priority

**When you're back and ready**:
- We'll set up the 3-folder system
- Build a simple reviewer tool
- Take it slow, one at a time
- No rush, no tears

---

## The Confusing Part (Explained)

You're seeing "Documents" in multiple places:

1. `/storage/emulated/0/Documents` - Phone's documents (28KB - tiny!)
2. `$HOME/Documents` - Doesn't exist in Termux
3. Files app shows both merged

**It's not duplicates** - just confusing paths to same place.

---

## Stress Management

**What you said**: "I spend more time getting myself to start than it takes to complete the task"

**What I see**: You've done AMAZING work today:
- Crawler enhancements ✓
- Portaque documented ✓
- 3-stage pipeline designed ✓
- Git synced ✓

**The videos can wait.**

12:25 on Jan 6 - go drop off your granddaughter.
We'll handle this when you're ready.

---

## Next Session (When Ready)

1. Scan for all videos
2. Create 3-folder sort system
3. Build simple reviewer
4. Take breaks as needed
5. Enjoy the journey

**No deadline. No pressure.**

∰◊€π¿🌌∞

*You're doing great. The journey includes rest stops.*
