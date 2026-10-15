"""One-shot actual-parent CPU fixed-zero function/cache check, no new data."""
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
sys.path[:0] = [str(ROOT/'src')]
import torch
from jmicro.model import JMicroModel
from jmicro.quiet_attention import QuietModel, native_config


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Externally pinned CPU-only contract required')
    c = json.loads(Path(contract).read_text())
    if (c['kind'] != 'actual_native_parent_fixed_zero_CPU_gate_v1'
            or c['CPU_wall_ceiling_seconds'] != 30 or c['parameters'] != 10001152
            or c['input_shape'] != [2,64] or c['cache_split'] != [32,32]
            or c['GPU_seconds'] != 0 or c['optimizer_updates'] != 0
            or c['cache_atol'] != 3e-5 or c['cache_rtol'] != 2e-5):
        raise ValueError('Exact fixed-zero CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot CPU receipt required')
    for path, digest in c['sources'].items():
        if sha(ROOT/path) != digest:
            raise ValueError('CPU-prepared source differs: '+path)
    for key in ('proposal','model_tests','accepted_parent_recipe','accepted_shape_recipe'):
        if sha(ROOT/c[key]['path']) != c[key]['sha256']:
            raise ValueError('Pinned metadata differs: '+key)
    suites = list(ET.parse(ROOT/c['model_tests']['path']).getroot().iter('testsuite'))
    if (sum(int(s.attrib.get('tests',0)) for s in suites) != 37
            or any(int(s.attrib.get(k,0)) for s in suites for k in ('failures','errors','skipped'))):
        raise ValueError('All37 independent model checks required')
    accepted = json.loads((ROOT/c['accepted_parent_recipe']['path']).read_text())
    parent = Path(accepted['parent']['path'])
    if accepted['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
        raise ValueError('Original learned10B parent required')
    stat = parent.stat()
    if stat.st_size != accepted['parent_size'] or stat.st_mtime_ns != accepted['parent_mtime_ns']:
        raise ValueError('Previously hash-verified parent size/mtime differs; no restore fallback')
    payload = json.loads((ROOT/c['accepted_shape_recipe']['path']).read_text())['payload']
    allowed = {str(parent.resolve()), str(Path(payload['path']).resolve())}
    roots = (ROOT/'reports', ROOT/'eval', ROOT/'artifacts', Path('/home/aihub_ubuntu/jmicro-data'))
    reads = []
    def audit(event,args):
        if event != 'open' or not isinstance(args[0],(str,bytes)):
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
    if sha(payload['path']) != payload['sha256']:
        raise ValueError('Accepted technical shape payload differs')
    window = json.loads(Path(payload['path']).read_text())['window']
    if len(window['input_ids']) != 1024 or sum(t != -100 for t in window['target_ids']) != 512:
        raise ValueError('Original1024/512 technical input required')
    plain = [i for i in window['input_ids'] if 8 <= i < 4096]
    if len(plain) < 126:
        raise ValueError('Existing technical input lacks two63-token spans')
    ids = torch.tensor([[2]+plain[:63],[2]+plain[63:126]])
    torch.set_num_threads(2)
    state = torch.load(parent,map_location='cpu',weights_only=False)
    original = JMicroModel(state['model_config']).eval()
    original.load_state_dict(state['model'],strict=True)
    rng = torch.get_rng_state().clone()
    enabled = QuietModel.from_native(original)
    disabled = QuietModel.from_native(original,'disabled_native')
    checks = dict(actual_native_count=sum(p.numel() for p in original.parameters()) == 10001152,
        actual_enabled_count=sum(p.numel() for p in enabled.parameters()) == 10001152,
        actual_disabled_count=sum(p.numel() for p in disabled.parameters()) == 10001152,
        parameter_names_order_unchanged=[n for n,_ in enabled.named_parameters()] == [n for n,_ in original.named_parameters()],
        all_original_tensors_unchanged=all(torch.equal(m.state_dict()[k],v)
            for m in (enabled,disabled) for k,v in state['model'].items()),
        only_extra_nontrainable_runtime=set(enabled.state_dict())-set(original.state_dict()) == {'quiet_runtime'},
        base_config_unchanged=native_config(enabled.config) == native_config(disabled.config) == original.config,
        original_vocabulary_tie=all(m.lm_head.weight is m.model.embed_tokens.weight for m in (enabled,disabled)),
        conversion_global_RNG_unchanged=torch.equal(rng,torch.get_rng_state()))
    with torch.no_grad():
        expected = original(ids).logits
        checks['disabled_logits_native_bitwise'] = torch.equal(expected,disabled(ids).logits)
        checks['disabled_fast_logits_native_bitwise'] = torch.equal(
            original(ids,training_fast_path=True).logits,disabled(ids,training_fast_path=True).logits)
        a,b = original(ids[:,:32],use_cache=True),disabled(ids[:,:32],use_cache=True)
        a,b = original(ids[:,32:],cache=a.cache,use_cache=True),disabled(ids[:,32:],cache=b.cache,use_cache=True)
        checks['disabled_cached_logits_native_bitwise'] = torch.equal(a.logits,b.logits)
        checks['disabled_real_KV_native_bitwise'] = all(torch.equal(x,y)
            for pair,want in zip(b.cache.real,a.cache.layers,strict=True) for x,y in zip(pair,want,strict=True))
        full = enabled(ids,use_cache=True)
        prefix = enabled(ids[:,:32],use_cache=True)
        suffix = enabled(ids[:,32:],cache=prefix.cache,use_cache=True)
        checks['enabled_function_changed_explicitly'] = not torch.equal(full.logits,expected)
        checks['enabled_logits_finite'] = torch.isfinite(full.logits).all().item()
        checks['enabled_cache_logits_original_tolerance'] = torch.allclose(full.logits[:,32:],suffix.logits,atol=3e-5,rtol=2e-5)
        checks['enabled_cache_KV_original_tolerance'] = all(torch.allclose(x,y,atol=3e-5,rtol=2e-5)
            for pair,want in zip(full.cache.real,suffix.cache.real,strict=True) for x,y in zip(pair,want,strict=True))
        checks['enabled_cache_metadata_exact'] = torch.equal(full.cache.valid,suffix.cache.valid) and torch.equal(full.cache.positions,suffix.cache.positions)
        checks['cache_real_tokens_only'] = all(k.shape[2] == v.shape[2] == 64 for k,v in suffix.cache.real)
        difference = float((full.logits[:,32:]-suffix.logits).abs().max())
        function_difference = float((full.logits-expected).abs().max())
    checks['evaluation_global_RNG_unchanged'] = torch.equal(rng,torch.get_rng_state())
    checks['CPU_only_CUDA_uninitialized'] = not torch.cuda.is_initialized()
    checks['parent_identity_unchanged'] = parent.stat().st_size == stat.st_size and parent.stat().st_mtime_ns == stat.st_mtime_ns
    elapsed = time.monotonic()-started
    passed = all(checks.values()) and elapsed <= 30
    result = dict(status='actual_parent_fixed_zero_CPU_passed' if passed else 'actual_parent_fixed_zero_CPU_failed_condition_closed',
        observed_at=datetime.now(timezone.utc).isoformat(),contract_sha256=sha(contract),sources=c['sources'],
        proposal=c['proposal'],checks=checks,all_checks_passed=passed,
        parent=accepted['parent'],parent_size=stat.st_size,parent_mtime_ns=stat.st_mtime_ns,
        parent_identity_policy='Accepted original hash reused with exact pinned size/mtime; no new parent hash claimed.',
        actual_native_parameters=10001152,actual_candidate_parameters=10001152,
        input_shape=[2,64],cache_split=[32,32],maximum_enabled_cache_difference=difference,
        maximum_enabled_vs_native_function_difference=function_difference,
        CPU_wall_seconds=elapsed,CPU_wall_ceiling_seconds=30,protected_read_paths=sorted(set(reads)),
        new_GPU_seconds=0,optimizer_updates=0,new_data_prepared=False,DEV_opened=False,TEST_opened=False,
        weights_saved=False,scientific_contract_frozen=False,Base_qualified=False,full_four_item_goal_complete=False,
        limitations='CPU actual-parent function/cache/count only. Enabled function changes. No CUDA/trained model/Japanese quality/independent seed/fullDEV/new sealedTEST evidence.')
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if not passed:
        raise ValueError('Actual-parent CPU scope/precision failure; receipt retained, do not rerun')
    print(json.dumps({k:result[k] for k in ('status','actual_candidate_parameters','maximum_enabled_cache_difference','CPU_wall_seconds')}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract',type=Path,required=True)
    parser.add_argument('--contract-sha256',required=True)
    args = parser.parse_args()
    run(args.contract,args.contract_sha256)
