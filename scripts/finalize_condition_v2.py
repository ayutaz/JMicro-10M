"""Verify and record the actual v2 preparation-failure branch; never launch GPU."""
import json
from pathlib import Path
import sys
import urllib.request
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.complete_units import unit_hash
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from phase6_performance import alive
from prepare_condition_v2 import DATA, RUN, excluded_hashes


def main():
    assert sys.version_info[:3] == (3, 12, 7)
    review = read_json(RUN / 'data-review.json')
    ready = read_json(DATA / 'ready.json')
    job = read_json(DATA / 'prepare-job.json')
    calibration = read_json(DATA / 'calibration.json')
    calibrated = read_json(DATA / 'calibration-review.json')
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=15) as response:
        http = json.load(response)
    checks = {}

    def require(name, condition):
        checks[name] = bool(condition)
        assert condition, name

    require('stage1_fixed32_disjoint_all_specific_notes',
        len(calibrated['rows']) == 32 and len({r['text_sha256'] for r in calibrated['rows']}) == 32
        and all(unit_hash(r['text']) == r['text_sha256'] and r['rationale'] for r in calibrated['rows'])
        and not set(calibration['previous_inspected_hashes']).intersection(r['text_sha256'] for r in calibrated['rows']))
    require('stage1_frozen_actual_v1_v2_calibration_binding',
        calibrated['calibration_sha256'] == sha256(DATA / 'calibration.json')
        and calibrated['selector_sha256'] == ready['binding']['selector_sha256']
        and review['calibration_review_sha256'] == ready['binding']['source_calibration_sha256'] == sha256(DATA / 'calibration-review.json')
        and review['plan_sha256'] == sha256(ROOT / 'docs/64_condition_selector_v2_execution.md'))
    require('stage2_actual_builder_complete_exited_budget',
        job['status'] == 'complete' and not alive(job) and job['binding'] == ready['binding']
        and job['elapsed_seconds'] <= 1800 and review['job_sha256'] == sha256(DATA / 'prepare-job.json'))
    require('stage2_all_data_evidence_passed_exact_pools', all(review['checks'].values())
        and review['ready_sha256'] == sha256(DATA / 'ready.json')
        and review['summaries']['control']['tokens'] == review['summaries']['refined']['tokens'] == 20000072)
    require('stage2_known_old_and_calibration_excluded_frozen',
        set(ready['binding']['excluded_inspected_hashes']) == excluded_hashes() | {r['text_sha256'] for r in calibration['rows']})
    require('stage2_all80_raw_bound_individual_notes_no_redraw',
        all(len(review['individual_reviews'][a]) == 40 and review['summaries'][a]['samples_sha256']
            == sha256(DATA / a / 'samples.json') for a in ('control', 'refined')))
    require('stage2_actual_unchanged_preparation_conditions_failed',
        not review['accepted_for_experiment']
        and not review['preparation_gates']['candidate_weak_less_than_control']
        and not review['preparation_gates']['candidate_weak_at_most10_of40']
        and review['summaries']['control']['weak_examples'] == 12
        and review['summaries']['refined']['weak_examples'] == 14)
    require('stage3_skipped_per_preparation_failure_branch',
        not any(RUN.glob('**/*.pt')) and not (RUN / 'screen-job.json').exists()
        and not (RUN / 'result.json').exists() and not (RUN / 'evaluation').exists())
    require('stage4_full_not_launched', not (RUN / 'full').exists())
    require('original10B_UI_actual_process_and_HTTP', alive(ui)
        and ui['status'] == 'running' and http['checkpoint_sha256']
        == '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
        and http['training_tokens'] == 10000007168 and not http['busy'])
    require('frozen_runtime_sources_preserved', all(sha256(ROOT / p) == h for p, h in review['source_sha256'].items()))
    require('all_source_and_note_files_bound',
        review['notes_sha256'] == sha256(ROOT / 'reports/phase6/condition_v2_source_notes.json')
        and calibrated['notes_sha256'] == sha256(ROOT / 'reports/phase6/condition_v2_calibration_notes.json'))
    judgment = dict(decision='preparation_rejected_no_GPU',
        failed_gates=[k for k, v in review['preparation_gates'].items() if not v],
        weak_examples={a: s['weak_examples'] for a, s in review['summaries'].items()},
        review_sha256=sha256(RUN / 'data-review.json'), calibrated_counts=calibrated['counts'],
        scientific_training_tokens=0, verification_tokens=0, GPU_evaluation_started=False,
        candidate_adopted=False, quality_targets_achieved=False, model_quality_changed=False,
        interpretation='Development calibration improvement did not transfer to the unseen fixed40 under unchanged readiness. Nonblind small samples do not establish population worsening. 100M hypothesis remains untested.',
        next_proposal='Design a separate small individually confirmed whole-story learning contrast; no contract change or new data/GPU in this completed scope.', checked_at=now())
    write_json(RUN / 'judgment.json', judgment)
    report = ROOT / 'docs/65_condition_selector_v2_preparation_results.md'
    require('stage4_results_and_judgment_saved', report.is_file() and (RUN / 'judgment.json').is_file())
    completion = dict(status='complete_authorized_four_steps_preparation_failure_branch',
        checks=checks, checked_at=now(), report_sha256=sha256(report),
        data_review_sha256=sha256(RUN / 'data-review.json'), judgment_sha256=sha256(RUN / 'judgment.json'),
        finalizer_sha256=sha256(Path(__file__)), original_UI=ui, HTTP_model=http,
        scientific_training_tokens=0, verification_tokens=0, candidate_adopted=False,
        quality_targets_achieved=False,
        stop_boundary='New four steps: preparation failed, no100M/primary/full/500M/1B/20B/Chat/test/push; verified local commit and stop.')
    write_json(RUN / 'completion.json', completion)
    print(json.dumps(dict(status=completion['status'], checks=len(checks), original_UI_PID=ui['pid'])))


if __name__ == '__main__':
    main()
