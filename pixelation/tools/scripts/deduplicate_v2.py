import os
import shutil
from collections import defaultdict
import sys

# The file containing the list of duplicate files
DUPLICATES_FILE = '/data/data/com.termux/files/home/.gemini/tmp/2bf7c6a953ab15026b493341f2de7f67c82c1c73e82862940125d89bee1bb191/duplicates.txt'

# Path prefixes to prioritize for keeping files
# Files with these prefixes are less likely to be the "main" copy
PATH_KEYWORDS_TO_AVOID = [
    '.trashed',
    '_duplicates',
    'Copy of',
    'backup',
    'archive',
    'incubator'
]

def choose_file_to_keep(files):
    """
    Chooses which file to keep from a list of duplicates.
    The last file in the sorted list will be kept.
    """
    return sorted(files, key=lambda f: sum(k in f for k in PATH_KEYWORDS_TO_AVOID))[-1]

def main():
    if not os.path.exists(DUPLICATES_FILE):
        print(f"Error: Duplicates file not found at {DUPLICATES_FILE}")
        return

    with open(DUPLICATES_FILE, 'r') as f:
        lines = f.readlines()

    groups = defaultdict(list)
    all_hashes = []
    current_hash = None
    for line in lines:
        line = line.strip()
        if not line:
            current_hash = None
            continue

        parts = line.split(maxsplit=1)
        if len(parts) < 2:
            continue

        file_hash, file_path = parts
        if current_hash != file_hash:
            current_hash = file_hash
            all_hashes.append(current_hash)
        
        # All paths in duplicates.txt are relative to Q_pixel8
        full_path = os.path.join('Q_pixel8', file_path)
        groups[current_hash].append(full_path)

    for file_hash in all_hashes:
        files = groups[file_hash]
        if len(files) < 2:
            continue

        file_to_keep = choose_file_to_keep(files)
        
        # New name for the file to keep
        count = len(files)
        name, ext = os.path.splitext(os.path.basename(file_to_keep))
        new_name = f"{name}_{count}{ext}"
        new_filepath = os.path.join(os.path.dirname(file_to_keep), new_name)

        print(f"Duplicate set hash: {file_hash}")
        print(f"  - Keeping: {file_to_keep}")
        print(f"  - Renaming to: {new_name}")

        # Rename the file that we are keeping first
        if os.path.exists(file_to_keep):
            try:
                # Ensure new_filepath is unique before renaming
                counter = 1
                while os.path.exists(new_filepath):
                    new_filepath = os.path.join(os.path.dirname(file_to_keep), f"{name}_{count}_{counter}{ext}")
                    counter += 1
                os.rename(file_to_keep, new_filepath)
                print(f"  - Renamed to: {new_filepath}")

            except Exception as e:
                print(f"  - Error renaming {file_to_keep} to {new_filepath}: {e}")
        else:
            print(f"  - Skipped renaming (not found): {file_to_keep}")

        for file_path in files:
            if file_path != file_to_keep:
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                        print(f"  - Deleted: {file_path}")
                    except Exception as e:
                        print(f"  - Error deleting {file_path}: {e}")
                else:
                    # This is expected if the file was deleted as part of another group
                    pass
            
        print("-" * 20)

if __name__ == '__main__':
    main()