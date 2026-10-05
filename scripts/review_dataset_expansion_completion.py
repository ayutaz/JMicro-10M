"""Requirement-by-requirement completion audit of authorized plan58 stages1–3."""
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from urllib.request import urlopen
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive
import run_dataset_expansion as study
from probe_dataset_expansion_supply import DATA

def main():
    assert sys.version_info[:3]==(3,12,7)
    c=study.load_config();run=study.RUN;checks={}
    def require(name,condition):checks[name]=bool(condition);assert condition,name
    ready=read_json(DATA/'shards/ready.json');manifest=read_json(DATA/'shards/manifest.json')
    builder=read_json(DATA/'prepare-job.json');content=read_json(DATA/'content-review.json')
    require('stage1_actual_builder_complete_exited_within1800',builder['status']=='complete' and not alive(builder) and builder['elapsed_seconds']<=1800)
    require('stage1_actual200M_with140M_new_source',ready['totals']['tokens']==manifest['splits']['train']['tokens'] and ready['totals']['tokens']>=200000000 and ready['new_source_tokens']>=140000000 and ready['copied_old_tokens']==59963449)
    require('stage1_train_only_whole_source_contract',ready['source_train_only'] and ready['whole_original_documents'] and not ready['official_validation_test_acquired'] and all('train' in f['path'] for f in ready['files_used']))
    require('stage1_manifest_and_new_stream_hash',sha256(DATA/'shards/manifest.json')==ready['manifest_sha256'] and (DATA/'shards/train.bin').stat().st_size==ready['totals']['tokens']*2 and sha256(DATA/'shards/train.bin')==manifest['splits']['train']['stream_sha256'])
    require('stage1_complete40_individual_source_notes',content['accepted_for_experiment'] and content['samples_sha256']==sha256(DATA/'shards/samples.json') and len(content['notes'])==40 and {r['sample_position'] for r in content['notes']}==set(range(40)) and all(r['rationale'] for r in content['notes']))
    require('stage1_length_EOS_source_changes_frozen_disclosed',not c['actual_data']['length_and_EOS_density_within5percent'] and c['comparison_interpretation'].startswith('Amount plus new translated-story') and c['actual_data']['body_tokens_mean']==ready['body_tokens_mean'])
    result=read_json(run/'result.json');job=read_json(run/'screen-job.json');review=read_json(run/'review.json')
    require('stage2_actual_scientific_job_complete_exited',job['status']=='complete' and not alive(job))
    require('stage2_two1B_scientific_and_verification_separate',result['scientific_tokens']==2000027648 and result['verification_tokens']==262144 and all(r['additional_input_tokens']==1000013824 and r['tokens']==11000020992 for r in result['arms'].values()))
    require('stage2_actual_CUDA_save_resume_exact',result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()))
    require('stage2_actual_matching_routes_schedule_and_midpoints',all(review['checks'][a+'_actual_all_LR_stable_decay'] and review['checks'][a+'_actual_source_routes_short_cursors'] and review['checks'][a+'_actual500M_saved_same_lineage'] for a in ('control','refined')) and review['checks']['same_actual_Web_routes_tokens_and_final_cursor'])
    require('stage3_all_primary_evidence_checks_pass',review['status']=='passed' and all(review['checks'].values()) and review['result_sha256']==sha256(run/'result.json') and review['annotations_sha256']==sha256(run/'annotations.json'))
    require('stage3_correct_applied_LR_reviewer_provenance',review['reviewer_version']==2 and review['reviewer_sha256']==sha256(ROOT/'scripts/review_dataset_expansion_v2.py') and review['frozen_v1_reviewer_sha256']==c['source_sha256']['scripts/review_dataset_expansion.py'])
    suites=list(ET.parse(run/'reviewer-tests.xml').getroot().iter('testsuite'))
    require('stage3_LR_audit_real_scheduler_tests',sum(int(s.attrib['tests']) for s in suites)>=2 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped')))
    require('stage3_all160_individual_content_reviews',all(len(review['scored_outputs'][a])==80 and review['checks'][a+'_all80_individual_notes'] for a in ('control','refined')))
    require('stage3_Japanese192_331_1119_and_common256',all(review['checks'][a+'_Japanese_complete_RNG_isolated'] and review['checks'][a+'_common256_actual_NLL_BPB'] for a in ('control','refined')))
    eligible=review['eligible_for_full'];full=None
    if eligible:
        full=read_json(run/'full/review.json');full_job=read_json(run/'full/full-job.json')
        require('stage3_entered_full_actual_complete_exited',full_job['status']=='complete' and not alive(full_job) and full['status']=='passed' and all(full['checks'].values()))
    else:
        require('stage3_ineligible_full_not_launched',not (run/'full/full-job.json').exists())
    judgment=read_json(run/'judgment.json')
    adopted=eligible and bool(full and full['candidate_passes_all_full_conditions'])
    require('stage3_unchanged_gates_actual_judgment',judgment['candidate_adopted']==adopted and judgment['primary_review_sha256']==sha256(run/'review.json') and not judgment['quality_targets_achieved'])
    require('stage3_GPU_budget_scientific_scope_and_test_exclusion',result['GPU_seconds']<=4800 and (not eligible or read_json(run/'full/result.json')['GPU_seconds']<=1800) and not result['protected_test_used'] and not review['protected_test_used'])
    server=read_json(ROOT/'reports/local/webui/server.json')
    model=json.loads(urlopen('http://127.0.0.1:7860/api/model',timeout=5).read())
    require('original10B_UI_actual_process_and_HTTP_restored',server['status']=='running' and alive(server) and model['checkpoint_sha256']==c['parent']['sha256'] and model['training_tokens']==10000007168 and not model['busy'])
    report=ROOT/'docs/60_dataset_expansion_results.md'
    require('final_results_report_saved',report.exists() and all(s in report.read_text() for s in ('200,000,192','2,000,027,648','262,144')))
    write_json(run/'completion.json',dict(status='complete_requested_stages1_to3',checks=checks,checked_at=now(),
        report_sha256=sha256(report),judgment_sha256=sha256(run/'judgment.json'),review_sha256=sha256(run/'review.json'),
        original_UI=server,HTTP_model=model,scientific_tokens=result['scientific_tokens'],verification_tokens=result['verification_tokens'],
        quality_targets_achieved=False,candidate_adopted=adopted,stop_boundary='Plan58 stages1–3 delivered; no new GPU/data/20B/Chat/test/push',
        reviewer_sha256=sha256(Path(__file__))))
    print(json.dumps(dict(status='complete_requested_stages1_to3',checks=checks)),flush=True)

if __name__=='__main__':main()
