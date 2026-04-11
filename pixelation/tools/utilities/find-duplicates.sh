#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Duplicate File Finder
# Finds duplicate files and moves them to PIXEL_DUPLICATES

set -e

PIXEL_DIR="/data/data/com.termux/files/home/pixelation"
DUP_DIR="/data/data/com.termux/files/home/PIXEL_DUPLICATES"
LOG_FILE="$DUP_DIR/DUPLICATE_LOG.md"

echo "🔍 PIXEL Duplicate Finder"
echo "========================="
echo ""

# Check if fdupes is installed
if ! command -v fdupes &> /dev/null; then
    echo "⚠️  fdupes not found. Install with: pkg install fdupes"
    echo ""
    echo "Alternative: Using find with md5sum (slower)..."

    # Alternative method using md5sum
    cd "$PIXEL_DIR" || exit 1
    find . -type f -not -path '*/\.*' -exec md5sum {} \; | \
        sort | \
        uniq -w32 -dD | \
        while read sum file; do
            echo "Duplicate: $file (md5: $sum)"
        done

    exit 0
fi

# Use fdupes to find duplicates
echo "Scanning for duplicates in: $PIXEL_DIR"
echo "This may take a while..."
echo ""

fdupes -r "$PIXEL_DIR" > /tmp/pixel-duplicates.txt

# Process results
if [ -s /tmp/pixel-duplicates.txt ]; then
    echo "✓ Found duplicates!"
    echo ""
    cat /tmp/pixel-duplicates.txt
    echo ""

    # Ask user what to do
    echo "Would you like to:"
    echo "  1) Review interactively"
    echo "  2) Generate report only"
    echo "  3) Auto-move duplicates (keeps first, moves rest)"
    echo ""
    read -p "Choice (1-3): " choice

    case $choice in
        1)
            fdupes -r -d "$PIXEL_DIR"
            ;;
        2)
            cp /tmp/pixel-duplicates.txt "$DUP_DIR/duplicate-report.txt"
            echo "✓ Report saved to: $DUP_DIR/duplicate-report.txt"
            ;;
        3)
            echo "Auto-moving duplicates..."
            # This would need more sophisticated logic
            echo "⚠️  Manual review recommended - use option 1 instead"
            ;;
    esac
else
    echo "✓ No duplicates found!"
fi

rm -f /tmp/pixel-duplicates.txt
echo ""
echo "Done!"
