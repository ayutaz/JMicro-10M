"""Requirement-by-requirement completion for plan66, including original UI proof."""
import json
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive
import run_condition_diagnostic as study


def main():
    c=study.load_config();run=study.RUN;ready=read_json(study.DATA/'ready.json');review=read_json(run/'review.json');result=read_json(run/'result.json');probe=read_json(run/'packing-probe.json')
    checks={}
    def require(name,value):
        checks[name]=bool(value)
        assert value,name
    require('stage1_fixed_real_1000_5000_whole_documents',ready['pools']['compact']['documents']==1000 and ready['pools']['expanded']['documents']==5000 and ready['pools']['compact']['unique_tokens']==55273 and ready['pools']['expanded']['unique_tokens']==280724 and ready['pools']==c['pools'])
    require('stage1_fixed100_unseen_names_structure_and_eval_separation',ready['dev_documents']==100 and ready['train_dev_full_text_disjoint'] and ready['dev_names_not_in_train'] and ready['structural_dev_template_not_trained'] and ready['fixed_eval_prefixes_not_in_train'])
    suites=list(ET.parse(run/'tests.xml').getroot().iter('testsuite'))
    require('stage1_relevant_CPU5_tests_no_failures',sum(int(s.attrib['tests']) for s in suites)==5 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped')))
    require('stage2_real_two_finite_checkpointed_24969216_train_and_dev_evals',set(result['checkpoints'])=={'compact','expanded'} and all(d['additional_input_tokens']==24969216 and Path(d['checkpoint']).is_file() and sha256(Path(d['checkpoint']))==d['checkpoint_sha256'] for d in result['checkpoints'].values()) and all(result['conditions'][a]['results'][s]['summary']['total']==100 for a in ('compact','expanded') for s in ('train','dev')))
    require('stage2_actual_CUDA_full_state_resume_gate',result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()) and result['verification_tokens']==262144)
    require('stage3_actual_same_budget_expansion_failed_goal_not_rerolled',not result['mixed100m_executed'] and all(not result['conditions'][a]['diagnostic_pass'] for a in ('compact','expanded')) and not any((run/a).exists() for a in ('mixed-control','mixed-candidate')))
    require('stage3_real_bound_packed_vs_isolated_probe_no_learning',probe['status']=='complete' and probe['additional_learning_tokens']==0 and not alive(probe['identity']) and all(probe['arms'][a]['checkpoint_sha256']==result['checkpoints'][a]['checkpoint_sha256'] and probe['arms'][a]['packed_correct']==probe['arms'][a]['retained'] and probe['arms'][a]['isolated_correct']<probe['arms'][a]['packed_correct'] for a in ('compact','expanded')))
    require('stage4_all_new_Japanese_and160_raw_bound_content_evidence',review['status']=='passed_evidence_audit' and all(review['checks'].values()) and review['result_sha256']==sha256(run/'result.json') and review['annotations_sha256']==sha256(run/'annotations.json') and len(read_json(run/'annotations.json')['arms'])==2)
    require('stage4_unchanged_adoption_failed_full_not_started',not review['comparisons']['compact__expanded']['eligible_for_full'] and not (run/'full').exists())
    require('actual_scientific_job_exited',read_json(run/'job.json')['status']=='complete' and not alive(read_json(run/'job.json')))
    require('actual_tokens_GPU_budgets_separate',result['scientific_tokens']==49938432 and result['verification_tokens']==262144 and result['GPU_seconds']+probe['GPU_wall_seconds']<=c['total_gpu_budget_seconds'])
    require('actual_each_train_within_frozen_180s',all(d['training_seconds']<=c['diagnostic_train_budget_seconds'] for d in result['checkpoints'].values()))
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:http=json.load(response)
    require('original10B_UI_actual_identity_HTTP',ui['status']=='running' and alive(ui) and http['checkpoint_sha256']==c['parent']['sha256'] and http['training_tokens']==c['parent']['tokens_seen'] and not http['busy'])
    report=ROOT/'docs/67_condition_learning_diagnostic_results.md'
    require('stage4_results_report_real_and_frozen_sources_intact',report.is_file() and review['config_sha256']==sha256(study.CONFIG))
    judgment=dict(candidate_adopted=False,quality_targets_achieved=False,decision='diagnostic_learning_complete_both_goals_missed_candidates_rejected',
        train_dev={a:{s:result['conditions'][a]['results'][s]['summary'] for s in ('train','dev')} for a in ('compact','expanded')},
        matched100m_hypothesis='Not executed because frozen prerequisite failed',
        measured_finding='Both models answer retained train targets100% with original packed context; standalone context falls to72/95 and65/96',
        next_proposal='Compare document-isolated learning against fixed cross-document packing, preserving body/EOS and equal budgets; not launched',checked_at=now())
    write_json(run/'judgment.json',judgment)
    completion=dict(status='complete_plan66_stages1_to4_with_actual_learning_failed_diagnostic_branch',checks=checks,
        report_sha256=sha256(report),review_sha256=sha256(run/'review.json'),probe_sha256=sha256(run/'packing-probe.json'),
        judgment_sha256=sha256(run/'judgment.json'),finalizer_sha256=sha256(Path(__file__)),scientific_tokens=49938432,
        verification_tokens=262144,quality_targets_achieved=False,original_UI=ui,HTTP_model=http,checked_at=now(),
        stop_boundary='Verified local commit and stop; no further learning,20B,Chat,test,push or publication')
    write_json(run/'completion.json',completion)
    print(json.dumps(dict(status=completion['status'],checks=len(checks),UI_PID=ui['pid'])),flush=True)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);main()
