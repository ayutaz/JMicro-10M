"""No live completion, no empty quality conjunction, no learned-parent fresh claim."""
import copy
import json
from pathlib import Path
import sys
import pytest
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
import complete_base_parallel_residual as closeout
from base_parallel_residual_model import POLICY
from base_parallel_residual_trainer import KIND


def review():
    return dict(quality_comparisons={k: dict(passed=True) for k in ('new_sequential', 'strong', 'cached_native')},
        absolute_dev_screen=dict.fromkeys(('grammar_at_least56', 'coherence_at_least27',
            'appropriate_at_least27', 'EOS_at_least37', 'repetition_at_most18', 'no_empty_role_unicode'), True),
        original_Web=dict.fromkeys(('EOS_at_least8_more', 'repetition_no_worse', 'no_empty_role_unicode',
            'BPB_degradation_at_most1percent', 'no_punctuation_only_stops'), True),
        eligible_for_final_Base_validation=True)


def test_full_conjunction_controls_qualification_and_not_Base_adoption():
    r = review()
    assert closeout.qualification(r)
    r['quality_comparisons']['strong']['passed'] = False
    with pytest.raises(ValueError):
        closeout.qualification(r)
    r['eligible_for_final_Base_validation'] = False
    assert not closeout.qualification(r)
    r['quality_comparisons']['strong']['passed'] = 0
    with pytest.raises(ValueError):
        closeout.qualification(r)


def test_missing_or_empty_quality_sections_cannot_vacuously_pass():
    for section in ('quality_comparisons', 'absolute_dev_screen', 'original_Web'):
        r = review()
        del r[section][next(iter(r[section]))]
        with pytest.raises(ValueError):
            closeout.qualification(r)
        r[section] = {}
        with pytest.raises(ValueError):
            closeout.qualification(r)


def test_exact_fresh_both2B_terminal_no_parent_or_probe_reuse():
    root = Path(__file__).resolve().parents[1]
    c = json.loads((root / 'reports/phase6/base_parallel_residual_proposal.json').read_text())
    for arm in ('sequential', 'parallel'):
        name = 'ParallelResidualModel' if arm == 'parallel' else 'JMicroModel'
        t = dict(status='complete', arm=arm, scientific_CE_teacher_tokens=2000000000,
            counters=dict(supervised_tokens=2000000000, source_teachers=c['goals']),
            model_config=c['variants'][arm], residual_model_class=name, residual_policy=POLICY,
            spec=dict(kind=KIND, arm=arm, residual_policy=POLICY, model_class=name, actual_unique_parameters=10001152),
            scheduler=dict(tokens=2000000000, last_lr=c['optimizer']['final_lr']),
            lineage=dict(parent=None, learned_parent_weights_used=False, probe_weights_used=False))
        closeout.validate_completed_arm(c, arm, t)
        for field in ('parent', 'probe', 'gold'):
            bad = copy.deepcopy(t)
            if field == 'parent':
                bad['lineage']['parent'] = 'learned_checkpoint'
            elif field == 'probe':
                bad['lineage']['probe_weights_used'] = True
            else:
                bad['counters']['supervised_tokens'] -= 1
            with pytest.raises(ValueError):
                closeout.validate_completed_arm(c, arm, bad)


def test_actual_live_science_cannot_write_closeout(monkeypatch, tmp_path):
    (tmp_path / 'job.json').write_text(json.dumps(dict(status='running', pid=1)))
    monkeypatch.setattr(closeout, 'RUN', tmp_path)
    monkeypatch.setattr(closeout, 'alive', lambda job: True)
    with pytest.raises(ValueError, match='must finish and exit'):
        closeout.require_exited({})
    assert not (tmp_path / 'result.json').exists()
