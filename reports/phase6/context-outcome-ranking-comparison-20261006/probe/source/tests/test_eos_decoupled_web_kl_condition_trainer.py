import copy
import sys
import torch
from jmicro.experiment import ROOT
from jmicro.training import rng_state
sys.path.insert(0,str(ROOT/'scripts'))
from eos_decoupled_web_kl_condition_trainer import WebKLTrainer
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


def test_combined_CPU_updates_full_resume_teacher_immutable_and_separate_reference_ledger(tmp_path):
    pool,parent,binding,positive=setup(tmp_path)
    cursor=copy.deepcopy(parent['sampler'])
    parent=copy.deepcopy(parent)
    parent.update(update=320435,tokens=10500014080,supervised_tokens=10477786961,
        sampler=dict(kind='eos-pilot-mixture-v1',position=0,routes=[],web=cursor,short=dict(position=0),
            source_tokens=dict(web=0,short=0),source_eos=dict(web=0,short=0)))
    for g in parent['optimizer']['param_groups']:
        g['lr']=.00001;g['initial_lr']=.0001
    parent['scheduler']['base_lrs']=[.0001]*len(parent['optimizer']['param_groups'])
    parent['scheduler']['_last_lr']=[.00001]*len(parent['optimizer']['param_groups'])
    parent['scheduler']['last_epoch']=320435
    goals=dict(web=83,story=31,ordinary_textbook=29,conditional_textbook=37)
    def build():return WebKLTrainer(parent,pool,pool,positive,goals,binding,'cpu',8,3,2)
    continuous=build()
    assert equal_state(continuous.model.state_dict(),parent['model'])
    assert equal_state(continuous.optimizer.state_dict(),parent['optimizer'])
    assert equal_state(rng_state(),parent['rng'])
    a=[continuous.step() for _ in range(4)];continuous.save(tmp_path/'continuous.pt')
    split=build();b=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    resumed=build();resumed.load(tmp_path/'split.pt');b.extend(resumed.step() for _ in range(2));resumed.save(tmp_path/'resumed.pt')
    left=torch.load(tmp_path/'continuous.pt',map_location='cpu',weights_only=False)
    right=torch.load(tmp_path/'resumed.pt',map_location='cpu',weights_only=False)
    assert equal_state(left,right)
    for x,y in zip(a,b,strict=True):
        for key in ('loss','ordinary_CE_loss','reference_KL_loss','gradient_norm','token_digest','reference_digest','reference_soft_target_body_positions'):
            assert x[key]==y[key],key
    assert resumed.replay.physical_input_tokens==64
    assert resumed.tokens-parent['tokens']==96
    assert resumed.supervised_tokens-parent['supervised_tokens']==sum(resumed.sampler.source_teachers.values())
    assert a[0]['reference_KL_loss']==0.
    assert any(v['reference_KL_loss']>0 for v in a[1:])
    assert 0<resumed.reference_non_EOS_teacher_mass<resumed.replay.body_positions
    assert left['KL_state']['non_EOS_teacher_probability_mass']==a[-1]['reference_non_EOS_teacher_probability_mass']
    resumed.verify_teacher()
