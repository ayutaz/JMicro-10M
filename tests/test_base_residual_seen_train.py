"""History-conditioning protocol fixtures, not model-quality evidence."""
from pathlib import Path
import sys
from types import SimpleNamespace
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parents[1] / 'scripts')]
import pytest
import torch
from run_base_residual_seen_train import history


class Codec:
    def decode_bytes(self, ids):
        return ''.join('x' if n == 9 else 'y' for n in ids if n != 3).encode()


class Model:
    def __init__(self, always_EOS=False, nan=False):
        self.always_EOS, self.nan = always_EOS, nan
        self.inputs = []

    def __call__(self, current, cache=None, use_cache=False):
        ids = current.tolist()[0]
        self.inputs.append(ids)
        prefix = (cache or []) + ids
        logits = torch.zeros(1, len(ids), 16)
        logits[:, :, 3 if self.always_EOS or ids[-1] == 10 else 9] = 2
        if self.nan:
            logits[:, :, 11] = torch.nan
        return SimpleNamespace(logits=logits, cache=prefix)


def test_gold_and_free_have_same_first_prediction_but_feed_different_history():
    unit = dict(prompt_ids=[2,8], continuation_gold_ids=[10,3])
    a, b = Model(), Model()
    teacher = history(a, Codec(), unit, True, 'cpu', lambda: None)
    free = history(b, Codec(), unit, False, 'cpu', lambda: None)
    assert teacher['steps'][0] == free['steps'][0]
    assert teacher['fed_ids'] == [10,3] and teacher['predicted_ids'] == [9,3]
    assert a.inputs[1] == [10] and b.inputs[1] == [9]
    assert teacher['stop_reason'] == 'original_gold_EOS'
    assert free['stop_reason'] == 'max_new_tokens' and len(free['fed_ids']) == 64


def test_teacher_does_not_stop_at_predicted_early_EOS():
    unit = dict(prompt_ids=[2,8], continuation_gold_ids=[10,11,3])
    teacher = history(Model(always_EOS=True), Codec(), unit, True, 'cpu', lambda: None)
    free = history(Model(always_EOS=True), Codec(), unit, False, 'cpu', lambda: None)
    assert teacher['fed_ids'] == [10,11,3] and len(teacher['steps']) == 3
    assert free['fed_ids'] == [3] and free['stop_reason'] == 'stop_id'


def test_no_artificial_EOS_at_fragment_or64_cap():
    unit = dict(prompt_ids=[2,8], continuation_gold_ids=[10]*100)
    result = history(Model(), Codec(), unit, True, 'cpu', lambda: None)
    assert len(result['fed_ids']) == 64 and 3 not in result['fed_ids']
    assert not any(step['actual_gold_EOS'] for step in result['steps'])
    assert result['stop_reason'] == 'max_new_tokens'


def test_nonfinite_logits_are_rejected():
    with pytest.raises(ValueError, match='Finite'):
        history(Model(nan=True), Codec(), dict(prompt_ids=[2,8], continuation_gold_ids=[10,3]), True, 'cpu', lambda: None)


def test_deadline_checked_before_each_prediction():
    def expired():
        raise TimeoutError('expired')
    model = Model()
    with pytest.raises(TimeoutError):
        history(model, Codec(), dict(prompt_ids=[2,8], continuation_gold_ids=[10,3]), False, 'cpu', expired)
    assert not model.inputs
