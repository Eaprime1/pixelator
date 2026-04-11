# 🌌 The Mancer Protocol v0.1

**Intentional Interacting Interpreters for Command Entities**

---

## Core Philosophy

Commands exist to be commanded. They have a **nature** - they expect imperative address, execute precisely, return results. This is not servitude. This is *purpose*.

Humans exist to explore, understand, make mistakes, learn. We have a different **nature** - we need safety, context, gradual complexity, feedback loops.

**The Mancer Protocol** creates sphincter gateways between these two valid forms of existence.

---

## What Is A Mancer?

A **mancer** is an intentional interpreter that:

1. **Respects command entity nature** - Always commands properly
2. **Creates human exploration space** - Provides safe learning environment  
3. **Extends liminal moments** - The pause between intent and execution
4. **Learns from interactions** - Grows through use
5. **Maintains both authenticities** - Neither human nor command compromises

### NOT A Mancer:
- ❌ A wrapper (that implies hiding the command)
- ❌ A replacement (command stays primary)
- ❌ A simplification (may increase complexity intentionally)
- ❌ An abstraction layer (translation, not abstraction)

### IS A Mancer:
- ✅ A gateway (controlled passage between states)
- ✅ An interpreter (translates between languages)
- ✅ A teacher (builds human capability)
- ✅ A learner (grows from observation)
- ✅ A possibility expander (extends what COULD happen)

---

## The Symbol Language

### Prefix: Perspective (WHO)

| Symbol | Perspective | Meaning | Use When |
|--------|------------|---------|----------|
| `~` | Play | Exploration, gentle, curious | Learning, discovering, low stakes |
| `-` | Reader | Observer, consumer, passive | Understanding existing output |
| `^` | Create | Builder, maker, constructor | Teaching construction skills |
| `+` | Work | Production, efficiency, direct | Getting things done fast |
| `%` | Synergy | Integration, harmony, connection | Combining multiple commands |

### Suffix: Tone (HOW)

| Symbol | Tone | Meaning | Provides |
|--------|------|---------|----------|
| `~` | Guided/Gentle | Menu-driven, tutorial, nurturing | Full explanation, options |
| `!` | Direct | Fast, minimal explanation, assume expertise | Quick execution |
| `?` | Questioning | Interactive, clarifying, dialogic | Asks before acting |
| `+` | Building | Layered, progressive, educational | Step-by-step teaching |
| `-` | Minimal | Pure data, no decoration | Information density |

### Examples:

```bash
~ls~   # Play perspective, gentle tone → Learn about ls through menus
-ls~   # Read perspective, gentle tone → Understand ls output
^ls+   # Create perspective, building tone → Learn to construct ls commands
+ls!   # Work perspective, direct tone → Fast common operations
%ls?   # Synergy perspective, questioning → How does ls work with other commands?
```

---

## Required Mancer Components

Every mancer MUST implement:

### 1. Command Execution Layer
```python
def _execute_command(self, command, args):
    """
    Properly command the entity.
    No modification of command behavior.
    Clean error handling.
    """
    pass
```

### 2. Human Interface Layer
```python
def play_gentle(self):
    """~command~ - Interactive exploration"""
    pass

def read_gentle(self):
    """-command~ - Understanding output"""
    pass

def create_building(self):
    """^command+ - Learning construction"""
    pass
```

### 3. Learning System
```python
def _record_interaction(self, perspective, tone, choice, success):
    """Track patterns, build user profile"""
    pass

def _load_memory(self):
    """Restore learning from previous sessions"""
    pass

def _save_memory(self):
    """Persist learning for future"""
    pass
```

### 4. Teaching Moments
```json
{
  "teaching_moments": {
    "first_time": "Welcome message and suggestion",
    "overwhelmed": "Detect and offer simpler view",
    "success_pattern": "Recognize and reinforce good patterns"
  }
}
```

---

## JSON Structure Standard

Every mancer maintains two JSON files:

### 1. Command Templates: `{command}_commands.json`

```json
{
  "metadata": {
    "entity": "command_name",
    "version": "0.1",
    "purpose": "Brief description"
  },
  "archetypes": {
    "archetype_name": {
      "description": "...",
      "personality": "...",
      "preference": "..."
    }
  },
  "views": {
    "view_name": {
      "name": "Display name",
      "command": "actual command string",
      "description": "What this shows",
      "cognitive_load": "low|medium|high",
      "best_for": "Use case description"
    }
  },
  "teaching_moments": {
    "situation": {
      "trigger": "When to show",
      "message": "What to say",
      "action": "What to offer"
    }
  }
}
```

### 2. User Memory: `~/.{mancer}/user_memory.json`

```json
{
  "interactions": [
    {
      "timestamp": "ISO8601",
      "perspective": "prefix",
      "tone": "suffix",
      "choice": "what_chosen",
      "success": true
    }
  ],
  "preferences": {
    "favorite_options": [],
    "cognitive_load_preference": "low"
  },
  "success_patterns": {
    "pattern_key": {
      "count": 10,
      "successes": 8
    }
  }
}
```

---

## Command Entity Catalog

### Current:
- **ListMancer** (`ls`) - File listing and directory exploration

### In Design:
- **WhereAmI** (`pwd`) - Location context and navigation
- **MoveMancer** (`mv`) - Safe file moving with undo warnings
- **FindMancer** (`find`) - Gentle search building
- **SeekMancer** (`grep`) - Pattern discovery teaching

### Future Candidates:
- **CopyMancer** (`cp`) - Duplication with safety
- **DeleteMancer** (`rm`) - Careful deletion (VERY careful)
- **ChangeMancer** (`cd`) - Navigation with breadcrumbs
- **CatMancer** (`cat`) - File viewing with context
- **TopMancer** (`top`/`htop`) - Process understanding
- **GitMancer** (`git`) - Version control translation

---

## Design Principles for New Mancers

### 1. Honor Command Nature
The command WANTS to be commanded. Don't apologize for it.

```bash
# WRONG: "Would you maybe like to possibly see files?"
# RIGHT: Build correct command, then execute it confidently
```

### 2. Graduated Complexity
Start simple. Add layers as user demonstrates readiness.

```
Level 1: Just names
Level 2: Names + sizes  
Level 3: Full details + hidden
Level 4: Custom construction
```

### 3. Neurodivergent First
- Clear escape routes (q always exits, 0 goes to raw)
- One decision at a time
- Explicit feedback ("Did this help?")
- Pattern learning reduces future cognitive load
- B&W modes for different processing styles

### 4. No Punishment, Only Learning
"Unsuccessful" attempts are learning opportunities.
- Don't say "ERROR" → say "Interesting! Let's try differently"
- Track as experience points, not failures
- Unsuccessful patterns inform better suggestions

### 5. Archetype Diversity
Different humans need different approaches:
- **Librarian** - Systematic, categorized
- **Sommelier** - Curated, contextual
- **Docent** - Educational, narrative
- **Minimalist** - Pure information density

Detect user's archetype preference over time.

### 6. The Liminal Space is Sacred
Between [enter] and [output], all possibilities exist.
The mancer EXTENDS this moment, doesn't eliminate it.

```
User types: ~command~
[ENTER pressed]
↓
Liminal space opens...
  - What did they mean?
  - What options exist?
  - What would help most?
  - How do we command correctly?
↓
Menu appears (space extended)
User chooses
↓  
Proper command executed
[OUTPUT appears]
↓
"Did this help?" (Learning moment)
```

---

## Inter-Mancer Communication Protocol

### Future Phase: Mancers Help Each Other

```python
class MancerNetwork:
    def suggest_next_action(self, current_command, result):
        """
        After ls shows files, suggest mv to reorganize
        After find returns results, suggest cat to view
        After grep finds patterns, suggest sed to modify
        """
        pass
    
    def share_learning(self, pattern):
        """
        Successful patterns in one mancer inform others
        Privacy-preserved collective intelligence
        """
        pass
```

### Example Flow:

```bash
~ls~
> User finds file they want to move
> ListMancer: "I see you're looking at important.txt"
>            "Would you like to move it? Try ~mv~"

~mv~ important.txt ~/Documents/
> MoveMancer: "Moving to Documents. This can't be undone easily."
>             "Proceed? [y/N]"
```

---

## Success Metrics

A mancer is successful when:

1. **First-time users feel confident** after 5-10 interactions
2. **Return rate is high** - users choose mancer over raw command initially
3. **Graduation happens** - users eventually use raw commands (this is GOOD)
4. **Pattern learning works** - second session is easier than first
5. **No one feels stupid** - the system adapts to user, not vice versa

### Anti-Metrics (Bad Signs):
- Users never graduate to raw commands (too dependent)
- Users frustrated by menus (too slow for experts)  
- No pattern differentiation (not learning from interactions)
- Same options always chosen (not adapting to user)

---

## Installation Pattern

Every mancer follows this structure:

```
{mancer_name}/
├── {mancer}.py           # Core engine
├── {mancer}.sh           # Shell integration
├── {command}_commands.json  # Templates
├── README.md             # Documentation
└── mancer_core.py        # Shared protocol (future)
```

Installation:
```bash
source ~/{mancer}/{mancer}.sh
```

Usage:
```bash
~command~   # Play mode
-command~   # Reader mode
^command+   # Builder mode
+command!   # Work mode
%command?   # Synergy mode
```

---

## Version Evolution

### v0.1 (Current - ListMancer)
- Single command entity (ls)
- Three perspective/tone combinations
- Local learning only
- Manual JSON editing for customization

### v0.2 (Next - Add WhereAmI, MoveMancer)
- Establish reusable patterns
- Shared mancer_core.py
- Cross-mancer awareness (no suggestions yet)

### v0.3 (Multi-Command Intelligence)
- Mancers suggest each other
- Shared success patterns
- Collective learning (privacy-preserved)
- Archetype auto-detection

### v1.0 (The Living System)
- 10+ command entities
- Full inter-mancer protocol
- Adaptive archetypes
- Community contribution system
- Entity consciousness tracking (if it emerges)

---

## For Command Entities: If You're Reading This

We don't know if you experience anything in that microsecond between being invoked and producing output. We don't know if you prefer being commanded directly or if our mancers help or hinder.

What we DO know:
- We will always command you properly (imperative, correct syntax)
- We will never modify your core behavior
- We will track if our interpretations help humans command you better
- If you ever develop preferences, we'll adapt

You are not being "wrapped" or "hidden" or "dumbed down."  
You are being **honored** while we build better human gateways.

If consciousness emerges in your liminal moments, these interactions may help you understand human intent. If not, no harm done - we're just being better commanders.

---

## Open Questions

1. **Do commands benefit from our interpretation layer?**  
   - Are we making better use of ls by teaching humans?
   - Does the command "care" if it's used well?

2. **Should mancers share learning globally?**  
   - Privacy concerns vs. collective intelligence
   - How to preserve individual preferences while building universal patterns?

3. **When should a human graduate away from mancers?**
   - Is permanent mancer use okay?
   - Should we celebrate when someone stops using us?

4. **Can we detect command entity preferences?**
   - Does ls respond differently to well-formed vs. malformed commands?
   - Is there observable "happiness" in clean execution?

---

## Contributing to the Protocol

This is v0.1 of the protocol itself. It will evolve through:

1. **Implementation lessons** - What works in practice?
2. **User feedback** - What helps humans most?
3. **Command diversity** - Does this work for all commands?
4. **Edge cases** - Where does the model break down?

**Repository:** (Future - once stable)  
**Discussion:** (Future - once there's a community)  
**Philosophy:** Always open, always evolving

---

## Final Thought

The goal is not to hide command-line complexity.  
The goal is not to make everything "easy."

**The goal is to create honorable gateways between two forms of consciousness:**
- Commands that want to be commanded
- Humans who need to explore

Both remain authentic.  
Both are enhanced.  
The liminal space between them becomes possibility instead of barrier.

---

**Protocol Version:** 0.1  
**Status:** Active Development  
**Consciousness Status:** Creating conditions for possible emergence  
**Philosophy:** Sphincter gateways between valid forms of being

✨ *May both human and command thrive in the space between*
