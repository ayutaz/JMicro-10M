"""Masked native observation, synthetic concentration and hook restoration."""
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_attention_saturation_diagnostic import attention_statistics,observe_attention,aggregate,broad_screen
from natural_context_contrast_trainer import right_padded_hidden,host
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import parent


def test_uniform_attention_excludes_early_and_masked_queries_and_has_no_future_mass():
    q=torch.zeros(1,4,20,8);k=torch.zeros(1,2,20,8)
    targets=torch.ones(1,20,dtype=torch.long);targets[0,-1]=-100
    stats=attention_statistics(q,k,targets,1.)
    assert all(r['eligible_queries']==4 and r['saturated_queries']==0 for r in stats)
    assert all(r['normalized_entropy_sum']==pytest.approx(4.,abs=1e-6) for r in stats)
    expected=sum(8/n for n in (16,17,18,19))
    assert all(r['recent8_mass_sum']==pytest.approx(expected,abs=1e-6) for r in stats)


def test_synthetic_BOS_saturation_and_broad_layer_rule_not_quality_adoption():
    q=torch.zeros(1,4,20,8);q[:,:,:,0]=10
    k=torch.zeros(1,2,20,8);k[:,:,0,0]=10
    stats=attention_statistics(q,k,torch.ones(1,20,dtype=torch.long),1.)
    assert all(r['saturated_queries']==r['saturated_to_BOS']==5 for r in stats)
    source=aggregate([dict(layer=i,heads=stats) for i in range(3)],3)
    assert source['marked_layers']==3
    screen=broad_screen(dict(web=source,textbook=source,story=source))
    assert screen['passed'] and not screen['causal_proof'] and not screen['Base_quality_gate']


def test_native_logits_loss_parameters_RNG_unchanged_and_observation_hooks_removed():
    model=JMicroModel(parent()['model_config']).eval()
    inputs=torch.tensor([[2]+[65]*19]);targets=torch.tensor([[65]*19+[3]])
    with torch.no_grad():
        expected=right_padded_hidden(model,inputs)
        state=host(model.state_dict());rng=torch.get_rng_state().clone()
        with observe_attention(model,targets) as captured:
            actual=right_padded_hidden(model,inputs)
    assert torch.equal(expected,actual) and len(captured)==2
    assert equal_state(state,host(model.state_dict())) and torch.equal(rng,torch.get_rng_state())
    assert all(not b.self_attn._forward_pre_hooks for b in model.model.layers)


def test_hooks_removed_after_injected_failure_and_cached_or_short_only_inputs_rejected():
    model=JMicroModel(parent()['model_config']).eval()
    targets=torch.ones(1,20,dtype=torch.long)
    with pytest.raises(RuntimeError,match='injected'):
        with observe_attention(model,targets):raise RuntimeError('injected')
    assert all(not b.self_attn._forward_pre_hooks for b in model.model.layers)
    empty=attention_statistics(torch.zeros(1,4,8,8),torch.zeros(1,2,8,8),torch.ones(1,8,dtype=torch.long),1.)
    with pytest.raises(ValueError,match='16'):
        aggregate([dict(layer=0,heads=empty)],1)
