import copy
import sys
import torch
from jmicro.experiment import ROOT
from jmicro.training import rng_state
sys.path.insert(0,str(ROOT/'scripts'))
from context_outcome_ranking_trainer import ContextOutcomeRankingTrainer
from eos_decoupled_web_kl_condition_trainer import WebKLTrainer as Control
from test_original_web_retention_trainer import setup
from test_context_outcome_ranking import toy_view
from run_eos_short_pilot import equal_state


def test_all3_gradient_paths_single_Adam_update_and_full_resume_all_samplers_ledgers(tmp_path):
    pool,parent,binding,positive=setup(tmp_path)
    cursor=copy.deepcopy(parent['sampler']);parent=copy.deepcopy(parent)
    parent.update(update=320435,tokens=10500014080,supervised_tokens=10477786961,
        sampler=dict(kind='eos-pilot-mixture-v1',position=0,routes=[],web=cursor,short=dict(position=0),
            source_tokens=dict(web=0,short=0),source_eos=dict(web=0,short=0)))
    for group in parent['optimizer']['param_groups']:
        group['lr']=.00001;group['initial_lr']=.0001
    parent['scheduler']['base_lrs']=[.0001]*len(parent['optimizer']['param_groups'])
    parent['scheduler']['_last_lr']=[.00001]*len(parent['optimizer']['param_groups'])
    parent['scheduler']['last_epoch']=320435
    goals=dict(web=83,story=31,ordinary_textbook=29,conditional_textbook=37)
    def build():return ContextOutcomeRankingTrainer(parent,pool,pool,positive,goals,binding,toy_view(),'cpu',8,3,2)
    full=build()
    assert equal_state(full.model.state_dict(),parent['model'])
    assert equal_state(full.optimizer.state_dict(),parent['optimizer'])
    assert equal_state(rng_state(),parent['rng'])
    left=[full.step() for _ in range(4)];full.save(tmp_path/'full.pt')
    split=build();right=[split.step() for _ in range(2)];split.save(tmp_path/'split.pt')
    resumed=build();resumed.load(tmp_path/'split.pt')
    right.extend(resumed.step() for _ in range(2));resumed.save(tmp_path/'resumed.pt')
    a=torch.load(tmp_path/'full.pt',map_location='cpu',weights_only=False)
    b=torch.load(tmp_path/'resumed.pt',map_location='cpu',weights_only=False)
    assert equal_state(a,b)
    for x,y in zip(left,right,strict=True):
        for key in ('loss','ordinary_CE_loss','reference_KL_loss','ranking_loss','gradient_norm','lr',
                'token_digest','reference_digest','ranking_digest','ranking_family_indices',
                'ranking_gold_body_scored_positions','ranking_foil_body_scored_positions',
                'ranking_relational_choice_labels','combined_student_physical_input_tokens','combined_student_valid_input_tokens'):
            assert x[key]==y[key],key
    for param,state in a['optimizer']['state'].items():
        assert int(state['step'])==int(parent['optimizer']['state'][param]['step'])+4
    assert a['ranking_state']['sampler']['relational_choice_labels']==16
    assert left[-1]['ranking_physical_input_positions']==256
    assert left[-1]['main_and_Web_reference_physical_input_tokens']==160
    assert left[-1]['combined_student_physical_input_tokens']==416
    assert left[-1]['combined_student_valid_input_tokens']==256
    assert resumed.supervised_tokens-parent['supervised_tokens']==sum(resumed.sampler.source_teachers.values())
    assert all(row['ranking_loss']>0 for row in left)
    assert left[0]['reference_KL_loss']==0
    resumed.verify_teacher()
    control=Control(parent,pool,pool,positive,goals,binding,'cpu',8,3,2)
    plain=[control.step() for _ in range(4)]
    for x,y in zip(left,plain,strict=True):
        for key in ('token_digest','source_teachers','source_eos','source_input_tokens','source_body_bytes',
                'source_focus_teachers','reference_input_tokens','reference_soft_target_body_positions','reference_digest',
                'reference_non_EOS_teacher_probability_mass'):
            assert x[key]==y[key],key
    assert any(not torch.equal(a['model'][key],control.model.state_dict()[key]) for key in a['model'])
