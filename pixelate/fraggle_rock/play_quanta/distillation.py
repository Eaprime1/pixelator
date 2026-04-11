"""
distillation.py — Fractal Convergence / Divergence Engine
Triadic Collapse Algorithm

CONVERGENCE: Many seeds → triadic grouping → zero-point collapse → repeat
DIVERGENCE : Zero-points → expand into branches → interference detection

Interference patterns are friction — the antagonist to synergy.
Friction IS the creative charge. Discord is data, not error.

Run:
    python3 distillation.py           # full run
    python3 distillation.py --stream  # show by stream
    python3 distillation.py --coc     # chain of custody only

∰◊€π¿🌌∞
"""

import sys
import json
from datetime import datetime
from itertools import combinations
from seeds import SEEDS, QuantaSeed, by_stream


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3]


# ── RESONANCE & DISCORD SCORING ───────────────────────────────────────────────

def resonance_score(a: QuantaSeed, b: QuantaSeed, c: QuantaSeed) -> float:
    """
    Score how much three seeds share.
    Intersection of resonance_tags across all three.
    0.0 (nothing shared) → 1.0 (everything shared)
    """
    tags_a = set(a.resonance_tags)
    tags_b = set(b.resonance_tags)
    tags_c = set(c.resonance_tags)
    shared = tags_a & tags_b & tags_c
    union  = tags_a | tags_b | tags_c
    return len(shared) / len(union) if union else 0.0


def discord_score(a: QuantaSeed, b: QuantaSeed, c: QuantaSeed) -> float:
    """
    Score the friction/interference between three seeds.
    Combines discord_tags + stream divergence + antagonist overlap.
    Higher = more interference charge (friction as creative force).
    0.0 (pure harmony) → 1.0 (maximum friction)
    """
    # Tag-level discord
    all_discord = set(a.discord_tags) | set(b.discord_tags) | set(c.discord_tags)
    avg_discord = len(all_discord) / 3.0

    # Stream divergence (different streams = interference)
    streams   = {a.stream, b.stream, c.stream}
    stream_div = (len(streams) - 1) / 2.0  # 0 (all same) to 1 (all different)

    # Antagonist overlap (do any antagonize each other?)
    antag_hits = 0
    for seed, others in [(a, [b, c]), (b, [a, c]), (c, [a, b])]:
        for other in others:
            if any(tag in other.name.lower() or tag in other.nature.lower()
                   for tag in seed.antagonist.lower().split()):
                antag_hits += 1
    antag_score = min(antag_hits / 6.0, 1.0)

    return (avg_discord * 0.4) + (stream_div * 0.4) + (antag_score * 0.2)


# ── ZERO-POINT COLLAPSE ───────────────────────────────────────────────────────

def zero_point(a: QuantaSeed, b: QuantaSeed, c: QuantaSeed,
               label: str, iteration: int) -> QuantaSeed:
    """
    Collapse three seeds into one zero-point seed.
    The zero-point captures: shared nature, merged resonance,
    acknowledged discord (friction preserved, not erased).
    """
    # Shared resonance (AND)
    shared_res = list(
        set(a.resonance_tags) & set(b.resonance_tags) |
        set(b.resonance_tags) & set(c.resonance_tags) |
        set(a.resonance_tags) & set(c.resonance_tags)
    )

    # All discord preserved (interference charge)
    all_discord = list(set(a.discord_tags + b.discord_tags + c.discord_tags))

    # Dominant stream (most common, or 'convergent' if all differ)
    streams = [a.stream, b.stream, c.stream]
    dominant = max(set(streams), key=streams.count)
    if len(set(streams)) == 3:
        dominant = "convergent"

    # Synthesize nature from the three
    natures = [a.nature.split("—")[0].strip(),
               b.nature.split("—")[0].strip(),
               c.nature.split("—")[0].strip()]

    return QuantaSeed(
        name           = label,
        source         = f"Triadic collapse L{iteration}: {a.name}+{b.name}+{c.name}",
        nature         = f"{natures[0]} / {natures[1]} / {natures[2]}",
        role           = f"zero-point of [{a.name}, {b.name}, {c.name}]",
        scale          = "adaptive",
        pinnacle       = f"emergent from: {a.pinnacle} / {b.pinnacle}",
        antagonist     = f"interference of: {a.antagonist[:40]} ++ {b.antagonist[:40]}",
        resonance_tags = shared_res,
        discord_tags   = all_discord[:6],          # preserve top discord
        stream         = dominant,
    )


# ── TRIADIC GROUPING ──────────────────────────────────────────────────────────

def group_into_triads(seeds: list, strategy: str = "resonance") -> list:
    """
    Group seeds into triads optimized for the strategy.

    strategy='resonance': maximize shared resonance (convergence)
    strategy='discord'  : maximize friction (interference/creative charge)
    strategy='bridge'   : mix streams for cross-pollination
    """
    used   = [False] * len(seeds)
    triads = []

    if strategy == "resonance":
        # Greedy: find the best resonance triad each round
        while sum(1 for u in used if not u) >= 3:
            best_score = -1
            best_triad = None
            avail = [i for i, u in enumerate(used) if not u]
            for combo in combinations(avail, 3):
                i, j, k = combo
                score = resonance_score(seeds[i], seeds[j], seeds[k])
                if score > best_score:
                    best_score = best_triad = None
                    best_score = score
                    best_triad = combo
            if best_triad:
                triads.append((seeds[best_triad[0]],
                               seeds[best_triad[1]],
                               seeds[best_triad[2]],
                               best_score))
                for idx in best_triad:
                    used[idx] = True
            else:
                break

    elif strategy == "discord":
        # Greedy: maximize friction
        while sum(1 for u in used if not u) >= 3:
            best_score = -1
            best_triad = None
            avail = [i for i, u in enumerate(used) if not u]
            for combo in combinations(avail, 3):
                i, j, k = combo
                score = discord_score(seeds[i], seeds[j], seeds[k])
                if score > best_score:
                    best_score = score
                    best_triad = combo
            if best_triad:
                triads.append((seeds[best_triad[0]],
                               seeds[best_triad[1]],
                               seeds[best_triad[2]],
                               best_score))
                for idx in best_triad:
                    used[idx] = True
            else:
                break

    elif strategy == "bridge":
        # Group by crossing streams (work + play + keep in each triad)
        stream_groups = {}
        for i, s in enumerate(seeds):
            if not used[i]:
                stream_groups.setdefault(s.stream, []).append(i)
        # Pull one from each stream per triad
        stream_keys = list(stream_groups.keys())
        while all(len(stream_groups.get(k, [])) >= 1 for k in stream_keys[:3]):
            combo_idx = [stream_groups[k].pop(0) for k in stream_keys[:3]]
            a, b, c   = seeds[combo_idx[0]], seeds[combo_idx[1]], seeds[combo_idx[2]]
            score     = resonance_score(a, b, c)
            triads.append((a, b, c, score))
            for idx in combo_idx:
                used[idx] = True
            if not all(stream_groups.get(k) for k in stream_keys[:3]):
                break

    # Leftover seeds — append as singleton info
    leftover = [seeds[i] for i, u in enumerate(used) if not u]

    return triads, leftover


# ── CONVERGENCE PASS ──────────────────────────────────────────────────────────

def convergence_pass(seeds: list, iteration: int,
                     strategy: str = "resonance") -> tuple:
    """
    One full convergence pass: group triads, collapse to zero-points.
    Returns (zero_points, triads_detail, leftover)
    """
    triads, leftover = group_into_triads(seeds, strategy)
    zero_points      = []
    triads_detail    = []

    for i, (a, b, c, rscore) in enumerate(triads):
        dscore = discord_score(a, b, c)
        label  = f"ZP_L{iteration}_{i+1:02d}"
        zp     = zero_point(a, b, c, label, iteration)

        zero_points.append(zp)
        triads_detail.append({
            "label"         : label,
            "seeds"         : [a.name, b.name, c.name],
            "resonance"     : round(rscore, 3),
            "discord"       : round(dscore, 3),
            "charge"        : round(dscore * 100, 1),
            "zero_point_tags": zp.resonance_tags,
            "stream"        : zp.stream,
        })

    return zero_points, triads_detail, leftover


# ── FRACTAL CONVERGENCE STREAM ────────────────────────────────────────────────

def fractal_convergence(seeds: list, target_size: int = 3,
                        max_iterations: int = 5,
                        strategy: str = "resonance") -> dict:
    """
    Repeatedly collapse seeds until target_size is reached.
    Each iteration: triad → zero-point → new seed set.
    Returns the full convergence history + final zero-points.
    """
    coc_id     = f"CONV_{now_stamp()}"
    history    = []
    current    = seeds[:]
    all_triads = []

    for iteration in range(1, max_iterations + 1):
        if len(current) <= target_size:
            break
        if len(current) < 3:
            break

        zps, triads_detail, leftover = convergence_pass(current, iteration, strategy)
        all_triads.extend(triads_detail)

        history.append({
            "iteration"  : iteration,
            "input_count": len(current),
            "triads"     : len(triads_detail),
            "output_zps" : len(zps),
            "leftover"   : [s.name for s in leftover],
            "triads_detail": triads_detail,
        })

        current = zps + leftover  # zero-points become next round's seeds

    return {
        "coc_id"    : coc_id,
        "strategy"  : strategy,
        "iterations": len(history),
        "history"   : history,
        "final"     : current,
        "all_triads": all_triads,
    }


# ── FRACTAL DIVERGENCE STREAM ─────────────────────────────────────────────────

def fractal_divergence(zero_points: list, depth: int = 2) -> dict:
    """
    Expand zero-points back outward.
    Each zero-point spawns branches based on its resonance_tags and stream.
    Interference patterns between branches are detected.
    """
    coc_id   = f"DIV_{now_stamp()}"
    branches = {}

    EXPANSION_MAP = {
        "work"       : ["scanner", "builder", "executor", "verifier"],
        "play"       : ["narrator", "herald", "scribe", "medium", "teacher"],
        "keep"       : ["steward", "keeper", "archivist", "ledger"],
        "seek"       : ["explorer", "purpose-finder", "connector"],
        "convergent" : ["bridge", "translator", "interfacer"],
        "interference": ["antagonist", "friction-source", "charge-generator"],
    }

    interference_pairs = []

    for zp in zero_points:
        exp_roles = EXPANSION_MAP.get(zp.stream, ["generic"])
        branch    = {
            "zero_point"  : zp.name,
            "stream"      : zp.stream,
            "resonance"   : zp.resonance_tags,
            "discord"     : zp.discord_tags,
            "expands_to"  : exp_roles,
            "entity_seeds": [
                f"{role}_{zp.name.lower().replace(' ', '_')}"
                for role in exp_roles
            ],
        }
        branches[zp.name] = branch

    # Detect interference between branches (where streams diverge)
    zp_list = list(zero_points)
    for i in range(len(zp_list)):
        for j in range(i + 1, len(zp_list)):
            a, b = zp_list[i], zp_list[j]
            if a.stream != b.stream:
                shared = set(a.resonance_tags) & set(b.resonance_tags)
                discord = set(a.discord_tags) | set(b.discord_tags)
                charge  = len(discord) - len(shared)  # net friction
                interference_pairs.append({
                    "pair"   : [a.name, b.name],
                    "streams": [a.stream, b.stream],
                    "shared" : list(shared),
                    "charge" : charge,
                    "note"   : "creative friction — productive interference"
                    if charge > 0 else "resonant bridge",
                })

    return {
        "coc_id"              : coc_id,
        "branches"            : branches,
        "interference_pairs"  : interference_pairs,
        "total_entity_seeds"  : sum(
            len(b["entity_seeds"]) for b in branches.values()
        ),
    }


# ── THREE-STREAM ALIGNMENT ────────────────────────────────────────────────────

def three_stream_alignment(seeds: list) -> dict:
    """
    Find how Henry (work) + Doozer (work/build) + Play Quanta align
    from the germ — their shared zero-point and interference charge.
    """
    henry  = next((s for s in seeds if s.name == "Henry"), None)
    doozer = next((s for s in seeds if s.name == "Doozer (SPIKE)"), None)
    sprite = next((s for s in seeds if s.name == "SPRITE"), None)

    if not all([henry, doozer, sprite]):
        return {"error": "Platform seeds not found"}

    res    = resonance_score(henry, doozer, sprite)
    disc   = discord_score(henry, doozer, sprite)
    zp     = zero_point(henry, doozer, sprite, "GERM_ZERO_POINT", 0)

    return {
        "triad"           : ["Henry", "Doozer(SPIKE)", "SPRITE"],
        "resonance"       : round(res, 3),
        "discord_charge"  : round(disc, 3),
        "charge_pct"      : f"{disc*100:.1f}%",
        "zero_point"      : zp.name,
        "shared_tags"     : zp.resonance_tags,
        "friction_tags"   : zp.discord_tags,
        "stream"          : zp.stream,
        "interpretation"  : {
            "resonance" : "What all three share — their germ",
            "discord"   : "Where they differ — the creative charge",
            "zero_point": "Their collapsed essence — one concept beneath all three",
        }
    }


# ── REPORT ────────────────────────────────────────────────────────────────────

def print_convergence_report(result: dict):
    print(f"\n{'='*62}")
    print(f"FRACTAL CONVERGENCE — {result['strategy'].upper()} strategy")
    print(f"COC: {result['coc_id']}")
    print(f"{'='*62}")

    for h in result["history"]:
        print(f"\n  ── ITERATION {h['iteration']} ──────────────────────────────")
        print(f"  Input: {h['input_count']} seeds → {h['triads']} triads → {h['output_zps']} zero-points")
        if h["leftover"]:
            print(f"  Leftover (carry forward): {h['leftover']}")
        print()
        for t in h["triads_detail"]:
            charge = "⚡" * min(int(t["charge"] / 20), 5)
            print(f"  [{t['label']}]")
            print(f"    Seeds    : {' + '.join(t['seeds'])}")
            print(f"    Resonance: {t['resonance']:.3f}  Discord: {t['discord']:.3f}  Charge: {charge} ({t['charge']}%)")
            print(f"    Stream   : {t['stream']}")
            print(f"    Tags     : {t['zero_point_tags']}")
            print()

    print(f"\n  ── FINAL ZERO-POINTS ({len(result['final'])}) ─────────────────")
    for zp in result["final"]:
        print(f"  ● {zp.name}")
        print(f"    Stream: {zp.stream} | Tags: {zp.resonance_tags[:4]}")
    print()


def print_divergence_report(result: dict):
    print(f"\n{'='*62}")
    print(f"FRACTAL DIVERGENCE — expanding from zero-points")
    print(f"COC: {result['coc_id']}")
    print(f"{'='*62}")

    for name, branch in result["branches"].items():
        print(f"\n  ● {name} [{branch['stream']}]")
        print(f"    Expands to: {branch['expands_to']}")
        print(f"    Entity seeds: {branch['entity_seeds']}")

    if result["interference_pairs"]:
        print(f"\n  ── INTERFERENCE PAIRS (creative friction) ─────────────")
        for pair in result["interference_pairs"]:
            note = "⚡ CHARGE" if pair["charge"] > 0 else "〰 BRIDGE"
            print(f"  {note}  {pair['pair'][0]} ↔ {pair['pair'][1]}")
            print(f"    Streams: {pair['streams']}  Charge: {pair['charge']}")
            if pair["shared"]:
                print(f"    Shared: {pair['shared']}")
    print()


def print_alignment(result: dict):
    print(f"\n{'='*62}")
    print(f"THREE-STREAM ALIGNMENT — Henry + Doozer + SPRITE")
    print(f"From the germ:")
    print(f"{'='*62}")
    print(f"  Triad         : {result['triad']}")
    print(f"  Resonance     : {result['resonance']} (shared essence)")
    print(f"  Discord Charge: {result['charge_pct']} (creative friction)")
    print(f"  Zero-Point    : {result['zero_point']}")
    print(f"  Shared Tags   : {result['shared_tags']}")
    print(f"  Friction Tags : {result['friction_tags'][:4]}")
    print(f"  Stream        : {result['stream']}")
    print()


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    print(f"\n∰◊€π¿🌌∞")
    print(f"DISTILLATION ENGINE — Fractal Convergence/Divergence")
    print(f"Timestamp: {now_stamp()}")
    print(f"Seeds loaded: {len(SEEDS)}")

    if "--stream" in args:
        from seeds import all_streams, by_stream
        for stream in sorted(all_streams()):
            group = by_stream(stream)
            print(f"\n── {stream.upper()} ({len(group)}) ──")
            for s in group:
                print(f"  {s.name:28s} {s.nature[:50]}")
        return

    # ── Three-stream alignment (the germ) ─────────────────────────────────────
    alignment = three_stream_alignment(SEEDS)
    print_alignment(alignment)

    # ── Convergence: resonance strategy ───────────────────────────────────────
    print("\n[ CONVERGENCE STREAM — Resonance Strategy ]")
    conv_res = fractal_convergence(SEEDS, target_size=3,
                                   max_iterations=4, strategy="resonance")
    print_convergence_report(conv_res)

    # ── Convergence: discord strategy (interference-first) ────────────────────
    print("\n[ CONVERGENCE STREAM — Discord/Friction Strategy ]")
    conv_disc = fractal_convergence(SEEDS, target_size=3,
                                    max_iterations=4, strategy="discord")
    print_convergence_report(conv_disc)

    # ── Divergence from resonance zero-points ─────────────────────────────────
    print("\n[ DIVERGENCE STREAM — from resonance zero-points ]")
    div = fractal_divergence(conv_res["final"])
    print_divergence_report(div)

    # ── Save results ──────────────────────────────────────────────────────────
    import os
    os.makedirs("reports", exist_ok=True)
    stamp = now_stamp()

    results = {
        "timestamp"            : stamp,
        "alignment"            : alignment,
        "convergence_resonance": {
            "iterations": conv_res["iterations"],
            "final_count": len(conv_res["final"]),
            "final_names": [zp.name for zp in conv_res["final"]],
        },
        "convergence_discord"  : {
            "iterations": conv_disc["iterations"],
            "final_count": len(conv_disc["final"]),
            "final_names": [zp.name for zp in conv_disc["final"]],
        },
        "divergence": {
            "total_entity_seeds": div["total_entity_seeds"],
            "interference_pairs": len(div["interference_pairs"]),
        },
    }

    out_path = f"reports/distillation_{stamp}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n  Report saved: {out_path}")
    print(f"\n∰◊€π¿🌌∞")
    print(f"€(distillation_{stamp})")
    print(f"*Status: CONVERGENCE_COMPLETE*\n")


if __name__ == "__main__":
    main()
