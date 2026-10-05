"""Audit the actual coverage comparison; research completion does not adopt Base."""
import argparse
import json
import math
from pathlib import Path
import sys
import tarfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from review_textbook_improved_base import audit_extension
from review_amount_learning_comparison import audit_checkpoint
from review_textbook_quantity_comparison import validate_notes
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import equal_state,rate
from run_textbook_coverage_v2 import RUN,CONFIG,PROBE_CONFIG,SPEED_RUN,BASELINE,CANDIDATE,TARGET,DECAY,CEILING,inspect,probe_evidence

NOTES=ROOT/'reports/phase6/textbook_coverage_2b_notes.json'


def point(template=False):
    c,base,_,_=inspect(CONFIG);progress=read_json(RUN/'progress-result.json')
    d=progress['decay'][CANDIDATE];ev=progress['evaluations'][CANDIDATE];rows=ev['generation']['outputs']
    assert ev['binding']==d['binding'] and d['binding']['config_sha256']==sha256(CONFIG)
    assert ev['checkpoint_sha256']==d['checkpoint_sha256'] and ev['evaluation_RNG_isolated'] and not ev['protected_test_used']
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    assert len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows)
    assert ev['greedy_rates']==rate(rows)
    assert all(ev['diagnostics'][k]['complete'] and ev['diagnostics'][k]['count']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items())
    body=ev['body'];assert body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343
    assert all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) for r in body['rows'])
    assert math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/472055,rel_tol=1e-12)
    raw=RUN/'evaluation'/CANDIDATE/'evaluation/generation.json'
    if template:
        assert not NOTES.exists(),'Preserve existing content notes'
        write_json(NOTES,dict(reviewer='Codex nonblind; all80 individually read',independent_human_blind=False,
            generation_sha256=sha256(raw),notes=[[r['id'],None,None,None,None,''] for r in rows]));return
    notes=read_json(NOTES);scores=validate_notes(rows,notes,sha256(raw))
    summary=dict(prepared_tokens=c['prepared_tokens'],stable_teachers=TARGET,decay_teachers=DECAY,BPB=body['bpb'],rates=ev['greedy_rates'],
        grammar2=sum(s['grammar']==2 for s in scores.values()),relevance2=sum(s['relevance']==2 for s in scores.values()),
        coherent=sum(s['coherence']==2 for s in scores.values()),appropriate=sum(s['completion'] for s in scores.values()),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        generation_sha256=sha256(raw),notes_sha256=sha256(NOTES),Base_adopted=False,independent_human_blind=False)
    write_json(RUN/'content-review.json',summary);write_json(ROOT/'reports/phase6/textbook_coverage_2b_content_review.json',summary)
    return summary,scores


def audit():
    c,base,parent,source=inspect(CONFIG);job=read_json(RUN/'job.json');result=read_json(RUN/'compare-result.json');probe=probe_evidence()
    assert job['status']=='complete' and not alive(job) and job['config_sha256']==result['config_sha256']==sha256(CONFIG)
    assert result['GPU_seconds']==job['GPU_elapsed_seconds']<=c['GPU_budget_seconds']
    assert job['GPU_elapsed_seconds']+probe['GPU_seconds']<=CEILING
    assert result['scientific_stable_teachers']==1000000000 and result['scientific_decay_teachers']==DECAY
    assert result['scientific_job_includes_actual2B_decay_verification'] and not result['Base_adopted'] and not result['protected_test_used']
    for section in ('stable','decay','evaluations'):
        assert set(result[section])=={BASELINE,CANDIDATE} and equal_state(result[section][BASELINE],source[section][BASELINE])
    history=[json.loads(s) for s in (RUN/'stable/metrics.jsonl').read_text().splitlines()]
    stable=audit_extension(result['stable'][CANDIDATE],history,parent,c,base)
    dh=[json.loads(s) for s in (RUN/'decay/metrics.jsonl').read_text().splitlines()]
    decay=audit_checkpoint(result['decay'][CANDIDATE],dh,base,'decay',DECAY)
    assert result['decay'][CANDIDATE]['binding']['parent']['sha256']==result['stable'][CANDIDATE]['checkpoint_sha256']
    assert equal_state(decay['lineage']['actual_parent_sampler'],stable['sampler'])
    assert result['additional_valid_input_tokens']==stable['tokens']-parent['tokens']+result['decay'][CANDIDATE]['additional_input_tokens']
    assert result['additional_physical_input_tokens']==sum(stable['sampler']['source_physical_tokens'].values())-sum(parent['sampler']['source_physical_tokens'].values())+result['decay'][CANDIDATE]['physical_input_tokens']
    gate=read_json(RUN/'resume-gate/decay/result.json')
    assert gate==result['actual2B_decay_gate'] and gate['passed'] and all(gate['checks'].values()) and gate['config_sha256']==sha256(CONFIG)
    assert gate['GPU_optimizer_updates']==8 and result['verification_teacher_tokens']==probe['verification_teacher_tokens']+gate['verification_teacher_tokens']
    summary,scores=point();ev=result['evaluations'][CANDIDATE]
    baseline_scores=validate_notes(source['evaluations'][BASELINE]['generation']['outputs'],read_json(Path(c['control_notes']['path'])),c['control_generation']['sha256'])
    bodies=[source['evaluations'][BASELINE]['body'],ev['body']]
    assert [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in bodies[0]['rows']]==[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in bodies[1]['rows']]
    relative=quality_gates(source['evaluations'][BASELINE],ev,baseline_scores,scores,'amount')
    checks=dict(grammar_at_least56=summary['grammar2']>=56,coherence_at_least27=summary['coherent']>=27,
        appropriate_at_least27=summary['appropriate']>=27,EOS_at_least37=summary['rates']['eos']>=37,
        repetition_at_most18=summary['rates']['repetition']<=18,
        no_empty_role_unicode=all(summary['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(read_json(Path(base['reference']['web_screen']['path'])),ev)
    annotations=dict(reviewer='Codex nonblind',independent_human_blind=False,arms={
        BASELINE:dict(notes=read_json(Path(c['control_notes']['path']))['notes'],notes_sha256=c['control_notes']['sha256'],generation_sha256=c['control_generation']['sha256']),
        CANDIDATE:dict(notes=read_json(NOTES)['notes'],notes_sha256=sha256(NOTES),generation_sha256=summary['generation_sha256'])})
    write_json(RUN/'annotations.json',annotations)
    report=dict(status='coverage_learning_and_all80_evidence_complete',point=CANDIDATE,summary=summary,
        quality_comparison=relative,absolute_dev_screen=checks,original_Web=original,
        eligible_for_final_Base_validation=all(checks.values()) and all(original.values()),
        scientific_stable_teachers=1000000000,scientific_decay_teachers=DECAY,verification_teacher_tokens=result['verification_teacher_tokens'],
        GPU_seconds=job['GPU_elapsed_seconds'],verification_GPU_seconds=probe['GPU_seconds'],
        actual_parent_cursor=parent['sampler']['short'],final_stable_cursor=stable['sampler']['short'],final_decay_cursor=decay['sampler']['short'],
        result_sha256=sha256(RUN/'compare-result.json'),annotations_sha256=sha256(RUN/'annotations.json'),notes_sha256=sha256(NOTES),
        quality_criteria_unchanged=True,historical_quality_extension_refusal_preserved=True,
        Base_adopted=False,Chat_adopted=False,protected_test_used=False,independent_human_blind=False,
        final_seed_full_evaluation_test_pending=True,requested_five_steps_complete=False,old_numerical7_preserved=True,created_at=now())
    write_json(RUN/'review.json',report);write_json(ROOT/'reports/phase6/textbook_coverage_2b_review.json',report)
    write_json(ROOT/'reports/phase6/textbook_coverage_2b_annotations.json',annotations)
    print(json.dumps(report,ensure_ascii=False),flush=True)


def archive():
    c,_,_,_=inspect(CONFIG);job=read_json(RUN/'job.json');review=read_json(RUN/'review.json')
    assert job['status']=='complete' and not alive(job) and review['status']=='coverage_learning_and_all80_evidence_complete'
    assert review['result_sha256']==sha256(RUN/'compare-result.json') and review['annotations_sha256']==sha256(RUN/'annotations.json')
    assert review['notes_sha256']==sha256(NOTES)
    paths={p for p in RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1','.xml')}
    paths.update(p for p in SPEED_RUN.rglob('*') if p.is_file() and p.suffix in ('.json','.jsonl','.py','.ps1'))
    paths.update((CONFIG,PROBE_CONFIG,NOTES,ROOT/'reports/phase6/textbook_coverage_tests.xml',ROOT/'reports/phase6/textbook_coverage_v2_tests.xml'))
    paths.update(Path(c[k]['path']) for k in ('original_config','source_result','source_review','source_annotations','control_notes','control_generation','prior_UL_review'))
    paths=sorted(paths);assert all(p.is_file() and p.resolve().is_relative_to(ROOT) for p in paths)
    output=ROOT/'reports/phase6/textbook-coverage-2b-20261006_evidence.tar.gz'
    assert not output.exists(),'Completed archive is immutable'
    manifest=ROOT/'reports/phase6/textbook_coverage_2b_evidence_manifest.json'
    entries=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha256(p),bytes=p.stat().st_size) for p in paths]
    write_json(manifest,dict(entries=entries,text_files=len(entries),uncompressed_bytes=sum(e['bytes'] for e in entries),
        checkpoint_tensors_included=False,native_checkpoints_retained=True,created_at=now()))
    temporary=output.with_suffix(output.suffix+'.tmp')
    with tarfile.open(temporary,'w:gz',compresslevel=1) as stream:
        for path in (*paths,manifest):stream.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(output);print(json.dumps(dict(path=str(output),sha256=sha256(output),bytes=output.stat().st_size,text_files=len(entries))))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--template',action='store_true');g.add_argument('--archive',action='store_true')
    args=p.parse_args()
    if args.template:point(True)
    elif args.archive:archive()
    else:audit()
