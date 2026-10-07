"""FFN mathematics, causal/cache paths, paired gold and committed resume state."""
import copy
import json
import sys
from pathlib import Path

import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from base_relu_squared_model import (SquaredReLUMLP, SquaredReLUModel, squared_config,
                                     model_from_config, native_config)
from base_relu_squared_trainer import FreshFFNTrainer, committed_state
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.training import rng_state
from test_natural_context_contrast_corpus import fixture_pool, FixtureCodec, parent


def builders(tmp_path):
    pool = tmp_path / 'pool'
    manifest = fixture_pool(pool)
    config = copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
    configs = dict(SwiGLU=config, ReLU_squared=squared_config(config))
    goals = dict(web=7500, textbook=2000, story=500)
    def source():
        return CEOnlyOriginalSampler(pool, manifest, FixtureCodec(), goals)
    def build(arm='ReLU_squared'):
        return FreshFFNTrainer(configs[arm], source(), dict(proposal='fixture'), arm,
                               batch=4, device='cpu', warmup=1000)
    return configs, source, build


def test_squared_relu_forward_and_independent_analytical_gradients():
    mlp = SquaredReLUMLP(2, 3).double()
    with torch.no_grad():
        mlp.up_proj.weight.copy_(torch.tensor([[1., 0.], [0., 1.], [1., -1.]]))
        mlp.down_proj.weight.copy_(torch.tensor([[1., 2., 3.], [-1., .5, 2.]]))
    x = torch.tensor([[2., -1.], [-1., 3.]], dtype=torch.float64, requires_grad=True)
    pre = x.detach() @ mlp.up_proj.weight.detach().T
    active = pre.clamp(min=0)
    expected = active.square() @ mlp.down_proj.weight.detach().T
    actual = mlp(x)
    assert torch.equal(actual, expected)
    actual.sum().backward()
    delta = (torch.ones_like(actual) @ mlp.down_proj.weight.detach()) * (2 * active)
    assert torch.equal(x.grad, delta @ mlp.up_proj.weight.detach())
    assert torch.equal(mlp.up_proj.weight.grad, delta.T @ x.detach())
    assert torch.equal(mlp.down_proj.weight.grad, torch.ones_like(actual).T @ active.square())
    assert mlp.up_proj.bias is None and mlp.down_proj.bias is None


def test_paired_non_ffn_weights_global_rng_optimizer_and_exact_parameter_budget(tmp_path):
    _, _, build = builders(tmp_path)
    native = build('SwiGLU')
    native_state, native_rng = host(native.model.state_dict()), host(rng_state())
    square = build()
    assert equal_state(native_rng, host(rng_state()))
    for key, value in native_state.items():
        if '.mlp.' not in key:
            assert torch.equal(value, square.model.state_dict()[key]), key
    assert sum(p.numel() for p in native.model.parameters()) == sum(p.numel() for p in square.model.parameters())
    assert square.model.lm_head.weight is square.model.model.embed_tokens.weight
    actual = [id(p) for p in square.model.parameters()]
    optimizer = [id(p) for g in square.optimizer.param_groups for p in g['params']]
    assert actual == optimizer and len(set(actual)) == len(actual)
    assert not square.optimizer.state
    assert equal_state(host(square.model.state_dict()), host(build().model.state_dict()))
    assert square.lineage['parent'] is None and not square.lineage['learned_parent_weights_used']


def test_actual_native10M_and_candidate10M_counts():
    path = Path(__file__).resolve().parents[1] / 'reports/phase6/base_relu_squared_proposal.json'
    config = json.loads(path.read_text())['variants']['SwiGLU']
    torch.manual_seed(42)
    raw = JMicroModel(config)
    non_ffn = {k: v.clone() for k, v in raw.state_dict().items() if '.mlp.' not in k}
    assert sum(p.numel() for p in raw.parameters()) == 10001152
    square = SquaredReLUModel.from_native_fresh(raw)
    assert sum(p.numel() for p in square.parameters()) == 10001152
    assert len(square.model.layers) == 13 and square.config['intermediate_size'] == 960
    assert all(torch.equal(v, square.state_dict()[k]) for k, v in non_ffn.items())


def test_full_fast_padding_causality_chunk_cache_and_shifted_labels(tmp_path):
    _, _, build = builders(tmp_path)
    model = build().model.eval()
    ids = torch.tensor([[2, 65, 66, 67, 68], [2, 69, 70, 71, 72]])
    expected = model(ids).logits
    assert torch.allclose(model(ids, training_fast_path=True).logits, expected, atol=1e-6)
    hidden = right_padded_hidden(model, ids)
    assert torch.allclose(model.lm_head(hidden).float(), expected, atol=1e-6)
    first = model(ids[:, :2], use_cache=True)
    last = model(ids[:, 2:], cache=first.cache, use_cache=True)
    assert len(last.cache.layers) == len(model.model.layers)
    assert torch.allclose(torch.cat((first.logits, last.logits), 1), expected, atol=1e-6)
    padded = torch.tensor([[0, 0, 2, 65, 66], [2, 69, 70, 0, 0]])
    masked = model(padded, attention_mask=padded.ne(0)).logits
    assert torch.allclose(masked[0, 2:], model(padded[:1, 2:]).logits[0], atol=1e-6)
    assert torch.allclose(masked[1, :3], model(padded[1:, :3]).logits[0], atol=1e-6)
    assert torch.equal(masked[~padded.ne(0)], torch.zeros_like(masked[~padded.ne(0)]))
    a = model(padded[:, :3], attention_mask=padded[:, :3].ne(0), use_cache=True)
    b = model(padded[:, 3:], attention_mask=padded[:, 3:].ne(0), cache=a.cache, use_cache=True)
    assert torch.allclose(torch.cat((a.logits, b.logits), 1), masked, atol=1e-6)
    changed = ids.clone(); changed[:, -1] = 80
    assert torch.equal(model(changed).logits[:, :-1], expected[:, :-1])
    labels = ids.clone(); labels[:, :2] = -100
    loss = F.cross_entropy(expected[:, :-1].reshape(-1, 128), labels[:, 1:].reshape(-1), ignore_index=-100)
    assert float(model(ids, labels=labels).loss.detach()) == pytest.approx(float(loss.detach()), abs=1e-6)


def test_tagged_save_load_and_wrong_factory_width_or_foreign_tags_refused(tmp_path):
    configs, _, build = builders(tmp_path)
    model = build().model.eval()
    model.save(tmp_path / 'model')
    loaded = SquaredReLUModel.load(tmp_path / 'model').eval()
    assert equal_state(model.state_dict(), loaded.state_dict())
    assert loaded.lm_head.weight is loaded.model.embed_tokens.weight
    with pytest.raises(ValueError): JMicroModel(model.config)
    with pytest.raises(ValueError): SquaredReLUModel(configs['SwiGLU'])
    wrong = copy.deepcopy(model.config); wrong['intermediate_size'] += 1
    with pytest.raises(ValueError): model_from_config(wrong)
    with pytest.raises(ValueError): model_from_config(dict(model.config, output_probability_link='sigsoftmax'))
    assert native_config(model.config) == configs['SwiGLU']
    with pytest.raises(ValueError): model.hf_reference()


def test_original_masked_gold_CE_EOS_source_and_schedule_identical_between_arms(tmp_path):
    _, source, build = builders(tmp_path)
    native, square = build('SwiGLU'), build()
    rows = source().take(4)
    ids, _ = right_pad([r['input_ids'] for r in rows], 'cpu')
    labels = torch.full_like(ids, -100)
    for index, row in enumerate(rows):
        labels[index, :len(row['target_ids'])] = torch.tensor(row['target_ids'])
    expected = F.cross_entropy(square.model(ids).logits.reshape(-1, 128), labels.reshape(-1), ignore_index=-100)
    first, other = square.step(), native.step()
    assert first['CE_loss'] == pytest.approx(float(expected.detach()), abs=1e-6)
    for _ in range(3):
        for key in (*square.counters, 'draw_trace', 'lr'):
            assert equal_state(first[key], other[key]), key
        first, other = square.step(), native.step()
    assert equal_state(square.sampler.state_dict(), native.sampler.state_dict())
    assert square.counters['supervised_tokens'] == square.scheduler.tokens


@pytest.mark.parametrize('arm', ['SwiGLU', 'ReLU_squared'])
def test_saved_four_vs_two_plus_two_full_state_and_history(tmp_path, arm):
    _, _, build = builders(tmp_path)
    continuous = build(arm)
    full = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = build(arm)
    rows = [split.step() for _ in range(2)]
    path = tmp_path / 'checkpoint.pt'
    split.save(path)
    resumed = build(arm)
    resumed.load(path)
    rows += [resumed.step() for _ in range(2)]
    assert committed_state(expected) and equal_state(expected, host(resumed.state_dict()))
    for a, b in zip(full, rows, strict=True):
        assert equal_state({k: v for k, v in a.items() if k not in ('seconds', 'data_wait_seconds')},
                           {k: v for k, v in b.items() if k not in ('seconds', 'data_wait_seconds')})


@pytest.mark.parametrize('field', ['kind', 'arm', 'width', 'Adam', 'sampler', 'scheduler', 'nonfinite'])
def test_reject_wrong_or_uncommitted_state_before_model_mutation(tmp_path, field):
    _, _, build = builders(tmp_path)
    t = build(); t.step()
    state = copy.deepcopy(host(t.state_dict()))
    if field == 'kind': state['kind'] = 'old_MHA'
    if field == 'arm': state['spec']['arm'] = 'SwiGLU'
    if field == 'width': state['model_config']['intermediate_size'] += 1
    if field == 'Adam': next(iter(state['optimizer']['state'].values()))['step'].zero_()
    if field == 'sampler': state['sampler']['consumed']['web'] += 1
    if field == 'scheduler': state['scheduler']['tokens'] -= 1
    if field == 'nonfinite': next(iter(state['model'].values())).fill_(float('nan'))
    assert not committed_state(state)
    path = tmp_path / 'bad.pt'; torch.save(state, path)
    recipient = build(); before = host(recipient.model.state_dict())
    with pytest.raises(ValueError): recipient.load(path)
    assert equal_state(before, host(recipient.model.state_dict()))


def test_error_after_Adam_refuses_save_and_continue(tmp_path):
    _, _, build = builders(tmp_path)
    t = build()
    original = t.optimizer.step
    def fail(*args, **kwargs):
        original(*args, **kwargs)
        raise RuntimeError('After Adam fixture failure')
    t.optimizer.step = fail
    with pytest.raises(RuntimeError): t.step()
    with pytest.raises(ValueError): t.save(tmp_path / 'partial.pt')
    with pytest.raises(ValueError): t.step()
    assert not (tmp_path / 'partial.pt').exists()
    clean = build(); clean.step()
    with torch.no_grad(): next(clean.model.parameters()).fill_(float('nan'))
    with pytest.raises(ValueError): clean.save(tmp_path / 'nonfinite.pt')
    assert not (tmp_path / 'nonfinite.pt').exists()
