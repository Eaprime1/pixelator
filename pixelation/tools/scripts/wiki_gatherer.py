#!/usr/bin/env python3
"""
Universal Wiki Data Gatherer
Collect knowledge from Wikipedia and other wiki sources
"""

import requests
import json
import os
from urllib.parse import quote

class WikiUniverseGatherer:
    """Gather comprehensive wiki data for any entity"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'WikiUniverseGatherer/1.0 (Educational Research)'
        })
    
    def get_wikipedia_data(self, term):
        """Get comprehensive Wikipedia data for a term"""
        base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
        url = base_url + quote(term)
        
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"❌ Wikipedia error for '{term}': {e}")
        return None
    
    def get_wiktionary_data(self, term):
        """Get Wiktionary dictionary data"""
        base_url = "https://en.wiktionary.org/api/rest_v1/page/summary/"
        url = base_url + quote(term)
        
        try:
            response = self.session.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"❌ Wiktionary error for '{term}': {e}")
        return None
    
    def gather_entity_knowledge(self, entity_name, output_dir="wikis"):
        """Gather comprehensive knowledge about an entity"""
        print(f"📚 Gathering knowledge for: {entity_name}")
        
        os.makedirs(output_dir, exist_ok=True)
        
        knowledge_package = {
            "entity": entity_name,
            "wikipedia": self.get_wikipedia_data(entity_name),
            "wiktionary": self.get_wiktionary_data(entity_name),
            "gathered_at": str(datetime.now())
        }
        
        output_file = os.path.join(output_dir, f"{entity_name.replace(' ', '_')}_knowledge.json")
        with open(output_file, 'w') as f:
            json.dump(knowledge_package, f, indent=2)
        
        print(f"✅ Knowledge saved: {output_file}")
        return knowledge_package

if __name__ == "__main__":
    import sys
    from datetime import datetime
    
    if len(sys.argv) < 2:
        print("Usage: python wiki_gatherer.py <entity_name>")
        sys.exit(1)
    
    entity = " ".join(sys.argv[1:])
    gatherer = WikiUniverseGatherer()
    gatherer.gather_entity_knowledge(entity)
