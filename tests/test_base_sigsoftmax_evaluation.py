"""Actual CPU likelihood/wiring checks; not GPU or Japanese quality evidence."""
import copy
from pathlib import Path
import sys
import pytest
import torch
from torch.nn import functional as F
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import base_sigsoftmax_evaluation as linked
from base_sigsoftmax_model import LINK, SigSoftmaxModel, sigsoftmax_logits
from jmicro.experiment import read_json
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from test_natural_context_contrast_corpus import parent, FixtureCodec


def record():
    return dict(output_probability_link=LINK, model_config={'output_probability_link': LINK})


def call(tmp_path, trained=None):
    return linked.evaluate('fixture', trained if trained is not None else record(),
        None, None, {}, {}, lambda *a, **k: None, lambda: None, 0, tmp_path)


def test_scoped_factory_actual_CPU_likelihood_cache_and_persisted_tag(tmp_path, monkeypatch):
    original_factory, original_run = linked.native.JMicroModel, linked.native.RUN
    saved = parent()
    config = copy.deepcopy(saved['model_config'])
    config['output_probability_link'] = LINK
    def evaluate(*args):
        assert linked.native.RUN == tmp_path
        model = linked.native.JMicroModel(config).eval()
        assert isinstance(model, SigSoftmaxModel)
        model.load_state_dict(saved['model'], strict=True)
        raw = JMicroModel(saved['model_config']).eval()
        raw.load_state_dict(saved['model'], strict=True)
        ids = torch.tensor([[2, 65, 66]])
        with torch.no_grad():
            scores = raw(ids).logits
            assert torch.equal(model(ids).logits, sigsoftmax_logits(scores))
            prefill = model(ids[:, :2], use_cache=True)
            cached = model(ids[:, 2:], cache=prefill.cache, use_cache=True)
            assert torch.allclose(cached.logits, model(ids).logits[:, 2:], atol=1e-6)
        scorer = NativeLikelihood(model, FixtureCodec(), device='cpu', dtype='fp32')
        result = scorer.score([('A', 'B')])[0]
        independent_scores = scores[0, 1].double()
        probability = independent_scores.exp() * independent_scores.sigmoid()
        expected = (probability[66] / probability.sum()).log().item()
        assert result['log_likelihood'] == pytest.approx(expected, abs=1e-6)
        return dict(body={'fixture_log_likelihood': result['log_likelihood']})
    monkeypatch.setattr(linked.native, 'evaluate', evaluate)
    result = call(tmp_path)
    assert result['output_probability_link'] == LINK
    assert result['linked_head_used_for_full_cache_generation_and_likelihood'] is True
    assert read_json(tmp_path/'fixture/evaluation/result.json') == result
    assert (linked.native.JMicroModel, linked.native.RUN) == (original_factory, original_run)


@pytest.mark.parametrize('field', ['output_probability_link', 'model_config'])
def test_wrong_record_tag_rejected_before_evaluation(tmp_path, monkeypatch, field):
    def forbidden(*args):
        pytest.fail('Wrong checkpoint must not reach evaluator')
    monkeypatch.setattr(linked.native, 'evaluate', forbidden)
    trained = record()
    trained[field] = 'wrong' if field == 'output_probability_link' else {}
    with pytest.raises(ValueError, match='tagged'):
        call(tmp_path, trained)


def test_untagged_terminal_not_reused(tmp_path, monkeypatch):
    atomic_json(tmp_path/'fixture/evaluation/result.json', {'output_probability_link': 'ordinary'})
    monkeypatch.setattr(linked.native, 'evaluate', lambda *args: pytest.fail('Refuse old evaluation'))
    with pytest.raises(ValueError, match='untagged'):
        call(tmp_path)


def test_failure_restores_original_factory_and_root(tmp_path, monkeypatch):
    original = linked.native.JMicroModel, linked.native.RUN
    def fail(*args):
        assert linked.native.JMicroModel is SigSoftmaxModel
        raise RuntimeError('fixture interrupted evaluation')
    monkeypatch.setattr(linked.native, 'evaluate', fail)
    with pytest.raises(RuntimeError, match='interrupted'):
        call(tmp_path)
    assert (linked.native.JMicroModel, linked.native.RUN) == original
    assert not (tmp_path/'fixture/evaluation/result.json').exists()
