#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Simple Audit (works around permission issues)
# Basic content discovery without complex operations

echo ""
echo "🔍 PIXEL Domos Simple Audit"
echo "============================="
echo ""

cd /data/data/com.termux/files/home/pixelation || exit 1

echo "📊 Current Location:"
pwd
echo ""

echo "📁 Top-level directories:"
ls -lh | grep "^d" | awk '{print $9, "(" $5 ")"}'
echo ""

echo "📄 Top-level files:"
ls -lh | grep "^-" | awk '{print $9, "(" $5 ")"}'
echo ""

echo "📈 Quick Statistics:"
echo "  Total items: $(ls -1 | wc -l)"
echo "  Directories: $(ls -l | grep "^d" | wc -l)"
echo "  Files: $(ls -l | grep "^-" | wc -l)"
echo ""

echo "💾 Disk Usage (top level):"
du -sh */ 2>/dev/null | sort -h -r | head -10
echo ""

echo "🔎 Looking for sort/temp/old folders..."
find . -maxdepth 2 -type d \( -iname "*sort*" -o -iname "*temp*" -o -iname "*tmp*" -o -iname "*old*" -o -iname "*backup*" \) 2>/dev/null | head -20
echo ""

echo "📦 Largest files (top 10):"
find . -maxdepth 2 -type f -exec ls -lh {} \; 2>/dev/null | sort -k5 -h -r | head -10 | awk '{print $9, ":", $5}'
echo ""

echo "📝 File count by extension:"
find . -maxdepth 2 -type f 2>/dev/null | sed 's/.*\.//' | sort | uniq -c | sort -rn | head -15
echo ""

echo "✅ Simple audit complete!"
echo ""
echo "For detailed audit, run: ./tools/utilities/content-audit.sh"
echo "To organize content: ./tools/utilities/migration-helper.sh"
echo ""
