import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_preference_trainer import CommonWebTrainer,PairPreferenceTrainer,PairQuotaSampler,build_reference
from test_livedoor_base_trainer import prefix_fixture
from run_eos_short_pilot import equal_state
from jmicro.training import rng_state


def fixture(tmp_path):
    web,parent,binding=prefix_fixture(tmp_path)
    parent['sampler']=dict(kind='eos-pilot-mixture-v1',web=parent['sampler']['streams']['web']['sampler'],position=0)
    pairs=[dict(id=str(i),prompt_ids=[2,8,9],chosen_ids=[10,11,3],rejected_ids=[12,12,12,12]) for i in range(6)]
    return web,parent,binding,pairs


def test_actual_common_Web_inherits_and_exact_quota_resume(tmp_path):
    web,parent,binding,_=fixture(tmp_path)
    def build():return CommonWebTrainer(parent,web,95,binding,'cpu',8,3)
    a=build()
    for key,actual in (('model',a.model.state_dict()),('optimizer',a.optimizer.state_dict()),('scheduler',a.scheduler.state_dict()),('rng',rng_state())):
        assert equal_state(actual,parent[key])
    while a.sampler.source_teachers!=a.sampler.goals:a.step()
    a.save(tmp_path/'continuous.pt')
    b=build();b.step();b.step();b.save(tmp_path/'split.pt');b=build();b.load(tmp_path/'split.pt')
    while b.sampler.source_teachers!=b.sampler.goals:b.step()
    b.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'continuous.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    assert a.supervised_tokens-parent['supervised_tokens']==95


def test_full_pair_reference_loss_and_every_state_exact_resume_both_objectives(tmp_path):
    web,parent,binding,pairs=fixture(tmp_path);common=CommonWebTrainer(parent,web,50,binding,'cpu',8,3)
    while common.sampler.source_teachers!=common.sampler.goals:common.step()
    common.save(tmp_path/'common.pt');parent=torch.load(tmp_path/'common.pt',weights_only=False)
    sampler=PairQuotaSampler(pairs,100,2,web.byte_lengths,'unused');reference=build_reference(common.model,sampler,'cpu','fp32')
    for coefficient in (0.,.1):
        def build():return PairPreferenceTrainer(parent,web,pairs,100,coefficient,reference,binding,'cpu',2)
        a=build();left=[a.step() for _ in range(4)];a.save(tmp_path/f'a-{coefficient}.pt')
        b=build();right=[b.step() for _ in range(2)];b.save(tmp_path/f'split-{coefficient}.pt');b=build();b.load(tmp_path/f'split-{coefficient}.pt');right+=[b.step() for _ in range(2)];b.save(tmp_path/f'b-{coefficient}.pt')
        assert equal_state(torch.load(tmp_path/f'a-{coefficient}.pt',weights_only=False),torch.load(tmp_path/f'b-{coefficient}.pt',weights_only=False))
        assert left[0]['mean_reference_ratio_margin']==0.
        for key in left[0]:
            if key!='seconds':assert [r[key] for r in left]==[r[key] for r in right]
        assert left[0]['loss']==pytest.approx(left[0]['CE_loss']+coefficient*left[0]['DPO_loss'],rel=1e-6)


def test_partial_CE_tail_full_active_DPO_positions_and_binding_rejection(tmp_path):
    web,parent,binding,pairs=fixture(tmp_path);base=CommonWebTrainer(parent,web,50,binding,'cpu',8,3)
    reference=build_reference(base.model,PairQuotaSampler(pairs,7,2,web.byte_lengths,'unused'),'cpu','fp32')
    records=[];states=[]
    for coefficient in (0.,.1):
        trainer=PairPreferenceTrainer(parent,web,pairs,7,coefficient,reference,binding,'cpu',2)
        rows=[]
        while trainer.sampler.teachers!=7:rows.append(trainer.step())
        trainer.save(tmp_path/f'terminal-{coefficient}.pt');states.append(torch.load(tmp_path/f'terminal-{coefficient}.pt',weights_only=False));records.append(rows)
        assert trainer.sampler.teachers==7 and trainer.sampler.scored_chosen==9 and trainer.sampler.scored_rejected==12
        assert trainer.sampler.active_pair_exposures==3 and trainer.sampler.EOS==2
    assert equal_state(states[0]['sampler'],states[1]['sampler']) and states[0]['token_digest']==states[1]['token_digest']
    assert records[0][-1]['optimizer_pair_exposures']==0 and records[1][-1]['optimizer_pair_exposures']==3
    bad=copy.deepcopy(reference);bad['span']+=1
    with pytest.raises(ValueError):PairPreferenceTrainer(parent,web,pairs,7,.1,bad,binding,'cpu',2)
