"""Decouple the requested comparison property from entity position, train only."""
from collections import Counter
import copy
import hashlib
from pathlib import Path
import random

SEED = 2026100671
KIND = 'local_condition_comparison_query_balance_v1'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-query-balance-20261006')
QUESTIONS = {
    'comparison-0': ('長い方の棒を持っているのは、', '短い方の棒を持っているのは、'),
    'comparison-1': ('二人のうち、長い棒を持つ人は、', '二人のうち、短い棒を持つ人は、'),
    'comparison-2': ('長い方の持ち主は、', '短い方の持ち主は、'),
    'comparison-3': ('長い方の棒を選ぶと、持ち主は、', '短い方の棒を選ぶと、持ち主は、'),
}


def shorter_query(row):
    if row['split'] != 'train' or row['category'] != 'comparison' or row['template_id'] not in QUESTIONS:
        raise ValueError('Only existing four train comparison forms may change')
    old, new = QUESTIONS[row['template_id']]
    if not row['prefix'].endswith(old):
        raise ValueError('Expected exact query suffix required')
    a, b = row['facts']['A'], row['facts']['B']
    x, y = row['local_state']['A_length'], row['local_state']['B_length']
    if x == y:
        raise ValueError('Grounded unequal lengths required')
    longer, shorter = (a, b) if x > y else (b, a)
    if row['outcome'] != longer + 'である。' or row['choices'][row['label']] != row['outcome']:
        raise ValueError('Original longer-entity conclusion differs from state')
    result = copy.deepcopy(row)
    result['prefix'] = row['prefix'][:-len(old)] + new
    result['label'] = 1 - row['label']
    result['outcome'] = result['choices'][result['label']]
    if result['outcome'] != shorter + 'である。':
        raise ValueError('Shorter-entity conclusion differs from state')
    result.update(requested_relation='shorter', original_context_branch=row['label'])
    result['text'] = result['prefix'] + result['outcome']
    result['text_sha256'] = hashlib.sha256(result['text'].encode()).hexdigest()
    result['cut'], result['end'] = len(result['prefix']), len(result['text'])
    return result


def build_rows(source):
    rows, families = source['rows'], source['families']
    if (len(rows) != 2048 or len(families) != 1024 or len({r['id'] for r in rows}) != 2048
            or any(r['split'] != 'train' for r in rows) or any(f['split'] != 'train' for f in families)):
        raise ValueError('Same original train-only2048/1024 selection required')
    selected = set()
    for i, template in enumerate(QUESTIONS):
        choices = sorted(f['id'] for f in families if f['template_id'] == template)
        if len(choices) != (43 if i < 3 else 42):
            raise ValueError('Original four-form family counts differ')
        random.Random(SEED + i).shuffle(choices)
        selected.update(choices[:(len(choices) + int(i % 2 == 0)) // 2])
    if len(selected) != 86:
        raise ValueError('Fixed86 shorter-query families required')
    out = [shorter_query(r) if r['family'] in selected else copy.deepcopy(r) for r in rows]
    if (sum(a != b for a, b in zip(rows, out, strict=True)) != 172
            or len({r['text_sha256'] for r in out}) != 2048
            or Counter(r['category'] for r in rows) != Counter(r['category'] for r in out)
            or any(a != b for a, b in zip(rows, out, strict=True) if a['category'] != 'comparison')):
        raise ValueError('Only172 comparison documents may change; counts and others byte-exact')
    return out, sorted(selected)


def pilot_rows(rows):
    # One opposed-state family per train surface/query variant, then four more.
    # Selection uses train IDs only; never probe errors, content rerolls or scores.
    groups = {}
    for r in rows:
        query = r.get('requested_relation', 'longer') if r['category'] == 'comparison' else 'original'
        groups.setdefault((r['template_id'], query), set()).add(r['family'])
    if len(groups) != 28:
        raise ValueError('24 old relation forms, with four additional train query variants required')
    chosen = {sorted(ids)[0] for ids in groups.values()}
    chosen.update(sorted({r['family'] for r in rows} - chosen)[:32 - len(chosen)])
    selected = [r for r in rows if r['family'] in chosen]
    if len(selected) != 64 or any(sum(r['family'] == f for r in selected) != 2 for f in chosen):
        raise ValueError('Fixed64 complete opposite-state source documents required')
    return selected


class QueryBalancedTrainView:
    def __init__(self, directory, manifest_sha256, require_accepted=True):
        import json
        import numpy as np
        self.directory = Path(directory)
        digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
        if digest(self.directory / 'manifest.json') != manifest_sha256:
            raise ValueError('Query-source manifest differs')
        m = self.manifest = json.loads((self.directory / 'manifest.json').read_text())
        if (m['kind'] != KIND or m['documents'] != 2048 or m['changed_documents'] != 172
                or m['newly_prepared_original_corpus_tokens'] != 0
                or digest(self.directory / 'train.npz') != m['arrays_sha256']
                or m['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
            raise ValueError('Fixed train-only query material differs')
        if require_accepted:
            review = json.loads((self.directory / 'content-review.json').read_text())
            if (not review['all64_read'] or not review['training_pool_accepted'] or review['weak_documents'] > 10
                    or review['unresolved_grammar_documents'] or review['manifest_sha256'] != manifest_sha256
                    or review['pilot_sha256'] != m['pilot_sha256']
                    or review['notes_sha256'] != digest(self.directory / 'content-notes.json')):
                raise ValueError('Raw-bound all64 content acceptance required')
        with np.load(self.directory / 'train.npz', allow_pickle=False) as arrays:
            self.tokens = arrays['tokens'].copy()
            self.focus = arrays['focus'].astype(bool)
            self.offsets = arrays['offsets'].copy()
            self.lengths = arrays['lengths'].copy()
        if (len(self.offsets) != 2048 or len(self.tokens) != m['serialized_tokens']
                or self.focus.shape != self.tokens.shape or int(self.focus.sum()) != m['outcome_focus_body_targets']
                or not np.array_equal(self.offsets, np.r_[0, np.cumsum(self.lengths)[:-1]])
                or int(self.lengths.sum()) != len(self.tokens) or np.any(self.focus & (self.tokens < 8))
                or np.count_nonzero(self.tokens == 2) != 2048 or np.count_nonzero(self.tokens == 3) != 2048
                or not np.all(self.tokens[self.offsets] == 2) or not np.all(self.tokens[self.offsets + self.lengths - 1] == 3)
                or np.any(self.tokens >= 4096) or np.any(np.isin(self.tokens, [0, 1, 4, 5, 6, 7]))):
            raise ValueError('Complete native body/EOS arrays differ')
        self.manifest_sha256 = manifest_sha256
