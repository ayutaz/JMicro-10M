"""Owned CUDA: independent operator, capacity before Adam, both-arm resume.

The closed mathematical runtime's GPU seconds remain charged. Do not change
geometry, source, gates or thresholds if this new explicit runtime fails.
Verification checkpoints stay WSL and never initialize scientific learning.
"""
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
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import sha256, now
from jmicro.forgetting_attention_fused import FusedForgettingModel, ARMS, IMPLEMENTATION, tiled_attention
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, rng_state, restore_rng
from forgetting_attention_fused_trainer import FusedForgettingTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity
from probe_context_likelihood import weights_digest, passed_tests

CONFIG = ROOT/'configs/phase6/forgetting_attention_fused_probe_20261015.json'
RUN = ROOT/'reports/phase6/forgetting-attention-fused-probe-20261015'


def assert_scope(c):
    expected = dict(kind='owned_forgetting_fused_CUDA_technical_v1', batch=48, seed=42,
        GPU_ceiling_seconds=180, prior_technical_GPU_seconds=1.2446600809926167, timed_updates_per_arm=32,
        continuous_updates_per_arm=6, split_updates=[3, 3], capacity_shape=[48, 1024],
        candidate_parameters=10014516, main_teachers_per_scientific_arm=100000000,
        maximum_new_GPU_seconds=4800, scientific_teacher_positions=0,
        native_function_parity_expected=False, attention_implementation=IMPLEMENTATION,
        capacity_before_any_optimizer_update=True, Base_adopted=False, TEST_prepared=False)
    expected.update(operator_lengths=[17, 64], operator_absolute_tolerance=1e-2,
                    operator_relative_tolerance=0., operator_all_QKV_log_gate_gradients=True,
                    verify_matched_initial_states=True)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k, v in expected.items()):
        raise ValueError('Exact owned both-arm180/4800/48x1024 scope required')


def forecast(timings):
    if set(timings) != set(ARMS) or any(len(timings[a]) != 32 or any(
            not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in timings[a]) for a in ARMS):
        raise ValueError('All32 finite measured timings for BOTH arms required')
    return math.ceil(sum(17698/32*sum(r['seconds'] for r in timings[a])*1.3+600 for a in ARMS))


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('Externally pinned technical config required')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for path, digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen probe source differs: '+path)
    for name in ('proposal', 'actual_CPU', 'accepted_config', 'accepted_shape_recipe', 'capacity_payload', 'tokenizer', 'prior_completion', 'source_preparation'):
        if sha256(Path(c[name]['path'])) != c[name]['sha256']:
            raise ValueError('Frozen accepted evidence differs: '+name)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Actual CPU evidence differs')
        passed_tests(row['path'], row['expected_tests'])
    actual = json.loads(Path(c['actual_CPU']['path']).read_text())
    if (not all(actual['checks'].values()) or actual['candidate_parameters'] != 10014516
            or actual['maximum_matched_initial_difference'] != 0
            or actual['original_parent'] != c['parent']):
        raise ValueError('Actual original parent matched/cache CPU gate required')
    prior = json.loads(Path(c['prior_completion']['path']).read_text())
    if (prior['cumulative_technical_GPU_seconds'] != c['prior_technical_GPU_seconds']
            or prior['original_technical_cap_seconds'] != 180 or prior['original_total_GPU_cap_seconds'] != 4800
            or not prior['cumulative_GPU_ledger_closed'] or not prior['implementation_condition_closed']
            or prior['verification_optimizer_updates'] != 0):
        raise ValueError('ALL prior spent GPU seconds and original unchanged cumulative caps required')
    accepted = json.loads(Path(c['accepted_config']['path']).read_text())
    stat = Path(c['parent']['path']).stat()
    if (accepted['parent'] != c['parent'] or c['parent']['sha256'] !=
            '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != c['parent_size'] or stat.st_mtime_ns != c['parent_mtime_ns']):
        raise ValueError('Previously hash-verified exact parent size/mtime required')
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('Existing one-shot owned job: inspect, never relaunch')
    return c


def build(c, parent, arm):
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    codec = Tokenizer(ROOT/old['tokenizer'])
    source = old['source_binding']
    sampler = OriginalTrainCorpusSampler(source['pool'], source['manifest_sha256'], codec, old['goals'], seed=42)
    if sampler.binding != source:
        raise ValueError('Existing accepted TRAIN identity differs')
    binding = dict(parent=c['parent'], source_binding=source, weights_role='verification_only',
                   protocol='forgetting_key_bias_owned_CUDA_both_arms')
    return FusedForgettingTrainer(parent, sampler, binding, batch=48, device='cuda', seed=42, arm=arm)


def capacity(model, window):
    model.train()
    model.zero_grad(set_to_none=True)
    before = weights_digest(dict(model=host(model.state_dict())))
    torch.cuda.reset_peak_memory_stats()
    ids = torch.tensor([window['input_ids']]*48, device='cuda')
    targets = torch.tensor([window['target_ids']]*48, device='cuda')
    if ids.shape != (48, 1024) or int(targets[0].ne(-100).sum()) != 512:
        raise ValueError('Existing accepted48x1024/512 capacity window required')
    with sdpa_kernel(SDPBackend.MATH), torch.autocast('cuda', dtype=torch.bfloat16):
        hidden = model.right_padded_hidden(ids)
        selected = targets.ne(-100)
        loss = F.cross_entropy(model.lm_head(hidden[selected]).float(), targets[selected])
        loss.backward()
    grad = model.clip_grad_norm(1., error_if_nonfinite=True)
    torch.cuda.synchronize()
    if (not torch.isfinite(loss) or not 0 < float(grad) < float('inf')
            or weights_digest(dict(model=host(model.state_dict()))) != before):
        raise ValueError('Finite complete max-shape backward and unchanged weights required')
    result = dict(passed=True, shape=[48, 1024], teachers=int(selected.sum()),
        physical_input_tokens=ids.numel(), loss=float(loss.detach()), gradient_norm=float(grad),
        peak_VRAM_bytes=torch.cuda.max_memory_allocated(), optimizer_updates=0,
        backend='pinned_author_Triton', gate_bias_precision='FP32', autocast='BF16')
    model.zero_grad(set_to_none=True)
    return result


def independent_attention(q, k_base, v_base, log_gates):
    """Explicit float32 matrix reference, causal gates and original GQA map."""
    groups = q.shape[1]//k_base.shape[1]
    k, v = k_base.repeat_interleave(groups, 1), v_base.repeat_interleave(groups, 1)
    cumulative = log_gates.cumsum(-1)
    scores = (q.float() @ k.float().transpose(-1, -2)) * q.shape[-1]**-.5
    scores = scores + cumulative[..., :, None]-cumulative[..., None, :]
    allowed = torch.ones(q.shape[2], q.shape[2], device=q.device, dtype=torch.bool).tril()
    probability = scores.masked_fill(~allowed, -torch.inf).softmax(-1)
    return (probability @ v.float()).to(q.dtype)


def operator_gate(beat):
    before, records = host(rng_state()), []
    try:
        for length in (17, 64):
            beat('independent_operator_BF16_all_gradients_T'+str(length))
            generator = torch.Generator().manual_seed(71+length)
            def fresh(shape, dtype):
                return (torch.randn(shape, generator=generator)*.3).to('cuda', dtype=dtype).requires_grad_()
            inputs = [fresh(shape, dtype) for shape, dtype in (
                ((2, 4, length, 64), torch.bfloat16), ((2, 2, length, 64), torch.bfloat16),
                ((2, 2, length, 64), torch.bfloat16), ((2, 4, length), torch.float32))]
            other = [t.detach().clone().requires_grad_() for t in inputs]
            q, k, v, gates = inputs
            logs = F.logsigmoid(gates)
            logs.retain_grad()
            expected_logs = F.logsigmoid(other[3])
            expected_logs.retain_grad()
            actual = tiled_attention(q, k.repeat_interleave(2, 1), v.repeat_interleave(2, 1), logs, .125)
            expected = independent_attention(*other[:3], expected_logs)
            dout = (torch.randn(actual.shape, generator=generator)*.1).to('cuda', dtype=torch.bfloat16)
            actual.backward(dout)
            expected.backward(dout)
            compared = [('output', actual, expected)]
            compared += [(name, a.grad, b.grad) for name, a, b in zip(
                ('Q', 'K_original_KV2', 'V_original_KV2', 'gate_logits'), inputs, other, strict=True)]
            compared.append(('FP32_log_gate', logs.grad, expected_logs.grad))
            row = dict(length=length, Q_heads=4, original_KV_heads=2, dimension=64,
                       absolute_tolerance=1e-2, relative_tolerance=0., maximum_differences={})
            for name, a, b in compared:
                if a is None or b is None or not torch.isfinite(a).all() or not torch.isfinite(b).all():
                    raise ValueError('Missing/nonfinite independent operator tensor: '+name)
                row['maximum_differences'][name] = float((a.float()-b.float()).abs().max())
            row['passed'] = all(torch.allclose(a, b, atol=1e-2, rtol=0.) for _, a, b in compared)
            records.append(row)
            if not row['passed']:
                raise ValueError('Original predeclared BF16 operator precision failed: '+json.dumps(row))
        return dict(passed=True, cases=records, RNG_restored=True,
                    scope='Small independent BF16 attention and ALL gradients only; not FP32 cache/update tolerance')
    finally:
        restore_rng(before)


def cache_gate(model, window):
    plain = [i for i in window['input_ids'] if 8 <= i < 4096]
    if len(plain) < 126:
        raise ValueError('Accepted same2x64 technical spans required')
    ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]], device='cuda')
    before, mode = host(rng_state()), model.training
    try:
        model.eval()
        with torch.no_grad(), sdpa_kernel(SDPBackend.MATH), torch.autocast('cuda', enabled=False):
            full = model(ids, use_cache=True)
            first = model(ids[:, :32], use_cache=True)
            last = model(ids[:, 32:], cache=first.cache, use_cache=True)
        log_close = all(torch.allclose(a, b, atol=3e-5, rtol=2e-5)
            for a, b in zip(full.cache.log_gates, last.cache.log_gates, strict=True))
        if (not torch.isfinite(full.logits).all() or not torch.isfinite(last.logits).all()
                or not log_close or not torch.allclose(full.logits[:, 32:], last.logits, atol=3e-5, rtol=2e-5)
                or not torch.equal(full.cache.positions, last.cache.positions)
                or not torch.equal(full.cache.valid, last.cache.valid)
                or not equal_state(before, host(rng_state()))):
            raise ValueError('Active actual-parent FP32 cached/full gate failed at ORIGINAL tolerances')
        return dict(passed=True, maximum_logit_difference=float((full.logits[:, 32:]-last.logits).abs().max()),
            absolute_tolerance=3e-5, relative_tolerance=2e-5, log_gate_history_passed=True,
            RNG_unchanged=True, optimizer_updates=0, dtype='FP32', backend='math')
    finally:
        model.train(mode)


def run(pin):
    c = inspect(pin)
    RUN.mkdir(parents=True, exist_ok=True)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin,
               scientific_teacher_positions=0, cumulative_GPU_ledger_closed=False,
               prior_technical_GPU_seconds=c['prior_technical_GPU_seconds'])
    atomic_json(RUN/'job.json', job)
    started, result, updates, teachers = None, None, 0, 0
    def check(*args):
        if args or (started is not None and time.monotonic()-started+c['prior_technical_GPU_seconds'] > 180):
            raise TimeoutError('Owned cumulative180s ceiling exhausted')
    def beat(stage):
        check()
        job.update(status='running', stage=stage, heartbeat_at=now(),
                   GPU_occupancy_seconds=time.monotonic()-started)
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
            memory = configure_resident_memory(0)
            job['memory_policy'] = memory
            parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
            operator_evidence = operator_gate(beat)
            job['independent_operator_equivalence'] = operator_evidence
            clear()
            original = JMicroModel(parent['model_config']).eval()
            original.load_state_dict(parent['model'], strict=True)
            window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
            model = FusedForgettingModel.from_native(original).to('cuda')
            beat('capacity_FIRST48x1024_no_Adam')
            maximum_shape = capacity(model, window)
            job['capacity'] = maximum_shape
            if maximum_shape['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']:
                raise ValueError('Max-shape exceeds measured resident allocator allowance')
            del model, original
            clear()
            summaries, timings, first_state, first_CE = {}, {}, None, None
            strip = lambda r: {k: v for k, v in r.items() if k not in ('seconds', 'data_wait_seconds')}
            for arm in ARMS:
                beat(arm+'_continuous6')
                full = build(c, parent, arm)
                initial = host(full.state_dict())
                if first_state is None:
                    first_state = initial
                elif not all(equal_state(first_state[k], initial[k]) for k in
                             ('model', 'optimizer', 'scheduler', 'RNG', 'sampler', 'counters')):
                    raise ValueError('BOTH actual CUDA arm initial numerical states must match')
                expected_rows = [learn(full) for _ in range(6)]
                if first_CE is None:
                    first_CE = expected_rows[0]['CE_loss']
                elif first_CE != expected_rows[0]['CE_loss']:
                    raise ValueError('Matched initial CUDA CE must be exactly equal')
                expected = host(full.state_dict())
                gate_tensors = {name: float(value.abs().max()) for name, value in expected['model'].items()
                                if '.forget_proj.' in name}
                if (len(gate_tensors) != 26 or any(not math.isfinite(v) for v in gate_tensors.values())
                        or (arm == 'learned_forget' and any(v <= 0 for v in gate_tensors.values()))
                        or (arm == 'static_half_forget' and any(v != 0 for v in gate_tensors.values()))):
                    raise ValueError('Actual gate weight AND bias activity for every layer required: '+arm)
                full.sampler.handle.close()
                del full
                clear()
                split = build(c, parent, arm)
                rows = [learn(split) for _ in range(3)]
                split.save(RUN/(arm+'_verification_split.pt'))
                split.sampler.handle.close()
                del split
                clear()
                resumed = build(c, parent, arm)
                resumed.load(RUN/(arm+'_verification_split.pt'))
                rows.extend(learn(resumed) for _ in range(3))
                if (not equal_state(expected, host(resumed.state_dict()))
                        or not equal_state([strip(r) for r in expected_rows], [strip(r) for r in rows])):
                    raise ValueError('Actual full typed state/history resume mismatch: '+arm)
                job.setdefault('resume_completed_arms', {})[arm] = True
                if ((arm == 'learned_forget') != (rows[-1]['forget_projection_abs_max'] > 0)):
                    raise ValueError('Actual learned/static gate activity differs: '+arm)
                beat(arm+'_active_FP32_cache')
                cache = cache_gate(resumed.model, window)
                beat(arm+'_steady32')
                timings[arm] = [learn(resumed) for _ in range(32)]
                resumed.save(RUN/(arm+'_verification_final.pt'))
                summaries[arm] = dict(full_state_history_resume_exact=True, active_cache=cache,
                    gate_projection_abs_max=timings[arm][-1]['forget_projection_abs_max'],
                    all_gate_weight_and_bias_tensors_after6=gate_tensors)
                resumed.sampler.handle.close()
                del resumed
                clear()
            check()
            result = dict(status='complete', passed=True, arms=summaries, all32_timings=timings,
                scientific_forecast_seconds=forecast(timings), capacity=maximum_shape, memory_policy=memory,
                independent_operator_equivalence=operator_evidence,
                both_arm_initial_numerical_state_and_first_CE_exact=True)
    except Exception as error:
        result = dict(status='failed', passed=False, error_type=type(error).__name__, error=str(error),
                      traceback=traceback.format_exc(), failed_stage=job.get('stage'),
                      memory_policy=job.get('memory_policy'),
                      independent_operator_equivalence=job.get('independent_operator_equivalence'),
                      capacity=job.get('capacity'), resume_completed_arms=job.get('resume_completed_arms'),
                      peak_VRAM_bytes=torch.cuda.max_memory_allocated() if torch.cuda.is_initialized() else None)
    finally:
        elapsed = 0 if started is None else time.monotonic()-started
        if result is None:
            result = dict(status='failed', passed=False, error='No terminal evidence')
        if elapsed+c['prior_technical_GPU_seconds'] > 180:
            result.update(status='failed', passed=False, error='Owned180s interval exceeded')
        result.update(config_sha256=pin, actual_identity=identity(), GPU_occupancy_seconds=elapsed,
            technical_GPU_seconds_including_prior=elapsed+c['prior_technical_GPU_seconds'], cumulative_GPU_ledger_closed=True,
            verification_optimizer_updates=updates, verification_main_CE_positions=teachers,
            scientific_teacher_positions=0, TEST_opened=False, DEV_opened=False,
            Base_qualified=False, Base_adopted=False,
            science_budget_eligible=bool(result['passed'] and result['scientific_forecast_seconds']+elapsed+c['prior_technical_GPU_seconds'] <= 4800))
        job.update(status=result['status'], ended_at=now(), GPU_occupancy_seconds=elapsed,
                   technical_GPU_seconds_including_prior=elapsed+c['prior_technical_GPU_seconds'],
                   cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json', result)
        atomic_json(RUN/'job.json', job)
    print(json.dumps({k: result.get(k) for k in ('status', 'passed', 'GPU_occupancy_seconds',
        'verification_optimizer_updates', 'science_budget_eligible', 'failed_stage', 'error')}), flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('inspect', 'run'))
    parser.add_argument('--config-sha256', required=True)
    args = parser.parse_args()
    if args.action == 'inspect':
        inspect(args.config_sha256)
        print('Owned both-arm CUDA preflight passed; no CUDA allocation')
    else:
        run(args.config_sha256)
