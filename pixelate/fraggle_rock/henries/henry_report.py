"""
Henry Report Generator
Produces structured markdown reports and CoC-compatible summaries.
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict

from henry_classes import Issue


@dataclass
class HenryReport:
    """Complete scan report produced by a Henry entity"""
    entity_name   : str
    target_path   : str
    timestamp     : str
    issues        : List[Issue]  = field(default_factory=list)
    files_scanned : int          = 0
    files_skipped : int          = 0
    coc_entries   : List[dict]   = field(default_factory=list)

    def add_issue(self, issue: Issue):
        self.issues.append(issue)

    def summary(self) -> Dict:
        by_class    = {}
        by_severity = {"INFO": 0, "WARN": 0, "ERROR": 0}
        auto_count  = 0
        for issue in self.issues:
            by_class[issue.issue_class] = by_class.get(issue.issue_class, 0) + 1
            by_severity[issue.severity] = by_severity.get(issue.severity, 0) + 1
            if issue.auto_fixable:
                auto_count += 1
        return {
            "total_issues" : len(self.issues),
            "files_scanned": self.files_scanned,
            "files_skipped": self.files_skipped,
            "by_class"     : by_class,
            "by_severity"  : by_severity,
            "auto_fixable" : auto_count,
        }

    def to_markdown(self) -> str:
        s     = self.summary()
        names = {
            "A": "Whitespace",
            "B": "Symbols/Filenames",
            "C": "Titles",
            "D": "Git-Specific",
            "E": "Structural",
        }

        lines = [
            f"# Henry Report — {self.entity_name}",
            f"**Target**    : `{self.target_path}`",
            f"**Timestamp** : {self.timestamp}",
            f"**Scanned**   : {s['files_scanned']} files | **Skipped**: {s['files_skipped']}",
            "",
            "## Summary",
            "| Metric | Count |",
            "|--------|-------|",
            f"| Total Issues | **{s['total_issues']}** |",
            f"| ERROR        | {s['by_severity']['ERROR']} |",
            f"| WARN         | {s['by_severity']['WARN']} |",
            f"| INFO         | {s['by_severity']['INFO']} |",
            f"| Auto-fixable | {s['auto_fixable']} |",
            "",
        ]

        if s["by_class"]:
            lines.append("## Issues by Class")
            for cls in sorted(s["by_class"]):
                lines.append(f"- **CLASS {cls}** ({names.get(cls, '')}): {s['by_class'][cls]}")
            lines.append("")

        lines.append("## Detailed Findings")
        if not self.issues:
            lines.append("*No issues found. Clean.*")
        else:
            by_class = {}
            for issue in self.issues:
                by_class.setdefault(issue.issue_class, []).append(issue)

            for cls in sorted(by_class):
                lines.append(f"### CLASS {cls} — {names.get(cls, '')}")
                for issue in by_class[cls]:
                    fixable  = " `✓fix`" if issue.auto_fixable else ""
                    line_ref = f"L{issue.line_number}" if issue.line_number else "file"
                    lines.append(
                        f"- `[{issue.severity}]` **{issue.issue_type}**  "
                        f"`{issue.filepath}:{line_ref}`{fixable}"
                    )
                    lines.append(f"  ↳ {issue.detail}")
                lines.append("")

        lines += [
            "---",
            "∰◊€π¿🌌∞",
            f"€(henry_report_{self.timestamp})",
            f"*Entity*: {self.entity_name}",
            f"*Status*: REPORT_COMPLETE",
        ]
        return "\n".join(lines)

    def to_coc_entry(self) -> dict:
        s = self.summary()
        return {
            "timestamp"    : self.timestamp,
            "entity"       : self.entity_name,
            "action"       : "SCAN_COMPLETE",
            "target"       : self.target_path,
            "files_scanned": s["files_scanned"],
            "total_issues" : s["total_issues"],
            "by_class"     : s["by_class"],
            "by_severity"  : s["by_severity"],
        }
