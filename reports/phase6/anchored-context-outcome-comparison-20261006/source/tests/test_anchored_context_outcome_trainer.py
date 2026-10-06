import copy
import sys
import pytest
import torch
from jmicro.experiment import ROOT
from jmicro.model import JMicroModel
from jmicro.training import rng_state
sys.path.insert(0,str(ROOT/'scripts'))
from anchored_context_outcome_trainer import AnchoredContextOutcomeTrainer
from context_outcome_ranking_trainer import ContextOutcomeRankingTrainer
from test_original_web_retention_trainer import setup
from test_context_outcome_ranking import toy_view
from run_eos_short_pilot import equal_state


def parent_fixture(tmp_path):
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
    return pool,parent,binding,positive


def test_full_resume_anchor_ledger_all_three_samplers_and_single_Adam_update(tmp_path):
    pool,parent,binding,positive=parent_fixture(tmp_path)
    goals=dict(web=83,story=31,ordinary_textbook=29,conditional_textbook=37)
    def build():return AnchoredContextOutcomeTrainer(parent,pool,pool,positive,goals,binding,toy_view(),'cpu',8,3,2)
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
        for key in x:
            if key not in ('seconds','data_wait_seconds','tokens_per_second'):assert equal_state(x[key],y[key]),key
    assert a['positive_anchor_state']['body_teacher_tokens']==16
    assert a['ranking_state']['sampler']['gold_body_scored_positions']==16
    assert left[-1]['combined_hard_teacher_positions']==sum(full.sampler.source_teachers.values())+16
    assert left[-1]['combined_student_physical_input_tokens']==416
    assert left[-1]['combined_student_valid_input_tokens']==256
    for param,state in a['optimizer']['state'].items():
        assert int(state['step'])==int(parent['optimizer']['state'][param]['step'])+4
    resumed.verify_teacher()
    control=ContextOutcomeRankingTrainer(parent,pool,pool,positive,goals,binding,toy_view(),'cpu',8,3,2)
    plain=[control.step() for _ in range(4)]
    for x,y in zip(left,plain,strict=True):
        for key in ('token_digest','source_teachers','source_eos','source_input_tokens','source_body_bytes',
            'source_focus_teachers','reference_input_tokens','reference_soft_target_body_positions',
            'reference_digest','reference_non_EOS_teacher_probability_mass','ranking_family_indices',
            'ranking_digest','ranking_gold_body_scored_positions','ranking_foil_body_scored_positions',
            'combined_student_physical_input_tokens','combined_student_valid_input_tokens'):
            assert x[key]==y[key],key
    assert any(not torch.equal(a['model'][k],control.model.state_dict()[k]) for k in a['model'])
    bad=copy.deepcopy(a);bad['positive_anchor_state']['body_teacher_tokens']-=1
    torch.save(bad,tmp_path/'bad.pt')
    with pytest.raises(ValueError,match='Positive hard teachers'):build().load(tmp_path/'bad.pt')


def test_actual_model_padded_valid_logits_and_future_token_causality(tmp_path):
    _,parent,_,_=parent_fixture(tmp_path)
    model=JMicroModel(parent['model_config']).eval();model.load_state_dict(parent['model'])
    inputs=torch.tensor([[2,8,9,10,0,0],[2,12,13,14,15,0]])
    valid=inputs.ne(0)
    with torch.no_grad():
        padded=model(inputs,attention_mask=valid).logits
        for row,length in ((0,4),(1,5)):
            separate=model(inputs[row:row+1,:length]).logits
            torch.testing.assert_close(padded[row,:length],separate[0],rtol=1e-5,atol=1e-6)
        changed=inputs.clone();changed[0,3]=20;changed[1,4]=21
        future=model(changed,attention_mask=valid).logits
        torch.testing.assert_close(padded[0,:3],future[0,:3],rtol=0,atol=0)
        torch.testing.assert_close(padded[1,:4],future[1,:4],rtol=0,atol=0)

