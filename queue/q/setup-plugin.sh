#!/data/data/com.termux/files/usr/bin/bash
# Termux Setup Plugin - Directory Structure Creator
# Creates the complete plugin directory structure

PLUGIN_DIR="$HOME/.claude/plugins/termux-setup"

echo "🚀 Creating Termux Setup Plugin structure..."

# Create main directories
mkdir -p "$PLUGIN_DIR/.claude-plugin"
mkdir -p "$PLUGIN_DIR/commands"
mkdir -p "$PLUGIN_DIR/agents"
mkdir -p "$PLUGIN_DIR/scripts"

# Create skill directories
mkdir -p "$PLUGIN_DIR/skills/termux-permissions/references"
mkdir -p "$PLUGIN_DIR/skills/git-workflow/references"
mkdir -p "$PLUGIN_DIR/skills/git-workflow/scripts"
mkdir -p "$PLUGIN_DIR/skills/workspace-navigation/references"

echo "✅ Directory structure created!"
echo ""
echo "📁 Plugin location: $PLUGIN_DIR"
echo ""
echo "📂 Structure:"
tree -L 3 "$PLUGIN_DIR" 2>/dev/null || ls -R "$PLUGIN_DIR"

echo ""
echo "✨ Ready for component files!"
