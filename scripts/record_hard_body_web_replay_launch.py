"""Persist actual CUDA evidence and live scientific replay identity."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_hard_body_web_replay_comparison as study


def main():
    probe = study.probe_evidence()
    c = read_json(study.CONFIG)
    job = read_json(study.RUN/'job.json')
    if job['config_sha256'] != sha256(study.CONFIG) or not alive(job):
        raise ValueError('Actual owned science process required')
    target = ROOT/'reports/phase6/hard_body_web_replay_comparison_launch.json'
    if target.exists():
        raise ValueError('Preserve launch record')
    atomic_json(target, dict(status='actual_gold_body_replay_CUDA_verified_science_launched', created_at=now(),
        config=study.reference(study.CONFIG), probe=study.reference(study.RUN/'probe/result.json'),
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        full_resume_checks=probe['gate']['checks'], initial_parent_preservation=probe['initial_parent_preservation'],
        actual_verification_optimizer_updates=probe['GPU_optimizer_updates'],
        actual_verification_main_CE_teacher_tokens=probe['verification_teacher_tokens'],
        actual_verification_auxiliary_hard_body_teacher_tokens=probe['verification_reference_hard_positions'],
        actual_verification_reference_input_tokens=probe['verification_reference_input_tokens'],
        actual_verification_reference_non_EOS_teacher_probability_mass=probe['verification_reference_non_EOS_teacher_probability_mass'],
        all32_main_and_reference_input_protocols_equal_cached_conditional_KL=True,
        actual_verification_GPU_seconds=probe['GPU_seconds'], steady_step_seconds=c['measured_timing']['steady_step_seconds'],
        estimated_science_GPU_seconds_with_margin=c['estimated_GPU_seconds_with_margin'],
        estimated_current_study_all_GPU_seconds=c['estimated_GPU_seconds_with_margin']+c['verification_GPU_seconds'],
        current_study_GPU_ceiling_seconds=900, previous_related_study_GPU_seconds=c['previous_related_study_GPU_seconds'],
        scientific_main_CE_teacher_budget=100000000, expected_auxiliary_hard_body_teacher_positions=25026383,
        expected_combined_hard_teacher_positions=125026383, reference_input_budget=25133056,
        quality_screen_baseline=study.QUALITY_BASELINE, newly_prepared_source_tokens=0,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True,
        next_action='Finish owned100M CE and separate gold-body replay; fixed256byte/Japanese/all80/bridge/retention. Read all80 and audit full3068 input protocols, exact gold target counts and float probability mass. ConditionalKL is supervision comparator; original stronger stagedCE is mandatory adoption control. Independent seed/full dev/protected test only after quality pilot passes.'))
    print('Actual live scientific gold-body replay and CUDA gate saved')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
