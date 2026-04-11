#!/bin/bash
#
# ListMancer Shell Integration
# Add to .bashrc or .zshrc: source /path/to/listmancer.sh
#
# This creates the symbol-based commands that invoke the Python mancer
#

# Find the directory where this script lives
LISTMANCER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LISTMANCER_PY="${LISTMANCER_DIR}/listmancer.py"

# Make sure Python script is executable
chmod +x "${LISTMANCER_PY}" 2>/dev/null

# Play mode - gentle guided exploration
alias '~ls~'="python3 '${LISTMANCER_PY}' '~ls~'"

# Reader mode - understand what you see
alias '-ls~'="python3 '${LISTMANCER_PY}' '-ls~'"

# Builder mode - learn to construct
alias '^ls+'="python3 '${LISTMANCER_PY}' '^ls+'"

# Main mancer command for other operations
listmancer() {
    python3 "${LISTMANCER_PY}" "$@"
}

# Helper to show available modes
lsmancer() {
    cat << 'EOF'

╔══════════════════════════════════════════════════════╗
║              ListMancer Command Gateway              ║
╠══════════════════════════════════════════════════════╣
║                                                      ║
║  Available Commands:                                 ║
║                                                      ║
║    ~ls~   🌊 Play Mode                              ║
║           Gentle guided exploration                  ║
║           Perfect for learning and discovery         ║
║                                                      ║
║    -ls~   📖 Reader Mode                            ║
║           Understand what you're seeing              ║
║           Explains symbols and patterns              ║
║                                                      ║
║    ^ls+   🏗️  Builder Mode                          ║
║           Learn to construct commands                ║
║           Educational and empowering                 ║
║                                                      ║
║  Statistics:                                         ║
║    listmancer --stats                                ║
║                                                      ║
║  Philosophy:                                         ║
║    Commands MUST be commanded (that's their nature)  ║
║    Humans need exploration space (that's OUR nature) ║
║    The mancer creates liminal possibility between    ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

EOF
}

# Quick access to stats
lsstats() {
    listmancer --stats
}

# Export functions so they're available in subshells
export -f listmancer
export -f lsmancer
export -f lsstats

# Friendly reminder on first load
if [[ -z "${LISTMANCER_LOADED}" ]]; then
    echo "✨ ListMancer loaded! Try: ~ls~ or -ls~ or ^ls+"
    echo "   (Type 'lsmancer' for help)"
    export LISTMANCER_LOADED=1
fi
