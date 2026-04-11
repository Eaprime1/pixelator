# runic_engine.py
from dataclasses import dataclass
from typing import Dict, Optional, List
import json
import math

@dataclass
class Rune:
    symbol: str
    meaning: str
    frequency: float
    element: str
    ethics: str
    functional: Dict[str, float]  # numeric modifiers: e.g., {"growth": 0.1}

class RunicMatrix:
    def __init__(self):
        self.runes: Dict[str, Rune] = {}

    def load_from_json(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for sym, meta in data.items():
            rune = Rune(
                symbol=sym,
                meaning=meta.get("meaning", ""),
                frequency=float(meta.get("freq", 0.0)),
                element=meta.get("element", "spirit"),
                ethics=meta.get("ethics", "neutral"),
                functional=meta.get("functional", {})
            )
            self.runes[sym] = rune

    def add_rune(self, rune: Rune):
        self.runes[rune.symbol] = rune

    def encode_text(self, text: str) -> str:
        # naive mapping: characters -> runes by hash (improvable)
        out = []
        keys = list(self.runes.keys())
        if not keys:
            return ""
        for ch in text:
            idx = (ord(ch) + len(text)) % len(keys)
            out.append(keys[idx])
        return "".join(out)

    def resonance_score(self, runic_string: str) -> float:
        return sum(self.runes[r].frequency for r in runic_string if r in self.runes)

    def influence_modifiers(self, runic_string: str) -> Dict[str, float]:
        agg = {}
        for r in runic_string:
            rune = self.runes.get(r)
            if not rune:
                continue
            for k, v in rune.functional.items():
                agg[k] = agg.get(k, 0.0) + float(v)
        return agg

# Example usage
if __name__ == "__main__":
    rm = RunicMatrix()
    # load a runic JSON file, e.g. runes_v2.json
    try:
        rm.load_from_json("config/runes_v2.json")
        enc = rm.encode_text("hello world")
        print("Encoded:", enc)
        print("Resonance:", rm.resonance_score(enc))
    except FileNotFoundError:
        print("Place runes_v2.json in config/ to enable demonstration.")
