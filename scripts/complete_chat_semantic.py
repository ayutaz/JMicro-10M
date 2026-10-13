"""Requirement-level six-stage audit; never adopts Base/Chat or grades by words."""
from datetime import datetime
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review, paired_chat_comparison
from chat_semantic_contract import RUN, B, LIMITS, SUITES, preflight, reference, require_ref
from phase6_performance import alive, finite_state
from review_chat_semantic_observer import get_items
from run_eos_short_pilot import equal_state
import compare_chat_semantic as comparison
import audit_chat_semantic_progress as observer

comparison.get_items = get_items


def canonical(value):
    return json.loads(json.dumps(value))


def verify_ledger(ledger, config):
    assert ledger['limits'] == LIMITS and ledger['total_limit'] == 21600
    totals = dict.fromkeys(LIMITS, 0.)
    previous_end = None
    for row in ledger['entries']:
        assert row['status'] in ('complete', 'failed_or_stopped') and not alive(row)
        assert row['config_sha256'] == config['config_sha256']
        assert row['category'] in totals and row['category'] != 'train_S0'
        start, end = (datetime.fromisoformat(row[k]) for k in ('started_at', 'ended_at'))
        assert start <= end and (previous_end is None or previous_end <= start)
        assert 0 < row['charged_seconds'] <= (end - start).total_seconds() + 2
        totals[row['category']] += row['charged_seconds']
        previous_end = end
    assert all(totals[k] <= LIMITS[k] for k in totals)
    assert sum(totals.values()) <= 21600
    assert math.isclose(sum(totals.values()), ledger['total_charged_seconds'], abs_tol=1e-8)
    # CPU milestone gate references prevent dropping or rewriting early charges.
    early_path = RUN / 'technical_milestone.json'
    if early_path.exists():
        early = read_json(early_path)
        assert early['config_sha256'] == config['config_sha256']
        assert ledger['entries'][:len(early['ledger_entries'])] == early['ledger_entries']
    return totals


def verify_selection(selection, progress, config):
    assert selection['config_sha256'] == config['config_sha256'] and selection['point'] == 't3'
    summaries, paired, repetitions = {}, {}, {}
    for suite in SUITES:
        data = {arm: comparison.reviewed(arm, 't3', suite) for arm in ('S0', 'S1')}
        comp = paired_chat_comparison(data['S0'][0], data['S1'][0], data['S0'][1], data['S1'][1],
                                     data['S0'][3], data['S1'][3])
        comp['difference_direction'] = 'S1 minus latestD1 S0; positive failure difference is worse'
        paired[suite] = canonical(comp)
        for arm, (evaluation, _, review, _) in data.items():
            checks = comparison.absolute_checks(evaluation, review)
            summaries.setdefault(arm, {})[suite] = dict(content=canonical(review['summaries']),
                mechanical={key: evaluation[key] for key in
                            ('primary', 'role_control', 'own_history_final24', 'own_history_all_turns')},
                absolute_checks=checks, absolute_passed=all(checks.values()))
            assert progress['reviews'][arm + '-t3-' + suite]['summaries'] == canonical(review['summaries'])
        repetitions[suite] = all(summaries['S1'][suite]['mechanical'][key]['repetition'] <=
                                 summaries['S0'][suite]['mechanical'][key]['repetition']
                                 for key in ('primary', 'own_history_all_turns'))
    assert selection['summary'] == summaries and selection['paired'] == paired
    absolute = {arm: all(summaries[arm][suite]['absolute_passed'] for suite in SUITES)
                for arm in ('S0', 'S1')}
    lower = paired['new']['paired']['primary']['joint_grammar_relevance']['ci95'][0]
    eligible = absolute['S1'] and all(repetitions.values()) and lower > 0
    assert selection['absolute_eligibility'] == absolute
    assert selection['S1_repetition_not_increased_vs_S0'] == repetitions
    assert selection['new_joint_CI_lower'] == lower
    assert selection['prespecified_new_joint_improvement'] == (lower > 0)
    assert selection['candidate_eligible'] == eligible
    assert selection['eligible_candidate'] == ('S1' if eligible else None)
    assert selection['all_suites_passed'] == eligible
    assert not any(selection[k] for k in ('Base_adopted', 'Chat_adopted', 'protected_TEST_used', 'quality_complete'))
    return eligible


def verify_technical_gates(config):
    refs = {}
    for filename in ('native_probe.json', 'native_resume_gate.json', 'evaluation_forecast.json'):
        report = read_json(RUN / filename)
        assert report['passed'] and report['config_sha256'] == config['config_sha256']
        assert report['quality_evidence'] is False
        refs[filename] = reference(RUN / filename)
    probe = read_json(require_ref(refs['native_probe.json']))
    assert probe['GPU_optimizer_updates'] == 9 and probe['candidate_learning_updates'] == 0
    assert probe['arms']['S1']['finite'] and probe['arms']['S1']['within_limit']
    assert probe['arms']['S1']['forecast_training_seconds'] <= LIMITS['train_S1']
    resume = read_json(require_ref(refs['native_resume_gate.json']))
    assert resume['GPU_optimizer_updates'] == 16 and resume['candidate_learning_updates'] == 0
    for name in ('S1-full-contract', 'S1-epoch-and-terminal'):
        gate = resume['gates'][name]
        assert gate['passed'] and all(gate['checks'].values())
        states = [torch.load(require_ref(gate['checkpoint_refs'][branch]), map_location='cpu', weights_only=False)
                  for branch in ('continuous', 'resumed')]
        assert all(finite_state(s) for s in states)
        for key in ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens',
                    'body_bytes', 'token_digest', 'lineage', 'update', 'spec'):
            assert equal_state(states[0][key], states[1][key]), key
    forecast = read_json(require_ref(refs['evaluation_forecast.json']))
    assert forecast['maximum_required_responses'] == 4818 and forecast['maximum_new_NLL_batches'] == 264
    assert forecast['includes_all_greedy_savepoints_and_conditional_three_seed_sampling']
    assert forecast['forecast_evaluation_seconds'] <= LIMITS['evaluation']
    return refs


def verify_terminal_raw(row):
    path = require_ref(row['raw'])
    raw = read_json(path)
    job = read_json(path.with_name('job.json'))
    assert job['binding'] == raw['binding']
    if 'pid' in job:
        assert job['status'] == 'complete' and not alive(job)
    else:
        assert job['status'] == 'historical_generation_reused' and job['new_GPU_outputs'] == 0
        original_job = read_json(require_ref(job['original_job']))
        assert original_job['status'] == 'complete' and not alive(original_job)
        provenance = raw['historical_generation_reuse']
        assert provenance['exact_raw_and_actual_history'] and provenance['new_GPU_generation_outputs'] == 0
        original = read_json(require_ref(provenance['original_result']))
        assert original['outputs'] == raw['outputs'] and original['rollouts'] == raw['rollouts']
        assert original['binding']['checkpoint_sha256'] == raw['binding']['checkpoint_sha256']
        for ref in provenance['original_terminal_chain']:
            require_ref(ref)
    notes = read_json(require_ref(row['notes']))
    if 'authored_score_file' in notes:
        require_ref(notes['authored_score_file'])


def verify_training(config):
    reuse = read_json(require_ref(config['historical_control_evidence']))
    assert reuse['passed'] and reuse['new_learning_updates'] == 0
    assert not alive(read_json(require_ref(reuse['original_job'])))
    directory = RUN / 'S1'
    job, result, audit = [read_json(directory / filename) for filename in ('job.json', 'result.json', 'training_audit.json')]
    assert job['status'] == result['status'] == 'learning_complete' and not alive(job)
    assert result['config_sha256'] == audit['config_sha256'] == config['config_sha256']
    assert audit['passed'] and audit['parameter_count'] == 10001152 and audit['fresh_optimizer']
    assert audit['audit_source_sha256'] == sha256(ROOT / 'scripts/audit_chat_semantic_training.py')
    assert audit['exact_dry_run_order_quantities_LR'] and audit['all_optimizer_steps_finite']
    require_ref(audit['metrics'])
    dry = read_json(RUN / 'S1_dry_run.json')
    assert audit['updates'] == audit['new_learning_updates'] == dry['updates'] == 3646
    assert audit['Assistant_teachers'] == dry['Assistant_teachers'] == 1899557
    assert audit['final_overshoot'] == audit['Assistant_teachers'] - B == 2
    points = read_json(directory / 'checkpoints.json')
    assert set(points) == {'t1', 't2', 't3'} and points == result['checkpoints']
    for point, ref in points.items():
        require_ref(ref)
        assert audit['checkpoints'][point]['reference'] == ref
        state = torch.load(ref['path'], map_location='cpu', weights_only=False)
        assert finite_state(state) and state['supervised_tokens'] == ref['Assistant_teachers']
        assert state['lineage']['base_checkpoint'] == config['parent'] and state['update'] == ref['update']
        stream = read_json(directory / (point + '_audit.json'))
        assert stream['passed'] and stream['checkpoint'] == ref
        assert stream['source_sha256'] == sha256(ROOT / 'scripts/audit_chat_semantic_savepoint.py')
        assert stream['actual_sampler_cursor_and_full_padded_stream_digest']
    return dict(S0=dict(preparation=config['historical_control_evidence'], new_learning_updates=0,
                       checkpoints=reuse['checkpoints']),
                S1=dict(audit=reference(directory / 'training_audit.json'), result=reference(directory / 'result.json'),
                        updates=audit['updates'], teachers=audit['Assistant_teachers'], checkpoints=points))


def verify_branches(config, selected, tok):
    if not selected:
        assert not (RUN / 'retention/job.json').exists()
        assert not any((RUN / 'evaluation').glob('S1/t3/*/seed-*/result.json'))
        return dict(retention=dict(status='skipped_no_eligible_candidate', executed=False,
                                   passed=False, quality_unconfirmed=True),
                    sampling=dict(status='skipped_no_eligible_candidate', executed=False,
                                  passed=False, quality_unconfirmed=True))
    from run_chat_semantic_retention import review as retention_review
    retention_path = RUN / 'retention/retention_review.json'
    saved = read_json(retention_path)
    retention_review(config, tok, require_ref(saved['authored_notes']))
    assert read_json(retention_path) == saved
    sampling_refs, screens = [], []
    from evaluate_chat_semantic import evaluation_binding
    checkpoint = read_json(RUN / 'S1/checkpoints.json')['t3']
    for suite in SUITES:
        for seed in (42, 43, 44):
            path = RUN / 'evaluation/S1/t3' / suite / f'seed-{seed}/result.json'
            evaluation, items = get_items(path)
            assert evaluation['binding'] == evaluation_binding(config, 'S1', 't3', checkpoint, suite, seed, 'sampling')
            notes = read_json(path.with_name('notes.json'))
            reviewed = content_review(evaluation, sha256(path), notes, items)
            assert canonical(reviewed) == read_json(path.with_name('review.json'))
            verify_terminal_raw(dict(raw=reference(path), notes=reference(path.with_name('notes.json'))))
            checks = comparison.absolute_checks(evaluation, reviewed)
            screens.append(all(checks.values()))
            sampling_refs.append(dict(raw=reference(path), notes=reference(path.with_name('notes.json')),
                                      review=reference(path.with_name('review.json')), original_gate_checks=checks))
    assert len(sampling_refs) == 9
    return dict(retention=dict(status='executed_reviewed', executed=True, passed=saved['passed'],
                               quality_unconfirmed=False, review=reference(retention_path)),
                sampling=dict(status='executed_all9_suites_1971_judgments', executed=True,
                              passed=all(screens), quality_unconfirmed=False, evaluations=sampling_refs))


def main():
    config, tok, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    observer.main()
    progress = read_json(RUN / 'progress_audit.json')
    assert not progress['pending'], progress['pending']
    assert (progress['reviewed_suites'], progress['content_judgments'], progress['fixed_NLL_points']) == (21, 4599, 7)
    gates = verify_technical_gates(config)
    training = verify_training(config)
    for row in progress['reviews'].values():
        verify_terminal_raw(row)
    registered = read_json(RUN / 'historical_control_registration.json')
    assert registered['passed'] and registered['config_sha256'] == config['config_sha256']
    assert registered['suites_reused'] == 8 and registered['known_suite_judgments_reused'] == 1752
    for row in registered['records']:
        for name in ('original_raw', 'original_notes', 'original_job', 'current_raw', 'current_notes'):
            require_ref(row[name])
    selection = read_json(RUN / 'selection.json')
    selected = verify_selection(selection, progress, config)
    analysis = read_json(RUN / 'final_analysis.json')
    assert analysis['config_sha256'] == config['config_sha256']
    assert analysis['source_sha256'] == sha256(ROOT / 'scripts/analyze_chat_semantic_results.py')
    assert set(analysis['rows']) == set(progress['reviews'])
    for key, row in analysis['rows'].items():
        actual = progress['reviews'][key]
        assert row['raw'] == actual['raw'] and row['notes'] == actual['notes']
        assert row['summaries'] == actual['summaries']
        assert row['matched24_provided_context2'] == actual['matched24_provided_context2']
        assert row['matched24_own_context2'] == actual['matched24_own_context2']
        assert row['fixed_NLL'] == progress['fixed_NLL']['-'.join(key.split('-')[:2])]['summaries']
        assert len(row['matched24']) == len({r['id'] for r in row['matched24']}) == 24
    branches = verify_branches(config, selected, tok)
    ledger = read_json(RUN / 'GPU_ledger.json')
    totals = verify_ledger(ledger, config)
    assert totals['train_S0'] == 0
    if not selected:
        assert totals['retention'] == 0
    tests = read_json(RUN / 'completion_gate_checks.json')
    assert tests['passed'] and tests['config_sha256'] == config['config_sha256']
    assert tests['actual_selection'] == reference(RUN / 'selection.json')
    assert tests['actual_ledger'] == reference(RUN / 'GPU_ledger.json')
    assert tests['actual_NLL'] == reference(RUN / 'NLL/S1/t3.json')
    for ref in tests['sources'].values():
        require_ref(ref)
    from inspect_chat_semantic_environment import inspect
    environment = inspect()
    assert environment['conflicts'] == [] and environment['kernel_GPU_lock_owner_verified']
    assert environment['frozen_model_source_sha256'] == config['source_sha256']['src/jmicro/model.py']
    atomic_json(RUN / 'conditional_branches.json', dict(config_sha256=config['config_sha256'],
                observed_at=now(), selection=reference(RUN / 'selection.json'), **branches))
    scope = read_json(RUN / 'scope.json')
    assert scope['config']['sha256'] == config['config_sha256'] and len(scope['steps']) == 6
    stages = dict(comparison_design=dict(config=reference(Path(config['config_path']))),
                  TRAIN_QA_and_freeze=dict(evidence=config['preparation_evidence']),
                  unseen_DEV_plus2_regressions=dict(suites=config['suites'], NLL=config['fixed_NLL']),
                  technical_resource_gates_and_learning=dict(gates=gates, training=training),
                  all_quality_and_conditional_retention=dict(progress=reference(RUN / 'progress_audit.json'),
                                                            selection=reference(RUN / 'selection.json'), branches=branches),
                  evidence_audit_report_and_stop=dict(analysis=reference(RUN / 'final_analysis.json'),
                                                     gate_checks=reference(RUN / 'completion_gate_checks.json')))
    assert set(stages) == set(scope['steps'])
    output = dict(status='six_requested_stages_scientifically_complete', scope_complete=True,
                  all_six_steps_complete=True, completed_at=now(), observer=reference(Path(__file__)),
                  scope=reference(RUN / 'scope.json'), config=reference(Path(config['config_path'])), stages=stages,
                  eligible_candidate=selection['eligible_candidate'], all21_suites_4599_judgments_verified=True,
                  all7_NLL_points_2554_targets_each_verified=True, original_UI=environment,
                  GPU_ledger=reference(RUN / 'GPU_ledger.json'), GPU_seconds_by_category=totals,
                  GPU_total_seconds=sum(totals.values()), GPU_limit_seconds=21600,
                  Base_adopted=False, Chat_adopted=False, model_quality_complete=False,
                  independent_trained_seed=False, independent_human_blind=False, fullDEV=False,
                  protected_TEST_used=False, recovery_executed=False, efficiency_executed=False,
                  quantization_executed=False, publication_executed=False,
                  documentation_delivery_and_commit_still_required=True)
    atomic_json(RUN / 'completion.json', output)
    print('Six-stage scientific audit passed; finish documentation/archive/commit before goal completion')


if __name__ == '__main__':
    main()
