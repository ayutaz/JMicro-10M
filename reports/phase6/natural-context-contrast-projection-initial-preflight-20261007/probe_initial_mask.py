"""One bounded, resident CUDA projection/source/resume probe; uv only."""
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
from jmicro.training import atomic_json, gpu_lock, rng_state
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_projection import ProjectedCorpusTrainer, gradient_norm
from natural_context_contrast_trainer import host, right_pad, right_padded_hidden, symmetric_InfoNCE, COEFFICIENT
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity, alive, finite_state

CONFIG = ROOT/'configs/phase6/natural_context_contrast_projection_probe.json'
RUN = ROOT/'reports/phase6/natural-context-contrast-projection-probe-20261007'
TESTS = ROOT/'reports/phase6/natural_context_contrast_projection_tests.xml'
SOURCES = ('scripts/natural_context_contrast_projection.py',
    'scripts/probe_natural_context_contrast_projection.py', 'scripts/probe_natural_context_contrast_projection.ps1',
    'tests/test_natural_context_contrast_projection.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','src/jmicro/model.py','src/jmicro/training.py',
    'src/jmicro/phase5.py','src/jmicro/tokenizer.py','uv.lock')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def prepare():
    if CONFIG.exists():
        raise ValueError('Preserve one-shot frozen projection probe')
    old = json.loads((ROOT/'configs/phase6/natural_context_contrast_corpus_probe.json').read_text())
    sample = json.loads((ROOT/'configs/phase6/natural_context_contrast_probe.json').read_text())
    gate = ROOT/'reports/phase6/natural_context_contrast_comparison_completion.json'
    closed = json.loads(gate.read_text())
    suites = list(ET.parse(TESTS).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 7 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Seven successful projection protocol CPU tests required')
    old_job = json.loads((ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/job.json').read_text())
    if old_job['status'] != 'complete' or alive(old_job):
        raise ValueError('Previous scientific job must actually be finished')
    c = dict(created_at=now(), sources={s:sha256(ROOT/s) for s in SOURCES},
        proposal=ref(ROOT/'reports/phase6/natural_context_contrast_projection_proposal.json'),
        CPU_tests=ref(TESTS), prior_completed_comparison=ref(gate),
        parent=old['parent'], parent_size=old['parent_size'],parent_mtime_ns=old['parent_mtime_ns'],
        payload=old['payload'], sample=sample['sample'], source_binding=old['source_binding'],
        tokenizer_sha256=old['tokenizer_sha256'], goals=old['goals'],seed=42,
        GPU_limit_seconds=180,batch_candidates=[16,32,48,64],warmup_updates=3,timed_updates=5,
        matched_scientific_batch=48, resident_allocator_fraction=.90,
        head_seed=2026100751, native_parameters=10001152,train_only_parameters=98304,
        capacity_policy='Actual maximum-context auxiliary/head and CE backward with initialized optimizer under resident90percent allocator; optimizer0 in stress. Stop increasing batch after first OOM.',
        batch_policy='Measure fastest resident batch separately. A cached-control comparison requires identical batch48/source/digest; no silent batch change or rerun of completed controls.',
        prototype_policy='Use all original fixed TRAIN64 once solely for finite shared/head backward. Full-source four versus two-save-resume-two checks all state/history. All probe weights discarded.',
        scientific_teacher_tokens=0, Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='projection_probe_frozen_GPU0',config_sha256=sha256(CONFIG))))


def inspect():
    c = json.loads(CONFIG.read_text())
    for key in ('proposal','CPU_tests','prior_completed_comparison','payload','sample'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Frozen reference differs: '+key)
    for name,digest in c['sources'].items():
        if sha256(ROOT/name) != digest:
            raise ValueError('Frozen source differs: '+name)
    stat = Path(c['parent']['path']).stat()
    if (stat.st_size,stat.st_mtime_ns) != (c['parent_size'],c['parent_mtime_ns']):
        raise ValueError('Previously hash-verified parent identity differs')
    if (RUN/'job.json').exists():
        raise ValueError('Inspect one-shot job; never duplicate or blindly retry completed/failed probe')
    return c


def worst_shape(t,window,batch):
    torch.cuda.reset_peak_memory_stats()
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
        t.optimizer.zero_grad(set_to_none=True)
        ids = torch.tensor([window['input_ids']]*(2*batch),device=t.device)
        h = right_padded_hidden(t.model,ids)
        projected = t.projector(h[:,-1])
        loss = projected.float().square().mean()
        loss.backward()
        norms = dict(native=gradient_norm(t.model),head=gradient_norm(t.projector))
        if not all(0 < n < float('inf') for n in norms.values()):
            raise ValueError('Maximum-shape native/head backward must be finite and nonzero')
        del h,ids,projected,loss
        t.optimizer.zero_grad(set_to_none=True)
        ids = torch.tensor([window['input_ids']]*batch,device=t.device)
        targets = torch.tensor([window['target_ids']]*batch,device=t.device)
        selected = targets != -100
        logits = t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float()
        ce = F.cross_entropy(logits,targets[selected]);ce.backward()
        if not torch.isfinite(ce) or any(not torch.isfinite(p.grad).all() for p in t.parameters if p.grad is not None):
            raise ValueError('Nonfinite maximum-context CE backward')
    torch.cuda.synchronize()
    peak = torch.cuda.max_memory_allocated()
    t.optimizer.zero_grad(set_to_none=True)
    return dict(passed=True,peak_VRAM_bytes=peak,maximum_context=len(window['input_ids']),
        auxiliary_gradient_norms=norms,optimizer_updates=0,physical_backward_passes=2,
        negative_batch_claimed=False,scientific_teacher_tokens=0)


def run():
    c=inspect()
    if not torch.cuda.is_available():raise RuntimeError('Actual CUDA required')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='scripts/probe_natural_context_contrast_projection.ps1 -Worker; inspect actual identity first; do not retry a completed or failed one-shot')
    atomic_json(RUN/'job.json',job)
    histories,capacities,timings,initial,fixed = {},{},{},{},[]
    started=None
    def check(*args):
        if args or (started is not None and time.monotonic()-started>c['GPU_limit_seconds']):
            raise TimeoutError('Projection probe GPU180s exhausted')
    def beat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def clear():gc.collect();torch.cuda.empty_cache()
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        codec=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        if sha256(codec.path)!=c['tokenizer_sha256']:raise ValueError('Tokenizer differs')
        binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),
            weights_role='verification_only',sources=c['sources'])
        def build(batch,projected=True):
            sampler=OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],codec,c['goals'],42)
            if sampler.binding!=c['source_binding']:raise ValueError('Original corpus identity differs')
            cls=ProjectedCorpusTrainer if projected else NaturalCorpusTrainer
            return cls(parent,sampler,binding,batch=batch)
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            job['status']='running';memory=configure_resident_memory(0)
            beat('native-initial-state-and-fixed64')
            rows=json.loads(Path(c['sample']['path']).read_text())['rows']
            if len(rows)!=64:raise ValueError('Original fixed TRAIN64 required')
            t=build(16,False);expected_rng=host(rng_state());expected_weights=host(t.model.state_dict())
            ids=torch.tensor([[2]+rows[0]['prefix_ids']],device='cuda')
            with torch.no_grad(),sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                expected_logits=t.model(ids).logits.detach().clone()
            del t;clear();t=build(16)
            initial=dict(native_weights=equal_state(expected_weights,host(t.model.state_dict())),
                original_parent_weights=equal_state(parent['model'],host(t.model.state_dict())),
                native_RNG=equal_state(expected_rng,host(rng_state())),
                native_parameters=sum(p.numel() for p in t.model.parameters())==10001152,
                head_parameters=sum(p.numel() for p in t.projector.parameters())==98304,
                native_tied=t.model.lm_head.weight is t.model.model.embed_tokens.weight,
                separate_head_state=not any('projector' in k for k in t.model.state_dict()))
            with torch.no_grad(),sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                initial['native_logits']=torch.equal(expected_logits,t.model(ids).logits)
            if not all(initial.values()):raise ValueError('Native initialization/head isolation differs: '+repr(initial))
            del expected_weights,expected_logits,ids
            for offset in range(0,64,16):
                check();group=rows[offset:offset+16]
                t.optimizer.zero_grad(set_to_none=True)
                auxiliary=[[2]+r['prefix_ids'] for r in group]+[[2]+r['suffix_ids'] for r in group]
                with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                    ids,lengths=right_pad(auxiliary,'cuda');h=right_padded_hidden(t.model,ids)
                    z=t.projector(h[torch.arange(32,device='cuda'),lengths-1])
                    loss,stats=symmetric_InfoNCE(z[:16],z[16:]);(COEFFICIENT*loss).backward()
                norms=dict(native=gradient_norm(t.model),head=gradient_norm(t.projector))
                if not torch.isfinite(loss) or not all(0<n<float('inf') for n in norms.values()):
                    raise ValueError('Fixed original TRAIN64 shared/head finite backward failed')
                fixed.append(dict(first=offset,pairs=16,loss=float(loss.detach()),gradient_norms=norms,
                    auxiliary_inputs=sum(map(len,auxiliary)),physical_inputs=ids.numel(),optimizer_updates=0))
                del ids,lengths,h,z,loss
            del t;clear()
            window=json.loads(Path(c['payload']['path']).read_text())['window']
            for batch in c['batch_candidates']:
                beat(f'capacity-and-source-batch{batch}');t=build(batch);history=[];histories[str(batch)]=history
                try:
                    # Materialize real Adam states before maximum-shape stress.
                    history.append(t.step());capacities[str(batch)]=worst_shape(t,window,batch)
                    torch.cuda.reset_peak_memory_stats()
                    for _ in range(7):check();history.append(t.step())
                    state=host(t.state_dict())
                    if not finite_state(state) or not all(torch.isfinite(p).all() for p in state['projector'].values()):
                        raise ValueError('Nonfinite native/head/optimizer state')
                    timings[str(batch)]=dict(stable=True,batch=batch,history=history,
                        peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                        median_CE_targets_per_second=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:]))
                    del state
                except torch.cuda.OutOfMemoryError as exc:
                    capacities.setdefault(str(batch),dict(passed=False,batch=batch,error=str(exc)))
                    timings[str(batch)]=dict(stable=False,batch=batch,history=history,error=str(exc))
                    break
                finally:del t;clear()
                atomic_json(RUN/'partial.json',dict(initial=initial,fixed64=fixed,capacity=capacities,timings=timings))
            stable=[b for b in c['batch_candidates'] if timings.get(str(b),{}).get('stable') and capacities[str(b)]['peak_VRAM_bytes']<memory['allocator_allowance_bytes']]
            batch=c['matched_scientific_batch']
            if batch not in stable:raise ValueError('Cached-control batch48 lacks stable resident projection evidence; no silent batch change')
            best=max(stable,key=lambda b:timings[str(b)]['median_CE_targets_per_second'])
            folder=RUN/'resume-gate';folder.mkdir(exist_ok=True);states,logs=[],[]
            for route in ('continuous','resumed'):
                beat('full-source-'+route);t=build(batch);history=[];histories[route]=history
                for i in range(4):
                    check();history.append(t.step())
                    if route=='resumed' and i==1:
                        t.save(folder/'split.pt');del t;clear();t=build(batch);t.load(folder/'split.pt')
                t.save(folder/(route+'.pt'));states.append(torch.load(folder/(route+'.pt'),map_location='cpu',weights_only=False))
                logs.append(history);del t;clear()
            checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
            checks['finite']=all(finite_state(s) and all(torch.isfinite(v).all() for v in s['projector'].values()) for s in states)
            checks['all_history_except_timing']=all(equal_state(
                {k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
            if not all(checks.values()):raise ValueError('Projected full-source CUDA state/history differs: '+repr(checks))
            check();elapsed=time.monotonic()-started
            result=dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                initial_checks=initial,fixed64=fixed,memory_policy=memory,capacity=capacities,timings=timings,
                measured_fastest_resident_batch=best,selected_matched_batch=batch,resume_checks=checks,
                resume_histories=logs,resume_checkpoints={r:ref(folder/(r+'.pt')) for r in ('continuous','resumed')},
                verification_updates=sum(len(h) for h in histories.values()),
                verification_CE_teacher_tokens=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                GPU_occupancy_seconds=elapsed,scientific_teacher_tokens=0,probe_weights_used_for_science=False,
                Base_complete=False,Chat_started=False,quantization_started=False,
                next_action='Implement/freeze one persistent projected100M command using measured matched-batch time; reuse closed CE/direct100M controls. No scientific launch before command/budget/evaluation ready. Original full Base criteria remain required.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed);atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='complete',matched_batch=batch,fastest_batch=best,GPU_seconds=elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),GPU_occupancy_seconds=time.monotonic()-started if started else 0)
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'failure-partial.json',dict(initial=initial,fixed64=fixed,capacity=capacities,timings=timings,histories=histories));raise
    finally:signal.alarm(0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--prepare',action='store_true');g.add_argument('--inspect',action='store_true');a=p.parse_args()
    if a.prepare:prepare()
    elif a.inspect:inspect();print('Frozen projection/source probe inspected; GPU0')
    else:run()
