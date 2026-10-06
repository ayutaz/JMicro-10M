"""Reuse completed dev scores to measure context sensitivity; no GPU or learning."""
import json
import math
from pathlib import Path
import statistics
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from phase6_performance import alive


def pair_categories(rows):
    families = {}
    for row in rows:
        if row['split'] != 'dev' or type(row['label']) is not int or row['label'] not in (0, 1):
            raise ValueError('Only fixed binary dev scores accepted')
        if len(row['choices']) != 2 or len(row['scores']) != 2 or any(not math.isfinite(x) for x in row['scores']):
            raise ValueError('Binary finite scores required')
        winners = {i for i, value in enumerate(row['scores']) if value == max(row['scores'])}
        expected = int(row['label'] in winners) / len(winners)
        if row['credit'] != expected:
            raise ValueError('Fractional tie credit differs from actual scores')
        families.setdefault(row['family'], []).append(row)
    categories = {}
    for family, pair in families.items():
        if (len(pair) != 2 or {r['label'] for r in pair} != {0, 1}
                or len({r['id'] for r in pair}) != 2 or pair[0]['context'] == pair[1]['context']
                or pair[0]['choices'] != pair[1]['choices'] or pair[0]['category'] != pair[1]['category']):
            raise ValueError('Complete opposite-label family with shared candidates required')
        pair.sort(key=lambda r: r['label'])
        winners = [{i for i, score in enumerate(r['scores']) if score == max(r['scores'])} for r in pair]
        margins = [r['scores'][0] - r['scores'][1] for r in pair]
        record = dict(family=family, ids=[r['id'] for r in pair],
            credits=[r['credit'] for r in pair], margins_candidate0_minus1=margins,
            context_margin_shift=margins[0] - margins[1],
            both_correct=all(r['credit'] == 1 for r in pair),
            neither_correct=all(r['credit'] == 0 for r in pair),
            has_tie=any(len(w) != 1 for w in winners),
            same_unique_prediction=all(len(w) == 1 for w in winners) and winners[0] == winners[1],
            unique_prediction_changes=all(len(w) == 1 for w in winners) and winners[0] != winners[1])
        categories.setdefault(pair[0]['category'], []).append(record)
    return {category: dict(families=len(pairs), examples=2 * len(pairs),
        accuracy=sum(sum(p['credits']) for p in pairs) / (2 * len(pairs)),
        both_correct=sum(p['both_correct'] for p in pairs),
        neither_correct=sum(p['neither_correct'] for p in pairs),
        same_unique_prediction=sum(p['same_unique_prediction'] for p in pairs),
        unique_prediction_changes=sum(p['unique_prediction_changes'] for p in pairs),
        families_with_ties=sum(p['has_tie'] for p in pairs),
        aligned_context_margin_shift=sum(p['context_margin_shift'] > 0 for p in pairs),
        median_context_margin_shift=statistics.median(p['context_margin_shift'] for p in pairs),
        pairs=pairs) for category, pairs in sorted(categories.items())}


def main():
    started = time.perf_counter()
    run = ROOT / 'reports/phase6/story-weight-comparison-20261006'
    job = read_json(run / 'job.json'); review = read_json(run / 'review.json')
    result = read_json(run / 'compare-result.json')
    if (job['status'] != 'complete' or alive(job) or review['result_sha256'] != sha256(run / 'compare-result.json')
            or review['new_scientific_teacher_tokens'] != 200000000 or review['protected_test_used']):
        raise ValueError('Actual completed reviewed study required')
    suite = ROOT / 'eval/japanese_semantics_v2_1.jsonl'
    config = read_json(ROOT / 'configs/phase6/story_weight_comparison.json')
    base = read_json(Path(config['original_config']['path']))
    if sha256(suite) != base['evaluation']['semantic_sha256']:
        raise ValueError('Fixed dev suite changed')
    cases = {r['id']: r for r in (json.loads(s) for s in suite.read_text().splitlines()) if r['split'] == 'dev'}
    sources = {arm: (run / f'evaluation/{arm}/evaluation/semantics.json',
                    result['checkpoints'][arm]['checkpoint_sha256']) for arm in ('control', 'story20')}
    sources['parent2B'] = (ROOT / 'reports/phase6/textbook-coverage-2b-20261006/evaluation/large-2000000000/evaluation/semantics.json',
                          config['parent']['sha256'])
    models = {}; references = {}
    for model, (path, checkpoint_sha) in sources.items():
        raw = read_json(path); binding = json.loads(raw['binding']); rows = raw['rows']
        if (not raw['complete'] or raw['expected'] != 192 or len(rows) != 192
                or binding['checkpoint_sha256'] != checkpoint_sha
                or len({r['id'] for r in rows}) != 192 or {r['id'] for r in rows} != set(cases)
                or any(any(r[k] != cases[r['id']][k] for k in ('family', 'category', 'split', 'context', 'choices', 'label')) for r in rows)):
            raise ValueError('Actual fixed192/weight/context binding differs')
        models[model] = pair_categories(rows)
        if (set(models[model]) != {'negation','quantity','time','comparison','coreference','causality'}
                or any(c['families'] != 16 for c in models[model].values())
                or not math.isclose(sum(r['credit'] for r in rows) / 192,
                                    raw['summary']['primary']['accuracy']['point'], abs_tol=1e-12)):
            raise ValueError('Actual six categories/96 families/accuracy differs')
        references[model] = dict(path=str(path), sha256=sha256(path), checkpoint_sha256=checkpoint_sha)
    report = dict(status='completed_fixed_dev_condition_pair_analysis', models=models, references=references,
        suite_sha256=sha256(suite), study_review_sha256=sha256(run / 'review.json'),
        script_sha256=sha256(Path(__file__)), created_at=now(), CPU_seconds=time.perf_counter() - started,
        actual_GPU_seconds=0, scientific_teacher_tokens=0, prepared_tokens=0, protected_test_used=False,
        Base_adopted=False, Chat_adopted=False, requested_five_steps_complete=False,
        limitations='Reuse of fixed dev96 paired families, one learned seed. Same prediction after a context change is descriptive evidence of candidate preference on these examples, not proof of missing attention or model capacity limits. Positive margin shift is not correct generation. No new training or test; do not train on these evaluation prompts.')
    write_json(ROOT / 'reports/phase6/story_weight_condition_pair_analysis.json', report)
    print(json.dumps({m: {k: {key: val for key, val in v.items() if key != 'pairs'} for k, v in cats.items()}
                      for m, cats in models.items()}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
