#!/data/data/com.termux/files/usr/bin/bash
# Plugin Validation Script
# Checks if termux-setup plugin is properly structured

PLUGIN_DIR="$HOME/.claude/plugins/termux-setup"
ERRORS=0
WARNINGS=0

echo "🔍 Validating Termux Setup Plugin"
echo "=================================="
echo ""

# Check plugin directory exists
if [ ! -d "$PLUGIN_DIR" ]; then
  echo "❌ Plugin directory not found: $PLUGIN_DIR"
  exit 1
fi

echo "📁 Plugin directory: $PLUGIN_DIR"
echo ""

# Check manifest
echo "Checking manifest..."
if [ -f "$PLUGIN_DIR/.claude-plugin/plugin.json" ]; then
  echo "  ✅ plugin.json exists"
  # Validate JSON
  if command -v python >/dev/null 2>&1; then
    python -m json.tool "$PLUGIN_DIR/.claude-plugin/plugin.json" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
      echo "  ✅ plugin.json is valid JSON"
    else
      echo "  ❌ plugin.json has invalid JSON"
      ((ERRORS++))
    fi
  fi
else
  echo "  ❌ plugin.json missing"
  ((ERRORS++))
fi
echo ""

# Check commands
echo "Checking commands..."
COMMANDS=("setup-storage" "check-env" "init-git" "locate-code" "workspace-status")
for cmd in "${COMMANDS[@]}"; do
  if [ -f "$PLUGIN_DIR/commands/$cmd.md" ]; then
    echo "  ✅ $cmd.md exists"
    # Check for frontmatter
    if head -1 "$PLUGIN_DIR/commands/$cmd.md" | grep -q "^---$"; then
      echo "     ✅ Has YAML frontmatter"
    else
      echo "     ⚠️  Missing YAML frontmatter"
      ((WARNINGS++))
    fi
  else
    echo "  ❌ $cmd.md missing"
    ((ERRORS++))
  fi
done
echo ""

# Check skills
echo "Checking skills..."
SKILLS=("termux-permissions" "git-workflow" "workspace-navigation")
for skill in "${SKILLS[@]}"; do
  if [ -f "$PLUGIN_DIR/skills/$skill/SKILL.md" ]; then
    echo "  ✅ $skill/SKILL.md exists"
    # Check for frontmatter
    if head -1 "$PLUGIN_DIR/skills/$skill/SKILL.md" | grep -q "^---$"; then
      echo "     ✅ Has YAML frontmatter"
    else
      echo "     ⚠️  Missing YAML frontmatter"
      ((WARNINGS++))
    fi
  else
    echo "  ❌ $skill/SKILL.md missing"
    ((ERRORS++))
  fi
done
echo ""

# Check agents
echo "Checking agents..."
if [ -f "$PLUGIN_DIR/agents/env-validator.md" ]; then
  echo "  ✅ env-validator.md exists"
  # Check for frontmatter
  if head -1 "$PLUGIN_DIR/agents/env-validator.md" | grep -q "^---$"; then
    echo "     ✅ Has YAML frontmatter"
  else
    echo "     ⚠️  Missing YAML frontmatter"
    ((WARNINGS++))
  fi
else
  echo "  ❌ env-validator.md missing"
  ((ERRORS++))
fi
echo ""

# Check README
echo "Checking documentation..."
if [ -f "$PLUGIN_DIR/README.md" ]; then
  echo "  ✅ README.md exists"
else
  echo "  ⚠️  README.md missing"
  ((WARNINGS++))
fi
echo ""

# Summary
echo "=================================="
echo "Validation Summary"
echo "=================================="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
  echo "✅ All checks passed!"
  echo ""
  echo "Plugin is ready to use!"
  echo ""
  echo "Next steps:"
  echo "  1. Reload Claude Code: cc --plugin-dir ~/.claude/plugins/termux-setup"
  echo "  2. Test commands: /setup-storage --verify-only"
  echo "  3. Check help: cc --help | grep termux"
  exit 0
elif [ $ERRORS -eq 0 ]; then
  echo "⚠️  Validation passed with $WARNINGS warnings"
  echo ""
  echo "Plugin should work but has minor issues to address."
  exit 0
else
  echo "❌ Validation failed with $ERRORS errors and $WARNINGS warnings"
  echo ""
  echo "Please fix errors before using the plugin."
  exit 1
fi
