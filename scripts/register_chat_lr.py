"""Freeze LR-only config; verify real historical state and rebind exact12 reviews."""
import argparse
import copy
import json
from pathlib import Path
import torch
from chat_lr_contract import RUN, OLD, DATA, CONFIG, B, SPEC, CONTROL_SPEC, SUITES, LIMITS, TOTAL, reference, require_ref, preflight, ABSOLUTE_GATES
from jmicro.experiment import ROOT, read_json, now, sha256
from jmicro.training import atomic_json, implementation_hashes
from jmicro.teacher_chat_training import teacher_lr
from jmicro.chat_review import content_review
from phase6_performance import finite_state, alive
from review_chat_semantic_observer import get_items as old_items
from review_chat_lr import get_items
from evaluate_chat_lr import core as evaluator

SOURCES = ('scripts/chat_lr_contract.py', 'scripts/prepare_chat_lr.py', 'scripts/repair_chat_lr_preparation.py',
           'scripts/register_chat_lr.py', 'scripts/run_chat_lr.py', 'scripts/evaluate_chat_lr.py',
           'scripts/review_chat_lr.py', 'scripts/compare_chat_lr.py', 'scripts/audit_chat_lr.py',
           'scripts/check_chat_lr_gates.py', 'scripts/inspect_chat_lr_environment.py', 'scripts/run_chat_lr.ps1',
           'scripts/chat_semantic_contract.py', 'scripts/run_chat_semantic.py', 'scripts/evaluate_chat_semantic.py',
           'scripts/review_chat_semantic.py', 'scripts/review_chat_semantic_observer.py',
           'scripts/inspect_chat_semantic_environment.py', 'scripts/phase6_performance.py', 'scripts/chat_first_contract.py',
           'scripts/run_eos_short_pilot.py', 'src/jmicro/model.py', 'src/jmicro/training.py',
           'src/jmicro/teacher_chat_training.py', 'src/jmicro/assistant_sampler.py',
           'src/jmicro/chat_evaluation.py', 'src/jmicro/chat_review.py', 'src/jmicro/tokenizer.py')


def prepare():
    assert not CONFIG.exists()
    old_path = ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json'
    old = read_json(old_path)
    done = read_json(OLD / 'completion.json')
    assert done['all_six_steps_complete'] and done['config'] == reference(old_path)
    result = read_json(OLD / 'S1/result.json')
    job = read_json(OLD / 'S1/job.json')
    assert result['status'] == job['status'] == 'learning_complete' and not alive(job)
    assert result['config_sha256'] == job['config_sha256'] == sha256(old_path)
    assert old['spec'] == CONTROL_SPEC and old['teacher_budget'] == B
    dry = read_json(OLD / 'S1_dry_run.json')
    candidate_dry = read_json(RUN / 'S1_dry_run.json')
    atomic_json(RUN / 'preparation_incident_v1/scaled_LR_plan_before_exact_formula.json', candidate_dry)
    consumed = 0
    for row, previous in zip(candidate_dry['rows'], dry['rows'], strict=True):
        assert previous['lr'] == teacher_lr(consumed, previous['teachers'], B, CONTROL_SPEC['lr'])
        assert row['teachers'] == previous['teachers']
        row['lr'] = teacher_lr(consumed, row['teachers'], B, SPEC['lr'])
        consumed += row['teachers']
    import math
    candidate_dry['log_decay'] = sum(math.log1p(-r['lr'] * .01) for r in candidate_dry['rows'])
    candidate_dry['decay_coefficient'] = math.exp(candidate_dry['log_decay'])
    candidate_dry['LR_recomputed_with_exact_frozen_teacher_formula'] = True
    atomic_json(RUN / 'S1_dry_run.json', candidate_dry)
    prep = read_json(RUN / 'preparation.json')
    prep.update(dry_run=reference(RUN / 'S1_dry_run.json'), exact_LR_formula_correction_observer=reference(Path(__file__)))
    atomic_json(RUN / 'preparation.json', prep)
    points = read_json(OLD / 'S1/checkpoints.json')
    assert set(points) == {'t1', 't2', 't3'}
    actual = {}
    for point, ref in points.items():
        state = torch.load(require_ref(ref), map_location='cpu', weights_only=False)
        assert finite_state(state) and state['implementation_sha256'] == old['implementation'] == implementation_hashes()
        assert {key: state['spec'][key] for key in CONTROL_SPEC} == CONTROL_SPEC
        assert state['lineage']['base_checkpoint'] == old['parent'] and state['lineage']['optimizer_policy'] == 'fresh'
        assert state['spec']['teacher_chat']['budget'] == B
        assert state['spec']['teacher_chat']['data_binding'] == dry['sampler_binding']
        assert state['supervised_tokens'] == ref['Assistant_teachers'] and state['update'] == ref['update']
        assert all(key in state for key in ('model', 'optimizer', 'scheduler', 'rng', 'sampler'))
        actual[point] = dict(checkpoint=ref, finite_all_state=True, parent_SPEC_data_budget_verified=True)
        del state
    assert points['t3']['Assistant_teachers'] == 1899557 and points['t3']['update'] == 3646
    atomic_json(RUN / 'historical_control_preparation.json', dict(passed=True, created_at=now(), arm='S0',
        original_config=reference(old_path), original_job=reference(OLD / 'S1/job.json'),
        original_result=reference(OLD / 'S1/result.json'), original_completion=reference(OLD / 'completion.json'),
        checkpoints=points, actual_state_checks=actual, new_learning_updates=0,
        parent=old['parent'], spec=CONTROL_SPEC, sampler_binding=dry['sampler_binding']))
    source_reports = ('docs/123_base_teacher_decay_2b_results.md', 'docs/base_ademamix_100m_results.md',
                      'docs/53_story20_low_lr_judgment.md', 'docs/124_base_recovery_plan.md',
                      'docs/138_chat_semantic_diversity_results.md')
    evidence = []
    for path in source_reports:
        target = RUN / 'selection_evidence' / path
        target.parent.mkdir(parents=True, exist_ok=True)
        assert not target.exists()
        target.write_bytes((ROOT / path).read_bytes())
        evidence.append(dict(original_path=path, snapshot=reference(target)))
    atomic_json(RUN / 'intervention_selection.json', dict(completed_at=now(), new_candidate_conditions=1,
        selected='peak SFT LR1e-4 to3e-5; identical accepted semantic TRAIN and original10B parent',
        Base_route_considered=True, Base_root_cause_confirmed=False,
        prior_failed_Base_conditions_not_restarted=True, evidence=evidence,
        observations_source=reference(OLD / 'final_analysis.json'),
        hypothesis='Lower peak LR may reduce late deterioration on unseen input at unchanged teacher budget',
        confound='Decoupled weight decay integral also changes with LR although coefficient0.01 is fixed',
        effect_unconfirmed=True, new_training_updates=0, protected_split_incident=reference(RUN / 'protected_split_incident.json')))
    print('Actual historical3 model/Adam/scheduler/RNG/sampler states validated; one intervention selected; GPU0')


def freeze():
    assert not CONFIG.exists()
    old_path = ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json'
    old = read_json(old_path)
    prep = read_json(RUN / 'preparation.json')
    assert prep['passed'] and prep['original_Chat_TEST_unreferenced'] is False
    dry = read_json(RUN / 'S1_dry_run.json')
    historical = reference(RUN / 'historical_control_preparation.json')
    assert read_json(require_ref(historical))['passed']
    assert all((ROOT / path).is_file() for path in SOURCES)
    c = dict(format='teacher-chat-lr-only-v1', created_at=now(), purpose='bounded_LR_only_SFT_from_unadopted_original10B',
        spec=SPEC, control_spec=CONTROL_SPEC, teacher_budget=B, parameter_count=10001152,
        fixed_padding=True, implementation=implementation_hashes(), source_sha256={path: sha256(ROOT / path) for path in SOURCES},
        GPU_limits_seconds=LIMITS, GPU_total_limit_seconds=TOTAL, absolute_quality_gates=ABSOLUTE_GATES,
        comparison=dict(control='S0_historical_semantic_S1', candidate='S1_peak_LR3e-5', final_point='t3',
            suites=list(SUITES), required_suites=28, required_content_judgments=6132, required_fixed_NLL_points=7,
            required_fixed_NLL_targets_each=2634, new_joint_paired_CI_lower_gt_zero=True),
        parent=old['parent'], tokenizer=old['tokenizer'], old_config=reference(old_path),
        TRAIN=old['arms']['S1']['records'], TRAIN_manifest=old['arms']['S1']['manifest'],
        TRAIN_QA=reference(OLD / 'train_content_review_final.json'),
        DEV_audit=reference(RUN / 'dev_audit.json'), fixed_NLL=reference(DATA / 'nll_fixed.jsonl'),
        historical_consumption=reference(OLD / 'S1_dry_run.json'), candidate_consumption=reference(RUN / 'S1_dry_run.json'),
        sampler_binding=dry['sampler_binding'],
        historical_training_audit=reference(OLD / 'S1/training_audit.json'), historical_control_evidence=historical,
        historical_learning_metrics=reference(OLD / 'S1/metrics.jsonl'),
        protected_split_incident=reference(RUN / 'protected_split_incident.json'),
        original_Chat_TEST_parsed_in_failed_preparation=True, original_Base_TEST_not_parsed=True,
        final_Chat_TEST_requires_fresh_sealed_cases=True,
        suites=dict(new=reference(DATA / 'dev.jsonl'), semantic=old['suites']['new'],
                    previous=old['suites']['previous'], old=old['suites']['old']),
        arms={name: dict(old['arms']['S1']) for name in ('S0', 'S1')},
        historical_reviewer_display_aliases=['Codex plan135 reviewer'],
        conditional_retention=old['conditional_retention'],
        conditional_sampling=dict(required_if_candidate_qualified=True, point='t3', seeds=[42,43,44],
                                  suites=list(SUITES), temperature=.8, top_p=.9, top_k=50, all_raw_and_content_required=True),
        conditional_independent=dict(required_only_if_absolute_paired_retention_and_sampling_pass=True,
            fresh_learning_seed=43, independent_human_blind_required=True, fullDEV_required=True,
            protected_TEST_after_sealed_selection=True, original_Chat_TEST_not_eligible=True,
            new_TEST_required=True, preserve_original_native_Base_final_gates=True,
            implementation_before_dependent_GPU_execution=True, third_party_messages_authorized=False,
            existing_Base_policy=reference(ROOT / 'configs/phase6/base_parallel_residual_review.json'),
            original_Base_final_runner=reference(ROOT / 'scripts/run_final_base_test.py'),
            original_Base_final_reviewer=reference(ROOT / 'scripts/review_final_base_test.py')),
        Base_adopted=False, Chat_adopted=False, protected_TEST_used=False)
    atomic_json(CONFIG, c)
    preflight(CONFIG)
    atomic_json(RUN / 'scope.json', dict(created_at=now(), goal='3まで進めてください',
        interpreted_from='immediately preceding three-numbered answer', config=reference(CONFIG),
        steps=['select_one_intervention', 'compare_under10M_and_original_gates', 'conditional_independent_confirmation'],
        explicit_research_resumption=True, new_candidate_conditions=1, all_three_steps_complete=False,
        Base_adopted=False, Chat_adopted=False, protected_split_incident=reference(RUN / 'protected_split_incident.json')))
    print('New LR-only contract frozen and preflight passed; no GPU learning')


def register():
    c, tok, _ = preflight()
    records = []
    mapping = dict(semantic='new', previous='previous', old='old')
    for arm, points in (('parent', ('t0',)), ('S0', ('t1', 't2', 't3'))):
        old_arm = 'parent' if arm == 'parent' else 'S1'
        for point in points:
            ref = c['parent'] if arm == 'parent' else read_json(require_ref(c['historical_control_evidence']))['checkpoints'][point]
            for suite, previous_suite in mapping.items():
                source = OLD / 'evaluation' / old_arm / point / previous_suite / 'greedy/result.json'
                source_notes = source.with_name('notes.json')
                original, original_items = old_items(source)
                notes = read_json(source_notes)
                content_review(original, sha256(source), notes, original_items)
                assert original['binding']['checkpoint_sha256'] == ref['sha256']
                assert original['binding']['suite_sha256'] == c['suites'][suite]['sha256']
                target = RUN / 'evaluation' / arm / point / suite / 'greedy/result.json'
                assert not target.exists(), 'Completed historical rebind retained'
                raw = copy.deepcopy(read_json(source))
                raw['binding'] = evaluator.evaluation_binding(c, arm, point, ref, suite)
                raw['requested_three_steps_complete'] = False
                raw['historical_exact_raw_source'] = reference(source)
                atomic_json(target, raw)
                evaluation, items = get_items(target)
                assert list(items) == list(original_items)
                for key in items:
                    assert items[key] == original_items[key]
                current_notes = copy.deepcopy(notes)
                current_notes['evaluation_sha256'] = sha256(target)
                current_notes['historical_complete_notes_source'] = reference(source_notes)
                current_notes['new_content_judgments'] = 0
                review = content_review(evaluation, sha256(target), current_notes, items)
                atomic_json(target.with_name('notes.json'), current_notes)
                atomic_json(target.with_name('review.json'), review)
                atomic_json(target.with_name('job.json'), dict(status='complete_historical_reuse',
                    source=reference(source.with_name('job.json')), original_raw=reference(source), new_GPU_evaluation=0))
                records.append(dict(arm=arm, point=point, suite=suite, original_raw=reference(source),
                    original_notes=reference(source_notes), current_raw=reference(target),
                    current_notes=reference(target.with_name('notes.json')), judgments=219))
    assert len(records) == 12
    atomic_json(RUN / 'historical_control_registration.json', dict(passed=True, config_sha256=c['config_sha256'],
        records=records, suites_reused=12, known_suite_judgments_reused=2628, new_learning_updates=0,
        new_GPU_evaluation=0, new_content_judgments=0, independent_quality_evidence=False, completed_at=now()))
    print('12 exact known suites/2628 judgments rebound with original scores and raw/history evidence; GPU0')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('mode', choices=('prepare', 'freeze', 'register'))
    args = p.parse_args()
    dict(prepare=prepare, freeze=freeze, register=register)[args.mode]()
