import copy
import sys
import torch
import pytest
from jmicro.experiment import ROOT,sha256
sys.path.insert(0,str(ROOT/'scripts'))
import run_web_kl_comparison as study
from web_kl_comparison_accounting import audit_reference,weight_digest
from web_kl_preservation import POLICY


def test_fixed_KL_policy_main100M_and_Base_only_scope():
    c=dict(KL_policy=POLICY,failed_probe_GPU_seconds=0,research_kind=study.KIND,arms={study.ARM:study.GOALS},outcome_weights={study.ARM:1},
        teachers_per_new_arm=100000000,total_comparison_teachers=200000000,total_new_GPU_ceiling_seconds=900,
        peak_lr=.00001,optimizer_policy='inherit',source_order=list(study.SOURCE_ORDER),
        shapes=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1',Base_adopted=False,Chat_adopted=False,quantization_started=False,
        protected_test_used=False,requested_five_steps_complete=False,quality_criteria_unchanged=True)
    study.scope(c)
    for key,value in (('KL_policy',{**POLICY,'coefficient':2}),('KL_policy',{**POLICY,'reference_batch':16}),
        ('peak_lr',.0002),('source_order',list(reversed(study.SOURCE_ORDER))),('Chat_adopted',True)):
        with pytest.raises(ValueError):study.scope({**c,key:value})


def test_auxiliary_teacher_and_cursor_counters_cannot_be_hidden_or_changed():
    cursor=dict(seed=42,epoch=0,position=0,context=1024,blocks=100)
    parent=dict(update=320435,model=dict(weight=torch.tensor([1.,2.])),shard_manifest_sha256='web',
        sampler=dict(kind='eos-pilot-mixture-v1',position=0,routes=[],web=cursor,short=dict(position=0),
            source_tokens=dict(web=0,short=0),source_eos=dict(web=0,short=0)),optimizer=dict(param_groups=[dict(lr=.00001)]))
    sources={k:sha256(ROOT/k) for k in ('scripts/web_kl_preservation.py','scripts/web_kl_condition_trainer.py')}
    ref=dict(path='parent',sha256='fixed');digest=weight_digest(parent['model'])
    replay=dict(kind=POLICY['kind'],batch=8,context=1024,initial_cursor=cursor,updates=2,physical_input_tokens=16384,
        body_positions=16000,ignored_positions=384,digest='22'*32,
        stream=dict(kind='actual-parent-Web-block-cursor-v1',manifest_sha256='web',sampler={**cursor,'position':16}))
    state=dict(update=320437,spec=dict(KL_policy=POLICY,KL_sources=sources),
        lineage=dict(reference_teacher=ref,reference_teacher_weight_digest=digest),
        KL_state=dict(policy=POLICY,source_sha256=sources,reference_teacher=ref,teacher_weight_digest=digest,replay=replay))
    record=dict(KL_policy=POLICY,reference_replay=replay,reference_teacher_weight_digest=digest,reference_input_tokens=16384,
        reference_soft_target_body_positions=16000,additional_input_tokens=65536,combined_student_physical_input_tokens=81920,
        additional_supervised_tokens=65000)
    history=[dict(reference_input_tokens=i*8192,reference_soft_target_body_positions=i*8000,reference_ignored_positions=i*192,
        physical_input_tokens=i*32768,combined_student_physical_input_tokens=i*40960,reference_digest=(str(i)*2)*32) for i in (1,2)]
    config=dict(parent=ref,KL_policy=POLICY,source_sha256=sources)
    assert audit_reference(parent,state,record,history,config)['reference_cursor_blocks']==16
    bad=copy.deepcopy(record);bad['reference_input_tokens']=0
    with pytest.raises(ValueError):audit_reference(parent,state,bad,history,config)
    bad=copy.deepcopy(state);bad['KL_state']['teacher_weight_digest']='wrong'
    with pytest.raises(ValueError):audit_reference(parent,bad,record,history,config)
    bad=copy.deepcopy(history);bad[-1]['combined_student_physical_input_tokens']-=1
    with pytest.raises(ValueError):audit_reference(parent,state,record,bad,config)
