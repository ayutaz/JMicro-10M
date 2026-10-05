"""CPU review of the new candidate and saved controls; do not rerun old GPU work."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import clustered_ci,repetition_metrics
from phase6_performance import alive,finite_state
from review_eos_5b_finish import validate_rows
from run_story10_comparison import selection_checks
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import routes,rate
from review_story20_budget import expected_cursor
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
import run_complete_document_500m as study


def primary_review():
    config=study.load_config();result=read_json(study.RUN/'result.json');job=read_json(study.RUN/'screen-job.json')
    annotations=read_json(study.RUN/'annotations.json');tok=Tokenizer(ROOT/config['tokenizer']);checks={}
    def require(name,value):checks[name]=bool(value);assert value,name
    require('actual_job_complete_exited_within_budget',job['status']=='complete' and not alive(job) and result['binding']==job['binding'] and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=1800)
    require('actual_new_data_CUDA_exact_save_resume',result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()) and result['verification_tokens']==262144)
    require('single500M_scientific_budget',result['scientific_tokens']==500006912 and not result['protected_test_used'])
    directory=study.RUN/'whole20';evaluation=read_json(directory/'evaluation/result.json');rows=evaluation['generation']['outputs']
    validate_rows(rows,tok)
    cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    require('fixed80_exact_IDs_and_prefixes',len(rows)==80 and {r['id'] for r in rows}==set(cases) and all(r['prefix']==cases[r['id']]['prefix'] for r in rows))
    require('annotations_bound_to_actual_raw_generation',annotations['generation_sha256']==sha256(directory/'evaluation/generation.json'))
    entries=annotations['scores'];scores={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in entries}
    require('all80_individual_content_notes',len(entries)==len(scores)==80 and set(scores)==set(cases) and all(r['rationale'] and all(r[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and r['completion'] in (0,1) for r in scores.values()))
    require('appropriate_completion_only_actual_EOS',all(not scores[r['id']]['completion'] or r['stop_reason']=='stop_id' for r in rows))
    detail=result['trained'];state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
    require('actual_checkpoint_finite_full_state_hash',finite_state(state) and detail['checkpoint_sha256']==sha256(Path(detail['checkpoint']))==evaluation['checkpoint_sha256'])
    history=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
    require('all15259_actual_contiguous_finite_updates',len(history)==15259 and [r['update'] for r in history]==list(range(305177,320436)) and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
    require('checkpoint_all_resume_states_and_counters',all(k in state for k in ('optimizer','scheduler','rng','sampler','body_bytes','supervised_tokens')) and state['update']==320435 and state['tokens']==10500014080 and state['pilot_binding']==detail['binding']==evaluation['binding']==job['binding'] and state['token_digest']==history[-1]['token_digest'])
    require('fixed_saved_control_schedule_and_LR',state['spec']['lr']==.0001 and state['spec']['pilot_schedule']==dict(parent_update=305176,stable_updates=14500,decay_updates=759))
    require('source_tokens_and_routes_actual',state['sampler']['source_tokens']==dict(web=400031744,short=99975168) and tuple(state['sampler']['routes'])==tuple(routes(15259,3051)))
    cursor=state['sampler']['short'];pool=read_json(Path(config['pool_ready']['path']))
    require('actual_short_exposure_and_cursor_disclosed',tuple(cursor[k] for k in ('epoch','position'))==expected_cursor(99975168,1024,cursor['blocks']) and math.isclose(pool['short_exposure_ratio'],99975168/pool['totals']['tokens']))
    body=evaluation['body']
    require('common256_body_bytes_tokens_actual_NLL',body['documents']==len(body['rows'])==256 and body['body_bytes']==472055 and body['body_tokens']==122343 and all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
    require('raw_rates_recomputed',evaluation['greedy_rates']==rate(rows))
    require('all_Japanese_diagnostics_complete_and_RNG_isolated',evaluation['evaluation_RNG_isolated'] and all(evaluation['diagnostics'][k]['complete'] and evaluation['diagnostics'][k]['count']==evaluation['diagnostics'][k]['expected']==n for k,n in {'semantics':192,'jblimp':331,'jcqa':1119}.items()))
    prior_review=read_json(Path(config['reference']['prior_review']['path']))
    prior_scores={a:{r['id']:r for r in prior_review['scored_outputs'][a]['result']} for a in ('web','coherent20')}
    controls={a:read_json(Path(config['reference'][a+'_screen']['path'])) for a in ('web','story')}
    require('matched_saved_controls_same_schedule_parent_budget',all(r['tokens']==10500014080 and r['additional_input_tokens']==500006912 for r in read_json(Path(config['reference']['prior_training']['path']))['arms'].values()))
    for control in controls.values():
        require('controls_fixed80_alignment_'+control['checkpoint_sha256'][:8],[(r['id'],r['prefix']) for r in control['generation']['outputs']]==[(r['id'],r['prefix']) for r in rows] and [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in control['body']['rows']]==[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in body['rows']])
    original=selection_checks(controls['web'],evaluation,prior_scores['web'],scores)
    differences=[dict(id=k,family=k,difference=int(scores[k]['coherence']==2)-int(prior_scores['coherent20'][k]['coherence']==2)) for k in scores]
    paired=clustered_ci(differences,key='difference')
    # Same prespecified paired bootstrap as the previous selection; explicit new comparison.
    array=np.array([d['difference'] for d in sorted(differences,key=lambda r:r['id'])]);rng=np.random.default_rng(42)
    interval=np.quantile(array[rng.integers(0,80,size=(2000,80))].mean(axis=1),[.025,.975]).tolist()
    summary={k+'_score2':sum(r[k]==2 for r in scores.values()) for k in ('grammar','relevance','coherence')}
    summary.update(count=80,appropriate_EOS=sum(r['completion'] for r in scores.values()))
    improvement=dict(coherence_gain_over_story_at_least8=int(array.sum())>=8,paired_CI_lower_above0=interval[0]>0,
                     EOS_no_worse_than_story=evaluation['greedy_rates']['eos']>=controls['story']['greedy_rates']['eos'],
                     repetition_no_worse_than_story=evaluation['greedy_rates']['repetition']<=controls['story']['greedy_rates']['repetition'],
                     appropriate_completion_at_least27=summary['appropriate_EOS']>=27)
    diagnostic_differences={}
    old_run=Path(config['reference']['prior_review']['path']).parent
    for task in config['evaluation']['tasks']:
        new={r['id']:r for r in read_json(directory/'evaluation'/(task+'.json'))['rows']}
        old={r['id']:r for r in read_json(old_run/'evaluation/result/coherent20/evaluation'/(task+'.json'))['rows']}
        require('paired_actual_diagnostic_IDs_'+task,set(old)==set(new))
        diagnostic_differences[task]=clustered_ci([dict(id=k,family=new[k].get('family',k),difference=new[k]['credit']-old[k]['credit']) for k in new],key='difference')
    review=dict(status='passed',checks=checks,summary=summary,rates=evaluation['greedy_rates'],BPB=body['bpb'],diagnostics=evaluation['diagnostics'],
                original_selection=original,new_improvement=improvement,paired_coherence_vs_story=dict(difference_count=int(array.sum()),CI95=interval,clustered=paired),
                paired_diagnostics_vs_story=diagnostic_differences,eligible_for_full=original['eligible_for_full'] and all(improvement.values()),
                scored_outputs=[dict(row,**scores[row['id']]) for row in rows],config_sha256=sha256(study.CONFIG),result_sha256=sha256(study.RUN/'result.json'),
                annotations_sha256=sha256(study.RUN/'annotations.json'),reviewer_sha256=sha256(Path(__file__)),checked_at=now(),
                independent_human_blind='not performed; Codex individual content diagnosis',protected_test_used=False,quality_targets_achieved=False)
    write_json(study.RUN/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k not in ('scored_outputs','diagnostics')},ensure_ascii=False),flush=True)


def full_review():
    config=study.load_config();output=study.RUN/'full';result=read_json(output/'result.json');job=read_json(output/'full-job.json');checks={}
    def require(name,value):checks[name]=bool(value);assert value,name
    require('actual_eligible_full_job_complete_exited',job['status']=='complete' and not alive(job) and read_json(study.RUN/'review.json')['eligible_for_full'])
    require('full_binding_budget_zero_learning',result['binding']==job['binding'] and result['binding']['review_sha256']==sha256(study.RUN/'review.json') and result['GPU_seconds']<=job['gpu_elapsed_seconds']<=1800 and result['additional_training_tokens']==0)
    full=read_json(output/'candidate-full.json');body=full['body'];generation=full['generation'];trained=read_json(study.RUN/'result.json')['trained']
    require('actual_final_checkpoint_and_RNG_binding',full['binding']==result['binding'] and full['checkpoint_sha256']==trained['checkpoint_sha256']==sha256(Path(trained['checkpoint'])) and full['evaluation_RNG_isolated'])
    require('all89416_actual_body_coverage_NLL_BPB',full['full'] and body['documents']==len(body['rows'])==89416 and body['body_bytes']==164344743 and body['body_tokens']==42003934 and all(r['body_tokens']==r['scored_body_tokens'] and math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
    parent_body=read_json(Path(config['reference']['parent_body']['path']))['body'];parent_gen=read_json(Path(config['reference']['parent_generation']['path']))['generation']
    control=read_json(Path(config['reference']['web_full']['path']));story=read_json(Path(config['reference']['story_full']['path']))
    for label,other in [('parent',dict(body=parent_body,generation=parent_gen)),('web',control),('story',story)]:
        require_alignment(body,generation,other['body'],other['generation']);require('full_same_documents_and400_requests_'+label,True)
    tok=Tokenizer(ROOT/config['tokenizer']);validate_rows(generation['outputs'],tok)
    require('all400_raw_output_flags',len(generation['outputs'])==400)
    fixed={r['id']:r for r in generation['outputs'] if r['decoding']=='greedy' and r['suppressed']}
    primary=read_json(study.RUN/'whole20/evaluation/result.json')
    require('fixed80_same_actual_ids_as_primary',all(fixed[r['id']]['generated_ids']==r['generated_ids'] for r in primary['generation']['outputs']))
    long=read_json(output/'long-generation.json')
    require('complete40_long_requests_and_binding',long['complete'] and len(long['rows'])==40 and long['binding']==json.dumps(result['binding'],sort_keys=True) and {r['max_new_tokens'] for r in long['rows']}=={128,512})
    for row in long['rows']:
        ids=row['generated_ids'];raw=tok.decode_bytes(ids)
        try:text=raw.decode('utf-8');valid=True
        except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
        assert row['text']==text and row['valid_utf8']==valid and repetition_metrics(row)==row['metrics'] and 0<len(ids)<=row['max_new_tokens'] and 3 not in ids[:-1]
    require('long_raw_UTF8_and_repetition_recomputed',True)
    for maximum in (128,512):
        rows=[r for r in long['rows'] if r['max_new_tokens']==maximum];summary=long['summary'][str(maximum)]
        require('long'+str(maximum)+'_summaries_recomputed',summary['count']==summary['expected']==len(rows)==20 and summary['natural_eos']==sum(r['metrics']['natural_eos'] for r in rows) and summary['same_sentence_repeat']==sum(r['metrics']['same_sentence_reappears'] for r in rows) and summary['raw_utf8_failure']==sum(r['metrics']['raw_utf8_failure'] for r in rows))
    summary=summarize('whole20',trained['tokens'],body,generation);parent=summarize('parent10B',10000007168,parent_body,parent_gen)
    actual=dict(mixture=adoption_checks(control,full),parent_growth=growth_checks(summary,parent))
    require('all_original_full_gates_recomputed',actual==result['checks'] and result['candidate_passes_all_full_conditions']==(all(actual['mixture'].values()) and all(actual['parent_growth'].values())))
    require('scope_no_protected_test_no_quality_claim',not result['protected_test_used'] and not result['quality_targets_achieved'])
    write_json(output/'review.json',dict(status='passed',checks=checks,checked_at=now(),summary=summary,long=long['summary'],actual_conditions=actual,candidate_passes_all_full_conditions=result['candidate_passes_all_full_conditions'],result_sha256=sha256(output/'result.json'),raw_full_sha256=sha256(output/'candidate-full.json'),raw_long_sha256=sha256(output/'long-generation.json'),reviewer_sha256=sha256(Path(__file__))))
    print(json.dumps(dict(checks=checks,full_conditions=actual)),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('primary','full'),default='primary');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='primary':primary_review()
    else:full_review()
