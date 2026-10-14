"""Prospective objective arithmetic, original targets, and saved-context state."""
import copy
import hashlib
import math

import pytest
import torch

from jmicro.context_likelihood import (CAPACITY, ContextFIFO, ids_digest, original_anchors, pair_loss)


def anchor(i=0, source='web', prefix_length=20):
    prefix, suffix = [65 + i] * prefix_length, [100 + i] * 20
    return dict(source=source, source_family=f'fixture-{i}', body_sha256=hashlib.sha256(bytes(prefix + suffix)).hexdigest(),
                prefix_ids=prefix, suffix_ids=suffix, prefix_sha256=ids_digest(prefix), suffix_sha256=ids_digest(suffix))


def test_same_suffix_positions_and_body_targets_only():
    memory = ContextFIFO({'fixture': True})
    memory.commit([anchor(0)])
    assert memory.select([anchor(1)])[0]['suffix_tokens'] == 20
    pair = memory.select([anchor(1)])[0]
    left, right = pair['positive'], pair['negative']
    assert left['target_ids'] == right['target_ids'] == [-100] * 20 + [101] * 20
    assert len(left['input_ids']) == len(right['input_ids']) == 40
    assert left['input_ids'] == [2] + [66] * 20 + [101] * 19
    assert right['input_ids'] == [2] + [65] * 20 + [101] * 19
    assert 3 not in left['target_ids'] and 3 not in right['target_ids']


def test_no_current_batch_contexts_and_exact_source_length_family_exclusions():
    memory = ContextFIFO({'fixture': True})
    assert memory.select([anchor(0), anchor(1)]) == []
    memory.commit([anchor(0)])
    assert memory.select([anchor(0)]) == []
    assert memory.select([anchor(1, source='story')]) == []
    assert memory.select([anchor(1, prefix_length=21)]) == []
    duplicate_prefix = anchor(1)
    duplicate_prefix['prefix_ids'] = anchor(0)['prefix_ids']
    duplicate_prefix['prefix_sha256'] = ids_digest(duplicate_prefix['prefix_ids'])
    assert memory.select([duplicate_prefix]) == []


def test_oldest_matching_context_and_saved_FIFO_resume_are_identical():
    memory = ContextFIFO({'fixture': True})
    memory.commit([anchor(0), anchor(1)])
    saved = memory.state_dict()
    resumed = ContextFIFO({'fixture': True})
    resumed.load_state_dict(saved)
    assert memory.select([anchor(2)]) == resumed.select([anchor(2)])
    assert memory.select([anchor(2)])[0]['negative_body_sha256'] == anchor(0)['body_sha256']
    memory.commit([anchor(2)])
    resumed.commit([anchor(2)])
    assert memory.state_dict() == resumed.state_dict()
    saved['entries'][0]['prefix_ids'][0] = 12
    assert memory.state_dict() == resumed.state_dict()  # Snapshot is not an alias.


def test_capacity_eviction_and_repeated_family_do_not_create_duplicate_entries():
    memory = ContextFIFO({'fixture': True})
    for i in range(CAPACITY + 2):
        a = anchor(i)
        memory.commit([a])
    state = memory.state_dict()
    assert len(state['entries']) == CAPACITY and state['committed_anchors'] == CAPACITY + 2
    assert state['entries'][0]['body_sha256'] == anchor(2)['body_sha256']
    memory.commit([anchor(2)])
    assert len(memory.entries) == CAPACITY and memory.entries[-1]['body_sha256'] == anchor(2)['body_sha256']


@pytest.mark.parametrize('bad', ['binding', 'capacity', 'prefix', 'duplicate', 'counter'])
def test_invalid_saved_FIFO_rejected_before_mutation(bad):
    memory = ContextFIFO({'fixture': True})
    memory.commit([anchor(0), anchor(1)])
    before, saved = memory.state_dict(), memory.state_dict()
    if bad == 'binding': saved['binding'] = {'wrong': True}
    elif bad == 'capacity': saved['capacity'] = 129
    elif bad == 'prefix': saved['entries'][0]['prefix_ids'][0] = 12
    elif bad == 'duplicate': saved['entries'][1] = copy.deepcopy(saved['entries'][0])
    else: saved['committed_anchors'] = 0
    with pytest.raises(ValueError):
        memory.load_state_dict(saved)
    assert memory.state_dict() == before


def test_pairwise_logistic_loss_and_gradient_signs_and_prior_cancellation():
    positive = torch.tensor([-2., -3.], requires_grad=True)
    negative = torch.tensor([-3., -2.], requires_grad=True)
    loss = pair_loss(positive, negative)
    assert float(loss.detach()) == pytest.approx((math.log1p(math.exp(-1)) + math.log1p(math.exp(1))) / 2)
    loss.backward()
    assert torch.all(positive.grad < 0) and torch.all(negative.grad > 0)
    assert torch.equal(positive.grad, -negative.grad)
    prior = torch.tensor([-7., -13.])
    assert torch.equal(loss.detach(), pair_loss(positive.detach() + prior, negative.detach() + prior))


def test_nonfinite_scores_and_invalid_commit_cannot_produce_a_valid_state():
    with pytest.raises(ValueError):
        pair_loss(torch.tensor([float('nan')]), torch.tensor([-1.]))
    with pytest.raises(ValueError):
        pair_loss(torch.tensor([]), torch.tensor([]))
    memory = ContextFIFO({'fixture': True})
    before = memory.state_dict()
    bad = anchor(0)
    bad['prefix_ids'][0] = 3
    with pytest.raises(ValueError):
        memory.commit([anchor(1), bad])
    assert memory.state_dict() == before


def test_anchors_recover_original_joint_suffix_and_do_not_mutate_main_CE():
    class Codec:
        def decode_bytes(self, ids): return bytes(ids)
        def encode(self, text): return list(text.encode())
    a = anchor(0)
    row = dict(source='web', source_family=a['source_family'], original_document_first_window=True,
               full_original_body_sha256=a['body_sha256'], prefix_ids=a['prefix_ids'], suffix_ids=a['suffix_ids'],
               original_body_tokens=40, teacher_tokens=41,
               input_ids=[2] + a['prefix_ids'] + a['suffix_ids'], target_ids=[65] * 20 + [100] * 20 + [3])
    before = copy.deepcopy(row)
    assert original_anchors([row, row], Codec()) == [a]
    assert row == before
    broken = copy.deepcopy(row)
    broken['full_original_body_sha256'] = '0' * 64
    with pytest.raises(ValueError):
        original_anchors([broken], Codec())
    partial = copy.deepcopy(row)
    partial['teacher_tokens'] = 40
    partial['target_ids'][-1] = -100
    assert original_anchors([partial], Codec()) == []
    long = copy.deepcopy(row)
    long['original_body_tokens'] = 512
    long['teacher_tokens'] = 512
    assert original_anchors([long], Codec()) == []
