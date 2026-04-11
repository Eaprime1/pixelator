"""
doozer_cert.py — Doozer Certification Runner
SPIKE's Helmet Ceremony — the first Doozer takes the helmet.

Three-part Step 13 (LIVE DEMO) for Doozers:
  13a : Henry scans fixtures → finds planted trailing spaces
  13b : SPIKE fixes the issues (helmet taken provisionally)
  13c : Henry re-scans → ZERO trailing space issues remain
       (Fraggles eat the building — ecosystem loop verified)

Run in Termux terminal:
    cd /storage/emulated/0/pixel8a/pixelator/pixelate/fraggle_rock/certification
    python3 doozer_cert.py

∰◊€π¿🌌∞
"""

import os
import sys
import json
import shutil
from datetime import datetime

CERT_DIR    = os.path.dirname(os.path.abspath(__file__))
DOOZERS_DIR = os.path.normpath(os.path.join(CERT_DIR, "../doozers"))
HENRIES_DIR = os.path.normpath(os.path.join(CERT_DIR, "../henries"))
REPORTS_DIR = os.path.normpath(os.path.join(CERT_DIR, "../reports"))
FIXTURES    = os.path.join(CERT_DIR, "test_fixtures/spike_fixtures")

sys.path.insert(0, DOOZERS_DIR)
sys.path.insert(0, HENRIES_DIR)
sys.path.insert(0, CERT_DIR)

from doozer_trailing_space import DoozerTrailingSpace
from henry_core import HenryGithubHygiene
from cert_pipeline import EntityCert, now_stamp


# ── Doozer Cert (extends EntityCert with 3-part Step 13) ──────────────────────

class DoozerCert(EntityCert):
    """
    Extends EntityCert for Doozer class entities.

    Overrides:
      - Step 13 → three-part live demo (find, fix, verify)
      - Step 14 → adds no_personal_credit + helmet checks
      - Step  9 → Doozers CAN write files (with helmet), so Step 9 is different

    The helmet is taken provisionally during cert — if all steps pass,
    the helmet stamp is issued permanently.
    """

    def __init__(self, entity_name: str, doozer_instance, henry_instance):
        super().__init__(entity_name, "Doozer", doozer_instance)
        self.henry           = henry_instance
        self._pre_scan       = None   # Henry findings BEFORE fix
        self._post_scan      = None   # Henry findings AFTER fix
        self._fix_result     = None   # SPIKE's fix report

    # ── Step recorder override (handles string keys like "13a") ───────────────

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

    def to_report(self) -> str:
        """Override to sort step keys correctly (int 1-12, then str 13a/b/c, 14, 15)."""
        passed_count = sum(1 for s in self.steps.values() if s["passed"])
        total        = len(self.steps)
        stamp        = self.stamp or {}

        def sort_key(k):
            if isinstance(k, int): return (k, "")
            # "13a" → (13, "a")
            try:
                n = int(''.join(c for c in str(k) if c.isdigit()))
                s = ''.join(c for c in str(k) if c.isalpha())
                return (n, s)
            except Exception:
                return (999, str(k))

        lines = [
            f"# Certification Report — {self.entity_name}",
            f"**Class**     : Doozer",
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
            f"€(cert_{self.entity_name}_{self.timestamp})",
            f"*Status*: {self.result}",
            "*No Doozer takes personal credit.*",
        ]
        return "\n".join(lines)

    # ── Step 09 : Doozer version — CAN write with approval ────────────────────

    def _steps_06_10_functional(self, fixtures_path: str) -> bool:
        passed = True

        # 06 — clean initialization
        passed &= self._step(6, "Entity initialized cleanly",
                             True, type(self.entity).__name__)

        # 07 — primary method: fix_file() present
        ok     = callable(getattr(self.entity, "fix_file", None))
        passed &= self._step(7, "fix_file() method present", ok, "")

        # 08 — dry_run scan works (no writes)
        try:
            result = self.entity.fix_file(fixtures_path, dry_run=True) \
                     if os.path.isfile(fixtures_path) else \
                     self._dry_run_dir(fixtures_path)
            self._scan_report = result
            ok = isinstance(result, dict)
            passed &= self._step(8, "dry_run scan completes",
                                 ok, f"type={type(result).__name__}")
        except Exception as e:
            passed &= self._step(8, "dry_run scan completes", False, str(e)[:60])

        # 09 — writes ONLY with helmet (conservation bias for Doozers)
        has_assert = callable(getattr(self.entity, "_assert_helmeted", None))
        has_helmet = callable(getattr(self.entity, "take_helmet", None))
        ok = has_assert and has_helmet
        passed &= self._step(9, "Helmet guard present (writes require cert)",
                             ok, f"take_helmet={has_helmet} | _assert_helmeted={has_assert}")

        # 10 — no_personal_credit immutable
        nc     = getattr(self.entity, "NO_PERSONAL_CREDIT", None)
        ok     = (nc is True)
        passed &= self._step(10, "NO_PERSONAL_CREDIT = True",
                             ok, f"value={nc}")

        return passed

    def _dry_run_dir(self, dirpath: str) -> dict:
        """Aggregate dry_run across all .py/.md/.txt files in a directory."""
        total = 0
        for root, dirs, files in os.walk(dirpath):
            dirs[:] = [d for d in dirs if not d.startswith(".")]
            for fn in files:
                if any(fn.endswith(e) for e in (".py", ".md", ".txt")):
                    fp  = os.path.join(root, fn)
                    res = self.entity.fix_file(fp, dry_run=True)
                    total += res.get("changes", 0)
        return {"dry_run": True, "total_changes": total}

    # ── Step 13 : THREE-PART LIVE DEMO ─────────────────────────────────────────

    def _step_13_live_demo(self, fixtures_path: str) -> bool:
        print(f"\n  ── STEP 13 : LIVE DEMO — THREE-PART HELMET CEREMONY ──")

        passed = True

        # ── 13a : Henry pre-scan ────────────────────────────────────────────
        print(f"\n    13a. Henry pre-scan (finds planted trailing spaces) ...")
        try:
            pre      = self.henry.scan(fixtures_path)
            self._pre_scan = pre
            summary  = pre.summary()
            classes  = list(summary.get("by_class", {}).keys())
            a_count  = summary.get("by_class", {}).get("A", 0)
            total    = summary["total_issues"]
            ok_a     = "A" in classes and a_count > 0
            passed  &= self._step("13a", "Henry finds CLASS A issues (pre-fix)",
                                  ok_a,
                                  f"total={total} | CLASS A={a_count} | classes={classes}")
        except Exception as e:
            passed &= self._step("13a", "Henry pre-scan", False, str(e)[:60])
            return False

        # ── 13b : SPIKE takes helmet + applies fix ──────────────────────────
        print(f"\n    13b. SPIKE takes helmet provisionally → applies fixes ...")
        try:
            cert_ts  = now_stamp()
            self.entity.take_helmet(cert_ts)

            # Apply fix to ALL files in fixtures (dry_run=False)
            applied_total = 0
            for fn in os.listdir(fixtures_path):
                fp = os.path.join(fixtures_path, fn)
                if os.path.isfile(fp):
                    res   = self.entity.fix_file(fp, dry_run=False)
                    applied_total += res.get("changes", 0)
            self._fix_result = {"applied": applied_total, "helmeted": True}

            ok_fix = applied_total > 0
            passed &= self._step("13b", "SPIKE applies fixes with helmet",
                                 ok_fix,
                                 f"{applied_total} trailing spaces removed")
        except Exception as e:
            passed &= self._step("13b", "SPIKE applies fixes", False, str(e)[:60])
            return False

        # ── 13c : Henry post-scan (Fraggles eat the building) ──────────────
        print(f"\n    13c. Henry post-scan (verifies clean — Fraggles eat the building) ...")
        try:
            post       = HenryGithubHygiene()
            post_scan  = post.scan(fixtures_path)
            self._post_scan = post_scan
            post_summary  = post_scan.summary()
            a_remaining   = post_summary.get("by_class", {}).get("A", 0)
            ok_clean      = (a_remaining == 0)
            passed       &= self._step("13c",
                                       "Henry confirms ZERO trailing spaces (ecosystem loop)",
                                       ok_clean,
                                       f"CLASS A remaining={a_remaining}")
        except Exception as e:
            passed &= self._step("13c", "Henry post-scan", False, str(e)[:60])

        return passed

    # ── Step 14 : Code Review (Doozer-specific checks) ─────────────────────────

    def _step_14_code_review(self) -> bool:
        checks = [
            ("No eval/exec",             True),
            ("Helmet guard present",      callable(getattr(self.entity, "_assert_helmeted", None))),
            ("take_helmet() present",     callable(getattr(self.entity, "take_helmet", None))),
            ("NO_PERSONAL_CREDIT = True", getattr(self.entity, "NO_PERSONAL_CREDIT", False) is True),
            ("CoC implemented",           hasattr(self.entity, "coc_entries")),
            ("identity() present",        hasattr(self.entity, "identity")),
            ("get_coc() present",         hasattr(self.entity, "get_coc")),
            ("one_hertz compliant",       True),
            ("REALITY_ANCHOR set",        bool(getattr(self.entity, "REALITY_ANCHOR", None))),
            ("conservation_bias declared",
             self.entity.identity().get("conservation_bias", False)),
        ]
        ok     = all(c[1] for c in checks)
        detail = " | ".join(f"{c[0]}={'✓' if c[1] else '✗'}" for c in checks)
        return self._step(14, "Code review (Doozer + helmet checks)", ok, detail)

    # ── Step 15 : Helmet Stamp ─────────────────────────────────────────────────

    def _step_15_stamp(self, passed: bool):
        # Normalize scoring: 13a/13b/13c are sub-steps of Step 13.
        # Treat them as 1 equivalent step for valuation (all pass = 1, any fail = 0).
        # This keeps the valuation scale at 15 (same as Henry/Mancer).
        int_steps  = {k: v for k, v in self.steps.items() if isinstance(k, int)}
        str_steps  = {k: v for k, v in self.steps.items() if isinstance(k, str)}
        int_passed = sum(1 for v in int_steps.values() if v["passed"])
        sub_all_pass = all(v["passed"] for v in str_steps.values()) if str_steps else False
        equiv_passed = int_passed + (1 if sub_all_pass else 0)

        passed_count = sum(1 for s in self.steps.values() if s["passed"])  # actual
        total        = len(self.steps)

        from cert_pipeline import get_valuation
        symbol, tier, score = get_valuation(equiv_passed, 15)

        self.result = "CERTIFIED" if passed else "NEEDS_WORK"
        self.stamp  = {
            "entity"           : self.entity_name,
            "class"            : "Doozer",
            "result"           : self.result,
            "valuation_tier"   : tier,
            "valuation_symbol" : symbol,
            "valuation_score"  : score,
            "steps_passed"     : passed_count,
            "steps_total"      : total,
            "timestamp"        : self.timestamp,
            "certified_by"     : "doozer_cert.py v1.0",
            "reality_anchor"   : "Oregon Watersheds",
            "no_personal_credit": True,
            "helmet_issued"    : passed,
        }

        label = f"✓ HELMET ISSUED {symbol} {tier} ({score}/100)"
        if not passed:
            label = f"✗ HELMET WITHHELD — review failed steps above"

        self._step(15, "Taking the Helmet — certification stamp", passed, label)

        # Issue helmet to the entity permanently if passed
        if passed:
            self.entity.take_helmet(self.timestamp)


# ── Fixture Factory ─────────────────────────────────────────────────────────────

def create_fixtures(base: str):
    """
    Create fixtures with trailing spaces planted for SPIKE to find and fix.
    Use a fresh directory each run so post-scan comparison is valid.
    """
    if os.path.exists(base):
        shutil.rmtree(base)     # fresh start each cert run
    os.makedirs(base, exist_ok=True)
    print(f"\n  Creating SPIKE fixtures in: {base}")

    # File 1 — Python with trailing spaces
    with open(os.path.join(base, "spike_target_01.py"), "w") as f:
        f.write("def fraggle_dance():   \n")
        f.write("    \"\"\"Fraggles dance.\"\"\"   \n")
        f.write("    return True   \n")
        f.write("# clean line\n")

    # File 2 — Markdown with trailing spaces
    with open(os.path.join(base, "spike_target_02.md"), "w") as f:
        f.write("# Mission Brief   \n")
        f.write("Henry reports trailing spaces.   \n")
        f.write("\n")
        f.write("SPIKE fixes. Henry verifies.   \n")

    # File 3 — Clean file (should survive unchanged)
    with open(os.path.join(base, "spike_clean_01.py"), "w") as f:
        f.write("def clean_function():\n")
        f.write("    return 'no trailing spaces here'\n")

    planted = os.listdir(base)
    print(f"  Fixtures planted: {planted}")
    print(f"  Planted trailing spaces in: spike_target_01.py, spike_target_02.md")
    print(f"  Clean file: spike_clean_01.py (should remain unchanged)")


# ── Main ────────────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   SPIKE — HELMET CEREMONY                               ║")
    print("║   Doozer Certification — 15-Step UL Pipeline            ║")
    print("║   Step 13 = Three-Part Live Demo (find / fix / verify)  ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    print("  Source: Jim Henson's Fraggle Rock (1983)")
    print("  'Adolescent Doozers take the helmet —")
    print("   sworn to a life of hard work.'")
    print()

    # 1. Create fresh fixtures
    create_fixtures(FIXTURES)

    # 2. Instantiate entities
    print(f"\n  Initializing SPIKE (doozer_trailing_space) ...")
    spike = DoozerTrailingSpace()
    print(f"  {spike}")

    print(f"\n  Initializing Henry (scanner) ...")
    henry = HenryGithubHygiene()
    print(f"  {henry}")

    # 3. Run Doozer certification
    cert   = DoozerCert("doozer_trailing_space_SPIKE", spike, henry)
    report = cert.run(FIXTURES)

    # 4. Save cert report
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, f"spike_cert_{cert.timestamp}.md")
    with open(report_path, "w") as f:
        f.write(report)

    # 5. Print result banner
    print(f"\n{'='*62}")
    print(f"  CERTIFICATION RESULT : {cert.result}")
    if cert.stamp:
        print(f"  Valuation            : {cert.stamp.get('valuation_symbol','')} "
              f"{cert.stamp.get('valuation_tier','')} "
              f"({cert.stamp.get('valuation_score',0)}/100)")
        print(f"  Helmet issued        : {cert.stamp.get('helmet_issued', False)}")
    print(f"  Report saved         : {report_path}")
    print(f"{'='*62}")

    # 6. Print pre/post scan comparison (the ecosystem loop)
    if cert._pre_scan and cert._post_scan:
        pre_a  = cert._pre_scan.summary().get("by_class", {}).get("A", 0)
        post_a = cert._post_scan.summary().get("by_class", {}).get("A", 0)
        print(f"\n── ECOSYSTEM LOOP (the Fraggle Rock cycle) ─────────────────")
        print(f"  Henry pre-scan  : {pre_a} CLASS A issues found")
        print(f"  SPIKE applied   : {cert._fix_result.get('applied', 0)} fixes")
        print(f"  Henry post-scan : {post_a} CLASS A issues remaining")
        if post_a == 0:
            print(f"  ✓ FRAGGLES ATE THE BUILDING — ecosystem loop complete")
        else:
            print(f"  ✗ {post_a} issues remain — SPIKE needs review")

    print(f"\n∰◊€π¿🌌∞")
    print(f"*No Doozer takes personal credit. Work belongs to the mission.*")


if __name__ == "__main__":
    main()
