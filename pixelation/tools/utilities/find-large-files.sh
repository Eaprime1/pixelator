#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Large File Finder
# Finds files over size thresholds

set -e

PIXEL_DIR="/data/data/com.termux/files/home/pixelation"
DUP_DIR="/data/data/com.termux/files/home/PIXEL_DUPLICATES"
REPORT_FILE="$DUP_DIR/large-files-report.txt"

echo "📊 PIXEL Large File Finder"
echo "==========================="
echo ""

# Thresholds in KB
THRESHOLD_IMAGE=10240      # 10MB
THRESHOLD_VIDEO=51200      # 50MB
THRESHOLD_ARCHIVE=25600    # 25MB
THRESHOLD_DOC=5120         # 5MB
THRESHOLD_CODE=1024        # 1MB
THRESHOLD_GENERAL=10240    # 10MB default

echo "Scanning for large files in: $PIXEL_DIR"
echo ""
echo "Thresholds:"
echo "  Images:   > 10MB"
echo "  Videos:   > 50MB"
echo "  Archives: > 25MB"
echo "  Docs:     > 5MB"
echo "  Code:     > 1MB"
echo "  Other:    > 10MB"
echo ""

# Find all files and sort by size
echo "Finding files..."
cd "$PIXEL_DIR" || exit 1

# Create report header
cat > "$REPORT_FILE" << 'EOF'
# Large Files Report
Generated: $(date)

## All Files Over 10MB
EOF

# Find large files (over 10MB)
echo "" >> "$REPORT_FILE"
echo "### Files over 10MB" >> "$REPORT_FILE"
find . -type f -size +10M -not -path '*/\.*' -exec ls -lh {} \; | \
    awk '{print $9 " - " $5}' | \
    sort -k3 -h -r >> "$REPORT_FILE"

# Find by category
echo "" >> "$REPORT_FILE"
echo "### Large Images (>10MB)" >> "$REPORT_FILE"
find . -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.bmp" -o -iname "*.tiff" \) \
    -size +10M -not -path '*/\.*' -exec ls -lh {} \; | \
    awk '{print $9 " - " $5}' | \
    sort -k3 -h -r >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "### Large Videos (>50MB)" >> "$REPORT_FILE"
find . -type f \( -iname "*.mp4" -o -iname "*.mov" -o -iname "*.avi" -o -iname "*.mkv" -o -iname "*.flv" -o -iname "*.wmv" \) \
    -size +50M -not -path '*/\.*' -exec ls -lh {} \; | \
    awk '{print $9 " - " $5}' | \
    sort -k3 -h -r >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "### Large Archives (>25MB)" >> "$REPORT_FILE"
find . -type f \( -iname "*.zip" -o -iname "*.tar" -o -iname "*.tar.gz" -o -iname "*.rar" -o -iname "*.7z" \) \
    -size +25M -not -path '*/\.*' -exec ls -lh {} \; | \
    awk '{print $9 " - " $5}' | \
    sort -k3 -h -r >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "### Suspicious Large Code Files (>1MB)" >> "$REPORT_FILE"
find . -type f \( -iname "*.js" -o -iname "*.py" -o -iname "*.java" -o -iname "*.cpp" -o -iname "*.c" -o -iname "*.go" \) \
    -size +1M -not -path '*/\.*' -not -path '*/node_modules/*' -exec ls -lh {} \; | \
    awk '{print $9 " - " $5}' | \
    sort -k3 -h -r >> "$REPORT_FILE"

# Display summary
echo "✓ Report generated!"
echo ""
echo "Summary:"
echo "--------"

LARGE_COUNT=$(find . -type f -size +10M -not -path '*/\.*' | wc -l)
TOTAL_SIZE=$(find . -type f -size +10M -not -path '*/\.*' -exec du -ch {} + | tail -1 | awk '{print $1}')

echo "Files over 10MB: $LARGE_COUNT"
echo "Total size: $TOTAL_SIZE"
echo ""

echo "📄 Full report saved to:"
echo "   $REPORT_FILE"
echo ""

# Ask if user wants to view top 20
echo "Show top 20 largest files? (y/n)"
read -p "> " show_top

if [ "$show_top" = "y" ] || [ "$show_top" = "Y" ]; then
    echo ""
    echo "Top 20 Largest Files:"
    echo "===================="
    find . -type f -not -path '*/\.*' -exec ls -lh {} \; | \
        sort -k5 -h -r | \
        head -20 | \
        awk '{print $5 "\t" $9}'
fi

echo ""
echo "Done!"
