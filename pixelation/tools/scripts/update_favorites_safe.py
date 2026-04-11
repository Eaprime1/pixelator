#!/usr/bin/env python3
"""
Update UI favorites with safe commands (no HERE documents)
"""

import json
from pathlib import Path

def update_favorites():
    prefs_file = Path.home() / 'simplex_ui_preferences.json'
    
    if prefs_file.exists():
        with open(prefs_file, 'r') as f:
            data = json.load(f)
        
        # Add safe versions of the problematic commands
        data['favorites']['Safe Entity Classification Report'] = 'bash ~/safe_entity_classification_script.sh'
        data['favorites']['Safe Priority Actions Report'] = 'bash ~/safe_priority_actions_script.sh'
        
        # Remove or update the problematic ones if they exist
        problematic_keys = []
        for key, command in data['favorites'].items():
            if 'EOF' in command or '<<' in command:
                problematic_keys.append(key)
        
        for key in problematic_keys:
            print(f"🔧 Found problematic command: {key}")
            print(f"   Command: {data['favorites'][key][:100]}...")
            # Keep it but mark it as potentially problematic
            data['favorites'][f"{key} (CLIPBOARD_ISSUE)"] = data['favorites'][key]
            del data['favorites'][key]
        
        # Update timestamp
        from datetime import datetime
        data['last_updated'] = datetime.now().isoformat()
        
        # Save updated preferences
        with open(prefs_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print("✅ Updated UI preferences with safe commands")
        print("🔧 Added safe script alternatives")
        if problematic_keys:
            print(f"⚠️ Marked {len(problematic_keys)} potentially problematic commands")
    else:
        print("❌ No preferences file found")

if __name__ == "__main__":
    update_favorites()