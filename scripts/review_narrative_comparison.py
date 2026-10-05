"""Audit actual training and raw-bound content under the unchanged quality gates."""
import argparse
import gzip
import json
import math
from pathlib import Path
import sys
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.packing_study import teacher_lr
from jmicro.narrative_study import structural_summary
from jmicro.japanese_evaluation import clustered_ci
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate
from review_eos_5b_finish import validate_rows
from run_narrative_comparison import RUN,DATA,CONFIG,load_config


def audit(stage):
    c=load_config();result=read_json(RUN/(stage+'-result.json'));job=read_json(RUN/('job-'+stage+'.json'))
    assert job['status']=='complete' and not alive(job)
    assert result['binding']['plan_sha256']==sha256(CONFIG) and not result['protected_test_used']
    assert result['gpu_seconds']<=job['gpu_elapsed_seconds']<=c['comparison_gpu_budget_seconds' if stage=='compare' else 'expansion_gpu_budget_seconds']
    if stage=='compare':assert result['binding']==job['binding']
    else:
        assert result['binding']['growth_parent']==read_json(RUN/'compare-result.json')['checkpoints']['mixed-diverse']['checkpoint_sha256']
        assert result['binding']['growth_preparation_sha256']==sha256(DATA/'ready-expanded.json')
        assert result['binding']['growth_review_sha256']==sha256(RUN/'expanded-content-review.json')
    annotations=read_json(RUN/(stage+'-annotations.json'));scores={};summaries={};samplers={};tok=Tokenizer(ROOT/c['tokenizer'])
    cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    for arm,detail in result['checkpoints'].items():
        assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
        state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
        history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert finite_state(state) and all(k in state for k in ('optimizer','scheduler','rng','sampler','token_digest','lineage'))
        assert state['pilot_binding']==detail['binding'] and state['sampler']['source_teachers']==detail['binding']['goals']
        assert state['lineage']['optimizer_policy']=='inherit'
        assert state['supervised_tokens']-state['lineage']['parent_supervised_tokens']==detail['additional_supervised_tokens']==sum(detail['binding']['goals'].values())
        assert state['tokens']-state['lineage']['parent_tokens']==detail['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert len(history)==state['update']-state['lineage']['parent_update']==state['sampler']['position']
        assert [r['update'] for r in history]==list(range(state['lineage']['parent_update']+1,state['update']+1))
        assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history)
        assert state['token_digest']==history[-1]['token_digest']
        assert state['sampler']['source_physical_tokens']==detail['sampler']['source_physical_tokens']
        assert sum(state['sampler']['source_physical_tokens'].values())==detail['physical_input_tokens']>=detail['additional_input_tokens']
        previous=0;total=detail['additional_supervised_tokens']
        for row in history:
            assert math.isclose(row['lr'],teacher_lr(previous,total,detail['binding']['peak_lr']),rel_tol=1e-12)
            current=sum(row['source_teachers'].values());assert previous<current<=total;previous=current
        assert previous==total;samplers[arm]=state['sampler'];del state
        evaluation=result['evaluations'][arm];rows=evaluation['generation']['outputs'];validate_rows(rows,tok)
        assert len(rows)==80 and evaluation['checkpoint_sha256']==detail['checkpoint_sha256'] and evaluation['binding']==detail['binding']
        assert not evaluation['protected_test_used'] and evaluation['evaluation_RNG_isolated'] and evaluation['greedy_rates']==rate(rows)
        assert {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
        body=evaluation['body'];assert body['documents']==256 and body['body_bytes']==472055 and body['body_tokens']==122343
        assert all(r['scored_body_tokens']==r['body_tokens'] and math.isfinite(r['body_nll']) for r in body['rows'])
        assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12)
        assert all(evaluation['diagnostics'][k]['complete'] and evaluation['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
        entry=annotations['arms'][arm];assert entry['generation_sha256']==sha256(RUN/'evaluation'/arm/'evaluation/generation.json')
        notes=entry['notes'];assert len(notes)==80
        scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
        assert set(scores[arm])==set(cases) and len(scores[arm])==80
        assert all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values())
        assert all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' and scores[arm][r['id']]['relevance']>=1 and scores[arm][r['id']]['coherence']>=1 for r in rows)
        structure=result['structures'][arm];assert structure['checkpoint_sha256']==detail['checkpoint_sha256'] and structure['dev64_sha256']==c['dev64_sha256']
        assert structure['groups']==structural_summary(structure['body'],read_json(DATA/'dev64.json'))
        assert structure['body']['documents']==64 and structure['body']['body_bytes']==51110
        assert all(v['documents']==32 for v in structure['groups'].values())
        summaries[arm]=dict(teacher_tokens=total,valid_input=detail['additional_input_tokens'],physical_input=detail['physical_input_tokens'],
            updates=len(history),training_seconds=detail['training_seconds'],peak_allocated_bytes=detail['peak_allocated_bytes'],
            EOS_teachers=detail['source_eos_teachers'],BPB=body['bpb'],rates=evaluation['greedy_rates'],
            grammar_score2=sum(s['grammar']==2 for s in scores[arm].values()),relevance_score2=sum(s['relevance']==2 for s in scores[arm].values()),
            coherent=sum(s['coherence']==2 for s in scores[arm].values()),appropriate=sum(s['completion'] for s in scores[arm].values()),
            Japanese=evaluation['diagnostics'],structural=structure['groups'])
    assert sum(v['teacher_tokens'] for v in summaries.values())==result['scientific_teacher_tokens']
    if stage=='compare':
        left,right='mixed-control','mixed-diverse';a,b=[result['evaluations'][k] for k in (left,right)]
        assert samplers[left]['web']==samplers[right]['web']
        assert [(r['id'],r['prefix']) for r in a['generation']['outputs']]==[(r['id'],r['prefix']) for r in b['generation']['outputs']]
        assert [(r['doc_id'],r['body_bytes']) for r in a['body']['rows']]==[(r['doc_id'],r['body_bytes']) for r in b['body']['rows']]
        gate=read_json(RUN/'resume-gate.json');assert gate['binding']==job['binding'] and gate['passed'] and all(gate['checks'].values())
        assert gate['optimizer_updates']==8 and gate['verification_teacher_tokens']==result['verification_teacher_tokens']
        left_scores=scores[left];differences={}
        for task in ('semantics','jblimp','jcqa'):
            l,r=[{v['id']:v for v in read_json(RUN/'evaluation'/name/'evaluation'/(task+'.json'))['rows']} for name in (left,right)]
            assert set(l)==set(r)
            differences[task]=clustered_ci([dict(id=k,family=r[k].get('family',k),difference=r[k]['credit']-l[k]['credit']) for k in l],key='difference')
    else:
        right='mixed-expanded';a=read_json(RUN/'compare-result.json')['evaluations']['mixed-control'];b=result['evaluations'][right]
        old_notes=read_json(RUN/'compare-annotations.json')['arms']['mixed-control']['notes']
        left_scores={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in old_notes};differences={}
    quality=quality_gates(a,b,left_scores,scores[right],'content');s=summaries[right]
    practical=dict(coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,
        EOS_at_least37=b['greedy_rates']['eos']>=37,repetition_at_most18=b['greedy_rates']['repetition']<=18)
    assert all(sha256(Path(v['path']))==v['sha256'] for v in c['reference'].values())
    original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),b)
    passed=quality['passed'] and all(practical.values()) and all(original.values())
    report=dict(status='passed_learning_content_evidence',summaries=summaries,quality=quality,practical=practical,original_Web_gates=original,
        eligible_for_expansion=passed if stage=='compare' else False,adopted=passed if stage=='expand' else False,
        scientific_teacher_tokens=result['scientific_teacher_tokens'],verification_teacher_tokens=result['verification_teacher_tokens'],
        gpu_seconds=result['gpu_seconds'],paired_Japanese_differences=differences,independent_human_blind=False,
        quality_targets_achieved=passed,protected_test_used=False,reviewer_sha256=sha256(Path(__file__)),
        annotations_sha256=sha256(RUN/(stage+'-annotations.json')),result_sha256=sha256(RUN/(stage+'-result.json')),config_sha256=sha256(CONFIG),checked_at=now())
    atomic_json(RUN/('review.json' if stage=='compare' else 'expansion-review.json'),report)
    print(json.dumps(dict(stage=stage,summaries={k:{n:v[n] for n in ('teacher_tokens','BPB','rates','coherent','appropriate')} for k,v in summaries.items()},quality=quality,practical=practical,eligible_for_expansion=report['eligible_for_expansion']),ensure_ascii=False),flush=True)


def completion():
    c=load_config();review=read_json(RUN/'review.json');reports={'compare':review}
    if review['eligible_for_expansion']:
        if (RUN/'expansion-review.json').exists():reports['expand']=read_json(RUN/'expansion-review.json');boundary='bounded_growth_complete'
        else:
            failure=read_json(RUN/'growth-not-launched.json');assert failure['reason']=='frozen_preparation_failed' and not (RUN/'job-expand.json').exists()
            boundary='growth_preparation_failed'
    else:
        assert not (RUN/'job-expand.json').exists();boundary='quality_gate_rejected_growth_not_launched'
    for stage in reports:
        job=read_json(RUN/('job-'+stage+'.json'));assert job['status']=='complete' and not alive(job)
    ui=read_json(ROOT/'reports/local/webui/server.json');assert ui['status']=='running'
    assert ui['boot_id']==Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    assert int(ui['start_ticks'])==int(Path(f'/proc/{ui["pid"]}/stat').read_text().split()[21])
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:model=json.load(response)
    assert model['checkpoint_sha256']==c['parent']['sha256'] and model['training_tokens']==c['parent']['tokens_seen'] and not model['busy']
    files={str(p.relative_to(RUN)):p.read_text() for p in RUN.rglob('*.json') if 'source' not in p.parts}
    bundle=ROOT/'reports/phase6/narrative_diversity_evidence.json.gz'
    bundle.write_bytes(gzip.compress(json.dumps(files,ensure_ascii=False,separators=(',',':')).encode(),compresslevel=6,mtime=0))
    assert json.loads(gzip.decompress(bundle.read_bytes()))==files
    out=dict(status='completed_requested_three_stage_branch',boundary=boundary,reports=reports,
        new_scientific_teacher_tokens=sum(r['scientific_teacher_tokens'] for r in reports.values()),
        verification_teacher_tokens=review['verification_teacher_tokens'],gpu_seconds=sum(r['gpu_seconds'] for r in reports.values()),
        UI_identity=ui,UI_model=model,cpu_tests=9,checkpoints_and_raw_retained=True,protected_test_used=False,push_performed=False,
        evidence_bundle_sha256=sha256(bundle),created_at=now(),precision_failures_result72_unchanged=True)
    atomic_json(ROOT/'reports/phase6/narrative_diversity_completion.json',out)
    print(json.dumps(dict(status=out['status'],boundary=boundary,scientific=out['new_scientific_teacher_tokens'],GPU_seconds=out['gpu_seconds'])),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=('compare','expand','completion'));args=parser.parse_args()
    if args.stage=='completion':completion()
    else:audit(args.stage)
