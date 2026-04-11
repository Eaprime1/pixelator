# quantum_grove.py


import json
import time
from typing import Any, Dict, List, optional
from runic_engine import RunicMatrix

class QuantumGrove:
    def __init__(self, state_path: str = "quantum_grove/grove_state.json", runic_matrix: Optional[RunicMatrix] = None):
        self.state_path = state_path
        self.state: Dict[str, Any] = {"roots": [], "branches": {}, "leaves": []}
        self.rm = runic_matrix
        self._load_state()

    def _now(self) -> float:
        return time.time()

    def _load_state(self):
        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                self.state = json.load(f)
        except FileNotFoundError:
            self._save_state()

    def _save_state(self):
        import os
        os.makedirs(self.state_path.rsplit("/", 1)[0], exist_ok=True)
        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2)

    def bind_rune(self, runic_symbol: str, context: str):
        entry = {"rune": runic_symbol, "context": context, "time": self._now()}
        self.state["roots"].append(entry)
        self._save_state()
        return entry

    def grow(self, input_signal: str) -> Dict[str, Any]:
        # input_signal: raw text or runic code
        if self.rm:
            encoded = self.rm.encode_text(input_signal)
            score = self.rm.resonance_score(encoded)
            mods = self.rm.influence_modifiers(encoded)
        else:
            encoded = input_signal
            score = len(input_signal)
            mods = {}
        branch_id = f"b_{int(self._now()*1000)}"
        branch = {"id": branch_id, "encoded": encoded, "score": score, "mods": mods, "time": self._now()}
        self.state["branches"][branch_id] = branch
        self.state["leaves"].append({"branch": branch_id, "time": self._now()})
        self._save_state()
        return branch

    def query_branches(self) -> List[str]:
        return list(self.state["branches"].keys())
