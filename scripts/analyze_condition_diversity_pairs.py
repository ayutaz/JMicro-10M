"""Secondary paired-context ranking analysis; reuse completed192 dev scores."""
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from analyze_condition_positive_pairs import pair_categories


def main():
    started=time.monotonic(); run=ROOT/'reports/phase6/condition-diversity-comparison-20261006'
    job=read_json(run/'job.json'); result=read_json(run/'compare-result.json'); review=read_json(run/'review.json')
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(run/'compare-result.json')
            or review['new_scientific_teacher_tokens']!=25000000 or review['protected_test_used']):
        raise ValueError('Actual completed reviewed25M expansion comparison required')
    config=read_json(ROOT/'configs/phase6/condition_diversity_comparison.json')
    base=read_json(Path(config['original_config']['path'])); suite=ROOT/'eval/japanese_semantics_v2_1.jsonl'
    if sha256(suite)!=base['evaluation']['semantic_sha256']: raise ValueError('Fixed dev suite changed')
    cases={r['id']:r for r in (json.loads(s) for s in suite.read_text().splitlines()) if r['split']=='dev'}
    paths=dict(control=ROOT/'reports/phase6/condition-positive-comparison-20261006/evaluation/control/evaluation/semantics.json',
        large2048=run/'evaluation/large2048/evaluation/semantics.json',
        parent2B=ROOT/'reports/phase6/textbook-coverage-2b-20261006/evaluation/large-2000000000/evaluation/semantics.json')
    models={}; refs={}
    for arm,path in paths.items():
        raw=read_json(path); rows=raw['rows']; binding=json.loads(raw['binding'])
        cp=config['parent']['sha256'] if arm=='parent2B' else result['checkpoints'][arm]['checkpoint_sha256']
        if (not raw['complete'] or raw['expected']!=192 or len(rows)!=192 or len({r['id'] for r in rows})!=192
                or {r['id'] for r in rows}!=set(cases) or binding['checkpoint_sha256']!=cp
                or any(any(r[k]!=cases[r['id']][k] for k in ('family','category','split','context','choices','label')) for r in rows)):
            raise ValueError('Actual common192 contexts/weights differ')
        models[arm]=pair_categories(rows)
        if (set(models[arm])!={'negation','quantity','time','comparison','coreference','causality'}
                or any(g['families']!=16 for g in models[arm].values())
                or not math.isclose(sum(r['credit'] for r in rows)/192,raw['summary']['primary']['accuracy']['point'],abs_tol=1e-12)):
            raise ValueError('Six categories and96 complete paired families required')
        refs[arm]=dict(path=str(path),sha256=sha256(path),checkpoint_sha256=cp)
    report=dict(status='completed_nested_source_fixed_dev_condition_pair_analysis',models=models,references=refs,
        suite_sha256=sha256(suite),study_review_sha256=sha256(run/'review.json'),script_sha256=sha256(Path(__file__)),
        pair_analysis_source_sha256=sha256(ROOT/'scripts/analyze_condition_positive_pairs.py'),
        actual_GPU_seconds=0,scientific_teacher_tokens=0,new_original_tokens=0,protected_test_used=False,
        Base_adopted=False,Chat_adopted=False,requested_five_steps_complete=False,CPU_seconds=time.monotonic()-started,
        created_at=now(),limitations='Same fixed96 dev families, one learned seed; descriptive ranking/context sensitivity, not independent generalization, fluent generation, attention failure or capacity proof. No dev texts enter learning; source quantity comparison uses existing train only.')
    atomic_json(ROOT/'reports/phase6/condition_diversity_condition_pair_analysis.json',report)
    print(json.dumps({m:{k:{x:v for x,v in g.items() if x!='pairs'} for k,g in cats.items()} for m,cats in models.items()}),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
