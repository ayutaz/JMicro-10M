"""One original10M CPU loss/ALL-parameter-gradient/cache equivalence assay."""
import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time
import weakref

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.model import JMicroModel
from jmicro.rdrop import two_view_objective,POLICY
from jmicro.rdrop_analytic import analytic_two_view_objective,IMPLEMENTATION
from jmicro.experiment import sha256,now
from jmicro.training import atomic_json,rng_state,restore_rng,seed_all
from jmicro.phase5 import equal_state
from base_residual_dropout import install_training_dropout
from natural_context_contrast_trainer import host,right_padded_hidden
from probe_document_progress import cache_observations
from probe_context_likelihood import passed_tests


def saved_storage(function):
    generator = torch.Generator().manual_seed(20261015)
    a = torch.randn(32,4096,generator=generator,requires_grad=True)
    b = torch.randn(32,4096,generator=generator,requires_grad=True)
    targets = torch.randint(4096,(32,),generator=generator)
    packed = []
    class Saved:
        def __init__(self,tensor): self.tensor = tensor.detach()
    def pack(tensor):
        saved = Saved(tensor)
        if tensor.shape == a.shape:
            packed.append(weakref.ref(saved))
        return saved
    with torch.autograd.graph.saved_tensors_hooks(pack,lambda saved:saved.tensor):
        result = function(a,b,targets)
    storages = {}
    for ref in packed:
        saved = ref()
        if saved is not None:
            storage = saved.tensor.untyped_storage()
            storages[storage.data_ptr()] = storage.nbytes()
    return dict(shape=[32,4096],live_unique_dense_count=len(storages),live_unique_dense_bytes=sum(storages.values()))


def run(contract,pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha256(Path(contract)) != pin:
        raise ValueError('Externally pinned CPU-only contract required')
    c = json.loads(Path(contract).read_text())
    expected = dict(kind='original10M_analytic_RDrop_loss_exact_CPU_v1',CPU_wall_ceiling_seconds=30,
        input_shape=[2,64],borrowed_selected_spans=[[512,576],[576,640]],policy=POLICY,
        loss_runtime=IMPLEMENTATION,optimizer_updates=0,GPU_seconds=0,native_parameters=10001152,
        exact_ALL_parameter_gradients_required=True)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in expected.items()):
        raise ValueError('Exact prospective analytic native10M CPU scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot CPU record required')
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen CPU source differs: '+path)
    for key in ('proposal','accepted_config','capacity_payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('CPU suite differs')
        passed_tests(row['path'],row['expected_tests'])
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    parent = Path(old['parent']['path'])
    stat = parent.stat()
    if (old['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != old['parent_size'] or stat.st_mtime_ns != old['parent_mtime_ns']):
        raise ValueError('Previously verified original parent hash binding/size/mtime required')
    allowed = {str(parent.resolve()),str(Path(c['capacity_payload']['path']).resolve())}
    roots = (ROOT/'reports',ROOT/'eval',ROOT/'artifacts',Path('/home/aihub_ubuntu/jmicro-data'))
    reads = []
    def audit(event,args):
        if event != 'open' or not isinstance(args[0],(str,bytes)): return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in roots):
            writing = any(flag in (args[1] or '') for flag in 'wax+')
            if path in (output.resolve(),output.with_suffix('.json.tmp').resolve()) and writing: return
            if str(path) not in allowed or writing:
                raise ValueError('Forbidden model/data/DEV/TEST access: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    checks,cache,storage,details = {},None,None,{}
    error = None
    def timeout(*args): raise TimeoutError('Fixed30s CPU assay exceeded')
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(30)
    try:
        torch.set_num_threads(2)
        seed_all(42)
        storage = dict(reference=saved_storage(two_view_objective),analytic=saved_storage(analytic_two_view_objective))
        checks['strict_saved_dense_storage_reduction'] = storage['analytic']['live_unique_dense_bytes'] < storage['reference']['live_unique_dense_bytes']
        checks['only_two_logprob_dense_tensors_saved'] = storage['analytic']['live_unique_dense_count'] == 2
        saved = torch.load(parent,map_location='cpu',weights_only=False)
        window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
        ids = torch.tensor([window['input_ids'][a:b] for a,b in c['borrowed_selected_spans']])
        targets = torch.tensor([window['target_ids'][a:b] for a,b in c['borrowed_selected_spans']])
        if ids.shape != (2,64) or (targets < 8).any():
            raise ValueError('Existing selected original body spans, no synthetic EOS required')
        models = []
        for _ in range(2):
            model = JMicroModel(saved['model_config']).train()
            model.load_state_dict(saved['model'],strict=True)
            install_training_dropout(model)
            models.append(model)
        before = host(rng_state())
        losses,states,logits = [],[],[]
        with sdpa_kernel(SDPBackend.MATH):
            for model,function in zip(models,(two_view_objective,analytic_two_view_objective),strict=True):
                restore_rng(host(before))
                first = model.lm_head(right_padded_hidden(model,ids).reshape(-1,256))
                second = model.lm_head(right_padded_hidden(model,ids).reshape(-1,256))
                result = function(first,second,targets.reshape(-1))
                result['combined_loss'].backward()
                losses.append({k:float(v.detach()) for k,v in result.items()})
                states.append(host(rng_state()))
                logits.append((host(first),host(second)))
        names = [[n for n,_ in m.named_parameters()] for m in models]
        differences = [n for (n,p),(name,q) in zip(models[0].named_parameters(),models[1].named_parameters(),strict=True)
            if n != name or p.grad is None or q.grad is None or not torch.equal(p.grad,q.grad)]
        details.update(reference_losses=losses[0],analytic_losses=losses[1],different_gradient_names=differences,
            native_gradient_tensor_count=len(names[0]),maximum_gradient_difference=max(float((p.grad-q.grad).abs().max())
                for p,q in zip(models[0].parameters(),models[1].parameters(),strict=True)))
        checks.update(all_five_actual_losses_exact=losses[0] == losses[1],
            both_actual_stochastic_logit_views_exact=equal_state(logits[0],logits[1]),
            all_native_parameter_names_order_exact=names[0] == names[1],
            ALL_actual_native_gradients_exact=not differences,
            all_actual_gradients_finite=all(bool(torch.isfinite(p.grad).all()) for m in models for p in m.parameters()),
            actual_dropout_RNG_exact=equal_state(states[0],states[1]),
            actual_dropout_views_differ=not torch.equal(logits[1][0],logits[1][1]),
            actual_native_count=all(sum(p.numel() for p in m.parameters()) == 10001152 for m in models),
            original_weights_unchanged=all(torch.equal(v,saved['model'][k]) for m in models for k,v in m.state_dict().items()),
            tied_vocabulary=all(m.lm_head.weight is m.model.embed_tokens.weight for m in models))
        for m in models: m.eval()
        before_eval = host(rng_state())
        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH):
            a,b = (m(ids,use_cache=True) for m in models)
            prefix = models[1](ids[:,:32],use_cache=True)
            suffix = models[1](ids[:,32:],cache=prefix.cache,use_cache=True)
            cache = cache_observations(b,suffix,equal_state(before_eval,host(rng_state())))
            checks.update(native_eval_logits_exact=torch.equal(a.logits,b.logits),
                native_fast_logits_exact=torch.equal(models[0](ids,training_fast_path=True).logits,models[1](ids,training_fast_path=True).logits),
                original_cache_all_subchecks=cache['passed'],eval_RNG_unchanged=equal_state(before_eval,host(rng_state())),
                CUDA_not_initialized=not torch.cuda.is_initialized())
    except Exception as exc:
        error = dict(kind=type(exc).__name__,message=str(exc))
    finally:
        signal.alarm(0)
    elapsed = time.monotonic()-started
    passed = error is None and bool(checks) and all(checks.values()) and elapsed <= 30
    atomic_json(output,dict(status='actual10M_analytic_CPU_exact_GPU_unqualified' if passed else 'actual10M_analytic_CPU_mismatch_condition_closed',
        created_at=now(),config_sha256=pin,parent=old['parent'],all_checks_passed=passed,checks=checks,
        details=details,storage=storage,cache=cache,error=error,CPU_wall_seconds=elapsed,CPU_wall_ceiling_seconds=30,
        input_shape=[2,64],model_and_data_read_paths=sorted(set(reads)),optimizer_updates=0,scientific_teachers=0,
        new_GPU_seconds=0,DEV_opened=False,TEST_opened=False,Base_qualified=False,Base_adopted=False,
        full_four_item_goal_complete=False,limits='CPU saved tensors are not CUDA peak or speed. Borrowed technical spans and finite/exact gradients are not Japanese quality evidence.'))
    print(json.dumps(dict(passed=passed,CPU_wall_seconds=elapsed,checks=checks,storage=storage,error=error)),flush=True)
    if not passed: raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',required=True)
    parser.add_argument('--config-sha256',required=True)
    args = parser.parse_args()
    run(args.config,args.config_sha256)
