import os
from git import Repo

# --- THE SETUP ---
# This is the specific folder we are watching
repo_path = "/home/sauron/unexusi/unexusi_dev"

def check_my_repo():
    print(f"--- Checking: {repo_path} ---")

    try:
        # 1. CONNECT to the repo
        repo = Repo(repo_path)

        # 2. ASK: Is it dirty? (Meaning, are there unsaved changes?)
        is_dirty = repo.is_dirty(untracked_files=True)

        # 3. REPORT the result
        if is_dirty:
            print(f"⚠️  STATUS: You have UNSAVED changes in 'unexusi_dev'.")
            print("   Action needed: git add . && git commit")
        else:
            print(f"✅ STATUS: Clean. Everything is saved.")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the function
if __name__ == "__main__":
    check_my_repo()
