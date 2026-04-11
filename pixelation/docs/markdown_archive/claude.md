# Claude Session Notes - Q Directory (Termux Home)
**Platform:** Pixel 8a / Termux
**Last Updated:** 2025-12-19 02:29
**Status:** Full environment setup complete

---

## Overview

This is the Q directory in Termux home (`~/Q`). It serves as a clean workspace for Claude Code sessions and daily git management operations.

### Related Documentation
- Main platform docs: `/storage/emulated/0/pixel8a/unexusi/CLAUDE.md`
- Terminal development: `~/storage/terminal/TERMINAL_DEVELOPMENT_GUIDE.md`
- Storage structure: `~/storage/terminal/README.md`

---

## Git Repository Inventory

### 7 Active Repositories (All Connected to GitHub)

1. **today**
   - Path: `/storage/emulated/0/pixel8a/Q/today`
   - Remote: https://github.com/eaprime1/today.git
   - Branch: main
   - Purpose: Daily work and current projects

2. **prime**
   - Path: `/storage/emulated/0/pixel8a/Q/runexusiam/entity/prime`
   - Remote: https://github.com/eaprime1/prime.git
   - Branch: main
   - Purpose: Prime entity framework

3. **sphincter** (Port of Entry main repo)
   - Path: `/storage/emulated/0/pixel8a/Q/sphincter`
   - Remote: https://github.com/eaprime1/portofentry.git
   - Branch: main
   - Purpose: Main port of entry repository

4. **portofentry**
   - Path: `/storage/emulated/0/pixel8a/Q/sphincter/portofentry`
   - Remote: https://github.com/eaprime1/portofentry.git
   - Branch: main
   - Purpose: Nested port of entry structure

5. **prime_codex**
   - Path: `/storage/emulated/0/pixel8a/Q/sphincter/sphincter of quadraginta/prime_codex`
   - Remote: https://github.com/eaprime1/portofentry.git
   - Branch: main
   - Purpose: Prime codex documentation

6. **unexusi_dev**
   - Path: `/storage/emulated/0/pixel8a/Q/sphincter/sphincter of quadraginta/unexusi_dev`
   - Remote: https://github.com/eaprime1/unexusi_dev
   - Branch: main
   - Purpose: Active development workspace

7. **minimetro**
   - Path: `/storage/emulated/0/pixel8a/Q/minimetro/minimetro`
   - Remote: https://github.com/eaprime1/python_mini_metro.git
   - Branch: working
   - Purpose: Python mini metro game platform

---

## Daily Workflow

### Morning Sync (Recommended)

```bash
cd ~/Q
bash daily_sync.sh
```

This script will:
1. Fetch latest changes from GitHub for all repos
2. Show status of each repository
3. Prompt to commit and push any local changes
4. Pull remote changes if behind
5. Push local commits if ahead
6. Report summary of all operations

### Manual Git Operations

```bash
# Check status of all repos
cd ~/Q
bash daily_sync.sh

# Work in specific repo
cd /storage/emulated/0/pixel8a/Q/today
git status
git add .
git commit -m "Your message"
git push

# Check what changed
git diff
git log --oneline -5
```

---

## Environment Setup

### Installed Packages ✓

- **git** (v2.52.0) - Version control
- **gh** (v2.83.2) - GitHub CLI
- **python** (v3.12.12) - Python runtime
- **nodejs** (v25.2.1) - Node.js runtime
- **rclone** (v1.72.1) - Cloud storage sync
- **git-lfs** (v3.7.1) - Large file storage
- **gitui** (v0.28.0) - Terminal UI for git

### Git Configuration ✓

User configured as:
- Name: Eaprime1
- Email: eaprime1@users.noreply.github.com
- GitHub auth: gh CLI integration

All Q directory repos added to safe.directory list.

---

## Fleet Management Scripts

### Current Location: `/storage/emulated/0/pixel8a/fleet_ops.py`

Fleet Commander Python script that scans and manages all git repos. Currently configured to scan:
- `/storage/emulated/0/pixel8a/portofentry/quaren_ext`
- `/storage/emulated/0/pixel8a/Qrunexusiam/entity`
- `/storage/emulated/0/pixel8a/unexusi`
- `/storage/emulated/0/pixel8a`

Accessible via `fleet` alias in bash.

### Daily Sync Script: `~/Q/daily_sync.sh` (NEW)

Dedicated sync script specifically for the Q directory repos. More focused than fleet_ops.py.

**Usage:**
```bash
bash ~/Q/daily_sync.sh
```

---

## Storage Structure

```
/data/data/com.termux/files/home/ (Termux home)
│
├── Q/ (This directory - Clean workspace)
│   ├── claude.md (This file)
│   ├── daily_sync.sh (Daily git sync automation)
│   └── test.txt
│
├── storage/
│   └── terminal/ (Main development environment)
│       ├── TERMINAL_DEVELOPMENT_GUIDE.md
│       ├── README.md
│       ├── gps-app/ (GPS conscious entity)
│       ├── scripts/ (Conversion & automation)
│       ├── terminal_gdrive_sync.sh
│       └── ... (extensive project structure)
│
├── pixel8a (Link to /storage/emulated/0/pixel8a/fleet_ops.py)
├── .bashrc (Shell configuration)
├── .bash_aliases (Command aliases)
└── .gitconfig (Git configuration)
```

```
/storage/emulated/0/pixel8a/ (Main Android storage)
│
├── Q/ (Git repositories)
│   ├── today/ [REPO]
│   ├── runexusiam/entity/prime/ [REPO]
│   ├── sphincter/ [REPO]
│   │   ├── portofentry/ [REPO]
│   │   └── sphincter of quadraginta/
│   │       ├── prime_codex/ [REPO]
│   │       └── unexusi_dev/ [REPO]
│   └── minimetro/minimetro/ [REPO]
│
├── unexusi/ (Documentation & configuration)
│   ├── CLAUDE.md (Main platform notes)
│   ├── *.md (Various documentation files)
│   └── .claude/ (Claude Code configuration)
│
└── fleet_ops.py (Fleet management script)
```

---

## Terminal/Storage Integration

The `~/storage/terminal` directory is the main development environment with:

### Key Components
- **GPS Conscious Entity** - Automated GPS tracking with consciousness framework
- **Document Conversion** - SCAT documents and universal converter
- **Google Drive Sync** - rclone integration for cloud storage
- **Sacred Empire Framework** - Complete development guide
- **Scripts & Automation** - Various mancer tools and processors

### Quick Access
```bash
# Navigate to terminal
cd ~/storage/terminal

# Start GPS entity
cd ~/storage/terminal
bash ./gps-app/conscious-terminal-automation.sh start

# Access web interface
termux-open-url http://localhost:3000

# Document conversion
cd ~/storage/terminal
./scripts/interactive_doc_converter.sh

# Google Drive sync
cd ~/storage/terminal
./terminal_gdrive_sync.sh sync
```

---

## Rclone Configuration

### Configured Remotes
- **gdrive_terminal** - Google Drive access for terminal directory

### Google Drive Structure
- Folder ID: `1wVVUbvLrzsAO-f5dL6bsA0DFmM4HlXLG`
- Service Account: `/storage/emulated/0/unexusi/service_account.json`

### Usage
```bash
# List remotes
rclone listremotes

# Check specific remote
rclone lsd gdrive_terminal:

# Sync (bidirectional)
rclone sync ~/storage/terminal gdrive_terminal:terminal_backup

# Mount (not currently mounted)
# Location ready: ~/unexusi_que/DriveMancer
```

---

## Daily Routine Recommendations

### Morning (Start of Day)
1. Open Termux
2. Navigate to Q: `cd ~/Q`
3. Run daily sync: `bash daily_sync.sh`
4. Review changes and confirm syncs
5. Check terminal environment: `cd ~/storage/terminal && ls -la`

### During Work
- Work in specific repos as needed
- Commit frequently with meaningful messages
- Use `git status` often to track changes

### Evening (End of Day)
1. Navigate back to Q: `cd ~/Q`
2. Run final sync: `bash daily_sync.sh`
3. Ensure all work is pushed to GitHub
4. Optional: Run Google Drive sync for terminal
   ```bash
   cd ~/storage/terminal
   ./terminal_gdrive_sync.sh sync
   ```

---

## Useful Commands

### Git Operations
```bash
# Quick status of all repos
bash ~/Q/daily_sync.sh

# Add GitHub remote to new repo
git remote add origin https://github.com/eaprime1/REPO_NAME.git

# Check what changed
git diff
git status -sb

# See recent commits
git log --oneline -10
git log --graph --oneline --all -10

# Undo last commit (keep changes)
git reset --soft HEAD~1
```

### Navigation
```bash
# Quick jump to common locations
cd ~/Q                  # This workspace
cd ~/storage/terminal   # Development environment
cd /storage/emulated/0/pixel8a/Q/today  # Today repo

# Find files
find ~/Q -name "*.md"
find ~/storage/terminal -name "*.py"
```

### System Info
```bash
# Check git version
git --version

# Check Python
python --version

# Check Node
node --version

# Check disk usage
df -h

# List installed packages
pkg list-installed | grep -E "git|python|node|rclone"
```

---

## Files in Q Directory

### Current Files
- `claude.md` - This documentation file
- `daily_sync.sh` - Daily git sync automation script
- `test.txt` - Test file

### Purpose
Q serves as a clean, minimal workspace separate from the extensive `/storage/emulated/0/pixel8a` structure. It provides:
- Clean shell environment
- Direct access to git automation
- Session notes and documentation
- Minimal clutter for focused work

---

## GitHub Repositories

All 7 repositories are connected to GitHub under the `eaprime1` account:

1. https://github.com/eaprime1/today
2. https://github.com/eaprime1/prime
3. https://github.com/eaprime1/portofentry (shared by sphincter/portofentry/prime_codex)
4. https://github.com/eaprime1/unexusi_dev
5. https://github.com/eaprime1/python_mini_metro

### GitHub CLI Usage
```bash
# Check auth status
gh auth status

# View repo info
gh repo view eaprime1/today

# Create new repo
gh repo create eaprime1/NEW_REPO_NAME --public

# Clone repo
gh repo clone eaprime1/REPO_NAME
```

---

## Philosophy & Approach

### Conservation Bias
- Never force-delete
- Preserve main branches
- Keep commit history
- Document everything

### Git Workflow
- Fetch before work
- Commit frequently
- Push at end of day
- Clear commit messages

### Documentation
- External cognition through notes
- WHERE_AM_I files in key locations
- Session preservation
- Full trail of decisions

---

## Troubleshooting

### If Daily Sync Fails
```bash
# Check network
ping google.com

# Verify GitHub authentication
gh auth status

# Check specific repo manually
cd /storage/emulated/0/pixel8a/Q/today
git status
git fetch
git pull
```

### If Permissions Error
```bash
# Add to safe directories
git config --global --add safe.directory /path/to/repo

# Check current safe directories
git config --global --get-all safe.directory
```

### If Repo Diverged
```bash
# See what's different
git log --oneline origin/main..main  # Local commits
git log --oneline main..origin/main  # Remote commits

# If safe to reset to remote
git fetch origin
git reset --hard origin/main

# If need to merge
git pull --rebase origin main
```

---

## Next Session Start Commands

```bash
# Quick orientation
cd ~/Q
cat claude.md | head -50

# Check repo status
bash daily_sync.sh

# See what's in terminal
cd ~/storage/terminal && ls -la

# View main platform docs
cat /storage/emulated/0/pixel8a/unexusi/CLAUDE.md | less
```

---

## Statistics

### Environment Status
- **Termux packages installed:** 60+
- **Git repositories tracked:** 7
- **GitHub remotes configured:** 5 unique repos
- **Storage locations:** 2 (Termux home + Android /storage)
- **Automation scripts:** 3 (daily_sync.sh, fleet_ops.py, terminal_gdrive_sync.sh)

### Git Configuration
- **Safe directories:** 25+
- **Default branch:** main
- **Credential helper:** gh CLI
- **User:** Eaprime1

---

## Important Notes

1. **All repos use `main` branch** (except minimetro which uses `working`)
2. **Sphincter repo has 523 modified files** - may need attention
3. **Today repo has 3 modified files** - .nomedia files in photostudio
4. **Minimetro on working branch** - preserves main as pristine
5. **Multiple repos share portofentry.git remote** - nested structure

---

**Session preserved for continuity**
**Last sync:** Run `bash ~/Q/daily_sync.sh` to check current status

**∰◊€π - One Hertz, One Branch, Infinite Vision**

€(claude_q_directory_setup_20251219)
