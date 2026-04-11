#!/usr/bin/env python3
"""
Email Account Universe Discovery
Scan for email accounts and potential cloud storage connections
"""

import re
import os
import json

class EmailUniverseDiscovery:
    """Discover email accounts and associated cloud services"""
    
    def __init__(self):
        self.email_domains = {
            'gmail.com': ['Google Drive', 'Google Photos', 'YouTube'],
            'outlook.com': ['OneDrive', 'Office 365'],
            'hotmail.com': ['OneDrive', 'Office 365'], 
            'yahoo.com': ['Yahoo Mail', 'Flickr'],
            'icloud.com': ['iCloud Drive', 'iCloud Photos'],
            'protonmail.com': ['ProtonDrive'],
            'aol.com': ['AOL Services']
        }
        
        self.cloud_providers = [
            'dropbox', 'box', 'mega', 'amazon', 'aws', 'azure',
            'github', 'gitlab', 'bitbucket', 'sourceforge'
        ]
    
    def scan_email_patterns(self, text_content):
        """Scan text for email addresses and associated services"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails_found = re.findall(email_pattern, text_content)
        
        discovered_accounts = {}
        for email in emails_found:
            domain = email.split('@')[1].lower()
            discovered_accounts[email] = {
                'domain': domain,
                'potential_services': self.email_domains.get(domain, ['Unknown']),
                'cloud_potential': any(provider in email.lower() for provider in self.cloud_providers)
            }
        
        return discovered_accounts
    
    def generate_discovery_report(self, discovered_accounts):
        """Generate report of discovered email accounts and services"""
        print("\n📧 EMAIL UNIVERSE DISCOVERY REPORT")
        print("=" * 50)
        
        for email, info in discovered_accounts.items():
            print(f"\n📫 {email}")
            print(f"   Domain: {info['domain']}")
            print(f"   Services: {', '.join(info['potential_services'])}")
            if info['cloud_potential']:
                print(f"   ☁️ Cloud storage potential detected")

if __name__ == "__main__":
    discoverer = EmailUniverseDiscovery()
    
    # Example usage - could be expanded to scan actual files
    sample_text = """
    Contact me at eric@gmail.com or backup@dropbox.com
    Also try the-project@outlook.com for collaborative work
    """
    
    accounts = discoverer.scan_email_patterns(sample_text)
    discoverer.generate_discovery_report(accounts)
