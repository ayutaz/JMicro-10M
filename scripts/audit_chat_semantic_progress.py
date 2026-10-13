"""Observe all required saved-point evidence without grading or launching GPUs.

Missing evidence remains pending. Recompute raw-bound reviews and NLL totals;
this observer never adopts a model or declares the four-item goal complete.
"""
from collections import Counter
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.chat_review import content_review
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from chat_semantic_contract import RUN, LIMITS, preflight, reference, require_ref
from evaluate_chat_semantic import nll_windows
from phase6_performance import alive
from review_chat_semantic import get_items, fingerprint


def validate_generation_binding(evaluation, config, checkpoint, arm, point, suite):
    binding = evaluation['binding']
    assert binding['checkpoint'] == checkpoint['path']
    assert binding['checkpoint_sha256'] == checkpoint['sha256']
    assert binding['config_sha256'] == config['config_sha256']
    assert binding['stage'] == arm + '-' + point
    assert binding['source_sha256'] == config['source_sha256']
    assert binding['implementation'] == config['implementation']
    assert binding['tokenizer_sha256'] == config['tokenizer']['sha256']
    assert binding['suite_sha256'] == config['suites'][suite]['sha256']
    assert (binding['dtype'], binding['backend'], binding['decoding'], binding['evaluation_seed']) == (
        'bf16', 'math', 'greedy', 42)


def validate_nll(result, config, checkpoint, fixed):
    assert result['status'] == 'complete'
    assert result['binding'] == dict(config_sha256=config['config_sha256'],
                                    checkpoint=checkpoint, fixed_targets=config['fixed_NLL'])
    assert result['provided_gold_history'] is True
    assert result['own_generated_quality'] is False and result['protected_TEST_used'] is False
    rows = result['targets']
    assert len(rows) == len(fixed) == 2554 and len({r['id'] for r in rows}) == 2554
    for row, (target, _, labels) in zip(rows, fixed, strict=True):
        assert (row['id'], row['dataset'], row['body_bytes']) == (
            target['id'], target['dataset'], target['body_bytes'])
        assert row['body_teachers'] == int((labels >= 8).sum()) > 0
        assert row['EOT_teachers'] == int((labels == 7).sum()) == 1
        assert all(math.isfinite(row[k]) and row[k] >= 0 for k in ('body_NLL', 'EOT_NLL'))
    counts = Counter(r['dataset'] for r in rows)
    assert counts == {'S0_TRAIN': 112, 'S1_TRAIN': 112, 'new_DEV': 80, 'RPC_DEV': 2250}
    assert set(result['summaries']) == set(counts)
    for dataset in counts:
        selected = [row for row in rows if row['dataset'] == dataset]
        sums = {key: sum(row[key] for row in selected) for key in (
            'body_NLL', 'EOT_NLL', 'body_teachers', 'EOT_teachers', 'body_bytes')}
        expected = dict(sums, targets=len(selected),
                        body_mean_NLL=sums['body_NLL'] / sums['body_teachers'],
                        EOT_mean_NLL=sums['EOT_NLL'] / sums['EOT_teachers'],
                        body_BPB=sums['body_NLL'] / sums['body_bytes'] / math.log(2))
        assert result['summaries'][dataset] == expected
    return dict(targets=len(rows), datasets=dict(counts),
                summaries=result['summaries'], mathematical_totals_verified=True)


def main():
    config, tok, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    fixed = nll_windows(config, tok)
    points = [('parent', 't0')] + [(arm, point) for arm in ('S0', 'S1') for point in ('t1', 't2', 't3')]
    reuse = read_json(require_ref(config['historical_control_evidence']))
    checkpoints = {'S0': reuse['checkpoints'], 'S1': read_json(RUN/'S1/checkpoints.json') if (RUN/'S1/checkpoints.json').exists() else {}}
    reviews, nlls, pending = {}, {}, []
    item_cache = {}

    def evidence(path):
        path = Path(path)
        if path not in item_cache:
            item_cache[path] = get_items(path)
        return item_cache[path]

    for arm, point in points:
        checkpoint = config['parent'] if arm == 'parent' else checkpoints[arm].get(point)
        if checkpoint is None:
            pending.append(f'{arm}/{point} learned checkpoint')
        nll_path = RUN / 'NLL' / arm / (point + '.json')
        if checkpoint is not None and nll_path.exists():
            nlls[arm + '-' + point] = dict(reference=reference(nll_path),
                                         **validate_nll(read_json(nll_path), config, checkpoint, fixed))
        else:
            pending.append(f'NLL/{arm}/{point} complete 2554-target result')
        for suite in ('new', 'previous', 'old'):
            directory = RUN / 'evaluation' / arm / point / suite / 'greedy'
            raw_path, notes_path, review_path = [directory / name for name in ('result.json', 'notes.json', 'review.json')]
            if checkpoint is None or not all(p.exists() for p in (raw_path, notes_path, review_path)):
                pending.append(f'{arm}/{point}/{suite} complete raw/219 judgments/review')
                continue
            evaluation, items = evidence(raw_path)
            validate_generation_binding(evaluation, config, checkpoint, arm, point, suite)
            notes = read_json(notes_path)
            review = content_review(evaluation, sha256(raw_path), notes, items)
            assert json.loads(json.dumps(review)) == read_json(review_path)
            judgments = {row['key']: row for row in notes['judgments']}
            reused = 0
            for key, judgment in judgments.items():
                provenance = judgment.get('reuse')
                if provenance is None:
                    continue
                assert provenance['fingerprint'] == fingerprint(items[key])
                if 'packet_key' in provenance:
                    original = judgments[provenance['packet_key']]
                    assert fingerprint(items[provenance['packet_key']]) == fingerprint(items[key])
                else:
                    source = provenance['source_notes']
                    source_path = require_ref(source)
                    source_notes = read_json(source_path)
                    source_raw, source_items = evidence(source_path.with_name('result.json'))
                    content_review(source_raw, sha256(source_path.with_name('result.json')), source_notes, source_items)
                    original = next(row for row in source_notes['judgments'] if row['key'] == source['key'])
                    assert fingerprint(source_items[source['key']]) == fingerprint(items[key])
                assert all(judgment[k] == original[k] for k in ('grammar', 'relevance', 'context', 'rationale'))
                reused += 1
            matched = [item for item in items.values() if item.get('final_turn')]
            assert len(matched) == 24
            provided = {item['id']: judgments[item['key']] for item in items.values() if item['condition'] == 'suppressed'}
            reviews[arm + '-' + point + '-' + suite] = dict(
                raw=reference(raw_path), notes=reference(notes_path), review=reference(review_path),
                judgments=len(judgments), reused_with_verified_provenance=reused,
                summaries=review['summaries'], mechanical={name: evaluation[name] for name in (
                    'primary', 'role_control', 'own_history_all_turns')},
                matched24_provided_context2=sum(provided[item['id']]['context'] == 2 for item in matched),
                matched24_own_context2=review['summaries']['own_history_final24']['context_score2'])
    ledger = read_json(RUN / 'GPU_ledger.json') if (RUN/'GPU_ledger.json').exists() else dict(limits=LIMITS,total_limit=21600,entries=[])
    assert ledger['limits'] == LIMITS and ledger['total_limit'] == 21600
    charged = sum(row['charged_seconds'] for row in ledger['entries'])
    assert charged <= 21600
    assert all(sum(row['charged_seconds'] for row in ledger['entries'] if row['category'] == category) <= cap
               for category, cap in LIMITS.items())
    control_job=read_json(require_ref(reuse['original_job']))
    assert control_job['status']=='learning_complete' and not alive(control_job)
    jobs={'S0':dict(status='historical_learning_complete',currently_alive=False,
                   reference=reuse['original_job'],new_learning_updates=0)}
    job_path=RUN/'S1/job.json'
    if job_path.exists():
        job=read_json(job_path)
        jobs['S1']=dict(status=job['status'],currently_alive=alive(job),reference=reference(job_path))
    else:
        jobs['S1']=dict(status='not_started',currently_alive=False)
    if not (RUN/'S1/training_audit.json').exists():
        pending.append('S1 final complete-state/consumption audit')
    for relative in ('selection.json', 'final_analysis.json'):
        if not (RUN / relative).exists():
            pending.append(relative)
    output = dict(observed_at=now(), observer=reference(Path(__file__)), config=reference(Path(config['config_path'])),
                  reviewed_suites=len(reviews), required_suites=21,
                  content_judgments=sum(row['judgments'] for row in reviews.values()), required_judgments=4599,
                  fixed_NLL_points=len(nlls), required_fixed_NLL_points=7,
                  reviews=reviews, fixed_NLL=nlls, pending=pending,
                  jobs=jobs, GPU_charged_including_running_heartbeat=charged,
                  status='continue', all_first_comparison_raw_reviews_present=len(reviews) == 21,
                  overall_goal_complete=False, Base_adopted=False, Chat_adopted=False, protected_TEST_used=False,
                  limitation='Observation validates existing outputs; conditional branches and final completion require separate audit.')
    atomic_json(RUN / 'progress_audit.json', output)
    print(json.dumps({key: output[key] for key in (
        'status', 'reviewed_suites', 'content_judgments', 'fixed_NLL_points', 'pending', 'overall_goal_complete')}, ensure_ascii=False))


if __name__ == '__main__':
    main()
