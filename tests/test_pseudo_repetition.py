import copy
import hashlib
import math

import pytest
import torch

from jmicro.pseudo_repetition import (repeat_rows, sentence_repeat_row,
                                     repetition_decay_loss)


class ByteCodec:
    def encode(self, text):
        return [byte + 8 for byte in text.encode()]

    def decode_bytes(self, ids):
        return bytes(token - 8 for token in ids)


def original(text='最初の文章です。次の文章を書きます。最後も原文です。', family='one'):
    codec = ByteCodec()
    body = codec.encode(text)
    return dict(original_document_first_window=True, original_body_tokens=len(body),
        teacher_tokens=len(body) + 1, input_ids=[2] + body, target_ids=body + [3],
        full_original_body_sha256=hashlib.sha256(text.encode()).hexdigest(),
        source='web', source_family=family)


def scores_with_probabilities(probs, dtype=torch.float64):
    values = torch.zeros(len(probs), 4096, dtype=dtype)
    for row, probability in enumerate(probs):
        values[row, 8] = math.log(probability / (1 - probability) * 4095)
    return values.requires_grad_()


def test_original_joint_tokens_context_shift_whole_copies_and_no_mutation():
    codec, row = ByteCodec(), original()
    saved = copy.deepcopy(row)
    state = torch.get_rng_state().clone()
    built = sentence_repeat_row(row, codec)
    width, start = built['sentence_tokens'], built['prefix_tokens']
    sequence = built['input_ids'] + built['target_ids'][-1:]
    assert sequence == [2] + row['input_ids'][1:1+start] + row['input_ids'][1+start:1+start+width] * built['copies']
    assert 4 <= built['copies'] <= 16 and len(built['input_ids']) <= 512
    assert built['target_ids'] == sequence[1:]
    assert all(built['target_ids'][i] == built['target_ids'][j]
               for i, j in zip(built['current_positions'], built['previous_positions']))
    assert min(built['current_positions']) == start + width
    assert max(built['current_positions']) == len(built['target_ids']) - 1
    assert 3 not in built['target_ids'] and 2 not in built['target_ids']
    assert row == saved and torch.equal(state, torch.get_rng_state())


def test_partial_long_nonhead_and_missing_sentence_are_skipped_not_truncated():
    codec = ByteCodec()
    for changes in ({'original_document_first_window': False}, {'teacher_tokens': 1},
                    {'original_body_tokens': 512}):
        row = original()
        row.update(changes)
        assert sentence_repeat_row(row, codec) is None
    assert sentence_repeat_row(original('句読点もない文章をここに書きます'), codec) is None
    assert sentence_repeat_row(original('短。短。'), codec) is None


def test_earliest_sentence_original_order_distinct_families_and_eight_cap():
    rows = [original(family=str(i)) for i in range(12)]
    # Same body is excluded even across families. Different complete sentences
    # retain deterministic original order rather than selection by model loss.
    for i, row in enumerate(rows):
        rows[i] = original('最初の文章です。次の文章を書きます。原文の番号は'+str(i)+'です。', str(i))
    rows.insert(1, copy.deepcopy(rows[0]))
    selected = repeat_rows(rows, ByteCodec())
    assert len(selected) == 8
    assert [row['source_family'] for row in selected] == [str(i) for i in range(8)]
    assert all(row['sentence_sha256'] == hashlib.sha256('次の文章を書きます。'.encode()).hexdigest() for row in selected)


def test_broken_original_bytes_or_targets_rejected():
    codec = ByteCodec()
    for changes in ({'full_original_body_sha256': '0'*64}, {'target_ids': [8, 3]}):
        row = original()
        row.update(changes)
        with pytest.raises(ValueError):
            sentence_repeat_row(row, codec)


def test_sentence_boundary_inside_original_token_is_not_reencoded():
    class ChunkCodec:
        def __init__(self, text):
            raw = text.encode()
            self.pieces = {i+300: raw[start:start+4]
                           for i, start in enumerate(range(0, len(raw), 4))}
            self.text = text

        def encode(self, text):
            assert text == self.text  # Encoding a sentence fragment is forbidden.
            return list(self.pieces)

        def decode_bytes(self, ids):
            return b''.join(self.pieces[i] for i in ids)

    text = '一文です。二文です。'
    codec = ChunkCodec(text)
    row = original(text)
    body = codec.encode(text)
    row.update(original_body_tokens=len(body), teacher_tokens=len(body)+1,
               input_ids=[2]+body, target_ids=body+[3])
    assert sentence_repeat_row(row, codec) is None


def test_independent_probability_formula_and_detached_previous_occurrence():
    probs = [.8, .6, .2]
    scores = scores_with_probabilities(probs)
    targets = torch.full((3,), 8, dtype=torch.long)
    loss = repetition_decay_loss(scores, targets, [1, 2], [0, 1])
    expected = (-math.log(1 - abs(.6 - .5*.8)) - math.log(1 - abs(.2 - .5*.6))) / 2
    assert loss.item() == pytest.approx(expected, abs=1e-13)
    loss.backward()
    assert torch.equal(scores.grad[0], torch.zeros(4096, dtype=torch.float64))
    # p1 gets only its own comparison's derivative; its target for p2 is detached.
    assert scores.grad[1, 8].item() == pytest.approx(.6*.4/(1-(.6-.4))/2)
    assert scores.grad[2, 8].item() == pytest.approx(-.2*.8/(1-(.3-.2))/2)


def test_target_is_not_zero_and_low_probability_is_raised():
    scores = scores_with_probabilities([.8, .1])
    loss = repetition_decay_loss(scores, torch.tensor([8, 8]), [1], [0])
    loss.backward()
    # DITTO differs from zero-target UL: under target .4, increase current p.
    assert scores.grad[1, 8] < 0
    assert torch.count_nonzero(scores.grad[0]) == 0


def test_extreme_saturation_finite_without_clamp_and_corrective_gradient():
    scores = torch.zeros(2, 4096)
    scores[0, 8], scores[1, 8] = -1000, 1000
    scores.requires_grad_()
    loss = repetition_decay_loss(scores, torch.tensor([8, 8]), [1], [0])
    loss.backward()
    assert torch.isfinite(loss) and loss > 900
    assert torch.isfinite(scores.grad).all() and scores.grad[1, 8] > .99
    assert torch.count_nonzero(scores.grad[0]) == 0


@pytest.mark.parametrize('bad', ['mismatched_ids', 'EOS', 'bad_indices', 'duplicate', 'nan', 'bad_vocab'])
def test_invalid_pseudo_pairs_rejected(bad):
    scores = scores_with_probabilities([.5, .8, .7])
    targets, current, previous = torch.tensor([8, 8, 8]), [1, 2], [0, 1]
    if bad == 'mismatched_ids':
        targets[1] = 9
    elif bad == 'EOS':
        targets[:] = 3
    elif bad == 'bad_indices':
        previous[0] = 2
    elif bad == 'duplicate':
        current = [1, 1]
        previous = [0, 0]
    elif bad == 'nan':
        scores = scores.detach()
        scores[0, 0] = torch.nan
    else:
        scores = scores[:, :16]
    with pytest.raises(ValueError):
        repetition_decay_loss(scores, targets, current, previous)
