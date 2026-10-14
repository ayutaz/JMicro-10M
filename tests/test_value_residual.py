"""CPU mechanism, zero-conversion and active inference; no quality evidence."""
import copy
import json
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

from jmicro.model import JMicroModel, rope
from jmicro.phase5 import equal_state
from jmicro.value_residual import (TAG, ValueResidualModel, mix_values,
                                   native_config, tagged_config)

torch.set_num_threads(2)


def config(layers=3):
    c = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    c.update(num_hidden_layers=layers, hidden_size=32, head_dim=8, rotary_dim=8,
        attention_scale=8**-.5, intermediate_size=64, vocab_size=128, qk_norm_type='none')
    with torch.device('meta'):
        model = JMicroModel(c)
    c['expected_parameter_count'] = sum(p.numel() for p in model.parameters())
    return c


def native():
    torch.manual_seed(13)
    return JMicroModel(config()).eval()


def test_value_formula_signed_gradient_and_information_not_in_current_values():
    first = torch.tensor([[[[2., -3.], [4., 5.]]]], requires_grad=True)
    current = torch.zeros_like(first, requires_grad=True)
    alpha = torch.tensor(-.5, requires_grad=True)
    mixed = mix_values(current, first, alpha)
    assert torch.equal(mixed, -.5*first)
    mixed.sum().backward()
    assert torch.equal(first.grad, torch.full_like(first, -.5))
    assert torch.equal(current.grad, torch.ones_like(current))
    assert alpha.grad == first.detach().sum()
    # A current-V-only attention/readout emits zero here; the shortcut does not.
    assert torch.count_nonzero(mixed) == 4


def test_full_model_independent_attention_matrix_reference_active():
    candidate = ValueResidualModel.from_native(native()).double()
    with torch.no_grad():
        candidate.model.layers[1].self_attn.value_alpha.fill_(.4)
        candidate.model.layers[2].self_attn.value_alpha.fill_(-.3)
    ids = torch.tensor([[2, 11, 21, 31, 3]])
    positions = torch.arange(5)[None]
    x = candidate.model.embed_tokens(ids)
    first = None
    for index, block in enumerate(candidate.model.layers):
        a = block.self_attn
        h = block.input_layernorm(x)
        def project(layer, heads):
            return layer(h).view(1, 5, heads, 8).transpose(1, 2)
        q = rope(a.q_norm(project(a.q_proj, 4)), positions, a.theta)
        k = rope(a.k_norm(project(a.k_proj, 2)), positions, a.theta)
        v = project(a.v_proj, 2)
        if index == 0:
            first = v
        else:
            v = v + a.value_alpha*first
        maps = (q @ k.repeat_interleave(2, dim=1).transpose(-1,-2))*a.scale
        maps = maps.masked_fill(~torch.ones(5,5,dtype=torch.bool).tril(), -torch.inf).softmax(-1)
        attended = maps @ v.repeat_interleave(2, dim=1)
        x = x + a.o_proj(attended.transpose(1,2).reshape(1,5,32))
        x = x + block.mlp(block.post_attention_layernorm(x))
    expected = candidate.lm_head(candidate.model.norm(x)).float()
    assert torch.allclose(candidate(ids).logits, expected, atol=2e-7, rtol=2e-6)


def test_zero_conversion_original_weights_logits_gradients_RNG_and_tie_exact():
    original = native().train()
    before = torch.get_rng_state().clone()
    candidate = ValueResidualModel.from_native(original).train()
    assert torch.equal(before, torch.get_rng_state())
    assert candidate.lm_head.weight is candidate.model.embed_tokens.weight
    old = dict(original.named_parameters())
    new = dict(candidate.named_parameters())
    assert all(torch.equal(p, new[n]) and p.data_ptr() != new[n].data_ptr() for n,p in old.items())
    assert sum(p.numel() for p in candidate.parameters()) == sum(p.numel() for p in original.parameters())+2
    ids = torch.tensor([[2, 11, 12, 13, 3], [2, 31, 33, 35, 3]])
    a, b = original(ids, labels=ids), candidate(ids, labels=ids)
    assert torch.equal(a.logits,b.logits) and torch.equal(a.loss,b.loss)
    a.loss.backward()
    b.loss.backward()
    assert all(torch.equal(p.grad,new[n].grad) for n,p in old.items())
    assert all(new[n].grad.abs().sum()>0 for n in new if n.endswith('.value_alpha'))


@pytest.mark.parametrize('arm',['value_learned','static_identity'])
def test_active_or_static_cache_padding_chunk_causality_fast_hidden_and_labels(arm):
    candidate = ValueResidualModel.from_native(native(),arm)
    if arm == 'value_learned':
        with torch.no_grad():
            candidate.model.layers[1].self_attn.value_alpha.fill_(.3)
            candidate.model.layers[2].self_attn.value_alpha.fill_(-.2)
    ids = torch.tensor([[2,11,12,13,14,15,16,3],[2,31,32,33,34,3,0,0]])
    valid = ids.ne(0)
    full = candidate(ids,attention_mask=valid,use_cache=True)
    first = candidate(ids[:,:3],attention_mask=valid[:,:3],use_cache=True)
    last = candidate(ids[:,3:],attention_mask=valid[:,3:],cache=first.cache,use_cache=True)
    assert torch.allclose(full.logits[:,3:],last.logits,atol=3e-7,rtol=2e-6)
    assert torch.equal(full.cache.valid,last.cache.valid)
    assert torch.equal(full.cache.positions,last.cache.positions)
    for (a,b),(c,d) in zip(full.cache.layers,last.cache.layers):
        assert torch.allclose(a,c,atol=3e-7,rtol=2e-6)
        assert torch.allclose(b,d,atol=3e-7,rtol=2e-6)
        assert a.shape[1] == b.shape[1] == 2
    changed = ids.clone()
    changed[0,5:] = torch.tensor([99,98,97])
    assert torch.equal(full.logits[0,:5],candidate(changed,attention_mask=valid).logits[0,:5])
    assert torch.allclose(candidate.lm_head(candidate.right_padded_hidden(ids))[valid],
                          full.logits[valid],atol=3e-7,rtol=2e-6)
    assert torch.allclose(candidate(ids[:1]).logits,
        candidate(ids[:1],training_fast_path=True).logits,atol=3e-7,rtol=2e-6)
    labels=ids.clone()
    labels[~valid]=-100
    actual=candidate(ids,attention_mask=valid,labels=labels)
    expected=F.cross_entropy(actual.logits[:,:-1].reshape(-1,128),labels[:,1:].reshape(-1),ignore_index=-100)
    assert torch.equal(actual.loss,expected)


def test_native_hidden_helper_fails_instead_of_silently_bypassing_new_path():
    sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
    from natural_context_contrast_trainer import right_padded_hidden
    with pytest.raises(ValueError,match='decoder traversal required'):
        right_padded_hidden(ValueResidualModel.from_native(native()),torch.tensor([[2,11,3]]))


def test_static_arm_three_Adam_steps_matches_all_original_weights_and_named_Adam():
    original=native().train()
    candidate=ValueResidualModel.from_native(original,'static_identity').train()
    opts=[torch.optim.AdamW(m.parameters(),lr=1e-5,weight_decay=.1) for m in (original,candidate)]
    ids=torch.tensor([[2,11,12,13,3]])
    for _ in range(3):
        for m,opt in zip((original,candidate),opts):
            opt.zero_grad(set_to_none=True)
            m(ids,labels=ids).loss.backward()
        new=dict(candidate.named_parameters())
        assert all(torch.equal(p.grad,new[n].grad) for n,p in original.named_parameters())
        a=torch.nn.utils.clip_grad_norm_(original.parameters(),1.)
        b=candidate.clip_grad_norm(1.)
        assert torch.equal(a,b)
        assert all(torch.equal(p.grad,new[n].grad) for n,p in original.named_parameters())
        for opt in opts: opt.step()
        for n,p in original.named_parameters():
            assert torch.equal(p,new[n])
            assert equal_state(opts[0].state[p],opts[1].state[new[n]])
        assert all(p.item()==0 and p.grad.item()==0 for n,p in new.items() if n.endswith('.value_alpha'))


def test_scientific_learned_clip_includes_extra_scalar_coordinates():
    model=ValueResidualModel.from_native(native())
    old=model.model.layers[0].self_attn.v_proj.weight
    alpha=model.model.layers[1].self_attn.value_alpha
    old.grad=torch.zeros_like(old)
    old.grad[0,0]=4.
    alpha.grad=torch.tensor(3.)
    norm=model.clip_grad_norm(1.)
    assert norm.item()==5.
    factor=1./(5.+1e-6)
    assert old.grad[0,0].item()==pytest.approx(4.*factor,abs=1e-7)
    assert alpha.grad.item()==pytest.approx(3.*factor,abs=1e-7)


@pytest.mark.parametrize('bad',['missing','nan','shape','dtype','tie','static_nonzero'])
def test_bad_state_rejected_before_mutation(bad):
    model=ValueResidualModel.from_native(native(),'static_identity' if bad=='static_nonzero' else 'value_learned')
    before=copy.deepcopy(model.state_dict())
    state=copy.deepcopy(before)
    key='model.layers.1.self_attn.value_alpha'
    if bad=='missing': del state[key]
    elif bad=='nan': state[key].fill_(float('nan'))
    elif bad=='shape': state[key]=state[key].reshape(1)
    elif bad=='dtype': state[key]=state[key].double()
    elif bad=='tie': state['lm_head.weight']=state['lm_head.weight'].clone()+.1
    else: state[key].fill_(1.)
    with pytest.raises(ValueError): model.load_state_dict(state)
    assert equal_state(before,model.state_dict())


@pytest.mark.parametrize('bad',['policy','count','arm','norm'])
def test_invalid_architecture_tag_refused(bad):
    c=tagged_config(config())
    if bad=='policy': c[TAG]['policy']['first_value_detached']=True
    elif bad=='count': c['expected_parameter_count']+=1
    elif bad=='arm': c[TAG]['arm']='other'
    else: c['qk_norm_type']='rms_head_shared'
    with pytest.raises(ValueError): ValueResidualModel(c)


def test_actual_13layer_budget_meta_and_strict_state_roundtrip_no_native_export(tmp_path):
    c=json.loads((Path(__file__).resolve().parents[1]/'reports/phase6/cross-gqa-map-science-20261015/training.json').read_text())['spec']['original_model_config']
    with torch.device('meta'):
        actual=ValueResidualModel(tagged_config(c))
    assert sum(p.numel() for p in actual.parameters())==10001164
    first=ValueResidualModel.from_native(native())
    with torch.no_grad(): first.model.layers[1].self_attn.value_alpha.fill_(.3)
    second=ValueResidualModel(copy.deepcopy(first.config))
    second.load_state_dict(first.state_dict())
    assert equal_state(first.state_dict(),second.state_dict())
    assert native_config(first.config)==config()
    for action in (first.hf_reference,lambda:first.save(tmp_path),lambda:ValueResidualModel.load(tmp_path)):
        with pytest.raises(ValueError): action()
