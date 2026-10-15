"""One CPU-only observation of saved verification3, NOT failed CUDA update6.

No optimizer, new training stream, held-out data, inference quality or CUDA.
Never rerun the closed owned probe to recover missing diagnostic measurements.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'scripts')]
import torch
from jmicro.forgetting_attention_fused import FusedForgettingModel
from forgetting_attention_fused_trainer import committed_state
from phase6_performance import alive

CONFIG = ROOT/'configs/phase6/forgetting_attention_fused_probe_20261015.json'
RUN = ROOT/'reports/phase6/forgetting-attention-fused-probe-20261015'
OUTPUT = ROOT/'reports/phase6/forgetting-attention-fused-preparation-20261015/CPU_active_checkpoint3_cache.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(CONFIG) != pin or OUTPUT.exists():
        raise ValueError('Fresh bounded CPU-only observation of pinned terminal run required')
    c = json.loads(CONFIG.read_text())
    result = json.loads((RUN/'result.json').read_text())
    if (alive(result['actual_identity']) or result['status'] != 'failed'
            or result['failed_stage'] != 'learned_forget_active_FP32_cache'
            or not result['cumulative_GPU_ledger_closed']):
        raise ValueError('Exited failed original cache guard required')
    for path, pin_value in c['sources'].items():
        if sha(ROOT/path) != pin_value:
            raise ValueError('Closed runtime source changed')
    checkpoint = RUN/'learned_forget_verification_split.pt'
    allowed = {checkpoint.resolve(), Path(c['capacity_payload']['path']).resolve()}
    protected = (ROOT/'reports', ROOT/'eval', ROOT/'artifacts', Path('/home/aihub_ubuntu/jmicro-data'))
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(folder) for folder in protected):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if writing and path == OUTPUT.resolve():
                return
            if writing or path not in allowed:
                raise ValueError('Outside fixed CPU checkpoint/input scope: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    checkpoint_sha = sha(checkpoint)
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    if (not committed_state(state) or state['binding']['weights_role'] != 'verification_only'
            or state['counters']['update'] != 3 or state['spec']['forgetting_arm'] != 'learned_forget'):
        raise ValueError('Actual complete verification-only update3 required')
    if sha(c['capacity_payload']['path']) != c['capacity_payload']['sha256']:
        raise ValueError('Existing technical input differs')
    window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
    plain = [i for i in window['input_ids'] if 8 <= i < 4096]
    ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]])
    torch.set_num_threads(2)
    model = FusedForgettingModel(state['model_config']).eval()
    model.load_state_dict(state['model'])
    with torch.no_grad():
        full = model(ids, use_cache=True)
        prefix = model(ids[:, :32], use_cache=True)
        last = model(ids[:, 32:], cache=prefix.cache, use_cache=True)
    checks = dict(finite_logits=bool(torch.isfinite(full.logits).all() and torch.isfinite(last.logits).all()),
        logits_within_original_combined_tolerance=torch.allclose(full.logits[:, 32:], last.logits, atol=3e-5, rtol=2e-5),
        log_gate_history_within_original_tolerance=all(torch.allclose(a, b, atol=3e-5, rtol=2e-5)
            for a, b in zip(full.cache.log_gates, last.cache.log_gates, strict=True)),
        positions_exact=torch.equal(full.cache.positions, last.cache.positions),
        validity_exact=torch.equal(full.cache.valid, last.cache.valid), CUDA_initialized=torch.cuda.is_initialized())
    gate_activity = {name: float(value.abs().max()) for name, value in state['model'].items()
                     if '.forget_proj.' in name}
    elapsed = time.monotonic()-started
    if elapsed > 30 or checks['CUDA_initialized'] or not checks['finite_logits']:
        raise ValueError('Finite bounded CPU-only observation failed')
    record = dict(status='saved_verification3_CPU_cache_observation_complete',
        created_at=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
        config_sha256=pin, checkpoint_sha256=checkpoint_sha, checkpoint_update=3,
        checkpoint_supervised_positions=state['counters']['supervised_tokens'], checks=checks,
        maximum_logit_difference=float((full.logits[:, 32:]-last.logits).abs().max()),
        outside_original_logit_tolerance=int((~torch.isclose(full.logits[:, 32:], last.logits, atol=3e-5, rtol=2e-5)).sum()),
        maximum_log_gate_difference=max(float((a-b).abs().max())
            for a, b in zip(full.cache.log_gates, last.cache.log_gates, strict=True)),
        gate_tensor_abs_max=gate_activity, CPU_wall_seconds=elapsed,
        protected_read_paths=sorted(set(reads)), optimizer_updates=0, new_GPU_seconds=0,
        new_TRAIN_stream_opened=False, DEV_opened=False, TEST_opened=False, model_weights_saved=False,
        limitations='CPU update3 only. Failed guard was CUDA update6; its specific failing subcheck/maxima were not retained. This observation neither recreates that exact endpoint nor diagnoses a unique arithmetic cause or validates any repair.')
    OUTPUT.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: record[k] for k in ('status', 'CPU_wall_seconds', 'checks', 'maximum_logit_difference',
        'outside_original_logit_tolerance', 'maximum_log_gate_difference')}), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config-sha256', required=True)
    args = parser.parse_args()
    run(args.config_sha256)
