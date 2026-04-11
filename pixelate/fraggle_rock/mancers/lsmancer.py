"""
lsmancer — List/Structure Mancer
Domain  : Directory and file structure analysis
State   : Fluid in liminal — solid while reading

Already exists in platform as bash alias 'lsmancer'.
This is the formalized Python entity.

Usage:
    python3 lsmancer.py /path/to/target
"""

import os
import sys

from mancer_base import MancerBase, now_stamp


class LsMancer(MancerBase):
    """
    lsmancer — reads and reports directory structure.
    Produces tree view with git repo markers and file counts.
    Read-only. Conservation bias.
    """

    def __init__(self, max_depth: int = 4, show_hidden: bool = False):
        super().__init__(name="lsmancer", domain="directory_structure")
        self.max_depth   = max_depth
        self.show_hidden = show_hidden

    def analyze(self, target: str) -> dict:
        """Walk target directory up to max_depth. Returns structure dict."""
        target = os.path.abspath(target)
        self._log_coc("ANALYZE", f"Reading: {target} (depth={self.max_depth})")

        stats  = {"dirs": 0, "files": 0, "git_repos": 0, "total_size_bytes": 0}
        tree   = self._walk(target, 0, stats)

        self._log_coc(
            "STRUCTURE_READ",
            f"dirs={stats['dirs']} files={stats['files']} repos={stats['git_repos']}",
        )

        return {
            "timestamp" : now_stamp(),
            "target"    : target,
            "max_depth" : self.max_depth,
            "tree"      : tree,
            "stats"     : stats,
        }

    def _walk(self, path: str, depth: int, stats: dict) -> dict:
        stats["dirs"] += 1
        node = {
            "name"    : os.path.basename(path) or path,
            "type"    : "dir",
            "path"    : path,
            "is_git"  : os.path.isdir(os.path.join(path, ".git")),
            "children": [],
        }
        if node["is_git"]:
            stats["git_repos"] += 1

        if depth >= self.max_depth:
            return node

        try:
            entries = sorted(os.scandir(path), key=lambda e: (e.is_file(), e.name.lower()))
        except PermissionError:
            return node

        for entry in entries:
            if not self.show_hidden and entry.name.startswith("."):
                continue
            if entry.is_dir(follow_symlinks=False):
                node["children"].append(self._walk(entry.path, depth + 1, stats))
            elif entry.is_file(follow_symlinks=False):
                try:
                    size = entry.stat().st_size
                except OSError:
                    size = 0
                stats["files"]            += 1
                stats["total_size_bytes"] += size
                node["children"].append({
                    "name": entry.name,
                    "type": "file",
                    "path": entry.path,
                    "size": size,
                })

        return node

    def to_text(self, result: dict) -> str:
        """Render result as a readable text tree"""
        stats = result["stats"]
        mb    = stats["total_size_bytes"] / (1024 * 1024)
        lines = [
            "lsmancer — Structure Report",
            f"Target    : {result['target']}",
            f"Timestamp : {result['timestamp']}",
            f"Stats     : {stats['dirs']} dirs | {stats['files']} files | "
            f"{stats['git_repos']} git repos | {mb:.2f} MB total",
            "",
        ]
        self._render(result["tree"], lines, 0)
        return "\n".join(lines)

    def _render(self, node: dict, lines: list, indent: int):
        prefix = "  " * indent
        if node["type"] == "dir":
            git = " [git]" if node.get("is_git") else ""
            lines.append(f"{prefix}{node['name']}/{git}")
            for child in node.get("children", []):
                self._render(child, lines, indent + 1)
        else:
            size = node.get("size", 0)
            if size >= 1024 * 1024:
                size_str = f" ({size/(1024*1024):.1f}M)"
            elif size >= 1024:
                size_str = f" ({size/1024:.1f}K)"
            else:
                size_str = f" ({size}B)"
            lines.append(f"{prefix}  {node['name']}{size_str}")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    mancer = LsMancer(max_depth=3)
    result = mancer.run(target, mission_label="directory_scan")
    print(mancer.to_text(result))
