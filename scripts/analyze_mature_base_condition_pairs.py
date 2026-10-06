"""Analyze already scored fixeddev96 opposed families; additional GPU/learning0."""
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
from analyze_condition_positive_pairs import pair_categories
import run_mature_base_condition_comparison as study


def main():
    started = time.monotonic(); job = read_json(study.RUN / 'job.json')
    result = read_json(study.RUN / 'compare-result.json'); c = read_json(study.CONFIG)
    if job['status'] != 'complete' or alive(job) or result['config_sha256'] != sha256(study.CONFIG) or result['protected_test_used']:
        raise ValueError('Actual terminal same300M study required')
    base = read_json(Path(c['original_config']['path'])); suite = ROOT / base['evaluation']['semantic_suite']
    if sha256(suite) != base['evaluation']['semantic_sha256']: raise ValueError('Fixed dev suite changed')
    cases = {r['id']:r for r in (json.loads(s) for s in suite.read_text().splitlines()) if r['split'] == 'dev'}
    models, references = {}, {}
    for arm in ('parent10B', *study.ARMS):
        path = study.RUN / f'evaluation/{arm}/evaluation/semantics.json'
        raw = read_json(path); rows = raw['rows']; bound = json.loads(raw['binding'])
        cp = result['checkpoints'][arm]['checkpoint_sha256']
        if (not raw['complete'] or raw['expected'] != 192 or len(rows) != 192 or len({r['id'] for r in rows}) != 192
                or {r['id'] for r in rows} != set(cases) or bound['checkpoint_sha256'] != cp
                or bound['binding'] != result['checkpoints'][arm]['binding']
                or any(any(r[k] != cases[r['id']][k] for k in ('family','category','split','context','choices','label')) for r in rows)):
            raise ValueError('All192 identical contexts/choices and actual checkpoint required')
        models[arm] = pair_categories(rows)
        if (any(r['families'] != 16 for r in models[arm].values())
                or not math.isclose(sum(r['credit'] for r in rows)/192, raw['summary']['primary']['accuracy']['point'], abs_tol=1e-12)):
            raise ValueError('Six categories/96 complete opposed families required')
        references[arm] = dict(path=str(path), sha256=sha256(path), checkpoint_sha256=cp)
    report = dict(status='actual_mature_parent_matched300M_fixeddev96_pairs_reused', created_at=now(), models=models,
        references=references, result_sha256=sha256(study.RUN / 'compare-result.json'), suite_sha256=sha256(suite),
        script_sha256=sha256(Path(__file__)), CPU_seconds=time.monotonic()-started, actual_GPU_seconds=0,
        scientific_teacher_tokens=0, protected_test_used=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        limitations='Repeatedly inspected fixeddev and one learned seed; descriptive context response, separate from fluent generation and local generator probes. Not an isolated parent-training-amount causal comparison.')
    atomic_json(ROOT / 'reports/phase6/mature_base_condition_pair_analysis.json', report)
    print({a:{k:r['both_correct'] for k,r in groups.items()} for a,groups in models.items()})


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
