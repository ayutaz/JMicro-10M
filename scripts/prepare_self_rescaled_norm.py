"""One CPU original-parent rescaling/cache gate on accepted technical spans."""
import argparse
from datetime import datetime,timezone
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
from jmicro.self_rescaled_model import SelfRescaledModel,native_config


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(contract,pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(contract) != pin:
        raise ValueError('Externally pinned CPU-only scope required')
    c = json.loads(Path(contract).read_text())
    expected = dict(kind='actual_native_parent_self_rescaled_RMS_CPU_gate_v1',CPU_wall_ceiling_seconds=30,
        native_parameters=10001152,candidate_parameters=10014976,input_shape=[2,64],cache_split=[32,32],
        active_beta=.01,GPU_seconds=0,optimizer_updates=0,cache_atol=3e-5,cache_rtol=2e-5)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in expected.items()):
        raise ValueError('Exact single-vector original parent CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot CPU receipt required')
    for path,digest in c['sources'].items():
        if sha(ROOT/path) != digest:
            raise ValueError('Prepared CPU source differs: '+path)
    for key in ('proposal','accepted_parent_recipe','accepted_shape_recipe'):
        if sha(ROOT/c[key]['path']) != c[key]['sha256']:
            raise ValueError('Pinned evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha(ROOT/row['path']) != row['sha256']:
            raise ValueError('CPU evidence differs')
        suites = list(ET.parse(ROOT/row['path']).getroot().iter('testsuite'))
        if (sum(int(s.attrib.get('tests',0)) for s in suites) != row['expected_tests']
                or any(int(s.attrib.get(k,0)) for s in suites for k in ('failures','errors','skipped'))):
            raise ValueError('All independent mathematical/model CPU checks required')
    accepted = json.loads((ROOT/c['accepted_parent_recipe']['path']).read_text())
    parent = Path(accepted['parent']['path'])
    stat = parent.stat()
    if (accepted['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != accepted['parent_size'] or stat.st_mtime_ns != accepted['parent_mtime_ns']):
        raise ValueError('Previously hash-verified original parent size/mtime differs')
    payload = json.loads((ROOT/c['accepted_shape_recipe']['path']).read_text())['payload']
    allowed = {str(parent.resolve()),str(Path(payload['path']).resolve())}
    roots = (ROOT/'reports',ROOT/'eval',ROOT/'artifacts',Path('/home/aihub_ubuntu/jmicro-data'))
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
        raise ValueError('Accepted technical payload differs')
    window = json.loads(Path(payload['path']).read_text())['window']
    if len(window['input_ids']) != 1024 or sum(i != -100 for i in window['target_ids']) != 512:
        raise ValueError('Original1024/512 technical input required')
    plain = [i for i in window['input_ids'] if 8 <= i < 4096]
    if len(plain) < 126:
        raise ValueError('Existing technical input lacks two63-token spans')
    ids = torch.tensor([[2]+plain[:63],[2]+plain[63:126]])
    torch.set_num_threads(2)
    saved = torch.load(parent,map_location='cpu',weights_only=False)
    original = JMicroModel(saved['model_config']).eval()
    original.load_state_dict(saved['model'],strict=True)
    rng = torch.get_rng_state().clone()
    enabled = SelfRescaledModel.from_native(original)
    disabled = SelfRescaledModel.from_native(original,'disabled_zero')
    old_names = [n for n,_ in original.named_parameters()]
    extras = {n for n,_ in enabled.named_parameters() if n not in old_names}
    checks = dict(native_count=sum(p.numel() for p in original.parameters()) == 10001152,
        candidate_count=sum(p.numel() for p in enabled.parameters()) == 10014976,
        disabled_count=sum(p.numel() for p in disabled.parameters()) == 10014976,
        only54_new_norm_vectors=len(extras) == 54 and all(n.endswith(('.rescale_alpha','.rescale_beta')) for n in extras),
        original_parameter_names_order=[n for n,_ in enabled.named_parameters() if n not in extras] == old_names,
        all_original_tensors_unchanged=all(torch.equal(m.state_dict()[k],v) for m in (enabled,disabled) for k,v in saved['model'].items()),
        original_base_config_unchanged=native_config(enabled.config) == native_config(disabled.config) == original.config,
        vocabulary_tied=all(m.lm_head.weight is m.model.embed_tokens.weight for m in (enabled,disabled)),
        conversion_RNG_unchanged=torch.equal(rng,torch.get_rng_state()))
    with torch.no_grad():
        native_full = original(ids).logits
        initial_full = enabled(ids).logits
        checks['enabled_initial_logits_native_bitwise'] = torch.equal(initial_full,native_full)
        checks['disabled_logits_native_bitwise'] = torch.equal(disabled(ids).logits,native_full)
        checks['enabled_initial_fast_native_bitwise'] = torch.equal(enabled(ids,training_fast_path=True).logits,original(ids,training_fast_path=True).logits)
        a,b = original(ids[:,:32],use_cache=True),enabled(ids[:,:32],use_cache=True)
        a,b = original(ids[:,32:],cache=a.cache,use_cache=True),enabled(ids[:,32:],cache=b.cache,use_cache=True)
        checks['enabled_initial_cached_logits_native_bitwise'] = torch.equal(a.logits,b.logits)
        checks['enabled_initial_cached_KV_native_bitwise'] = all(torch.equal(x,y)
            for pair,want in zip(b.cache.real,a.cache.layers,strict=True) for x,y in zip(pair,want,strict=True))
        for n,p in enabled.named_parameters():
            if n.endswith('.rescale_beta'): p.fill_(.01)
        full = enabled(ids,use_cache=True)
        prefix = enabled(ids[:,:32],use_cache=True)
        suffix = enabled(ids[:,32:],cache=prefix.cache,use_cache=True)
        checks['active_logits_finite'] = torch.isfinite(full.logits).all().item()
        checks['active_function_not_disabled'] = not torch.equal(full.logits,native_full)
        checks['active_cache_logits_original_tolerance'] = torch.allclose(full.logits[:,32:],suffix.logits,atol=3e-5,rtol=2e-5)
        checks['active_cache_KV_original_tolerance'] = all(torch.allclose(x,y,atol=3e-5,rtol=2e-5)
            for pair,want in zip(full.cache.real,suffix.cache.real,strict=True) for x,y in zip(pair,want,strict=True))
        checks['active_cache_metadata_exact'] = torch.equal(full.cache.valid,suffix.cache.valid) and torch.equal(full.cache.positions,suffix.cache.positions)
        active_difference = float((full.logits[:,32:]-suffix.logits).abs().max())
    checks['evaluation_RNG_unchanged'] = torch.equal(rng,torch.get_rng_state())
    checks['CPU_only_CUDA_uninitialized'] = not torch.cuda.is_initialized()
    checks['parent_identity_unchanged'] = parent.stat().st_size == stat.st_size and parent.stat().st_mtime_ns == stat.st_mtime_ns
    elapsed = time.monotonic()-started
    passed = all(checks.values()) and elapsed <= 30
    result = dict(status='actual_parent_self_rescaled_RMS_CPU_passed' if passed else 'actual_parent_self_rescaled_RMS_CPU_failed_condition_closed',
        observed_at=datetime.now(timezone.utc).isoformat(),contract_sha256=sha(contract),sources=c['sources'],
        proposal=c['proposal'],checks=checks,all_checks_passed=passed,parent=accepted['parent'],
        parent_size=stat.st_size,parent_mtime_ns=stat.st_mtime_ns,
        parent_identity_policy='Accepted original hash reused with exact size/mtime guard; no repeated full parent hash claimed.',
        actual_native_parameters=10001152,actual_candidate_parameters=10014976,
        input_shape=[2,64],cache_split=[32,32],active_beta=.01,
        maximum_initial_native_logit_difference=float((initial_full-native_full).abs().max()),
        maximum_active_cache_difference=active_difference,CPU_wall_seconds=elapsed,CPU_wall_ceiling_seconds=30,
        protected_read_paths=sorted(set(reads)),new_GPU_seconds=0,optimizer_updates=0,
        new_data_prepared=False,DEV_opened=False,TEST_opened=False,weights_saved=False,
        science_contract_frozen=False,Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False,
        limitations='CPU original-parent conversion/active cache/count only. Beta.01 is a manual numerical fixture, not trained weights or scientific initialization. No CUDA, Japanese quality, independent seed, fullDEV or sealedTEST evidence.')
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if not passed:
        raise ValueError('Original-parent scope/precision failed; retain receipt, do not rescue or rerun')
    print(json.dumps({k:result[k] for k in ('status','actual_candidate_parameters','maximum_initial_native_logit_difference','maximum_active_cache_difference','CPU_wall_seconds')}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract',type=Path,required=True)
    parser.add_argument('--contract-sha256',required=True)
    args = parser.parse_args()
    run(args.contract,args.contract_sha256)
