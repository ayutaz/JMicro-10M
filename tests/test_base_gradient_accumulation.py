"""Unequal original-teacher gradients and real optimizer/state grouping fixtures."""
from pathlib import Path
import copy
import sys

import pytest
import torch
from torch.nn import functional as F
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
from base_gradient_accumulation_trainer import GroupedTrainer, committed_group
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden
from jmicro.phase5 import equal_state
from base_parallel_residual_trainer import FreshResidualTrainer,CEOnlyOriginalSampler
from jmicro.model import JMicroModel
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


@pytest.fixture
def builders(tmp_path):
    pool = tmp_path/'pool'
    manifest = fixture_pool(pool)
    config = copy.deepcopy(parent()['model_config'])
    with torch.device('meta'):
        config['expected_parameter_count'] = sum(p.numel() for p in JMicroModel(config).parameters())
    def source():
        return CEOnlyOriginalSampler(pool,manifest,FixtureCodec(),dict(web=75000,textbook=20000,story=5000))
    def build(arm):
        return FreshResidualTrainer(config,source(),dict(proposal='fixture'),arm,
                                    batch=4,device='cpu',warmup=1000)
    return source,build


def test_accumulation1_matches_original_learning_state_and_stream_exact(builders):
    _,build = builders
    baseline = build('sequential')
    original = baseline.step()
    grouped = GroupedTrainer(build('sequential'),1)
    result = grouped.step()
    expected = host(baseline.state_dict())
    actual = host(grouped.native.state_dict())
    assert equal_state(expected,actual)
    for key in ('CE_loss','gradient_norm','lr','token_digest','source_teachers','supervised_tokens'):
        assert result[key] == original[key]


def test_unequal_microbatches_match_full_teacher_weighted_gradient(builders):
    source,build = builders
    sampler = source()
    rows = [sampler.take(4) for _ in range(4)]
    sizes = [sum(r['teacher_tokens'] for r in batch) for batch in rows]
    assert len(set(sizes))>1
    flat = [r for batch in rows for r in batch]
    reference = build('sequential')
    ids,_ = right_pad([r['input_ids'] for r in flat],'cpu')
    targets = torch.full_like(ids,-100)
    for i,row in enumerate(flat):
        targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'])
    valid = targets.ne(-100)
    loss = F.cross_entropy(reference.model.lm_head(right_padded_hidden(reference.model,ids)[valid]),targets[valid])
    loss.backward()
    torch.nn.utils.clip_grad_norm_(reference.model.parameters(),1.)
    expected = {k:p.grad.clone() for k,p in reference.model.named_parameters()}
    grouped = GroupedTrainer(build('sequential'),4)
    result = grouped.step()
    torch.testing.assert_close(torch.tensor(result['CE_loss']),loss.detach(),atol=1e-6,rtol=1e-6)
    for name,p in grouped.native.model.named_parameters():
        torch.testing.assert_close(p.grad,expected[name],atol=3e-6,rtol=1e-5)
    assert grouped.native.sampler.consumed == sampler.consumed
    assert result['supervised_tokens'] == sum(sizes)
    assert result['update']==1 and result['microbatches']==4


def test_grouped_continuous_four_matches_two_save_resume_two_complete_state(builders,tmp_path):
    _,build = builders
    a = GroupedTrainer(build('sequential'))
    full = [a.step() for _ in range(4)]
    expected = host(a.state_dict())
    b = GroupedTrainer(build('sequential'))
    split = [b.step() for _ in range(2)]
    b.save(tmp_path/'saved.pt')
    c = GroupedTrainer(build('sequential'))
    c.load(tmp_path/'saved.pt')
    split.extend(c.step() for _ in range(2))
    assert committed_group(c.state_dict())
    assert equal_state(expected,host(c.state_dict()))
    for x,y in zip(full,split,strict=True):
        assert equal_state({k:v for k,v in x.items() if k not in ('seconds','data_wait_seconds')},
                           {k:v for k,v in y.items() if k not in ('seconds','data_wait_seconds')})
