#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Test Sync
# Safe sync test with dry-run option

echo ""
echo "🔄 PIXEL Domos Sync Test"
echo "========================"
echo ""

INTERNAL="/data/data/com.termux/files/home/pixelation"
EXTERNAL="/data/data/com.termux/files/home/storage/shared/pixelate"

echo "Checking paths..."
echo "  Internal: $INTERNAL"
echo "  External: $EXTERNAL"
echo ""

# Check if rsync is available
if ! command -v rsync &> /dev/null; then
    echo "❌ rsync not found!"
    echo ""
    echo "Install with: pkg install rsync"
    exit 1
fi

echo "✓ rsync is available"
echo ""

# Check if directories exist
if [ ! -d "$INTERNAL" ]; then
    echo "❌ Internal directory not found!"
    exit 1
fi

if [ ! -d "$EXTERNAL" ]; then
    echo "⚠️  External directory not found, creating..."
    mkdir -p "$EXTERNAL"
fi

echo "✓ Directories verified"
echo ""

# Offer dry-run first
echo "Run as dry-run first (recommended)? (y/n)"
read -p "> " dryrun

if [ "$dryrun" = "y" ] || [ "$dryrun" = "Y" ]; then
    echo ""
    echo "🔍 DRY RUN - Showing what would be synced..."
    echo ""

    # Dry run - internal to external
    echo "Internal → External (dry-run):"
    rsync -avzn --exclude-from="${INTERNAL}/.sync/exclude.txt" \
        "${INTERNAL}/projects/shared/" "${EXTERNAL}/projects/shared/" 2>&1 | head -20

    echo ""
    echo "This is what WOULD happen. No files were actually copied."
    echo ""
    echo "Run actual sync? (y/n)"
    read -p "> " runsync

    if [ "$runsync" != "y" ] && [ "$runsync" != "Y" ]; then
        echo "Cancelled."
        exit 0
    fi
fi

# Actual sync
echo ""
echo "🚀 Running actual sync..."
echo ""

# Ensure shared directories exist
mkdir -p "${INTERNAL}/projects/shared"
mkdir -p "${EXTERNAL}/projects/shared"
mkdir -p "${INTERNAL}/assets/shared"
mkdir -p "${EXTERNAL}/assets/shared"

# Sync shared projects
echo "Syncing projects/shared..."
rsync -avz --delete --exclude-from="${INTERNAL}/.sync/exclude.txt" \
    "${INTERNAL}/projects/shared/" "${EXTERNAL}/projects/shared/"

rsync -avz --exclude-from="${INTERNAL}/.sync/exclude.txt" \
    "${EXTERNAL}/projects/shared/" "${INTERNAL}/projects/shared/"

# Sync shared assets
echo ""
echo "Syncing assets/shared..."
rsync -avz --delete --exclude-from="${INTERNAL}/.sync/exclude.txt" \
    "${INTERNAL}/assets/shared/" "${EXTERNAL}/assets/shared/"

rsync -avz --exclude-from="${INTERNAL}/.sync/exclude.txt" \
    "${EXTERNAL}/assets/shared/" "${INTERNAL}/assets/shared/"

# Update state
SYNC_TIME=$(date '+%Y-%m-%d %H:%M:%S')

echo ""
echo "✅ Sync complete!"
echo "   Time: $SYNC_TIME"
echo ""

# Show what was synced
echo "📊 External size:"
du -sh "$EXTERNAL" 2>/dev/null

echo ""
echo "View full sync log: cat .sync/sync.log"
echo "View sync state: cat .sync/last-sync.json"
echo ""
