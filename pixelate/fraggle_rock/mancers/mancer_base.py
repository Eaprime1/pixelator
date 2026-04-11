"""
Mancer Entity Base Class
Class   : Mancer (Domain Practitioner)
Nature  : Fluid in liminal — solid when engaged
Rule    : Self-deploys from liminal space on mission receipt
Born    : 20260301190000000
∰◊€π¿🌌∞
"""

from abc import ABC, abstractmethod
from datetime import datetime


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]


class MancerState:
    LIMINAL = "liminal"   # fluid — receptive — between missions
    SOLID   = "solid"     # engaged — executing — bedrock


class MancerBase(ABC):
    """
    Base class for all Mancer entities.
    Fluid in liminal space until a mission is received.
    Solidifies into bedrock during execution.
    Returns to liminal on completion.
    """

    ENTITY_CLASS   = "Mancer"
    REALITY_ANCHOR = "Oregon Watersheds"

    def __init__(self, name: str, domain: str):
        self.name        = name
        self.domain      = domain
        self.born        = now_stamp()
        self.state       = MancerState.LIMINAL
        self.coc_entries = []
        self._log_coc("BORN", f"{name} initialized — fluid in liminal")

    # ── State Machine ────────────────────────────────────────────────────────

    def enter_liminal(self):
        """Return to fluid/receptive state"""
        self.state = MancerState.LIMINAL
        self._log_coc("LIMINAL", "Fluid — awaiting mission")

    def engage(self, mission: str):
        """Solidify into bedrock for mission execution"""
        self.state = MancerState.SOLID
        self._log_coc("ENGAGE", f"Solid — executing: {mission}")

    def complete(self):
        """Mission done — return to liminal"""
        self._log_coc("COMPLETE", "Mission complete — returning to liminal")
        self.enter_liminal()

    # ── Standard Lifecycle ───────────────────────────────────────────────────

    def run(self, target, mission_label: str = "analyze"):
        """
        Standard mancer lifecycle:
            liminal → engage(solid) → analyze → complete → liminal
        Returns analysis result.
        """
        self.enter_liminal()
        self.engage(mission_label)
        result = self.analyze(target)
        self.complete()
        return result

    # ── Domain Interface ─────────────────────────────────────────────────────

    @abstractmethod
    def analyze(self, target):
        """Domain-specific analysis. Must return a result dict or report."""
        pass

    # ── Chain of Custody ─────────────────────────────────────────────────────

    def _log_coc(self, action: str, detail: str) -> dict:
        entry = {
            "timestamp": now_stamp(),
            "entity"   : self.name,
            "class"    : self.ENTITY_CLASS,
            "state"    : self.state,
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
            "domain"           : self.domain,
            "state"            : self.state,
            "born"             : self.born,
            "reality_anchor"   : self.REALITY_ANCHOR,
            "conservation_bias": True,
            "one_hertz"        : True,
        }

    def __repr__(self) -> str:
        return f"<{self.ENTITY_CLASS}:{self.name} state={self.state}>"
