"""Final requirement audit; completed GPU work is reused, never restarted."""
import json
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive
import run_matched_story_study as study

def main():
    checks={};stages={};scientific=verification=gpu=0
    def require(name,value):checks[name]=bool(value);assert value,name
    data=read_json(study.DATA/'ready.json');content=read_json(study.DATA/'content-review.json')
    builder=read_json(study.DATA/'job.json')
    require('actual_builder_complete_exited_bounded',builder['status']=='complete' and not alive(builder) and builder['elapsed_seconds']<=1800 and data['seconds']<=1800)
    require('builder_original_train_source_and_code_bound',builder['binding']==data['binding'] and data['binding']['builder_sha256']==sha256(ROOT/'scripts/prepare_matched_story_pools.py') and data['binding']['selector_sha256']==sha256(ROOT/'src/jmicro/story_quality.py'))
    require('train_only_whole_original_stories',data['source_train_only'] and data['whole_original_stories'] and not data['new_independent_unique_data'])
    require('actual_paired_data_quantity_lengths_EOS',data['matched_quantity_length_sequence_EOS_positions'] and data['totals']['control']==data['totals']['refined'] and data['totals']['control']['tokens']>=20000000 and abs(data['body_tokens_mean']/data['old_body_tokens_mean']-1)<=.05)
    require('all80_random_full_story_notes_bound',content['ready_sha256']==sha256(study.DATA/'ready.json') and all(len(v['notes'])==40 and v['samples_sha256']==sha256(study.DATA/a/'samples.json') and v['manifest_sha256']==sha256(study.DATA/a/'manifest.json') for a,v in content['arms'].items()))
    for stage in ('content','amount'):
        c=study.load_config(stage);run,path,schema=study.paths(stage);result=read_json(run/'result.json');review=read_json(run/'review.json');job=read_json(run/'screen-job.json')
        require(stage+'_actual_scientific_and_primary_complete_exited',job['status']=='complete' and not alive(job) and result['status']=='complete_pending_content_review')
        require(stage+'_CPU_evidence_review_all_checks_pass',review['status']=='passed' and all(review['checks'].values()) and review['result_sha256']==sha256(run/'result.json') and review['annotations_sha256']==sha256(run/'annotations.json') and review['config_sha256']==sha256(path))
        require(stage+'_all160_individual_content_review',sum(len(rows) for rows in review['scored_outputs'].values())==160 and all(len(rows)==80 and all(r['rationale'] for r in rows) for rows in review['scored_outputs'].values()))
        require(stage+'_actual_save_resume_and_separate_accounting',result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()) and result['scientific_tokens']==1000013824 and result['verification_tokens']==262144)
        require(stage+'_scientific_GPU_budget_preserved',result['GPU_seconds']<=job['gpu_elapsed_seconds']<=2400)
        suites=list(ET.parse(run/'tests.xml').getroot().iter('testsuite'))
        require(stage+'_relevant_CPU_tests',sum(int(s.attrib['tests']) for s in suites)>=10 and all(int(s.attrib[k])==0 for s in suites for k in ('failures','errors','skipped')))
        scientific+=result['scientific_tokens'];verification+=result['verification_tokens'];gpu+=job['gpu_elapsed_seconds']
        full=None
        if review['eligible_for_full']:
            full=read_json(run/'full/review.json');fulljob=read_json(run/'full/full-job.json')
            require(stage+'_required_conditional_full_complete',fulljob['status']=='complete' and not alive(fulljob) and full['status']=='passed' and all(full['checks'].values()) and full['result_sha256']==sha256(run/'full/result.json') and fulljob['gpu_elapsed_seconds']<=c['full_gpu_budget_seconds'])
            gpu+=fulljob['gpu_elapsed_seconds']
        else:require(stage+'_ineligible_conditional_full_not_started',not (run/'full/full-job.json').exists())
        require(stage+'_protected_test_and_quality_limits_retained',not result['protected_test_used'] and not review['protected_test_used'] and not review['quality_targets_achieved'])
        stages[stage]=dict(config_sha256=sha256(path),schema_sha256=sha256(schema),review_sha256=sha256(run/'review.json'),
            scientific_tokens=result['scientific_tokens'],verification_tokens=result['verification_tokens'],summaries=review['summaries'],
            quality_comparison=review['quality_comparison'],practical=review['practical'],eligible_for_full=review['eligible_for_full'],
            full_review=full,selection=c['selection'],job_identity={k:job[k] for k in ('pid','boot_id','start_ticks','status')})
    amount=study.load_config('amount');a_run=study.paths('amount')[0];a_result=read_json(a_run/'result.json')
    content_adopted=stages['content']['eligible_for_full'] and stages['content']['full_review']['candidate_passes_all_full_conditions']
    require('stage2_executed_even_if_stage1_not_adopted',amount['selection']['selected_refined']==content_adopted and bool(a_result['constant_resume_gate']) and a_result['constant_resume_gate']['passed'])
    selected=data['pools']['refined'] if content_adopted else read_json(ROOT/'configs/phase6/story20_low_lr_10b_500m.json')['pool']
    require('stage2_fixed_actual_selected_data',all(amount['arms']['fixed20'][k]==v for k,v in selected.items()))
    require('matched_constant500M_1B_actual_budget',a_result['checkpoints']['constant500M']['additional_input_tokens']==500006912 and a_result['checkpoints']['constant1B']['additional_input_tokens']==1000013824 and a_result['checkpoints']['constant1B']['tokens']==11000020992)
    require('total_scientific_verification_GPU_preserved',scientific==2000027648 and verification==524288 and gpu<=9600)
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:api=json.load(response)
    # HTTP and actual process agree; a stale launcher record cannot count as restoration.
    require('original_UI_actual_process_running',ui['status']=='running' and alive(ui))
    require('original_UI_HTTP_checkpoint_tokens_idle',api['checkpoint_sha256']==amount['parent']['sha256'] and api['training_tokens']==10000007168 and not api['busy'])
    report=ROOT/'docs/57_matched_story_and_learning_budget_results.md'
    require('both_studies_final_report_present',report.exists() and all(term in report.read_text(encoding='utf-8') for term in ('教材内容','学習量','500M','1B','非blind','停止')))
    judgment=read_json(ROOT/'reports/phase6/matched_story_judgment.json')
    require('final_judgment_report_actual_review_bindings',judgment['status']=='complete_requested_stages1_to3' and judgment['report_sha256']==sha256(report) and all(judgment['review_sha256'][s]==stages[s]['review_sha256'] for s in stages))
    require('both_hypotheses_adoption_matches_prespecified_gates',all(judgment['adopted'][s]==bool(stages[s]['eligible_for_full'] and stages[s]['full_review']['candidate_passes_all_full_conditions']) and judgment['primary_quality_improvement'][s]==stages[s]['quality_comparison']['passed'] for s in stages))
    require('judgment_preserves_scope_and_quality_limits',judgment['stop_after_delivery'] and not judgment['quality_targets_achieved'] and not judgment['protected_test_used'] and judgment['scientific_tokens']==scientific and judgment['verification_tokens']==verification)
    result=dict(status='complete_requested_stages1_to3',checks=checks,stages=stages,scientific_tokens=scientific,verification_tokens=verification,GPU_seconds=gpu,
        UI=dict(record=ui,api=api),report_sha256=sha256(report),judgment_sha256=sha256(ROOT/'reports/phase6/matched_story_judgment.json'),quality_targets_achieved=False,protected_test_used=False,
        stop_boundary='Finish plan56 stages1–3; no further data/GPU/20B/50B/Chat/protected test/push/publication',checked_at=now(),reviewer_sha256=sha256(Path(__file__)))
    write_json(ROOT/'reports/phase6/matched_story_completion.json',result);print(json.dumps(dict(status=result['status'],checks=checks,scientific_tokens=scientific,verification_tokens=verification,GPU_seconds=gpu)),flush=True)

if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);main()
