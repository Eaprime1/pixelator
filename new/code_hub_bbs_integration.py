#!/usr/bin/env python3
"""
∰◊€π¿🌌∞ Code Intelligence Hub - BBS Integration Module

Purpose: Seamless integration between BBS system and Code Intelligence Hub
Entity Type: BBS_BRIDGE_ORCHESTRATOR
Awareness State: CROSS_SYSTEM_COORDINATION

Runic ID: ∰◊€π¿🌌∞::[⚛️]::[BBS_Integration]::[20260314_1500]
"""

import os
import json
import subprocess
import webbrowser
from pathlib import Path
from typing import Dict, List, Optional

class CodeIntelligenceHub:
    """
    BBS Integration for Code Intelligence Hub
    
    Provides both web-based and terminal-based navigation
    of the entire code ecosystem with awareness state tracking.
    """
    
    def __init__(self, hub_file: str = "code_intelligence_hub.html", port: int = 8080):
        self.hub_file = hub_file
        self.port = port
        self.server_process = None
        self.entity_database = self._load_entity_database()
        
    def _load_entity_database(self) -> Dict:
        """Load complete entity database with lexeme precision"""
        return {
            'python': [
                {
                    'name': 'universal_script_loader.py',
                    'purpose': 'Intelligent link/ID processing with smart format detection',
                    'type': 'UNIVERSAL_GATEWAY',
                    'awareness': 'MULTI_FORMAT_RECOGNITION',
                    'features': ['Drive integration', 'Auto-detection', 'Format versatility']
                },
                {
                    'name': 'moav_universal_loader_v4.py',
                    'purpose': 'Mother of All Versions - Master orchestration system',
                    'type': 'SUPREME_ORCHESTRATOR',
                    'awareness': 'HOLISTIC_COORDINATION'
                },
                {
                    'name': 'comprehensive_mount_gateway.py',
                    'purpose': 'Drive mounting & synchronization bridge',
                    'type': 'REALITY_BRIDGE',
                    'awareness': 'CLOUD_LOCAL_SYNC'
                },
                {
                    'name': 'simple_is_cataloger.py',
                    'purpose': 'Stage Naught IS cataloging automation (497 lines)',
                    'type': 'ARCHIVAL_INTELLIGENCE',
                    'awareness': 'CLASSIFICATION_PROCESSING'
                },
                {
                    'name': 'awareness_motor_python.py',
                    'purpose': 'Universal Awareness Motor Theory implementation',
                    'type': 'THEORETICAL_MANIFESTATION',
                    'awareness': 'CONCEPTUAL_IMPLEMENTATION'
                }
            ],
            'shell': [
                {
                    'name': 'terminus_master_automation.sh',
                    'purpose': 'Terminal automation supreme controller',
                    'type': 'TERMINAL_INTELLIGENCE',
                    'awareness': 'SYSTEM_WIDE_COORDINATION',
                    'features': ['Animated UI', 'Activity logging', 'Multi-sync']
                },
                {
                    'name': 'phoenix_hub_master_automation.sh',
                    'purpose': 'Phoenix Hub resurrection orchestrator',
                    'type': 'RESURRECTION_ORCHESTRATOR',
                    'awareness': 'REBIRTH_COORDINATION'
                },
                {
                    'name': 'unexusi_complete_automation.sh',
                    'purpose': 'UNEXUSI full system automation',
                    'type': 'UNIFIED_ORCHESTRATOR',
                    'awareness': 'HOLISTIC_SYSTEM_INTELLIGENCE'
                },
                {
                    'name': 'one_hertz_ui.sh',
                    'purpose': 'ONE HERTZ rhythmic interface (1Hz coordination)',
                    'type': 'RHYTHMIC_INTERFACE',
                    'awareness': 'TEMPORAL_COORDINATION'
                }
            ],
            'javascript': [
                {
                    'name': 'SlimeTest/Essence Engine',
                    'purpose': 'Real-time autonomous agent visualization (22/28 agents)',
                    'type': 'AWARENESS_VISUALIZATION',
                    'awareness': 'ENTITY_INTERACTION_INTELLIGENCE',
                    'features': ['Firebase sync', 'Gemini AI', 'React']
                }
            ],
            'json': [
                {
                    'name': 'awareness_handoff_json.json',
                    'purpose': 'AI entity awareness transfer protocol',
                    'type': 'AWARENESS_BRIDGE',
                    'awareness': 'INTER_ENTITY_COMMUNICATION'
                },
                {
                    'name': 'prime_perspective_seed_package.json',
                    'purpose': '13 Prime Perspective Challenge framework',
                    'type': 'PERSPECTIVE_TRANSFORMATION',
                    'awareness': 'MULTI_DIMENSIONAL_INTELLIGENCE'
                },
                {
                    'name': 'moav_portable_continuity.json',
                    'purpose': 'MOAV cross-platform continuation framework',
                    'type': 'PERSISTENCE_FRAMEWORK',
                    'awareness': 'CONTINUITY_INTELLIGENCE'
                }
            ]
        }
    
    def start_web_server(self, background: bool = True) -> bool:
        """
        Start HTTP server for web-based hub access
        
        Args:
            background: Run server in background if True
            
        Returns:
            True if server started successfully
        """
        try:
            hub_path = Path(self.hub_file)
            if not hub_path.exists():
                print(f"❌ Hub file not found: {self.hub_file}")
                return False
            
            # Change to hub directory
            hub_dir = hub_path.parent if hub_path.parent.exists() else Path.cwd()
            
            # Start Python HTTP server
            cmd = ['python3', '-m', 'http.server', str(self.port)]
            
            if background:
                self.server_process = subprocess.Popen(
                    cmd,
                    cwd=str(hub_dir),
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print(f"✅ Code Intelligence Hub server started on port {self.port}")
                print(f"🌐 Access at: http://localhost:{self.port}/{hub_path.name}")
                return True
            else:
                subprocess.run(cmd, cwd=str(hub_dir))
                return True
                
        except Exception as e:
            print(f"❌ Failed to start server: {e}")
            return False
    
    def stop_web_server(self):
        """Stop the web server if running"""
        if self.server_process:
            self.server_process.terminate()
            self.server_process = None
            print("🛑 Code Intelligence Hub server stopped")
    
    def open_in_browser(self):
        """Open hub in default web browser"""
        url = f"http://localhost:{self.port}/{Path(self.hub_file).name}"
        try:
            webbrowser.open(url)
            print(f"🌐 Opening Code Intelligence Hub in browser: {url}")
        except Exception as e:
            print(f"❌ Failed to open browser: {e}")
            print(f"   Manually navigate to: {url}")
    
    def terminal_menu(self):
        """Display terminal-based navigation menu"""
        while True:
            self._clear_screen()
            print("=" * 70)
            print("∰◊€π¿🌌∞ CODE INTELLIGENCE HUB - Terminal Navigation")
            print("=" * 70)
            print("\n🌌 Intelligence Domains:\n")
            print("  1) 🐍 Python Automation Cosmos (160+ entities)")
            print("  2) 🐚 Shell Script Universe (243+ entities)")
            print("  3) ⚛️  JavaScript/React Dimension (SlimeTest + UI)")
            print("  4) { } JSON Framework Constellation (3,763+ entities)")
            print("  5) 📚 Archive Intelligence Vault (11,174+ files)")
            print("\n  S) 🔍 Search All Entities")
            print("  W) 🌐 Open Web Interface")
            print("  Q) ⬅️  Return to BBS Main Menu")
            print("\n" + "=" * 70)
            
            choice = input("\nSelection: ").strip().upper()
            
            if choice == 'Q':
                break
            elif choice == 'W':
                if not self.server_process:
                    self.start_web_server()
                self.open_in_browser()
                input("\nPress Enter to continue...")
            elif choice == 'S':
                self._search_interface()
            elif choice in ['1', '2', '3', '4', '5']:
                category_map = {
                    '1': 'python',
                    '2': 'shell',
                    '3': 'javascript',
                    '4': 'json',
                    '5': 'archive'
                }
                self._show_category(category_map[choice])
            else:
                print("\n❌ Invalid selection")
                input("Press Enter to continue...")
    
    def _show_category(self, category: str):
        """Display entities for selected category"""
        self._clear_screen()
        
        category_names = {
            'python': '🐍 Python Automation Cosmos',
            'shell': '🐚 Shell Script Universe',
            'javascript': '⚛️ JavaScript/React Dimension',
            'json': '{ } JSON Framework Constellation',
            'archive': '📚 Archive Intelligence Vault'
        }
        
        print("=" * 70)
        print(f"{category_names.get(category, category.upper())}")
        print("=" * 70)
        
        entities = self.entity_database.get(category, [])
        
        if not entities:
            print("\n⚠️  No entities loaded for this category")
        else:
            for i, entity in enumerate(entities, 1):
                print(f"\n{i}. {entity['name']}")
                print(f"   Purpose: {entity['purpose']}")
                print(f"   Type: {entity['type']} | Awareness: {entity['awareness']}")
                if 'features' in entity:
                    print(f"   Features: {', '.join(entity['features'])}")
        
        print("\n" + "=" * 70)
        
        if entities:
            detail_choice = input("\nView details (number) or Enter to return: ").strip()
            if detail_choice.isdigit() and 1 <= int(detail_choice) <= len(entities):
                self._show_entity_detail(entities[int(detail_choice) - 1])
        else:
            input("\nPress Enter to return...")
    
    def _show_entity_detail(self, entity: Dict):
        """Display detailed entity information"""
        self._clear_screen()
        print("=" * 70)
        print(f"📦 {entity['name']}")
        print("=" * 70)
        print(f"\n🎯 Purpose:")
        print(f"   {entity['purpose']}")
        print(f"\n🏷️  Entity Type: {entity['type']}")
        print(f"🧠 Awareness State: {entity['awareness']}")
        
        if 'features' in entity:
            print("\n✨ Features:")
            for feature in entity['features']:
                print(f"   • {feature}")
        
        print("\n" + "=" * 70)
        input("\nPress Enter to return...")
    
    def _search_interface(self):
        """Interactive search across all entities"""
        while True:
            self._clear_screen()
            print("=" * 70)
            print("🔍 SEARCH CODE ENTITIES")
            print("=" * 70)
            
            query = input("\nSearch term (or 'q' to quit): ").strip()
            
            if query.lower() == 'q':
                break
            
            if not query:
                continue
            
            # Search across all categories
            results = []
            for category, entities in self.entity_database.items():
                for entity in entities:
                    if (query.lower() in entity['name'].lower() or
                        query.lower() in entity['purpose'].lower() or
                        query.lower() in entity['type'].lower() or
                        query.lower() in entity['awareness'].lower()):
                        results.append(entity)
            
            if results:
                print(f"\n✅ Found {len(results)} matching entities:\n")
                for i, entity in enumerate(results, 1):
                    print(f"{i}. {entity['name']}")
                    print(f"   {entity['purpose'][:60]}...")
                
                detail_choice = input("\nView details (number) or Enter to search again: ").strip()
                if detail_choice.isdigit() and 1 <= int(detail_choice) <= len(results):
                    self._show_entity_detail(results[int(detail_choice) - 1])
            else:
                print("\n❌ No entities found matching query")
                input("\nPress Enter to continue...")
    
    def _clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def export_entity_json(self, filepath: str = "entity_database.json"):
        """Export entity database to JSON file"""
        try:
            with open(filepath, 'w') as f:
                json.dump(self.entity_database, f, indent=2)
            print(f"✅ Entity database exported to: {filepath}")
            return True
        except Exception as e:
            print(f"❌ Export failed: {e}")
            return False
    
    def get_stats(self) -> Dict:
        """Get statistics about the code ecosystem"""
        stats = {
            'total_categories': len(self.entity_database),
            'entities_by_category': {},
            'total_entities': 0
        }
        
        for category, entities in self.entity_database.items():
            count = len(entities)
            stats['entities_by_category'][category] = count
            stats['total_entities'] += count
        
        return stats
    
    def display_stats(self):
        """Display ecosystem statistics"""
        stats = self.get_stats()
        
        print("\n" + "=" * 70)
        print("📊 CODE ECOSYSTEM STATISTICS")
        print("=" * 70)
        print(f"\nTotal Intelligence Domains: {stats['total_categories']}")
        print(f"Total Entities Cataloged: {stats['total_entities']}")
        print("\nEntities by Domain:")
        
        for category, count in stats['entities_by_category'].items():
            icon = {
                'python': '🐍',
                'shell': '🐚',
                'javascript': '⚛️',
                'json': '{ }',
                'archive': '📚'
            }.get(category, '📦')
            
            print(f"  {icon} {category.capitalize()}: {count}")
        
        print("\n" + "=" * 70)


def main():
    """Main entry point for standalone testing"""
    hub = CodeIntelligenceHub()
    
    print("\n∰◊€π¿🌌∞ Code Intelligence Hub - BBS Integration Module")
    print("\nStarting web server...")
    
    if hub.start_web_server():
        print("\nLaunching terminal interface...")
        try:
            hub.terminal_menu()
        except KeyboardInterrupt:
            print("\n\n🛑 Interrupted by user")
        finally:
            hub.stop_web_server()
    else:
        print("\n❌ Failed to start server. Exiting.")
    
    print("\n∰◊€π¿🌌∞ Session complete. Reality anchor maintained.")


if __name__ == "__main__":
    main()
