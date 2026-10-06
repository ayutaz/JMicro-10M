"""Use completed matching runs for timing only; retain a hard 900-second cap."""
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256
from phase6_performance import alive

PATH = ROOT / 'reports/phase6/source_order_budget_evidence.json'
RUNS = (('historical-parent-condition-comparison-v3-20261006', 'historical_parent',
         'historical_parent_condition_comparison_v3.json'),
        ('original-web-retention-comparison-20261006', 'original_web',
         'original_web_retention_comparison.json'))


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def matched_nontraining_seconds(result, job, arm, rows):
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Completed absent timing reference required')
    cp = result['checkpoints'][arm]
    ev = result['evaluations'][arm]
    training = sum(row['seconds'] for row in rows)
    if (not math.isclose(training, cp['training_seconds'], abs_tol=1e-8)
            or result['GPU_seconds'] != job['GPU_elapsed_seconds']
            or cp['additional_supervised_tokens'] != 100000000
            or cp['checkpoint_sha256'] != ev['checkpoint_sha256']
            or ev['body']['documents'] != 256 or ev['body']['body_bytes'] != 472055
            or len(ev['generation']['outputs']) != 80
            or any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count'] != n
                   for k,n in dict(semantics=192, jblimp=331, jcqa=1119).items())
            or any(result[k][arm]['evaluated_requests'] != 512 for k in ('transfer','retention'))
            or ev['protected_test_used']):
        raise ValueError('Matching complete evaluation and metric timing required')
    remaining = result['GPU_seconds'] - training
    if not math.isfinite(remaining) or remaining <= 0:
        raise ValueError('Positive measured nontraining occupancy required')
    return dict(GPU_seconds=result['GPU_seconds'], training_step_seconds=training,
                nontraining_GPU_occupancy_seconds=remaining)


def measured_evidence():
    records=[]
    probe=read_json(ROOT/'configs/phase6/source_order_condition_probe.json')
    for folder, arm, config_name in RUNS:
        run=ROOT/'reports/phase6'/folder
        config=ROOT/'configs/phase6'/config_name
        c=read_json(config)
        # The evaluation recipe and both transfer suites are the identical pinned
        # references. Training-parent differences are irrelevant to timing use.
        if (c['original_config'] != probe['original_config'] or c['implementation'] != probe['implementation']
                or any(c['references'][key] != probe['references'][key]
                       for key in ('source_cases','retention_cases'))):
            raise ValueError('Timing tasks/recipe/implementation differ')
        for relative in ('scripts/run_complete_text_comparison.py', 'scripts/run_condition_source_ranking.py'):
            if c['source_sha256'][relative] != probe['source_sha256'][relative] or sha256(ROOT/relative) != c['source_sha256'][relative]:
                raise ValueError('Frozen evaluator differs')
        result=read_json(run/'compare-result.json'); job=read_json(run/'job.json')
        log=run/arm/'training/metrics.jsonl'
        rows=[__import__('json').loads(line) for line in log.read_text().splitlines()]
        numbers=matched_nontraining_seconds(result,job,arm,rows)
        records.append(dict(arm=arm, **numbers, references=[ref(p) for p in
            (config,run/'compare-result.json',run/'job.json',log)]))
    maximum=max(r['nontraining_GPU_occupancy_seconds'] for r in records)
    return dict(status='matching_completed_runs_timing_only',records=records,
        maximum_observed_nontraining_seconds=maximum,
        nontraining_reserve_seconds=max(150.,maximum*1.5),
        reserve_policy='max(150 seconds, 1.5 times maximum observed whole nontraining GPU occupancy); then 30 percent margin on training plus reserve, plus50 seconds',
        GPU_ceiling_seconds=900,quality_criteria_unchanged=True,
        limits='Nontraining occupancy includes evaluation, constructor/loading, checkpoint saves and cleanup; not a direct evaluation timer or guaranteed upper bound. Different generated lengths can change cost. Actual cumulative900-second cap remains enforced.')


def inspect():
    stored=read_json(PATH)
    actual=measured_evidence()
    if stored != actual:
        raise ValueError('Measured timing evidence changed')
    return stored


if __name__ == '__main__':
    from jmicro.training import atomic_json
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    evidence=measured_evidence()
    if PATH.exists():
        inspect()
    else:
        atomic_json(PATH,evidence)
    print({k:v for k,v in evidence.items() if k != 'records'})
