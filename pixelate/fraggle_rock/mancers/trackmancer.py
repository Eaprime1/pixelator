"""
trackmancer — Chain of Custody Tracking Mancer
Domain  : CoC ledger management
State   : Fluid in liminal — solid while reading/writing ledger

Reads, writes, and queries the fraggle_ledger.json.
The memory of all missions.

Usage:
    python3 trackmancer.py /path/to/fraggle_ledger.json
"""

import os
import sys
import json

from mancer_base import MancerBase, now_stamp


class TrackMancer(MancerBase):
    """
    trackmancer — manages the Chain of Custody ledger.
    Every mission entry, status update, and audit trail lives here.
    """

    def __init__(self, ledger_path: str):
        super().__init__(name="trackmancer", domain="chain_of_custody")
        self.ledger_path = ledger_path
        self.ledger      = self._load_ledger()

    # ── Ledger I/O ───────────────────────────────────────────────────────────

    def _load_ledger(self) -> dict:
        if os.path.exists(self.ledger_path):
            try:
                with open(self.ledger_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {
            "ledger_id": "fraggle_github_hygiene",
            "created"  : now_stamp(),
            "entries"  : [],
        }

    def _save_ledger(self):
        os.makedirs(os.path.dirname(os.path.abspath(self.ledger_path)), exist_ok=True)
        with open(self.ledger_path, "w") as f:
            json.dump(self.ledger, f, indent=2)

    # ── Ledger Operations ────────────────────────────────────────────────────

    def add_entry(self, entity: str, action: str, detail: str,
                  status: str = "ACTIVE", **kwargs) -> str:
        """Add CoC entry. Returns coc_id."""
        coc_id = f"COC-{len(self.ledger['entries'])+1:04d}"
        entry  = {
            "coc_id"   : coc_id,
            "timestamp": now_stamp(),
            "entity"   : entity,
            "action"   : action,
            "detail"   : detail,
            "status"   : status,
            **kwargs,
        }
        self.ledger["entries"].append(entry)
        self._save_ledger()
        self._log_coc("ENTRY_ADDED", f"{coc_id}: {entity} {action}")
        return coc_id

    def update_status(self, coc_id: str, status: str) -> bool:
        """Update the status of an existing entry. Returns True if found."""
        for entry in self.ledger["entries"]:
            if entry["coc_id"] == coc_id:
                entry["status"]  = status
                entry["updated"] = now_stamp()
                self._save_ledger()
                self._log_coc("STATUS_UPDATE", f"{coc_id} → {status}")
                return True
        return False

    def query(self, status: str = None, entity: str = None) -> list:
        """Query entries by status and/or entity name."""
        results = self.ledger["entries"]
        if status:
            results = [e for e in results if e.get("status") == status]
        if entity:
            results = [e for e in results if e.get("entity") == entity]
        return results

    # ── Mancer Interface ─────────────────────────────────────────────────────

    def analyze(self, target=None) -> dict:
        """Return ledger summary"""
        entries    = self.ledger.get("entries", [])
        by_status  = {}
        for e in entries:
            s = e.get("status", "UNKNOWN")
            by_status[s] = by_status.get(s, 0) + 1
        return {
            "ledger_id"    : self.ledger.get("ledger_id"),
            "total_entries": len(entries),
            "by_status"    : by_status,
            "last_entry"   : entries[-1] if entries else None,
        }

    def report(self) -> str:
        """Generate readable markdown ledger report"""
        summary = self.analyze()
        lines   = [
            "# TrackMancer — CoC Ledger Report",
            f"**Ledger**        : {summary['ledger_id']}",
            f"**Total Entries** : {summary['total_entries']}",
            f"**By Status**     : {summary['by_status']}",
            "",
            "## Entries",
        ]
        for e in self.ledger.get("entries", []):
            lines.append(
                f"- `{e['coc_id']}` | {e['timestamp']} | "
                f"**{e['entity']}** | {e['action']} | `{e['status']}`"
            )
            if e.get("detail"):
                lines.append(f"  ↳ {e['detail']}")
        lines += [
            "",
            "---",
            "∰◊€π¿🌌∞",
            f"€(trackmancer_report_{now_stamp()})",
            "*Status: LEDGER_REPORTED*",
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    ledger_path = sys.argv[1] if len(sys.argv) > 1 else "fraggle_rock/fraggle_ledger.json"
    mancer = TrackMancer(ledger_path)
    mancer.run(mission_label="ledger_report")
    print(mancer.report())
