"""Weighted original CE objective and independent grouped resume checks."""
import copy
from pathlib import Path
import sys

import pytest
import torch
from torch.nn import functional as F

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_kv_allocation_bucketed import BucketedKVAllocationTrainer, grouped_backward
from natural_context_contrast_trainer import host, right_pad
from jmicro.phase5 import equal_state
from test_base_kv_allocation_trainer import builders


@pytest.mark.parametrize('name',['GQA','MHA'])
def test_unequal_length_group_objective_and_every_gradient_match_native_masked_ce(tmp_path,name):
    source,build,_ = builders(tmp_path)
    rows = source().take(16)
    model = build(name).model
    ids,_ = right_pad([r['input_ids'] for r in rows],'cpu')
    targets = torch.full_like(ids,-100)
    for i,row in enumerate(rows):
        targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'])
    native = F.cross_entropy(model(ids).logits.reshape(-1,128),targets.reshape(-1),ignore_index=-100)
    native.backward()
    expected = {name:p.grad.detach().clone() for name,p in model.named_parameters()}
    model.zero_grad(set_to_none=True)
    actual,physical,groups = grouped_backward(model,rows,'cpu')
    assert actual == pytest.approx(float(native.detach()),abs=1e-6)
    assert groups > 1 and physical < ids.numel()
    for key,p in model.named_parameters():
        torch.testing.assert_close(p.grad,expected[key],rtol=1e-5,atol=1e-6)


@pytest.mark.parametrize('name',['GQA','MHA'])
def test_grouped_full_state_continuous_four_vs_saved_two_and_original_source_identity(tmp_path,name):
    source,build,configs = builders(tmp_path)
    def bucket():
        return BucketedKVAllocationTrainer(configs[name],source(),dict(proposal='fixture'),batch=4,device='cpu',warmup=1000)
    continuous = bucket()
    history = [continuous.step() for _ in range(4)]
    expected = host(continuous.state_dict())
    split = bucket()
    rows = [split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt')
    resumed = bucket()
    resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    assert all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                          {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})
               for a,b in zip(history,rows,strict=True))
    flat = build(name)
    for a in history:
        b = flat.step()
        for key in ('source_teachers','source_EOS','supervised_tokens','CE_input_tokens','original_body_bytes','token_digest','draw_trace','lr'):
            assert equal_state(a[key],b[key])
    assert equal_state(continuous.sampler.state_dict(),flat.sampler.state_dict())
    flat.save(tmp_path/'flat.pt')
    with pytest.raises(ValueError,match='binding'):
        bucket().load(tmp_path/'flat.pt')
