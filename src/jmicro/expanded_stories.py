"""Whole translated stories; source-specific length contract, no truncation."""
from collections import Counter
import re
from jmicro.complete_units import balanced, complete_sentences, unit_hash
from jmicro.evaluation import canonicalize_text
from jmicro.coherent_units import DEPENDENT_START

def translated_candidate(text, tok):
    text = canonicalize_text(text).strip()
    if not text or DEPENDENT_START.search(text) or not balanced(text): return None
    if re.search(r'https?://|www\.|```|<\||続きを読む|つづく|続きはこちら|…|⋯|\.{3}|翻訳：|日本語訳：', text, re.I): return None
    sentences = list(complete_sentences(text))
    if not 2 <= len(sentences) <= 24: return None
    end = 0
    for start, stop, _ in sentences:
        if text[end:start].strip(): return None
        end = stop
    if text[end:].strip() or re.search(r'[?？][」』]*$', text): return None
    parts = [s[2] for s in sentences]
    if len(set(parts)) != len(parts) or re.search(r'(.{4,}?)\1\1', text): return None
    grams = Counter(text[i:i+4] for i in range(max(0,len(text)-3)))
    repetition = 1-len(grams)/sum(grams.values()) if grams else 0
    if repetition > .15: return None
    ids = tok.encode(text)
    if not 32 <= len(ids) <= 512 or any(i<8 for i in ids): return None
    return dict(text=text, ids=ids, sentences=len(parts), text_sha256=unit_hash(text), char4_repetition=repetition)
