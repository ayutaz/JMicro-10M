"""One bounded full-source capacity/throughput/actual full-state CUDA probe."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host, right_padded_hidden
from phase6_performance import identity, alive, finite_state

CONFIG = ROOT/'configs/phase6/natural_context_contrast_corpus_probe.json'
RUN = ROOT/'reports/phase6/natural-context-contrast-corpus-probe-20261007'
PREPARATION = ROOT/'reports/phase6/natural_context_contrast_corpus_preparation.json'
CAPACITY = ROOT/'reports/phase6/natural_context_contrast_capacity_preparation.json'
TESTS = ROOT/'reports/phase6/natural_context_contrast_corpus_tests.xml'
OLD_GATE = ROOT/'reports/phase6/natural_context_contrast_probe_completion.json'
SOURCES = ('scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/probe_natural_context_contrast_corpus.py','scripts/probe_natural_context_contrast_corpus.ps1',
    'tests/test_natural_context_contrast_corpus.py','src/jmicro/model.py','src/jmicro/training.py',
    'src/jmicro/phase5.py','src/jmicro/tokenizer.py','scripts/phase6_performance.py','uv.lock')


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def prepare():
    if CONFIG.exists():
        raise ValueError('Preserve frozen full-source probe')
    old = json.loads(OLD_GATE.read_text())
    if old['actual_CUDA_full_state_checks'] != 26 or old['scientific_teacher_tokens'] or alive(old['actual_identity']):
        raise ValueError('Completed actual fixed64 CUDA gate required')
    prep, capacity = json.loads(PREPARATION.read_text()), json.loads(CAPACITY.read_text())
    suites = list(ET.parse(TESTS).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 6 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Six actual source/window/accounting/resume CPU checks required')
    original = json.loads((ROOT/'configs/phase6/natural_context_contrast_probe.json').read_text())
    if (capacity['corpus_preparation']['sha256'] != sha256(PREPARATION)
            or prep['scientific_teacher_tokens'] or prep['optimizer_updates']):
        raise ValueError('Actual bounded source preparation required')
    c = dict(created_at=now(), source_preparation=ref(PREPARATION), capacity_preparation=ref(CAPACITY),
        payload=capacity['payload'], previous_actual_gate=ref(OLD_GATE), CPU_tests=ref(TESTS),
        parent=original['parent'], parent_size=original['parent_size'], parent_mtime_ns=original['parent_mtime_ns'],
        source_binding=prep['source_binding'], tokenizer_sha256=prep['tokenizer_sha256'],
        sources={s:sha256(ROOT/s) for s in SOURCES}, batch_candidates=[16,32,48,64,96,128],
        warmup_updates=3,timed_updates=5,GPU_limit_seconds=180,
        goals=dict(web=75000000,textbook=20000000,story=5000000),seed=42,
        capacity_policy='Before actual timings, stress full CE and two-branch hidden activation shapes at actual maximum original source context. Repeated original contexts are physical backward tests, not contrastive negatives/optimizer updates. Stop increasing batch after first OOM.',
        batch_policy='Highest minimum median real-source CE targets/sec across two arms among stable worst-shape batches; no quality-based selection',
        temperature=.1,coefficient=.1,scientific_teacher_tokens=0,Base_complete=False,
        Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='frozen_full_source_probe_GPU0',config_sha256=sha256(CONFIG))))


def inspect():
    c = json.loads(CONFIG.read_text())
    for name in ('source_preparation','capacity_preparation','payload','previous_actual_gate','CPU_tests'):
        if sha256(Path(c[name]['path'])) != c[name]['sha256']:
            raise ValueError('Frozen source reference differs: '+name)
    for name,value in c['sources'].items():
        if sha256(ROOT/name) != value:
            raise ValueError('Frozen source code differs: '+name)
    stat = Path(c['parent']['path']).stat()
    if (stat.st_size,stat.st_mtime_ns) != (c['parent_size'],c['parent_mtime_ns']):
        raise ValueError('Original parent differs after previous actual SHA check')
    return c


def worst_shape(trainer, window, batch):
    """Memory/finite backward only; no optimizer, false labels or quality claim."""
    torch.cuda.reset_peak_memory_stats()
    device = trainer.device
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION), torch.autocast('cuda',dtype=torch.bfloat16):
        trainer.optimizer.zero_grad(set_to_none=True)
        ids = torch.tensor([window['input_ids']]*(2*batch),device=device)
        hidden = right_padded_hidden(trainer.model,ids)
        feature_probe = hidden[:,-1].float().square().mean()
        feature_probe.backward()
        if not torch.isfinite(feature_probe) or any(not torch.isfinite(p.grad).all() for p in trainer.model.parameters() if p.grad is not None):
            raise ValueError('Nonfinite actual maximum-context hidden capacity backward')
        del hidden,ids,feature_probe
        trainer.optimizer.zero_grad(set_to_none=True)
        ids = torch.tensor([window['input_ids']]*batch,device=device)
        targets = torch.tensor([window['target_ids']]*batch,device=device)
        selected = targets != -100
        logits = trainer.model.lm_head(right_padded_hidden(trainer.model,ids)[selected]).float()
        ce = F.cross_entropy(logits,targets[selected])
        ce.backward()
        if not torch.isfinite(ce) or any(not torch.isfinite(p.grad).all() for p in trainer.model.parameters() if p.grad is not None):
            raise ValueError('Nonfinite maximum-context original-window CE backward')
    torch.cuda.synchronize()
    peak = torch.cuda.max_memory_allocated()
    trainer.optimizer.zero_grad(set_to_none=True)
    return dict(passed=True,peak_VRAM_bytes=peak,maximum_context=len(window['input_ids']),
        hidden_branch_sequences=2*batch,physical_backward_passes=2,optimizer_updates=0,
        negative_batch_claimed=False,scientific_teacher_tokens=0)


def run():
    c = inspect()
    if (RUN/'job.json').exists():
        raise ValueError('Inspect actual one-shot state; no completed/failed duplicate')
    if not torch.cuda.is_available():
        raise RuntimeError('Actual CUDA hardware required')
    RUN.mkdir(parents=True,exist_ok=True)
    job = dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='scripts/probe_natural_context_contrast_corpus.ps1 -Worker; inspect saved actual identity; never blindly restart completed/failed one-shot')
    atomic_json(RUN/'job.json',job)
    histories,timings,capacity,gates = {},{},{},{}
    started = None
    def check(*args):
        if args or (started is not None and time.monotonic()-started>180):
            raise TimeoutError('Full-source probe GPU180s exhausted')
    def beat(stage):
        check()
        job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        tokenizer = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        if sha256(tokenizer.path) != c['tokenizer_sha256']:
            raise ValueError('Original Tokenizer differs')
        window = json.loads(Path(c['payload']['path']).read_text())['window']
        binding = dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),
            weights_role='verification_only',sources=c['sources'])
        def build(batch,contrast):
            source = OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],tokenizer,c['goals'],42)
            if source.binding != c['source_binding']:
                raise ValueError('Actual whole-corpus source identity differs')
            t = NaturalCorpusTrainer(parent,source,binding,batch=batch,contrast=contrast)
            if sum(p.numel() for p in t.model.parameters()) != 10001152:
                raise ValueError('Native tied10M model required')
            return t
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target = RUN/'source'/name
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/name,target)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM,check)
            signal.alarm(180)
            job['status']='running'
            for batch in c['batch_candidates']:
                beat(f'worst-shape-batch{batch}')
                t = build(batch,False)
                try:
                    capacity[str(batch)] = worst_shape(t,window,batch)
                except torch.cuda.OutOfMemoryError as exc:
                    capacity[str(batch)] = dict(passed=False,error=str(exc),batch=batch)
                    break
                finally:
                    del t
                    gc.collect()
                    torch.cuda.empty_cache()
                for contrast in (False,True):
                    arm = 'contrast' if contrast else 'CE'
                    key = f'{arm}-batch{batch}'
                    beat(key)
                    t = build(batch,contrast)
                    history = []
                    histories[key] = history
                    torch.cuda.reset_peak_memory_stats()
                    try:
                        with (RUN/(key+'.jsonl')).open('x',buffering=1) as log:
                            for _ in range(8):
                                check()
                                row=t.step();history.append(row)
                                log.write(json.dumps(row,allow_nan=False)+'\n')
                                beat(key)
                        if not finite_state(host(t.state_dict())):
                            raise ValueError('Nonfinite actual source CUDA model/Adam')
                        timings[key]=dict(stable=True,batch=batch,arm=arm,history=history,
                            peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                            median_CE_targets_per_second=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:]))
                    except torch.cuda.OutOfMemoryError as exc:
                        timings[key]=dict(stable=False,batch=batch,arm=arm,history=history,error=str(exc))
                    finally:
                        del t;gc.collect();torch.cuda.empty_cache()
                atomic_json(RUN/'partial.json',dict(capacity=capacity,timings=timings))
            stable=[b for b in c['batch_candidates'] if all(timings.get(f'{a}-batch{b}',{}).get('stable',False) for a in ('CE','contrast'))]
            if not stable:
                raise ValueError('No stable maximum-context and actual-source batch')
            best=max(stable,key=lambda b:(min(timings[f'{a}-batch{b}']['median_CE_targets_per_second'] for a in ('CE','contrast')),b))
            for contrast in (False,True):
                arm='contrast' if contrast else 'CE'
                folder=RUN/arm/'resume-gate';folder.mkdir(parents=True,exist_ok=True)
                states,logs=[],[]
                for route in ('continuous','resumed'):
                    key=arm+'-'+route;beat(key);t=build(best,contrast);history=[];histories[key]=history
                    for i in range(4):
                        check();history.append(t.step())
                        if route=='resumed' and i==1:
                            t.save(folder/'split.pt');del t;gc.collect();torch.cuda.empty_cache()
                            t=build(best,contrast);t.load(folder/'split.pt')
                    t.save(folder/(route+'.pt'))
                    states.append(torch.load(folder/(route+'.pt'),map_location='cpu',weights_only=False))
                    logs.append(history);del t;gc.collect();torch.cuda.empty_cache()
                checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
                checks['finite']=all(finite_state(s) for s in states)
                checks['all_history_except_timing']=all(equal_state(
                    {k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                    {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
                gates[arm]=dict(passed=all(checks.values()),checks=checks,histories=logs,
                    checkpoints={r:ref(folder/(r+'.pt')) for r in ('continuous','resumed')})
                atomic_json(folder/'result.json',gates[arm])
                if not all(checks.values()):
                    raise ValueError('Actual source full CUDA state/history differs: '+repr(checks))
            check();elapsed=time.monotonic()-started
            result=dict(status='complete',passed=True,config_sha256=sha256(CONFIG),actual_identity=identity(),
                selected_measured_batch=best,maximum_stable_measured_batch=max(stable),capacity=capacity,timings=timings,gates=gates,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_CE_teacher_tokens=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                verification_auxiliary_input_tokens=sum(r['auxiliary_inputs_this_update'] for h in histories.values() for r in h),
                verification_physical_inputs=sum(r['physical_inputs_this_update'] for h in histories.values() for r in h),
                GPU_occupancy_seconds=elapsed,scientific_teacher_tokens=0,probe_weights_used_for_science=False,
                Base_complete=False,Chat_started=False,quantization_started=False,
                next_action='Implement/freeze persistent long-job runner and fixed evaluation; derive finite GPU budget from actual source timing before two100M CE arms. Common CE source trace/counters must match; auxiliary exposures and time remain separate. All Base gates unchanged.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='complete',batch=best,GPU_seconds=elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),GPU_occupancy_seconds=time.monotonic()-started if started else 0)
        atomic_json(RUN/'job.json',job)
        atomic_json(RUN/'failure-partial.json',dict(capacity=capacity,timings=timings,gates=gates,histories=histories))
        raise
    finally:
        signal.alarm(0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--prepare',action='store_true');g.add_argument('--inspect',action='store_true');a=p.parse_args()
    if a.prepare:prepare()
    elif a.inspect:inspect();print('Frozen real-source probe inspected; GPU0')
    else:run()
