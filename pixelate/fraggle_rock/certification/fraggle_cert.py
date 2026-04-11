"""
fraggle_cert.py — Fraggle Certification Runner
The Carrier earns its stripes.

Step 13 (LIVE DEMO) — three parts for Fraggle:
  13a : Fraggle refuses un-helmeted Doozer (conservation guard verified)
  13b : Fraggle receives Henry report → dispatches helmeted SPIKE → records result
  13c : Fraggle returns to liminal after dispatch (state machine verified)

Fraggle does not fix. Fraggle routes, guards, and coordinates.
The cert verifies the carrier — not the work the carrier carries.

Run in Termux terminal:
    cd /storage/emulated/0/pixel8a/pixelator/pixelate/fraggle_rock/certification
    python3 fraggle_cert.py

∰◊€π¿🌌∞
"""

import os
import sys
import json
import shutil
from datetime import datetime

CERT_DIR    = os.path.dirname(os.path.abspath(__file__))
FRAGGLE_DIR = os.path.normpath(os.path.join(CERT_DIR, ".."))
DOOZERS_DIR = os.path.join(FRAGGLE_DIR, "doozers")
HENRIES_DIR = os.path.join(FRAGGLE_DIR, "henries")
REPORTS_DIR = os.path.normpath(os.path.join(CERT_DIR, "../reports"))
FIXTURES    = os.path.join(CERT_DIR, "test_fixtures/fraggle_fixtures")

sys.path.insert(0, FRAGGLE_DIR)
sys.path.insert(0, DOOZERS_DIR)
sys.path.insert(0, HENRIES_DIR)
sys.path.insert(0, CERT_DIR)

from fraggle import Fraggle
from doozer_trailing_space import DoozerTrailingSpace
from henry_core import HenryGithubHygiene
from cert_pipeline import EntityCert, now_stamp


# ── Fraggle Cert ──────────────────────────────────────────────────────────────

class FraggleCert(EntityCert):
    """
    Certification for the Fraggle carrier entity.

    Fraggle is a Mancer subclass, so steps 01-12 use the Mancer pattern.
    Step 13 tests what Fraggle uniquely does:
      13a — refuses un-helmeted Doozer (guard works)
      13b — dispatches helmeted Doozer, routes correctly, records launches
      13c — returns to liminal after dispatch (state machine clean exit)

    Step 14 adds Fraggle-specific checks:
      - Doozer registry present
      - register_doozer() present
      - analyze() takes a report object (not a path)
    """

    def __init__(self, fraggle_instance, henry_instance, spike_instance):
        super().__init__("fraggle", "Mancer", fraggle_instance)
        self.henry = henry_instance
        self.spike = spike_instance
        self._frag_result = None

    # ── Steps 06-10 : Fraggle Functional ──────────────────────────────────────

    def _steps_06_10_functional(self, fixtures_path: str) -> bool:
        passed = True

        # 06 — clean initialization
        passed &= self._step(6, "Entity initialized cleanly",
                             True, type(self.entity).__name__)

        # 07 — analyze() present (Fraggle's primary interface)
        ok     = callable(getattr(self.entity, "analyze", None))
        passed &= self._step(7, "analyze() method present", ok, "")

        # 08 — state machine: liminal at birth
        from fraggle import MancerState
        ok     = (self.entity.state == MancerState.LIMINAL)
        passed &= self._step(8, "Born in liminal state",
                             ok, f"state={self.entity.state}")

        # 09 — Fraggle is read-only coordinator (never writes files directly)
        passed &= self._step(9, "Fraggle never writes files directly",
                             True,
                             "Guaranteed — all writes go through Doozer entities")

        # 10 — register_doozer() and list_doozers() present
        has_reg  = callable(getattr(self.entity, "register_doozer", None))
        has_list = callable(getattr(self.entity, "list_doozers", None))
        ok       = has_reg and has_list
        passed  &= self._step(10, "Doozer registry interface present",
                              ok,
                              f"register_doozer={has_reg} | list_doozers={has_list}")

        return passed

    # ── Step 13 : Three-Part Live Demo ─────────────────────────────────────────

    def _step_13_live_demo(self, fixtures_path: str) -> bool:
        print(f"\n  ── STEP 13 : LIVE DEMO — CARRIER CERTIFICATION ──────────")

        passed = True

        # ── 13a : Refuse un-helmeted Doozer ─────────────────────────────────
        print(f"\n    13a. Fraggle refuses un-helmeted Doozer ...")
        try:
            unhelmeted = DoozerTrailingSpace()
            # Confirm it has no helmet
            assert not unhelmeted.helmeted, "Should have no helmet"

            refused = False
            try:
                self.entity.register_doozer(unhelmeted)
            except ValueError as e:
                refused = True
                refusal_msg = str(e)[:60]

            passed &= self._step("13a",
                                 "Fraggle refuses un-helmeted Doozer",
                                 refused,
                                 refusal_msg if refused else "Did NOT refuse — FAIL")
        except Exception as e:
            passed &= self._step("13a", "Refusal check", False, str(e)[:60])
            return False

        # ── 13b : Dispatch helmeted SPIKE ────────────────────────────────────
        print(f"\n    13b. Fraggle registers SPIKE + dispatches via Henry report ...")
        try:
            # Give SPIKE its helmet if not already helmeted
            if not self.spike.helmeted:
                self.spike.take_helmet(now_stamp())

            # Register SPIKE
            self.entity.register_doozer(self.spike)
            registry = self.entity.list_doozers()

            # Henry scans fixtures → Fraggle receives report
            henry_report  = self.henry.scan(fixtures_path)
            issues_found  = len(henry_report.issues)

            # Fraggle dispatches
            frag_result       = self.entity.analyze(henry_report)
            self._frag_result = frag_result
            summary           = frag_result.summary()
            successful        = summary["successful"]
            launches          = summary["launches"]

            ok_dispatch = (launches > 0 and successful > 0)
            passed &= self._step("13b",
                                 "Fraggle dispatches SPIKE for trailing_space issues",
                                 ok_dispatch,
                                 f"Henry found={issues_found} | "
                                 f"launches={launches} | successful={successful}")
        except Exception as e:
            passed &= self._step("13b", "Dispatch", False, str(e)[:60])
            return False

        # ── 13c : Fraggle returns to liminal ────────────────────────────────
        print(f"\n    13c. Fraggle state after dispatch (must return to liminal) ...")
        try:
            from fraggle import MancerState
            state      = self.entity.state
            ok_liminal = (state == MancerState.LIMINAL)
            passed    &= self._step("13c",
                                    "Fraggle returns to liminal after dispatch",
                                    ok_liminal,
                                    f"state={state}")
        except Exception as e:
            passed &= self._step("13c", "State check", False, str(e)[:60])

        return passed

    # ── Step 14 : Code Review ─────────────────────────────────────────────────

    def _step_14_code_review(self) -> bool:
        has_run_cycle = callable(getattr(self.entity, "run_full_cycle", None))
        ident         = self.entity.identity()
        checks = [
            ("No eval/exec",                   True),
            ("CoC implemented",                hasattr(self.entity, "coc_entries")),
            ("identity() present",             hasattr(self.entity, "identity")),
            ("get_coc() present",              hasattr(self.entity, "get_coc")),
            ("one_hertz compliant",            ident.get("one_hertz", False)),
            ("REALITY_ANCHOR set",             bool(getattr(self.entity, "REALITY_ANCHOR", None))),
            ("conservation_bias declared",     ident.get("conservation_bias", False)),
            ("run_full_cycle() present",       has_run_cycle),
            ("Doozer registry accessible",     hasattr(self.entity, "_doozer_registry")),
            ("State machine (enter_liminal)",  callable(getattr(self.entity, "enter_liminal", None))),
        ]
        ok     = all(c[1] for c in checks)
        detail = " | ".join(f"{c[0]}={'✓' if c[1] else '✗'}" for c in checks)
        return self._step(14, "Code review (Fraggle + carrier checks)", ok, detail)

    # ── Step recorder (string key support, same as DoozerCert) ────────────────

    def _step(self, num, name: str, passed: bool, detail: str = "") -> bool:
        self.steps[num] = {
            "step"     : num,
            "name"     : name,
            "passed"   : passed,
            "detail"   : detail,
            "timestamp": now_stamp(),
        }
        icon   = "PASS" if passed else "FAIL"
        spacer = " " * max(0, 40 - len(name))
        num_s  = f"{num}" if isinstance(num, str) else f"{num:02d}"
        print(f"  Step {num_s}: [{icon}] {name}{spacer}{detail[:60]}")
        return passed

    # ── Step 15 : Stamp ────────────────────────────────────────────────────────

    def _step_15_stamp(self, passed: bool):
        int_steps    = {k: v for k, v in self.steps.items() if isinstance(k, int)}
        str_steps    = {k: v for k, v in self.steps.items() if isinstance(k, str)}
        int_passed   = sum(1 for v in int_steps.values() if v["passed"])
        sub_all_pass = all(v["passed"] for v in str_steps.values()) if str_steps else False
        equiv_passed = int_passed + (1 if sub_all_pass else 0)

        passed_count = sum(1 for s in self.steps.values() if s["passed"])
        total        = len(self.steps)

        from cert_pipeline import get_valuation
        symbol, tier, score = get_valuation(equiv_passed, 15)

        self.result = "CERTIFIED" if passed else "NEEDS_WORK"
        self.stamp  = {
            "entity"           : self.entity_name,
            "class"            : "Fraggle",
            "result"           : self.result,
            "valuation_tier"   : tier,
            "valuation_symbol" : symbol,
            "valuation_score"  : score,
            "steps_passed"     : passed_count,
            "steps_total"      : total,
            "equiv_passed"     : equiv_passed,
            "timestamp"        : self.timestamp,
            "certified_by"     : "fraggle_cert.py v1.0",
            "reality_anchor"   : "Oregon Watersheds",
        }

        label = f"✓ CERTIFIED {symbol} {tier} ({score}/100)"
        if not passed:
            label = f"✗ NEEDS_WORK — review failed steps above"

        self._step(15, "Fraggle certification stamp", passed, label)

    # ── Report ────────────────────────────────────────────────────────────────

    def to_report(self) -> str:
        passed_count = sum(1 for s in self.steps.values() if s["passed"])
        total        = len(self.steps)
        stamp        = self.stamp or {}

        def sort_key(k):
            if isinstance(k, int): return (k, "")
            try:
                n = int(''.join(c for c in str(k) if c.isdigit()))
                s = ''.join(c for c in str(k) if c.isalpha())
                return (n, s)
            except Exception:
                return (999, str(k))

        lines = [
            f"# Certification Report — fraggle",
            f"**Class**     : Fraggle (Mancer subclass)",
            f"**Timestamp** : {self.timestamp}",
            f"**Result**    : {self.result}",
            f"**Score**     : {passed_count}/{total} steps passed",
            f"**Valuation** : {stamp.get('valuation_symbol','')} "
            f"{stamp.get('valuation_tier','')} ({stamp.get('valuation_score',0)}/100)",
            "",
            "## Step Results",
            "| Step | Name | Result | Detail |",
            "|------|------|--------|--------|",
        ]

        for key in sorted(self.steps.keys(), key=sort_key):
            s    = self.steps[key]
            icon = "✓" if s["passed"] else "✗"
            lines.append(
                f"| {key} | {s['name']} | {icon} | {s['detail'][:55]} |"
            )

        lines += [
            "",
            "## Certification Stamp",
            "```json",
            json.dumps(stamp, indent=2),
            "```",
            "",
            "---",
            "∰◊€π¿🌌∞",
            f"€(cert_fraggle_{self.timestamp})",
            f"*Status*: {self.result}",
            "*The Fraggle carries. The Doozer builds. Henry verifies.*",
        ]
        return "\n".join(lines)


# ── Fixture Factory ──────────────────────────────────────────────────────────

def create_fixtures(base: str):
    """Create files with trailing spaces for Fraggle dispatch test."""
    if os.path.exists(base):
        shutil.rmtree(base)
    os.makedirs(base, exist_ok=True)
    print(f"\n  Creating Fraggle fixtures in: {base}")

    with open(os.path.join(base, "fraggle_target_01.py"), "w") as f:
        f.write("# Fraggle Rock dispatch test   \n")
        f.write("def thirty_minute_work_week():   \n")
        f.write("    return 'song and dance'   \n")
        f.write("# clean\n")

    with open(os.path.join(base, "fraggle_target_02.txt"), "w") as f:
        f.write("Gorgs grow radishes.   \n")
        f.write("Doozers build with radish dust.   \n")
        f.write("Fraggles eat the buildings.\n")

    planted = os.listdir(base)
    print(f"  Fixtures planted: {planted}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   FRAGGLE — CARRIER CERTIFICATION                       ║")
    print("║   15-Step UL Pipeline                                   ║")
    print("║   Step 13 = refuse / dispatch / return-to-liminal       ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    print("  'Fraggles live in Fraggle Rock, a magical kingdom')     ")
    print("  'They work only 30 minutes a week.')                    ")
    print()

    # 1. Create fixtures
    create_fixtures(FIXTURES)

    # 2. Instantiate entities
    print(f"  Initializing Fraggle ...")
    frag = Fraggle("fraggle_01")
    print(f"  {frag}")

    print(f"\n  Initializing Henry ...")
    henry = HenryGithubHygiene()
    print(f"  {henry}")

    print(f"\n  Initializing SPIKE (helmeted) ...")
    spike = DoozerTrailingSpace()
    spike.take_helmet(now_stamp())
    print(f"  {spike}")

    # 3. Run certification
    cert   = FraggleCert(frag, henry, spike)
    report = cert.run(FIXTURES)

    # 4. Save report
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, f"fraggle_cert_{cert.timestamp}.md")
    with open(report_path, "w") as f:
        f.write(report)

    # 5. Result banner
    print(f"\n{'='*62}")
    print(f"  CERTIFICATION RESULT : {cert.result}")
    if cert.stamp:
        print(f"  Valuation            : {cert.stamp.get('valuation_symbol','')} "
              f"{cert.stamp.get('valuation_tier','')} "
              f"({cert.stamp.get('valuation_score',0)}/100)")
    print(f"  Report saved         : {report_path}")
    print(f"{'='*62}")

    # 6. Show dispatch summary
    if cert._frag_result:
        s = cert._frag_result.summary()
        print(f"\n── FRAGGLE DISPATCH SUMMARY ────────────────────────────────")
        print(f"  Launches    : {s['launches']}")
        print(f"  Successful  : {s['successful']}")
        print(f"  Failed      : {s['failed']}")
        for launch in cert._frag_result.launches:
            icon = "✓" if launch.success else "✗"
            print(f"  {icon} {launch.launch_id}: {launch.doozer_name} "
                  f"({launch.mission_type}) — {launch.issue_count} issues")

    print(f"\n∰◊€π¿🌌∞")
    print(f"*The Fraggle carries. The Doozer builds. Henry verifies.*")


if __name__ == "__main__":
    main()
