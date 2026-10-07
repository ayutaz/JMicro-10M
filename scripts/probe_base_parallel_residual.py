"""Durable one-shot paired residual CUDA/resume/capacity/timing verification."""
import argparse
import gc
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from base_parallel_residual_model import model_from_config, parallel_config
from base_parallel_residual_trainer import ARMS, FreshResidualTrainer, committed_state
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity
from probe_base_kv_allocation import worst_shape

CONFIG = ROOT / 'configs/phase6/base_parallel_residual_probe.json'
RUN = ROOT / 'reports/phase6/base-parallel-residual-probe-20261007'
SOURCES = ('scripts/base_parallel_residual_model.py', 'scripts/base_parallel_residual_trainer.py',
    'scripts/base_parallel_residual_evaluation.py', 'scripts/prepare_base_parallel_residual_proposal.py',
    'scripts/probe_base_parallel_residual.py', 'scripts/probe_base_parallel_residual.ps1',
    'tests/test_base_parallel_residual_model.py', 'tests/test_base_parallel_residual_trainer.py',
    'tests/test_base_parallel_residual_evaluation.py', 'tests/test_base_parallel_residual_workflow.py',
    'scripts/base_kv_allocation_trainer.py', 'scripts/probe_base_kv_allocation.py',
    'scripts/base_native_teacher_KD_trainer.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/training.py',
    'src/jmicro/tokenizer.py', 'scripts/run_complete_text_comparison.py',
    'src/jmicro/japanese_evaluation.py', 'uv.lock')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def validate_contract(p):
    if (set(p['variants']) != set(ARMS) or p['original_gold_each'] != 2000000000
            or p['scientific_gold_total'] != 4000000000 or p['new_unique_corpus_tokens'] != 0
            or p['goals'] != dict(web=1500000000, textbook=400000000, story=100000000)
            or p['variants']['parallel'] != parallel_config(p['variants']['sequential'])
            or p['resource']['own_probe_GPU_cap_seconds'] != 180
            or p['resource']['total_GPU_cap_seconds'] != 86400
            or p['resource']['fixed_batch'] != 80 or p['resource']['capacity_shape'] != [80, 1024]
            or p['resource']['stride'] != 512 or p['optimizer']['batch'] != 80):
        raise ValueError('Exact fresh paired2B residual contract and prospective24h ceiling required')


def forecast(seconds, gold):
    if (type(seconds) not in (int, float) or not math.isfinite(seconds) or seconds <= 0
            or type(gold) is not int or gold <= 0):
        raise ValueError('Positive finite SUM all32 seconds and original gold required')
    return math.ceil(2000000000 * seconds / gold * 1.3 + 900)


def paired_budget(timing, elapsed):
    if (set(timing) != set(ARMS) or type(elapsed) not in (int, float)
            or not math.isfinite(elapsed) or not 0 < elapsed <= 180):
        raise ValueError('Both exact arms and bounded actual own probe required')
    budgets = {arm: forecast(timing[arm]['total_seconds'], timing[arm]['total_original_gold']) for arm in ARMS}
    return budgets, sum(budgets.values()) + elapsed <= 86400


def passed_tests(path, expected):
    suites = list(ET.parse(path).getroot().iter('testsuite'))
    if (sum(int(s.attrib['tests']) for s in suites) != expected
            or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped'))):
        raise ValueError('Actual complete current CPU checks required: ' + str(path))


def source_checks(left, right):
    return dict(full_counters=equal_state(left['counters'], right['counters']),
                full_sampler=equal_state(left['sampler'], right['sampler']),
                full_scheduler=equal_state(left['scheduler'], right['scheduler']))


def prepare():
    started = time.monotonic()
    if CONFIG.exists() or (RUN / 'job.json').exists():
        raise ValueError('Preserve one-shot prospective residual probe')
    proposal = ROOT / 'reports/phase6/base_parallel_residual_proposal.json'
    p = read_json(proposal)
    validate_contract(p)
    preparation = ROOT / 'reports/phase6/base_parallel_residual_CPU_preparation.json'
    prepared = read_json(preparation)
    if prepared['proposal_sha256'] != sha256(proposal) or prepared['total_current_CPU_tests'] != 25:
        raise ValueError('Current25 CPU preparation must bind exact proposal')
    for name, digest in prepared['source_sha256'].items():
        if sha256(ROOT / name) != digest:
            raise ValueError('Current CPU-tested implementation changed: ' + name)
    CPU_tests = []
    for name, expected in zip(prepared['current_tests'], (11, 11, 3), strict=True):
        path = ROOT / name
        passed_tests(path, expected)
        CPU_tests.append(ref(path))
    workflow_tests = ROOT / 'reports/phase6/base_parallel_residual_workflow_tests.xml'
    passed_tests(workflow_tests, 17)
    old = read_json(ROOT / 'configs/phase6/base_kv_allocation_probe.json')
    codec = Tokenizer(ROOT / p['tokenizer'])
    if sha256(codec.path) != p['tokenizer_sha256']:
        raise ValueError('Pinned tokenizer differs')
    variants = p['variants']
    counts = {}
    for arm, config in variants.items():
        with torch.device('meta'):
            model = model_from_config(config)
        counts[arm] = sum(v.numel() for v in model.parameters())
    if counts != dict.fromkeys(ARMS, 10001152):
        raise ValueError('Both actual exact native10M counts required')
    source = CEOnlyOriginalSampler(p['source_binding']['pool'], p['source_binding']['manifest_sha256'], codec, p['goals'])
    if source.binding != p['source_binding']:
        raise ValueError('Existing verified original TRAIN binding differs')
    payload = old['payload']
    if sha256(Path(payload['path'])) != payload['sha256']:
        raise ValueError('Previously fixed full1024 TRAIN payload differs')
    elapsed = time.monotonic() - started
    if elapsed > p['resource']['CPU_preparation_cap_seconds']:
        raise TimeoutError('Prospective CPU preparation30s exhausted')
    resource = dict(p['resource'], warmup_updates=3, timed_updates=32)
    atomic_json(CONFIG, dict(created_at=now(), proposal=ref(proposal), CPU_preparation=ref(preparation),
        CPU_tests=CPU_tests, CPU_workflow_tests=ref(workflow_tests),
        source_sha256={s: sha256(ROOT / s) for s in SOURCES}, variants=variants,
        parameter_counts=counts, source_binding=p['source_binding'], goals=p['goals'],
        optimizer=p['optimizer'], resource=resource, payload=payload,
        original_gold_each=p['original_gold_each'], scientific_gold_total=p['scientific_gold_total'],
        new_unique_corpus_tokens=0,
        tokenizer=p['tokenizer'], tokenizer_sha256=p['tokenizer_sha256'],
        CPU_preparation_seconds=elapsed, scientific_gold_tokens=0, Base_complete=False,
        Chat_started=False, quantization_started=False))
    print('Frozen paired exact10M residual probe; current25+17 CPU passed; GPU0')


def inspect(permit_existing=False):
    c = read_json(CONFIG)
    p = read_json(Path(c['proposal']['path']))
    validate_contract(p)
    for name in ('proposal', 'CPU_preparation', 'CPU_workflow_tests', 'payload'):
        if sha256(Path(c[name]['path'])) != c[name]['sha256']:
            raise ValueError('Frozen reference changed: ' + name)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Frozen current CPU tests changed')
    if any(c[k] != p[k] for k in ('variants', 'source_binding', 'goals', 'optimizer',
                                  'original_gold_each', 'scientific_gold_total', 'new_unique_corpus_tokens')):
        raise ValueError('Probe recipe differs from frozen prospective contract')
    if c['resource'] != dict(p['resource'], warmup_updates=3, timed_updates=32):
        raise ValueError('Original all32 timing and fixed resource contract required')
    for name, digest in c['source_sha256'].items():
        if sha256(ROOT / name) != digest:
            raise ValueError('Frozen source changed: ' + name)
    if not permit_existing and (RUN / 'job.json').exists():
        raise ValueError('Inspect saved exact PID/results; never repeat one-shot probe')
    return c


def run():
    c = inspect()
    if not torch.cuda.is_available():
        raise RuntimeError('Actual WSL CUDA required')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
        scientific_gold_tokens=0, Base_complete=False, Chat_started=False, quantization_started=False,
        restart_command='One-shot180s probe; inspect exact identity and partial evidence, do not retry unchanged failure.')
    atomic_json(RUN / 'job.json', job)
    histories, capacity, resume, timing, streams = {}, {}, {}, {}, {}
    initial_checks = {}
    started = None
    def check(*args):
        if args or (started is not None and time.monotonic() - started > c['resource']['own_probe_GPU_cap_seconds']):
            raise TimeoutError('Fixed paired residual GPU180s exhausted')
    def beat(stage):
        check()
        job.update(status='running', stage=stage, heartbeat_at=now(), GPU_seconds=time.monotonic() - started)
        atomic_json(RUN / 'job.json', job)
    def clear():
        gc.collect(); torch.cuda.empty_cache()
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        codec = Tokenizer(ROOT / c['tokenizer'])
        if sha256(codec.path) != c['tokenizer_sha256']:
            raise ValueError('Actual pinned tokenizer differs')
        binding = dict(config_sha256=sha256(CONFIG), proposal=c['proposal'], weights_role='verification_only')
        def build(arm):
            sampler = CEOnlyOriginalSampler(c['source_binding']['pool'], c['source_binding']['manifest_sha256'], codec, c['goals'])
            if sampler.binding != c['source_binding']:
                raise ValueError('Actual original source identity differs')
            o = c['optimizer']
            return FreshResidualTrainer(c['variants'][arm], sampler, binding, arm, batch=o['batch'],
                seed=o['seed'], warmup=o['warmup_gold'], peak=o['peak_lr'], final=o['final_lr'])
        for name in (*SOURCES, CONFIG.relative_to(ROOT).as_posix()):
            destination = RUN / 'source' / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, check)
            signal.alarm(c['resource']['own_probe_GPU_cap_seconds'])
            memory = configure_resident_memory(0)
            window = read_json(Path(c['payload']['path']))['window']
            a = build('sequential'); before = host(rng_state())
            b = build('parallel')
            initial_checks = dict(every_initial_tensor_equal=equal_state(a.model.state_dict(), b.model.state_dict()),
                paired_global_RNG_equal=equal_state(before, host(rng_state())),
                tied_heads=all(t.model.lm_head.weight is t.model.model.embed_tokens.weight for t in (a, b)),
                parameter_counts_exact=all(sum(p.numel() for p in t.model.parameters()) == 10001152 for t in (a, b)),
                optimizers_actual_only=all([id(p) for p in t.model.parameters()] ==
                    [id(p) for g in t.optimizer.param_groups for p in g['params']] for t in (a, b)))
            if not all(initial_checks.values()):
                raise ValueError('Actual paired CUDA initialization invariants failed')
            del a, b; clear()
            gate = RUN / 'resume-gate'; gate.mkdir(exist_ok=True)
            for arm in ARMS:
                states, logs = [], []
                for route in ('continuous', 'resumed'):
                    beat(arm + '-' + route)
                    t = build(arm)
                    history = []; histories[arm + '-' + route] = history
                    for index in range(4):
                        check(); history.append(t.step())
                        if route == 'resumed' and index == 1:
                            t.save(gate / (arm + '-split.pt'))
                            del t; clear(); t = build(arm); t.load(gate / (arm + '-split.pt'))
                    path = gate / (arm + '-' + route + '.pt')
                    t.save(path)
                    states.append(torch.load(path, map_location='cpu', weights_only=False))
                    logs.append(history)
                    del t; clear()
                checks = {k: equal_state(states[0][k], states[1][k]) for k in states[0]}
                checks['committed_finite_state'] = all(committed_state(s) for s in states)
                checks['all_history_except_timing'] = all(equal_state(
                    {k: v for k, v in x.items() if k not in ('seconds', 'data_wait_seconds')},
                    {k: v for k, v in y.items() if k not in ('seconds', 'data_wait_seconds')})
                    for x, y in zip(*logs, strict=True))
                if not all(checks.values()):
                    raise ValueError('Actual full-state residual CUDA resume mismatch: ' + repr(checks))
                resume[arm] = dict(checks=checks, histories=logs,
                    checkpoints={r: ref(gate / (arm + '-' + r + '.pt')) for r in ('continuous', 'resumed')})
                streams[arm] = {k: states[0][k] for k in ('counters', 'sampler', 'scheduler')}
                del states, logs; clear()
                beat(arm + '-worst1024-and-timing')
                t = build(arm)
                history = []; histories[arm + '-timing'] = history
                for _ in range(c['resource']['warmup_updates']):
                    check(); history.append(t.step())
                frozen_weights = host(t.model.state_dict())
                capacity[arm] = worst_shape(t, window, c['optimizer']['batch'])
                capacity[arm]['weights_unchanged_by_stress'] = equal_state(frozen_weights, host(t.model.state_dict()))
                if (not capacity[arm]['weights_unchanged_by_stress']
                        or capacity[arm]['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']):
                    raise ValueError('Resident full1024 stress changed weights or exceeded actual allowance')
                del frozen_weights
                measured = []
                for _ in range(c['resource']['timed_updates']):
                    check(); row = t.step(); history.append(row); measured.append(row)
                seconds = sum(r['seconds'] for r in measured)
                teachers = sum(r['CE_targets_this_update'] for r in measured)
                timing[arm] = dict(timed_updates=measured, total_seconds=seconds, total_original_gold=teachers,
                    seconds_per_original_gold=seconds / teachers,
                    original_gold_per_second=teachers / seconds,
                    total_data_wait_seconds=sum(r['data_wait_seconds'] for r in measured),
                    science_cap_seconds=forecast(seconds, teachers))
                del t; clear()
            keys = ('source_teachers', 'source_EOS', 'CE_input_tokens', 'physical_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'lr')
            parity = all(equal_state(a[k], b[k]) for a, b in zip(
                resume['sequential']['histories'][0], resume['parallel']['histories'][0], strict=True) for k in keys)
            if not parity:
                raise ValueError('Paired actual original gold/mask/source/EOS stream differs')
            stream_checks = source_checks(streams['sequential'], streams['parallel'])
            if not all(stream_checks.values()):
                raise ValueError('Actual entire paired sampler/counters/scheduler differs')
            check(); elapsed = time.monotonic() - started
            budgets, eligible = paired_budget(timing, elapsed)
            all_forecast = sum(budgets.values()) + elapsed
            result = dict(status='complete', passed=True, actual_identity=identity(), config_sha256=sha256(CONFIG),
                initial_checks=initial_checks, memory_policy=memory, capacity=capacity, resume=resume,
                timing=timing, histories=histories, original_stream_parity=parity,
                original_stream_checks=stream_checks, forecast_arm_seconds=budgets,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_gold=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                GPU_seconds=elapsed, GPU_cap_seconds=c['resource']['own_probe_GPU_cap_seconds'],
                forecast_all_new_GPU_seconds=all_forecast, science_budget_eligible=eligible,
                scientific_gold_tokens=0, probe_weights_used_for_science=False,
                Base_complete=False, Chat_started=False, quantization_started=False,
                next_action='Implement/freeze durable typed two-arm2B science and unchanged review only if measured fixed86400s cap fits. Otherwise close without batch/cap/teacher rescue.')
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', stage='complete', ended_at=now(), GPU_seconds=elapsed)
            atomic_json(RUN / 'job.json', job)
            print('Paired residual CUDA/resume/capacity complete; forecast_seconds=' + str(all_forecast)
                  + '; science_budget_eligible=' + str(result['science_budget_eligible']))
    except BaseException as exc:
        job.update(status='failed_or_interrupted', error=repr(exc), ended_at=now(),
            GPU_seconds=time.monotonic() - started if started is not None else 0)
        atomic_json(RUN / 'job.json', job)
        atomic_json(RUN / 'failure-partial.json', dict(initial_checks=initial_checks,
            histories=histories, capacity=capacity, resume=resume, timing=timing))
        raise
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prepare', action='store_true')
    group.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    if args.prepare:
        prepare()
    elif args.inspect:
        inspect(); print('Frozen paired residual probe inspected; GPU0')
    else:
        run()
