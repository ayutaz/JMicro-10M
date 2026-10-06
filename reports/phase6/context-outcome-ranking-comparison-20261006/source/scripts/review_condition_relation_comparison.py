"""New100M fullstate/all80 vs raw preserved natural100M; unchanged Base gates."""
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
import run_condition_relation_comparison as study

NOTES=ROOT/'reports/phase6/condition_relation_language_notes.json'


def point(template=False):
    c,base,_,_,_,positive=study.inspect(study.CONFIG);r=read_json(study.RUN/'progress-result.json')
    ev=r['evaluations'][study.ARM];record=r['checkpoints'][study.ARM];rows=ev['generation']['outputs']
    raw=study.RUN/f'evaluation/{study.ARM}/evaluation/generation.json'
    if (ev['binding']!=record['binding'] or ev['checkpoint_sha256']!=record['checkpoint_sha256'] or record['additional_supervised_tokens']!=study.TOTAL
            or read_json(raw)!=ev['generation'] or ev['greedy_rates']!=rate(rows) or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']):
        raise ValueError('Actual100M raw generation/lineage required')
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    if len(rows)!=80 or {r['id'] for r in rows}!=set(cases) or any(r['prefix']!=cases[r['id']]['prefix'] for r in rows):raise ValueError('Fixed originaldev80 differs')
    if template:
        if NOTES.exists():raise ValueError('Preserve existing content notes')
        atomic_json(NOTES,dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,
            generation_sha256=sha256(raw),notes=[[r['id'],None,None,None,None,''] for r in rows]));return
    scores=validate_notes(rows,read_json(NOTES),sha256(raw));body=ev['body']
    if (body['documents']!=256 or len(body['rows'])!=256 or body['body_bytes']!=472055 or body['body_tokens']!=122343
            or any(v['body_tokens']!=v['scored_body_tokens'] or not math.isfinite(v['body_nll']) for v in body['rows'])
            or not math.isclose(body['bpb'],sum(v['body_nll'] for v in body['rows'])/math.log(2)/472055,rel_tol=1e-12)):
        raise ValueError('Complete common-byte body dev required')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count']!=n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()):raise ValueError('Complete Japanese diagnostics required')
    summary=dict(BPB=body['bpb'],rates=ev['greedy_rates'],grammar2=sum(v['grammar']==2 for v in scores.values()),relevance2=sum(v['relevance']==2 for v in scores.values()),
        coherent=sum(v['coherence']==2 for v in scores.values()),appropriate=sum(v['completion'] for v in scores.values()),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        new_teacher_tokens=study.TOTAL,source_teacher_tokens=study.GOALS,outcome_weight=1,conditional_source_documents=2048,
        mean_conditional_target_exposures=10000000/positive.manifest['full_CE_targets'],generated_serialized_tokens=positive.manifest['serialized_tokens'],
        generation_sha256=sha256(raw),notes_sha256=sha256(NOTES),Base_adopted=False,independent_human_blind=False)
    atomic_json(study.RUN/'relation-content-review.json',summary);return summary,scores


def audit():
    c,base,parent,control,control_ev,_=study.inspect(study.CONFIG);job=read_json(study.RUN/'job.json');r=read_json(study.RUN/'compare-result.json');probe=study.probe_evidence()
    if (job['status']!='complete' or alive(job) or r['config_sha256']!=sha256(study.CONFIG) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']+probe['GPU_seconds']>study.CEILING or r['scientific_teacher_tokens']!=study.TOTAL or r['protected_test_used']
            or r['checkpoints']['control']!=control or r['evaluations']['control']!=control_ev or set(r['transfer'])!={'parent2B','curriculum100M','relation100M'}):
        raise ValueError('Actual terminal bounded100M and unchanged reused control required')
    record=r['checkpoints'][study.ARM];study.check_reference(dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']))
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False);sampler=state['sampler']
    history=[json.loads(s) for s in (study.RUN/study.ARM/'training/metrics.jsonl').read_text().splitlines()]
    if (not finite_state(state) or state['study_binding']!=study.binding(c,study.CONFIG) or state['study_binding']!=record['binding']
            or state['supervised_tokens']!=parent['supervised_tokens']+study.TOTAL or sampler['source_teachers']!=study.GOALS
            or state['spec']['research_kind']!=study.KIND or state['spec']['outcome_weight']!=1 or state['spec']['lr']!=.0002
            or not equal_state(state['lineage']['actual_parent_sampler'],parent['sampler']) or not equal_state(state['lineage']['parent_scheduler'],parent['scheduler'])
            or state['lineage']['parent']!=c['parent'] or not state['lineage']['no_reheat']
            or any(not math.isclose(g['lr'],.0002,rel_tol=1e-10) for g in state['optimizer']['param_groups'])):raise ValueError('Finite inherited fullstate/quota/recipe differs')
    if (len(history)!=sampler['position'] or len(history)!=state['update']-parent['update']
            or [v['update'] for v in history]!=list(range(parent['update']+1,state['update']+1))
            or any(not math.isfinite(v['loss']) or not math.isfinite(v['gradient_norm']) or v['lr']!=.0002 for v in history)
            or history[-1]['token_digest']!=state['token_digest'] or history[-1]['focus_token_digest']!=state['focus_token_digest']
            or state['tokens']-parent['tokens']!=len(history)*32768 or state['tokens']-parent['tokens']!=sum(sampler['source_tokens'].values())
            or state['body_bytes']-parent['body_bytes']!=sum(sampler['source_body_bytes'].values()) or state['weighted_teacher_mass']!=study.TOTAL
            or state['focus_teacher_tokens']!=sum(sampler['source_focus_teachers'].values()) or record['additional_input_tokens']!=state['tokens']-parent['tokens']):raise ValueError('Actual completed history/state accounting differs')
    ordinary=read_json(Path(c['references']['ordinary_stream_audit']['path']))
    for key,target in (('source_teachers','teachers'),('source_eos','EOS'),('source_body_bytes','body_bytes')):
        if any(sampler[key][g]!=ordinary['actual_generated'][target][g] for g in ('web','story','ordinary_textbook')):raise ValueError('Actual original3 ordinary supervision differs')
    del state
    prepared=read_json(Path(c['references']['source_cases']['path']))
    if len(prepared['cases'])!=512 or len(prepared['families'])!=128:raise ValueError('All128 transfer families required')
    expected_CP=dict(parent2B=c['parent']['sha256'],curriculum100M=control['checkpoint_sha256'],relation100M=record['checkpoint_sha256'])
    for arm,transfer in r['transfer'].items():
        if (transfer['config_sha256']!=sha256(study.CONFIG) or transfer['checkpoint_sha256']!=expected_CP[arm]
                or transfer['cases_sha256']!=c['references']['source_cases']['sha256'] or not all(transfer['checks'].values())
                or transfer['evaluated_requests']!=512 or transfer['optimizer_updates'] or transfer['scientific_teacher_tokens'] or transfer['protected_test_used']):raise ValueError('Actual read-only complete transfer binding differs')
        rows=[]
        for start in range(0,512,16):
            saved=read_json(study.RUN/f'transfer/bridge/{arm}/{start:04d}.json')
            if any(saved[k]!=transfer[k] for k in ('config_sha256','checkpoint_sha256','cases_sha256')):raise ValueError('Raw transfer batch differs')
            study.ranking.validate_scores(saved['rows'],prepared['cases'][start:start+16]);rows.extend(saved['rows'])
        if transfer['summary']!=study.summarize_transfer(rows,prepared):raise ValueError('Raw transfer aggregation differs')
    retained=read_json(Path(c['references']['retention_cases']['path']))
    previous=read_json(study.control_study.RUN/'compare-result.json')
    if (set(r['retention'])!={'parent2B','curriculum100M','relation100M'}
            or r['retention']['parent2B']!=previous['transfer']['parent2B']
            or r['retention']['curriculum100M']!=previous['transfer']['curriculum100M']
            or c['references']['retention_cases']['sha256']!=previous['transfer']['curriculum100M']['cases_sha256']):
        raise ValueError('Original128 cached control retention differs')
    fresh=r['retention']['relation100M'];retained_rows=[]
    if (fresh['checkpoint_sha256']!=record['checkpoint_sha256'] or fresh['config_sha256']!=sha256(study.CONFIG)
            or fresh['cases_sha256']!=c['references']['retention_cases']['sha256'] or fresh['evaluated_requests']!=512
            or not all(fresh['checks'].values()) or fresh['scientific_teacher_tokens'] or fresh['optimizer_updates']):
        raise ValueError('Actual read-only new retention binding differs')
    for start in range(0,512,16):
        saved=read_json(study.RUN/f'transfer/retention/relation100M/{start:04d}.json')
        if any(saved[k]!=fresh[k] for k in ('config_sha256','checkpoint_sha256','cases_sha256')):raise ValueError('Raw retention binding differs')
        study.ranking.validate_scores(saved['rows'],retained['cases'][start:start+16]);retained_rows.extend(saved['rows'])
    if fresh['summary']!=study.summarize_transfer(retained_rows,retained):raise ValueError('Raw retention aggregation differs')
    new,ns=point();old_review=read_json(Path(c['references']['control_review']['path']));old=old_review['summaries']['curriculum']
    control_notes=Path(c['references']['control_notes']['path']);control_raw=Path(c['references']['control_generation']['path'])
    if old['notes_sha256']!=sha256(control_notes) or old['generation_sha256']!=sha256(control_raw) or read_json(control_raw)!=control_ev['generation']:raise ValueError('Historical natural content changed')
    old_scores=validate_notes(control_ev['generation']['outputs'],read_json(control_notes),sha256(control_raw))
    if [(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in control_ev['body']['rows']]!=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in r['evaluations'][study.ARM]['body']['rows']]:raise ValueError('Common targets differ')
    quality=quality_gates(control_ev,r['evaluations'][study.ARM],old_scores,ns,'content')
    absolute=dict(grammar_at_least56=new['grammar2']>=56,coherence_at_least27=new['coherent']>=27,appropriate_at_least27=new['appropriate']>=27,
        EOS_at_least37=new['rates']['eos']>=37,repetition_at_most18=new['rates']['repetition']<=18,no_empty_role_unicode=all(new['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    study.check_reference(base['reference']['web_screen']);web=read_json(Path(base['reference']['web_screen']['path']))
    if [(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in web['body']['rows']]!=[(v['doc_id'],v['body_tokens'],v['body_bytes']) for v in r['evaluations'][study.ARM]['body']['rows']]:raise ValueError('OriginalWeb common-byte targets differ')
    original=adoption_checks(web,r['evaluations'][study.ARM])
    atomic_json(study.RUN/'annotations.json',dict(control_notes=read_json(control_notes),control_reused=True,relation_notes=read_json(NOTES),independent_human_blind=False))
    report=dict(status='actual_relation100M_all80_bridge128_retention128_and_reused_curriculum100M_complete',created_at=now(),
        summaries=dict(control=old,relation=new),quality_comparison=quality,absolute_dev_screen=absolute,original_Web=original,
        eligible_for_final_Base_validation=all(absolute.values()) and all(original.values()) and quality['passed'],
        transfer_aggregates={a:t['summary']['aggregate'] for a,t in r['transfer'].items()},ordinary_stream_checks=ordinary['checks'],
        retention_aggregates={a:t['summary']['aggregate'] for a,t in r['retention'].items()},
        new_scientific_teacher_tokens=study.TOTAL,reused_control_teacher_tokens=study.TOTAL,verification_teacher_tokens=probe['verification_teacher_tokens'],
        GPU_seconds=r['GPU_seconds'],verification_GPU_seconds=probe['GPU_seconds'],result_sha256=sha256(study.RUN/'compare-result.json'),
        annotations_sha256=sha256(study.RUN/'annotations.json'),Base_adopted=False,Chat_adopted=False,protected_test_used=False,independent_human_blind=False,
        quality_criteria_unchanged=True,old_numerical7_preserved=True,requested_five_steps_complete=False,
        limitations='One learned seed, nonblind judgments, repeatedly inspected fixeddev; local generator probes are not independent natural-language quality. Only negation/comparison language replaced, with token lengths/lexical/EOS-density effects. Original128 are retention, not new grammar holdouts. OriginalWeb BPB reference0.971570 comes from a historical10B arm; final1percent guard is retained, not an equal-budget100M control.')
    atomic_json(study.RUN/'review.json',report);atomic_json(ROOT/'reports/phase6/condition_relation_comparison_review.json',report)
    print(json.dumps(report,ensure_ascii=False),flush=True)


def archive():
    c,*_=study.inspect(study.CONFIG);job=read_json(study.RUN/'job.json');review=read_json(study.RUN/'review.json')
    if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'):raise ValueError('Terminal raw-bound review required')
    paths={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.lock')}
    paths.update((study.CONFIG,study.PROBE_CONFIG,study.PROPOSAL,NOTES,ROOT/'reports/phase6/condition_relation_comparison_tests.xml'))
    target=ROOT/'reports/phase6/condition-relation-comparison-20261006_evidence.tar.gz'
    if target.exists():raise ValueError('Preserve immutable archive')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in sorted(paths)];temporary=target.with_suffix('.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for p in sorted(paths):stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(target);manifest=dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(r['bytes'] for r in entries),
        archive=dict(path=str(target),sha256=sha256(target),bytes=target.stat().st_size),checkpoint_tensors_included=False)
    atomic_json(ROOT/'reports/phase6/condition_relation_comparison_evidence_manifest.json',manifest);print({k:v for k,v in manifest.items() if k!='entries'})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--template',action='store_true');m.add_argument('--point',action='store_true');m.add_argument('--archive',action='store_true');a=p.parse_args()
    if a.template:point(True)
    elif a.point:point()
    elif a.archive:archive()
    else:audit()
