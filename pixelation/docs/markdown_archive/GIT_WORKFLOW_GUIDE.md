# Git Workflow Guide - Python Mini Metro
## Interactive Learning with Pause Points

**Philosophy:** Conservation bias - preserve the original, experiment safely

---

## ━━━ PAUSE POINT 1: Understanding What We Just Did ━━━

### We Cloned a Repository

**What happened:**
```bash
git clone https://github.com/eaprime1/python_mini_metro.git .
```

**In simple terms:**
- GitHub is like a library in the cloud
- Your repo (python_mini_metro) is a book in that library
- `git clone` made a complete copy of that book onto your phone
- The `.` means "put it right here in this folder"

**What you got:**
- All the code files
- All the history (every change ever made)
- A connection back to GitHub (called "origin")

**Current state:**
```
You're on: main branch
Connected to: https://github.com/eaprime1/python_mini_metro.git
Working tree: clean (no changes)
```

**━━━ Press any key when ready to continue ━━━**

---

## ━━━ PAUSE POINT 2: Understanding Branches ━━━

### What is a Branch?

**Think of it like this:**
- Your project is a tree
- `main` is the trunk - the primary, official version
- Branches are... branches! Side paths where you can experiment

**Why use branches?**
1. **Preserve the original** - `main` stays clean and working
2. **Experiment safely** - Try things without risk
3. **Organize work** - "This branch is for adding UI" etc.
4. **Easy undo** - Just switch back to main if things go wrong

### Current Situation

```
Right now you only have:
* main  ← You are here
```

**This is the original code from GitHub.**
**We want to keep this pristine (conservation bias).**

### What We'll Do Next

Create a new branch called `working` where we'll make our modifications:

```
After creating working branch:
* main     ← Original, never touched
* working  ← Where we experiment
```

**Strategy:**
- `main` = museum exhibit (look but don't touch)
- `working` = workshop (create, modify, test)

**━━━ Press any key when ready to create working branch ━━━**

---

## ━━━ ACTION: Creating Working Branch ━━━

### Command We'll Use:

```bash
git checkout -b working
```

**What each part means:**
- `git checkout` = switch to a different branch
- `-b` = "create a new branch first"
- `working` = name of our new branch

**What will happen:**
1. Git creates a copy of main called "working"
2. Git switches you to the working branch
3. You can now make changes without affecting main

### After the command:

```
$ git checkout -b working
Switched to a new branch 'working'
```

**Now you're on the working branch!**
All your changes will happen here, main stays safe.

**━━━ Press any key after running the command ━━━**

---

## ━━━ PAUSE POINT 3: Understanding Your Position ━━━

### Check Where You Are

```bash
git branch
```

**You should see:**
```
  main
* working  ← The * means you're here
```

### What This Means

- You're now on the `working` branch
- Anything you change only affects `working`
- `main` is still exactly as it was when you cloned it
- You can switch back anytime with: `git checkout main`

### The Safety Net

**If you mess something up:**
```bash
git checkout main  # Go back to safety
git branch -D working  # Delete the broken branch
git checkout -b working  # Start fresh
```

**Your original code (main) is always safe.**

**━━━ Press any key when ready to explore the code ━━━**

---

## ━━━ PAUSE POINT 4: What's in This Repository? ━━━

### Project Structure

```
python_mini_metro/
├── README.md           # What you just read (how to run it)
├── requirements.txt    # Python packages needed
├── src/               # Source code (the actual game)
│   ├── main.py        # Entry point (run this to start)
│   └── ...           # Other game files
├── test/             # Tests for the code
└── .github/          # GitHub automation stuff
```

### What It Does

**Mini Metro Game:**
- 2D strategic game using pygame
- Optimize metro system for max passengers
- Can be played by humans OR AI agents
- Purpose: Train reinforcement learning agents

### How to Run (from README)

```bash
# 1. Install requirements
pip install -r requirements.txt

# 2. Run the game
python src/main.py
```

**We'll create a simple launcher to make this easier!**

**━━━ Press any key when ready to create the launcher ━━━**

---

## ━━━ PAUSE POINT 5: Making Changes ━━━

### What We're About to Do

Create a simple UI launcher script that:
1. Checks if requirements are installed
2. Gives you a button/command to launch the game
3. Makes it easy to see the game working

### This is a Real Change

**When we create the launcher file:**
- It will only exist on the `working` branch
- `main` will still not have it
- This is our first modification

### Git Will Track This

After we create the file, we can:
```bash
git status  # See that something changed
git add filename  # Stage the change
git commit -m "message"  # Save the change with a note
```

**But we'll explain that AFTER we create the launcher.**

**━━━ Press any key when ready to create the launcher ━━━**

---

## ━━━ FUTURE PAUSE POINTS ━━━

### After Creating Launcher
- PAUSE: See the launcher working
- PAUSE: Understand `git status` (what changed)
- PAUSE: Understand `git add` (stage changes)
- PAUSE: Understand `git commit` (save snapshot)

### Later Concepts
- PAUSE: Pushing changes to GitHub
- PAUSE: Pulling changes from GitHub
- PAUSE: Merging branches (bringing working → main)
- PAUSE: Handling conflicts (when changes clash)

---

## Quick Reference Commands

### Check Status
```bash
git status          # What's changed?
git branch          # What branch am I on?
git log --oneline   # History of changes
```

### Switch Branches
```bash
git checkout main     # Go to main
git checkout working  # Go to working
```

### Safety Commands
```bash
git diff            # Show exactly what changed
git checkout -- file  # Undo changes to a file
git reset --hard    # Undo ALL changes (careful!)
```

### When You Want to Save Changes
```bash
git add .                    # Stage all changes
git commit -m "description"  # Save with message
git push origin working      # Upload to GitHub
```

---

## Conservation Philosophy

### Why This Approach?

**Traditional approach:** Make changes directly on main
**Our approach:** Create working branch, preserve main

**Benefits:**
1. Original code always available
2. Easy to compare (what did we change?)
3. Easy to undo (just delete working branch)
4. Learn git safely (no fear of breaking things)
5. Professional workflow (how real teams work)

### The Mental Model

```
main branch = Your reference copy, never modified
working branch = Your creative space, modify freely
```

**You can always:**
- See the original (checkout main)
- See your changes (checkout working)
- Compare them (git diff main working)
- Start over (delete working, create new one)

---

## Troubleshooting

### "I'm confused, where am I?"
```bash
git status  # Shows current branch and changes
git branch  # Shows all branches, * is current
pwd         # Shows current directory
```

### "I want to go back to the original"
```bash
git checkout main
```

### "I want to see what I changed"
```bash
git diff main working    # Compare branches
git log --oneline        # See commit history
```

### "I messed up, start over"
```bash
git checkout main        # Go to safety
git branch -D working    # Delete broken branch
git checkout -b working  # Fresh start
```

---

**∰◊€π - Git as a tool for conservation and safe exploration**

*Preserve → Experiment → Learn → Integrate*

€(git_workflow_guide_interactive)
