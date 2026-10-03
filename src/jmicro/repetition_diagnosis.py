"""Read-only repetition and sampler diagnostics; never change frozen metrics."""
from collections import Counter
import re

import numpy as np


def repetition_details(text):
    match = re.search(r"(.{2,}?)\1\1", text, flags=re.DOTALL)
    return {"repetition": match is not None,
            "first_match_start_char": match.start() if match else None,
            "first_match_end_char": match.end() if match else None,
            "repeated_unit": match.group(1) if match else None}


def repeated_ngram_fraction(sequence, n=4):
    grams = Counter(tuple(sequence[i:i+n]) for i in range(len(sequence)-n+1))
    total = sum(grams.values())
    return sum(count-1 for count in grams.values()) / total if total else 0.


def target_block_counts(positions, blocks, context):
    """Target position k belongs to (k-1)//context, including boundary EOS."""
    positions = np.asarray(positions, dtype=np.int64)
    positions = positions[(positions > 0) & (positions <= blocks*context)]
    return np.bincount((positions-1)//context, minlength=blocks)


def consumed_targets(counts, sampler):
    blocks = sampler['blocks']
    if len(counts) != blocks or not 0 <= sampler['position'] <= blocks:
        raise ValueError('Invalid sampler/counts')
    order = np.random.default_rng(np.random.SeedSequence(
        [sampler['seed'], sampler['epoch']])).permutation(blocks)
    return int(sampler['epoch']*counts.sum() + counts[order[:sampler['position']]].sum())


def paired_transitions(old, new):
    def key(row):
        return row['id'], row['decoding'], row['suppressed'], row['seed']
    before, after = {key(r): r for r in old}, {key(r): r for r in new}
    if len(before) != len(old) or len(after) != len(new) or before.keys() != after.keys():
        raise ValueError('Duplicate or mismatched paired generation cases')
    groups = {}
    for k, a in before.items():
        b = after[k]
        group = f"{a['decoding']}-suppressed{int(a['suppressed'])}"
        result = groups.setdefault(group, dict(outputs=0, neither=0, new_only=0,
            old_only=0, both=0, new_only_ids=[], old_only_ids=[]))
        result['outputs'] += 1
        label = 'both' if a['repetition'] and b['repetition'] else 'old_only' if a['repetition'] else 'new_only' if b['repetition'] else 'neither'
        result[label] += 1
        if label in ('new_only', 'old_only'):
            result[label+'_ids'].append({'id': k[0], 'seed': k[3]})
    return groups
