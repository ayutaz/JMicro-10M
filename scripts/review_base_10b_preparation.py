"""Review step1 saved preparation evidence on CPU; never starts science training."""
import json
import math
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jsonschema import validate
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import equal_state
from jmicro.training import implementation_hashes, learning_rate_factor
from phase6_performance import alive, finite_state
from run_base_5b import test_counts
from run_base_10b import SOURCES, sanity, binding_for, require_prepared


def main():
    torch.set_num_threads(2)
    plan_path = ROOT / 'configs/phase6/base_10b.json'
    plan = read_json(plan_path)
    validate(plan,read_json(ROOT / 'schemas/configs/phase6/base_10b.schema.json'))
    sanity(plan)
    output = ROOT / plan['output']
    binding = binding_for(plan,plan_path)
    prepared = require_prepared(output,binding)
    job = read_json(output / 'preparation-job.json')
    gate = read_json(output / 'cuda-resume-gate.json')
    checks = {}
    def require(name,condition):
        checks[name] = bool(condition)
        assert condition,name
    require('actual_verification_process_complete_exited',job['status']=='complete' and not alive(job) and job['binding']==binding)
    require('science_training_not_started',prepared['scientific_training_input_tokens']==0 and
        not any((output/name).exists() for name in ('stable','decay','result.json','job.json')))
    require('frozen_sources_core',plan['implementation']==implementation_hashes() and
        plan['source_sha256']=={name:sha256(ROOT/name) for name in SOURCES})
    require('tests_no_failure_error_skip',test_counts(Path(plan['tests']['path']))==plan['tests']['counts'] and
        plan['tests']['counts']['tests']>=10 and sha256(Path(plan['tests']['path']))==plan['tests']['sha256'])
    require('train_manifest_tokenizer_unchanged',sha256(Path(plan['shards'])/'manifest.json')==plan['shard_manifest_sha256'] and
        sha256(ROOT/plan['tokenizer'])==plan['tokenizer_sha256'])
    for field in ('go_evidence','stable_parent_evidence'):
        require(field+'_bound',sha256(Path(plan[field]['path']))==plan[field]['sha256'])
    require('real_CUDA16_verification_tokens_separate',gate['passed'] and all(gate['checks'].values()) and
        gate['optimizer_updates']==prepared['verification_optimizer_updates']==16 and
        gate['input_tokens']==prepared['verification_input_tokens']==plan['verification_input_tokens']==524288)
    require('CUDA_budget',0<job['gpu_elapsed_seconds']<=plan['preparation_gpu_budget_seconds'])
    parent_path = Path(plan['parent']['path'])
    parent = torch.load(parent_path,map_location='cpu',weights_only=False)
    require('immutable_real_stable4_75B_parent',sha256(parent_path)==plan['parent']['sha256'] and
        parent['update']==144959 and parent['tokens']==4750016512 and parent['spec']==plan['parent']['spec'] and finite_state(parent))
    require('no_LR_jump_or_other_setting_change',all(g['lr']==.002 for g in parent['optimizer']['param_groups']) and
        {k:v for k,v in plan['spec'].items() if k!='schedule_updates'}==
        {k:v for k,v in parent['spec'].items() if k!='schedule_updates'})
    # The tied embedding/output tensor appears twice in state_dict, but is
    # one parameter. Count saved tensor identities, and verify the actual tie.
    weights = {t.data_ptr():t for t in parent['model'].values()}
    require('model10M_unchanged',sum(t.numel() for t in weights.values())==plan['parameters']==10001152 and
        parent['model']['lm_head.weight'].data_ptr()==parent['model']['model.embed_tokens.weight'].data_ptr() and
        parent['model_config']==plan['model_config'])
    require('data_cursor_epoch0_can_reach10B',parent['sampler']['epoch']==0 and
        parent['sampler']['position']==144959*32 and plan['end_update']*32<=parent['sampler']['blocks'])
    require('direct10B_exact_budget',plan['end_tokens']==10000007168 and plan['stable_end_tokens']==9500000256 and
        plan['additional_training_tokens']==5249990656 and plan['decay_updates']==15259)
    require('production_LR_curve_floor',learning_rate_factor(plan['spec'],plan['stable_end_update'])==1 and
        math.isclose(learning_rate_factor(dict(plan['spec'],scheduler='wsd_decay',branch_at=plan['stable_end_update'],
            schedule_updates=plan['end_update'],decay_updates=plan['decay_updates'],minimum_lr_ratio=.1),plan['end_update']),.1))
    for mode in ('stable-extension','decay'):
        directory = output / 'verification' / mode
        expected = torch.load(directory/'continuous/checkpoint.pt',map_location='cpu',weights_only=False)
        actual = torch.load(directory/'resumed/checkpoint.pt',map_location='cpu',weights_only=False)
        paused = torch.load(directory/'paused/checkpoint.pt',map_location='cpu',weights_only=False)
        require(mode+'_all_saved_state_exact',expected.keys()==actual.keys() and
            all(equal_state(expected[k],actual[k]) for k in expected) and finite_state(expected) and finite_state(actual))
        require(mode+'_completed_updates_tokens_saved',paused['update']==144961 and actual['update']==144963 and
            paused['tokens']==4750016512+65536 and actual['tokens']==4750016512+131072)
        require(mode+'_Adam_scheduler_RNG_sampler_counters',all(int(s['step'])==actual['update'] for s in actual['optimizer']['state'].values()) and
            actual['scheduler']['last_epoch']==actual['update'] and len(actual['rng']['cuda'])==1 and
            actual['sampler']['position']==parent['sampler']['position']+128 and actual['sampler']['epoch']==0 and
            actual['supervised_tokens']>parent['supervised_tokens'] and actual['body_bytes']>parent['body_bytes'])
        histories = gate['histories'][mode]
        require(mode+'_finite_forward_backward_and_matching_history',all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in
            histories['continuous']+histories['resumed']) and all(
            [r[k] for r in histories['continuous']]==[r[k] for r in histories['resumed']]
            for k in ('loss','lr','token_digest','tokens_seen')))
        if mode=='stable-extension':
            require('stable_extension_lineage_from_correct_parent',actual['lineage']['parent_sha256']==plan['parent']['sha256'] and
                actual['lineage']['parent_tokens']==4750016512 and actual['lineage']['new_schedule_updates']==289917)
        else:
            require('verification4_update_decay_is_not_production15259',actual['spec']['decay_updates']==4 and
                all(math.isclose(g['lr'],.0002) for g in actual['optimizer']['param_groups']))
        del expected,actual,paused
    env = read_json(output/'environment.json')
    require('uv_pinned_Python_WSL4090_BF16',env['python'].startswith('3.12.7') and '/.venv/' in env['executable'] and
        '4090' in env['device'] and 'Linux' in env['platform'] and env['mode']=='verify-only' and parent['spec']['dtype']=='bf16')
    review = dict(status='completed_step1_ready_before_scientific10B',completed_at=now(),checks=checks,binding=binding,
        parent=plan['parent'],tests=plan['tests']['counts'],scientific_training_input_tokens=0,
        verification_optimizer_updates=16,verification_input_tokens=524288,
        preparation_gpu_elapsed_seconds=job['gpu_elapsed_seconds'],planned_scientific_additional_tokens=5249990656,
        planned_total_training_tokens=10000007168,quality_targets_achieved=False,evaluation_started=False,
        explicit_future_training_command=plan['restart_command'],
        preparation_sha256=sha256(output/'preparation.json'),cuda_gate_sha256=sha256(output/'cuda-resume-gate.json'),
        preparation_job_sha256=sha256(output/'preparation-job.json'),stop_boundary=plan['preparation_stop_boundary'])
    write_json(ROOT/'reports/phase6/base_10b_preparation_review.json',review)
    print(json.dumps(dict(status=review['status'],checks=checks,tests=review['tests'],GPU_seconds=job['gpu_elapsed_seconds'])))


if __name__ == '__main__':
    main()
