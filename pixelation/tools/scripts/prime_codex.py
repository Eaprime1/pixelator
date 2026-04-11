# prime_codex.py
from runic_engine import RunicMatrix
from quantum_grove import QuantumGrove
from compression_nexus import QuantumCompressionNexus
import json

class PrimeCodex:
    def __init__(self, runes_json="config/runes_v2.json", grove_state="quantum_grove/grove_state.json"):
        self.runic = RunicMatrix()
        try:
            self.runic.load_from_json(runes_json)
        except:
            pass
        self.grove = QuantumGrove(state_path=grove_state, runic_matrix=self.runic)
        self.nexus = QuantumCompressionNexus()

    def process_signal(self, signal: str) -> dict:
        branch = self.grove.grow(signal)
        # signature uses the highest-frequency rune in encoded string:
        encoded = branch["encoded"]
        sig = encoded[:6] if isinstance(encoded, str) else ""
        crystal = self.nexus.compress(branch["encoded"].encode("utf-8") if isinstance(branch["encoded"], str) else branch["encoded"], signature=sig)
        return {"branch": branch, "crystal_size": len(crystal)}

    def save_codex_snapshot(self, path="prime_codex_snapshot.json"):
        import os
        snapshot = {
            "roots": self.grove.state.get("roots", []),
            "branches": self.grove.state.get("branches", {}),
            "runes_loaded": list(self.runic.runes.keys())
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snapshot, f, indent=2)
