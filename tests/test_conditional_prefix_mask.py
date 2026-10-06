"""Original inputs/quotas versus masked teachers, and actual CPU fullstate resume."""
import copy
import hashlib
import sys
from pathlib import Path
import pytest
import torch
from jmicro.training import rng_state
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from conditional_prefix_mask_trainer import PrefixMaskSampler,PrefixMaskTrainer
from source_order_condition_trainer import SourceOrderQuotaSampler
from parameter_displacement_anchor_trainer import ParameterAnchorTrainer
from test_parameter_displacement_anchor import mixed_fixture
from run_eos_short_pilot import equal_state


def shared_fixture(tmp_path):
    pool,parent,b,positive=mixed_fixture(tmp_path)
    trainer=ParameterAnchorTrainer(parent,pool,pool,positive,
        dict(web=19,story=11,ordinary_textbook=25,conditional_textbook=150),b,0.,'cpu',8,3)
    for _ in range(2):trainer.step()
    assert trainer.sampler.source_teachers['conditional_textbook']==0
    trainer.save(tmp_path/'shared.pt')
    return pool,torch.load(tmp_path/'shared.pt',weights_only=False),b,positive


def test_original_input_reference_digest_masked_targets_and_terminal_padding(tmp_path):
    pool,parent,b,positive=shared_fixture(tmp_path)
    original=SourceOrderQuotaSampler(pool,pool,positive,parent['sampler']['streams']['web']['sampler'],
        parent['sampler']['goals'],8,42)
    original.load_state_dict(parent['sampler'])
    masked=PrefixMaskSampler(pool,pool,positive,parent['sampler']);masked.reference_token_digest=parent['token_digest']
    digest=parent['token_digest'];conditional_zero_focus=False;terminal_padding=False
    while original.source_teachers!=original.goals:
        x,y,_,focus=original.batch(100);a,z,_,f=masked.batch(100)
        assert torch.equal(x,a) and torch.equal(focus,f)
        d=hashlib.sha256(bytes.fromhex(digest));d.update(x.numpy().astype('<i8').tobytes());d.update(y.numpy().astype('<i8').tobytes());digest=d.hexdigest()
        assert digest==masked.reference_token_digest
        assert equal_state(original.state_dict(),masked.reference_state())
        for i,genre in enumerate(masked.last_genres):
            if genre=='conditional_textbook':
                keep=focus[i]|y[i].eq(3);expected=y[i].clone();expected[~keep]=-100
                assert torch.equal(z[i],expected)
                conditional_zero_focus|=not bool(focus[i].any())
            else:assert torch.equal(z[i],y[i])
            terminal_padding|=genre=='web' and not bool(y[i].ne(-100).any())
    assert terminal_padding
    assert sum(masked.actual['removed_prefix'].values())>0
    assert masked.actual['eos']['conditional_textbook']==original.source_eos['conditional_textbook']
    wrong=copy.deepcopy(masked.state_dict());wrong['prefix_mask_accounting']['actual']['teachers']['story']+=1
    with pytest.raises(ValueError,match='accounting'):masked.load_state_dict(wrong)
    zero_focus=copy.copy(positive);zero_focus.focus=positive.focus.copy();zero_focus.focus[:]=False
    sampler=PrefixMaskSampler(pool,pool,zero_focus,parent['sampler']);sampler.reference_token_digest=parent['token_digest']
    _,y,_,f=sampler.batch(100)
    conditional=[i for i,g in enumerate(sampler.last_genres) if g=='conditional_textbook']
    assert conditional and not f[conditional].any()
    assert y[conditional].eq(3).any() and not y[conditional].ge(8).any()


def test_initial_fullstate_and_resume_across_real_conditional_mask_transition(tmp_path):
    pool,parent,b,positive=shared_fixture(tmp_path)
    def build(binding=b):return PrefixMaskTrainer(parent,pool,pool,positive,binding,'cpu')
    initial=build()
    for key,actual in [('model',initial.model.state_dict()),('optimizer',initial.optimizer.state_dict()),
            ('scheduler',initial.scheduler.state_dict()),('rng',rng_state()),('sampler',initial.sampler.reference_state())]:
        assert equal_state(actual,parent[key]),key
    left=[initial.step() for _ in range(4)];initial.save(tmp_path/'continuous.pt')
    trainer=build();right=[trainer.step() for _ in range(2)];trainer.save(tmp_path/'split.pt')
    trainer=build();trainer.load(tmp_path/'split.pt');right.extend(trainer.step() for _ in range(2));trainer.save(tmp_path/'resumed.pt')
    a=torch.load(tmp_path/'continuous.pt',weights_only=False);z=torch.load(tmp_path/'resumed.pt',weights_only=False)
    assert equal_state(a,z)
    for key in set(left[0])-{'seconds','data_wait_seconds','tokens_per_second'}:
        assert equal_state([r[key] for r in left],[r[key] for r in right]),key
    assert all(r['lr']==.00001 for r in left)
    assert any(r['removed_prefix_targets']['conditional_textbook']>0 for r in left)
    assert left[0]['source_teachers']['ordinary_textbook']>parent['sampler']['source_teachers']['ordinary_textbook']
    assert left[-1]['additional_teacher_tokens']<left[-1]['reference_suffix_teacher_tokens']
    with pytest.raises(ValueError):build(dict(b,arm='other')).load(tmp_path/'split.pt')


def test_same_input_budget_uses_remaining_updates_and_own_all32_timings():
    from run_conditional_prefix_mask import estimate_training
    t=dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],terminal_save_seconds=.2)
    r=dict(timing=t)
    measured,total=estimate_training(r,318)
    assert measured['estimated_updates']==318
    assert total==pytest.approx((318*.05+1.2+.6)*1.3+150+50)
    t['histories'].pop()
    with pytest.raises(ValueError):estimate_training(r,318)
