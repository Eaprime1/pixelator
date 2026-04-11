#!/usr/bin/env python3
"""
Google Drive Trash Inventory Tool
----------------------------------
Gets a list of all files in Google Drive trash using rclone,
with progress indication and timeout handling.
"""

import subprocess
import sys
import time
from pathlib import Path

def run_rclone_command(cmd, timeout=300):
    """Run rclone command with timeout and progress indication."""
    print(f"Running: {' '.join(cmd)}")
    print("This may take a few minutes... (Ctrl+C to cancel)")

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )

        # Show progress dots while waiting
        start_time = time.time()
        dots = 0
        while process.poll() is None:
            if time.time() - start_time > timeout:
                process.kill()
                print("\n⚠️  Command timed out after", timeout, "seconds")
                return None, "Timeout"

            time.sleep(2)
            dots += 1
            print("." * min(dots, 3), end="\r")
            sys.stdout.flush()

        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"\n❌ Error: {stderr}")
            return None, stderr

        return stdout, None

    except KeyboardInterrupt:
        process.kill()
        print("\n⚠️  Cancelled by user")
        return None, "Cancelled"

def get_trash_listing(remote="gdrive_terminal"):
    """Get listing of all files in Google Drive trash."""
    print(f"\n🗑️  Getting trash inventory for {remote}...")
    print("="*60)

    # Try to get a quick count first with lsf (list files)
    cmd = [
        "rclone", "lsf",
        f"{remote}:",
        "--drive-trashed-only",
        "--files-only",
        "--format", "p"  # Just paths for now
    ]

    output, error = run_rclone_command(cmd, timeout=120)

    if output is None:
        print("\n⚠️  Could not get trash listing directly.")
        print("Trying alternative method...")

        # Try with ls instead (slower but more reliable)
        cmd = [
            "rclone", "ls",
            f"{remote}:",
            "--drive-trashed-only"
        ]
        output, error = run_rclone_command(cmd, timeout=180)

    if output:
        files = [line.strip() for line in output.split('\n') if line.strip()]
        return files
    else:
        return []

def save_inventory(files, output_file="gdrive_trash_inventory.txt"):
    """Save file list to output file."""
    output_path = Path(output_file)

    with open(output_path, 'w') as f:
        f.write(f"Google Drive Trash Inventory\n")
        f.write(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total files: {len(files)}\n")
        f.write("="*60 + "\n\n")

        for file in files:
            f.write(f"{file}\n")

    print(f"\n✅ Inventory saved to: {output_path}")
    print(f"📊 Total files: {len(files)}")

    return output_path

def main():
    """Main execution."""
    remote = "gdrive_terminal"

    print("\n🔍 Google Drive Trash Inventory Tool")
    print("="*60)

    # Get the trash listing
    files = get_trash_listing(remote)

    if not files:
        print("\n⚠️  No files found in trash (or unable to access)")
        print("\nPossible reasons:")
        print("  1. Trash is empty")
        print("  2. All items in trash are folders (not files)")
        print("  3. Network/auth issue")
        print("\nTrying to check trash status with 'rclone about'...")

        # Get trash size info
        cmd = ["rclone", "about", f"{remote}:"]
        output, error = run_rclone_command(cmd, timeout=30)
        if output:
            print(output)
        return

    # Save the inventory
    output_file = "gdrive_trash_inventory.txt"
    save_inventory(files, output_file)

    # Show sample
    print("\n📋 First 10 files:")
    for file in files[:10]:
        print(f"   {file}")

    if len(files) > 10:
        print(f"   ... and {len(files) - 10} more")

if __name__ == "__main__":
    main()
