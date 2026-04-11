#!/usr/bin/env python3
"""
Intelligent Duplicate Manager with Entity Recognition
CRISPR-NiE: Precise file entity identification and management
"""

import os
import hashlib
import json
from pathlib import Path
from collections import defaultdict
import argparse

class CRISPRNiEDuplicateManager:
    """
    CRISPR-NiE (Clustered Regularly Interspaced Short Palindromic Repeats - Nano Intelligence Entity)
    Intelligent duplicate detection with entity awareness
    """
    
    def __init__(self, scan_directory):
        self.scan_dir = Path(scan_directory)
        self.duplicates = defaultdict(list)
        self.entity_types = {}
        self.file_hashes = {}
        
    def calculate_file_hash(self, filepath):
        """Calculate SHA256 hash for file comparison"""
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            print(f"❌ Error hashing {filepath}: {e}")
            return None
    
    def classify_entity_type(self, filepath):
        """Classify file as entity type based on content and extension"""
        path = Path(filepath)
        ext = path.suffix.lower()
        
        entity_classifications = {
            '.py': 'Python Entity',
            '.json': 'JSON Entity', 
            '.html': 'HTML Entity',
            '.tsx': 'TSX Entity',
            '.js': 'JavaScript Entity',
            '.md': 'Markdown Entity',
            '.txt': 'Text Entity',
            '.pdf': 'Document Entity',
            '.jpg': 'Image Entity',
            '.png': 'Image Entity',
            '.mp4': 'Video Entity',
            '.zip': 'Archive Entity'
        }
        
        return entity_classifications.get(ext, 'Unknown Entity')
    
    def scan_for_duplicates(self):
        """Scan directory for duplicate files with entity awareness"""
        print(f"🔍 Scanning: {self.scan_dir}")
        
        for filepath in self.scan_dir.rglob('*'):
            if filepath.is_file():
                file_hash = self.calculate_file_hash(filepath)
                if file_hash:
                    self.file_hashes[filepath] = file_hash
                    self.duplicates[file_hash].append(filepath)
                    self.entity_types[filepath] = self.classify_entity_type(filepath)
    
    def generate_report(self):
        """Generate duplicate analysis report"""
        duplicate_groups = {k: v for k, v in self.duplicates.items() if len(v) > 1}
        
        print("\n📊 CRISPR-NiE DUPLICATE ANALYSIS REPORT")
        print("=" * 50)
        
        if not duplicate_groups:
            print("✅ No duplicates found!")
            return
        
        total_duplicates = sum(len(group) - 1 for group in duplicate_groups.values())
        print(f"🔍 Found {len(duplicate_groups)} duplicate groups")
        print(f"📁 Total duplicate files: {total_duplicates}")
        
        for hash_val, file_list in duplicate_groups.items():
            print(f"\n🔗 Duplicate Group (Hash: {hash_val[:8]}...)")
            for i, filepath in enumerate(file_list):
                entity_type = self.entity_types[filepath]
                size = filepath.stat().st_size
                print(f"  {i+1}. [{entity_type}] {filepath} ({size} bytes)")
    
    def move_duplicates_to_folder(self, target_folder="duplicates"):
        """Move duplicates to specified folder, keeping first occurrence"""
        duplicate_groups = {k: v for k, v in self.duplicates.items() if len(v) > 1}
        
        if not duplicate_groups:
            print("✅ No duplicates to move")
            return
        
        target_path = Path(target_folder)
        target_path.mkdir(exist_ok=True)
        
        moved_count = 0
        for file_list in duplicate_groups.values():
            # Keep first file, move others
            for duplicate_file in file_list[1:]:
                try:
                    new_location = target_path / duplicate_file.name
                    # Handle name conflicts in duplicate folder
                    counter = 1
                    while new_location.exists():
                        name_parts = duplicate_file.stem, counter, duplicate_file.suffix
                        new_location = target_path / f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                        counter += 1
                    
                    duplicate_file.rename(new_location)
                    moved_count += 1
                    print(f"📦 Moved: {duplicate_file} → {new_location}")
                except Exception as e:
                    print(f"❌ Failed to move {duplicate_file}: {e}")
        
        print(f"✅ Moved {moved_count} duplicate files to {target_path}")

def main():
    parser = argparse.ArgumentParser(description="CRISPR-NiE Intelligent Duplicate Manager")
    parser.add_argument("directory", help="Directory to scan for duplicates")
    parser.add_argument("--move", action="store_true", help="Move duplicates to duplicates folder")
    parser.add_argument("--target", default="duplicates", help="Target folder for duplicates")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.directory):
        print(f"❌ Directory not found: {args.directory}")
        return
    
    manager = CRISPRNiEDuplicateManager(args.directory)
    manager.scan_for_duplicates()
    manager.generate_report()
    
    if args.move:
        manager.move_duplicates_to_folder(args.target)

if __name__ == "__main__":
    main()
