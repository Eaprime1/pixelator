#!/usr/bin/env python3
"""
File Gatherer - Find & Fix Scattered Restored Files
----------------------------------------------------
Finds files scattered across directories, handles problematic filenames
(spaces, special chars), and gathers them into one location.

One Hertz: Find first, review, then gather in batches
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict

class FileGatherer:
    """Finds scattered files and consolidates them."""

    def __init__(self, search_root, gather_location=None):
        self.search_root = Path(search_root).expanduser()

        if gather_location is None:
            gather_location = Path.cwd() / "gathered_files"
        self.gather_location = Path(gather_location)
        self.gather_location.mkdir(parents=True, exist_ok=True)

        # Problem patterns in filenames
        self.problem_patterns = [
            r'\s',           # Spaces
            r'[()]',         # Parentheses
            r'[\[\]]',       # Brackets
            r'[&]',          # Ampersand
            r"[']",          # Apostrophes
            r'[!@#$%^*+=]'  # Special chars
        ]

        self.stats = {
            'files_found': 0,
            'problem_files': 0,
            'files_gathered': 0,
            'files_renamed': 0
        }

        self.found_files = []

    def has_problem_chars(self, filename):
        """Check if filename has problematic characters."""
        for pattern in self.problem_patterns:
            if re.search(pattern, filename):
                return True
        return False

    def sanitize_filename(self, filename):
        """Clean up problematic filename.

        Rules:
        - Spaces → underscores
        - Remove or replace special chars
        - Keep alphanumeric, dash, underscore, dot
        """
        # Get name and extension
        path = Path(filename)
        stem = path.stem
        suffix = path.suffix

        # Replace spaces with underscores
        stem = stem.replace(' ', '_')

        # Remove parentheses but keep content
        stem = re.sub(r'[()]', '', stem)
        stem = re.sub(r'[\[\]]', '', stem)

        # Remove or replace special chars
        stem = stem.replace('&', 'and')
        stem = stem.replace("'", '')
        stem = re.sub(r'[!@#$%^*+=]', '', stem)

        # Remove consecutive underscores
        stem = re.sub(r'_+', '_', stem)

        # Remove leading/trailing underscores
        stem = stem.strip('_')

        return stem + suffix

    def find_files(self, pattern='*', newer_than=None, limit=None):
        """Find files matching pattern.

        Args:
            pattern: Glob pattern (default: all files)
            newer_than: Only files modified after this date (datetime object)
            limit: Max files to find (for testing)
        """
        print(f"\n🔍 Searching: {self.search_root}")
        print(f"Pattern: {pattern}")
        if newer_than:
            print(f"Modified after: {newer_than}")
        print("-" * 60)

        # Search recursively
        all_files = self.search_root.rglob(pattern)

        for filepath in all_files:
            if not filepath.is_file():
                continue

            # Skip hidden files and git directories
            if any(part.startswith('.') for part in filepath.parts):
                continue

            # Check modification time
            if newer_than:
                mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
                if mtime < newer_than:
                    continue

            self.found_files.append(filepath)
            self.stats['files_found'] += 1

            # Check for problem characters
            if self.has_problem_chars(filepath.name):
                self.stats['problem_files'] += 1

            # Progress
            if self.stats['files_found'] % 50 == 0:
                print(f"Found {self.stats['files_found']} files...", end='\r')

            # Limit for testing
            if limit and self.stats['files_found'] >= limit:
                break

        print(f"Found {self.stats['files_found']} files    ")
        print(f"Files with problem chars: {self.stats['problem_files']}")

        return self.found_files

    def show_samples(self, n=10):
        """Show sample of found files, especially problem ones."""
        print("\n📋 Sample Files Found")
        print("=" * 60)

        # Show problem files first
        problem_files = [f for f in self.found_files if self.has_problem_chars(f.name)]
        regular_files = [f for f in self.found_files if not self.has_problem_chars(f.name)]

        if problem_files:
            print("\n⚠️  Files with problematic names:")
            for f in problem_files[:n]:
                clean_name = self.sanitize_filename(f.name)
                print(f"  {f.name}")
                if clean_name != f.name:
                    print(f"    → {clean_name}")
            if len(problem_files) > n:
                print(f"  ... and {len(problem_files) - n} more")

        if regular_files:
            print(f"\n✓ Sample regular files:")
            for f in regular_files[:5]:
                print(f"  {f.name}")

    def gather_files(self, dry_run=True, rename=True):
        """Gather found files into gather_location.

        Args:
            dry_run: If True, just show what would happen
            rename: If True, sanitize filenames during gather
        """
        print(f"\n{'🔍 DRY RUN - ' if dry_run else '📦 '}Gathering files to: {self.gather_location}")
        print("=" * 60)

        for filepath in self.found_files:
            # Determine destination filename
            if rename and self.has_problem_chars(filepath.name):
                dest_name = self.sanitize_filename(filepath.name)
                self.stats['files_renamed'] += 1
            else:
                dest_name = filepath.name

            dest_path = self.gather_location / dest_name

            # Handle name conflicts
            if dest_path.exists():
                base = dest_path.stem
                ext = dest_path.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = self.gather_location / f"{base}_dup{counter}{ext}"
                    counter += 1

            # Show sample actions
            if self.stats['files_gathered'] < 5:
                print(f"  {filepath.name}")
                if dest_name != filepath.name:
                    print(f"    → {dest_name}")
                print(f"    from: {filepath.parent}")

            if not dry_run:
                try:
                    shutil.copy2(str(filepath), str(dest_path))
                except Exception as e:
                    print(f"⚠️  Error copying {filepath.name}: {e}")
                    continue

            self.stats['files_gathered'] += 1

        if self.stats['files_gathered'] > 5:
            print(f"  ... and {self.stats['files_gathered'] - 5} more files")

    def print_stats(self):
        """Display statistics."""
        print("\n" + "=" * 60)
        print("📊 File Gatherer Statistics")
        print("=" * 60)
        print(f"Files found:        {self.stats['files_found']:6d}")
        print(f"Problem filenames:  {self.stats['problem_files']:6d}")
        print(f"Files gathered:     {self.stats['files_gathered']:6d}")
        print(f"Files renamed:      {self.stats['files_renamed']:6d}")
        print("=" * 60)


def main():
    """Main execution - find recently restored files."""
    import sys
    from datetime import timedelta

    print("📦 File Gatherer - Find & Fix Scattered Files")
    print("=" * 60)

    # Default: search from home directory
    if len(sys.argv) > 1:
        search_root = sys.argv[1]
    else:
        search_root = "~"

    # Look for files modified in last 24 hours (recently restored)
    recent_cutoff = datetime.now() - timedelta(hours=24)

    print(f"\n🎯 Strategy: Find files modified in last 24 hours")
    print(f"(Assumes trash was just restored)")

    # Create gatherer
    gatherer = FileGatherer(
        search_root=search_root,
        gather_location="./gathered_files"
    )

    # ONE HERTZ: Find first 100 files
    print("\n🐌 One Hertz Mode: Finding first 100 recent files...")
    files = gatherer.find_files(
        pattern='*',
        newer_than=recent_cutoff,
        limit=100
    )

    if not files:
        print("\n⚠️  No recently modified files found")
        print("Try:")
        print("  - Increasing time window (modify recent_cutoff)")
        print("  - Different search pattern")
        print("  - Manual path specification")
        return

    # Show samples
    gatherer.show_samples(n=10)

    # Dry run gather
    gatherer.gather_files(dry_run=True, rename=True)

    gatherer.print_stats()

    print("\n✅ DRY RUN COMPLETE - No files were copied")
    print("\nNext steps:")
    print("1. Review the samples above")
    print("2. Check if filename cleaning looks good")
    print("3. Run with dry_run=False to actually gather")
    print("\nTo gather for real:")
    print("  gatherer.gather_files(dry_run=False)")


if __name__ == "__main__":
    main()
