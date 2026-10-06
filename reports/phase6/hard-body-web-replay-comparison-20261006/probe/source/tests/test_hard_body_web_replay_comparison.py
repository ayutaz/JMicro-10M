import copy
import sys
import torch
import pytest
from jmicro.experiment import ROOT, sha256
sys.path.insert(0, str(ROOT/'scripts'))
import run_hard_body_web_replay_comparison as study
from hard_body_web_replay_accounting import audit_reference, weight_digest
from hard_body_web_replay import POLICY


def test_fixed_gold_policy_and_stronger_quality_control_Base_only_scope():
    c = dict(quality_screen_baseline=study.QUALITY_BASELINE, auxiliary_policy=POLICY,
        prior_probe_GPU_seconds=study.PRIOR_GPU, research_kind=study.KIND,
        arms={study.ARM:study.GOALS}, outcome_weights={study.ARM:1}, teachers_per_new_arm=100000000,
        total_comparison_teachers=200000000, total_new_GPU_ceiling_seconds=900, peak_lr=.00001,
        optimizer_policy='inherit', source_order=list(study.SOURCE_ORDER),
        shapes=dict(context=1024, batch=32, accumulation=1, backend='flash', compile_mode='reduce-overhead', dtype='bf16'),
        loss='ordinary original body+EOS CE, outcome weight1', Base_adopted=False, Chat_adopted=False,
        quantization_started=False, protected_test_used=False, requested_five_steps_complete=False,
        quality_criteria_unchanged=True)
    study.scope(c)
    for key, value in (('quality_screen_baseline', 'weaker-conditionalKL-control'),
            ('auxiliary_policy', {**POLICY, 'coefficient':2}), ('auxiliary_policy', {**POLICY, 'reference_batch':16}),
            ('peak_lr', .0002), ('source_order', list(reversed(study.SOURCE_ORDER))), ('Chat_adopted', True)):
        with pytest.raises(ValueError):
            study.scope({**c,key:value})


def test_hard_target_counts_cannot_be_hidden_in_weighted_mass_or_soft_target_ledger():
    cursor = dict(seed=42, epoch=0, position=0, context=1024, blocks=100)
    parent = dict(update=320435, model=dict(weight=torch.tensor([1.,2.])), shard_manifest_sha256='web',
        sampler=dict(kind='eos-pilot-mixture-v1', position=0, routes=[], web=cursor, short=dict(position=0),
            source_tokens=dict(web=0,short=0), source_eos=dict(web=0,short=0)), optimizer=dict(param_groups=[dict(lr=.00001)]))
    sources = {k:sha256(ROOT/k) for k in ('scripts/hard_body_web_replay.py', 'scripts/hard_body_web_replay_trainer.py', 'scripts/web_kl_preservation.py')}
    ref = dict(path='parent',sha256='fixed')
    digest = weight_digest(parent['model'])
    replay = dict(kind=POLICY['kind'], batch=8, context=1024, initial_cursor=cursor, updates=2, physical_input_tokens=16384,
        body_positions=16000, ignored_positions=384, digest='22'*32,
        stream=dict(kind='actual-parent-Web-block-cursor-v1', manifest_sha256='web', sampler={**cursor,'position':16}))
    state = dict(update=320437, spec=dict(auxiliary_policy=POLICY, auxiliary_sources=sources),
        lineage=dict(reference_teacher=ref, reference_teacher_weight_digest=digest),
        hard_replay_state=dict(hard_body_teacher_tokens=16000, non_EOS_teacher_probability_mass=15999.,
            policy=POLICY, source_sha256=sources, reference_teacher=ref, teacher_weight_digest=digest, replay=replay))
    record = dict(reference_non_EOS_teacher_probability_mass=15999., auxiliary_policy=POLICY, reference_replay=replay,
        reference_teacher_weight_digest=digest, reference_input_tokens=16384, reference_hard_body_target_positions=16000,
        additional_input_tokens=65536, combined_student_physical_input_tokens=81920,
        additional_supervised_tokens=65000, combined_hard_teacher_positions=81000)
    history = [dict(reference_non_EOS_teacher_probability_mass=i*7999.5, reference_input_tokens=i*8192,
        reference_hard_body_target_positions=i*8000, reference_ignored_positions=i*192,
        physical_input_tokens=i*32768, combined_student_physical_input_tokens=i*40960,
        reference_digest=(str(i)*2)*32, additional_teacher_tokens=i*32500, combined_hard_teacher_positions=i*40500) for i in (1,2)]
    config = dict(parent=ref, auxiliary_policy=POLICY, source_sha256=sources)
    result = audit_reference(parent,state,record,history,config)
    assert result['reference_cursor_blocks'] == 16
    assert result['reference_hard_body_teacher_tokens'] == 16000
    assert result['combined_hard_teacher_positions'] == 81000
    bad = copy.deepcopy(state)
    bad['hard_replay_state']['hard_body_teacher_tokens'] = 15999  # Probability mass isn't integer target count.
    with pytest.raises(ValueError):
        audit_reference(parent,bad,record,history,config)
    bad = copy.deepcopy(record)
    bad['reference_non_EOS_teacher_probability_mass'] = 0
    with pytest.raises(ValueError):
        audit_reference(parent,state,bad,history,config)
    bad = copy.deepcopy(history)
    bad[-1]['combined_hard_teacher_positions'] = 65000  # Hides additional gold teachers.
    with pytest.raises(ValueError):
        audit_reference(parent,state,record,bad,config)
    bad = copy.deepcopy(state)
    bad['hard_replay_state']['teacher_weight_digest'] = 'wrong'
    with pytest.raises(ValueError):
        audit_reference(parent,bad,record,history,config)
