import copy
import sys
from pathlib import Path

import pytest
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts'),str(Path(__file__).resolve().parents[1]/'src')]
from jmicro.model import JMicroModel
from base_embedding_gradient_diagnostic import decompose,gradient_statistics,interference_screen


def test_actual_tied_gradient_is_sum_of_paths_without_mutation():
    c=__import__('json').loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    c.update(hidden_size=32,num_attention_heads=4,num_key_value_heads=2,head_dim=8,
        rotary_dim=8,num_hidden_layers=2,intermediate_size=40,vocab_size=64,qk_norm_type='none')
    torch.manual_seed(42)
    model=JMicroModel(c).eval(); saved=copy.deepcopy(model.state_dict()); rng=torch.get_rng_state().clone()
    inputs=torch.tensor([[2,8,9,10,0],[2,11,12,13,14]])
    targets=torch.tensor([[8,9,10,3,-100],[-100,-100,13,14,3]])
    with sdpa_kernel(SDPBackend.MATH):stats,a,b=decompose(model,inputs,targets)
    assert stats['teachers']==7 and stats['EOS_teachers']==2
    assert stats['logit_max_error']==0 and stats['decomposition_relative_error']<1e-5
    assert stats['EOS_input_norm']==0 and stats['EOS_output_norm']>0
    assert torch.equal(rng,torch.get_rng_state())
    assert all(torch.equal(saved[k],v) for k,v in model.state_dict().items())
    assert model.lm_head.weight is model.model.embed_tokens.weight
    assert all(p.grad is None for p in model.parameters())


def test_statistics_distinguish_cancellation_and_aligned_paths():
    a=torch.arange(1.,17.).reshape(4,4)
    opposite=gradient_statistics(a,-a);aligned=gradient_statistics(a,a)
    assert opposite['cosine']==pytest.approx(-1) and opposite['cancellation_ratio']==0
    assert opposite['conflicting_shared_rows']==4 and opposite['combined_norm']==0
    assert aligned['cosine']==pytest.approx(1) and aligned['cancellation_ratio']==pytest.approx(1)
    with pytest.raises(ValueError):gradient_statistics(a,torch.zeros_like(a))


def test_predeclared_screen_requires_multiple_sources_and_never_adopts_base():
    weak=dict(cosine=-.01,cancellation_ratio=.6)
    strong=dict(cosine=-.2,cancellation_ratio=.7)
    assert not interference_screen(dict(web=strong,textbook=weak,story=weak))['passed']
    actual=interference_screen(dict(web=strong,textbook=strong,story=weak))
    assert actual['passed'] and not actual['Base_quality_gate'] and not actual['causal_proof']
    with pytest.raises(ValueError):interference_screen(dict(web=strong))
