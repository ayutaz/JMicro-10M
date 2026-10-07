from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import base_native_teacher_KD_compiled as compiled
import base_native_teacher_KD_trainer as eager
from test_base_native_teacher_KD import builders
from jmicro.phase5 import equal_state
from natural_context_contrast_trainer import host


@pytest.fixture
def dispatch(monkeypatch):
    calls = []
    def factory(fn, **kwargs):
        assert fn is compiled.ORIGINAL_HIDDEN
        assert kwargs == dict(backend='inductor', mode='default', dynamic=True, fullgraph=True)
        def hidden(model, ids):
            calls.append((model, tuple(ids.shape)))
            return fn(model, ids)
        return hidden
    monkeypatch.setattr(compiled, '_compiled_hidden', None)
    monkeypatch.setattr(torch, 'compile', factory)
    return calls


def builder(tmp_path):
    p, teacher, original = builders(tmp_path)
    def build():
        t = original()
        return compiled.CompiledNativeTeacherKDTrainer(p, t.sampler, t.binding,
            teacher, t.spec['teacher'], batch=4, device='cpu')
    return build, original


def test_dispatch_restored_bare_weights_teacher_only_and_recipe(dispatch, tmp_path):
    build, original = builder(tmp_path)
    t, reference = build(), original()
    a, b = t.step(), reference.step()
    assert eager.right_padded_hidden is compiled.ORIGINAL_HIDDEN
    assert len(dispatch) == 2 and {id(x[0]) for x in dispatch} == {id(t.model), id(t.teacher)}
    assert equal_state(host(t.model.state_dict()), host(reference.model.state_dict()))
    assert equal_state(a['native_teacher_KD'], b['native_teacher_KD'])
    assert not any('_orig_mod' in k for k in t.state_dict()['model'])
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    assert t.spec['hidden_execution'] == compiled.RECIPE


def test_dispatch_restores_on_compiler_failure_no_eager_fallback(dispatch, tmp_path):
    build, _ = builder(tmp_path)
    t = build()
    def fail(*args): raise RuntimeError('compiler failure fixture')
    t._hidden = fail
    with pytest.raises(RuntimeError, match='compiler failure fixture'): t.step()
    assert eager.right_padded_hidden is compiled.ORIGINAL_HIDDEN
    assert t.counters['update'] == 0 and not dispatch


def test_compiled_route_saved_resume_all_state(dispatch, tmp_path):
    build, _ = builder(tmp_path)
    t = build()
    for _ in range(4): t.step()
    expected = host(t.state_dict())
    split = build()
    for _ in range(2): split.step()
    split.save(tmp_path / 'split.pt')
    resumed = build(); resumed.load(tmp_path / 'split.pt')
    for _ in range(2): resumed.step()
    assert equal_state(expected, host(resumed.state_dict()))


@pytest.mark.parametrize('other', ['eager', 'different_recipe'])
def test_cross_implementation_resume_rejected(dispatch, tmp_path, other):
    build, original = builder(tmp_path)
    t = original() if other == 'eager' else build()
    t.step()
    state = host(t.state_dict())
    if other == 'different_recipe': state['spec']['hidden_execution']['dynamic'] = False
    torch.save(state, tmp_path / 'wrong.pt')
    with pytest.raises(ValueError): build().load(tmp_path / 'wrong.pt')
