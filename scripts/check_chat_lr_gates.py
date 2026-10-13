"""Reject condition drift before launching the new LR-only comparison."""
import copy
from pathlib import Path
from chat_lr_contract import CONFIG, RUN, preflight, reference
import chat_lr_contract as contract
from jmicro.training import atomic_json
from jmicro.experiment import now, read_json, sha256
from review_chat_semantic_observer import protocol_view


def main():
    original = read_json(CONFIG)
    real_read = contract.read_json
    checks = {}
    changes = {
        'candidate_LR_drift': lambda c: c['spec'].update(lr=1e-4),
        'control_LR_drift': lambda c: c['control_spec'].update(lr=3e-5),
        'teacher_budget_extension': lambda c: c.update(teacher_budget=1899556),
        'model_enlargement': lambda c: c.update(parameter_count=12000000),
        'quality_gate_weakening': lambda c: c['absolute_quality_gates'].update(joint_minimum=19),
        'GPU_budget_increase': lambda c: c.update(GPU_total_limit_seconds=40000),
        'TRAIN_hash_mismatch': lambda c: c['TRAIN'].update(sha256='0' * 64),
        'source_edit': lambda c: c['source_sha256'].update({'src/jmicro/model.py': '0' * 64}),
        'Base_adoption_without_evidence': lambda c: c.update(Base_adopted=True),
        'TEST_used_as_selection': lambda c: c.update(protected_TEST_used=True),
    }
    preflight()
    for name, mutation in changes.items():
        changed = copy.deepcopy(original)
        mutation(changed)
        def substitute(path, altered=changed):
            return copy.deepcopy(altered) if Path(path).resolve() == CONFIG else real_read(path)
        contract.read_json = substitute
        try:
            preflight()
        except (AssertionError, ValueError):
            checks[name] = True
        else:
            raise AssertionError('Invalid condition accepted: ' + name)
        finally:
            contract.read_json = real_read
    try:
        protocol_view(dict(requested_six_steps_complete=True))
    except AssertionError:
        checks['legacy_completion_true_rejected'] = True
    else:
        raise AssertionError('Invalid inherited completion marker accepted')
    assert read_json(CONFIG) == original
    atomic_json(RUN / 'technical_gate_checks.json', dict(passed=True, checks=checks,
        check_count=len(checks), config=reference(CONFIG), source=reference(Path(__file__)), completed_at=now(),
        stored_evidence_unchanged=True, GPU_updates=0, quality_evidence=False))
    print(f'{len(checks)} condition-drift/metadata CPU rejection checks passed; stored evidence unchanged')


if __name__ == '__main__':
    main()
