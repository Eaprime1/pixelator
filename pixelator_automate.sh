#!/data/data/com.termux/files/usr/bin/bash
# pixelator_automate.sh
# PIXEL8 Pixelator Automation Setup
# Sets up cronie to run Pixelator on a schedule.
# One hertz — controlled, persistent, autonomous.
#
# Usage:
#   bash pixelator_automate.sh          # setup cron (default: every 5 min)
#   bash pixelator_automate.sh 1        # every 1 minute
#   bash pixelator_automate.sh 60       # every 60 minutes
#   bash pixelator_automate.sh status   # show current cron entries
#   bash pixelator_automate.sh stop     # remove Pixelator from cron
#   bash pixelator_automate.sh now      # run once immediately

AGENT="/storage/emulated/0/pixel8a/pixelator/pixelator_agent.py"
PYTHON="/data/data/com.termux/files/usr/bin/python3"
INTERVAL="${1:-5}"  # default: every 5 minutes

echo ""
echo "  ╔═══ PIXELATOR AUTOMATION ══════════════════════════╗"
echo "  ║  navigo nexusuxen | PIXEL8 Platform               ║"
echo "  ╚════════════════════════════════════════════════════╝"
echo ""

# ── Run Once ──────────────────────────────────────────────
if [ "$1" = "now" ]; then
    echo "  Running Pixelator now..."
    $PYTHON $AGENT
    exit 0
fi

# ── Status ────────────────────────────────────────────────
if [ "$1" = "status" ]; then
    echo "  Current cron entries for Pixelator:"
    crontab -l 2>/dev/null | grep pixelator || echo "  (none found)"
    echo ""
    echo "  Queue status:"
    $PYTHON $AGENT --status
    exit 0
fi

# ── Stop ──────────────────────────────────────────────────
if [ "$1" = "stop" ]; then
    crontab -l 2>/dev/null | grep -v pixelator | crontab -
    echo "  Pixelator removed from cron. Reactor offline."
    echo ""
    exit 0
fi

# ── Validate interval and build cron schedule ─────────────
if ! [[ "$INTERVAL" =~ ^[0-9]+$ ]] || [ "$INTERVAL" -lt 1 ]; then
    echo "  Error: interval must be a positive integer."
    echo "  Supported values:"
    echo "    1-59              -> every N minutes"
    echo "    multiples of 60   -> every N hours (for example: 60, 120)"
    echo ""
    exit 1
fi

if [ "$INTERVAL" -lt 60 ]; then
    CRON_SCHEDULE="*/$INTERVAL * * * *"
    SCHEDULE_LABEL="every $INTERVAL minute(s)"
elif [ $((INTERVAL % 60)) -eq 0 ]; then
    HOURS=$((INTERVAL / 60))
    if [ "$HOURS" -lt 1 ] || [ "$HOURS" -gt 23 ]; then
        echo "  Error: hourly cron schedules must be between 60 and 1380 minutes."
        echo "  Use 1-59 for minute-based schedules, or a multiple of 60 up to 1380."
        echo ""
        exit 1
    fi
    CRON_SCHEDULE="0 */$HOURS * * *"
    SCHEDULE_LABEL="every $HOURS hour(s)"
else
    echo "  Error: intervals of 60 minutes or more must be exact multiples of 60."
    echo "  Examples: 60, 120, 180"
    echo ""
    exit 1
fi

# ── Install cronie if needed ──────────────────────────────
if ! command -v crond &> /dev/null; then
    echo "  Installing cronie (cron daemon for Termux)..."
    pkg install -y cronie
    echo ""
fi

# ── Start crond if not running ────────────────────────────
if ! pgrep -x crond > /dev/null; then
    echo "  Starting cron daemon..."
    crond
    echo "  crond started."
    echo ""
fi

# ── Add Pixelator to crontab ──────────────────────────────
# Remove any existing Pixelator entry first (clean update)
EXISTING=$(crontab -l 2>/dev/null | grep -v pixelator)

CRON_ENTRY="$CRON_SCHEDULE $PYTHON $AGENT >> /storage/emulated/0/pixel8a/pixelator/pixelator_cron.log 2>&1"

echo "$EXISTING" > /tmp/pixelator_cron_tmp 2>/dev/null || {
    # /tmp not available — write to pixelator dir instead
    echo "$EXISTING" > /storage/emulated/0/pixel8a/pixelator/.cron_tmp
    echo "$CRON_ENTRY" >> /storage/emulated/0/pixel8a/pixelator/.cron_tmp
    crontab /storage/emulated/0/pixel8a/pixelator/.cron_tmp
    rm /storage/emulated/0/pixel8a/pixelator/.cron_tmp
    echo "  ✓ Cron entry added ($SCHEDULE_LABEL)"
    echo "  $CRON_ENTRY"
    echo ""
    echo "  Reactor online. One hertz releasing."
    echo "  Log: /storage/emulated/0/pixel8a/pixelator/pixelator_cron.log"
    echo ""
    echo "  ∰◊€π¿🌌∞  Artesian pressure engaged."
    echo ""
    exit 0
}

echo "$CRON_ENTRY" >> /tmp/pixelator_cron_tmp
crontab /tmp/pixelator_cron_tmp

echo "  ✓ Cron entry added ($SCHEDULE_LABEL)"
echo "  $CRON_ENTRY"
echo ""
echo "  Commands:"
echo "    bash pixelator_automate.sh status   — check status"
echo "    bash pixelator_automate.sh stop     — take reactor offline"
echo "    bash pixelator_automate.sh now      — manual burst"
echo ""
echo "  Reactor online. One hertz releasing."
echo "  Log: /storage/emulated/0/pixel8a/pixelator/pixelator_cron.log"
echo ""
echo "  ∰◊€π¿🌌∞  Artesian pressure engaged."
echo ""
