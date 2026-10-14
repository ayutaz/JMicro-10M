"""Same native fixed-diagnostic scoring, without mixed-source task builders.

This adapter never loads checkpoints or establishes Base qualification. Its
caller must own the selected model, GPU lock, deadline and persistent outputs.
"""
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from jmicro.evaluation_boundary import reject_symlinks, require_digest
from jmicro.evaluation_choice_boundary import COUNTS, WIDTHS, load_choices
from jmicro.japanese_evaluation import (
    NativeLikelihood, classification_summary, clustered_ci, tied_prediction)

CONTROLS = {
    'semantics': {'chance': .5, 'train_majority_label': 0,
                  'constant_candidate': 'paired variants have identical candidates and opposite gold labels'},
    'jblimp': {'chance': .5, 'train_majority_label': None,
              'note': 'minimal pair preference; labels are not a classification prior'},
    'jcqa': {'chance': .2, 'train_majority_label': 1}}
TRAIN_IDS_SHA = '4544bcd918f5653be6580bbbaaca3995b21d0250fe5f68c7d33205088df955c2'


def load_unigram(path, pin):
    """Reuse the saved exact2M TRAIN count vector; do not reopen TRAIN tokens."""
    require_digest(pin)
    path = Path(path)
    reject_symlinks(path)
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != pin:
        raise ValueError('Pinned saved TRAIN unigram record differs')
    record = json.loads(raw)
    if (record.get('sample_ids_sha256') != TRAIN_IDS_SHA or record.get('sample_ids') != 2000000
            or record.get('body_ids') != 1991411 or record.get('smoothing') != 1.0
            or record.get('sampling') != 'first pinned train shard token IDs'
            or not isinstance(record.get('counts'), list) or len(record['counts']) != 4096):
        raise ValueError('Exact fixed native TRAIN unigram provenance required')
    counts = np.asarray(record['counts'], dtype=float)
    if (not np.isfinite(counts).all() or np.any(counts[:8] != 0)
            or np.any(counts[8:] < 1) or np.any(counts != np.floor(counts))
            or float(counts.sum()) != 1991411 + 4088):
        raise ValueError('Saved original integer counts plus smoothing differ')
    return np.log(np.maximum(counts, 1e-300) / counts.sum()), {
        'unigram_sha256': pin, 'train_sample_ids_sha256': TRAIN_IDS_SHA,
        'sample_ids': 2000000, 'smoothing': 1.0, 'opened_paths': [str(path)],
        'TRAIN_token_stream_opened': False}


def score_case(case, likelihoods, task, unigram):
    """Preserve raw-sum/SLOR, token-normalized secondary, and fractional ties."""
    if (task not in WIDTHS or len(case['choices']) != WIDTHS[task]
            or len(likelihoods) != WIDTHS[task] or unigram.shape != (4096,)
            or not np.isfinite(unigram).all()):
        raise ValueError('Exact native diagnostic choice/vector widths required')
    for scored in likelihoods:
        ids = scored['target_ids']
        if (not isinstance(ids, list) or not ids or scored['target_tokens'] != len(ids)
                or type(scored['target_tokens']) is not int
                or any(type(i) is not int or not 8 <= i < 4096 for i in ids)
                or not math.isfinite(scored['log_likelihood']) or scored['log_likelihood'] > 0):
            raise ValueError('Finite original body likelihood and matching target IDs required')
        if 'token_nll' in scored and (len(scored['token_nll']) != len(ids)
                or any(not math.isfinite(v) or v < 0 for v in scored['token_nll'])
                or scored['log_likelihood'] != -sum(scored['token_nll'])):
            raise ValueError('Original likelihood token accounting differs')
    raw = [s['log_likelihood'] for s in likelihoods]
    prior = [float(unigram[s['target_ids']].sum()) for s in likelihoods]
    normalized = [ll / s['target_tokens'] for ll, s in zip(raw, likelihoods)]
    corrected = [(ll - base) / s['target_tokens'] for ll, base, s in zip(raw, prior, likelihoods)]
    slor = task == 'jblimp'
    primary = corrected if slor else raw
    unigram_scores = [base / s['target_tokens'] for base, s in zip(prior, likelihoods)] if slor else prior
    row = {**case, **tied_prediction(primary, case['label']), 'scores': primary,
           'raw_log_likelihood': raw, 'target_tokens': [s['target_tokens'] for s in likelihoods],
           'token_normalized': normalized, 'train_sample_slor': corrected, 'unigram_scores': unigram_scores}
    secondary = tied_prediction(normalized, case['label'])
    baseline = tied_prediction(unigram_scores, case['label'])
    row.update(normalized_prediction=secondary['prediction'], normalized_credit=secondary['credit'],
               unigram_prediction=baseline['prediction'], unigram_credit=baseline['credit'])
    if slor:
        row['raw_credit'] = tied_prediction(raw, case['label'])['credit']
    return row


def summarize_choices(rows, control):
    """Identical fixed-diagnostic summary conventions; no new acceptance gate."""
    count = len(rows)
    categories = defaultdict(list)
    for row in rows:
        categories[row['category']].append(row)
    summaries = {}
    for name, credit, pred in (
        ('primary', 'credit', 'prediction'),
        ('per_token_secondary', 'normalized_credit', 'normalized_prediction'),
        ('unigram_control', 'unigram_credit', 'unigram_prediction')):
        mapped = [dict(row, credit=row[credit], prediction=row[pred]) for row in rows]
        summaries[name] = ({'accuracy': clustered_ci(mapped),
                            **classification_summary(mapped, len(rows[0]['choices']))}
                           if rows else {'count': 0})
    majority = control.get('train_majority_label')
    return {'count': count, **summaries, 'chance': control['chance'],
            'above_chance_evidence': bool(count and summaries['primary']['accuracy']['ci95'][0] > control['chance']),
            'train_majority_accuracy': (sum(row['label'] == majority for row in rows) / count
                                        if majority is not None and count else None),
            'categories': {key: clustered_ci(value) for key, value in categories.items()},
            'tie_examples': sum(row['ties'] > 1 for row in rows),
            'limitations': 'single model training seed; dev diagnostic, no practical-quality acceptance'}


def evaluate_cases(scorer, cases, task, unigram, check, progress):
    rows = []
    for first in range(0, len(cases), 32):
        check()
        chunk = cases[first:first + 32]
        scored = scorer.score([(c['context'], choice) for c in chunk for choice in c['choices']])
        if len(scored) != sum(len(c['choices']) for c in chunk):
            raise ValueError('Scorer omitted or duplicated a fixed diagnostic choice')
        offset = 0
        for case in chunk:
            width = len(case['choices'])
            rows.append(score_case(case, scored[offset:offset + width], task, unigram))
            offset += width
        progress(task, len(rows), len(cases))
    check()
    result = {'rows': rows, 'expected': len(cases), 'complete': len(rows) == len(cases),
              'control': CONTROLS[task].copy(), 'summary': summarize_choices(rows, CONTROLS[task])}
    if task == 'jblimp' and rows:
        result['raw_pair_accuracy'] = sum(r['raw_credit'] for r in rows) / len(rows)
    return result


def evaluate_isolated_japanese(model, tokenizer, manifest, manifest_pin,
                               unigram_path, unigram_pin, check, progress, device='cuda'):
    """Preflight all isolated inputs before any forward; return complete tasks.

    Callers attach their real checkpoint binding and persist returned results.
    An exception or expired budget produces no claimed complete evaluation.
    """
    if model.training or tokenizer.vocab_size != 4096:
        raise ValueError('Original4096 codec and eval-mode model required')
    check()
    inputs = {task: load_choices(manifest, manifest_pin, task) for task in COUNTS}
    unigram, prior_provenance = load_unigram(unigram_path, unigram_pin)
    input_families = defaultdict(list)
    for case in inputs['semantics'][0]:
        input_families[case['family']].append(case)
    if len(input_families) != 96 or any(len(cases) != 2 for cases in input_families.values()):
        raise ValueError('All96 original paired semantic families required before scoring')
    check()
    scorer = NativeLikelihood(model, tokenizer, device=device, dtype='bf16', batch=16)
    tasks = {task: evaluate_cases(scorer, inputs[task][0], task, unigram, check, progress) for task in COUNTS}
    families = defaultdict(list)
    for row in tasks['semantics']['rows']:
        families[row['family']].append(row['credit'])
    if len(families) != 96 or any(len(credits) != 2 for credits in families.values()):
        raise ValueError('All96 original paired semantic families required')
    return {'tasks': tasks, 'semantic_both_contexts': {
        'correct': sum(all(c == 1 for c in credits) for credits in families.values()),
        'total': 96, 'fraction': sum(all(c == 1 for c in credits) for credits in families.values()) / 96},
        'input_provenance': {task: inputs[task][1] for task in COUNTS}, 'unigram_provenance': prior_provenance,
        'evaluation_read_paths': sorted({p for _, provenance in inputs.values() for p in provenance['opened_paths']}
                                         | set(prior_provenance['opened_paths'])),
        'forward_tokens': scorer.forward_tokens, 'complete': all(t['complete'] for t in tasks.values()),
        'TEST_opened': False, 'legacy_mixed_suite_opened': False, 'Base_qualified': False,
        'independent_learning_evidence': False}
