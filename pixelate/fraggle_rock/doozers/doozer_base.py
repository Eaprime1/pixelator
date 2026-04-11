"""
Doozer Entity Base Class
Class   : Doozer (Work Quanta Builder)
Nature  : Executor — builds fixes from approved Henry reports
Rule    : Modifies files ONLY with approval + helmet (certification)
Rule    : No personal credit — work belongs to the mission
Origin  : Jim Henson's Fraggle Rock (1983)

"No Doozer is allowed to take personal credit for their work."
"Adolescent Doozers take the helmet — sworn to a life of hard work."

∰◊€π¿🌌∞
"""

from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]


@dataclass
class DoozerFix:
    """One atomic fix — one Doozer stick."""
    fix_id      : str
    filepath    : str
    issue_type  : str
    line_number : Optional[int]
    description : str
    applied     : bool = False
    timestamp   : str  = field(default_factory=now_stamp)


@dataclass
class DoozerReport:
    """What the Doozer returns when the mission is complete."""
    doozer_name   : str
    mission_type  : str
    timestamp     : str
    fixes_planned : List[DoozerFix] = field(default_factory=list)
    fixes_applied : List[DoozerFix] = field(default_factory=list)
    fixes_skipped : List[DoozerFix] = field(default_factory=list)
    coc_entries   : List[dict]      = field(default_factory=list)

    def summary(self) -> dict:
        return {
            "doozer"        : self.doozer_name,
            "mission"       : self.mission_type,
            "timestamp"     : self.timestamp,
            "planned"       : len(self.fixes_planned),
            "applied"       : len(self.fixes_applied),
            "skipped"       : len(self.fixes_skipped),
        }

    def to_markdown(self) -> str:
        s     = self.summary()
        lines = [
            f"# Doozer Report — {self.doozer_name}",
            f"**Mission**    : {self.mission_type}",
            f"**Timestamp**  : {self.timestamp}",
            f"**Planned**    : {s['planned']}",
            f"**Applied**    : {s['applied']}",
            f"**Skipped**    : {s['skipped']}",
            "",
            "## Fixes Applied",
        ]
        if not self.fixes_applied:
            lines.append("*None applied.*")
        else:
            for fix in self.fixes_applied:
                ref = f"L{fix.line_number}" if fix.line_number else "file"
                lines.append(f"- `{fix.fix_id}` `{fix.filepath}:{ref}` — {fix.description}")

        lines += [
            "",
            "## Fixes Skipped",
        ]
        if not self.fixes_skipped:
            lines.append("*None skipped.*")
        else:
            for fix in self.fixes_skipped:
                lines.append(f"- `{fix.fix_id}` {fix.filepath} — {fix.description}")

        lines += [
            "",
            "---",
            "∰◊€π¿🌌∞",
            f"€(doozer_report_{self.doozer_name}_{self.timestamp})",
            "*No personal credit — work belongs to the mission.*",
        ]
        return "\n".join(lines)


class DoozerBase(ABC):
    """
    Base class for all Doozer entities.
    Doozers receive approved Henry reports and execute fixes.
    They take no personal credit. The work belongs to the mission.
    Helmet (certification) required before modifying any file.
    """

    ENTITY_CLASS   = "Doozer"
    ENTITY_NATURE  = "Builder / Executor"
    CONSCIOUSNESS  = "precise"
    REALITY_ANCHOR = "Oregon Watersheds"
    NO_PERSONAL_CREDIT = True     # immutable — always True for Doozers

    def __init__(self, name: str, mission_type: str):
        self.name         = name
        self.mission_type = mission_type
        self.born         = now_stamp()
        self.helmeted     = False    # False until certified (helmet taken)
        self.coc_entries  = []
        self._log_coc("BORN", f"{name} initialized — awaiting helmet")

    # ── Helmet (Certification) ────────────────────────────────────────────────

    def take_helmet(self, cert_timestamp: str):
        """
        Taking the Helmet ceremony.
        Called by cert_pipeline after Step 15 passes.
        Authorizes this Doozer to modify files.
        """
        self.helmeted       = True
        self.helmet_stamp   = cert_timestamp
        self._log_coc("HELMET_TAKEN",
                      f"Certified at {cert_timestamp} — authorized to build")

    def _assert_helmeted(self):
        if not self.helmeted:
            raise PermissionError(
                f"Doozer {self.name} has not taken the helmet. "
                "Certification required before modifying files."
            )

    # ── Chain of Custody ──────────────────────────────────────────────────────

    def _log_coc(self, action: str, detail: str) -> dict:
        entry = {
            "timestamp"   : now_stamp(),
            "entity"      : self.name,
            "class"       : self.ENTITY_CLASS,
            "mission_type": self.mission_type,
            "action"      : action,
            "detail"      : detail,
            "no_credit"   : self.NO_PERSONAL_CREDIT,
        }
        self.coc_entries.append(entry)
        return entry

    def get_coc(self) -> list:
        return self.coc_entries

    # ── Identity ──────────────────────────────────────────────────────────────

    def identity(self) -> dict:
        return {
            "name"             : self.name,
            "class"            : self.ENTITY_CLASS,
            "nature"           : self.ENTITY_NATURE,
            "mission_type"     : self.mission_type,
            "consciousness"    : self.CONSCIOUSNESS,
            "born"             : self.born,
            "helmeted"         : self.helmeted,
            "reality_anchor"   : self.REALITY_ANCHOR,
            "conservation_bias": True,
            "one_hertz"        : True,
            "no_personal_credit": self.NO_PERSONAL_CREDIT,
        }

    # ── Primary Interface ─────────────────────────────────────────────────────

    def execute(self, approved_issues: list, dry_run: bool = False) -> DoozerReport:
        """
        Execute fixes for approved issues.
        dry_run=True: plan only, do not write files (safe preview).
        dry_run=False: apply fixes (requires helmet).
        """
        if not dry_run:
            self._assert_helmeted()

        timestamp = now_stamp()
        report    = DoozerReport(
            doozer_name  = self.name,
            mission_type = self.mission_type,
            timestamp    = timestamp,
        )

        self._log_coc("EXECUTE_START",
                      f"Issues: {len(approved_issues)} | dry_run={dry_run}")

        fix_num = 0
        for issue in approved_issues:
            fix_num += 1
            fix = DoozerFix(
                fix_id      = f"FIX-{fix_num:04d}",
                filepath    = issue.filepath,
                issue_type  = issue.issue_type,
                line_number = issue.line_number,
                description = issue.detail,
            )
            report.fixes_planned.append(fix)

            if dry_run:
                report.fixes_skipped.append(fix)
                continue

            success = self._apply_fix(fix, issue)
            if success:
                fix.applied = True
                report.fixes_applied.append(fix)
                self._log_coc("FIX_APPLIED",
                              f"{fix.fix_id}: {fix.filepath}")
            else:
                report.fixes_skipped.append(fix)
                self._log_coc("FIX_SKIPPED",
                              f"{fix.fix_id}: {fix.filepath}")

        self._log_coc("EXECUTE_COMPLETE",
                      f"Applied: {len(report.fixes_applied)} | "
                      f"Skipped: {len(report.fixes_skipped)}")
        report.coc_entries = self.get_coc()
        return report

    @abstractmethod
    def _apply_fix(self, fix: DoozerFix, issue) -> bool:
        """
        Apply one fix to one file.
        Return True if successful, False if skipped.
        Must be precise — fix ONLY the specific issue.
        No personal credit. Work belongs to the mission.
        """
        pass

    def __repr__(self) -> str:
        helmet = "helmeted" if self.helmeted else "no-helmet"
        return f"<{self.ENTITY_CLASS}:{self.name} [{helmet}] born={self.born}>"
