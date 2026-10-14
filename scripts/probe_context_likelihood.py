"""One owned native CUDA probe, separate from scientific learning/evaluation.

Verification weights stay WSL-only. The original10B parent is verified before
use; no verification checkpoint may initialize science. Never rerun a terminal
probe. CPU prepare does not repeat the completed32-batch corpus feasibility.
"""
import argparse
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.context_likelihood import pair_loss
from jmicro.experiment import sha256, now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from context_likelihood_trainer import ContextLikelihoodTrainer, suffix_scores
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity, alive
from probe_base_kv_allocation import worst_shape

PREP = ROOT / 'reports/phase6/context-likelihood-preparation-20261015'
RUN = ROOT / 'reports/phase6/context-likelihood-probe-20261015'
CONFIG = ROOT / 'configs/phase6/context_likelihood_probe_20261015.json'
SOURCES = ('scripts/probe_context_likelihood.py', 'scripts/probe_context_likelihood.ps1',
    'scripts/context_likelihood_trainer.py', 'src/jmicro/context_likelihood.py',
    'scripts/natural_context_contrast_corpus.py', 'scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py', 'scripts/probe_base_kv_allocation.py',
    'scripts/base_fim_trainer.py', 'scripts/base_fim_sampler.py', 'scripts/base_kv_allocation_trainer.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/tokenizer.py',
    'src/jmicro/training.py', 'tests/test_context_likelihood_probe.py', 'uv.lock')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def weights_digest(state):
    digest = hashlib.sha256()
    for name, tensor in sorted(state['model'].items()):
        digest.update(name.encode())
        digest.update(str(tensor.dtype).encode())
        digest.update(str(tuple(tensor.shape)).encode())
        digest.update(tensor.detach().cpu().numpy().tobytes())
    return digest.hexdigest()


def assert_scope(c):
    expected = dict(kind='owned_native_context_likelihood_CUDA_technical_v1',
        batch=48, seed=42, GPU_ceiling_seconds=180, timed_updates=32,
        continuous_updates=6, split_updates=[3, 3], capacity_shape=[48, 1024],
        auxiliary_capacity_shape=[96, 512], main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0,
        Base_adopted=False, TEST_prepared=False)
    if any(c.get(k) != value for k, value in expected.items()):
        raise ValueError('Exact one-shot technical scope required')


def passed_tests(path, count):
    suites = list(ET.parse(path).getroot().iter('testsuite'))
    if (sum(int(s.attrib.get('tests', 0)) for s in suites) != count
            or any(int(s.attrib.get(k, 0)) for s in suites for k in ('failures', 'errors', 'skipped'))):
        raise ValueError('Completed actual CPU checks required')


def build(c, parent, device='cpu', legacy=False):
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    codec = Tokenizer(ROOT / old['tokenizer'])
    source = old['source_binding']
    sampler = OriginalTrainCorpusSampler(source['pool'], source['manifest_sha256'], codec, old['goals'], seed=42)
    if sampler.binding != source:
        raise ValueError('Prior verified accepted TRAIN identity differs')
    binding = dict(parent=c['parent'], source_binding=source,
                   weights_role='verification_only', protocol='context_likelihood_owned_CUDA_technical')
    if legacy:
        return NaturalCorpusTrainer(parent, sampler, binding, batch=48, contrast=False, device=device, seed=42)
    return ContextLikelihoodTrainer(parent, sampler, binding, batch=48, device=device, seed=42)


def prepare():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or CONFIG.exists() or (RUN / 'job.json').exists():
        raise ValueError('Fresh CPU-only preparation required; preserve existing evidence')
    started = time.monotonic()
    torch.set_num_threads(2)
    p = json.loads((PREP / 'proposal.json').read_text())
    completion = json.loads((PREP / 'CPU_preparation.json').read_text())
    feasibility = json.loads((PREP / 'CPU_feasibility.json').read_text())
    if (p['native_parameters'] != 10001152 or p['extra_parameters'] != 0
            or p['main_CE']['batch'] != 48 or p['main_CE']['seed'] != 42
            or p['main_CE']['targets'] != 100000000 or p['auxiliary']['coefficient'] != .1
            or p['owned_technical_GPU_cap_seconds'] != 180 or p['prospective_GPU_cap_seconds'] != 4800
            or p['science_frozen'] is not False or p['Base_adopted'] is not False
            or feasibility['eligible_for_owned_CUDA_implementation_probe'] is not True):
        raise ValueError('Unchanged prospective mechanism and passed source feasibility required')
    for path, pin in completion['source_sha256'].items():
        if sha256(ROOT / path) != pin:
            raise ValueError('CPU-verified implementation differs: ' + path)
    tests = ((PREP / 'CPU_tests.xml', 12), (PREP / 'trainer_CPU_tests.xml', 11),
             (PREP / 'probe_CPU_tests.xml', 8))
    for path, count in tests:
        passed_tests(path, count)
    accepted_path = ROOT / 'configs/phase6/natural_context_contrast_comparison.json'
    old = json.loads(accepted_path.read_text())
    if old['parent'] != p['parent'] or old['source_binding'] != p['accepted_source_binding']:
        raise ValueError('Matched historical native source/parent differs')
    if sha256(Path(p['parent']['path'])) != p['parent']['sha256']:
        raise ValueError('Original learned parent differs')
    parent = torch.load(p['parent']['path'], map_location='cpu', weights_only=False)
    c = dict(kind='owned_native_context_likelihood_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, timed_updates=32, continuous_updates=6, split_updates=[3, 3],
        capacity_shape=[48, 1024], auxiliary_capacity_shape=[96, 512], main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0, Base_adopted=False, TEST_prepared=False,
        parent=p['parent'], proposal=ref(PREP / 'proposal.json'), preparation=ref(PREP / 'CPU_preparation.json'),
        feasibility=ref(PREP / 'CPU_feasibility.json'), accepted_config=ref(accepted_path),
        CPU_tests=[dict(**ref(path), expected_tests=count) for path, count in tests],
        tokenizer=ref(ROOT / old['tokenizer']), sources={path: sha256(ROOT / path) for path in SOURCES})
    assert_scope(c)
    candidate = build(c, parent)
    zero = host(candidate.state_dict())
    control = build(c, parent, legacy=True)
    old_zero = host(control.state_dict())
    if not all(equal_state(zero[k], old_zero[k]) for k in ('model', 'optimizer', 'scheduler', 'RNG', 'sampler')):
        raise ValueError('Actual10M original-parent initialization and full data state differ')
    if candidate.spec['actual_unique_parameters'] != 10001152:
        raise ValueError('Actual unchanged10M required')
    payload = json.loads((ROOT / 'configs/phase6/base_parallel_residual_probe.json').read_text())['payload']
    if sha256(Path(payload['path'])) != payload['sha256']:
        raise ValueError('Accepted full-context technical payload differs')
    window = json.loads(Path(payload['path']).read_text())['window']
    if len(window['input_ids']) != 1024 or sum(i != -100 for i in window['target_ids']) != 512:
        raise ValueError('Existing native1024/512 technical window required')
    # Maximum auxiliary tensor geometry only; borrowed accepted token spans,
    # not newly accepted sentences or scientific matching examples.
    body = [i for i in window['target_ids'] if i >= 8]
    inputs = [i for i in window['input_ids'] if i >= 8]
    if len(body) < 496 or len(inputs) < 32:
        raise ValueError('Fixed accepted technical spans lack worst auxiliary shape')
    prefix = inputs[:16]
    alternate = next((inputs[i:i + 16] for i in range(16, len(inputs) - 15)
                      if inputs[i:i + 16] != prefix), None)
    if alternate is None:
        raise ValueError('Two distinct original technical prefix spans required')
    suffix = body[:496]
    stress_pair = dict(positive=dict(input_ids=[2] + prefix + suffix[:-1], target_ids=[-100] * 16 + suffix),
                      negative=dict(input_ids=[2] + alternate + suffix[:-1], target_ids=[-100] * 16 + suffix))
    RUN.mkdir(parents=True, exist_ok=True)
    stress_path = RUN / 'verification_shape_input.pt'
    torch.save(dict(window=window, auxiliary_pair=stress_pair,
                    role='technical_tensor_geometry_only_not_scientific_document'), stress_path)
    c.update(capacity_payload=ref(stress_path), initial_weights_sha256=weights_digest(zero),
             CPU_wall_seconds=time.monotonic() - started)
    candidate.sampler.handle.close()
    control.sampler.handle.close()
    atomic_json(CONFIG, c)
    print(json.dumps(dict(status='owned_technical_contract_frozen_no_GPU',
        actual_native_parameters=10001152, initial_original_parent_and_Adam_RNG_sampler_equal=True,
        CPU_wall_seconds=c['CPU_wall_seconds'])), flush=True)


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('Pinned owned technical config differs')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for key in ('parent', 'proposal', 'preparation', 'feasibility', 'accepted_config', 'tokenizer', 'capacity_payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Owned probe reference differs: ' + key)
    for source, digest in c['sources'].items():
        if sha256(ROOT / source) != digest:
            raise ValueError('Frozen probe source differs: ' + source)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('CPU evidence changed')
        passed_tests(row['path'], row['expected_tests'])
    if (RUN / 'job.json').exists() or (RUN / 'result.json').exists():
        raise ValueError('Inspect existing actual probe identity/results; do not relaunch')
    return c


def run(pin):
    c = inspect(pin)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin,
               scientific_teacher_positions=0, cumulative_GPU_ledger_closed=False)
    atomic_json(RUN / 'job.json', job)
    started = None
    updates = teachers = 0
    result = None
    def check(*args):
        if args or (started is not None and time.monotonic() - started > 180):
            raise TimeoutError('Owned CUDA180s ceiling exhausted; preserve terminal evidence')
    def beat(stage):
        check()
        job.update(stage=stage, heartbeat_at=now(), GPU_occupancy_seconds=time.monotonic() - started)
        atomic_json(RUN / 'job.json', job)
    def learn(trainer):
        nonlocal updates, teachers
        check()
        row = trainer.step()
        updates += 1
        teachers += row['CE_targets_this_update']
        return row
    def clear():
        gc.collect()
        torch.cuda.empty_cache()
    def dispose(trainer):
        trainer.sampler.handle.close()
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM, check)
            signal.signal(signal.SIGINT, check)
            if not torch.cuda.is_available():
                raise RuntimeError('Actual local CUDA inaccessible')
            job['status'] = 'running'
            memory = configure_resident_memory(0)
            parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
            full = build(c, parent, 'cuda')
            zero = host(full.state_dict())
            if weights_digest(zero) != c['initial_weights_sha256']:
                raise ValueError('Actual CUDA initialization differs from original parent')
            torch.save(zero, RUN / 'verification_zero.pt')
            beat('continuous6')
            full_history = [learn(full) for _ in range(6)]
            expected = host(full.state_dict())
            if not expected['counters']['auxiliary_pairs']:
                raise ValueError('Resume verification must actually exercise auxiliary FIFO/loss')
            dispose(full)
            del full
            clear()
            split = build(c, parent, 'cuda')
            actual_history = [learn(split) for _ in range(3)]
            split.save(RUN / 'verification_split.pt')
            dispose(split)
            del split
            clear()
            resumed = build(c, parent, 'cuda')
            resumed.load(RUN / 'verification_split.pt')
            actual_history.extend(learn(resumed) for _ in range(3))
            strip = lambda r: {k: v for k, v in r.items() if k not in ('seconds', 'data_wait_seconds')}
            if (not equal_state(expected, host(resumed.state_dict()))
                    or not equal_state([strip(r) for r in full_history], [strip(r) for r in actual_history])):
                raise ValueError('Actual CUDA complete state/FIFO/history resume mismatch')
            shape = torch.load(c['capacity_payload']['path'], map_location='cpu', weights_only=False)
            beat('worst_CE48x1024')
            before = weights_digest(host(resumed.state_dict()))
            ce_capacity = worst_shape(resumed, shape['window'], 48)
            beat('worst_aux96x512')
            torch.cuda.reset_peak_memory_stats()
            resumed.optimizer.zero_grad(set_to_none=True)
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION), torch.autocast('cuda', dtype=torch.bfloat16):
                positive, negative, counts = suffix_scores(resumed.model, [shape['auxiliary_pair']] * 48, 'cuda')
                loss = pair_loss(positive, negative)
                loss.backward()
            gradient = torch.nn.utils.clip_grad_norm_(resumed.model.parameters(), 1., error_if_nonfinite=True)
            torch.cuda.synchronize()
            if not torch.isfinite(loss) or not 0 < float(gradient) < float('inf'):
                raise ValueError('Finite nonzero worst auxiliary CUDA backward required')
            aux_capacity = dict(passed=True, physical_input_tokens=counts['physical_inputs'],
                likelihood_positions=counts['target_evaluations'], peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                loss=float(loss.detach()), gradient_norm=float(gradient), optimizer_updates=0,
                scope='maximum tensor geometry from accepted token spans; not scientific document matching')
            del positive, negative, loss, gradient
            resumed.optimizer.zero_grad(set_to_none=True)
            if (weights_digest(host(resumed.state_dict())) != before
                    or max(ce_capacity['peak_VRAM_bytes'], aux_capacity['peak_VRAM_bytes']) >= memory['allocator_allowance_bytes']):
                raise ValueError('Worst-shape altered weights or exceeded resident allowance')
            beat('steady32')
            timings = [learn(resumed) for _ in range(32)]
            if any(not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in timings):
                raise ValueError('Finite actual native timing rows required')
            resumed.save(RUN / 'verification_final.pt')
            forecast = math.ceil(100000000 / sum(r['CE_targets_this_update'] for r in timings)
                                 * sum(r['seconds'] for r in timings) * 1.3 + 600)
            check()
            result = dict(status='complete', passed=True, config_sha256=pin, actual_identity=identity(),
                memory_policy=memory, CE_capacity=ce_capacity, auxiliary_capacity=aux_capacity,
                all_state_and_history_resume_equal=True, actual_auxiliary_active=True,
                initial_original_parent_weights_equal=True, native_parameters=10001152,
                all32_timings=timings, scientific_forecast_seconds=forecast,
                verification_optimizer_updates=updates, verification_main_CE_positions=teachers,
                scientific_teacher_positions=0, DEV_opened=False, TEST_opened=False, Base_qualified=False, Base_adopted=False)
            dispose(resumed)
            del resumed
            clear()
    except Exception as error:
        result = dict(status='failed', passed=False, config_sha256=pin, actual_identity=identity(),
            error_type=type(error).__name__, error=str(error), traceback=traceback.format_exc(),
            verification_optimizer_updates=updates, verification_main_CE_positions=teachers,
            scientific_teacher_positions=0, Base_qualified=False, Base_adopted=False)
    finally:
        elapsed = 0 if started is None else time.monotonic() - started
        if result is None:
            result = dict(status='failed', passed=False, error='Probe terminated before a complete result', scientific_teacher_positions=0)
        if elapsed > 180:
            result.update(status='failed', passed=False, error='Total owned GPU interval exceeded180s')
        result.update(GPU_occupancy_seconds=elapsed, cumulative_GPU_ledger_closed=True,
            science_budget_eligible=bool(result['passed'] and result['scientific_forecast_seconds'] + elapsed <= 4800))
        job.update(status=result['status'], ended_at=now(), GPU_occupancy_seconds=elapsed,
                   cumulative_GPU_ledger_closed=True)
        atomic_json(RUN / 'result.json', result)
        atomic_json(RUN / 'job.json', job)
    print(json.dumps({k: result.get(k) for k in ('status', 'passed', 'GPU_occupancy_seconds',
        'verification_optimizer_updates', 'scientific_forecast_seconds', 'science_budget_eligible', 'error')}), flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'inspect', 'run'))
    parser.add_argument('--config-sha256')
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare()
    elif args.action == 'inspect':
        inspect(args.config_sha256)
        print('Owned native technical preflight passed; no CUDA allocation')
    else:
        run(args.config_sha256)
