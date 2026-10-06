"""Real CPU fork and sampler checks, not evidence of Base quality or CUDA speed."""
import copy
import sys
import pytest
import torch
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
import run_condition_source_learning as study
from test_condition_positive_trainer import positive_fixture
from test_condition_diversity_comparison import expanded_fixture
from test_story_weight_comparison import fixture
from run_eos_short_pilot import equal_state


def test_equal_ordinary_teachers_after_new100M_style_terminal_quotas(tmp_path,monkeypatch):
    pool,_,_=fixture(tmp_path);small=positive_fixture(tmp_path);large=expanded_fixture(tmp_path/'large',small)
    monkeypatch.setattr(study,'GOALS',dict(web=417,story=209,ordinary_textbook=213,conditional_textbook=211))
    left=study.ordinary_stream_digest(pool,small);right=study.ordinary_stream_digest(pool,large)
    for key in ('target_sha256','teachers','EOS','body_bytes'):assert left[key]==right[key]


def test_both_actual_CPU_new_forks_resume_with_full_state_and_reject_old_binding(tmp_path,monkeypatch):
    pool,parent,b=fixture(tmp_path);small=positive_fixture(tmp_path);large=expanded_fixture(tmp_path/'large',small)
    monkeypatch.setattr(study,'GOALS',dict(web=400,story=200,ordinary_textbook=200,conditional_textbook=200))
    for arm,positive in (('small512',small),('large2048',large)):
        binding=dict(b,arm=arm,study_kind=study.KIND)
        build=lambda:study.trainer_for(parent,pool,positive,binding,'cpu',8,3)
        a=build();left=[a.step() for _ in range(4)];a.save(tmp_path/arm/'a.pt')
        t=build();right=[t.step() for _ in range(2)];t.save(tmp_path/arm/'split.pt')
        t=build();t.load(tmp_path/arm/'split.pt');right.extend(t.step() for _ in range(2));t.save(tmp_path/arm/'b.pt')
        x=torch.load(tmp_path/arm/'a.pt',weights_only=False);y=torch.load(tmp_path/arm/'b.pt',weights_only=False)
        for key in ('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes','token_digest','focus_token_digest','spec','study_binding'):
            assert equal_state(x[key],y[key]),key
        assert [r['loss'] for r in left]==[r['loss'] for r in right]
        assert x['spec']['research_kind']==study.KIND and x['weighted_teacher_mass']==x['supervised_tokens']-parent['supervised_tokens']
        wrong=study.trainer_for(parent,pool,positive,dict(binding,study_kind='old25M'),'cpu',8,3)
        with pytest.raises(ValueError):wrong.load(tmp_path/arm/'split.pt')


def test_both_measured100M_budget_includes_saves_and_two_evaluations_plus_source_cases():
    timing=dict(histories=[dict(seconds=.2 if i<8 else .05) for i in range(32)],verification_teacher_tokens=32000*32,terminal_save_seconds=.2)
    out,total=study.estimate_training(dict(timings={a:copy.deepcopy(timing) for a in study.ARMS}))
    assert all(x['estimated_updates']==3125 for x in out.values())
    assert total==pytest.approx(2*(3125*.05+1.2+2.8)*1.3+620)
    bad=copy.deepcopy(timing);bad['histories'].pop()
    with pytest.raises(ValueError):study.estimate_training(dict(timings=dict(small512=timing,large2048=bad)))


def test_original_source_fit_uses_only_actual_original_label_and_keeps_weak_subset():
    prepared=dict(cases=[],families=[]);rows=[]
    for family,group in enumerate(('old512_fixed64','new1536_fixed64')):
        prepared['families'].append(dict(index=family,content_annotation=dict(weak_pair=family==1)))
        for mode in study.ranking.MODES:
            for label in (0,1):
                for candidate in (0,1):
                    index=len(rows);prepared['cases'].append(dict(index=index,family=family,group=group,mode=mode,candidate=candidate,source_matching_label=label))
                    rows.append(dict(index=index,target_tokens=2,log_likelihood=-4. if candidate==label else -20.))
    out=study.source_fit(rows,prepared)
    assert out['original_history']['all128']['outcomes']==4
    assert out['original_history']['all128']['token_weighted_mean_NLL']==2
    assert out['original_history']['nonweak116']['outcomes']==2
    assert out['isolated_condition']['new1536_fixed64']['outcomes']==2


def test_scope_requires_two_fresh_equal100M_weight1_Base_only():
    c=dict(research_kind=study.KIND,arms={a:study.GOALS for a in study.ARMS},outcome_weights={a:1 for a in study.ARMS},
        teachers_per_arm=100000000,new_scientific_teacher_tokens=200000000,total_new_GPU_ceiling_seconds=1200,peak_lr=.0002,optimizer_policy='inherit',
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),loss='ordinary original body+EOS CE, outcome weight1',
        Base_adopted=False,Chat_adopted=False,protected_test_used=False,requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for change in (dict(teachers_per_arm=25000000),dict(Chat_adopted=True),dict(outcome_weights={a:4 for a in study.ARMS}),dict(protected_test_used=True)):
        with pytest.raises(ValueError):study.scope(dict(c,**change))
