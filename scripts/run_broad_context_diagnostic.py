"""Read-only context diagnostic on actual broad-material checkpoints, via uv."""
import argparse
from collections import Counter
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import re
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
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.learning_curve import LazyDocumentBlocks
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer, SUPPRESS_IDS
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, restore_rng, seed_all
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive, identity
from run_eos_short_pilot import equal_state

RUN = ROOT / 'reports/phase6/broad-context-diagnostic-20261006'
CONFIG = ROOT / 'configs/phase6/broad_context_diagnostic.json'
COVERAGE = ROOT / 'reports/phase6/textbook-coverage-2b-20261006'
QUANTITY = ROOT / 'reports/phase6/textbook-quantity-comparison-20261006'
COVERAGE_CONFIG = ROOT / 'configs/phase6/textbook_coverage_2b_v2.json'
SOURCES = ('scripts/run_broad_context_diagnostic.py', 'scripts/run_broad_context_diagnostic.ps1',
           'scripts/cached_three_source_index.py', 'scripts/textbook_quantity_trainer.py',
           'src/jmicro/learning_curve.py', 'src/jmicro/eos_pilot.py', 'src/jmicro/tokenizer.py',
           'scripts/phase6_performance.py', 'scripts/run_eos_short_pilot.py')
GENRES = ('web', 'story', 'textbook')


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def check_reference(ref):
    if sha256(Path(ref['path'])) != ref['sha256']:
        raise ValueError('Reference bytes differ: ' + ref['path'])


def validate_case(case, context=1024, max_new=64):
    prefix, gold, preceding = case['prefix_ids'], case['gold_ids'], case['previous_context_ids']
    if (case['split'] != 'train' or case['source'] not in GENRES or not preceding
            or not prefix or prefix[0] != 2 or len(prefix) < 9
            or len(gold) < 2 or gold[-1] != 3
            or any(type(i) is not int or i < 8 or i >= 4096 for i in prefix[1:] + gold[:-1])
            or any(type(i) is not int or not 0 <= i < 4096 for i in preceding)
            or len(preceding) + len(prefix) + max_new > context
            or len(preceding) + len(prefix) + len(gold) - 1 > context):
        raise ValueError('Invalid common train target or context budget')
    if case['body_ids'] != prefix[1:] + gold[:-1]:
        raise ValueError('Prefix/gold do not reconstruct the same train document')


def extract_cases(batch, targets, tags, locations, tok, remaining, seen):
    """Keep first complete eligible docs per genre; no model-dependent selection."""
    selected, skips = [], Counter()
    for row, (x, y, source_tags, location) in enumerate(zip(batch, targets, tags, locations, strict=True)):
        ids = x.tolist() + [2 if int(y[-1]) == -100 else int(y[-1])]
        for start, value in enumerate(ids[:-1]):
            if value != 2 or start == 0:
                continue
            end = next((i for i in range(start + 1, len(ids)) if ids[i] in (2, 3)), None)
            if end is None or ids[end] != 3:
                skips['incomplete_document'] += 1
                continue
            body = ids[start + 1:end]
            genre = GENRES[int(source_tags[start])]
            if remaining[genre] == 0:
                continue
            if len(body) < 16 or any(i < 8 for i in body):
                skips['short_or_structural_body'] += 1
                continue
            document = location(start)
            if document['document_index'] in seen:
                skips['already_selected_train_document'] += 1
                continue
            if document['body_tokens'] != len(body):
                raise ValueError('Packed complete document differs from accepted index')
            length = min(32, len(body) // 2)
            while length >= 8:
                try:
                    prefix_text = tok.decode(body[:length])
                    gold_text = tok.decode(body[length:])
                    text = tok.decode(body)
                    break
                except UnicodeDecodeError:
                    length -= 1
            if length < 8:
                skips['no_complete_utf8_prefix'] += 1
                continue
            case = dict(id=f"train-{document['document_index']}", split='train', source=genre,
                body_ids=body, prefix_ids=[2, *body[:length]], gold_ids=[*body[length:], 3],
                previous_context_ids=ids[:start], prefix_text=prefix_text, gold_text=gold_text,
                text=text, body_text_sha256=hashlib.sha256(text.encode()).hexdigest(),
                packed_row=row, BOS_position=start, **document)
            try:
                validate_case(case)
            except ValueError:
                skips['generation_context_budget'] += 1
                continue
            if any(int(source_tags[i]) != GENRES.index(genre) for i in range(start, end)):
                raise ValueError('Source tags differ within document body/EOS')
            selected.append(case)
            remaining[genre] -= 1
            seen.add(document['document_index'])
    return selected, skips


def freeze():
    if CONFIG.exists():
        inspect(); print('Existing frozen train selection retained'); return
    if (RUN / 'cases.json').exists() or (RUN / 'batches.json').exists():
        raise ValueError('Partial selection exists; inspect and repair instead of resampling')
    prior = read_json(COVERAGE_CONFIG)
    job = read_json(COVERAGE / 'job.json')
    review_path = ROOT / 'reports/phase6/textbook_coverage_2b_review.json'
    review = read_json(review_path)
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Scientific comparison must actually finish first')
    result_path = COVERAGE / 'compare-result.json'
    if (review['result_sha256'] != sha256(result_path) or review['summary']['coherent'] != 14
            or review['eligible_for_final_Base_validation'] or review['protected_test_used']):
        raise ValueError('Diagnostic must bind to the recorded failed Base candidate')
    if prior['implementation'] != implementation_hashes():
        raise ValueError('Existing canonical core implementation differs')
    for relative, digest in prior['source_sha256'].items():
        if sha256(ROOT / relative) != digest:
            raise ValueError('Existing frozen training source differs: ' + relative)
    old_path = QUANTITY / 'compare-result.json'
    check_reference(prior['source_result'])
    old = read_json(old_path); current = read_json(result_path)
    check_reference(prior['parent'])
    parent = torch.load(prior['parent']['path'], map_location='cpu', weights_only=False)
    if parent['sampler']['short'] != prior['actual_parent_cursor']:
        raise ValueError('Shared stable parent sampler differs')
    check_reference(prior['cached_index_ready'])  # fail before any possible original index scan
    view = TrainView(prior['pool']['pool'], prior['pool']['manifest_sha256'])
    view.index = CachedThreeSourceIndex(view)
    if not view.index.cache_reused:
        raise ValueError('Accepted compact index must be reused')
    tok_path = ROOT / 'artifacts/phase2/4096/tokenizer.model'
    tok = Tokenizer(tok_path)
    if view.manifest['tokenizer_sha256'] != sha256(tok_path):
        raise ValueError('Pool tokenizer differs')
    sampler = LazyDocumentBlocks(view, 1024, 42)
    sampler.load_state_dict(prior['actual_parent_cursor'])
    cases, batches, seen, skipped = [], [], set(), Counter()
    remaining = dict.fromkeys(GENRES, 8)
    for batch_number in range(4):
        before = sampler.state_dict()
        block_numbers = sampler.order[sampler.position:sampler.position + 32].tolist()
        if len(block_numbers) != 32:
            raise ValueError('Selection would cross an epoch; do not silently alter plan')
        x, y, _ = sampler.batch(32)
        tags = sampler.last_target_tags.copy()
        locations = []
        for block in block_numbers:
            def locate(start, block=int(block)):
                position = block * 1024 + start
                slot = int(np.searchsorted(sampler.ends, position, side='right'))
                doc = int(sampler.documents[slot])
                document_start = int(sampler.ends[slot] - sampler.lengths[doc])
                if position != document_start:
                    raise ValueError('BOS position differs from shuffled document index')
                return dict(block_number=block, document_index=doc,
                            original_train_offset=int(sampler.offsets[doc]),
                            body_tokens=int(sampler.lengths[doc]) - 2, batch_number=batch_number)
            locations.append(locate)
        kept, reasons = extract_cases(x.numpy(), y.numpy(), tags, locations, tok, remaining, seen)
        cases.extend(kept); skipped.update(reasons)
        batches.append(dict(batch_number=batch_number, before=before, after=sampler.state_dict(),
                            block_numbers=block_numbers, x=x.tolist(), y=y.tolist(), tags=tags.tolist()))
        if not any(remaining.values()):
            break
    if not cases:
        raise ValueError('No common eligible train documents; do not reroll')
    RUN.mkdir(parents=True, exist_ok=True)
    atomic_json(RUN / 'cases.json', cases); atomic_json(RUN / 'batches.json', batches)
    checkpoints = {}
    for name, record in [('oneB', old['decay']['large-1000000000']),
                         ('twoB', current['decay']['large-2000000000'])]:
        checkpoints[name] = dict(path=record['checkpoint'], sha256=record['checkpoint_sha256'])
        check_reference(checkpoints[name])
    c = dict(research_kind='broad_material_packed_vs_standalone_train_context',
        output=str(RUN.relative_to(ROOT)), created_at=now(),
        checkpoints=checkpoints, shared_stable_parent=prior['parent'],
        parent_cursor=prior['actual_parent_cursor'], pool=prior['pool'],
        prepared_tokens=prior['prepared_tokens'], tokenizer=reference(tok_path),
        references=dict(coverage_config=reference(COVERAGE_CONFIG),
            coverage_result=reference(result_path), coverage_review=reference(review_path),
            quantity_result=reference(old_path), compact_index=prior['cached_index_ready']),
        files={name: sha256(RUN / name) for name in ('cases.json', 'batches.json')},
        source_sha256={relative: sha256(ROOT / relative) for relative in SOURCES},
        implementation=implementation_hashes(),
        selection=dict(case_count=len(cases), source_counts=dict(Counter(r['source'] for r in cases)),
            maximum_batches=4, actual_batches=len(batches), batch=32, maximum_per_source=8,
            skipped=dict(skipped), optimizer_independent=True, selection_model_inference=False,
            sampler_after_selection=sampler.state_dict(), context_truncated=False),
        context=1024, max_new_tokens=64, generation_suppression_ids=list(SUPPRESS_IDS),
        seed=42, GPU_budget_seconds=180, optimizer_updates=0, scientific_teacher_tokens=0,
        contexts=['packed', 'standalone'], dtype='bf16', backend='math',
        marker=dict(min_mean_body_nll_advantage_nats=.1, min_fraction_positive=.6,
            interpretation='Local context-dependence marker, not statistical or causal proof'),
        quality_criteria_unchanged=True, old_numerical7_preserved=True,
        Base_adopted=False, Chat_adopted=False, protected_test_used=False,
        requested_five_steps_complete=False,
        limitations='Local train-only selected complete docs, not representative corpus/human quality; prior compact packing comparisons not rerun')
    atomic_json(CONFIG, c)
    inspect()
    print(json.dumps(dict(status='frozen', selection=c['selection'], config_sha256=sha256(CONFIG))), flush=True)


def inspect():
    c = read_json(CONFIG)
    if (c['research_kind'] != 'broad_material_packed_vs_standalone_train_context'
            or c['GPU_budget_seconds'] != 180 or c['optimizer_updates'] != 0
            or c['scientific_teacher_tokens'] != 0 or c['protected_test_used']
            or c['Base_adopted'] or c['Chat_adopted'] or not c['quality_criteria_unchanged']
            or c['contexts'] != ['packed', 'standalone'] or c['context'] != 1024
            or c['max_new_tokens'] != 64 or c['generation_suppression_ids'] != list(SUPPRESS_IDS)):
        raise ValueError('Diagnostic scope changed')
    if c['implementation'] != implementation_hashes():
        raise ValueError('Frozen canonical core implementation differs')
    for relative, digest in c['source_sha256'].items():
        if sha256(ROOT / relative) != digest:
            raise ValueError('Frozen source differs: ' + relative)
    for ref in [c['tokenizer'], c['shared_stable_parent'], *c['checkpoints'].values(), *c['references'].values()]:
        check_reference(ref)
    for name, digest in c['files'].items():
        if sha256(RUN / name) != digest:
            raise ValueError('Frozen train selection bytes differ')
    job = read_json(COVERAGE / 'job.json')
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Previous science not terminal')
    cases = read_json(RUN / 'cases.json')
    if len(cases) != c['selection']['case_count'] or len({r['id'] for r in cases}) != len(cases):
        raise ValueError('Frozen case coverage differs')
    for case in cases:
        validate_case(case)
    if (RUN / 'job.json').exists() and alive(read_json(RUN / 'job.json')):
        raise ValueError('Existing diagnostic process is live')
    return c, cases


def score_targets(logits, gold):
    """Common continuation only; preceding documents and prefix are never scored."""
    if logits.shape[0] != len(gold) or len(gold) < 2 or gold[-1] != 3:
        raise ValueError('Gold alignment/EOS differs')
    if not bool(torch.isfinite(logits).all()):
        raise ValueError('Nonfinite inference logits')
    labels = torch.tensor(gold, device=logits.device)
    nll = F.cross_entropy(logits.float(), labels, reduction='none')
    rank = (logits > logits.gather(-1, labels[:, None])).sum(-1) + 1
    return dict(target_ids=gold, target_nll=nll.tolist(), target_rank=rank.tolist(),
        body_tokens=len(gold) - 1, body_nll_sum=float(nll[:-1].sum()), body_nll_mean=float(nll[:-1].mean()),
        first_target_nll=float(nll[0]), first_target_rank=int(rank[0]),
        EOS_nll=float(nll[-1]), EOS_rank=int(rank[-1]), EOS_top1=int(rank[-1]) == 1)


@torch.inference_mode()
def evaluate_case(model, tok, case, context, device, check):
    validate_case(case)
    prefix = case['prefix_ids']
    if context == 'packed':
        prefix = case['previous_context_ids'] + prefix
    elif context != 'standalone':
        raise ValueError('Unknown context condition')
    gold = case['gold_ids']
    current = torch.tensor([prefix + gold[:-1]], device=device)
    check()
    with torch.autocast(device, dtype=torch.bfloat16, enabled=device == 'cuda'):
        logits = model(current).logits[0, len(prefix) - 1:len(prefix) - 1 + len(gold)]
    scored = score_targets(logits, gold)
    generated, cache = [], None
    current = torch.tensor([prefix], device=device)
    for _ in range(64):
        check()
        with torch.autocast(device, dtype=torch.bfloat16, enabled=device == 'cuda'):
            output = model(current, cache=cache, use_cache=True)
        cache = output.cache
        scores = output.logits[0, -1].clone()
        if not bool(torch.isfinite(scores).all()):
            raise ValueError('Nonfinite greedy logits')
        scores[list(SUPPRESS_IDS)] = -torch.inf
        token = int(scores.argmax()); generated.append(token)
        if token == 3:
            break
        current = torch.tensor([[token]], device=device)
    raw = tok.decode_bytes(generated)
    try:
        text = raw.decode(); valid = True
    except UnicodeDecodeError:
        text = raw.decode(errors='replace'); valid = False
    return dict(id=case['id'], source=case['source'], context=context, prefix_ids=prefix,
        prefix_text=case['prefix_text'], gold_text=case['gold_text'], scored=scored,
        generated_ids=generated, generated_bytes_hex=raw.hex(), text=text, valid_utf8=valid,
        EOS=generated[-1] == 3, stop_reason='stop_id' if generated[-1] == 3 else 'max_new_tokens',
        repetition=bool(re.search(r'(.{2,}?)\1\1', text, flags=re.DOTALL)),
        role_leak=any(i in (4, 5, 6, 7) for i in generated), empty=not text.strip(),
        suppressed=True, suppression_ids=list(SUPPRESS_IDS), decoding='greedy', seed=42)


def summarize(rows, cases, marker):
    expected = {(arm, r['id'], context) for arm in ('oneB', 'twoB') for r in cases
                for context in ('packed', 'standalone')}
    keyed = {(r['checkpoint'], r['id'], r['context']): r for r in rows}
    if len(keyed) != len(rows) or set(keyed) != expected:
        raise ValueError('Incomplete or duplicate checkpoint/context cases')
    out = {}
    for arm in ('oneB', 'twoB'):
        packed = [keyed[(arm, c['id'], 'packed')] for c in cases]
        single = [keyed[(arm, c['id'], 'standalone')] for c in cases]
        if any(p['scored']['target_ids'] != s['scored']['target_ids'] for p, s in zip(packed, single, strict=True)):
            raise ValueError('Context conditions scored different targets')
        differences = [s['scored']['body_nll_mean'] - p['scored']['body_nll_mean']
                       for p, s in zip(packed, single, strict=True)]
        mean = float(np.mean(differences)); positive = sum(d > 0 for d in differences) / len(cases)
        conditions = {}
        for name, values in [('packed', packed), ('standalone', single)]:
            tokens = sum(r['scored']['body_tokens'] for r in values)
            conditions[name] = dict(body_teacher_forcing_NLL_per_token=sum(r['scored']['body_nll_sum'] for r in values) / tokens,
                common_body_tokens=tokens, gold_EOS_top1=sum(r['scored']['EOS_top1'] for r in values),
                greedy_EOS=sum(r['EOS'] for r in values), greedy_repetition=sum(r['repetition'] for r in values),
                Unicode_failures=sum(not r['valid_utf8'] for r in values),
                role_leaks=sum(r['role_leak'] for r in values), empty=sum(r['empty'] for r in values))
        out[arm] = dict(case_count=len(cases), contexts=conditions,
            paired_body_nll_advantage_of_packed=differences,
            mean_case_body_nll_advantage_of_packed=mean, fraction_positive=positive,
            local_context_dependence_marker=mean >= marker['min_mean_body_nll_advantage_nats']
                and positive >= marker['min_fraction_positive'],
            marker_is_not_causal_or_statistical_proof=True)
    return out


def run():
    c, cases = inspect()
    job_path = RUN / 'job.json'
    old = read_json(job_path) if job_path.exists() else {}
    if old and old['config_sha256'] != sha256(CONFIG):
        raise ValueError('Prior diagnostic recipe differs')
    if old.get('status') == 'complete':
        print('Completed diagnostic retained; no duplicate GPU'); return
    prior = old.get('GPU_elapsed_seconds', 0.)
    started, stopped = [None], [False]
    job = dict(status='setup', **identity(), started_at=old.get('started_at', now()),
        config_sha256=sha256(CONFIG), GPU_elapsed_seconds=prior, GPU_budget_seconds=180,
        optimizer_updates=0, scientific_teacher_tokens=0, protected_test_used=False,
        restart_command='scripts/run_broad_context_diagnostic.ps1 -Worker')
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Interrupted; completed cases retained')
        if started[0] is not None and prior + time.monotonic() - started[0] > 180:
            raise TimeoutError('Cumulative diagnostic GPU180s budget exhausted')
    def heartbeat(**values):
        check(); job.update(heartbeat_at=now(), **values)
        if started[0] is not None:
            job['GPU_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(job_path, job)
    try:
        heartbeat(stage='setup')
        for relative in (*SOURCES, *c['implementation'], CONFIG.relative_to(ROOT).as_posix()):
            target = RUN / 'source' / relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                if target.read_bytes() != (ROOT / relative).read_bytes():
                    raise ValueError('Saved source snapshot differs')
            else:
                shutil.copyfile(ROOT / relative, target)
        torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True)
        tok = Tokenizer(c['tokenizer']['path'])
        rows, checks = [], {}
        with gpu_lock('cuda'):
            started[0] = time.monotonic()
            for arm, ref in c['checkpoints'].items():
                check(); state = torch.load(ref['path'], map_location='cpu', weights_only=False)
                before_rng = rng_state()
                model = JMicroModel(state['model_config']).to('cuda').eval()
                model.load_state_dict(state['model'], strict=True)
                before = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
                hook = model.register_forward_pre_hook(lambda *_: check())
                with sdpa_kernel(SDPBackend.MATH):
                    for case in cases:
                        for context in c['contexts']:
                            path = RUN / 'outputs' / arm / (case['id'] + '-' + context + '.json')
                            if path.exists():
                                record = read_json(path)
                                if (record['config_sha256'] != sha256(CONFIG)
                                        or record['checkpoint_sha256'] != ref['sha256']
                                        or record['case_sha256'] != hashlib.sha256(json.dumps(case, sort_keys=True).encode()).hexdigest()):
                                    raise ValueError('Completed case binding differs')
                            else:
                                record = evaluate_case(model, tok, case, context, 'cuda', check)
                                record.update(checkpoint=arm, checkpoint_sha256=ref['sha256'],
                                    config_sha256=sha256(CONFIG),
                                    case_sha256=hashlib.sha256(json.dumps(case, sort_keys=True).encode()).hexdigest())
                                path.parent.mkdir(parents=True, exist_ok=True); atomic_json(path, record)
                            rows.append(record)
                            heartbeat(status='running', stage=arm, completed_outputs=len(rows),
                                      total_outputs=len(cases) * 4)
                            if len(rows) % 8 == 0:
                                print(json.dumps(dict(checkpoint=arm, completed_outputs=len(rows), GPU_seconds=job['GPU_elapsed_seconds'])), flush=True)
                hook.remove()
                checks[arm] = dict(weights_unchanged=all(torch.equal(before[k], v.detach().cpu()) for k, v in model.state_dict().items()),
                    eval_mode=not model.training, no_gradients=all(p.grad is None for p in model.parameters()))
                restore_rng(before_rng)
                checks[arm]['RNG_restored'] = equal_state(before_rng, rng_state())
                if not all(checks[arm].values()):
                    raise ValueError('Read-only model invariants failed')
                del model, state, before; gc.collect(); torch.cuda.empty_cache()
            summary = summarize(rows, cases, c['marker'])
            check()
            result = dict(status='all_common_train_contexts_measured', config_sha256=sha256(CONFIG),
                cases_sha256=c['files']['cases.json'], rows=rows, summary=summary, checks=checks,
                GPU_seconds=prior + time.monotonic() - started[0], optimizer_updates=0, scientific_teacher_tokens=0,
                Base_adopted=False, Chat_adopted=False, protected_test_used=False,
                requested_five_steps_complete=False, independent_human_blind=False,
                quality_criteria_unchanged=True, old_numerical7_preserved=True,
                completed_at=now(), limitations=c['limitations'])
            atomic_json(RUN / 'result.json', result)
            heartbeat(status='complete', stage='complete', completed_at=now())
    except BaseException as error:
        job.update(status='failed', error=repr(error)); raise
    finally:
        if started[0] is not None:
            job['GPU_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(job_path, job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned Python3.12.7 required; launch through uv')
    parser = argparse.ArgumentParser(); mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--freeze', action='store_true'); mode.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    if args.freeze:
        freeze()
    elif args.inspect:
        c, cases = inspect(); print(json.dumps(dict(status='preflight_passed', cases=len(cases), GPU_limit=180)))
    else:
        run()
