"""Small protocol fixtures; no trained GPU or quality evidence."""
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from run_natural_context_contrast_dev_transfer import fixed_body_rows, make_pairs, retrieval


class ByteCodec:
    def decode_bytes(self, ids):
        return bytes(i - 8 for i in ids)


def test_real_section_wrapper_binds_DEV_cache_to_checkpoint():
    cache = dict(binding=json.dumps(dict(checkpoint_sha256='frozen')),
        body=dict(split='dev', documents=2, rows=[dict(doc_id='a'), dict(doc_id='b')]))
    assert len(fixed_body_rows(cache, 'frozen', count=2)) == 2
    with pytest.raises(ValueError, match='DEV body cache'):
        fixed_body_rows(cache, 'other', count=2)
    cache['body']['split'] = 'test'
    with pytest.raises(ValueError, match='DEV body cache'):
        fixed_body_rows(cache, 'frozen', count=2)


def fixture(texts):
    rows, expected, stream = [], [], []
    for i, text in enumerate(texts):
        raw = text.encode('utf-8')
        body = [b + 8 for b in raw]
        row = dict(doc_id=f'doc-{i}', split='dev', body_tokens=len(body), bytes=len(raw),
            offset=len(stream), canonical_sha256=hashlib.sha256(raw).hexdigest())
        rows.append(row)
        expected.append(dict(doc_id=row['doc_id'], body_tokens=len(body), body_bytes=len(raw)))
        stream.extend([2, *body, 3])
    return rows, np.asarray(stream, dtype='<u2'), expected


def test_fixed_order_unique_original_bytes_and_UTF8_boundary():
    docs, stream, expected = fixture(['short', 'aaaaaaaあbbbbbbbb',
        'aaaaaaaあbbbbbbbb', 'abcdefghijklmnopq'])
    rows, excluded = make_pairs(docs, stream, ByteCodec(), expected, limit=2)
    assert [row['doc_id'] for row in rows] == ['doc-1', 'doc-3']
    assert rows[0]['token_cut'] == 10  # UTF8 midpoint is inside the Japanese character.
    assert excluded == {'body_length_not_executable': 1, 'exact_body_duplicate': 1}
    for row in rows:
        raw = ByteCodec().decode_bytes(row['prefix_ids'] + row['suffix_ids'])
        assert hashlib.sha256(raw).hexdigest() == row['body_sha256']
        assert ByteCodec().decode_bytes(row['prefix_ids']).decode('utf-8')
        assert ByteCodec().decode_bytes(row['suffix_ids']).decode('utf-8')
        assert row['appended_EOS'] is False


def test_other_split_accounting_or_body_corruption_rejected():
    docs, stream, expected = fixture(['abcdefghijklmnopq', 'ABCDEFGHIJKLMNOPQ'])
    docs[1]['split'] = 'test'
    with pytest.raises(ValueError, match='Fixed DEV'):
        make_pairs(docs, stream, ByteCodec(), expected, limit=1)
    docs[1]['split'] = 'dev'
    expected[0]['body_bytes'] += 1
    with pytest.raises(ValueError, match='Fixed DEV'):
        make_pairs(docs, stream, ByteCodec(), expected, limit=1)
    expected[0]['body_bytes'] -= 1
    stream[1] += 1
    with pytest.raises(ValueError, match='body bytes'):
        make_pairs(docs, stream, ByteCodec(), expected, limit=1)


def test_pair_permutation_and_ties_are_not_unique_retrieval_success():
    rows = [dict(doc_id=str(i)) for i in range(4)]
    identity = torch.eye(4)
    correct = retrieval(identity, identity, rows)
    wrong = retrieval(identity, identity.flip(0), rows)
    ties = retrieval(torch.ones(4, 4), torch.ones(4, 4), rows)
    assert correct['bidirectional_unique_top1'] == 1
    assert wrong['bidirectional_unique_top1'] == 0
    assert wrong['symmetric_InfoNCE'] > correct['symmetric_InfoNCE']
    assert ties['bidirectional_unique_top1'] == 0
    assert all(row['prefix_positive_ties'] == 4 for row in ties['rows'])
    with pytest.raises(ValueError, match='Nonfinite'):
        retrieval(torch.full((4, 4), float('nan')), identity, rows)
