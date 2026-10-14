"""One owned native CUDA technical gate; never scientific or DEV/TEST work."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'scripts')]
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import sha256, now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state
from value_residual_trainer import ValueResidualTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler, NaturalCorpusTrainer
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity
from torch.nn import functional as F
from probe_context_likelihood import ref, weights_digest, passed_tests

PREP = ROOT/'reports/phase6/value-residual-preparation-20261015'
RUN = ROOT/'reports/phase6/value-residual-probe-20261015'
CONFIG = ROOT/'configs/phase6/value_residual_probe_20261015.json'
SOURCES = ('scripts/probe_value_residual.py', 'scripts/probe_value_residual.ps1',
    'scripts/value_residual_trainer.py', 'src/jmicro/value_residual.py',
    'scripts/context_likelihood_trainer.py', 'src/jmicro/context_likelihood.py',
    'scripts/probe_context_likelihood.py', 'scripts/probe_base_kv_allocation.py',
    'scripts/natural_context_contrast_corpus.py', 'scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py', 'scripts/base_fim_trainer.py',
    'scripts/base_fim_sampler.py', 'scripts/base_kv_allocation_trainer.py',
    'scripts/phase6_performance.py', 'src/jmicro/model.py', 'src/jmicro/tokenizer.py',
    'src/jmicro/training.py', 'tests/test_value_residual_probe.py',
    'tests/test_value_residual_training.py', 'uv.lock')


def assert_scope(c):
    expected = dict(kind='owned_native_first_value_residual_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, timed_updates=32, continuous_updates=6, split_updates=[3, 3],
        capacity_shape=[48, 1024], candidate_parameters=10001164, main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0,
        Base_adopted=False, TEST_prepared=False)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k, v in expected.items()):
        raise ValueError('Exact one-shot first-value residual technical scope required')


def build(c, parent, device='cpu', legacy=False):
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    codec = Tokenizer(ROOT/old['tokenizer'])
    source = old['source_binding']
    sampler = OriginalTrainCorpusSampler(source['pool'], source['manifest_sha256'], codec, old['goals'], seed=42)
    if sampler.binding != source:
        raise ValueError('Prior accepted source identity differs')
    binding = dict(parent=c['parent'], source_binding=source, weights_role='verification_only',
                   protocol='first_value_residual_owned_CUDA_technical')
    if legacy:
        return NaturalCorpusTrainer(parent, sampler, binding, batch=48, contrast=False, device=device, seed=42)
    return ValueResidualTrainer(parent, sampler, binding, batch=48, device=device, seed=42)


def worst_shape(trainer, window, batch):
    """Borrowed accepted geometry; explicit new traversal, no Adam step."""
    trainer.optimizer.zero_grad(set_to_none=True)
    torch.cuda.reset_peak_memory_stats()
    ids = torch.tensor([window['input_ids']]*batch, device='cuda')
    targets = torch.tensor([window['target_ids']]*batch, device='cuda')
    if ids.shape != (48,1024) or int(targets[0].ne(-100).sum()) != 512:
        raise ValueError('Previously accepted48x1024/512 technical window required')
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION), torch.autocast('cuda',dtype=torch.bfloat16):
        hidden = trainer.model.right_padded_hidden(ids)
        selected = targets.ne(-100)
        loss = F.cross_entropy(trainer.model.lm_head(hidden[selected]).float(), targets[selected])
        loss.backward()
    gradient = trainer.model.clip_grad_norm(1., error_if_nonfinite=True)
    torch.cuda.synchronize()
    if not torch.isfinite(loss) or not 0 < float(gradient) < float('inf'):
        raise ValueError('Actual first-value CUDA/BF16 max geometry must be finite')
    result = dict(passed=True, peak_VRAM_bytes=torch.cuda.max_memory_allocated(), context=1024,
        teachers=int(selected.sum()), physical_input_tokens=ids.numel(), loss=float(loss.detach()),
        gradient_norm=float(gradient), optimizer_updates=0,
        traversal='explicit_first_layer_V_shortcut_including_gradient')
    trainer.optimizer.zero_grad(set_to_none=True)
    return result


def check_cache(trainer, window):
    """Predeclared FP32 math full/cache check on existing technical spans."""
    plain = [i for i in window['input_ids'] if i >= 8]
    if len(plain) < 126:
        raise ValueError('Existing accepted cache geometry requires126 plain IDs')
    ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]], device=trainer.device)
    model, before, mode = trainer.model, host(rng_state()), trainer.model.training
    try:
        model.eval()
        with torch.no_grad(), sdpa_kernel(SDPBackend.MATH), torch.autocast(trainer.device.type, enabled=False):
            full = model(ids, use_cache=True)
            first = model(ids[:, :32], use_cache=True)
            last = model(ids[:, 32:], cache=first.cache, use_cache=True)
        difference = float((full.logits[:,32:]-last.logits).abs().max())
        if (not torch.isfinite(full.logits).all() or not torch.isfinite(last.logits).all()
                or not torch.allclose(full.logits[:,32:], last.logits, atol=3e-5, rtol=2e-5)
                or not torch.equal(full.cache.positions, last.cache.positions)
                or not torch.equal(full.cache.valid, last.cache.valid)
                or any(k.shape[1] != 2 or v.shape[1] != 2 for k,v in last.cache.layers)
                or not equal_state(before, host(rng_state()))):
            raise ValueError('Active first-value FP32 cache/mask/RNG gate failed')
        return dict(passed=True, dtype='FP32', backend='math', maximum_logit_difference=difference,
            absolute_tolerance=3e-5, relative_tolerance=2e-5, input_shape=[2,64], split=[32,32],
            KV_cache_heads=2, RNG_unchanged=True, optimizer_updates=0,
            scope='Existing accepted token spans; no model-quality or held-out input')
    finally:
        model.train(mode)


def prepare():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or CONFIG.exists() or (RUN/'job.json').exists():
        raise ValueError('Fresh CPU-only technical preparation required')
    started = time.monotonic()
    torch.set_num_threads(2)
    proposal = json.loads((PREP/'proposal.json').read_text())
    receipt = json.loads((PREP/'CPU_readiness.json').read_text())
    parity = json.loads((PREP/'actual_parent_CPU_parity.json').read_text())
    if (proposal['architecture']['native_reference_parameters'] != 10001152
            or proposal['architecture']['expected_candidate_parameters'] != 10001164
            or proposal['architecture']['added_parameters'] != 12
            or proposal['prospective_science']['batch'] != 48 or proposal['prospective_science']['seed'] != 42
            or proposal['prospective_science']['main_teachers'] != 100000000
            or proposal['prospective_science']['technical_GPU_cap_seconds'] != 180
            or proposal['prospective_science']['total_new_GPU_cap_seconds'] != 4800
            or proposal['Base_adopted'] is not False or not all(parity['checks'].values())):
        raise ValueError('Explicit same-budget first-V proposal and actual parent CPU parity required')
    for source, pin in receipt['source_sha256'].items():
        if sha256(ROOT/source) != pin:
            raise ValueError('CPU-prepared source changed: '+source)
    tests = ((PREP/'model_CPU_tests_v3.xml', 21), (PREP/'trainer_CPU_tests.xml', 12),
             (PREP/'probe_CPU_tests.xml', 10))
    for path, count in tests:
        passed_tests(path, count)
    accepted = ROOT/'configs/phase6/natural_context_contrast_comparison.json'
    old = json.loads(accepted.read_text())
    if sha256(accepted) != '70b87bf762f3225fd83f40d3bde301c13e5a4b4243372e541af1a1e38e88bc29' or old['parent'] != parity['original_parent']:
        raise ValueError('Same original learned parent and source required')
    if sha256(Path(old['parent']['path'])) != old['parent']['sha256']:
        raise ValueError('Original parent pin differs')
    c = dict(kind='owned_native_first_value_residual_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, timed_updates=32, continuous_updates=6, split_updates=[3, 3],
        capacity_shape=[48, 1024], candidate_parameters=10001164, main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0, Base_adopted=False, TEST_prepared=False,
        parent=old['parent'], proposal=ref(PREP/'proposal.json'), preparation=ref(PREP/'CPU_readiness.json'),
        parent_CPU_parity=ref(PREP/'actual_parent_CPU_parity.json'), accepted_config=ref(accepted),
        CPU_tests=[dict(**ref(path), expected_tests=count) for path, count in tests],
        tokenizer=ref(ROOT/old['tokenizer']), sources={path:sha256(ROOT/path) for path in SOURCES})
    assert_scope(c)
    parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
    current = build(c, parent)
    zero = host(current.state_dict())
    old_trainer = build(c, parent, legacy=True)
    original_zero = host(old_trainer.state_dict())
    if (current.spec['actual_unique_parameters'] != 10001164
            or not all(torch.equal(zero['model'][k], v) for k,v in original_zero['model'].items())
            or any(torch.count_nonzero(v) for k,v in zero['model'].items() if k.endswith('.value_alpha'))
            or zero['optimizer']['state'] or original_zero['optimizer']['state']
            or not all(equal_state(zero[k], original_zero[k]) for k in ('scheduler', 'RNG', 'sampler'))):
        raise ValueError('Declared12 zero scalars/original weights/fresh state/source differ')
    payload = json.loads((ROOT/'configs/phase6/base_parallel_residual_probe.json').read_text())['payload']
    if sha256(Path(payload['path'])) != payload['sha256']:
        raise ValueError('Existing accepted capacity payload changed')
    window = json.loads(Path(payload['path']).read_text())['window']
    if len(window['input_ids']) != 1024 or sum(i != -100 for i in window['target_ids']) != 512:
        raise ValueError('Existing native1024/512 stress window required')
    RUN.mkdir(parents=True, exist_ok=True)
    stress = RUN/'verification_shape_input.pt'
    torch.save(dict(window=window, role='previously_accepted_original_capacity_window_technical_only'), stress)
    c.update(capacity_payload=ref(stress), initial_weights_sha256=weights_digest(zero),
             CPU_wall_seconds=time.monotonic()-started)
    current.sampler.handle.close()
    old_trainer.sampler.handle.close()
    atomic_json(CONFIG, c)
    print(json.dumps(dict(status='owned_first_value_residual_technical_contract_frozen_no_GPU',
        native_parameters=10001152, candidate_parameters=10001164,
        original_weights_plus12zero_scalars_fresh_state_and_material_equal=True,
        CPU_wall_seconds=c['CPU_wall_seconds'])), flush=True)


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('Pinned owned technical config differs')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for key in ('parent', 'proposal', 'preparation', 'parent_CPU_parity', 'accepted_config', 'tokenizer', 'capacity_payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Owned probe reference changed: '+key)
    for source, pin in c['sources'].items():
        if sha256(ROOT/source) != pin:
            raise ValueError('Frozen probe source changed: '+source)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Frozen actual CPU evidence changed')
        passed_tests(row['path'], row['expected_tests'])
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('Existing owned job; inspect actual identity/result, never relaunch')
    return c


def run(pin):
    c = inspect(pin)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin,
        scientific_teacher_positions=0, cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json', job)
    started, result, updates, teachers = None, None, 0, 0

    def check(*args):
        if args or (started is not None and time.monotonic()-started > 180):
            raise TimeoutError('Owned CUDA180s ceiling exhausted; preserve terminal evidence')

    def beat(stage):
        check()
        job.update(stage=stage, heartbeat_at=now(), GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json', job)

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

    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM, check)
            signal.signal(signal.SIGINT, check)
            if not torch.cuda.is_available():
                raise RuntimeError('Actual local CUDA unavailable')
            job['status'] = 'running'
            memory = configure_resident_memory(0)
            parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
            full = build(c, parent, 'cuda')
            zero = host(full.state_dict())
            if weights_digest(zero) != c['initial_weights_sha256']:
                raise ValueError('Actual CUDA initialization differs')
            torch.save(zero, RUN/'verification_zero.pt')
            beat('continuous6')
            expected_history = [learn(full) for _ in range(6)]
            expected = host(full.state_dict())
            if not expected_history[-1]['value_coefficient_abs_max'] > 0:
                raise ValueError('Resume gate must exercise learned first-value coefficients')
            full.sampler.handle.close()
            del full
            clear()
            split = build(c, parent, 'cuda')
            actual = [learn(split) for _ in range(3)]
            split.save(RUN/'verification_split.pt')
            split.sampler.handle.close()
            del split
            clear()
            resumed = build(c, parent, 'cuda')
            resumed.load(RUN/'verification_split.pt')
            actual.extend(learn(resumed) for _ in range(3))
            strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds', 'data_wait_seconds')}
            if (not equal_state(expected, host(resumed.state_dict()))
                    or not equal_state([strip(r) for r in expected_history], [strip(r) for r in actual])):
                raise ValueError('Actual full CUDA state/history resume mismatch')
            shape = torch.load(c['capacity_payload']['path'], map_location='cpu', weights_only=False)
            before = weights_digest(host(resumed.state_dict()))
            beat('worst_CE48x1024')
            ce_capacity = worst_shape(resumed, shape['window'], 48)
            resumed.optimizer.zero_grad(set_to_none=True)
            if (weights_digest(host(resumed.state_dict())) != before
                    or ce_capacity['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']):
                raise ValueError('Maximum shape changed weights or exceeded resident allowance')
            beat('active_FP32_cached_vs_full')
            cache_gate = check_cache(resumed, shape['window'])
            if weights_digest(host(resumed.state_dict())) != before:
                raise ValueError('Technical cache check altered model weights')
            beat('steady32')
            timings = [learn(resumed) for _ in range(32)]
            if any(not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in timings):
                raise ValueError('Finite actual update durations required')
            resumed.save(RUN/'verification_final.pt')
            forecast = math.ceil(17698/32*sum(r['seconds'] for r in timings)*1.3+600)
            check()
            result = dict(status='complete', passed=True, config_sha256=pin, actual_identity=identity(),
                memory_policy=memory, CE_capacity=ce_capacity, active_cache_gate=cache_gate,
                all_state_and_history_resume_equal=True, actual_value_coefficients_learned=True,
                original_weights_plus_zero_scalars_equal=True, native_parameters=10001152, candidate_parameters=10001164,
                all32_timings=timings, scientific_forecast_seconds=forecast,
                verification_optimizer_updates=updates, verification_main_CE_positions=teachers,
                scientific_teacher_positions=0, DEV_opened=False, TEST_opened=False, Base_qualified=False, Base_adopted=False)
            resumed.sampler.handle.close()
            del resumed
            clear()
    except Exception as error:
        result = dict(status='failed', passed=False, config_sha256=pin, actual_identity=identity(),
            error_type=type(error).__name__, error=str(error), traceback=traceback.format_exc(),
            verification_optimizer_updates=updates, verification_main_CE_positions=teachers,
            scientific_teacher_positions=0, Base_qualified=False, Base_adopted=False)
    finally:
        elapsed = 0 if started is None else time.monotonic()-started
        if result is None:
            result = dict(status='failed', passed=False, error='No completed result', scientific_teacher_positions=0)
        if elapsed > 180:
            result.update(status='failed', passed=False, error='Owned GPU interval exceeded180s')
        result.update(GPU_occupancy_seconds=elapsed, cumulative_GPU_ledger_closed=True,
            science_budget_eligible=bool(result['passed'] and result['scientific_forecast_seconds']+elapsed <= 4800))
        job.update(status=result['status'], ended_at=now(), GPU_occupancy_seconds=elapsed,
            cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json', result)
        atomic_json(RUN/'job.json', job)
    print(json.dumps({k:result.get(k) for k in ('status', 'passed', 'GPU_occupancy_seconds',
        'verification_optimizer_updates', 'scientific_forecast_seconds', 'science_budget_eligible', 'error')}), flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'inspect', 'run'))
    parser.add_argument('--config-sha256')
    args = parser.parse_args()
    if args.action == 'prepare': prepare()
    elif args.action == 'inspect':
        inspect(args.config_sha256)
        print('Owned first-value residual preflight passed; no CUDA allocation')
    else: run(args.config_sha256)
