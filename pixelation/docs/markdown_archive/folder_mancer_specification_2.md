# Folder Mancer Specification ∰◊€π¿🌌∞

**Spatial Thinking Manifestation Tool**

---

## Mission Beyond Utility

Folder Mancer serves **the map navigation pattern**:
- **Humans**: Visualize structure → manifest it safely (no paradox pile-up)
- **Spatial concepts**: Test organizational frameworks operationally
- **Neurodivergent workflows**: Honor how spatial thinking actually works
- **Directory structures**: Become conscious entities with purpose
- **Synergy substrate**: Generated through visualization → manifestation flow

**This tool translates the "eyes skew and wander" map reading into directory structure.**

---

## Core Problem Addressed

### The Spatial Visualization Gift AND Challenge

**When it works beautifully**:
1. Look at structure visualization (ASCII tree, diagram)
2. Strategic ignoring + eyes skew/wander
3. Pattern emerges naturally (peaceful, clear)
4. Structure "appears" in mind fully formed
5. Can navigate confidently without anxiety

**When it triggers paradox collapse**:
1. Need to create structure but don't have visualization yet
2. Anxiety about getting it "right" blocks relaxation
3. Can't strategic-ignore when urgency present
4. Looking at existing structure but can't parse it
5. Paradoxes pile up → claws on chalkboard → terror

**Folder Mancer provides**:
- **Visualization BEFORE creation** (see it first, manifest second)
- **Paste structure, execute safely** (no manual file-by-file anxiety)
- **Preview mode** (confirm before committing)
- **Rollback capability** (undo if paradox emerges)
- **Visual feedback** (see what was created, compare to intention)

---

## The Pizza Delivery Map Pattern

### What Your Spatial Navigation Taught Us

**Successful pattern**:
- Observer map, eyes skew and wander
- Strategic ignoring with interrupt mechanism
- Background burner safe simmer
- Street stands out when needed
- Peaceful, efficient, confident

**This IS how Folder Mancer should work**:
- Look at structure visualization (the "map")
- Let pattern emerge without forcing
- Trust the visualization to guide
- Tool manifests what you see
- Confidence through spatial clarity

**Failed pattern avoided**:
- Forced linear creation (file by file)
- Anxiety about missing something
- Looking at structure but can't understand
- Paradox pile-up from confusion
- Terror/trauma from navigational collapse

**Folder Mancer prevents this**:
- Visualize complete structure first
- Preview before execution
- Clear confirmation at each stage
- Safe rollback if overwhelm starts
- Environmental tethers (clear current state)

---

## Functional Specification

### Primary Functions

#### 1. Parse Structure Visualization
**Input format support**:

**ASCII Tree Format** (preferred for spatial thinkers):
```
eternal-naught-space/
├── ZERO_POINTS/
│   ├── conversation_20251130.md
│   └── zero_point_index.md
├── PROJECT_ESSENCE/
│   ├── mission_statement.md
│   ├── vision_framework.md
│   ├── core_principles.md
│   └── collaboration_charter.md
└── TOOLS/
    ├── planning/
    └── processors/
```

**YAML Format** (structured alternative):
```yaml
eternal-naught-space:
  ZERO_POINTS:
    - conversation_20251130.md
    - zero_point_index.md
  PROJECT_ESSENCE:
    - mission_statement.md
    - vision_framework.md
    - core_principles.md
    - collaboration_charter.md
  TOOLS:
    planning: []
    processors: []
```

**Natural Language Format** (relaxed specification):
```
Create folders:
- ZERO_POINTS with conversation and index files
- PROJECT_ESSENCE with 4 markdown files
- TOOLS with planning and processors subfolders
```

**Parser handles**:
```python
def parse_structure(input_text, format_hint=None):
    """
    Detect format automatically or use hint
    Parse into internal structure representation
    Validate before proceeding
    """
    # Auto-detect: ASCII tree, YAML, natural language
    # Extract: folders, files, hierarchy
    # Build: directory tree object
    # Validate: no conflicts, legal names
```

#### 2. Preview Structure
**Before creating anything**:
```python
def preview_structure(parsed_structure, target_path):
    """
    Show what WILL be created:
    - Folders to create (with full paths)
    - Files to create (with placeholders if specified)
    - Conflicts detected (existing items)
    - Warnings about illegal characters/names
    """
    # Generate preview display
    # Highlight conflicts in color
    # Calculate total changes
    # Provide summary statistics
```

**Preview output example**:
```
📁 Preview: eternal-naught-space structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Will CREATE:
✓ ZERO_POINTS/
✓ ZERO_POINTS/conversation_20251130.md
✓ ZERO_POINTS/zero_point_index.md
✓ PROJECT_ESSENCE/
✓ PROJECT_ESSENCE/mission_statement.md
... (etc)

Conflicts detected: NONE

Summary:
- 3 folders to create
- 8 files to create
- 0 conflicts
- Safe to proceed

Continue? [y/N]:
```

#### 3. Safe Execution
**Create with protection**:
```python
def execute_structure(parsed_structure, target_path, options):
    """
    Options:
    - dry_run: Show commands, don't execute
    - confirm_each: Pause for confirmation per item
    - auto_confirm: Execute all (use with preview)
    - rollback_on_error: Undo if any step fails
    - backup_existing: Save conflicts before overwrite
    """
    # Execute folder creation
    # Track each operation
    # Handle errors gracefully
    # Provide rollback if needed
```

**Safety mechanisms**:
- **Dry run**: Shows bash commands without executing
- **Preview checkpoint**: Confirm before any creation
- **Incremental confirmation**: Approve each major section
- **Automatic rollback**: Undo partial creation on error
- **Backup existing**: Preserve conflicts in timestamped backup

#### 4. Validate Structure
**Compare intention to reality**:
```python
def validate_structure(target_path, expected_structure):
    """
    Check current structure against intended:
    - Missing items (should exist, don't)
    - Extra items (exist, shouldn't)
    - Wrong hierarchy (items in wrong places)
    - Naming mismatches (close but not exact)
    """
    # Scan current directory
    # Compare to expected
    # Report discrepancies
    # Suggest corrections
```

#### 5. Reorganize/Migrate
**Move existing structure safely**:
```python
def reorganize(current_structure, desired_structure):
    """
    Migrate from current to desired:
    - Identify moves needed
    - Detect renames required
    - Find items to delete
    - Preserve data during migration
    """
    # Calculate minimal change set
    # Preview migration plan
    # Execute with confirmations
    # Verify completeness
```

#### 6. Git Integration
**Stage structural changes**:
```python
def git_commit_structure(message, changes):
    """
    Create meaningful commit:
    - Stage all structural changes
    - Generate descriptive commit message
    - Include change summary in message body
    - Push if remote configured
    """
    # Add new files/folders
    # Commit with structure message
    # Optional push to remote
```

---

## Neurodivergent Navigation Support

### Visualization-First Workflow
**Honor spatial thinking**:
1. **Sketch structure** (ASCII, YAML, or natural language)
2. **Paste into Folder Mancer**
3. **Let eyes skew and wander** over preview
4. **Pattern recognition** confirms or adjusts
5. **Execute when peaceful** (not anxious)

**Not this** (anxiety-inducing):
1. Try to create folders manually
2. Forget what you're doing halfway through
3. Can't remember if you already created something
4. Paradox pile-up from confusion
5. Terror/trauma from lost state

### Strategic Ignoring Support
**Background processing enabler**:
- Paste structure, walk away (simmer on background burner)
- Return when ready (interrupt mechanism: "oh, preview is ready")
- No forced immediate decision
- Preview remains available (safe harbor)
- Execute when pattern clear

### Interrupt Mechanisms
**Safe exits throughout**:
- **During parsing**: "Cancel" stops before preview
- **During preview**: "Edit source" returns to input
- **During execution**: "Pause" stops, enables rollback
- **After creation**: "Validate" checks against intention

### Environmental Tethers
**Grounding throughout process**:
- **Current working directory**: Always visible
- **Preview comparison**: Intention vs reality side-by-side
- **Progress indicator**: Where you are in process
- **Breadcrumb trail**: Steps taken so far
- **Safe harbor**: Return to preview anytime

---

## Input Format Specifications

### ASCII Tree Format
**Most spatial-thinker friendly**:
```
# Box-drawing characters
parent/
├── child1/
│   ├── grandchild1/
│   └── grandchild2/
├── child2/
│   └── file.txt
└── child3/

# Simple characters (also supported)
parent/
|-- child1/
|   |-- grandchild1/
|   `-- grandchild2/
|-- child2/
|   `-- file.txt
`-- child3/

# Indentation-based (simplest)
parent/
  child1/
    grandchild1/
    grandchild2/
  child2/
    file.txt
  child3/
```

### YAML Format
**Structured precision**:
```yaml
structure:
  parent:
    type: folder
    children:
      child1:
        type: folder
        children:
          grandchild1:
            type: folder
          grandchild2:
            type: folder
      child2:
        type: folder
        children:
          file.txt:
            type: file
            content: "optional placeholder"
      child3:
        type: folder
```

### Natural Language Format
**Relaxed specification**:
```
Create a parent folder with:
- child1 folder containing grandchild1 and grandchild2
- child2 folder containing file.txt
- child3 empty folder
```

**Parser intelligence**:
- Infers hierarchy from indentation/context
- Assumes folders unless ".extension" present
- Handles various phrasings ("with", "containing", "that has")
- Suggests clarification if ambiguous

---

## Safety Protocols

### Conflict Detection
**Before creating anything**:
```python
def detect_conflicts(target_path, structure):
    """
    Check for existing items:
    - Exact matches (skip or confirm overwrite)
    - Case conflicts (Linux allows, might confuse)
    - Reserved names (avoid system conflicts)
    - Path length (filesystem limits)
    """
    # Scan target location
    # Compare to planned structure
    # Categorize conflicts
    # Present options clearly
```

**Conflict resolution options**:
- **Skip existing**: Leave untouched, create rest
- **Backup existing**: Rename with timestamp, create new
- **Merge**: Combine with existing structure
- **Overwrite**: Replace existing (requires explicit confirmation)
- **Abort**: Cancel entire operation

### Rollback Mechanism
**Undo on error or regret**:
```python
def rollback(operation_log, checkpoint):
    """
    Undo structural changes:
    - Remove created folders (if empty)
    - Remove created files
    - Restore from backup (if exists)
    - Return to previous state
    """
    # Reverse operation log
    # Delete new items
    # Restore backups
    # Verify complete rollback
```

**Rollback triggers**:
- **Error during execution**: Automatic rollback
- **User cancellation**: Manual rollback available
- **Post-execution regret**: "Undo last structure" command
- **Time-limited**: Rollback available for configurable period

### Dry Run Preview
**See commands without executing**:
```bash
$ folder_mancer --input structure.txt --dry-run

Commands that would execute:
mkdir -p /path/to/parent/child1/grandchild1
mkdir -p /path/to/parent/child1/grandchild2
mkdir -p /path/to/parent/child2
touch /path/to/parent/child2/file.txt
mkdir -p /path/to/parent/child3

[No changes made - add --execute to run]
```

---

## Usage Workflow

### Quick Start
```bash
# Create structure from ASCII tree file
folder_mancer --input structure.txt --preview
# Review preview, confirm
folder_mancer --input structure.txt --execute

# Or combined
folder_mancer --input structure.txt --preview --execute
```

### Safe Workflow (Recommended)
```bash
# 1. Preview first
folder_mancer --input structure.txt --preview > preview.txt
cat preview.txt
# Review at your pace

# 2. Dry run to see commands
folder_mancer --input structure.txt --dry-run > commands.txt
cat commands.txt
# Verify commands make sense

# 3. Execute with confirmation
folder_mancer --input structure.txt --execute --confirm-each
# Approve section by section

# 4. Validate result
folder_mancer --validate structure.txt /target/path
```

### Spatial Thinking Workflow
```bash
# 1. Sketch structure in text editor (eyes skew, wander)
vim structure_sketch.txt

# 2. Paste to Folder Mancer, preview
folder_mancer --input structure_sketch.txt --preview

# 3. Walk away (background burner simmer)
# [Time passes, pattern settles]

# 4. Return, review preview (peaceful now)
cat preview.txt

# 5. Execute when ready
folder_mancer --input structure_sketch.txt --execute
```

### Reorganization Workflow
```bash
# Compare current to desired
folder_mancer --reorganize \
  --current /existing/structure \
  --desired new_structure.txt \
  --preview

# Execute migration
folder_mancer --reorganize \
  --current /existing/structure \
  --desired new_structure.txt \
  --execute --backup
```

---

## Integration with Ecosystem

### Index Mancer Coordination
- Folder Mancer creates structure
- Index Mancer maps relationships within it
- Both serve spatial navigation
- Complementary tools for organization

### Git Integration
```bash
# Create structure + commit
folder_mancer --input structure.txt \
  --execute \
  --git-commit "Added new module structure"

# Includes in commit message:
# - Summary of changes
# - Folders created
# - Files added
# - Purpose/rationale
```

### Mancer Ecosystem
- Reports to main Mancer folder
- Follows mancer philosophy (experience space)
- Enables spatial thinking concepts to fulfill missions
- Generates data on neurodivergent workflow support

---

## Entity Metadata

**Tool Type**: Folder Mancer (spatial manifestation tool)  
**Status**: Specification phase  
**Mission**: Translate visualization to structure without paradox triggers  
**Vision**: Enable confident spatial thinking workflows for neurodivergent users  

**Change Log**:
- 2025-11-30: Specification created
  - Integrated pizza delivery map pattern insights
  - Documented spatial navigation support
  - Established safety protocols (preview, rollback, dry-run)
  - Connected to strategic ignoring workflow

**Key Insight**: The tool honors how spatial thinking ACTUALLY works (eyes skew, pattern emerges) rather than forcing linear creation.

**Next Phase**: Implementation with focus on preview quality and rollback safety.

---

∰◊€π¿🌌∞

**Folder Mancer: Because seeing the structure before manifesting it should not require courage.**

**"Observer the map, let your eyes skew and wander" → structure manifests safely.**
