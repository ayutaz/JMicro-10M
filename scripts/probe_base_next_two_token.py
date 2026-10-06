"""Native CUDA next-two state/source/batch measurement; no scientific weights."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,now,sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,rng_state
from base_next_two_token_trainer import NextTwoTokenTrainer,next_two_targets,COEFFICIENT
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host,right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive,finite_state

CONFIG=ROOT/'configs/phase6/base_next_two_token_probe.json'
RUN=ROOT/'reports/phase6/base-next-two-token-probe-20261007'
SOURCES=('scripts/base_next_two_token_trainer.py','scripts/probe_base_next_two_token.py',
    'scripts/probe_base_next_two_token.ps1','tests/test_base_next_two_token_trainer.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/phase6_performance.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock')


def read(path):return json.loads(Path(path).read_text())
def ref(path):return dict(path=str(path),sha256=sha256(path))


def prepare():
    if CONFIG.exists() or (RUN/'job.json').exists():raise ValueError('Preserve one measured future-head probe')
    proposal=ROOT/'reports/phase6/base_next_two_token_proposal.json';p=read(proposal)
    for path,row in p['source_references'].items():
        if sha256(Path(row['path']))!=row['sha256']:raise ValueError('Fixed CPU-verified source differs: '+path)
    c=dict(created_at=now(),proposal=ref(proposal),CPU_tests=p['CPU_tests'],previous_completion=p['previous_attention_completion'],
        sources={s:sha256(ROOT/s) for s in SOURCES},parent=p['parent'],parent_size=p['parent_size'],
        parent_mtime_ns=p['parent_mtime_ns'],source_binding=p['source_binding'],goals=p['goals'],payload=p['payload'],
        tokenizer_sha256=p['tokenizer_sha256'],batch=48,seed=42,coefficient=COEFFICIENT,
        native_parameters=10001152,train_only_parameters=688896,GPU_limit_seconds=180,
        warmup_updates=3,timed_updates=32,maximum_scientific_GPU_seconds=3965,
        scientific_teacher_positions=0,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,c);print(json.dumps(dict(status='native_next_two_probe_frozen_GPU0',config_sha256=sha256(CONFIG))))


def inspect():
    c=read(CONFIG)
    for key in ('proposal','CPU_tests','previous_completion','payload'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen reference differs: '+key)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen source differs: '+path)
    stat=Path(c['parent']['path']).stat()
    if (stat.st_size,stat.st_mtime_ns)!=(c['parent_size'],c['parent_mtime_ns']):raise ValueError('Actual audited native parent identity differs')
    if alive(read(c['previous_completion']['path'])['actual_identity']):raise ValueError('Previous native assay still alive')
    if (RUN/'job.json').exists():raise ValueError('Inspect actual one-shot PID/results before any next action')
    return c


def worst_shape(t,window,batch):
    t.optimizer.zero_grad(set_to_none=True);torch.cuda.reset_peak_memory_stats()
    ids=torch.tensor([window['input_ids']]*batch,device='cuda')
    targets=torch.tensor([window['target_ids']]*batch,device='cuda');future=next_two_targets(targets)
    if ids.shape[1]!=1024 or int(targets[0].ne(-100).sum())!=512:raise ValueError('Actual maximum original window required')
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
        h=right_padded_hidden(t.model,ids);m=targets.ne(-100);m2=future.ne(-100)
        ce=F.cross_entropy(t.model.lm_head(h[m]).float(),targets[m])
        h2=t.future_head(h);ce2=F.cross_entropy(t.model.lm_head(h2[m2]).float(),future[m2])
        loss=ce+COEFFICIENT*ce2;loss.backward()
    norm=torch.nn.utils.clip_grad_norm_(t.all_parameters,1.,error_if_nonfinite=True)
    torch.cuda.synchronize()
    if not torch.isfinite(loss) or not 0<float(norm)<float('inf'):raise ValueError('Actual maximum-shape native/aux loss and gradient must be finite')
    row=dict(passed=True,context=1024,original_targets=int(m.sum()),next_two_targets=int(m2.sum()),
        peak_VRAM_bytes=torch.cuda.max_memory_allocated(),combined_loss=float(loss.detach()),gradient_norm=float(norm),optimizer_updates=0)
    t.optimizer.zero_grad(set_to_none=True);return row


def run():
    c=inspect()
    if not torch.cuda.is_available():raise RuntimeError('Actual native WSL CUDA required')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teacher_positions=0,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='One-shot future-head probe: inspect actual PID and terminal/partial records; no blind rerun.')
    atomic_json(RUN/'job.json',job)
    started=None;initial={};histories={};capacity={};checks={}
    def check(*args):
        if args or started is not None and time.monotonic()-started>c['GPU_limit_seconds']:
            raise TimeoutError('Fixed future-head GPU180s exhausted')
    def clear():gc.collect();torch.cuda.empty_cache()
    def beat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started);atomic_json(RUN/'job.json',job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        codec=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        if sha256(codec.path)!=c['tokenizer_sha256']:raise ValueError('Actual pinned tokenizer differs')
        binding=dict(parent=c['parent'],probe=ref(CONFIG),weights_role='verification_only')
        def build(aux=True):
            s=OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],codec,c['goals'])
            if s.binding!=c['source_binding']:raise ValueError('Actual original accepted source differs')
            cls=NextTwoTokenTrainer if aux else NaturalCorpusTrainer
            return cls(parent,s,binding,batch=48,contrast=False)
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            dest=RUN/'source'/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,dest)
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            memory=configure_resident_memory(0);job['status']='running';beat('native-inference-RNG-initialization')
            t=build(False);t.model.eval();ids=torch.tensor([[2,8,9,10]],device='cuda')
            with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):expected=t.model(ids).logits.detach().clone()
            expected_rng=host(rng_state());del t;clear()
            t=build();t.model.eval()
            with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):actual=t.model(ids).logits
            initial=dict(native_logits=torch.equal(expected,actual),native_weights=equal_state(parent['model'],host(t.model.state_dict())),
                native_RNG=equal_state(expected_rng,host(rng_state())),native_parameters=t.spec['native_parameters']==10001152,
                train_only_parameters=t.spec['train_only_parameters']==688896,
                native_tied=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                auxiliary_not_native_module=all(module is not t.future_head for module in t.model.modules()))
            if not all(initial.values()):raise ValueError('Actual native initialization/inference/RNG differs: '+repr(initial))
            del t,ids,expected,actual;clear()
            beat('native-source-capacity-and-all32-timings');t=build();history=[];histories['timing']=history
            check();history.append(t.step())
            capacity=worst_shape(t,read(c['payload']['path'])['window'],48)
            for _ in range(c['warmup_updates']):check();history.append(t.step())
            timed=[]
            for _ in range(c['timed_updates']):
                check();row=t.step();history.append(row);timed.append(row['CE_targets_this_update']/row['seconds'])
            speed=statistics.median(timed);del t;clear()
            gate=RUN/'resume-gate';gate.mkdir(exist_ok=True);states=[];logs=[]
            for route in ('continuous','resumed'):
                beat(route);t=build();history=[];histories[route]=history
                for index in range(4):
                    check();history.append(t.step())
                    if route=='resumed' and index==1:
                        t.save(gate/'split.pt');del t;clear();t=build();t.load(gate/'split.pt')
                t.save(gate/(route+'.pt'));states.append(torch.load(gate/(route+'.pt'),map_location='cpu',weights_only=False));logs.append(history)
                del t;clear()
            checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
            checks['finite_native_optimizer']=all(finite_state(s) for s in states)
            checks['finite_auxiliary_model']=all(torch.isfinite(p).all().item() for s in states for p in s['auxiliary_model'].values())
            checks['all_history_except_timing']=all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
            checks['auxiliary_accounting']=all(s['counters']['next_two_teacher_positions']==sum(s['counters']['source_next_two_teachers'].values())
                and s['counters']['next_two_target_mass']==.1*s['counters']['next_two_teacher_positions'] for s in states)
            beat('original-control-stream-only-no-quality-evaluation');control=build(False);control_history=[];histories['control_verification']=control_history
            for _ in range(4):check();control_history.append(control.step())
            keys=('source_teachers','source_EOS','supervised_tokens','CE_input_tokens','physical_input_tokens','original_body_bytes','token_digest','draw_trace','lr')
            checks['original_control_stream']=all(equal_state(a[k],b[k]) for a,b in zip(logs[0],control_history,strict=True) for k in keys)
            checks['full_original_control_sampler']=equal_state(states[0]['sampler'],control.sampler.state_dict())
            del control;clear()
            if not all(checks.values()):raise ValueError('Native future-head full-state/stream CUDA verification differs: '+repr(checks))
            check();elapsed=time.monotonic()-started;cap=math.ceil(100000000/speed*1.3+900)
            result=dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                initial_checks=initial,memory_policy=memory,capacity=capacity,all_resume_and_source_checks=checks,
                median_original_teachers_per_second=speed,all32_timing_speeds=timed,selected_matched_batch=48,
                science_cap_seconds=cap,maximum_scientific_GPU_seconds=3965,science_budget_eligible=cap<=3965,
                GPU_occupancy_seconds=elapsed,GPU_limit_seconds=180,histories=histories,
                resume_checkpoints={route:ref(gate/(route+'.pt')) for route in ('continuous','resumed')},
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                verification_next_two_positions=sum(r.get('next_two_targets_this_update',0) for h in histories.values() for r in h),
                scientific_teacher_positions=0,probe_weights_used_for_science=False,Base_complete=False,
                Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
                next_action='If budget passes, implement/freeze persistent same-parent next-two100M runner/evaluator/reviewer and full80 content. Otherwise close fixed objective/probe without horizon/coefficient/teacher/cap rescue.')
            atomic_json(RUN/'result.json',result);job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed);atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='native_next_two_probe_complete',GPU_seconds=elapsed,original_teachers_per_second=speed,science_cap_seconds=cap,science_budget_eligible=cap<=3965)))
    except BaseException as exc:
        signal.alarm(0);job.update(status='failed',ended_at=now(),error=repr(exc),GPU_occupancy_seconds=0 if started is None else time.monotonic()-started)
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'failure-partial.json',dict(initial=initial,capacity=capacity,checks=checks,histories=histories));raise
    finally:signal.alarm(0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--prepare',action='store_true');g.add_argument('--inspect',action='store_true')
    args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Fixed native next-two probe inspected; GPU0')
    else:run()
