#!/usr/bin/env python3
"""
Directory Navigator UI for Simplex AI Development
Interactive terminal-based file explorer with search capabilities
"""

import os
import sys
from pathlib import Path
import subprocess
import json

class DirectoryNavigator:
    def __init__(self, start_path=None):
        self.current_path = Path(start_path or os.getcwd())
        self.search_results = []
        self.bookmarks = {
            'home': Path.home(),
            'terminal': Path.home() / 'storage' / 'terminal',
            'phoenix': Path.home() / 'storage' / 'terminal' / 'phoenix_hub',
            'universe': Path.home() / 'storage' / 'terminal' / 'universe',
            'sacred': Path.home() / 'storage' / 'terminal' / 'sacred_empire'
        }
    
    def clear_screen(self):
        os.system('clear')
    
    def display_header(self):
        print("🌌" + "="*60 + "🌌")
        print("    SIMPLEX AI OMEGA - DIRECTORY NAVIGATOR")
        print("    Current Path:", str(self.current_path))
        print("🌌" + "="*60 + "🌌")
        print()
    
    def list_directory(self, show_hidden=False):
        try:
            items = []
            for item in self.current_path.iterdir():
                if not show_hidden and item.name.startswith('.'):
                    continue
                items.append(item)
            
            items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
            
            for i, item in enumerate(items[:50], 1):  # Limit to 50 items
                if item.is_dir():
                    print(f"{i:2d}. 📁 {item.name}/")
                else:
                    size = self.get_file_size(item)
                    ext = item.suffix.lower()
                    icon = self.get_file_icon(ext)
                    print(f"{i:2d}. {icon} {item.name} ({size})")
            
            if len(list(self.current_path.iterdir())) > 50:
                print(f"    ... and {len(list(self.current_path.iterdir())) - 50} more items")
            
            return items[:50]
        except PermissionError:
            print("❌ Permission denied accessing this directory")
            return []
    
    def get_file_size(self, file_path):
        try:
            size = file_path.stat().st_size
            if size < 1024:
                return f"{size}B"
            elif size < 1024**2:
                return f"{size/1024:.1f}KB"
            elif size < 1024**3:
                return f"{size/(1024**2):.1f}MB"
            else:
                return f"{size/(1024**3):.1f}GB"
        except:
            return "?"
    
    def get_file_icon(self, ext):
        icons = {
            '.py': '🐍', '.js': '📜', '.json': '📋', '.md': '📝',
            '.txt': '📄', '.log': '📊', '.sh': '⚡', '.html': '🌐',
            '.css': '🎨', '.jpg': '🖼️', '.png': '🖼️', '.pdf': '📕',
            '.zip': '📦', '.mp3': '🎵', '.mp4': '🎬'
        }
        return icons.get(ext, '📄')
    
    def search_files(self, pattern, search_path=None):
        search_path = search_path or self.current_path
        print(f"🔍 Searching for '{pattern}' in {search_path}...")
        
        self.search_results = []
        try:
            for root, dirs, files in os.walk(search_path):
                root_path = Path(root)
                for file in files:
                    if pattern.lower() in file.lower():
                        self.search_results.append(root_path / file)
                for dir in dirs:
                    if pattern.lower() in dir.lower():
                        self.search_results.append(root_path / dir)
        except Exception as e:
            print(f"❌ Search error: {e}")
            return
        
        print(f"📊 Found {len(self.search_results)} matches:")
        for i, result in enumerate(self.search_results[:20], 1):
            rel_path = result.relative_to(search_path) if result.is_relative_to(search_path) else result
            if result.is_dir():
                print(f"{i:2d}. 📁 {rel_path}/")
            else:
                print(f"{i:2d}. 📄 {rel_path}")
        
        if len(self.search_results) > 20:
            print(f"    ... and {len(self.search_results) - 20} more results")
    
    def display_menu(self):
        print("\n" + "─"*60)
        print("📋 NAVIGATION COMMANDS:")
        print("  [number] - Enter directory or view file")
        print("  b/back   - Go back to parent directory")
        print("  h/home   - Go to home directory")
        print("  s/search - Search for files/directories")
        print("  sa       - Search AI/Simplex related files")
        print("  bm       - Show bookmarks")
        print("  pwd      - Show current path")
        print("  info     - Show file/directory info")
        print("  q/quit   - Exit navigator")
        print("─"*60)
    
    def show_bookmarks(self):
        print("\n📖 BOOKMARKS:")
        for name, path in self.bookmarks.items():
            exists = "✅" if path.exists() else "❌"
            print(f"  {name}: {path} {exists}")
        print("\nType bookmark name to navigate (e.g., 'terminal')")
    
    def search_ai_files(self):
        ai_patterns = ['simplex', 'ai', 'neural', 'omega', 'consciousness', 'phoenix']
        print("🤖 Searching for AI/Simplex related files...")
        
        all_results = []
        for pattern in ai_patterns:
            for root, dirs, files in os.walk(Path.home()):
                try:
                    root_path = Path(root)
                    for file in files:
                        if pattern.lower() in file.lower():
                            file_path = root_path / file
                            if file_path not in all_results:
                                all_results.append(file_path)
                    for dir in dirs:
                        if pattern.lower() in dir.lower():
                            dir_path = root_path / dir
                            if dir_path not in all_results:
                                all_results.append(dir_path)
                except PermissionError:
                    continue
        
        self.search_results = all_results[:50]  # Limit results
        print(f"🔍 Found {len(self.search_results)} AI-related items:")
        for i, result in enumerate(self.search_results, 1):
            if result.is_dir():
                print(f"{i:2d}. 📁 {result}")
            else:
                print(f"{i:2d}. 📄 {result}")
    
    def show_file_info(self, file_path):
        try:
            stat = file_path.stat()
            print(f"\n📊 FILE INFO: {file_path.name}")
            print(f"   Path: {file_path}")
            print(f"   Size: {self.get_file_size(file_path)}")
            print(f"   Type: {'Directory' if file_path.is_dir() else 'File'}")
            print(f"   Modified: {stat.st_mtime}")
            
            if file_path.is_file() and file_path.suffix.lower() in ['.py', '.js', '.json', '.md', '.txt']:
                print(f"\n📖 PREVIEW (first 5 lines):")
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        for i, line in enumerate(f):
                            if i >= 5:
                                break
                            print(f"   {i+1}: {line.rstrip()}")
                except Exception as e:
                    print(f"   ❌ Cannot preview: {e}")
        except Exception as e:
            print(f"❌ Error getting file info: {e}")
    
    def run(self):
        while True:
            self.clear_screen()
            self.display_header()
            
            items = self.list_directory()
            self.display_menu()
            
            try:
                command = input("\n🎯 Enter command: ").strip()
                
                if command.lower() in ['q', 'quit']:
                    break
                elif command.lower() in ['b', 'back']:
                    self.current_path = self.current_path.parent
                elif command.lower() in ['h', 'home']:
                    self.current_path = Path.home()
                elif command.lower() in ['s', 'search']:
                    pattern = input("🔍 Enter search pattern: ").strip()
                    if pattern:
                        self.search_files(pattern)
                        input("\nPress Enter to continue...")
                elif command.lower() == 'sa':
                    self.search_ai_files()
                    input("\nPress Enter to continue...")
                elif command.lower() == 'bm':
                    self.show_bookmarks()
                    bookmark = input("\nEnter bookmark name (or Enter to continue): ").strip()
                    if bookmark in self.bookmarks:
                        self.current_path = self.bookmarks[bookmark]
                elif command.lower() == 'pwd':
                    print(f"📍 Current path: {self.current_path}")
                    input("Press Enter to continue...")
                elif command.lower() == 'info':
                    if items:
                        try:
                            num = int(input("Enter item number for info: "))
                            if 1 <= num <= len(items):
                                self.show_file_info(items[num-1])
                                input("\nPress Enter to continue...")
                        except ValueError:
                            pass
                elif command.isdigit():
                    num = int(command)
                    if 1 <= num <= len(items):
                        selected = items[num-1]
                        if selected.is_dir():
                            self.current_path = selected
                        else:
                            self.show_file_info(selected)
                            view = input("\nView file content? (y/n): ").strip().lower()
                            if view == 'y':
                                try:
                                    subprocess.run(['less', str(selected)], check=True)
                                except:
                                    print("❌ Cannot view file")
                                    input("Press Enter to continue...")
                elif command in self.bookmarks:
                    self.current_path = self.bookmarks[command]
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                input("Press Enter to continue...")

if __name__ == "__main__":
    print("🚀 Starting Simplex AI Directory Navigator...")
    navigator = DirectoryNavigator()
    navigator.run()
    print("👋 Directory Navigator closed. Happy coding!")