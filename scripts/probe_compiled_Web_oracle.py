"""Single FP32 fullgraph/default compilation diagnostic, no learned updates."""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import argparse
import gc
import json
import math
from pathlib import Path
import signal
import statistics
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,rng_state,implementation_hashes
from jmicro.model import JMicroModel
from phase6_performance import identity,alive
from run_eos_short_pilot import equal_state
from finite_Web_constraint import BodyOracle
from probe_finite_Web_oracle_efficiency import EfficientBodyOracle,compare_gradients,NLL_ATOL
import probe_finite_Web_oracle_efficiency as prior
import run_finite_Web_constraint as original

RUN=ROOT/'reports/phase6/compiled-Web-oracle-20261006'
CONFIG=ROOT/'configs/phase6/compiled_Web_oracle.json'
SOURCES=('scripts/probe_compiled_Web_oracle.py','scripts/probe_compiled_Web_oracle.ps1')
SETTINGS=dict(dtype='float32',autocast=False,TF32=False,microbatch=8,backend='EFFICIENT_ATTENTION',
    compile_fullgraph=True,compile_mode='default',compile_backend='inductor',compile_dynamic=False,
    fallback_allowed=False,forward_measurements=4,gradient_measurements=4)


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();c=prior.inspect();r=read_json(prior.RUN/'result.json');job=read_json(prior.RUN/'job.json')
    if job['status']!='complete' or alive(job) or not r['passed'] or r['config_sha256']!=sha256(prior.CONFIG):
        raise ValueError('Actual completed prior implementation evidence required')
    source=original.inspect(original.PROBE_CONFIG);raw=original.probe_evidence()
    config=dict(kind='readonly_compiled_fixed_FP32_efficient_SDPA_v1',created_at=now(),GPU_budget_seconds=120,
        settings=SETTINGS,numerical_tolerances=c['numerical_tolerances'],memory=c['memory'],memory_binding=c['memory_binding'],
        checkpoints=c['checkpoints'],source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        old_source_sha256={**c['old_source_sha256'],**c['source_sha256']},implementation=implementation_hashes(),
        references=dict(previous_config=original.reference(prior.CONFIG),previous_result=original.reference(prior.RUN/'result.json'),
            original_config=original.reference(original.PROBE_CONFIG),original_result=original.reference(original.RUN/'probe/result.json')),
        previous_related_GPU_seconds=raw['GPU_seconds']+r['GPU_seconds'],
        future_science_total_GPU_ceiling_seconds=2400,original_body_ceiling_multiplier=1.01,
        completion='Both preselected weights: strict original MATH NLL/gradient parity, bitwise repeat, unchanged native weights/RNG/grad, four actual forward and gradient timings; compile warm-up counted. No optimizer, alternate compile mode/dtype/backend/checkpoint rescue.',
        scope='TRAIN implementation probe; not future global equivalence, quality, or science authorization.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        optimizer_updates=0,new_source_CE_teacher_tokens=0,quality_criteria_unchanged=True)
    elapsed=time.monotonic()-started
    if elapsed>20:raise TimeoutError('CPU preparation20s exhausted')
    config['CPU_preparation_seconds']=elapsed;atomic_json(CONFIG,config);inspect()
    print(json.dumps(dict(status='compiled_oracle_prepared',CPU_seconds=elapsed,GPU_seconds=0)),flush=True)


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!='readonly_compiled_fixed_FP32_efficient_SDPA_v1' or c['GPU_budget_seconds']!=120
            or c['settings']!=SETTINGS or c['future_science_total_GPU_ceiling_seconds']!=2400
            or c['numerical_tolerances']!=read_json(prior.CONFIG)['numerical_tolerances']
            or c['implementation']!=implementation_hashes() or c['optimizer_updates'] or c['new_source_CE_teacher_tokens']
            or c['Base_complete'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started'] or c['protected_test_used']):
        raise ValueError('Fixed compilation scope/settings differ')
    for s,digest in {**c['source_sha256'],**c['old_source_sha256']}.items():
        if sha256(ROOT/s)!=digest:raise ValueError('Frozen source differs '+s)
    for ref in (*c['references'].values(),c['memory'],*c['checkpoints'].values()):original.check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual live duplicate forbidden')
    return c


def run():
    c=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json'
    if jp.exists():
        previous=read_json(jp)
        if previous['status']=='complete':print('Completed compiled oracle retained');return
        raise ValueError('Retain one-shot terminal/interrupted probe; no unbounded retry')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0)
    atomic_json(jp,job);started=None;stopped=[False];result=dict(checkpoints={},optimizer_updates=0,new_source_CE_teacher_tokens=0)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Readonly compiled diagnostic interrupted')
        if started is not None and time.monotonic()-started>120:raise TimeoutError('Own120s GPU/compile budget exhausted')
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for s in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/s;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((ROOT/s).read_bytes())
        memory=torch.load(c['memory']['path'],map_location='cpu',weights_only=False)
        with gpu_lock('cuda'):
            started=time.monotonic();job.update(status='running');atomic_json(jp,job)
            for label,ref in c['checkpoints'].items():
                check();job.update(stage=label+'_compile_and_parity',GPU_elapsed_seconds=time.monotonic()-started);atomic_json(jp,job)
                state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).to('cuda');model.load_state_dict(state['model']);model.train()
                before=[p.detach().clone() for p in model.parameters()];before_rng=rng_state()
                reference=BodyOracle(model,memory,8)
                base_value,base_gradient=reference.measure(True);check()
                # Sole candidate. Compiler errors/graph breaks are failures;
                # no eager fallback or mode search is permitted.
                compiled=torch.compile(model,fullgraph=True,mode='default',backend='inductor',dynamic=False)
                candidate=EfficientBodyOracle(compiled,memory,8)
                warm_start=time.monotonic();value,gradient=candidate.measure(True);warm_seconds=time.monotonic()-warm_start;check()
                repeated_value,repeated_gradient=candidate.measure(True);check()
                # no_grad and autograd have distinct compiler specializations.
                # Count both first calls in the real GPU clock; steady forward
                # timings must not accidentally measure first compilation.
                forward_warm_start=time.monotonic();forward_value,_=candidate.measure()
                forward_warm_seconds=time.monotonic()-forward_warm_start;check()
                parity=compare_gradients(base_gradient,gradient)
                checks=dict(NLL=abs(base_value-value)<=NLL_ATOL,forward_NLL=abs(base_value-forward_value)<=NLL_ATOL,gradient=parity['passed'],
                    candidate_bitwise_repeat=repeated_value==value and all(torch.equal(a,b) for a,b in zip(gradient,repeated_gradient,strict=True)),
                    no_parameter_grads=all(p.grad is None for p in model.parameters()),
                    weights_unchanged=all(torch.equal(a,b) for a,b in zip(model.parameters(),before,strict=True)),
                    RNG_unchanged=equal_state(before_rng,rng_state()),training_state_unchanged=model.training,
                    native_parameter_identity=list(model.parameters())==candidate.parameters)
                point=dict(reference_checkpoint=ref,reference_body_NLL=base_value,candidate_body_NLL=value,
                    NLL_absolute_error=abs(base_value-value),gradient_parity=parity,checks=checks,
                    first_gradient_compile_and_warmup_seconds=warm_seconds,first_forward_compile_and_warmup_seconds=forward_warm_seconds,
                    native_parameter_count=sum(p.numel() for p in model.parameters()))
                result['checkpoints'][label]=point;atomic_json(RUN/'progress-result.json',result)
                if not all(checks.values()):raise ValueError('Fixed compiled numeric/readonly gate failed '+label+' '+repr(checks))
                del base_gradient,gradient,repeated_gradient
                timings=dict(forward_only_seconds=[],gradient_seconds=[])
                for i in range(4):
                    check();candidate.measure();timings['forward_only_seconds'].append(candidate.last_seconds)
                    check();_,gradient=candidate.measure(True);timings['gradient_seconds'].append(candidate.last_seconds);del gradient
                checks.update(final_weights_unchanged=all(torch.equal(a,b) for a,b in zip(model.parameters(),before,strict=True)),
                    final_RNG_unchanged=equal_state(before_rng,rng_state()),final_no_parameter_grads=all(p.grad is None for p in model.parameters()))
                if not all(checks.values()):raise ValueError('Final native state changed')
                point.update(timings=timings,reference_counts=reference.stats,candidate_counts=candidate.stats,
                    peak_allocated_bytes=torch.cuda.max_memory_allocated(),peak_reserved_bytes=torch.cuda.max_memory_reserved())
                atomic_json(RUN/'progress-result.json',result)
                job.update(stage=label+'_complete',GPU_elapsed_seconds=time.monotonic()-started);atomic_json(jp,job)
                del candidate,compiled,reference,model,before,state;gc.collect();torch.cuda.empty_cache()
            check();elapsed=time.monotonic()-started
            forwards=[v for p in result['checkpoints'].values() for v in p['timings']['forward_only_seconds']]
            gradients=[v for p in result['checkpoints'].values() for v in p['timings']['gradient_seconds']]
            raw=read_json(Path(c['references']['original_result']['path']));rows=raw['timing']['histories']
            source=statistics.median(v['seconds'] for v in rows[8:]);math_forward=max(raw['oracle_timings']['forward_only_seconds'])
            warm=max(0.,sum(v['seconds'] for v in rows[:8])-8*source)
            # Conservatively reserve six candidate forwards + one gradient and
            # one mandatory original MATH acceptance audit for every update.
            worst=max(0.,source-math_forward)+6*max(forwards)+max(gradients)+math_forward
            compile_cost=sum(p['first_gradient_compile_and_warmup_seconds']+p['first_forward_compile_and_warmup_seconds'] for p in result['checkpoints'].values())
            estimate=(3068*worst+warm+14*raw['timing']['terminal_save_seconds']+compile_cost)*1.3+200
            result.update(status='readonly_compiled_oracle_complete',passed=True,config_sha256=sha256(CONFIG),GPU_seconds=elapsed,
                maximum_compiled_forward_seconds=max(forwards),maximum_compiled_gradient_seconds=max(gradients),
                estimated_science_with_original_math_acceptance_seconds=estimate,
                estimated_total_with_prior_and_own_probes=estimate+elapsed+c['previous_related_GPU_seconds'],
                science_launch_authorized=False,estimate_scope='Planning only; new actual transactional CUDA resume/timing gate remains required.',
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
            atomic_json(RUN/'result.json',result);job.update(status='complete',completed_at=now(),GPU_elapsed_seconds=elapsed)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true')
    a=p.parse_args()
    if a.prepare:prepare()
    elif a.inspect:inspect()
    else:run()
