#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Bidirectional Sync Script
# Syncs between pixel8 (internal) and pixel8a (external) based on rules

set -e  # Exit on error

# Paths
INTERNAL="/data/data/com.termux/files/home/pixelation"
EXTERNAL="/data/data/com.termux/files/home/storage/shared/pixelate"
EXCLUDE_FILE="${INTERNAL}/.sync/exclude.txt"
RULES_FILE="${INTERNAL}/.sync/rules.yaml"
LOG_FILE="${INTERNAL}/.sync/sync.log"
STATE_FILE="${INTERNAL}/.sync/last-sync.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
log() {
    echo -e "${GREEN}[SYNC]${NC} $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] WARN: $1" >> "$LOG_FILE"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: $1" >> "$LOG_FILE"
}

info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

# Banner
echo ""
echo "╔════════════════════════════════════════╗"
echo "║     PIXEL Domos Sync System            ║"
echo "║  pixel8 (internal) ⇄ pixel8a (external)║"
echo "╚════════════════════════════════════════╝"
echo ""

# Check if rsync is available
if ! command -v rsync &> /dev/null; then
    error "rsync not found. Install with: pkg install rsync"
    exit 1
fi

# Verify paths exist
if [ ! -d "$INTERNAL" ]; then
    error "Internal path not found: $INTERNAL"
    exit 1
fi

if [ ! -d "$EXTERNAL" ]; then
    warn "External path not found, creating: $EXTERNAL"
    mkdir -p "$EXTERNAL"
fi

# Start sync
log "Starting bidirectional sync..."
log "Internal: $INTERNAL"
log "External: $EXTERNAL"
echo ""

# Sync bidirectional folders
info "Phase 1: Syncing bidirectional folders..."
echo ""

# Projects shared
if [ -d "${INTERNAL}/projects/shared" ]; then
    log "Syncing projects/shared/ (bidirectional)"

    # Internal → External
    rsync -avz --delete \
        --exclude-from="$EXCLUDE_FILE" \
        "${INTERNAL}/projects/shared/" \
        "${EXTERNAL}/projects/shared/" 2>&1 | tee -a "$LOG_FILE"

    # External → Internal
    rsync -avz \
        --exclude-from="$EXCLUDE_FILE" \
        "${EXTERNAL}/projects/shared/" \
        "${INTERNAL}/projects/shared/" 2>&1 | tee -a "$LOG_FILE"

    echo ""
fi

# Docs public (if exists)
if [ -d "${INTERNAL}/docs/public" ]; then
    log "Syncing docs/public/ (bidirectional)"

    # Internal → External
    rsync -avz --delete \
        --exclude-from="$EXCLUDE_FILE" \
        "${INTERNAL}/docs/public/" \
        "${EXTERNAL}/docs/public/" 2>&1 | tee -a "$LOG_FILE"

    # External → Internal
    rsync -avz \
        --exclude-from="$EXCLUDE_FILE" \
        "${EXTERNAL}/docs/public/" \
        "${INTERNAL}/docs/public/" 2>&1 | tee -a "$LOG_FILE"

    echo ""
fi

# Assets shared
if [ -d "${INTERNAL}/assets/shared" ]; then
    log "Syncing assets/shared/ (bidirectional)"

    # Internal → External
    rsync -avz --delete \
        --exclude-from="$EXCLUDE_FILE" \
        "${INTERNAL}/assets/shared/" \
        "${EXTERNAL}/assets/shared/" 2>&1 | tee -a "$LOG_FILE"

    # External → Internal
    rsync -avz \
        --exclude-from="$EXCLUDE_FILE" \
        "${EXTERNAL}/assets/shared/" \
        "${INTERNAL}/assets/shared/" 2>&1 | tee -a "$LOG_FILE"

    echo ""
fi

# Sync external-only from external to internal (read-only)
info "Phase 2: Pulling external-only content..."
echo ""

if [ -d "${EXTERNAL}/published" ]; then
    log "Pulling published/ (external → internal, read-only mirror)"

    mkdir -p "${INTERNAL}/published"
    rsync -avz \
        --exclude-from="$EXCLUDE_FILE" \
        "${EXTERNAL}/published/" \
        "${INTERNAL}/published/" 2>&1 | tee -a "$LOG_FILE"

    echo ""
fi

if [ -d "${EXTERNAL}/releases" ]; then
    log "Pulling releases/ (external → internal, read-only mirror)"

    mkdir -p "${INTERNAL}/releases"
    rsync -avz \
        --exclude-from="$EXCLUDE_FILE" \
        "${EXTERNAL}/releases/" \
        "${INTERNAL}/releases/" 2>&1 | tee -a "$LOG_FILE"

    echo ""
fi

# Update state file
SYNC_TIME=$(date -Iseconds)
TOTAL_SIZE=$(du -sh "$EXTERNAL" | cut -f1)

cat > "$STATE_FILE" << EOF
{
  "last_sync": "$SYNC_TIME",
  "status": "success",
  "internal_path": "$INTERNAL",
  "external_path": "$EXTERNAL",
  "conflicts": [],
  "stats": {
    "sync_time": "$SYNC_TIME",
    "external_size": "$TOTAL_SIZE"
  }
}
EOF

# Summary
echo ""
echo "╔════════════════════════════════════════╗"
echo "║           Sync Complete ✓              ║"
echo "╚════════════════════════════════════════╝"
echo ""
log "Sync completed successfully"
info "Last sync: $SYNC_TIME"
info "External size: $TOTAL_SIZE"
echo ""
info "Check log: cat .sync/sync.log"
info "Check state: cat .sync/last-sync.json"
echo ""
