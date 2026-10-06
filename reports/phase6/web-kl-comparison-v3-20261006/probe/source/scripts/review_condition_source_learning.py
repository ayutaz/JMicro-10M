"""Actual matched100M checkpoints, full160 content and unchanged Base gates."""
import argparse
import json
import math
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from run_eos_short_pilot import equal_state,rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
import run_condition_source_learning as study
import run_condition_source_ranking as ranking


def notes_path(arm):return ROOT/f'reports/phase6/condition_source_learning_{arm}_notes.json'


def point(arm,template=False):
    c,base,_,data=study.inspect(study.CONFIG);progress=read_json(study.RUN/'progress-result.json')
    ev=progress['evaluations'][arm];cp=progress['checkpoints'][arm];rows=ev['generation']['outputs']
    if ev['binding']!=cp['binding'] or ev['checkpoint_sha256']!=cp['checkpoint_sha256'] or cp['additional_supervised_tokens']!=study.TOTAL:
        raise ValueError('Actual100M checkpoint/evaluation required')
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    if len(rows)!=80 or {r['id'] for r in rows}!=set(cases) or any(r['prefix']!=cases[r['id']]['prefix'] for r in rows):raise ValueError('Common originaldev80 differs')
    raw=study.RUN/f'evaluation/{arm}/evaluation/generation.json'
    if read_json(raw)!=ev['generation'] or ev['greedy_rates']!=rate(rows) or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']:
        raise ValueError('Raw generation/stop/scope differs')
    if template:
        if notes_path(arm).exists():raise ValueError('Preserve existing raw content notes')
        atomic_json(notes_path(arm),dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,
            generation_sha256=sha256(raw),notes=[[r['id'],None,None,None,None,''] for r in rows]));return
    scores=validate_notes(rows,read_json(notes_path(arm)),sha256(raw));body=ev['body']
    if (body['documents']!=256 or len(body['rows'])!=256 or body['body_bytes']!=472055 or body['body_tokens']!=122343
            or any(r['body_tokens']!=r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)):
        raise ValueError('Common byte scoring differs')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count']!=n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()):raise ValueError('Japanese evaluation incomplete')
    result=dict(BPB=body['bpb'],rates=ev['greedy_rates'],grammar2=sum(s['grammar']==2 for s in scores.values()),
        relevance2=sum(s['relevance']==2 for s in scores.values()),coherent=sum(s['coherence']==2 for s in scores.values()),
        appropriate=sum(s['completion'] for s in scores.values()),Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        new_teacher_tokens=study.TOTAL,source_teacher_tokens=study.GOALS,outcome_weight=1,
        conditional_source_documents=data[arm].manifest['documents'],mean_conditional_target_exposures=10000000/data[arm].manifest['full_CE_targets'],
        generation_sha256=sha256(raw),notes_sha256=sha256(notes_path(arm)),Base_adopted=False,independent_human_blind=False)
    atomic_json(study.RUN/f'{arm}-content-review.json',result);return result,scores


def audit():
    c,base,parent,_=study.inspect(study.CONFIG);job=read_json(study.RUN/'job.json');result=read_json(study.RUN/'compare-result.json');probe=study.probe_evidence()
    if (job['status']!='complete' or alive(job) or result['config_sha256']!=sha256(study.CONFIG)
            or result['GPU_seconds']!=job['GPU_elapsed_seconds'] or result['GPU_seconds']+probe['GPU_seconds']>study.CEILING
            or result['scientific_teacher_tokens']!=2*study.TOTAL or result['protected_test_used']
            or any(set(result[k])!=set(study.ARMS) for k in ('checkpoints','evaluations','source_rankings'))):raise ValueError('Actual complete bounded two100M study required')
    ordinary=read_json(Path(c['references']['ordinary_stream_audit']['path']));prepared=read_json(Path(c['references']['source_cases']['path']))
    if not all(ordinary['checks'].values()) or ordinary['goals']!=study.GOALS:raise ValueError('Actual common ordinary teacher audit missing')
    for arm in study.ARMS:
        record=result['checkpoints'][arm];study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
        state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False);sampler=state['sampler']
        rows=[json.loads(s) for s in (study.RUN/arm/'training/metrics.jsonl').read_text().splitlines()]
        if (not finite_state(state) or state['study_binding']!=study.binding(c,study.CONFIG,arm) or state['study_binding']!=record['binding']
                or state['supervised_tokens']!=parent['supervised_tokens']+study.TOTAL or sampler['source_teachers']!=study.GOALS
                or state['spec']['research_kind']!=study.KIND or state['spec']['outcome_weight']!=1 or state['spec']['lr']!=.0002
                or not equal_state(state['lineage']['actual_parent_sampler'],parent['sampler']) or not equal_state(state['lineage']['parent_scheduler'],parent['scheduler'])
                or state['lineage']['parent']!=c['parent'] or not state['lineage']['no_reheat']
                or any(not math.isclose(g['lr'],.0002,rel_tol=1e-10) for g in state['optimizer']['param_groups'])):
            raise ValueError('Actual inherited parent/optimizer/quota/recipe differs')
        if (len(rows)!=state['update']-parent['update'] or len(rows)!=sampler['position']
                or [r['update'] for r in rows]!=list(range(parent['update']+1,state['update']+1))
                or any(not math.isfinite(r['loss']) or not math.isfinite(r['gradient_norm']) or r['lr']!=.0002 for r in rows)
                or rows[-1]['token_digest']!=state['token_digest'] or rows[-1]['focus_token_digest']!=state['focus_token_digest']
                or state['tokens']-parent['tokens']!=len(rows)*32768 or state['tokens']-parent['tokens']!=sum(sampler['source_tokens'].values())
                or state['body_bytes']-parent['body_bytes']!=sum(sampler['source_body_bytes'].values())
                or state['weighted_teacher_mass']!=study.TOTAL or state['focus_teacher_tokens']!=sum(sampler['source_focus_teachers'].values())
                or record['additional_supervised_tokens']!=study.TOTAL or record['additional_input_tokens']!=state['tokens']-parent['tokens']):
            raise ValueError('Completed update/state/counter/digest accounting differs')
        for key,saved_key in (('source_teachers','teachers'),('source_eos','EOS'),('source_body_bytes','body_bytes')):
            if any(sampler[key][g]!=ordinary['small' if arm=='small512' else 'large'][saved_key][g] for g in ('web','story','ordinary_textbook')):
                raise ValueError('Actual completed ordinary stream differs')
        ranks=result['source_rankings'][arm];raw_rows=[]
        if (ranks['config_sha256']!=sha256(study.CONFIG) or ranks['checkpoint_sha256']!=record['checkpoint_sha256']
                or ranks['cases_sha256']!=c['references']['source_cases']['sha256'] or not all(ranks['checks'].values())
                or ranks['evaluated_requests']!=1024 or ranks['optimizer_updates'] or ranks['scientific_teacher_tokens'] or ranks['protected_test_used']):raise ValueError('Read-only original source scores incomplete')
        for start in range(0,1024,16):
            saved=read_json(study.RUN/f'source-ranking/{arm}/{start:04d}.json')
            if any(saved[k]!=ranks[k] for k in ('config_sha256','checkpoint_sha256','cases_sha256')):raise ValueError('Raw source batch binding differs')
            ranking.validate_scores(saved['rows'],prepared['cases'][start:start+16]);raw_rows.extend(saved['rows'])
        if ranks['summary']!=ranking.summarize([dict(checkpoint=arm,**r) for r in raw_rows],prepared,arms=(arm,)) or ranks['original_outcome_fit']!=study.source_fit(raw_rows,prepared):
            raise ValueError('Raw source matching/fit aggregate differs')
        del state
    summaries={};scores={}
    for arm in study.ARMS:summaries[arm],scores[arm]=point(arm)
    left,right=(result['evaluations'][a] for a in study.ARMS)
    if [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in left['body']['rows']]!=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in right['body']['rows']]:raise ValueError('Different common dev targets')
    quality=quality_gates(left,right,scores['small512'],scores['large2048'],'content')
    absolute={};original={};study.check_reference(base['reference']['web_screen'])
    for arm,s in summaries.items():
        absolute[arm]=dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,appropriate_at_least27=s['appropriate']>=27,
            EOS_at_least37=s['rates']['eos']>=37,repetition_at_most18=s['rates']['repetition']<=18,no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
        original[arm]=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),result['evaluations'][arm])
    old=read_json(Path(c['references']['previous25M_result']['path']));old_review=read_json(Path(c['references']['previous25M_review']['path']));learning={}
    for arm,key in (('small512','control'),('large2048','large2048')):
        folder=study.prior.prior.RUN if arm=='small512' else study.prior.RUN
        note=ROOT/f"reports/phase6/{'condition_positive_control' if arm=='small512' else 'condition_diversity_large2048'}_notes.json"
        raw=folder/f'evaluation/{key}/evaluation/generation.json';previous=old['evaluations'][key]
        if sha256(note)!=old_review['summaries'][key]['notes_sha256'] or sha256(raw)!=old_review['summaries'][key]['generation_sha256'] or read_json(raw)!=previous['generation']:
            raise ValueError('Historical25M notes/bytes differ')
        prev_scores=validate_notes(previous['generation']['outputs'],read_json(note),sha256(raw))
        learning[arm]=quality_gates(previous,result['evaluations'][arm],prev_scores,scores[arm],'content')
    annotations={a:dict(notes=read_json(notes_path(a))['notes'],notes_sha256=sha256(notes_path(a)),reused=False) for a in study.ARMS}
    atomic_json(study.RUN/'annotations.json',dict(reviewer='Codex nonblind',independent_human_blind=False,arms=annotations))
    report=dict(status='actual_both100M_all160_content_source128_complete',created_at=now(),summaries=summaries,quality_comparison=quality,
        absolute_dev_screen=absolute,original_Web=original,learning25M_to100M=learning,
        learning_reference_note='Same data/parent/nominal recipe with different teacher budgets; historical25M terminal masks differ, not guaranteed exact trajectory prefixes or independent quality replication.',
        source_rankings={a:dict(aggregate=result['source_rankings'][a]['summary']['aggregate'][a],original_outcome_fit=result['source_rankings'][a]['original_outcome_fit']) for a in study.ARMS},
        eligible_for_final_Base_validation={a:all(absolute[a].values()) and all(original[a].values()) for a in study.ARMS},
        new_scientific_teacher_tokens=2*study.TOTAL,verification_teacher_tokens=probe['verification_teacher_tokens'],GPU_seconds=result['GPU_seconds'],verification_GPU_seconds=probe['GPU_seconds'],
        result_sha256=sha256(study.RUN/'compare-result.json'),annotations_sha256=sha256(study.RUN/'annotations.json'),ordinary_stream_checks=ordinary['checks'],
        Base_adopted=False,Chat_adopted=False,protected_test_used=False,independent_human_blind=False,quality_criteria_unchanged=True,old_numerical7_preserved=True,requested_five_steps_complete=False)
    atomic_json(study.RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/condition_source_learning_review.json',report)
    print(json.dumps(report,ensure_ascii=False),flush=True)


def archive():
    c,*_=study.inspect(study.CONFIG);job=read_json(study.RUN/'job.json');review=read_json(study.RUN/'review.json')
    if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'):raise ValueError('Terminal raw-bound review required')
    target=ROOT/'reports/phase6/condition-source-learning-100m-20261006_evidence.tar.gz'
    if target.exists():raise ValueError('Evidence archive immutable')
    paths={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.lock')}
    paths.update((study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,Path(c['references']['source_cases']['path']),ROOT/'reports/phase6/condition_source_learning_tests.xml',*(notes_path(a) for a in study.ARMS)))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)];temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target);manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),checkpoint_tensors_included=False)
    atomic_json(ROOT/'reports/phase6/condition_source_learning_evidence_manifest.json',manifest);print(json.dumps({k:v for k,v in manifest.items() if k!='entries'}),flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);p=argparse.ArgumentParser();p.add_argument('--arm',choices=study.ARMS,default='small512');mode=p.add_mutually_exclusive_group()
    mode.add_argument('--template',action='store_true');mode.add_argument('--point',action='store_true');mode.add_argument('--archive',action='store_true');args=p.parse_args()
    if args.template or args.point:point(args.arm,args.template)
    elif args.archive:archive()
    else:audit()
