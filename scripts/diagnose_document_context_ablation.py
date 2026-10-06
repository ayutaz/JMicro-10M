"""Fixed TRAIN16 cached full-history CE versus same-document native attention."""
import argparse
import gc
import hashlib
import json
import os
from pathlib import Path
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json,implementation_hashes,rng_state,restore_rng,gpu_lock,synchronize
from phase6_performance import identity,alive
from run_eos_short_pilot import equal_state
from source_gradient_attribution import GROUPS,target_groups,readonly_checks
from document_context_ablation import context_logits,group_losses,all_groups,summarize
import diagnose_source_gradient_attribution as prior

PROPOSAL=ROOT/'reports/phase6/document_context_ablation_proposal.json'
CONFIG=ROOT/'configs/phase6/document_context_ablation.json'
RUN=ROOT/'reports/phase6/document-context-ablation-20261006'
TESTS=ROOT/'reports/phase6/document_context_ablation_tests.xml'
SOURCES=('scripts/document_context_ablation.py','scripts/diagnose_document_context_ablation.py',
    'scripts/diagnose_document_context_ablation.ps1','tests/test_document_context_ablation.py','scripts/source_gradient_attribution.py')
reference,check_reference=prior.reference,prior.check_reference
MARKER=dict(completed_conditional_CE_increase_at_least_nats=.1,completed_logical_batches_with_increase_at_least_nats=.1,
    completed_batches_at_least=12,learned_endpoint_only_not_parent_selection=True)


def previous_terminal():
    job=read_json(prior.RUN/'job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Previous actual gradient job must be terminal')


def input_check(entry,row):
    x,y,routes=entry['x'],entry['y'],entry['routes']
    if (x.shape!=(32,1024) or y.shape!=x.shape or x.eq(0).any() or routes!=row['actual_source_routes']
            or hashlib.sha256(x.numpy().astype('<i8').tobytes()).hexdigest()!=row['input_sha256']
            or hashlib.sha256(y.numpy().astype('<i8').tobytes()).hexdigest()!=row['target_sha256']
            or int(y.ne(-100).sum())!=row['teachers']
            or {g:int(m.sum()) for g,m in target_groups(y,routes).items()}!=row['teachers_by_group']):
        raise ValueError('All fixed original TRAIN input/masked targets/groups/counts required')


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();p=read_json(PROPOSAL);old=prior.inspect();previous_terminal()
    if (p['frozen_checkpoints']!=old['checkpoints'] or p['CPU_preparation_ceiling_seconds']!=15 or p['total_new_GPU_ceiling_seconds']!=30
            or p['descriptive_marker']!=MARKER or p['optimizer_updates'] or p['new_teacher_tokens'] or p['protected_test_used']):
        raise ValueError('Original sole read-only document-history hypothesis required')
    for ref in (p['trigger'],p['source_config'],p['cached_full_causal_reference'],p['fixed_inputs']['samples'],p['fixed_inputs']['metadata']):check_reference(ref)
    suites=list(ET.parse(TESTS).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Three actual CPU native-control/boundary/delta tests required')
    batches=torch.load(p['fixed_inputs']['samples']['path'],map_location='cpu',weights_only=False)
    metadata=read_json(Path(p['fixed_inputs']['metadata']['path']));cached=read_json(Path(p['cached_full_causal_reference']['path']))
    if len(batches)!=16 or not metadata['matched_existing_training_all16'] or cached['config_sha256']!=sha256(prior.CONFIG):raise ValueError('Completed fixed TRAIN16 reference required')
    for i,(entry,row) in enumerate(zip(batches,metadata['rows'],strict=True)):
        input_check(entry,row)
        for arm,model in cached['models'].items():
            record=model['records'][i]
            if record['input']!=row or model['checkpoint']!=p['frozen_checkpoints'][arm] or not all(model['read_only_checks'].values()):
                raise ValueError('Every actual cached model/count input must match')
            if {g:record['diagnostics']['groups'][g]['teachers'] for g in GROUPS}!=row['teachers_by_group']:raise ValueError('Cached group teacher count differs')
    elapsed=time.monotonic()-started
    if elapsed>15:raise TimeoutError('CPU15s exhausted')
    RUN.mkdir(parents=True,exist_ok=True)
    c=dict(checkpoints=p['frozen_checkpoints'],proposal=reference(PROPOSAL),references=dict(trigger=p['trigger'],source_config=p['source_config'],
        cached_full_causal=p['cached_full_causal_reference'],samples=p['fixed_inputs']['samples'],metadata=p['fixed_inputs']['metadata'],CPU_tests=reference(TESTS)),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},implementation=implementation_hashes(),
        logical_batch=32,microbatch=8,context=1024,batches=16,dtype='bf16',backend='math',position_policy='Original absolute positions, no position reset',
        control_tolerance=dict(atol=.02,rtol=.002),descriptive_marker=MARKER,CPU_preparation_seconds=elapsed,GPU_ceiling_seconds=30,
        optimizer_updates=0,new_teacher_tokens=0,quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,created_at=now())
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='fixed_same_document_history_assay_prepared',CPU_seconds=elapsed)),flush=True)


def inspect():
    c=read_json(CONFIG);p=read_json(PROPOSAL);previous_terminal()
    if (c['checkpoints']!=p['frozen_checkpoints'] or c['source_sha256']!={s:sha256(ROOT/s) for s in SOURCES}
            or c['implementation']!=implementation_hashes() or (c['logical_batch'],c['microbatch'],c['context'],c['batches'],c['GPU_ceiling_seconds'])!=(32,8,1024,16,30)
            or (c['dtype'],c['backend'])!=('bf16','math') or c['position_policy']!='Original absolute positions, no position reset'
            or c['control_tolerance']!=dict(atol=.02,rtol=.002) or c['descriptive_marker']!=MARKER
            or c['optimizer_updates'] or c['new_teacher_tokens'] or c['protected_test_used'] or c['Base_complete'] or c['Chat_started'] or c['quantization_started']):
        raise ValueError('Frozen bounded native document-context protocol differs')
    for ref in (c['proposal'],*c['references'].values(),*c['checkpoints'].values()):check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual context diagnostic live; no duplicate')
    return c


def run():
    c=inspect();jp=RUN/'job.json';old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(CONFIG):raise ValueError('Previous diagnostic job binding differs')
    if old.get('status')=='complete':print('Original completed document-context assay retained');return
    previous=old.get('GPU_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),GPU_seconds=previous,started_at=now(),
        restart_command='scripts/diagnose_document_context_ablation.ps1 -Worker',optimizer_updates=0,new_teacher_tokens=0)
    atomic_json(jp,job)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Read-only context assay interrupted')
        if started[0] is not None and previous+time.monotonic()-started[0]>30:raise TimeoutError('Cumulative GPU30s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        batches=torch.load(c['references']['samples']['path'],map_location='cpu',weights_only=False)
        metadata=read_json(Path(c['references']['metadata']['path']));cached=read_json(Path(c['references']['cached_full_causal']['path']));outputs={}
        for entry,row in zip(batches,metadata['rows'],strict=True):input_check(entry,row)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();before_rng=rng_state()
            try:
                for arm,ref in c['checkpoints'].items():
                    heartbeat(arm+'-loading');state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True);initial_rng=rng_state()
                    controls_path=RUN/f'controls/{arm}.json'
                    if controls_path.exists():
                        control=read_json(controls_path)
                        if control['config_sha256']!=sha256(CONFIG) or control['checkpoint']!=ref or not control['allclose']:raise ValueError('Saved numeric native control differs')
                    else:
                        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):
                            x=batches[0]['x'][:8].to('cuda');y=batches[0]['y'][:8].to('cuda');routes=batches[0]['routes'][:8]
                            native=model(x,training_fast_path=True).logits;custom=context_logits(model,x,False)
                            delta=custom-native;matched=torch.allclose(native,custom,**c['control_tolerance'])
                            native_losses=all_groups(group_losses(native,y,routes));custom_losses=all_groups(group_losses(custom,y,routes))
                            control=dict(config_sha256=sha256(CONFIG),checkpoint=ref,allclose=matched,tolerance=c['control_tolerance'],
                                maximum_absolute_logit_difference=float(delta.abs().max()),RMS_logit_difference=float(delta.square().mean().sqrt()),
                                native_groups=native_losses,custom_full_causal_groups=custom_losses,
                                total_CE_difference=custom_losses['all']['CE_mean']-native_losses['all']['CE_mean'],
                                fixed_first8_input_sha256=hashlib.sha256(batches[0]['x'][:8].numpy().astype('<i8').tobytes()).hexdigest())
                            del native,custom,delta,x,y
                        atomic_json(controls_path,control)
                        if not matched:raise ValueError('Owned full-causal path did not match native; end assay without tolerance widening')
                    records=[]
                    for i,(entry,row) in enumerate(zip(batches,metadata['rows'],strict=True)):
                        heartbeat(arm+'-isolated-history',batch=i,completed_batches=len(records),total_batches=16)
                        point=RUN/f'points/{arm}/{i:02d}.json'
                        if point.exists():
                            record=read_json(point)
                            if record['config_sha256']!=sha256(CONFIG) or record['checkpoint']!=ref or record['input']!=row:raise ValueError('Saved isolated TRAIN point differs')
                        else:
                            groups={g:dict(teachers=0,nll_sum=0.) for g in GROUPS}
                            for offset in range(0,32,8):
                                check()
                                with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):
                                    x=entry['x'][offset:offset+8].to('cuda');y=entry['y'][offset:offset+8].to('cuda')
                                    logits=context_logits(model,x,True);part=group_losses(logits,y,entry['routes'][offset:offset+8])
                                    for g in GROUPS:
                                        groups[g]['teachers']+=part[g]['teachers'];groups[g]['nll_sum']+=part[g]['nll_sum']
                                    del logits,x,y
                            if {g:v['teachers'] for g,v in groups.items()}!=row['teachers_by_group']:raise ValueError('All original target groups must match')
                            old_groups=cached['models'][arm]['records'][i]['diagnostics']['groups']
                            full={g:dict(teachers=old_groups[g]['teachers'],nll_sum=old_groups[g]['CE_mean']*old_groups[g]['teachers'] if old_groups[g]['teachers'] else 0.) for g in GROUPS}
                            record=dict(index=i,config_sha256=sha256(CONFIG),checkpoint=ref,input=row,
                                isolated_groups=all_groups(groups),cached_full_causal_groups=all_groups(full),
                                cached_full_causal_result_sha256=c['references']['cached_full_causal']['sha256'])
                            atomic_json(point,record)
                        records.append(record)
                    checks=readonly_checks(model,state['model']);checks['RNG_unchanged_during_forwards']=equal_state(initial_rng,rng_state())
                    if not all(checks.values()):raise ValueError('Actual unchanged eval model invariant failed')
                    outputs[arm]=dict(checkpoint=ref,control=control,records=records,read_only_checks=checks,summary=summarize(records))
                    del model,state;gc.collect();torch.cuda.empty_cache()
            finally:restore_rng(before_rng)
            check();synchronize('cuda');elapsed=previous+time.monotonic()-started[0];restored=equal_state(before_rng,rng_state())
            if not restored or elapsed>30:raise ValueError('Bounded actual RNG-isolated context assay required')
            supported=outputs['completed_masked_mixed']['summary']['descriptive_conditional_history_dependence_marker']
            result=dict(status='fixed_document_context_ablation_complete',config_sha256=sha256(CONFIG),models=outputs,GPU_seconds=elapsed,RNG_restored=True,
                completed_endpoint_history_dependence_marker=supported,optimizer_updates=0,new_teacher_tokens=0,
                distinct_TRAIN_input_tokens=524288,logical_TRAIN_batches_per_model=16,cached_full_causal_reference=c['references']['cached_full_causal'],
                next_action='Define a paired Base attention-policy learning experiment with matched numerical conditions and unchanged quality gates.' if supported else 'End this packing hypothesis; no packing training variant. Determine a distinct Base mechanism from retained evidence.',
                limitations='Local16 correlated TRAIN batches/two fixed checkpoints; nativeBF16/math; changing only attention availability with unchanged absolute RoPE positions. '
                    'Cached full-history CE retained; only first8 native control per endpoint rerun. Context reliance does not establish natural generation improvement or model-capacity limit.',
                quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
            atomic_json(RUN/'result.json',result);job.update(status='complete',GPU_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true');a=p.parse_args()
    if a.prepare:prepare()
    elif a.inspect:inspect()
    else:run()
