"""Read-only original-target fitting diagnostic; all Python launched through uv."""
import argparse
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, restore_rng, seed_all
from condition_positive_trainer import PositiveTrainView
from phase6_performance import alive, identity
from run_eos_short_pilot import equal_state

RUN = ROOT / 'reports/phase6/condition-trainfit-diagnostic-20261006'
CONFIG = ROOT / 'configs/phase6/condition_trainfit_diagnostic.json'
STUDY = ROOT / 'reports/phase6/condition-positive-comparison-20261006'
STUDY_CONFIG = ROOT / 'configs/phase6/condition_positive_comparison.json'
PROPOSAL = ROOT / 'reports/phase6/condition_positive_trainfit_diagnostic_proposal.json'
ARMS = ('parent2B', 'control', 'positive4')
GROUPS = ('focus_body', 'other_body', 'EOS')
SOURCES = ('scripts/run_condition_trainfit_diagnostic.py', 'scripts/run_condition_trainfit_diagnostic.ps1',
           'scripts/condition_positive_trainer.py', 'scripts/phase6_performance.py',
           'scripts/run_eos_short_pilot.py')


def reference(path): return dict(path=str(path), sha256=sha256(path))


def check_reference(ref):
    if sha256(Path(ref['path'])) != ref['sha256']:
        raise ValueError('Frozen reference differs: ' + ref['path'])


def scope(c):
    if (c['kind'] != 'original_condition_train_target_fit' or c['GPU_budget_seconds'] != 60
            or c['optimizer_updates'] != 0 or c['scientific_teacher_tokens'] != 0
            or c['protected_test_used'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started']
            or not c['quality_criteria_unchanged'] or list(c['checkpoints']) != list(ARMS)
            or c['documents'] != 512 or c['batch'] != 32 or c['dtype'] != 'bf16'
            or c['backend'] != 'math' or c['context'] != 'same_original_standalone_BOS_body_EOS'):
        raise ValueError('Bounded Base-only diagnostic scope differs')


def freeze():
    if CONFIG.exists(): inspect(); return
    old_job = read_json(STUDY / 'job.json')
    result, review, science = (read_json(p) for p in (STUDY / 'compare-result.json', STUDY / 'review.json', STUDY_CONFIG))
    proposal = read_json(PROPOSAL)
    if (old_job['status'] != 'complete' or alive(old_job)
            or result['config_sha256'] != sha256(STUDY_CONFIG)
            or review['result_sha256'] != sha256(STUDY / 'compare-result.json')
            or review['new_scientific_teacher_tokens'] != 50000000
            or review['protected_test_used'] or proposal['GPU_budget_seconds'] != 60
            or proposal['documents'] != 512 or proposal['optimizer_updates'] != 0):
        raise ValueError('Completed reviewed comparison and bounded proposal required')
    data = science['positive_data']
    view = PositiveTrainView(data['path'], data['manifest_sha256'])
    if (view.manifest_sha256 != proposal['source_manifest_sha256'] or len(view.lengths) != 512
            or int(view.lengths.max()) > 1025):
        raise ValueError('Original frozen512 targets do not fit common context')
    c = dict(kind='original_condition_train_target_fit', documents=512, batch=32, dtype='bf16', backend='math',
        context='same_original_standalone_BOS_body_EOS', GPU_budget_seconds=60,
        optimizer_updates=0, scientific_teacher_tokens=0, new_original_tokens=0,
        protected_test_used=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        quality_criteria_unchanged=True, old_numerical7_preserved=True,
        checkpoints=dict(parent2B=science['parent'], **{arm: dict(path=result['checkpoints'][arm]['checkpoint'],
            sha256=result['checkpoints'][arm]['checkpoint_sha256']) for arm in ARMS[1:]}),
        positive_data=data, manifest=reference(view.directory / 'manifest.json'),
        arrays=reference(view.directory / 'train.npz'),
        references=dict(proposal=reference(PROPOSAL), study_config=reference(STUDY_CONFIG),
            result=reference(STUDY / 'compare-result.json'), review=reference(STUDY / 'review.json')),
        source_sha256={p: sha256(ROOT / p) for p in SOURCES}, implementation=implementation_hashes(),
        target_counts=dict(focus_body=int(view.focus.sum()), other_body=view.manifest['original_body_tokens']-int(view.focus.sum()), EOS=512),
        limitations=proposal['limitations'], created_at=now())
    scope(c); atomic_json(CONFIG, c); inspect()
    print('Frozen all512 original targets/3 checkpoints; optimizer0, no GPU yet', flush=True)


def inspect():
    c = read_json(CONFIG); scope(c)
    if c['implementation'] != implementation_hashes(): raise ValueError('Core implementation changed')
    for path, digest in c['source_sha256'].items():
        if sha256(ROOT / path) != digest: raise ValueError('Diagnostic source changed: ' + path)
    for ref in (*c['references'].values(), *c['checkpoints'].values(), c['manifest'], c['arrays']): check_reference(ref)
    if alive(read_json(STUDY / 'job.json')): raise ValueError('Previous GPU study still live')
    if (RUN / 'job.json').exists() and alive(read_json(RUN / 'job.json')):
        raise ValueError('Existing diagnostic is live; never duplicate')
    view = PositiveTrainView(c['positive_data']['path'], c['positive_data']['manifest_sha256'])
    if (len(view.lengths) != 512 or int(view.focus.sum()) != c['target_counts']['focus_body']
            or view.manifest['full_CE_targets'] != sum(c['target_counts'].values())):
        raise ValueError('Original target counts differ')
    return c, view


def documents(view, start, end):
    rows = []
    for index in range(start, end):
        offset, length = int(view.offsets[index]), int(view.lengths[index])
        ids = view.tokens[offset:offset+length].astype(int).tolist()
        focus = view.focus[offset+1:offset+length].tolist()
        if (ids[0] != 2 or ids[-1] != 3 or any(i < 8 for i in ids[1:-1])
                or len(ids) > 1025 or focus[-1] or any(type(x) is not bool for x in focus)):
            raise ValueError('Original body/EOS alignment differs')
        rows.append(dict(index=index, id=view.manifest['metadata'][index]['id'], ids=ids, focus=focus,
            target_sha256=hashlib.sha256(json.dumps(dict(ids=ids, focus=focus), sort_keys=True).encode()).hexdigest()))
    return rows


def group_losses(nll, labels, focus):
    if (nll.ndim != 1 or labels.shape != nll.shape or focus.shape != nll.shape
            or focus.dtype != torch.bool or len(nll) < 2 or int(labels[-1]) != 3
            or int((labels == 3).sum()) != 1 or bool(focus[-1])
            or bool((focus & (labels < 8)).any()) or not bool(torch.isfinite(nll).all())):
        raise ValueError('Finite original focus/body/EOS targets required')
    masks = dict(focus_body=focus, other_body=(labels >= 8) & ~focus, EOS=labels == 3)
    if sum(int(m.sum()) for m in masks.values()) != len(nll): raise ValueError('Structural or omitted target')
    return {name: dict(tokens=int(mask.sum()), nll_sum=float(nll[mask].double().sum()),
        mean_nll=float(nll[mask].double().mean()) if bool(mask.any()) else None) for name, mask in masks.items()}


@torch.inference_mode()
def score_batch(model, cases, device):
    width = max(len(r['ids']) - 1 for r in cases)
    x = torch.zeros((len(cases), width), dtype=torch.long, device=device)
    valid = torch.zeros_like(x, dtype=torch.bool)
    for i, case in enumerate(cases):
        length = len(case['ids']) - 1
        x[i, :length] = torch.tensor(case['ids'][:-1], device=device); valid[i, :length] = True
    with torch.autocast(device, dtype=torch.bfloat16, enabled=device == 'cuda'):
        logits = model(x, attention_mask=valid).logits
    rows = []
    for i, case in enumerate(cases):
        length = len(case['ids']) - 1
        scores = logits[i, :length]
        if not bool(torch.isfinite(scores).all()): raise ValueError('Nonfinite original logits')
        labels = torch.tensor(case['ids'][1:], device=device)
        focus = torch.tensor(case['focus'], dtype=torch.bool, device=device)
        nll = F.cross_entropy(scores.float(), labels, reduction='none')
        rows.append(dict(index=case['index'], id=case['id'], target_sha256=case['target_sha256'],
            target_ids=case['ids'][1:], focus=case['focus'], target_nll=nll.tolist(),
            groups=group_losses(nll, labels, focus)))
    return rows


def summarize(rows, c):
    keyed = {(r['checkpoint'], r['index']): r for r in rows}
    if len(rows) != len(keyed) or set(keyed) != {(arm, i) for arm in ARMS for i in range(c['documents'])}:
        raise ValueError('Incomplete or duplicate original-target coverage')
    for i in range(c['documents']):
        originals = [keyed[(arm, i)] for arm in ARMS]
        if any(any(row[k] != originals[0][k] for k in ('id', 'target_sha256', 'target_ids', 'focus')) for row in originals[1:]):
            raise ValueError('Different original targets scored between checkpoints')
    result, deltas = {}, {}
    for arm in ARMS:
        selected = [keyed[(arm, i)] for i in range(c['documents'])]
        result[arm] = {}
        for group in GROUPS:
            tokens = sum(r['groups'][group]['tokens'] for r in selected)
            nll = sum(r['groups'][group]['nll_sum'] for r in selected)
            if tokens != c['target_counts'][group] or not math.isfinite(nll): raise ValueError('Group coverage or finite loss differs')
            result[arm][group] = dict(tokens=tokens, nll_sum=nll, mean_nll=nll/tokens)
    for before, after in (('parent2B', 'control'), ('parent2B', 'positive4'), ('control', 'positive4')):
        deltas[before+'->'+after] = {}
        for group in GROUPS:
            values = [keyed[(after, i)]['groups'][group]['mean_nll'] - keyed[(before, i)]['groups'][group]['mean_nll']
                for i in range(c['documents']) if keyed[(before, i)]['groups'][group]['tokens']]
            deltas[before+'->'+after][group] = dict(documents=len(values), improved_documents=sum(x < 0 for x in values),
                mean_document_delta=float(np.mean(values)), median_document_delta=float(np.median(values)),
                token_weighted_delta=result[after][group]['mean_nll']-result[before][group]['mean_nll'])
    return dict(absolute=result, paired_deltas= deltas)


def run():
    c, view = inspect(); config_sha = sha256(CONFIG); path = RUN / 'job.json'
    old = read_json(path) if path.exists() else {}
    if old and old['config_sha256'] != config_sha: raise ValueError('Prior diagnostic binding differs')
    if old.get('status') == 'complete': print('Completed diagnostic retained; no duplicate GPU'); return
    prior = old.get('GPU_elapsed_seconds', 0.); started, stopped = [None], [False]
    job = dict(status='setup', **identity(), config_sha256=config_sha, started_at=old.get('started_at', now()),
        GPU_elapsed_seconds=prior, GPU_budget_seconds=60, optimizer_updates=0, scientific_teacher_tokens=0,
        protected_test_used=False, restart_command='scripts/run_condition_trainfit_diagnostic.ps1 -Worker')
    for sig in (signal.SIGINT, signal.SIGTERM): signal.signal(sig, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('Interrupted; complete batches retained')
        if started[0] is not None and prior + time.monotonic()-started[0] > 60: raise TimeoutError('Cumulative GPU60s exhausted')
    def heartbeat(**values):
        check(); job.update(heartbeat_at=now(), **values)
        if started[0] is not None: job['GPU_elapsed_seconds'] = prior + time.monotonic()-started[0]
        atomic_json(path, job)
    try:
        heartbeat(stage='setup')
        for relative in (*SOURCES, *c['implementation'], CONFIG.relative_to(ROOT).as_posix()):
            target = RUN / 'source' / relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != (ROOT / relative).read_bytes(): raise ValueError('Source snapshot differs')
            if not target.exists(): shutil.copyfile(ROOT / relative, target)
        torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True)
        rows, checks = [], {}
        with gpu_lock('cuda'):
            started[0] = time.monotonic()
            for arm, ref in c['checkpoints'].items():
                check(); state = torch.load(ref['path'], map_location='cpu', weights_only=False)
                before_rng = rng_state(); model = JMicroModel(state['model_config']).to('cuda').eval()
                model.load_state_dict(state['model'], strict=True)
                before = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
                hook = model.register_forward_pre_hook(lambda *_: check())
                with sdpa_kernel(SDPBackend.MATH):
                    for start in range(0, c['documents'], c['batch']):
                        cases = documents(view, start, min(start+c['batch'], c['documents']))
                        output = RUN / 'outputs' / arm / f'{start:04d}.json'
                        if output.exists():
                            saved = read_json(output)
                            if (saved['config_sha256'] != config_sha or saved['checkpoint_sha256'] != ref['sha256']
                                    or [r['target_sha256'] for r in saved['rows']] != [r['target_sha256'] for r in cases]):
                                raise ValueError('Completed batch binding differs')
                            scored = saved['rows']
                        else:
                            scored = score_batch(model, cases, 'cuda')
                            atomic_json(output, dict(config_sha256=config_sha, checkpoint_sha256=ref['sha256'], rows=scored))
                        rows.extend(dict(checkpoint=arm, **r) for r in scored)
                        heartbeat(status='running', stage=arm, completed_documents=len(rows), total_documents=1536)
                    # Numerical diagnostic, not a replacement for the preserved old numerical gates.
                    one = score_batch(model, documents(view, 0, 1), 'cuda')[0]
                    batched = next(r for r in rows if r['checkpoint'] == arm and r['index'] == 0)
                    spot_delta = max(abs(a-b) for a,b in zip(one['target_nll'], batched['target_nll'], strict=True))
                hook.remove(); restore_rng(before_rng)
                checks[arm] = dict(weights_unchanged=all(torch.equal(before[k], v.detach().cpu()) for k,v in model.state_dict().items()),
                    RNG_restored=equal_state(before_rng, rng_state()), no_gradients=all(p.grad is None for p in model.parameters()),
                    eval_mode=not model.training)
                if not all(checks[arm].values()): raise ValueError('Read-only invariants failed')
                checks[arm]['first_document_batched_vs_single_max_NLL_difference'] = spot_delta
                del state, model, before; gc.collect(); torch.cuda.empty_cache()
                print(json.dumps(dict(checkpoint=arm, complete_documents=512, GPU_seconds=job['GPU_elapsed_seconds'])), flush=True)
            summary = summarize(rows, c); torch.cuda.synchronize(); check()
            elapsed = prior + time.monotonic()-started[0]
            atomic_json(RUN / 'result.json', dict(status='all512_original_targets_3_checkpoints_measured',
                config_sha256=config_sha, checks=checks, summary=summary, GPU_seconds=elapsed, evaluated_documents=1536,
                optimizer_updates=0, scientific_teacher_tokens=0, new_original_tokens=0, protected_test_used=False,
                Base_adopted=False, Chat_started=False, quantization_started=False, requested_five_steps_complete=False,
                quality_criteria_unchanged=True, old_numerical7_preserved=True, limitations=c['limitations'], completed_at=now()))
            heartbeat(status='complete', stage='complete', completed_at=now())
    except BaseException as error:
        job.update(status='failed', error=repr(error)); raise
    finally:
        if started[0] is not None: job['GPU_elapsed_seconds'] = prior + time.monotonic()-started[0]
        atomic_json(path, job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser(); mode = p.add_mutually_exclusive_group()
    mode.add_argument('--freeze', action='store_true'); mode.add_argument('--inspect', action='store_true')
    args = p.parse_args()
    if args.freeze: freeze()
    elif args.inspect:
        c, _ = inspect(); print(json.dumps(dict(status='preflight_passed', documents=512, GPU_budget=60)))
    else: run()
