import importlib.util
from pathlib import Path
from types import SimpleNamespace
import torch

spec = importlib.util.spec_from_file_location('signal', Path(__file__).parents[1]/'scripts/teacher_semantic_signal.py')
signal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(signal)


def test_causal_shift_excludes_context_and_padding():
    class Fixture:
        def __call__(self, input_ids, attention_mask, use_cache):
            assert not use_cache and attention_mask.tolist() == [[True, True, True], [True, False, False]]
            logits = torch.zeros((*input_ids.shape, 8))
            logits[0, 1, 3] = 3
            logits[0, 2, 4] = 2
            logits[1, 0, 5] = 1
            return SimpleNamespace(logits=logits)
    encoded = [dict(ids=[7,2,3,4],context_tokens=2,target_ids=[3,4],target_bytes=6),
        dict(ids=[7,5],context_tokens=1,target_ids=[5],target_bytes=3)]
    scores = signal.hf_scores(Fixture(), encoded, 'cpu')
    assert [s['target_tokens'] for s in scores] == [2,1]
    assert scores[0]['log_likelihood'] < 0 and len(scores[0]['token_nll']) == 2
    assert all(s['is_greedy'] for s in scores)


def test_byte_drift_and_static_preference_do_not_prove_context_signal():
    case = dict(id='a',family='pair',category='x',context='p\n',choices=['yes','no'],label=0)
    values = [dict(log_likelihood=-1,target_tokens=1,target_bytes=3),dict(log_likelihood=-2,target_tokens=1,target_bytes=2)]
    one = signal.case_scores(case, values)
    two = signal.case_scores(dict(case,id='b',context='q\n',label=1),values)
    result = signal.summary([one,two])
    assert result['accuracy']['point'] == .5
    assert result['both_contexts_hard_correct']['point'] == 0
    changed = signal.case_scores(case,[dict(values[0],target_bytes=4),values[1]])
    import pytest
    with pytest.raises(ValueError,match='UTF8 bytes'):
        signal.compare([one],[changed])
