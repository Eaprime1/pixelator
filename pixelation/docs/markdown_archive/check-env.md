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
