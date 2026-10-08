"""Actual learned-parent resume and compact accounting; no GPU/quality claim."""
import copy
import hashlib
from pathlib import Path
import sys

import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_teacher_decay_trainer import TeacherDecayTrainer
from base_teacher_decay_2b_protocol import (resume_probe,common_stream,compact_update,
                                          audit_compact_history,audit_terminal,TOTAL,EXTRA)
from natural_context_contrast_trainer import host
from test_base_teacher_decay import build


def test_real_learned_parent_continuous_vs_resumed_allstate_history(build,tmp_path):
    source = TeacherDecayTrainer(build())
    source.step(); source.step()
    path = tmp_path/'parent.pt'
    source.save(path)
    before = hashlib.sha256(path.read_bytes()).hexdigest()
    def make(checkpoint):
        trainer = TeacherDecayTrainer(build())
        trainer.load(checkpoint)
        return trainer
    result = resume_probe(make,path,tmp_path/'split.pt',lambda:None)
    assert all(result['checks'].values())
    assert result['initial_counters']['update']==2
    assert result['final_verification_counters']['update']==6
    assert result['actual_CUDA_or_CPU_updates']==8
    assert result['verification_teacher_tokens']==2*(result['final_verification_counters']['supervised_tokens']-source.native.counters['supervised_tokens'])
    assert result['verification_weights_used_for_science'] is False
    assert before==hashlib.sha256(path.read_bytes()).hexdigest()


def test_compact_log_checks_actual_all_updates_and_same_native_stream(build):
    candidate = TeacherDecayTrainer(build())
    candidate.step(); candidate.step()
    parent = copy.deepcopy(candidate.native.counters)
    rows = [compact_update(candidate.step()) for _ in range(4)]
    final = host(candidate.state_dict())
    assert all('draw_trace' not in row for row in rows)
    actual = audit_compact_history(iter(rows),parent,final)
    assert actual['updates']==4 and actual['new_teacher_tokens']==final['counters']['supervised_tokens']-parent['supervised_tokens']
    control = build()
    for _ in range(6): control.step()
    assert all(common_stream(final,host(control.state_dict())).values())
    broken = copy.deepcopy(rows)
    broken[2]['effective_weight_decay'] = .1
    with pytest.raises(ValueError,match='LR/decay'):
        audit_compact_history(iter(broken),parent,final)
    with pytest.raises(ValueError,match='Contiguous'):
        audit_compact_history(iter(rows[1:]),parent,final)


@pytest.mark.parametrize('bad',['live','GPU_cap','combined','stream','teachers'])
def test_terminal_refuses_live_unmatched_or_undercounted_comparison(bad):
    c=dict(GPU_cap_seconds=100,prior_pilot_GPU_seconds=10,maximum_combined_GPU_seconds=110,
           parent_checkpoint=dict(path='parent',sha256='parent'),parent_counters=dict(supervised_tokens=94160195))
    job=dict(status='complete',config_sha256='frozen',pid=123,boot_id='boot',start_ticks='4',
             GPU_seconds=90,cumulative_GPU_ledger_closed=True)
    result=dict(status='learning_and_native_evaluation_complete_content_pending',config=dict(sha256='frozen'),
        identity={k:job[k] for k in ('pid','boot_id','start_ticks')},cumulative_GPU_ledger_closed=True,
        GPU_seconds=90,prior_pilot_GPU_seconds=10,combined_GPU_seconds=100,new_scientific_teacher_tokens=EXTRA,
        scientific_cumulative_teacher_tokens=TOTAL,reused_control_teacher_tokens=TOTAL,counters=dict(supervised_tokens=TOTAL),
        stream_checks=dict(full_counters=True,full_sampler=True,full_scheduler=True),
        resume_gate=dict(config_sha256='frozen',parent_checkpoint=c['parent_checkpoint'],initial_counters=c['parent_counters'],
            checks=dict(exact=True),actual_CUDA_or_CPU_updates=8,actual_device='cuda',verification_weights_used_for_science=False),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False)
    audit_terminal(job,result,c,'frozen',False)
    if bad=='GPU_cap': job['GPU_seconds']=result['GPU_seconds']=101; result['combined_GPU_seconds']=111
    elif bad=='combined': result['combined_GPU_seconds']=90
    elif bad=='stream': result['stream_checks']['full_sampler']=False
    elif bad=='teachers': result['new_scientific_teacher_tokens']=TOTAL
    with pytest.raises(ValueError): audit_terminal(job,result,c,'frozen',bad=='live')
