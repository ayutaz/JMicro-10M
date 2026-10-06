"""Architecture/real tiny fullstate tests; no GPU speed or Base quality claim."""
import copy
import json
from pathlib import Path
import sys
import pytest
import torch
from jmicro.model import JMicroModel, KVCache
from jmicro.training import rng_state

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from gated_shared_model import GatedSharedModel, POLICY
from gated_shared_trainer import GatedSharedTrainer, GATE_LR
from test_parameter_displacement_anchor import mixed_fixture
from run_eos_short_pilot import equal_state


def fixture_model():
    config = json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    config.update(num_hidden_layers=2, hidden_size=16, intermediate_size=32,
        num_attention_heads=2, num_key_value_heads=1, head_dim=8, rotary_dim=8, vocab_size=32)
    return JMicroModel(config).eval()


def test_zero_reuse_preserves_exact_native_function_objects_gradients_and_RNG():
    torch.manual_seed(42)
    native=fixture_model();comparison=copy.deepcopy(native);before=rng_state()
    shared=GatedSharedModel.from_native(native)
    assert equal_state(before,rng_state())
    assert shared.model is native.model and shared.lm_head.weight is shared.model.embed_tokens.weight
    assert sum(p.numel() for p in shared.parameters())==sum(p.numel() for p in native.parameters())+2
    x=torch.tensor([[2,8,9,10,11]])
    a=comparison(x).logits;b=shared(x).logits
    assert torch.equal(a,b)
    loss_a=a.square().sum();loss_b=b.square().sum();loss_a.backward();loss_b.backward()
    for name,p in comparison.named_parameters():
        torch.testing.assert_close(p.grad,dict(shared.named_parameters())[name].grad,rtol=0,atol=0)
    assert shared.reuse_gates.grad.abs().sum()>0
    torch.testing.assert_close(shared(x,training_fast_path=True).logits,b,rtol=1e-5,atol=1e-5)


def test_nonzero_signed_gates_ragged_logical_cache_chunk_and_causality():
    model=GatedSharedModel.from_native(fixture_model())
    with torch.no_grad():model.reuse_gates.copy_(torch.tensor([.25,-.125]))
    x=torch.tensor([[2,8,9,10,11,12],[2,8,0,0,9,10]])
    valid=x.ne(0)
    with torch.no_grad():
        full=model(x,valid).logits
        prefix=model(x[:,:4],valid[:,:4],use_cache=True)
        chunk=model(x[:,4:],valid[:,4:],prefix.cache,use_cache=True)
        assert len(chunk.cache.layers)==4
        assert chunk.cache.layers[0][0].data_ptr()!=chunk.cache.layers[1][0].data_ptr()
        torch.testing.assert_close(chunk.logits,full[:,4:],atol=1e-5,rtol=1e-4)
        assert chunk.cache.positions[1,-2:].tolist()==[2,3]
        assert full[~valid].count_nonzero()==0
        for row in range(2):
            torch.testing.assert_close(full[row,valid[row]],model(x[row:row+1,valid[row]]).logits[0],atol=1e-5,rtol=1e-4)
        changed=x.clone();changed[:,4:]=torch.tensor([[13,14],[15,16]])
        assert torch.equal(full[:,:4],model(changed,valid).logits[:,:4])
        bad=KVCache(prefix.cache.layers[:2],prefix.cache.valid,prefix.cache.positions)
        with pytest.raises(ValueError,match='logical-layer'):model(x[:,4:],cache=bad)


def test_config_save_load_loss_support_and_parameter_budget(tmp_path):
    shared=GatedSharedModel.from_native(fixture_model())
    with torch.no_grad():shared.reuse_gates.fill_(.3)
    x=torch.tensor([[2,8,9,10,0]])
    labels=torch.tensor([[-100,-100,9,10,-100]])
    result=shared(x,x.ne(0),labels=labels)
    expected=torch.nn.functional.cross_entropy(result.logits[:,1:3].reshape(-1,32),torch.tensor([9,10]))
    torch.testing.assert_close(result.loss,expected)
    shared.save(tmp_path);loaded=GatedSharedModel.load(tmp_path)
    assert loaded.config['gated_shared_reuse']==POLICY and equal_state(shared.state_dict(),loaded.state_dict())
    assert torch.equal(result.logits,loaded(x,x.ne(0)).logits)
    with pytest.raises(ValueError,match='dedicated export'):loaded.hf_reference()
    with pytest.raises(ValueError,match='config'):GatedSharedModel(fixture_model().config)
    native=json.loads((Path(__file__).resolve().parents[1]/'configs/models/t4k.json').read_text())
    # Production parent uses a different frozen FFN/depth; verify its dimensions
    # when defining the actual comparison, rather than claim this random model.
    assert native['vocab_size']==4096


def test_native_Adam_preservation_gate_group_and_exact_fullstate_resume(tmp_path):
    pool,parent,binding,positive=mixed_fixture(tmp_path)
    goals=dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=80)
    def build():return GatedSharedTrainer(parent,pool,pool,positive,goals,binding,'cpu',8,3)
    whole=build();opt=whole.optimizer.state_dict()
    assert equal_state(opt['state'],parent['optimizer']['state'])
    assert equal_state(opt['param_groups'][:2],parent['optimizer']['param_groups'])
    assert len(opt['param_groups'])==3 and opt['param_groups'][-1]['lr']==GATE_LR
    assert equal_state(rng_state(),parent['rng']) and whole.model.reuse_gates.count_nonzero()==0
    left=[whole.step() for _ in range(4)];whole.save(tmp_path/'whole.pt')
    split=build();right=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    split=build();split.load(tmp_path/'split.pt');right += [split.step() for _ in range(2)];split.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'whole.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    for key in ('loss','CE_loss','gradient_norm','source_teachers','token_digest','new_gate_LR'):
        assert [r[key] for r in left]==[r[key] for r in right]
    assert whole.model.reuse_gates.count_nonzero()>0
    assert all(r['lr']==.00001 and r['new_gate_LR']==GATE_LR for r in left)
