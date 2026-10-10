"""Close the bounded failed-screen diagnostic with an evidence audit."""
import sys
import json
from pathlib import Path
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.chat_review import content_review
from chat_first_contract import RUN,parent_state,preflight
from review_chat_first_sft import load_evaluation
from phase6_performance import alive
from run_chat_first_sft import SOURCES


def run():
    config=ROOT/'configs/phase7/chat_first_sft.json';c,*_=preflight(config,SOURCES)
    state=parent_state(c)
    audit=read_json(RUN/'training_audit.json')
    assert audit['config_sha256']==sha256(config) and audit['CUDA_resume_exact_all19']
    assert audit['TRAIN_passes']==3 and audit['Assistant_teacher_tokens']==1899555
    assert audit['EOT_teachers']==121098 and audit['parameter_count']==10001152
    for key,file in [('result_sha256','result.json'),('job_sha256','job.json'),('metrics_sha256','metrics.jsonl')]:
        assert audit[key]==sha256(RUN/file)
    comp=read_json(RUN/'greedy_comparison.json')
    assert comp['selected_candidate'] is None and not comp['sampling_required'] and not comp['retention_required']
    assert not any(r['dev_screen_passed'] for r in comp['checkpoint_summaries'])
    reviews={};jobs=[]
    for stage in ('base','epoch1','epoch2','epoch3'):
        directory=RUN.with_name(RUN.name+f'-{stage}-chat')/'greedy'
        ev,items=load_evaluation(directory/'result.json')
        notes=read_json(directory/'content_notes.json');stored=read_json(directory/'content_review.json')
        repeated=content_review(ev,sha256(directory/'result.json'),notes,items)
        for key in ('summaries','categories','content_checks','mechanical_checks','judgments','dev_screen_passed'):
            assert json.loads(json.dumps(repeated[key]))==stored[key],(stage,key)
        assert stored['annotations_sha256']==sha256(directory/'content_notes.json')
        assert stored['evaluation_sha256']==sha256(directory/'result.json')
        assert len(items)==len(stored['judgments'])==219 and not stored['dev_screen_passed']
        assert not stored['Chat_adopted'] and not ev['protected_test_used']
        assert comp['comparisons'].get(stage,{}).get('evidence',{}).get('candidate',{}).get('review_sha256',sha256(directory/'content_review.json'))==sha256(directory/'content_review.json')
        for name,digest in notes['manual_judgment_sources'].items():assert sha256(directory/name)==digest
        reviews[stage]=dict(evaluation_sha256=sha256(directory/'result.json'),notes_sha256=sha256(directory/'content_notes.json'),
            review_sha256=sha256(directory/'content_review.json'),all219_reviewed=True,
            grammar=stored['summaries']['primary']['grammar_score2'],joint=stored['summaries']['primary']['joint_grammar_relevance_score2'],
            final_context=stored['summaries']['own_history_final24']['context_score2'],primary=ev['primary'],own_all=ev['own_history_all_turns'],
            content_checks=stored['content_checks'],mechanical_checks=stored['mechanical_checks'])
        jobs.append(directory.parent/'job.json')
    jobs.extend([RUN/'job.json',RUN/'resume-gate/job.json',RUN.with_name(RUN.name+'-probe')/'probe-job.json'])
    ledger=[]
    for path in jobs:
        job=read_json(path);assert job['status']=='complete' and not alive(job)
        seconds=job['GPU_elapsed_seconds'];assert 0<seconds
        ledger.append(dict(path=str(path),sha256=sha256(path),seconds=seconds,pid=job['pid'],boot_id=job['boot_id'],start_ticks=job['start_ticks']))
    total=sum(r['seconds'] for r in ledger);assert total<=c['total_experiment_GPU_budget_seconds']
    tests=0
    for file in RUN.with_name(RUN.name+'-preparation').glob('*tests.xml'):
        root=ET.parse(file).getroot();suites=[root] if root.tag=='testsuite' else list(root.iter('testsuite'))
        for suite in suites:
            assert int(suite.get('failures','0'))==int(suite.get('errors','0'))==int(suite.get('skipped','0'))==0
            tests+=int(suite.get('tests','0'))
    assert tests==25
    ui=read_json(RUN/'ui_restored.json');model=ui['model']
    assert model['checkpoint_sha256']==c['parent']['sha256'] and not model['busy'] and model['parameters']==10001152
    server=read_json(ROOT/'reports/local/webui/server.json');assert alive(server)
    checks=dict(original_parent_hash_and_model_preserved=True,dedicated_entry_and_CPU25_and_CUDA19=True,
        one_condition_exact_three_TRAIN_passes=True,four_matched_conditions_all876_content_judgments=True,
        fixed_selection_and_conditional_skip_respected=True,all_experiment_jobs_complete_and_dead=True,
        GPU_ledger_within_six_hours=True,original_UI_restored_and_process_alive=True)
    out=dict(status='bounded_diagnostic_complete_condition_rejected',completed_at=now(),requirements=checks,
        requested_five_steps_complete=True,technical_complete=True,learning_complete=True,matched_content_review_complete=True,
        config_sha256=sha256(config),training_audit_sha256=sha256(RUN/'training_audit.json'),comparison_sha256=sha256(RUN/'greedy_comparison.json'),
        reviews=reviews,CPU_tests_passed=tests,GPU_ledger=ledger,total_GPU_elapsed_seconds=total,GPU_budget_seconds=21600,
        selected_candidate=None,diagnostic_best_failed=comp['diagnostic_best'],dev_screen_passed=False,
        conditional_evaluations=dict(sampling='skipped_no_screen_qualified_candidate',Base_retention='skipped_no_screen_qualified_candidate',
            five_local_chat_conversations='skipped_no_screen_qualified_candidate'),Base_retention_passed=None,
        Base_adopted=False,Chat_adopted=False,protected_test_used=False,
        quality_completion=False,independent_human_blind=False,independent_training_seed43=False,
        next_action='Report and stop. No further training, comparisons, quantization, deployment or publication.',
        UI_evidence_sha256=sha256(RUN/'ui_restored.json'),audit_source_sha256=sha256(Path(__file__)))
    write_json(RUN/'completion.json',out)
    print(f'All five steps audited; condition rejected; GPU {total:.3f}s; Base/Chat unadopted')


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    run()
