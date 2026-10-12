"""Reject fabricated completion evidence using copies of actual final metadata.

These are targeted CPU checks of accounting/provenance and conditional gates,
not extra model evaluations, automatic scoring, or mutation of stored evidence.
"""
from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, now
from jmicro.training import atomic_json
from chat_generalization_contract import RUN, preflight, reference
from complete_chat_generalization import recovery_checks, verify_ledger, verify_selection
from audit_chat_generalization_progress import validate_nll
from evaluate_chat_generalization import nll_windows


def main():
    config, tok, _ = preflight(ROOT / 'configs/phase7/chat-generalization-20261013.json')
    progress = read_json(RUN / 'progress_audit.json')
    ledger = read_json(RUN / 'GPU_ledger.json')
    checks = []

    def rejected(name, function, value, mutate):
        changed = deepcopy(value)
        mutate(changed)
        try:
            function(changed)
        except AssertionError:
            checks.append(dict(name=name, rejected=True))
        else:
            raise AssertionError('Fabricated evidence accepted: ' + name)

    assert not all(recovery_checks(config, progress).values())
    synthetic = deepcopy(progress)
    for suite in ('new', 'old'):
        row = synthetic['reviews']['D1-t3-' + suite]
        row['summaries']['primary']['joint_grammar_relevance_score2'] = 56
        row['matched24_provided_context2'] = 15
        row['matched24_own_context2'] = 24
        row['mechanical']['primary'].update(stop=76, empty=4, role_leak=0, unicode_failure=0, trimmed_history=0)
    assert not all(recovery_checks(config, synthetic).values())
    checks.append(dict(name='no_recovery_without_any_own_failure', rejected=True))
    synthetic['reviews']['D1-t3-new']['matched24_own_context2'] = 23
    assert all(recovery_checks(config, synthetic).values())
    checks.append(dict(name='own23of24_triggers_when_all_other_predicates_hold', verified=True))
    for name, mutate in (
        ('recovery_rejects_joint55', lambda p: p['reviews']['D1-t3-new']['summaries']['primary'].update(joint_grammar_relevance_score2=55)),
        ('recovery_rejects_provided14', lambda p: p['reviews']['D1-t3-old'].update(matched24_provided_context2=14)),
        ('recovery_rejects_primary_unicode', lambda p: p['reviews']['D1-t3-new']['mechanical']['primary'].update(unicode_failure=1)),
        ('recovery_rejects_primary_history_loss', lambda p: p['reviews']['D1-t3-new']['mechanical']['primary'].update(trimmed_history=1)),
        ('recovery_rejects_no_new_improvement', lambda p: p['reviews']['D0-t3-new']['summaries']['primary'].update(joint_grammar_relevance_score2=56)),
    ):
        copy = deepcopy(synthetic)
        mutate(copy)
        assert not all(recovery_checks(config, copy).values()), name
        checks.append(dict(name=name, rejected=True))
    verify_ledger(ledger, config)
    for name, mutate in (
        ('ledger_rejects_changed_historical_charge', lambda l: l['entries'][0].update(charged_seconds=1.)),
        ('ledger_rejects_unregistered_config', lambda l: l['entries'][-1].update(config_sha256='0' * 64)),
        ('ledger_rejects_dropped_failed_forecast', lambda l: l['entries'].pop(2)),
        ('ledger_rejects_overlapping_GPU_jobs', lambda l: l['entries'][-1].update(started_at=l['entries'][-2]['started_at'])),
        ('ledger_rejects_increased_category_cap', lambda l: l['limits'].update(recovery=2701.)),
        ('ledger_rejects_fabricated_total', lambda l: l.update(total_charged_seconds=0.)),
    ):
        rejected(name, lambda l: verify_ledger(l, config), ledger, mutate)
    selection = read_json(RUN / 'selection.json')
    rejected('selection_rejects_fabricated_passing_count', lambda s: verify_selection(s, progress, config), selection,
             lambda s: s['summary']['D1']['new']['content']['primary'].update(joint_grammar_relevance_score2=56))
    rejected('selection_rejects_false_candidate', lambda s: verify_selection(s, progress, config), selection,
             lambda s: s.update(eligible_candidate='D1'))
    checkpoint = read_json(RUN / 'D1/checkpoints.json')['t3']
    nll = read_json(RUN / 'NLL/D1/t3.json')
    fixed = nll_windows(config, tok)
    for name, mutate in (
        ('NLL_rejects_changed_target_ID', lambda n: n['targets'][0].update(id='fabricated-target')),
        ('NLL_rejects_changed_byte_denominator', lambda n: n['targets'][0].update(body_bytes=n['targets'][0]['body_bytes'] + 1)),
        ('NLL_rejects_changed_teacher_denominator', lambda n: n['targets'][0].update(body_teachers=n['targets'][0]['body_teachers'] + 1)),
        ('NLL_rejects_nonfinite_loss', lambda n: n['targets'][0].update(body_NLL=float('nan'))),
        ('NLL_rejects_fabricated_mean', lambda n: n['summaries']['new_DEV'].update(body_mean_NLL=0.)),
    ):
        rejected(name, lambda n: validate_nll(n, config, checkpoint, fixed), nll, mutate)
    output = dict(passed=True, completed_at=now(), checks=checks, CPU_checks=len(checks),
                  sources={name: reference(ROOT / 'scripts' / name) for name in (
                      'check_chat_generalization_completion_gates.py', 'complete_chat_generalization.py',
                      'audit_chat_generalization_progress.py')},
                  actual_selection=reference(RUN / 'selection.json'), actual_ledger=reference(RUN / 'GPU_ledger.json'),
                  actual_progress=reference(RUN / 'progress_audit.json'), actual_NLL=reference(RUN / 'NLL/D1/t3.json'),
                  stored_evidence_changed=False, new_GPU_work=False, model_quality_evidence=False)
    atomic_json(RUN / 'completion_gate_checks.json', output)
    print(f'{len(checks)} targeted CPU gate checks passed; original evidence unchanged')


if __name__ == '__main__':
    main()
