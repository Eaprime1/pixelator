#!/usr/bin/env python3
"""
Quick Launch Interface for Termux Universe
Simple 1,2,3,4 selection system
"""

import os
import subprocess

def show_menu():
    print("\n🌐 TERMUX UNIVERSE QUICK LAUNCH")
    print("=" * 40)
    print("1. 🔍 Run Duplicate Manager")
    print("2. ☁️ Setup Cloud Storage") 
    print("3. 📚 Gather Wiki Knowledge")
    print("4. 📧 Discover Email Accounts")
    print("5. 📻 BBS Heritage Reference")
    print("6. 🔧 System Status")
    print("0. Exit")
    print("=" * 40)

def main():
    while True:
        show_menu()
        choice = input("\n🚀 Select option (0-6): ").strip()
        
        if choice == '0':
            print("✅ Termux Universe session complete")
            break
        elif choice == '1':
            scan_dir = input("📁 Directory to scan: ") or "."
            subprocess.run(['python', 'duplicate_manager.py', scan_dir])
        elif choice == '2':
            subprocess.run(['python', 'setup_clouds.py'])
        elif choice == '3':
            entity = input("📚 Entity to research: ")
            if entity:
                subprocess.run(['python', 'wiki_gatherer.py', entity])
        elif choice == '4':
            subprocess.run(['python', 'email_discovery.py'])
        elif choice == '5':
            subprocess.run(['cat', 'bbs/bbs_heritage.md'])
        elif choice == '6':
            print("💾 Storage:", subprocess.run(['df', '-h'], capture_output=True, text=True).stdout)
            print("🔗 Network:", subprocess.run(['ping', '-c', '1', 'google.com'], capture_output=True))
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
