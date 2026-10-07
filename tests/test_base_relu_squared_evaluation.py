"""Actual CPU likelihood and typed wiring; not GPU or Japanese quality."""
import copy
import sys
from pathlib import Path

import pytest
import torch
from torch.nn import functional as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import base_relu_squared_evaluation as typed
from base_relu_squared_model import POLICY, squared_config, SquaredReLUModel
from jmicro.experiment import read_json
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.training import atomic_json
from test_natural_context_contrast_corpus import parent, FixtureCodec


def record(arm='ReLU_squared'):
    config = parent()['model_config']
    if arm == 'ReLU_squared':
        config = squared_config(config)
    return dict(ffn_variant=arm, ffn_policy=POLICY, model_config=config,
                FFN_model_class='SquaredReLUModel' if arm == 'ReLU_squared' else 'JMicroModel')


def call(tmp_path, trained=None):
    trained = trained if trained is not None else record()
    return typed.evaluate(trained['ffn_variant'], trained, None, None, {}, {},
        lambda *a, **k: None, lambda: None, 0, tmp_path)


@pytest.mark.parametrize('arm', ['SwiGLU', 'ReLU_squared'])
def test_scoped_factory_actual_likelihood_full_cache_and_metadata(tmp_path, monkeypatch, arm):
    original = typed.native.JMicroModel, typed.native.RUN
    trained = record(arm)
    def evaluate(*args):
        assert typed.native.RUN == tmp_path
        model = typed.native.JMicroModel(trained['model_config']).eval()
        assert isinstance(model, SquaredReLUModel) == (arm == 'ReLU_squared')
        ids = torch.tensor([[2, 65, 66]])
        with torch.no_grad():
            logits = model(ids).logits
            first = model(ids[:, :2], use_cache=True)
            cached = model(ids[:, 2:], cache=first.cache, use_cache=True)
            assert torch.allclose(cached.logits, logits[:, 2:], atol=1e-6)
            independent = -F.cross_entropy(logits[0, 1].double()[None], torch.tensor([66])).item()
        actual = NativeLikelihood(model, FixtureCodec(), device='cpu', dtype='fp32').score([('A', 'B')])[0]
        assert actual['log_likelihood'] == pytest.approx(independent, abs=1e-6)
        return dict(body={'fixture_log_likelihood': actual['log_likelihood']})
    monkeypatch.setattr(typed.native, 'evaluate', evaluate)
    result = call(tmp_path, trained)
    assert result['native_likelihood_cache_and_greedy_use_same_FFN'] is True
    assert read_json(tmp_path / arm / 'evaluation/result.json') == result
    assert (typed.native.JMicroModel, typed.native.RUN) == original


@pytest.mark.parametrize('field', ['ffn_policy', 'model_config', 'FFN_model_class'])
def test_wrong_metadata_refused_before_evaluation(tmp_path, monkeypatch, field):
    trained = copy.deepcopy(record())
    trained[field] = {} if field != 'FFN_model_class' else 'JMicroModel'
    monkeypatch.setattr(typed.native, 'evaluate', lambda *a: pytest.fail('Invalid FFN reached evaluator'))
    with pytest.raises(ValueError): call(tmp_path, trained)


def test_legacy_terminal_and_failure_restore_factory(tmp_path, monkeypatch):
    original = typed.native.JMicroModel, typed.native.RUN
    terminal = tmp_path / 'ReLU_squared/evaluation/result.json'
    atomic_json(terminal, {'ffn_variant': 'SwiGLU'})
    monkeypatch.setattr(typed.native, 'evaluate', lambda *a: pytest.fail('Legacy result reused'))
    with pytest.raises(ValueError, match='legacy'): call(tmp_path)
    terminal.unlink()
    def fail(*args):
        assert typed.native.JMicroModel is typed.model_from_config
        raise RuntimeError('Fixture interrupted evaluation')
    monkeypatch.setattr(typed.native, 'evaluate', fail)
    with pytest.raises(RuntimeError, match='interrupted'): call(tmp_path)
    assert (typed.native.JMicroModel, typed.native.RUN) == original
    assert not terminal.exists()
