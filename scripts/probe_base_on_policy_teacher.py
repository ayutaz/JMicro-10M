"""Finite actual CUDA state, worst-shape and scheduled on-policy cost gate."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import statistics
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json,gpu_lock
from jmicro.tokenizer import Tokenizer
from base_on_policy_teacher_trainer import OnPolicyTeacherTrainer,committed_state,RECIPE
from base_native_teacher_KD_trainer import predictive_KL,finite_KD_state
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host,right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive

CONFIG=ROOT/'configs/phase6/base_on_policy_teacher_probe.json'
RUN=ROOT/'reports/phase6/base-on-policy-teacher-probe-20261007'
PROPOSAL=ROOT/'reports/phase6/base_on_policy_teacher_proposal_v2.json'
SOURCES=('scripts/base_on_policy_teacher_trainer.py','scripts/probe_base_on_policy_teacher.py',
    'scripts/probe_base_on_policy_teacher.ps1','tests/test_base_on_policy_teacher.py','tests/test_base_on_policy_teacher_probe.py',
    'scripts/base_native_teacher_KD_trainer.py','scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock')
REF_KEYS=('proposal','CPU_tests','CPU_protocol_tests','payload','fixed_TRAIN24','control_CE','control_result')


def ref(p):return dict(path=str(p),sha256=sha256(p))


def forecast(history):
    if len(history)!=32 or sum(bool(r['rollout_records']) for r in history)!=2:
        raise ValueError('Exactly32 real timings spanning two scheduled rollouts required')
    times=[r['seconds'] for r in history]
    if not all(math.isfinite(t) and t>0 for t in times):raise ValueError('Finite real step times required')
    return math.ceil(17698/32*sum(times)*1.3+900)


def prepare():
    if CONFIG.exists() or RUN.exists():raise ValueError('Keep one-shot on-policy CUDA gate')
    c=read_json(ROOT/'configs/phase6/base_native_teacher_KD_probe_v2.json')
    p=read_json(PROPOSAL)
    for name,value in p['references'].items():
        if sha256(Path(value['path']))!=value['sha256']:raise ValueError('Historical evidence changed: '+name)
    suites=ET.parse(ROOT/'reports/phase6/base_on_policy_teacher_tests.xml').getroot()
    if sum(int(s.get('tests',0)) for s in suites.iter('testsuite'))!=20 or any(int(s.get(k,0)) for s in suites.iter('testsuite') for k in ('failures','errors','skipped')):
        raise ValueError('Actual20 related CPU checks required')
    protocol=ET.parse(ROOT/'reports/phase6/base_on_policy_teacher_probe_tests.xml').getroot()
    if sum(int(s.get('tests',0)) for s in protocol.iter('testsuite'))!=4 or any(int(s.get(k,0)) for s in protocol.iter('testsuite') for k in ('failures','errors','skipped')):
        raise ValueError('Actual4 timing/budget protocol checks required')
    keep=('parent','parent_size','parent_mtime_ns','teacher','teacher_size','teacher_mtime_ns','source_binding','goals',
        'tokenizer','tokenizer_sha256','dev_shards','dev_manifest_sha256','suite_sha256','evaluation','payload','control_CE','control_result')
    c={k:c[k] for k in keep}
    c.update(created_at=now(),proposal=ref(PROPOSAL),CPU_tests=ref(ROOT/'reports/phase6/base_on_policy_teacher_tests.xml'),
        CPU_protocol_tests=ref(ROOT/'reports/phase6/base_on_policy_teacher_probe_tests.xml'),
        fixed_TRAIN24=ref(ROOT/'reports/phase6/base_gradient_precision_payload.json'),recipe=RECIPE,
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},batch=48,seed=42,probe_GPU_cap_seconds=180,
        total_GPU_cap_seconds=7200,warmup_updates=3,timed_updates=32,continuous_updates=32,saved_split_updates=16,
        scientific_teacher_positions=0,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,c);print(json.dumps(dict(status='on_policy_CUDA_gate_frozen_GPU0',sha256=sha256(CONFIG))))


def inspect():
    c=read_json(CONFIG)
    for key in REF_KEYS:
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen ref differs: '+key)
    for p,digest in c['source_sha256'].items():
        if sha256(ROOT/p)!=digest:raise ValueError('Frozen source differs: '+p)
    for name in ('parent','teacher'):
        st=Path(c[name]['path']).stat()
        if (st.st_size,st.st_mtime_ns)!=(c[name+'_size'],c[name+'_mtime_ns']):raise ValueError('Pinned checkpoint differs: '+name)
    if c['recipe']!=RECIPE or c['total_GPU_cap_seconds']!=7200:raise ValueError('One fixed recipe/budget required')
    if RUN.exists():raise ValueError('Inspect actual previous identity/result; no duplicate/retry')
    return c


def run():
    c=inspect();RUN.mkdir();job=dict(status='running',stage='initializing',**identity(),created_at=now(),config_sha256=sha256(CONFIG),scientific_teacher_positions=0)
    atomic_json(RUN/'job.json',job);start=None;histories={};initial={};checks={}
    def clear():gc.collect();torch.cuda.empty_cache()
    def elapsed():return time.monotonic()-start if start is not None else 0.
    def check():
        if elapsed()>180:raise TimeoutError('Prospective on-policy probe180s exhausted')
    def beat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=elapsed());atomic_json(RUN/'job.json',job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        teacher=torch.load(c['teacher']['path'],map_location='cpu',weights_only=False)
        tokenizer=Tokenizer(ROOT/c['tokenizer']);binding=dict(parent=c['parent'],config_sha256=sha256(CONFIG),weights_role='verification_only')
        def build(on_policy=True):
            sampler=OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],tokenizer,c['goals'],42)
            if sampler.binding!=c['source_binding']:raise ValueError('Cached original accepted source changed')
            if not on_policy:return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False)
            return OnPolicyTeacherTrainer(parent,sampler,binding,teacher,c['teacher'],batch=48)
        with gpu_lock('cuda'):
            start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('On-policy hard wall cap180s')))
            signal.setitimer(signal.ITIMER_REAL,180);memory=configure_resident_memory(11987593728)
            t=build();initial.update(parent_weights=equal_state(parent['model'],host(t.model.state_dict())),
                teacher_weights=equal_state(teacher['model'],host(t.teacher.state_dict())),
                frozen_teacher=not t.teacher.training and all(not p.requires_grad for p in t.teacher.parameters()),
                native_tied_vocab=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                teacher_tied_vocab=t.teacher.lm_head.weight is t.teacher.model.embed_tokens.weight,
                native_parameters=sum(p.numel() for p in t.model.parameters())==10001152,
                student_only_optimizer={id(p) for g in t.optimizer.param_groups for p in g['params']}=={id(p) for p in t.model.parameters()})
            beat('worst_gold48x1024_plus_aux8x49')
            window=read_json(Path(c['payload']['path']))['window']
            ids=torch.tensor([window['input_ids']]*48,device='cuda');targets=torch.tensor([window['target_ids']]*48,device='cuda');mask=targets.ne(-100)
            if ids.shape!=(48,1024) or int(mask[0].sum())!=512:raise ValueError('Frozen originalTRAIN1024/512 required')
            t.optimizer.zero_grad(set_to_none=True);torch.cuda.reset_peak_memory_stats()
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                logits=t.model.lm_head(right_padded_hidden(t.model,ids)[mask]).float();ce=F.cross_entropy(logits,targets[mask]);ce.backward()
                rows=[r for r in read_json(Path(c['fixed_TRAIN24']['path']))['rows'] if r['source']=='textbook']
                if len(rows)!=8 or any(len(r['input_ids'])<50 for r in rows):raise ValueError('Fixed original shortTRAIN8 capacity refs required')
                short=torch.tensor([r['input_ids'][:49] for r in rows],device='cuda')
                smask=torch.zeros_like(short,dtype=torch.bool);smask[:,-32:]=True
                observed=torch.tensor([r['input_ids'][18:50] for r in rows],device='cuda').flatten()
                with torch.no_grad():q=t.teacher.lm_head(right_padded_hidden(t.teacher,short)[smask]).float()
                p=t.model.lm_head(right_padded_hidden(t.model,short)[smask]).float()
                kl,_=predictive_KL(p,q,observed,256);kl.backward()
            gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True);torch.cuda.synchronize()
            capacity=dict(main_shape=list(ids.shape),auxiliary_shape=list(short.shape),diagnostic_gold_positions=int(mask.sum()),
                diagnostic_auxiliary_positions=256,CE_loss=float(ce.detach()),teacher_feedback_KL=float(kl.detach()),gradient_norm=float(gradient),
                peak_VRAM_bytes=torch.cuda.max_memory_allocated(),optimizer_updates=0,scientific_teachers=0,
                scope='Original fixed TRAIN worst gold window plus original shortTRAIN8 hypothetical prefix score upper bound.8x49 exceeds actual max8x48 scoring by one position; not current-student rollout science.')
            atomic_json(RUN/'capacity.json',capacity)
            if not finite_KD_state(capacity) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:raise ValueError('Finite resident worst-shape backward required')
            initial['teacher_unchanged_stress']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
            del t,ids,targets,mask,logits,ce,short,smask,observed,q,p,kl;clear();beat('continuous32_vs_saved16plus16');states=[];logs=[]
            for route in ('continuous','resumed'):
                t=build();history=[];histories[route]=history
                for i in range(32):
                    check();history.append(t.step());atomic_json(RUN/'partial_histories.json',histories)
                    if route=='resumed' and i==15:
                        t.save(RUN/'split.pt');del t;clear();t=build();t.load(RUN/'split.pt')
                initial['teacher_unchanged_'+route]=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
                t.save(RUN/(route+'.pt'));states.append(host(t.state_dict()));logs.append(history);del t;clear()
            checks.update({k:equal_state(states[0][k],states[1][k]) for k in states[0]})
            checks['committed_all_state']=all(committed_state(s) for s in states)
            checks['history_except_timing']=all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
            checks['actual_two_rollout_batches']=states[0]['on_policy_teacher']['rollout_batches']==2 and states[0]['on_policy_teacher']['distribution_positions']>0
            beat('original_gold_control32');control=build(False);ch=[];histories['control']=ch
            for _ in range(32):check();ch.append(control.step())
            keys=(*control.counters,'draw_trace','lr')
            checks['same_original_gold_stream']=all(equal_state(a[k],b[k]) for a,b in zip(logs[0],ch,strict=True) for k in keys)
            checks['full_original_sampler']=equal_state(states[0]['sampler'],control.sampler.state_dict())
            checks['short_only_teacher']=states[0]['on_policy_teacher']['source_positions']['web']==0
            del control;clear();atomic_json(RUN/'resume_checks.json',checks)
            if not all(initial.values()) or not all(checks.values()):raise ValueError('Actual on-policy CUDA/fullstate/source gate failed')
            beat('warmup3_plus_timing32');t=build();history=[];histories['timing']=history
            for _ in range(35):check();history.append(t.step());atomic_json(RUN/'partial_histories.json',histories)
            initial['teacher_unchanged_timings']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
            if not all(initial.values()):raise ValueError('Teacher immutable through all actual work required')
            del t;clear();check();budget=forecast(history[3:]);duration=elapsed()
            result=dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                initial_checks=initial,all_resume_and_source_checks=checks,capacity=capacity,memory_policy=memory,histories=histories,
                median_original_teachers_per_second=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:]),
                postwarmup_total32_step_seconds=sum(r['seconds'] for r in history[3:]),
                rollout_step_seconds=[r['seconds'] for r in history[3:] if r['rollout_records']],
                ordinary_step_seconds=[r['seconds'] for r in history[3:] if not r['rollout_records']],
                science_budget_seconds=budget,science_budget_eligible=duration+budget<=7200,total_GPU_cap_seconds=7200,GPU_occupancy_seconds=duration,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                verification_distribution_positions=sum(r.get('distribution_positions_this_update',0) for h in histories.values() for r in h),
                scientific_teacher_positions=0,probe_weights_used_for_science=False,Base_complete=False,Chat_started=False,quantization_started=False)
            atomic_json(RUN/'result.json',result);signal.alarm(0);job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=duration)
            atomic_json(RUN/'job.json',job);print(json.dumps(dict(status='on_policy_CUDA_gate_complete',GPU_seconds=duration,science_seconds=budget,eligible=result['science_budget_eligible'])))
    except BaseException as error:
        signal.alarm(0);job.update(status='failed',ended_at=now(),error=repr(error),GPU_occupancy_seconds=elapsed())
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'partial_histories.json',histories);atomic_json(RUN/'initial_checks.json',initial);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group();group.add_argument('--prepare',action='store_true');group.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Frozen on-policy native teacher preflight passed;GPU0')
    else:run()
