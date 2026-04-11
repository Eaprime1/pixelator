#!/usr/bin/env python3
"""
ListMancer v0.1 - Command Entity Gateway
The intentional interacting interpreter for ls

Philosophy:
- Commands MUST be commanded (that's their nature)
- Humans need exploration space (that's OUR nature)
- The mancer creates liminal possibility between both
- ls may never understand us, but we can work together harmoniously

Symbol Language:
  PREFIX (perspective):
    ~ = play/explore
    - = read/observe
    ^ = create/build
    + = work/produce
    % = synergy/integrate
  
  SUFFIX (tone):
    ~ = guided/gentle
    ! = direct/fast
    ? = questioning/interactive
    + = building/layered
    - = minimal/pure
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

class ListMancer:
    """The interpreter between human intent and ls command entity"""
    
    def __init__(self):
        self.home = Path.home() / ".listmancer"
        self.home.mkdir(exist_ok=True)
        self.memory_file = self.home / "user_memory.json"
        self.commands_file = Path(__file__).parent / "ls_commands.json"
        self.memory = self._load_memory()
        self.commands = self._load_commands()
        
    def _load_memory(self):
        """Load user's interaction history and preferences"""
        if self.memory_file.exists():
            with open(self.memory_file) as f:
                return json.load(f)
        return {
            "interactions": [],
            "preferences": {
                "color_mode": "auto",
                "last_archetype": None,
                "favorite_options": []
            },
            "achievements": [],
            "success_patterns": {}
        }
    
    def _save_memory(self):
        """Persist learning back to JSON"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def _load_commands(self):
        """Load command templates and archetypes"""
        if self.commands_file.exists():
            with open(self.commands_file) as f:
                return json.load(f)
        # Default fallback if JSON doesn't exist yet
        return self._default_commands()
    
    def _default_commands(self):
        """Minimal working command set"""
        return {
            "archetypes": {
                "librarian": "Organized, categorized, systematic",
                "sommelier": "Curated, contextual, refined",
                "docent": "Educational, narrative, illuminating"
            },
            "views": {
                "colors": {
                    "name": "🎨 Colors - Group by type",
                    "command": "ls --color=auto -lh",
                    "description": "See files grouped by what they ARE"
                },
                "time": {
                    "name": "📅 Time - When things changed",
                    "command": "ls -lt",
                    "description": "Most recent changes first"
                },
                "size": {
                    "name": "📏 Size - What's taking space",
                    "command": "ls -lhS",
                    "description": "Largest files at top"
                },
                "tree": {
                    "name": "🌳 Tree - Show structure",
                    "command": "ls -R",
                    "description": "Everything under here, organized"
                },
                "simple": {
                    "name": "📝 Simple - Just names",
                    "command": "ls -1",
                    "description": "Clean list, one per line"
                },
                "all": {
                    "name": "👁️ All - Include hidden",
                    "command": "ls -la",
                    "description": "Show me EVERYTHING"
                },
                "bw": {
                    "name": "⬛ Pure B&W - Information density",
                    "command": "ls -lh --color=never",
                    "description": "No decoration, pure data"
                }
            }
        }
    
    def _record_interaction(self, perspective, tone, choice, success=None):
        """Learn from each interaction"""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "perspective": perspective,
            "tone": tone,
            "choice": choice,
            "success": success
        }
        self.memory["interactions"].append(interaction)
        
        # Track success patterns
        key = f"{perspective}{tone}:{choice}"
        if key not in self.memory["success_patterns"]:
            self.memory["success_patterns"][key] = {"count": 0, "successes": 0}
        
        self.memory["success_patterns"][key]["count"] += 1
        if success:
            self.memory["success_patterns"][key]["successes"] += 1
        
        self._save_memory()
    
    def _execute_ls(self, command, path="."):
        """Actually command the ls entity"""
        try:
            # Ensure path is safe
            safe_path = str(Path(path).resolve())
            full_command = f"{command} {safe_path}"
            
            result = subprocess.run(
                full_command,
                shell=True,
                capture_output=True,
                text=True
            )
            
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Error commanding ls: {e}"
    
    def _show_menu(self, views, title="ListMancer", prompt="Choose your vision:"):
        """Display interactive menu"""
        print(f"\n╔{'═' * 50}╗")
        print(f"║ {title:^48} ║")
        print(f"╠{'═' * 50}╣")
        print(f"║ {prompt:^48} ║")
        print(f"║{' ' * 50}║")
        
        options = list(views.items())
        for i, (key, view) in enumerate(options, 1):
            name = view['name']
            print(f"║  {i}. {name:<45}║")
        
        print(f"║{' ' * 50}║")
        print(f"║  0. ⚙️  Raw - Just give me ls [options]{' ' * 9}║")
        print(f"║  q. Exit{' ' * 42}║")
        print(f"╚{'═' * 50}╝\n")
        
        return options
    
    def play_gentle(self, path="."):
        """~ls~ - Play perspective, gentle guided mode"""
        print("\n🌊 Welcome to ListMancer - Gentle Exploration Mode")
        print("   I help you see what's here, at your own pace\n")
        
        views = self.commands["views"]
        
        while True:
            options = self._show_menu(views, 
                                     title="ListMancer - Play Mode (~ls~)",
                                     prompt="What would you like to see?")
            
            choice = input("Enter your choice: ").strip().lower()
            
            if choice == 'q':
                print("\n✨ Thank you for exploring together\n")
                break
            
            if choice == '0':
                print("\n⚙️  Raw mode - Command ls directly:")
                raw_opts = input("ls options (or Enter for basic): ").strip()
                command = f"ls {raw_opts}" if raw_opts else "ls"
                output = self._execute_ls(command, path)
                print(f"\n{output}")
                self._record_interaction("~", "~", "raw", True)
                continue
            
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    key, view = options[idx]
                    print(f"\n{view['description']}\n")
                    
                    # Confirm before executing
                    confirm = input("Execute this view? [Y/n]: ").strip().lower()
                    if confirm in ['', 'y', 'yes']:
                        output = self._execute_ls(view['command'], path)
                        print(f"\n{output}")
                        
                        # Simple satisfaction check
                        satisfied = input("\nDid this help? [Y/n]: ").strip().lower()
                        success = satisfied in ['', 'y', 'yes']
                        self._record_interaction("~", "~", key, success)
                        
                        if success:
                            print("⭐ Great! This pattern has been remembered.")
                    else:
                        print("No problem, let's try something else.")
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Please enter a number or 'q' to quit.")
    
    def read_gentle(self, path="."):
        """-ls~ - Reader perspective, gentle guided mode"""
        print("\n📖 ListMancer Reader Mode - Understanding What You See")
        print("   I explain what's here and what it means\n")
        
        # First, show what's here
        basic_output = self._execute_ls("ls -lh --color=auto", path)
        print("Current view:\n")
        print(basic_output)
        
        print("\n" + "─" * 50)
        print("Let me help you understand this...")
        print("─" * 50 + "\n")
        
        views = self.commands["views"]
        
        while True:
            print("\nWhat would you like to know about?")
            print("  1. 🎨 What do the colors mean?")
            print("  2. 📅 How do I see recent changes?")
            print("  3. 📏 What's using the most space?")
            print("  4. 👁️ Are there hidden files?")
            print("  5. 📝 Explain the symbols (d, r, w, x)")
            print("  0. Show me a different view")
            print("  q. Exit\n")
            
            choice = input("Your question: ").strip().lower()
            
            if choice == 'q':
                print("\n✨ Happy reading!\n")
                break
            
            if choice == '1':
                print("\n🎨 Colors help you see types at a glance:")
                print("   BLUE = Directories (folders you can enter)")
                print("   GREEN = Executable files (programs you can run)")
                print("   RED = Archives (compressed files like .zip)")
                print("   WHITE = Regular files")
                print("   CYAN = Symbolic links (shortcuts to other files)")
                self._record_interaction("-", "~", "colors_explained", True)
            
            elif choice == '2':
                print("\n📅 To see recent changes:")
                output = self._execute_ls("ls -lt", path)
                print(output)
                print("\nNewest modifications appear first!")
                self._record_interaction("-", "~", "time_view", True)
            
            elif choice == '3':
                print("\n📏 Files sorted by size:")
                output = self._execute_ls("ls -lhS", path)
                print(output)
                print("\nLargest files at the top!")
                self._record_interaction("-", "~", "size_view", True)
            
            elif choice == '4':
                print("\n👁️ Including hidden files (starting with .):")
                output = self._execute_ls("ls -la", path)
                print(output)
                print("\nHidden files often contain configuration!")
                self._record_interaction("-", "~", "all_view", True)
            
            elif choice == '5':
                print("\n📝 Symbol guide:")
                print("   d = Directory")
                print("   - = Regular file")
                print("   l = Link (shortcut)")
                print("   r = Readable")
                print("   w = Writable")
                print("   x = Executable")
                print("\nExample: drwxr-xr-x")
                print("  └─ Directory, owner can rwx, others can rx")
                self._record_interaction("-", "~", "symbols_explained", True)
            
            elif choice == '0':
                self.play_gentle(path)
                break
            
            else:
                print("Please choose a number from the menu.")
    
    def create_building(self, path="."):
        """^ls+ - Create perspective, building/teaching mode"""
        print("\n🏗️ ListMancer Builder Mode - Learn to Construct")
        print("   I teach you how to build your own ls commands\n")
        
        print("Let's build a custom ls command together!\n")
        
        print("Step 1: What information do you want?")
        print("  [l] Long format (detailed info)")
        print("  [1] Simple list (just names)")
        print("  [Enter] Basic format\n")
        
        format_choice = input("Choose format: ").strip().lower()
        
        command_parts = ["ls"]
        explanation = []
        
        if format_choice == 'l':
            command_parts.append("-l")
            explanation.append("-l = long format with details")
        elif format_choice == '1':
            command_parts.append("-1")
            explanation.append("-1 = one file per line")
        
        print("\nStep 2: How should it be sorted?")
        print("  [t] By time (newest first)")
        print("  [S] By size (largest first)")
        print("  [r] Reverse order")
        print("  [Enter] Default (alphabetical)\n")
        
        sort_choice = input("Choose sorting: ").strip()
        
        if sort_choice == 't':
            command_parts.append("-t")
            explanation.append("-t = sort by modification time")
        elif sort_choice == 'S':
            command_parts.append("-S")
            explanation.append("-S = sort by size")
        elif sort_choice == 'r':
            command_parts.append("-r")
            explanation.append("-r = reverse sort order")
        
        print("\nStep 3: What files to show?")
        print("  [a] All (including hidden)")
        print("  [A] Almost all (no . and ..)")
        print("  [Enter] Visible files only\n")
        
        show_choice = input("Choose visibility: ").strip().lower()
        
        if show_choice == 'a':
            command_parts.append("-a")
            explanation.append("-a = show all files including hidden")
        elif show_choice == 'A':
            command_parts.append("-A")
            explanation.append("-A = show hidden but not . and ..")
        
        print("\nStep 4: Human-friendly sizes?")
        human = input("Show sizes as 1K, 234M, 2G? [Y/n]: ").strip().lower()
        
        if human in ['', 'y', 'yes']:
            command_parts.append("-h")
            explanation.append("-h = human-readable sizes")
        
        # Build the final command
        final_command = " ".join(command_parts)
        
        print("\n" + "═" * 50)
        print("🎉 You've built this command:")
        print(f"   {final_command}")
        print("\nWhat each part does:")
        for exp in explanation:
            print(f"   • {exp}")
        print("═" * 50)
        
        execute = input("\nTry it now? [Y/n]: ").strip().lower()
        
        if execute in ['', 'y', 'yes']:
            output = self._execute_ls(final_command, path)
            print(f"\n{output}")
            
            print(f"\n💡 Tip: You can use this command anytime:")
            print(f"   $ {final_command}")
            
            self._record_interaction("^", "+", "custom_build", True)
        
        again = input("\nBuild another? [y/N]: ").strip().lower()
        if again in ['y', 'yes']:
            self.create_building(path)
    
    def show_stats(self):
        """Display learning statistics"""
        print("\n📊 ListMancer Learning Statistics\n")
        print(f"Total interactions: {len(self.memory['interactions'])}")
        
        if self.memory['success_patterns']:
            print("\nMost successful patterns:")
            sorted_patterns = sorted(
                self.memory['success_patterns'].items(),
                key=lambda x: x[1]['successes'] / max(x[1]['count'], 1),
                reverse=True
            )[:5]
            
            for pattern, stats in sorted_patterns:
                success_rate = stats['successes'] / max(stats['count'], 1) * 100
                print(f"  {pattern}: {success_rate:.0f}% success ({stats['count']} uses)")

def main():
    """Entry point for ListMancer"""
    if len(sys.argv) < 2:
        print("ListMancer - Command entity gateway")
        print("\nUsage:")
        print("  ~ls~   Play mode - gentle guided exploration")
        print("  -ls~   Reader mode - understand what you see")
        print("  ^ls+   Builder mode - learn to construct commands")
        print("  listmancer --stats   Show learning statistics")
        return
    
    mode = sys.argv[1]
    path = sys.argv[2] if len(sys.argv) > 2 else "."
    
    mancer = ListMancer()
    
    if mode == "~ls~":
        mancer.play_gentle(path)
    elif mode == "-ls~":
        mancer.read_gentle(path)
    elif mode == "^ls+":
        mancer.create_building(path)
    elif mode == "--stats":
        mancer.show_stats()
    else:
        print(f"Unknown mode: {mode}")
        print("Available: ~ls~, -ls~, ^ls+")

if __name__ == "__main__":
    main()
