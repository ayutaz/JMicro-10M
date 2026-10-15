"""One CPU parent/inference/two-view backward assay on accepted saved spans."""
import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.model import JMicroModel
from jmicro.rdrop import POLICY,two_view_objective
from jmicro.experiment import sha256,now
from jmicro.training import atomic_json,rng_state,seed_all
from jmicro.phase5 import equal_state
from base_residual_dropout import install_training_dropout
from natural_context_contrast_trainer import host,right_padded_hidden
from probe_document_progress import cache_observations
from probe_context_likelihood import passed_tests


def run(contract,pin):
    started = time.monotonic()
    contract = Path(contract)
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha256(contract) != pin:
        raise ValueError('Externally pinned CPU-only scope required')
    c = json.loads(Path(contract).read_text())
    expected = dict(kind='native_original10M_normalized_RDrop_CPU_assay_v1',CPU_wall_ceiling_seconds=30,
        native_parameters=10001152,training_parameters=10001152,input_shape=[2,64],cache_split=[32,32],
        borrowed_selected_spans=[[512,576],[576,640]],GPU_seconds=0,optimizer_updates=0,
        cache_atol=3e-5,cache_rtol=2e-5,policy=POLICY,seed=42)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in expected.items()):
        raise ValueError('Exact fixed normalized RDrop CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Preserve completed one-shot CPU evidence')
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Prepared source differs: '+path)
    for key in ('proposal','accepted_config','capacity_payload','CPU_tests','CPU_scope_tests'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned CPU evidence differs: '+key)
    passed_tests(c['CPU_tests']['path'],39)
    passed_tests(c['CPU_scope_tests']['path'],6)
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    parent = Path(old['parent']['path'])
    stat = parent.stat()
    if (old['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != old['parent_size'] or stat.st_mtime_ns != old['parent_mtime_ns']):
        raise ValueError('Accepted previously hashed parent size/mtime required')
    allowed = {str(parent.resolve()),str(Path(c['capacity_payload']['path']).resolve())}
    roots = (ROOT/'reports',ROOT/'eval',ROOT/'artifacts',Path('/home/aihub_ubuntu/jmicro-data'))
    reads = []
    def audit(event,args):
        if event != 'open' or not isinstance(args[0],(str,bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in roots):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if path in (output.resolve(),output.with_suffix('.json.tmp').resolve()) and writing:
                return
            if str(path) not in allowed or writing:
                raise ValueError('Forbidden model/data/DEV/TEST read or write: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    checks,cache,losses = {},None,None
    error = None
    def timeout(*args):
        raise TimeoutError('Fixed30s CPU assay exceeded')
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(30)
    try:
        torch.set_num_threads(2)
        seed_all(42)
        saved = torch.load(parent,map_location='cpu',weights_only=False)
        window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
        ids = torch.tensor([window['input_ids'][a:b] for a,b in c['borrowed_selected_spans']])
        targets = torch.tensor([window['target_ids'][a:b] for a,b in c['borrowed_selected_spans']])
        if ids.shape != (2,64) or (targets < 8).any():
            raise ValueError('Saved original selected body spans required, no synthetic EOS')
        native = JMicroModel(saved['model_config']).eval()
        native.load_state_dict(saved['model'],strict=True)
        candidate = JMicroModel(saved['model_config']).eval()
        candidate.load_state_dict(saved['model'],strict=True)
        before = host(rng_state())
        install_training_dropout(candidate)
        checks.update(original_count=sum(p.numel() for p in native.parameters()) == 10001152,
            candidate_count=sum(p.numel() for p in candidate.parameters()) == 10001152,
            exact_native_config=candidate.config == native.config,
            no_new_state_keys=set(candidate.state_dict()) == set(native.state_dict()),
            vocabulary_tied=candidate.lm_head.weight is candidate.model.embed_tokens.weight,
            hooks_do_not_advance_RNG=equal_state(before,host(rng_state())))
        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH):
            a,b = native(ids,use_cache=True),candidate(ids,use_cache=True)
            checks['eval_full_native_bitwise'] = torch.equal(a.logits,b.logits)
            checks['eval_fast_native_bitwise'] = torch.equal(native(ids,training_fast_path=True).logits,
                candidate(ids,training_fast_path=True).logits)
            p,q = native(ids[:,:32],use_cache=True),candidate(ids[:,:32],use_cache=True)
            p,q = native(ids[:,32:],cache=p.cache,use_cache=True),candidate(ids[:,32:],cache=q.cache,use_cache=True)
            checks['eval_cached_native_bitwise'] = torch.equal(p.logits,q.logits)
            checks['eval_KV_native_bitwise'] = all(torch.equal(x,y) for pair,want in zip(p.cache.layers,q.cache.layers,strict=True)
                for x,y in zip(pair,want,strict=True))
            cache = cache_observations(b,q,equal_state(before,host(rng_state())))
            checks['original_cache_all_subchecks_pass'] = cache['passed']
            checks['eval_RNG_unchanged'] = equal_state(before,host(rng_state()))
        candidate.train()
        with sdpa_kernel(SDPBackend.MATH):
            first = candidate.lm_head(right_padded_hidden(candidate,ids).reshape(-1,256))
            second = candidate.lm_head(right_padded_hidden(candidate,ids).reshape(-1,256))
            objective = two_view_objective(first,second,targets.reshape(-1))
            objective['combined_loss'].backward()
        norm = torch.nn.utils.clip_grad_norm_(candidate.parameters(),1.,error_if_nonfinite=True)
        losses = {k:float(v.detach()) for k,v in objective.items()}
        checks.update(two_train_predictions_differ=not torch.equal(first,second),
            symmetric_KL_positive=losses['symmetric_KL'] > 0,
            all_losses_finite=all(torch.isfinite(v) for v in objective.values()),
            finite_nonzero_joint_gradient=0 < float(norm) < float('inf'),
            training_dropout_advances_saved_RNG=not equal_state(before,host(rng_state())),
            every_original_weight_unchanged=all(torch.equal(v,saved['model'][k]) for k,v in candidate.state_dict().items()),
            CUDA_not_initialized=not torch.cuda.is_initialized())
        checks = {k:bool(v) for k,v in checks.items()}
    except Exception as exc:
        error = dict(kind=type(exc).__name__,message=str(exc))
    finally:
        signal.alarm(0)
    elapsed = time.monotonic()-started
    passed = error is None and bool(checks) and all(checks.values()) and elapsed <= 30
    atomic_json(output,dict(status='CPU_actual_parent_passed_GPU_unqualified' if passed else 'CPU_actual_parent_failed_condition_closed',
        created_at=now(),config_sha256=pin,parent=old['parent'],actual_native_parameters=10001152,
        actual_training_parameters=10001152,all_checks_passed=passed,checks=checks,cache=cache,losses=losses,error=error,
        input_shape=[2,64],borrowed_selected_spans=c['borrowed_selected_spans'],CPU_wall_seconds=elapsed,
        CPU_wall_ceiling_seconds=30,model_and_data_read_paths=sorted(set(reads)),
        guard_limit='Python open audit, not OS sandbox. Only saved accepted technical spans; no quality examples or dataset preparation.',
        optimizer_updates=0,scientific_teachers=0,GPU_seconds=0,DEV_opened=False,TEST_opened=False,
        Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False))
    print(json.dumps(dict(passed=passed,CPU_wall_seconds=elapsed,checks=checks,error=error)),flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',required=True)
    parser.add_argument('--config-sha256',required=True)
    args = parser.parse_args()
    run(args.config,args.config_sha256)
