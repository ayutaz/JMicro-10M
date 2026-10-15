"""Owned actual-parent rank8 branch gate; no scientific/DEV/TEST learning."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import sha256,now
from jmicro.independent_map import IndependentMapModel,IMPLEMENTATION,extra_parameter
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,rng_state
from independent_map_trainer import IndependentMapTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from probe_context_likelihood import weights_digest,passed_tests

CONFIG=ROOT/'configs/phase6/independent_map_probe_20261015.json'
RUN=ROOT/'reports/phase6/independent-map-probe-20261015'


def assert_scope(c):
    expected=dict(kind='owned_native_independent_rank8_map_CUDA_technical_v1',batch=48,seed=42,
        GPU_ceiling_seconds=180,prior_technical_GPU_seconds=72.56365345604718,
        timed_updates=32,continuous_updates=6,split_updates=[3,3],disabled_native_updates=3,
        capacity_shape=[48,1024],candidate_parameters=10067764,main_teacher_goal=100000000,
        maximum_new_GPU_seconds=4800,scientific_teacher_positions=0,attention_implementation=IMPLEMENTATION,
        capacity_before_any_optimizer=True,preserve_actual6_and_all_cache_subchecks=True,
        Base_adopted=False,TEST_prepared=False)
    if any(type(c.get(k)) is not type(v) or c[k]!=v for k,v in expected.items()):
        raise ValueError('Exact rank8/native-matched original cumulative180/4800 scope required')


def forecast(rows):
    if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 for r in rows):
        raise ValueError('All32 finite positive original-step durations required')
    return math.ceil(17698/32*sum(r['seconds'] for r in rows)*1.3+600)


def cache_observations(full,cached,rng_equal):
    a,b=full.logits[:,-cached.logits.shape[1]:],cached.logits
    if a.shape!=b.shape or len(full.cache.secondary)!=len(cached.cache.secondary):
        raise ValueError('Matching real full/suffix output and all K2 layers required')
    close=torch.isclose(a,b,atol=3e-5,rtol=2e-5)
    secondary=[dict(layer=i,maximum_difference=float((x-y).abs().max()),
        within_original_tolerance=torch.allclose(x,y,atol=3e-5,rtol=2e-5))
        for i,(x,y) in enumerate(zip(full.cache.secondary,cached.cache.secondary,strict=True))]
    checks=dict(finite_logits=bool(torch.isfinite(a).all() and torch.isfinite(b).all()),
        logits_within_original_tolerance=bool(close.all()),
        secondary_K2_within_original_tolerance=all(r['within_original_tolerance'] for r in secondary),
        positions_exact=torch.equal(full.cache.positions,cached.cache.positions),
        validity_exact=torch.equal(full.cache.valid,cached.cache.valid),RNG_unchanged=bool(rng_equal))
    bad=[]
    for index in (~close).nonzero()[:8].cpu().tolist():
        key=tuple(index)
        bad.append(dict(index=index,full_value=float(a[key]),cached_value=float(b[key]),
            absolute_difference=float((a[key]-b[key]).abs()),allowed_error=float(3e-5+2e-5*b[key].abs())))
    return dict(passed=all(checks.values()),subchecks=checks,absolute_tolerance=3e-5,relative_tolerance=2e-5,
        maximum_logit_difference=float((a-b).abs().max()),outside_original_logit_tolerance=int((~close).sum()),
        first_eight_outside=bad,secondary_K2=secondary)


def inspect(pin):
    if sha256(CONFIG)!=pin: raise ValueError('Externally pinned technical config required')
    c=json.loads(CONFIG.read_text())
    assert_scope(c)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path)!=digest: raise ValueError('Frozen source differs: '+path)
    for key in ('proposal','actual_CPU','accepted_config','capacity_payload','tokenizer','prior_completion'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']: raise ValueError('Pinned evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha256(Path(row['path']))!=row['sha256']: raise ValueError('CPU evidence differs')
        passed_tests(row['path'],row['expected_tests'])
    actual=json.loads(Path(c['actual_CPU']['path']).read_text())
    if (not actual['all_checks_passed'] or not all(actual['checks'].values())
            or actual['maximum_logit_difference']!=0 or actual['actual_candidate_parameters']!=10067764
            or actual['original_parent']!=c['parent']):
        raise ValueError('Actual10M original-function and active-cache CPU qualification required')
    prior=json.loads(Path(c['prior_completion']['path']).read_text())
    if (alive(prior['actual_identity']) or not prior['cumulative_GPU_ledger_closed']
            or prior['cumulative_technical_GPU_seconds']!=c['prior_technical_GPU_seconds']
            or prior['original_technical_cap_seconds']!=180 or prior['original_total_GPU_cap_seconds']!=4800):
        raise ValueError('Exited previous profile and ALL carried original cumulative budget required')
    old=json.loads(Path(c['accepted_config']['path']).read_text())
    stat=Path(c['parent']['path']).stat()
    if (old['parent']!=c['parent'] or c['parent']['sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size!=old['parent_size'] or stat.st_mtime_ns!=old['parent_mtime_ns']):
        raise ValueError('Previously hash-verified original parent size/mtime required')
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot owned gate exists; inspect actual process, never duplicate')
    return c


def build(c,parent,*,legacy=False,arm='independent_learned'):
    old=json.loads(Path(c['accepted_config']['path']).read_text())
    source=old['source_binding']
    codec=Tokenizer(ROOT/old['tokenizer'])
    sampler=OriginalTrainCorpusSampler(source['pool'],source['manifest_sha256'],codec,old['goals'],seed=42)
    if sampler.binding!=source: raise ValueError('Original accepted TRAIN source differs')
    binding=dict(parent=c['parent'],source_binding=source,weights_role='verification_only',protocol='owned_independent_QK_rank8_v1')
    if legacy: return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42)
    return IndependentMapTrainer(parent,sampler,binding,batch=48,device='cuda',seed=42,arm=arm)


def cache_gate(model,ids):
    mode,before=model.training,host(rng_state())
    try:
        model.eval()
        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',enabled=False):
            full=model(ids,use_cache=True)
            prefix=model(ids[:,:32],use_cache=True)
            cached=model(ids[:,32:],cache=prefix.cache,use_cache=True)
        return cache_observations(full,cached,equal_state(before,host(rng_state())))
    finally: model.train(mode)


def capacity(model,window):
    model.zero_grad(set_to_none=True)
    before=weights_digest(dict(model=host(model.state_dict())))
    torch.cuda.reset_peak_memory_stats()
    ids=torch.tensor([window['input_ids']]*48,device='cuda')
    targets=torch.tensor([window['target_ids']]*48,device='cuda')
    if ids.shape!=(48,1024) or int(targets[0].ne(-100).sum())!=512: raise ValueError('Original48x1024/512 geometry required')
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
        hidden=model.right_padded_hidden(ids)
        selected=targets.ne(-100)
        loss=F.cross_entropy(model.lm_head(hidden[selected]).float(),targets[selected])
        loss.backward()
    grad=model.clip_grad_norm(1.,error_if_nonfinite=True)
    torch.cuda.synchronize()
    if (not torch.isfinite(loss) or not 0<float(grad)<float('inf')
            or weights_digest(dict(model=host(model.state_dict())))!=before):
        raise ValueError('Finite maximum backward and unchanged weights required')
    result=dict(passed=True,shape=[48,1024],physical_input_tokens=49152,teachers=24576,
        optimizer_updates=0,loss=float(loss.detach()),gradient_norm=float(grad),peak_VRAM_bytes=torch.cuda.max_memory_allocated())
    model.zero_grad(set_to_none=True)
    return result


def run(pin):
    c=inspect(pin)
    RUN.mkdir(parents=True,exist_ok=True)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=pin,cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json',job)
    started=result=None
    updates=teachers=0
    def check(*args):
        if args or (started is not None and time.monotonic()-started+c['prior_technical_GPU_seconds']>180):
            raise TimeoutError('Original cumulative180s technical ceiling exceeded')
    def beat(stage):
        check()
        job.update(status='running',stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def learn(t):
        nonlocal updates,teachers
        check()
        row=t.step()
        updates+=1
        teachers+=row['CE_targets_this_update']
        return row
    def clear():
        gc.collect()
        torch.cuda.empty_cache()
    try:
        with gpu_lock('cuda'):
            started=time.monotonic()
            signal.signal(signal.SIGTERM,check)
            signal.signal(signal.SIGINT,check)
            memory=configure_resident_memory(0)
            parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
            window=json.loads(Path(c['capacity_payload']['path']).read_text())['window']
            plain=[i for i in window['input_ids'] if 8<=i<4096]
            ids=torch.tensor([[2]+plain[:63],[2]+plain[63:126]],device='cuda')
            full=build(c,parent)
            zero=host(full.state_dict())
            initial_weights=weights_digest(zero)
            full.save(RUN/'verification_zero.pt')
            beat('capacity_FIRST_no_Adam')
            job['capacity']=capacity(full.model,window)
            if job['capacity']['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Maximum shape exceeds resident allowance')
            full.sampler.handle.close()
            del full
            clear()
            beat('disabled_zero_vs_native3')
            disabled=build(c,parent,arm='disabled_zero')
            initial=host(disabled.state_dict())
            with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',enabled=False):
                disabled_logits=disabled.model(ids).logits.cpu()
            disabled_rows=[]
            snapshots=[]
            for _ in range(3):
                disabled_rows.append(learn(disabled))
                snapshots.append(host(disabled.state_dict()))
            disabled.sampler.handle.close()
            del disabled
            clear()
            native=build(c,parent,legacy=True)
            baseline=host(native.state_dict())
            with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',enabled=False):
                native_logits=native.model(ids).logits.cpu()
            if (not torch.equal(disabled_logits,native_logits)
                    or not all(torch.equal(initial['model'][k],v) for k,v in baseline['model'].items())
                    or not all(equal_state(initial[k],baseline[k]) for k in ('sampler','scheduler','RNG'))):
                raise ValueError('Actual original function/weights/RNG/source conversion parity failed')
            for index in range(3):
                row=learn(native)
                candidate=snapshots[index]
                record={k:equal_state(disabled_rows[index][k],row[k]) for k in ('CE_loss','gradient_norm',
                        'token_digest','source_teachers','source_EOS','physical_input_tokens','CE_input_tokens',
                        'original_body_bytes','draw_trace','lr')}
                actual_native=host(native.state_dict())
                record['original_model_weights_exact']=all(torch.equal(candidate['model'][k],v) for k,v in actual_native['model'].items())
                for k in ('sampler','scheduler','RNG'):
                    record[k+'_exact']=equal_state(candidate[k],actual_native[k])
                # Match Adam by parameter NAME, never shifted parameter identifiers.
                with torch.device('meta'): descriptor=IndependentMapModel(candidate['model_config'])
                identifier=dict(zip((n for n,_ in descriptor.named_parameters()),candidate['optimizer']['param_groups'][0]['params'],strict=True))
                original_Adam={name:equal_state(candidate['optimizer']['state'][identifier[name]],host(native.optimizer.state[p]))
                               for name,p in native.model.named_parameters()}
                record['original_Adam_all_coordinates_exact']=all(original_Adam.values())
                record['different_Adam_names']=[n for n,ok in original_Adam.items() if not ok]
                job.setdefault('disabled_native3_subchecks',[]).append(record)
                atomic_json(RUN/'job.json',job)
                if not all(v for k,v in record.items() if k!='different_Adam_names'):
                    raise ValueError('Disabled branch changed actual native3 learning: '+repr(record))
            job['native_initial_and_disabled3_all_original_weights_Adam_CE_stream_exact']=True
            native.sampler.handle.close()
            del native,snapshots
            clear()
            beat('learned_continuous6')
            full=build(c,parent)
            history=[learn(full) for _ in range(6)]
            expected=host(full.state_dict())
            activity={n:dict(change=float((p.detach().cpu()-zero['model'][n]).abs().max()),
                Adam_moment_abs_max=float(full.optimizer.state[p]['exp_avg'].abs().max()),
                gradient_abs_max=float(p.grad.abs().max())) for n,p in full.model.named_parameters() if extra_parameter(n)}
            if len(activity)!=52 or any(not all(math.isfinite(v) and v>0 for v in r.values()) for r in activity.values()):
                raise ValueError('All52 independent coefficient/down/Q2/K2 tensors must learn: '+repr(activity))
            job['all52_new_projection_and_coefficient_tensors_active']=activity
            full.sampler.handle.close()
            del full
            clear()
            split=build(c,parent)
            actual=[learn(split) for _ in range(3)]
            split.save(RUN/'verification_split.pt')
            split.sampler.handle.close()
            del split
            clear()
            resumed=build(c,parent)
            resumed.load(RUN/'verification_split.pt')
            actual.extend(learn(resumed) for _ in range(3))
            strip=lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
            if not equal_state(expected,host(resumed.state_dict())) or not equal_state([strip(r) for r in history],[strip(r) for r in actual]):
                raise ValueError('Actual learned6 vs3+save3 fullstate/history mismatch')
            job['full_state_history_resume_exact']=True
            resumed.save(RUN/'verification6_before_cache.pt')
            job['verification6_snapshot']=dict(path=str(RUN/'verification6_before_cache.pt'),sha256=sha256(RUN/'verification6_before_cache.pt'))
            beat('actual_learned6_FP32_cache')
            job['active_cache']=cache_gate(resumed.model,ids)
            atomic_json(RUN/'job.json',job)
            if not job['active_cache']['passed']: raise ValueError('Original active cache gate failed; all subchecks retained')
            beat('steady32')
            timings=[learn(resumed) for _ in range(32)]
            resumed.save(RUN/'verification_final.pt')
            result=dict(status='complete',passed=True,capacity=job['capacity'],memory_policy=memory,
                initial_weights_sha256=initial_weights,initial_native_function_parity=True,
                disabled3_original_numeric_state_and_stream_exact=True,full_state_history_resume_exact=True,
                all52_new_tensors_active=activity,active_cache=job['active_cache'],verification6_snapshot=job['verification6_snapshot'],
                all32_timings=timings,scientific_forecast_seconds=forecast(timings),candidate_parameters=10067764,native_parameters=10001152)
            result['disabled_native3_subchecks']=job['disabled_native3_subchecks']
            resumed.sampler.handle.close()
            del resumed
            clear()
            check()
    except Exception as error:
        result=dict(status='failed',passed=False,error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc(),
            failed_stage=job.get('stage'),capacity=job.get('capacity'),active_cache=job.get('active_cache'),
            verification6_snapshot=job.get('verification6_snapshot'),new_tensor_activity=job.get('all52_new_projection_and_coefficient_tensors_active'))
        result['disabled_native3_subchecks']=job.get('disabled_native3_subchecks')
    finally:
        elapsed=0 if started is None else time.monotonic()-started
        if result is None: result=dict(status='failed',passed=False,error='No terminal evidence')
        cumulative=elapsed+c['prior_technical_GPU_seconds']
        if cumulative>180: result.update(status='failed',passed=False,error='Original technical180s interval exceeded')
        result.update(config_sha256=pin,actual_identity=identity(),GPU_occupancy_seconds=elapsed,
            cumulative_technical_GPU_seconds=cumulative,cumulative_GPU_ledger_closed=True,
            verification_optimizer_updates=updates,verification_main_CE_positions=teachers,
            scientific_teacher_positions=0,DEV_opened=False,TEST_opened=False,Base_qualified=False,Base_adopted=False,
            science_budget_eligible=bool(result['passed'] and result['scientific_forecast_seconds']+cumulative<=4800))
        job.update(status=result['status'],ended_at=now(),GPU_occupancy_seconds=elapsed,cumulative_technical_GPU_seconds=cumulative,cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json',result)
        atomic_json(RUN/'job.json',job)
    print(json.dumps({k:result.get(k) for k in ('status','passed','GPU_occupancy_seconds','cumulative_technical_GPU_seconds',
        'scientific_forecast_seconds','science_budget_eligible','failed_stage','error')}),flush=True)
    if not result['passed']: raise SystemExit(1)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('inspect','run'))
    parser.add_argument('--config-sha256',required=True)
    args=parser.parse_args()
    if args.action=='inspect':
        inspect(args.config_sha256)
        print('Independent rank8 original-parent CUDA preflight passed; no CUDA allocation')
    else: run(args.config_sha256)
