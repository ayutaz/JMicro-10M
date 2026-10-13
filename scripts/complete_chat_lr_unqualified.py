"""Close the registered three-step scope only after proven unqualified all28 results.

A qualified candidate is deliberately rejected by this closeout entrypoint:
its registered independent confirmation remains required instead.
"""
from datetime import datetime
import json
import math
from pathlib import Path
import torch
from chat_lr_contract import RUN, OLD, B, SPEC, SUITES, LIMITS, TOTAL, preflight, reference, require_ref
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import finite_state, alive
from run_eos_short_pilot import equal_state
from observe_chat_lr import audit
from compare_chat_lr_observed import calculate
from inspect_chat_lr_environment import observer as environment_observer


def verify_NLL(c, progress):
    targets = [json.loads(line) for line in require_ref(c['fixed_NLL']).read_text().splitlines()]
    assert len(targets) == 2634
    for key, entry in progress['fixed_NLL'].items():
        path = require_ref(entry['source'])
        result = read_json(path)
        assert result['binding']['fixed_targets'] == c['fixed_NLL']
        assert result['binding']['config_sha256'] == c['config_sha256']
        assert len(result['targets']) == 2634
        for target, row in zip(targets, result['targets'], strict=True):
            assert target['id'] == row['id'] and target['dataset'] == row['dataset']
            assert row['body_bytes'] == target['body_bytes']
            assert row['EOT_teachers'] == 1 and row['body_teachers'] + 1 == target['teachers']
            assert all(math.isfinite(row[name]) and row[name] >= 0 for name in ('body_NLL', 'EOT_NLL'))
        if key.startswith(('parent-', 'S0-')):
            arm, point = key.split('-')
            source = OLD / 'NLL' / ('parent' if arm == 'parent' else 'S1') / (point + '.json')
            original = read_json(source)
            assert result['binding']['checkpoint']['sha256'] == original['binding']['checkpoint']['sha256']
            indexed = {r['id']: r for r in result['targets']}
            for row in original['targets']:
                current = indexed[row['id']]
                assert all(current[name] == row[name] for name in ('id','body_NLL','EOT_NLL','body_teachers','EOT_teachers','body_bytes'))
            assert result['new_GPU_NLL_targets'] == 80 and len(original['targets']) == 2554
            assert result['historical_exact_NLL_reuse'][0]['source'] == reference(source)
        else:
            assert result['new_GPU_NLL_targets'] == 2634 and result['historical_exact_NLL_reuse'] == []


def main():
    c, _, _ = preflight()
    audit.training(c)
    audit.progress(c)
    progress = read_json(RUN / 'progress_audit.json')
    assert progress['reviewed_suites'] == 28 and progress['content_judgments'] == 6132
    assert progress['fixed_NLL_points'] == 7
    assert set(progress['pending']) <= {'conditional_branches.json', 'completion.json'}
    selection = read_json(RUN / 'selection.json')
    expected = json.loads(json.dumps(calculate('t3', c)))
    assert all(selection[key] == value for key, value in expected.items())
    assert selection['eligible_candidate'] is None and not selection['candidate_eligible'], (
        'Qualified candidate requires registered retention/sampling and independent confirmation; do not close here')
    analysis = read_json(RUN / 'final_analysis.json')
    assert analysis['config_sha256'] == c['config_sha256'] and len(analysis['rows']) == 28
    require_ref(analysis['source'])
    for key, row in analysis['rows'].items():
        actual = progress['reviews'][key]
        assert row['raw'] == actual['raw'] and row['notes'] == actual['notes'] and row['summaries'] == actual['summaries']
        assert len(row['matched24']) == len({r['id'] for r in row['matched24']}) == 24
    verify_NLL(c, progress)
    registration = read_json(RUN / 'historical_control_registration.json')
    assert registration['passed'] and registration['config_sha256'] == c['config_sha256']
    assert registration['suites_reused'] == 12 and registration['known_suite_judgments_reused'] == 2628
    for row in registration['records']:
        for name in ('original_raw', 'original_notes', 'current_raw', 'current_notes'):
            require_ref(row[name])
    technical = read_json(RUN / 'technical_milestone.json')
    assert technical['passed'] and technical['config_sha256'] == c['config_sha256']
    assert technical['verification_GPU_updates'] == 25 and technical['candidate_learning_updates'] == 0
    for ref in technical['gates'].values():
        require_ref(ref)
    resumed = read_json(RUN / 'native_resume_gate.json')
    for gate in resumed['gates'].values():
        states = [torch.load(require_ref(gate['checkpoint_refs'][name]), map_location='cpu', weights_only=False)
                  for name in ('continuous','resumed')]
        assert all(finite_state(state) for state in states)
        assert all(equal_state(states[0][key], states[1][key]) for key in
                   ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','lineage','update','spec'))
        del states
    ledger = read_json(RUN / 'GPU_ledger.json')
    assert ledger['limits'] == LIMITS and ledger['total_limit'] == TOTAL
    assert ledger['entries'][:3] == technical['ledger_entries']
    totals = dict.fromkeys(LIMITS, 0.)
    previous_end = None
    for row in ledger['entries']:
        assert row['status'] in ('complete','failed_or_stopped') and not alive(row)
        assert row['config_sha256'] == c['config_sha256']
        begin, end = (datetime.fromisoformat(row[key]) for key in ('started_at','ended_at'))
        assert begin <= end and (previous_end is None or previous_end <= begin)
        previous_end = end
        assert 0 < row['charged_seconds'] <= (end - begin).total_seconds() + 2
        totals[row['category']] += row['charged_seconds']
    assert all(totals[key] <= LIMITS[key] for key in totals) and sum(totals.values()) <= TOTAL
    assert math.isclose(sum(totals.values()), ledger['total_charged_seconds'], abs_tol=1e-8)
    assert all(totals[key] == 0 for key in ('train_S0','retention','independent_training','independent_evaluation','fullDEV','protectedTEST'))
    # No unregistered qualified-only job/artifact may be hidden by a false flag.
    for pattern in ('*retention*job*', '*independent*job*', '*fullDEV*job*', '*protectedTEST*job*'):
        assert not list(RUN.rglob(pattern)), pattern
    assert not list((RUN / 'evaluation').rglob('seed-*/result.json'))
    assert not (RUN / 'independent-seed43').exists()
    branches = {key: dict(status='skipped_no_eligible_candidate', executed=False, passed=False, quality_unconfirmed=True)
                for key in ('Base_retention','sampling','independent_learning_seed43','human_blind','fullDEV','sealed_TEST','adoption')}
    atomic_json(RUN / 'conditional_branches.json', dict(config_sha256=c['config_sha256'], observed_at=now(),
        selection=reference(RUN / 'selection.json'), branches=branches,
        original_Chat_TEST_preparation_exposure=reference(RUN / 'protected_split_incident.json'),
        future_TEST_requires_fresh_sealed_Chat_cases=True, original_Base_TEST_not_parsed=True))
    environment = environment_observer.inspect()
    assert not environment['conflicts'] and environment['kernel_GPU_lock_owner_verified']
    assert environment['frozen_model_source_sha256'] == '298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83'
    scope = read_json(RUN / 'scope.json')
    assert scope['config'] == reference(c['config_path']) and len(scope['steps']) == 3
    atomic_json(RUN / 'completion.json', dict(status='three_requested_steps_scientifically_complete_rejected',
        completed_at=now(), all_three_step_decisions_complete=True, config=reference(c['config_path']), scope=reference(RUN / 'scope.json'),
        intervention=reference(RUN / 'intervention_selection.json'),
        progress=reference(RUN / 'progress_audit.json'), selection=reference(RUN / 'selection.json'),
        analysis=reference(RUN / 'final_analysis.json'), conditional_branches=reference(RUN / 'conditional_branches.json'),
        technical=reference(RUN / 'technical_milestone.json'), training=reference(RUN / 'S1/training_audit.json'),
        GPU_ledger=reference(RUN / 'GPU_ledger.json'), GPU_seconds_by_category=totals, GPU_total_seconds=sum(totals.values()),
        original_UI=environment, all28_suites_6132_judgments_verified=True, all7_NLL_2634_targets_verified=True,
        eligible_candidate=None, new_candidate_conditions=1, Base_adopted=False, Chat_adopted=False,
        independent_confirmation_executed=False, independent_quality_unconfirmed=True,
        original_Chat_TEST_preparation_exposure_preserved=True, model_quality_complete=False,
        documentation_archive_and_commit_still_required=True, push_executed=False, publication_executed=False,
        source=reference(Path(__file__))))
    print('Three-stage scientific decisions passed for rejected candidate; finish report/archive/local commit before goal completion')


if __name__ == '__main__':
    main()
