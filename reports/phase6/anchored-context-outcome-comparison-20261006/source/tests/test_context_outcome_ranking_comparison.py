import copy
import sys
import pytest
from jmicro.experiment import ROOT,read_json
sys.path.insert(0,str(ROOT/'scripts'))
import run_context_outcome_ranking_comparison as study
from context_outcome_ranking import POLICY,OutcomePairSampler
from context_outcome_ranking_accounting import audit_ranking


def test_stronger_quality_Base_only_and_fixed_auxiliary_scope():
    c=read_json(ROOT/'configs/phase6/eos_decoupled_web_kl_comparison.json')
    c.update(research_kind=study.KIND,arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},
        ranking_policy=POLICY,ranking_inputs=read_json(study.PROPOSAL)['ranking_inputs'],prior_probe_GPU_seconds=0)
    study.scope(c)
    for key,value in (('ranking_policy',{**POLICY,'coefficient':2}),
            ('ranking_policy',{**POLICY,'families_per_update':4}),('ranking_inputs',dict(path='dev',sha256='dev')),
            ('quality_screen_baseline','weaker_mechanism_control'),('Chat_adopted',True),
            ('peak_lr',.00002),('teachers_per_new_arm',50000000)):
        with pytest.raises(ValueError):study.scope({**c,key:value})


def test_actual_prepared_train_inputs_all_counters_and_tampering():
    inputs=read_json(study.PROPOSAL)['ranking_inputs'];view=study.ranking_view(inputs)
    sampler=OutcomePairSampler(view,2,42);history=[]
    for i in (1,2):
        _,_,_,selected=sampler.next()
        history.append(dict(ranking_family_indices=selected,ranking_digest=sampler.digest,
            **{'ranking_'+k:v for k,v in study.ranking_counts(type('T',(),dict(ranking=sampler))()).items()
               if k not in ('updates','families_seen')},
            main_and_Web_reference_physical_input_tokens=i*40960,
            combined_student_physical_input_tokens=i*40960+sampler.physical_input_positions,
            combined_student_valid_input_tokens=i*40960+sampler.valid_input_tokens))
    state=dict(update=320437,spec=dict(ranking_policy=POLICY),
        ranking_state=dict(policy=POLICY,input_binding=view.binding,sampler=sampler.state_dict()))
    record=dict(ranking_input_binding=view.binding,ranking_policy=POLICY,ranking_sampler=sampler.state_dict(),
        ranking_exposure=study.ranking_counts(type('T',(),dict(ranking=sampler))()),
        main_and_Web_reference_physical_input_tokens=81920,
        combined_student_physical_input_tokens=81920+sampler.physical_input_positions,
        combined_student_valid_input_tokens=81920+sampler.valid_input_tokens)
    config=dict(ranking_inputs=inputs);parent=dict(update=320435)
    assert audit_ranking(parent,state,record,history,config)['ranking_exposure']['relational_choice_labels']==8
    for field in ('ranking_foil_body_scored_positions','ranking_valid_input_tokens',
                  'combined_student_physical_input_tokens','combined_student_valid_input_tokens'):
        bad=copy.deepcopy(history);bad[-1][field]+=1
        with pytest.raises(ValueError):audit_ranking(parent,state,record,bad,config)
    bad=copy.deepcopy(history);bad[0]['ranking_family_indices'].reverse()
    with pytest.raises(ValueError):audit_ranking(parent,state,record,bad,config)
    bad=copy.deepcopy(record);bad['ranking_exposure']['relational_choice_labels']=0
    with pytest.raises(ValueError):audit_ranking(parent,state,bad,history,config)
