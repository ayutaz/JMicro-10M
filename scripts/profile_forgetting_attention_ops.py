"""One instrumented saved6 forward/backward, no optimizer or new TRAIN stream."""
import argparse
from collections import defaultdict
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
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import now, sha256
from jmicro.forgetting_attention_shared_rope import SharedRopeForgettingModel, IMPLEMENTATION
from jmicro.phase5 import equal_state
from jmicro.training import atomic_json, gpu_lock, rng_state, restore_rng
from forgetting_attention_shared_rope_trainer import committed_state
from natural_context_contrast_memory import configure_resident_memory
from natural_context_contrast_trainer import host
from phase6_performance import identity, alive
from probe_context_likelihood import weights_digest, passed_tests

CONFIG = ROOT/'configs/phase6/forgetting_attention_operation_profile_20261015.json'
RUN = ROOT/'reports/phase6/forgetting-attention-operation-profile-20261015'


def assert_scope(c):
    expected = dict(kind='owned_single_saved6_operator_profile_no_optimizer_v1',
        checkpoint_update=6, input_shape=[48, 1024], labels_per_row=512, profiled_steps=1,
        warmup_steps=0, optimizer_updates=0, scientific_teacher_positions=0,
        dtype='BF16', attention_implementation=IMPLEMENTATION,
        new_GPU_ceiling_seconds=30, prior_technical_GPU_seconds=70.04953129705973,
        original_technical_cap_seconds=180, original_total_GPU_cap_seconds=4800,
        new_TRAIN_stream_opened=False, DEV_opened=False, TEST_opened=False,
        model_weights_saved=False, science_forecast=False)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k, v in expected.items()):
        raise ValueError('Exact single no-optimizer/no-new-data/profile-only original cumulative scope required')


def summarize(events, averages):
    operators = []
    for r in averages:
        row = dict(name=r.key, count=int(r.count), CPU_self_us=float(r.self_cpu_time_total),
            CPU_inclusive_us=float(r.cpu_time_total), CUDA_self_us=float(r.self_device_time_total),
            CUDA_inclusive_us=float(r.device_time_total), input_shapes=r.input_shapes)
        if row['count'] <= 0 or any(not math.isfinite(row[k]) for k in
            ('CPU_self_us', 'CPU_inclusive_us', 'CUDA_self_us', 'CUDA_inclusive_us')):
            raise ValueError('Finite raw profiler operator durations/count required')
        operators.append(row)
    kernels = defaultdict(lambda: dict(count=0, total_us=0.))
    for event in events:
        if str(event.device_type) != 'DeviceType.CUDA':
            continue
        duration = float(event.time_range.elapsed_us())
        if not math.isfinite(duration) or duration < 0:
            raise ValueError('Finite nonnegative actual CUDA event duration required')
        kernels[event.name]['count'] += 1
        kernels[event.name]['total_us'] += duration
    if not kernels:
        raise ValueError('No actual CUDA kernel events collected; no device timing inference allowed')
    kernel_rows = sorted((dict(name=k, **v) for k, v in kernels.items()), key=lambda r: -r['total_us'])
    return dict(CPU_operator_self_sum_us=sum(r['CPU_self_us'] for r in operators),
        CPU_negative_self_time_rows=sum(r['CPU_self_us'] < 0 for r in operators),
        operators_by_CPU_self=sorted(operators, key=lambda r: -r['CPU_self_us'])[:120],
        operators_by_inclusive_CUDA=sorted(operators, key=lambda r: -r['CUDA_inclusive_us'])[:120],
        CUDA_event_count=sum(r['count'] for r in kernel_rows),
        CUDA_event_duration_sum_us=sum(r['total_us'] for r in kernel_rows), CUDA_events=kernel_rows,
        limits='Instrumented ONE max-shape step, not steady training speed or science forecast. Inclusive operator/device totals overlap. CUDA event duration sum is reported separately, not added to operator totals.')


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('Externally pinned one-shot profile config required')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for path, digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen profile source differs: '+path)
    for key in ('proposal', 'prior_completion', 'checkpoint', 'capacity_payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned profile evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Profile CPU scope/summary evidence differs')
        passed_tests(row['path'], row['expected_tests'])
    prior = json.loads(Path(c['prior_completion']['path']).read_text())
    if (alive(prior['actual_identity']) or not prior['implementation_condition_closed']
            or not prior['cumulative_GPU_ledger_closed'] or prior['science_budget_eligible']
            or prior['cumulative_technical_GPU_seconds'] != c['prior_technical_GPU_seconds']
            or prior['original_technical_cap_seconds'] != 180 or prior['original_total_GPU_cap_seconds'] != 4800):
        raise ValueError('Exited closed prior source and ALL cumulative consumed seconds required')
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot profile already exists; inspect its actual process, never relaunch')
    return c


def run(pin):
    c = inspect(pin)
    RUN.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin,
        optimizer_updates=0, scientific_teacher_positions=0, cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json', job)
    started = result = before = None
    def check(*args):
        elapsed = 0 if started is None else time.monotonic()-started
        if args or elapsed > 30 or elapsed+c['prior_technical_GPU_seconds'] > 180:
            raise TimeoutError('Single profile30 or original cumulative180 exceeded')
    protected = (ROOT/'reports', ROOT/'eval', ROOT/'artifacts', Path('/home/aihub_ubuntu/jmicro-data'))
    allowed = {Path(c[k]['path']).resolve() for k in ('checkpoint', 'capacity_payload')}
    lock = Path('/home/aihub_ubuntu/jmicro-data/gpu.lock')
    writes = {lock, *[RUN/name for name in ('job.json', 'job.json.tmp', 'result.json', 'result.json.tmp')]}
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in protected):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if path in writes and (writing or path == lock):
                return
            if writing or path not in allowed:
                raise ValueError('Outside saved6/fixed-window profile scope: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM, check)
            signal.signal(signal.SIGINT, check)
            signal.signal(signal.SIGALRM, check)
            signal.setitimer(signal.ITIMER_REAL, 30)
            memory = configure_resident_memory(0)
            state = torch.load(c['checkpoint']['path'], map_location='cpu', weights_only=False)
            if (not committed_state(state) or state['binding']['weights_role'] != 'verification_only'
                    or state['counters']['update'] != 6 or state['spec']['forgetting_arm'] != 'learned_forget'):
                raise ValueError('Actual complete verification-only learned6 required')
            model = SharedRopeForgettingModel(state['model_config']).to('cuda').train()
            model.load_state_dict(state['model'])
            window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
            ids = torch.tensor([window['input_ids']]*48, device='cuda')
            targets = torch.tensor([window['target_ids']]*48, device='cuda')
            if list(ids.shape) != [48,1024] or int(targets[0].ne(-100).sum()) != 512:
                raise ValueError('Same original48x1024/512-label technical window required')
            before = host(rng_state())
            digest = weights_digest(dict(model=host(model.state_dict())))
            model.zero_grad(set_to_none=True)
            torch.cuda.synchronize()
            job.update(status='running', stage='single_instrumented_forward_backward', heartbeat_at=now())
            atomic_json(RUN/'job.json', job)
            measured = time.monotonic()
            with torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU,
                    torch.profiler.ProfilerActivity.CUDA], record_shapes=True,
                    profile_memory=False, with_stack=False) as prof:
                with torch.profiler.record_function('jmicro_original_forward_backward_once'):
                    with sdpa_kernel(SDPBackend.MATH), torch.autocast('cuda', dtype=torch.bfloat16):
                        hidden = model.right_padded_hidden(ids)
                        selected = targets.ne(-100)
                        loss = F.cross_entropy(model.lm_head(hidden[selected]).float(), targets[selected])
                        loss.backward()
                    torch.cuda.synchronize()
            instrumented_wall = time.monotonic()-measured
            metrics = summarize(prof.events(), prof.key_averages(group_by_input_shape=True))
            unchanged = digest == weights_digest(dict(model=host(model.state_dict())))
            finite = bool(torch.isfinite(loss) and all(p.grad is not None and torch.isfinite(p.grad).all()
                                                      for p in model.parameters()))
            rng_equal = equal_state(before, host(rng_state()))
            check()
            if not unchanged or not finite:
                raise ValueError('Unchanged weights and finite original backward required')
            result = dict(status='complete', observation_complete=True, profile=metrics,
                instrumented_wall_seconds=instrumented_wall, loss=float(loss.detach()),
                weights_unchanged=unchanged, all_gradients_finite=finite,
                RNG_unchanged_before_restore=rng_equal, memory_policy=memory,
                profiled_steps=1, checkpoint_update=6, science_forecast=False,
                limits='Single maximum shape with instrumentation; not original step timing, unique causal bottleneck, quality or new science eligibility.')
    except Exception as error:
        result = dict(status='failed', observation_complete=False, error_type=type(error).__name__,
                      error=str(error), traceback=traceback.format_exc())
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if before is not None:
            restore_rng(before)
        elapsed = 0 if started is None else time.monotonic()-started
        if result is None:
            result = dict(status='failed', observation_complete=False, error='No profile evidence')
        if elapsed > 30 or elapsed+c['prior_technical_GPU_seconds'] > 180:
            result.update(status='failed', observation_complete=False, error='Original profile deadline exceeded')
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
    print(json.dumps({k: result.get(k) for k in ('status', 'observation_complete',
        'GPU_occupancy_seconds', 'cumulative_technical_GPU_seconds', 'error')}), flush=True)
    if not result['observation_complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('inspect', 'run'))
    parser.add_argument('--config-sha256', required=True)
    args = parser.parse_args()
    if args.action == 'inspect':
        inspect(args.config_sha256)
        print('Single profile preflight passed; no CUDA allocation')
    else:
        run(args.config_sha256)
