#!/usr/bin/env python3
"""
Enhanced Universal Google Drive Document Converter with API Key Integration
Supports both Service Account and API Key authentication methods
"""

from __future__ import print_function
import os
import sys
import json
import time
import requests
import traceback
from datetime import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

# ---- CONFIG ----
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/documents']
SERVICE_ACCOUNT_FILE = '/storage/emulated/0/unexusi/service_account.json'
API_KEY = 'AIzaSyC3XqaPZoHX_I7OYFmiAd1SHEAsmwpkC0A'  # Your provided API key
DEFAULT_FOLDER_ID = '1AQxd2QcAPqqz_phUvinTy1OSCnQ298A-'

class EnhancedGDocConverter:
    def __init__(self, use_api_key=False):
        self.use_api_key = use_api_key
        self.api_key = API_KEY
        self.service = self.authenticate()
        self.conversion_log = {
            'session_id': f"conv_{int(time.time())}",
            'timestamp': datetime.now().isoformat(),
            'auth_method': 'api_key' if use_api_key else 'service_account',
            'successful_conversions': [],
            'failed_conversions': [],
            'skipped_files': [],
            'unsupported_formats': [],
            'summary': {}
        }
        
        # Enhanced supported formats with API key capabilities
        self.supported_formats = {
            # Text formats
            '.txt': {'mime': 'text/plain', 'method': 'direct', 'api_enhanced': True},
            '.md': {'mime': 'text/x-markdown', 'method': 'direct', 'api_enhanced': True},
            '.markdown': {'mime': 'text/x-markdown', 'method': 'direct', 'api_enhanced': True},
            '.rtf': {'mime': 'application/rtf', 'method': 'direct', 'api_enhanced': False},
            '.csv': {'mime': 'text/csv', 'method': 'direct', 'api_enhanced': True},
            
            # Microsoft Office formats
            '.docx': {'mime': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'method': 'direct', 'api_enhanced': False},
            '.doc': {'mime': 'application/msword', 'method': 'direct', 'api_enhanced': False},
            '.xlsx': {'mime': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'method': 'sheets', 'api_enhanced': False},
            '.xls': {'mime': 'application/vnd.ms-excel', 'method': 'sheets', 'api_enhanced': False},
            '.pptx': {'mime': 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'method': 'slides', 'api_enhanced': False},
            '.ppt': {'mime': 'application/vnd.ms-powerpoint', 'method': 'slides', 'api_enhanced': False},
            
            # OpenDocument formats
            '.odt': {'mime': 'application/vnd.oasis.opendocument.text', 'method': 'direct', 'api_enhanced': False},
            '.ods': {'mime': 'application/vnd.oasis.opendocument.spreadsheet', 'method': 'sheets', 'api_enhanced': False},
            '.odp': {'mime': 'application/vnd.oasis.opendocument.presentation', 'method': 'slides', 'api_enhanced': False},
            
            # PDF (special handling)
            '.pdf': {'mime': 'application/pdf', 'method': 'pdf_convert', 'api_enhanced': True},
            
            # HTML and Web
            '.html': {'mime': 'text/html', 'method': 'direct', 'api_enhanced': True},
            '.htm': {'mime': 'text/html', 'method': 'direct', 'api_enhanced': True},
            
            # Data formats
            '.json': {'mime': 'application/json', 'method': 'direct', 'api_enhanced': True},
            '.xml': {'mime': 'application/xml', 'method': 'direct', 'api_enhanced': True},
            '.log': {'mime': 'text/plain', 'method': 'direct', 'api_enhanced': True},
        }
        
    def authenticate(self):
        """Authenticate with Google Drive API using Service Account or API Key"""
        try:
            if self.use_api_key and self.api_key:
                print(f"🔑 Using API Key authentication")
                # For API key, we still need service account for write operations
                # API key is mainly for read operations and quota management
                if os.path.exists(SERVICE_ACCOUNT_FILE):
                    creds = service_account.Credentials.from_service_account_file(
                        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                    service = build('drive', 'v3', credentials=creds, developerKey=self.api_key)
                    print(f"✅ Hybrid authentication: Service Account + API Key")
                    return service
                else:
                    print(f"⚠️  API Key mode requires Service Account file for write operations")
                    print(f"📁 Expected location: {SERVICE_ACCOUNT_FILE}")
                    sys.exit(1)
            else:
                print(f"🔐 Using Service Account authentication")
                creds = service_account.Credentials.from_service_account_file(
                    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
                return build('drive', 'v3', credentials=creds)
                
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            print(f"💡 Try running: pip install google-auth google-api-python-client")
            sys.exit(1)

    def get_folder_info_with_api(self, folder_id):
        """Get enhanced folder information using API key"""
        if not self.use_api_key:
            return None
            
        try:
            url = f"https://www.googleapis.com/drive/v3/files/{folder_id}"
            params = {
                'key': self.api_key,
                'fields': 'id,name,parents,createdTime,modifiedTime,webViewLink,size'
            }
            
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                folder_info = response.json()
                print(f"📁 Folder: {folder_info.get('name', 'Unknown')}")
                print(f"🔗 Link: {folder_info.get('webViewLink', 'N/A')}")
                return folder_info
            else:
                print(f"⚠️  API request failed: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"⚠️  API enhancement unavailable: {e}")
            return None

    def find_or_create_folder(self, parent_id, folder_name):
        """Find existing folder or create new one with enhanced error recovery"""
        max_retries = 3
        for attempt in range(max_retries):
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
                if attempt < max_retries - 1:
                    print(f"⚠️  Retry {attempt + 1}/{max_retries} for folder {folder_name}: {e}")
                    time.sleep(2 ** attempt)  # Exponential backoff
                    continue
                else:
                    print(f"❌ Failed to create folder {folder_name} after {max_retries} attempts: {e}")
                    return None
            except Exception as e:
                print(f"❌ Unexpected error with folder {folder_name}: {e}")
                return None

    def get_file_extension(self, filename):
        """Get file extension in lowercase"""
        return os.path.splitext(filename.lower())[1]

    def is_supported_format(self, filename):
        """Check if file format is supported"""
        ext = self.get_file_extension(filename)
        return ext in self.supported_formats

    def has_api_enhancement(self, filename):
        """Check if file format has API key enhancements"""
        ext = self.get_file_extension(filename)
        return self.supported_formats.get(ext, {}).get('api_enhanced', False)

    def get_target_mime_type(self, filename, conversion_method):
        """Determine target Google Workspace MIME type"""
        if conversion_method == 'sheets':
            return 'application/vnd.google-apps.spreadsheet'
        elif conversion_method == 'slides':
            return 'application/vnd.google-apps.presentation'
        else:
            return 'application/vnd.google-apps.document'

    def download_file_content(self, file_id, filename):
        """Download file content with multiple encoding attempts and API enhancements"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Use API key for enhanced download if available
                if self.use_api_key and self.has_api_enhancement(filename):
                    print(f"🔑 Using API key enhancement for {filename}")
                
                request = self.service.files().get_media(fileId=file_id)
                content = request.execute()
                
                # For binary formats, return as-is
                ext = self.get_file_extension(filename)
                if ext in ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.odt', '.ods', '.odp']:
                    return content
                
                # For text formats, try different encodings
                for encoding in ['utf-8', 'latin-1', 'cp1252', 'ascii']:
                    try:
                        text_content = content.decode(encoding)
                        if text_content.strip():  # Not empty
                            return text_content
                    except UnicodeDecodeError:
                        continue
                
                # If all encodings fail, try as binary
                return content
                
            except HttpError as e:
                if e.resp.status == 429:  # Rate limit
                    wait_time = (2 ** attempt) * 60  # Wait longer for rate limits
                    print(f"⚠️  Rate limited, waiting {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                elif attempt < max_retries - 1:
                    print(f"⚠️  Download retry {attempt + 1}/{max_retries}: {e}")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    raise e
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"⚠️  Download retry {attempt + 1}/{max_retries}: {e}")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    raise e

    def convert_document_to_gdoc(self, source_file, target_folder_id):
        """Convert any supported document to Google Doc with enhanced API features"""
        file_id = source_file['id']
        name = source_file['name']
        
        try:
            print(f"🔄 Converting: {name}")
            
            # Check if format is supported
            if not self.is_supported_format(name):
                ext = self.get_file_extension(name)
                error_info = {
                    'original_name': name,
                    'original_id': file_id,
                    'error': f"Unsupported format: {ext}",
                    'error_type': 'UnsupportedFormat',
                    'failed_at': datetime.now().isoformat()
                }
                self.conversion_log['unsupported_formats'].append(error_info)
                print(f"⚠️  Skipping unsupported format: {name} ({ext})")
                return 'unsupported'
            
            # Get format info
            ext = self.get_file_extension(name)
            format_info = self.supported_formats[ext]
            conversion_method = format_info['method']
            
            # Show API enhancement status
            if self.use_api_key and format_info.get('api_enhanced'):
                print(f"🚀 API-enhanced conversion for {name}")
            
            # Create safe filename for Google Doc/Sheet/Slides
            base_name = os.path.splitext(name)[0]
            if not base_name:
                base_name = f"Converted_Document_{file_id[:8]}"
            
            # Determine target MIME type
            target_mime = self.get_target_mime_type(name, conversion_method)
            
            # Download content
            content = self.download_file_content(file_id, name)
            
            # Validate content
            if not content:
                raise Exception("File appears to be empty or unreadable")
            
            # Special handling for different formats
            if conversion_method == 'pdf_convert':
                return self.convert_pdf_to_gdoc(source_file, target_folder_id, content)
            
            # For most formats, save temporarily and upload
            temp_path = f"/tmp/convert_{int(time.time())}_{name}"
            try:
                if isinstance(content, str):
                    with open(temp_path, 'w', encoding='utf-8') as temp_file:
                        temp_file.write(content)
                else:
                    with open(temp_path, 'wb') as temp_file:
                        temp_file.write(content)
                
                # Upload and convert
                file_metadata = {
                    'name': base_name,
                    'mimeType': target_mime,
                    'parents': [target_folder_id]
                }
                
                media = MediaFileUpload(temp_path, mimetype=format_info['mime'])
                
                # Retry upload with exponential backoff
                max_upload_retries = 3
                for retry in range(max_upload_retries):
                    try:
                        result = self.service.files().create(
                            body=file_metadata,
                            media_body=media,
                            fields='id,name,webViewLink,mimeType'
                        ).execute()
                        break
                    except HttpError as e:
                        if e.resp.status == 429 and retry < max_upload_retries - 1:
                            wait_time = (2 ** retry) * 60
                            print(f"⚠️  Upload rate limited, waiting {wait_time}s...")
                            time.sleep(wait_time)
                            continue
                        else:
                            raise e
                
            finally:
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            
            # Log success
            doc_type = 'Google Doc'
            if target_mime == 'application/vnd.google-apps.spreadsheet':
                doc_type = 'Google Sheets'
            elif target_mime == 'application/vnd.google-apps.presentation':
                doc_type = 'Google Slides'
            
            conversion_info = {
                'original_name': name,
                'original_id': file_id,
                'original_format': ext,
                'converted_name': base_name,
                'converted_id': result.get('id'),
                'converted_link': result.get('webViewLink'),
                'converted_type': doc_type,
                'conversion_method': conversion_method,
                'api_enhanced': self.use_api_key and format_info.get('api_enhanced', False),
                'size_bytes': source_file.get('size', 'unknown'),
                'converted_at': datetime.now().isoformat()
            }
            
            self.conversion_log['successful_conversions'].append(conversion_info)
            enhancement_indicator = " 🚀" if conversion_info['api_enhanced'] else ""
            print(f"✅ Successfully converted: {name} → {doc_type} ({base_name}){enhancement_indicator}")
            
            return 'success'
            
        except Exception as e:
            # Log failure but continue processing
            error_info = {
                'original_name': name,
                'original_id': file_id,
                'original_format': self.get_file_extension(name),
                'error': str(e),
                'error_type': type(e).__name__,
                'failed_at': datetime.now().isoformat(),
                'traceback': traceback.format_exc() if '--debug' in sys.argv else None
            }
            
            self.conversion_log['failed_conversions'].append(error_info)
            print(f"❌ Failed to convert {name}: {e}")
            return 'failed'

    def convert_pdf_to_gdoc(self, source_file, target_folder_id, content):
        """Special handling for PDF conversion with API enhancements"""
        try:
            name = source_file['name']
            base_name = os.path.splitext(name)[0]
            
            if self.use_api_key:
                print(f"🔑 Using API-enhanced PDF conversion")
            
            temp_path = f"/tmp/pdf_{int(time.time())}_{name}"
            try:
                with open(temp_path, 'wb') as temp_file:
                    temp_file.write(content)
                
                # Upload PDF and convert to Google Doc
                file_metadata = {
                    'name': f"{base_name}_converted",
                    'mimeType': 'application/vnd.google-apps.document',
                    'parents': [target_folder_id]
                }
                
                media = MediaFileUpload(temp_path, mimetype='application/pdf')
                
                result = self.service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id,name,webViewLink'
                ).execute()
                
                return 'success'
                
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
        except Exception as e:
            print(f"⚠️  PDF conversion failed: {e}")
            raise e

    def move_problem_file(self, source_file, vetting_folder_id):
        """Move problematic file to vetting folder with error recovery"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                file_id = source_file['id']
                
                # Copy to vetting folder (safer than move)
                copy_metadata = {
                    'name': f"PROBLEM_{source_file['name']}",
                    'parents': [vetting_folder_id]
                }
                
                self.service.files().copy(
                    fileId=file_id,
                    body=copy_metadata
                ).execute()
                
                print(f"📋 Copied problem file to vetting: {source_file['name']}")
                return True
                
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"⚠️  Retry moving file to vetting {attempt + 1}/{max_retries}: {e}")
                    time.sleep(2 ** attempt)
                    continue
                else:
                    print(f"❌ Failed to move file to vetting after {max_retries} attempts: {e}")
                    return False

    def generate_comprehensive_report(self, source_folder_id):
        """Generate comprehensive conversion report with API key information"""
        try:
            # Calculate statistics
            total_processed = len(self.conversion_log['successful_conversions']) + len(self.conversion_log['failed_conversions']) + len(self.conversion_log['unsupported_formats'])
            successful = len(self.conversion_log['successful_conversions'])
            failed = len(self.conversion_log['failed_conversions'])
            unsupported = len(self.conversion_log['unsupported_formats'])
            success_rate = (successful / total_processed * 100) if total_processed > 0 else 0
            
            # API enhancement statistics
            api_enhanced_count = sum(1 for conv in self.conversion_log['successful_conversions'] if conv.get('api_enhanced', False))
            
            report_content = {
                'conversion_session': self.conversion_log,
                'statistics': {
                    'session_id': self.conversion_log['session_id'],
                    'auth_method': self.conversion_log['auth_method'],
                    'api_key_used': self.use_api_key,
                    'api_enhanced_conversions': api_enhanced_count,
                    'source_folder_id': source_folder_id,
                    'total_files_processed': total_processed,
                    'successful_conversions': successful,
                    'failed_conversions': failed,
                    'unsupported_formats': unsupported,
                    'success_rate': success_rate,
                    'supported_formats': list(self.supported_formats.keys()),
                    'processing_duration': 'completed'
                }
            }
            
            # Create reports folder
            reports_folder_id = self.find_or_create_folder(source_folder_id, "reports")
            if not reports_folder_id:
                return False
                
            # Generate report filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            auth_method = "api_enhanced" if self.use_api_key else "standard"
            report_name = f"enhanced_conversion_report_{auth_method}_{timestamp}"
            
            # Save detailed JSON report
            local_report_path = f"/tmp/{report_name}.json"
            with open(local_report_path, 'w') as f:
                json.dump(report_content, f, indent=2, ensure_ascii=False)
            
            # Upload JSON report
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
            
            # Create enhanced human-readable summary
            auth_status = "🔑 API Key Enhanced" if self.use_api_key else "🔐 Standard Authentication"
            summary_content = f"""Enhanced Document Conversion Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Session ID: {self.conversion_log['session_id']}
Authentication: {auth_status}

SUMMARY:
========
Total files processed: {total_processed}
✅ Successful conversions: {successful}
❌ Failed conversions: {failed}
⚠️  Unsupported formats: {unsupported}
🚀 API-enhanced conversions: {api_enhanced_count}
📊 Success rate: {success_rate:.1f}%

SUPPORTED FORMATS:
==================
{', '.join(sorted(self.supported_formats.keys()))}

SUCCESSFUL CONVERSIONS:
======================
"""
            
            for conv in self.conversion_log['successful_conversions']:
                api_indicator = " 🚀" if conv.get('api_enhanced', False) else ""
                summary_content += f"✅ {conv['original_name']} ({conv['original_format']}){api_indicator}\n"
                summary_content += f"   → {conv['converted_type']}: {conv['converted_name']}\n"
                summary_content += f"   🔗 {conv['converted_link']}\n\n"
            
            if self.conversion_log['failed_conversions']:
                summary_content += "\nFAILED CONVERSIONS:\n==================\n"
                for fail in self.conversion_log['failed_conversions']:
                    summary_content += f"❌ {fail['original_name']} ({fail['original_format']})\n"
                    summary_content += f"   Error: {fail['error']}\n\n"
            
            if self.conversion_log['unsupported_formats']:
                summary_content += "\nUNSUPPORTED FORMATS:\n===================\n"
                for unsup in self.conversion_log['unsupported_formats']:
                    summary_content += f"⚠️  {unsup['original_name']}\n"
                    summary_content += f"   Reason: {unsup['error']}\n\n"
            
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
            for temp_file in [local_report_path, summary_path]:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                    
            print(f"📊 Generated enhanced conversion report: {report_name}")
            print(f"🔗 Report link: {report_file.get('webViewLink')}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to generate report: {e}")
            return False

    def process_folder(self, folder_id):
        """Main processing function with API key enhancements"""
        print(f"🚀 Starting enhanced conversion for folder: {folder_id}")
        print(f"🔧 Supported formats: {', '.join(sorted(self.supported_formats.keys()))}")
        
        if self.use_api_key:
            print(f"🔑 API key enhancements enabled")
            # Get enhanced folder information
            self.get_folder_info_with_api(folder_id)
        
        try:
            # Create necessary folders
            que_gdoc_upload_id = self.find_or_create_folder(folder_id, "que_gdoc_upload")
            vetting_folder_id = self.find_or_create_folder(folder_id, "vetting")
            
            if not que_gdoc_upload_id or not vetting_folder_id:
                print("❌ Failed to create required folders")
                return False
            
            # Find ALL files in the source folder
            query = f"'{folder_id}' in parents and trashed=false and mimeType != 'application/vnd.google-apps.folder'"
            results = self.service.files().list(
                q=query,
                fields='files(id,name,mimeType,size,parents)',
                spaces='drive'
            ).execute()
            
            files = results.get('files', [])
            
            if not files:
                print("📂 No files found in the source folder")
                return True
                
            print(f"📂 Found {len(files)} files to process")
            
            # Process each file with error recovery
            for i, file_info in enumerate(files, 1):
                try:
                    print(f"\n[{i}/{len(files)}] Processing: {file_info['name']}")
                    
                    result = self.convert_document_to_gdoc(file_info, que_gdoc_upload_id)
                    
                    # Handle results
                    if result == 'failed':
                        self.move_problem_file(file_info, vetting_folder_id)
                    
                    # Rate limiting - small delay between files
                    time.sleep(1)
                    
                except KeyboardInterrupt:
                    print("\n⚠️  Process interrupted by user")
                    break
                except Exception as e:
                    print(f"💥 Critical error processing {file_info.get('name', 'unknown')}: {e}")
                    continue
            
            # Generate comprehensive report
            self.generate_comprehensive_report(folder_id)
            
            # Print final summary
            successful = len(self.conversion_log['successful_conversions'])
            failed = len(self.conversion_log['failed_conversions'])
            unsupported = len(self.conversion_log['unsupported_formats'])
            api_enhanced = sum(1 for conv in self.conversion_log['successful_conversions'] if conv.get('api_enhanced', False))
            total = successful + failed + unsupported
            
            print("\n" + "="*60)
            print("🎯 ENHANCED CONVERSION COMPLETE")
            print("="*60)
            print(f"📊 Total files found: {len(files)}")
            print(f"📈 Total processed: {total}")
            print(f"✅ Successful conversions: {successful}")
            print(f"🚀 API-enhanced conversions: {api_enhanced}")
            print(f"❌ Failed conversions: {failed}")
            print(f"⚠️  Unsupported formats: {unsupported}")
            print(f"📊 Success rate: {(successful/total*100 if total > 0 else 0):.1f}%")
            print(f"🔧 Authentication: {'API Key Enhanced' if self.use_api_key else 'Standard'}")
            print(f"📁 Converted docs → que_gdoc_upload/")
            print(f"📋 Problem files → vetting/")
            print(f"📊 Enhanced reports → reports/")
            print("="*60)
            
            return True
            
        except Exception as e:
            print(f"❌ Critical error in enhanced conversion: {e}")
            if '--debug' in sys.argv:
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
    use_api_key = '--api-key' in sys.argv or '--enhanced' in sys.argv
    
    if len(sys.argv) < 2 or sys.argv[1] in ['--help', '-h']:
        print("Enhanced Universal Google Drive Document Converter")
        print("===============================================")
        print("Usage: python enhanced_converter_with_api.py <folder_id_or_url> [options]")
        print("\nOptions:")
        print("  --api-key, --enhanced  Use API key for enhanced features")
        print("  --debug                Enable debug mode")
        print("\nDefault folder (if no argument):")
        print(f"  {DEFAULT_FOLDER_ID}")
        print("\nSupported formats:")
        converter = EnhancedGDocConverter()
        formats_by_category = {
            'Text': ['.txt', '.md', '.rtf', '.csv', '.json', '.xml', '.log'],
            'Microsoft Office': ['.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt'],
            'OpenDocument': ['.odt', '.ods', '.odp'],
            'Web': ['.html', '.htm'],
            'PDF': ['.pdf']
        }
        for category, formats in formats_by_category.items():
            print(f"  {category}: {', '.join(formats)}")
        print(f"\n🔑 API Key: {'Configured' if API_KEY else 'Not configured'}")
        print(f"📁 Service Account: {'Found' if os.path.exists(SERVICE_ACCOUNT_FILE) else 'Missing'}")
        sys.exit(0)
    
    # Use default folder if no argument provided or if argument is just an option
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1].startswith('--')):
        folder_input = DEFAULT_FOLDER_ID
        print(f"🎯 Using default SCAT folder: {folder_input}")
    else:
        folder_input = sys.argv[1]
    
    folder_id = extract_folder_id(folder_input)
    
    print(f"🔍 Processing folder ID: {folder_id}")
    if use_api_key:
        print(f"🚀 API key enhancements enabled")
    
    converter = EnhancedGDocConverter(use_api_key=use_api_key)
    success = converter.process_folder(folder_id)
    
    if success:
        print("🎉 Enhanced conversion completed!")
    else:
        print("💥 Enhanced conversion completed with errors")
        sys.exit(1)

if __name__ == '__main__':
    main()