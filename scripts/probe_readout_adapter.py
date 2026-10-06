"""Own CUDA identity/cache/frozen-state/resume/32timing within120s; no science."""
import argparse
import copy
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,implementation_hashes,rng_state
from jmicro.model import JMicroModel
from jmicro.eos_pilot import TrainView
from cached_three_source_index import CachedThreeSourceIndex
from condition_relation_language import RelationLanguageTrainView
from readout_adapter_model import ReadoutAdapterModel,POLICY
from readout_adapter_trainer import ReadoutAdapterTrainer,KIND,READOUT_LR
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
from probe_gated_shared_comparison import compare,estimate_training
import run_parameter_displacement_anchor_v3 as native

PROPOSAL=ROOT/'reports/phase6/readout_adapter_proposal.json'
RUN=ROOT/'reports/phase6/readout-adapter-comparison-v2-20261006'
CONFIG=ROOT/'configs/phase6/readout_adapter_probe_v2.json'
FAILED_RUN=ROOT/'reports/phase6/readout-adapter-comparison-20261006/probe'
SOURCES=('scripts/readout_adapter_model.py','scripts/readout_adapter_trainer.py','scripts/define_readout_adapter_comparison.py',
    'scripts/probe_readout_adapter.py','scripts/probe_readout_adapter.ps1','tests/test_readout_adapter.py',
    'tests/test_readout_probe_import.py')
reference,check_reference=native.reference,native.check_reference
TRACKED=('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes',
    'token_digest','focus_token_digest','focus_teacher_tokens','weighted_teacher_mass','update','spec','model_config','pilot_binding','study_binding')


def prepare():
    if CONFIG.exists():inspect();return
    start=time.monotonic();p=read_json(PROPOSAL);old=native.inspect(native.CONFIG)
    if (p['kind']!=KIND or p['policy']!=POLICY or p['parent']!=old['parent'] or p['readout_LR']!=READOUT_LR
            or p['unique_parameters']!=10099456 or p['new_parameters']!=98304
            or p['ordinary_source_CE_teacher_tokens']!=100000000 or p['own_CUDA_probe_ceiling_seconds']!=120
            or p['total_new_GPU_ceiling_seconds']!=900 or any(p[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Fixed nonlinear readout proposal required')
    failure=read_json(FAILED_RUN/'job.json')
    if alive(failure) or failure['status']!='failed_or_interrupted' or failure['error']!="RuntimeError('No CUDA GPUs are available')":
        raise ValueError('Preserved actual import-side-effect failure required')
    refs=dict(p['references'],proposal=reference(PROPOSAL),memory=reference(ROOT/'reports/phase6/finite-Web-constraint-20261006/memory.pt'),
        original_failure=reference(FAILED_RUN/'job.json'),import_regression_tests=reference(ROOT/'reports/phase6/readout_probe_import_tests.xml'))
    c=dict(kind=KIND,phase='architecture_probe',policy=POLICY,parent=old['parent'],readout_LR=READOUT_LR,
        source=old,references=refs,implementation=implementation_hashes(),source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        old_source_sha256={**old['old_source_sha256'],**old['source_sha256'],
            'scripts/probe_gated_shared_comparison.py':sha256(ROOT/'scripts/probe_gated_shared_comparison.py')},
        unique_parameters=10099456,new_parameters=98304,logical_layers=13,GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=900,
        previous_failed_GPU_seconds=failure['GPU_elapsed_seconds'],
        repair='Replace CPU preparation-module import with its unchanged proposal path; no recipe change. Preserve original config/source/failure.',
        numerical_tolerances=dict(identity_FP32_absolute=2e-6,identity_FP32_relative=2e-6,identity_BF16_absolute=0.,identity_BF16_relative=0.,
            nonzero_cache_FP32_absolute=2e-5,nonzero_cache_FP32_relative=2e-4),
        CPU_preparation_seconds=time.monotonic()-start,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    if c['CPU_preparation_seconds']>30:raise TimeoutError('CPU probe preparation30s exhausted')
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='readout_probe_frozen',GPU_seconds=0,CPU_seconds=c['CPU_preparation_seconds'])))


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!=KIND or c['phase']!='architecture_probe' or c['policy']!=POLICY or c['readout_LR']!=READOUT_LR
            or c['unique_parameters']!=10099456 or c['new_parameters']!=98304 or c['logical_layers']!=13
            or c['GPU_budget_seconds']!=120 or c['total_new_GPU_ceiling_seconds']!=900 or c['implementation']!=implementation_hashes()
            or c['previous_failed_GPU_seconds']!=read_json(FAILED_RUN/'job.json')['GPU_elapsed_seconds']
            or any(c[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Frozen readout probe scope differs')
    for name,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'],*c['references'].values()):check_reference(ref)
    if (RUN/'probe/job.json').exists() and alive(read_json(RUN/'probe/job.json')):raise ValueError('Actual live probe; no duplicate')
    return c


def native_unchanged(model,parent):
    return all(not p.requires_grad and p.grad is None and torch.equal(p.detach().cpu(),parent['model'][k])
        for k,p in model.named_parameters() if k not in ('lm_head.down','lm_head.up'))


def architecture(parent,memory,c,check):
    original=JMicroModel(parent['model_config']).to('cuda').eval();original.load_state_dict(parent['model'])
    before=rng_state();model=ReadoutAdapterModel.from_native(original);x=memory['inputs'][:1].to('cuda');checks={};tol=c['numerical_tolerances']
    for dtype in (torch.float32,torch.bfloat16):
        for n in (32,1024):
            check();label='FP32' if dtype==torch.float32 else 'BF16'
            with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast(device_type='cuda',dtype=torch.bfloat16,enabled=dtype!=torch.float32):
                a=original(x[:,:n]).logits;b=model(x[:,:n]).logits
            checks[label+'_'+str(n)]=compare(a,b,tol['identity_'+label+'_absolute'],tol['identity_'+label+'_relative'])
            del a,b
    with torch.no_grad():model.lm_head.up.fill_(.01)
    with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast(device_type='cuda',enabled=False):
        check();full=model(x).logits;first=model(x[:,:1008],use_cache=True);chunk=model(x[:,1008:],cache=first.cache,use_cache=True)
        checks['nonzero_cache1024']=compare(full[:,1008:],chunk.logits,tol['nonzero_cache_FP32_absolute'],tol['nonzero_cache_FP32_relative'])
        if len(chunk.cache.layers)!=13:raise ValueError('Native13 caches required')
    if not native_unchanged(model,parent) or not equal_state(before,rng_state()):raise ValueError('Diagnostic changed native weights/RNG')
    result=dict(checks=checks,native_weights_frozen_unchanged=True,RNG_unchanged=True,diagnostic_forward_calls=11,
        diagnostic_forward_context_positions=6272,optimizer_updates=0,diagnostic_up_values_discarded=True)
    del full,first,chunk,model,original;gc.collect();torch.cuda.empty_cache();return result


def resume_gate(build,folder,c,check,parent):
    folder.mkdir(parents=True,exist_ok=True);states=[];histories=[];teachers=0
    for route in ('continuous','resumed'):
        trainer=build();before=trainer.supervised_tokens;history=[]
        for i in range(4):
            check();history.append(trainer.step())
            if route=='resumed' and i==1:
                trainer.save(folder/'split.pt');del trainer;gc.collect();torch.cuda.empty_cache()
                trainer=build();trainer.load(folder/'split.pt')
        if not native_unchanged(trainer.model,parent):raise ValueError('Training modified frozen native parameters')
        teachers+=trainer.supervised_tokens-before;path=folder/(route+'.pt');trainer.save(path)
        states.append(torch.load(path,map_location='cpu',weights_only=False));histories.append(history)
        del trainer;gc.collect();torch.cuda.empty_cache()
    checks={k:equal_state(states[0][k],states[1][k]) for k in TRACKED}
    for k in histories[0][0]:
        if k not in ('seconds','data_wait_seconds','tokens_per_second'):
            checks['history_'+k]=all(equal_state(a[k],b[k]) for a,b in zip(*histories,strict=True))
    checks.update(finite=all(finite_state(s) for s in states),fixed_fresh_readout_LR=all(v['lr']==READOUT_LR for h in histories for v in h))
    if not all(checks.values()):raise ValueError('Own fullstate/history/frozen readout CUDA resume differs: '+repr(checks))
    result=dict(passed=True,checks=checks,histories=histories,config_sha256=sha256(CONFIG),GPU_optimizer_updates=8,verification_teacher_tokens=teachers)
    atomic_json(folder/'result.json',result);return result


def run():
    c=inspect();folder=RUN/'probe';folder.mkdir(parents=True,exist_ok=True);jp=folder/'job.json'
    if jp.exists():
        if read_json(jp)['status']=='complete':print('Completed readout probe retained');return
        raise ValueError('One-shot failed/interrupted probe retained; documented repair required')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0,
        restart_command='scripts/probe_readout_adapter.ps1 -Worker; preserve terminal probe, documented repair only')
    atomic_json(jp,job);started=None;stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Readout probe interrupted')
        if started is not None and time.monotonic()-started>120:raise TimeoutError('Own120s readout probe exhausted')
    def heartbeat(stage,**kw):
        check();job.update(stage=stage,heartbeat_at=now(),**kw)
        if started is not None:job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for relative in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=folder/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/relative,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);old=c['source']
        memory=torch.load(c['references']['memory']['path'],map_location='cpu',weights_only=False)
        pool=TrainView(old['pool']['pool'],old['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused:raise ValueError('Accepted217MB index cache must be reused')
        original=TrainView(old['original_web']['path'],old['original_web']['manifest_sha256'])
        positive=RelationLanguageTrainView(old['positive_data']['path'],old['positive_data']['manifest_sha256'])
        binding=dict(config_sha256=sha256(CONFIG),parent=c['parent'],arm='readout_adapter',study_kind=KIND,teacher_goals=native.GOALS,policy=POLICY)
        def build():return ReadoutAdapterTrainer(parent,pool,original,positive,native.GOALS,binding)
        with gpu_lock('cuda'):
            started=time.monotonic();job['status']='running';heartbeat('architecture-forward-controls')
            result=dict(architecture=architecture(parent,memory,c,check));initial=build()
            checks=dict(native_weights_frozen_unchanged=native_unchanged(initial.model,parent),
                fresh_readout_Adam=initial.optimizer.state_dict()['state']=={},only_two_trainable_tensors=len(initial.optimizer.param_groups[0]['params'])==2,
                actual_readout_LR=initial.optimizer.param_groups[0]['lr']==READOUT_LR,zero_initial_up=initial.model.lm_head.up.count_nonzero().item()==0,
                unique_parameters=sum(p.numel() for p in initial.model.parameters())==10099456,
                trainable_parameters=sum(p.numel() for p in initial.model.parameters() if p.requires_grad)==98304,
                parent_RNG=equal_state(rng_state(),parent['rng']),
                actual_Web_cursor=equal_state(initial.sampler.streams['web'].sampler.state_dict(),parent['sampler']['streams']['web']['sampler']))
            if not all(checks.values()):raise ValueError('Initial native/fresh readout contract differs')
            result['initial_preservation']=checks;del initial;gc.collect();torch.cuda.empty_cache()
            heartbeat('own-CUDA-resume-gate');gate=resume_gate(build,folder/'resume-gate',c,check,parent);result['resume_gate']=gate
            heartbeat('own32-CUDA-timing');trainer=build();rows=[];torch.cuda.reset_peak_memory_stats()
            with (folder/'metrics.jsonl').open('x',buffering=1) as stream:
                for i in range(32):
                    check();row=trainer.step();rows.append(row);stream.write(json.dumps(row,allow_nan=False)+'\n')
                    if (i+1)%8==0:heartbeat('own32-CUDA-timing',completed_updates=i+1)
            for a,b in zip(rows[:4],gate['histories'][0],strict=True):
                if any(not equal_state(a[k],b[k]) for k in ('loss','gradient_norm','token_digest','source_teachers','readout_LR')):
                    raise ValueError('Own32 and resume trajectories differ')
            if not native_unchanged(trainer.model,parent):raise ValueError('Timing changed native weights')
            path=folder/'timing.pt';saved=trainer.save(path)
            if not finite_state(torch.load(path,map_location='cpu',weights_only=False)):raise ValueError('Finite actual CUDA checkpoint required')
            result['timing']=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                terminal_save_seconds=saved,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),checkpoint=reference(path))
            check();elapsed=time.monotonic()-started;measured,forecast=estimate_training(result)
            result.update(passed=True,GPU_seconds=elapsed,config_sha256=sha256(CONFIG),optimizer_updates=40,
                verification_teacher_tokens=gate['verification_teacher_tokens']+result['timing']['verification_teacher_tokens'],
                scientific_teacher_tokens=0,diagnostic_weights_discarded_for_science=True,measured_timing=measured,
                previous_failed_GPU_seconds=c['previous_failed_GPU_seconds'],estimated_science_GPU_seconds=forecast,
                estimated_total_GPU_seconds=forecast+elapsed+c['previous_failed_GPU_seconds'],
                within900_seconds=forecast+elapsed+c['previous_failed_GPU_seconds']<=900,Base_complete=False)
            atomic_json(folder/'result.json',result);job.update(status='complete',stage='probe-complete-not-science',GPU_elapsed_seconds=elapsed,ended_at=now())
            atomic_json(jp,job);print(json.dumps(dict(status=job['stage'],GPU_seconds=elapsed,estimated_total_GPU_seconds=forecast+elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),GPU_elapsed_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(jp,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();group=p.add_mutually_exclusive_group();group.add_argument('--prepare',action='store_true');group.add_argument('--inspect',action='store_true');args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Fixed readout preflight valid; GPU0')
    else:run()
