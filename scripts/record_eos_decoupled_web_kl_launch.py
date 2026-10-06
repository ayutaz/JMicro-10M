"""Persist actual own CUDA verification and durable component-ablation launch."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_eos_decoupled_web_kl_comparison as study


def main():
    probe = study.probe_evidence(); c = read_json(study.CONFIG); job = read_json(study.RUN/'job.json')
    if job['config_sha256'] != sha256(study.CONFIG) or not alive(job):
        raise ValueError('Actual owned science process required')
    report = dict(status='actual_conditional_non_EOS_KL_CUDA_verified_science_launched',created_at=now(),
        config=study.reference(study.CONFIG),probe=study.reference(study.RUN/'probe/result.json'),
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        full_resume_checks=probe['gate']['checks'],initial_parent_preservation=probe['initial_parent_preservation'],
        actual_verification_optimizer_updates=probe['GPU_optimizer_updates'],
        actual_verification_CE_teacher_tokens=probe['verification_teacher_tokens'],
        actual_verification_reference_input_tokens=probe['verification_reference_input_tokens'],
        actual_verification_reference_body_positions=probe['verification_reference_soft_positions'],
        actual_verification_reference_non_EOS_teacher_probability_mass=probe['verification_reference_non_EOS_teacher_probability_mass'],
        all32_main_and_reference_input_protocols_equal_cached_full_KL=True,
        actual_verification_GPU_seconds=probe['GPU_seconds'],steady_step_seconds=c['measured_timing']['steady_step_seconds'],
        estimated_science_GPU_seconds_with_margin=c['estimated_GPU_seconds_with_margin'],
        estimated_current_study_all_GPU_seconds=c['estimated_GPU_seconds_with_margin']+c['verification_GPU_seconds'],
        current_study_GPU_ceiling_seconds=900,previous_related_study_GPU_seconds=c['previous_related_study_GPU_seconds'],
        scientific_main_CE_teacher_budget=100000000,reference_input_budget=25133056,
        quality_screen_baseline=study.QUALITY_BASELINE,newly_prepared_source_tokens=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        next_action='Finish owned100M CE/reference comparison, all fixed256byte/Japanese/80greedy/bridge/retention and individually read all80. Audit separate probability mass and all3068 main/reference protocols against fullKL. Mechanism comparison must not replace the mandatory stronger stagedCE quality screen. Only actual quality-qualified Base may enter independent learned seed/full dev/protected test adoption.')
    path = ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_launch.json'
    if path.exists():
        raise ValueError('Preserve launch record')
    atomic_json(path,report)
    print({k:report[k] for k in ('status','actual_identity','estimated_current_study_all_GPU_seconds')})


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
