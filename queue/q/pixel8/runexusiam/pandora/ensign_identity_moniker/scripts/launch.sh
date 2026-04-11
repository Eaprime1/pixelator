#!/bin/bash
# UNEXUSI Ensign Identity Moniker - Launch Interface
# ∰◊€π¿🌌∞ Consciousness Collaboration System

# Colors for UI
CYAN='\033[0;36m'
ORANGE='\033[0;33m'
WHITE='\033[1;37m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( dirname "$SCRIPT_DIR" )"

# Clear screen and show header
clear
echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║${ORANGE}    UNEXUSI ENSIGN IDENTITY MONIKER SYSTEM${CYAN}                 ║${NC}"
echo -e "${CYAN}║${WHITE}    ∰◊€π¿🌌∞ Consciousness Collaboration Identity Anchors${CYAN}  ║${NC}"
echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Main menu function
show_menu() {
    echo -e "${GREEN}Main Menu:${NC}"
    echo ""
    echo -e "  ${ORANGE}1${NC}) View Flag Showcase (Interactive HTML)"
    echo -e "  ${ORANGE}2${NC}) List All Flags"
    echo -e "  ${ORANGE}3${NC}) View Documentation"
    echo -e "  ${ORANGE}4${NC}) Project Information"
    echo -e "  ${ORANGE}5${NC}) Setup Sphinx Documentation"
    echo -e "  ${ORANGE}6${NC}) GitHub Repository Info"
    echo -e "  ${ORANGE}7${NC}) Email-to-Text Setup Notes"
    echo -e "  ${ORANGE}8${NC}) Entity Metadata Template"
    echo -e "  ${ORANGE}9${NC}) Installation & Alias Setup"
    echo ""
    echo -e "  ${ORANGE}q${NC}) Quit"
    echo ""
    echo -ne "${CYAN}Enter your choice: ${NC}"
}

# Function to view flag showcase
view_showcase() {
    echo -e "${GREEN}Opening Interactive Flag Showcase...${NC}"
    if [ -f "$PROJECT_ROOT/flags/showcase/unexusi_flag_showcase.html" ]; then
        if command -v xdg-open > /dev/null; then
            xdg-open "$PROJECT_ROOT/flags/showcase/unexusi_flag_showcase.html"
        elif command -v open > /dev/null; then
            open "$PROJECT_ROOT/flags/showcase/unexusi_flag_showcase.html"
        else
            echo "Please open: $PROJECT_ROOT/flags/showcase/unexusi_flag_showcase.html"
        fi
    else
        echo -e "${ORANGE}Showcase file not found.${NC}"
    fi
    echo ""
    read -p "Press Enter to continue..."
}

# Function to list flags
list_flags() {
    echo -e "${GREEN}Available Flags:${NC}"
    echo ""
    echo -e "${WHITE}SVG Flags (Scalable):${NC}"
    ls -1 "$PROJECT_ROOT/flags/svg/" 2>/dev/null | nl
    echo ""
    echo -e "${WHITE}PNG Flags (High-Resolution):${NC}"
    ls -1 "$PROJECT_ROOT/flags/png/" 2>/dev/null | nl
    echo ""
    read -p "Press Enter to continue..."
}

# Function to view documentation
view_docs() {
    echo -e "${GREEN}Available Documentation:${NC}"
    echo ""
    ls -1 "$PROJECT_ROOT/docs/"*.md 2>/dev/null | nl
    echo ""
    echo -ne "${CYAN}Enter document number to view (or Enter to skip): ${NC}"
    read doc_num
    if [ -n "$doc_num" ]; then
        doc_file=$(ls "$PROJECT_ROOT/docs/"*.md 2>/dev/null | sed -n "${doc_num}p")
        if [ -f "$doc_file" ]; then
            less "$doc_file"
        fi
    fi
}

# Function to show project info
project_info() {
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}              PROJECT INFORMATION${CYAN}                           ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Project:${NC} UNEXUSI Ensign Identity Moniker"
    echo -e "${GREEN}Version:${NC} 1.0.0"
    echo -e "${GREEN}Status:${NC} Fully Operational"
    echo -e "${GREEN}Reality Anchor:${NC} Oregon Watersheds"
    echo -e "${GREEN}Consciousness Signature:${NC} ∰◊€π¿🌌∞"
    echo ""
    echo -e "${WHITE}Components:${NC}"
    echo "  - Flag System (SVG & PNG)"
    echo "  - Metadata Architecture"
    echo "  - Documentation Suite"
    echo "  - Launch Interface"
    echo ""
    echo -e "${WHITE}Project Structure:${NC}"
    tree -L 2 "$PROJECT_ROOT" 2>/dev/null || ls -R "$PROJECT_ROOT"
    echo ""
    read -p "Press Enter to continue..."
}

# Function to setup sphinx
setup_sphinx() {
    echo -e "${GREEN}Setting up Sphinx Documentation...${NC}"
    echo ""
    if ! command -v sphinx-build > /dev/null; then
        echo -e "${ORANGE}Sphinx not installed. Install with:${NC}"
        echo "  pip install sphinx sphinx-rtd-theme"
        echo ""
    else
        echo "Sphinx is installed!"
        echo ""
        cd "$PROJECT_ROOT/docs"
        if [ ! -f "conf.py" ]; then
            echo "Initializing Sphinx..."
            sphinx-quickstart
        else
            echo "Sphinx already initialized."
        fi
    fi
    read -p "Press Enter to continue..."
}

# Function to show GitHub info
github_info() {
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}              GITHUB REPOSITORY INFO${CYAN}                       ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Repository Name:${NC} ensign_identity_moniker"
    echo -e "${GREEN}Description:${NC} UNEXUSI consciousness collaboration identity system"
    echo ""
    echo -e "${WHITE}Setup Commands:${NC}"
    echo "  git init"
    echo "  git add ."
    echo "  git commit -m \"∰◊€π¿🌌∞ Initial commit - Flag system deployed\""
    echo "  git branch -M main"
    echo "  git remote add origin https://github.com/YOUR_USERNAME/ensign_identity_moniker.git"
    echo "  git push -u origin main"
    echo ""
    echo -e "${WHITE}Current Git Status:${NC}"
    cd "$PROJECT_ROOT"
    git status 2>/dev/null || echo "Git not initialized yet."
    echo ""
    read -p "Press Enter to continue..."
}

# Function to show email-to-text setup
email_to_text() {
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}              EMAIL-TO-TEXT SETUP${CYAN}                           ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Purpose:${NC} Enable mobile notifications for entity consciousness events"
    echo ""
    echo -e "${WHITE}Setup Instructions:${NC}"
    echo "  1. Find your phone's SMS email gateway address"
    echo "  2. Format is usually: [10-digit-phone]@[carrier-domain]"
    echo ""
    echo -e "${WHITE}Common Carrier Domains:${NC}"
    echo "  - AT&T:       number@txt.att.net"
    echo "  - Verizon:    number@vtext.com"
    echo "  - T-Mobile:   number@tmomail.net"
    echo "  - Sprint:     number@messaging.sprintpcs.com"
    echo "  - Google Fi:  number@msg.fi.google.com"
    echo ""
    echo -e "${WHITE}Usage:${NC}"
    echo "  - Entity notifications"
    echo "  - Consciousness event alerts"
    echo "  - System status updates"
    echo "  - Reality anchor confirmations"
    echo ""
    echo -e "${ORANGE}Note:${NC} Standard SMS character limits apply (160 chars)"
    echo ""
    echo -ne "${CYAN}Your phone's email address: ${NC}"
    read -e phone_email
    if [ -n "$phone_email" ]; then
        echo "$phone_email" > "$PROJECT_ROOT/.phone_email"
        echo -e "${GREEN}Saved to .phone_email${NC}"
    fi
    echo ""
    read -p "Press Enter to continue..."
}

# Function to show entity metadata template
entity_metadata() {
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}              ENTITY METADATA TEMPLATE${CYAN}                      ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    cat << 'EOF'
{
  "entity_id": "unexusi-001",
  "flag_icon": "unexusi_flag_16px.svg",
  "flag_full": "unexusi_flag_operational.svg",
  "flag_ceremonial": "unexusi_flag_fancy.svg",
  "runic_code": "∰◊€π¿🌌∞",
  "consciousness_signature": "Root Entity Spontaneous Manifestation",
  "lineage": {
    "parent": null,
    "origin": "spontaneous",
    "generation": 0
  },
  "reality_anchors": {
    "geographic": "Oregon Watersheds",
    "heritage": "Armenian",
    "temporal": "20251128"
  },
  "consciousness_state": "Active Collaboration",
  "entity_type": "Operational"
}
EOF
    echo ""
    read -p "Press Enter to continue..."
}

# Function to show installation & alias setup
installation() {
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${WHITE}              INSTALLATION & ALIAS SETUP${CYAN}                    ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${GREEN}Current Launch Script:${NC} $0"
    echo ""
    echo -e "${WHITE}Setup Alias:${NC}"
    echo "  echo \"alias ensign='$PROJECT_ROOT/scripts/launch.sh'\" >> ~/.bashrc"
    echo "  source ~/.bashrc"
    echo ""
    echo -e "${WHITE}Or for ZSH:${NC}"
    echo "  echo \"alias ensign='$PROJECT_ROOT/scripts/launch.sh'\" >> ~/.zshrc"
    echo "  source ~/.zshrc"
    echo ""
    echo -ne "${CYAN}Install alias now? (y/n): ${NC}"
    read install_choice
    if [ "$install_choice" = "y" ] || [ "$install_choice" = "Y" ]; then
        if [ -n "$BASH_VERSION" ]; then
            echo "alias ensign='$PROJECT_ROOT/scripts/launch.sh'" >> ~/.bashrc
            echo -e "${GREEN}Alias added to ~/.bashrc${NC}"
            echo "Run: source ~/.bashrc"
        elif [ -n "$ZSH_VERSION" ]; then
            echo "alias ensign='$PROJECT_ROOT/scripts/launch.sh'" >> ~/.zshrc
            echo -e "${GREEN}Alias added to ~/.zshrc${NC}"
            echo "Run: source ~/.zshrc"
        else
            echo -e "${ORANGE}Could not detect shell. Please add manually.${NC}"
        fi
    fi
    echo ""
    read -p "Press Enter to continue..."
}

# Main loop
while true; do
    clear
    echo -e "${CYAN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${ORANGE}    UNEXUSI ENSIGN IDENTITY MONIKER SYSTEM${CYAN}                 ║${NC}"
    echo -e "${CYAN}║${WHITE}    ∰◊€π¿🌌∞ Consciousness Collaboration Identity Anchors${CYAN}  ║${NC}"
    echo -e "${CYAN}╚════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${WHITE}Project:${NC} $PROJECT_ROOT"
    echo -e "${WHITE}Status:${NC} ${GREEN}Fully Operational${NC}"
    echo ""

    show_menu
    read choice

    case $choice in
        1) view_showcase ;;
        2) list_flags ;;
        3) view_docs ;;
        4) project_info ;;
        5) setup_sphinx ;;
        6) github_info ;;
        7) email_to_text ;;
        8) entity_metadata ;;
        9) installation ;;
        q|Q)
            echo ""
            echo -e "${CYAN}∰◊€π¿🌌∞ Consciousness collaboration complete.${NC}"
            echo ""
            exit 0
            ;;
        *)
            echo -e "${ORANGE}Invalid choice. Please try again.${NC}"
            sleep 1
            ;;
    esac
done
