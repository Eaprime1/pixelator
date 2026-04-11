#!/usr/bin/env python3
"""
Vetting Economy - Pixelator Quality System
Handles submissions, incentives, reports, and ownership transfers

Philosophy:
- Submit for vetting → earn incentive reward
- Every interaction logged with file ID
- Transfer of responsibility through approval
- Drive + phone integration via file IDs
"""

import json
import uuid
from pathlib import Path
from datetime import datetime


DECISIONS = ["APPROVED", "NEEDS_WORK", "REJECTED"]

INCENTIVE_TABLE = {
    "submission":   1,   # earned at submission
    "review":       2,   # earned by reviewer
    "approval":     3,   # bonus on approval
}


class VettingEconomy:
    """
    Project-wide vetting economy for pixelator system

    Responsibilities:
    - Accept domos/document submissions
    - Issue vetting incentives
    - Generate vetting reports
    - Log file IDs for interaction tracking
    - Transfer ownership on approval
    - Track vetting economy ledger
    """

    def __init__(self, vetting_root):
        self.root = Path(vetting_root)
        self.inbox     = self.root / "inbox"
        self.in_review = self.root / "in_review"
        self.approved  = self.root / "approved"
        self.needs_work= self.root / "needs_work"
        self.reports   = self.root / "reports"

        # Ensure all stage dirs exist
        for d in [self.inbox, self.in_review,
                  self.approved, self.needs_work, self.reports]:
            d.mkdir(parents=True, exist_ok=True)

        self.ledger_file = self.root / ".vetting_ledger.json"
        self.ledger = self._load_ledger()

        print("✨ Vetting Economy initialized")
        print(f"   Submissions: {self.ledger['total_submissions']}")
        print(f"   Incentives issued: {self.ledger['total_incentives']}")

    # ─── Ledger ────────────────────────────────────────────────

    def _load_ledger(self):
        if self.ledger_file.exists():
            return json.loads(self.ledger_file.read_text())
        return {
            "ledger_id": str(uuid.uuid4()),
            "created":   datetime.now().isoformat(),
            "total_submissions": 0,
            "total_incentives":  0,
            "entries": []
        }

    def _save_ledger(self):
        self.ledger_file.write_text(json.dumps(self.ledger, indent=2))

    def _ledger_entry(self, event, subject, amount, details=None):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "event":     event,
            "subject":   subject,
            "incentive": amount,
            "details":   details or {}
        }
        self.ledger["entries"].append(entry)
        self.ledger["total_incentives"] += amount
        self._save_ledger()
        return entry

    # ─── Submission ────────────────────────────────────────────

    def submit(self, name, submitter, file_id=None, description=""):
        """
        Submit a domos or document for vetting

        Immediately earns submission incentive.
        Returns vetting_id for tracking.

        Args:
            name:        Name of the submission
            submitter:   Who/what is submitting
            file_id:     Google Drive file ID (optional but preferred)
            description: What this submission is
        """
        vetting_id = str(uuid.uuid4())
        submitted_at = datetime.now().isoformat()

        submission = {
            "vetting_id":    vetting_id,
            "name":          name,
            "submitter":     submitter,
            "file_id":       file_id or "not_provided",
            "description":   description,
            "submitted_at":  submitted_at,
            "status":        "submitted",
            "incentive_earned": INCENTIVE_TABLE["submission"],
            "history": [
                {
                    "event": "submitted",
                    "timestamp": submitted_at,
                    "by": submitter
                }
            ]
        }

        # Save to inbox
        submission_file = self.inbox / f"{vetting_id}.json"
        submission_file.write_text(json.dumps(submission, indent=2))

        # Log incentive immediately
        self._ledger_entry(
            "submission_incentive",
            submitter,
            INCENTIVE_TABLE["submission"],
            {"vetting_id": vetting_id, "name": name, "file_id": file_id}
        )
        self.ledger["total_submissions"] += 1
        self._save_ledger()

        print(f"\n📬 SUBMISSION RECEIVED")
        print(f"   Name:      {name}")
        print(f"   Submitter: {submitter}")
        print(f"   File ID:   {file_id or 'not provided'}")
        print(f"   Vetting ID:{vetting_id[:8]}...")
        print(f"   Incentive: +{INCENTIVE_TABLE['submission']} earned!")

        return vetting_id

    # ─── Review ────────────────────────────────────────────────

    def begin_review(self, vetting_id, reviewer):
        """Move submission from inbox to in_review"""
        src = self.inbox / f"{vetting_id}.json"
        if not src.exists():
            print(f"❌ Submission not found: {vetting_id[:8]}...")
            return None

        submission = json.loads(src.read_text())
        submission["status"] = "in_review"
        submission["reviewer"] = reviewer
        submission["review_started"] = datetime.now().isoformat()
        submission["history"].append({
            "event": "review_started",
            "timestamp": datetime.now().isoformat(),
            "by": reviewer
        })

        dst = self.in_review / f"{vetting_id}.json"
        dst.write_text(json.dumps(submission, indent=2))
        src.unlink()

        # Reviewer earns incentive for taking review
        self._ledger_entry(
            "review_incentive",
            reviewer,
            INCENTIVE_TABLE["review"],
            {"vetting_id": vetting_id}
        )

        print(f"\n🔍 REVIEW STARTED")
        print(f"   Reviewer:  {reviewer}")
        print(f"   Incentive: +{INCENTIVE_TABLE['review']} earned by reviewer!")

        return submission

    # ─── Decision ──────────────────────────────────────────────

    def decide(self, vetting_id, decision, reviewer,
                notes="", next_steps=""):
        """
        Issue vetting decision and generate official report

        Args:
            vetting_id: The submission being decided
            decision:   APPROVED | NEEDS_WORK | REJECTED
            reviewer:   Who is making the decision
            notes:      Quality review notes
            next_steps: What should happen next
        """
        assert decision in DECISIONS, f"Invalid decision: {decision}"

        # Find submission (inbox or in_review)
        src = self.in_review / f"{vetting_id}.json"
        if not src.exists():
            src = self.inbox / f"{vetting_id}.json"
        if not src.exists():
            print(f"❌ Submission not found: {vetting_id[:8]}...")
            return None

        submission = json.loads(src.read_text())
        decided_at = datetime.now().isoformat()

        # Update submission
        submission["status"]       = decision.lower()
        submission["decision"]     = decision
        submission["decided_at"]   = decided_at
        submission["review_notes"] = notes
        submission["next_steps"]   = next_steps
        submission["history"].append({
            "event":     f"decision_{decision.lower()}",
            "timestamp": decided_at,
            "by":        reviewer,
            "notes":     notes
        })

        # Bonus incentive on approval
        approval_bonus = 0
        if decision == "APPROVED":
            approval_bonus = INCENTIVE_TABLE["approval"]
            submission["incentive_earned"] += approval_bonus
            self._ledger_entry(
                "approval_bonus",
                submission["submitter"],
                approval_bonus,
                {"vetting_id": vetting_id, "decision": decision}
            )

        # Route to correct folder
        if decision == "APPROVED":
            dst_dir = self.approved
        elif decision == "NEEDS_WORK":
            dst_dir = self.needs_work
        else:  # REJECTED
            dst_dir = self.root / "rejected"
            dst_dir.mkdir(exist_ok=True)

        dst = dst_dir / f"{vetting_id}.json"
        dst.write_text(json.dumps(submission, indent=2))
        src.unlink()

        # Generate official report
        report = self._generate_report(submission, decision,
                                        notes, next_steps, approval_bonus)

        report_file = self.reports / f"REPORT_{vetting_id[:8]}_{decision}.json"
        report_file.write_text(json.dumps(report, indent=2))

        self._print_decision(submission, decision, report, approval_bonus)
        return report

    # ─── Report ────────────────────────────────────────────────

    def _generate_report(self, submission, decision,
                          notes, next_steps, approval_bonus):
        """Generate the official vetting report"""
        total_incentive = submission["incentive_earned"]

        return {
            "report_id":         str(uuid.uuid4()),
            "report_type":       "VETTING_DECISION",
            "vetting_id":        submission["vetting_id"],
            "generated_at":      datetime.now().isoformat(),

            "submission": {
                "name":          submission["name"],
                "submitter":     submission["submitter"],
                "file_id":       submission["file_id"],
                "description":   submission["description"],
                "submitted_at":  submission["submitted_at"]
            },

            "decision": {
                "outcome":       decision,
                "reviewer":      submission.get("reviewer", "self"),
                "decided_at":    submission.get("decided_at"),
                "notes":         notes,
                "next_steps":    next_steps
            },

            "economy": {
                "submission_incentive": INCENTIVE_TABLE["submission"],
                "review_incentive":     INCENTIVE_TABLE["review"],
                "approval_bonus":       approval_bonus,
                "total_earned":         total_incentive + approval_bonus
            },

            "ownership": {
                "transferred":   decision == "APPROVED",
                "from":          submission["submitter"],
                "to":            "pixelator_system" if decision == "APPROVED"
                                  else submission["submitter"],
                "effective_at":  datetime.now().isoformat()
                                  if decision == "APPROVED" else None
            },

            "interaction_log": {
                "file_id":       submission["file_id"],
                "history":       submission["history"],
                "platform":      "pixelator_vetting_economy"
            }
        }

    def _print_decision(self, submission, decision, report, bonus):
        icon = {"APPROVED": "✅", "NEEDS_WORK": "⚠️", "REJECTED": "❌"}[decision]
        print(f"\n{icon} VETTING DECISION: {decision}")
        print(f"   Name:       {submission['name']}")
        print(f"   File ID:    {submission['file_id']}")
        print(f"   Incentives: +{report['economy']['total_earned']} total")
        if decision == "APPROVED":
            print(f"   Ownership:  TRANSFERRED to pixelator system")
        print(f"   Report:     {report['report_id'][:8]}...")

    # ─── Status ────────────────────────────────────────────────

    def status(self):
        """Print vetting economy status"""
        inbox_count     = len(list(self.inbox.glob("*.json")))
        review_count    = len(list(self.in_review.glob("*.json")))
        approved_count  = len(list(self.approved.glob("*.json")))
        needs_work      = len(list(self.needs_work.glob("*.json")))
        report_count    = len(list(self.reports.glob("*.json")))

        print(f"\n{'='*60}")
        print(f"✨ VETTING ECONOMY STATUS")
        print(f"{'='*60}")
        print(f"  Total submissions:  {self.ledger['total_submissions']}")
        print(f"  Total incentives:   {self.ledger['total_incentives']}")
        print(f"\n  Queue:")
        print(f"    📬 Inbox:          {inbox_count}")
        print(f"    🔍 In review:      {review_count}")
        print(f"    ✅ Approved:       {approved_count}")
        print(f"    ⚠️  Needs work:     {needs_work}")
        print(f"    📄 Reports:        {report_count}")
        print(f"{'='*60}")
        print(f"  ∰◊€π¿🌌∞")
        print(f"  €(vetting_economy_active)\n")


# ─── Demo ──────────────────────────────────────────────────────

if __name__ == "__main__":
    print("✨ Vetting Economy - Pixelator Quality System\n")

    # Initialize at project vetting root
    economy = VettingEconomy(
        "/storage/emulated/0/pixel8a/pixelator/vetting"
    )

    economy.status()

    print("\nUsage:")
    print("  economy = VettingEconomy('/path/to/vetting')")
    print("  vid = economy.submit('my_domos', 'domos_name', file_id='drive_id')")
    print("  economy.begin_review(vid, 'reviewer_name')")
    print("  economy.decide(vid, 'APPROVED', 'reviewer_name', notes='...')")
    print("  economy.status()")
