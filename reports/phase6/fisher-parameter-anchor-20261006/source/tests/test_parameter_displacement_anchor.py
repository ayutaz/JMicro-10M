"""Actual small CPU states and analytic objective; no quality or GPU-speed claim."""
import copy
import sys
from pathlib import Path
import pytest
import torch
from jmicro.training import rng_state
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from parameter_displacement_anchor_trainer import parameter_penalty,ParameterAnchorTrainer
from original_web_retention_trainer import OriginalWebQuotaSampler
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


def mixed_fixture(tmp_path):
    pool,parent,b,positive=setup(tmp_path)
    sampler=OriginalWebQuotaSampler(pool,pool,positive,parent['sampler'],
        dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=16),8)
    while sampler.source_teachers!=sampler.goals:sampler.batch(3)
    parent=copy.deepcopy(parent);parent['sampler']=sampler.state_dict()
    for group in parent['optimizer']['param_groups']:
        group['lr']=.00001;group['initial_lr']=.0001
    parent['scheduler']['base_lrs']=[.0001,.0001];parent['scheduler']['_last_lr']=[.00001,.00001]
    return pool,parent,b,positive


def test_tied_parameter_penalty_analytic_gradient_no_teacher_or_anchor_mutation():
    model=torch.nn.Module();model.a=torch.nn.Linear(2,2,bias=False);model.b=model.a
    with torch.no_grad():model.a.weight.fill_(2)
    named=list(model.named_parameters());assert len(named)==1
    anchor={k:torch.zeros_like(v) for k,v in named}
    penalty=parameter_penalty(named,anchor,.5);penalty.backward()
    assert float(penalty.detach())==4 and torch.equal(model.a.weight.grad,torch.ones_like(model.a.weight))
    assert all(torch.count_nonzero(v)==0 and v.grad is None for v in anchor.values())
    with pytest.raises(ValueError):parameter_penalty(named,{},.5)
    with pytest.raises(ValueError):parameter_penalty(named,anchor,float('nan'))


@pytest.mark.parametrize('coefficient',[0.,.04161064039180984])
def test_fullstate_initial_preservation_and_resume_through_staged_boundaries(tmp_path,coefficient):
    pool,parent,b,positive=mixed_fixture(tmp_path)
    goals=dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=80)
    def build(binding=b):return ParameterAnchorTrainer(parent,pool,pool,positive,goals,binding,coefficient,'cpu',8,3)
    trainer=build()
    assert equal_state(trainer.model.state_dict(),parent['model'])
    assert equal_state(trainer.optimizer.state_dict(),parent['optimizer'])
    assert equal_state(trainer.scheduler.state_dict(),parent['scheduler'])
    assert equal_state(rng_state(),parent['rng'])
    assert equal_state(trainer.sampler.streams['web'].sampler.state_dict(),parent['sampler']['streams']['web']['sampler'])
    assert trainer.sampler.position==0 and trainer.lineage['actual_parent_sampler']==parent['sampler']
    left=[trainer.step() for _ in range(4)];trainer.save(tmp_path/'a.pt')
    split=build();right=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    split=build();split.load(tmp_path/'split.pt');right.extend(split.step() for _ in range(2));split.save(tmp_path/'b.pt')
    a=torch.load(tmp_path/'a.pt',weights_only=False);z=torch.load(tmp_path/'b.pt',weights_only=False)
    assert equal_state(a,z)
    for key in ('loss','CE_loss','parameter_penalty','gradient_norm','source_teachers','token_digest'):
        assert [r[key] for r in left]==[r[key] for r in right]
    assert all(r['lr']==.00001 and r['parameter_penalty_teacher_tokens']==0 for r in left)
    assert left[0]['parameter_penalty']==0
    assert split.anchor_digest()==split.anchor_initial_digest
    wrong=build(dict(b,arm='different'))
    with pytest.raises(ValueError):wrong.load(tmp_path/'split.pt')
    wrong=build();wrong.anchor[next(iter(wrong.anchor))].add_(1)
    with pytest.raises(ValueError,match='anchor'):wrong.save(tmp_path/'bad.pt')


def test_own_two_arm_budget_requires_all32_rows_and_counts_saves_and_probe_separately():
    from run_parameter_displacement_anchor import estimate_training,ARMS
    timing=dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],
        verification_teacher_tokens=32000*32,terminal_save_seconds=.2)
    r=dict(timings={arm:copy.deepcopy(timing) for arm in ARMS})
    measured,total=estimate_training(r)
    assert all(t['estimated_updates']==3125 for t in measured.values())
    assert total==pytest.approx(2*(3125*.05+1.2+2.8)*1.3+150+50)
    r['timings'][ARMS[1]]['histories'].pop()
    with pytest.raises(ValueError):estimate_training(r)
