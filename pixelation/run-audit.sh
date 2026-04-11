#!/data/data/com.termux/files/usr/bin/bash
# Quick audit runner
cd /data/data/com.termux/files/home/pixelation
chmod +x tools/utilities/content-audit.sh
chmod +x tools/utilities/find-duplicates.sh
chmod +x tools/utilities/find-large-files.sh
chmod +x tools/utilities/migration-helper.sh
chmod +x tools/sync/basic-sync.sh

echo "Making all scripts executable..."
echo "✓ Scripts are now executable"
echo ""

echo "Running content audit..."
./tools/utilities/content-audit.sh
