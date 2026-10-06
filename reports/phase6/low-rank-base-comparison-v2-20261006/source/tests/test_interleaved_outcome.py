"""Small real CPU optimizer states; synthetic historical counters are protocol fixtures."""
import copy
import hashlib
import sys
from pathlib import Path
import pytest
import torch
from jmicro.training import rng_state
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from interleaved_outcome_trainer import InterleavedOutcomeSampler,InterleavedOutcomeTrainer,SOURCE_ORDER
from original_web_retention_trainer import OriginalWebQuotaSampler
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


def historical_fixture(tmp_path):
    pool,parent,b,positive=setup(tmp_path);parent=copy.deepcopy(parent)
    cursor=parent['sampler'];parent['sampler']=dict(kind='eos-pilot-mixture-v1',position=0,routes=[],
        web=cursor,short=dict(position=0),source_tokens=dict(web=0,short=0),source_eos=dict(web=0,short=0))
    parent.update(update=320435,tokens=10500014080,supervised_tokens=10477786961)
    for group in parent['optimizer']['param_groups']:group.update(lr=.00001,initial_lr=.0001)
    parent['scheduler']['base_lrs']=[.0001,.0001];parent['scheduler']['_last_lr']=[.00001,.00001]
    return pool,parent,b,positive


def test_original_interleaved_reference_and_both_order_source_windows_targets_are_identical(tmp_path):
    pool,parent,_,positive=historical_fixture(tmp_path);cursor=parent['sampler']['web']
    goals=dict(web=199,story=51,ordinary_textbook=71,conditional_textbook=197)
    original=OriginalWebQuotaSampler(pool,pool,positive,cursor,goals,8)
    mixed=InterleavedOutcomeSampler(pool,pool,positive,cursor,goals,8);mixed.reference_token_digest=parent['token_digest']
    digest=parent['token_digest']
    while original.source_teachers!=goals:
        x,y,_,f=original.batch(3);a,z,_,focused=mixed.batch(3)
        assert torch.equal(x,a) and torch.equal(f,focused)
        d=hashlib.sha256(bytes.fromhex(digest));d.update(x.numpy().astype('<i8').tobytes());d.update(y.numpy().astype('<i8').tobytes());digest=d.hexdigest()
        assert digest==mixed.reference_token_digest and equal_state(original.state_dict(),mixed.reference_state())
        for i,g in enumerate(mixed.last_genres):
            expected=y[i].clone()
            if g=='conditional_textbook':expected[~(f[i]|y[i].eq(3))]=-100
            assert torch.equal(expected,z[i])
    staged=InterleavedOutcomeSampler(pool,pool,positive,cursor,goals,8,reference_policy='staged');staged.reference_token_digest=parent['token_digest']
    while staged.source_teachers!=goals:staged.batch(3)
    assert mixed.source_digests==staged.source_digests and mixed.actual==staged.actual
    assert mixed.reference_token_digest!=staged.reference_token_digest
    for key in ('streams','source_tokens','source_teachers','source_eos','source_body_bytes','source_focus_teachers'):
        assert equal_state(mixed.reference_state()[key],staged.reference_state()[key]),key


def test_original_fullstate_LR_and_exact_cpu_resume_with_active_mixed_mask(tmp_path):
    pool,parent,b,positive=historical_fixture(tmp_path);goals=dict(web=199,story=51,ordinary_textbook=71,conditional_textbook=197)
    def build(binding=b):return InterleavedOutcomeTrainer(parent,pool,pool,positive,goals,binding,'cpu',8,3)
    t=build()
    for key,value in [('model',t.model.state_dict()),('optimizer',t.optimizer.state_dict()),('scheduler',t.scheduler.state_dict()),('rng',rng_state())]:
        assert equal_state(value,parent[key]),key
    assert t.sampler.streams['web'].sampler.state_dict()==parent['sampler']['web']
    a=[t.step() for _ in range(4)];t.save(tmp_path/'continuous.pt')
    t=build();z=[t.step() for _ in range(2)];t.save(tmp_path/'split.pt');t=build();t.load(tmp_path/'split.pt')
    z.extend(t.step() for _ in range(2));t.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'continuous.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    for key in set(a[0])-{'seconds','data_wait_seconds','tokens_per_second'}:assert equal_state([r[key] for r in a],[r[key] for r in z]),key
    assert a[-1]['removed_prefix_targets']['conditional_textbook']>0 and all(r['lr']==.00001 for r in a)
    assert a[-1]['additional_teacher_tokens']<a[-1]['reference_suffix_teacher_tokens']
    with pytest.raises(ValueError):build(dict(b,arm='wrong')).load(tmp_path/'split.pt')
    bad=copy.deepcopy(t.sampler.state_dict());bad['prefix_mask_accounting']['reference_policy']='staged'
    with pytest.raises(ValueError):t.sampler.load_state_dict(bad)


def test_reference_update_budget_uses_own32_timings_save_margin_and_evaluation_reserve():
    from run_interleaved_outcome_order import estimate_training
    r=dict(timing=dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],terminal_save_seconds=.2))
    t,total=estimate_training(r,3068)
    assert t['estimated_updates']==3068
    assert total==pytest.approx((3068*.05+1.2+2.8)*1.3+150+50)
    r['timing']['histories'].pop()
    with pytest.raises(ValueError):estimate_training(r,3068)
