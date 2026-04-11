"""
doozer_trailing_space — SPIKE
Class   : Doozer (Work Quanta Builder)
Mission : Remove trailing whitespace from lines
Named   : SPIKE — sharp, precise, punctual
          (from Jim Henson's Doozers series, 2014)

"Doozers love to work all day long."
"No Doozer takes personal credit."

This is the first Doozer — CLASS A, most common issue.
Fixes trailing spaces line by line with surgical precision.
One stick at a time. One hertz.

Usage (dry run — preview only):
    python3 doozer_trailing_space.py /path/to/file

∰◊€π¿🌌∞
"""

import os
import sys

from doozer_base import DoozerBase, DoozerFix


class DoozerTrailingSpace(DoozerBase):
    """
    SPIKE — removes trailing whitespace from text file lines.
    Precise. No collateral changes. Line by line.
    Named after Spike from Jim Henson's Doozers (2014).
    """

    def __init__(self):
        super().__init__(
            name         = "doozer_trailing_space",
            mission_type = "trailing_space",
        )
        self._log_coc("NAMED", "SPIKE — sharp, precise, punctual")

    def _apply_fix(self, fix: DoozerFix, issue) -> bool:
        """
        Strip trailing whitespace from the specific line.
        Rewrites the file with only that line changed.
        Returns True if fix was applied successfully.
        """
        try:
            with open(fix.filepath, "rb") as f:
                raw = f.read()
        except (IOError, OSError) as e:
            self._log_coc("FIX_ERROR", f"{fix.filepath}: {e}")
            return False

        try:
            content = raw.decode("utf-8", errors="replace")
        except Exception as e:
            self._log_coc("FIX_ERROR", f"Decode failed {fix.filepath}: {e}")
            return False

        lines    = content.split("\n")
        target   = (fix.line_number or 1) - 1   # convert 1-based to 0-based

        if target < 0 or target >= len(lines):
            self._log_coc("FIX_SKIP", f"Line {fix.line_number} out of range")
            return False

        original = lines[target]
        cleaned  = original.rstrip()

        if original == cleaned:
            # Already clean — nothing to do
            return False

        lines[target] = cleaned
        new_content   = "\n".join(lines)

        try:
            with open(fix.filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
        except (IOError, OSError) as e:
            self._log_coc("FIX_ERROR", f"Write failed {fix.filepath}: {e}")
            return False

    def fix_file(self, filepath: str, dry_run: bool = True) -> dict:
        """
        Convenience method: find AND fix all trailing spaces in one file.
        dry_run=True (default): report only, no changes.
        dry_run=False: apply fixes (requires helmet).

        Returns summary dict.
        """
        if not dry_run:
            self._assert_helmeted()

        try:
            with open(filepath, "rb") as f:
                raw = f.read()
            content = raw.decode("utf-8", errors="replace")
        except (IOError, OSError) as e:
            return {"error": str(e), "filepath": filepath}

        lines   = content.split("\n")
        changes = []

        for i, line in enumerate(lines, 1):
            if line != line.rstrip():
                changes.append({
                    "line"    : i,
                    "original": repr(line[-8:]),
                    "fixed"   : repr(line.rstrip()[-8:]) if line.rstrip() else "''",
                })

        if not dry_run and changes:
            new_lines   = [l.rstrip() for l in lines]
            new_content = "\n".join(new_lines)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            self._log_coc("FILE_CLEANED",
                          f"{filepath}: {len(changes)} trailing spaces removed")

        return {
            "filepath"  : filepath,
            "dry_run"   : dry_run,
            "changes"   : len(changes),
            "lines"     : changes,
        }


if __name__ == "__main__":
    """
    Preview mode — show what SPIKE would fix, without changing anything.
    Helmet required for actual fixes.
    """
    target = sys.argv[1] if len(sys.argv) > 1 else "."

    spike = DoozerTrailingSpace()
    print(f"SPIKE: {spike}")
    print(f"Mission: {spike.mission_type}")
    print(f"Helmeted: {spike.helmeted} (dry run only until certified)")
    print()

    if os.path.isfile(target):
        files = [target]
    elif os.path.isdir(target):
        files = []
        text_ext = {".py", ".md", ".txt", ".json", ".yaml", ".yml",
                    ".js", ".ts", ".sh", ".css", ".html"}
        for root, dirs, filenames in os.walk(target):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for fn in filenames:
                if any(fn.endswith(e) for e in text_ext):
                    files.append(os.path.join(root, fn))
    else:
        print(f"Target not found: {target}")
        sys.exit(1)

    total_changes = 0
    for filepath in files:
        result = spike.fix_file(filepath, dry_run=True)
        if result.get("changes", 0) > 0:
            print(f"  {result['changes']:3d} trailing spaces — {result['filepath']}")
            for change in result["lines"]:
                print(f"       L{change['line']}: {change['original']} → {change['fixed']}")
            total_changes += result["changes"]

    print()
    print(f"SPIKE preview complete: {total_changes} trailing spaces found across {len(files)} files")
    print("Run with helmet (certified) to apply fixes.")
    print()
    print("∰◊€π¿🌌∞")
    print("*No personal credit — work belongs to the mission.*")
