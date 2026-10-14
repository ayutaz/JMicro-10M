"""Prospective observed-context likelihood contrast; unchanged native CE.

Match exactly the original suffix targets and prefix token length. A distractor
is another observed context, not a certified false factual continuation. The
bounded FIFO holds only previously committed TRAIN contexts, never features or
learned parameters. This module does not open datasets or checkpoints.
"""
import copy
import hashlib
import json

from jmicro.evaluation_boundary import require_digest

KIND = 'observed_TRAIN_equal_length_context_likelihood_FIFO_v1'
CAPACITY = 128
MAXIMUM = 1024
COEFFICIENT = .1
GENRES = ('web', 'textbook', 'story')


def ids_digest(ids):
    return hashlib.sha256(json.dumps(ids, separators=(',', ':')).encode()).hexdigest()


def original_anchors(rows, tokenizer):
    """Recover original whole-body suffix IDs, not independently recoded IDs.

    Reuses the frozen sampler's previously validated byte-exact observed pair.
    Re-encoding the concatenated original bytes recovers its canonical native
    body, including the exact suffix token IDs. All rows still teach main CE.
    """
    anchors, families, bodies = [], set(), set()
    for row in rows:
        prefix, independently_encoded_suffix = row['prefix_ids'], row['suffix_ids']
        if (not row['original_document_first_window'] or not prefix or not independently_encoded_suffix
                or row['original_body_tokens'] + 1 > 512
                or row['teacher_tokens'] != row['original_body_tokens'] + 1
                or row['source_family'] in families or row['full_original_body_sha256'] in bodies):
            continue
        raw = tokenizer.decode_bytes(prefix + independently_encoded_suffix)
        if hashlib.sha256(raw).hexdigest() != row['full_original_body_sha256']:
            raise ValueError('Original observed pair bytes differ')
        body = tokenizer.encode(raw.decode('utf-8'))
        if (len(body) != row['original_body_tokens'] or body[:len(prefix)] != prefix
                or tokenizer.decode_bytes(body) != raw):
            raise ValueError('Original prefix/body codec boundary differs')
        if row['input_ids'] != [2] + body or row['target_ids'] != body + [3]:
            raise ValueError('All auxiliary target identities must already teach this complete main CE row')
        suffix = body[len(prefix):]
        if len(body) > MAXIMUM - 1:
            continue
        if not 16 <= len(prefix) or not 16 <= len(suffix):
            raise ValueError('Original observed split minimum length differs')
        if any(type(i) is not int or not 8 <= i < 4096 for i in body):
            raise ValueError('Original4096 plain-body IDs required')
        families.add(row['source_family'])
        bodies.add(row['full_original_body_sha256'])
        anchors.append(dict(source=row['source'], source_family=row['source_family'],
            body_sha256=row['full_original_body_sha256'], prefix_ids=prefix.copy(), suffix_ids=suffix,
            prefix_sha256=ids_digest(prefix), suffix_sha256=ids_digest(suffix)))
    return anchors


def validate_anchor(anchor):
    if (set(anchor) != {'source', 'source_family', 'body_sha256', 'prefix_ids', 'suffix_ids',
                       'prefix_sha256', 'suffix_sha256'} or anchor['source'] not in GENRES
            or not isinstance(anchor['source_family'], str) or not anchor['source_family']):
        raise ValueError('Strict observed TRAIN anchor schema required')
    for key in ('body_sha256', 'prefix_sha256', 'suffix_sha256'):
        require_digest(anchor[key])
    for key in ('prefix_ids', 'suffix_ids'):
        if (not isinstance(anchor[key], list) or len(anchor[key]) < 16
                or any(type(i) is not int or not 8 <= i < 4096 for i in anchor[key])):
            raise ValueError('Plain original prefix/suffix tokens required')
    if (len(anchor['prefix_ids']) + len(anchor['suffix_ids']) > MAXIMUM - 1
            or anchor['prefix_sha256'] != ids_digest(anchor['prefix_ids'])
            or anchor['suffix_sha256'] != ids_digest(anchor['suffix_ids'])):
        raise ValueError('Original context bound/token identities differ')


def likelihood_row(prefix, suffix):
    """Only suffix body labels; prefix/BOS ignored, no added EOS or markers."""
    return dict(input_ids=[2] + prefix + suffix[:-1], target_ids=[-100] * len(prefix) + suffix)


class ContextFIFO:
    def __init__(self, binding):
        self.binding = copy.deepcopy(binding)
        self.entries = []
        self.committed_anchors = 0

    def select(self, anchors):
        for anchor in anchors:
            validate_anchor(anchor)
        pairs = []
        for anchor in anchors:
            # Oldest matching context, independent of model losses; no reroll.
            candidate = next((entry for entry in self.entries
                if entry['source'] == anchor['source']
                and len(entry['prefix_ids']) == len(anchor['prefix_ids'])
                and entry['source_family'] != anchor['source_family']
                and entry['body_sha256'] != anchor['body_sha256']
                and entry['prefix_sha256'] != anchor['prefix_sha256']
                and entry['suffix_sha256'] != anchor['suffix_sha256']), None)
            if candidate is None:
                continue
            pairs.append(dict(source=anchor['source'], source_family=anchor['source_family'],
                positive_body_sha256=anchor['body_sha256'], negative_body_sha256=candidate['body_sha256'],
                positive_prefix_sha256=anchor['prefix_sha256'], negative_prefix_sha256=candidate['prefix_sha256'],
                suffix_sha256=anchor['suffix_sha256'], prefix_tokens=len(anchor['prefix_ids']),
                suffix_tokens=len(anchor['suffix_ids']),
                positive=likelihood_row(anchor['prefix_ids'], anchor['suffix_ids']),
                negative=likelihood_row(candidate['prefix_ids'], anchor['suffix_ids'])))
        return pairs

    def commit(self, anchors):
        """Call only after the owner's Adam update completed successfully."""
        for anchor in anchors:
            validate_anchor(anchor)
        entries = copy.deepcopy(self.entries)
        for anchor in anchors:
            entries = [entry for entry in entries if entry['source_family'] != anchor['source_family']
                       and entry['body_sha256'] != anchor['body_sha256']]
            entries.append({key: copy.deepcopy(value) for key, value in anchor.items() if key != 'suffix_ids'})
            entries = entries[-CAPACITY:]
        self.entries = entries
        self.committed_anchors += len(anchors)

    def state_dict(self):
        return dict(kind=KIND, binding=copy.deepcopy(self.binding), capacity=CAPACITY,
                    committed_anchors=self.committed_anchors, entries=copy.deepcopy(self.entries))

    def load_state_dict(self, state):
        if (set(state) != {'kind', 'binding', 'capacity', 'committed_anchors', 'entries'}
                or state['kind'] != KIND or state['binding'] != self.binding or state['capacity'] != CAPACITY
                or type(state['committed_anchors']) is not int or state['committed_anchors'] < 0
                or not isinstance(state['entries'], list)
                or len(state['entries']) > min(CAPACITY, state['committed_anchors'])):
            raise ValueError('Completed context FIFO recipe/binding/counters required')
        families, bodies = set(), set()
        for entry in state['entries']:
            if (set(entry) != {'source', 'source_family', 'body_sha256', 'prefix_ids', 'prefix_sha256', 'suffix_sha256'}
                    or entry['source'] not in GENRES or not isinstance(entry['source_family'], str)
                    or not entry['source_family'] or entry['source_family'] in families
                    or entry['body_sha256'] in bodies or not isinstance(entry['prefix_ids'], list)
                    or not 16 <= len(entry['prefix_ids']) <= MAXIMUM - 17
                    or any(type(i) is not int or not 8 <= i < 4096 for i in entry['prefix_ids'])
                    or ids_digest(entry['prefix_ids']) != entry['prefix_sha256']):
                raise ValueError('Original committed context FIFO identities differ')
            for key in ('body_sha256', 'prefix_sha256', 'suffix_sha256'):
                require_digest(entry[key])
            families.add(entry['source_family'])
            bodies.add(entry['body_sha256'])
        self.entries = copy.deepcopy(state['entries'])
        self.committed_anchors = state['committed_anchors']


def pair_loss(positive, negative):
    """FP32 pairwise logistic contrast of conditional suffix log-likelihoods.

    Same suffix and exactly equal prefix length remove suffix-only priors and
    position-count cues. This does not certify the distractor is nonsensical.
    """
    import torch
    from torch.nn import functional as F
    if (positive.ndim != 1 or positive.shape != negative.shape or not positive.numel()
            or not bool(torch.isfinite(positive).all()) or not bool(torch.isfinite(negative).all())):
        raise ValueError('Nonempty paired finite suffix likelihood vectors required')
    with torch.autocast(positive.device.type, enabled=False):
        return F.softplus(negative.float() - positive.float()).mean()
