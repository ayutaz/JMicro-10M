"""Review all protected Base test outputs; never select recipes using test."""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from run_eos_short_pilot import rate
from review_eos_5b_finish import validate_rows
from review_final_base_dev import row_key,validate_content
import run_final_base_dev as dev
from run_final_base_test import preflight,SELECTION


def validate_generation(generation,cases,tok,expected_cases):
    rows=generation['outputs']
    assert generation['split']=='test' and generation['max_new_tokens']==64 and generation['sampling_evaluated']
    assert generation['temperature']==.8 and generation['top_p']==.9
    assert len(cases)==expected_cases and len(rows)==5*expected_cases
    expected={(case['id'],mode,suppressed,seed) for case in cases.values()
        for mode,suppressed,seed in (('greedy',True,42),('greedy',False,42),
                                    ('sampling',True,42),('sampling',True,43),('sampling',True,44))}
    assert len({row_key(r) for r in rows})==len(rows)
    assert {(r['id'],r['decoding'],r['suppressed'],r['seed']) for r in rows}==expected
    assert all(r['split']=='test' and r['prefix']==cases[r['id']]['prefix']
        and r['category']==cases[r['id']]['category'] for r in rows)
    validate_rows(rows,tok)
    return [r for r in rows if r['decoding']=='greedy' and r['suppressed']]


def quality_checks(rows,scores,rules,all_rows):
    count=len(rows);assert count==rules['primary_cases']>0
    ns=[scores[row_key(r)] for r in rows];rates=rate(rows);raw=rate(all_rows)
    return dict(grammar_at_least70pct=sum(n[1]==2 for n in ns)>=math.ceil(count*rules['grammar_2_rate']),
        coherence_at_least_dev_rate=sum(n[3]==2 for n in ns)>=math.ceil(count*rules['coherence_2_rate']),
        appropriate_at_least_dev_rate=sum(n[4] for n in ns)>=math.ceil(count*rules['appropriate_completion_rate']),
        stop_success_at_least_protocol95pct=rates['eos']>=math.ceil(count*rules['stop_success_min']),
        repetition_within_dev_rate=rates['repetition']<=math.floor(count*rules['repetition_max_rate']),
        empty_within_protocol=rates['empty']<=math.floor(count*rules['empty_response_max']),
        role_within_protocol=rates['role_leak']<=math.floor(count*rules['role_leak_max']),
        Unicode_within_protocol=rates['unicode_failure']<=rules['unicode_failure_max'],
        all100_raw_failures_zero=all(raw[k]==0 for k in ('empty','role_leak','unicode_failure')))


def review(path,notes_path,template=False):
    config=read_json(path);run=ROOT/config['output'];job=read_json(run/'job.json')
    if job['status']!='complete' or alive(job):
        raise ValueError('Protected test must actually finish before review')
    config,screen=preflight(path);result=read_json(run/'result.json')
    assert job['config_sha256']==result['binding']['config_sha256']==sha256(path)
    assert result['binding']['checkpoint_sha256']==config['checkpoint']['sha256']
    assert result['binding']['selection_sha256']==job['selection_sha256']==sha256(SELECTION)
    assert result['GPU_seconds']==job['GPU_elapsed_seconds']<=config['GPU_budget_seconds']
    assert result['protected_test_used'] and result['weights_unchanged'] and result['evaluation_RNG_isolated']
    assert result['additional_training_tokens']==0 and not result['Base_adopted']
    body_path=run/'test-body.json';raw_path=run/'test-generation.json'
    assert result['body_sha256']==sha256(body_path) and result['generation_sha256']==sha256(raw_path)
    body_doc=read_json(body_path);generated_doc=read_json(raw_path)
    assert body_doc['binding']==generated_doc['binding']==result['binding']
    body=body_doc['body'];generation=generated_doc['generation']
    assert body['split']=='test' and body['limit_documents'] is None
    assert body['documents']==len(body['rows']) and len({r['doc_id'] for r in body['rows']})==body['documents']
    assert all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll'])
        and math.isfinite(r['eos_nll']) for r in body['rows'])
    manifest=read_json(Path(config['shards'])/'manifest.json')['splits']['test']
    assert body['documents']==manifest['documents']
    assert body['body_bytes']==sum(r['body_bytes'] for r in body['rows'])>0
    assert body['body_tokens']==sum(r['body_tokens'] for r in body['rows'])
    assert math.isclose(body['body_nll'],sum(r['body_nll'] for r in body['rows']),rel_tol=1e-12)
    assert math.isclose(body['bpb'],body['body_nll']/body['body_bytes']/math.log(2),rel_tol=1e-12)
    cases={r['id']:r for r in (json.loads(s) for s in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='test'}
    assert generation['suite_sha256']==config['suite_sha256']
    primary=validate_generation(generation,cases,Tokenizer(config['tokenizer']['path']),config['rules']['primary_cases'])
    if template:
        assert not notes_path.exists(),'Preserve existing notes'
        atomic_json(notes_path,dict(generation_sha256=sha256(raw_path),independent_human_blind=False,
            reviewer='Codex nonblind; all100 individually read',notes=[[row_key(r),None,None,None,None,''] for r in generation['outputs']]))
        return
    document=read_json(notes_path);assert document['generation_sha256']==sha256(raw_path)
    assert document['independent_human_blind'] is False and document['reviewer'].strip()
    scores=validate_content(generation['outputs'],document['notes'])
    checks=quality_checks(primary,scores,config['rules'],generation['outputs']);passed=all(checks.values())
    report=dict(status='fixed_recipe_final_test_all100_content_evidence_complete',checks=checks,
        final_test_passed=passed,checkpoint_sha256=config['checkpoint']['sha256'],
        config_sha256=sha256(path),result_sha256=sha256(run/'result.json'),notes_sha256=sha256(notes_path),
        notes_path=str(notes_path),body_BPB=body['bpb'],primary_rates=rate(primary),all100_rates=rate(generation['outputs']),
        protected_test_used=True,independent_training_seed_confirmed=True,
        independent_human_blind=False,quality_criteria_unchanged=True,Base_adopted=passed,
        test_sample_size=len(primary),test_uncertainty='20 fixed families; descriptive rates, not broad quality/causality proof',
        Chat_adopted=False,requested_five_steps_complete=False,created_at=now())
    atomic_json(run/'review.json',report)
    if passed:
        primary_config=read_json(Path(config['primary_dev_config']['path']))
        _,_,_,annotations=dev.source_evidence(Path(primary_config['training_config']['path']),
            Path(primary_config['source_run']),primary_config['point'])
        evaluation_path=run/'adopted-Base-dev-screen.json';annotation_path=run/'adopted-Base-dev-annotations.json'
        atomic_json(evaluation_path,screen);atomic_json(annotation_path,annotations)
        acceptance=dict(kind='final_Base_after_independent_seed_full_dev_and_protected_test',
            Base_adopted=True,checkpoint_sha256=config['checkpoint']['sha256'],
            evaluation_sha256=sha256(evaluation_path),annotations_sha256=sha256(annotation_path),
            final_test_config=dev.ref(path),final_test_review=dev.ref(run/'review.json'),
            final_test_result=dev.ref(run/'result.json'),confirmations=config['confirmations'],
            selected_training_seed=42,independent_training_seed_confirmed=True,
            protected_test_used=True,quality_criteria_unchanged=True,
            independent_human_blind=False,Chat_adopted=False,requested_five_steps_complete=False,created_at=now())
        atomic_json(run/'Base-acceptance.json',acceptance)
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True);p.add_argument('--notes',type=Path,required=True)
    p.add_argument('--template',action='store_true');args=p.parse_args()
    path=args.config.resolve();notes=args.notes.resolve()
    assert path.is_relative_to(ROOT/'configs/phase6') and notes.is_relative_to(ROOT/'reports/phase6')
    review(path,notes,args.template)
