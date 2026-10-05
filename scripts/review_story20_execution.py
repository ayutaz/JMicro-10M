"""Inspect actual plan52 evidence and conditional full results without GPU execution."""
import argparse
import json
import math
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import repetition_metrics
from phase6_performance import alive
import run_story20_low_lr as run
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from run_eos_complete_100m import adoption_checks
from review_eos_5b_finish import validate_rows


def full_review():
    config=run.load_config();output=run.RUN/'full';checks={}
    def require(name,value):
        checks[name]=bool(value);assert value,name
    job=read_json(output/'full-job.json');result=read_json(output/'result.json');primary=read_json(run.RUN/'review.json')
    require('actual_full_job_complete_exited',job['status']=='complete' and not alive(job))
    require('full_config_screen_review_binding',result['binding']==job['binding'] and result['binding']['plan_sha256']==sha256(run.CONFIG)
            and result['binding']['review_sha256']==sha256(run.RUN/'review.json'))
    require('screen_was_eligible',primary['status']=='passed' and primary['selection']['eligible_for_full'])
    require('full_budget_zero_learning_and_honest_scope',result['GPU_seconds']<=job['gpu_elapsed_seconds']<=config['full_gpu_budget_seconds']
            and result['additional_training_tokens']==0 and not result['protected_test_used'] and not result['quality_targets_achieved'])
    parent_body=read_json(Path(config['reference']['parent_body']['path']))['body']
    parent_generation=read_json(Path(config['reference']['parent_generation']['path']))['generation']
    trained={'web':read_json(Path(config['reference']['control_training']['path']))['arms']['web'],
             'coherent20':read_json(run.RUN/'result.json')['trained']}
    tok=Tokenizer(ROOT/config['tokenizer']);full={};long={};sources={}
    counts={};selected=[]
    for line in (ROOT/'eval/base.jsonl').read_text().splitlines():
        case=json.loads(line)
        if case['split']=='dev' and counts.get(case['category'],0)<2:
            counts[case['category']]=counts.get(case['category'],0)+1;selected.append(case['id'])
    for arm,detail in trained.items():
        path=output/(arm+'-full.json');record=read_json(path);full[arm]=record
        body,generation=record['body'],record['generation']
        expected_binding={**result['binding'],'arm':arm,'checkpoint_sha256':detail['checkpoint_sha256']}
        require(arm+'_actual_checkpoint_and_full_binding',record['binding']==expected_binding and
                record['checkpoint_sha256']==detail['checkpoint_sha256']==sha256(Path(detail['checkpoint'])))
        require(arm+'_full_common89416_complete_coverage',record['full'] and record['evaluation_RNG_isolated'] and
                len(body['rows'])==body['documents']==89416 and body['body_bytes']==164344743 and body['body_tokens']==42003934 and
                all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows']))
        require(arm+'_actual_BPB_from_finite_NLL',all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and
                math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        require_alignment(body,generation,parent_body,parent_generation)
        require(arm+'_parent_aligned_documents_and400_requests',True)
        validate_rows(generation['outputs'],tok)
        require(arm+'_actual_raw400_ID_flags',len(generation['outputs'])==400)
        original=read_json(Path(config['reference']['screen']['path'])) if arm=='web' else read_json(run.RUN/'coherent20/evaluation/result.json')
        fixed={r['id']:r for r in generation['outputs'] if r['decoding']=='greedy' and r['suppressed']}
        require(arm+'_fixed80_match_primary_IDs',all(fixed[r['id']]['generated_ids']==r['generated_ids'] for r in original['generation']['outputs']))
        long_path=output/arm/'long-generation.json';long[arm]=read_json(long_path);record_long=long[arm]
        require(arm+'_long_binding_requests_and_complete',record_long['binding']==json.dumps(expected_binding,sort_keys=True) and record_long['complete'] and
                [(r['id'],r['max_new_tokens']) for r in record_long['rows']]==[(i,m) for m in (128,512) for i in selected])
        for row in record_long['rows']:
            ids=row['generated_ids'];assert 0<len(ids)<=row['max_new_tokens'] and 3 not in ids[:-1]
            raw=tok.decode_bytes(ids)
            try:text=raw.decode('utf-8');valid=True
            except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
            assert row['text']==text and row['valid_utf8']==valid and repetition_metrics(row)==row['metrics']
            assert row['stop_reason']==('stop_id' if ids[-1]==3 else 'max_new_tokens')
        require(arm+'_long_raw_text_stops_UTF8_and_metrics',True)
        for maximum in (128,512):
            rows=[r for r in record_long['rows'] if r['max_new_tokens']==maximum];summary=record_long['summary'][str(maximum)]
            require(arm+'_long'+str(maximum)+'_summary_from_rows',summary['count']==summary['expected']==len(rows)==20 and
                    summary['natural_eos']==sum(r['metrics']['natural_eos'] for r in rows) and
                    summary['same_sentence_repeat']==sum(r['metrics']['same_sentence_reappears'] for r in rows) and
                    summary['raw_utf8_failure']==sum(r['metrics']['raw_utf8_failure'] for r in rows))
        require(arm+'_long_saved_summary_binding',result['long_generation'][arm]['complete'] and result['long_generation'][arm]['conditions']==record_long['summary'])
        sources[str(path)]=sha256(path);sources[str(long_path)]=sha256(long_path)
    require_alignment(full['web']['body'],full['web']['generation'],full['coherent20']['body'],full['coherent20']['generation'])
    require('same_full_document_and_generation_requests_between_arms',True)
    summaries={a:summarize(a,d['tokens'],full[a]['body'],full[a]['generation']) for a,d in trained.items()}
    parent=summarize('parent10B',10000007168,parent_body,parent_generation)
    actual={'mixture':adoption_checks(full['web'],full['coherent20']),'parent_growth':growth_checks(summaries['coherent20'],parent)}
    require('actual_summaries_original_gates_recomputed',result['summary']==summaries and result['parent']==parent and result['checks']==actual and
            result['candidate_passes_all_full_conditions']==(all(actual['mixture'].values()) and all(actual['parent_growth'].values())))
    review=dict(status='passed',checked_at=now(),checks=checks,summary=summaries,parent=parent,adoption_checks=actual,
                candidate_passes_all_full_conditions=result['candidate_passes_all_full_conditions'],long_generation=result['long_generation'],
                additional_training_tokens=0,protected_test_used=False,quality_targets_achieved=False,independent_human_blind='not performed',
                GPU_seconds=result['GPU_seconds'],sources=sources,result_sha256=sha256(output/'result.json'),reviewer_sha256=sha256(Path(__file__)))
    write_json(output/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k not in ('sources','long_generation')},ensure_ascii=False),flush=True)


def completion():
    config=run.load_config();screen=read_json(run.RUN/'result.json');review=read_json(run.RUN/'review.json');job=read_json(run.RUN/'screen-job.json')
    checks={};sources={}
    def require(name,value):
        checks[name]=bool(value);assert value,name
    require('actual_scientific_job_complete_exited',job['status']=='complete' and not alive(job))
    require('source_config_screen_review_bound',review['status']=='passed' and review['config_sha256']==sha256(run.CONFIG) and
            review['screen_sha256']==sha256(run.RUN/'result.json') and screen['binding']==job['binding'])
    suites=list(ET.parse(run.RUN/'tests.xml').getroot().iter('testsuite'))
    require('20_relevant_tests_passed',sum(int(s.attrib['tests']) for s in suites)==20 and
            all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped')))
    require('actual_CUDA25_save_resume_checks',screen['resume_gate']['passed'] and len(screen['resume_gate']['checks'])==25 and
            all(screen['resume_gate']['checks'].values()) and screen['verification_tokens']==262144)
    require('frozen_screen_GPU_budget',screen['GPU_seconds']<=job['gpu_elapsed_seconds']<=config['screen_gpu_budget_seconds'])
    trained=screen['trained'];evaluation=read_json(run.RUN/'coherent20/evaluation/result.json')
    control=read_json(Path(config['reference']['screen']['path']));body=evaluation['body']
    require('actual_checkpoint_matches_evaluation',sha256(Path(trained['checkpoint']))==trained['checkpoint_sha256']==evaluation['checkpoint_sha256'])
    require('common256_complete_body_coverage',body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343 and
            [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in body['rows']]==[(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in control['body']['rows']] and
            all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows']))
    require('screen_BPB_from_finite_document_NLL',all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and
            math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
    history=[json.loads(line) for line in (run.RUN/'coherent20/metrics.jsonl').read_text().splitlines()]
    require('actual100M_finite3052_updates_and_final101B',trained['additional_input_tokens']==screen['scientific_tokens']==100007936 and
            trained['tokens']==10100015104 and trained['update']==308228 and len(history)==3052 and
            [r['update'] for r in history]==list(range(305177,308229)) and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
    require('actual_lowLR_schedule',history[0]['lr']==.0001 and math.isclose(history[-1]['lr'],.00001,rel_tol=.001))
    require('actual20percent_source_counts_no_wrap',trained['source_tokens']==dict(web=80019456,short=19988480) and trained['sampler']['short']['epoch']==0)
    normal_config=read_json(ROOT/'configs/phase6/complete_text_10b_100m.json')
    normal_history=ROOT/'reports/phase6/complete-text-10b-100m-20261004/coherent20/metrics.jsonl'
    normal_last=json.loads(normal_history.read_text().splitlines()[-1])
    require('same20percent_input_digest_as_normalLR_reference',normal_config['parent']==config['parent'] and
            normal_config['arms']['coherent20']['manifest_sha256']==config['pool']['manifest_sha256'] and
            normal_last['token_digest']==history[-1]['token_digest'] and normal_last['tokens_seen']==history[-1]['tokens_seen'])
    sources[str(normal_history)]=sha256(normal_history)
    require('saved_matched_Web_control_explicitly_reused',screen['control_reused']==config['reference'] and
            read_json(Path(config['reference']['control_config']['path']))['peak_lr']==.0001)
    tok=Tokenizer(ROOT/config['tokenizer']);validate_rows(evaluation['generation']['outputs'],tok)
    actual={r['id']:r for r in evaluation['generation']['outputs']}
    cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    require('exact80_protected_dev_ID_prefixes',set(actual)==set(cases) and all(r['prefix']==cases[k]['prefix'] for k,r in actual.items()))
    require('all80_content_scores_bound_to_actual_raw',len(review['rows'])==80 and all(r['generated_ids']==actual[r['id']]['generated_ids'] and
            r['text']==actual[r['id']]['text'] and r['rationale'] for r in review['rows']))
    reference_scores={r['id']:r for r in read_json(Path(config['reference']['content']['path']))['scored_outputs']['web']}
    require('original_selection_recomputed',run.selection.selection_checks(control,evaluation,reference_scores,{r['id']:r for r in review['rows']})==review['selection'])
    require('complete_Japanese_diagnostics_and_RNG_isolation',evaluation['evaluation_RNG_isolated'] and
            all(evaluation['diagnostics'][k]['complete'] and evaluation['diagnostics'][k]['count']==evaluation['diagnostics'][k]['expected']==n
                for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()) and evaluation['diagnostics']['semantic_both_contexts']['total']==96)
    require('protected_test_unused_honest_quality',not screen['protected_test_used'] and not review['protected_test_used'] and
            not review['quality_targets_achieved'] and review['independent_human_blind']=='not performed')
    full=review['selection']['eligible_for_full'];GPU=screen['GPU_seconds']
    if full:
        evidence=read_json(run.RUN/'full/review.json');record=read_json(run.RUN/'full/result.json');full_job=read_json(run.RUN/'full/full-job.json')
        require('eligible_full_actual_review_bound',evidence['status']=='passed' and all(evidence['checks'].values()) and evidence['result_sha256']==sha256(run.RUN/'full/result.json'))
        require('actual_full_job_complete_exited',full_job['status']=='complete' and not alive(full_job))
        require('full_failure_branch_finished',not record['candidate_passes_all_full_conditions'],'Passing full gates require actual conditional500M before completion')
        GPU+=record['GPU_seconds'];sources[str(run.RUN/'full/review.json')]=sha256(run.RUN/'full/review.json')
    else:require('failed_screen_correctly_skips_full',not (run.RUN/'full/full-job.json').exists())
    require('no500M_without_full_entry_conditions',not (ROOT/'reports/phase6/story20-low-lr-10b-500m-20261005/job.json').exists())
    server=read_json(ROOT/'reports/local/webui/server.json')
    require('actual_original_UI_identity_live',server['status']=='running' and alive(server))
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:model=json.load(response)
    require('HTTP_original10B_UI_restored',model['checkpoint_sha256']==config['parent']['sha256'] and model['training_tokens']==10000007168 and not model['busy'])
    for path in (run.CONFIG,run.RUN/'result.json',run.RUN/'review.json',run.RUN/'tests.xml',
                 ROOT/'docs/52_story20_low_lr_execution.md',ROOT/'docs/53_story20_low_lr_judgment.md',ROOT/'docs/autonomous_status.md'):
        require('artifact_exists_'+str(path.relative_to(ROOT)),path.is_file());sources[str(path)]=sha256(path)
    result=dict(status='passed',scope='plan52 stages1–4 actual conditional failure branch, judgment/proposal, original UI restored',checked_at=now(),
                checks=checks,scientific_tokens=100007936,verification_tokens=262144,GPU_seconds=GPU,conditional_full_performed=full,
                pool_expansion_performed=False,conditional500M_performed=False,original_acceptance_gates_unchanged=True,
                checkpoint=trained['checkpoint'],checkpoint_sha256=trained['checkpoint_sha256'],original_UI=model,
                normalLR20_and_lowerLR20_same_input_digest=history[-1]['token_digest'],
                UI_identity={k:server[k] for k in ('pid','boot_id','start_ticks','ready_at')},sources=sources,reviewer_sha256=sha256(Path(__file__)),
                quality_targets_achieved=False,protected_test_used=False,independent_human_blind='not performed',
                remaining_delivery='Verify final local commit, clean worktree and evidence hashes before marking goal complete')
    write_json(ROOT/'reports/phase6/story20_execution_completion.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('sources','original_UI')},ensure_ascii=False),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('full','complete'),required=True);args=parser.parse_args()
    if args.mode=='full':full_review()
    else:completion()
