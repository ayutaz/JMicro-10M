"""Reuse source ranking scores for original-outcome fit and local exposure counts."""
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_condition_source_ranking as study


def main():
    started=time.monotonic(); c,prepared=study.inspect()
    review=read_json(study.RUN/'review.json'); result=read_json(study.RUN/'result.json');job=read_json(study.RUN/'job.json')
    if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'result.json'):
        raise ValueError('All actual scores and terminal review required')
    families={f['index']:f for f in prepared['families']}; groups={}
    for arm in study.ARMS:
        by_index={}
        for start in range(0,1024,16):
            saved=read_json(study.RUN/'outputs'/arm/f'{start:04d}.json'); cases=prepared['cases'][start:start+16]
            if (saved['checkpoint_sha256']!=c['checkpoints'][arm]['sha256']
                    or saved['cases_sha256']!=c['references']['cases']['sha256']
                    or saved['config_sha256']!=sha256(study.CONFIG)): raise ValueError('Raw scores changed')
            study.validate_scores(saved['rows'],cases);by_index.update({r['index']:r for r in saved['rows']})
        groups[arm]={}
        for mode in study.MODES:
            groups[arm][mode]={}
            for subset in ('all128','nonweak116','old512_fixed64','new1536_fixed64'):
                cases=[r for r in prepared['cases'] if r['mode']==mode and r['candidate']==r['source_matching_label']
                    and (subset=='all128' or (subset=='nonweak116' and not families[r['family']]['content_annotation']['weak_pair']) or r['group']==subset)]
                rows=[by_index[r['index']] for r in cases]; tokens=sum(r['target_tokens'] for r in rows); bytes_=sum(r['target_bytes'] for r in rows)
                nll=-sum(r['log_likelihood'] for r in rows)
                groups[arm][mode][subset]=dict(outcomes=len(rows),target_tokens=tokens,target_bytes=bytes_,NLL_sum=nll,
                    token_weighted_mean_NLL=nll/tokens,byte_weighted_mean_NLL=nll/bytes_)
    # The actual sampler used native data manifests, not optional portable copies.
    recipes=dict(control512=ROOT/'configs/phase6/condition_positive_comparison.json',
        large2048=ROOT/'configs/phase6/condition_diversity_comparison.json')
    manifests={arm:Path(read_json(recipe)['positive_data']['path'])/'manifest.json' for arm,recipe in recipes.items()}
    exposure={}
    comparison=read_json(ROOT/'reports/phase6/condition-diversity-comparison-20261006/compare-result.json')
    for arm,path in manifests.items():
        manifest=read_json(path);binding=comparison['checkpoints']['control' if arm=='control512' else 'large2048']['binding']
        if sha256(path)!=binding['positive_manifest_sha256']: raise ValueError('Actual original CE manifest differs')
        exposure[arm]=dict(manifest_path=str(path),manifest_sha256=sha256(path),full_CE_targets=manifest['full_CE_targets'],conditional_teacher_tokens=2500000,
            average_conditional_target_exposures=2500000/manifest['full_CE_targets'],
            caveat='Aggregate teacher mass / prepared CE target count, not exact equal repetitions per document or sampler epoch. Same full25M teacher budget, distinct source sizes.')
    report=dict(status='actual_original_outcome_fit_and_source_exposure_reused',created_at=now(),groups=groups,exposure=exposure,
        ranking_review_sha256=sha256(study.RUN/'review.json'),ranking_result_sha256=sha256(study.RUN/'result.json'),
        script_sha256=sha256(Path(__file__)),CPU_seconds=time.monotonic()-started,actual_GPU_seconds=0,scientific_teacher_tokens=0,
        protected_test_used=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        limitations='Fixed selected train128 and original source-matching targets, not heldout quality, incompatible negatives, total corpus fit or causal proof of exposure insufficiency. Complete and isolated contexts have different histories; primary Base scoring/gates unchanged.')
    atomic_json(ROOT/'reports/phase6/condition_source_ranking_fit_analysis.json',report)
    print(json.dumps(dict(exposure=exposure,original_history={a:{g:round(v['token_weighted_mean_NLL'],6) for g,v in groups[a]['original_history'].items()} for a in study.ARMS})),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
