"""Reject forged final evidence in memory using the actual completion checks."""
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch, Mock
import json

from chat_lr_contract import RUN, preflight, reference
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json
import complete_chat_lr_unqualified as completion
from observe_chat_lr import audit


def main():
    config, _, _ = preflight()
    progress = read_json(RUN / 'progress_audit.json')
    assert (progress['reviewed_suites'], progress['content_judgments'], progress['fixed_NLL_points']) == (28, 6132, 7)
    selection = read_json(RUN / 'selection.json')
    expected = json.loads(json.dumps(completion.calculate('t3', config)))
    assert all(selection[key] == value for key, value in expected.items())
    completion.verify_NLL(config, progress)
    checks = []

    def rejected(name, check):
        try:
            check()
        except (AssertionError, KeyError, ValueError):
            checks.append(dict(name=name, rejected=True))
        else:
            raise AssertionError('Forged evidence accepted: ' + name)

    # Exercise the production closeout's comparison assertions, without repeating
    # already audited checkpoint loading or allowing any actual output mutation.
    for name, mutate in (
        ('selection_wrong_point', lambda r: r.update(point='t2')),
        ('selection_false_candidate', lambda r: r.update(eligible_candidate='S1')),
        ('selection_false_eligibility', lambda r: r.update(candidate_eligible=True)),
        ('selection_fabricated_CI', lambda r: r.update(new_joint_CI_lower=.01)),
        ('selection_dropped_regression', lambda r: r['summary']['S1'].pop('old')),
        ('selection_fabricated_content', lambda r: r['summary']['S1']['new']['content']['primary'].update(joint_grammar_relevance_score2=56)),
    ):
        altered = deepcopy(selection)
        mutate(altered)
        original_read = completion.read_json

        def reader(path):
            return altered if Path(path) == RUN / 'selection.json' else original_read(path)

        def check():
            with patch.object(completion, 'preflight', return_value=(config, None, None)), \
                 patch.object(completion.audit, 'training'), patch.object(completion.audit, 'progress'), \
                 patch.object(completion, 'read_json', side_effect=reader), \
                 patch.object(completion, 'calculate', return_value=expected), \
                 patch.object(completion, 'atomic_json') as writer:
                try:
                    completion.main()
                finally:
                    assert not writer.called

        rejected(name, check)

    nll_path = RUN / 'NLL/S1/t3.json'
    nll = read_json(nll_path)
    for name, mutate in (
        ('NLL_target_count', lambda r: r['targets'].pop()),
        ('NLL_target_ID', lambda r: r['targets'][0].update(id='fabricated')),
        ('NLL_dataset', lambda r: r['targets'][0].update(dataset='TRAIN')),
        ('NLL_byte_denominator', lambda r: r['targets'][0].update(body_bytes=r['targets'][0]['body_bytes'] + 1)),
        ('NLL_teacher_denominator', lambda r: r['targets'][0].update(body_teachers=r['targets'][0]['body_teachers'] + 1)),
        ('NLL_EOT_mask', lambda r: r['targets'][0].update(EOT_teachers=0)),
        ('NLL_nonfinite', lambda r: r['targets'][0].update(body_NLL=float('nan'))),
        ('NLL_negative_loss', lambda r: r['targets'][0].update(EOT_NLL=-1.)),
        ('NLL_changed_target_binding', lambda r: r['binding']['fixed_targets'].update(sha256='0' * 64)),
    ):
        altered = deepcopy(nll)
        mutate(altered)
        original_read = completion.read_json

        def reader(path):
            return altered if Path(path) == nll_path else original_read(path)

        def check():
            with patch.object(completion, 'read_json', side_effect=reader):
                completion.verify_NLL(config, progress)

        rejected(name, check)

    # The existing progress audit recomputes totals and the common denominators.
    for name, mutate in (
        ('NLL_fabricated_mean', lambda r: r['summaries']['new_DEV'].update(body_mean_NLL=0.)),
        ('NLL_fabricated_loss_sum', lambda r: r['summaries']['new_DEV'].update(body_NLL=0.)),
        ('NLL_fabricated_byte_sum', lambda r: r['summaries']['new_DEV'].update(body_bytes=1)),
        ('NLL_duplicate_target_ID', lambda r: r['targets'][0].update(id=r['targets'][1]['id'])),
        ('NLL_reclassified_split', lambda r: r['targets'][0].update(dataset='fabricated')),
    ):
        altered = deepcopy(nll)
        mutate(altered)
        original_read = audit.read_json

        def reader(path):
            return altered if Path(path) == nll_path else original_read(path)

        def check():
            with patch.object(audit, 'read_json', side_effect=reader), patch.object(audit, 'atomic_json') as writer:
                try:
                    audit.progress(config)
                finally:
                    assert not writer.called

        rejected(name, check)

    assert read_json(RUN / 'selection.json') == selection and read_json(nll_path) == nll
    atomic_json(RUN / 'completion_gate_checks.json', dict(passed=True, completed_at=now(),
        config_sha256=config['config_sha256'], CPU_checks=len(checks), checks=checks,
        actual_selection=reference(RUN / 'selection.json'), actual_NLL=reference(nll_path),
        sources={name: reference(Path(__file__).parent / name) for name in
                 ('check_chat_lr_completion_gates.py', 'complete_chat_lr_unqualified.py',
                  'audit_chat_lr.py', 'compare_chat_lr_observed.py')},
        stored_evidence_changed=False, new_GPU_work=False, model_quality_evidence=False,
        coverage='Actual final comparison assertions, target identity/masks/denominators and aggregate math; no automatic content scoring or independent quality certification.'))
    print(f'{len(checks)} targeted final CPU rejection checks passed; actual evidence unchanged')


if __name__ == '__main__':
    main()
