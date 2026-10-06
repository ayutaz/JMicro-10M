"""Record the actual resident-loader gate and owned durable science launch."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_web_kl_comparison_v3 as study


def main():
    probe = study.probe_evidence()
    config = read_json(study.CONFIG)
    job = read_json(study.RUN / 'job.json')
    if job['config_sha256'] != sha256(study.CONFIG) or not alive(job):
        raise ValueError('Actual owned science process required')
    previous = read_json(Path(read_json(study.RESIDENT_PROPOSAL)['prior_successful_probe']['path']))
    from statistics import median
    old_step = median(r['seconds'] for r in previous['timing']['histories'][8:])
    step = config['measured_timing']['steady_step_seconds']
    report = dict(status='actual_resident_CUDA_verified_science_launched', created_at=now(),
        config=study.reference(study.CONFIG), probe=study.reference(study.RUN / 'probe/result.json'),
        actual_identity={k:job[k] for k in ('pid', 'boot_id', 'start_ticks')},
        initial_parent_preservation=probe['initial_parent_preservation'],
        full_resume_checks=probe['gate']['checks'],
        all32_v2_update_trajectory_identical=True,
        previous_step_seconds=old_step, resident_step_seconds=step, speed_ratio=old_step / step,
        prior_GPU_seconds=study.PRIOR_GPU, resident_probe_GPU_seconds=probe['GPU_seconds'],
        known_verification_teacher_tokens=previous['verification_teacher_tokens'] + probe['verification_teacher_tokens'],
        known_verification_reference_input_tokens=previous['verification_reference_input_tokens'] + probe['verification_reference_input_tokens'],
        known_verification_reference_soft_positions=previous['verification_reference_soft_positions'] + probe['verification_reference_soft_positions'],
        failed_v1_executed_update_count='unknown; missing terminal checkpoint is not proof of zero updates',
        estimated_science_GPU_seconds_with_margin=config['estimated_GPU_seconds_with_margin'],
        estimated_all_GPU_seconds=config['estimated_GPU_seconds_with_margin'] + config['verification_GPU_seconds'],
        total_GPU_ceiling_seconds=study.CEILING, scientific_ordinary_CE_budget=study.TOTAL,
        scientific_reference_input_budget=3068 * 8 * 1024, newly_prepared_source_tokens=0,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True,
        next_action='Finish owned100M ordinary CE plus separate train-Web soft targets; full fixed evaluations, all80 individual readings and unchanged relative/absolute/historical Web guards. Only passed quality pilots may enter independent learned seed/full dev/protected test. Stop after Base completion; no Chat/quantization.')
    path = ROOT / 'reports/phase6/web_kl_comparison_launch.json'
    if path.exists():
        raise ValueError('Preserve existing launch record')
    atomic_json(path, report)
    print({k:report[k] for k in ('status', 'actual_identity', 'speed_ratio', 'estimated_all_GPU_seconds')})


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
