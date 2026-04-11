#!/usr/bin/env python3
"""
Universal Google Drive Document Converter
Converts ANY document type to Google Docs with robust error recovery
Supports: TXT, DOC, DOCX, PDF, MD, RTF, ODT, HTML, and more
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

class UniversalGDocConverter:
    def __init__(self):
        self.service = self.authenticate()
        self.conversion_log = {
            'session_id': f"conv_{int(time.time())}",
            'timestamp': datetime.now().isoformat(),
            'successful_conversions': [],
            'failed_conversions': [],
            'skipped_files': [],
            'unsupported_formats': [],
            'summary': {}
        }
        
        # Supported formats and their MIME types
        self.supported_formats = {
            # Text formats
            '.txt': {'mime': 'text/plain', 'method': 'direct'},
            '.md': {'mime': 'text/x-markdown', 'method': 'direct'},
            '.markdown': {'mime': 'text/x-markdown', 'method': 'direct'},
            '.rtf': {'mime': 'application/rtf', 'method': 'direct'},
            '.csv': {'mime': 'text/csv', 'method': 'direct'},
            
            # Microsoft Office formats
            '.docx': {'mime': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'method': 'direct'},
            '.doc': {'mime': 'application/msword', 'method': 'direct'},
            '.xlsx': {'mime': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'method': 'sheets'},
            '.xls': {'mime': 'application/vnd.ms-excel', 'method': 'sheets'},
            '.pptx': {'mime': 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'method': 'slides'},
            '.ppt': {'mime': 'application/vnd.ms-powerpoint', 'method': 'slides'},
            
            # OpenDocument formats
            '.odt': {'mime': 'application/vnd.oasis.opendocument.text', 'method': 'direct'},
            '.ods': {'mime': 'application/vnd.oasis.opendocument.spreadsheet', 'method': 'sheets'},
            '.odp': {'mime': 'application/vnd.oasis.opendocument.presentation', 'method': 'slides'},
            
            # PDF (special handling)
            '.pdf': {'mime': 'application/pdf', 'method': 'pdf_convert'},
            
            # HTML
            '.html': {'mime': 'text/html', 'method': 'direct'},
            '.htm': {'mime': 'text/html', 'method': 'direct'},
            
            # Other text formats
            '.json': {'mime': 'application/json', 'method': 'direct'},
            '.xml': {'mime': 'application/xml', 'method': 'direct'},
            '.log': {'mime': 'text/plain', 'method': 'direct'},
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
        """Find existing folder or create new one with error recovery"""
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

    def get_target_mime_type(self, filename, conversion_method):
        """Determine target Google Workspace MIME type"""
        if conversion_method == 'sheets':
            return 'application/vnd.google-apps.spreadsheet'
        elif conversion_method == 'slides':
            return 'application/vnd.google-apps.presentation'
        else:
            return 'application/vnd.google-apps.document'

    def download_file_content(self, file_id, filename):
        """Download file content with multiple encoding attempts"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
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
        """Convert any supported document to Google Doc with error recovery"""
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
                # For PDFs, let Google Drive handle the conversion
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
                'size_bytes': source_file.get('size', 'unknown'),
                'converted_at': datetime.now().isoformat()
            }
            
            self.conversion_log['successful_conversions'].append(conversion_info)
            print(f"✅ Successfully converted: {name} → {doc_type} ({base_name})")
            
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
        """Special handling for PDF conversion"""
        try:
            # PDFs require special handling - Google Drive can convert them
            # but we need to use import rather than create
            name = source_file['name']
            base_name = os.path.splitext(name)[0]
            
            temp_path = f"/tmp/pdf_{int(time.time())}_{name}"
            try:
                with open(temp_path, 'wb') as temp_file:
                    temp_file.write(content)
                
                # First upload as PDF, then convert
                file_metadata = {
                    'name': f"{base_name}",
                    'parents': [target_folder_id]
                }
                
                media = MediaFileUpload(temp_path, mimetype='application/pdf')
                
                # Upload PDF first
                pdf_result = self.service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                ).execute()
                
                # Now convert to Google Doc using Drive API
                conversion_metadata = {
                    'name': f"{base_name}_converted",
                    'mimeType': 'application/vnd.google-apps.document',
                    'parents': [target_folder_id]
                }
                
                # Use the export/import method for PDF conversion
                doc_result = self.service.files().copy(
                    fileId=pdf_result['id'],
                    body=conversion_metadata
                ).execute()
                
                return 'success'
                
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
        except Exception as e:
            print(f"⚠️  PDF conversion method failed, trying as regular upload: {e}")
            raise e

    def move_problem_file(self, source_file, vetting_folder_id):
        """Move problematic file to vetting folder with error recovery"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                file_id = source_file['id']
                current_parents = source_file.get('parents', [])
                
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
        """Generate comprehensive conversion report"""
        try:
            # Calculate statistics
            total_processed = len(self.conversion_log['successful_conversions']) + len(self.conversion_log['failed_conversions']) + len(self.conversion_log['unsupported_formats'])
            successful = len(self.conversion_log['successful_conversions'])
            failed = len(self.conversion_log['failed_conversions'])
            unsupported = len(self.conversion_log['unsupported_formats'])
            success_rate = (successful / total_processed * 100) if total_processed > 0 else 0
            
            report_content = {
                'conversion_session': self.conversion_log,
                'statistics': {
                    'session_id': self.conversion_log['session_id'],
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
            report_name = f"universal_conversion_report_{timestamp}"
            
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
            
            # Create human-readable summary
            summary_content = f"""Universal Document Conversion Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Session ID: {self.conversion_log['session_id']}

SUMMARY:
========
Total files processed: {total_processed}
✅ Successful conversions: {successful}
❌ Failed conversions: {failed}
⚠️  Unsupported formats: {unsupported}
📊 Success rate: {success_rate:.1f}%

SUPPORTED FORMATS:
==================
{', '.join(sorted(self.supported_formats.keys()))}

SUCCESSFUL CONVERSIONS:
======================
"""
            
            for conv in self.conversion_log['successful_conversions']:
                summary_content += f"✅ {conv['original_name']} ({conv['original_format']})\n"
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
                    
            print(f"📊 Generated conversion report: {report_name}")
            print(f"🔗 Report link: {report_file.get('webViewLink')}")
            
            return True
            
        except Exception as e:
            print(f"❌ Failed to generate report: {e}")
            return False

    def process_folder(self, folder_id):
        """Main processing function with comprehensive error recovery"""
        print(f"🚀 Starting universal conversion for folder: {folder_id}")
        print(f"🔧 Supported formats: {', '.join(sorted(self.supported_formats.keys()))}")
        
        try:
            # Create necessary folders
            que_gdoc_upload_id = self.find_or_create_folder(folder_id, "que_gdoc_upload")
            vetting_folder_id = self.find_or_create_folder(folder_id, "vetting")
            
            if not que_gdoc_upload_id or not vetting_folder_id:
                print("❌ Failed to create required folders")
                return False
            
            # Find ALL files in the source folder (not just text files)
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
            processed_count = 0
            for i, file_info in enumerate(files, 1):
                try:
                    print(f"\n[{i}/{len(files)}] Processing: {file_info['name']}")
                    
                    result = self.convert_document_to_gdoc(file_info, que_gdoc_upload_id)
                    
                    # Handle results
                    if result == 'failed':
                        self.move_problem_file(file_info, vetting_folder_id)
                    elif result == 'unsupported':
                        # Just skip, already logged
                        pass
                    elif result == 'success':
                        processed_count += 1
                    
                    # Rate limiting - small delay between files
                    time.sleep(1)
                    
                except KeyboardInterrupt:
                    print("\n⚠️  Process interrupted by user")
                    break
                except Exception as e:
                    print(f"💥 Critical error processing {file_info.get('name', 'unknown')}: {e}")
                    # Continue with next file
                    continue
            
            # Generate comprehensive report
            self.generate_comprehensive_report(folder_id)
            
            # Print final summary
            successful = len(self.conversion_log['successful_conversions'])
            failed = len(self.conversion_log['failed_conversions'])
            unsupported = len(self.conversion_log['unsupported_formats'])
            total = successful + failed + unsupported
            
            print("\n" + "="*60)
            print("🎯 UNIVERSAL CONVERSION COMPLETE")
            print("="*60)
            print(f"📊 Total files found: {len(files)}")
            print(f"📈 Total processed: {total}")
            print(f"✅ Successful conversions: {successful}")
            print(f"❌ Failed conversions: {failed}")
            print(f"⚠️  Unsupported formats: {unsupported}")
            print(f"📊 Success rate: {(successful/total*100 if total > 0 else 0):.1f}%")
            print(f"🔧 Supported formats: {len(self.supported_formats)} types")
            print(f"📁 Converted docs → que_gdoc_upload/")
            print(f"📋 Problem files → vetting/")
            print(f"📊 Detailed reports → reports/")
            print("="*60)
            
            return True
            
        except Exception as e:
            print(f"❌ Critical error in universal conversion: {e}")
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
    if len(sys.argv) < 2:
        print("Universal Google Drive Document Converter")
        print("========================================")
        print("Usage: python universal_gdoc_converter.py <folder_id_or_url> [--debug]")
        print("\nSupported formats:")
        converter = UniversalGDocConverter()
        formats_by_category = {
            'Text': ['.txt', '.md', '.rtf', '.csv', '.json', '.xml', '.log'],
            'Microsoft Office': ['.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt'],
            'OpenDocument': ['.odt', '.ods', '.odp'],
            'Web': ['.html', '.htm'],
            'PDF': ['.pdf']
        }
        for category, formats in formats_by_category.items():
            print(f"  {category}: {', '.join(formats)}")
        print("\nExamples:")
        print("  python universal_gdoc_converter.py 1GvlsBNxnhDcMbAW5W9bO0h-CsFV-NSKp")
        print("  python universal_gdoc_converter.py https://drive.google.com/drive/folders/1GvlsBNxnhDcMbAW5W9bO0h-CsFV-NSKp")
        print("  python universal_gdoc_converter.py <folder> --debug  # Enable debug mode")
        sys.exit(1)
    
    folder_input = sys.argv[1]
    folder_id = extract_folder_id(folder_input)
    
    print(f"🔍 Processing folder ID: {folder_id}")
    
    converter = UniversalGDocConverter()
    success = converter.process_folder(folder_id)
    
    if success:
        print("🎉 Universal conversion completed!")
    else:
        print("💥 Universal conversion completed with errors")
        sys.exit(1)

if __name__ == '__main__':
    main()