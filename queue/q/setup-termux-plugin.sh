#!/data/data/com.termux/files/usr/bin/bash
# Termux Setup Plugin - CORRECTED VERSION
# Handles Termux environment quirks and creates proper plugin structure

set -e  # Exit on any error

# Force explicit HOME path for Termux
export HOME=/data/data/com.termux/files/home
PLUGIN_DIR="$HOME/.claude/plugins/termux-setup"

echo "🚀 Setting up Termux Setup Plugin"
echo "=================================="
echo "HOME: $HOME"
echo "Plugin location: $PLUGIN_DIR"
echo ""

# Clean up any existing plugin
if [ -d "$PLUGIN_DIR" ]; then
  echo "⚠️  Removing existing plugin directory..."
  rm -rf "$PLUGIN_DIR"
fi

# Create directory structure
echo "📁 Creating directory structure..."
mkdir -p "$PLUGIN_DIR/commands"
mkdir -p "$PLUGIN_DIR/agents"
mkdir -p "$PLUGIN_DIR/skills/termux-permissions/references"
mkdir -p "$PLUGIN_DIR/skills/git-workflow/references"
mkdir -p "$PLUGIN_DIR/skills/workspace-navigation/references"

# Create plugin.json at ROOT (not in subdirectory!)
echo "📝 Creating plugin manifest..."
cat > "$PLUGIN_DIR/plugin.json" << 'EOF'
{
  "name": "termux-setup",
  "version": "1.0.0",
  "description": "Termux-optimized workspace setup and environment validation",
  "author": "Termux User",
  "commands": {
    "setup-storage": "commands/setup-storage.md",
    "check-env": "commands/check-env.md",
    "init-git": "commands/init-git.md",
    "locate-code": "commands/locate-code.md",
    "workspace-status": "commands/workspace-status.md"
  },
  "agents": {
    "env-validator": "agents/env-validator.md"
  },
  "skills": {
    "termux-permissions": "skills/termux-permissions/SKILL.md",
    "git-workflow": "skills/git-workflow/SKILL.md",
    "workspace-navigation": "skills/workspace-navigation/SKILL.md"
  }
}
EOF

# Create a simple test command
echo "📝 Creating test command..."
cat > "$PLUGIN_DIR/commands/check-env.md" << 'EOF'
---
description: Verify Termux environment and Claude Code setup
---

# Termux Environment Check

Check the current Termux environment and verify it's properly configured for Claude Code.

## Actions

1. Display current environment variables
2. Check storage permissions
3. Verify git configuration
4. Show current working directory

## Implementation

```bash
echo "🔍 Termux Environment Check"
echo "=========================="
echo ""
echo "📍 Current Directory: $(pwd)"
echo "🏠 HOME: $HOME"
echo "👤 USER: $USER"
echo "💻 SHELL: $SHELL"
echo ""
echo "📦 Storage Access:"
if [ -d "$HOME/storage" ]; then
  echo "  ✅ Storage mounted at $HOME/storage"
  ls -la "$HOME/storage" 2>/dev/null | head -5
else
  echo "  ❌ Storage not mounted (run: termux-setup-storage)"
fi
echo ""
echo "🔧 Git Config:"
if command -v git >/dev/null 2>&1; then
  echo "  ✅ Git installed: $(git --version)"
  echo "  User: $(git config --global user.name 2>/dev/null || echo 'Not set')"
  echo "  Email: $(git config --global user.email 2>/dev/null || echo 'Not set')"
else
  echo "  ❌ Git not installed (run: pkg install git)"
fi
echo ""
echo "✨ Environment check complete!"
```
EOF

# Create README
cat > "$PLUGIN_DIR/README.md" << 'EOF'
# Termux Setup Plugin

Claude Code plugin optimized for Termux environments.

## Commands

- `/check-env` - Verify Termux environment setup

## Installation

This plugin should be auto-discovered from `~/.claude/plugins/termux-setup/`

## Testing

After creating the plugin, restart Claude Code and run:
```
/check-env
```
EOF

echo ""
echo "✅ Plugin structure created!"
echo ""
echo "📂 Verifying structure..."
ls -la "$PLUGIN_DIR/"
echo ""
if [ -f "$PLUGIN_DIR/plugin.json" ]; then
  echo "✅ plugin.json exists at root"
else
  echo "❌ plugin.json NOT at root!"
  exit 1
fi

echo ""
echo "=================================="
echo "🎉 Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "  1. RESTART Claude Code (exit current session and start new one)"
echo "  2. Test with: /check-env"
echo ""
echo "Plugin location: $PLUGIN_DIR"
echo ""
