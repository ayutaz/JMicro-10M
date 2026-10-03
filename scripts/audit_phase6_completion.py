"""Audit the requested generation/export and settings scope; never start Base."""
from pathlib import Path
import argparse
import collections
import hashlib
import html
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import implementation_hashes
from phase6_performance import alive
from run_base import validate_config


def document_links(root):
    files=[root/'AGENTS.md',root/'README.md',*sorted((root/'docs').glob('*.md')),
           root/'data/README.md',root/'eval/README.md',root/'reports/README.md',
           root/'reports/phase4/resource_budget.md',*sorted((root/'reports/phase5').glob('*.md'))]
    def slug(text):
        text=re.sub(r'<[^>]+>','',text)
        text=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',text)
        text=html.unescape(text).lower().replace('`','')
        return ''.join(c for c in text if c.isalnum() or c in '_- ').replace(' ','-')
    anchors={}
    for path in files:
        counts=collections.Counter();values=set()
        for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',path.read_text(),re.M):
            key=slug(heading);count=counts[key]
            values.add(key if not count else f'{key}-{count}');counts[key]+=1
        anchors[path.resolve()]=values
    errors=[];links=0
    for path in files:
        text=path.read_text()
        for label,target in re.findall(r'\[([^]\n]+)\]\(([^)\n]+)\)',text):
            if re.match(r'^(https?://|app://|mailto:)',target):continue
            target=target.split(' "',1)[0].strip('<>');relative,_,anchor=target.partition('#')
            dest=(path.parent/relative).resolve() if relative else path.resolve();links+=1
            if not dest.exists() or anchor and dest in anchors and anchor not in anchors[dest]:
                errors.append(f'{path.relative_to(root)}: {target}')
        in_code=False
        for line in text.splitlines():
            if line.startswith('```'):in_code=not in_code
            elif in_code and (re.match(r'^\s*(python(?:3)?|py)\s',line) or re.match(r'^\s*uv\s+run\s',line) and '--frozen' not in line):
                errors.append(f'{path.relative_to(root)}: direct/unfrozen Python command')
    return {'markdown_files':len(files),'internal_links':links,'errors':errors}


def audit(windows,run):
    reports=windows/'reports/phase6'
    core=implementation_hashes()
    gen=read_json(reports/'generation_diagnostics.json')
    export=read_json(reports/'nonorm_export_parity_report.json')
    cli=read_json(reports/'readiness_export_audit.json')
    gpu=read_json(reports/'readiness_gpu_audit.json')
    stability=read_json(run/'readiness_stability_report.json')
    full=read_json(reports/'expanded_dev_baseline.json')
    config=validate_config(ROOT/'configs/phase6/base_frozen.json')
    old=read_json(windows/'configs/phase6/base_frozen_blocked_v1.json')
    launch=read_json(reports/'base_launch_plan.json')
    guard=read_json(reports/'base_launch_guard_report.json')
    history=read_json(reports/'readiness_historical_binding.json')
    tests=ET.parse(reports/'readiness_precision_tests.xml').getroot()
    counts={key:sum(int(suite.get(key,0)) for suite in tests.iter('testsuite')) for key in ('tests','errors','failures','skipped')}
    checks={}
    outputs=gen['generation']['outputs']
    checks['1_all_400_fixed_dev_outputs']=gen['status']=='passed_diagnosis' and len(outputs)==400 and all(row['split']=='dev' for row in outputs)
    checks['1_five_groups_each_80']=len(gen['rates'])==5 and all(row['outputs']==80 for row in gen['rates'].values())
    checks['1_generation_source_matches_current_training']=gen['implementation']==core
    checks['1_original_quality_failures_retained']=not gen['quality_targets_achieved'] and not gen['human_scoring_performed'] and not config['quality_targets_achieved']
    checks['1_cuda_cache_original_tolerance']=gen['cuda_cache_tolerance']=={'atol':1e-5,'rtol':1e-4} and gen['cuda_cache_max_abs_error']<=1e-5
    checks['2_original_12_comparisons_and_13_contracts']=export['status']=='passed' and len(export['comparisons'])==12 and len(export['checks'])==13 and all(export['checks'].values()) and all(row['passed'] for row in export['comparisons'].values())
    checks['2_original_fixed_tolerance']=export['tolerance']=={'atol':1e-5,'rtol':1e-4}
    checks['2_final_actual_export_bound']=sha256(run/'export-stable-f32/nonorm_export_parity_report.json')==sha256(reports/'nonorm_export_parity_report.json')
    checks['2_independent_149_weight_and_real_cli_checks']=cli['status']=='passed_export_and_cli' and len(cli['checks'])==149 and all(cli['checks'].values()) and len(cli['cli_cases'])==9
    checks['2_current_real_CLI_source_bound']=all(sha256(ROOT/name)==digest for name,digest in cli['source_sha256'].items())
    checks['2_export_CLI_proof_bound']=cli['evidence'][str(run/'export-stable-f32/nonorm_export_parity_report.json')]==sha256(run/'export-stable-f32/nonorm_export_parity_report.json')
    checks['2_stock_failures_preserved']=all(read_json(reports/name)['status']=='failed' for name in ('nonorm_export_stock_fp32_failure.json','nonorm_export_initial_failure.json','nonorm_export_precision_failure.json','nonorm_cuda_reference_report.json'))
    raw_path=Path(full['raw_report']['path'])
    raw=read_json(raw_path);body=raw['body'];rows=body['rows']
    checks['3_full_dev_raw_population_and_digest']=sha256(raw_path)==full['raw_report']['sha256'] and len(rows)==body['documents']==89416 and body['body_bytes']==164344743
    checks['3_every_body_token_once_eos_separate']=body['body_tokens']==42003934 and all(row['scored_body_tokens']==row['body_tokens'] for row in rows) and sum(row['scored_body_tokens'] for row in rows)==42003934
    checks['3_scalar_batched_prior_gate']=raw['scalar_batched_gpu_agreement']['bpb_abs_difference']<=raw['scalar_batched_gpu_agreement']['bpb_tolerance_frozen']==.001
    checks['3_current_eval_source_bound']=raw['implementation']==core and sha256(ROOT/'src/jmicro/readiness.py')==stability['binding']['evaluation_sha256']
    checks['4_three_fixed_lr_budgets']=len(stability['lr_results'])==3 and {row['lr'] for row in stability['lr_results']}=={.001,.002,.003} and all(row['stable']['update']==2000 and row['decay']['update']==2100 and row['stable']['finite'] and row['decay']['finite'] for row in stability['lr_results'])
    checks['4_best_stable_bounded_lr_selected']=config['lr']==stability['selected_lr']==min(stability['lr_results'],key=lambda row:row['dev']['body']['bpb'])['lr']==.002
    checks['5_exact_50_cold_25_checks']=len(stability['exact']['checks'])==50 and len(stability['cold_checks'])==25 and all(stability['exact']['checks'].values()) and all(stability['cold_checks'].values())
    checks['5_independent_106_GPU_checks']=gpu['status']=='passed_bounded_gpu' and len(gpu['checks'])==106 and all(gpu['checks'].values()) and gpu['implementation']==core
    checks['5_training_implementation_and_worker_unchanged']=stability['binding']['implementation']==core and sha256(ROOT/'scripts/phase6_performance.py')==stability['binding']['worker_sha256'] and sha256(ROOT/'scripts/phase6_readiness.py')==stability['binding']['runner_sha256']
    checks['5_GPU_audit_raw_evidence_bound']=all(sha256(Path(path))==digest for path,digest in gpu['evidence'].items())
    checks['6_frozen_version2_all_technical_gates']=config['version']==2 and config['launch_enabled'] and all(config['launch_gates'].values())
    checks['6_batch_lr_wsd_global_budget']=config['batch']==32 and config['context']==1024 and config['accumulation']==1 and config['input_tokens_per_update']==32768 and config['warmup']==200 and config['schedule_updates']==305176 and config['scheduler']=='wsd'
    checks['6_cpu_precision_artifacts_and_runtime_bound']='validated_inference' in config and config['validated_inference']['profile']=='cpu-f32-f64-accumulation-v1'
    checks['6_launch_plan_binds_actual_config']=launch['status']=='frozen_not_started' and launch['config_sha256']==sha256(ROOT/'configs/phase6/base_frozen.json')==sha256(windows/'configs/phase6/base_frozen.json')
    checks['6_all_5_launch_resume_and_evaluation_commands']=len(launch['milestones'])==5 and all(set(row)=={'prepare','stable_start_or_resume','decay_start_or_resume','full_dev_and_400_generation'} and all(command[:3]==['uv','run','--frozen'] for command in row.values()) for row in launch['milestones'].values())
    prepared=read_json(ROOT/'reports/local/base_prepare_validated_500m.json')
    checks['6_real_prepare_preserves_global_schedule_without_execution']=prepared['status']=='prepared_not_started' and prepared['launch_enabled'] and prepared['end_update']==15259 and '--execute' not in prepared['commands'][0] and prepared['commands'][0][prepared['commands'][0].index('--schedule-updates')+1]=='305176'
    checks['6_old_config_and_specific_launch_rejection_preserved']=not old['launch_enabled'] and guard['status']=='passed_rejection' and all(guard['checks'].values()) and guard['config_sha256']==sha256(windows/'configs/phase6/base_frozen_blocked_v1.json')
    checks['6_budget_and_capacity_bound']=config['capacity']['checkpoint_retention'].startswith('all completed') and config['capacity']['estimated_checkpoint_bytes']<config['capacity']['maximum_output_bytes'] and config['measured_budget']['all_full_dev_and_generation_seconds']>0
    query=subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-compute-apps=pid','--format=csv,noheader'],capture_output=True,text=True,check=True)
    jobs=[read_json(run/'job.json'),read_json(run/'cpu-precision/job.json')]
    checks['stop_no_live_GPU_or_identified_jobs']=not query.stdout.strip() and all(job['status']=='complete' and not alive(job) for job in jobs)
    checks['stop_no_Base_scaling_run_or_output']=not config['scaling_started'] and not (ROOT/'reports/phase6/base-20261003').exists() and not (windows/'reports/phase6/base-20261003').exists()
    checks['all_90_tests_no_skip_error_failure']=counts=={'tests':90,'errors':0,'failures':0,'skipped':0}
    checks['73_historical_reports_byte_preserved']=len(history['files'])==73 and all(sha256(windows/name)==digest for name,digest in history['files'].items())
    checks['dependency_lock_byte_preserved']=sha256(windows/'uv.lock')==history['dependency_lock_sha256']
    links=document_links(windows);checks['all_document_links_and_uv_contracts']=not links['errors']
    sync=['AGENTS.md','docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md','docs/24_phase6_plan.md','docs/27_phase6_remaining_plan.md','docs/30_phase6_readiness_execution.md',
          *config['source_sha256'], 'configs/phase6/base_frozen.json','schemas/configs/phase6/base_frozen.schema.json']
    checks['Windows_and_Linux_final_code_settings_docs_synchronized']=all((windows/name).read_bytes().replace(b'\r\n',b'\n')==(ROOT/name).read_bytes().replace(b'\r\n',b'\n') for name in sync)
    package={'status':'passed_package' if all(checks.values()) else 'failed','checks':checks,'tests':counts,'documentation':links,
             'overall_readiness_complete':all(checks.values()),'scope':'Requested Phase6 readiness steps4/5; not Base training or quality completion','completed_at':now()}
    write_json(reports/'readiness_package_audit.json',package)
    requirements=[]
    names=['400 fixed dev generation and cache diagnosis; unmet quality retained',
           'Learned HF/Llama and float GGUF, original short/1024/cache/tolerance, IDs/tie/real EOS/EOT stops',
           '89,416 heldout dev documents scored completely, common-byte BPB and measured time',
           '3 bounded equal-budget LR/stable/independent decay comparisons with unchanged parents',
           'Changed training source verified strict/cold exact resume with all state and histories',
           'Final model/data/source/precision/optimizer/budget/capacity/CLI/persistent recovery settings frozen']
    evidence=[['generation_diagnostics.json'],['nonorm_export_parity_report.json','readiness_export_audit.json'],
              ['expanded_dev_baseline.json','readiness_gpu_audit.json'],['readiness_stability_report.json','readiness_gpu_audit.json'],
              ['readiness_stability_report.json','readiness_gpu_audit.json'],['base_launch_plan.json','base_launch_guard_report.json']]
    for number,(name,paths) in enumerate(zip(names,evidence),1):
        subset={key:value for key,value in checks.items() if key.startswith(f'{number}_')}
        requirements.append({'item':number,'requirement':name,'state':'proved_complete' if all(subset.values()) else 'incomplete',
                             'checks':subset,'evidence':{str(reports/name):sha256(reports/name) for name in paths}})
    result={'status':'passed_requested_scope' if all(checks.values()) else 'incomplete',
        'objective':'Finish generation/export validation and long-training settings, then stop before 500M Base scaling',
        'requirements':requirements,'checks':checks,'package_audit':'reports/phase6/readiness_package_audit.json',
        'tests':'reports/phase6/readiness_precision_tests.xml','overall_goal_achieved':all(checks.values()),
        'previous_goal_turn':'no_progress: plan/status only; this turn implemented and validated inference repair and settings',
        'current_goal_turn':'progress','base_quality_targets_achieved':False,'long_training_started':False,
        'remaining_outside_requested_scope':['500M+ Base scaling and quality evaluation','Chat','quantized quality and local distribution'],
        'next_action':'Commit verified final result and stop; next Base stage requires user resumption',
        'user_action_required':False,'completed_at':now()}
    write_json(reports/'readiness_gate_audit.json',result)
    print(json.dumps({'status':result['status'],'checks':len(checks),'failed':[key for key,value in checks.items() if not value],'link_errors':links['errors']}),flush=True)
    assert all(checks.values()),checks


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--windows',type=Path,default=Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m'))
    parser.add_argument('--run',type=Path,default=ROOT/'reports/phase6/readiness-20261003')
    args=parser.parse_args();audit(args.windows.resolve(),args.run.resolve())
