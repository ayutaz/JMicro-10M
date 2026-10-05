"""Requirement-by-requirement final audit for plan54; no training or evaluation."""
import json
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive,identity
from jmicro.eos_pilot import TrainView
from jmicro.tokenizer import Tokenizer
from jmicro.whole_short_text import whole_candidate
import run_complete_document_500m as study


def main():
    assert sys.version_info[:3]==(3,12,7)
    config=study.load_config();pool=Path(config['pool']['pool']);checks={};sources={}
    def require(name,value):checks[name]=bool(value);assert value,name
    def bind(path):sources[str(path)]=sha256(path)
    ready=read_json(pool/'ready.json');samples=read_json(pool/'samples.json');content=read_json(pool/'content-review.json')
    builder=read_json(pool.parent/'job.json')
    require('stage1_actual_builder_complete_exited_budget',builder['status']=='complete' and not alive(builder) and ready['seconds']<=1800 and ready['scan']['web_scan_tokens']<=8000000000)
    require('stage1_actual100to120M_whole_train_data',100000000<=ready['totals']['tokens']<=120000000 and ready['source_train_only'] and ready['whole_original_documents'] and set(ready['by_source'])=={'story','web'} and sum(v['tokens'] for v in ready['by_source'].values())==ready['totals']['tokens'])
    view=TrainView(pool,config['pool']['manifest_sha256'],check_stream=True);tok=Tokenizer(ROOT/config['tokenizer'])
    require('stage1_new_stream_and_index_hashes',sha256(pool/'train.index.jsonl')==view.manifest['splits']['train']['index_sha256'] and view.manifest['splits']['train']['tokens']==ready['totals']['tokens'])
    require('stage1_random40_content_actual_binding',samples['seed']==20261005 and samples['method'].startswith('uniform reservoir') and len(samples['rows'])==len(content['notes'])==40 and content['accepted_for_experiment'] and content['samples_sha256']==sha256(pool/'samples.json'))
    old_views={s:TrainView(ref['directory'],ref['manifest_sha256']) for s,ref in ready['binding']['sources'].items()}
    for i,row in enumerate(samples['rows']):
        a,n=row['offset'],row['body_tokens'];original=old_views[row['source']].tokens[row['source_start']:row['source_end']+1]
        selected=view.tokens[a:a+n+2]
        assert len(original)==len(selected)==n+2 and (original==selected).all() and selected[0]==2 and selected[-1]==3
        text=tok.decode_bytes(selected[1:-1].tolist()).decode('utf-8').strip();unit=whole_candidate(text,n,row['source'])
        assert unit and text==row['text'] and unit['text_sha256']==row['text_sha256']==content['notes'][i]['text_sha256'] and row['split']=='train'
    require('stage1_random40_actual_original_full_documents_no_slicing',True)
    for path in (pool/'manifest.json',pool/'ready.json',pool/'samples.json',pool/'content-review.json',pool.parent/'job.json'):bind(path)
    primary=read_json(study.RUN/'review.json');result=read_json(study.RUN/'result.json');job=read_json(study.RUN/'screen-job.json')
    require('stage2_actual_completed_job_exited_not_proposal',job['status']=='complete' and not alive(job) and result['scientific_tokens']==500006912 and result['trained']['tokens']==10500014080)
    require('stage2_new_data_actual_save_resume_separate_account',result['verification_tokens']==262144 and result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values()))
    suites=list(ET.parse(study.RUN/'tests.xml').getroot().iter('testsuite'))
    require('stage2_actual_related_tests_passed',sum(int(s.attrib['tests']) for s in suites)>=8 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped')))
    require('stage3_primary_actual_state_raw_and80_review',primary['status']=='passed' and all(primary['checks'].values()) and len(primary['scored_outputs'])==80 and primary['result_sha256']==sha256(study.RUN/'result.json') and primary['annotations_sha256']==sha256(study.RUN/'annotations.json'))
    if primary['eligible_for_full']:
        full=read_json(study.RUN/'full/review.json');full_job=read_json(study.RUN/'full/full-job.json')
        require('stage3_required_eligible_full_actual_and_exited',full['status']=='passed' and all(full['checks'].values()) and full_job['status']=='complete' and not alive(full_job))
        for path in (study.RUN/'full/result.json',study.RUN/'full/review.json',study.RUN/'full/candidate-full.json',study.RUN/'full/long-generation.json',study.RUN/'full/full-job.json'):bind(path)
        adopted=full['candidate_passes_all_full_conditions']
    else:
        require('stage3_ineligible_full_not_started',not (study.RUN/'full/full-job.json').exists())
        adopted=False
    judgment=read_json(study.RUN/'judgment.json');report=ROOT/'docs/55_complete_document_500m_results.md'
    require('stage4_judgment_matches_actual_gate_and_report',judgment['status']=='complete_stages1to4' and judgment['adopted']==adopted and judgment['primary_review_sha256']==sha256(study.RUN/'review.json') and judgment['report_sha256']==sha256(report))
    require('stage4_no_false_project_quality_completion',not judgment['quality_targets_achieved'] and not judgment['protected_test_used'] and judgment['independent_human_blind']=='not performed' and judgment['stop_after_delivery'])
    require('stage4_actual_data_learning_amounts_reported',judgment['prepared_short_tokens']==ready['totals']['tokens'] and judgment['scientific_tokens']==500006912 and judgment['verification_tokens']==262144)
    ui=read_json(ROOT/'reports/local/webui/server.json')
    require('stage4_actual_original_UI_process_live',ui['status']=='running' and alive(ui))
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=5) as response:model=json.load(response)
    require('stage4_HTTP_original10B_idle',model['checkpoint_sha256']==config['parent']['sha256'] and model['training_tokens']==10000007168 and not model['busy'])
    for path in (study.RUN/'result.json',study.RUN/'review.json',study.RUN/'annotations.json',study.RUN/'screen-job.json',study.RUN/'judgment.json',study.RUN/'tests.xml',report,study.CONFIG,study.SCHEMA):bind(path)
    for ref in config['reference'].values():bind(Path(ref['path']))
    for name,digest in config['source_sha256'].items():
        require('frozen_source_'+name,sha256(ROOT/name)==digest);bind(ROOT/name)
    output=dict(status='passed',checks=checks,checked_at=now(),source_sha256=sources,UI=ui,HTTP_model=model,stage4_adopted=adopted,
                scientific_tokens=500006912,verification_tokens=262144,quality_targets_achieved=False,protected_test_used=False,
                reviewer_sha256=sha256(Path(__file__)),local_commit_checked_separately_after_delivery=True)
    write_json(study.RUN/'completion.json',output)
    print(json.dumps(dict(status='passed',check_count=len(checks),adopted=adopted,UI_pid=ui['pid'])),flush=True)


if __name__=='__main__':main()
