"""One bounded, persisted native GQA/MHA batch and complete resume probe."""
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
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from base_kv_allocation_trainer import CEOnlyOriginalSampler, FreshKVAllocationTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host, right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import alive, finite_state, identity

CONFIG = ROOT/'configs/phase6/base_kv_allocation_probe.json'
RUN = ROOT/'reports/phase6/base-kv-allocation-probe-20261007'
SOURCES = ('scripts/base_kv_allocation_trainer.py','scripts/probe_base_kv_allocation.py',
    'scripts/probe_base_kv_allocation.ps1','tests/test_base_kv_allocation_trainer.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/phase6_performance.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock')
GOALS = dict(web=225000000,textbook=60000000,story=15000000)


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def prepare():
    started = time.monotonic()
    if CONFIG.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve fixed one-shot probe')
    proposal = ROOT/'reports/phase6/base_kv_allocation_proposal.json'
    p = json.loads(proposal.read_text())
    closed = ROOT/'reports/phase6/base_kv_head_gradient_completion.json'
    completion = json.loads(closed.read_text())
    if not completion['fixed_diagnostic_closed'] or alive(completion['actual_identity']):
        raise ValueError('Previous native diagnostic must be complete and absent')
    tests = ROOT/'reports/phase6/base_kv_allocation_trainer_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites) != 9 or any(
            int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Actual nine CPU checks required')
    old = json.loads((ROOT/'configs/phase6/base_label_smoothing_probe.json').read_text())
    codec = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    if sha256(codec.path) != old['tokenizer_sha256']:
        raise ValueError('Pinned tokenizer differs')
    def timeout(*_):
        raise TimeoutError('Fixed CPU preparation30s exhausted')
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(30)
    try:
        original = OriginalTrainCorpusSampler(p['source_binding']['pool'],p['source_binding']['manifest_sha256'],codec,GOALS)
        ce = CEOnlyOriginalSampler(p['source_binding']['pool'],p['source_binding']['manifest_sha256'],codec,GOALS)
        if ce.binding != p['source_binding']:
            raise ValueError('Accepted original TRAIN binding differs')
        trace = []
        excluded = {'prefix_ids','suffix_ids','auxiliary_eligibility'}
        for _ in range(8):
            a,b = original.take(4),ce.take(4)
            if not equal_state([{k:v for k,v in r.items() if k not in excluded} for r in a],
                               [{k:v for k,v in r.items() if k not in excluded} for r in b]):
                raise ValueError('Actual original source gold/byte/mask identity differs')
            trace.extend(dict(source=r['source'],family=r['source_family'],body_sha256=r['full_original_body_sha256'],
                index_position=r['index_byte_position'],teachers=r['teacher_tokens'],body_bytes=r['teacher_body_bytes'],
                EOS=r['original_EOS_targets']) for r in b)
        for key in ('binding','RNG','consumed','draws','documents_drawn','windows_emitted'):
            if not equal_state(original.state_dict()[key],ce.state_dict()[key]):
                raise ValueError('Actual original draw/teacher accounting differs: '+key)
        parity = dict(passed=True,rows=len(trace),trace=trace,source_teachers=ce.consumed,
            scope='Fixed first32 original rows; exact gold/windows/bytes/EOS/draws, auxiliary metadata deliberately different',
            CPU_seconds=time.monotonic()-started, scientific_teachers=0)
        c = dict(created_at=now(),proposal=ref(proposal),CPU_tests=ref(tests),previous_completion=ref(closed),
            sources={s:sha256(ROOT/s) for s in SOURCES},variants=p['variants'],goals=GOALS,seed=42,
            optimizer=p['optimizer'],source_binding=p['source_binding'],tokenizer_sha256=old['tokenizer_sha256'],
            payload=old['payload'],probe=p['probe'],all_new_GPU_ceiling=p['absolute_all_new_GPU_ceiling_seconds'],
            actual_original_source_parity=parity,scientific_teachers=0,Base_complete=False,
            Chat_started=False,quantization_started=False)
        if parity['CPU_seconds'] > 30:
            timeout()
        atomic_json(CONFIG,c)
        print(json.dumps(dict(status='paired_probe_frozen_GPU0',CPU_seconds=parity['CPU_seconds'],actual_source_rows=32)))
    finally:
        signal.alarm(0)


def inspect():
    c = json.loads(CONFIG.read_text())
    for key in ('proposal','CPU_tests','previous_completion','payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Frozen reference differs: '+key)
    for source,digest in c['sources'].items():
        if sha256(ROOT/source) != digest:
            raise ValueError('Frozen source differs: '+source)
    previous = json.loads(Path(c['previous_completion']['path']).read_text())
    if alive(previous['actual_identity']):
        raise ValueError('Prior diagnostic still alive')
    if (RUN/'job.json').exists():
        raise ValueError('Inspect existing one-shot PID/results; no blind retry')
    return c


def worst_shape(t,window,batch):
    t.optimizer.zero_grad(set_to_none=True)
    torch.cuda.reset_peak_memory_stats()
    ids = torch.tensor([window['input_ids']]*batch,device='cuda')
    targets = torch.tensor([window['target_ids']]*batch,device='cuda')
    if ids.shape[1] != 1024 or int(targets[0].ne(-100).sum()) != 512:
        raise ValueError('Previously verified full1024/512 original window required')
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
        hidden = right_padded_hidden(t.model,ids)
        mask = targets.ne(-100)
        loss = F.cross_entropy(t.model.lm_head(hidden[mask]).float(),targets[mask])
        loss.backward()
    gradient = torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
    torch.cuda.synchronize()
    if not torch.isfinite(loss) or not 0 < float(gradient) < float('inf'):
        raise ValueError('Actual full-context CUDA/BF16 must be finite')
    result = dict(passed=True,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),context=1024,
        teachers=int(mask.sum()),physical_input_tokens=ids.numel(),loss=float(loss.detach()),
        gradient_norm=float(gradient),optimizer_updates=0)
    t.optimizer.zero_grad(set_to_none=True)
    return result


def run():
    c = inspect()
    if not torch.cuda.is_available():
        raise RuntimeError('Actual WSL CUDA required')
    RUN.mkdir(parents=True,exist_ok=True)
    job = dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teachers=0,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='One-shot180s probe: inspect terminal/partial PID and evidence, no blind repetition.')
    atomic_json(RUN/'job.json',job)
    histories,capacity,timings,resume = {},{}, {},{}
    started = None
    def check(*args):
        if args or (started is not None and time.monotonic()-started > c['probe']['total_GPU_cap_seconds']):
            raise TimeoutError('Fixed paired native GPU180s exhausted')
    def beat(stage):
        check()
        job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def clear():
        gc.collect()
        torch.cuda.empty_cache()
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        codec = Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        if sha256(codec.path) != c['tokenizer_sha256']:
            raise ValueError('Pinned tokenizer differs')
        binding = dict(proposal=c['proposal'],config_sha256=sha256(CONFIG),weights_role='verification_only')
        def build(arm,batch):
            s = CEOnlyOriginalSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],codec,c['goals'])
            if s.binding != c['source_binding']:
                raise ValueError('Actual accepted original TRAIN binding differs')
            return FreshKVAllocationTrainer(c['variants'][arm],s,binding,batch=batch)
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target = RUN/'source'/name
            target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(ROOT/name,target)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM,check)
            signal.alarm(c['probe']['total_GPU_cap_seconds'])
            job['status'] = 'running'
            memory = configure_resident_memory(0)
            window = json.loads(Path(c['payload']['path']).read_text())['window']
            for arm in c['variants']:
                capacity[arm],timings[arm] = {},{}
                for batch in c['probe']['candidate_batches']:
                    key = arm+'-batch'+str(batch)
                    beat(key)
                    t = build(arm,batch)
                    history = []
                    histories[key] = history
                    try:
                        # Allocate real Adam state before full-context resident capacity stress.
                        check();history.append(t.step())
                        capacity[arm][str(batch)] = worst_shape(t,window,batch)
                        for _ in range(c['probe']['warmup_steps']):
                            check();history.append(t.step())
                        measured = []
                        for _ in range(c['probe']['timed_steps']):
                            check();row = t.step();history.append(row);measured.append(row)
                        timings[arm][str(batch)] = dict(
                            median_original_teachers_per_second=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in measured),
                            median_physical_inputs_per_second=statistics.median(r['physical_inputs_this_update']/r['seconds'] for r in measured),
                            median_data_wait_seconds=statistics.median(r['data_wait_seconds'] for r in measured),
                            timed_updates=measured)
                    except torch.OutOfMemoryError as exc:
                        capacity[arm][str(batch)] = dict(passed=False,OOM=repr(exc),stop_larger_candidates=True)
                        break
                    finally:
                        del t;clear()
            common = [b for b in c['probe']['candidate_batches'] if all(str(b) in timings[a] and
                capacity[a][str(b)]['passed'] for a in c['variants'])]
            if not common:
                raise ValueError('No measured common resident-stable batch')
            def cost(batch):
                return sum(300000000/timings[a][str(batch)]['median_original_teachers_per_second'] for a in c['variants'])
            selected = min(common,key=cost)
            gate = RUN/'resume-gate'
            gate.mkdir(exist_ok=True)
            for arm in c['variants']:
                states,logs = [],[]
                for route in ('continuous','resumed'):
                    beat(arm+'-'+route)
                    t = build(arm,selected)
                    history = []
                    histories[arm+'-'+route] = history
                    for index in range(4):
                        check();history.append(t.step())
                        if route == 'resumed' and index == 1:
                            t.save(gate/(arm+'-split.pt'))
                            del t;clear();t=build(arm,selected);t.load(gate/(arm+'-split.pt'))
                    path = gate/(arm+'-'+route+'.pt')
                    t.save(path)
                    states.append(torch.load(path,map_location='cpu',weights_only=False))
                    logs.append(history)
                    del t;clear()
                checks = {k:equal_state(states[0][k],states[1][k]) for k in states[0]}
                checks['finite'] = all(finite_state(s) for s in states)
                checks['token_schedule_accounting'] = all(s['scheduler']['tokens']==s['counters']['supervised_tokens']
                    ==sum(s['counters']['source_teachers'].values()) and s['counters']['source_teachers']==s['sampler']['consumed'] for s in states)
                checks['all_history_except_timing'] = all(equal_state(
                    {k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                    {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
                if not all(checks.values()):
                    raise ValueError('Actual native full-state resume differs: '+repr(checks))
                resume[arm] = dict(checks=checks,histories=logs,checkpoints={route:ref(gate/(arm+'-'+route+'.pt')) for route in ('continuous','resumed')})
                del states,logs;clear()
            parity_keys = ('source_teachers','source_EOS','CE_input_tokens','physical_input_tokens','original_body_bytes','token_digest','draw_trace','lr')
            stream_parity = all(equal_state(a[k],b[k]) for a,b in zip(resume['GQA']['histories'][0],resume['MHA']['histories'][0],strict=True) for k in parity_keys)
            if not stream_parity:
                raise ValueError('Native allocation arms consume different original source stream')
            check()
            elapsed = time.monotonic()-started
            budgets = {a:math.ceil(300000000/timings[a][str(selected)]['median_original_teachers_per_second']*1.3+900) for a in c['variants']}
            eligible = sum(budgets.values())+elapsed <= c['all_new_GPU_ceiling']
            result = dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                memory_policy=memory,capacity=capacity,timings=timings,selected_common_batch=selected,
                common_resident_candidates=common,resume=resume,original_stream_parity=stream_parity,
                histories=histories,verification_updates=sum(len(h) for h in histories.values()),
                verification_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                GPU_occupancy_seconds=elapsed,GPU_limit_seconds=180,science_caps_seconds=budgets,
                forecast_all_new_GPU_seconds=sum(budgets.values())+elapsed,science_budget_eligible=eligible,
                scientific_teachers=0,probe_weights_used_for_science=False,Base_complete=False,
                Chat_started=False,quantization_started=False,
                next_action='Implement/freeze bounded scientific runner and review only if measured total fits9000s; otherwise preserve actual failed budget and close this proposed300M protocol without raising its cap.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='paired_native_probe_complete',batch=selected,GPU_seconds=elapsed,
                forecast_GPU_seconds=result['forecast_all_new_GPU_seconds'],science_budget_eligible=eligible)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),
            GPU_occupancy_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(RUN/'job.json',job)
        atomic_json(RUN/'failure-partial.json',dict(histories=histories,capacity=capacity,timings=timings,resume=resume))
        raise
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true')
    group.add_argument('--inspect',action='store_true')
    args = parser.parse_args()
    if args.prepare:
        prepare()
    elif args.inspect:
        inspect();print('Frozen paired native probe inspected; GPU0')
    else:
        run()
