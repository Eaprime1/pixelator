"""
Henry CLASS Detectors — A through E
Each detector takes filepath + content, returns list of Issue objects.
Never modifies files.

CLASS A : Whitespace
CLASS B : Symbols & Filenames
CLASS C : Titles & Messages
CLASS D : Git-Specific
CLASS E : Structural
"""

import os
from dataclasses import dataclass, field
from typing import List, Optional


# Symbols that cause shell/git problems in filenames
PROBLEM_FILENAME_CHARS = set('&?#%!@()[]{}^`~|<>;,\'"\\')

# Consciousness symbols — flag for review, never auto-remove
CONSCIOUSNESS_SYMBOLS = set('∰◊€π¿🌌∞₿§♪℞')

# Files larger than this should use git-lfs or be excluded
LARGE_FILE_BYTES = 50 * 1024 * 1024  # 50 MB


@dataclass
class Issue:
    """A single detected hygiene issue"""
    issue_class  : str            # A, B, C, D, or E
    issue_type   : str            # e.g. trailing_space
    filepath     : str
    line_number  : Optional[int]  # None if whole-file issue
    detail       : str
    severity     : str = "WARN"   # INFO | WARN | ERROR
    auto_fixable : bool = False


# ── CLASS A : WHITESPACE ──────────────────────────────────────────────────────

def detect_trailing_spaces(filepath: str, content: str) -> List[Issue]:
    issues = []
    for i, line in enumerate(content.split("\n"), 1):
        if line != line.rstrip():
            issues.append(Issue(
                issue_class  = "A",
                issue_type   = "trailing_space",
                filepath     = filepath,
                line_number  = i,
                detail       = f"Trailing whitespace: {repr(line[-6:])}",
                severity     = "WARN",
                auto_fixable = True,
            ))
    return issues


def detect_crlf(filepath: str, raw: bytes) -> List[Issue]:
    count = raw.count(b"\r\n")
    if count:
        return [Issue(
            issue_class  = "A",
            issue_type   = "crlf_endings",
            filepath     = filepath,
            line_number  = None,
            detail       = f"Windows CRLF line endings: {count} occurrences",
            severity     = "WARN",
            auto_fixable = True,
        )]
    return []


def detect_trailing_newline(filepath: str, raw: bytes) -> List[Issue]:
    if not raw:
        return []
    if not raw.endswith(b"\n"):
        return [Issue(
            issue_class  = "A",
            issue_type   = "missing_final_newline",
            filepath     = filepath,
            line_number  = None,
            detail       = "File does not end with a newline",
            severity     = "INFO",
            auto_fixable = True,
        )]
    if raw.endswith(b"\n\n"):
        return [Issue(
            issue_class  = "A",
            issue_type   = "extra_final_newlines",
            filepath     = filepath,
            line_number  = None,
            detail       = "File ends with multiple blank newlines",
            severity     = "INFO",
            auto_fixable = True,
        )]
    return []


def detect_mixed_indent(filepath: str, content: str) -> List[Issue]:
    has_tab   = any(l.startswith("\t")    for l in content.splitlines())
    has_space = any(l.startswith("    ")  for l in content.splitlines())
    if has_tab and has_space:
        return [Issue(
            issue_class  = "A",
            issue_type   = "mixed_indentation",
            filepath     = filepath,
            line_number  = None,
            detail       = "Mixed tab and space indentation detected",
            severity     = "WARN",
            auto_fixable = False,
        )]
    return []


# ── CLASS B : SYMBOLS & FILENAMES ────────────────────────────────────────────

def detect_filename_spaces(filepath: str) -> List[Issue]:
    name = os.path.basename(filepath)
    if " " in name:
        return [Issue(
            issue_class  = "B",
            issue_type   = "filename_spaces",
            filepath     = filepath,
            line_number  = None,
            detail       = f"Spaces in filename: '{name}'",
            severity     = "WARN",
            auto_fixable = True,
        )]
    return []


def detect_filename_symbols(filepath: str) -> List[Issue]:
    name  = os.path.basename(filepath)
    found = [c for c in name if c in PROBLEM_FILENAME_CHARS]
    if found:
        return [Issue(
            issue_class  = "B",
            issue_type   = "filename_problem_chars",
            filepath     = filepath,
            line_number  = None,
            detail       = f"Problematic chars in filename: {found}",
            severity     = "ERROR",
            auto_fixable = False,
        )]
    return []


def detect_consciousness_symbols(filepath: str, content: str) -> List[Issue]:
    """Flag consciousness symbols for review — DO NOT auto-remove."""
    found = list(set(c for c in content if c in CONSCIOUSNESS_SYMBOLS))
    if found:
        return [Issue(
            issue_class  = "B",
            issue_type   = "consciousness_symbols",
            filepath     = filepath,
            line_number  = None,
            detail       = f"Consciousness symbols present (REVIEW ONLY — do not remove): {found}",
            severity     = "INFO",
            auto_fixable = False,
        )]
    return []


# ── CLASS C : TITLES ──────────────────────────────────────────────────────────

def detect_long_h1(filepath: str, content: str) -> List[Issue]:
    issues = []
    for i, line in enumerate(content.splitlines(), 1):
        if line.startswith("# "):
            title = line[2:].strip()
            if len(title) > 80:
                issues.append(Issue(
                    issue_class  = "C",
                    issue_type   = "h1_too_long",
                    filepath     = filepath,
                    line_number  = i,
                    detail       = f"H1 is {len(title)} chars (max 80): '{title[:50]}...'",
                    severity     = "WARN",
                    auto_fixable = False,
                ))
    return issues


def detect_title_whitespace(filepath: str, content: str) -> List[Issue]:
    issues = []
    for i, line in enumerate(content.splitlines(), 1):
        if line.startswith("#"):
            parts = line.split(" ", 1)
            if len(parts) > 1:
                text = parts[1]
                if text != text.strip() or "  " in text:
                    issues.append(Issue(
                        issue_class  = "C",
                        issue_type   = "title_whitespace",
                        filepath     = filepath,
                        line_number  = i,
                        detail       = f"Title has extra whitespace: {repr(text[:40])}",
                        severity     = "INFO",
                        auto_fixable = True,
                    ))
    return issues


# ── CLASS D : GIT-SPECIFIC ────────────────────────────────────────────────────

def detect_large_file(filepath: str) -> List[Issue]:
    try:
        size = os.path.getsize(filepath)
        if size > LARGE_FILE_BYTES:
            return [Issue(
                issue_class  = "D",
                issue_type   = "large_file",
                filepath     = filepath,
                line_number  = None,
                detail       = f"File is {size/(1024*1024):.1f} MB — exceeds 50 MB git threshold",
                severity     = "ERROR",
                auto_fixable = False,
            )]
    except OSError:
        pass
    return []


# ── CLASS E : STRUCTURAL ──────────────────────────────────────────────────────

def detect_deep_path(filepath: str, base_path: str, max_depth: int = 8) -> List[Issue]:
    rel   = os.path.relpath(filepath, base_path)
    depth = len(rel.split(os.sep))
    if depth > max_depth:
        return [Issue(
            issue_class  = "E",
            issue_type   = "deep_path",
            filepath     = filepath,
            line_number  = None,
            detail       = f"Path depth {depth} exceeds {max_depth}: {rel}",
            severity     = "WARN",
            auto_fixable = False,
        )]
    return []
