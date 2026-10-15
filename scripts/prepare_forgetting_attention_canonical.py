"""Bounded actual-parent matched conversion, no learning/new corpus/DEV/TEST."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'scripts')]
import torch
from jmicro.forgetting_attention_canonical import CanonicalForgettingModel as ForgettingModel, TAG, native_config
from jmicro.model import JMicroModel


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Externally pinned CPU-only conversion contract required')
    c = json.loads(Path(contract).read_text())
    if (c['kind'] != 'actual_native_parent_forgetting_canonical_CPU_v1'
            or c['CPU_wall_ceiling_seconds'] != 30 or c['native_parameters'] != 10001152
            or c['candidate_parameters'] != 10014516 or c['input_shape'] != [2, 64]
            or c['cache_split'] != [32, 32] or c['GPU_seconds'] != 0
            or c['optimizer_updates'] != 0 or c['native_function_parity_expected'] is not False
            or c['cache_atol'] != 3e-5 or c['cache_rtol'] != 2e-5):
        raise ValueError('Exact changed-function matched CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot CPU receipt required')
    for path, expected in c['sources'].items():
        if sha(ROOT/path) != expected:
            raise ValueError('Prepared source differs: '+path)
    for key in ('proposal', 'design', 'model_tests', 'accepted_parent_recipe', 'accepted_shape_recipe'):
        if sha(ROOT/c[key]['path']) != c[key]['sha256']:
            raise ValueError('Pinned metadata differs: '+key)
    for key, count in (('model_tests', 23),):
        suites = list(ET.parse(ROOT/c[key]['path']).getroot().iter('testsuite'))
        if (sum(int(s.attrib.get('tests', 0)) for s in suites) != count
                or any(int(s.attrib.get(k, 0)) for s in suites for k in ('failures', 'errors', 'skipped'))):
            raise ValueError('Actual complete CPU tests required: '+key)
    accepted = json.loads((ROOT/c['accepted_parent_recipe']['path']).read_text())
    parent = Path(accepted['parent']['path'])
    if accepted['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Original native10B parent required')
    stat = parent.stat()
    if stat.st_size != accepted['parent_size'] or stat.st_mtime_ns != accepted['parent_mtime_ns']:
        raise ValueError('Previously verified parent size/mtime differs')
    payload = json.loads((ROOT/c['accepted_shape_recipe']['path']).read_text())['payload']
    allowed = {str(parent.resolve()), str(Path(payload['path']).resolve())}
    roots = (ROOT/'reports', ROOT/'eval', ROOT/'artifacts', Path('/home/aihub_ubuntu/jmicro-data'))
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in roots):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if path == output.resolve() and writing:
                return
            if writing or str(path) not in allowed:
                raise ValueError('Protected path outside bounded CPU contract: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    if sha(Path(payload['path'])) != payload['sha256']:
        raise ValueError('Accepted technical input differs')
    shape = json.loads(Path(payload['path']).read_text())['window']
    if len(shape['input_ids']) != 1024 or sum(i != -100 for i in shape['target_ids']) != 512:
        raise ValueError('Accepted technical1024/512 window required')
    plain = [i for i in shape['input_ids'] if 8 <= i < 4096]
    if len(plain) < 126:
        raise ValueError('Two existing plain63-token spans required')
    ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]])
    torch.set_num_threads(2)
    saved = torch.load(parent, map_location='cpu', weights_only=False)
    original = JMicroModel(saved['model_config']).eval()
    original.load_state_dict(saved['model'], strict=True)
    rng = torch.get_rng_state().clone()
    candidate = ForgettingModel.from_native(original)
    control = ForgettingModel.from_native(original, 'static_half_forget')
    old_state, a_state, b_state = original.state_dict(), candidate.state_dict(), control.state_dict()
    checks = dict(native_parameters=sum(p.numel() for p in original.parameters()) == 10001152,
        both_candidate_parameters=all(sum(p.numel() for p in m.parameters()) == 10014516 for m in (candidate, control)),
        both_total_trainable_within_budget=all(9500000 <= sum(p.numel() for p in m.parameters() if p.requires_grad) <= 10100000 for m in (candidate, control)),
        both_original_weights_exact=all(torch.equal(a_state[k], v) and torch.equal(b_state[k], v) for k, v in old_state.items()),
        only_declared_gate_coordinates=set(a_state)-set(old_state) == {
            f'model.layers.{i}.self_attn.forget_proj.{part}' for i in range(13) for part in ('weight', 'bias')},
        both_zero_gate_coordinates=all(torch.count_nonzero(v) == 0 for k, v in a_state.items() if '.forget_proj.' in k),
        both_base_config_exact=all(native_config(m.config) == original.config for m in (candidate, control)),
        tied_vocabulary=all(m.lm_head.weight is m.model.embed_tokens.weight for m in (candidate, control)),
        conversion_RNG_exact=torch.equal(rng, torch.get_rng_state()))
    with torch.no_grad():
        native_logits = original(ids).logits
        a, b = candidate(ids, use_cache=True), control(ids, use_cache=True)
        checks['matched_initial_logits_bitwise_equal'] = torch.equal(a.logits, b.logits)
        checks['explicitly_different_native_function'] = not torch.equal(a.logits, native_logits)
        checks['all_logits_finite'] = all(torch.isfinite(v).all() for v in (native_logits, a.logits, b.logits))
        differences = []
        for model, full in ((candidate, a), (control, b)):
            prefix = model(ids[:, :32], use_cache=True)
            suffix = model(ids[:, 32:], cache=prefix.cache, use_cache=True)
            differences.append(float((suffix.logits-full.logits[:, 32:]).abs().max()))
            checks[model.config[TAG]['arm']+'_cache_logits_within_declared_precision'] = torch.allclose(
                suffix.logits, full.logits[:, 32:], atol=c['cache_atol'], rtol=c['cache_rtol'])
            checks[model.config[TAG]['arm']+'_cache_logs_and_positions_exact'] = (
                all(torch.equal(u, v) for u, v in zip(suffix.cache.log_gates, full.cache.log_gates, strict=True))
                and torch.equal(suffix.cache.positions, full.cache.positions))
    checks = {key: bool(value) for key, value in checks.items()}
    elapsed = time.monotonic()-started
    if (not all(checks.values()) or elapsed > c['CPU_wall_ceiling_seconds']
            or stat.st_size != parent.stat().st_size or stat.st_mtime_ns != parent.stat().st_mtime_ns):
        print(json.dumps(dict(status='failed_actual_parent_CPU_diagnostic', checks=checks,
            CPU_wall_seconds=elapsed, maximum_cache_differences=differences,
            maximum_native_function_difference=float((a.logits-native_logits).abs().max()),
            native_function_parity_expected=False)), flush=True)
        raise ValueError('Actual parent matched conversion/cache/budget failed: '+repr(checks))
    receipt = dict(status='actual_native10M_canonical_adapter_CPU_conversion_verified',
        created_at=datetime.now(timezone.utc).isoformat(), contract_sha256=sha(contract), checks=checks,
        original_parent=accepted['parent'], parent_size=stat.st_size, parent_mtime_ns=stat.st_mtime_ns,
        parent_identity_policy='Previously verified hash plus exact size/mtime; not a new full weight rehash.',
        original_parameters=10001152, candidate_parameters=10014516, input_shape=list(ids.shape),
        maximum_native_function_difference=float((a.logits-native_logits).abs().max()),
        maximum_matched_initial_difference=float((a.logits-b.logits).abs().max()),
        maximum_cache_differences=differences, CPU_wall_seconds=elapsed,
        checkpoint_and_payload_read_paths=sorted(set(reads)), optimizer_updates=0, new_GPU_seconds=0,
        DEV_opened=False, TEST_opened=False, new_dataset_prepared=False, model_weights_saved=False,
        scientific_contract_frozen=False, Base_qualified=False, full_four_item_goal_complete=False,
        limits='Actual learned-parent CPU conversion only. Initial gates .5 change native function. No learning/CUDA/quality/independent seed/fullDEV/final TEST evidence.')
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: receipt[k] for k in ('status', 'candidate_parameters', 'CPU_wall_seconds',
        'maximum_matched_initial_difference', 'maximum_native_function_difference', 'maximum_cache_differences')}), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
