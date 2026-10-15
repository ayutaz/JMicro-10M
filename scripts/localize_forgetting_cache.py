"""One bounded CPU localization on accepted technical spans; no new learning."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src')]
import torch
from jmicro.forgetting_attention import ForgettingModel
from jmicro.model import JMicroModel


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(path, pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha(path) != pin:
        raise ValueError('Pinned CPU-only localization contract required')
    c = json.loads(Path(path).read_text())
    if (c['kind'] != 'actual_parent_forgetting_cache_layer_localization_v1'
            or c['CPU_wall_ceiling_seconds'] != 30 or c['input_shape'] != [2, 64]
            or c['cache_split'] != [32, 32] or c['cache_atol'] != 3e-5 or c['cache_rtol'] != 2e-5):
        raise ValueError('Exact bounded localization scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh bounded receipt required')
    for name, digest in c['sources'].items():
        if sha(ROOT/name) != digest:
            raise ValueError('Frozen source differs: '+name)
    previous = json.loads((ROOT/c['previous_contract']).read_text())
    if sha(ROOT/c['previous_contract']) != c['previous_contract_sha256']:
        raise ValueError('Actual failed contract differs')
    for key in ('accepted_parent_recipe', 'accepted_shape_recipe'):
        ref = previous[key]
        if sha(ROOT/ref['path']) != ref['sha256']:
            raise ValueError('Accepted prior metadata differs')
    accepted = json.loads((ROOT/previous['accepted_parent_recipe']['path']).read_text())
    payload = json.loads((ROOT/previous['accepted_shape_recipe']['path']).read_text())['payload']
    parent = Path(accepted['parent']['path'])
    before = parent.stat()
    if (accepted['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or before.st_size != accepted['parent_size'] or before.st_mtime_ns != accepted['parent_mtime_ns']):
        raise ValueError('Previously verified original parent identity differs')
    allowed = {parent.resolve(), Path(payload['path']).resolve()}
    roots = (ROOT/'reports', ROOT/'eval', ROOT/'artifacts', Path('/home/aihub_ubuntu/jmicro-data'))
    reads = []
    def audit(event, args):
        if event != 'open' or not isinstance(args[0], (str, bytes)):
            return
        opened = Path(os.fsdecode(args[0])).resolve()
        if any(opened.is_relative_to(root) for root in roots):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if opened == output.resolve() and writing:
                return
            if writing or opened not in allowed:
                raise ValueError('Read/write outside bounded localization: '+str(opened))
            reads.append(str(opened))
    sys.addaudithook(audit)
    if sha(payload['path']) != payload['sha256']:
        raise ValueError('Previously accepted shape payload differs')
    window = json.loads(Path(payload['path']).read_text())['window']
    plain = [i for i in window['input_ids'] if 8 <= i < 4096]
    if len(window['input_ids']) != 1024 or len(plain) < 126:
        raise ValueError('Exact prior technical input required')
    ids = torch.tensor([[2]+plain[:63], [2]+plain[63:126]])
    torch.set_num_threads(2)
    saved = torch.load(parent, map_location='cpu', weights_only=False)
    native = JMicroModel(saved['model_config']).eval()
    native.load_state_dict(saved['model'], strict=True)
    candidate = ForgettingModel.from_native(native)
    results = {}
    for label, model in (('native', native), ('forgetting_reference', candidate)):
        trace, handles = {}, []
        selected = ('input_layernorm', 'self_attn.q_proj', 'self_attn.k_proj',
                    'self_attn.v_proj', 'self_attn.forget_proj', 'self_attn',
                    'post_attention_layernorm', 'mlp')
        for i, block in enumerate(model.model.layers):
            modules = dict(block.named_modules())
            for name in selected:
                if name not in modules:
                    continue
                key = f'{i:02d}.{name}'
                def hook(module, inputs, out, key=key):
                    value = out[0] if isinstance(out, tuple) else out
                    trace[key] = value.detach().clone()
                handles.append(modules[name].register_forward_hook(hook))
        with torch.no_grad():
            full = model(ids, use_cache=True)
            full_trace = trace.copy()
            trace.clear()
            prefix = model(ids[:, :32], use_cache=True)
            prefix_trace = trace.copy()
            trace.clear()
            suffix = model(ids[:, 32:], cache=prefix.cache, use_cache=True)
            suffix_trace = trace.copy()
        for handle in handles:
            handle.remove()
        def differences(part, start):
            rows = []
            for name, want in full_trace.items():
                a, b = want[:, start:start+32], part[name]
                rows.append(dict(stage=name, exact=torch.equal(a, b),
                    abs_max=float((a-b).abs().max()),
                    outside_declared_logit_precision=int((~torch.isclose(a, b, atol=c['cache_atol'], rtol=c['cache_rtol'])).sum())))
            return rows
        prefix_diff, suffix_diff = differences(prefix_trace, 0), differences(suffix_trace, 32)
        results[label] = dict(first_prefix_nonexact=next((r for r in prefix_diff if not r['exact']), None),
            first_suffix_nonexact=next((r for r in suffix_diff if not r['exact']), None),
            prefix_stages=prefix_diff, suffix_stages=suffix_diff,
            cache_logit_abs_max=float((suffix.logits-full.logits[:, 32:]).abs().max()),
            cache_logits_within_original_precision=torch.allclose(suffix.logits, full.logits[:, 32:],
                atol=c['cache_atol'], rtol=c['cache_rtol']))
    elapsed = time.monotonic()-started
    if elapsed > c['CPU_wall_ceiling_seconds'] or parent.stat().st_mtime_ns != before.st_mtime_ns:
        raise ValueError('Bounded localization identity/deadline failed')
    receipt = dict(status='actual_parent_CPU_cache_layer_localization_complete',
        created_at=datetime.now(timezone.utc).isoformat(), contract_sha256=sha(path),
        results=results, CPU_wall_seconds=elapsed, checkpoint_and_payload_read_paths=sorted(set(reads)),
        parent_identity='Previously verified hash plus exact size/mtime, not a new whole weight hash',
        input_scope='Reused same2x64 accepted technical spans; no new corpus/DEV/TEST',
        model_weights_saved=False, new_GPU_seconds=0, optimizer_updates=0, quality_evidence=False,
        limitations='First nonexact intermediate localizes onset, not a proof of a unique rounding cause or a repair. Original logit tolerances are descriptive at intermediate layers, not new acceptance thresholds.')
    output.write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(CPU_wall_seconds=elapsed, models={k: {field: v[field] for field in
        ('first_prefix_nonexact', 'first_suffix_nonexact', 'cache_logit_abs_max',
         'cache_logits_within_original_precision')} for k, v in results.items()})), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', required=True)
    parser.add_argument('--contract-sha256', required=True)
    args = parser.parse_args()
    run(args.contract, args.contract_sha256)
