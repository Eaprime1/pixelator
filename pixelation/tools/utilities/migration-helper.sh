#!/data/data/com.termux/files/usr/bin/bash

# PIXEL Domos - Interactive Migration Helper
# Helps organize content into proper PIXEL structure

set -e

PIXEL_DIR="/data/data/com.termux/files/home/pixelation"
DUP_DIR="/data/data/com.termux/files/home/PIXEL_DUPLICATES"
LOG_FILE="${PIXEL_DIR}/RESTRUCTURE_LOG.md"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo "╔════════════════════════════════════════╗"
echo "║    PIXEL Domos Migration Helper        ║"
echo "╚════════════════════════════════════════╝"
echo ""

cd "$PIXEL_DIR" || exit 1

# Helper function to log migration
log_migration() {
    local action="$1"
    local source="$2"
    local dest="$3"
    local reason="$4"

    cat >> "$LOG_FILE" << EOF

## [$(date '+%Y-%m-%d %H:%M')] Content Migration

### Type: $action

**What**: Moved content
- Source: $source
- Destination: $dest

**Why**: $reason

**Impact**: Content organization

---
EOF

    echo -e "${GREEN}✓${NC} Logged to RESTRUCTURE_LOG.md"
}

# Main menu
show_menu() {
    echo ""
    echo -e "${CYAN}What would you like to organize?${NC}"
    echo ""
    echo "  1) Move files to projects/"
    echo "  2) Move files to assets/"
    echo "  3) Move files to docs/"
    echo "  4) Move files to archive/"
    echo "  5) Move files to PIXEL_DUPLICATES"
    echo "  6) Delete files/folders"
    echo "  7) Batch rename"
    echo "  8) View directory structure"
    echo "  9) Exit"
    echo ""
    read -p "Choice (1-9): " choice

    case $choice in
        1) move_to_projects ;;
        2) move_to_assets ;;
        3) move_to_docs ;;
        4) move_to_archive ;;
        5) move_to_duplicates ;;
        6) delete_content ;;
        7) batch_rename ;;
        8) view_structure ;;
        9) exit 0 ;;
        *) echo -e "${RED}Invalid choice${NC}" ; show_menu ;;
    esac
}

move_to_projects() {
    echo ""
    echo -e "${CYAN}Move to projects/${NC}"
    echo ""
    read -p "Source path (relative to pixelation): " source
    echo ""
    echo "Choose destination:"
    echo "  1) projects/pixel8/ (internal-only)"
    echo "  2) projects/pixel8a/ (external projects)"
    echo "  3) projects/experimental/ (experiments)"
    echo "  4) projects/shared/ (synced bidirectionally)"
    echo ""
    read -p "Choice (1-4): " dest_choice

    case $dest_choice in
        1) dest="projects/pixel8/" ;;
        2) dest="projects/pixel8a/" ;;
        3) dest="projects/experimental/" ;;
        4) dest="projects/shared/" ;;
        *) echo -e "${RED}Invalid choice${NC}" ; return ;;
    esac

    read -p "Project name: " project_name
    dest="${dest}${project_name}"

    read -p "Reason for move: " reason

    echo ""
    echo -e "${YELLOW}Moving:${NC} $source → $dest"
    read -p "Confirm? (y/n): " confirm

    if [ "$confirm" = "y" ]; then
        mkdir -p "$dest"
        mv "$source" "$dest/"
        echo -e "${GREEN}✓ Moved${NC}"
        log_migration "MOVE" "$source" "$dest" "$reason"
    fi

    show_menu
}

move_to_assets() {
    echo ""
    echo -e "${CYAN}Move to assets/${NC}"
    echo ""
    read -p "Source path (relative to pixelation): " source
    echo ""
    echo "Choose asset type:"
    echo "  1) assets/images/"
    echo "  2) assets/videos/"
    echo "  3) assets/audio/"
    echo "  4) assets/data/"
    echo "  5) assets/shared/ (synced)"
    echo ""
    read -p "Choice (1-5): " dest_choice

    case $dest_choice in
        1) dest="assets/images/" ;;
        2) dest="assets/videos/" ;;
        3) dest="assets/audio/" ;;
        4) dest="assets/data/" ;;
        5) dest="assets/shared/" ;;
        *) echo -e "${RED}Invalid choice${NC}" ; return ;;
    esac

    read -p "Reason for move: " reason

    echo ""
    echo -e "${YELLOW}Moving:${NC} $source → $dest"
    read -p "Confirm? (y/n): " confirm

    if [ "$confirm" = "y" ]; then
        mkdir -p "$dest"
        mv "$source" "$dest/"
        echo -e "${GREEN}✓ Moved${NC}"
        log_migration "MOVE" "$source" "$dest" "$reason"
    fi

    show_menu
}

move_to_docs() {
    echo ""
    echo -e "${CYAN}Move to docs/${NC}"
    echo ""
    read -p "Source path (relative to pixelation): " source
    echo ""
    echo "Choose docs type:"
    echo "  1) docs/architecture/"
    echo "  2) docs/guides/"
    echo "  3) docs/api/"
    echo "  4) docs/vision/"
    echo "  5) docs/public/ (synced)"
    echo ""
    read -p "Choice (1-5): " dest_choice

    case $dest_choice in
        1) dest="docs/architecture/" ;;
        2) dest="docs/guides/" ;;
        3) dest="docs/api/" ;;
        4) dest="docs/vision/" ;;
        5) dest="docs/public/" ;;
        *) echo -e "${RED}Invalid choice${NC}" ; return ;;
    esac

    read -p "Reason for move: " reason

    echo ""
    echo -e "${YELLOW}Moving:${NC} $source → $dest"
    read -p "Confirm? (y/n): " confirm

    if [ "$confirm" = "y" ]; then
        mkdir -p "$dest"
        mv "$source" "$dest/"
        echo -e "${GREEN}✓ Moved${NC}"
        log_migration "MOVE" "$source" "$dest" "$reason"
    fi

    show_menu
}

move_to_archive() {
    echo ""
    echo -e "${CYAN}Move to archive/${NC}"
    echo ""
    read -p "Source path (relative to pixelation): " source
    echo ""
    echo "Choose archive type:"
    echo "  1) archive/sorted/ (previously sorted)"
    echo "  2) archive/legacy/ (old projects)"
    echo ""
    read -p "Choice (1-2): " dest_choice

    case $dest_choice in
        1) dest="archive/sorted/" ;;
        2) dest="archive/legacy/" ;;
        *) echo -e "${RED}Invalid choice${NC}" ; return ;;
    esac

    # Add timestamp to archived items
    timestamp=$(date +%Y%m%d)
    basename=$(basename "$source")
    dest="${dest}${basename}-${timestamp}"

    read -p "Reason for archiving: " reason

    echo ""
    echo -e "${YELLOW}Archiving:${NC} $source → $dest"
    read -p "Confirm? (y/n): " confirm

    if [ "$confirm" = "y" ]; then
        mkdir -p "$(dirname "$dest")"
        mv "$source" "$dest"
        echo -e "${GREEN}✓ Archived${NC}"
        log_migration "ARCHIVE" "$source" "$dest" "$reason"
    fi

    show_menu
}

move_to_duplicates() {
    echo ""
    echo -e "${CYAN}Move to PIXEL_DUPLICATES/${NC}"
    echo ""
    read -p "Source path (relative to pixelation): " source
    echo ""
    echo "Choose duplicate category:"
    echo "  1) duplicates/"
    echo "  2) large-files/"
    echo "  3) questionable/"
    echo ""
    read -p "Choice (1-3): " dest_choice

    case $dest_choice in
        1) dest="${DUP_DIR}/duplicates/" ;;
        2) dest="${DUP_DIR}/large-files/" ;;
        3) dest="${DUP_DIR}/questionable/" ;;
        *) echo -e "${RED}Invalid choice${NC}" ; return ;;
    esac

    read -p "Reason: " reason

    echo ""
    echo -e "${YELLOW}Moving:${NC} $source → $dest"
    read -p "Confirm? (y/n): " confirm

    if [ "$confirm" = "y" ]; then
        mkdir -p "$dest"
        mv "$source" "$dest/"
        echo -e "${GREEN}✓ Moved to PIXEL_DUPLICATES${NC}"

        # Log to duplicate log
        echo "### [$(date '+%Y-%m-%d')] $(basename "$source")" >> "${DUP_DIR}/DUPLICATE_LOG.md"
        echo "- **Original**: $source" >> "${DUP_DIR}/DUPLICATE_LOG.md"
        echo "- **Moved to**: $dest" >> "${DUP_DIR}/DUPLICATE_LOG.md"
        echo "- **Reason**: $reason" >> "${DUP_DIR}/DUPLICATE_LOG.md"
        echo "" >> "${DUP_DIR}/DUPLICATE_LOG.md"
    fi

    show_menu
}

delete_content() {
    echo ""
    echo -e "${RED}⚠️  DELETE CONTENT${NC}"
    echo ""
    read -p "Path to delete (relative to pixelation): " target
    echo ""
    echo -e "${RED}WARNING: This will permanently delete:${NC}"
    echo "  $target"
    echo ""
    read -p "Type 'DELETE' to confirm: " confirm

    if [ "$confirm" = "DELETE" ]; then
        rm -rf "$target"
        echo -e "${GREEN}✓ Deleted${NC}"
        log_migration "DELETE" "$target" "deleted" "User confirmed deletion"
    else
        echo -e "${YELLOW}Cancelled${NC}"
    fi

    show_menu
}

batch_rename() {
    echo ""
    echo -e "${CYAN}Batch Rename${NC}"
    echo ""
    read -p "Directory path: " dir_path
    read -p "Find pattern: " find_pattern
    read -p "Replace with: " replace_pattern

    echo ""
    echo "Preview:"
    find "$dir_path" -name "*${find_pattern}*" | while read file; do
        new_name=$(echo "$file" | sed "s/${find_pattern}/${replace_pattern}/")
        echo "  $file → $new_name"
    done

    echo ""
    read -p "Execute rename? (y/n): " confirm

    if [ "$confirm" = "y" ]; then
        find "$dir_path" -name "*${find_pattern}*" | while read file; do
            new_name=$(echo "$file" | sed "s/${find_pattern}/${replace_pattern}/")
            mv "$file" "$new_name"
        done
        echo -e "${GREEN}✓ Renamed${NC}"
    fi

    show_menu
}

view_structure() {
    echo ""
    if command -v tree &> /dev/null; then
        tree -L 2 -d
    else
        find . -type d -not -path '*/\.*' | head -30 | sort
    fi
    show_menu
}

# Start
show_menu
