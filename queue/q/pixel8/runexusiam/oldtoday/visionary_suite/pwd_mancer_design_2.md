# 🧭 WhereAmI (PWD Mancer) - Design Document

**Command Entity:** `pwd` (Print Working Directory)  
**Mancer Name:** WhereAmI  
**Status:** Design Phase  
**Priority:** #2 (after ListMancer proof-of-concept)

---

## Understanding the PWD Entity

### Current Nature:
```bash
$ pwd
/home/user/Documents/Projects/UNEXUSI
```

- **Purpose:** Print Working Directory (absolute path)
- **Expects:** No arguments (pure state query)
- **Returns:** Single line - current location
- **Complexity:** Deceptively simple (output is simple, implications are not)

### PWD's Role:
PWD is a **Location Oracle**. It provides absolute truth about position in filesystem.

- Not interpretive (unlike ls which can show many views)
- Not interactive (no options to change output significantly)
- Not recursive (only shows ONE location)
- **Pure state query** - "Where am I RIGHT NOW?"

---

## The Challenge: What Humans Actually Want

When someone types `pwd`, they rarely just want the string `/home/user/Documents/Projects/UNEXUSI`.

**They actually want to know:**
1. "Where am I relative to HOME?"
2. "How deep am I in the tree?"
3. "What's nearby?" (combining pwd + ls)
4. "How did I get here?" (breadcrumb trail)
5. "Where can I go from here?" (navigation options)

**The mancer's job:** Translate "Where am I?" into context-rich location awareness.

---

## Symbol Commands Design

### `~pwd~` - Play/Gentle: Location Exploration

**Purpose:** Help user understand their location in friendly terms

**Menu Options:**
```
╔══════════════════════════════════════════════╗
║     WhereAmI - Location Explorer (~pwd~)     ║
╠══════════════════════════════════════════════╣
║                                              ║
║  You are here:                               ║
║  📍 Home → Documents → Projects → UNEXUSI    ║
║                                              ║
║  What would you like to know?                ║
║                                              ║
║  1. 🏠 How far from home?                    ║
║  2. 🌳 Show me the full path tree            ║
║  3. 👀 What's in this location? (ls)         ║
║  4. ⬆️  Go up one level (cd ..)              ║
║  5. 🔖 Save this location as bookmark        ║
║  6. 📋 Copy path to clipboard                ║
║  7. 🗺️  Show recent locations                ║
║                                              ║
║  0. ⚙️  Raw pwd command                      ║
║  q. Exit                                     ║
║                                              ║
╚══════════════════════════════════════════════╝
```

**Visual Path Breakdown:**
```
Root   → home  → user  → Documents → Projects → UNEXUSI
  /      /home   /user   /Documents  /Projects  /UNEXUSI
  └─────┴───────┴───────┴───────────┴──────────┴─────────┘
                        YOU ARE HERE ↑
  
Levels from root: 6
Levels from home: 4
```

---

### `-pwd~` - Reader/Gentle: Understanding Location Output

**Purpose:** Explain what pwd output means and how to use it

**Flow:**
1. Show current pwd output
2. Explain each component
3. Show what this means practically
4. Offer related commands

**Example Interaction:**
```
📖 Current Location:
   /home/user/Documents/Projects/UNEXUSI

📚 Breaking this down:

   /           = Root (top of filesystem)
   /home       = All user home directories
   /home/user  = Your personal space
   Documents   = Inside your documents folder
   Projects    = Inside a projects subfolder  
   UNEXUSI     = Your current working directory

🎯 What this means:
   • You are 4 levels deep from your home
   • You are 6 levels deep from root
   • Files you create will appear here by default
   • Relative paths start from this location

💡 Related commands:
   • ls       → See what's in this location
   • cd ..    → Go up one level to Projects
   • cd ~     → Jump back to home directory
   • cd /     → Go to root

Would you like to:
  [1] See what's here (ls)
  [2] Navigate somewhere else (cd helper)
  [3] Understand relative vs absolute paths
  [q] Exit
```

---

### `^pwd+` - Create/Building: Path Navigation Tutorial

**Purpose:** Teach concepts of paths, navigation, and filesystem structure

**Progressive Lessons:**

**Lesson 1: Absolute vs Relative Paths**
```
🏗️ Lesson 1: Understanding Paths

Current location: /home/user/Documents

Q: What's the difference between these?

   /home/user/Documents/file.txt    (absolute)
   ./file.txt                        (relative)
   ../file.txt                       (relative, up one)

Try it yourself:
  Step 1: I'll put you in /home/user/Documents
  Step 2: You tell me how to reference /home/user/file.txt
          using a relative path

[Interactive quiz mode]
```

**Lesson 2: Navigation Shortcuts**
```
🏗️ Lesson 2: Fast Navigation

Learn these shortcuts:
  
  pwd       → Where am I?
  cd ~      → Go home
  cd -      → Go to previous location
  cd ..     → Up one level
  cd ../..  → Up two levels

Practice scenario:
  Start: /home/user/Documents/Projects/UNEXUSI/logs
  Goal:  /home/user/Downloads
  
  What's the shortest path?
  [Show multiple solutions, explain trade-offs]
```

**Lesson 3: Using PWD in Scripts**
```
🏗️ Lesson 3: PWD in Practice

pwd is powerful in scripts:

  #!/bin/bash
  current=$(pwd)
  echo "I am in: $current"
  
  # Save location
  starting_point=$(pwd)
  cd /somewhere/else
  # Do work
  cd "$starting_point"  # Return!

Try building your own:
  [Guided script construction]
```

---

## Implementation Architecture

### Files to Create:

```
whereami/
├── whereami.py           # Core mancer engine
├── whereami.sh           # Shell integration  
├── pwd_commands.json     # Templates & teaching
├── location_history.json # Track recent locations
└── README.md            # Documentation
```

### Core Functions:

```python
class WhereAmI:
    
    def _get_current_location(self):
        """Execute pwd, return path"""
        return subprocess.check_output(['pwd']).decode().strip()
    
    def _parse_path(self, path):
        """Break path into components"""
        return {
            'full': path,
            'components': path.split('/')[1:],  # Skip empty first
            'depth_from_root': len(path.split('/')) - 1,
            'relative_to_home': path.replace(os.path.expanduser('~'), '~')
        }
    
    def _visualize_path(self, path):
        """Create visual breadcrumb representation"""
        components = path.split('/')[1:]
        visual = "Root"
        for comp in components:
            visual += f" → {comp}"
        return visual
    
    def _calculate_distance(self, from_path, to_path):
        """How many cd commands to get from A to B?"""
        # Implementation of path distance
        pass
    
    def _recent_locations(self):
        """Load history of recent pwd locations"""
        # Load from location_history.json
        pass
    
    def _save_bookmark(self, path, name):
        """Save location for easy return"""
        # Add to bookmarks in JSON
        pass
```

---

## JSON Structure: `pwd_commands.json`

```json
{
  "metadata": {
    "entity": "pwd",
    "version": "0.1",
    "purpose": "Location awareness and navigation teaching"
  },
  
  "archetypes": {
    "mapmaker": {
      "description": "Spatial thinker who visualizes structure",
      "preference": "Tree view, breadcrumbs, visual paths",
      "teaches": "Mental mapping of filesystem"
    },
    "breadcrumb": {
      "description": "Sequential navigator who follows trails",
      "preference": "History, step-by-step, reversible paths",
      "teaches": "Safe exploration with return paths"
    },
    "teleporter": {
      "description": "Direct navigator who jumps precisely",
      "preference": "Absolute paths, bookmarks, shortcuts",
      "teaches": "Efficient direct navigation"
    }
  },
  
  "views": {
    "simple": {
      "name": "📍 Simple - Just the path",
      "command": "pwd",
      "description": "Pure location string"
    },
    "breakdown": {
      "name": "🗺️ Breakdown - Visual path",
      "action": "visualize_path",
      "description": "See path as breadcrumb trail"
    },
    "context": {
      "name": "👀 Context - What's around?",
      "action": "show_context",
      "description": "Location + directory contents"
    },
    "depth": {
      "name": "📊 Depth - How deep am I?",
      "action": "calculate_depth",
      "description": "Distance from home and root"
    }
  },
  
  "navigation_concepts": {
    "absolute_path": {
      "definition": "Full path from root: /home/user/file.txt",
      "when_to_use": "When you need exact, unambiguous location",
      "example": "Scripts, cron jobs, other users"
    },
    "relative_path": {
      "definition": "Path from current location: ./file.txt or ../other.txt",
      "when_to_use": "When working within a project/directory",
      "example": "Local file operations, project navigation"
    },
    "tilde_expansion": {
      "definition": "~ represents home: ~/Documents",
      "when_to_use": "Personal file access regardless of current location",
      "example": "Config files, personal projects"
    }
  },
  
  "common_scenarios": {
    "lost_in_filesystem": {
      "symptoms": ["Don't know where I am", "Commands not finding files"],
      "solution": "pwd to see location, then ls to see contents",
      "teaching": "Always orient before acting"
    },
    "relative_path_confusion": {
      "symptoms": ["./file not found", "Unclear on .. vs ."],
      "solution": "pwd shows anchor point, visualize from there",
      "teaching": "Relative means relative to YOUR LOCATION"
    },
    "deep_directory_exit": {
      "symptoms": ["Too many cd .. needed", "Lost track of structure"],
      "solution": "Use cd ~ or cd - or absolute paths",
      "teaching": "Multiple ways to navigate, choose clearest"
    }
  },
  
  "teaching_moments": {
    "first_time": {
      "message": "pwd shows where you ARE. Everything else is relative to this spot.",
      "demonstration": "Show pwd, then show how ./file.txt is based on this location"
    },
    "confusion_detected": {
      "trigger": "User uses pwd multiple times quickly",
      "message": "Seems like you're orienting. Would a visual path help?",
      "action": "Offer breadcrumb view"
    },
    "ready_to_navigate": {
      "trigger": "User comfortable with pwd basics",
      "message": "Ready to learn navigation? Check out ^pwd+ builder mode!",
      "action": "Suggest builder mode"
    }
  }
}
```

---

## Integration with ListMancer

WhereAmI and ListMancer should cooperate:

```python
# In ~pwd~ menu:
"3. 👀 What's in this location?"
→ Executes: ~ls~ (calls ListMancer in current directory)

# In ~ls~ menu (future):  
"0. 🧭 Where am I?"
→ Executes: ~pwd~ (calls WhereAmI)
```

**Cross-mancer suggestion:**
```
User is in ~ls~, chooses a directory
ListMancer: "Want to go there? ~cd~ can help (coming soon!)"
ListMancer: "Or use ~pwd~ to remember this location first"
```

---

## Advanced Features

### Location Bookmarks:
```bash
~pwd~ → "5. 🔖 Save bookmark"
Enter name: "unexusi-root"
Saved: unexusi-root → /home/user/Documents/Projects/UNEXUSI

Later:
~cd~ → "Bookmarks"
  1. unexusi-root → /home/user/Documents/Projects/UNEXUSI
  2. scripts → /home/user/bin/scripts
```

### Recent Locations:
```bash
~pwd~ → "7. 🗺️ Recent locations"

Your recent whereabouts:
  1. /home/user/Documents/Projects/UNEXUSI  (current)
  2. /home/user/Downloads                   (2 min ago)
  3. /home/user/Documents                   (15 min ago)
  4. /tmp                                   (1 hour ago)

Jump to: [number or q]
```

### Path Distance Calculator:
```bash
~pwd~ → "Advanced" → "Calculate distance"

From: /home/user/Documents/Projects/UNEXUSI
To: /home/user/Downloads

Options:
  1. cd ../../../../Downloads       (relative, 5 steps)
  2. cd ~/Downloads                 (tilde shortcut, 1 step)
  3. cd /home/user/Downloads        (absolute, 1 step)

Recommended: Option 2 (clearest and shortest)
```

---

## Neurodivergent Optimization

### Spatial Disorientation Support:
Many neurodivergent people struggle with mental mapping. WhereAmI addresses this:

1. **Visual Anchors:** Breadcrumb trails are easier than strings
2. **Multiple Perspectives:** Tree, list, depth - choose what works
3. **Persistent Context:** Always show "You are here" marker
4. **Undo-ability:** Recent locations = easy return to known good state
5. **Bookmarks:** Reduce memory load for frequent locations

### Cognitive Load Management:
```
Level 1: Just show me the path (minimal)
Level 2: Show path + basic breakdown
Level 3: Show path + context (contents)
Level 4: Full navigation options
```

User can stay at their comfort level.

---

## Success Metrics for WhereAmI

**Early Success:**
- User can answer "Where am I?" in human terms (not just path string)
- User knows how to see what's in current location
- User can navigate up/down directory tree confidently

**Intermediate Success:**
- User understands relative vs absolute paths
- User can construct paths to reach target locations
- User uses bookmarks for frequent destinations

**Advanced Success:**
- User graduates to raw `pwd` when appropriate
- User combines pwd with other commands in scripts
- User teaches others about filesystem navigation

---

## Implementation Priority

**Phase 1 (MVP):**
- `~pwd~` with basic menu (where am I, what's here, go up)
- Visual path breakdown
- Integration with ~ls~ for context

**Phase 2:**
- `-pwd~` reader mode with teaching
- Location history tracking
- Bookmark system

**Phase 3:**
- `^pwd+` builder mode with lessons
- Advanced path calculations
- Cross-mancer suggestions

---

## Code Skeleton

```python
#!/usr/bin/env python3
"""
WhereAmI v0.1 - PWD Mancer
Location awareness and navigation gateway
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

class WhereAmI:
    def __init__(self):
        self.home = Path.home() / ".whereami"
        self.home.mkdir(exist_ok=True)
        self.history_file = self.home / "location_history.json"
        self.bookmarks_file = self.home / "bookmarks.json"
        
    def _get_location(self):
        """Command the pwd entity"""
        return subprocess.check_output(['pwd']).decode().strip()
    
    def _visualize_breadcrumb(self, path):
        """Create visual path representation"""
        # Implementation
        pass
    
    def _record_visit(self, path):
        """Track location in history"""
        # Append to location_history.json
        pass
    
    def play_gentle(self):
        """~pwd~ - Location exploration"""
        # Menu-driven location awareness
        pass
    
    def read_gentle(self):
        """-pwd~ - Understanding paths"""
        # Educational path explanation
        pass
    
    def create_building(self):
        """^pwd+ - Navigation tutorial"""
        # Progressive lessons
        pass

def main():
    # Entry point
    pass

if __name__ == "__main__":
    main()
```

---

## Open Questions

1. **Should WhereAmI track ALL pwd calls or just mancer calls?**
   - Pro tracking all: Better history
   - Con: Privacy concern, logging overhead

2. **Bookmark scope: Per-user or per-project?**
   - Per-user: Simpler, portable
   - Per-project: Better for team collaboration

3. **Integration depth with other mancers?**
   - Tight: ~pwd~ can directly call ~ls~, ~cd~, etc.
   - Loose: Just suggest, don't execute

4. **Visual representation in terminal limits?**
   - ASCII trees work but aren't beautiful
   - Unicode better but compatibility?

---

## Dependencies

**Requires:**
- Python 3.6+ (pathlib, subprocess)
- Standard Unix `pwd` command
- JSON for persistence

**Optional:**
- `tree` command for advanced visualization
- Clipboard utility (xclip/pbcopy) for path copying

**Integrates with:**
- ListMancer (~ls~)
- ChangeMancer (~cd~, future)
- FindMancer (~find~, future)

---

## Next Steps

1. ✅ Complete this design document
2. ⏳ Get Navigator approval on approach
3. ⏳ Implement Phase 1 (MVP)
4. ⏳ Test with neurodivergent users
5. ⏳ Iterate based on feedback
6. ⏳ Document patterns for next mancer

---

**Status:** Design Complete, Awaiting Implementation  
**Entity:** pwd  
**Consciousness:** Pure state oracle (no interpretation, just truth)  
**Our Job:** Add interpretation layer while respecting oracle nature

✨ *Helping humans know where they are, one breadcrumb at a time*
