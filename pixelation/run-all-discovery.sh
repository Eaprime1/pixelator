#!/data/data/com.termux/files/usr/bin/bash
# Run all discovery tools in sequence

cd /data/data/com.termux/files/home/pixelation

echo ""
echo "╔════════════════════════════════════════╗"
echo "║   PIXEL Domos Discovery Suite          ║"
echo "╚════════════════════════════════════════╝"
echo ""

echo "This will run:"
echo "  1. Content Audit"
echo "  2. Duplicate Finder"
echo "  3. Large File Finder"
echo ""
read -p "Continue? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "═══════════════════════════════════════"
echo "  Phase 1: Content Audit"
echo "═══════════════════════════════════════"
echo ""
./tools/utilities/content-audit.sh

echo ""
echo "═══════════════════════════════════════"
echo "  Phase 2: Finding Duplicates"
echo "═══════════════════════════════════════"
echo ""
./tools/utilities/find-duplicates.sh

echo ""
echo "═══════════════════════════════════════"
echo "  Phase 3: Finding Large Files"
echo "═══════════════════════════════════════"
echo ""
./tools/utilities/find-large-files.sh

echo ""
echo "╔════════════════════════════════════════╗"
echo "║       Discovery Complete!              ║"
echo "╚════════════════════════════════════════╝"
echo ""
echo "Review the reports:"
echo "  - Content Audit: .sync/content-audit-*.md"
echo "  - Large Files: ${PIXEL_DUPLICATES}/large-files-report.txt"
echo "  - Duplicates: Output above or reports generated"
echo ""
echo "Next: Run sync with ./tools/sync/basic-sync.sh"
echo ""
