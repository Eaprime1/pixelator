# pixelator Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill captures practical patterns for the `pixelator` repository, which is primarily a Termux/Bash workflow (`termux_proc.sh`) with lightweight Python test coverage (`test_sample.py`). Use it to keep script changes consistent and run quick validation before commits.

## Coding Conventions

### File Naming
- Use **snake_case** for script and Python file names.
  - Example: `termux_proc.sh`, `test_sample.py`

### Shell Script Style
- Keep menu options and prompts clear and stable in `termux_proc.sh`.
- Prefer straightforward Bash flow (`case`, `if`, `echo`, `read`) over unnecessary abstraction.

### Test Naming
- Use pytest-discoverable `test_*.py` naming.
  - Example: `test_sample.py`

### Commit Patterns
- Commit messages are **freeform** (no enforced prefixes).
- Typical message length: ~20 characters.
  - Example: `fix menu cert output`

## Workflows

### Updating the Procedure Script
**Trigger:** When changing mobile workflow behavior.
**Command:** `/update-script`

1. Update `termux_proc.sh` with minimal, focused edits.
2. Preserve option numbering and output format compatibility where possible.
3. Verify the script still supports start/resume, completion cert output, and log visibility.

### Running Tests
**Trigger:** When you want to verify code correctness.
**Command:** `/run-tests`

1. Run pytest from the repository root:
   ```
   pytest
   ```

### Committing Changes
**Trigger:** When you have changes ready to save.
**Command:** `/commit-changes`

1. Write a concise, freeform commit message (~20 chars recommended).
2. Commit your changes.
   - Example:
     ```
     git commit -m "add blur filter"
     ```

## Testing Patterns

- Test files follow pytest-style `test_*.py` naming.
- Current tests are root-level (for example, `test_sample.py`).
- Use `pytest` for validation.

## Commands
| Command         | Purpose                                 |
|-----------------|-----------------------------------------|
| /update-script  | Update `termux_proc.sh` behavior safely |
| /run-tests      | Run all test files in the repository    |
| /commit-changes | Commit your staged changes              |
