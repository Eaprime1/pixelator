#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Comprehensive Content Audit
# Analyzes all content in pixelation and generates detailed report

set -e

PIXEL_DIR="/data/data/com.termux/files/home/pixelation"
DUP_DIR="/data/data/com.termux/files/home/PIXEL_DUPLICATES"
REPORT_DIR="${PIXEL_DIR}/.sync"
REPORT_FILE="${REPORT_DIR}/content-audit-$(date +%Y%m%d-%H%M%S).md"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo "╔════════════════════════════════════════╗"
echo "║      PIXEL Domos Content Audit         ║"
echo "╚════════════════════════════════════════╝"
echo ""

cd "$PIXEL_DIR" || exit 1

# Create report header
cat > "$REPORT_FILE" << 'EOF'
# PIXEL Domos Content Audit Report

**Generated**: $(date)
**Location**: /data/data/com.termux/files/home/pixelation

---

## Executive Summary

EOF

echo -e "${BLUE}[INFO]${NC} Scanning directory structure..."

# Count statistics
TOTAL_FILES=$(find . -type f -not -path '*/\.*' | wc -l)
TOTAL_DIRS=$(find . -type d -not -path '*/\.*' | wc -l)
TOTAL_SIZE=$(du -sh . | cut -f1)

# Add to report
cat >> "$REPORT_FILE" << EOF
- **Total Files**: $TOTAL_FILES
- **Total Directories**: $TOTAL_DIRS
- **Total Size**: $TOTAL_SIZE

---

## Directory Structure

\`\`\`
EOF

# Generate tree view (limited depth)
if command -v tree &> /dev/null; then
    tree -L 3 -d -I '.git' >> "$REPORT_FILE"
else
    find . -type d -not -path '*/\.*' | head -50 | sort >> "$REPORT_FILE"
fi

cat >> "$REPORT_FILE" << 'EOF'
```

---

## File Type Distribution

EOF

echo -e "${BLUE}[INFO]${NC} Analyzing file types..."

# File type analysis
find . -type f -not -path '*/\.*' -exec file {} \; | \
    awk -F: '{print $2}' | \
    sort | uniq -c | sort -rn | head -20 >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## Large Files (>10MB)

EOF

echo -e "${BLUE}[INFO]${NC} Finding large files..."

# Find large files
find . -type f -size +10M -not -path '*/\.*' -exec ls -lh {} \; | \
    awk '{print $5 "\t" $9}' | \
    sort -h -r >> "$REPORT_FILE" || echo "*No large files found*" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## Potential "Sort" Folders

EOF

echo -e "${BLUE}[INFO]${NC} Looking for sort/temp folders..."

# Find sort-like folders
find . -type d \( -name '*sort*' -o -name '*temp*' -o -name '*tmp*' -o -name '*old*' -o -name '*backup*' \) \
    -not -path '*/\.*' >> "$REPORT_FILE" || echo "*No sort folders found*" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## File Extensions Summary

EOF

echo -e "${BLUE}[INFO]${NC} Counting file extensions..."

# Count by extension
find . -type f -not -path '*/\.*' | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -30 >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## Recently Modified Files (Last 7 days)

EOF

echo -e "${BLUE}[INFO]${NC} Finding recent files..."

# Recent files
find . -type f -mtime -7 -not -path '*/\.*' -exec ls -lh {} \; | \
    awk '{print $6, $7, $8, "\t", $9}' | \
    head -20 >> "$REPORT_FILE" || echo "*No recently modified files*" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## Oldest Files

EOF

echo -e "${BLUE}[INFO]${NC} Finding oldest files..."

# Oldest files
find . -type f -not -path '*/\.*' -exec ls -lt {} \; | \
    tail -20 | \
    awk '{print $6, $7, $8, "\t", $9}' >> "$REPORT_FILE" || echo "*No old files found*" >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## Hidden Files/Directories

EOF

echo -e "${BLUE}[INFO]${NC} Listing hidden files..."

# Hidden files
find . -name ".*" -not -path '*/\.' -not -path '*/..' | head -50 >> "$REPORT_FILE"

cat >> "$REPORT_FILE" << 'EOF'

---

## Recommendations

### Immediate Actions
1. Review large files (>10MB) - consider moving to PIXEL_DUPLICATES
2. Sort "sort/temp/old" folders into proper locations
3. Archive oldest files if no longer needed
4. Review hidden files for cleanup

### Content Organization
1. Move active projects to appropriate `projects/` subdirectories
2. Sort media to `assets/` by type
3. Organize documentation to `docs/`
4. Archive historical content to `archive/`

### Cleanup Opportunities
- Remove duplicate files
- Delete temporary files
- Compress large archives
- Clean up old backups

---

## Next Steps

1. Run duplicate finder: `./tools/utilities/find-duplicates.sh`
2. Run large file analyzer: `./tools/utilities/find-large-files.sh`
3. Review this report and create migration plan
4. Execute content migration systematically
5. Update RESTRUCTURE_LOG.md with changes

---

**Report saved**: `.sync/content-audit-[timestamp].md`

EOF

# Display summary
echo ""
echo -e "${GREEN}✓ Audit Complete${NC}"
echo ""
echo -e "${CYAN}Summary:${NC}"
echo "  Files: $TOTAL_FILES"
echo "  Directories: $TOTAL_DIRS"
echo "  Total Size: $TOTAL_SIZE"
echo ""
echo -e "${CYAN}Report saved to:${NC}"
echo "  $REPORT_FILE"
echo ""
echo "View with: cat $REPORT_FILE"
echo "  or: less $REPORT_FILE"
echo ""

# Ask if user wants to view now
echo "View report now? (y/n)"
read -p "> " view_now

if [ "$view_now" = "y" ] || [ "$view_now" = "Y" ]; then
    if command -v less &> /dev/null; then
        less "$REPORT_FILE"
    else
        cat "$REPORT_FILE"
    fi
fi

echo ""
echo -e "${BLUE}[INFO]${NC} Next: Run find-duplicates.sh and find-large-files.sh for detailed analysis"
echo ""
