"""Final requirement audit of plan49's actual failure branch, UI restoration, and proposal."""
import json
import math
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive
import run_story10_comparison as first
import run_story10_low_lr as second
from review_eos_5b_finish import validate_rows
from jmicro.tokenizer import Tokenizer


def main():
    checks={};sources={};science=0;verification=0;GPU=0;jobs=[];arms=[];reviews={}
    def require(name,value):
        checks[name]=bool(value)
        assert value,name
    dev_cases={r['id']:r for r in (json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()) if r['split']=='dev'}
    expected_diagnostics={'semantics':192,'jblimp':331,'jcqa':1119}
    for label,module,test_count in [('normalLR',first,14),('lowerLR',second,16)]:
        config=module.load_config();run=module.RUN
        screen=read_json(run/'result.json');review=read_json(run/'review.json');job=read_json(run/'screen-job.json')
        reviews[label]=review
        require(label+'_actual_job_complete_and_exited',job['status']=='complete' and not alive(job))
        require(label+'_source_config_and_screen_bindings',review['status']=='passed' and review['config_sha256']==sha256(module.CONFIG)
                and review['screen_sha256']==sha256(run/'result.json') and screen['binding']==job['binding'])
        suites=list(ET.parse(run/'tests.xml').getroot().iter('testsuite'))
        require(label+'_relevant_tests',sum(int(s.attrib['tests']) for s in suites)==test_count and
                all(int(s.attrib[k])==0 for s in suites for k in ('failures','errors','skipped')))
        require(label+'_actual_CUDA_save_resume',screen['resume_gate']['passed'] and all(screen['resume_gate']['checks'].values()) and
                screen['verification_tokens']==screen['resume_gate']['input_tokens']==262144)
        require(label+'_original_GPU_budget',screen['GPU_seconds']<=job['gpu_elapsed_seconds']<=config['screen_gpu_budget_seconds'])
        require(label+'_protected_test_unused',not screen['protected_test_used'] and not review['protected_test_used'])
        require(label+'_honest_quality_scope',not review['quality_targets_achieved'] and review['independent_human_blind']=='not performed')
        reference_body=read_json(Path(config['reference']['screen']['path']))['body']
        trained=screen['arms'] if 'arms' in screen else {'coherent10':screen['trained']}
        scientific=sum(a['additional_input_tokens'] for a in trained.values())
        require(label+'_scientific_accounting',scientific==screen['scientific_tokens'])
        tok=Tokenizer(ROOT/config['tokenizer'])
        for arm,detail in trained.items():
            directory=run/arm;evaluation=read_json(directory/'evaluation/result.json')
            body=evaluation['body']
            require(label+'_'+arm+'_common256_body_coverage',len(body['rows'])==body['documents']==256 and
                    body['body_bytes']==reference_body['body_bytes']==472055 and body['body_tokens']==reference_body['body_tokens']==122343 and
                    [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in body['rows']]==
                    [(r['doc_id'],r['body_bytes'],r['body_tokens']) for r in reference_body['rows']] and
                    all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows']))
            require(label+'_'+arm+'_BPB_from_actual_finite_NLL',math.isfinite(body['bpb']) and
                    all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and
                    math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
            require(label+'_'+arm+'_actual_checkpoint_hash',sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']==evaluation['checkpoint_sha256'])
            history=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
            require(label+'_'+arm+'_equal100M_finite_updates',detail['additional_input_tokens']==100007936 and detail['tokens']==10100015104 and
                    detail['update']==308228 and len(history)==3052 and [r['update'] for r in history]==list(range(305177,308229)) and
                    all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
            require(label+'_'+arm+'_fixed_fork_LR',history[0]['lr']==config['peak_lr'] and math.isclose(history[-1]['lr'],config['peak_lr']*.1,rel_tol=.001))
            short=0 if arm=='web' else 9994240
            require(label+'_'+arm+'_source_counts_no_story_wrap',detail['source_tokens']==dict(web=100007936-short,short=short) and detail['sampler']['short']['epoch']==0)
            validate_rows(evaluation['generation']['outputs'],tok)
            content=review['scored_outputs'][arm] if 'scored_outputs' in review else review['rows']
            actual={r['id']:r for r in evaluation['generation']['outputs']}
            require(label+'_'+arm+'_exact80_dev_requests',set(actual)==set(dev_cases) and
                    all(r['prefix']==dev_cases[k]['prefix'] for k,r in actual.items()))
            require(label+'_'+arm+'_all80_content_matches_actual_raw',len(content)==len(actual)==80 and
                    all(row['generated_ids']==actual[row['id']]['generated_ids'] and row['text']==actual[row['id']]['text'] and row['rationale'] for row in content))
            require(label+'_'+arm+'_complete_Japanese_diagnostics',all(evaluation['diagnostics'][task]['complete'] and
                    evaluation['diagnostics'][task]['count']==evaluation['diagnostics'][task]['expected']==expected_diagnostics[task]
                    for task in config['evaluation']['tasks']) and
                    evaluation['diagnostics']['semantic_both_contexts']['total']==96 and evaluation['evaluation_RNG_isolated'])
            arms.append(dict(stage=label,arm=arm,checkpoint=detail['checkpoint'],checkpoint_sha256=detail['checkpoint_sha256'],
                             total_tokens=detail['tokens'],additional_tokens=detail['additional_input_tokens'],source_tokens=detail['source_tokens']))
        for path in (run/'result.json',run/'review.json',run/'tests.xml',module.CONFIG):sources[str(path)]=sha256(path)
        jobs.append({k:job[k] for k in ('pid','boot_id','start_ticks','status','gpu_elapsed_seconds')})
        science+=scientific;verification+=screen['verification_tokens'];GPU+=screen['GPU_seconds']
    require('first_screen_failed_frozen_content_gain',not reviews['normalLR']['selection']['eligible_for_full'] and
            reviews['normalLR']['selection']['coherence_difference_count']==4)
    # This final audit implements the actually taken, bounded failure branch. A passing screen requires full evaluation instead.
    require('lowerLR_screen_failed_original_selection',not reviews['lowerLR']['selection']['eligible_for_full'])
    require('conditional_full_correctly_not_run',not (first.RUN/'full/full-job.json').exists() and not (second.RUN/'full/full-job.json').exists())
    require('no_500M_without_entry_conditions',science==300023808 and verification==524288)
    server=read_json(ROOT/'reports/local/webui/server.json')
    require('actual_UI_identity_live',server['status']=='running' and alive(server))
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:model=json.load(response)
    require('HTTP_UI_original_parent_restored',model['checkpoint_sha256']==first.load_config()['parent']['sha256'] and model['training_tokens']==10000007168 and not model['busy'])
    for path in ('docs/50_story10_and_budget_execution.md','docs/51_story10_judgment_and_next_proposal.md','docs/autonomous_status.md'):
        require('report_exists_'+path,(ROOT/path).is_file());sources[path]=sha256(ROOT/path)
    result=dict(status='passed',checked_at=now(),scope='plan49 stages1–3:100M screen, prespecified matched lowerLR alternative, judgment/proposal;500M entry not met',
                checks=checks,arms=arms,terminal_jobs=jobs,scientific_tokens=science,verification_tokens=verification,GPU_seconds=GPU,
                conditional_full_performed=False,pool_expansion_performed=False,original_acceptance_gates_unchanged=True,
                original_UI=model,UI_identity={k:server[k] for k in ('pid','boot_id','start_ticks','ready_at')},
                quality_targets_achieved=False,independent_human_blind='not performed',protected_test_used=False,
                sources=sources,reviewer_source_sha256=sha256(Path(__file__)),
                remaining_delivery='Verify final local milestone commit and clean worktree before marking goal complete')
    write_json(ROOT/'reports/phase6/story10_execution_completion.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('sources','arms')},ensure_ascii=False),flush=True)


if __name__=='__main__':main()
