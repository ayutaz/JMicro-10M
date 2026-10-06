import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from base_context_mixing_trainer import ContextMixingTrainer, mix_inputs
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import FixtureCodec, fixture_pool, parent


def builders(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    p = parent()
    def build(probability=.05, control=False):
        sampler = OriginalTrainCorpusSampler(pool, manifest, FixtureCodec(), dict(web=7500, textbook=2000, story=500))
        args = (p, sampler, dict(parent={'sha256':'fixture'}, weights_role='verification_only'))
        kwargs = dict(batch=4, contrast=False, device='cpu')
        return NaturalCorpusTrainer(*args, **kwargs) if control else ContextMixingTrainer(*args, **kwargs, probability=probability)
    return p, build


def test_replacements_are_causal_keep_boundaries_and_ignore_future_prediction():
    ids = torch.tensor([[2,40,41,3,0], [42,43,44,45,46]])
    predictions = torch.tensor([[80,81,82,83,84], [90,91,92,93,94]])
    generator = torch.Generator().manual_seed(42)
    mixed, selected, eligible = mix_inputs(ids, predictions, generator, 1.)
    assert torch.equal(mixed, torch.tensor([[2,80,81,3,0], [42,90,91,92,93]]))
    assert selected.sum()==eligible==6
    changed = predictions.clone(); changed[:,4]=100
    assert torch.equal(mixed, mix_inputs(ids, changed, generator, 1.)[0])
    invalid = predictions.clone(); invalid[0,0]=3
    with pytest.raises(ValueError, match='body tokens'): mix_inputs(ids, invalid, generator, 1.)


def test_zero_mixing_is_exact_clean_CE_weight_optimizer_and_original_source_control(tmp_path):
    p, build = builders(tmp_path)
    candidate, control = build(0.), build(control=True)
    assert equal_state(p['model'], host(candidate.model.state_dict()))
    assert candidate.model.lm_head.weight is candidate.model.model.embed_tokens.weight
    for _ in range(4):
        a, b = candidate.step(), control.step()
        for key in ('CE_loss','gradient_norm','draw_trace', *candidate.counters):
            assert equal_state(a[key], b[key]), key
    for key in ('model','optimizer','scheduler','RNG','sampler','counters'):
        assert equal_state(host(candidate.state_dict()[key]), host(control.state_dict()[key])), key
    assert not candidate.mixing['selected_positions'] and not candidate.mixing['prediction_valid_inputs']


def test_mixing_preserves_gold_stream_while_changing_training_input(tmp_path):
    p, build = builders(tmp_path)
    # The tied random tiny fixture otherwise copies its repeated A/B inputs.
    # Stress a deliberately imperfect predictor, keeping its weights tied.
    for name, weight in p['model'].items():
        if name.endswith('self_attn.o_proj.weight'):
            weight.mul_(50)
    candidate, control = build(), build(control=True)
    for _ in range(4):
        a,b = candidate.step(),control.step()
        for key in (*candidate.counters, 'draw_trace'):
            assert equal_state(a[key],b[key]), key
    assert candidate.mixing['changed_positions'] > 0
    assert candidate.mixing['prediction_valid_inputs']==candidate.counters['CE_input_tokens']
    assert candidate.mixing['prediction_physical_inputs']==candidate.counters['physical_input_tokens']
    assert equal_state(candidate.sampler.state_dict(), control.sampler.state_dict())
    assert not equal_state(candidate.model.state_dict(), control.model.state_dict())


def test_continuous_vs_saved_resume_includes_mixing_rng_and_all_committed_history(tmp_path):
    _, build = builders(tmp_path)
    continuous = build(); expected_rows=[continuous.step() for _ in range(4)]
    expected=host(continuous.state_dict())
    split=build(); rows=[split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed=build(); resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    omitted=('seconds','data_wait_seconds')
    for a,b in zip(expected_rows,rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in omitted},
                           {k:v for k,v in b.items() if k not in omitted})


@pytest.mark.parametrize('mutation',['recipe','updates','counts','source','rng'])
def test_wrong_recipe_or_uncommitted_mixing_state_is_rejected(tmp_path,mutation):
    _,build=builders(tmp_path)
    t=build(); t.step(); state=host(t.state_dict())
    if mutation=='recipe': state['spec']['context_mixing_probability']=.1
    if mutation=='updates': state['context_mixing']['updates']+=1
    if mutation=='counts': state['context_mixing']['selected_positions']=-1
    if mutation=='source': state['counters']['source_teachers']['web']+=1
    if mutation=='rng': state['context_mixing_RNG']=torch.tensor([1.])
    torch.save(state,tmp_path/'bad.pt')
    with pytest.raises(ValueError): build().load(tmp_path/'bad.pt')
