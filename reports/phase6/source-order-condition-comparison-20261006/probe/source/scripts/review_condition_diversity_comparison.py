"""Completed nested-source25M and reused control; raw80 content and old gates."""
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
import review_condition_positive_comparison as old_review
import run_condition_diversity_comparison as study

NOTES=ROOT/'reports/phase6/condition_diversity_large2048_notes.json'


def point(template=False):
    c,base,parent,control,control_ev,_=study.inspect(study.CONFIG)
    progress=read_json(study.RUN/'progress-result.json'); arm=study.ARM
    ev=progress['evaluations'][arm]; trained=progress['checkpoints'][arm]; rows=ev['generation']['outputs']
    if ev['binding']!=trained['binding'] or ev['checkpoint_sha256']!=trained['checkpoint_sha256']: raise ValueError('Actual checkpoint differs')
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    if len(rows)!=80 or {r['id'] for r in rows}!=set(cases) or any(r['prefix']!=cases[r['id']]['prefix'] for r in rows): raise ValueError('Fixed dev80 differs')
    raw=study.RUN/'evaluation'/arm/'evaluation/generation.json'
    if read_json(raw)!=ev['generation'] or ev['greedy_rates']!=rate(rows) or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']: raise ValueError('Raw generation/scope differs')
    if template:
        if NOTES.exists(): raise ValueError('Preserve existing content notes')
        atomic_json(NOTES,dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,
            generation_sha256=sha256(raw),notes=[[r['id'],None,None,None,None,''] for r in rows])); return
    scores=validate_notes(rows,read_json(NOTES),sha256(raw)); body=ev['body']
    if (body['documents']!=256 or len(body['rows'])!=256 or body['body_bytes']!=472055 or body['body_tokens']!=122343
            or any(r['body_tokens']!=r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)):
        raise ValueError('Common body byte scoring differs')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count']!=n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()): raise ValueError('Japanese evaluation incomplete')
    summary=dict(BPB=body['bpb'],rates=ev['greedy_rates'],grammar2=sum(s['grammar']==2 for s in scores.values()),
        relevance2=sum(s['relevance']==2 for s in scores.values()),coherent=sum(s['coherence']==2 for s in scores.values()),
        appropriate=sum(s['completion'] for s in scores.values()),Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        new_teacher_tokens=study.TOTAL,source_teacher_tokens=study.GOALS,outcome_weight=1,
        conditional_source_documents=2048,generation_sha256=sha256(raw),notes_sha256=sha256(NOTES),
        Base_adopted=False,independent_human_blind=False)
    atomic_json(study.RUN/'large2048-content-review.json',summary)
    return summary,scores


def audit():
    c,base,parent,control,control_ev,_=study.inspect(study.CONFIG)
    job=read_json(study.RUN/'job.json'); result=read_json(study.RUN/'compare-result.json'); probe=study.probe_evidence()
    if (job['status']!='complete' or alive(job) or result['config_sha256']!=sha256(study.CONFIG)
            or result['GPU_seconds']!=job['GPU_elapsed_seconds'] or result['GPU_seconds']+probe['GPU_seconds']>study.CEILING
            or result['scientific_teacher_tokens']!=study.TOTAL or result['reused_control_teacher_tokens']!=study.TOTAL
            or result['total_comparison_teacher_tokens']!=2*study.TOTAL or result['protected_test_used']
            or result['checkpoints']['control']!=control or result['evaluations']['control']!=control_ev):
        raise ValueError('Actual complete bounded25M and reused25M required')
    record=result['checkpoints'][study.ARM]; cp=Path(record['checkpoint'])
    study.check_reference(dict(path=str(cp),sha256=record['checkpoint_sha256']))
    state=torch.load(cp,map_location='cpu',weights_only=False)
    rows=[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()]
    sampler=state['sampler']
    if (not finite_state(state) or state['study_binding']!=study.binding(c,study.CONFIG)
            or state['study_binding']!=record['binding'] or state['supervised_tokens']!=parent['supervised_tokens']+study.TOTAL
            or sampler['source_teachers']!=study.GOALS or state['spec']['outcome_weight']!=1
            or state['spec']['research_kind']!='nested_condition_source_quantity' or state['spec']['lr']!=.0002
            or not equal_state(state['lineage']['actual_parent_sampler'],parent['sampler'])
            or not equal_state(state['lineage']['parent_scheduler'],parent['scheduler'])
            or state['lineage']['parent']!=c['parent'] or not state['lineage']['no_reheat']
            or any(not math.isclose(g['lr'],.0002,rel_tol=1e-10) for g in state['optimizer']['param_groups'])):
        raise ValueError('Actual parent/optimizer/source recipe differs')
    if (len(rows)!=state['update']-parent['update'] or len(rows)!=sampler['position']
            or [r['update'] for r in rows]!=list(range(parent['update']+1,state['update']+1))
            or any(not math.isfinite(r['loss']) or not math.isfinite(r['gradient_norm']) or r['lr']!=.0002 for r in rows)
            or rows[-1]['token_digest']!=state['token_digest'] or rows[-1]['focus_token_digest']!=state['focus_token_digest']
            or state['tokens']-parent['tokens']!=sum(sampler['source_tokens'].values())
            or state['tokens']-parent['tokens']!=len(rows)*32768
            or state['body_bytes']-parent['body_bytes']!=sum(sampler['source_body_bytes'].values())
            or state['weighted_teacher_mass']!=study.TOTAL or state['focus_teacher_tokens']!=sum(sampler['source_focus_teachers'].values())
            or record['additional_supervised_tokens']!=study.TOTAL or record['additional_input_tokens']!=state['tokens']-parent['tokens']):
        raise ValueError('Completed update/teacher/input/digest accounting differs')
    ordinary=read_json(Path(c['references']['ordinary_stream_audit']['path']))
    if (not all(ordinary['checks'].values()) or ordinary['large_manifest_sha256']!=c['positive_data']['manifest_sha256']
            or ordinary['small_manifest_sha256']!=c['small_data']['manifest_sha256']): raise ValueError('Exact ordinary target sequence audit missing')
    for key,saved_key in (('source_teachers','teachers'),('source_eos','EOS'),('source_body_bytes','body_bytes')):
        if any(sampler[key][g]!=ordinary['large'][saved_key][g] for g in ('web','story','ordinary_textbook')):
            raise ValueError('Actual completed ordinary stream count/bytes differ')
    large,large_scores=point(); small,small_scores=old_review.point('control')
    if ([(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in control_ev['body']['rows']]
            !=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in result['evaluations'][study.ARM]['body']['rows']]): raise ValueError('Different dev byte targets')
    quality=quality_gates(control_ev,result['evaluations'][study.ARM],small_scores,large_scores,'content')
    summaries=dict(control=small,large2048=large); absolute={}; original={}
    study.check_reference(base['reference']['web_screen'])
    for arm,s in summaries.items():
        absolute[arm]=dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,
            appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,
            repetition_at_most18=s['rates']['repetition']<=18,no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
        original[arm]=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),result['evaluations'][arm])
    annotations=dict(reviewer='Codex nonblind',independent_human_blind=False,
        control=dict(notes=read_json(old_review.notes_path('control'))['notes'],notes_sha256=sha256(old_review.notes_path('control')),reused=True),
        large2048=dict(notes=read_json(NOTES)['notes'],notes_sha256=sha256(NOTES),reused=False))
    atomic_json(study.RUN/'annotations.json',annotations)
    report=dict(status='nested512_vs2048_same25M_actual_all160_content_complete',created_at=now(),summaries=summaries,
        quality_comparison=quality,absolute_dev_screen=absolute,original_Web=original,
        eligible_for_final_Base_validation={arm:all(absolute[arm].values()) and all(original[arm].values()) for arm in summaries},
        new_scientific_teacher_tokens=study.TOTAL,reused_control_teacher_tokens=study.TOTAL,total_comparison_teacher_tokens=2*study.TOTAL,
        verification_teacher_tokens=probe['verification_teacher_tokens'],GPU_seconds=result['GPU_seconds'],verification_GPU_seconds=probe['GPU_seconds'],
        ordinary_stream_checks=ordinary['checks'],result_sha256=sha256(study.RUN/'compare-result.json'),annotations_sha256=sha256(study.RUN/'annotations.json'),
        Base_adopted=False,Chat_adopted=False,protected_test_used=False,independent_human_blind=False,
        quality_criteria_unchanged=True,old_numerical7_preserved=True,requested_five_steps_complete=False)
    atomic_json(study.RUN/'review.json',report); atomic_json(ROOT/'reports/phase6/condition_diversity_comparison_review.json',report)
    print(json.dumps(report,ensure_ascii=False),flush=True)


def archive():
    c,*_=study.inspect(study.CONFIG); job=read_json(study.RUN/'job.json'); review=read_json(study.RUN/'review.json')
    if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'): raise ValueError('Complete raw-bound review required')
    target=ROOT/'reports/phase6/condition-diversity-comparison-20261006_evidence.tar.gz'
    if target.exists(): raise ValueError('Evidence archive immutable')
    paths={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.lock')}
    paths.update((study.CONFIG,study.PROBE_CONFIG,NOTES,old_review.notes_path('control'),
        ROOT/'reports/phase6/condition_diversity_comparison_tests.xml'))
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)]
    temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths): stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target)
    atomic_json(ROOT/'reports/phase6/condition_diversity_comparison_evidence_manifest.json',dict(entries=entries,
        text_files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),checkpoint_tensors_included=False))
    print(dict(archive=str(target),sha256=sha256(target)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2); p=argparse.ArgumentParser(); modes=p.add_mutually_exclusive_group()
    modes.add_argument('--template',action='store_true'); modes.add_argument('--point',action='store_true'); modes.add_argument('--archive',action='store_true')
    args=p.parse_args()
    if args.template or args.point: point(args.template)
    elif args.archive: archive()
    else: audit()
