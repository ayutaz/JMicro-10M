"""Audit actual learning and apply unchanged content gates; never learns."""
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
from jmicro.natural_learning import material
from phase6_performance import alive,finite_state
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import rate
from review_eos_5b_finish import validate_rows
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import clustered_ci
from run_natural_learning import RUN,DATA,CONFIG,load_config


def audit_stage(stage):
    c=load_config();result=read_json(RUN/(stage+'-result.json'));job=read_json(RUN/('job-'+stage+'.json'))
    assert sha256(ROOT/c['tokenizer'])==c['tokenizer_sha256'] and sha256(ROOT/'eval/base.jsonl')==c['suite_sha256']
    assert all(sha256(Path(v['path']))==v['sha256'] for v in c['reference'].values())
    assert job['status']=='complete' and not alive(job)
    assert result['gpu_seconds']<=job['gpu_elapsed_seconds']<=c[{'diagnostic':'diagnostic_gpu_budget_seconds','compare':'comparison_gpu_budget_seconds','expand':'expansion_gpu_budget_seconds'}[stage]]
    if stage=='expand':
        parent=read_json(RUN/'compare-result.json')['checkpoints']['mixed-natural']
        assert result['binding']==dict(job['binding'],growth_parent=parent['checkpoint_sha256'])
    else:
        assert result['binding']==job['binding']
    assert result['binding']['plan_sha256']==sha256(CONFIG) and not result['protected_test_used']
    summaries={};samplers={}
    for arm,detail in result['checkpoints'].items():
        assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
        state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
        history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert finite_state(state) and all(k in state for k in ('optimizer','scheduler','rng','sampler','token_digest','lineage'))
        assert state['pilot_binding']==detail['binding'] and state['sampler']['source_teachers']==detail['binding']['goals']
        assert state['supervised_tokens']-state['lineage']['parent_supervised_tokens']==detail['additional_supervised_tokens']==sum(detail['binding']['goals'].values())
        assert state['tokens']-state['lineage']['parent_tokens']==detail['additional_input_tokens']==sum(state['sampler']['source_tokens'].values())
        assert len(history)==state['update']-state['lineage']['parent_update']==state['sampler']['position']
        assert [r['update'] for r in history]==list(range(state['lineage']['parent_update']+1,state['update']+1))
        assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history)
        assert state['token_digest']==history[-1]['token_digest']
        assert state['sampler']['source_physical_tokens']==detail['sampler']['source_physical_tokens']
        assert sum(state['sampler']['source_physical_tokens'].values())==detail['physical_input_tokens']>=detail['additional_input_tokens']
        samplers[arm]=state['sampler']
        previous=0;peak=detail['binding']['peak_lr'];total=detail['additional_supervised_tokens']
        for row in history:
            assert math.isclose(row['lr'],teacher_lr(previous,total,peak),rel_tol=1e-12)
            current=sum(row['source_teachers'].values());assert previous<current<=total;previous=current
        assert previous==total
        assert state['lineage']['optimizer_policy']==detail['binding']['optimizer_policy']
        memory=result['conditions'][arm]
        assert memory['checkpoint_sha256']==detail['checkpoint_sha256']
        for split,expected in [('train',64),('dev',128)]:
            rows=memory['results'][split];gold=read_json(DATA/('train64.json' if split=='train' else 'dev128.json'))
            assert len(rows['teacher'])==len(rows['generation'])==expected
            assert [r['id'] for r in rows['generation']]==[r['id'] for r in gold]
            exact=sum(r['exact_gold'] for r in rows['generation']);summary=rows['summary']
            assert exact==summary['exact_gold']==summary['appropriate_gold_eos']
            assert all(not r['exact_gold'] or r['stop_reason']=='eos' for r in rows['generation'])
            correct=sum(sum(step['target_rank']==1 for step in r['teacher_steps']) for r in rows['teacher'])
            targets=sum(len(r['teacher_steps']) for r in rows['teacher'])
            assert summary['teacher_correct']==correct and summary['teacher_targets']==targets
        summary=memory['results']['train']['summary'];goal=c['memorization_goal']
        assert memory['passed']==(summary['teacher_accuracy']>=goal and summary['exact_fraction']>=goal and summary['appropriate_fraction']>=goal)
        summaries[arm]=dict(teacher_tokens=total,valid_input=detail['additional_input_tokens'],physical_input=detail['physical_input_tokens'],
            updates=len(history),train=summary,dev=memory['results']['dev']['summary'],diagnostic_pass=memory['passed'],
            training_seconds=detail['training_seconds'],peak_allocated_bytes=detail['peak_allocated_bytes'],
            optimizer_policy=detail['binding']['optimizer_policy'],EOS_teachers=detail['source_eos_teachers'])
        del state
    assert sum(r['teacher_tokens'] for r in summaries.values())==result['scientific_teacher_tokens']
    if stage=='diagnostic':
        gate=read_json(RUN/'resume-gate.json');assert gate['passed'] and gate['binding']==job['binding']
        assert gate['optimizer_updates']==16 and all(all(r['checks'].values()) for r in gate['arms'].values())
        assert gate['verification_teacher_tokens']==result['verification_teacher_tokens']
        eligible=[a for a in ('adam-inherit','adam-fresh') if summaries[a]['diagnostic_pass']]
        selected=max(eligible,key=lambda a:(summaries[a]['train']['exact_fraction'],summaries[a]['train']['teacher_accuracy'],a=='adam-inherit')) if eligible else None
        selection=read_json(RUN/'selection.json');assert selection['selected']==selected and selection['prerequisite_met']==bool(selected)
        report=dict(status='passed_learning_evidence',stage=stage,summaries=summaries,selection=selection,
            verification_teacher_tokens=gate['verification_teacher_tokens'],scientific_teacher_tokens=result['scientific_teacher_tokens'],
            gpu_seconds=result['gpu_seconds'],quality_targets_achieved=False,protected_test_used=False)
        atomic_json(RUN/'diagnostic-review.json',report)
    else:
        annotations=read_json(RUN/(stage+'-annotations.json'));scores={};evaluations=result['evaluations'];tok=Tokenizer(ROOT/c['tokenizer'])
        cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
        for arm,evaluation in evaluations.items():
            rows=evaluation['generation']['outputs'];validate_rows(rows,tok)
            assert len(rows)==80 and evaluation['checkpoint_sha256']==result['checkpoints'][arm]['checkpoint_sha256']
            assert evaluation['binding']==result['checkpoints'][arm]['binding'] and not evaluation['protected_test_used']
            assert {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
            assert evaluation['evaluation_RNG_isolated'] and evaluation['greedy_rates']==rate(rows)
            assert evaluation['body']['documents']==256 and evaluation['body']['body_bytes']==472055
            body=evaluation['body']
            assert body['body_tokens']==122343 and all(r['scored_body_tokens']==r['body_tokens'] and math.isfinite(r['body_nll']) for r in body['rows'])
            assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12)
            assert all(evaluation['diagnostics'][k]['complete'] and evaluation['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
            entry=annotations['arms'][arm]
            assert entry['generation_sha256']==sha256(RUN/'evaluation'/arm/'evaluation/generation.json')
            notes=entry['notes'];assert len(notes)==80
            scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in notes}
            assert len(scores[arm])==80 and set(scores[arm])=={r['id'] for r in rows}
            assert all(s['rationale'] and all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) for s in scores[arm].values())
            assert all(not scores[arm][r['id']]['completion'] or r['stop_reason']=='stop_id' and scores[arm][r['id']]['relevance']>=1 and scores[arm][r['id']]['coherence']>=1 for r in rows)
            summaries[arm].update(BPB=evaluation['body']['bpb'],rates=evaluation['greedy_rates'],
                grammar_score2=sum(s['grammar']==2 for s in scores[arm].values()),relevance_score2=sum(s['relevance']==2 for s in scores[arm].values()),
                coherent=sum(s['coherence']==2 for s in scores[arm].values()),appropriate=sum(s['completion'] for s in scores[arm].values()),
                Japanese=evaluation['diagnostics'])
        if stage=='compare':
            left,right='mixed-control','mixed-natural'
            a,b=evaluations[left],evaluations[right]
            assert [(r['id'],r['prefix']) for r in a['generation']['outputs']]==[(r['id'],r['prefix']) for r in b['generation']['outputs']]
            assert samplers[left]['web']==samplers[right]['web']
            assert [(r['doc_id'],r['body_bytes']) for r in a['body']['rows']]==[(r['doc_id'],r['body_bytes']) for r in b['body']['rows']]
            differences={}
            for task in ('semantics','jblimp','jcqa'):
                l,r=[{v['id']:v for v in read_json(RUN/'evaluation'/name/'evaluation'/(task+'.json'))['rows']} for name in (left,right)]
                assert set(l)==set(r)
                differences[task]=clustered_ci([dict(id=k,family=r[k].get('family',k),difference=r[k]['credit']-l[k]['credit']) for k in l],key='difference')
            quality=quality_gates(a,b,scores[left],scores[right],'content')
            practical=dict(coherence_at_least27=summaries[right]['coherent']>=27,appropriate_at_least27=summaries[right]['appropriate']>=27,
                EOS_at_least37=b['greedy_rates']['eos']>=37,repetition_at_most18=b['greedy_rates']['repetition']<=18)
            original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),b)
            report=dict(status='passed_learning_content_evidence',summaries=summaries,quality=quality,practical=practical,original_Web_gates=original,
                eligible_for_expansion=quality['passed'] and all(practical.values()) and all(original.values()),
                scientific_teacher_tokens=result['scientific_teacher_tokens'],gpu_seconds=result['gpu_seconds'],
                paired_Japanese_differences=differences,
                independent_human_blind=False,quality_targets_achieved=False,protected_test_used=False)
            atomic_json(RUN/'review.json',report)
        else:
            # Growth must retain all original comparative and absolute quality gates.
            old=read_json(RUN/'compare-result.json');old_annotations=read_json(RUN/'compare-annotations.json')
            left={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in old_annotations['arms']['mixed-control']['notes']}
            b=evaluations['mixed-expanded'];quality=quality_gates(old['evaluations']['mixed-control'],b,left,scores['mixed-expanded'],'content')
            s=summaries['mixed-expanded'];practical=dict(coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,
                EOS_at_least37=b['greedy_rates']['eos']>=37,repetition_at_most18=b['greedy_rates']['repetition']<=18)
            original=adoption_checks(read_json(Path(c['reference']['web_screen']['path'])),b)
            report=dict(status='passed_growth_content_evidence',summaries=summaries,quality=quality,practical=practical,original_Web_gates=original,
                adopted=quality['passed'] and all(practical.values()) and all(original.values()),scientific_teacher_tokens=result['scientific_teacher_tokens'],
                gpu_seconds=result['gpu_seconds'],independent_human_blind=False,protected_test_used=False)
            atomic_json(RUN/'expansion-review.json',report)
    report.update(reviewer_sha256=sha256(Path(__file__)),config_sha256=sha256(CONFIG),result_sha256=sha256(RUN/(stage+'-result.json')),checked_at=now())
    if stage!='diagnostic':report['annotations_sha256']=sha256(RUN/(stage+'-annotations.json'))
    atomic_json(RUN/({'diagnostic':'diagnostic-review.json','compare':'review.json','expand':'expansion-review.json'}[stage]),report)
    print(json.dumps(dict(status=report['status'],stage=stage,quality=report.get('quality'),practical=report.get('practical'),eligible_for_expansion=report.get('eligible_for_expansion'),scientific_teacher_tokens=report['scientific_teacher_tokens']),ensure_ascii=False),flush=True)


def completion():
    c=load_config();diag=read_json(RUN/'diagnostic-review.json')
    reports={'diagnostic':diag}
    if diag['selection']['prerequisite_met']:
        review=read_json(RUN/'review.json');reports['compare']=review
        if review['eligible_for_expansion']:
            reports['expand']=read_json(RUN/'expansion-review.json');boundary='bounded_growth_complete'
        else:
            assert not (RUN/'job-expand.json').exists();boundary='quality_gate_rejected_growth_not_launched'
    else:
        assert 'new-init' in diag['summaries']
        assert not (RUN/'job-compare.json').exists() and not (RUN/'job-expand.json').exists();boundary='memorization_prerequisite_failed'
    for stage in reports:
        job=read_json(RUN/('job-'+stage+'.json'));assert job['status']=='complete' and not alive(job)
    ui=read_json(ROOT/'reports/local/webui/server.json');assert ui['status']=='running'
    assert ui['boot_id']==Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    assert int(ui['start_ticks'])==int(Path(f'/proc/{ui["pid"]}/stat').read_text().split()[21])
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:model=json.load(response)
    assert model['checkpoint_sha256']==c['parent']['sha256'] and model['training_tokens']==c['parent']['tokens_seen'] and not model['busy']
    files={str(p.relative_to(RUN)):p.read_text() for p in RUN.rglob('*.json') if 'source' not in p.parts}
    bundle=ROOT/'reports/phase6/natural_learning_evidence.json.gz'
    bundle.write_bytes(gzip.compress(json.dumps(files,ensure_ascii=False,separators=(',',':')).encode(),compresslevel=6,mtime=0))
    recovered=json.loads(gzip.decompress(bundle.read_bytes()));assert all(recovered[k]==v for k,v in files.items())
    result=dict(status='completed_requested_four_stage_branch',boundary=boundary,reports=reports,
        new_scientific_teacher_tokens=sum(r['scientific_teacher_tokens'] for r in reports.values()),
        verification_teacher_tokens=diag['verification_teacher_tokens'],
        gpu_seconds=sum(r['gpu_seconds'] for r in reports.values()),UI_identity=ui,UI_model=model,
        cpu_tests=4,checkpoints_and_raw_retained=True,protected_test_used=False,push_performed=False,
        evidence_bundle_sha256=sha256(bundle),created_at=now(),precision_failures_result72_unchanged=True)
    atomic_json(ROOT/'reports/phase6/natural_learning_completion.json',result)
    print(json.dumps(dict(status=result['status'],boundary=boundary,scientific=result['new_scientific_teacher_tokens'],GPU_seconds=result['gpu_seconds'])),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=('diagnostic','compare','expand','completion'));args=parser.parse_args()
    if args.stage=='completion':completion()
    else:audit_stage(args.stage)
