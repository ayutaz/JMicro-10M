"""Whole-document material and exact 1:5 nested length/source matching."""
from collections import Counter, defaultdict
import hashlib
import random
import re

from jmicro.coherent_units import DEPENDENT_START, BOILERPLATE, FORWARD_END
from jmicro.complete_units import balanced, complete_sentences, unit_hash

MAGIC = re.compile(r"魔法|ドラゴン|妖精|異世界|時間旅行|怪物|恐竜")
MISSING = re.compile(r"[（(]\s*[,、:：]|[,、:：]\s*[）)]|[（(]\s*[）)]")


def whole_material(text, size, source):
    """Keep the original complete body, never shorten or rewrite its ending."""
    lower, upper = (32, 512) if source == "story" else (64, 1024)
    original = text
    text = text.strip()
    if not lower <= size <= upper or not balanced(text) or DEPENDENT_START.search(text):
        return None
    if re.search(r"https?://|www\.|```|<\||…|⋯|\.{3}", text, re.I):
        return None
    if BOILERPLATE.search(text) or FORWARD_END.search(text) or MISSING.search(text):
        return None
    if source == "story" and MAGIC.search(text):
        return None
    sentences = list(complete_sentences(text))
    if not (2 if source == "story" else 1) <= len(sentences) <= 64:
        return None
    end = 0
    for start, stop, _ in sentences:
        if text[end:start].strip():
            return None
        end = stop
    if text[end:].strip() or re.search(r"[？?][」』]*$", text):
        return None
    parts = [s[2] for s in sentences]
    if len(set(parts)) != len(parts) or re.search(r"(.{4,}?)\1\1", text):
        return None
    grams = Counter(text[i:i+4] for i in range(max(0, len(text)-3)))
    repetition = 1 - len(grams) / sum(grams.values()) if grams else 0
    if repetition > .15:
        return None
    family = source + ":" + unit_hash(re.sub(r"[0-9０-９]+", "N", parts[0]))
    split = "dev" if int(hashlib.sha256(family.encode()).hexdigest()[:8], 16) % 100 == 0 else "train"
    return dict(text=original, canonical_sha256=unit_hash(original), source_family=family,
                split=split, sentences=len(parts), char4_repetition=repetition)


class NestedGroups:
    """Five distinct same-source/same-length documents; one goes into both pools."""
    def __init__(self, seed):
        self.pending = defaultdict(list)
        self.rng = random.Random(seed)

    def add(self, record):
        key = (record["source"], record["body_tokens"])
        bucket = self.pending[key]
        bucket.append(record)
        if len(bucket) < 5:
            return None
        group = list(bucket)
        bucket.clear()
        return group, self.rng.randrange(5)
