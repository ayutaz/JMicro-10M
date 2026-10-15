"""One original10M CPU derivative assay; no Adam, CUDA, new data or DEV/TEST."""
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
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import now,sha256
from jmicro.model import JMicroModel
from jmicro.scalegrad import POLICY,selected_novel_mask,scalegrad_objective
from jmicro.training import atomic_json
from natural_context_contrast_trainer import right_padded_hidden
from probe_context_likelihood import passed_tests


def run(contract,pin):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or sha256(Path(contract)) != pin:
        raise ValueError('Externally pinned CPU-only contract required')
    c = json.loads(Path(contract).read_text())
    expected = dict(kind='original10M_visible_prefix_ScaleGrad_CPU_gradient_assay_v1',
        CPU_wall_ceiling_seconds=30,input_shape=[2,64],borrowed_selected_spans=[[512,576],[576,640]],
        policy=POLICY,optimizer_updates=0,GPU_seconds=0,native_parameters=10001152,
        native_disable_ALL_parameter_gradients_exact_required=True)
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in expected.items()):
        raise ValueError('Exact prospective original10M CPU derivative scope required')
    output = ROOT/c['output']
    if output.exists() or not output.resolve().is_relative_to(ROOT/'reports/phase6'):
        raise ValueError('Fresh one-shot CPU result required')
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen CPU source differs: '+path)
    for key in ('proposal','accepted_config','capacity_payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned CPU evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Pinned CPU fixture evidence differs')
        passed_tests(row['path'],row['expected_tests'])
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    parent = Path(old['parent']['path'])
    stat = parent.stat()
    if (old['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != old['parent_size'] or stat.st_mtime_ns != old['parent_mtime_ns']):
        raise ValueError('Accepted original parent SHA binding and fixed size/mtime required')
    protected = (ROOT/'reports',ROOT/'eval',ROOT/'artifacts',Path.home()/'jmicro-data')
    allowed = {parent.resolve(),Path(c['capacity_payload']['path']).resolve()}
    writes = {output.resolve(),output.with_suffix('.json.tmp').resolve()}
    reads = []
    def audit(event,args):
        if event != 'open' or not isinstance(args[0],(str,bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if any(path.is_relative_to(root) for root in protected):
            writing = any(flag in (args[1] or '') for flag in 'wax+') or bool(
                args[2] & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
            if path in writes and writing:
                return
            if writing or path not in allowed:
                raise ValueError('Outside original-parent/fixed-span CPU read set: '+str(path))
            reads.append(str(path))
    sys.addaudithook(audit)
    def timeout(*args):
        raise TimeoutError('Fixed30s CPU derivative assay exhausted')
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(30)
    checks,details,error = {},{},None
    try:
        torch.set_num_threads(2)
        torch.manual_seed(42)
        state = torch.load(parent,map_location='cpu',weights_only=False)
        window = json.loads(Path(c['capacity_payload']['path']).read_text())['window']
        rows = [dict(input_ids=window['input_ids'][a:b],target_ids=window['target_ids'][a:b])
            for a,b in c['borrowed_selected_spans']]
        ids = torch.tensor([r['input_ids'] for r in rows])
        targets = torch.tensor([r['target_ids'] for r in rows])
        if list(ids.shape) != [2,64] or (targets < 8).any():
            raise ValueError('Same already accepted technical original body spans required')
        model = JMicroModel(state['model_config']).train()
        model.load_state_dict(state['model'],strict=True)
        before = torch.get_rng_state().clone()
        novelty = selected_novel_mask(rows,4096,'cpu')
        with sdpa_kernel(SDPBackend.MATH):
            logits = model.lm_head(right_padded_hidden(model,ids).reshape(-1,256)).float()
            labels = targets.reshape(-1)
            native = F.cross_entropy(logits,labels)
            disabled = scalegrad_objective(logits,labels,novelty,gamma=1.)
            active = scalegrad_objective(logits,labels,novelty)
            parameters = list(model.parameters())
            native_grad = torch.autograd.grad(native,parameters,retain_graph=True)
            disabled_grad = torch.autograd.grad(disabled['combined_loss'],parameters,retain_graph=True)
            active['combined_loss'].backward()
        names = [n for n,_ in model.named_parameters()]
        mismatches = [n for n,g,h in zip(names,native_grad,disabled_grad,strict=True) if not torch.equal(g,h)]
        chosen_novel = novelty.gather(-1,labels[:,None]).squeeze(-1)
        gradient_difference = max(float((p.grad-g).abs().max()) for p,g in zip(parameters,native_grad,strict=True))
        checks.update(actual_native_parameter_count=sum(p.numel() for p in parameters) == 10001152,
            tied_native_vocabulary=model.lm_head.weight is model.model.embed_tokens.weight,
            original_native_weights_unchanged=all(torch.equal(v,state['model'][k]) for k,v in model.state_dict().items()),
            native_disable_scalar_exact=torch.equal(native,disabled['combined_loss']),
            native_disable_ALL_parameter_gradients_exact=not mismatches,
            active_original_CE_metric_exact=torch.equal(native,active['CE_loss']),
            active_loss_changes=not torch.equal(native,active['combined_loss']),
            active_gradients_finite=all(p.grad is not None and torch.isfinite(p.grad).all() for p in parameters),
            active_gradient_changes=gradient_difference > 0,
            no_future_target_history=all(bool(novelty[k,labels[k]]) == (int(labels[k]) not in {
                t for t in rows[k//64]['input_ids'][:k%64+1] if t >= 8}) for k in range(128)),
            both_novel_and_seen_original_gold_observed=0 < int(chosen_novel.sum()) < 128,
            CPU_RNG_unchanged=torch.equal(before,torch.get_rng_state()),
            CUDA_not_initialized=not torch.cuda.is_initialized())
        details.update(native_CE_loss=float(native.detach()),active_ScaleGrad_loss=float(active['combined_loss'].detach()),
            native_gradient_tensor_count=len(names),native_disable_gradient_mismatches=mismatches,
            native_disable_max_gradient_difference=max(float((g-h).abs().max()) for g,h in zip(native_grad,disabled_grad,strict=True)),
            active_max_gradient_difference_from_native=gradient_difference,
            original_selected_teachers=128,novel_gold_positions=int(chosen_novel.sum()),seen_gold_positions=128-int(chosen_novel.sum()),
            novelty_vocabulary_size=4096,original_body_only_no_synthetic_EOS=True)
    except Exception as exc:
        error = dict(type=type(exc).__name__,message=str(exc))
    finally:
        signal.alarm(0)
    elapsed = time.monotonic()-started
    passed = error is None and bool(checks) and all(checks.values()) and elapsed <= 30
    atomic_json(output,dict(status='actual10M_ScaleGrad_CPU_passed_GPU_unqualified' if passed else 'actual10M_ScaleGrad_CPU_failed_condition_closed',
        created_at=now(),config_sha256=pin,all_checks_passed=passed,checks=checks,details=details,error=error,
        CPU_wall_seconds=elapsed,CPU_wall_ceiling_seconds=30,input_shape=[2,64],model_and_data_read_paths=sorted(set(reads)),
        optimizer_updates=0,scientific_teacher_positions=0,new_GPU_seconds=0,DEV_opened=False,TEST_opened=False,
        Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False,
        limits='Original parent/small borrowed body spans and finite/exact CPU derivatives do not prove CUDA capacity, resume, throughput or Japanese quality. Original inference implementation is unchanged; accepted native cache evidence is reused, not rerun.'))
    print(json.dumps(dict(passed=passed,CPU_wall_seconds=elapsed,checks=checks,details=details,error=error)),flush=True)
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',required=True)
    parser.add_argument('--config-sha256',required=True)
    args = parser.parse_args()
    run(args.config,args.config_sha256)
