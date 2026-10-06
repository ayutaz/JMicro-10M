"""Real CPU tiny state/cache/gradient contracts, not GPU or quality evidence."""
import copy
from pathlib import Path
import sys
import pytest
import torch
from jmicro.training import rng_state
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from readout_adapter_model import ReadoutAdapterModel,POLICY
from readout_adapter_trainer import ReadoutAdapterTrainer,READOUT_LR
from test_gated_shared import fixture_model
from test_parameter_displacement_anchor import mixed_fixture
from run_eos_short_pilot import equal_state


def test_identity_native_frozen_parameters_private_RNG_and_body_capability():
    native=fixture_model();reference=copy.deepcopy(native);before=rng_state();adapted=ReadoutAdapterModel.from_native(native)
    assert equal_state(before,rng_state()) and adapted.model is native.model
    assert adapted.lm_head.weight is adapted.model.embed_tokens.weight
    assert [k for k,p in adapted.named_parameters() if p.requires_grad]==['lm_head.down','lm_head.up']
    x=torch.tensor([[2,8,9,10,11]])
    assert torch.equal(reference(x).logits,adapted(x).logits)
    loss=adapted(x).logits.square().sum();loss.backward()
    assert adapted.lm_head.up.grad.abs().sum()>0 and adapted.lm_head.down.grad.count_nonzero()==0
    assert all(p.grad is None for p in adapted.parameters() if not p.requires_grad)
    with torch.no_grad():adapted.lm_head.up.fill_(.03)
    changed=adapted(x).logits;original=reference(x).logits
    assert (changed[...,8:]-original[...,8:]).abs().sum()>0
    # Same-history decoder caches themselves remain exactly native.
    a=adapted(x,use_cache=True);b=reference(x,use_cache=True)
    assert equal_state(a.cache.layers,b.cache.layers)
    assert all(torch.equal(p,dict(reference.named_parameters())[k]) for k,p in adapted.named_parameters() if not p.requires_grad)


def test_ragged_full_chunk_fast_labels_and_native_save_load(tmp_path):
    model=ReadoutAdapterModel.from_native(fixture_model())
    with torch.no_grad():model.lm_head.up.fill_(.05)
    x=torch.tensor([[2,8,9,10,11,12],[2,8,0,0,9,10]]);mask=x.ne(0)
    with torch.no_grad():
        full=model(x,mask).logits;first=model(x[:,:4],mask[:,:4],use_cache=True)
        chunk=model(x[:,4:],mask[:,4:],first.cache,use_cache=True)
        assert len(chunk.cache.layers)==2
        torch.testing.assert_close(chunk.logits,full[:,4:],rtol=1e-4,atol=1e-5)
        assert full[~mask].count_nonzero()==0
        changed=x.clone();changed[:,4:]=torch.tensor([[13,14],[15,16]])
        assert torch.equal(full[:,:4],model(changed,mask).logits[:,:4])
        torch.testing.assert_close(model(x[:1],training_fast_path=True).logits,full[:1],rtol=1e-4,atol=1e-5)
    labels=torch.tensor([[-100,-100,9,10,11,-100],[-100,8,-100,-100,9,10]])
    output=model(x,mask,labels=labels)
    expected=torch.nn.functional.cross_entropy(output.logits[:,:-1].reshape(-1,32),labels[:,1:].reshape(-1),ignore_index=-100)
    torch.testing.assert_close(output.loss,expected)
    model.save(tmp_path);loaded=ReadoutAdapterModel.load(tmp_path)
    assert loaded.config['readout_adapter']==POLICY and equal_state(model.state_dict(),loaded.state_dict())
    assert loaded.lm_head.weight is loaded.model.embed_tokens.weight and torch.equal(loaded(x,mask).logits,full)
    with pytest.raises(ValueError,match='dedicated export'):loaded.hf_reference()


def test_actual_fresh_readout_only_Adam_and_continuous_resumed_fullstate(tmp_path):
    pool,parent,binding,positive=mixed_fixture(tmp_path);goals=dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=80)
    def build():return ReadoutAdapterTrainer(parent,pool,pool,positive,goals,binding,'cpu',8,3)
    whole=build();assert whole.optimizer.state_dict()['state']=={}
    assert len(whole.optimizer.param_groups)==1 and len(whole.optimizer.param_groups[0]['params'])==2
    assert equal_state(rng_state(),parent['rng'])
    left=[whole.step() for _ in range(4)];whole.save(tmp_path/'whole.pt')
    split=build();right=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    split=build();split.load(tmp_path/'split.pt');right += [split.step() for _ in range(2)];split.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'whole.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    for key in ('loss','gradient_norm','source_teachers','token_digest','readout_LR'):
        assert [v[key] for v in left]==[v[key] for v in right]
    assert all(v['lr']==READOUT_LR and v['native_optimizer_updates']==0 for v in left)
    assert all(torch.equal(p.cpu(),parent['model'][k]) for k,p in whole.model.named_parameters() if not p.requires_grad)
    assert len(whole.optimizer.state_dict()['state'])==2 and whole.model.lm_head.down.grad.abs().sum()>0
