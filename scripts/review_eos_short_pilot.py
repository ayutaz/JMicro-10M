"""Audit actual completed pilot artifacts and produce its compact result; use uv."""
import json
import math
from pathlib import Path
import statistics
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from phase6_performance import alive


def main():
    torch.set_num_threads(2)
    plan_path=ROOT/'configs/phase6/eos_short_pilot.json'
    plan=read_json(plan_path)
    run=ROOT/plan['output']
    raw=read_json(run/'review.json')
    job=read_json(run/'job.json')
    checks={}
    def require(name,value):
        checks[name]=bool(value)
        if not value:
            raise AssertionError(name)
    require('terminal_job_not_live',job['status']=='complete' and not alive(job))
    require('frozen_plan',raw['plan']==plan and raw['binding']['plan_sha256']==sha256(plan_path))
    require('training_source_unchanged',raw['binding']['implementation']==implementation_hashes())
    require('pilot_module_unchanged',raw['binding']['module_sha256']==sha256(ROOT/'src/jmicro/eos_pilot.py'))
    require('runner_unchanged',raw['binding']['runner_sha256']==sha256(ROOT/'scripts/run_eos_short_pilot.py'))
    require('parent2B_checkpoint_unchanged',sha256(Path(plan['parent']['path']))==plan['parent']['sha256'])
    require('GPU_budget_including_retired_attempt',job['gpu_elapsed_seconds']<=plan['gpu_budget_seconds'])
    gate=read_json(run/'resume-gate.json')
    require('real_CUDA_mixed_resume_all_fields',gate['passed'] and all(gate['checks'].values()) and gate['GPU_optimizer_updates']==8)
    baseline=read_json(run/'generation-baseline-check.json')
    require('original8_generated_IDs_reproduced',baseline['passed'] and len(baseline['checks'])==8 and all(baseline['checks'].values()))
    counts={k:0 for k in ('tests','failures','errors','skipped')}
    for suite in ET.parse(run/'tests.xml').getroot().iter('testsuite'):
        for key in counts:
            counts[key]+=int(suite.attrib.get(key,0))
    require('five_relevant_unit_tests',counts=={'tests':5,'failures':0,'errors':0,'skipped':0})
    tok=Tokenizer(ROOT/plan['tokenizer'])
    evaluations={}
    arms={}
    for arm in ('web','short20'):
        record=read_json(run/arm/'result.json')
        path=Path(record['checkpoint'])
        require(f'{arm}_checkpoint_hash',sha256(path)==record['checkpoint_sha256'])
        state=torch.load(path,map_location='cpu',weights_only=False)
        required=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes',
                  'token_digest','spec','model_config','implementation_sha256','update','lineage','pilot_binding')
        require(f'{arm}_resume_fields',all(key in state for key in required))
        require(f'{arm}_763_updates_25M',state['update']==61799 and state['tokens']==2025029632 and
                record['additional_input_tokens']==25001984 and state['sampler']['position']==763)
        require(f'{arm}_source_accounting',state['sampler']['source_tokens']==record['source_tokens'] and
                sum(record['source_tokens'].values())==25001984 and
                record['source_tokens']['short']==(5013504 if arm=='short20' else 0))
        require(f'{arm}_same_parent_and_schedule',state['lineage']['parent_tokens']==2000027648 and
                state['lineage']['parent_update']==61036 and state['pilot_binding']['parent']==plan['parent'] and
                state['spec']['pilot_schedule']=={'parent_update':61036,'stable_updates':725,'decay_updates':38})
        require(f'{arm}_optimizer_scheduler_RNG',len(state['optimizer']['state'])>0 and
                state['scheduler']['last_epoch']==61799 and len(state['rng']['cuda'])==1)
        tensors=[*state['model'].values(),*[v for r in state['optimizer']['state'].values() for v in r.values() if isinstance(v,torch.Tensor)]]
        require(f'{arm}_saved_tensors_finite',all(bool(torch.isfinite(v).all()) for v in tensors))
        history_path=(Path(record['reused_control']['source_result']).parent if 'reused_control' in record else run/arm)/'metrics.jsonl'
        history=[json.loads(line) for line in history_path.read_text().splitlines()]
        require(f'{arm}_all_completed_updates',len(history)==763 and [r['update'] for r in history]==list(range(61037,61800)))
        require(f'{arm}_finite_training',all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        evaluation=read_json(run/f'{arm}-evaluation.json')
        require(f'{arm}_evaluation_checkpoint',evaluation['checkpoint_sha256']==record['checkpoint_sha256'])
        require(f'{arm}_256_dev_body_coverage',evaluation['body']['documents']==256 and
                all(r['body_tokens']==r['scored_body_tokens'] for r in evaluation['body']['rows']))
        rows=evaluation['generation']['outputs']
        require(f'{arm}_80_original_greedy64',len(rows)==80 and evaluation['generation']['max_new_tokens']==64 and
                evaluation['generation']['suite_sha256']==plan['suite_sha256'] and
                all(r['split']=='dev' and r['decoding']=='greedy' and r['suppressed'] for r in rows))
        require(f'{arm}_natural_stop_IDs',all((r['stop_reason']=='stop_id')==(r['generated_ids'][-1]==3) and len(r['generated_ids'])<=64 for r in rows))
        # Metadata is re-decoded, without another model forward or full corpus pass.
        for row in rows:
            data=tok.decode_bytes(row['generated_ids'])
            try:
                text=data.decode('utf-8');valid=True
            except UnicodeDecodeError:
                text=data.decode('utf-8',errors='replace');valid=False
            require(f'{arm}_decoded_{row["id"]}',text==row['text'] and valid==row['valid_utf8'])
        warm=[r['tokens_per_second'] for r in history[24:725]]
        arms[arm]={'checkpoint':{'path':str(path),'sha256':record['checkpoint_sha256']},
            'additional_input_tokens':25001984,'final_cumulative_input_tokens':state['tokens'],
            'training_seconds':record['training_seconds'],'steady_median_tokens_per_second':statistics.median(warm),
            'source_tokens':record['source_tokens'],'source_eos_teachers':record['source_eos_teachers'],
            'dev256_bpb':evaluation['body']['bpb'],
            'mean_dev256_eos_nll':evaluation['body']['eos_nll']/256,
            'greedy64':evaluation['greedy_rates'],'reused_completed_control':'reused_control' in record}
        evaluations[arm]=evaluation
        del state,tensors
    require('same_256_documents_and_bytes',[r['doc_id'] for r in evaluations['web']['body']['rows']]==[r['doc_id'] for r in evaluations['short20']['body']['rows']] and
            evaluations['web']['body']['body_bytes']==evaluations['short20']['body']['body_bytes'])
    require('same80_prompt_IDs',[r['id'] for r in evaluations['web']['generation']['outputs']]==[r['id'] for r in evaluations['short20']['generation']['outputs']])
    require('scientific50M_and_verification_separate',raw['scientific_training_input_tokens']==50003968 and raw['verification_training_input_tokens']==524288)
    require('conditional_full_evaluation',raw['candidate_full_evaluation_performed']==all(raw['improvement_checks'][k] for k in
            ('EOS_at_least8_more','repetition_no_worse','no_empty_role_unicode','BPB_degradation_at_most1percent')))
    if raw['candidate_full_evaluation_performed']:
        full=read_json(run/'candidate-full-evaluation.json')
        require('full_89416_dev_400_outputs',full['body']['documents']==89416 and full['body']['body_bytes']==164344743 and len(full['generation']['outputs'])==400)
    pool=read_json(Path(plan['short_pool'])/'ready.json')
    index=read_json(Path(plan['short_pool'])/'train.index.json')
    require('short_pool_train_only_complete_bounds',pool['heldout_used'] is False and len(index)==pool['documents'] and
            all(r['split']=='train' and 32<=r['body_tokens']<=128 and r['source_end']-r['source_start']-1==r['body_tokens'] for r in index))
    selected_lengths=[r['body_tokens'] for r in index]
    relative=(arms['short20']['dev256_bpb']/arms['web']['dev256_bpb']-1)*100
    report={'status':'completed_verified_two_arm_EOS_comparison','completed_at':now(),'plan':str(plan_path),
        'parent':plan['parent'],'model_parameters':10000152,
        'scientific_training_input_tokens':50003968,'verification_training_input_tokens':524288,
        'actual_GPU_seconds_including_retired_attempt':job['gpu_elapsed_seconds'],'arms':arms,
        'common_dev_documents':256,'common_dev_body_bytes':evaluations['web']['body']['body_bytes'],
        'short_vs_control_BPB_change_percent':relative,'improvement_checks':raw['improvement_checks'],
        'improvement_gate_passed':raw['improvement_gate_passed'],'decision':raw['decision'],
        'short_pool':{'documents':pool['documents'],'input_tokens':pool['tokens'],'extraction_seconds':pool['seconds'],
            'body_tokens_mean':pool['body_tokens_mean'],'body_tokens_at_most64':sum(n<=64 for n in selected_lengths),
            'body_tokens_median':statistics.median(selected_lengths),'selection':plan['short_selection']},
        'test_split_used':False,'quality_targets_achieved':False,
        'candidate_full_evaluation':raw['candidate_full_evaluation'],
        'next_action_proposal_not_started':{'hypothesis':'The short pool median is107 body tokens and only712/47844 documents are at most64 tokens; length alignment for the64-token stopping target remains weak, but this is not proof of the cause.',
            'data':'Prepare a sufficiently varied32-64-token set of complete Japanese training units from train only. Define sentence/paragraph units explicitly, preserve source membership and complete sentence boundaries; do not cycle the tiny712-document subset or attach EOS to arbitrary token cuts.',
            'comparison':'Reuse the verified Web control if parent/schedule/core source remain identical; run one new25M treatment fork with the same20percent input mixture and fixed80 greedy/256-dev measurements, after freezing data and budget. No automatic sweep or5B growth.',
            'improvement_gate':'Keep EOS+8/80 versus control, repetition non-worsening, no empty/role/Unicode failures, BPB<=1percent worse; original Base/Chat goals unchanged.',
            'status':'proposed_not_started'},
        'completion_checks_passed':all(checks.values()),'completion_checks':checks,'tests':counts,
        'reviewer_source_sha256':sha256(Path(__file__)),
        'raw_run':str(run),'raw_evidence':{name:{'path':str(run/name),'sha256':sha256(run/name)} for name in
            ('job.json','review.json','resume-gate.json','generation-baseline-check.json','web-evaluation.json','short20-evaluation.json','tests.xml','pipeline.log')},
        'limits':['Single seed,25M-per-arm and20.0524percent short mixture only; neither a successful result nor failure generalizes to all short-data schedules.',
            '256 dev BPB is comparable between these arms; it is not the full89416-dev BPB0.982882.',
            'Pool documents are original train documents with punctuation and ellipsis/read-more filters; semantic completeness is not certified by blind human review.',
            'The initial Web control checkpoint was retained after pre-treatment content refinement and strictly reused without another25M training pass.',
            'No full corpus re-audit, EOS forcing/bias/penalty, test scoring,5B scaling or Chat training was performed.']}
    write_json(ROOT/'reports/phase6/eos_short_pilot_review.json',report)
    print(json.dumps({k:report[k] for k in ('status','arms','short_vs_control_BPB_change_percent','improvement_gate_passed','actual_GPU_seconds_including_retired_attempt','short_pool')},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
