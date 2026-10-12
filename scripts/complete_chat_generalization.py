"""Audit the four requested items; rejected conditions are not adopted models.

Reconstruct every raw-bound review/NLL via the existing progress observer,
then verify final selection, conditional predicates, numerical padding evidence,
terminal accounting and the live original UI. No training or automatic grading.
"""
from datetime import datetime
import json
import math
from pathlib import Path
import sys
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.chat_review import paired_chat_comparison
from chat_generalization_contract import RUN, B, LIMITS, preflight, reference, require_ref
from phase6_performance import alive, finite_state
from compare_chat_generalization import reviewed, absolute_checks
from compare_chat_generalization_provenance import canonical_review
from run_eos_short_pilot import equal_state
import audit_chat_generalization_progress as observer


def canonical(value):
    return json.loads(json.dumps(value))


def verify_ledger(ledger, config):
    assert ledger['limits'] == LIMITS and ledger['total_limit'] == 21600
    history = ledger['allocation_history']
    assert len(history) == 1
    previous = history[0]
    old = read_json(require_ref(previous['source_config']))
    failed = read_json(require_ref(previous['old_failed_forecast']))
    assert old['GPU_limits_seconds'] == previous['previous_limits']
    assert old['GPU_total_limit_seconds'] == sum(previous['previous_limits'].values()) == 21600
    assert failed['passed'] is False and failed['config_sha256'] == previous['source_config']['sha256']
    for key in ('parent', 'tokenizer', 'implementation', 'spec', 'arms', 'new_DEV', 'old_suite', 'fixed_NLL', 'teacher_budget'):
        assert old[key] == config[key], key
    archive = Path(previous['source_config']['path']).parent
    original = read_json(archive / 'GPU_ledger.json')
    count = len(original['entries'])
    assert count == 3 and ledger['entries'][:count] == original['entries'], 'Historical charges or failures changed'
    proof = read_json(RUN / 'budget_reconciliation.json')
    assert proof['passed'] and proof['config_sha256'] == config['config_sha256']
    assert proof['previous_config'] == previous['source_config']
    assert proof['previous_failed_forecast'] == previous['old_failed_forecast']
    assert proof['GPU_charged_seconds_preserved'] == sum(row['charged_seconds'] for row in original['entries'])
    assert proof['both_conditional_branches_retained'] and proof['main_training_before_reconciliation'] == 0
    assert proof['quality_gates_weakened'] is False and proof['current_category_caps'] == LIMITS
    changed = datetime.fromisoformat(previous['changed_at'])
    assert datetime.fromisoformat(original['entries'][-1]['ended_at']) <= changed
    assert changed <= datetime.fromisoformat(ledger['entries'][count]['started_at'])
    totals = dict.fromkeys(LIMITS, 0.)
    previous_end = None
    for index, row in enumerate(ledger['entries']):
        assert row['status'] in ('complete', 'failed_or_stopped') and not alive(row)
        expected_sha = previous['source_config']['sha256'] if index < count else config['config_sha256']
        assert row['config_sha256'] == expected_sha, 'Unregistered ledger config'
        start, end = (datetime.fromisoformat(row[k]) for k in ('started_at', 'ended_at'))
        assert start <= end and (previous_end is None or previous_end <= start)
        assert 0 < row['charged_seconds'] <= (end - start).total_seconds() + 2
        totals[row['category']] += row['charged_seconds']
        previous_end = end
    assert all(totals[k] <= LIMITS[k] for k in totals) and sum(totals.values()) <= 21600
    assert math.isclose(sum(totals.values()), ledger['total_charged_seconds'], abs_tol=1e-8)
    return totals


def recovery_checks(config, progress):
    predicate = config['recovery_predicate']
    assert predicate['final_point'] == 't3'
    assert predicate['both_suites_joint_at_least'] == 56
    assert predicate['both_suites_matched_provided_context_at_least'] == 15
    assert predicate['all_primary_mechanical_gates'] is True
    assert predicate['new_joint_improvement_over_D0_required'] is True
    assert predicate['own_history_failure_required'] is True
    checks = {}
    for suite in ('new', 'old'):
        row = progress['reviews']['D1-t3-' + suite]
        mechanical = row['mechanical']['primary']
        checks[suite + '_joint56'] = row['summaries']['primary']['joint_grammar_relevance_score2'] >= 56
        checks[suite + '_provided_context15'] = row['matched24_provided_context2'] >= 15
        checks[suite + '_primary_mechanical'] = (
            mechanical['stop'] >= 76 and mechanical['empty'] <= 4
            and all(mechanical[k] == 0 for k in ('role_leak', 'unicode_failure', 'trimmed_history')))
    checks['new_joint_improvement'] = (
        progress['reviews']['D1-t3-new']['summaries']['primary']['joint_grammar_relevance_score2']
        > progress['reviews']['D0-t3-new']['summaries']['primary']['joint_grammar_relevance_score2'])
    checks['any_own_final_context_below2'] = any(
        progress['reviews']['D1-t3-' + suite]['matched24_own_context2'] < 24 for suite in ('new', 'old'))
    return checks


def verify_selection(selection, progress, config):
    assert selection['config_sha256'] == config['config_sha256'] and selection['point'] == 't3'
    assert selection['source_sha256'] == config['source_sha256']['scripts/compare_chat_generalization.py']
    alias = selection['comparison_observer']
    require_ref({'path': alias['path'], 'sha256': alias['sha256']})
    assert alias['matched_rubric_and_nonblind_protocol'] and not alias['scores_or_raw_changed']
    assert alias['frozen_sources_changed'] is False
    for ref in alias['original_notes'].values():
        require_ref(ref)
    expected = {}
    for suite in ('new', 'old'):
        data = {arm: reviewed(arm, 't3', suite) for arm in ('D0', 'D1')}
        for arm, (evaluation, _, review) in data.items():
            row = progress['reviews'][arm + '-t3-' + suite]
            checks = absolute_checks(evaluation, review)
            expected.setdefault(arm, {})[suite] = dict(
                content=canonical(review['summaries']),
                mechanical={k: evaluation[k] for k in ('primary', 'role_control', 'own_history_all_turns', 'own_history_final24')},
                absolute_checks=checks, absolute_passed=all(checks.values()))
            assert row['summaries'] == expected[arm][suite]['content']
        paired = paired_chat_comparison(data['D0'][0], data['D1'][0], data['D0'][1], data['D1'][1],
                                       canonical_review(data['D0'][2]), canonical_review(data['D1'][2]))
        saved = selection['paired'][suite]
        for key, value in canonical(paired).items():
            if key not in ('status', 'difference_direction', 'summaries', 'dev_screens', 'pending'):
                assert saved[key] == value, (suite, key)
        assert saved['difference_direction'] == 'D1 minus D0; positive failure difference is worse'
        assert saved['summaries'] == {arm: canonical(data[arm][2]['summaries']) for arm in ('D0', 'D1')}
        assert saved['dev_screens'] == {arm: data[arm][2]['dev_screen_passed'] for arm in ('D0', 'D1')}
    assert selection['summary'] == expected
    repetitions = {suite: all(
        expected['D1'][suite]['mechanical'][k]['repetition'] <= expected['D0'][suite]['mechanical'][k]['repetition']
        for k in ('primary', 'own_history_all_turns')) for suite in ('new', 'old')}
    eligibility = {arm: all(expected[arm][suite]['absolute_passed'] for suite in ('new', 'old'))
                   and (arm == 'D0' or all(repetitions.values())) for arm in ('D0', 'D1')}
    assert selection['eligibility'] == eligibility
    assert selection['D1_repetition_not_increased_vs_D0'] == repetitions
    candidates = [arm for arm in eligibility if eligibility[arm]]
    def rank(arm):
        row = expected[arm]['new']
        return (row['content']['primary']['joint_grammar_relevance_score2'],
                row['content']['own_history_final24']['context_score2'],
                -row['mechanical']['primary']['repetition'],
                -row['mechanical']['own_history_all_turns']['repetition'], arm == 'D0')
    selected = max(candidates, key=rank) if candidates else None
    assert selection['eligible_candidate'] == selected
    assert selection['both_suites_passed'] == (selected is not None)
    return eligibility


def verify_padding(config):
    from chat_generalization_padding import check_contract, TOLERANCES
    contract = check_contract(config)
    result = read_json(RUN / 'padding/result.json')
    assert require_ref(result['contract']) == RUN / 'padding/contract.json'
    assert contract['parent'] == config['parent'] and contract['records'] == config['arms']['D1']['records']
    assert contract['teacher_budget'] == B and contract['exact_nonPAD_inputs_labels_complete_update_groups_LR']
    assert contract['dynamic_sampler_terminal_resume'] and contract['GPU_resume_all_state_exact_required']
    dry = read_json(RUN / 'D1_dry_run.json')
    assert contract['full_teacher_updates'] == dry['updates'] == 3641
    assert contract['Assistant_teachers'] == dry['Assistant_teachers'] == 1899562
    assert contract['physical_fixed'] == dry['physical_inputs']
    assert 0 < contract['physical_dynamic'] < contract['physical_fixed']
    assert contract['existing_numerical_tolerances'] == TOLERANCES
    histories = result['histories']
    rates = {}
    actual_loss_errors = []
    for name in ('fixed', 'dynamic'):
        rows = histories[name]
        assert len(rows) == 8 and [r['update'] for r in rows] == list(range(1, 9))
        assert all(math.isfinite(r[k]) for r in rows for k in ('loss', 'gradient_norm', 'seconds', 'lr'))
        assert all(r['seconds'] > 0 and r['teachers_this_update'] > 0 for r in rows)
        rates[name] = sum(r['teachers_this_update'] for r in rows[2:]) / sum(r['seconds'] for r in rows[2:])
    for i in range(3):
        fixed, dynamic = histories['fixed'][i], histories['dynamic'][i]
        assert all(fixed[k] == dynamic[k] for k in ('teachers_this_update', 'microbatches', 'lr', 'EOT_teachers'))
        delta = abs(fixed['loss'] - dynamic['loss'])
        if delta > TOLERANCES['loss_atol']:
            actual_loss_errors.append(dict(update=i + 1, kind='loss', delta=delta))
    saved_loss_errors = [r for r in result['numerical_errors'] if r['kind'] == 'loss']
    assert saved_loss_errors == actual_loss_errors and actual_loss_errors
    assert result['numerical_tolerances_met'] is False and result['efficiency_candidate_qualified'] is False
    assert result['teacher_tokens_per_second'] == rates
    assert result['speed_relative_improvement'] == rates['dynamic'] / rates['fixed'] - 1
    states = [torch.load(require_ref(result['checkpoint_refs'][name]), map_location='cpu', weights_only=False)
              for name in ('continuous', 'resumed')]
    for key in ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens',
                'body_bytes', 'token_digest', 'lineage', 'update', 'spec'):
        assert equal_state(states[0][key], states[1][key]), key
    assert all(finite_state(state) and state['update'] == 4 for state in states)
    assert result['exact_dynamic_resume'] and all(result['exact_dynamic_resume'].values())
    assert result['GPU_optimizer_updates'] == contract['GPU_optimizer_updates_planned'] == 24
    assert result['learning_updates_of_main_candidate'] == 0 and result['main_training_unchanged']
    assert result['quality_evidence'] is False and result['quality_model_adopted'] is False
    return dict(status='completed_rejected_numerical_gate', contract=reference(RUN / 'padding/contract.json'),
                result=reference(RUN / 'padding/result.json'), loss_errors=actual_loss_errors,
                full_B_CPU_parity_recorded=True, actual_dynamic_resume_all_state_verified=True,
                adopted=False, quality_evidence=False)


def main():
    config, _, _ = preflight(ROOT / 'configs/phase7/chat-generalization-20261013.json')
    observer.main()
    progress = read_json(RUN / 'progress_audit.json')
    assert not progress['pending']
    assert (progress['reviewed_suites'], progress['content_judgments'], progress['fixed_NLL_points']) == (14, 3066, 7)
    gates = {}
    for filename in ('native_probe.json', 'native_resume_gate.json', 'evaluation_forecast.json'):
        report = read_json(RUN / filename)
        assert report['passed'] and report['config_sha256'] == config['config_sha256']
        original_ref = report.get('original_GPU_evidence') or report.get('original_failed_forecast')
        if original_ref is not None:
            require_ref(original_ref)
        gates[filename] = reference(RUN / filename)
    for row in progress['reviews'].values():
        path = require_ref(row['raw'])
        evaluation = read_json(path)
        job = read_json(path.with_name('job.json'))
        assert job['status'] == 'complete' and job['binding'] == evaluation['binding']
        if 'pid' in job:
            assert not alive(job)
        else:
            assert job['historical_reuse'] is True and job['new_GPU_work'] == 0
            provenance = evaluation['historical_reuse']
            assert provenance['identical_actual_history_and_raw_output'] and provenance['new_generated_responses'] == 0
            original_path = require_ref(provenance['raw'])
            require_ref(provenance['notes'])
            original = read_json(original_path)
            assert original['binding'] == provenance['original_binding']
            assert original['binding']['checkpoint_sha256'] == evaluation['binding']['checkpoint_sha256']
            original_job = read_json(original_path.with_name('job.json'))
            assert original_job['status'] == 'complete' and original_job['binding'] == original['binding']
            if 'pid' in original_job:
                assert not alive(original_job)
            else:
                reuse = original_job['reuse_provenance']
                assert reuse['new_GPU_generation_seconds'] == 0 and reuse['all219_raw_history_ID_bytes_verified']
                terminal = read_json(require_ref(reuse['original_job']))
                assert terminal['status'] == 'complete' and not alive(terminal)
        notes = read_json(require_ref(row['notes']))
        if 'authored_score_file' in notes:
            require_ref(notes['authored_score_file'])
    training = {}
    for arm in ('D0', 'D1'):
        directory = RUN / arm
        job, result, audit = [read_json(directory / name) for name in ('job.json', 'result.json', 'training_audit.json')]
        assert job['status'] == result['status'] == 'learning_complete' and not alive(job)
        assert audit['passed'] and audit['config_sha256'] == config['config_sha256']
        assert audit['audit_source_sha256'] == config['source_sha256']['scripts/audit_chat_generalization_training.py']
        assert audit['parameter_count'] == 10001152 and audit['fresh_optimizer']
        assert audit['exact_dry_run_order_quantities_LR'] and audit['all_optimizer_steps_finite']
        require_ref(audit['metrics'])
        points = read_json(directory / 'checkpoints.json')
        assert set(points) == {'t1', 't2', 't3'} and points == result['checkpoints']
        for point, checkpoint in points.items():
            require_ref(checkpoint)
            assert audit['checkpoints'][point]['reference'] == checkpoint
            assert all(v for k, v in audit['checkpoints'][point].items() if k != 'reference')
        assert result['checkpoint']['update'] == audit['updates']
        assert audit['Assistant_teachers'] == points['t3']['Assistant_teachers']
        assert 0 <= audit['Assistant_teachers'] - B == audit['final_overshoot'] <= 64
        if arm == 'D0':
            assert audit['historical_reuse'] and audit['new_learning_updates'] == 0
        else:
            assert audit['new_learning_updates'] == 3641 and audit['Assistant_teachers'] == 1899562
            stream = read_json(directory / 't3_audit.json')
            assert stream['passed'] and stream['checkpoint'] == points['t3']
            assert stream['source_sha256'] == sha256(ROOT / 'scripts/audit_chat_generalization_savepoint.py')
            assert stream['actual_sampler_cursor_and_full_padded_stream_digest']
        training[arm] = dict(audit=reference(directory / 'training_audit.json'), result=reference(directory / 'result.json'),
                             updates=audit['updates'], teachers=audit['Assistant_teachers'],
                             new_learning_updates=audit['new_learning_updates'], final_checkpoint=points['t3'])
    selection = read_json(RUN / 'selection.json')
    verify_selection(selection, progress, config)
    analysis = read_json(RUN / 'final_analysis.json')
    assert analysis['config_sha256'] == config['config_sha256']
    assert analysis['source_sha256'] == config['source_sha256']['scripts/analyze_chat_generalization_results.py']
    assert set(analysis['rows']) == set(progress['reviews'])
    for key, row in analysis['rows'].items():
        actual = progress['reviews'][key]
        assert row['raw'] == actual['raw'] and row['notes'] == actual['notes']
        assert row['summaries'] == actual['summaries']
        assert row['matched24_provided_context2'] == actual['matched24_provided_context2']
        assert row['matched24_own_context2'] == actual['matched24_own_context2']
        point = '-'.join(key.split('-')[:2])
        assert row['fixed_NLL'] == progress['fixed_NLL'][point]['summaries']
        assert len(row['matched24']) == 24 and len({r['id'] for r in row['matched24']}) == 24
    checks = recovery_checks(config, progress)
    if all(checks.values()):
        raise RuntimeError('Recovery predicate is true: actual registered recovery learning and full evaluation are required')
    if selection['eligible_candidate'] is not None:
        raise RuntimeError('Eligible candidate: actual registered retention and all sampling content reviews are required')
    padding = verify_padding(config)
    ledger = read_json(RUN / 'GPU_ledger.json')
    totals = verify_ledger(ledger, config)
    assert totals['recovery'] == totals['retention'] == totals['train_D0'] == 0
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    assert ui['status'] == 'running' and alive(ui)
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=5) as response:
        http = json.load(response)
    assert http['checkpoint_sha256'] == config['parent']['sha256'] and http['tokenizer_sha256'] == config['tokenizer']['sha256']
    assert http['parameters'] == 10001152 and not http['busy']
    import check_chat_generalization_launch
    check_chat_generalization_launch.main()
    branches = dict(recovery=dict(status='not_triggered', executed=False, checks=checks,
                                  failed_checks=[k for k, v in checks.items() if not v], quality_unconfirmed=True),
                    retention=dict(status='skipped_no_eligible_candidate', executed=False, passed=False, quality_unconfirmed=True),
                    sampling=dict(status='skipped_no_eligible_candidate', executed=False, passed=False, quality_unconfirmed=True))
    atomic_json(RUN / 'conditional_branches.json', dict(config_sha256=config['config_sha256'], observed_at=now(),
                selection=reference(RUN / 'selection.json'), progress=reference(RUN / 'progress_audit.json'), **branches))
    output = dict(status='four_requested_items_complete_no_quality_candidate', requested_four_items_complete=True,
                  scope_complete=True, completed_at=now(), observer=reference(Path(__file__)),
                  config=reference(Path(config['config_path'])), gates=gates, training=training,
                  progress=reference(RUN / 'progress_audit.json'), selection=reference(RUN / 'selection.json'),
                  analysis=reference(RUN / 'final_analysis.json'), branches=reference(RUN / 'conditional_branches.json'),
                  items=dict(item1='revised_TRAIN_and_unseen_DEV_frozen_with_QA',
                             item2='full_B_and_all14_reviews_3066_judgments_7_fixed_NLL_points_complete',
                             item3='registered_recovery_predicate_audited_not_triggered',
                             item4='separate_full_B_CPU_and24_GPU_padding_updates_complete_rejected'),
                  padding=padding, GPU_ledger=reference(RUN / 'GPU_ledger.json'), GPU_seconds_by_category=totals,
                  GPU_total_seconds=sum(totals.values()), GPU_limit_seconds=21600,
                  original_UI=dict(observed_at=now(), identity={k: ui[k] for k in ('pid', 'boot_id', 'start_ticks')}, HTTP=http),
                  Base_adopted=False, Chat_adopted=False, model_quality_complete=False,
                  independent_trained_seed=False, independent_human_blind=False, fullDEV=False, protected_TEST_used=False,
                  quantization_executed=False, publication_executed=False,
                  caveats=['Codex nonblind, no independent human confirmation',
                           'Repeated points and own24 subsets are not additional independent families',
                           'D0 historical reuse is not new learning or independent GPU evidence',
                           'Untriggered recovery and retention do not establish their efficacy',
                           'Rejected numerical padding is not adopted despite short-run speed improvement',
                           '10M capacity limit and a single failure cause are not established'])
    atomic_json(RUN / 'completion.json', output)
    print('Four-item completion audit passed; no quality candidate; Base/Chat remain unadopted')


if __name__ == '__main__':
    main()
