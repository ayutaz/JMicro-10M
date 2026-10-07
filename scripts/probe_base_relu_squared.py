"""Durable one-shot paired FFN CUDA/resume/capacity/timing verification."""
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
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from base_relu_squared_model import model_from_config, squared_config
from base_relu_squared_trainer import ARMS, FreshFFNTrainer, committed_state
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import alive, identity
from probe_base_kv_allocation import worst_shape

CONFIG = ROOT / 'configs/phase6/base_relu_squared_probe.json'
RUN = ROOT / 'reports/phase6/base-relu-squared-probe-20261007'
SOURCES = ('scripts/base_relu_squared_model.py', 'scripts/base_relu_squared_trainer.py',
    'scripts/base_relu_squared_evaluation.py', 'scripts/prepare_base_relu_squared_proposal.py',
    'scripts/probe_base_relu_squared.py', 'scripts/probe_base_relu_squared.ps1',
    'tests/test_base_relu_squared.py', 'tests/test_base_relu_squared_evaluation.py',
    'scripts/base_kv_allocation_trainer.py', 'scripts/probe_base_kv_allocation.py',
    'scripts/base_native_teacher_KD_trainer.py', 'scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py', 'scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/training.py',
    'src/jmicro/tokenizer.py', 'scripts/run_complete_text_comparison.py',
    'src/jmicro/japanese_evaluation.py', 'uv.lock')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def prepare():
    started = time.monotonic()
    if CONFIG.exists() or (RUN / 'job.json').exists():
        raise ValueError('Preserve one-shot prospective FFN probe')
    proposal = ROOT / 'reports/phase6/base_relu_squared_proposal.json'
    p = read_json(proposal)
    tests = ROOT / 'reports/phase6/base_relu_squared_CPU_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if (sum(int(s.attrib['tests']) for s in suites) != 22
            or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped'))):
        raise ValueError('Actual22 CPU model/trainer/typed-likelihood checks required')
    old = read_json(ROOT / 'configs/phase6/base_kv_allocation_probe.json')
    codec = Tokenizer(ROOT / p['tokenizer'])
    if sha256(codec.path) != p['tokenizer_sha256']:
        raise ValueError('Pinned tokenizer differs')
    variants = dict(SwiGLU=p['variants']['SwiGLU'],
                    ReLU_squared=squared_config(p['variants']['SwiGLU'], p['optimizer']['seed']))
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
    atomic_json(CONFIG, dict(created_at=now(), proposal=ref(proposal), CPU_tests=ref(tests),
        initial_failed_CPU_tests=ref(ROOT / 'reports/phase6/base_relu_squared_tests_initial.xml'),
        initial_failure='Test assertion passed a requires-grad Tensor to pytest.approx; fixed by detach+float. No numeric/model or acceptance threshold change.',
        source_sha256={s: sha256(ROOT / s) for s in SOURCES}, variants=variants,
        parameter_counts=counts, source_binding=p['source_binding'], goals=p['goals'],
        optimizer=p['optimizer'], resource=p['resource'], payload=payload,
        tokenizer=p['tokenizer'], tokenizer_sha256=p['tokenizer_sha256'],
        CPU_preparation_seconds=elapsed, scientific_gold_tokens=0, Base_complete=False,
        Chat_started=False, quantization_started=False))
    print('Frozen paired exact10M FFN probe;22 CPU passed; GPU0')


def inspect(permit_existing=False):
    c = read_json(CONFIG)
    for name in ('proposal', 'CPU_tests', 'initial_failed_CPU_tests', 'payload'):
        if sha256(Path(c[name]['path'])) != c[name]['sha256']:
            raise ValueError('Frozen reference changed: ' + name)
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
    histories, capacity, resume, timing = {}, {}, {}, {}
    initial_checks = {}
    started = None
    def check(*args):
        if args or (started is not None and time.monotonic() - started > c['resource']['probe_GPU_cap_seconds']):
            raise TimeoutError('Fixed paired FFN GPU180s exhausted')
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
            return FreshFFNTrainer(c['variants'][arm], sampler, binding, arm, batch=o['batch'],
                seed=o['seed'], warmup=o['warmup_gold'], peak=o['peak_lr'], final=o['final_lr'])
        for name in (*SOURCES, CONFIG.relative_to(ROOT).as_posix()):
            destination = RUN / 'source' / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGALRM, check)
            signal.alarm(c['resource']['probe_GPU_cap_seconds'])
            memory = configure_resident_memory(0)
            window = read_json(Path(c['payload']['path']))['window']
            a = build('SwiGLU'); before = host(rng_state())
            b = build('ReLU_squared')
            initial_checks = dict(non_FFN_tensors_equal=all(torch.equal(v, b.model.state_dict()[k])
                for k, v in a.model.state_dict().items() if '.mlp.' not in k),
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
                    raise ValueError('Actual full-state FFN CUDA resume mismatch: ' + repr(checks))
                resume[arm] = dict(checks=checks, histories=logs,
                    checkpoints={r: ref(gate / (arm + '-' + r + '.pt')) for r in ('continuous', 'resumed')})
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
                    science_cap_seconds=math.ceil(300000000 * seconds / teachers * 1.3 + 900))
                del t; clear()
            keys = ('source_teachers', 'source_EOS', 'CE_input_tokens', 'physical_input_tokens',
                    'original_body_bytes', 'token_digest', 'draw_trace', 'lr')
            parity = all(equal_state(a[k], b[k]) for a, b in zip(
                resume['SwiGLU']['histories'][0], resume['ReLU_squared']['histories'][0], strict=True) for k in keys)
            if not parity:
                raise ValueError('Paired actual original gold/mask/source/EOS stream differs')
            check(); elapsed = time.monotonic() - started
            forecast = sum(v['science_cap_seconds'] for v in timing.values()) + elapsed
            result = dict(status='complete', passed=True, actual_identity=identity(), config_sha256=sha256(CONFIG),
                initial_checks=initial_checks, memory_policy=memory, capacity=capacity, resume=resume,
                timing=timing, histories=histories, original_stream_parity=parity,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_original_gold=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                GPU_seconds=elapsed, GPU_cap_seconds=c['resource']['probe_GPU_cap_seconds'],
                forecast_all_new_GPU_seconds=forecast,
                science_budget_eligible=forecast <= c['resource']['total_GPU_cap_seconds'],
                scientific_gold_tokens=0, probe_weights_used_for_science=False,
                Base_complete=False, Chat_started=False, quantization_started=False,
                next_action='Implement/freeze durable typed two-arm300M science and unchanged review only if measured fixed14400s cap fits. Otherwise close without batch/cap/teacher rescue.')
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', stage='complete', ended_at=now(), GPU_seconds=elapsed)
            atomic_json(RUN / 'job.json', job)
            print('Paired FFN CUDA/resume/capacity complete; forecast_seconds=' + str(forecast)
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
        inspect(); print('Frozen paired FFN probe inspected; GPU0')
    else:
        run()
