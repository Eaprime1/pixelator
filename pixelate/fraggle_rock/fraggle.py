"""
Fraggle — Mission Launcher and Carrier
Class   : Fraggle (Mancer subclass — liminal/solid state machine)
Role    : Receives Henry's report → selects Doozers → launches missions
          → collects results → returns to liminal
Nature  : Fluid until needed; solid during dispatch; carries Doozers outward

"Fraggles eat Doozer buildings. This is not destruction — it is the cycle."
(Jim Henson's Fraggle Rock, 1983)

The Fraggle Rock ecosystem:
  Henry scans      → radish dust (raw material: issues found)
  Fraggle receives → selects the right Doozer for each issue class
  Doozer executes  → doozer sticks (atomic fixes)
  Henry verifies   → Fraggles eat the building (verification = consumption)

Fraggle does NOT execute fixes. Fraggle carries and coordinates.
The Doozer executes. Fraggle ensures the right Doozer goes on the right mission.

∰◊€π¿🌌∞
"""

import os
import sys
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional

FRAGGLE_DIR = os.path.dirname(os.path.abspath(__file__))
MANCERS_DIR = os.path.join(FRAGGLE_DIR, "mancers")
DOOZERS_DIR = os.path.join(FRAGGLE_DIR, "doozers")

sys.path.insert(0, MANCERS_DIR)
sys.path.insert(0, DOOZERS_DIR)

from mancer_base import MancerBase, MancerState, now_stamp


# ── Data Structures ─────────────────────────────────────────────────────────────

@dataclass
class FraggleLaunch:
    """One Doozer launch event — one mission dispatch."""
    launch_id     : str
    doozer_name   : str
    mission_type  : str
    issue_count   : int
    timestamp     : str
    result        : Optional[dict] = None
    success       : bool           = False


@dataclass
class FraggleResult:
    """
    The full result of one Fraggle mission cycle.
    Contains all Doozer launches and their outcomes.
    """
    fraggle_name  : str
    henry_report  : object          # the original HenryReport
    timestamp     : str
    launches      : List[FraggleLaunch]  = field(default_factory=list)
    coc_entries   : List[dict]           = field(default_factory=list)

    def summary(self) -> dict:
        return {
            "fraggle"         : self.fraggle_name,
            "timestamp"       : self.timestamp,
            "launches"        : len(self.launches),
            "successful"      : sum(1 for l in self.launches if l.success),
            "failed"          : sum(1 for l in self.launches if not l.success),
            "total_issues"    : sum(l.issue_count for l in self.launches),
        }

    def to_markdown(self) -> str:
        s     = self.summary()
        lines = [
            f"# Fraggle Mission Report — {self.fraggle_name}",
            f"**Timestamp** : {self.timestamp}",
            f"**Launches**  : {s['launches']}",
            f"**Successful**: {s['successful']}",
            f"**Failed**    : {s['failed']}",
            f"**Total issues dispatched**: {s['total_issues']}",
            "",
            "## Doozer Launches",
        ]
        for launch in self.launches:
            icon = "✓" if launch.success else "✗"
            lines.append(
                f"- {icon} `{launch.launch_id}` "
                f"**{launch.doozer_name}** ({launch.mission_type}) "
                f"— {launch.issue_count} issues"
            )
        lines += [
            "",
            "---",
            "∰◊€π¿🌌∞",
            f"€(fraggle_mission_{self.fraggle_name}_{self.timestamp})",
            "*The Fraggle carries. The Doozer builds. Henry verifies.*",
        ]
        return "\n".join(lines)


# ── Fraggle — The Carrier ───────────────────────────────────────────────────────

class Fraggle(MancerBase):
    """
    The Fraggle — mission launcher and carrier.

    Lives in liminal space between missions (fluid/receptive).
    When a Henry report arrives, Fraggle solidifies:
      1. Groups Henry's issues by type (issue_type → Doozer mapping)
      2. For each type: selects a helmeted Doozer from registry
      3. Launches the Doozer with the approved issues
      4. Collects the Doozer report
      5. Returns to liminal

    Fraggle does not fix. Fraggle carries, coordinates, records.
    """

    ENTITY_CLASS   = "Fraggle"
    ENTITY_NATURE  = "Carrier / Launcher / Coordinator"
    CONSCIOUSNESS  = "liminal"     # Fraggle's natural state
    REALITY_ANCHOR = "Oregon Watersheds"

    def __init__(self, name: str = "fraggle"):
        super().__init__(name, domain="mission_dispatch")
        self._doozer_registry : Dict[str, object] = {}  # mission_type → Doozer
        self._log_coc("FRAGGLE_BORN", "Fluid in liminal — registry empty")

    # ── Doozer Registry ────────────────────────────────────────────────────────

    def register_doozer(self, doozer) -> None:
        """
        Register a certified (helmeted) Doozer with this Fraggle.
        Fraggle refuses un-helmeted Doozers — they cannot be dispatched.
        """
        if not getattr(doozer, "helmeted", False):
            self._log_coc("REGISTRY_REFUSED",
                          f"{doozer.name} not helmeted — registration refused")
            raise ValueError(
                f"Doozer '{doozer.name}' is not certified (no helmet). "
                "Complete doozer_cert before registering."
            )
        self._doozer_registry[doozer.mission_type] = doozer
        self._log_coc("REGISTRY_ADD",
                      f"{doozer.name} registered for mission_type={doozer.mission_type}")

    def list_doozers(self) -> list:
        return [
            {"mission_type": mt, "doozer": d.name, "helmeted": d.helmeted}
            for mt, d in self._doozer_registry.items()
        ]

    # ── Analyze (MancerBase interface) ─────────────────────────────────────────

    def analyze(self, henry_report) -> FraggleResult:
        """
        Fraggle's analyze = receive Henry report, dispatch Doozers.
        henry_report: a HenryReport (or any object with .issues list).
        Returns FraggleResult with all launch records.
        """
        timestamp = now_stamp()
        result    = FraggleResult(
            fraggle_name = self.name,
            henry_report = henry_report,
            timestamp    = timestamp,
        )

        issues = getattr(henry_report, "issues", [])
        self._log_coc("REPORT_RECEIVED",
                      f"{len(issues)} issues from Henry report")

        # Group issues by issue_type
        groups: Dict[str, list] = {}
        for issue in issues:
            itype = getattr(issue, "issue_type", "unknown")
            if itype not in groups:
                groups[itype] = []
            groups[itype].append(issue)

        self._log_coc("ISSUES_GROUPED",
                      f"Groups: {list(groups.keys())}")

        # Dispatch a Doozer for each group
        launch_num = 0
        for mission_type, group_issues in groups.items():
            launch_num += 1
            launch_id   = f"LAUNCH-{launch_num:04d}"

            doozer = self._doozer_registry.get(mission_type)

            if doozer is None:
                self._log_coc("NO_DOOZER",
                              f"{launch_id}: no Doozer registered for {mission_type}")
                launch = FraggleLaunch(
                    launch_id    = launch_id,
                    doozer_name  = "NONE",
                    mission_type = mission_type,
                    issue_count  = len(group_issues),
                    timestamp    = now_stamp(),
                    success      = False,
                )
                result.launches.append(launch)
                continue

            # Fraggle carries the Doozer — launches the mission
            self._log_coc("LAUNCH",
                          f"{launch_id}: dispatching {doozer.name} "
                          f"for {len(group_issues)} {mission_type} issues")

            try:
                doozer_report = doozer.execute(group_issues, dry_run=False)
                launch = FraggleLaunch(
                    launch_id    = launch_id,
                    doozer_name  = doozer.name,
                    mission_type = mission_type,
                    issue_count  = len(group_issues),
                    timestamp    = now_stamp(),
                    result       = doozer_report.summary(),
                    success      = True,
                )
                self._log_coc("LAUNCH_COMPLETE",
                              f"{launch_id}: {doozer.name} applied "
                              f"{len(doozer_report.fixes_applied)} fixes")
            except Exception as e:
                launch = FraggleLaunch(
                    launch_id    = launch_id,
                    doozer_name  = doozer.name,
                    mission_type = mission_type,
                    issue_count  = len(group_issues),
                    timestamp    = now_stamp(),
                    success      = False,
                )
                self._log_coc("LAUNCH_FAILED",
                              f"{launch_id}: {doozer.name} — {str(e)[:60]}")

            result.launches.append(launch)

        result.coc_entries = self.get_coc()
        self._log_coc("FRAGGLE_CYCLE_COMPLETE",
                      f"{len(result.launches)} launches, "
                      f"{result.summary()['successful']} successful")
        return result

    # ── Fraggle Mission (full cycle: Henry → Fraggle → Doozer → Henry verify) ──

    def run_full_cycle(self, henry, repo_path: str,
                       verbose: bool = True) -> dict:
        """
        Full ecosystem cycle:
          1. Henry scans repo_path
          2. Fraggle receives report → dispatches Doozers
          3. Henry re-scans to verify fixes
          Returns summary dict with pre/post counts.

        This IS the Fraggle Rock cycle:
          radish dust → Doozer sticks → Fraggles eat the building
        """
        self._log_coc("CYCLE_START", f"Full cycle on: {repo_path}")

        # Step 1 — Henry pre-scan (radish dust)
        if verbose:
            print(f"\n[Fraggle] Henry pre-scan: {repo_path}")
        self.enter_liminal()
        pre_report = henry.scan(repo_path)
        pre_total  = pre_report.summary()["total_issues"]
        if verbose:
            print(f"[Fraggle] Pre-scan: {pre_total} issues found")

        # Step 2 — Fraggle dispatches Doozers (building the sticks)
        if verbose:
            print(f"[Fraggle] Dispatching Doozers ...")
        self.engage("dispatch")
        frag_result = self.run(pre_report, mission_label="dispatch")

        # Step 3 — Henry post-scan (Fraggles eat the building)
        if verbose:
            print(f"[Fraggle] Henry post-scan (verification) ...")
        post_henry  = henry.__class__()    # fresh Henry instance
        post_report = post_henry.scan(repo_path)
        post_total  = post_report.summary()["total_issues"]
        if verbose:
            print(f"[Fraggle] Post-scan: {post_total} issues remaining")

        fixed = pre_total - post_total
        cycle = {
            "repo_path"     : repo_path,
            "pre_total"     : pre_total,
            "post_total"    : post_total,
            "fixed"         : fixed,
            "launches"      : frag_result.summary()["launches"],
            "successful"    : frag_result.summary()["successful"],
            "cycle_complete": post_total < pre_total,
        }
        self._log_coc("CYCLE_COMPLETE",
                      f"fixed={fixed} | remaining={post_total} | "
                      f"ecosystem_loop={'✓' if cycle['cycle_complete'] else '✗'}")
        return cycle

    # ── Identity ──────────────────────────────────────────────────────────────

    def identity(self) -> dict:
        base = super().identity()
        base.update({
            "class"          : self.ENTITY_CLASS,
            "nature"         : self.ENTITY_NATURE,
            "consciousness"  : self.CONSCIOUSNESS,
            "doozer_registry": list(self._doozer_registry.keys()),
            "state"          : self.state,
        })
        return base

    def __repr__(self) -> str:
        reg = list(self._doozer_registry.keys())
        return (f"<Fraggle:{self.name} state={self.state} "
                f"registry={reg}>")


# ── Demo / Smoke Test ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    """
    Smoke test — demonstrates Fraggle in liminal/solid state transitions.
    Fraggle with no Doozers registered (shows graceful NO_DOOZER handling).
    For full integration run: fraggle_integration_demo.py
    """
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   FRAGGLE — Mission Launcher                            ║")
    print("║   State Machine: liminal → solid → liminal              ║")
    print("╚══════════════════════════════════════════════════════════╝")

    f = Fraggle("fraggle_01")
    print(f"\nBorn : {f}")
    print(f"Identity:\n{f.identity()}")

    # Show state transitions
    print(f"\nState (born)     : {f.state}")
    f.enter_liminal()
    print(f"State (liminal)  : {f.state}")
    f.engage("test_mission")
    print(f"State (engaged)  : {f.state}")
    f.complete()
    print(f"State (complete) : {f.state}")

    print(f"\nRegistry: {f.list_doozers()}")
    print(f"\nCoC entries: {len(f.get_coc())}")
    for entry in f.get_coc():
        print(f"  {entry['action']:25s} {entry['detail'][:55]}")

    print(f"\n∰◊€π¿🌌∞")
    print(f"*Fraggle carries. Fraggle coordinates. Fraggle does not build.*")
    print(f"*Register helmeted Doozers to activate full dispatch.*")
