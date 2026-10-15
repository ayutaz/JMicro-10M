"""One owned read-only CUDA observation of saved verification3, not update6.

Original closed learning/probe is never resumed. All subchecks are observations,
not a new acceptance policy; no optimizer, training stream, or held-out input.
"""
import argparse
import json
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
from jmicro.experiment import now, sha256
from jmicro.forgetting_attention_fused import FusedForgettingModel
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json, gpu_lock, rng_state
from forgetting_attention_fused_trainer import committed_state
from natural_context_contrast_memory import configure_resident_memory
from natural_context_contrast_trainer import host
from phase6_performance import identity, alive
from probe_context_likelihood import passed_tests

CONFIG = ROOT/'configs/phase6/forgetting_attention_fused_cache_diagnostic_20261015.json'
RUN = ROOT/'reports/phase6/forgetting-attention-fused-cache-diagnostic-20261015'


def assert_scope(c):
    expected = dict(kind='owned_readonly_saved_fused3_FP32_cache_observation_v1',
        read_only=True, checkpoint_update=3, input_shape=[2, 64], cache_split=[32, 32],
        dtype='FP32', backend='MATH', absolute_tolerance=3e-5, relative_tolerance=2e-5,
        new_GPU_ceiling_seconds=30, original_technical_cap_seconds=180,
        original_total_GPU_cap_seconds=4800, prior_technical_GPU_seconds=12.881095835007727,
        optimizer_updates=0, scientific_teacher_positions=0, TEST_opened=False,
        recreate_failed_update6=False)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k, v in expected.items()):
        raise ValueError('Exact read-only saved3 original-precision cumulative scope required')


def observations(full, cached, rng_equal):
    n = cached.logits.shape[1]
    a, b = full.logits[:, -n:], cached.logits
    if a.shape != b.shape or len(full.cache.log_gates) != len(cached.cache.log_gates):
        raise ValueError('Matching full/suffix output and complete cache layers required')
    finite = bool(torch.isfinite(a).all() and torch.isfinite(b).all())
    close = torch.isclose(a, b, atol=3e-5, rtol=2e-5)
    logs = [dict(layer=i, maximum_difference=float((x-y).abs().max()),
        within_original_tolerance=torch.allclose(x, y, atol=3e-5, rtol=2e-5))
        for i, (x, y) in enumerate(zip(full.cache.log_gates, cached.cache.log_gates, strict=True))]
    checks = dict(finite_logits=finite, logits_within_original_tolerance=bool(close.all()),
        log_gate_history_within_original_tolerance=all(r['within_original_tolerance'] for r in logs),
        positions_exact=torch.equal(full.cache.positions, cached.cache.positions),
        validity_exact=torch.equal(full.cache.valid, cached.cache.valid), RNG_unchanged=bool(rng_equal))
    bad = []
    for index in (~close).nonzero()[:8].cpu().tolist():
        key = tuple(index)
        bad.append(dict(index=index, full_value=float(a[key]), cached_value=float(b[key]),
            absolute_difference=float((a[key]-b[key]).abs()),
            allowed_error_using_cached_reference=float(3e-5+2e-5*b[key].abs())))
    kv = [dict(layer=i, K_maximum_difference=float((x[0]-y[0]).abs().max()),
        V_maximum_difference=float((x[1]-y[1]).abs().max()))
        for i, (x, y) in enumerate(zip(full.cache.layers, cached.cache.layers, strict=True))]
    return dict(original_guard_subchecks=checks, all_original_guards_passed=all(checks.values()),
        maximum_logit_difference=float((a-b).abs().max()), outside_original_logit_tolerance=int((~close).sum()),
        first_eight_outside_logits=bad, layer_log_gate_observations=logs,
        descriptive_KV_differences_not_additional_gates=kv)


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('Pinned read-only diagnostic config required')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for path, digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen diagnostic/runtime source changed: '+path)
    for name in ('prior_completion', 'CPU_observation', 'checkpoint', 'capacity_payload'):
        if sha256(Path(c[name]['path'])) != c[name]['sha256']:
            raise ValueError('Pinned diagnostic evidence changed: '+name)
    prior = json.loads(Path(c['prior_completion']['path']).read_text())
    if (alive(prior['actual_identity']) or not prior['implementation_condition_closed']
            or not prior['cumulative_GPU_ledger_closed']
            or prior['cumulative_technical_GPU_seconds'] != c['prior_technical_GPU_seconds']
            or prior['original_technical_cap_seconds'] != 180 or prior['original_total_GPU_cap_seconds'] != 4800):
        raise ValueError('Exited closed prior job and ALL original consumed budget required')
    for test in c['CPU_tests']:
        if sha256(Path(test['path'])) != test['sha256']:
            raise ValueError('CPU scope evidence changed')
        passed_tests(test['path'], test['expected_tests'])
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot diagnostic exists; inspect actual identity/result, never relaunch')
    return c


def run(pin):
    c = inspect(pin)
    RUN.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin,
        prior_technical_GPU_seconds=c['prior_technical_GPU_seconds'], cumulative_GPU_ledger_closed=False,
        optimizer_updates=0, scientific_teacher_positions=0)
    atomic_json(RUN/'job.json', job)
    started, result = None, None
    def check(*args):
        elapsed = 0 if started is None else time.monotonic()-started
        if args or elapsed > 30 or elapsed+c['prior_technical_GPU_seconds'] > 180:
            raise TimeoutError('Original cumulative180 or owned read-only30s ceiling exceeded')
    protected = (ROOT/'reports', ROOT/'eval', ROOT/'artifacts', Path('/home/aihub_ubuntu/jmicro-data'))
    allowed_reads = {Path(c[k]['path']).resolve() for k in ('checkpoint', 'capacity_payload')}
    lock = Path('/home/aihub_ubuntu/jmicro-data/gpu.lock')
    writes = {lock, *[RUN/name for name in ('job.json', 'job.json.tmp', 'result.json', 'result.json.tmp')]}
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(folder) for folder in protected):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if path in writes and (writing or path == lock):
                return
            if writing or path not in allowed_reads:
                raise ValueError('Outside read-only checkpoint/fixed technical input scope: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM, check)
            signal.signal(signal.SIGINT, check)
            memory = configure_resident_memory(0)
            state = torch.load(c['checkpoint']['path'], map_location='cpu', weights_only=False)
            if (not committed_state(state) or state['binding']['weights_role'] != 'verification_only'
                    or state['counters']['update'] != 3 or state['spec']['forgetting_arm'] != 'learned_forget'):
                raise ValueError('Complete actual verification-only saved update3 required')
            window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
            plain = [i for i in window['input_ids'] if 8 <= i < 4096]
            if len(plain) < 126:
                raise ValueError('Same accepted two63-token spans required')
            ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]], device='cuda')
            model = FusedForgettingModel(state['model_config']).to('cuda').eval()
            model.load_state_dict({k: v.to('cuda') for k, v in state['model'].items()})
            before = host(rng_state())
            job.update(status='running', stage='readonly_saved3_FP32_full_and32plus32', heartbeat_at=now())
            atomic_json(RUN/'job.json', job)
            with torch.no_grad(), sdpa_kernel(SDPBackend.MATH), torch.autocast('cuda', enabled=False):
                full = model(ids, use_cache=True)
                prefix = model(ids[:, :32], use_cache=True)
                cached = model(ids[:, 32:], cache=prefix.cache, use_cache=True)
            metrics = observations(full, cached, equal_state(before, host(rng_state())))
            torch.cuda.synchronize()
            check()
            result = dict(status='complete', observation_complete=True, observation=metrics,
                memory_policy=memory, checkpoint_update=3, checkpoint_sha256=c['checkpoint']['sha256'],
                model_parameter_dtypes=sorted({str(p.dtype) for p in model.parameters()}), TF32_enabled=False,
                CUBLAS_WORKSPACE_CONFIG=os.environ.get('CUBLAS_WORKSPACE_CONFIG'),
                limits='CUDA update3 observation only, NOT failed update6 reproduction, repair or quality evidence.')
    except Exception as error:
        result = dict(status='failed', observation_complete=False, error_type=type(error).__name__,
                      error=str(error), traceback=traceback.format_exc())
    finally:
        elapsed = 0 if started is None else time.monotonic()-started
        if result is None:
            result = dict(status='failed', observation_complete=False, error='No diagnostic evidence')
        if elapsed > 30 or elapsed+c['prior_technical_GPU_seconds'] > 180:
            result.update(status='failed', observation_complete=False, error='Original owned deadline exceeded')
        result.update(config_sha256=pin, actual_identity=identity(), GPU_occupancy_seconds=elapsed,
            cumulative_technical_GPU_seconds=elapsed+c['prior_technical_GPU_seconds'],
            cumulative_GPU_ledger_closed=True, optimizer_updates=0, scientific_teacher_positions=0,
            protected_read_paths=sorted(set(reads)), new_TRAIN_stream_opened=False,
            DEV_opened=False, TEST_opened=False, model_weights_saved=False, Base_qualified=False)
        job.update(status=result['status'], ended_at=now(), GPU_occupancy_seconds=elapsed,
                   cumulative_technical_GPU_seconds=result['cumulative_technical_GPU_seconds'],
                   cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json', result)
        atomic_json(RUN/'job.json', job)
    print(json.dumps({k: result.get(k) for k in ('status', 'observation_complete', 'GPU_occupancy_seconds',
        'cumulative_technical_GPU_seconds', 'error')}), flush=True)
    if not result['observation_complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('inspect', 'run'))
    parser.add_argument('--config-sha256', required=True)
    args = parser.parse_args()
    if args.action == 'inspect':
        inspect(args.config_sha256)
        print('Read-only saved3 diagnostic preflight passed; no CUDA allocation')
    else:
        run(args.config_sha256)
