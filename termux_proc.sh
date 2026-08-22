#!/data/data/com.termux/files/usr/bin/bash
# termux_proc.sh — Procedure tracker for Pixel 8a / Termux
# Generates short verification certificates — safe to copy-paste back to Claude

STORE="$HOME/.pixelator"
LOG="$STORE/proc_log.txt"
CERT_FILE="$STORE/last_cert.txt"

mkdir -p "$STORE"

# ── helpers ──────────────────────────────────────────────────────────────────

ts()   { date '+%Y%m%d-%H%M%S'; }
ts_readable() { date '+%Y-%m-%d %H:%M:%S %Z'; }
short(){ echo "$1" | sha256sum | cut -c1-8; }
# Roll-to-icon mapping: 1-6 use die faces, 7-12 use dice-adjacent symbols.
ROLL_ICONS=(⚀ ⚁ ⚂ ⚃ ⚄ ⚅ 🎲 🧊 🔷 🔶 ⭐ ✨)

roll_d12() {
    if command -v shuf >/dev/null 2>&1; then
        shuf -i 1-12 -n 1
    else
        echo $((RANDOM % 12 + 1))
    fi
}

dice_icon_for_roll() {
    local roll="$1"
    if ! [[ "$roll" =~ ^[0-9]+$ ]]; then
        echo "🎲"
        return
    fi
    if [[ "$roll" -lt 1 || "$roll" -gt 12 ]]; then
        echo "🎲"
        return
    fi
    echo "${ROLL_ICONS[$((roll - 1))]}"
}

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
    echo "6) Roll D12 insight (timestamp + icon)"
    echo "7) Quit"
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

do_d12_insight() {
    local roll
    roll=$(roll_d12)
    local icon
    icon=$(dice_icon_for_roll "$roll")
    local stamp
    stamp=$(ts_readable)
    local insight
    case "$roll" in
        1) insight="Start small and keep momentum." ;;
        2) insight="Pair up tasks to reduce friction." ;;
        3) insight="Trim one unnecessary step right now." ;;
        4) insight="Stabilize before you optimize." ;;
        5) insight="Document while context is fresh." ;;
        6) insight="Test the riskiest path first." ;;
        7) insight="Ship a small visible improvement." ;;
        8) insight="Refactor one repeated pattern." ;;
        9) insight="Validate assumptions with a quick check." ;;
        10) insight="Choose clarity over cleverness." ;;
        11) insight="Close one open loop before adding more." ;;
        12) insight="Review results and lock in the win." ;;
    esac
    echo "${stamp} | D12=${roll} ${icon} | ${insight}"
    log_entry "INSIGHT [${stamp}] D12=${roll} ${icon} ${insight}"
    cert "INSIGHT-D12-${roll}"
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
        6) do_d12_insight ;;
        7) echo "Bye."; break ;;
        *) echo "Invalid choice." ;;
    esac
done
