"""
mancer_cert.py — Mancer Entity Certification Runner

Certifies: lsmancer, trackmancer
Each mancer runs its live demo against test fixtures in Step 13.

Run in Termux terminal:
    cd /storage/emulated/0/pixel8a/pixelator/pixelate/fraggle_rock/certification
    python3 mancer_cert.py

∰◊€π¿🌌∞
"""

import os
import sys

CERT_DIR    = os.path.dirname(os.path.abspath(__file__))
MANCERS_DIR = os.path.normpath(os.path.join(CERT_DIR, "../mancers"))
REPORTS_DIR = os.path.normpath(os.path.join(CERT_DIR, "../reports"))
FIXTURES    = os.path.join(CERT_DIR, "test_fixtures")

sys.path.insert(0, MANCERS_DIR)
sys.path.insert(0, CERT_DIR)

from lsmancer    import LsMancer
from trackmancer import TrackMancer
from cert_pipeline import EntityCert


# ── lsmancer Certification ────────────────────────────────────────────────────

def cert_lsmancer(target: str) -> str:
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║   LSMANCER CERTIFICATION                                ║")
    print("║   Domain: Directory Structure Analysis                  ║")
    print("╚══════════════════════════════════════════════════════════╝")

    mancer = LsMancer(max_depth=3)
    cert   = EntityCert("lsmancer", "Mancer", mancer)
    report = cert.run(target)

    os.makedirs(REPORTS_DIR, exist_ok=True)
    path = os.path.join(REPORTS_DIR, f"lsmancer_cert_{cert.timestamp}.md")
    with open(path, "w") as f:
        f.write(report)

    print(f"\n  RESULT   : {cert.result}")
    print(f"  Valuation: {cert.stamp.get('valuation_symbol','')} "
          f"{cert.stamp.get('valuation_tier','')} "
          f"({cert.stamp.get('valuation_score',0)}/100)")
    print(f"  Report   : {path}")

    print("\n── LSMANCER LIVE OUTPUT ─────────────────────────────────────")
    fresh  = LsMancer(max_depth=3)
    result = fresh.run(target, mission_label="certification_demo")
    print(fresh.to_text(result))

    return cert.result


# ── trackmancer Certification ─────────────────────────────────────────────────

def cert_trackmancer() -> str:
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║   TRACKMANCER CERTIFICATION                             ║")
    print("║   Domain: Chain of Custody Ledger                      ║")
    print("╚══════════════════════════════════════════════════════════╝")

    os.makedirs(FIXTURES, exist_ok=True)
    ledger_path = os.path.join(REPORTS_DIR, "test_ledger.json")
    os.makedirs(REPORTS_DIR, exist_ok=True)

    mancer = TrackMancer(ledger_path)

    # Pre-populate with test entries for certification demo
    id1 = mancer.add_entry("henry_test",    "SCAN",    "Test scan entry",    "COMPLETE")
    id2 = mancer.add_entry("lsmancer_test", "ANALYZE", "Test analyze entry", "COMPLETE")
    id3 = mancer.add_entry("fraggle_test",  "LAUNCH",  "Test launch entry",  "ACTIVE")
    mancer.update_status(id3, "COMPLETE")

    cert   = EntityCert("trackmancer", "Mancer", mancer)
    report = cert.run(FIXTURES)

    path = os.path.join(REPORTS_DIR, f"trackmancer_cert_{cert.timestamp}.md")
    with open(path, "w") as f:
        f.write(report)

    print(f"\n  RESULT   : {cert.result}")
    print(f"  Valuation: {cert.stamp.get('valuation_symbol','')} "
          f"{cert.stamp.get('valuation_tier','')} "
          f"({cert.stamp.get('valuation_score',0)}/100)")
    print(f"  Report   : {path}")

    print("\n── TRACKMANCER LIVE OUTPUT ──────────────────────────────────")
    print(mancer.report())

    return cert.result


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   MANCER CERTIFICATION SUITE                            ║")
    print("║   lsmancer + trackmancer                                ║")
    print("║   15-Step UL Pipeline — Step 13 = Live Demo            ║")
    print("╚══════════════════════════════════════════════════════════╝")

    target = sys.argv[1] if len(sys.argv) > 1 else CERT_DIR

    r1 = cert_lsmancer(target)
    r2 = cert_trackmancer()

    print(f"\n{'='*62}")
    print(f"  MANCER CERTIFICATION SUMMARY")
    print(f"  lsmancer    : {r1}")
    print(f"  trackmancer : {r2}")
    all_certified = all(r == "CERTIFIED" for r in [r1, r2])
    final = "ALL MANCERS CERTIFIED ✓" if all_certified else "REVIEW REQUIRED"
    print(f"  Final       : {final}")
    print(f"{'='*62}")
    print("\n  ∰◊€π¿🌌∞")
    print("  €(mancer_certification_complete)")


if __name__ == "__main__":
    main()
