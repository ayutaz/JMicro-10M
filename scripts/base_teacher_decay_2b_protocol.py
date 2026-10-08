"""Continuation/resume and accounting contracts, without changing learned state."""
import gc
import math

import torch
from jmicro.phase5 import equal_state
from natural_context_contrast_trainer import host

TOTAL = 2000000000
START = 94160195
EXTRA = TOTAL-START
STREAM_KEYS = ('full_counters','full_sampler','full_scheduler')
COUNTERS = ('update','supervised_tokens','CE_input_tokens','auxiliary_input_tokens','auxiliary_pairs',
            'physical_input_tokens','original_body_bytes','token_digest','source_teachers','source_EOS')
LOG_KEYS = (*COUNTERS,'CE_targets_this_update','CE_loss','gradient_norm','lr','effective_weight_decay',
            'decay_only_factor_this_update','seconds','data_wait_seconds','committed_update')


def ancestry_binding(pilot):
    return dict(config_sha256=pilot['sha256'],source_binding=pilot['source_binding'],
                weights_role='scientific_fresh_teacher_decay_pilot')


def compact_update(row):
    return {key:row[key] for key in LOG_KEYS}


def common_stream(state,control):
    return {key:equal_state(state[field],control[field]) for key,field in
            zip(STREAM_KEYS,('counters','sampler','scheduler'),strict=True)}


def resume_probe(make,parent,save_path,check):
    """Run exactly4 vs2+save+2 updates from the SAME learned parent."""
    a = make(parent)
    device = a.native.device
    initial = host(a.state_dict())
    first = []
    for _ in range(4):
        check(); first.append(a.step())
    expected = host(a.state_dict())
    del a
    gc.collect()
    if device.type=='cuda': torch.cuda.empty_cache()
    b = make(parent)
    same_parent = equal_state(initial,host(b.state_dict()))
    second = []
    for _ in range(2):
        check(); second.append(b.step())
    b.save(save_path)
    del b
    gc.collect()
    if device.type=='cuda': torch.cuda.empty_cache()
    d = make(save_path)
    for _ in range(2):
        check(); second.append(d.step())
    actual = host(d.state_dict())
    del d
    gc.collect()
    if device.type=='cuda': torch.cuda.empty_cache()
    strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    checks = {key:equal_state(expected[key],actual[key]) for key in expected}
    checks.update(same_learned_parent_before_first_update=same_parent,
                  full_committed_history=equal_state([strip(r) for r in first],[strip(r) for r in second]))
    return dict(checks=checks,actual_CUDA_or_CPU_updates=8,verification_microbatches=8,
        initial_counters=initial['counters'],final_verification_counters=expected['counters'],
        verification_teacher_tokens=2*(expected['counters']['supervised_tokens']-initial['counters']['supervised_tokens']),
        verification_weights_used_for_science=False)


def audit_terminal(job,result,c,digest,live):
    if (live or job['status']!='complete' or result['status']!='learning_and_native_evaluation_complete_content_pending'
            or job['config_sha256']!=digest or result['config']['sha256']!=digest
            or result['identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not job['cumulative_GPU_ledger_closed'] or not result['cumulative_GPU_ledger_closed']
            or not 0<result['GPU_seconds']==job['GPU_seconds']<=c['GPU_cap_seconds']
            or result['prior_pilot_GPU_seconds']!=c['prior_pilot_GPU_seconds']
            or result['combined_GPU_seconds']!=result['GPU_seconds']+c['prior_pilot_GPU_seconds']
            or result['combined_GPU_seconds']>c['maximum_combined_GPU_seconds']
            or result['new_scientific_teacher_tokens']!=EXTRA
            or result['scientific_cumulative_teacher_tokens']!=TOTAL
            or result['reused_control_teacher_tokens']!=TOTAL
            or result['counters']['supervised_tokens']!=TOTAL
            or set(result['stream_checks'])!=set(STREAM_KEYS)
            or not all(v is True for v in result['stream_checks'].values())
            or result['resume_gate']['config_sha256']!=digest
            or result['resume_gate']['parent_checkpoint']!=c['parent_checkpoint']
            or result['resume_gate']['initial_counters']!=c['parent_counters']
            or not result['resume_gate']['checks'] or not all(v is True for v in result['resume_gate']['checks'].values())
            or result['resume_gate']['actual_CUDA_or_CPU_updates']!=8
            or result['resume_gate']['actual_device']!='cuda'
            or result['resume_gate']['verification_weights_used_for_science'] is not False
            or any(result[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
        raise ValueError('Actual exited bounded same-parent cumulative2B comparison required')


def audit_compact_history(rows,parent,terminal):
    """One pass over small update records; no replay or full draw-trace scan."""
    from base_teacher_decay_trainer import effective_decay
    count = parent['update']
    tokens = parent['supervised_tokens']
    last = None
    schedule = terminal['scheduler']
    for row in rows:
        count += 1
        n = row['CE_targets_this_update']
        tokens += n
        lr = (schedule['peak']*tokens/schedule['warmup'] if tokens<=schedule['warmup'] else
              schedule['final']+(schedule['peak']-schedule['final'])*(1+math.cos(
                  math.pi*((tokens-schedule['warmup'])/(schedule['total']-schedule['warmup']))))/2)
        if (row['update']!=count or row['supervised_tokens']!=tokens or type(n) is not int or n<=0
                or not row['committed_update'] or not math.isfinite(row['CE_loss'])
                or not 0<row['gradient_norm']<math.inf or row['lr']!=lr
                or row['effective_weight_decay']!=effective_decay(lr,n)
                or row['decay_only_factor_this_update']!=1-lr*row['effective_weight_decay']):
            raise ValueError('Contiguous finite original-teacher LR/decay update required')
        last = row
    if (last is None or count!=terminal['counters']['update']
            or any(last[k]!=terminal['counters'][k] for k in COUNTERS)):
        raise ValueError('Exact final compact history and fullstate counters required')
    return dict(updates=count-parent['update'],new_teacher_tokens=tokens-parent['supervised_tokens'],
                first_update=parent['update']+1,last_update=count,
                all_committed_updates_finite_LR_decay_counters_verified=True,full_draw_traces_rescanned=False)
