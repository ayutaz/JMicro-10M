"""Check old scoring math with fixtures; never load real TEST or models."""
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
import pytest

from jmicro.isolated_japanese_scoring import (
    CONTROLS, TRAIN_IDS_SHA, evaluate_cases, evaluate_isolated_japanese, load_unigram, score_case)

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from evaluate_japanese_base import evaluate_choices


class FixtureScorer:
    def score(self, pairs):
        values = {'a': (-2., [8]), 'bb': (-3., [9, 9]), 'c': (-2., [8]),
                  'd': (-2., [8]), 'e': (-2., [8])}
        return [dict(log_likelihood=values[choice][0], target_ids=values[choice][1],
                     target_tokens=len(values[choice][1])) for _, choice in pairs]


@pytest.mark.parametrize('task', ['semantics', 'jblimp', 'jcqa'])
def test_all_row_math_and_summaries_equal_frozen_evaluator_on_fixtures(tmp_path, task):
    choices = ['a', 'bb'] if task != 'jcqa' else ['a', 'bb', 'c', 'd', 'e']
    cases = [dict(id=str(i), family='paired', category='fixture', context='', choices=choices, label=i)
             for i in range(2)]
    unigram = np.full(4096, -10.)
    unigram[9] = -1.
    progress = []
    result = evaluate_cases(FixtureScorer(), cases, task, unigram, lambda: None,
                            lambda *args: progress.append(args))
    path = tmp_path / 'old.json'
    evaluate_choices(FixtureScorer(), cases, CONTROLS[task], unigram, path, 'fixture-only',
                     time.monotonic() + 30, slor=task == 'jblimp')
    old = json.loads(path.read_text())
    assert result['rows'] == old['rows'] and result['summary'] == old['summary']
    assert result['complete'] and progress == [(task, 2, 2)]
    # JBLiMP primary favors the shorter corrected score; raw sum favors a.
    if task == 'jblimp':
        assert result['rows'][0]['scores'] == [8., -.5]
    if task == 'jcqa':
        assert result['rows'][0]['ties'] == 4 and result['rows'][0]['credit'] == .25


def record(tmp_path):
    counts = [0.] * 8 + [1.] * 4088
    counts[8] += 1991411
    path = tmp_path / 'unigram.json'
    path.write_text(json.dumps(dict(sample_ids_sha256=TRAIN_IDS_SHA, sample_ids=2000000,
        body_ids=1991411, smoothing=1., sampling='first pinned train shard token IDs', counts=counts)))
    return path, hashlib.sha256(path.read_bytes()).hexdigest()


def test_saved_counts_reused_with_exact_original_normalization(tmp_path):
    path, pin = record(tmp_path)
    vector, provenance = load_unigram(path, pin)
    assert vector.shape == (4096,) and np.isfinite(vector).all()
    assert np.exp(vector[8]) == pytest.approx(1991412 / (1991411 + 4088))
    assert provenance['TRAIN_token_stream_opened'] is False
    assert provenance['opened_paths'] == [str(path)]


@pytest.mark.parametrize('bad', ['hash', 'sample', 'count', 'special', 'nan'])
def test_wrong_baseline_and_mutated_counts_fail(tmp_path, bad):
    path, pin = record(tmp_path)
    data = json.loads(path.read_text())
    if bad == 'hash':
        pin = '0' * 64
    else:
        if bad == 'sample': data['sample_ids_sha256'] = '0' * 64
        elif bad == 'count': data['counts'][8] -= 1
        elif bad == 'special': data['counts'][0] = 1
        else: data['counts'][9] = float('nan')
        path.write_text(json.dumps(data))
        pin = hashlib.sha256(path.read_bytes()).hexdigest()
    with pytest.raises(ValueError):
        load_unigram(path, pin)


@pytest.mark.parametrize('bad', ['nan', 'tokens', 'special', 'nll'])
def test_invalid_scorer_output_cannot_be_scored(bad):
    values = FixtureScorer().score([('', 'a'), ('', 'bb')])
    if bad == 'nan': values[0]['log_likelihood'] = float('nan')
    elif bad == 'tokens': values[0]['target_tokens'] = 2
    elif bad == 'special': values[0]['target_ids'] = [3]
    else: values[0]['token_nll'] = [1.]
    with pytest.raises(ValueError):
        score_case(dict(choices=['a', 'bb'], label=0), values, 'semantics', np.full(4096, -10.))


def test_missing_choice_and_expired_budget_fail_without_complete_result():
    case = dict(id='fixture', family='f', category='f', context='', choices=['a', 'bb'], label=0)
    class Missing(FixtureScorer):
        def score(self, pairs): return super().score(pairs)[:-1]
    with pytest.raises(ValueError, match='omitted'):
        evaluate_cases(Missing(), [case], 'semantics', np.full(4096, -10.), lambda: None, lambda *a: None)
    def expired(): raise TimeoutError('fixture-budget')
    with pytest.raises(TimeoutError):
        evaluate_cases(FixtureScorer(), [case], 'semantics', np.full(4096, -10.), expired, lambda *a: None)


def test_complete_adapter_reads_five_known_files_and_never_mixed_or_TEST(tmp_path, monkeypatch):
    import jmicro.isolated_japanese_scoring as module
    from jmicro.evaluation_choice_boundary import COUNTS, WIDTHS, MANIFEST_NAME
    from unittest.mock import patch

    manifest = dict(kind='isolated_previously_observed_Japanese_diagnostics_v1',
                    project_role='dev_fixed_diagnostics', tasks={}, TEST_read_for_export=False)
    for task, count in COUNTS.items():
        rows = [dict(id=str(i), family=str(i // 2) if task == 'semantics' else str(i),
                     category='fixture', context='', choices=['文'] * WIDTHS[task], label=0) for i in range(count)]
        raw = ''.join(json.dumps(r) + '\n' for r in rows).encode()
        name = task + '.dev.jsonl'
        (tmp_path / name).write_bytes(raw)
        manifest['tasks'][task] = dict(file=name, count=count, sha256=hashlib.sha256(raw).hexdigest(), source_sha256='a' * 64)
    path = tmp_path / MANIFEST_NAME
    path.write_text(json.dumps(manifest))
    pin = hashlib.sha256(path.read_bytes()).hexdigest()
    prior_path, prior_pin = record(tmp_path)
    (tmp_path / 'test.jsonl').write_text('BROKEN_TEST_FIXTURE')
    class Model:
        training = False
    class Codec:
        vocab_size = 4096
    class Scorer:
        forward_tokens = 0
        def __init__(self, *args, **kwargs): pass
        def score(self, pairs):
            self.forward_tokens += len(pairs)
            return [dict(log_likelihood=-1., target_ids=[8], target_tokens=1) for _ in pairs]
    monkeypatch.setattr(module, 'NativeLikelihood', Scorer)
    import evaluate_japanese_base
    monkeypatch.setattr(evaluate_japanese_base, 'build_tasks', lambda *a, **k: pytest.fail('Mixed builder called'))
    allowed = {path, prior_path, *(tmp_path / (task + '.dev.jsonl') for task in COUNTS)}
    original_open, seen = Path.open, []
    def guarded(p, *args, **kwargs):
        assert p in allowed, 'Forbidden data or TEST open'
        seen.append(p)
        return original_open(p, *args, **kwargs)
    with patch.object(Path, 'open', guarded):
        result = evaluate_isolated_japanese(Model(), Codec(), path, pin, prior_path, prior_pin,
                                            lambda: None, lambda *a: None, device='cpu')
    assert set(seen) == allowed and set(result['evaluation_read_paths']) == {str(p) for p in allowed}
    assert result['complete'] and result['forward_tokens'] == 6641
    assert result['semantic_both_contexts']['total'] == 96
    assert result['TEST_opened'] is False and result['Base_qualified'] is False


def test_training_mode_rejected_before_input_reads(monkeypatch):
    class Model:
        training = True
    class Codec:
        vocab_size = 4096
    with pytest.raises(ValueError, match='eval-mode'):
        evaluate_isolated_japanese(Model(), Codec(), 'DO_NOT_OPEN', 'a' * 64,
                                   'DO_NOT_OPEN', 'a' * 64, lambda: None, lambda *a: None)
