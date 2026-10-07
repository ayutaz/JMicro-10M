"""Bounded real native predictive-KD CUDA/state/capacity/speed gate."""
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
from base_native_teacher_KD_trainer import NativeTeacherKDTrainer,predictive_KL,finite_KD_state
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host,right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive

PROPOSAL=ROOT/'reports/phase6/base_native_teacher_KD_proposal.json'
CONFIG=ROOT/'configs/phase6/base_native_teacher_KD_probe_v2.json'
RUN=ROOT/'reports/phase6/base-native-teacher-KD-probe-v2-20261007'
PREVIOUS=ROOT/'reports/phase6/base-native-teacher-KD-probe-20261007'
SOURCES=('scripts/base_native_teacher_KD_trainer.py','scripts/probe_base_native_teacher_KD_v2.py',
    'scripts/probe_base_native_teacher_KD_v2.ps1','tests/test_base_native_teacher_KD.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/phase6_performance.py','src/jmicro/model.py',
    'src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock')


def ref(p): return dict(path=str(p),sha256=sha256(p))


def prepare():
    if CONFIG.exists() or RUN.exists(): raise ValueError('Preserve one-shot predictive-KD gate')
    previous_config=ROOT/'configs/phase6/base_native_teacher_KD_probe.json'
    c=read_json(previous_config);job=read_json(PREVIOUS/'job.json');histories=read_json(PREVIOUS/'partial_histories.json')
    if (alive(job) or job['status']!='failed' or job['stage']!='worst_shape_48x1024' or
        job['config_sha256']!=sha256(previous_config) or 'AttributeError' not in job['error'] or len(histories.get('timing',[]))!=35):
        raise ValueError('Exact ended Path-read wrapper failure after35 actual updates required')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Original failed source changed')
    c.update(created_at=now(),previous_config=ref(previous_config),previous_job=ref(PREVIOUS/'job.json'),
        previous_timings=ref(PREVIOUS/'partial_histories.json'),prior_probe_GPU_seconds=job['GPU_occupancy_seconds'],
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        correction='Only cast existing JSON payload string to Path. Reuse frozen35 actual timing updates, do not repeat them; complete remaining capacity/resume/control checks under cumulative original180s/3600s caps. Preserve original failed config/script/job/history. Original timing teacher-equality bool was not persisted; independent remaining gates verify immutable teacher, do not fabricate the missing bool.')
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='native_predictive_KD_protocol_frozen_GPU0',config_sha256=sha256(CONFIG))))


def inspect():
    c=read_json(CONFIG)
    for key in ('proposal','CPU_tests','payload','control_CE','control_result','previous_config','previous_job','previous_timings'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']: raise ValueError('Frozen reference differs: '+key)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen source differs: '+name)
    for name in ('parent','teacher'):
        st=Path(c[name]['path']).stat()
        if (st.st_size,st.st_mtime_ns)!=(c[name+'_size'],c[name+'_mtime_ns']): raise ValueError('Pinned actual checkpoint identity changed: '+name)
    if RUN.exists(): raise ValueError('Inspect existing probe identity/results; no duplicate/retry')
    return c


def run():
    c=inspect();RUN.mkdir()
    job=dict(status='running',stage='initializing',**identity(),created_at=now(),config_sha256=sha256(CONFIG),scientific_teacher_positions=0)
    atomic_json(RUN/'job.json',job);start=None;histories={}
    def clear(): gc.collect();torch.cuda.empty_cache()
    def check():
        if start is not None and c['prior_probe_GPU_seconds']+time.monotonic()-start>180: raise TimeoutError('Predeclared cumulative native-KD probe180s exhausted')
    def beat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=c['prior_probe_GPU_seconds']+time.monotonic()-start);atomic_json(RUN/'job.json',job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        memory=configure_resident_memory(11987593728)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        teacher=torch.load(c['teacher']['path'],map_location='cpu',weights_only=False)
        tokenizer=Tokenizer(ROOT/c['tokenizer']);binding=dict(parent=c['parent'],config_sha256=sha256(CONFIG),weights_role='verification_only')
        def build(kd=True):
            sampler=OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],tokenizer,c['goals'],42)
            if sampler.binding!=c['source_binding']: raise ValueError('Cached accepted source changed')
            if not kd: return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False)
            return NativeTeacherKDTrainer(parent,sampler,binding,teacher,c['teacher'],batch=48)
        with gpu_lock('cuda'):
            start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('Native KD cumulative hard cap180s')));signal.setitimer(signal.ITIMER_REAL,180-c['prior_probe_GPU_seconds'])
            t=build()
            initial=dict(native_parent_weights=equal_state(parent['model'],host(t.model.state_dict())),
                frozen_teacher_weights=equal_state(teacher['model'],host(t.teacher.state_dict())),
                teacher_eval_no_grad=not t.teacher.training and all(not p.requires_grad for p in t.teacher.parameters()),
                native_tied_vocab=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                teacher_native_tied_vocab=t.teacher.lm_head.weight is t.teacher.model.embed_tokens.weight,
                parameters=sum(p.numel() for p in t.model.parameters())==10001152,
                teacher_parameters=sum(p.numel() for p in t.teacher.parameters())==10001152,
                student_optimizer_only={id(p) for g in t.optimizer.param_groups for p in g['params']}=={id(p) for p in t.model.parameters()})
            history=read_json(Path(c['previous_timings']['path']))['timing'];histories['timing']=history
            speed=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:])
            del t;clear();beat('worst_shape_48x1024')
            t=build();payload=read_json(Path(c['payload']['path']));window=payload['window']
            ids=torch.tensor([window['input_ids']]*48,device='cuda');targets=torch.tensor([window['target_ids']]*48,device='cuda')
            selected=targets.ne(-100)
            if ids.shape!=(48,1024) or int(selected[0].sum())!=512: raise ValueError('Existing exact1024/512 stress window required')
            t.optimizer.zero_grad(set_to_none=True);torch.cuda.reset_peak_memory_stats()
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                with torch.no_grad(): q=t.teacher.lm_head(right_padded_hidden(t.teacher,ids)[selected]).float()
                p=t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float()
                ce=F.cross_entropy(p,targets[selected]);kl,_=predictive_KL(p,q,targets[selected],int(selected.sum()));loss=ce+kl;loss.backward()
            gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True);torch.cuda.synchronize()
            capacity=dict(batch=48,context=1024,target_stride=512,diagnostic_positions=int(selected.sum()),
                peak_VRAM_bytes=torch.cuda.max_memory_allocated(),CE_loss=float(ce.detach()),KD_loss=float(kl.detach()),gradient_norm=float(gradient),
                optimizer_updates=0,scientific_teachers=0,
                scope='Artificial all-KD upper-bound shape on the existing originalTRAIN1024 stress window, not relabeled short-source training or new science.')
            initial['teacher_unchanged_after_stress']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
            if not torch.isfinite(loss) or not 0<float(gradient)<float('inf') or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite resident worst-shape native CE/KD backward required')
            del t,p,q,ids,targets,selected,loss,ce,kl;clear();states=[];logs=[];beat('continuous_vs2plus2')
            for route in ('continuous','resumed'):
                t=build();history=[];histories[route]=history
                for index in range(4):
                    check();history.append(t.step())
                    if route=='resumed' and index==1:
                        t.save(RUN/'split.pt');del t;clear();t=build();t.load(RUN/'split.pt')
                initial['teacher_unchanged_'+route]=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
                t.save(RUN/(route+'.pt'));states.append(host(t.state_dict()));logs.append(history);del t;clear()
            checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
            checks['finite_all_state']=all(finite_KD_state(s) for s in states)
            checks['history_except_timing']=all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
            control=build(False);ch=[];histories['control']=ch;beat('original_gold_control')
            for _ in range(4):check();ch.append(control.step())
            keys=('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens','original_body_bytes','token_digest','draw_trace','lr')
            checks['same_original_gold_stream']=all(equal_state(a[k],b[k]) for a,b in zip(logs[0],ch,strict=True) for k in keys)
            checks['full_original_sampler']=equal_state(states[0]['sampler'],control.sampler.state_dict())
            kd=states[0]['native_teacher_KD'];checks['short_only_teacher_positions']=kd['teacher_positions']==sum(states[0]['counters']['source_teachers'][g] for g in ('textbook','story'))>0
            del control;clear();check()
            if not all(initial.values()) or not all(checks.values()):raise ValueError('Actual native predictive-KD CUDA/fullstate gate failed')
            elapsed=c['prior_probe_GPU_seconds']+time.monotonic()-start;forecast=math.ceil(100000000/speed*1.3+900)
            result=dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                initial_checks=initial,all_resume_and_source_checks=checks,memory_policy=memory,capacity=capacity,
                histories=histories,all32_timing_speeds=[r['CE_targets_this_update']/r['seconds'] for r in histories['timing'][3:]],
                median_original_teachers_per_second=speed,science_budget_seconds=forecast,science_budget_eligible=elapsed+forecast<=3600,
                total_GPU_cap_seconds=3600,GPU_occupancy_seconds=elapsed,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                verification_KD_positions=sum(r.get('KD_targets_this_update',0) for h in histories.values() for r in h),
                native_teacher_KD_state=kd,scientific_teacher_positions=0,probe_weights_used_for_science=False,
                original_timing_result=c['previous_timings'],prior_probe_GPU_seconds=c['prior_probe_GPU_seconds'],
                additional_probe_GPU_seconds=elapsed-c['prior_probe_GPU_seconds'],
                timing_teacher_equality_bool_missing_from_initial_failure=True,
                Base_complete=False,Chat_started=False,quantization_started=False)
            atomic_json(RUN/'result.json',result);job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job);signal.alarm(0)
            print(json.dumps(dict(status='Native_teacher_KD_CUDA_gate_complete',speed=speed,GPU_seconds=elapsed,science_budget_seconds=forecast,eligible=result['science_budget_eligible'])))
    except BaseException as error:
        signal.alarm(0);job.update(status='failed',ended_at=now(),error=repr(error),GPU_occupancy_seconds=c['prior_probe_GPU_seconds']+time.monotonic()-start if start else c['prior_probe_GPU_seconds'])
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'partial_histories.json',histories);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group();group.add_argument('--prepare',action='store_true');group.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Frozen native predictive-KD CUDA gate preflight passed;GPU0')
    else:run()
