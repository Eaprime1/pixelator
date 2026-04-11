#!/usr/bin/env python3
"""
Simple File Finder for Simplex AI Development
Quick search tool for finding AI-related code and documents
"""

import os
import fnmatch
from pathlib import Path

def find_files(search_terms, root_dir=None, max_results=50):
    """Find files matching search terms"""
    root_dir = root_dir or Path.home()
    results = []
    
    # Convert single string to list
    if isinstance(search_terms, str):
        search_terms = [search_terms]
    
    print(f"🔍 Searching in: {root_dir}")
    print(f"🎯 Looking for: {', '.join(search_terms)}")
    print("-" * 50)
    
    try:
        for root, dirs, files in os.walk(root_dir):
            # Skip hidden and cache directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]
            
            root_path = Path(root)
            
            # Check directories
            for dir_name in dirs:
                for term in search_terms:
                    if term.lower() in dir_name.lower():
                        results.append({
                            'type': 'directory',
                            'path': root_path / dir_name,
                            'name': dir_name,
                            'match': term
                        })
            
            # Check files
            for file_name in files:
                for term in search_terms:
                    if term.lower() in file_name.lower():
                        file_path = root_path / file_name
                        try:
                            size = file_path.stat().st_size
                            results.append({
                                'type': 'file',
                                'path': file_path,
                                'name': file_name,
                                'match': term,
                                'size': size
                            })
                        except:
                            pass
            
            if len(results) >= max_results:
                break
                
    except PermissionError as e:
        print(f"❌ Permission denied: {e}")
    except Exception as e:
        print(f"❌ Search error: {e}")
    
    return results[:max_results]

def format_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024**2:
        return f"{size_bytes/1024:.1f}KB"
    elif size_bytes < 1024**3:
        return f"{size_bytes/(1024**2):.1f}MB"
    else:
        return f"{size_bytes/(1024**3):.1f}GB"

def display_results(results):
    """Display search results in organized format"""
    if not results:
        print("❌ No matches found")
        return
    
    # Separate by type
    directories = [r for r in results if r['type'] == 'directory']
    files = [r for r in results if r['type'] == 'file']
    
    if directories:
        print(f"\n📁 DIRECTORIES ({len(directories)}):")
        for result in directories:
            print(f"   📁 {result['path']}")
    
    if files:
        print(f"\n📄 FILES ({len(files)}):")
        for result in files:
            size_str = format_size(result['size']) if 'size' in result else "?"
            print(f"   📄 {result['path']} ({size_str})")
    
    print(f"\n📊 Total results: {len(results)}")

if __name__ == "__main__":
    print("🤖 Simple File Finder for Simplex AI")
    print("=" * 50)
    
    # Search for AI-related terms
    ai_terms = ['simplex', 'ai', 'neural', 'omega', 'consciousness', 'phoenix']
    
    print("🔍 Searching for AI/Simplex related files...")
    results = find_files(ai_terms, max_results=30)
    display_results(results)
    
    print("\n" + "=" * 50)
    print("💡 To search specific terms, edit the script or run:")
    print("   python3 simple_file_finder.py")