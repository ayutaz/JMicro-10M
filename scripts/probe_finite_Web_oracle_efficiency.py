"""One readonly FP32 SDPA implementation comparison; no optimizer or adoption."""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import argparse
import copy
import gc
import json
import math
from pathlib import Path
import signal
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,rng_state,synchronize,implementation_hashes
from jmicro.model import JMicroModel
from phase6_performance import identity,alive
from run_eos_short_pilot import equal_state
from finite_Web_constraint import BodyOracle
import run_finite_Web_constraint as old

RUN=ROOT/'reports/phase6/finite-Web-oracle-efficiency-20261006'
CONFIG=ROOT/'configs/phase6/finite_Web_oracle_efficiency.json'
SOURCES=('scripts/probe_finite_Web_oracle_efficiency.py','scripts/probe_finite_Web_oracle_efficiency.ps1')
NLL_ATOL=2e-6;GRAD_ABS=2e-6;GRAD_REL=2e-5


class EfficientBodyOracle(BodyOracle):
    """Same unpadded labels/microbatch/denominator; only SDPA backend differs."""
    def measure(self,gradient=False):
        synchronize(self.x.device);started=time.perf_counter();training=self.model.training
        self.model.eval();total=0.;gradients=[torch.zeros_like(p) for p in self.parameters] if gradient else None
        try:
            with sdpa_kernel(SDPBackend.EFFICIENT_ATTENTION),torch.autocast(device_type=self.x.device.type,enabled=False),\
                    (torch.enable_grad() if gradient else torch.no_grad()):
                for begin in range(0,len(self.x),self.microbatch):
                    x=self.x[begin:begin+self.microbatch];y=self.y[begin:begin+self.microbatch]
                    logits=self.model(x,training_fast_path=True).logits
                    loss=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),y.reshape(-1),ignore_index=-100,reduction='sum')/self.teachers
                    if not bool(torch.isfinite(loss)):raise ValueError('Nonfinite efficient body NLL')
                    total+=float(loss.detach())
                    if gradient:
                        values=torch.autograd.grad(loss,self.parameters)
                        for accumulator,value in zip(gradients,values,strict=True):accumulator.add_(value.detach())
                    del logits,loss
            if not math.isfinite(total) or total<0:raise ValueError('Finite body NLL required')
            if gradient and any(not bool(torch.isfinite(g).all()) for g in gradients):raise ValueError('Nonfinite efficient gradient')
            self.stats['gradient_calls' if gradient else 'forward_only_calls']+=1
            self.stats['teacher_observations']+=self.teachers;self.stats['physical_input_tokens']+=self.physical
            if gradient:self.stats['gradient_teacher_tokens']+=self.teachers
            return total,gradients
        finally:
            self.model.train(training);synchronize(self.x.device);self.last_seconds=time.perf_counter()-started


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();c=old.inspect(old.PROBE_CONFIG);r=old.probe_evidence()
    if old.CONFIG.exists() or old.estimate_training(r)+r['GPU_seconds']<=2400:raise ValueError('Actual budget rejection required')
    config=dict(kind='readonly_fixed_FP32_efficient_SDPA_oracle_probe_v1',created_at=now(),GPU_budget_seconds=60,
        CPU_preparation_ceiling_seconds=20,original_config=old.reference(old.PROBE_CONFIG),
        original_probe=old.reference(old.RUN/'probe/result.json'),memory=c['memory'],memory_binding=c['memory_binding'],
        checkpoints=dict(original_fullparent=c['parent'],fixed_masked_staged=c['violating_numerical_control']),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},old_source_sha256=c['source_sha256'],implementation=implementation_hashes(),
        settings=dict(dtype='float32',autocast=False,TF32=False,microbatch=8,backend='EFFICIENT_ATTENTION',fallback_allowed=False,
            reference_backend='MATH',first_call_warmup=True,forward_measurements=4,gradient_measurements=4),
        numerical_tolerances=dict(body_NLL_absolute=NLL_ATOL,gradient_element_absolute=GRAD_ABS,gradient_element_relative=GRAD_REL,
            gradient_global_relative_L2=GRAD_REL),
        completion='Both fixed checkpoints: finite NLL/grad, element/global parity, repeated bitwise output+gradient, read-only weights/grad/RNG and owned timings; failures terminal without alternate backend/dtype/memory rescue.',
        scope='TRAIN implementation diagnostic only, not held-out quality or proof of parity for all future weights.',
        quality_criteria_unchanged=True,optimizer_updates=0,new_source_CE_teacher_tokens=0,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    elapsed=time.monotonic()-started
    if elapsed>20:raise TimeoutError('Preparation budget exceeded')
    config['CPU_preparation_seconds']=elapsed;atomic_json(CONFIG,config);inspect()
    print(json.dumps(dict(status='oracle_efficiency_prepared',CPU_seconds=elapsed,new_GPU_seconds=0)),flush=True)


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!='readonly_fixed_FP32_efficient_SDPA_oracle_probe_v1' or c['GPU_budget_seconds']!=60
            or c['numerical_tolerances']!=dict(body_NLL_absolute=NLL_ATOL,gradient_element_absolute=GRAD_ABS,
                gradient_element_relative=GRAD_REL,gradient_global_relative_L2=GRAD_REL)
            or c['implementation']!=implementation_hashes() or c['optimizer_updates'] or c['new_source_CE_teacher_tokens']
            or c['Base_complete'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started'] or c['protected_test_used']):
        raise ValueError('Fixed readonly budget/scope differs')
    for s,digest in {**c['source_sha256'],**c['old_source_sha256']}.items():
        if sha256(ROOT/s)!=digest:raise ValueError('Frozen source differs '+s)
    for ref in (c['original_config'],c['original_probe'],c['memory'],*c['checkpoints'].values()):old.check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual live duplicate forbidden')
    return c


def compare_gradients(reference,candidate):
    if len(reference)!=len(candidate):raise ValueError('Unique parameter count differs')
    maximum=0.;squared_error=0.;squared_ref=0.;elements=True
    for a,b in zip(reference,candidate,strict=True):
        difference=(a-b).double();maximum=max(maximum,float(difference.abs().max()))
        squared_error+=float(difference.square().sum());squared_ref+=float(a.double().square().sum())
        elements=elements and bool((difference.abs()<=GRAD_ABS+GRAD_REL*a.double().abs()).all())
    relative=math.sqrt(squared_error/max(squared_ref,1e-300))
    return dict(maximum_absolute=maximum,global_relative_L2=relative,all_elementwise=elements,
        passed=elements and relative<=GRAD_REL)


def run():
    c=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json';previous=read_json(jp) if jp.exists() else {}
    if previous.get('status')=='complete':print('Completed owned efficiency probe retained');return
    if previous:raise ValueError('Terminal/interrupted one-shot probe retained; no unbounded retry')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0)
    atomic_json(jp,job);started=None;stopped=[False];result=dict(checkpoints={},optimizer_updates=0,new_source_CE_teacher_tokens=0)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Readonly diagnostic interrupted, no restart')
        if started is not None and time.monotonic()-started>60:raise TimeoutError('Own60s GPU budget exhausted')
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for s in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/s;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/s).read_bytes())
        memory=torch.load(c['memory']['path'],map_location='cpu',weights_only=False)
        with gpu_lock('cuda'):
            started=time.monotonic();job.update(status='running',stage='readonly_fp32_oracle');atomic_json(jp,job)
            for label,ref in c['checkpoints'].items():
                check();state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                m=JMicroModel(state['model_config']).to('cuda');m.load_state_dict(state['model']);m.train()
                before=[p.detach().clone() for p in m.parameters()];before_rng=rng_state()
                reference=BodyOracle(m,memory,8);candidate=EfficientBodyOracle(m,memory,8)
                # One fixed warm-up per backend includes the parity gradient.
                base_value,base_gradient=reference.measure(True);check()
                fast_value,fast_gradient=candidate.measure(True);check()
                repeated_value,repeated_gradient=candidate.measure(True);check()
                parity=compare_gradients(base_gradient,fast_gradient)
                checks=dict(NLL=abs(base_value-fast_value)<=NLL_ATOL,gradient=parity['passed'],
                    candidate_bitwise_repeat=repeated_value==fast_value and all(torch.equal(a,b) for a,b in zip(fast_gradient,repeated_gradient,strict=True)),
                    no_parameter_grads=all(p.grad is None for p in m.parameters()),
                    weights_unchanged=all(torch.equal(a,b) for a,b in zip(m.parameters(),before,strict=True)),
                    RNG_unchanged=equal_state(before_rng,rng_state()),training_state_unchanged=m.training,
                    unique_tied_parameters=len({id(p) for p in m.parameters()})==len(reference.parameters))
                point=dict(reference_body_NLL=base_value,candidate_body_NLL=fast_value,NLL_absolute_error=abs(base_value-fast_value),
                    gradient_parity=parity,checks=checks,reference_checkpoint=ref,parameter_count=sum(p.numel() for p in m.parameters()))
                result['checkpoints'][label]=point;atomic_json(RUN/'progress-result.json',result)
                if not all(checks.values()):raise ValueError('Fixed numeric/read-only gate failed '+label+' '+repr(checks))
                del base_gradient,fast_gradient,repeated_gradient
                timings={}
                for name,oracle in (('math',reference),('efficient',candidate)):
                    timings[name]=dict(forward_only_seconds=[],gradient_seconds=[])
                    for i in range(4):
                        check();oracle.measure();timings[name]['forward_only_seconds'].append(oracle.last_seconds)
                        check();_,gradient=oracle.measure(True);timings[name]['gradient_seconds'].append(oracle.last_seconds);del gradient
                checks.update(final_weights_unchanged=all(torch.equal(a,b) for a,b in zip(m.parameters(),before,strict=True)),
                    final_RNG_unchanged=equal_state(before_rng,rng_state()),final_no_parameter_grads=all(p.grad is None for p in m.parameters()))
                if not all(checks.values()):raise ValueError('Final readonly state changed')
                point.update(timings=timings,reference_counts=reference.stats,candidate_counts=candidate.stats,
                    peak_allocated_bytes=torch.cuda.max_memory_allocated(),peak_reserved_bytes=torch.cuda.max_memory_reserved())
                atomic_json(RUN/'progress-result.json',result)
                job.update(stage=label+'_complete',GPU_elapsed_seconds=time.monotonic()-started);atomic_json(jp,job)
                del reference,candidate,m,before,state;gc.collect();torch.cuda.empty_cache()
            check();elapsed=time.monotonic()-started
            all_fast_forward=[v for p in result['checkpoints'].values() for v in p['timings']['efficient']['forward_only_seconds']]
            all_fast_gradient=[v for p in result['checkpoints'].values() for v in p['timings']['efficient']['gradient_seconds']]
            prior=read_json(Path(c['original_probe']['path']));rows=prior['timing']['histories']
            import statistics
            old_step=statistics.median(v['seconds'] for v in rows[8:]);old_forward=max(prior['oracle_timings']['forward_only_seconds'])
            warm=max(0.,sum(v['seconds'] for v in rows[:8])-8*old_step)
            worst_step=max(0.,old_step-old_forward)+6*max(all_fast_forward)+max(all_fast_gradient)
            estimate=(3068*worst_step+warm+14*prior['timing']['terminal_save_seconds'])*1.3+200
            # This is implementation-only planning; own transactional resume and
            # exact math acceptance audits still required before scientific use.
            result.update(status='readonly_oracle_efficiency_complete',passed=True,config_sha256=sha256(CONFIG),GPU_seconds=elapsed,
                maximum_fast_forward_seconds=max(all_fast_forward),maximum_fast_gradient_seconds=max(all_fast_gradient),
                illustrative_optimized_science_estimate_seconds=estimate,
                estimate_scope='Single implementation estimate from retained source timing; excludes future exact-math acceptance audits/new transactional CUDA gate. Not a scientific launch authorization.',
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
            atomic_json(RUN/'result.json',result);job.update(status='complete',completed_at=now(),GPU_elapsed_seconds=elapsed)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true')
    args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect()
    else:run()
