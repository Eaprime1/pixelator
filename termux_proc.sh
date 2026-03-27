#!/data/data/com.termux/files/usr/bin/bash
# termux_proc.sh — Procedure tracker for Pixel 8a / Termux
# Generates short verification certificates — safe to copy-paste back to Claude

STORE="$HOME/.pixelator"
LOG="$STORE/proc_log.txt"
CERT_FILE="$STORE/last_cert.txt"

mkdir -p "$STORE"

# ── helpers ──────────────────────────────────────────────────────────────────

ts()   { date '+%Y%m%d-%H%M%S'; }
short(){ echo "$1" | sha256sum | cut -c1-8; }

cert() {
    local label="$1"
    local stamp
    stamp=$(ts)
    local hash
    hash=$(short "${label}-${stamp}")
    local cert="CERT|${label}|${stamp}|${hash}"
    echo "$cert" | tee "$CERT_FILE"
    echo "---"
    echo "Paste the line above to Claude as verification."
}

log_entry() {
    echo "$(ts) | $*" >> "$LOG"
}

# ── main menu ─────────────────────────────────────────────────────────────────

show_menu() {
    echo ""
    echo "=== PIXELATOR PROC TRACKER ==="
    echo "1) Start / resume a procedure"
    echo "2) Complete a step  (generates cert)"
    echo "3) Show last cert"
    echo "4) View log"
    echo "5) Save a note"
    echo "6) Quit"
    echo "=============================="
    printf "Choice: "
}

do_start() {
    printf "Procedure name: "
    read -r name
    log_entry "START [$name]"
    echo "Started: $name"
    cert "START-${name// /_}"
}

do_step() {
    printf "Procedure name: "
    read -r name
    printf "Step number/description: "
    read -r step
    log_entry "STEP [$name] $step"
    cert "STEP-${name// /_}-${step// /_}"
}

do_last_cert() {
    if [[ -f "$CERT_FILE" ]]; then
        echo "--- Last cert ---"
        cat "$CERT_FILE"
        echo "---"
    else
        echo "No cert yet."
    fi
}

do_view_log() {
    if [[ -f "$LOG" ]]; then
        echo "--- Recent log (last 20) ---"
        tail -20 "$LOG"
        echo "---"
    else
        echo "Log is empty."
    fi
}

do_note() {
    printf "Note: "
    read -r note
    log_entry "NOTE: $note"
    echo "Saved."
    cert "NOTE-${note:0:20}"
}

# ── run ───────────────────────────────────────────────────────────────────────

while true; do
    show_menu
    read -r choice
    case "$choice" in
        1) do_start ;;
        2) do_step ;;
        3) do_last_cert ;;
        4) do_view_log ;;
        5) do_note ;;
        6) echo "Bye."; break ;;
        *) echo "Invalid choice." ;;
    esac
done
