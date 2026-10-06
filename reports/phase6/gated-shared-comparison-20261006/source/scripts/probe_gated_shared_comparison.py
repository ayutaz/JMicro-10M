"""One actual architecture/numerical/resume/timing gate; no science yet."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.model import JMicroModel
from jmicro.training import atomic_json,gpu_lock,implementation_hashes,rng_state
from cached_three_source_index import CachedThreeSourceIndex
from condition_relation_language import RelationLanguageTrainView
from gated_shared_model import GatedSharedModel,POLICY
from gated_shared_trainer import GatedSharedTrainer,KIND,NATIVE_LR,GATE_LR
from phase6_performance import alive,identity,finite_state
from run_eos_short_pilot import equal_state
import run_parameter_displacement_anchor_v3 as native

RUN=ROOT/'reports/phase6/gated-shared-comparison-20261006'
PROPOSAL=ROOT/'reports/phase6/gated_shared_proposal.json'
CONFIG=ROOT/'configs/phase6/gated_shared_probe.json'
SOURCES=('scripts/gated_shared_model.py','scripts/gated_shared_trainer.py','scripts/gated_shared_evaluation.py',
    'scripts/define_gated_shared_comparison.py','scripts/probe_gated_shared_comparison.py',
    'scripts/probe_gated_shared_comparison.ps1','tests/test_gated_shared.py')
reference,check_reference=native.reference,native.check_reference


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();p=read_json(PROPOSAL);old=native.inspect(native.CONFIG)
    if (p['kind']!=KIND or p['parent']!=old['parent'] or p['policy']!=POLICY
            or p['native_lr']!=NATIVE_LR or p['new_gate_lr']!=GATE_LR or p['new_gate_weight_decay']!=0
            or p['unique_parameters']!=10001165 or p['ordinary_source_CE_teacher_tokens']!=100000000
            or p['own_CUDA_probe_ceiling_seconds']!=120 or p['total_new_GPU_ceiling_seconds']!=1800
            or any(p[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Fixed function-preserving sharing research required')
    for ref in p['references'].values():check_reference(ref)
    references=dict(p['references'],proposal=reference(PROPOSAL),
        memory=reference(ROOT/'reports/phase6/finite-Web-constraint-20261006/memory.pt'))
    c=dict(kind=KIND,phase='architecture_probe',parent=old['parent'],policy=POLICY,
        native_LR=NATIVE_LR,new_gate_LR=GATE_LR,unique_parameters=10001165,logical_layers=26,
        references=references,source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        old_source_sha256={**old['old_source_sha256'],**old['source_sha256']},implementation=implementation_hashes(),
        source=old, GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=1800,
        numerical_tolerances=dict(zero_gate_FP32_absolute=2e-6,zero_gate_FP32_relative=2e-6,
            zero_gate_BF16_absolute=0.,zero_gate_BF16_relative=0.,signed_gate_cache_FP32_absolute=2e-5,signed_gate_cache_FP32_relative=2e-4),
        CPU_preparation_seconds=time.monotonic()-started,created_at=now(),Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False)
    if c['CPU_preparation_seconds']>30:raise TimeoutError('CPU probe preparation30s exhausted')
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='gated_shared_probe_frozen',CPU_seconds=c['CPU_preparation_seconds'],GPU_seconds=0)))


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!=KIND or c['phase']!='architecture_probe' or c['policy']!=POLICY
            or c['native_LR']!=NATIVE_LR or c['new_gate_LR']!=GATE_LR or c['unique_parameters']!=10001165
            or c['logical_layers']!=26 or c['GPU_budget_seconds']!=120 or c['total_new_GPU_ceiling_seconds']!=1800
            or c['implementation']!=implementation_hashes()
            or any(c[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Frozen gated architecture/probe differs')
    for name,digest in {**c['source_sha256'],**c['old_source_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'],*c['references'].values()):check_reference(ref)
    if (RUN/'probe/job.json').exists() and alive(read_json(RUN/'probe/job.json')):raise ValueError('Actual live duplicate forbidden')
    return c


def compare(a,b,absolute,relative):
    if not torch.isfinite(a).all() or not torch.isfinite(b).all():raise ValueError('Finite architecture logits required')
    torch.testing.assert_close(a,b,atol=absolute,rtol=relative)
    return dict(max_absolute_error=float((a-b).abs().max()),absolute_tolerance=absolute,relative_tolerance=relative,passed=True)


def architecture_probe(parent,memory,c,check):
    native_model=JMicroModel(parent['model_config']).to('cuda').eval();native_model.load_state_dict(parent['model'],strict=True)
    shared=GatedSharedModel.from_native(native_model).eval();x=memory['x'][:1].to('cuda');before=rng_state();results={}
    for dtype in (torch.float32,torch.bfloat16):
        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast(device_type='cuda',dtype=torch.bfloat16,enabled=dtype==torch.bfloat16):
            for length in (32,1024):
                check();a=native_model(x[:,:length]).logits;b=shared(x[:,:length]).logits
                tolerances=c['numerical_tolerances'];prefix='zero_gate_FP32' if dtype==torch.float32 else 'zero_gate_BF16'
                results[f'{dtype}_{length}']=compare(a,b,tolerances[prefix+'_absolute'],tolerances[prefix+'_relative'])
                del a,b
    # Deliberately signed, nonzero diagnostic gates; these are discarded and
    # never become scientific initialization or learned quality evidence.
    with torch.no_grad():shared.reuse_gates.copy_(torch.tensor([.1 if i%2==0 else -.05 for i in range(13)],device='cuda'))
    with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast(device_type='cuda',enabled=False):
        check();full=shared(x).logits;prefix=shared(x[:,:1008],use_cache=True)
        chunk=shared(x[:,1008:],cache=prefix.cache,use_cache=True)
        tol=c['numerical_tolerances'];results['signed_gate_cache1024']=compare(full[:,1008:],chunk.logits,
            tol['signed_gate_cache_FP32_absolute'],tol['signed_gate_cache_FP32_relative'])
        if len(chunk.cache.layers)!=26 or chunk.cache.layers[0][0].data_ptr()==chunk.cache.layers[1][0].data_ptr():
            raise ValueError('Separate logical26 cache required')
    if not equal_state(before,rng_state()):raise ValueError('Architecture forward changed RNG')
    # Matrix weights are shared exact objects with the native parent.
    if any(not torch.equal(v.detach().cpu(),parent['model'][k]) for k,v in native_model.state_dict().items()):
        raise ValueError('Architecture probe changed native parent weights')
    result=dict(checks=results,weights_unchanged=True,RNG_unchanged=True,optimizer_updates=0,
        diagnostic_forward_calls=11,diagnostic_forward_context_positions=4*(32+1024)+1024+1008+16,logical_layers=26)
    del full,prefix,chunk,shared,native_model;gc.collect();torch.cuda.empty_cache()
    return result


def estimate_training(result):
    record=result['timing'];rows=record['histories']
    if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 for r in rows):
        raise ValueError('Own32 finite measured updates required')
    step=statistics.median(r['seconds'] for r in rows[8:]);teachers=record['verification_teacher_tokens']/32
    updates=math.ceil(100000000/teachers);warm=max(0.,sum(r['seconds'] for r in rows[:8])-8*step)
    saving=(math.ceil(updates/250)+1)*record['terminal_save_seconds'];cost=updates*step+warm+saving
    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,
        warmup_seconds=warm,save_seconds=saving,estimated_training_seconds=cost),cost*1.3+300


def run():
    c=inspect();folder=RUN/'probe';folder.mkdir(parents=True,exist_ok=True);jp=folder/'job.json'
    if jp.exists():
        if read_json(jp)['status']=='complete':print('Completed sharing probe retained');return
        raise ValueError('One-shot failed/interrupted architecture probe retained; no sweep/retry')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0,
        restart_command='scripts/probe_gated_shared_comparison.ps1 -Worker; completed retained, terminal failure requires documented repair')
    atomic_json(jp,job);started=None;stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Gated architecture probe interrupted')
        if started is not None and time.monotonic()-started>120:raise TimeoutError('Actual120s architecture probe exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
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
        if not pool.index.cache_reused:raise ValueError('Accepted217MB compact cache required')
        original=TrainView(old['original_web']['path'],old['original_web']['manifest_sha256'])
        positive=RelationLanguageTrainView(old['positive_data']['path'],old['positive_data']['manifest_sha256'])
        b=dict(config_sha256=sha256(CONFIG),parent=c['parent'],arm='gated_shared',study_kind=KIND,
            teacher_goals=native.GOALS,policy=POLICY,native_LR=NATIVE_LR,new_gate_LR=GATE_LR)
        def build():return GatedSharedTrainer(parent,pool,original,positive,native.GOALS,b)
        with gpu_lock('cuda'):
            started=time.monotonic();job['status']='running';heartbeat('architecture-forward-controls')
            result=dict(architecture=architecture_probe(parent,memory,c,check))
            initial=build();optimizer=initial.optimizer.state_dict()
            expected_scheduler=copy.deepcopy(parent['scheduler'])
            for key,value in (('base_lrs',GATE_LR/.1),('_last_lr',GATE_LR),('lr_lambdas',None)):
                expected_scheduler[key].append(value)
            checks=dict(native_weights=all(torch.equal(v.detach().cpu(),parent['model'][k]) for k,v in initial.model.state_dict().items() if k!='reuse_gates'),
                native_Adam_moments=equal_state(native.prior.cpu_state(optimizer['state']),parent['optimizer']['state']),
                native_groups=equal_state(optimizer['param_groups'][:2],parent['optimizer']['param_groups']),
                fresh_gate_moments=len(optimizer['state'])==len(parent['optimizer']['state']),
                native_scheduler=equal_state(initial.scheduler.state_dict(),expected_scheduler),
                parent_RNG=equal_state(rng_state(),parent['rng']),zero_initial_gates=int(initial.model.reuse_gates.count_nonzero())==0,
                native_and_gate_LRs=[g['lr'] for g in initial.optimizer.param_groups]==[NATIVE_LR,NATIVE_LR,GATE_LR],
                unique_parameters=sum(p.numel() for p in initial.model.parameters())==10001165,
                actual_Web_cursor=equal_state(initial.sampler.streams['web'].sampler.state_dict(),parent['sampler']['streams']['web']['sampler']))
            if not all(checks.values()):raise ValueError('Exact native initial state/gate policy differs')
            result['initial_fullstate_preservation']=checks;del initial,optimizer;gc.collect();torch.cuda.empty_cache()
            heartbeat('own-CUDA-resume-gate')
            gate=native.prior.resume_gate(build,folder/'resume-gate',sha256(CONFIG),check)
            for key in ('CE_loss','new_gate_LR'):
                gate['checks']['history_'+key]=all(a[key]==b[key] for a,b in zip(*gate['histories'],strict=True))
            if not all(gate['checks'].values()):raise ValueError('Own gated objective/LR history differs')
            atomic_json(folder/'resume-gate/result.json',gate);result['resume_gate']=gate
            heartbeat('own32-CUDA-timing');trainer=build();rows=[];torch.cuda.reset_peak_memory_stats()
            log=folder/'metrics.jsonl'
            with log.open('x',buffering=1) as stream:
                for index in range(32):
                    check();row=trainer.step();rows.append(row);stream.write(json.dumps(row,allow_nan=False)+'\n')
                    if (index+1)%8==0:heartbeat('own32-CUDA-timing',completed_updates=index+1)
            for actual,expected in zip(rows[:4],gate['histories'][0],strict=True):
                if any(actual[k]!=expected[k] for k in ('loss','gradient_norm','token_digest','source_teachers','new_gate_LR')):
                    raise ValueError('Own32 and gate trajectories differ')
            path=folder/'timing.pt';saved=trainer.save(path)
            if not finite_state(torch.load(path,map_location='cpu',weights_only=False)):raise ValueError('Finite CUDA terminal state required')
            result['timing']=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                terminal_save_seconds=saved,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),checkpoint=reference(path))
            check();elapsed=time.monotonic()-started
            result.update(passed=True,GPU_seconds=elapsed,config_sha256=sha256(CONFIG),optimizer_updates=40,
                verification_teacher_tokens=gate['verification_teacher_tokens']+result['timing']['verification_teacher_tokens'],
                scientific_teacher_tokens=0,diagnostic_weights_discarded_for_science=True,Base_complete=False)
            timing,estimate=estimate_training(result);result.update(measured_timing=timing,estimated_science_GPU_seconds=estimate,
                estimated_total_GPU_seconds=estimate+elapsed,within1800_seconds=estimate+elapsed<=1800)
            atomic_json(folder/'result.json',result);job.update(status='complete',stage='probe-complete-not-science',GPU_elapsed_seconds=elapsed,ended_at=now())
            atomic_json(jp,job);print(json.dumps(dict(status=job['stage'],GPU_seconds=elapsed,estimated_total_GPU_seconds=estimate+elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',ended_at=now(),error=repr(exc),GPU_elapsed_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(jp,job);raise


if __name__=='__main__':
    parser=argparse.ArgumentParser();m=parser.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Fixed gated-sharing preflight valid; GPU0')
    else:run()
