"""Loss/mask math tests; no CUDA training or model-quality claim."""
import math

import pytest
import torch

from jmicro.sequence_unlikelihood import (repeated_ngram_mask, sequence_unlikelihood_sum,
                                        greedy_rollout, continuation_logits)


def small_model():
    from jmicro.experiment import ROOT,read_json
    from jmicro.model import JMicroModel
    torch.set_num_threads(2)
    config=read_json(ROOT/"configs/models/t4k.json")
    config.update(vocab_size=32,hidden_size=32,num_attention_heads=2,num_key_value_heads=1,
                  head_dim=16,rotary_dim=16,num_hidden_layers=1,intermediate_size=48,
                  attention_scale=.25,qk_norm_type="none")
    return JMicroModel(config)


def test_native_cached_rollout_matches_full_history_greedy_and_preserves_rng_mode():
    torch.manual_seed(41)
    model=small_model().train()
    prefix=torch.tensor([[2,8,9],[2,10,11]])
    rng=torch.get_rng_state().clone()
    actual=greedy_rollout(model,prefix,max_new_tokens=9)
    assert model.training and torch.equal(rng,torch.get_rng_state())
    model.eval();current=prefix;finished=torch.zeros(2,dtype=torch.bool);expected=[]
    with torch.no_grad():
        for _ in range(9):
            scores=model(current,attention_mask=current.ne(0)).logits[:,-1].clone()
            scores[:,[0,1,2,4,5,6,7]]=-torch.inf
            ids=scores.argmax(-1).masked_fill(finished,0)
            expected.append(ids);finished |= ids.eq(3)
            if finished.all(): break
            current=torch.cat((current,ids[:,None]),dim=1)
    assert torch.equal(actual,torch.stack(expected,dim=1))


def test_rollout_stops_rows_individually_and_keeps_actual_eos():
    from types import SimpleNamespace
    class ControlledModel(torch.nn.Module):
        config={"max_position_embeddings":16}
        def forward(self,ids,attention_mask=None,cache=None,use_cache=False):
            step=0 if cache is None else cache
            logits=torch.zeros(ids.shape[0],ids.shape[1],12)
            logits[0,-1,3]=9
            logits[1,-1,8 if step==0 else 3]=9
            return SimpleNamespace(logits=logits,cache=step+1)
    model=ControlledModel()
    assert greedy_rollout(model,torch.tensor([[2,8],[2,9]]),max_new_tokens=5).tolist()==[[3,0],[8,3]]


def test_generated_history_alignment_and_native_model_gradient():
    model=small_model()
    prefix=torch.tensor([[2,8,9],[2,10,11]])
    generated=torch.tensor([[8,9,8,9,3],[10,11,10,11,3]])
    logits=continuation_logits(model,prefix,generated)
    joined=torch.cat((prefix,generated),dim=1)
    full=model(joined).logits
    # Adding a causal suffix changes the FP32 matmul shape, not the token shift.
    # Compare numerically, as in the existing native cache/causality tests.
    torch.testing.assert_close(logits,full[:,2:7],atol=1e-6,rtol=1e-5)
    masks=torch.tensor(repeated_ngram_mask(generated.tolist(),n=2))
    loss=sequence_unlikelihood_sum(logits,generated,masks)
    loss.backward()
    assert loss>0 and all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())


def test_rollout_refuses_padding_and_context_overflow():
    model=small_model()
    with pytest.raises(ValueError):greedy_rollout(model,torch.tensor([[2,0]]))
    with pytest.raises(ValueError):greedy_rollout(model,torch.tensor([[2,8]]),max_new_tokens=10000)


def test_marks_later_whole_ngrams_once_and_keeps_sequences_separate():
    rows = [[8,9,10,11,12,8,9,10,11], [8,9,10,11], [8,8,8,8,8,8]]
    masks = repeated_ngram_mask(rows)
    assert masks == [[False]*5+[True]*4, [False]*4, [False]+[True]*5]


def test_special_boundaries_stops_and_short_continuations():
    rows = [[8,9,10,11,2,8,9,10,11],
            [8,9,10,11,3,8,9,10,11,8,9,10,11],
            [8,9,10,11,7,8,9,10,11,8,9,10,11], [], [8,9,10]]
    assert repeated_ngram_mask(rows) == [[False]*len(row) for row in rows]
    with pytest.raises(ValueError): repeated_ngram_mask([[True,8]])
    with pytest.raises(ValueError): repeated_ngram_mask([[8]],n=True)


def test_analytic_loss_gradient_and_unselected_positions():
    logits = torch.zeros(1,3,10,dtype=torch.float64,requires_grad=True)
    ids = torch.tensor([[8,9,3]])
    mask = torch.tensor([[True,False,False]])
    loss = sequence_unlikelihood_sum(logits,ids,mask)
    assert float(loss.detach()) == pytest.approx(-math.log(.9))
    loss.backward()
    assert float(logits.grad[0,0,8]) == pytest.approx(.1)
    assert float(logits.grad[0,0,9]) == pytest.approx(-.1/9)
    assert torch.count_nonzero(logits.grad[0,1:]) == 0
    assert torch.autograd.gradcheck(lambda x: sequence_unlikelihood_sum(x,ids,mask),
                                   (logits.detach().requires_grad_(),))


def test_saturated_negative_is_finite_and_still_has_corrective_gradient():
    logits = torch.zeros(1,1,10,requires_grad=True)
    with torch.no_grad(): logits[0,0,8] = 1000
    loss = sequence_unlikelihood_sum(logits,torch.tensor([[8]]),torch.tensor([[True]]))
    assert float(loss.detach()) == pytest.approx(1000-math.log(9),abs=1e-4)
    loss.backward()
    assert torch.isfinite(logits.grad).all() and float(logits.grad[0,0,8]) == 1


def test_bf16_promotes_and_empty_candidates_keep_zero_gradient():
    logits = torch.zeros(1,2,10,dtype=torch.bfloat16,requires_grad=True)
    ids = torch.tensor([[8,3]])
    loss = sequence_unlikelihood_sum(logits,ids,torch.tensor([[True,False]]))
    assert loss.dtype == torch.float32 and torch.isfinite(loss)
    zero = sequence_unlikelihood_sum(logits,ids,torch.zeros(1,2,dtype=torch.bool))
    zero.backward()
    assert zero == 0 and torch.count_nonzero(logits.grad) == 0


def test_refuses_special_candidates_and_misaligned_prediction_shapes():
    logits = torch.zeros(1,1,10)
    with pytest.raises(ValueError,match="Special"):
        sequence_unlikelihood_sum(logits,torch.tensor([[3]]),torch.tensor([[True]]))
    with pytest.raises(ValueError,match="aligned"):
        sequence_unlikelihood_sum(logits,torch.tensor([[8]]),torch.tensor([[1]]))
