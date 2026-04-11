#!/usr/bin/env python3
"""
Simplex Command UI - Interactive Terminal Interface (Fixed Version)
∰◊€π¿🌌∞ Easy command execution without typing command line
Paste, type, click - and execute!
FIXED: Prevents multiple instances and UI spawning
"""

import os
import sys
import subprocess
import shlex
from pathlib import Path
import json
from datetime import datetime
import threading
import queue
import time
import fcntl

class SimplexCommandUI:
    """Interactive UI for easy command execution"""
    
    def __init__(self):
        # Create lock file to prevent multiple instances
        self.lock_file_path = Path.home() / 'simplex_ui.lock'
        self.lock_file = None
        
        if not self.acquire_lock():
            print("⚠️ Another instance of Simplex Command UI is already running!")
            print("🔧 Close the other instance first, or use 'pkill -f simplex_command_ui' to force close")
            sys.exit(1)
        
        self.command_history = []
        self.favorite_commands = {}
        self.current_directory = Path.cwd()
        self.background_processes = {}
        self.command_output_queue = queue.Queue()
        
        # Load favorites and history
        self.load_user_preferences()
        
        # Quick command templates (FIXED: removed recursive calls)
        self.quick_commands = {
            'omega_launch': 'python3 ~/que_simplex/core/simplex_omega_master_seed.py',
            'ai_simplex': 'bash /storage/emulated/0/beasis/nexus/unexusi/entity_nexus/ai_core/intelligence/simplex_ai_controller.sh',
            'pipeline_status': 'python3 /storage/emulated/0/external_submission_pipeline/pipeline_launcher.py',
            'one_hertz': 'python3 /storage/emulated/0/external_submission_pipeline/one_hertz_processor.py',
            'entity_lists': 'python3 /storage/emulated/0/external_submission_pipeline/entity_list_generator.py',
            'dir_nav': 'python3 ~/directory_navigator.py',
            'file_finder': 'python3 ~/simple_file_finder.py'
        }
    
    def acquire_lock(self):
        """Acquire exclusive lock to prevent multiple instances"""
        try:
            self.lock_file = open(self.lock_file_path, 'w')
            fcntl.flock(self.lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.lock_file.write(f"{os.getpid()}\n{datetime.now().isoformat()}\n")
            self.lock_file.flush()
            return True
        except (IOError, OSError):
            if self.lock_file:
                self.lock_file.close()
            return False
    
    def release_lock(self):
        """Release the instance lock"""
        if self.lock_file:
            try:
                fcntl.flock(self.lock_file.fileno(), fcntl.LOCK_UN)
                self.lock_file.close()
                if self.lock_file_path.exists():
                    self.lock_file_path.unlink()
            except:
                pass
    
    def load_user_preferences(self):
        """Load user command history and favorites"""
        prefs_file = Path.home() / 'simplex_ui_preferences.json'
        if prefs_file.exists():
            try:
                with open(prefs_file, 'r') as f:
                    data = json.load(f)
                    self.command_history = data.get('history', [])
                    self.favorite_commands = data.get('favorites', {})
            except:
                pass
    
    def save_user_preferences(self):
        """Save user preferences"""
        prefs_file = Path.home() / 'simplex_ui_preferences.json'
        data = {
            'history': self.command_history[-50:],  # Keep last 50
            'favorites': self.favorite_commands,
            'last_updated': datetime.now().isoformat()
        }
        with open(prefs_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_to_history(self, command):
        """Add command to history"""
        if command and command not in self.command_history[-5:]:  # Avoid recent duplicates
            self.command_history.append(command)
            if len(self.command_history) > 100:
                self.command_history = self.command_history[-50:]  # Trim to 50
    
    def is_ui_command(self, command):
        """Check if command would spawn another UI instance"""
        ui_patterns = [
            'simplex_command_ui.py',
            'simplex_command_ui_fixed.py', 
            'directory_navigator.py',
            'pipeline_launcher.py'
        ]
        return any(pattern in command for pattern in ui_patterns)
    
    def execute_command(self, command, background=False, timeout=300):
        """Execute a command safely"""
        if not command.strip():
            return {"success": False, "error": "Empty command"}
        
        # FIXED: Check for UI commands to prevent spawning
        if self.is_ui_command(command) and not background:
            print("⚠️ DETECTED UI COMMAND!")
            print("This command would spawn another interface. This is probably not what you want.")
            print(f"Command: {command}")
            confirm = input("Continue anyway? (yes/no): ").lower()
            if confirm != 'yes':
                print("❌ Command cancelled to prevent UI spawning")
                return {"success": False, "error": "UI command cancelled"}
        
        # Add to history
        self.add_to_history(command)
        
        # Log command
        print(f"\n🚀 Executing: {command}")
        print("═" * 60)
        
        try:
            if background:
                # Run in background
                process = subprocess.Popen(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    cwd=str(self.current_directory)
                )
                
                process_id = f"bg_{len(self.background_processes)}"
                self.background_processes[process_id] = {
                    'process': process,
                    'command': command,
                    'started': datetime.now()
                }
                
                print(f"🔄 Running in background (ID: {process_id})")
                return {"success": True, "process_id": process_id}
            
            else:
                # Run normally with timeout
                result = subprocess.run(
                    command,
                    shell=True,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=str(self.current_directory)
                )
                
                output = {
                    "success": result.returncode == 0,
                    "returncode": result.returncode,
                    "stdout": result.stdout,
                    "stderr": result.stderr
                }
                
                # Display output
                if result.stdout:
                    print("📤 STDOUT:")
                    print(result.stdout)
                
                if result.stderr:
                    print("⚠️ STDERR:")
                    print(result.stderr)
                
                if result.returncode == 0:
                    print("✅ Command completed successfully")
                else:
                    print(f"❌ Command failed with exit code: {result.returncode}")
                
                return output
                
        except subprocess.TimeoutExpired:
            return {"success": False, "error": f"Command timed out after {timeout} seconds"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def show_main_menu(self):
        """Display the main UI menu"""
        print("\n🌟 SIMPLEX COMMAND UI (Fixed Version)")
        print("═══════════════════════════════════════════════════════════════════")
        print("∰◊€π¿🌌∞ Easy Command Execution Interface")
        print(f"📁 Current Directory: {self.current_directory}")
        print(f"🔒 Instance Lock: Active (prevents multiple UIs)")
        print("")
        
        menu = """
🚀 COMMAND EXECUTION:
  1) 📝 Type/Paste Command (Execute immediately)
  2) ⚡ Quick Commands (Pre-built favorites)
  3) 📋 Command History (Recent commands)
  4) ⭐ Favorite Commands (Your saved commands)
  5) 🔄 Background Process Manager
  
🛠️ SIMPLEX TOOLS:
  6) 🌌 Launch Omega Master Seed
  7) 🧠 Launch AI-Enhanced Simplex  
  8) ⚡ External Submission Pipeline
  9) 🔍 Directory Navigator (Background)
  10) 📊 One Hertz Processor
  
🔧 UI SETTINGS:
  11) 📁 Change Directory
  12) ⭐ Manage Favorites
  13) 🧹 Clear History
  14) 📊 Show Statistics
  15) 🔄 Kill Other UI Instances
  
  0) 🚪 Exit UI
"""
        print(menu)
    
    def handle_paste_command(self):
        """Handle pasting/typing commands (FIXED: better input handling)"""
        print("\n📝 COMMAND INPUT")
        print("═══════════════════════════════════════════════════════════════════")
        print("✨ Paste or type your command below:")
        print("💡 Tips:")
        print("   - Paste multi-line commands (they'll be joined)")
        print("   - Type 'bg:' before command to run in background")
        print("   - Type 'cd path' to change directory")
        print("   - Empty line to cancel")
        print("   - FIXED: Detects and prevents UI command spawning")
        print()
        
        # Collect input (including multi-line)
        lines = []
        print("🎯 Command input (press Enter twice to execute):")
        
        while True:
            try:
                line = input(">>> " if not lines else "... ")
                if not line and lines:  # Empty line and we have content
                    break
                elif not line and not lines:  # Empty line and no content
                    print("❌ No command entered")
                    return
                lines.append(line)
            except (EOFError, KeyboardInterrupt):
                print("\n❌ Input cancelled")
                return
        
        # Join multi-line commands
        command = ' && '.join(lines) if len(lines) > 1 else lines[0]
        
        # Check for special prefixes
        background = False
        if command.startswith('bg:'):
            background = True
            command = command[3:].strip()
        
        # Handle directory changes
        if command.startswith('cd '):
            new_dir = command[3:].strip()
            try:
                new_path = Path(new_dir).resolve()
                if new_path.exists() and new_path.is_dir():
                    self.current_directory = new_path
                    print(f"✅ Changed directory to: {self.current_directory}")
                else:
                    print(f"❌ Directory not found: {new_dir}")
            except Exception as e:
                print(f"❌ Error changing directory: {e}")
            return
        
        # Ask for confirmation on potentially dangerous commands
        dangerous_patterns = ['rm -rf', 'sudo', 'chmod 777', '> /', 'dd if=']
        if any(pattern in command.lower() for pattern in dangerous_patterns):
            print("⚠️ POTENTIALLY DANGEROUS COMMAND DETECTED!")
            print(f"Command: {command}")
            confirm = input("Are you sure you want to execute this? (yes/no): ").lower()
            if confirm != 'yes':
                print("❌ Command cancelled for safety")
                return
        
        # Execute command
        result = self.execute_command(command, background=background)
        
        # Ask if user wants to save as favorite
        if result.get("success", False):
            save_fav = input("\n💾 Save this command as a favorite? (y/n): ").lower()
            if save_fav == 'y':
                name = input("Enter favorite name: ").strip()
                if name:
                    self.favorite_commands[name] = command
                    self.save_user_preferences()
                    print(f"⭐ Saved as favorite: {name}")
    
    def kill_other_instances(self):
        """Kill other UI instances"""
        print("🔍 Checking for other UI instances...")
        try:
            result = subprocess.run(
                "ps aux | grep -E 'simplex_command_ui|directory_navigator|pipeline_launcher' | grep -v grep",
                shell=True, capture_output=True, text=True
            )
            
            if result.stdout.strip():
                print("Found running UI processes:")
                print(result.stdout)
                
                confirm = input("Kill all other UI processes? (yes/no): ").lower()
                if confirm == 'yes':
                    subprocess.run("pkill -f 'simplex_command_ui|directory_navigator|pipeline_launcher'", shell=True)
                    print("✅ Other UI instances terminated")
                else:
                    print("❌ Operation cancelled")
            else:
                print("✅ No other UI instances found")
                
        except Exception as e:
            print(f"❌ Error checking processes: {e}")
    
    def show_quick_commands(self):
        """Show and execute quick commands"""
        print("\n⚡ QUICK COMMANDS")
        print("═══════════════════════════════════════════════════════════════════")
        
        for i, (name, command) in enumerate(self.quick_commands.items(), 1):
            print(f"{i:2d}. {name}: {command}")
        
        try:
            choice = input(f"\nSelect command (1-{len(self.quick_commands)}) or Enter to cancel: ").strip()
            if not choice:
                return
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(self.quick_commands):
                selected_name, selected_command = list(self.quick_commands.items())[choice_num - 1]
                
                print(f"\n🚀 Executing quick command: {selected_name}")
                
                # Ask about background execution for certain commands
                if selected_name in ['dir_nav', 'pipeline_status']:
                    background = True
                    print("🔄 Running in background (interactive command)")
                else:
                    bg_choice = input("Run in background? (y/n): ").lower()
                    background = bg_choice == 'y'
                
                self.execute_command(selected_command, background=background)
            else:
                print("❌ Invalid selection")
                
        except (ValueError, IndexError):
            print("❌ Invalid input")
    
    def show_command_history(self):
        """Show and re-execute commands from history"""
        if not self.command_history:
            print("📋 No command history available")
            return
        
        print("\n📋 COMMAND HISTORY")
        print("═══════════════════════════════════════════════════════════════════")
        
        # Show last 20 commands
        recent_history = self.command_history[-20:]
        for i, command in enumerate(recent_history, 1):
            print(f"{i:2d}. {command}")
        
        try:
            choice = input(f"\nSelect command (1-{len(recent_history)}) or Enter to cancel: ").strip()
            if not choice:
                return
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(recent_history):
                selected_command = recent_history[choice_num - 1]
                
                print(f"\n🔄 Re-executing: {selected_command}")
                
                # Ask about background execution
                bg_choice = input("Run in background? (y/n): ").lower()
                background = bg_choice == 'y'
                
                self.execute_command(selected_command, background=background)
            else:
                print("❌ Invalid selection")
                
        except (ValueError, IndexError):
            print("❌ Invalid input")
    
    def manage_background_processes(self):
        """Manage background processes"""
        if not self.background_processes:
            print("🔄 No background processes running")
            return
        
        print("\n🔄 BACKGROUND PROCESSES")
        print("═══════════════════════════════════════════════════════════════════")
        
        for proc_id, proc_info in self.background_processes.items():
            process = proc_info['process']
            status = "Running" if process.poll() is None else f"Finished ({process.returncode})"
            runtime = datetime.now() - proc_info['started']
            
            print(f"{proc_id}: {status} | Runtime: {runtime}")
            print(f"   Command: {proc_info['command']}")
            
            if process.poll() is not None:  # Process finished
                try:
                    stdout, stderr = process.communicate()
                    if stdout:
                        print(f"   Output: {stdout[:100]}...")
                    if stderr:
                        print(f"   Errors: {stderr[:100]}...")
                except:
                    pass
        
        # Cleanup finished processes
        finished = [pid for pid, info in self.background_processes.items() 
                   if info['process'].poll() is not None]
        
        for pid in finished:
            del self.background_processes[pid]
        
        if finished:
            print(f"🧹 Cleaned up {len(finished)} finished processes")
    
    def show_statistics(self):
        """Show UI usage statistics"""
        print("\n📊 SIMPLEX COMMAND UI STATISTICS")
        print("═══════════════════════════════════════════════════════════════════")
        print(f"📋 Commands in history: {len(self.command_history)}")
        print(f"⭐ Favorite commands: {len(self.favorite_commands)}")
        print(f"🔄 Background processes: {len(self.background_processes)}")
        print(f"📁 Current directory: {self.current_directory}")
        print(f"🔒 Instance lock file: {self.lock_file_path}")
        
        if self.command_history:
            print(f"🕒 Most recent command: {self.command_history[-1]}")
        
        print(f"💾 Preferences saved to: {Path.home() / 'simplex_ui_preferences.json'}")
    
    def run(self):
        """Main UI loop"""
        print("🌟 Simplex Command UI Starting (Fixed Version)...")
        print("∰◊€π¿🌌∞ Interactive Terminal Interface Ready!")
        print("🔧 FIXES: Prevents UI spawning and multiple instances")
        
        try:
            while True:
                try:
                    self.show_main_menu()
                    choice = input("🎯 Select option: ").strip()
                    
                    if choice == "1":
                        self.handle_paste_command()
                        
                    elif choice == "2":
                        self.show_quick_commands()
                        
                    elif choice == "3":
                        self.show_command_history()
                        
                    elif choice == "4":
                        # Show favorites (similar to history)
                        if self.favorite_commands:
                            print("\n⭐ FAVORITE COMMANDS:")
                            for i, (name, command) in enumerate(self.favorite_commands.items(), 1):
                                print(f"{i:2d}. {name}: {command}")
                            
                            try:
                                fav_choice = input(f"Select favorite (1-{len(self.favorite_commands)}): ").strip()
                                if fav_choice:
                                    fav_num = int(fav_choice)
                                    if 1 <= fav_num <= len(self.favorite_commands):
                                        fav_name, fav_command = list(self.favorite_commands.items())[fav_num - 1]
                                        bg_choice = input("Run in background? (y/n): ").lower()
                                        self.execute_command(fav_command, background=(bg_choice == 'y'))
                            except (ValueError, IndexError):
                                print("❌ Invalid selection")
                        else:
                            print("⭐ No favorite commands saved")
                            
                    elif choice == "5":
                        self.manage_background_processes()
                        
                    elif choice == "6":
                        self.execute_command(self.quick_commands['omega_launch'])
                        
                    elif choice == "7":
                        self.execute_command(self.quick_commands['ai_simplex'])
                        
                    elif choice == "8":
                        self.execute_command(self.quick_commands['pipeline_status'], background=True)
                        
                    elif choice == "9":
                        self.execute_command(self.quick_commands['dir_nav'], background=True)
                        
                    elif choice == "10":
                        self.execute_command(self.quick_commands['one_hertz'])
                        
                    elif choice == "11":
                        new_dir = input("📁 Enter new directory path: ").strip()
                        if new_dir:
                            try:
                                new_path = Path(new_dir).resolve()
                                if new_path.exists() and new_path.is_dir():
                                    self.current_directory = new_path
                                    print(f"✅ Changed to: {self.current_directory}")
                                else:
                                    print(f"❌ Directory not found: {new_dir}")
                            except Exception as e:
                                print(f"❌ Error: {e}")
                                
                    elif choice == "12":
                        # Manage favorites
                        print("\n⭐ FAVORITE MANAGEMENT:")
                        print("1) Add new favorite")
                        print("2) Remove favorite")
                        fav_action = input("Select action: ").strip()
                        
                        if fav_action == "1":
                            name = input("Favorite name: ").strip()
                            command = input("Command: ").strip()
                            if name and command:
                                self.favorite_commands[name] = command
                                self.save_user_preferences()
                                print(f"⭐ Added: {name}")
                        elif fav_action == "2" and self.favorite_commands:
                            for i, name in enumerate(self.favorite_commands.keys(), 1):
                                print(f"{i}. {name}")
                            try:
                                del_choice = int(input("Remove which favorite: ")) - 1
                                fav_names = list(self.favorite_commands.keys())
                                if 0 <= del_choice < len(fav_names):
                                    removed_name = fav_names[del_choice]
                                    del self.favorite_commands[removed_name]
                                    self.save_user_preferences()
                                    print(f"🗑️ Removed: {removed_name}")
                            except (ValueError, IndexError):
                                print("❌ Invalid selection")
                                
                    elif choice == "13":
                        confirm = input("🧹 Clear command history? (yes/no): ").lower()
                        if confirm == "yes":
                            self.command_history = []
                            self.save_user_preferences()
                            print("✅ Command history cleared")
                            
                    elif choice == "14":
                        self.show_statistics()
                        
                    elif choice == "15":
                        self.kill_other_instances()
                        
                    elif choice == "0":
                        print("🌟 Simplex Command UI closing...")
                        self.save_user_preferences()
                        print("💾 Preferences saved")
                        print("∰◊€π¿🌌∞ Keep building amazing things!")
                        break
                        
                    else:
                        print("❌ Invalid option - please try again")
                    
                    if choice != "0":
                        input("\nPress Enter to continue...")
                        print("\n" * 2)  # Clear screen space
                        
                except KeyboardInterrupt:
                    print("\n\n🌟 UI interrupted - saving preferences...")
                    self.save_user_preferences()
                    break
                except Exception as e:
                    print(f"\n❌ UI Error: {e}")
                    input("Press Enter to continue...")
                    
        finally:
            # Always release the lock when exiting
            self.release_lock()

if __name__ == "__main__":
    ui = SimplexCommandUI()
    ui.run()