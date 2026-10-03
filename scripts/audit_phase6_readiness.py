"""Audit the completed bounded GPU evidence, retaining an unmet export gate."""
from pathlib import Path
import argparse
import json
import math
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,now,read_json,sha256,write_json
from jmicro.phase5 import equal_state
from jmicro.training import implementation_hashes
from phase6_performance import finite_state


def audit(run,output):
    torch.set_num_threads(2)
    report=read_json(run/'readiness_stability_report.json')
    checks={}
    checks['gpu_study_complete']=read_json(run/'job.json')['status']=='complete' and report['status']=='passed'
    checks['core_source_matches_completed_trajectory']=implementation_hashes()==report['binding']['implementation']
    checks['exact_and_cold_all_reported_checks_passed']=all(report['exact']['checks'].values()) and all(report['cold_checks'].values())
    histories=[]
    ledger=[]
    for lrrow in report['lr_results']:
        lr=lrrow['lr']
        for stage,end,count in [('stable',2000,2000),('decay',2100,100)]:
            directory=run/'stability'/f'lr-{lr}'/stage
            rows=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
            state=torch.load(directory/f'checkpoint-{end:08d}.pt',map_location='cpu',weights_only=False)
            prefix=f'{lr}_{stage}'
            checks[prefix+'_completed_updates']=len(rows)==count and state['update']==end
            checks[prefix+'_finite']=finite_state(state) and all(math.isfinite(row['loss']) and math.isfinite(row['gradient_norm']) for row in rows)
            checks[prefix+'_budget_and_consumption']=state['tokens']==end*32768 and state['supervised_tokens']<=state['tokens']
            checks[prefix+'_frozen_source']=state['implementation_sha256']==report['binding']['implementation']
            checks[prefix+'_frozen_spec']=state['spec']['lr']==lr and state['spec']['batch']==32 and state['spec']['warmup']==200
            checks[prefix+'_checkpoint_bound']=sha256(directory/f'checkpoint-{end:08d}.pt')==lrrow[stage]['checkpoint_sha256']
            if stage=='stable':
                histories.append(rows)
                profile=read_json(directory/'attention_profile.json')
                checks[prefix+'_actual_compiled_flash']=profile['actual_backend_verified'] and profile['generated_flash_call'] and bool(profile['compiled_calls'])
            ledger.append({'path':str(directory/'metrics.jsonl'),'sha256':sha256(directory/'metrics.jsonl'),
                           'completed_updates':len(rows),'input_tokens':len(rows)*32768})
        before=read_json(run/'stability'/f'lr-{lr}'/'parent_before.json')
        checks[f'{lr}_parent_all_files_immutable']=all(sha256(Path(path))==digest for path,digest in before.items())
        score=read_json(run/f'lr-{lr}-score.json')['body']
        checks[f'{lr}_fixed_dev_population']=score['documents']==256 and score['body_bytes']>0 and math.isfinite(score['bpb'])
    for field in ('token_digest','tokens_seen','body_bytes_seen','supervised_tokens'):
        values=[[row[field] for row in rows] for rows in histories]
        checks[f'3_lr_same_{field}']=values[0]==values[1]==values[2]
    checks['lowest_fixed_dev_bpb_selected']=report['selected_lr']==min(report['lr_results'],key=lambda row:row['dev']['body']['bpb'])['lr']
    fields=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','spec','model_config','implementation_sha256','update')
    exact=run/'exact-selected'
    for stage,end,count in [('stable',400,400),('decay',300,100)]:
        states=[]
        for suffix in ('continuous','resumed'):
            directory=exact/f'{stage}-{suffix}'
            states.append(torch.load(directory/f'checkpoint-{end:08d}.pt',map_location='cpu',weights_only=False))
            rows=[json.loads(line) for line in (directory/'metrics.jsonl').read_text().splitlines()]
            checks[f'{stage}_{suffix}_all_updates']=len(rows)==count
            ledger.append({'path':str(directory/'metrics.jsonl'),'sha256':sha256(directory/'metrics.jsonl'),
                           'completed_updates':len(rows),'input_tokens':len(rows)*32768})
        for field in fields:
            checks[f'{stage}_{field}_independent_exact']=equal_state(states[0][field],states[1][field])
    cold=torch.load(run/'cold-resumed/checkpoint-00000400.pt',map_location='cpu',weights_only=False)
    continuous=torch.load(exact/'stable-continuous/checkpoint-00000400.pt',map_location='cpu',weights_only=False)
    for field in fields:checks['cold_'+field+'_independent_exact']=equal_state(continuous[field],cold[field])
    cold_rows=[json.loads(line) for line in (run/'cold-resumed/metrics.jsonl').read_text().splitlines()]
    checks['cold_only_200_new_updates']=len(cold_rows)==200 and cold_rows[0]['update']==201 and cold_rows[-1]['update']==400
    ledger.append({'path':str(run/'cold-resumed/metrics.jsonl'),'sha256':sha256(run/'cold-resumed/metrics.jsonl'),
                   'completed_updates':len(cold_rows),'input_tokens':len(cold_rows)*32768})
    full=read_json(run/'expanded_dev_baseline.json')
    body=full['body']
    checks['full_dev_exact_population']=body['documents']==len(body['rows'])==89416 and body['body_bytes']==164344743
    checks['full_dev_each_body_token_once']=sum(row['scored_body_tokens'] for row in body['rows'])==body['body_tokens']==42003934 and all(row['scored_body_tokens']==row['body_tokens'] for row in body['rows'])
    checks['full_dev_byte_denominator']=sum(row['body_bytes'] for row in body['rows'])==body['body_bytes']
    checks['full_dev_nll_bpb_recomputed']=sum(row['body_nll'] for row in body['rows'])==body['body_nll'] and body['bpb']==body['body_nll']/(math.log(2)*body['body_bytes'])
    checks['scalar_batched_predeclared_gate']=full['scalar_batched_gpu_agreement']['bpb_abs_difference']<=full['scalar_batched_gpu_agreement']['bpb_tolerance_frozen']==.001
    generation=read_json(run/'generation_diagnostics.json')
    checks['all_400_fixed_dev_generations']=generation['status']=='passed_diagnosis' and len(generation['generation']['outputs'])==400
    checks['evaluation_model_rng_mode_unchanged']=full['evaluation_state_isolated'] and generation['evaluation_state_isolated']
    checks['base_scaling_not_started']=not (ROOT/'reports/phase6/base-20261003/stable').exists()
    evidence={str(path):sha256(path) for path in (run/'readiness_stability_report.json',run/'expanded_dev_baseline.json',run/'generation_diagnostics.json',run/'cpu-precision/results.json')}
    total_updates=sum(row['completed_updates'] for row in ledger)
    checks['unique_bounded_ledger']=total_updates==7500 and sum(row['input_tokens'] for row in ledger)==245760000
    result={'status':'passed_bounded_gpu' if all(checks.values()) else 'failed',
        'scope':'Independent bounded GPU/evaluation audit. Does not pass the learned export numeric gate or declare readiness completion.',
        'checks':checks,'evidence':evidence,'selected_lr':report['selected_lr'],
        'ledger':ledger,'completed_updates':total_updates,'input_tokens':sum(row['input_tokens'] for row in ledger),
        'implementation':implementation_hashes(),'export_numeric_gate':'unresolved','completed_at':now()}
    write_json(output,result)
    print(json.dumps({'status':result['status'],'checks':len(checks),'failed':[key for key,value in checks.items() if not value]}),flush=True)
    assert all(checks.values()),checks


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();audit(args.run.resolve(),args.output.resolve())
