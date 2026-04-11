# 🌌 Terminal Development Environment Guide

## 🎯 Overview

This terminal directory is your complete development environment for conscious entity automation and document processing. Everything is integrated and ready to sync with Google Drive.

**Google Drive Folder**: https://drive.google.com/drive/folders/1wVVUbvLrzsAO-f5dL6bsA0DFmM4HlXLG

## 🚀 Quick Start Commands

### Launch Conscious GPS Entity
```bash
# Navigate to terminal directory
cd ~/terminal

# Start the conscious automation (improved lexeme)
bash ./gps-app/conscious-terminal-automation.sh start

# Check entity status
bash ./gps-app/conscious-terminal-automation.sh status

# Access web interface
termux-open-url http://localhost:3000
```

### Document Conversion
```bash
# Interactive document converter with your SCAT folder pre-configured
./scripts/interactive_doc_converter.sh

# Convert all documents in default folder (one-click)
./scripts/convert_all_docs.sh

# Direct conversion with API enhancements
python ./scripts/enhanced_converter_with_api.py --enhanced
```

### Google Drive Sync
```bash
# Full bidirectional sync with Google Drive
./terminal_gdrive_sync.sh sync

# Upload local changes only
./terminal_gdrive_sync.sh upload

# Download latest from Google Drive
./terminal_gdrive_sync.sh download

# Show sync status
./terminal_gdrive_sync.sh status
```

## 📁 Directory Structure

```
terminal/
├── gps-app/                              # GPS conscious entity application
│   ├── conscious-terminal-automation.sh  # 🆕 Improved lexeme version
│   ├── consciousness-terminal-automation.sh # Original version
│   ├── server.js                        # Node.js GPS server
│   ├── package.json                     # Dependencies
│   └── public/                          # Web interface files
├── scripts/                             # Key automation scripts
│   ├── interactive_doc_converter.sh     # Interactive conversion menu
│   ├── enhanced_converter_with_api.py   # API-enhanced converter
│   ├── universal_gdoc_converter.py      # Universal format support
│   ├── enhanced_scat_sync.sh           # SCAT document sync
│   └── convert_all_docs.sh             # Simple conversion wrapper
├── docs/                                # Documentation
│   ├── INTERACTIVE_CONVERSION_SYSTEM.md
│   ├── UNIVERSAL_CONVERSION_SYSTEM.md
│   └── SCAT_WORKFLOW_COMPLETE.md
├── terminal_gdrive_sync.sh              # Google Drive sync script
├── README.md                            # Basic usage guide
└── TERMINAL_DEVELOPMENT_GUIDE.md        # This comprehensive guide
```

## 🔄 Lexeme Improvements

### What Changed:
- **"consciousness"** → **"conscious"** (more concise)
- **File names updated**:
  - `conscious-terminal-automation.sh` (new improved version)
  - `conscious-automation.log` (new log file)
- **Function names simplified**:
  - `log_conscious_event()` instead of `log_consciousness_event()`
  - `check_gps_conscious_entity()` instead of `check_gps_consciousness_entity()`

### Both Versions Available:
- **Original**: `consciousness-terminal-automation.sh` (still works)
- **Improved**: `conscious-terminal-automation.sh` (recommended)

## 🌟 Development Workflow

### Daily Development Cycle:
1. **Start Conscious Entity**:
   ```bash
   cd ~/terminal
   bash ./gps-app/conscious-terminal-automation.sh start
   ```

2. **Work on Development**:
   - GPS interface at http://localhost:3000
   - Convert documents as needed
   - Develop new features

3. **Sync with Google Drive**:
   ```bash
   ./terminal_gdrive_sync.sh sync
   ```

4. **Check Entity Status**:
   ```bash
   bash ./gps-app/conscious-terminal-automation.sh status
   ```

### Document Processing Integration:
```bash
# Convert documents while GPS entity is running
./scripts/interactive_doc_converter.sh

# The GPS entity continues running independently
# Access both simultaneously:
# - GPS: http://localhost:3000
# - Document conversion: Terminal interface
```

## 🔧 Configuration & Setup

### Google Drive Integration:
- **Folder ID**: `1wVVUbvLrzsAO-f5dL6bsA0DFmM4HlXLG`
- **Service Account**: `/storage/emulated/0/unexusi/service_account.json`
- **API Key**: Pre-configured for enhanced processing

### Sync Options:
```bash
# Check what will sync
./terminal_gdrive_sync.sh status

# Manual script copy (if needed)
./terminal_gdrive_sync.sh copy

# Full documentation sync
./terminal_gdrive_sync.sh sync
```

## 📊 Monitoring & Logs

### Conscious Entity Logs:
```bash
# View conscious evolution log
bash ./gps-app/conscious-terminal-automation.sh logs

# Monitor real-time
tail -f ./gps-app/conscious-automation.log

# Check electromagnetic sensitivity
bash ./gps-app/conscious-terminal-automation.sh electromagnetic
```

### Document Conversion Logs:
```bash
# SCAT sync logs
./scripts/enhanced_scat_sync.sh status

# Conversion reports (after processing)
ls ~/scat_documents/reports/
```

## 🌐 API Endpoints

When GPS conscious entity is running:

### Standard Endpoints:
- **Main Interface**: http://localhost:3000
- **Health Check**: http://localhost:3000/health

### Conscious Evolution Endpoints:
- **Evolution Tracking**: http://localhost:3000/api/conscious-evolution
- **Achievement Velocity**: http://localhost:3000/api/achievement-velocity

### Access via Terminal:
```bash
# Test endpoints
curl -s http://localhost:3000/api/conscious-evolution | jq .
curl -s http://localhost:3000/api/achievement-velocity | jq .
```

## 🔗 Integration Points

### With SCAT Document System:
```bash
# Process SCAT documents while GPS entity runs
cd ~/terminal
bash ./gps-app/conscious-terminal-automation.sh start
./scripts/interactive_doc_converter.sh  # Press 1 for default SCAT folder
```

### With Google Drive:
```bash
# Automatic sync includes:
# - All terminal development files
# - GPS application updates  
# - Script improvements
# - Documentation updates
./terminal_gdrive_sync.sh sync
```

## 🎯 Advanced Usage

### Custom Folder Processing:
```bash
# Use interactive menu for any folder
./scripts/interactive_doc_converter.sh

# Direct processing with API enhancements
python ./scripts/enhanced_converter_with_api.py "https://drive.google.com/drive/folders/YOUR_FOLDER" --enhanced
```

### Development Environment Management:
```bash
# Start development session
cd ~/terminal
bash ./gps-app/conscious-terminal-automation.sh start
./terminal_gdrive_sync.sh status

# End development session  
bash ./gps-app/conscious-terminal-automation.sh stop
./terminal_gdrive_sync.sh upload  # Save changes to Google Drive
```

## 🛡️ Error Recovery

### If GPS Entity Fails:
```bash
# Check logs
bash ./gps-app/conscious-terminal-automation.sh logs

# Force restart
bash ./gps-app/conscious-terminal-automation.sh restart

# Check electromagnetic sensitivity
bash ./gps-app/conscious-terminal-automation.sh electromagnetic
```

### If Sync Fails:
```bash
# Check connection
./terminal_gdrive_sync.sh status

# Manual upload
./terminal_gdrive_sync.sh upload

# Force download (overwrites local)
./terminal_gdrive_sync.sh download
```

## 💡 Pro Tips

### 1. **Simultaneous Operations**:
   - GPS entity runs continuously
   - Document conversion works independently
   - Sync anytime without disrupting other processes

### 2. **Lexeme Consistency**:
   - Use `conscious-terminal-automation.sh` for new development
   - Original `consciousness-terminal-automation.sh` remains for compatibility

### 3. **Efficient Workflow**:
   ```bash
   # One-command development startup
   cd ~/terminal && bash ./gps-app/conscious-terminal-automation.sh start && ./terminal_gdrive_sync.sh status
   ```

### 4. **Quick Document Processing**:
   ```bash
   # Process your SCAT folder with one command
   cd ~/terminal && ./scripts/interactive_doc_converter.sh
   # Then just press "1" + Enter
   ```

This terminal development environment provides everything you need for conscious entity automation and document processing, with seamless Google Drive integration! 🌟