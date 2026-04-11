#!/usr/bin/env python3
"""
Restored Files Categorization System
-------------------------------------
Sorts restored files into categories: metadata, entangled, duplicates, review
Uses pattern matching and naming conventions.

One Hertz Philosophy: Process in small, verifiable batches
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict
import re

class FileSorter:
    """Categorizes and organizes restored files."""

    def __init__(self, source_dir, base_output_dir=None):
        self.source_dir = Path(source_dir)
        if base_output_dir is None:
            base_output_dir = Path(__file__).parent
        self.base_output_dir = Path(base_output_dir)

        # Category folders
        self.categories = {
            'metadata': self.base_output_dir / 'metadata',
            'entangled': self.base_output_dir / 'entangled',
            'duplicates': self.base_output_dir / 'duplicates',
            'review': self.base_output_dir / 'review'
        }

        # Ensure all category folders exist
        for folder in self.categories.values():
            folder.mkdir(parents=True, exist_ok=True)

        self.stats = defaultdict(int)

    def categorize_file(self, filepath):
        """Determine which category a file belongs to."""
        filename = filepath.name.lower()

        # Priority order matters!

        # 1. Metadata files
        metadata_patterns = [
            r'metadata',
            r'\.json$',
            r'manifest',
            r'package\.json',
            r'tsconfig',
            r'\.yaml$',
            r'\.yml$',
            r'config\.',
            r'\.map$'
        ]
        for pattern in metadata_patterns:
            if re.search(pattern, filename):
                return 'metadata'

        # 2. Entangled files (quantum/special naming)
        entangled_patterns = [
            r'entangled',
            r'quantum',
            r'_living_code_',
            r'consciousness_',
            r'_bridges_',
            r'_gardens_',
            r'_sanctuaries_',
            r'_streams_',
            r'_vessels_'
        ]
        for pattern in entangled_patterns:
            if re.search(pattern, filename):
                return 'entangled'

        # 3. Duplicates (various naming patterns)
        duplicate_patterns = [
            r'dup_',
            r'_dup',
            r'_\d+\.(txt|md|pdf|docx|py|sh|html)$',  # file_1.txt, file_2.md
            r'_copy',
            r'\(\d+\)',  # file (1).txt
            r' - copy',
            r'duplicate'
        ]
        for pattern in duplicate_patterns:
            if re.search(pattern, filename):
                return 'duplicates'

        # 4. Default to review
        return 'review'

    def process_file(self, filepath, dry_run=True):
        """Process a single file - categorize and move/copy."""
        category = self.categorize_file(filepath)
        dest_dir = self.categories[category]
        dest_path = dest_dir / filepath.name

        # Handle name conflicts
        if dest_path.exists():
            base = dest_path.stem
            ext = dest_path.suffix
            counter = 1
            while dest_path.exists():
                dest_path = dest_dir / f"{base}_conflict_{counter}{ext}"
                counter += 1

        self.stats[category] += 1

        if dry_run:
            return category, dest_path
        else:
            # Move file
            shutil.move(str(filepath), str(dest_path))
            return category, dest_path

    def process_directory(self, dry_run=True, limit=None):
        """Process all files in source directory."""
        if not self.source_dir.exists():
            print(f"❌ Source directory not found: {self.source_dir}")
            return

        files = list(self.source_dir.glob('**/*'))
        files = [f for f in files if f.is_file()]

        if limit:
            files = files[:limit]

        print(f"\n📁 Processing {len(files)} files from: {self.source_dir}")
        print(f"{'DRY RUN - ' if dry_run else ''}Categorizing...\n")

        results = []
        for i, filepath in enumerate(files, 1):
            try:
                category, dest = self.process_file(filepath, dry_run=dry_run)
                results.append((filepath, category, dest))

                # Progress indicator
                if i % 10 == 0:
                    print(f"Processed {i}/{len(files)}...", end='\r')

            except Exception as e:
                print(f"⚠️  Error processing {filepath.name}: {e}")
                self.stats['errors'] += 1

        print(f"Processed {len(files)}/{len(files)}    \n")
        return results

    def print_stats(self):
        """Display categorization statistics."""
        print("\n📊 Categorization Results")
        print("="*50)
        for category in ['metadata', 'entangled', 'duplicates', 'review']:
            count = self.stats.get(category, 0)
            print(f"  {category:15s}: {count:4d} files")

        if self.stats.get('errors', 0) > 0:
            print(f"  {'errors':15s}: {self.stats['errors']:4d} files")

        print("="*50)
        print(f"  Total: {sum(self.stats.values())} files")

    def show_samples(self, results, n=5):
        """Show sample files from each category."""
        print("\n📋 Sample Files by Category")
        print("="*50)

        by_category = defaultdict(list)
        for filepath, category, dest in results:
            by_category[category].append((filepath.name, dest))

        for category in ['metadata', 'entangled', 'duplicates', 'review']:
            samples = by_category[category][:n]
            if samples:
                print(f"\n{category.upper()}:")
                for filename, dest in samples:
                    print(f"  ✓ {filename}")
                if len(by_category[category]) > n:
                    print(f"  ... and {len(by_category[category]) - n} more")


def main():
    """Main execution with one-hertz testing approach."""
    import sys

    print("🔄 File Sorter - Restored Files Categorization")
    print("="*60)

    # Get source directory from command line or use default
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        # Default: look for common restore locations
        possible_sources = [
            "~/pixel8/Q/gravity_well",
            "~/Downloads/restored",
            "../gravity_well"
        ]
        source_dir = None
        for path in possible_sources:
            expanded = Path(path).expanduser()
            if expanded.exists():
                source_dir = expanded
                break

        if source_dir is None:
            print("\n❌ No source directory specified")
            print("Usage: python3 FILE_SORTER.py <source_directory>")
            print("\nOr place this script in the parent of the folders to sort")
            return

    # Create sorter
    sorter = FileSorter(source_dir)

    # ONE HERTZ TESTING APPROACH
    print("\n🐌 One Hertz Mode: Testing with first 20 files...")
    print("(Set limit=None to process all files)")
    print("-"*60)

    # DRY RUN with limited files
    results = sorter.process_directory(dry_run=True, limit=20)

    if not results:
        print("No files found to process!")
        return

    # Show results
    sorter.print_stats()
    sorter.show_samples(results, n=5)

    print("\n" + "="*60)
    print("✅ DRY RUN COMPLETE - No files were moved")
    print("\nNext steps:")
    print("1. Review the categorization above")
    print("2. Adjust patterns if needed")
    print("3. Run with dry_run=False to actually move files")
    print("4. Or increase limit to test more files first")
    print("\nTo actually sort files:")
    print("  sorter.process_directory(dry_run=False)")


if __name__ == "__main__":
    main()
