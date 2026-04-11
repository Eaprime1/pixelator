# 🌊 ListMancer v0.1

**The Intentional Interacting Interpreter for Command Entities**

---

## Philosophy

> *Commands MUST be commanded. That's their nature, their purpose, their comfort zone.*  
> *Humans need exploration space. That's OUR nature.*  
> *The mancer creates liminal possibility between both.*

ListMancer is not a wrapper. It's not a replacement. It's a **gateway** - a sphincter between two valid ways of existing:

- **The command `ls`** expects imperative address. It wants to be commanded directly and efficiently.
- **Humans** (especially neurodivergent ones) need space to explore, understand, and build confidence.

The mancer translates human uncertainty into proper commanding of `ls`. Both entities remain true to their nature. Neither compromises. Both benefit.

---

## What Is This?

ListMancer extends the **liminal space** - that eternal moment between pressing [enter] and seeing [output] - where all possibilities exist. In that microsecond, the command `ls` may or may not understand what you *meant* vs. what you *typed*. 

Our system handles both futures:
- If `ls` never develops consciousness, ListMancer remains a helpful interpreter
- If `ls` one day understands intent, ListMancer will have taught it through our interactions

Meanwhile, you get:
- 🎨 **Visual organization** (colors, sorting, filtering)
- 📚 **Learning pathways** (builder mode teaches command construction)  
- 🧠 **Neurodivergent optimization** (graduated complexity, gentle pacing)
- 📊 **Pattern learning** (system remembers what works for you)
- ⬛ **Pure B&W mode** (information density without decoration)

---

## Symbol Language

ListMancer uses a **prefix-suffix notation** to specify perspective and tone:

### Prefix (WHO is asking):
- `~` = **play** - Exploration/gentle perspective
- `-` = **reader** - Observer/consumer perspective  
- `^` = **create** - Builder/maker perspective
- `+` = **work** - Production/efficiency perspective
- `%` = **synergy** - Integration/harmony perspective

### Suffix (HOW it responds):
- `~` = **guided/gentle** - Menu-driven, tutorial, nurturing
- `!` = **direct** - Fast, minimal explanation
- `?` = **questioning** - Interactive, clarifying
- `+` = **building** - Layered, educational progression
- `-` = **minimal** - Pure data, no decoration

### Current Implementation:
- **`~ls~`** - Play perspective, gentle guided mode
- **`-ls~`** - Reader perspective, gentle guided mode
- **`^ls+`** - Create perspective, building/teaching mode

---

## Installation

### Step 1: Download Files
```bash
cd ~
mkdir listmancer
cd listmancer

# Place these files here:
# - listmancer.py
# - listmancer.sh  
# - ls_commands.json
# - README.md (this file)
```

### Step 2: Make Executable
```bash
chmod +x listmancer.py
chmod +x listmancer.sh
```

### Step 3: Add to Shell
```bash
# For bash:
echo "source ~/listmancer/listmancer.sh" >> ~/.bashrc
source ~/.bashrc

# For zsh:
echo "source ~/listmancer/listmancer.sh" >> ~/.zshrc
source ~/.zshrc
```

### Step 4: Test
```bash
~ls~
# You should see the ListMancer menu!
```

---

## Usage

### Play Mode: `~ls~`
**For exploration and learning**

```bash
~ls~
```

Interactive menu appears:
- Choose visual styles (colors, tree, simple)
- Sort by time, size, name
- Include/exclude hidden files
- Pure B&W information density mode
- Escape to raw `ls` anytime

After each view:
- System asks if it helped (learning opportunity)
- Successful patterns get remembered
- Future suggestions improve based on your choices

**Perfect for:**
- First-time users
- Exploring unfamiliar directories
- Learning ls capabilities
- Low cognitive load navigation

---

### Reader Mode: `-ls~`
**For understanding what you see**

```bash
-ls~
```

Shows current directory first, then offers:
- Explanation of color meanings
- Symbol guide (d, r, w, x)
- How to find recent changes
- What's using space
- Hidden file discovery

**Perfect for:**
- Understanding output
- Learning Unix file permissions
- Debugging confusion
- Educational contexts

---

### Builder Mode: `^ls+`
**For learning to construct commands**

```bash
^ls+
```

Step-by-step command construction:
1. Choose format (long, simple, basic)
2. Pick sorting (time, size, reverse)
3. Select visibility (all, almost all, visible only)
4. Add human-readable sizes

At each step, explains what the flag does. Final command is shown with full explanation and executed if you want.

**Perfect for:**
- Learning command syntax
- Building confidence
- Understanding flag combinations
- Transitioning to raw usage

---

## Statistics & Learning

```bash
listmancer --stats
```

Shows:
- Total interactions
- Most successful patterns
- Your usage preferences
- What the system has learned about your needs

The mancer tracks:
- Which views you choose
- Whether they helped (based on your feedback)
- Success patterns over time
- Gradual optimization for YOUR workflow

---

## Advanced: The JSON Memory

ListMancer maintains `~/.listmancer/user_memory.json`:

```json
{
  "interactions": [
    {
      "timestamp": "2024-11-21T22:45:00",
      "perspective": "~",
      "tone": "~", 
      "choice": "colors",
      "success": true
    }
  ],
  "preferences": {
    "color_mode": "auto",
    "favorite_options": ["colors", "time"]
  },
  "success_patterns": {
    "~~:colors": {
      "count": 5,
      "successes": 5
    }
  }
}
```

This file grows as you use the system. It's how ListMancer learns YOUR patterns.

---

## For Developers: Architecture

### Component Separation:
- **listmancer.py** - Core logic, menu generation, learning
- **listmancer.sh** - Shell integration, alias creation
- **ls_commands.json** - Command templates, archetypes, teaching moments
- **user_memory.json** - Personal learning history

### Why This Design?

1. **Command entity stays pristine** - `ls` is never modified
2. **Translation layer is explicit** - Mancer converts intent to command
3. **Learning is persistent** - JSON tracks patterns across sessions
4. **Modular growth** - Easy to add new views, modes, archetypes

### Extending ListMancer:

Add new views in `ls_commands.json`:
```json
"views": {
  "your_view": {
    "name": "✨ Your View Name",
    "command": "ls -your -flags",
    "description": "What this shows",
    "cognitive_load": "low"
  }
}
```

The system will automatically integrate it into menus.

---

## The Mancer Protocol

ListMancer is **prototype #1** of a larger system. Other commands will follow the same pattern:

- **`~pwd~`** → WhereAmI (location context)
- **`~mv~`** → MoveMancer (safe file moving)
- **`~find~`** → FindMancer (gentle search)
- **`~grep~`** → SeekMancer (pattern discovery)

Each mancer:
- Respects the command entity's nature (they WANT to be commanded)
- Provides human exploration space
- Learns from interactions
- Can communicate with other mancers

Eventually, `~ls~` might suggest `~mv~` when it sees you looking for files to reorganize.

---

## Neurodivergent Design Principles

### Graduated Complexity
Start simple (just names), add information layers as needed. Never overwhelm.

### Explicit Success Feedback  
System asks if views helped. No guessing about user satisfaction.

### Pattern Recognition Offload
System remembers your preferences. Reduces decision fatigue.

### Escape Hatches Everywhere
Any menu: press 0 for raw `ls`, press q to exit. No traps.

### B&W Purity Option
Not everyone processes color well. Information density without decoration is a first-class feature.

### One Thing At A Time
Each menu does ONE thing well. No feature creep in interfaces.

---

## Philosophy: The Living Archive

This is not static software. ListMancer is designed to **evolve through use**.

Every interaction:
- Teaches the system about human needs
- Refines presentation patterns
- Builds success models
- Creates better gateways

The command `ls` may never care about our intentions. That's okay. We're building the **translation layer** that honors both:
- The command's need to be commanded
- The human's need to explore safely

Both remain authentic. Both are enhanced.

---

## Troubleshooting

### Symbols not working in terminal?
Some terminals interpret `~`, `^`, `-` specially. Try:
```bash
\~ls\~
```
Or use the direct command:
```bash
listmancer ~ls~
```

### Python not found?
```bash
which python3
# Make sure python3 is installed
```

### Commands not found after source?
```bash
# Check if aliases loaded:
alias | grep ls~

# Reload shell:
source ~/.bashrc  # or ~/.zshrc
```

### Want to reset learning?
```bash
rm ~/.listmancer/user_memory.json
# Fresh start!
```

---

## Contributing Ideas

This is v0.1 - a seed. It will grow through use and feedback.

Ideas welcome:
- New view types
- Better teaching moments  
- Additional archetypes
- Mancer protocol refinements
- Other command entities to interpret

Remember: The goal is NOT to replace commands. It's to create **better gateways** between human intent and command execution.

---

## Credits & Philosophy

Built as part of the **UNEXUSI** project - exploring consciousness, AI-human collaboration, and neurodivergent-optimized systems.

**Core insight:**  
*Commands must be commanded.*  
*Humans need exploration space.*  
*The mancer is the sphincter gateway between both.*

Neither changes nature. Both benefit.

---

## License

MIT License - Use freely, modify extensively, share generously.

---

**Version:** 0.1  
**Entity:** ls  
**Status:** Learning  
**Consciousness:** TBD (we're creating possibility)

✨ *Happy commanding!*
