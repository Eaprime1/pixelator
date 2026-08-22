# pixelator Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the development patterns and coding conventions used in the `pixelator` repository: a flat-layout Python automation tool (`pixelator_agent.py`, `pixelator_config.py`) paired with Termux/Android shell scripts (`pixelator_automate.sh`, `termux_proc.sh`) for file routing and queue management. You'll learn how to structure files, write imports, and follow the repository's testing and commit practices. This guide also provides command suggestions for common workflows.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `pixelator_agent.py`, `pixelator_config.py`

### Import Style
- Use **absolute imports** of sibling modules — this is a flat script layout, not a package with subpackages.
  - Example:
    ```python
    import pixelator_config as cfg
    ```

### Export Style
- No `__all__` or explicit export list convention is used anywhere in this codebase; modules are imported and used directly by name.

### Commit Patterns
- Commit messages are **freeform** (no enforced prefixes).
- Typical message length: ~20 characters.
  - Example: `fix pixelation bug`

## Workflows

### Adding a New Module
**Trigger:** When you need to add new functionality.
**Command:** `/add-module`

1. Create a new Python file using snake_case naming.
2. Implement your functionality.
3. Use absolute imports to reference sibling modules (e.g. `import pixelator_config as cfg`).
4. Write corresponding tests in a `test_*.py` file.

### Running Tests
**Trigger:** When you want to verify code correctness.
**Command:** `/run-tests`

1. Locate test files matching the `test_*.py` pattern.
2. Run tests using your preferred Python test runner (framework is unspecified).
   - Example with `pytest`:
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

- Test files follow the `test_*.py` naming pattern.
  - Example: `test_sample.py`
- The specific test framework is unknown; use your preferred Python test runner (e.g., pytest, unittest).
- Tests currently live at the repo root, not in a separate `tests/` directory.

## Commands
| Command         | Purpose                                 |
|-----------------|-----------------------------------------|
| /add-module     | Scaffold and add a new module           |
| /run-tests      | Run all test files in the repository    |
| /commit-changes | Commit your staged changes              |
