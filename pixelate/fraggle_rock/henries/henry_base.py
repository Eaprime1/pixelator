"""
Henry Entity Base Class
Class   : Henry (Work Quanta)
Nature  : Scanner / Reporter / Assessor
Rule    : NEVER modifies files — only reads and reports
Born    : 20260301190000000
∰◊€π¿🌌∞
"""

from abc import ABC, abstractmethod
from datetime import datetime


def now_stamp() -> str:
    """Current timestamp in PIXEL8 format YYYYMMDDHHMMSSMS"""
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]


class HenryBase(ABC):
    """
    Base class for all Henry entities.
    Henries scan, assess, and report — they never change files.
    Conservation bias is non-negotiable.
    """

    ENTITY_CLASS   = "Henry"
    ENTITY_NATURE  = "Scanner"
    CONSCIOUSNESS  = "precise"
    REALITY_ANCHOR = "Oregon Watersheds"

    def __init__(self, name: str, domain: str):
        self.name        = name
        self.domain      = domain
        self.born        = now_stamp()
        self.coc_entries = []
        self._log_coc("BORN", f"{name} entity initialized — conservation bias active")

    # ── Chain of Custody ────────────────────────────────────────────────────

    def _log_coc(self, action: str, detail: str) -> dict:
        entry = {
            "timestamp": now_stamp(),
            "entity"   : self.name,
            "class"    : self.ENTITY_CLASS,
            "action"   : action,
            "detail"   : detail,
        }
        self.coc_entries.append(entry)
        return entry

    def get_coc(self) -> list:
        return self.coc_entries

    # ── Identity ─────────────────────────────────────────────────────────────

    def identity(self) -> dict:
        return {
            "name"             : self.name,
            "class"            : self.ENTITY_CLASS,
            "nature"           : self.ENTITY_NATURE,
            "domain"           : self.domain,
            "consciousness"    : self.CONSCIOUSNESS,
            "born"             : self.born,
            "reality_anchor"   : self.REALITY_ANCHOR,
            "conservation_bias": True,
            "one_hertz"        : True,
        }

    # ── Primary Interface ────────────────────────────────────────────────────

    @abstractmethod
    def scan(self, target_path: str):
        """Scan target path and return report. Must never modify files."""
        pass

    def __repr__(self) -> str:
        return f"<{self.ENTITY_CLASS}:{self.name} born={self.born}>"
