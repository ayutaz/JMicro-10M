"""Select whole finished documents; heuristics are not semantic certification."""
from collections import Counter
import re

from jmicro.coherent_units import DEPENDENT_START, BOILERPLATE, FORWARD_END
from jmicro.complete_units import balanced, complete_sentences, unit_hash


def whole_candidate(text, size, source):
    text = text.strip()
    lower, upper = (32, 128) if source == 'story' else (64, 384)
    if not lower <= size <= upper or not balanced(text) or DEPENDENT_START.search(text):
        return None
    if re.search(r'https?://|www\.|```|<\||続きを読む|つづく|続きはこちら|…|⋯|\.{3}', text, re.I):
        return None
    if source == 'web' and (BOILERPLATE.search(text) or FORWARD_END.search(text)):
        return None
    sentences = list(complete_sentences(text))
    if not (2 if source == 'story' else 1) <= len(sentences) <= (8 if source == 'story' else 12):
        return None
    end = 0
    for start, stop, _ in sentences:
        if text[end:start].strip():
            return None
        end = stop
    if text[end:].strip() or re.search(r'[?？][」』]*$', text):
        return None
    parts = [s[2] for s in sentences]
    if len(parts) != len(set(parts)) or re.search(r'(.{4,}?)\1\1', text):
        return None
    grams = Counter(text[i:i+4] for i in range(max(0, len(text)-3)))
    repetition = 1 - len(grams)/sum(grams.values()) if grams else 0
    if repetition > (.08 if source == 'story' else .15):
        return None
    return dict(text=text, sentences=len(parts), text_sha256=unit_hash(text), char4_repetition=repetition)
