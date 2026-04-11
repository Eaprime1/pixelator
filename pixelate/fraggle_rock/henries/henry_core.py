"""
henry_core — GitHub Hygiene Henry
Scans git repositories for CLASS A-E hygiene issues.
Reports only. Never modifies files.

Usage:
    python3 henry_core.py /path/to/repo
"""

import os
import sys

from henry_base import HenryBase, now_stamp
from henry_classes import (
    detect_trailing_spaces, detect_crlf, detect_trailing_newline,
    detect_mixed_indent, detect_filename_spaces, detect_filename_symbols,
    detect_consciousness_symbols, detect_long_h1, detect_title_whitespace,
    detect_large_file, detect_deep_path, Issue,
)
from henry_report import HenryReport


TEXT_EXTENSIONS = {
    ".py", ".md", ".txt", ".json", ".yaml", ".yml",
    ".js", ".ts", ".sh", ".css", ".html", ".toml",
    ".cfg", ".ini", ".rst", ".gitignore",
}

SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    ".archive", "no_sync_private", "_.archive",
}


class HenryGithubHygiene(HenryBase):
    """
    Henry entity — GitHub hygiene scanner.
    Detects CLASS A-E issues across all files in a repository.
    Read-only. Conservation bias. One hertz.
    """

    ENTITY_NATURE = "GitHub Hygiene Scanner"

    def __init__(self):
        super().__init__(
            name   = "henry_github_hygiene",
            domain = "github_repositories",
        )

    def scan(self, target_path: str) -> HenryReport:
        """Scan target directory for all hygiene issues. Returns HenryReport."""
        target_path = os.path.abspath(target_path)
        timestamp   = now_stamp()

        report = HenryReport(
            entity_name = self.name,
            target_path = target_path,
            timestamp   = timestamp,
        )

        self._log_coc("SCAN_START", f"Target: {target_path}")

        for root, dirs, files in os.walk(target_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for filename in files:
                filepath = os.path.join(root, filename)
                self._scan_file(filepath, target_path, report)

        # CLASS E: README check at repo root
        if not os.path.exists(os.path.join(target_path, "README.md")):
            report.add_issue(Issue(
                issue_class  = "E",
                issue_type   = "missing_readme",
                filepath     = target_path,
                line_number  = None,
                detail       = "No README.md found in repository root",
                severity     = "WARN",
                auto_fixable = False,
            ))

        self._log_coc(
            "SCAN_COMPLETE",
            f"Files: {report.files_scanned} scanned, "
            f"{report.files_skipped} skipped, "
            f"{len(report.issues)} issues found",
        )
        report.coc_entries = self.get_coc()
        return report

    def _scan_file(self, filepath: str, base_path: str, report: HenryReport):
        """Scan one file. CLASS B + D always; CLASS A + C only for text files."""

        # CLASS B — filename checks (all files)
        report.issues.extend(detect_filename_spaces(filepath))
        report.issues.extend(detect_filename_symbols(filepath))

        # CLASS D — size check (all files)
        report.issues.extend(detect_large_file(filepath))

        # CLASS E — depth check (all files)
        report.issues.extend(detect_deep_path(filepath, base_path))

        ext = os.path.splitext(filepath)[1].lower()
        if ext not in TEXT_EXTENSIONS:
            report.files_skipped += 1
            return

        report.files_scanned += 1

        try:
            with open(filepath, "rb") as f:
                raw = f.read()
        except (IOError, OSError):
            return

        # CLASS A — byte-level checks
        report.issues.extend(detect_crlf(filepath, raw))
        report.issues.extend(detect_trailing_newline(filepath, raw))

        try:
            content = raw.decode("utf-8", errors="replace")
        except Exception:
            return

        # CLASS A — text-level checks
        report.issues.extend(detect_trailing_spaces(filepath, content))
        report.issues.extend(detect_mixed_indent(filepath, content))

        # CLASS B — consciousness symbols (text files)
        report.issues.extend(detect_consciousness_symbols(filepath, content))

        # CLASS C — titles (markup files only)
        if ext in {".md", ".rst", ".txt"}:
            report.issues.extend(detect_long_h1(filepath, content))
            report.issues.extend(detect_title_whitespace(filepath, content))


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    henry  = HenryGithubHygiene()
    print(f"Henry: {henry}")
    print()
    report = henry.scan(target)
    print(report.to_markdown())
