"""Verify the requested five-step 500M milestone without starting GPU work."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from audit_phase6_completion import document_links
from phase6_performance import alive
from run_base import validate_config


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--windows-root', type=Path, required=True)
    args = parser.parse_args()
    windows = args.windows_root
    run = ROOT / 'reports/phase6/base-20261003'
    config = validate_config(ROOT / 'configs/phase6/base_frozen.json')
    review_path = windows / 'reports/phase6/base_500m_review.json'
    review = read_json(review_path)
    protected = read_json(windows / 'reports/local/base-500m-existing-evidence.json')
    # The report index is current documentation. Preserve its original bytes
    # separately while adding links; all historical experiment reports stay put.
    index_name = 'reports/README.md'
    index_archive = windows / 'reports/local/base-500m-report-index-before.md'
    changed = [name for name, expected in protected.items() if
               sha256(index_archive if name == index_name else windows / name) != expected]
    preflight = read_json(windows / 'reports/phase6/base_500m_preflight.json')
    tests = read_json(windows / 'reports/phase6/base_500m_tests.json')
    links = document_links(windows)
    gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi', '--query-compute-apps=pid',
                          '--format=csv,noheader'], capture_output=True, text=True, check=True)
    state = dict(line.split('=', 1) for line in (ROOT / 'reports/local/base-500m-pipeline.state').read_text().splitlines())
    pipeline_identity = dict(pid=int(state['pid']), boot_id=state['boot_id'], start_ticks=state['start_ticks'])
    checks = {
        '1_preflight_and_frozen_source_data_runtime': preflight['status'] == 'passed_initial_preflight' and
            preflight['config_sha256_wsl'] == sha256(ROOT / 'configs/phase6/base_frozen.json') and
            not preflight['initial_gpu_compute_processes'] and not preflight['initial_base_output_exists'] and
            all(r['windows'] == r['wsl'] == r['frozen'] for r in preflight['source_checks']),
        '2_actual_stable_500M_and_resume_state': review['checkpoints']['stable']['update'] == 15259 and
            review['checkpoints']['stable']['tokens'] == 500006912 and
            sha256(Path(review['checkpoints']['stable']['path'])) == review['checkpoints']['stable']['sha256'],
        '3_actual_independent_decay_763_and_parent_preservation': review['checkpoints']['decay']['update'] == 16022 and
            review['checkpoints']['decay']['tokens'] == 525008896 and
            sha256(Path(review['checkpoints']['decay']['path'])) == review['checkpoints']['decay']['sha256'] and
            review['checks']['decay_parent_and_stable_immutable'],
        '4_same_full_dev_and_fixed_generation_actual_evidence': review['evaluation']['documents'] == 89416 and
            review['evaluation']['body_bytes'] == 164344743 and
            all(sha256(Path(path)) == expected for path, expected in review['evaluation']['evidence'].items()) and
            review['checks']['fixed_400_generations_redecoded_and_flags_independently_checked'],
        '4_independent_training_evaluation_checks_passed': review['status'] == 'passed_500M_training_and_evaluation_audit' and
            all(review['checks'].values()),
        '5_review_and_current_status_saved': review_path.with_suffix('.md').exists() and
            '500M学習・評価完了' in (windows / 'docs/autonomous_status.md').read_text(),
        'full_99_tests_no_failures_errors_or_skips': tests['tests'] == 99 and
            tests['failures'] == tests['errors'] == tests['skipped'] == 0 and
            sha256(Path(tests['xml_path'])) == tests['xml_sha256'],
        'historical_reports_configs_eval_lock_unchanged_and_old_index_archived': not changed,
        'document_links_and_uv_contracts_valid': not links['errors'],
        'pipeline_and_GPU_jobs_terminal': state['status'] == 'complete' and not alive(pipeline_identity) and
            not gpu.stdout.strip() and all(not alive(read_json(run / f'supervisor-{stage}-500M.json'))
                                           for stage in ('stable', 'decay', 'evaluate')),
        'stop_before_1B_and_quality_limitations_preserved': not (run / 'decay-1B').exists() and
            not review['test_evaluated'] and not review['human_scoring_performed'] and
            not review['quality_targets_achieved'] and config['milestones']['500M']['stable_updates'] == 15259,
    }
    result = dict(status='passed_requested_500M_scope' if all(checks.values()) else 'failed',
        completed_at=now(), checks=checks, changed_previous_files=changed,
        updated_documentation_index=index_name, original_index_archive_sha256=sha256(index_archive),
        previous_files_verified=len(protected), document_links=links,
        review_sha256=sha256(review_path), gpu_compute_processes=gpu.stdout.strip(),
        stop_boundary='500M training/decay/evaluation/report complete; commit and stop before 1B',
        quality_targets_achieved=False)
    write_json(windows / 'reports/phase6/base_500m_completion_audit.json', result)
    print(json.dumps(dict(status=result['status'], checks=len(checks),
        failed=[name for name, passed in checks.items() if not passed]), ensure_ascii=False), flush=True)
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == '__main__':
    main()
