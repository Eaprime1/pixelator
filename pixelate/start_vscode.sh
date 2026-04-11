#!/bin/bash
# start_vscode.sh
# code-server launcher with options for Termux/Pixel8a
# Usage: bash start_vscode.sh [option]
#   bash start_vscode.sh          — interactive menu
#   bash start_vscode.sh local    — localhost only, no auth
#   bash start_vscode.sh net      — network-wide (LAN access from laptop)
#   bash start_vscode.sh secure   — network-wide + HTTPS + password
#   bash start_vscode.sh stop     — kill running code-server
#   bash start_vscode.sh status   — check if running

PIXEL8A="/storage/emulated/0/pixel8a"
PORT=8080
CONFIG="$HOME/.config/code-server/config.yaml"
LOG="$HOME/.config/code-server/server.log"

# ── helpers ────────────────────────────────────────────────────────────────

find_binary() {
    for p in \
        "$HOME/.yarn/bin/code-server" \
        "$(yarn global bin 2>/dev/null)/code-server" \
        "/data/data/com.termux/files/usr/bin/code-server" \
        "$HOME/.local/bin/code-server"
    do
        [ -x "$p" ] && echo "$p" && return
    done
    # fallback: search PATH
    command -v code-server 2>/dev/null
}

is_running() {
    pgrep -f "code-server" > /dev/null 2>&1
}

get_local_ip() {
    ip route get 1 2>/dev/null | awk '{print $7; exit}' \
        || ifconfig 2>/dev/null | grep -o 'inet [0-9.]*' | grep -v '127.0.0.1' | head -1 | awk '{print $2}' \
        || echo "unknown"
}

get_password() {
    [ -f "$CONFIG" ] && grep "^password:" "$CONFIG" | awk '{print $2}'
}

show_status() {
    if is_running; then
        echo "  STATUS: RUNNING (pid: $(pgrep -f code-server | head -1))"
        LOCAL_IP=$(get_local_ip)
        echo "  Local:   http://localhost:$PORT"
        echo "  Network: http://$LOCAL_IP:$PORT"
        PWD_VAL=$(get_password)
        [ -n "$PWD_VAL" ] && echo "  Password: $PWD_VAL"
    else
        echo "  STATUS: not running"
    fi
}

stop_server() {
    if is_running; then
        pkill -f "code-server" && echo "  code-server stopped"
    else
        echo "  code-server is not running"
    fi
}

launch() {
    local MODE="$1"
    local CS_BIN
    CS_BIN=$(find_binary)

    if [ -z "$CS_BIN" ]; then
        echo ""
        echo "  ERROR: code-server not found."
        echo "  Run the installer first:"
        echo "    bash $PIXEL8A/pixelator/pixelate/install_code_server.sh"
        exit 1
    fi

    if is_running; then
        echo "  code-server is already running."
        show_status
        echo ""
        echo "  To restart: bash start_vscode.sh stop && bash start_vscode.sh"
        exit 0
    fi

    mkdir -p "$HOME/.config/code-server"
    LOCAL_IP=$(get_local_ip)

    case "$MODE" in

      local)
        echo "  Starting: localhost only, no auth"
        echo "  Folder: $PIXEL8A"
        nohup "$CS_BIN" \
            --bind-addr 127.0.0.1:$PORT \
            --auth none \
            --disable-telemetry \
            --user-data-dir "$HOME/.local/share/code-server" \
            "$PIXEL8A" \
            > "$LOG" 2>&1 &
        sleep 2
        echo ""
        echo "  Open in Chrome: http://localhost:$PORT"
        echo "  Log: $LOG"
        ;;

      net)
        echo "  Starting: network access (LAN), no auth"
        echo "  Folder: $PIXEL8A"
        nohup "$CS_BIN" \
            --bind-addr 0.0.0.0:$PORT \
            --auth none \
            --disable-telemetry \
            --user-data-dir "$HOME/.local/share/code-server" \
            "$PIXEL8A" \
            > "$LOG" 2>&1 &
        sleep 2
        echo ""
        echo "  On this phone:  http://localhost:$PORT"
        echo "  From laptop:    http://$LOCAL_IP:$PORT"
        echo "  Log: $LOG"
        ;;

      secure)
        # Requires: pkg install openssl-tool
        if ! command -v openssl > /dev/null 2>&1; then
            echo "  Installing openssl-tool..."
            pkg install openssl-tool -y
        fi
        echo "  Starting: network access + HTTPS + password auth"
        echo "  Folder: $PIXEL8A"
        nohup "$CS_BIN" \
            --bind-addr 0.0.0.0:$PORT \
            --cert \
            --disable-telemetry \
            --user-data-dir "$HOME/.local/share/code-server" \
            "$PIXEL8A" \
            > "$LOG" 2>&1 &
        sleep 2
        PWD_VAL=$(get_password)
        echo ""
        echo "  On this phone:  https://localhost:$PORT"
        echo "  From laptop:    https://$LOCAL_IP:$PORT"
        [ -n "$PWD_VAL" ] && echo "  Password: $PWD_VAL"
        echo "  Note: accept the self-signed cert warning in browser"
        echo "  HTTPS enables clipboard, better keyboard support"
        echo "  Log: $LOG"
        ;;

    esac
}

# ── option menu ────────────────────────────────────────────────────────────

interactive_menu() {
    echo ""
    echo "┌─────────────────────────────────────────┐"
    echo "│         code-server launcher             │"
    echo "│         pixel8a / Termux                 │"
    echo "└─────────────────────────────────────────┘"
    echo ""
    show_status
    echo ""
    echo "  1) local   — localhost only, no auth (fastest)"
    echo "  2) net     — LAN access, no auth (use from laptop)"
    echo "  3) secure  — LAN + HTTPS + password (clipboard works)"
    echo "  4) stop    — kill running instance"
    echo "  5) status  — show current status"
    echo "  q) quit"
    echo ""
    printf "  Choice [1]: "
    read -r CHOICE
    CHOICE="${CHOICE:-1}"

    case "$CHOICE" in
        1|local)  launch local  ;;
        2|net)    launch net    ;;
        3|secure) launch secure ;;
        4|stop)   stop_server   ;;
        5|status) show_status   ;;
        q|Q)      echo "bye"; exit 0 ;;
        *)        echo "  Unknown option"; exit 1 ;;
    esac
}

# ── entrypoint ─────────────────────────────────────────────────────────────

# Ensure PATH includes yarn bin
export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

case "${1:-}" in
    local)   launch local  ;;
    net)     launch net    ;;
    secure)  launch secure ;;
    stop)    stop_server   ;;
    status)  show_status   ;;
    "")      interactive_menu ;;
    *)
        echo "Usage: bash start_vscode.sh [local|net|secure|stop|status]"
        exit 1
        ;;
esac
