"""Freeze verified Base settings, then prepare or persist one explicit milestone.

Preparing commands is the default. --execute starts only the requested stage;
it never advances to the next milestone or decides whether quality is adequate.
"""
from pathlib import Path
import argparse
import json
import math
import os
import runpy
import shutil
import subprocess
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.training import implementation_hashes, source_snapshot
from phase6_performance import alive, identity

UV = ['uv', 'run', '--frozen', '--extra', 'hub', '--extra', 'data', '--extra', 'ml', '--extra', 'export']
TARGETS = {'500M':500_000_000, '1B':1_000_000_000, '2B':2_000_000_000, '5B':5_000_000_000, '10B':10_000_000_000}


def frozen_sources():
    return dict(implementation_hashes(), **{name:sha256(ROOT/name) for name in (
        'scripts/run_base.py','scripts/train.py','scripts/phase6_readiness.py',
        'src/jmicro/readiness.py','configs/phase6/readiness.json','src/jmicro/export.py',
        'scripts/verify_nonorm_export.py','src/jmicro/native_precision.py')})


def freeze(readiness, export, destination):
    ready = read_json(readiness/'readiness_stability_report.json')
    native = read_json(export/'nonorm_export_parity_report.json')
    full = read_json(readiness/'expanded_dev_baseline.json')
    generation = read_json(readiness/'generation_diagnostics.json')
    assert ready['status'] == native['status'] == full['status'] == 'passed'
    assert all(native['checks'].values()) and all(item['passed'] for item in native['comparisons'].values())
    assert all(ready['exact']['checks'].values()) and all(ready['cold_checks'].values())
    assert ready['binding']['implementation'] == implementation_hashes()
    assert full['body']['documents'] == 89416 and full['body']['body_bytes'] == 164344743
    assert generation['status'] == 'passed_diagnosis' and len(generation['generation']['outputs']) == 400
    assert len(ready['lr_results']) == 3
    selected = next(row for row in ready['lr_results'] if row['lr'] == ready['selected_lr'])
    assert selected['dev']['body']['bpb'] == min(row['dev']['body']['bpb'] for row in ready['lr_results'])
    for row in ready['lr_results']:
        assert row['stable']['finite'] and row['decay']['finite'] and row['parent_files_immutable']
        assert row['stable']['update'] == 2000 and row['decay']['update'] == 2100
    plan = ready['plan']
    model = read_json(ROOT/'reports/phase5/candidate_configs.json')['100m-no-qknorm']['model_config']
    model_path = ROOT/'reports/phase6/base_model.json'
    write_json(model_path, model)
    update_tokens = plan['context']*plan['batch']*plan['accumulation']
    milestones = {}
    for name, tokens in TARGETS.items():
        updates = math.ceil(tokens/update_tokens)
        decay = math.ceil(.05*updates)
        milestones[name] = {'requested_input_tokens':tokens, 'stable_updates':updates,
            'stable_input_tokens':updates*update_tokens, 'decay_updates':decay,
            'decay_input_tokens':decay*update_tokens, 'decay_end_update':updates+decay,
            'full_dev_documents':89416, 'generation_outputs':400}
    checkpoint_bytes = max(row['stable']['checkpoint_bytes'] for row in ready['lr_results'])
    throughput = selected['stable']['steady_tokens_per_second']
    # Retain every completed checkpoint. Bound storage before launch; no pruning.
    save_every = 1000
    checkpoint_count = math.ceil(milestones['10B']['stable_updates']/save_every)+len(milestones)
    checkpoint_count += sum(math.ceil(row['decay_updates']/save_every)+1 for row in milestones.values())
    config = {'version':1, 'phase':6, 'initialization':'new random weights, seed42; do not resume the Phase5 or readiness trajectory',
        'model':str(model_path.relative_to(ROOT)), 'model_sha256':sha256(model_path),
        'shards':plan['shards'], 'shard_manifest_sha256':plan['shard_manifest_sha256'],
        'tokenizer':plan['tokenizer'], 'tokenizer_sha256':plan['tokenizer_sha256'],
        'source_sha256':frozen_sources(), 'seed':plan['seed'], 'context':plan['context'],
        'batch':plan['batch'], 'accumulation':plan['accumulation'], 'input_tokens_per_update':update_tokens,
        'dtype':'bf16', 'parameter_dtype':'fp32', 'lr':ready['selected_lr'], 'weight_decay':plan['weight_decay'],
        'optimizer':{'name':'fused AdamW','betas':[.9,.95],'eps':1e-8,'gradient_clip':1.0},
        'warmup':200, 'scheduler':'wsd', 'schedule_updates':milestones['10B']['stable_updates'],
        'minimum_lr_ratio':.1, 'save_every':save_every, 'log_every':50,
        'memory_fraction':plan['memory_fraction'], 'variant':plan['variant'], 'milestones':milestones,
        'data_mixture':{'web':1.0}, 'unique_train_stream_tokens':756087912,
        'capacity':{'minimum_free_bytes':200*1024**3,'maximum_output_bytes':100*1024**3,
                    'checkpoint_retention':'all completed checkpoints, no automatic deletion',
                    'estimated_maximum_checkpoint_count':checkpoint_count,'measured_checkpoint_bytes':checkpoint_bytes,
                    'estimated_checkpoint_bytes':checkpoint_count*checkpoint_bytes},
        'evidence':{str(path):sha256(path) for path in (readiness/'readiness_stability_report.json',
            readiness/'expanded_dev_baseline.json',readiness/'generation_diagnostics.json',
            export/'nonorm_export_parity_report.json')},
        'measured_budget':{'steady_input_tokens_per_second':throughput,
            'full_dev_seconds':full['body']['seconds'],'400_generation_seconds':generation['generation_seconds'],
            'final_checkpoint_save_seconds':selected['stable']['save_seconds'],
            'observed_compile_first_update_seconds':selected['stable']['first_update_seconds'],
            'stable_training_seconds':milestones['10B']['stable_input_tokens']/throughput,
            'all_decay_training_seconds':sum(row['decay_input_tokens'] for row in milestones.values())/throughput,
            'all_full_dev_and_generation_seconds':len(milestones)*(full['body']['seconds']+generation['generation_seconds']),
            'estimate_limit':'Arithmetic estimate; compile, filesystem variability and training-dependent generation length remain separate'},
        'quality_targets_achieved':False, 'scaling_started':False, 'created_at':now()}
    assert config['capacity']['estimated_checkpoint_bytes'] < config['capacity']['maximum_output_bytes']
    if destination.exists():
        previous = read_json(destination)
        assert {key:value for key,value in previous.items() if key!='created_at'} == {key:value for key,value in config.items() if key!='created_at'}
        config = previous
    else:
        write_json(destination, config)
    # The repository requires a schema for every config JSON. Bind every value.
    relative = destination.resolve().relative_to(ROOT)
    write_json(ROOT/'schemas'/relative.with_suffix('.schema.json'), {
        '$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','additionalProperties':False,
        'required':list(config),'properties':{key:{'const':value} for key,value in config.items()}})
    launch = {'status':'frozen_not_started','config':str(destination),'config_sha256':sha256(destination),
        'milestones':{},'measured_budget':config['measured_budget'],'capacity':config['capacity'],
        'stop_boundary':'Settings freeze only. No 500M+ Base training is authorized by freezing.',
        'created_at':now()}
    for name in TARGETS:
        command = [*UV,'scripts/run_base.py','--config',str(relative),'--target',name,'--output','reports/phase6/base-20261003']
        launch['milestones'][name] = {'prepare':command,'stable_start_or_resume':[*command,'--operation','stable','--execute'],
            'decay_start_or_resume':[*command,'--operation','decay','--execute'],
            'full_dev_and_400_generation':[*command,'--operation','evaluate','--execute']}
    write_json(ROOT/'reports/phase6/base_launch_plan.json', launch)
    return launch


def validate_config(path):
    config = read_json(path)
    assert config['source_sha256'] == frozen_sources(), 'Frozen Base source changed'
    assert sha256(ROOT/config['model']) == config['model_sha256']
    assert sha256(ROOT/config['tokenizer']) == config['tokenizer_sha256']
    assert sha256(Path(config['shards'])/'manifest.json') == config['shard_manifest_sha256']
    for evidence, digest in config['evidence'].items():
        assert sha256(Path(evidence)) == digest
    return config


def prepare(config, target, output, operation):
    milestone = config['milestones'][target]
    stable = output/'stable'
    parent = stable/f"checkpoint-{milestone['stable_updates']:08d}.pt"
    run = stable if operation == 'stable' else output/f'decay-{target}'
    latest_path = run/'latest.json'
    resume = None
    if latest_path.exists():
        latest = read_json(latest_path)
        resume = Path(latest['path'])
        assert sha256(resume) == latest['sha256'], 'Resume checkpoint checksum differs'
    elif run.exists() and operation != 'evaluate':
        raise ValueError('Existing run without a valid checkpoint; preserve and inspect')
    if operation == 'evaluate':
        assert resume is not None and latest['update'] == milestone['decay_end_update']
        commands = []
        for kind, flag in [('full-dev','--full'),('generation','--diagnostics')]:
            commands.append(['scripts/phase6_readiness.py','--plan','configs/phase6/readiness.json',
                '--score-checkpoint',str(resume),'--result',str(output/f'evaluation-{target}'/f'{kind}.json'),flag])
        return {'operation':operation,'target':target,'commands':commands,'run':str(run),'checkpoint':str(resume)}
    end = milestone['stable_updates'] if operation == 'stable' else milestone['decay_end_update']
    schedule = config['schedule_updates'] if operation == 'stable' else end
    command = ['scripts/train.py','train','--model',config['model'],'--shards',config['shards'],
        '--output',str(run),'--phase','6','--device','cuda','--dtype',config['dtype'],'--scheduler','wsd',
        '--schedule-updates',str(schedule),'--stop-after',str(end),'--backend',config['variant']['backend'],
        '--compile','--compile-mode',config['variant']['compile_mode'],'--training-fast-path','--deterministic']
    for key in ('seed','context','batch','accumulation','lr','weight_decay','warmup','save_every','log_every'):
        command += ['--'+key.replace('_','-'),str(config[key])]
    if resume:
        command += ['--resume',str(resume)]
    elif operation == 'decay':
        assert parent.exists(), 'Stable observation checkpoint is required before decay'
        command += ['--branch-from',str(parent),'--decay-updates',str(milestone['decay_updates']),
                    '--minimum-lr-ratio',str(config['minimum_lr_ratio'])]
    complete = resume is not None and latest['update'] >= end
    return {'operation':operation,'target':target,'commands':[command],'run':str(run),
        'completed':complete,'end_update':end,'parent':str(parent) if operation=='decay' else None}


def execute(config_path, target, output, operation):
    import fcntl
    config = validate_config(config_path)
    output.mkdir(parents=True,exist_ok=True)
    with (output/'supervisor.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        record_path = output/'supervisor.json'
        if record_path.exists():
            previous = read_json(record_path)
            assert previous['config_sha256'] == sha256(config_path)
            assert not (previous.get('worker') and alive(previous['worker'])), 'Identified worker is still live'
        prepared = prepare(config,target,output,operation)
        if prepared.get('completed'):
            return dict(prepared,status='already_at_target')
        gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi','--query-compute-apps=pid','--format=csv,noheader'],capture_output=True,text=True,check=True)
        assert not gpu.stdout.strip(),'Existing GPU job; do not duplicate'
        assert shutil.disk_usage(output).free >= config['capacity']['minimum_free_bytes']
        if not (output/'source_sha256.json').exists():
            write_json(output/'source_sha256.json',source_snapshot(output/'snapshot'))
        record = {**identity(),'status':'running','started_at':now(),'config_sha256':sha256(config_path),
            'target':target,'operation':operation,'prepared':prepared,
            'restart_command':[*UV,'scripts/run_base.py','--config',str(config_path),'--target',target,
                '--output',str(output),'--operation',operation,'--execute']}
        parent_before = sha256(Path(prepared['parent'])) if prepared.get('parent') else None
        def allocated():
            return sum(path.stat().st_size for path in output.rglob('*') if path.is_file())
        try:
            for index,command in enumerate(prepared['commands']):
                request = output/f'{operation}-{target}-{index}.request.json'
                write_json(request,{'config':str(config_path),'command':command})
                log = output/f'{operation}-{target}-{index}.log'
                with log.open('a') as stream:
                    child = subprocess.Popen([sys.executable,str(Path(__file__)),'--worker-request',str(request)],stdout=stream,stderr=subprocess.STDOUT)
                    record.update(worker=identity(child.pid),log=str(log),heartbeat_at=now())
                    write_json(record_path,record)
                    while child.poll() is None:
                        time.sleep(5)
                        record['heartbeat_at']=now()
                        write_json(record_path,record)
                        if allocated() > config['capacity']['maximum_output_bytes'] or shutil.disk_usage(output).free < config['capacity']['minimum_free_bytes']:
                            child.terminate()
                            child.wait(timeout=60)
                            raise RuntimeError('Storage boundary reached; latest completed checkpoint retained')
                    assert child.returncode == 0,f'Worker failed; inspect {log}'
            if parent_before:
                assert sha256(Path(prepared['parent'])) == parent_before,'Decay changed stable parent'
            record.update(status='complete',completed_at=now(),worker=None,parent_checkpoint_immutable=bool(parent_before))
        except BaseException as error:
            record.update(status='failed',failure=f'{type(error).__name__}: {error}',completed_at=now())
            raise
        finally:
            write_json(record_path,record)
        return record


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--freeze-from',type=Path)
    parser.add_argument('--export',type=Path)
    parser.add_argument('--config',type=Path,default=ROOT/'configs/phase6/base_frozen.json')
    parser.add_argument('--output',type=Path,default=ROOT/'reports/phase6/base-20261003')
    parser.add_argument('--target',choices=list(TARGETS),default='500M')
    parser.add_argument('--operation',choices=['stable','decay','evaluate'],default='stable')
    parser.add_argument('--execute',action='store_true')
    parser.add_argument('--worker-request',type=Path)
    args=parser.parse_args()
    if args.worker_request:
        import torch
        request=read_json(args.worker_request)
        config=validate_config(Path(request['config']))
        torch.cuda.set_per_process_memory_fraction(config['memory_fraction'])
        sys.argv=request['command']
        runpy.run_path(str(ROOT/sys.argv[0]),run_name='__main__')
        return
    if args.freeze_from:
        if args.execute or not args.export:
            parser.error('Freeze requires --export and cannot execute training')
        result=freeze(args.freeze_from.resolve(),args.export.resolve(),args.config.resolve())
    elif args.execute:
        result=execute(args.config.resolve(),args.target,args.output.resolve(),args.operation)
    else:
        result=prepare(validate_config(args.config),args.target,args.output.resolve(),args.operation)
        result.update(status='prepared_not_started',uv_commands=[[*UV,*command] for command in result['commands']])
    print(json.dumps(result,ensure_ascii=False),flush=True)


if __name__=='__main__':
    main()
