# WHERE AM I?

## Location
`/storage/emulated/0/unexusi_pixel8a/unexusi_minimetro/`

## Purpose
**Python Mini Metro** - Game test platform and development workspace

## What This Is

A pygame-based implementation of Mini Metro:
- Strategic metro system optimization game
- Connect stations, manage passengers, optimize routes
- Supports both human and AI players
- Purpose: Game platform + reinforcement learning training environment

## Project Status

**Git Status:**
- Connected to: `https://github.com/eaprime1/python_mini_metro.git`
- Current branch: `working` (your modifications)
- Preserved branch: `main` (original, never touched)

**Philosophy:** Conservation bias - keep main pristine, experiment on working

## Quick Start

### Launch the Game
```bash
bash launcher.sh
```

The launcher will:
- Check if requirements installed
- Offer to install if needed
- Launch game with simple UI menu
- Show project status (git)

### Manual Commands
```bash
# Install requirements
pip install -r requirements.txt

# Run game directly
python src/main.py

# Run tests
python -m unittest -v

# Interactive git setup
bash setup_working_branch.sh
```

## Git Workflow

### Current Setup
```
* working  ← You are here (make changes)
  main     ← Original code (preserved)
```

### Branch Strategy
- **main**: Original code from GitHub, never modified (conservation)
- **working**: Your creative workspace, modify freely

### Common Commands
```bash
git status              # What changed?
git branch              # Where am I?
git checkout main       # See original
git checkout working    # Back to workspace
```

See `GIT_WORKFLOW_GUIDE.md` for detailed interactive explanations.

## File Structure

```
unexusi_minimetro/
├── launcher.sh                  [NEW] Simple UI launcher
├── setup_working_branch.sh      [NEW] Interactive git setup
├── GIT_WORKFLOW_GUIDE.md        [NEW] Git learning guide
├── WHERE_AM_I.md                [NEW] This file
│
├── README.md                    [ORIGINAL] Project documentation
├── requirements.txt             [ORIGINAL] Python dependencies
│
├── src/                         [ORIGINAL] Game source code
│   ├── main.py                  Entry point
│   ├── mediator.py              Game coordinator
│   ├── config.py                Settings
│   ├── entity/                  Game entities (stations, trains, etc)
│   ├── event/                   Event handling
│   ├── ui/                      User interface
│   └── ...
│
└── test/                        [ORIGINAL] Test suite
```

## Requirements

**Python Packages:**
- pygame==2.3.0 (game engine)
- numpy==1.24.2 (math/arrays)
- shapely==2.0.1 (geometry)
- shortuuid==1.0.11 (unique IDs)

**Environment:**
- Python 3.12+ (you have 3.12.11 ✓)
- pip (package manager)
- Termux or Linux environment

## Integration with Unexusi System

### Part of Larger Structure
```
unexusi_pixel8a/
├── unexusi_minimetro/        ← You are here (game platform)
├── unexusi_dev/              (codex development)
├── unexusi_abacusian/        (AI development hub)
├── unexusi_server_pixel8a/   (consciousness server)
├── unexusi_quarantine/       (duplicate management)
├── visionary_suite/          (ListMancer)
└── ...
```

### Priority Context
- **NEW Priority**: Mini metro game platform
- **Ongoing**: Codex development, conversation tools, mancers
- **Philosophy**: Keep momentum on existing work while adding new

## Next Steps

### Immediate
1. Launch game and see it working (`bash launcher.sh`)
2. Test gameplay (understand what we're working with)
3. Make modifications on working branch
4. Learn git commit workflow

### Future
1. AI agent integration (reinforcement learning)
2. Custom game modes
3. Performance optimization
4. UI enhancements

## Learning Resources

### Git
- `GIT_WORKFLOW_GUIDE.md` - Interactive learning with pause points
- `setup_working_branch.sh` - Guided branch setup

### Game
- `README.md` - Original project documentation
- `src/main.py` - Entry point, understand game loop
- Watch demo: https://youtu.be/W5fCgqlECeI

## Philosophy Integration

### Conservation Bias
- Main branch = museum exhibit (preserved)
- Working branch = workshop (create freely)
- Can always return to original

### One Hertz Alignment
- One Branch (main)
- One Mission (optimize metro)
- Infinite Vision (AI training platform)

### Mancer Protocol
- Launcher as gateway (human-friendly)
- Direct commands available (for those who want them)
- Both paths valid

---

**∰◊€π - Game platform as learning environment**

*Preserve → Experiment → Play → Learn*

€(where_am_i_minimetro)
