"""Paired context/prior accounting; a diagnostic, never an adoption metric."""
import copy
import math
import statistics

METRICS = ('sum_log_likelihood', 'mean_token_log_likelihood', 'mean_byte_log_likelihood')


def request(row, neutral=False):
    ids, target, cut = row['ids'], row['target_ids'], row['context_tokens']
    if (type(cut) is not int or not 1 <= cut < len(ids) or ids[0] != 2
            or not target or ids[cut:] != target
            or any(type(v) is not int or not 0 < v < 4096 for v in ids)
            or type(row['target_bytes']) is not int or row['target_bytes'] <= 0):
        raise ValueError('Exact BOS/input/target suffix/byte denominator required')
    out = copy.deepcopy(row)
    if neutral:
        out.update(ids=[2, *target], context_tokens=1, original_prefix=row.get('prefix'),
            prefix='', diagnostic_context_kind='BOS-only')
    else:
        out['diagnostic_context_kind'] = 'original'
    if out['ids'][out['context_tokens']:] != target or out['target_ids'] != target:
        raise ValueError('Never change a scored target span')
    return out


def index_cases(cases, count):
    indexed = {(c['family'], c['branch'], c['candidate']):c for c in cases}
    expected = {(f,b,k) for f in range(count) for b in (0,1) for k in (0,1)}
    if len(cases) != 4*count or len(indexed) != len(cases) or set(indexed) != expected:
        raise ValueError('Every complete opposite-context family required')
    for c in cases:
        request(c)
        if c['label'] != c['branch']:
            raise ValueError('Opposite branch labels must be retained')
    for f in range(count):
        for k in (0,1):
            a,b = indexed[(f,0,k)], indexed[(f,1,k)]
            if (a['target_ids'] != b['target_ids'] or a['target_bytes'] != b['target_bytes']
                    or a['outcome'] != b['outcome']):
                raise ValueError('Same candidates across both context poles required')
    return indexed


def validate_scores(scores, cases):
    if len(scores) != len(cases):
        raise ValueError('Every request score required')
    for s,c in zip(scores,cases,strict=True):
        if (s['index'] != c['index'] or s['target_ids'] != c['target_ids']
                or s['target_tokens'] != len(c['target_ids']) or s['target_bytes'] != c['target_bytes']
                or len(s['token_nll']) != s['target_tokens']
                or not all(math.isfinite(n) and n >= 0 for n in s['token_nll'])
                or not math.isclose(s['log_likelihood'], -sum(s['token_nll']), abs_tol=1e-10)):
            raise ValueError('Finite scores with identical target IDs/counts/bytes required')


def metric(row, name):
    if name not in METRICS:
        raise ValueError('Fixed metrics only')
    value = row['log_likelihood']
    return value if name == METRICS[0] else value/(row['target_tokens'] if name == METRICS[1] else row['target_bytes'])


def credits(margins):
    return [.5 if abs(v) <= 1e-9 else float(v > 0 if branch == 0 else v < 0)
        for branch,v in enumerate(margins)]


def family_rows(original, neutral, prepared):
    cases, families = prepared['cases'], prepared['families']
    indexed = index_cases(cases, len(families))
    validate_scores(original,cases)
    validate_scores(neutral,[request(c,True) for c in cases])
    scores = [{s['index']:s for s in rows} for rows in (original,neutral)]
    rows = []
    for f in families:
        index = f['index']
        for name in METRICS:
            full, prior = [], []
            for branch in (0,1):
                keys = [indexed[(index,branch,k)]['index'] for k in (0,1)]
                full.append(metric(scores[0][keys[0]],name)-metric(scores[0][keys[1]],name))
                prior.append(metric(scores[1][keys[0]],name)-metric(scores[1][keys[1]],name))
            # Same targets under BOS-only must have the same prior in both poles.
            if abs(prior[0]-prior[1]) > 1e-6:
                raise ValueError('Neutral scoring depends on source context or changed batch protocol')
            residual = [a-b for a,b in zip(full,prior,strict=True)]
            rows.append(dict(family=index,id=f['id'],split=f['split'],category=f['category'],metric=name,
                original_margins=full,prior_margins=prior,context_contribution=residual,
                original_credits=credits(full),diagnostic_context_only_credits=credits(residual),
                original_both_correct=credits(full)==[1.,1.],
                diagnostic_context_only_both_correct=credits(residual)==[1.,1.],
                same_unique_candidate=full[0]*full[1]>0,
                signed_context_separation=full[0]-full[1],
                prior_magnitude=abs(prior[0]),
                neutral_context_variation=abs(prior[0]-prior[1])))
    return rows


def aggregate(rows):
    if not rows:
        raise ValueError('Nonempty matched families required')
    return dict(families=len(rows), original_both_correct=sum(r['original_both_correct'] for r in rows),
        diagnostic_context_only_both_correct=sum(r['diagnostic_context_only_both_correct'] for r in rows),
        original_accuracy=sum(sum(r['original_credits']) for r in rows)/2/len(rows),
        same_unique_candidate=sum(r['same_unique_candidate'] for r in rows),
        aligned_context_separation=sum(r['signed_context_separation']>0 for r in rows),
        median_signed_context_separation=statistics.median(r['signed_context_separation'] for r in rows),
        mean_signed_context_separation=statistics.mean(r['signed_context_separation'] for r in rows),
        mean_prior_magnitude=statistics.mean(r['prior_magnitude'] for r in rows))


def compare_rows(before, after):
    key = lambda r:(r['family'],r['metric'])
    left, right = {key(r):r for r in before}, {key(r):r for r in after}
    if len(left) != len(before) or len(right) != len(after) or set(left) != set(right):
        raise ValueError('Every matched family/metric required')
    rows = []
    for k,a in left.items():
        b = right[k]
        if any(a[f] != b[f] for f in ('id','split','category')):
            raise ValueError('Family identity changed')
        old_context_new_prior = [x+y for x,y in zip(a['context_contribution'],b['prior_margins'],strict=True)]
        new_context_old_prior = [x+y for x,y in zip(b['context_contribution'],a['prior_margins'],strict=True)]
        rows.append(dict(family=a['family'],id=a['id'],category=a['category'],split=a['split'],metric=a['metric'],
            lost_both_correct=a['original_both_correct'] and not b['original_both_correct'],
            gained_both_correct=b['original_both_correct'] and not a['original_both_correct'],
            prior_change_loses_with_old_context=credits(old_context_new_prior)!=[1.,1.],
            context_change_loses_with_old_prior=credits(new_context_old_prior)!=[1.,1.],
            prior_margin_change=[y-x for x,y in zip(a['prior_margins'],b['prior_margins'],strict=True)],
            context_contribution_change=[y-x for x,y in zip(a['context_contribution'],b['context_contribution'],strict=True)],
            original_margin_change=[y-x for x,y in zip(a['original_margins'],b['original_margins'],strict=True)],
            signed_context_separation_change=b['signed_context_separation']-a['signed_context_separation']))
    return rows


def comparison_counts(rows):
    lost = [r for r in rows if r['lost_both_correct']]
    return dict(families=len(rows), lost_both_correct=len(lost), gained_both_correct=sum(r['gained_both_correct'] for r in rows),
        arithmetic_prior_change_only_loses=sum(r['prior_change_loses_with_old_context'] and not r['context_change_loses_with_old_prior'] for r in lost),
        arithmetic_context_change_only_loses=sum(r['context_change_loses_with_old_prior'] and not r['prior_change_loses_with_old_context'] for r in lost),
        arithmetic_either_change_loses=sum(r['prior_change_loses_with_old_context'] and r['context_change_loses_with_old_prior'] for r in lost),
        arithmetic_combination_needed=sum(not r['prior_change_loses_with_old_context'] and not r['context_change_loses_with_old_prior'] for r in lost),
        mean_signed_context_separation_change=statistics.mean(r['signed_context_separation_change'] for r in rows),
        limitations='Arithmetic component swaps are not realizable independently changed models or a causal training intervention.')
