#!/data/data/com.termux/files/usr/bin/bash
# Add helpful aliases for plugin development

BASHRC="$HOME/.bashrc"

echo "Adding termux-setup aliases to $BASHRC..."

# Backup .bashrc
cp "$BASHRC" "$BASHRC.backup.$(date +%Y%m%d-%H%M%S)"

# Add aliases
cat >> "$BASHRC" << 'EOF'

# Termux Setup Plugin aliases
alias plugin-dir='cd ~/.claude/plugins/termux-setup'
alias plugin-reload='cc --plugin-dir ~/.claude/plugins/termux-setup'
alias plugin-edit='cd ~/.claude/plugins/termux-setup && ls -la'

EOF

echo "✅ Aliases added to $BASHRC"
echo ""
echo "Available aliases:"
echo "  plugin-dir     - Navigate to plugin directory"
echo "  plugin-reload  - Reload Claude Code with plugin"
echo "  plugin-edit    - Go to plugin and show structure"
echo ""
echo "Run: source ~/.bashrc  (to activate now)"
