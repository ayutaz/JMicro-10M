"""One CPU conversion parity gate on the actual frozen10M parent.

Read an existing accepted technical input only. No corpus, DEV/TEST, tokenizer
training, optimizer, model-quality evaluation, CUDA or saved model weights.
"""
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
from jmicro.independent_map import IndependentMapModel, TAG, native_config
from jmicro.model import JMicroModel


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Externally pinned CPU-only conversion contract required')
    c = json.loads(Path(contract).read_text())
    if (c['kind'] != 'actual_native_parent_independent_map_CPU_parity_v1'
            or c['CPU_wall_ceiling_seconds'] != 30 or c['native_parameters'] != 10001152
            or c['candidate_parameters'] != 10067764 or c['input_shape'] != [2, 64]
            or c['cache_split'] != [32, 32] or c['GPU_seconds'] != 0
            or c['optimizer_updates'] != 0 or c['active_raw_coefficient'] != .25
            or c['cache_atol'] != 3e-5 or c['cache_rtol'] != 2e-5):
        raise ValueError('Exact changed-architecture CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot CPU receipt required')
    for path, pin_value in c['sources'].items():
        if sha(ROOT/path) != pin_value:
            raise ValueError('CPU-prepared implementation differs: '+path)
    for key in ('proposal', 'model_tests', 'accepted_parent_recipe', 'accepted_shape_recipe'):
        if sha(ROOT/c[key]['path']) != c[key]['sha256']:
            raise ValueError('Existing pinned metadata differs: '+key)
    suites = list(ET.parse(ROOT/c['model_tests']['path']).getroot().iter('testsuite'))
    if (sum(int(s.attrib.get('tests', 0)) for s in suites) != 27
            or any(int(s.attrib.get(k, 0)) for s in suites for k in ('failures', 'errors', 'skipped'))):
        raise ValueError('All27 actual CPU architecture checks required')
    accepted = json.loads((ROOT/c['accepted_parent_recipe']['path']).read_text())
    parent = Path(accepted['parent']['path'])
    if accepted['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Original learned10B native parent required')
    stat = parent.stat()
    if (stat.st_size != accepted['parent_size'] or stat.st_mtime_ns != accepted['parent_mtime_ns']):
        raise ValueError('Previously hash-verified original parent identity differs; no restore fallback')
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
            if str(path) not in allowed or writing:
                raise ValueError('Forbidden model/data/DEV/TEST open: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    if sha(Path(payload['path'])) != payload['sha256']:
        raise ValueError('Previously accepted technical shape payload differs')
    shape = json.loads(Path(payload['path']).read_text())['window']
    if len(shape['input_ids']) != 1024 or sum(i != -100 for i in shape['target_ids']) != 512:
        raise ValueError('Original accepted1024/512 technical window required')
    plain = [i for i in shape['input_ids'] if 8 <= i < 4096]
    if len(plain) < 126:
        raise ValueError('Existing technical input lacks two plain63-token spans')
    ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]])
    torch.set_num_threads(2)
    saved = torch.load(parent, map_location='cpu', weights_only=False)
    original = JMicroModel(saved['model_config']).eval()
    original.load_state_dict(saved['model'], strict=True)
    rng_before = torch.get_rng_state().clone()
    candidate = IndependentMapModel.from_native(original)
    checks = dict(
        original_unique_parameters=sum(p.numel() for p in original.parameters()) == 10001152,
        candidate_unique_parameters=sum(p.numel() for p in candidate.parameters()) == 10067764,
        only_declared_independent_projection_coordinates=set(candidate.state_dict())-set(original.state_dict()) == {
            f'model.layers.{i}.self_attn.{part}' for i in range(13) for part in
            ('independent_raw','independent_down.weight','independent_q.weight','independent_k.weight')},
        every_original_weight_unchanged=all(torch.equal(candidate.state_dict()[k], v)
            for k,v in saved['model'].items()),
        new_scalars_zero=all(torch.count_nonzero(p) == 0
            for name,p in candidate.named_parameters() if name.endswith('.independent_raw')),
        original_base_config_unchanged=native_config(candidate.config) == original.config,
        tied_vocabulary=candidate.lm_head.weight is candidate.model.embed_tokens.weight,
        conversion_RNG_unchanged=torch.equal(rng_before, torch.get_rng_state()))
    with torch.no_grad():
        expected, actual = original(ids).logits, candidate(ids).logits
        checks['all_logits_bitwise_parent_equal'] = torch.equal(expected, actual)
        before_a, before_b = original(ids[:, :32], use_cache=True), candidate(ids[:, :32], use_cache=True)
        after_a = original(ids[:, 32:], cache=before_a.cache, use_cache=True)
        after_b = candidate(ids[:, 32:], cache=before_b.cache, use_cache=True)
        checks['cached_logits_bitwise_parent_equal'] = torch.equal(after_a.logits, after_b.logits)
        checks['cached_KV_bitwise_parent_equal'] = all(torch.equal(k1,k2) and torch.equal(v1,v2)
            for (k1,v1),(k2,v2) in zip(after_a.cache.layers, after_b.cache.primary))
        checks['same_logical_cache_positions'] = torch.equal(after_a.cache.positions, after_b.cache.positions)
        for block in candidate.model.layers:
            block.self_attn.independent_raw.fill_(.25)
        active_full = candidate(ids,use_cache=True)
        active_prefix = candidate(ids[:,:32],use_cache=True)
        active_suffix = candidate(ids[:,32:],cache=active_prefix.cache,use_cache=True)
        active_difference = float((active_full.logits[:,32:]-active_suffix.logits).abs().max())
        checks['active_cache_logits_within_original_tolerance'] = torch.allclose(
            active_full.logits[:,32:],active_suffix.logits,atol=3e-5,rtol=2e-5)
        checks['active_cache_K2_within_original_tolerance'] = all(torch.allclose(x,y,atol=3e-5,rtol=2e-5)
            for x,y in zip(active_full.cache.secondary,active_suffix.cache.secondary,strict=True))
        checks['active_cache_valid_positions_exact'] = (torch.equal(active_full.cache.valid,active_suffix.cache.valid)
            and torch.equal(active_full.cache.positions,active_suffix.cache.positions))
    # torch.count_nonzero comparisons above are scalar tensors; serialize booleans.
    checks = {key:bool(value) for key,value in checks.items()}
    elapsed = time.monotonic()-started
    if stat.st_size != parent.stat().st_size or stat.st_mtime_ns != parent.stat().st_mtime_ns:
        raise ValueError('Actual parent identity changed during CPU gate')
    result = dict(status='actual_native10M_independent_map_conversion_CPU_parity_complete',
        observed_at=datetime.now(timezone.utc).isoformat(), contract_sha256=sha(contract),
        proposal=c['proposal'], sources=c['sources'], checks=checks,
        original_parent=accepted['parent'],
        parent_identity_policy='Reuse previously hash-verified exact parent with frozen size/mtime guard; no new full weight rehash claimed.',
        parent_size=stat.st_size, parent_mtime_ns=stat.st_mtime_ns,
        actual_native_parameters=10001152, actual_candidate_parameters=10067764,
        model_config=candidate.config, input_shape=list(ids.shape),
        input_scope='Borrowed accepted technical token spans; not new documents, training or generation quality.',
        checkpoint_and_payload_read_paths=sorted(set(reads)),
        maximum_logit_difference=float((expected-actual).abs().max()), CPU_wall_seconds=elapsed,
        active_raw_coefficient=.25, maximum_active_cache_difference=active_difference,
        all_checks_passed=all(checks.values()) and elapsed <= 30,
        optimizer_updates=0, new_GPU_seconds=0, DEV_opened=False, TEST_opened=False,
        new_dataset_prepared=False, model_weights_saved=False, scientific_contract_frozen=False,
        Base_qualified=False, Base_adopted=False, full_four_item_goal_complete=False,
        limitations='Zero-coefficient actual-parent parity only; active cache/gradient paths were tested on CPU fixtures. No trained10M model, CUDA, Japanese quality, independent seed, fullDEV or new sealedTEST evidence.')
    # The receipt is the sole permitted write after protected reads finish.
    output.parent.mkdir(parents=True, exist_ok=True)
    # Direct protected output is explicitly the new receipt, never model/data.
    if not result['all_checks_passed']:
        result['status'] = 'actual_native10M_independent_map_CPU_gate_failed_condition_closed'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    if not result['all_checks_passed']:
        raise ValueError('Actual parent function/cache/count or fixed CPU budget failed; receipt retained')
    print(json.dumps({key:result[key] for key in ('status', 'actual_native_parameters',
        'actual_candidate_parameters', 'maximum_logit_difference', 'CPU_wall_seconds', 'new_GPU_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
