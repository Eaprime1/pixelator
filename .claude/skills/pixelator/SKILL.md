```markdown
# pixelator Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the development patterns and coding conventions used in the `pixelator` repository, a Python-based project with no detected framework. You'll learn how to structure files, write imports and exports, and follow the repository's testing and commit practices. This guide also provides command suggestions for common workflows.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `image_processor.py`, `pixel_utils.py`

### Import Style
- Use **relative imports** within the codebase.
  - Example:
    ```python
    from .utils import resize_image
    ```

### Export Style
- Use **named exports** (explicitly listing what is exported from a module).
  - Example:
    ```python
    __all__ = ['resize_image', 'Pixelator']
    ```

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
3. Use relative imports to reference other modules.
4. Add named exports via `__all__` if necessary.
5. Write corresponding tests in a `*.test.*` file.

### Running Tests
**Trigger:** When you want to verify code correctness.
**Command:** `/run-tests`

1. Locate test files matching the `*.test.*` pattern.
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

- Test files follow the `*.test.*` naming pattern.
  - Example: `image_processor.test.py`
- The specific test framework is **unknown**; use your preferred Python test runner (e.g., `pytest`, `unittest`).
- Place tests alongside or near the modules they test.

## Commands
| Command         | Purpose                                 |
|-----------------|-----------------------------------------|
| /add-module     | Scaffold and add a new module           |
| /run-tests      | Run all test files in the repository    |
| /commit-changes | Commit your staged changes              |
```
