#!/usr/bin/env python3
"""
Cloud Storage Universe Access Configuration
Supports: Google Drive, Dropbox, OneDrive, Box, MEGA, Amazon S3, Azure
"""

import os
import json

CLOUD_PROVIDERS = {
    "google_drive": {
        "tool": "rclone",
        "config_name": "gdrive",
        "setup_cmd": "rclone config",
        "mount_cmd": "rclone mount gdrive: ~/universe/clouds/google"
    },
    "dropbox": {
        "tool": "rclone", 
        "config_name": "dropbox",
        "setup_cmd": "rclone config",
        "mount_cmd": "rclone mount dropbox: ~/universe/clouds/dropbox"
    },
    "onedrive": {
        "tool": "rclone",
        "config_name": "onedrive", 
        "setup_cmd": "rclone config",
        "mount_cmd": "rclone mount onedrive: ~/universe/clouds/onedrive"
    },
    "box": {
        "tool": "rclone",
        "config_name": "box",
        "setup_cmd": "rclone config", 
        "mount_cmd": "rclone mount box: ~/universe/clouds/box"
    },
    "amazon_s3": {
        "tool": "rclone",
        "config_name": "s3",
        "setup_cmd": "rclone config",
        "mount_cmd": "rclone mount s3: ~/universe/clouds/amazon"
    }
}

def setup_cloud_universe():
    print("☁️ CLOUD STORAGE UNIVERSE SETUP")
    print("Available providers:", list(CLOUD_PROVIDERS.keys()))
    
    # Save configuration for later use
    with open('~/universe/cloud_config.json', 'w') as f:
        json.dump(CLOUD_PROVIDERS, f, indent=2)
    
    print("✅ Cloud universe configuration saved")
    print("🔧 Run 'rclone config' to setup each cloud provider")

if __name__ == "__main__":
    setup_cloud_universe()
