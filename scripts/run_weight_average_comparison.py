"""Prepare one model-only midpoint and durably evaluate it without training."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json, gpu_lock, rng_state, restore_rng
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import alive, identity
from run_eos_short_pilot import equal_state
from weight_average_checkpoint import midpoint, KIND, TIED
import run_complete_text_comparison as evaluation
import run_source_order_condition_comparison_v2 as cached
import run_condition_source_ranking as ranking

CONFIG = ROOT / 'configs/phase6/weight_average_comparison.json'
RUN = ROOT / 'reports/phase6/weight-average-comparison-20261006'
ARM = 'midpoint50'


def check_reference(record):
    if sha256(Path(record['path'])) != record['sha256']:
        raise ValueError('Frozen reference differs: ' + record['path'])


def contract():
    c = read_json(CONFIG)
    if (c['kind'] != 'same_parent_fixed_half_weight_midpoint_research' or c['coefficients'] != [.5,.5]
            or c['new_scientific_teacher_tokens'] or c['new_optimizer_updates']
            or c['evaluation_GPU_ceiling_seconds'] != 300 or c['parameter_count'] != 10001152
            or c['strong_quality_control'] != 'source_order' or not c['quality_criteria_unchanged']
            or c['protected_test_used'] or c['Base_complete'] or c['Base_adopted']
            or c['Chat_started'] or c['quantization_started']):
        raise ValueError('Single preregistered midpoint scope differs')
    for path, digest in c['source_sha256'].items():
        if sha256(ROOT / path) != digest:
            raise ValueError('Frozen implementation differs: ' + path)
    for record in (*c['refs'].values(), *c['evaluation_refs']):
        check_reference(record)
    job = read_json(cached.RUN / 'job.json')
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Named endpoint science must have actually finished')
    own = RUN / 'job.json'
    if own.exists() and alive(read_json(own)):
        raise ValueError('Existing live midpoint job; do not duplicate')
    base = read_json(Path(c['evaluation_base_config']))
    if (sha256(ROOT/base['tokenizer']) != base['tokenizer_sha256']
            or sha256(Path(base['dev_shards'])/'manifest.json') != base['dev_manifest_sha256']):
        raise ValueError('Pinned tokenizer/dev differs')
    return c, base


def prepare():
    c, _ = contract(); RUN.mkdir(parents=True, exist_ok=True)
    destination = RUN / 'preparation.json'
    if destination.exists():
        record=read_json(destination); check_reference(record['checkpoint'])
        if record['config_sha256'] != sha256(CONFIG):
            raise ValueError('Existing preparation identity differs')
        print('Completed original midpoint preparation retained'); return
    job_path = RUN / 'preparation-job.json'
    if job_path.exists():
        raise ValueError('Preserve prior failed/partial preparation; no automatic midpoint overwrite')
    job=dict(status='preparing', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
        CPU_ceiling_seconds=60, GPU_seconds=0, scientific_teacher_tokens=0)
    atomic_json(job_path,job); started=time.monotonic()
    try:
        torch.set_num_threads(2); states=[]; references=[]
        for arm in ('control','source_order'):
            detail=c['checkpoints'][arm]
            ref=dict(path=detail['checkpoint'],sha256=detail['checkpoint_sha256'])
            check_reference(ref)
            state=torch.load(ref['path'],map_location='cpu',weights_only=False)
            if (state['lineage']['parent'] != c['common_parent']
                    or state['supervised_tokens']-state['lineage']['parent_supervised_tokens'] != 100000000
                    or state['sampler']['source_teachers'] != detail['source_teachers']):
                raise ValueError('Actual endpoint parent/teacher accounting differs')
            states.append(state); references.append(ref)
        merged=midpoint(*states,references)
        model=JMicroModel(merged['model_config']); model.load_state_dict(merged['model'],strict=True)
        if sum(p.numel() for p in model.parameters()) != c['parameter_count']:
            raise ValueError('Pinned10M architecture changed')
        path=RUN/'midpoint50-model-only.pt'
        if path.exists():
            raise ValueError('Preserve prior midpoint bytes')
        temporary=RUN/'midpoint50-model-only.pt.tmp'; torch.save(merged,temporary); temporary.replace(path)
        elapsed=time.monotonic()-started
        if elapsed>60:
            raise TimeoutError('CPU preparation exceeded60s; preserve failed cost')
        atomic_json(destination,dict(status='single_model_only_midpoint_complete_not_evaluated',
            config_sha256=sha256(CONFIG), checkpoint=dict(path=str(path),sha256=sha256(path)),
            input_checkpoints=references, parameter_count=c['parameter_count'], arithmetic=c['arithmetic'],
            input_checkpoints_verified_unchanged=True, model_keys=len(merged['model']),
            tied_embedding_identical=True, resumable_training_state=False,
            optimizer_scheduler_RNG_sampler_not_averaged=True, new_scientific_teacher_tokens=0,
            optimizer_updates=0, CPU_seconds=elapsed, GPU_seconds=0, protected_test_used=False))
        job.update(status='complete',CPU_seconds=elapsed,completed_at=now())
        atomic_json(job_path,job)
        print(json.dumps(dict(status='midpoint50_prepared',CPU_seconds=elapsed,parameters=c['parameter_count'],GPU_seconds=0)))
    except BaseException as error:
        job.update(status='failed_preserve_partial',error=repr(error),CPU_seconds=time.monotonic()-started)
        atomic_json(job_path,job); raise


def transfer(c, checkpoint, heartbeat, check, suite):
    key='source_cases' if suite=='bridge' else 'retention_cases'
    reference=c['refs'][key]; prepared=read_json(Path(reference['path']))
    folder=RUN/'transfer'/suite; terminal=folder/'result.json'
    binding=dict(config_sha256=sha256(CONFIG),checkpoint_sha256=checkpoint['sha256'],cases_sha256=reference['sha256'])
    if terminal.exists():
        saved=read_json(terminal)
        if saved['binding'] != binding:
            raise ValueError('Transfer terminal binding differs')
        return saved
    folder.mkdir(parents=True,exist_ok=True)
    state=torch.load(checkpoint['path'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).to('cuda').eval(); model.load_state_dict(state['model'],strict=True)
    before_rng=rng_state(); before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
    scorer=NativeLikelihood(model,None,'cuda','bf16',16); rows=[]
    hook=model.register_forward_pre_hook(lambda *_:check())
    try:
        with sdpa_kernel(SDPBackend.MATH):
            for start in range(0,512,16):
                check(); cases=prepared['cases'][start:start+16]; path=folder/f'{start:04d}.json'
                if path.exists():
                    saved=read_json(path)
                    if saved['binding'] != binding:
                        raise ValueError('Saved transfer binding differs')
                    scored=saved['rows']
                else:
                    scored=[dict(index=case['index'],**r) for case,r in zip(cases,scorer.score_encoded(cases),strict=True)]
                    atomic_json(path,dict(binding=binding,rows=scored))
                ranking.validate_scores(scored,cases); rows.extend(scored)
                heartbeat(suite,completed_requests=len(rows),total_requests=512)
        checks=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),
            no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training)
    finally:
        hook.remove();restore_rng(before_rng)
    checks['RNG_restored']=equal_state(before_rng,rng_state())
    if not all(checks.values()):
        raise ValueError('Read-only transfer changed model/RNG')
    result=dict(binding=binding,checks=checks,summary=cached.summarize_transfer(rows,prepared),
        evaluated_requests=512,optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False)
    atomic_json(terminal,result)
    del state,model,before,scorer;gc.collect();torch.cuda.empty_cache()
    return result


def run():
    c,base=contract(); preparation=read_json(RUN/'preparation.json'); check_reference(preparation['checkpoint'])
    if preparation['config_sha256'] != sha256(CONFIG):
        raise ValueError('Prepared midpoint/config mismatch')
    jp=RUN/'job.json'; old=read_json(jp) if jp.exists() else {}
    if old.get('status')=='complete':
        print('Completed midpoint evaluation retained'); return
    if old and old['config_sha256'] != sha256(CONFIG):
        raise ValueError('Interrupted job config differs')
    previous=old.get('GPU_elapsed_seconds',0.); start=[None]; stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),
        GPU_elapsed_seconds=previous,scientific_teacher_tokens=0,optimizer_updates=0,protected_test_used=False,
        restart_command='scripts/run_weight_average_comparison.ps1 -Worker')
    for sig in (signal.SIGTERM,signal.SIGINT):
        signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:
            raise InterruptedError('Evaluation interrupted; saved complete sections retained')
        if start[0] is not None and previous+time.monotonic()-start[0]>300:
            raise TimeoutError('Cumulative midpoint evaluation300s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if start[0] is not None:job['GPU_elapsed_seconds']=previous+time.monotonic()-start[0]
        atomic_json(jp,job)
    checkpoint=preparation['checkpoint']
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        source=RUN/'source'
        for relative in (*c['source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=source/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():
                raise ValueError('Source snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        with gpu_lock('cuda'):
            start[0]=time.monotonic();heartbeat('CUDA-read-only-finite')
            state=torch.load(checkpoint['path'],map_location='cpu',weights_only=False)
            if state['kind'] != KIND or state['resumable_training_state']:
                raise ValueError('Model-only midpoint state required')
            model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
            before_rng=rng_state();before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
            with torch.inference_mode(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',dtype=torch.bfloat16):
                output=model(torch.tensor([[2,8,9,10,3]],device='cuda'))
            finite=bool(torch.isfinite(output.logits).all())
            gate=dict(finite_CUDA_BF16_forward=finite,actual_learned_midpoint=True,optimizer_updates=0,
                weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),
                no_gradients=all(p.grad is None for p in model.parameters()),RNG_unchanged=equal_state(before_rng,rng_state()))
            if not all(gate[k] for k in ('finite_CUDA_BF16_forward','weights_unchanged','no_gradients','RNG_unchanged')):
                raise ValueError('Actual read-only CUDA finite gate failed')
            atomic_json(RUN/'CUDA-read-only-gate.json',gate)
            del model,state,before,output;gc.collect();torch.cuda.empty_cache()
            evaluation.RUN=RUN/'evaluation'
            binding=dict(config_sha256=sha256(CONFIG),preparation_sha256=sha256(RUN/'preparation.json'),
                checkpoint_sha256=checkpoint['sha256'],policy='fixed50percent_model_only_no_new_learning')
            detail=dict(checkpoint=checkpoint['path'],checkpoint_sha256=checkpoint['sha256'])
            result=evaluation.evaluate(ARM,detail,Shard(Path(base['dev_shards']),'dev'),Tokenizer(ROOT/base['tokenizer']),
                base,binding,heartbeat,check,start[0]+300-previous)
            transfers={name:transfer(c,checkpoint,heartbeat,check,name) for name in ('bridge','retention')}
            check();atomic_json(RUN/'result.json',dict(status='all_GPU_evaluations_complete_pending80_content',
                config_sha256=sha256(CONFIG),checkpoint=checkpoint,evaluation=result,transfer=transfers,
                preparation_sha256=sha256(RUN/'preparation.json'),gate=gate,
                GPU_seconds=previous+time.monotonic()-start[0],new_scientific_teacher_tokens=0,
                optimizer_updates=0,protected_test_used=False,Base_complete=False,Base_adopted=False))
        job.update(status='complete',completed_at=now(),GPU_elapsed_seconds=previous+time.monotonic()-start[0])
        atomic_json(jp,job)
        print(json.dumps(dict(status=job['status'],GPU_seconds=job['GPU_elapsed_seconds'],science_tokens=0)))
    except BaseException as error:
        job.update(status='failed_or_interrupted',error=repr(error),ended_at=now(),
            GPU_elapsed_seconds=previous+(time.monotonic()-start[0] if start[0] is not None else 0))
        atomic_json(jp,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();parser.add_argument('--prepare',action='store_true');parser.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:
        c,_=contract();p=read_json(RUN/'preparation.json');check_reference(p['checkpoint'])
        print(json.dumps(dict(status='preflight_complete',parameters=p['parameter_count'],coefficients=c['coefficients'],GPU_ceiling=300)))
    else:run()
