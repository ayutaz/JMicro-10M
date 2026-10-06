"""Two fixed models, original TRAIN16 inputs, exact logical token-mean CE."""
import argparse
import copy
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
from jmicro.training import atomic_json,gpu_lock,rng_state,restore_rng,implementation_hashes,synchronize
from phase6_performance import alive,identity,finite_state
from run_eos_short_pilot import equal_state
from historical_parent_condition_trainer import historical_web_cursor
from interleaved_outcome_trainer import InterleavedOutcomeSampler
from source_gradient_attribution import GROUPS,target_groups,gradients,describe,readonly_checks
import run_interleaved_outcome_order as prior

PROPOSAL=ROOT/'reports/phase6/source_gradient_attribution_proposal.json'
CONFIG=ROOT/'configs/phase6/source_gradient_attribution.json'
RUN=ROOT/'reports/phase6/source-gradient-attribution-20261006'
SAMPLES=RUN/'samples.pt'
TESTS=ROOT/'reports/phase6/source_gradient_attribution_tests.xml'
SOURCES=('scripts/source_gradient_attribution.py','scripts/diagnose_source_gradient_attribution.py',
    'scripts/diagnose_source_gradient_attribution.ps1','tests/test_source_gradient_attribution.py')
reference,check_reference=prior.reference,prior.check_reference
TOLERANCE=.02


def terminal_previous():
    job=read_json(prior.RUN/'job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Previous actual science must be terminal')


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();p=read_json(PROPOSAL);terminal_previous()
    if (p['CPU_preparation_ceiling_seconds']!=30 or p['total_new_GPU_ceiling_seconds']!=90
            or p['groups']!=list(GROUPS) or p['teacher_tokens_learned'] or p['optimizer_updates'] or p['protected_test_used']):
        raise ValueError('Frozen no-learning TRAIN attribution proposal required')
    for ref in (p['trigger'],*p['fixed_checkpoints'].values()):check_reference(ref)
    suites=list(ET.parse(TESTS).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Three passing actual attribution CPU tests required')
    old=prior.inspect(prior.CONFIG);pool,web,positive=prior.data(old)
    parent=torch.load(p['fixed_checkpoints']['original_fullparent']['path'],map_location='cpu',weights_only=False)
    if not finite_state(parent) or parent['update']!=320435:raise ValueError('Fixed finite original parent required')
    sampler=InterleavedOutcomeSampler(pool,web,positive,historical_web_cursor(parent),old['teacher_goals'],1024,42)
    sampler.reference_token_digest=parent['token_digest'];masked_digest=parent['token_digest'];batches=[];rows=[]
    ledger=read_json(prior.LEDGER)
    history=[json.loads(s) for s in (prior.RUN/prior.ARM/'training/metrics.jsonl').read_text().splitlines()]
    for i in range(16):
        x,y,body_bytes,focus=sampler.batch(32);routes=list(sampler.last_genres);masks=target_groups(y,routes)
        conditional=torch.tensor([g=='conditional_textbook' for g in routes])[:,None]
        if x.eq(0).any() or (conditional&y.ge(8)&~focus).any():raise ValueError('Same unpadded outcome/EOS targets required')
        digest=hashlib.sha256(bytes.fromhex(masked_digest));digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
        masked_digest=digest.hexdigest();entry=ledger['rows'][i]
        if (parent['update']+i+1!=entry['update'] or entry['reference_token_digest']!=sampler.reference_token_digest
                or routes!=entry['actual_source_routes'] or int(y.ne(-100).sum())!=entry['actual_teachers']
                or body_bytes!=entry['actual_body_bytes'] or history[i]['token_digest']!=masked_digest):
            raise ValueError('Full first16 original mixed input/reference/masked teacher history must match')
        rows.append(dict(index=i,update=entry['update'],input_sha256=hashlib.sha256(x.numpy().astype('<i8').tobytes()).hexdigest(),
            target_sha256=hashlib.sha256(y.numpy().astype('<i8').tobytes()).hexdigest(),actual_source_routes=routes,
            reference_token_digest=sampler.reference_token_digest,masked_token_digest=masked_digest,
            teachers=int(y.ne(-100).sum()),teachers_by_group={g:int(m.sum()) for g,m in masks.items()},body_bytes=body_bytes))
        batches.append(dict(x=x,y=y,routes=routes))
    RUN.mkdir(parents=True,exist_ok=True)
    if SAMPLES.exists():raise ValueError('Preserve partially prepared actual TRAIN input; no reroll')
    torch.save(batches,SAMPLES);atomic_json(RUN/'samples.json',dict(split='train',seed=42,logical_batch=32,microbatch=8,context=1024,
        consecutive_batches=16,rows=rows,matched_existing_training_all16=True,cache_reused=pool.index.cache_reused))
    elapsed=time.monotonic()-started
    if elapsed>30:raise TimeoutError('CPU30s exhausted')
    c=dict(checkpoints=p['fixed_checkpoints'],proposal=reference(PROPOSAL),references=dict(trigger=p['trigger'],old_config=reference(prior.CONFIG),
        source_ledger=reference(prior.LEDGER),samples=reference(SAMPLES),samples_metadata=reference(RUN/'samples.json'),CPU_tests=reference(TESTS)),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},original_sources=old['source_sha256'],implementation=implementation_hashes(),
        logical_batch=32,microbatch=8,context=1024,batches=16,dtype='bf16',backend='math',training_fast_path=True,
        numerical_decomposition_relative_L2_tolerance=TOLERANCE,
        numerical_protocol='Same independent sequences; four fixed8-sequence microbatches sum FP32 parameter gradients, each divided by all actual teachers in its logical32 batch. '
            'Group sum versus independent original CE must have relative L2 error<=.02 on every model/batch before descriptive interpretation. '
            'This preregistered nativeBF16 numerical bound is not a quality criterion. No optimizer/clip/weights/ratio/EOS coefficient changes.',
        CPU_preparation_seconds=elapsed,GPU_ceiling_seconds=90,optimizer_updates=0,new_teacher_tokens=0,
        quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,created_at=now())
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='fixed_TRAIN_gradient_diagnostic_prepared',CPU_seconds=elapsed)),flush=True)


def inspect():
    c=read_json(CONFIG);p=read_json(PROPOSAL);terminal_previous()
    if (c['checkpoints']!=p['fixed_checkpoints'] or c['source_sha256']!={s:sha256(ROOT/s) for s in SOURCES}
            or c['implementation']!=implementation_hashes() or c['original_sources']!={s:sha256(ROOT/s) for s in c['original_sources']}
            or (c['logical_batch'],c['microbatch'],c['context'],c['batches'],c['GPU_ceiling_seconds'])!=(32,8,1024,16,90)
            or (c['dtype'],c['backend'])!=('bf16','math') or not c['training_fast_path']
            or c['numerical_decomposition_relative_L2_tolerance']!=TOLERANCE or c['optimizer_updates'] or c['new_teacher_tokens']
            or c['protected_test_used'] or c['Base_complete'] or c['Chat_started'] or c['quantization_started']):
        raise ValueError('Fixed bounded read-only input/source/model protocol differs')
    for ref in (c['proposal'],*c['references'].values(),*c['checkpoints'].values()):check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual diagnostic live; no duplicate')
    return c


def run():
    c=inspect();jp=RUN/'job.json';old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(CONFIG):raise ValueError('Saved diagnostic binding differs')
    if old.get('status')=='complete':print('Actual completed diagnostic retained');return
    previous=old.get('GPU_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),GPU_seconds=previous,started_at=now(),
        restart_command='scripts/diagnose_source_gradient_attribution.ps1 -Worker',optimizer_updates=0,new_teacher_tokens=0)
    atomic_json(jp,job)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Read-only attribution interrupted')
        if started[0] is not None and previous+time.monotonic()-started[0]>90:raise TimeoutError('Cumulative GPU90s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        batches=torch.load(SAMPLES,map_location='cpu',weights_only=False);metadata=read_json(RUN/'samples.json');outputs={}
        if len(batches)!=16:raise ValueError('All16 fixed actual logical TRAIN batches required')
        with gpu_lock('cuda'):
            started[0]=time.monotonic();before_rng=rng_state()
            try:
                for arm,ref in c['checkpoints'].items():
                    heartbeat(arm+'-loading');state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                    parameters=list(model.parameters());records=[];initial_rng=rng_state()
                    for i,entry in enumerate(batches):
                        heartbeat(arm+'-gradient',batch=i,completed_batches=len(records),total_batches=16)
                        point=RUN/f'points/{arm}/{i:02d}.json';row=metadata['rows'][i]
                        if point.exists():
                            record=read_json(point)
                            if record['config_sha256']!=sha256(CONFIG) or record['checkpoint']!=ref or record['input']!=row:raise ValueError('Saved matched TRAIN point differs')
                        else:
                            x,y,routes=entry['x'],entry['y'],entry['routes'];denominator=int(y.ne(-100).sum())
                            if (hashlib.sha256(x.numpy().astype('<i8').tobytes()).hexdigest()!=row['input_sha256']
                                    or hashlib.sha256(y.numpy().astype('<i8').tobytes()).hexdigest()!=row['target_sha256'] or routes!=row['actual_source_routes']):
                                raise ValueError('Actual fixed logical inputs changed')
                            vectors=None;counts=dict.fromkeys(GROUPS,0);nll=dict.fromkeys(GROUPS,0.)
                            for offset in range(0,32,8):
                                check();a,b=x[offset:offset+8].to('cuda'),y[offset:offset+8].to('cuda');masks=target_groups(b,routes[offset:offset+8])
                                with sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):
                                    logits=model(a,training_fast_path=True).logits
                                    part,pc,pn=gradients(logits,b,masks,parameters,denominator)
                                if vectors is None:vectors=part
                                else:
                                    for k,v in part.items():vectors[k]+=v
                                for g in GROUPS:counts[g]+=pc[g];nll[g]+=pn[g]
                                del logits,part,a,b,masks
                            if counts!=row['teachers_by_group']:raise ValueError('Actual teacher grouping differs')
                            diagnostics=describe(vectors,counts,nll,TOLERANCE);del vectors
                            record=dict(config_sha256=sha256(CONFIG),checkpoint=ref,input=row,diagnostics=diagnostics)
                            atomic_json(point,record)
                        records.append(record)
                    checks=readonly_checks(model,state['model']);checks['RNG_unchanged_during_gradients']=equal_state(initial_rng,rng_state())
                    if not all(checks.values()):raise ValueError('Actual read-only learned model invariant failed')
                    outputs[arm]=dict(checkpoint=ref,records=records,read_only_checks=checks)
                    del model,state,parameters;gc.collect();torch.cuda.empty_cache()
            finally:restore_rng(before_rng)
            restored=equal_state(before_rng,rng_state());check();synchronize('cuda');elapsed=previous+time.monotonic()-started[0]
            if not restored or elapsed>90:raise ValueError('Finite bounded RNG-isolated diagnostic required')
            result=dict(status='fixed_TRAIN_gradient_attribution_complete',config_sha256=sha256(CONFIG),models=outputs,GPU_seconds=elapsed,
                RNG_restored=True,logical_TRAIN_batches_per_model=16,distinct_logical_input_tokens=16*32*1024,
                gradient_teacher_targets_per_model=sum(row['teachers'] for row in metadata['rows']),new_teacher_tokens=0,optimizer_updates=0,
                limitations='Local unchanged token-mean CE at16 fixed TRAIN batches/two preselected endpoints/one learned seed; BF16/math eager8-sequence chunks. '
                    'Not optimizer directions, GPU learning, model quality, causal dilution proof or an automatic reweighting recommendation.',
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
