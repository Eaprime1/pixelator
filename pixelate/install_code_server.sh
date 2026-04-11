#!/bin/bash
# install_code_server.sh
# Installs code-server (VS Code in browser) on Termux/Android
# Based on ppoffice gist + 2023-2025 community fixes
# Usage: bash install_code_server.sh
# Then visit: http://localhost:8080

set -e

echo "=== code-server installer for Termux ==="
echo ""

# Step 1: Update packages
echo "[1/6] Updating packages..."
pkg update -y

# Step 2: Install dependencies
# nodejs-lts = Node 18, which code-server expects
# binutils needed for native compilation
echo "[2/6] Installing dependencies..."
pkg install -y python nodejs-lts yarn git binutils ripgrep

# Step 3: Install code-server
# FORCE_NODE_VERSION=FALSE bypasses the Node version check
# --ignore-engines lets yarn proceed despite version mismatch
echo "[3/6] Installing code-server (this takes a while ~3-5 min)..."
FORCE_NODE_VERSION=FALSE yarn global add code-server --ignore-engines

# Step 4: Fix spdlog Android compilation issue
# code-server's spdlog dep needs -latomic to compile on Android
SPDLOG_DIR="$HOME/.config/yarn/global/node_modules/code-server/lib/vscode/node_modules/spdlog"

if [ -d "$SPDLOG_DIR" ]; then
    echo "[4/6] Fixing spdlog for Android..."
    cd "$SPDLOG_DIR"
    # Use Python to patch binding.gyp (no vim needed)
    python3 - <<'PYEOF'
import json, sys

with open("binding.gyp", "r") as f:
    content = f.read()

# Check if already patched
if '"-latomic"' in content:
    print("  spdlog already patched, skipping")
    sys.exit(0)

# Insert -latomic after "target_name": "spdlog",
patched = content.replace(
    '"target_name": "spdlog",',
    '"target_name": "spdlog",\n        "libraries": [ "-latomic" ],'
)

if patched == content:
    print("  WARNING: Could not find patch location in binding.gyp")
    sys.exit(0)

with open("binding.gyp", "w") as f:
    f.write(patched)

print("  binding.gyp patched successfully")
PYEOF

    # Recompile spdlog
    echo "  Recompiling spdlog..."
    npm install 2>&1 | tail -5
else
    echo "[4/6] spdlog dir not found, skipping fix (may not be needed in this version)"
fi

# Step 5: Fix file search (ripgrep symlink)
RG_VSCODE_DIR="$HOME/.config/yarn/global/node_modules/code-server/lib/vscode/node_modules/@vscode/ripgrep/bin"
if [ -d "$RG_VSCODE_DIR" ]; then
    echo "[5/6] Linking ripgrep for file search..."
    cd "$RG_VSCODE_DIR"
    if [ ! -f "rg" ]; then
        ln -s $(which rg) .
        echo "  ripgrep linked"
    else
        echo "  ripgrep already linked"
    fi
else
    echo "[5/6] Linking ripgrep (alternate path)..."
    ALT_RG_DIR="$HOME/.config/yarn/global/node_modules/code-server/lib/vscode/node_modules/vscode-ripgrep/bin"
    if [ -d "$ALT_RG_DIR" ]; then
        cd "$ALT_RG_DIR"
        [ ! -f "rg" ] && ln -s $(which rg) . && echo "  ripgrep linked"
    else
        echo "  ripgrep dir not found, file search may not work (non-critical)"
    fi
fi

# Step 6: Fix PATH so code-server binary is found
echo "[6/6] Checking PATH..."
CODE_SERVER_BIN="$HOME/.yarn/bin/code-server"
if [ ! -f "$CODE_SERVER_BIN" ]; then
    # Try npm global path
    CODE_SERVER_BIN="$(yarn global bin)/code-server"
fi

BASHRC="$HOME/.bashrc"
if ! grep -q "yarn/bin" "$BASHRC" 2>/dev/null; then
    echo 'export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"' >> "$BASHRC"
    echo "  Added yarn bin to PATH in .bashrc"
fi

echo ""
echo "=== Installation complete! ==="
echo ""
echo "To start code-server:"
echo "  source ~/.bashrc"
echo "  code-server --auth none --disable-telemetry"
echo ""
echo "Then open in phone browser: http://localhost:8080"
echo ""
echo "To start with network access (access from laptop on same WiFi):"
echo "  code-server --bind-addr 0.0.0.0:8080 --auth none --disable-telemetry"
echo ""
echo "To add a handy alias, add this to ~/.bashrc:"
echo "  alias vsc='code-server --auth none --disable-telemetry'"
echo ""
echo "NOTE: The terminal inside VS Code may not work (known Termux issue)."
echo "Use the Termux app itself as your terminal alongside VS Code in browser."
