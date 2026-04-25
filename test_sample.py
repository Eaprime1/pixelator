"""
Tests for pixelator_agent.py

Covers: route_file, log_entry, process_item (dry-run, move, collision),
        append_custody_log (write, accumulate).

Config is mocked so tests run off-device without Pixel 8a paths.
"""

import json
import os
import sys
from unittest.mock import MagicMock

# ── Mock config before agent import (agent imports cfg at module level) ───────
_mock_cfg = MagicMock()
_mock_cfg.ROUTING_RULES = [
    {"pattern": "approved_",     "dest": "/dest/pixelate",     "label": "pre-approved"},
    {"pattern": "entity",        "dest": "/dest/hodie/quanta", "label": "entity"},
    {"pattern": "consciousness", "dest": "/dest/hodie/quanta", "label": "entity"},
    {"pattern": "codex",         "dest": "/dest/codex",        "label": "codex"},
    {"pattern": "prime",         "dest": "/dest/prime",        "label": "prime"},
    {"pattern": "conversation",  "dest": "/dest/visionhaven",  "label": "seed"},
    {"pattern": "seed",          "dest": "/dest/visionhaven",  "label": "seed"},
    {"pattern": ".py",           "dest": "/dest/ai-projects",  "label": "script"},
    {"pattern": ".md",           "dest": "/dest/pixelating",   "label": "doc"},
    {"pattern": "*",             "dest": "/dest/pixelating",   "label": "unsorted"},
]
_mock_cfg.PIXELATING_DIR     = "/dest/pixelating"
_mock_cfg.CHAIN_OF_CUSTODY   = True
_mock_cfg.SKIP_HIDDEN        = True
_mock_cfg.COPY_NOT_MOVE      = False
_mock_cfg.DRY_RUN            = False
_mock_cfg.MAX_PER_RUN        = 10
_mock_cfg.PRESSURE_THRESHOLD = 50
_mock_cfg.LOG_FILE           = "/tmp/pixelator_test_log.json"
_mock_cfg.QUEUE_MANIFEST     = "/tmp/pixelator_test_queue.json"

sys.modules["pixelator_config"] = _mock_cfg

import pixelator_agent as agent  # noqa: E402


# ── route_file ────────────────────────────────────────────────────────────────

def test_route_file_entity():
    dest, label = agent.route_file("entity_awareness.txt")
    assert label == "entity"
    assert dest == "/dest/hodie/quanta"


def test_route_file_codex():
    dest, label = agent.route_file("codex_main.json")
    assert label == "codex"
    assert dest == "/dest/codex"


def test_route_file_prime():
    dest, label = agent.route_file("prime_directive.txt")
    assert label == "prime"
    assert dest == "/dest/prime"


def test_route_file_seed():
    dest, label = agent.route_file("seed_concept.txt")
    assert label == "seed"
    assert dest == "/dest/visionhaven"


def test_route_file_python_script():
    dest, label = agent.route_file("my_script.py")
    assert label == "script"
    assert dest == "/dest/ai-projects"


def test_route_file_markdown():
    dest, label = agent.route_file("notes.md")
    assert label == "doc"
    assert dest == "/dest/pixelating"


def test_route_file_approved_prefix():
    dest, label = agent.route_file("approved_draft.md")
    assert label == "pre-approved"
    assert dest == "/dest/pixelate"


def test_route_file_catch_all():
    dest, label = agent.route_file("random_image.jpg")
    assert label == "unsorted"
    assert dest == "/dest/pixelating"


def test_route_file_case_insensitive():
    dest, label = agent.route_file("ENTITY_RECORD.txt")
    assert label == "entity"


def test_route_file_first_match_wins():
    # 'approved_entity.txt' matches 'approved_' before 'entity'
    dest, label = agent.route_file("approved_entity.txt")
    assert label == "pre-approved"


# ── log_entry ─────────────────────────────────────────────────────────────────

def test_log_entry_has_required_fields():
    entry = agent.log_entry("MOVE", "/src/file.txt", "/dest/file.txt", "script", "SUCCESS", note="ok")
    assert entry["action"] == "MOVE"
    assert entry["source"] == "/src/file.txt"
    assert entry["destination"] == "/dest/file.txt"
    assert entry["label"] == "script"
    assert entry["status"] == "SUCCESS"
    assert entry["note"] == "ok"
    assert entry["agent"] == agent.AGENT_SIGNATURE
    assert "timestamp" in entry


def test_log_entry_agent_signature_present():
    entry = agent.log_entry("COPY", "/s", "/d", "seed", "SUCCESS")
    assert "pixelator_agent" in entry["agent"]
    assert "PIXEL8" in entry["agent"]


# ── process_item: dry run ─────────────────────────────────────────────────────

def test_process_item_dry_run_returns_simulated(tmp_path):
    src = tmp_path / "file.txt"
    src.write_text("content")

    item = {
        "source": str(src),
        "dest": str(tmp_path / "dest"),
        "label": "unsorted",
        "filename": "file.txt",
    }
    entry = agent.process_item(item, dry_run=True, copy_mode=False)

    assert entry["status"] == "SIMULATED"
    assert entry["action"] == "DRY_RUN"
    assert entry["label"] == "unsorted"
    assert src.exists(), "Dry run must not move the source file"


# ── process_item: live move ───────────────────────────────────────────────────

def test_process_item_moves_file_to_destination(tmp_path):
    src_dir = tmp_path / "source"
    src_dir.mkdir()
    src_file = src_dir / "note.md"
    src_file.write_text("hello")

    dest_dir = tmp_path / "dest"

    item = {
        "source": str(src_file),
        "dest": str(dest_dir),
        "label": "doc",
        "filename": "note.md",
    }
    entry = agent.process_item(item, dry_run=False, copy_mode=False)

    assert entry["status"] == "SUCCESS"
    assert entry["action"] == "MOVE"
    assert not src_file.exists()
    assert (dest_dir / "note.md").exists()


def test_process_item_copy_leaves_source_intact(tmp_path):
    src_dir = tmp_path / "source"
    src_dir.mkdir()
    src_file = src_dir / "note.md"
    src_file.write_text("hello")

    dest_dir = tmp_path / "dest"

    item = {
        "source": str(src_file),
        "dest": str(dest_dir),
        "label": "doc",
        "filename": "note.md",
    }
    entry = agent.process_item(item, dry_run=False, copy_mode=True)

    assert entry["status"] == "SUCCESS"
    assert entry["action"] == "COPY"
    assert src_file.exists(), "Copy mode must leave source intact"
    assert (dest_dir / "note.md").exists()


# ── process_item: collision handling ─────────────────────────────────────────

def test_process_item_collision_adds_timestamp_suffix(tmp_path):
    dest_dir = tmp_path / "dest"
    dest_dir.mkdir()
    (dest_dir / "file.txt").write_text("existing")

    src_dir = tmp_path / "source"
    src_dir.mkdir()
    src_file = src_dir / "file.txt"
    src_file.write_text("new content")

    item = {
        "source": str(src_file),
        "dest": str(dest_dir),
        "label": "doc",
        "filename": "file.txt",
    }
    entry = agent.process_item(item, dry_run=False, copy_mode=False)

    assert entry["status"] == "SUCCESS"
    dest_name = os.path.basename(entry["destination"])
    assert dest_name != "file.txt", "Collision should produce a renamed file"
    assert dest_name.startswith("file_"), "Renamed file should retain original stem"
    assert (dest_dir / "file.txt").read_text() == "existing", "Original must be untouched"


# ── append_custody_log ────────────────────────────────────────────────────────

def test_append_custody_log_creates_valid_json(tmp_path):
    log_path = tmp_path / "custody.json"
    _mock_cfg.LOG_FILE = str(log_path)

    entries = [agent.log_entry("MOVE", "/src/a.md", "/dest/a.md", "doc", "SUCCESS")]
    agent.append_custody_log(entries)

    assert log_path.exists()
    data = json.loads(log_path.read_text())
    assert len(data["entries"]) == 1
    assert data["entries"][0]["action"] == "MOVE"
    assert data["total_operations"] == 1
    assert "last_run" in data
    assert "agent" in data["entries"][0]


def test_append_custody_log_accumulates_across_runs(tmp_path):
    log_path = tmp_path / "custody.json"
    _mock_cfg.LOG_FILE = str(log_path)

    first  = [agent.log_entry("MOVE", "/src/a.txt", "/dest/a.txt", "doc",  "SUCCESS")]
    second = [agent.log_entry("COPY", "/src/b.txt", "/dest/b.txt", "seed", "SUCCESS")]

    agent.append_custody_log(first)
    agent.append_custody_log(second)

    data = json.loads(log_path.read_text())
    assert data["total_operations"] == 2
    actions = {e["action"] for e in data["entries"]}
    assert actions == {"MOVE", "COPY"}


def test_append_custody_log_skipped_when_disabled(tmp_path):
    log_path = tmp_path / "custody.json"
    _mock_cfg.LOG_FILE = str(log_path)
    _mock_cfg.CHAIN_OF_CUSTODY = False

    entries = [agent.log_entry("MOVE", "/src/a.md", "/dest/a.md", "doc", "SUCCESS")]
    agent.append_custody_log(entries)

    assert not log_path.exists(), "No log should be written when custody logging is off"

    _mock_cfg.CHAIN_OF_CUSTODY = True  # restore
