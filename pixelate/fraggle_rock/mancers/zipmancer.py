"""
ZIPMANCER
=========
Class   : ZipMancer (MancerBase subclass)
Domain  : Zip archive reading, inventory, and chain-of-custody intake
Role    : Reads zip archives → generates manifest → hands to Henry/Fraggle
Nature  : Fluid in liminal — solidifies when an archive is presented

Born from: The Telegard exploration, 202603260000.
  The Telegard archive arrived as zips. We needed to read them.
  ZipMancer is the entity that was missing.
  Zips store. Zaps transfer. ZipMancer bridges the cold and the live.

"A zip is a promise. ZipMancer keeps the inventory."

DOCUMENT INTAKE (Move, Not Copy):
  When documents enter chain of custody, they MOVE — they don't copy.
  ZipMancer records the move in CoC so nothing is lost and nothing is forgotten.
  Every file that enters through ZipMancer has a provenance record.

Usage:
  from zipmancer import ZipMancer
  zm = ZipMancer("zipmancer_01")
  report = zm.run("/path/to/archive.zip")
  # or intake a directory of zips:
  reports = zm.intake_directory("/path/to/inbox/", move_to="/path/to/processed/")

∰◊€π¿🌌∞
€(zipmancer_v1)
"""

import os
import sys
import json
import zipfile
import hashlib
import shutil
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mancer_base import MancerBase, MancerState, now_stamp


# ─── Data Structures ─────────────────────────────────────────────────────────

@dataclass
class ZipEntry:
    """One file inside a zip archive."""
    filename:     str
    size:         int          # uncompressed bytes
    compressed:   int          # compressed bytes
    ratio:        float        # compression ratio
    date_time:    Optional[str]
    is_dir:       bool
    crc:          int          # CRC32 from zip header
    extension:    str

    @property
    def size_kb(self) -> float:
        return round(self.size / 1024, 1)

    @property
    def size_mb(self) -> float:
        return round(self.size / (1024 * 1024), 2)


@dataclass
class ZipManifest:
    """
    Full inventory of one zip archive.
    This is the Henry Report for archives —
    structured handoff for Fraggle/Henry to act on.
    """
    zip_path:       str
    zip_name:       str
    zip_size:       int          # zip file size in bytes
    zip_sha256:     str          # sha256 of the zip file itself
    total_entries:  int
    total_files:    int
    total_dirs:     int
    uncompressed:   int          # total uncompressed bytes
    timestamp:      str
    entries:        List[ZipEntry] = field(default_factory=list)
    coc_entries:    List[dict]     = field(default_factory=list)
    error:          Optional[str]  = None

    # Classification by extension
    by_extension:   Dict[str, List[str]] = field(default_factory=dict)

    @property
    def zip_size_kb(self) -> float:
        return round(self.zip_size / 1024, 1)

    @property
    def uncompressed_mb(self) -> float:
        return round(self.uncompressed / (1024 * 1024), 2)

    @property
    def is_readable(self) -> bool:
        return self.error is None

    def extensions_summary(self) -> Dict[str, int]:
        return {ext: len(files) for ext, files in self.by_extension.items()}

    def files_by_ext(self, ext: str) -> List[str]:
        ext = ext.lower().lstrip(".")
        return self.by_extension.get(ext, [])

    def to_dict(self) -> dict:
        return {
            "zip_path":      self.zip_path,
            "zip_name":      self.zip_name,
            "zip_size_kb":   self.zip_size_kb,
            "zip_sha256":    self.zip_sha256,
            "total_files":   self.total_files,
            "total_dirs":    self.total_dirs,
            "uncompressed_mb": self.uncompressed_mb,
            "timestamp":     self.timestamp,
            "extensions":    self.extensions_summary(),
            "error":         self.error,
        }

    def to_markdown(self) -> str:
        lines = [
            f"# ZipManifest — {self.zip_name}",
            f"",
            f"| Field | Value |",
            f"|-------|-------|",
            f"| Path  | `{self.zip_path}` |",
            f"| Size  | {self.zip_size_kb} KB |",
            f"| SHA256 | `{self.zip_sha256[:16]}...` |",
            f"| Files | {self.total_files} |",
            f"| Dirs  | {self.total_dirs} |",
            f"| Uncompressed | {self.uncompressed_mb} MB |",
            f"| Scanned | {self.timestamp} |",
            f"",
        ]

        if self.error:
            lines += [f"**ERROR**: {self.error}", ""]
            return "\n".join(lines)

        # Extensions
        lines += ["## Contents by Type", ""]
        for ext, names in sorted(self.by_extension.items()):
            lines.append(f"**{ext or 'no-ext'}** ({len(names)})")
            for n in names[:10]:
                lines.append(f"  - `{n}`")
            if len(names) > 10:
                lines.append(f"  - *...and {len(names)-10} more*")
            lines.append("")

        # CoC
        if self.coc_entries:
            lines += ["## Chain of Custody", ""]
            for e in self.coc_entries:
                lines.append(f"- `{e['ts']}` **{e['action']}** — {e['note']}")

        return "\n".join(lines)


# ─── ZipMancer Entity ────────────────────────────────────────────────────────

class ZipMancer(MancerBase):
    """
    ZipMancer — reads zip archives, generates manifests, manages intake.

    Ancestry: Born from the Telegard archive exploration (202603260000).
    The BBS distributed software as zips. Every door game, every utility,
    every developer kit arrived compressed. Someone had to read them.
    ZipMancer is that someone.

    ZIP → cold storage (the promise, compressed, waiting)
    ZAP → transfer protocol (DirectZAP, ZedZap — from TELEGARD.H)
    ZipMancer → bridges cold to live, archive to chain of custody
    """

    ENTITY_CLASS = "ZipMancer"
    NO_PERSONAL_CREDIT = True   # work belongs to the mission

    def __init__(self, name: str = "zipmancer_01"):
        super().__init__(name=name, domain="zip_archive_intake")
        self.manifests: List[ZipManifest] = []

    # ─── Core Analysis ───────────────────────────────────────────────────────

    def analyze(self, target: str) -> ZipManifest:
        """
        Read a zip archive and produce a ZipManifest.
        Target: path to a .zip file.
        """
        zip_path = os.path.abspath(target)
        zip_name = os.path.basename(zip_path)
        ts       = now_stamp()

        manifest = ZipManifest(
            zip_path=zip_path,
            zip_name=zip_name,
            zip_size=0,
            zip_sha256="",
            total_entries=0,
            total_files=0,
            total_dirs=0,
            uncompressed=0,
            timestamp=ts,
        )
        manifest.coc_entries.append({
            "ts": ts, "action": "SCAN_START",
            "note": f"ZipMancer reading {zip_name}"
        })

        # File existence
        if not os.path.exists(zip_path):
            manifest.error = f"File not found: {zip_path}"
            manifest.coc_entries.append({
                "ts": now_stamp(), "action": "ERROR",
                "note": manifest.error
            })
            return manifest

        # File hash
        manifest.zip_size = os.path.getsize(zip_path)
        manifest.zip_sha256 = self._sha256(zip_path)

        # Validate zip
        if not zipfile.is_zipfile(zip_path):
            manifest.error = f"Not a valid zip file: {zip_name}"
            manifest.coc_entries.append({
                "ts": now_stamp(), "action": "ERROR",
                "note": manifest.error
            })
            return manifest

        # Read contents
        try:
            with zipfile.ZipFile(zip_path, "r") as zf:
                for info in zf.infolist():
                    is_dir = info.filename.endswith("/")
                    ext    = os.path.splitext(info.filename)[1].lower().lstrip(".")

                    entry = ZipEntry(
                        filename=info.filename,
                        size=info.file_size,
                        compressed=info.compress_size,
                        ratio=round(
                            (1 - info.compress_size / info.file_size) * 100
                            if info.file_size > 0 else 0, 1
                        ),
                        date_time=str(datetime(*info.date_time)) if info.date_time else None,
                        is_dir=is_dir,
                        crc=info.CRC,
                        extension=ext,
                    )
                    manifest.entries.append(entry)
                    manifest.total_entries += 1

                    if is_dir:
                        manifest.total_dirs += 1
                    else:
                        manifest.total_files += 1
                        manifest.uncompressed += info.file_size
                        # classify by extension
                        if ext not in manifest.by_extension:
                            manifest.by_extension[ext] = []
                        manifest.by_extension[ext].append(info.filename)

        except zipfile.BadZipFile as e:
            manifest.error = f"Bad zip: {e}"
        except Exception as e:
            manifest.error = f"Read error: {e}"

        manifest.coc_entries.append({
            "ts": now_stamp(), "action": "SCAN_COMPLETE",
            "note": (
                f"{manifest.total_files} files, "
                f"{manifest.total_dirs} dirs, "
                f"{manifest.uncompressed_mb}MB uncompressed"
                if not manifest.error else f"FAILED: {manifest.error}"
            )
        })

        self.manifests.append(manifest)
        return manifest

    # ─── Directory Intake ────────────────────────────────────────────────────

    def intake_directory(
        self,
        inbox_path: str,
        move_to: Optional[str] = None,
        write_manifests: bool = True,
        manifest_dir: Optional[str] = None,
    ) -> List[ZipManifest]:
        """
        Read all zip files in a directory.
        Optionally MOVE them to processed folder (chain of custody).
        Optionally write .manifest.json files.

        MOVE not copy: documents enter the chain.
        Once in, they are tracked. They don't disappear back to inbox.
        """
        inbox_path = os.path.abspath(inbox_path)
        if not os.path.isdir(inbox_path):
            raise ValueError(f"Not a directory: {inbox_path}")

        # Find all zips
        zip_files = [
            os.path.join(inbox_path, f)
            for f in sorted(os.listdir(inbox_path))
            if f.lower().endswith(".zip")
        ]

        self._log_coc(
            "INTAKE_START",
            f"{len(zip_files)} zips in {inbox_path}"
        )

        results = []
        for zip_path in zip_files:
            manifest = self.run(zip_path, mission_label=f"read:{os.path.basename(zip_path)}")
            results.append(manifest)

            # Write manifest file
            if write_manifests:
                mdir = manifest_dir or inbox_path
                os.makedirs(mdir, exist_ok=True)
                mpath = os.path.join(mdir, manifest.zip_name + ".manifest.json")
                with open(mpath, "w") as f:
                    json.dump(manifest.to_dict(), f, indent=2)
                manifest.coc_entries.append({
                    "ts": now_stamp(), "action": "MANIFEST_WRITTEN",
                    "note": mpath
                })

            # Move zip (not copy)
            if move_to and manifest.is_readable:
                os.makedirs(move_to, exist_ok=True)
                dest = os.path.join(move_to, manifest.zip_name)
                shutil.move(zip_path, dest)
                manifest.coc_entries.append({
                    "ts": now_stamp(), "action": "MOVED",
                    "note": f"{zip_path} → {dest}"
                })
                manifest.zip_path = dest   # update path in record

        self._log_coc(
            "INTAKE_COMPLETE",
            f"{len(results)} archives processed"
        )
        return results

    # ─── Utilities ───────────────────────────────────────────────────────────

    @staticmethod
    def _sha256(path: str) -> str:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()

    def summary(self) -> str:
        """Text summary of all manifests processed this session."""
        if not self.manifests:
            return "ZipMancer: no archives read yet."
        lines = [f"ZipMancer {self.name} — {len(self.manifests)} archives"]
        for m in self.manifests:
            status = "✓" if m.is_readable else "✗"
            lines.append(
                f"  {status} {m.zip_name:<30} "
                f"{m.total_files:4d} files  "
                f"{m.uncompressed_mb:6.1f}MB"
            )
        return "\n".join(lines)


# ─── Smoke Test ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    zm = ZipMancer("zipmancer_01")
    print(f"ZipMancer born: {zm.name} | state: {zm.state}")
    print(f"NO_PERSONAL_CREDIT: {zm.NO_PERSONAL_CREDIT}")
    print()

    # If path provided, scan it
    if len(sys.argv) > 1:
        target = sys.argv[1]

        if os.path.isdir(target):
            print(f"Scanning directory: {target}")
            manifests = zm.intake_directory(target, write_manifests=True)
            print()
            print(zm.summary())
            print()
            for m in manifests:
                if m.is_readable:
                    print(f"─── {m.zip_name} ───")
                    for ext, count in sorted(m.extensions_summary().items()):
                        print(f"  .{ext or '(none)'}: {count}")
                    print()

        elif os.path.isfile(target):
            print(f"Scanning archive: {target}")
            manifest = zm.run(target)
            print()
            print(manifest.to_markdown())

        else:
            print(f"Not found: {target}")

    else:
        # Demo with a temp zip if no arg given
        import tempfile

        print("Demo mode (no path given) — creating test zip...")
        with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
            tmp_path = tmp.name

        with zipfile.ZipFile(tmp_path, "w") as zf:
            zf.writestr("README.md",   "# Test Archive\nZipMancer demo.")
            zf.writestr("models.py",   "# Python models")
            zf.writestr("LINEAGE.md",  "# Lineage document")
            zf.writestr("data/record.json", '{"entity": "test"}')
            zf.writestr("docs/",       "")   # directory entry

        manifest = zm.run(tmp_path)
        os.unlink(tmp_path)

        print(manifest.to_markdown())
        print()
        print("CoC:")
        for e in manifest.coc_entries:
            print(f"  [{e['ts']}] {e['action']} — {e['note']}")

    print()
    print("∞ ZipMancer: READY")
