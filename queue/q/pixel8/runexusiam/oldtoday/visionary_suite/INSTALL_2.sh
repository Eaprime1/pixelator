#!/bin/bash
# ListMancer Quick Install Script
# Run with: bash INSTALL.sh

echo "🌊 ListMancer Installation"
echo "=========================="
echo ""

# Get the directory where this script is located
INSTALL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "📁 Installation directory: $INSTALL_DIR"
echo ""

# Make Python script executable
chmod +x "$INSTALL_DIR/listmancer.py"
echo "✓ Made listmancer.py executable"

# Detect shell
if [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
    SHELL_NAME="bash"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
    SHELL_NAME="zsh"
else
    echo "⚠️  Could not detect bash or zsh"
    echo "   Please manually add this line to your shell RC file:"
    echo "   source $INSTALL_DIR/listmancer.sh"
    exit 1
fi

echo "✓ Detected $SHELL_NAME shell"
echo ""

# Check if already installed
if grep -q "listmancer.sh" "$SHELL_RC"; then
    echo "⚠️  ListMancer already in $SHELL_RC"
    echo "   Skipping duplicate entry"
else
    echo "# ListMancer - Command entity gateway" >> "$SHELL_RC"
    echo "source \"$INSTALL_DIR/listmancer.sh\"" >> "$SHELL_RC"
    echo "✓ Added to $SHELL_RC"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "To activate in current session:"
echo "  source $SHELL_RC"
echo ""
echo "Or start a new terminal."
echo ""
echo "Then try:"
echo "  ~ls~   # Gentle exploration mode"
echo "  -ls~   # Reader/understanding mode"
echo "  ^ls+   # Builder/learning mode"
echo ""
echo "Type 'lsmancer' for help anytime!"
echo ""
echo "✨ Happy commanding!"
