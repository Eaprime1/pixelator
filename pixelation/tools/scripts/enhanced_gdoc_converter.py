#!/usr/bin/env python3
"""
Enhanced Google Drive TXT to Google Docs Converter
Converts TXT files to Google Docs with comprehensive reporting and error handling
"""

from __future__ import print_function
import os
import sys
import json
import time
import traceback
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# ---- CONFIG ----
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/documents']
SERVICE_ACCOUNT_FILE = '/storage/emulated/0/unexusi/service_account.json'

class GDocConverter:
    def __init__(self):
        self.service = self.authenticate()
        self.conversion_log = {
            'timestamp': datetime.now().isoformat(),
            'successful_conversions': [],
            'failed_conversions': [],
            'skipped_files': [],
            'summary': {}
        }
        
    def authenticate(self):
        """Authenticate with Google Drive API"""
        try:
            creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            return build('drive', 'v3', credentials=creds)
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            sys.exit(1)

    def find_or_create_folder(self, parent_id, folder_name):
        """Find existing folder or create new one"""
        try:
            # Search for the folder
            query = f"'{parent_id}' in parents and name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
            results = self.service.files().list(q=query, spaces='drive').execute()
            files = results.get('files', [])
            
            if files:
                print(f"📁 Found existing folder: {folder_name}")
                return files[0]['id']
                
            # Create if missing
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_id]
            }
            file = self.service.files().create(body=file_metadata, fields='id').execute()
            print(f"📁 Created new folder: {folder_name}")
            return file.get('id')
            
        except HttpError as e:
            print(f"❌ Error with folder {folder_name}: {e}")
            return None

    def get_file_info(self, file_id):
        """Get detailed file information"""
        try:
            return self.service.files().get(fileId=file_id, fields='id,name,mimeType,size,parents,createdTime,modifiedTime').execute()
        except HttpError as e:
            print(f"❌ Error getting file info: {e}")
            return None

    def convert_txt_to_gdoc(self, source_file, target_folder_id):
        """Convert a single TXT file to Google Doc"""
        file_id = source_file['id']
        name = source_file['name']
        
        try:
            # Create safe filename for Google Doc
            gdoc_name = name.replace('.txt', '').replace('.TXT', '')
            if not gdoc_name:
                gdoc_name = f"Converted_Document_{file_id[:8]}"
                
            print(f"🔄 Converting: {name}")
            
            # Download the txt file content
            request = self.service.files().get_media(fileId=file_id)
            content = request.execute()
            
            # Validate content
            try:
                text_content = content.decode('utf-8')
            except UnicodeDecodeError:
                try:
                    text_content = content.decode('latin-1')
                except UnicodeDecodeError:
                    raise Exception("Unable to decode file content")
            
            if len(text_content.strip()) == 0:
                raise Exception("File appears to be empty")
                
            # Save temporarily for upload
            temp_path = f"/tmp/{name}"
            with open(temp_path, 'w', encoding='utf-8') as temp_file:
                temp_file.write(text_content)
            
            # Create Google Doc
            file_metadata = {
                'name': gdoc_name,
                'mimeType': 'application/vnd.google-apps.document',
                'parents': [target_folder_id]
            }
            
            media = MediaFileUpload(temp_path, mimetype='text/plain')
            result = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id,name,webViewLink'
            ).execute()
            
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            # Log success
            conversion_info = {
                'original_name': name,
                'original_id': file_id,
                'gdoc_name': gdoc_name,
                'gdoc_id': result.get('id'),
                'gdoc_link': result.get('webViewLink'),
                'size_bytes': source_file.get('size', 'unknown'),
                'converted_at': datetime.now().isoformat()
            }
            
            self.conversion_log['successful_conversions'].append(conversion_info)
            print(f"✅ Successfully converted: {gdoc_name} (ID: {result.get('id')})")
            
            return True
            
        except Exception as e:
            # Log failure
            error_info = {
                'original_name': name,
                'original_id': file_id,
                'error': str(e),
                'error_type': type(e).__name__,
                'failed_at': datetime.now().isoformat()
            }
            
            self.conversion_log['failed_conversions'].append(error_info)
            print(f"❌ Failed to convert {name}: {e}")
            return False

    def move_problem_file(self, source_file, vetting_folder_id):
        """Move problematic file to vetting folder"""
        try:
            file_id = source_file['id']
            current_parents = source_file.get('parents', [])
            
            # Move file to vetting folder
            self.service.files().update(
                fileId=file_id,
                addParents=vetting_folder_id,
                removeParents=','.join(current_parents)
            ).execute()
            
            print(f"📋 Moved problem file to vetting: {source_file['name']}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to move file to vetting: {e}")
            return False

    def generate_inventory_report(self, source_folder_id):
        """Generate comprehensive inventory report"""
        try:
            report_content = {
                'conversion_session': self.conversion_log,
                'folder_analysis': {
                    'source_folder_id': source_folder_id,
                    'total_files_processed': len(self.conversion_log['successful_conversions']) + len(self.conversion_log['failed_conversions']),
                    'successful_conversions': len(self.conversion_log['successful_conversions']),
                    'failed_conversions': len(self.conversion_log['failed_conversions']),
                    'success_rate': 0 if not self.conversion_log['successful_conversions'] else 
                                   len(self.conversion_log['successful_conversions']) / 
                                   (len(self.conversion_log['successful_conversions']) + len(self.conversion_log['failed_conversions'])) * 100
                }
            }
            
            # Create reports folder
            reports_folder_id = self.find_or_create_folder(source_folder_id, "reports")
            if not reports_folder_id:
                return False
                
            # Generate report filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_name = f"conversion_report_{timestamp}"
            
            # Save report locally first
            local_report_path = f"/tmp/{report_name}.json"
            with open(local_report_path, 'w') as f:
                json.dump(report_content, f, indent=2, ensure_ascii=False)
            
            # Upload report to Google Drive
            file_metadata = {
                'name': f"{report_name}.json",
                'parents': [reports_folder_id]
            }
            
            media = MediaFileUpload(local_report_path, mimetype='application/json')
            report_file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id,webViewLink'
            ).execute()
            
            # Create human-readable summary
            summary_content = f"""SCAT Document Conversion Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

SUMMARY:
========
Total files processed: {report_content['folder_analysis']['total_files_processed']}
Successful conversions: {report_content['folder_analysis']['successful_conversions']}
Failed conversions: {report_content['folder_analysis']['failed_conversions']}
Success rate: {report_content['folder_analysis']['success_rate']:.1f}%

SUCCESSFUL CONVERSIONS:
======================
"""
            
            for conv in self.conversion_log['successful_conversions']:
                summary_content += f"✅ {conv['original_name']} → {conv['gdoc_name']}\n"
                summary_content += f"   Google Doc ID: {conv['gdoc_id']}\n"
                summary_content += f"   Link: {conv['gdoc_link']}\n\n"
            
            if self.conversion_log['failed_conversions']:
                summary_content += "\nFAILED CONVERSIONS:\n==================\n"
                for fail in self.conversion_log['failed_conversions']:
                    summary_content += f"❌ {fail['original_name']}\n"
                    summary_content += f"   Error: {fail['error']}\n\n"
            
            # Save and upload summary
            summary_path = f"/tmp/{report_name}_summary.txt"
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(summary_content)
                
            file_metadata = {
                'name': f"{report_name}_summary.txt",
                'parents': [reports_folder_id]
            }
            
            media = MediaFileUpload(summary_path, mimetype='text/plain')
            self.service.files().create(
                body=file_metadata,
                media_body=media
            ).execute()
            
            # Clean up temp files
            if os.path.exists(local_report_path):
                os.remove(local_report_path)
            if os.path.exists(summary_path):
                os.remove(summary_path)
                
            print(f"📊 Generated inventory report: {report_name}")
            print(f"🔗 Report link: {report_file.get('webViewLink')}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to generate inventory report: {e}")
            return False

    def process_folder(self, folder_id):
        """Main processing function"""
        print(f"🚀 Starting conversion process for folder: {folder_id}")
        
        try:
            # Create necessary folders
            que_gdoc_upload_id = self.find_or_create_folder(folder_id, "que_gdoc_upload")
            vetting_folder_id = self.find_or_create_folder(folder_id, "vetting")
            
            if not que_gdoc_upload_id or not vetting_folder_id:
                print("❌ Failed to create required folders")
                return False
            
            # Find all TXT files in the source folder
            query = f"'{folder_id}' in parents and (mimeType='text/plain' or name contains '.txt' or name contains '.TXT') and trashed=false"
            results = self.service.files().list(
                q=query,
                fields='files(id,name,mimeType,size,parents)',
                spaces='drive'
            ).execute()
            
            files = results.get('files', [])
            
            if not files:
                print("📝 No TXT files found in the source folder")
                return True
                
            print(f"📂 Found {len(files)} TXT files to process")
            
            # Process each file
            for file_info in files:
                success = self.convert_txt_to_gdoc(file_info, que_gdoc_upload_id)
                
                # Move failed files to vetting folder
                if not success:
                    self.move_problem_file(file_info, vetting_folder_id)
                    
                # Small delay to avoid API rate limits
                time.sleep(0.5)
            
            # Generate inventory report
            self.generate_inventory_report(folder_id)
            
            # Print final summary
            successful = len(self.conversion_log['successful_conversions'])
            failed = len(self.conversion_log['failed_conversions'])
            total = successful + failed
            
            print("\n" + "="*50)
            print("🎯 CONVERSION COMPLETE")
            print("="*50)
            print(f"📊 Total processed: {total}")
            print(f"✅ Successful: {successful}")
            print(f"❌ Failed: {failed}")
            print(f"📈 Success rate: {(successful/total*100 if total > 0 else 0):.1f}%")
            print(f"📁 Converted docs in: que_gdoc_upload")
            print(f"📋 Problem docs in: vetting")
            print(f"📊 Reports in: reports")
            print("="*50)
            
            return True
            
        except Exception as e:
            print(f"❌ Critical error in processing: {e}")
            traceback.print_exc()
            return False

def extract_folder_id(url_or_id):
    """Extract folder ID from Google Drive URL or return if already an ID"""
    if 'drive.google.com' in url_or_id:
        if '/folders/' in url_or_id:
            return url_or_id.split('/folders/')[1].split('?')[0].split('/')[0]
        elif 'id=' in url_or_id:
            return url_or_id.split('id=')[1].split('&')[0]
    return url_or_id

def main():
    if len(sys.argv) < 2:
        print("Usage: python enhanced_gdoc_converter.py <folder_id_or_url>")
        print("\nExamples:")
        print("  python enhanced_gdoc_converter.py 1GvlsBNxnhDcMbAW5W9bO0h-CsFV-NSKp")
        print("  python enhanced_gdoc_converter.py https://drive.google.com/drive/folders/1GvlsBNxnhDcMbAW5W9bO0h-CsFV-NSKp")
        sys.exit(1)
    
    folder_input = sys.argv[1]
    folder_id = extract_folder_id(folder_input)
    
    print(f"🔍 Processing folder ID: {folder_id}")
    
    converter = GDocConverter()
    success = converter.process_folder(folder_id)
    
    if success:
        print("🎉 Process completed successfully!")
    else:
        print("💥 Process completed with errors")
        sys.exit(1)

if __name__ == '__main__':
    main()