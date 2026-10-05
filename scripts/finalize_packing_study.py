"""Audit the authorized three stages, conditional comparison, judgment and UI."""
import json
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import implementation_hashes
from phase6_performance import alive
import run_packing_study as study


def main():
    c=study.load_config();run=study.RUN;result=read_json(run/'result.json');review=read_json(run/'review.json');job=read_json(run/'job.json')
    olddev=read_json(run/'previous-dev-evaluation.json');checks={}
    def require(name,value):
        checks[name]=bool(value)
        assert value,name
    require('stage1_exact_common_whole_train_pool_frozen',c['pool']['documents']==1000 and c['pool']['unique_tokens']==55273 and c['pool']['manifest_sha256']==sha256(Path(c['pool']['pool'])/'manifest.json') and review['config_sha256']==sha256(study.CONFIG))
    require('all_frozen_training_evaluation_sources_unchanged',all(sha256(ROOT/p)==digest for p,digest in c['source_sha256'].items()) and implementation_hashes()==c['implementation'])
    alias=read_json(run/'evaluation-alias-repair.json')
    require('legacy_evaluator_alias_exact_common_train_no_retraining',alias['scientific_retraining_tokens']==0 and alias['sha256']==c['train_eval_sha256']==sha256(study.DATA/'expanded-train-eval.json')==sha256(study.DATA/'compact-train-eval.json'))
    fresh=read_json(study.DATA/'dev.json');previous=read_json(study.DATA/'previous-dev.json')
    require('stage1_fresh100_no_prior_dev_overlap_balanced_structure',len(fresh)==100 and len({r['text'] for r in fresh})==100 and not {r['text'] for r in fresh}&{r['text'] for r in previous} and sum(r['structural_holdout'] for r in fresh)==50)
    suites=list(ET.parse(run/'tests.xml').getroot().iter('testsuite'))
    require('stage1_relevant_CPU5_tests_success',sum(int(s.attrib['tests']) for s in suites)==5 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped')))
    gate=result['resume_gate']
    require('stage1_three_actual_CUDA_modes_all_resume_state',gate['passed'] and set(gate['arms'])=={'fixed','shuffle','isolated'} and all(all(v['checks'].values()) for v in gate['arms'].values()) and gate['GPU_optimizer_updates']==24)
    require('stage2_three_actual25M_teacher_checkpoints',all(result['checkpoints'][a]['additional_supervised_tokens']==25000000 and Path(result['checkpoints'][a]['checkpoint']).is_file() and sha256(Path(result['checkpoints'][a]['checkpoint']))==result['checkpoints'][a]['checkpoint_sha256'] for a in ('fixed','shuffle','isolated')))
    require('stage2_train_fresh_previous100_separate_actual_evaluations',all(all(result['conditions'][a]['results'][s]['summary']['total']==100 for s in ('train','dev')) and olddev['arms'][a]['summary']['total']==100 for a in result['checkpoints']))
    eligible=[a for a in ('shuffle','isolated') if result['conditions'][a]['diagnostic_pass']]
    selected=max(eligible,key=lambda a:(result['conditions'][a]['results']['dev']['summary']['accuracy'],result['conditions'][a]['results']['dev']['summary']['both_accuracy'],a=='shuffle')) if eligible else None
    require('stage3_frozen_goal_and_candidate_selection',result['selected']==review['selected']==selected and bool(selected)==result['mixed100m_executed'])
    if selected:
        require('stage3_actual_two100M_same_Web80M_short20M',all(result['checkpoints'][a]['additional_supervised_tokens']==100000000 and result['checkpoints'][a]['source_teachers']==dict(web=80000000,short=20000000) for a in ('mixed-fixed','mixed-candidate')))
    else:require('stage3_no_unqualified100M_launched',not any((run/a).exists() for a in ('mixed-fixed','mixed-candidate')))
    require('stage3_all_new_terminal_Japanese_and_raw_content_verified',review['status']=='passed_evidence_audit' and all(review['checks'].values()) and review['result_sha256']==sha256(run/'result.json') and review['annotations_sha256']==sha256(run/'annotations.json') and all(len(r['notes'])==80 for r in read_json(run/'annotations.json')['arms'].values()))
    require('all_scientific_and_extra_eval_jobs_actual_exited',job['status']=='complete' and not alive(job) and olddev['status']=='complete' and not alive(olddev['identity']))
    require('actual_teacher_verification_PAD_GPU_budgets_separate',result['scientific_teacher_tokens']==75000000+(200000000 if selected else 0) and result['verification_teacher_tokens']==gate['verification_teacher_tokens'] and
        result['GPU_seconds']+olddev['GPU_wall_seconds']<=c['total_gpu_budget_seconds'] and result['physical_input_tokens']>=result['scientific_valid_input_tokens'])
    comparison=review['comparisons']['mixed-fixed__mixed-candidate' if selected else 'fixed__shuffle']
    if comparison['eligible_for_full']:
        raise AssertionError('Primary eligible; required full evaluation and acceptance remain unverified')
    require('unchanged_adoption_conditions_reject_full_not_started',not comparison['eligible_for_full'] and not (run/'full').exists())
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:http=json.load(response)
    require('original10B_UI_actual_process_HTTP',ui['status']=='running' and alive(ui) and http['checkpoint_sha256']==c['parent']['sha256'] and http['training_tokens']==c['parent']['tokens_seen'] and not http['busy'])
    report=ROOT/'docs/69_packing_learning_results.md'
    require('results_report_exists_and_all_frozen_sources_intact',report.is_file() and not result['protected_test_used'])
    judgment=dict(decision='Completed three-arm and conditional mixed comparison; candidate not adopted under unchanged primary quality gates',selected=selected,
        primary_failed_conditions={group:[k for k,v in values.items() if not v] for group,values in [('quality',comparison['quality']['checks']),('practical',comparison['practical']),('original_Web',comparison['original_Web_gates'])]},
        candidate_adopted=False,quality_targets_achieved=False,scientific_teacher_tokens=result['scientific_teacher_tokens'],verification_teacher_tokens=result['verification_teacher_tokens'],
        measured_finding='Same material: order shuffle and isolation learn standalone train conditions; general-language quality separately judged',checked_at=now())
    write_json(run/'judgment.json',judgment)
    completion=dict(status='complete_plan68_stages1_to3',checks=checks,report_sha256=sha256(report),review_sha256=sha256(run/'review.json'),judgment_sha256=sha256(run/'judgment.json'),
        finalizer_sha256=sha256(Path(__file__)),original_UI=ui,HTTP_model=http,scientific_teacher_tokens=result['scientific_teacher_tokens'],verification_teacher_tokens=result['verification_teacher_tokens'],
        selected=selected,candidate_adopted=False,quality_targets_achieved=False,checked_at=now(),stop_boundary='Verified local commit and stop; no further learning,20B,Chat,test,push/publication')
    write_json(run/'completion.json',completion)
    print(json.dumps(dict(status=completion['status'],checks=len(checks),selected=selected,UI_PID=ui['pid'])),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);main()
