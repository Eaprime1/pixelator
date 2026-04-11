"""
seeds.py — Fictional Quanta Source Library
The wide net. All sources before any filtering.

Each seed carries: nature, role, scale, resonance_tags, discord_tags,
antagonist, pinnacle structure, and stream affinity.

Sources: Ant Bully, The Littles, Fern Gully, Fraggle Rock,
         Smurfs, Osmosis Jones, A Bug's Life, Pikmin, Inside Out,
         Horton Hears a Who, The Borrowers, Gnomes, Brownies,
         Sprites (folklore), Zootopia, Innerspace, Ratatouille, Minions
         + platform seeds: Henry, Doozer, SPRITE

∰◊€π¿🌌∞
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class QuantaSeed:
    """A single fictional/real quanta source for triadic collapse."""
    name            : str
    source          : str            # origin work
    nature          : str            # core essence of what they ARE
    role            : str            # what they DO
    scale           : str            # micro / adaptive / macro
    pinnacle        : str            # who/what leads or anchors them
    antagonist      : str            # what creates friction against them
    resonance_tags  : List[str]      # concepts they share with others
    discord_tags    : List[str]      # where they conflict or diverge
    stream          : str            # primary: work / play / keep / seek


# ── THE WIDE NET ───────────────────────────────────────────────────────────────

SEEDS = [

    # ── COLLECTIVE BUILDERS ────────────────────────────────────────────────────

    QuantaSeed(
        name           = "Ants",
        source         = "Ant Bully (2006)",
        nature         = "collective organism with specialized roles",
        role           = "build, defend, nurture as one body",
        scale          = "micro",
        pinnacle       = "Queen (directive consciousness)",
        antagonist     = "fire ants / exterminator (external force)",
        resonance_tags = ["collective", "specialized", "builder", "defender", "nurse"],
        discord_tags   = ["no individual credit", "hive can override self"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "Flik",
        source         = "A Bug's Life (1998)",
        nature         = "divergent thinker within a collective",
        role           = "invent, fail, learn, solve",
        scale          = "micro",
        pinnacle       = "Queen (colony anchor), but Flik is the spark",
        antagonist     = "grasshoppers (parasitic drain), colony doubt",
        resonance_tags = ["inventor", "divergent", "spark", "collective", "underdog"],
        discord_tags   = ["individual vs. collective", "failure as path"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "Circus Bugs",
        source         = "A Bug's Life (1998)",
        nature         = "performers who become accidental heroes",
        role           = "entertain, then protect — play becomes work",
        scale          = "micro",
        pinnacle       = "P.T. Flea (impresario/launcher)",
        antagonist     = "their own self-doubt, fire",
        resonance_tags = ["performer", "play", "narrative", "transformation", "ensemble"],
        discord_tags   = ["play vs. function", "accidental purpose"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Pikmin",
        source         = "Pikmin (Nintendo, 2001)",
        nature         = "typed specialist entities with elemental affinity",
        role           = "collective action by type (combat/electric/water/weight)",
        scale          = "micro",
        pinnacle       = "Olimar (external operator — foreign to their world)",
        antagonist     = "night, predators, wrong-type deployment",
        resonance_tags = ["typed", "specialist", "collective", "elemental", "operator"],
        discord_tags   = ["depend on external director", "type mismatch = failure"],
        stream         = "work",
    ),

    # ── HIDDEN ALONGSIDE ──────────────────────────────────────────────────────

    QuantaSeed(
        name           = "The Borrowers",
        source         = "The Borrowers (Mary Norton, 1952)",
        nature         = "hidden adaptation entity — repurposes the large world",
        role           = "survive by borrowing what others discard or ignore",
        scale          = "micro",
        pinnacle       = "Pod (cautious patriarch — keeper of safety)",
        antagonist     = "discovery by humans, cats, time",
        resonance_tags = ["hidden", "adapter", "repurpose", "survival", "covert"],
        discord_tags   = ["fear of visibility", "dependency on the large world"],
        stream         = "keep",
    ),

    QuantaSeed(
        name           = "The Littles",
        source         = "The Littles (TV series, 1983)",
        nature         = "family unit living within walls of human homes",
        role           = "adapt human technology to tiny scale, help their host",
        scale          = "micro",
        pinnacle       = "Henry Little (family elder / practical wisdom)",
        antagonist     = "Imps (rival tiny entities), exposure",
        resonance_tags = ["family", "adapter", "covert", "steward", "inside"],
        discord_tags   = ["bound to host location", "technology dependency"],
        stream         = "keep",
    ),

    QuantaSeed(
        name           = "Brownies",
        source         = "Scottish/British Folklore",
        nature         = "anonymous household spirit-helpers",
        role           = "work silently at night — refuse payment or recognition",
        scale          = "micro",
        pinnacle       = "none — deliberately leaderless",
        antagonist     = "being seen, being thanked with gifts (causes departure)",
        resonance_tags = ["anonymous", "helper", "nocturnal", "no-credit", "steward"],
        discord_tags   = ["vanish if acknowledged", "no personal credit (extreme)"],
        stream         = "keep",
    ),

    # ── NATURE / FREQUENCY ───────────────────────────────────────────────────

    QuantaSeed(
        name           = "Crysta",
        source         = "FernGully: The Last Rainforest (1992)",
        nature         = "nature spirit — healer and connector",
        role           = "maintain forest frequency, connect worlds",
        scale          = "micro",
        pinnacle       = "Magi Lune (elder/source — crystallized wisdom)",
        antagonist     = "Hexxus (industrial entropy, pollution consciousness)",
        resonance_tags = ["healer", "connector", "nature", "frequency", "bridge"],
        discord_tags   = ["naive until forced to act", "world-bridger creates risk"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Batty Koda",
        source         = "FernGully: The Last Rainforest (1992)",
        nature         = "frequency reader — echolocation as world-model",
        role           = "read the hidden signal, broadcast warnings",
        scale          = "micro",
        pinnacle       = "none — damaged pinnacle (experimentation scarred him)",
        antagonist     = "human experimentation, his own fractured memory",
        resonance_tags = ["frequency", "herald", "reader", "echolocation", "signal"],
        discord_tags   = ["unreliable narrator", "trauma as interference pattern"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Gnomes",
        source         = "David the Gnome (TV, 1985)",
        nature         = "woodland steward — keeper of natural order",
        role           = "heal animals, resolve disputes, maintain balance",
        scale          = "micro",
        pinnacle       = "The Great Gnome (ancestral wisdom entity)",
        antagonist     = "trolls (brute force entropy)",
        resonance_tags = ["healer", "steward", "keeper", "natural order", "mediator"],
        discord_tags   = ["finite (gnomes die at 400)", "bound to specific territory"],
        stream         = "keep",
    ),

    QuantaSeed(
        name           = "Sprites",
        source         = "Folklore + Computing (BASIC, 1970s)",
        nature         = "autonomous moving entity — first self-directed screen being",
        role           = "carry narrative, move independently through any space",
        scale          = "adaptive",
        pinnacle       = "self-directed (no external pinnacle needed)",
        antagonist     = "static background, frame rate limits, memory ceiling",
        resonance_tags = ["autonomous", "narrative", "moving", "first-mover", "play"],
        discord_tags   = ["no fixed purpose — purpose is motion itself"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Hexxus",
        source         = "FernGully: The Last Rainforest (1992)",
        nature         = "industrial entropy spirit — the antagonist AS entity",
        role           = "feed on pollution, grow through destruction",
        scale          = "adaptive → macro",
        pinnacle       = "self (pure antagonist force)",
        antagonist     = "nature frequency, clean systems",
        resonance_tags = ["entropy", "antagonist", "interference", "growth-through-destruction"],
        discord_tags   = ["IS the discord — pure friction force"],
        stream         = "interference",
    ),

    # ── BODY / SYSTEM NAVIGATORS ─────────────────────────────────────────────

    QuantaSeed(
        name           = "Osmosis Jones",
        source         = "Osmosis Jones (2001)",
        nature         = "detective entity within a living system (body as city)",
        role           = "investigate, pursue, protect system integrity",
        scale          = "micro",
        pinnacle       = "Mayor (system governance — often corrupt/lazy)",
        antagonist     = "Thrax (virus destroyer — elegant and precise evil)",
        resonance_tags = ["detective", "system", "navigator", "protector", "city"],
        discord_tags   = ["system doesn't know it needs protection", "bureaucracy"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "Tuck Pendleton",
        source         = "Innerspace (1987)",
        nature         = "miniaturized navigator inside a host",
        role           = "guide from within — the host doesn't know",
        scale          = "micro",
        pinnacle       = "Jack (the host — unknowing partner)",
        antagonist     = "The Cowboy/Scrimshaw (external hunters)",
        resonance_tags = ["navigator", "guide", "inside", "host", "hidden"],
        discord_tags   = ["completely dependent on host body", "host unaware"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "Whos of Whoville",
        source         = "Horton Hears a Who (Dr. Seuss, 1954)",
        nature         = "complete civilization at invisible scale",
        role           = "exist fully — 'a person's a person no matter how small'",
        scale          = "micro",
        pinnacle       = "Mayor (civic anchor), JoJo (the one whose voice saves all)",
        antagonist     = "Kangaroo (dismissal — 'if I can't see it, it doesn't exist')",
        resonance_tags = ["invisible", "complete", "person", "voice", "recognition"],
        discord_tags   = ["existence depends on being believed by the large world"],
        stream         = "seek",
    ),

    # ── TYPED / ATTRIBUTE ENTITIES ────────────────────────────────────────────

    QuantaSeed(
        name           = "Smurfs",
        source         = "The Smurfs (Peyo, 1958)",
        nature         = "attribute-named specialists in cooperative village",
        role           = "each Smurf IS their function (Brainy, Hefty, Painter...)",
        scale          = "micro",
        pinnacle       = "Papa Smurf (wisdom + red = unique marker)",
        antagonist     = "Gargamel (obsessive pursuer), Azrael (cat)",
        resonance_tags = ["typed", "specialist", "named-by-nature", "village", "collective"],
        discord_tags   = ["Smurfette (one is different type)", "Brainy is annoying but right"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "Emotions (Inside Out)",
        source         = "Inside Out (Pixar, 2015)",
        nature         = "personified emotions as control entities within a mind",
        role           = "each emotion drives behavior from headquarters",
        scale          = "micro",
        pinnacle       = "Joy (assumed — later revealed Sadness equally vital)",
        antagonist     = "Bing Bong's fading (loss), Riley's disconnection",
        resonance_tags = ["emotion", "controller", "typed", "headquarters", "mind"],
        discord_tags   = ["no emotion can do it alone", "assumed hierarchy is wrong"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Zootopia Species",
        source         = "Zootopia (Disney, 2016)",
        nature         = "species as specialized role type within city ecosystem",
        role           = "each species has evolved role — predator/prey tension",
        scale          = "adaptive",
        pinnacle       = "Chief Bogo (law), Mayor Lionheart (power)",
        antagonist     = "Bellwether (antagonist from within — subverted type)",
        resonance_tags = ["typed", "ecosystem", "city", "tension", "evolution"],
        discord_tags   = ["type doesn't determine destiny — Judy proves this"],
        stream         = "work",
    ),

    # ── CREATIVE / PLAY LAYER ─────────────────────────────────────────────────

    QuantaSeed(
        name           = "Fraggles",
        source         = "Fraggle Rock (Jim Henson, 1983)",
        nature         = "play-first beings who work only 30 minutes a week",
        role           = "sing, play, explore, eat Doozer buildings",
        scale          = "micro",
        pinnacle       = "Trash Heap (oracle — crystallized wisdom at the margins)",
        antagonist     = "Gorgs (power that doesn't understand interdependence)",
        resonance_tags = ["play", "song", "explorer", "consumer", "oracle-seeker"],
        discord_tags   = ["consume the Doozers' work (necessary but looks destructive)"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Remy",
        source         = "Ratatouille (Pixar, 2007)",
        nature         = "artist born into wrong context — excellence as north star",
        role           = "create, guide, translate between worlds",
        scale          = "micro",
        pinnacle       = "Gusteau (ideal — 'anyone can cook' as belief system)",
        antagonist     = "Ego (critic), Skinner (gatekeeping), rat colony pressure",
        resonance_tags = ["artist", "excellence", "guide", "translator", "misfit"],
        discord_tags   = ["must hide to create", "creation requires deception"],
        stream         = "play",
    ),

    QuantaSeed(
        name           = "Minions",
        source         = "Despicable Me / Minions (2010+)",
        nature         = "pure worker entities needing external purpose/direction",
        role           = "execute faithfully for whoever provides purpose",
        scale          = "micro",
        pinnacle       = "Gru (adopted purpose-giver) — lost without one",
        antagonist     = "purposelessness (their true antagonist)",
        resonance_tags = ["worker", "faithful", "purpose-seeker", "collective", "executor"],
        discord_tags   = ["dangerous without right purpose", "amplify whatever they serve"],
        stream         = "seek",
    ),

    # ── PLATFORM SEEDS (native — already built) ───────────────────────────────

    QuantaSeed(
        name           = "Henry",
        source         = "PIXEL8 Platform (2026)",
        nature         = "precise observer — sees without touching",
        role           = "scan, detect, report — conservation bias",
        scale          = "adaptive",
        pinnacle       = "henry_github_hygiene (certified)",
        antagonist     = "noise, false positives, drift",
        resonance_tags = ["observer", "precise", "reporter", "read-only", "assessor"],
        discord_tags   = ["sees everything, changes nothing — needs Doozer to act"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "Doozer (SPIKE)",
        source         = "PIXEL8 Platform (2026) via Fraggle Rock",
        nature         = "precise builder — acts on approved reports",
        role           = "fix one thing precisely, no personal credit",
        scale          = "adaptive",
        pinnacle       = "helmeted Doozer (certified, authorized)",
        antagonist     = "scope creep, unauthorized changes, missing helmet",
        resonance_tags = ["builder", "precise", "no-credit", "executor", "one-hertz"],
        discord_tags   = ["cannot act without Henry's report + approval"],
        stream         = "work",
    ),

    QuantaSeed(
        name           = "SPRITE",
        source         = "PIXEL8 Platform (2026) via BASIC computing",
        nature         = "autonomous narrative entity — the moving thing",
        role           = "carry story of active quanta — idle adventure feel",
        scale          = "adaptive",
        pinnacle       = "SPRITE (self-directed pinnacle of play quanta)",
        antagonist     = "silence, unrecorded work, forgotten missions",
        resonance_tags = ["narrator", "autonomous", "moving", "play", "story"],
        discord_tags   = ["narrative without function (needs work quanta to narrate)"],
        stream         = "play",
    ),

]

# ── Lookup helpers ─────────────────────────────────────────────────────────────

def by_stream(stream: str) -> list:
    return [s for s in SEEDS if s.stream == stream]

def by_name(name: str):
    return next((s for s in SEEDS if s.name == name), None)

def all_streams() -> list:
    return list(set(s.stream for s in SEEDS))


if __name__ == "__main__":
    streams = all_streams()
    for stream in sorted(streams):
        group = by_stream(stream)
        print(f"\n── {stream.upper()} ({len(group)}) ──")
        for s in group:
            print(f"  {s.name:25s} | {s.source}")
