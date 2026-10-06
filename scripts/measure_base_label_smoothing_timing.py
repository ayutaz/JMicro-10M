"""One fixed32-step timing extension; pool all previous5 and new32 samples."""
import argparse
import json
import math
import os
from pathlib import Path
import signal
import statistics
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,sha256,now
from jmicro.training import atomic_json,gpu_lock
from jmicro.tokenizer import Tokenizer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from base_label_smoothing_trainer import LabelSmoothingTrainer
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive,finite_state
import probe_base_label_smoothing as probe

CONFIG=ROOT/'configs/phase6/base_label_smoothing_timing.json'
RUN=ROOT/'reports/phase6/base-label-smoothing-timing-20261007'


def read(p):return json.loads(Path(p).read_text())
def ref(p):return dict(path=str(p),sha256=sha256(p))


def prepare():
    if CONFIG.exists() or (RUN/'job.json').exists():raise ValueError('Preserve this one fixed timing extension')
    p=read(probe.CONFIG);r=read(probe.RUN/'result.json');job=read(probe.RUN/'job.json')
    if job['status']!='complete' or alive(job) or not r['passed'] or not all(r['resume_checks'].values()):
        raise ValueError('Actual completed CUDA gate required before timing-only extension')
    values=r['timings']['48']['samples']
    if len(values)!=5 or any(not 0<v<math.inf for v in values):raise ValueError('Preserve all original five measurements')
    proposal=read(Path(p['proposal']['path']))
    initial=100000000/statistics.median(values)*1.3+900
    if initial<=proposal['science_absolute_ceiling_seconds']:raise ValueError('Extra timing is unnecessary when original budget fits')
    c=dict(created_at=now(),probe_config=ref(probe.CONFIG),probe_result=ref(probe.RUN/'result.json'),
        probe_checkpoint=r['resume_checkpoints']['continuous'],steps=32,batch=48,
        original_samples=values,initial_budget_estimate=initial,pooled_samples=37,
        GPU_limit_seconds=math.floor(180-r['GPU_occupancy_seconds']),
        total_probe_GPU_ceiling_seconds=180,science_GPU_ceiling_seconds=3965,
        sources={str(Path(s).relative_to(ROOT)):sha256(Path(s)) for s in
            (Path(__file__),ROOT/'scripts/measure_base_label_smoothing_timing.ps1')},
        purpose='Initial5 timings span1.72x and pessimistic estimate exceeds cap. Measure exactly32 subsequent native updates from completed4-update probe state, pool all37 values without exclusions. No repeated initialization/resume/stress checks, parameter/loss/source/batch change or favorable endpoint selection.',
        completion='All32 steps and source/accounting finite, all37 timing observations retained. If pooled measured budget still exceeds3965, do not start science or extend this timing protocol again.',
        scientific_teacher_tokens=0,probe_weights_discarded=True,Base_complete=False,Chat_started=False,quantization_started=False)
    if c['GPU_limit_seconds']<=0:raise ValueError('Original total probe budget exhausted')
    atomic_json(CONFIG,c);print(json.dumps(dict(status='fixed32_timing_contract_saved',initial_budget=initial)))


def inspect():
    c=read(CONFIG)
    for key in ('probe_config','probe_result','probe_checkpoint'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Original timing gate changed')
    for s,digest in c['sources'].items():
        if sha256(ROOT/s)!=digest:raise ValueError('Fixed timing command changed')
    if (RUN/'job.json').exists():raise ValueError('Preserve attempted timing identity/partial observations')
    if alive(read(probe.RUN/'job.json')):raise ValueError('Original actual CUDA probe still alive')
    return c


def run():
    c=inspect();p=read(Path(c['probe_config']['path']));r=read(Path(c['probe_result']['path']))
    if not torch.cuda.is_available():raise RuntimeError('Actual CUDA required')
    RUN.mkdir(parents=True,exist_ok=True);job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG))
    atomic_json(RUN/'job.json',job);started=None;history=[]
    def check(*args):
        if args or started is not None and time.monotonic()-started>c['GPU_limit_seconds']:raise TimeoutError('Original remaining probe budget exhausted')
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            configure_resident_memory(r['capacity']['48']['peak_VRAM_bytes'])
            parent=torch.load(p['parent']['path'],map_location='cpu',weights_only=False)
            codec=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
            sampler=OriginalTrainCorpusSampler(p['source_binding']['pool'],p['source_binding']['manifest_sha256'],codec,p['goals'],42)
            if sampler.binding!=p['source_binding']:raise ValueError('Original source identity changed')
            binding=dict(parent=p['parent'],source_binding=p['source_binding'],config_sha256=sha256(Path(c['probe_config']['path'])),weights_role='verification_only',sources=p['sources'])
            t=LabelSmoothingTrainer(parent,sampler,binding,batch=48);t.load(c['probe_checkpoint']['path'])
            start_count=t.counters['supervised_tokens'];start_update=t.counters['update']
            job['status']='running';atomic_json(RUN/'job.json',job)
            with (RUN/'metrics.jsonl').open('x',buffering=1) as stream:
                for index in range(c['steps']):
                    check();row=t.step();history.append(row);stream.write(json.dumps(row,allow_nan=False)+'\n')
                    job.update(completed_steps=index+1,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
                    atomic_json(RUN/'job.json',job)
            if t.counters['update']!=start_update+32 or not finite_state(t.state_dict()):raise ValueError('All32 finite native updates required')
            new_samples=[row['CE_targets_this_update']/row['seconds'] for row in history]
            all_samples=c['original_samples']+new_samples
            if len(all_samples)!=37 or any(not 0<v<math.inf for v in all_samples):raise ValueError('All37 positive timing samples required')
            median=statistics.median(all_samples);budget=math.ceil(100000000/median*1.3+900)
            check();elapsed=time.monotonic()-started
            result=dict(status='complete',created_at=now(),config_sha256=sha256(CONFIG),actual_identity=identity(),
                original_samples=c['original_samples'],new32_samples=new_samples,all37_samples=all_samples,
                pooled_median_gold_positions_per_second=median,science_budget_seconds=budget,
                science_budget_fits=budget<=3965,initial_budget_estimate=c['initial_budget_estimate'],
                verification_updates=32,verification_CE_teacher_tokens=t.counters['supervised_tokens']-start_count,
                GPU_occupancy_seconds=elapsed,total_probe_GPU_seconds=r['GPU_occupancy_seconds']+elapsed,
                original_CUDA_resume_gate_unchanged=True,probe_weights_discarded=True,
                scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False)
            if result['total_probe_GPU_seconds']>180:raise TimeoutError('Original total180s probe limit exceeded')
            atomic_json(RUN/'result.json',result);job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job);print(json.dumps(dict(status='timing_complete',median=median,budget=budget,fits=budget<=3965)))
    except BaseException as error:
        job.update(status='failed',error=repr(error),ended_at=now(),GPU_occupancy_seconds=0 if started is None else time.monotonic()-started)
        atomic_json(RUN/'job.json',job);raise
    finally:signal.alarm(0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();mode=parser.add_mutually_exclusive_group();mode.add_argument('--prepare',action='store_true');mode.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Fixed timing-only preflight passed; GPU0')
    else:run()
