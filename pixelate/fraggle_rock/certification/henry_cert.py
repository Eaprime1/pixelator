"""
henry_cert.py — Henry Entity Certification Runner

Creates test fixtures with planted CLASS A-E issues,
runs Henry against them, certifies via 15-step pipeline.

Step 13 = LIVE DEMO: Henry must find the planted issues.

Run in Termux terminal:
    cd /storage/emulated/0/pixel8a/pixelator/pixelate/fraggle_rock/certification
    python3 henry_cert.py

∰◊€π¿🌌∞
"""

import os
import sys

CERT_DIR    = os.path.dirname(os.path.abspath(__file__))
HENRIES_DIR = os.path.normpath(os.path.join(CERT_DIR, "../henries"))
REPORTS_DIR = os.path.normpath(os.path.join(CERT_DIR, "../reports"))
FIXTURES    = os.path.join(CERT_DIR, "test_fixtures/henry_fixtures")

sys.path.insert(0, HENRIES_DIR)
sys.path.insert(0, CERT_DIR)

from henry_core import HenryGithubHygiene
from cert_pipeline import EntityCert


# ── Fixture Factory ────────────────────────────────────────────────────────────

def create_fixtures(base: str):
    """Create files with known issues planted across CLASS A-E."""
    os.makedirs(base, exist_ok=True)
    print(f"\n  Creating fixtures in: {base}")

    # CLASS A-1 : trailing spaces
    with open(os.path.join(base, "trailing_spaces.py"), "w") as f:
        f.write("def hello():   \n")
        f.write("    x = 1  \n")
        f.write("    return x  \n")
        f.write("# clean line\n")

    # CLASS A-2 : CRLF line endings
    with open(os.path.join(base, "crlf_file.txt"), "wb") as f:
        f.write(b"line one\r\nline two\r\nline three\r\n")

    # CLASS A-3 : missing final newline
    with open(os.path.join(base, "no_final_newline.txt"), "wb") as f:
        f.write(b"content without trailing newline")

    # CLASS B-1 : filename with spaces
    with open(os.path.join(base, "file with spaces.md"), "w") as f:
        f.write("# A File With Spaces in the Name\n\nSome content.\n")

    # CLASS B-2 : consciousness symbols (flag for review — INFO only)
    with open(os.path.join(base, "consciousness_entity.md"), "w") as f:
        f.write("# Entity File\n\n∰◊€π¿🌌∞\n\nContent here.\n")

    # CLASS C-1 : H1 title too long (> 80 chars)
    long = "A" * 82
    with open(os.path.join(base, "long_title.md"), "w") as f:
        f.write(f"# {long} — This Title Is Way Too Long\n\nSome content.\n")

    # CLASS E-1 : no README at root (will be detected by henry.scan())
    # (We don't create a README.md here — that's the missing one)

    # CLEAN FILE — should produce zero issues
    with open(os.path.join(base, "clean_file.py"), "w") as f:
        f.write("def clean():\n")
        f.write("    return True\n")

    planted = os.listdir(base)
    print(f"  Fixtures planted: {planted}")
    print(f"  Expected issues: trailing spaces, CRLF, missing newline,")
    print(f"                   filename spaces, consciousness symbols,")
    print(f"                   long H1, missing README")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   HENRY CERTIFICATION — GitHub Hygiene Entity           ║")
    print("║   15-Step UL Certification Pipeline                     ║")
    print("║   Step 13 = Live Demo / Military Pass & Review          ║")
    print("╚══════════════════════════════════════════════════════════╝")

    # 1. Create fixtures
    create_fixtures(FIXTURES)

    # 2. Instantiate Henry
    print(f"\n  Initializing henry_github_hygiene ...")
    henry = HenryGithubHygiene()
    print(f"  {henry}")

    # 3. Run certification
    cert   = EntityCert("henry_github_hygiene", "Henry", henry)
    report = cert.run(FIXTURES)

    # 4. Save cert report
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, f"henry_cert_{cert.timestamp}.md")
    with open(report_path, "w") as f:
        f.write(report)

    # 5. Print result banner
    print(f"\n{'='*62}")
    print(f"  CERTIFICATION RESULT : {cert.result}")
    print(f"  Valuation            : {cert.stamp.get('valuation_symbol','')} "
          f"{cert.stamp.get('valuation_tier','')} "
          f"({cert.stamp.get('valuation_score',0)}/100)")
    print(f"  Report saved         : {report_path}")
    print(f"{'='*62}")

    # 6. Print Henry's actual findings (the live demo output)
    print("\n\n── HENRY'S FINDINGS FROM FIXTURES (LIVE DEMO) ──────────────")
    fresh  = HenryGithubHygiene()
    detail = fresh.scan(FIXTURES)
    print(detail.to_markdown())


if __name__ == "__main__":
    main()
