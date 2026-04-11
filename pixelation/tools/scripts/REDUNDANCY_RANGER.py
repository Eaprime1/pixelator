#!/usr/bin/env python3
"""
Redundancy Ranger - Gravity Well Training Edition
--------------------------------------------------
Finds duplicate files, designates prime + shadows, adds count to prime's title.

Philosophy:
- Ranger finds 6 duplicates of same file
- Prime duplicate stays (gets count added to title: "file_6")
- Others become shadows (marked for removal)
- Prime goes to gravity well queue

One Hertz: Process in small, verifiable batches
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict
import shutil
import json
from datetime import datetime

class RedundancyRanger:
    """Hunts duplicates, marks prime, shadows the rest."""

    def __init__(self, source_dir, gravity_well_queue=None):
        self.source_dir = Path(source_dir)

        if gravity_well_queue is None:
            # Default gravity well queue location
            self.gravity_well_queue = self.source_dir.parent / "gravity_well_queue"
        else:
            self.gravity_well_queue = Path(gravity_well_queue)

        self.gravity_well_queue.mkdir(parents=True, exist_ok=True)

        # Shadow holding area
        self.shadow_realm = self.source_dir.parent / "shadow_realm"
        self.shadow_realm.mkdir(parents=True, exist_ok=True)

        self.duplicates = defaultdict(list)
        self.stats = {
            'files_scanned': 0,
            'duplicate_groups': 0,
            'primes_designated': 0,
            'shadows_marked': 0,
            'bytes_saved': 0
        }

    def calculate_hash(self, filepath, chunk_size=8192):
        """Calculate MD5 hash of file."""
        md5 = hashlib.md5()
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(chunk_size):
                    md5.update(chunk)
            return md5.hexdigest()
        except Exception as e:
            print(f"⚠️  Error hashing {filepath.name}: {e}")
            return None

    def scan_for_duplicates(self):
        """Scan directory and group duplicate files by hash."""
        print(f"\n🔍 Scanning: {self.source_dir}")
        print("-" * 60)

        files = [f for f in self.source_dir.rglob('*') if f.is_file()]

        for filepath in files:
            self.stats['files_scanned'] += 1

            file_hash = self.calculate_hash(filepath)
            if file_hash:
                self.duplicates[file_hash].append(filepath)

            # Progress indicator
            if self.stats['files_scanned'] % 10 == 0:
                print(f"Scanned {self.stats['files_scanned']} files...", end='\r')

        print(f"Scanned {self.stats['files_scanned']} files    ")

        # Filter to only groups with duplicates
        self.duplicates = {
            h: files for h, files in self.duplicates.items()
            if len(files) > 1
        }

        self.stats['duplicate_groups'] = len(self.duplicates)
        print(f"✓ Found {self.stats['duplicate_groups']} groups of duplicates")

    def select_prime(self, duplicate_group):
        """Select which file is the prime (keeper) from a duplicate group.

        Priority:
        1. Shortest filename (likely original)
        2. No numeric suffixes (_1, _2, etc)
        3. Oldest file (by modification time)
        """
        # Sort by filename length, then by mtime
        sorted_files = sorted(
            duplicate_group,
            key=lambda f: (
                len(f.name),  # Shorter names first
                '_' not in f.stem,  # Files without underscores first
                -f.stat().st_mtime  # Older files first (negative for descending)
            )
        )
        return sorted_files[0]

    def process_duplicate_group(self, file_hash, duplicate_group, dry_run=True):
        """Process a group of duplicates: designate prime, shadow the rest.

        Returns: (prime_file, shadow_files, count)
        """
        count = len(duplicate_group)

        # Select prime
        prime = self.select_prime(duplicate_group)
        shadows = [f for f in duplicate_group if f != prime]

        # Calculate bytes saved
        if shadows:
            shadow_size = sum(f.stat().st_size for f in shadows)
            self.stats['bytes_saved'] += shadow_size

        if not dry_run:
            # Rename prime with count
            prime_new_name = self.add_count_to_filename(prime, count)
            prime_new_path = prime.parent / prime_new_name

            # Handle conflicts
            if prime_new_path.exists() and prime_new_path != prime:
                print(f"⚠️  Prime rename conflict: {prime_new_name}")
                prime_new_path = prime  # Keep original if conflict
            else:
                prime.rename(prime_new_path)
                prime = prime_new_path

            # Move prime to gravity well queue
            self.queue_for_gravity_well(prime)

            # Move shadows to shadow realm
            for shadow in shadows:
                self.banish_to_shadow(shadow)

        self.stats['primes_designated'] += 1
        self.stats['shadows_marked'] += len(shadows)

        return prime, shadows, count

    def add_count_to_filename(self, filepath, count):
        """Add count to end of filename before extension.

        Example: "document.txt" + count=6 -> "document_6.txt"
        """
        stem = filepath.stem
        suffix = filepath.suffix

        # Remove existing count if present
        if '_' in stem and stem.split('_')[-1].isdigit():
            parts = stem.rsplit('_', 1)
            stem = parts[0]

        return f"{stem}_{count}{suffix}"

    def queue_for_gravity_well(self, filepath):
        """Move prime file to gravity well queue."""
        dest = self.gravity_well_queue / filepath.name

        # Handle name conflicts
        if dest.exists():
            base = dest.stem
            ext = dest.suffix
            counter = 1
            while dest.exists():
                dest = self.gravity_well_queue / f"{base}_q{counter}{ext}"
                counter += 1

        shutil.move(str(filepath), str(dest))
        return dest

    def banish_to_shadow(self, filepath):
        """Move shadow file to shadow realm."""
        dest = self.shadow_realm / filepath.name

        # Handle name conflicts
        if dest.exists():
            base = dest.stem
            ext = dest.suffix
            counter = 1
            while dest.exists():
                dest = self.shadow_realm / f"{base}_shadow{counter}{ext}"
                counter += 1

        shutil.move(str(filepath), str(dest))
        return dest

    def process_all_duplicates(self, dry_run=True, limit=None):
        """Process all duplicate groups."""
        print(f"\n{'🔍 DRY RUN - ' if dry_run else '⚡ PROCESSING '}Duplicate Groups")
        print("=" * 60)

        results = []
        groups_processed = 0

        for file_hash, duplicate_group in list(self.duplicates.items())[:limit]:
            groups_processed += 1
            prime, shadows, count = self.process_duplicate_group(
                file_hash, duplicate_group, dry_run=dry_run
            )
            results.append({
                'prime': prime,
                'shadows': shadows,
                'count': count,
                'hash': file_hash
            })

            # Show sample
            if groups_processed <= 5:
                print(f"\nGroup {groups_processed}: {count} duplicates")
                print(f"  ✓ Prime: {prime.name}")
                for shadow in shadows[:3]:
                    print(f"  ○ Shadow: {shadow.name}")
                if len(shadows) > 3:
                    print(f"  ... and {len(shadows) - 3} more shadows")

        if groups_processed > 5:
            print(f"\n... processed {groups_processed - 5} more groups")

        return results

    def save_report(self, results, output_file="redundancy_report.json"):
        """Save processing report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'source_dir': str(self.source_dir),
            'gravity_well_queue': str(self.gravity_well_queue),
            'shadow_realm': str(self.shadow_realm),
            'stats': self.stats,
            'duplicate_groups': [
                {
                    'prime': str(r['prime']),
                    'shadows': [str(s) for s in r['shadows']],
                    'count': r['count'],
                    'hash': r['hash']
                }
                for r in results
            ]
        }

        output_path = Path(output_file)
        with open(output_path, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n📄 Report saved: {output_path}")
        return output_path

    def print_stats(self):
        """Display statistics."""
        print("\n" + "=" * 60)
        print("📊 Redundancy Ranger Statistics")
        print("=" * 60)
        print(f"Files scanned:      {self.stats['files_scanned']:6d}")
        print(f"Duplicate groups:   {self.stats['duplicate_groups']:6d}")
        print(f"Primes designated:  {self.stats['primes_designated']:6d}")
        print(f"Shadows marked:     {self.stats['shadows_marked']:6d}")

        # Calculate space saved
        mb_saved = self.stats['bytes_saved'] / (1024 * 1024)
        print(f"Space saved:        {mb_saved:6.1f} MB")
        print("=" * 60)


def main():
    """Main execution with one-hertz testing."""
    import sys

    print("🤠 Redundancy Ranger - Gravity Well Training Edition")
    print("=" * 60)

    # Get source directory
    if len(sys.argv) > 1:
        source_dir = sys.argv[1]
    else:
        # Default to parent's gravity_well if it exists
        source_dir = Path(__file__).parent.parent / "gravity_well"
        if not source_dir.exists():
            print("\n❌ No source directory specified")
            print("Usage: python3 REDUNDANCY_RANGER.py <source_directory>")
            return

    # Create ranger
    ranger = RedundancyRanger(source_dir)

    # Scan for duplicates
    ranger.scan_for_duplicates()

    if ranger.stats['duplicate_groups'] == 0:
        print("\n✓ No duplicates found! Directory is clean.")
        return

    # ONE HERTZ MODE: Test with first 5 groups
    print("\n🐌 One Hertz Mode: Processing first 5 duplicate groups...")
    print("(Set limit=None to process all groups)")

    results = ranger.process_all_duplicates(dry_run=True, limit=5)

    ranger.print_stats()

    print("\n✅ DRY RUN COMPLETE - No files were moved")
    print("\nNext steps:")
    print("1. Review the groups above")
    print("2. Check if prime selection logic is correct")
    print("3. Run with dry_run=False to actually process")
    print("\nTo process for real:")
    print("  ranger.process_all_duplicates(dry_run=False)")


if __name__ == "__main__":
    main()
