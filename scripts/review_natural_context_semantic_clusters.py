"""Supplement saved native semantic scores with exact-content clustered CIs.

Keep all192 scores and weights. Repeated content under other IDs does not add
independent bootstrap clusters. This reads completed DEV caches only and does
not replace original scores, acceptance gates, or Base adoption evidence.
"""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.japanese_evaluation import clustered_ci
from phase6_performance import alive
from review_teacher_semantic_signal import exact_content_families
from teacher_semantic_signal import dev_cases
from review_natural_context_contrast import ARMS, CONFIG, RUN

INPUT_KEYS = ('id', 'family', 'category', 'split', 'context', 'choices', 'label')


def validate_cached(cached, trained, expected=192):
    binding = json.dumps(dict(binding=trained['binding'], checkpoint_sha256=trained['checkpoint_sha256']), sort_keys=True)
    rows = cached['rows']
    if (trained['status'] != 'complete' or cached['complete'] is not True or cached['expected'] != expected
            or cached['binding'] != binding or len(rows) != expected or len({r['id'] for r in rows}) != expected
            or any(r['split'] != 'dev' or not math.isfinite(r['credit']) or not 0 <= r['credit'] <= 1 for r in rows)):
        raise ValueError('Complete distinct-ID checkpoint-bound DEV semantic cache required')
    return rows


def summary(rows):
    groups, keys, aliases = exact_content_families(rows)
    mapped = [{**r, 'family': keys[r['family']]} for r in rows]
    both = [dict(id=f, family=keys[f], credit=float(all(r['credit'] == 1 for r in pair)))
            for f, pair in groups.items()]
    categories = {category: clustered_ci([r for r in mapped if r['category'] == category])
                  for category in sorted({r['category'] for r in rows})}
    return dict(cases=len(rows), nominal_families=len(groups), exact_content_pair_clusters=len(aliases),
        exact_alias_groups=[v for v in aliases.values() if len(v) > 1],
        original_nominal_accuracy=clustered_ci(rows), content_cluster_accuracy=clustered_ci(mapped),
        both_contexts_hard_correct=clustered_ci(both), categories=categories,
        all_original_example_weights_retained=True)


def require_same_inputs(control, candidate):
    left, right = ({r['id']: r for r in rows} for rows in (control, candidate))
    if set(left) != set(right) or any({k: left[i][k] for k in INPUT_KEYS} !=
                                     {k: right[i][k] for k in INPUT_KEYS} for i in left):
        raise ValueError('All paired IDs, contexts, choices and gold labels must match')
    return left, right


def paired(control, candidate):
    left, right = require_same_inputs(control, candidate)
    _, keys, aliases = exact_content_families(control)
    rows = [dict(id=i, family=keys[left[i]['family']], difference=right[i]['credit'] - left[i]['credit'])
            for i in sorted(left)]
    return dict(candidate_minus_control=clustered_ci(rows, key='difference'),
                exact_content_pair_clusters=len(aliases), cases=len(rows),
                new_acceptance_gate=False)


def load_arm(arm):
    path = RUN / f'evaluation/{arm}/evaluation/semantics.json'
    trained = read_json(RUN / arm / 'train-result.json')
    rows = validate_cached(read_json(path), trained)
    c = read_json(CONFIG)
    if trained['binding']['config_sha256'] != sha256(CONFIG):
        raise ValueError('Scientific recipe differs')
    source = ROOT / c['evaluation']['semantic_suite']
    if sha256(source) != c['evaluation']['semantic_sha256']:
        raise ValueError('Frozen semantic suite differs')
    original, selection = dev_cases(source)
    require_same_inputs(original, rows)
    return rows, dict(path=str(path), sha256=sha256(path), checkpoint_sha256=trained['checkpoint_sha256'],
        suite=str(source.relative_to(ROOT)), suite_sha256=sha256(source), DEV_selection=selection)


def main(arm):
    if arm:
        rows, reference = load_arm(arm)
        report = dict(arm=arm, reference=reference, summary=summary(rows))
        destination = ROOT / f'reports/phase6/natural_context_contrast_{arm}_semantic_clusters.json'
    else:
        job = read_json(RUN / 'job.json')
        if job['status'] != 'complete' or alive(job):
            raise ValueError('Both scientific arms must finish and actual process exit before comparison')
        left, a = load_arm('CE')
        right, b = load_arm('contrast')
        report = dict(references={'CE': a, 'contrast': b}, summaries={'CE': summary(left), 'contrast': summary(right)},
                      paired=paired(left, right))
        destination = ROOT / 'reports/phase6/natural_context_contrast_paired_semantic_clusters.json'
    report.update(created_at=now(), scientific_config_sha256=sha256(CONFIG), helper_sha256=sha256(Path(__file__)),
        alias_helper_sha256=sha256(ROOT / 'scripts/review_teacher_semantic_signal.py'),
        new_GPU_seconds=0, optimizer_updates=0, original_outputs_and_gates_unchanged=True,
        Base_complete=False, Chat_started=False, quantization_started=False,
        limitations='All original case weights retained; exact aliases are clustered, not counted as independent cases. '
                    'Other template correlations remain. CIs describe this constructed DEV packet, not natural Japanese '
                    'population accuracy. No protected TEST source file is opened by this supplement.')
    if destination.exists():
        raise ValueError('Preserve original semantic supplement')
    atomic_json(destination, report)
    detail = report.get('summary')
    print(json.dumps(dict(arm=arm, cases=detail['cases'] if detail else None,
        exact_content_pair_clusters=detail['exact_content_pair_clusters'] if detail else None,
        accuracy=detail['content_cluster_accuracy'] if detail else None, paired=report.get('paired')), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser()
    parser.add_argument('--arm', choices=ARMS)
    args = parser.parse_args()
    main(args.arm)
