import copy
import sys
from pathlib import Path
import pytest
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts'), str(Path(__file__).resolve().parents[1] / 'src')]
import run_condition_query_balance_comparison as study
from review_condition_query_balance_comparison import retained_sources


def test_frozen_scope_refuses_changed_scientific_budget_or_later_stages():
    c = dict(research_kind=study.KIND, arms={study.ARM:study.GOALS}, outcome_weights={study.ARM:1},
        teachers_per_new_arm=100000000, total_comparison_teachers=200000000, total_new_GPU_ceiling_seconds=900,
        peak_lr=.0002, optimizer_policy='inherit',
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1', Base_adopted=False, Chat_adopted=False,
        quantization_started=False, protected_test_used=False, requested_five_steps_complete=False,
        quality_criteria_unchanged=True)
    study.scope(c)
    for key, value in (('teachers_per_new_arm',200000000), ('peak_lr',.002), ('Chat_adopted',True),
                       ('quantization_started',True), ('quality_criteria_unchanged',False)):
        with pytest.raises(ValueError):
            study.scope({**c,key:value})


def test_three_source_retention_does_not_treat_changed_query_stream_as_control():
    parent = dict(shard_manifest_sha256='abc', sampler=dict(seed=42,context=1024,blocks=4,epoch=0,position=1))
    sampler = dict(streams=dict(web=dict(kind='actual-parent-Web-block-cursor-v1',manifest_sha256='abc',
                       sampler={**parent['sampler'],'position':2}), story=dict(cursor=5),
                       ordinary_textbook=dict(cursor=7), conditional_textbook=dict(manifest='new')))
    for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):
        sampler[key] = dict(web=1,story=1,ordinary_textbook=1,conditional_textbook=1)
    sampler['source_tokens']['web'] = 1024
    control = copy.deepcopy(sampler); control['streams']['conditional_textbook']['manifest']='old'
    assert retained_sources(parent,dict(sampler=sampler),dict(sampler=control))['three_unchanged_sources_cursors_and_accounting_equal']
    bad = copy.deepcopy(sampler); bad['streams']['story']['cursor']=6
    with pytest.raises(ValueError):
        retained_sources(parent,dict(sampler=bad),dict(sampler=control))
    bad = copy.deepcopy(sampler); bad['source_tokens']['web']=2048
    with pytest.raises(ValueError):
        retained_sources(parent,dict(sampler=bad),dict(sampler=control))
