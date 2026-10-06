"""CPU-only decomposition of completed, raw-bound Base transfer evidence."""
import hashlib
from collections import Counter
import json
import math
from pathlib import Path
import statistics
import sys
import time
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / 'reports/phase6/early-exposure-comparison-20261006'
FINAL = ROOT / 'reports/phase6/original-web-retention-comparison-20261006'
CONFIG = ROOT / 'configs/phase6/early_exposure_comparison.json'
OUTPUT = ROOT / 'reports/phase6/base_transfer_margin_diagnostic.json'
METRICS = ('sum_log_likelihood', 'mean_token_log_likelihood', 'mean_byte_log_likelihood')
REFERENCES = {}
EPS = 1e-9


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path, expected=None):
    path = Path(path)
    digest = sha(path)
    if expected is not None and digest != expected:
        raise ValueError(f'Immutable evidence SHA differs: {path}')
    REFERENCES[str(path)] = digest
    return json.loads(path.read_text(encoding='utf-8'))


def decomposition(margins):
    if len(margins) != 2 or not all(math.isfinite(x) for x in margins):
        raise ValueError('Two finite opposite-label margins required')
    m0, m1 = margins
    bias, sensitivity = (m0 + m1) / 2, (m0 - m1) / 2
    credits = [.5 if abs(m) <= EPS else float(m > 0 if b == 0 else m < 0)
               for b, m in enumerate(margins)]
    same = (m0 > EPS and m1 > EPS) or (m0 < -EPS and m1 < -EPS)
    return dict(margins=margins, candidate_preference_component=bias,
                aligned_context_component=sensitivity, credits=credits,
                both_correct=credits == [1., 1.], neither_correct=credits == [0., 0.],
                any_tie=.5 in credits, same_candidate=same,
                aligned_but_preference_dominates=sensitivity > EPS and same,
                nonpositive_context_component=sensitivity <= 0)


def validate_rows(rows, cases):
    if len(rows) != len(cases) or len({r['index'] for r in rows}) != len(rows):
        raise ValueError('Complete unique raw requests required')
    keyed = {r['index']: r for r in rows}
    if set(keyed) != {c['index'] for c in cases}:
        raise ValueError('Exact case IDs required')
    for c in cases:
        r = keyed[c['index']]
        if (r['target_ids'] != c['target_ids'] or r['target_tokens'] != len(c['target_ids'])
                or r['target_bytes'] != c['target_bytes'] or r['target_bytes'] <= 0
                or len(r['token_nll']) != r['target_tokens']
                or any(not math.isfinite(n) or n < 0 for n in r['token_nll'])
                or not math.isclose(r['log_likelihood'], -sum(r['token_nll']), rel_tol=0, abs_tol=1e-10)):
            raise ValueError('Finite exact target IDs/lengths/NLL required')
    return keyed


def analyze(rows, prepared, terminal):
    cases, families = prepared['cases'], prepared['families']
    keyed = validate_rows(rows, cases)
    case_key = {(c['family'], c['branch'], c['candidate']): c for c in cases}
    if (len(case_key) != len(cases) or len(families) != 128 or len(cases) != 512
            or len({f['index'] for f in families}) != 128):
        raise ValueError('Exactly128 complete two-condition families required')
    pairs = []
    for f in families:
        index = f['index']
        cells = [case_key[(index, b, k)] for b in (0, 1) for k in (0, 1)]
        if any(c['label'] != c['branch'] or c['split'] != f['split'] or c['category'] != f['category']
               or c['id'] != f['id'] for c in cells):
            raise ValueError('Family/label/split differs')
        for k in (0, 1):
            a, b = case_key[(index, 0, k)], case_key[(index, 1, k)]
            if a['target_ids'] != b['target_ids'] or a['outcome'] != b['outcome']:
                raise ValueError('Opposite contexts must use common candidate targets')
        first, second = cells[0]['target_ids'], cells[1]['target_ids']
        common = 0
        while common < min(len(first), len(second)) and first[common] == second[common]:
            common += 1
        if common == min(len(first), len(second)):
            raise ValueError('Candidates need an actual differing token')
        for metric in METRICS:
            values = {}
            for c in cells:
                r = keyed[c['index']]
                divisor = 1 if metric == METRICS[0] else r['target_tokens'] if metric == METRICS[1] else r['target_bytes']
                values[(c['branch'], c['candidate'])] = r['log_likelihood'] / divisor
            d = decomposition([values[(b, 0)] - values[(b, 1)] for b in (0, 1)])
            # Raw autoregressive scores must share the candidate prefix exactly.
            # This is the same context and same preceding tokens, not a new model run.
            for b in (0, 1):
                x, y = (keyed[case_key[(index, b, k)]['index']]['token_nll'] for k in (0, 1))
                if any(not math.isclose(a, z, rel_tol=0, abs_tol=1e-6) for a, z in zip(x[:common], y[:common])):
                    raise ValueError('Common autoregressive prefix scores disagree')
            pairs.append(dict(family=index, id=f['id'], split=f['split'], category=f['category'],
                template_id=f['template_id'], metric=metric, common_prefix_tokens=common,
                candidate_lengths=[len(first), len(second)], equal_target_tokens=len(first) == len(second),
                candidate_EOS_included=3 in first or 3 in second, **d))
    aggregates = {}
    for metric in METRICS:
        aggregates[metric] = {}
        for split in ('all128', 'lexical_holdout', 'structural_holdout'):
            selected = [p for p in pairs if p['metric'] == metric and (split == 'all128' or p['split'] == split)]
            groups = {'all': selected}
            groups.update({cat: [p for p in selected if p['category'] == cat] for cat in sorted({p['category'] for p in selected})})
            aggregates[metric][split] = {}
            for group, ps in groups.items():
                aggregates[metric][split][group] = dict(families=len(ps),
                    both_correct=sum(p['both_correct'] for p in ps), neither_correct=sum(p['neither_correct'] for p in ps),
                    same_candidate=sum(p['same_candidate'] for p in ps), any_tie=sum(p['any_tie'] for p in ps),
                    positive_context_component=sum(p['aligned_context_component'] > 0 for p in ps),
                    aligned_but_preference_dominates=sum(p['aligned_but_preference_dominates'] for p in ps),
                    median_context_component=statistics.median(p['aligned_context_component'] for p in ps),
                    median_abs_preference_component=statistics.median(abs(p['candidate_preference_component']) for p in ps),
                    equal_target_tokens=sum(p['equal_target_tokens'] for p in ps),
                    equal_length_both_correct=sum(p['equal_target_tokens'] and p['both_correct'] for p in ps))
            old = terminal['summary']['aggregate'][metric][split]
            current = aggregates[metric][split]['all']
            if (old['both_correct'] != current['both_correct'] or old['same_unique_candidate'] != current['same_candidate']
                    or old['aligned_context_margin_shift'] != current['positive_context_component']):
                raise ValueError('Reconstructed raw statistics do not reconcile with reviewed terminal')
    return dict(aggregate=aggregates, pairs=pairs, candidate_EOS_included=any(p['candidate_EOS_included'] for p in pairs),
                definition='m0=score(c0|context0)-score(c1|context0), m1 under context1; preference=(m0+m1)/2, sensitivity=(m0-m1)/2. Descriptive algebra, not an unconditional prior or causal decomposition.')


def main():
    started = time.perf_counter()
    c = read(CONFIG)
    result = read(RUN / 'compare-result.json')
    review = read(ROOT / 'reports/phase6/early_exposure_comparison_review.json')
    job = read(RUN / 'job.json')
    if (job['status'] != 'complete' or review['result_sha256'] != sha(RUN / 'compare-result.json')
            or result['config_sha256'] != sha(CONFIG) or review['Base_adopted'] or review['protected_test_used']):
        raise ValueError('Actual terminal raw-bound unqualified Base study required')
    stat = Path(f"/proc/{job['pid']}/stat")
    if stat.exists() and stat.read_text().split()[21] == str(job['start_ticks']):
        raise ValueError('Scientific process still live')
    models = {}
    for suite, key, result_key in (('bridge', 'source_cases', 'transfer'), ('retention', 'retention_cases', 'retention')):
        ref = c['references'][key]
        prepared = read(ref['path'], ref['sha256'])
        models[suite] = {}
        for arm in ('early8M', 'final100M'):
            terminal = result[result_key][arm]
            folder = RUN / 'transfer' / suite / arm if arm == 'early8M' else FINAL / 'transfer' / suite / 'original_web'
            raw_terminal = read(folder / 'result.json')
            if raw_terminal != terminal or terminal['cases_sha256'] != ref['sha256'] or not all(terminal['checks'].values()):
                raise ValueError('Actual completed common-case transfer binding differs')
            rows = []
            for start in range(0, 512, 16):
                batch = read(folder / f'{start:04d}.json')
                if any(batch[k] != terminal[k] for k in ('config_sha256', 'checkpoint_sha256', 'cases_sha256')):
                    raise ValueError('Raw score batch provenance differs')
                rows.extend(batch['rows'])
            models[suite][arm] = analyze(rows, prepared, terminal)
    # These likelihood requests did not score EOS. Use the separately scored
    # fixed byte-dev gold endpoints; no fabricated candidate or next-token EOS.
    endpoints = {}
    devs = {}
    for arm in ('early8M', 'final100M'):
        folder = RUN / 'evaluation/early8M/evaluation' if arm == 'early8M' else FINAL / 'evaluation/original_web/evaluation'
        raw = read(folder / 'body.json')
        if raw['body'] != result['evaluations'][arm]['body']:
            raise ValueError('Actual body evaluation cache differs')
        body = raw['body']; devs[arm] = body['rows']
        if len(body['rows']) != 256 or body['body_bytes'] != 472055:
            raise ValueError('Same fixed256 byte dev required')
        nll = [r['eos_nll'] for r in body['rows']]
        if not all(math.isfinite(v) and v >= 0 for v in nll) or not math.isclose(sum(nll), body['eos_nll'], abs_tol=1e-7):
            raise ValueError('All256 actual gold EOS denominators required')
        endpoints[arm] = dict(documents=256, mean_gold_EOS_nll=statistics.mean(nll),
                             median_gold_EOS_nll=statistics.median(nll))
    if [(r['doc_id'], r['body_tokens'], r['body_bytes']) for r in devs['early8M']] != [(r['doc_id'], r['body_tokens'], r['body_bytes']) for r in devs['final100M']]:
        raise ValueError('Common dev document targets differ')
    endpoints['paired'] = dict(documents_improved=sum(b['eos_nll'] < a['eos_nll'] for a, b in zip(devs['early8M'], devs['final100M'], strict=True)),
        mean_final_minus_early=statistics.mean(b['eos_nll'] - a['eos_nll'] for a, b in zip(devs['early8M'], devs['final100M'], strict=True)))
    source = Path(c['references']['source_cases']['path']).parent
    manifest = read(source / 'manifest.json', result['checkpoints']['final100M']['binding']['positive_manifest_sha256'])
    train = read(source / 'train-source.json', manifest['train_source_sha256'])
    if len(train['rows']) != 2048 or len(train['families']) != 1024:
        raise ValueError('Accepted original selected source required')
    comparison = [r for r in train['rows'] if r['category'] == 'comparison']
    last_entity = []
    for r in comparison:
        a, b = r['facts']['A'], r['facts']['B']
        if r['local_state']['A_length'] == r['local_state']['B_length']:
            raise ValueError('Comparison source unexpectedly tied')
        longer = a if r['local_state']['A_length'] > r['local_state']['B_length'] else b
        if r['outcome'] != longer + 'である。' or r['outcome'] != r['choices'][r['label']]:
            raise ValueError('Train comparator conclusion differs from ground truth')
        last = max((a, b), key=lambda name: r['prefix'].rfind(name))
        last_entity.append(dict(id=r['id'], template_id=r['template_id'], last_entity=last,
                                answer=longer, last_entity_is_answer=last == longer))
    training_orientation = dict(comparison_documents=len(comparison),
        requested_longer_documents=len(comparison), requested_shorter_documents=0,
        last_mentioned_entity_is_answer=sum(r['last_entity_is_answer'] for r in last_entity),
        templates=dict(Counter(r['template_id'] for r in comparison)),
        last_entity_matches_by_template={t: sum(r['last_entity_is_answer'] for r in last_entity if r['template_id'] == t)
                                        for t in sorted({r['template_id'] for r in comparison})},
        conclusion='All accepted comparison-source conclusions select the longer entity. Last-entity frequencies describe training text, not the learned decision rule; no source label errors were found in these grounded comparisons.')
    seconds = time.perf_counter() - started
    if seconds > 30:
        raise RuntimeError('Bounded CPU30s diagnostic exceeded')
    report = dict(status='completed_CPU_raw_transfer_margin_and_gold_endpoint_diagnostic',
        created_at=datetime.now(timezone.utc).isoformat(), CPU_seconds=seconds, GPU_seconds=0,
        scientific_teacher_tokens=0, optimizer_updates=0, models=models, gold_dev_endpoints=endpoints,
        training_orientation=training_orientation,
        source_sha256=sha(Path(__file__)), references=REFERENCES,
        Base_adopted=False, Base_complete=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True, old_numerical7_preserved=True,
        limitations='Posthoc analysis of repeated fixed dev/local generated probes, same one-seed nested trajectory. Components describe conditional scores; no unconditional preference measurement, intervention, capacity conclusion or calibrated causal attribution. Candidate requests omit EOS; gold-dev endpoints do not establish free stopping. Normalized scores are secondary only; original primary/adoption gates unchanged. Retention structural forms overlap training. Do not train on any heldout probes or dev prompts.')
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(CPU_seconds=seconds, models={s: {a: {split: cats['all'] for split, cats in m['aggregate'][METRICS[0]].items()} for a, m in arms.items()} for s, arms in models.items()}, gold_dev_endpoints=endpoints, training_orientation=training_orientation), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
