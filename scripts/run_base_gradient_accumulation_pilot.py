"""Durable fresh94.16M same-stream accumulation4 learning pilot, Base only."""
import argparse
import gc
import json
import os
from pathlib import Path
import signal
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,gpu_lock,rng_state
from jmicro.phase5 import equal_state
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_memory import bound_evaluation_cache
from base_gradient_accumulation_trainer import GroupedTrainer
from base_parallel_residual_model import model_from_config
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from run_base_parallel_residual import build_trainer
from run_base_residual_seen_train import wait_ui
from run_eos_short_pilot import greedy80

PHASE=ROOT/'reports/phase6'
CONFIG=ROOT/'configs/phase6/base_gradient_accumulation_pilot.json'
RUN=PHASE/'base-gradient-accumulation-pilot-20261008'
BASE_CONFIG=ROOT/'configs/phase6/base_parallel_residual_comparison.json'
LOCAL_SOURCES=('scripts/run_base_gradient_accumulation_pilot.py','scripts/run_base_gradient_accumulation_pilot.ps1',
    'scripts/base_gradient_accumulation_trainer.py','tests/test_base_gradient_accumulation.py')


def ref(path): return dict(path=str(path),sha256=sha256(path))


def checked(value):
    path=Path(value['path'])
    if sha256(path)!=value['sha256']: raise ValueError('Frozen reference differs: '+str(path))
    return read_json(path)


def freeze():
    if CONFIG.exists(): raise ValueError('Preserve frozen grouping comparison')
    audit_path=PHASE/'base_learning_decision_table_20261008.json';audit=read_json(audit_path)
    proposal=PHASE/'base_gradient_accumulation_pilot_proposal.json'
    tests=PHASE/'base_gradient_accumulation_tests.xml'
    suites=ET.parse(tests).getroot().findall('.//testsuite')
    if (sum(int(s.attrib['tests']) for s in suites)!=3
            or any(int(s.attrib.get('failures',0))+int(s.attrib.get('errors',0))+int(s.attrib.get('skipped',0)) for s in suites)):
        raise ValueError('All three actual CPU gradient/parity/resume tests required')
    if not audit['measured_budget_eligible'] or audit['actual_control_counters']['supervised_tokens']!=94160195:
        raise ValueError('Actual same-teacher checkpoint and measured budget required')
    base=read_json(BASE_CONFIG)
    if sha256(Path(audit['actual_control_checkpoint']['path']))!=audit['actual_control_checkpoint']['sha256']:
        raise ValueError('Actual fixed10000-update baseline changed')
    sources=dict(base['source_sha256'])
    sources.update({name:sha256(ROOT/name) for name in LOCAL_SOURCES})
    atomic_json(CONFIG,dict(created_at=now(),proposal=ref(proposal),audit=ref(audit_path),CPU_tests=ref(tests),
        base_config=ref(BASE_CONFIG),baseline=audit['actual_control_checkpoint'],source_sha256=sources,
        source_binding=base['source_binding'],accumulation=4,microbatches=10000,optimizer_updates=2500,
        scientific_teacher_tokens=94160195,GPU_cap_seconds=audit['proposed_pilot_GPU_cap_seconds'],
        expected_worst_peak_bytes=base['worst_measured_peak_bytes'],evaluation='fixed256DEV_and_fixed80greedy64',
        Base_complete=False,Chat_started=False,quantization_started=False,protected_test_scored=False))
    print(json.dumps(dict(status='grouping_pilot_frozen_not_started',GPU_cap_seconds=1992)))


def inspect(require_ui=False):
    c=read_json(CONFIG)
    if (RUN/'result.json').exists(): raise ValueError('Preserve completed pilot; no rerun')
    if (RUN/'job.json').exists():
        job=read_json(RUN/'job.json')
        if alive(job) or not job['cumulative_GPU_ledger_closed'] or job['config_sha256']!=sha256(CONFIG):
            raise ValueError('Live/unclosed/different previous grouping process')
        if job['GPU_seconds']>=c['GPU_cap_seconds']: raise ValueError('Cumulative pilot budget exhausted')
    for name in ('proposal','audit','CPU_tests','base_config'):
        value=c[name]
        if sha256(Path(value['path']))!=value['sha256']: raise ValueError('Frozen reference differs: '+name)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen source differs: '+name)
    base=checked(c['base_config'])
    for path,digest in ((ROOT/base['tokenizer'],base['tokenizer_sha256']),
            (ROOT/'eval/base.jsonl',base['suite_sha256']),
            (Path(base['dev_shards'])/'manifest.json',base['dev_manifest_sha256'])):
        if sha256(path)!=digest: raise ValueError('Frozen tokenizer/DEV differs')
    for folder in Path('/proc').iterdir():
        if not folder.name.isdecimal() or int(folder.name)==os.getpid(): continue
        try:
            cmd=(folder/'cmdline').read_bytes().split(b'\0')
            if 'python' in Path(cmd[0].decode()).name and any(arg.startswith((b'scripts/run_',b'scripts/probe_')) for arg in cmd[1:]):
                raise ValueError('Actual experiment process exists: '+folder.name)
        except (FileNotFoundError,ProcessLookupError,PermissionError): pass
    if require_ui:
        ui=read_json(ROOT/'reports/local/webui/server.json')
        with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response: model=json.load(response)
        if not alive(ui) or model['busy'] or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
            raise ValueError('Actual idle original10B UI required before planned stop')
    return c,base


def make(c,base,codec,role):
    binding=dict(config_sha256=sha256(CONFIG),source_binding=c['source_binding'],weights_role=role)
    return GroupedTrainer(build_trainer(base,codec,binding,'sequential'),4)


def gate(c,base,codec,check):
    path=RUN/'resume-gate.json'
    if path.exists():
        result=read_json(path)
        if result['config_sha256']!=sha256(CONFIG) or not all(result['checks'].values()): raise ValueError('Existing gate differs or failed')
        return result
    torch.cuda.reset_peak_memory_stats()
    a=make(c,base,codec,'verification_only');first=[]
    for _ in range(4): check();first.append(a.step())
    expected=host(a.state_dict());verification_teachers=expected['counters']['supervised_tokens']
    del a;gc.collect();torch.cuda.empty_cache()
    b=make(c,base,codec,'verification_only');second=[]
    for _ in range(2): check();second.append(b.step())
    b.save(RUN/'resume-gate.pt')
    del b;gc.collect();torch.cuda.empty_cache()
    d=make(c,base,codec,'verification_only');d.load(RUN/'resume-gate.pt')
    for _ in range(2): check();second.append(d.step())
    actual=host(d.state_dict());del d
    checks={k:equal_state(expected[k],actual[k]) for k in expected}
    strip=lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
    checks['full_committed_history']=equal_state([strip(r) for r in first],[strip(r) for r in second])
    peak=torch.cuda.max_memory_allocated()
    checks['resident_peak_under90percent']=peak<.9*torch.cuda.get_device_properties(0).total_memory
    result=dict(config_sha256=sha256(CONFIG),checks=checks,actual_CUDA_updates=8,
        verification_microbatches=32,verification_teacher_tokens=verification_teachers*2,
        peak_VRAM_bytes=peak,probe_weights_used_for_science=False)
    atomic_json(path,result)
    if not all(checks.values()): raise ValueError('Own actual grouped CUDA/full-state gate failed')
    gc.collect();torch.cuda.empty_cache()
    return result


def evaluate(name,state_path,base,codec,beat,check):
    terminal=RUN/(name+'-evaluation.json')
    binding=dict(config_sha256=sha256(CONFIG),checkpoint=ref(state_path),suite_sha256=base['suite_sha256'])
    if terminal.exists():
        old=read_json(terminal)
        if old['binding']!=binding: raise ValueError('Saved evaluation binding differs')
        return old
    state=torch.load(state_path,map_location='cpu',weights_only=False)
    model=model_from_config(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
    bound_evaluation_cache(model)
    before=host(rng_state());check();beat(name+'-dev256')
    with sdpa_kernel(SDPBackend.MATH):
        body=evaluate_batched(model,Shard(Path(base['dev_shards']),'dev'),'cuda','bf16',limit=256,batch=16,
            progress=lambda done,total:(check(),beat(name+'-dev256',completed_cases=done,total_cases=total)))
        outputs=greedy80(model,codec,beat,check)
    if not equal_state(before,host(rng_state())): raise ValueError('Evaluation altered training RNG')
    result=dict(status='complete_raw_content_review_pending',binding=binding,body=body,outputs=outputs,
        same_native_model_class=True,RNG_unchanged=True,Base_complete=False)
    atomic_json(terminal,result)
    del model,state;gc.collect();torch.cuda.empty_cache();return result


def run():
    c,base=inspect();RUN.mkdir(parents=True,exist_ok=True)
    previous=read_json(RUN/'job.json') if (RUN/'job.json').exists() else {}
    prior=previous.get('GPU_seconds',0);started=None;trainer=None;stopped=False
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),GPU_seconds=prior,
        cumulative_GPU_ledger_closed=False,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='scripts/run_base_gradient_accumulation_pilot.ps1 -Worker; inspect actual identity, closed ledger and committed grouped checkpoint first')
    atomic_json(RUN/'job.json',job)
    def stop(*_):
        nonlocal stopped
        stopped=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def check():
        if stopped: raise InterruptedError('Stop requested; retain completed grouped checkpoint')
        if started is not None and prior+time.monotonic()-started>=c['GPU_cap_seconds']: raise TimeoutError('Frozen cumulative1992-second pilot cap exhausted')
    def beat(stage,**values):
        check();job.update(status='running',stage=stage,heartbeat_at=now(),**values)
        job['GPU_seconds']=prior+time.monotonic()-started
        atomic_json(RUN/'job.json',job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        codec=Tokenizer(ROOT/base['tokenizer'])
        with gpu_lock('cuda'):
            started=time.monotonic();job['memory_policy']=configure_resident_memory(c['expected_worst_peak_bytes'])
            own_gate=gate(c,base,codec,check)
            beat('fresh-learning')
            trainer=make(c,base,codec,'scientific_fresh_grouped_pilot')
            latest=RUN/'latest.pt'
            if latest.exists(): trainer.load(latest)
            logpath=RUN/f"metrics-{job['pid']}-{job['start_ticks']}.jsonl"
            with logpath.open('x',buffering=1) as log:
                while trainer.microbatches<c['microbatches']:
                    check();row=trainer.step();log.write(json.dumps(row)+'\n')
                    if row['update']%20==0:
                        beat('fresh-learning',optimizer_updates=row['update'],microbatches=trainer.microbatches,
                            scientific_teacher_tokens=row['supervised_tokens'],CE_loss=row['CE_loss'])
                    if row['update']%100==0: trainer.save(latest)
            trainer.save(latest);state=host(trainer.state_dict())
            if sha256(Path(c['baseline']['path']))!=c['baseline']['sha256']: raise ValueError('Actual baseline changed')
            baseline=torch.load(c['baseline']['path'],map_location='cpu',weights_only=False)
            keys=('supervised_tokens','CE_input_tokens','physical_input_tokens','original_body_bytes','token_digest','source_teachers','source_EOS')
            checks={key:equal_state(state['counters'][key],baseline['counters'][key]) for key in keys}
            checks['sampler']=equal_state(state['sampler'],baseline['sampler'])
            checks['scheduler_teacher_position']=equal_state(state['scheduler'],baseline['scheduler'])
            checks['exact_microbatches']=trainer.microbatches==10000
            checks['exact_optimizer_updates']=state['counters']['update']==2500
            if not all(checks.values()): raise ValueError('Same exact baseline original stream/counters required')
            del trainer;trainer=None;gc.collect();torch.cuda.empty_cache()
            control=evaluate('control',Path(c['baseline']['path']),base,codec,beat,check)
            candidate=evaluate('candidate',latest,base,codec,beat,check)
            check();elapsed=prior+time.monotonic()-started
            result=dict(status='learning_and_raw_evaluation_complete_content_review_pending',created_at=now(),
                config=ref(CONFIG),identity=identity(),resume_gate=own_gate,stream_checks=checks,
                candidate_checkpoint=ref(latest),baseline=c['baseline'],counters=state['counters'],
                scientific_teacher_tokens=94160195,reused_control_teacher_tokens=94160195,
                control_evaluation=ref(RUN/'control-evaluation.json'),candidate_evaluation=ref(RUN/'candidate-evaluation.json'),
                GPU_seconds=elapsed,GPU_cap_seconds=c['GPU_cap_seconds'],cumulative_GPU_ledger_closed=True,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_seconds=elapsed,cumulative_GPU_ledger_closed=True)
            atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status=result['status'],GPU_seconds=elapsed,Base_complete=False)),flush=True)
    except BaseException as error:
        if trainer is not None and not trainer.in_progress:
            trainer.save(RUN/'latest.pt')
        if started is not None: torch.cuda.synchronize()
        job.update(status='failed_or_interrupted',error=repr(error),ended_at=now(),
            GPU_seconds=prior if started is None else prior+time.monotonic()-started,cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true');group.add_argument('--inspect',action='store_true')
    group.add_argument('--wait-ui',action='store_true')
    args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect(require_ui=True);print('Frozen pilot and actual idle UI passed preflight')
    elif args.wait_ui: wait_ui()
    else: run()
