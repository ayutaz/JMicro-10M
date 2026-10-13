"""Freeze the complete comparison contract before any new GPU work."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, implementation_hashes
from chat_semantic_contract import RUN, B, SPEC, LIMITS, SUITES, ABSOLUTE_GATES, reference, preflight

SOURCES = (
    'src/jmicro/model.py', 'src/jmicro/tokenizer.py', 'src/jmicro/training.py',
    'src/jmicro/teacher_chat_training.py', 'src/jmicro/assistant_sampler.py',
    'src/jmicro/chat_evaluation.py', 'src/jmicro/chat_review.py', 'src/jmicro/japanese_evaluation.py',
    'src/jmicro/chat_semantic_curriculum.py',
    'scripts/chat_semantic_contract.py', 'scripts/run_chat_semantic.py', 'scripts/run_chat_semantic.ps1',
    'scripts/evaluate_chat_semantic.py', 'scripts/review_chat_semantic.py', 'scripts/compare_chat_semantic.py',
    'scripts/inspect_chat_semantic_environment.py', 'scripts/prepare_chat_semantic_train.py',
    'scripts/review_chat_semantic_train.py', 'scripts/prepare_chat_semantic_QA_reuse.py',
    'scripts/finalize_chat_semantic_train.py', 'scripts/dry_run_chat_semantic.py',
    'scripts/prepare_chat_semantic_dev.py', 'scripts/audit_chat_semantic_dev.py',
    'scripts/prepare_chat_semantic_nll.py', 'scripts/prepare_chat_semantic_reuse.py',
    'scripts/register_chat_semantic_known_reuse.py', 'scripts/run_chat_semantic_retention.py',
    'scripts/freeze_chat_semantic_config.py',
    'scripts/chat_first_contract.py', 'scripts/phase6_performance.py', 'scripts/run_eos_short_pilot.py',
    'scripts/prepare_chat_improvement_train.py', 'scripts/dry_run_chat_improvement.py',
    'scripts/review_chat_generalization.py', 'scripts/compare_chat_generalization.py',
    'scripts/run_complete_text_comparison.py', 'scripts/run_chat_base_retention.py',
    'scripts/review_chat_base_retention.py', 'scripts/review_improved_base.py',
)


def main():
    path = ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json'
    assert not path.exists(), 'Frozen config must not be overwritten'
    data = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-semantic-diversity-20261013')
    control = Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-generalization-20261013')
    old_config = read_json(ROOT / 'configs/phase7/chat-generalization-20261013.json')
    dry = read_json(RUN / 'consumption_dry_run.json')
    config = dict(format='teacher-chat-semantic-diversity-v1', created_at=now(),
                  purpose='direct_SFT_diagnostic_from_unadopted_original10B',
                  teacher_budget=B, GPU_limits_seconds=LIMITS, GPU_total_limit_seconds=21600,
                  parameter_count=10001152, stop_after_stage=6, fixed_padding=True,
                  implementation=implementation_hashes(), spec=SPEC, absolute_quality_gates=ABSOLUTE_GATES,
                  comparison=dict(control='S0_latest_D1_historical', candidate='S1_one_semantic_data_recipe',
                                  final_point='t3', suites=list(SUITES), required_suites=21,
                                  required_content_judgments=4599, required_fixed_NLL_points=7,
                                  new_joint_paired_CI_lower_gt_zero=True,
                                  no_model_architecture_or_optimizer_change=True),
                  parent=old_config['parent'], tokenizer=old_config['tokenizer'],
                  historical_control_evidence=reference(RUN / 'historical_control_preparation.json'),
                  suites=dict(new=reference(data / 'dev.jsonl'), previous=old_config['new_DEV'], old=old_config['old_suite']),
                  fixed_NLL=reference(data / 'nll_fixed.jsonl'),
                  arms={name: dict(data_directory=str(directory), records=reference(directory / 'train.jsonl'),
                                   manifest=reference(directory / 'manifest.json'), sampler_binding=dry[name]['sampler_binding'])
                        for name, directory in (('S0', control), ('S1', data))},
                  preparation_evidence={name: reference(RUN / filename) for name, filename in
                                        dict(consumption='consumption_dry_run.json', review='train_content_review_final.json',
                                             DEV_audit='dev_audit.json', DEV='dev_preparation.json',
                                             TRAIN='train_preparation.json', NLL='nll_preparation.json').items()},
                  source_sha256={source: sha256(ROOT / source) for source in SOURCES},
                  historical_reviewer_display_aliases=['Codex plan131 reviewer', 'Codex plan133 reviewer', 'Codex plan135 reviewer'],
                  conditional_retention=dict(required_if_candidate_qualified=True, original_Base_is_unadopted=True,
                                             dev_documents=256, fixed_Base_prefixes=80, protected_TEST_used=False,
                                             reference_config=reference(ROOT / 'configs/phase6/amount_learning_comparison.json'),
                                             original_absolute_Base_screen_required=True, BPB_relative_maximum=1.01,
                                             no_more_repetition_empty_role_unicode=True),
                  conditional_sampling=dict(required_if_candidate_qualified=True, point='t3', seeds=[42, 43, 44],
                                            suites=list(SUITES), temperature=.8, top_p=.9, top_k=50,
                                            all_raw_and_content_required=True),
                  recovery_executed=False, efficiency_executed=False, independent_trained_seed=False,
                  human_blind=False, fullDEV=False, protected_TEST_used=False, Base_adopted=False, Chat_adopted=False)
    atomic_json(path, config)
    preflight(path)
    atomic_json(RUN / 'scope.json', dict(created_at=now(), user_goal='6まで進めてください',
                                       interpreted_from='immediately preceding six-stage answer and plan135',
                                       steps=['comparison_design', 'TRAIN_QA_and_freeze', 'unseen_DEV_plus2_regressions',
                                              'technical_resource_gates_and_learning', 'all_quality_and_conditional_retention',
                                              'evidence_audit_report_and_stop'],
                                       config=reference(path), explicit_research_resumption=True,
                                       new_candidate_conditions=1, all_six_steps_complete=False, model_quality_complete=False,
                                       automatic_later_stages_or_publication=False))
    print('Frozen six-stage contract passed CPU preflight; GPU0')


if __name__ == '__main__':
    main()
