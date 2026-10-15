"""One owned paired25M feasibility gate; verification weights never enter science."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback
from urllib.request import urlopen

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.document_progress import ARMS,POLICY,COEFFICIENT,progress_targets,progress_loss
from jmicro.experiment import sha256,now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,rng_state
from document_progress_trainer import DocumentProgressTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host,right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from probe_context_likelihood import weights_digest,passed_tests

CONFIG = ROOT/'configs/phase6/document_progress_probe_20261015.json'
RUN = ROOT/'reports/phase6/document-progress-probe-20261015'
GOALS = dict(web=18750000,textbook=5000000,story=1250000)


def scope():
    return dict(kind='owned_native_document_progress_paired25M_CUDA_v1',batch=48,seed=42,
        GPU_ceiling_seconds=180,prior_technical_GPU_seconds=98.4736015520757,
        prior_completed_science_GPU_seconds=1976.4175308110425,
        prior_total_GPU_seconds=2074.8911323631182,maximum_cumulative_GPU_seconds=4800,
        timed_updates_each=32,continuous_updates_each=6,split_updates_each=[3,3],control_native_updates=3,
        capacity_shape=[48,1024],capacity_before_any_optimizer=True,arms=list(ARMS),
        native_parameters=10001152,train_only_parameters=256,training_parameters=10001408,
        main_teacher_goal_each=25000000,goals=GOALS,progress_policy=POLICY,
        evaluation_save_reserve_each_seconds=600,preserve_actual6_and_all_cache_subchecks=True,
        new_matched_control_required=True,cached100M_is_matched25M_control=False,
        scientific_teacher_positions=0,TEST_prepared=False,Base_adopted=False)


def assert_scope(c):
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in scope().items()):
        raise ValueError('Exact paired25M/native scalar objective and original cumulative180/4800 scope required')


def forecast(rows):
    if (len(rows) != 32 or any(type(r.get('CE_targets_this_update')) is not int
            or r['CE_targets_this_update'] <= 0 or not isinstance(r.get('seconds'),(int,float))
            or not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in rows)):
        raise ValueError('ALL32 positive durations and actual main teacher counts required')
    return math.ceil(25000000*sum(r['seconds'] for r in rows)
        /sum(r['CE_targets_this_update'] for r in rows)*1.3+600)


def budget_eligible(passed,forecasts,new_seconds):
    return bool(passed and set(forecasts) == set(ARMS) and all(type(v) is int and v >= 600 for v in forecasts.values())
        and math.isfinite(new_seconds) and 0 <= new_seconds
        and new_seconds+scope()['prior_technical_GPU_seconds'] <= 180
        and sum(forecasts.values())+new_seconds+scope()['prior_total_GPU_seconds'] <= 4800)


def cache_observations(full,cached,rng_equal):
    a,b = full.logits[:,-cached.logits.shape[1]:],cached.logits
    if a.shape != b.shape or len(full.cache.layers) != len(cached.cache.layers) or not full.cache.layers:
        raise ValueError('Matching original native suffix and all real KV layers required')
    close = torch.isclose(a,b,atol=3e-5,rtol=2e-5)
    kv = [dict(layer=i,kind=kind,maximum_difference=float((x-y).abs().max()),
        within_original_tolerance=torch.allclose(x,y,atol=3e-5,rtol=2e-5),
        real_tokens_only=x.shape[2] == y.shape[2] == full.cache.valid.shape[1])
        for i,(pair,want) in enumerate(zip(full.cache.layers,cached.cache.layers,strict=True))
        for kind,x,y in zip(('K','V'),pair,want,strict=True)]
    checks = dict(finite_logits=bool(torch.isfinite(a).all() and torch.isfinite(b).all()),
        logits_within_original_tolerance=bool(close.all()),
        all_native_KV_within_original_tolerance=all(r['within_original_tolerance'] for r in kv),
        real_cache_length=all(r['real_tokens_only'] for r in kv),
        positions_exact=torch.equal(full.cache.positions,cached.cache.positions),
        validity_exact=torch.equal(full.cache.valid,cached.cache.valid),RNG_unchanged=bool(rng_equal))
    bad = []
    for index in (~close).nonzero()[:8].cpu().tolist():
        key = tuple(index)
        bad.append(dict(index=index,full_value=float(a[key]),cached_value=float(b[key]),
            absolute_difference=float((a[key]-b[key]).abs()),allowed_error=float(3e-5+2e-5*b[key].abs())))
    return dict(passed=all(checks.values()),subchecks=checks,absolute_tolerance=3e-5,relative_tolerance=2e-5,
        maximum_logit_difference=float((a-b).abs().max()),outside_original_logit_tolerance=int((~close).sum()),
        first_eight_outside=bad,native_KV=kv)


def cache_gate(model,ids):
    mode,before = model.training,host(rng_state())
    try:
        model.eval()
        with torch.no_grad(),sdpa_kernel(SDPBackend.MATH),torch.autocast('cuda',enabled=False):
            full = model(ids,use_cache=True)
            prefix = model(ids[:,:32],use_cache=True)
            cached = model(ids[:,32:],cache=prefix.cache,use_cache=True)
        return cache_observations(full,cached,equal_state(before,host(rng_state())))
    finally:
        model.train(mode)


def native_subchecks(candidate,native,candidate_row,native_row):
    result = {key:equal_state(candidate_row[key],native_row[key]) for key in ('CE_loss','gradient_norm',
        'token_digest','source_teachers','source_EOS','physical_input_tokens','CE_input_tokens',
        'original_body_bytes','draw_trace','lr')}
    result['original_model_weights_exact'] = equal_state(candidate['model'],native['model'])
    for key in ('sampler','scheduler','RNG'):
        result[key+'_exact'] = equal_state(candidate[key],native[key])
    cids = candidate['optimizer']['param_groups'][0]['params'][:-1]
    nids = native['optimizer']['param_groups'][0]['params']
    result['original_Adam_coordinates_exact'] = len(cids) == len(nids) and all(
        equal_state(candidate['optimizer']['state'][a],native['optimizer']['state'][b])
        for a,b in zip(cids,nids,strict=True))
    result['control_head_zero'] = bool(torch.count_nonzero(candidate['progress_head']['weight']) == 0)
    return result


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('Externally pinned technical config required')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen source differs: '+path)
    for key in ('proposal','CPU_readiness','accepted_config','capacity_payload','tokenizer','prior_completion'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Pinned CPU evidence differs')
        passed_tests(row['path'],row['expected_tests'])
    ready = json.loads(Path(c['CPU_readiness']['path']).read_text())
    for path,digest in ready['artifacts_sha256'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('CPU milestone differs: '+path)
    if (ready['CPU_label_head_checks'] != 23 or ready['CPU_real_Adam_trainer_fixture_checks'] != 21
            or not ready['CPU_both_arms6_vs3_save3_fullstate_history_exact']
            or not ready['CPU_control4_native_weights_Adam_by_name_CE_gradient_schedule_RNG_source_exact']
            or ready['inference_parameters'] != 10001152 or ready['each_training_total_parameters'] != 10001408
            or ready['carried_total_GPU_seconds'] != c['prior_total_GPU_seconds']):
        raise ValueError('Exact CPU native/head/fullstate evidence required')
    prior = json.loads(Path(c['prior_completion']['path']).read_text())
    if (alive(prior['actual_terminal_and_UI_proof']['technical_identity'])
            or not prior['cumulative_GPU_ledger_closed'] or not prior['fixed_condition_closed']
            or prior['cumulative_technical_GPU_seconds'] != c['prior_technical_GPU_seconds']
            or prior['prior_completed_science_GPU_seconds'] != c['prior_completed_science_GPU_seconds']
            or prior['cumulative_total_GPU_seconds'] != c['prior_total_GPU_seconds']):
        raise ValueError('Exited prior job and ALL spent technical/science seconds required')
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    stat = Path(c['parent']['path']).stat()
    if (old['parent'] != c['parent'] or c['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != old['parent_size'] or stat.st_mtime_ns != old['parent_mtime_ns']):
        raise ValueError('Accepted original parent hash binding/size/mtime required')
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot probe exists; inspect actual handle, never duplicate')
    return c


def observe_ui():
    saved = json.loads((ROOT/'reports/local/webui/server.json').read_text())
    if not alive(saved):
        raise ValueError('Saved original UI is not actually alive')
    with urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:
        ui = json.load(response)
    if (ui['busy'] or ui['parameters'] != 10001152
            or ui['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or ui['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
        raise ValueError('Actually running original idle UI identity required')
    lock = Path(os.environ.get('JMICRO_DATA_ROOT',str(Path.home()/'jmicro-data')))/'gpu.lock'
    stat = lock.stat()
    inode = f'{os.major(stat.st_dev):02x}:{os.minor(stat.st_dev):02x}:{stat.st_ino}'
    rows = [line for line in Path('/proc/locks').read_text().splitlines()
        if inode in line and 'FLOCK' in line and f'WRITE {saved["pid"]} ' in line]
    if len(rows) != 1:
        raise ValueError('Actual original UI kernel FLOCK on expected inode required')
    result = dict(observed_at=now(),identity=identity(saved['pid']),HTTP=ui,lock_inode=inode,kernel_FLOCK=rows)
    atomic_json(ROOT/'reports/phase6/document-progress-probe-launcher-20261015/UI_observation.json',result)
    return result


def build(c,parent,arm='document_progress',legacy=False):
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    source = old['source_binding']
    codec = Tokenizer(ROOT/old['tokenizer'])
    sampler = OriginalTrainCorpusSampler(source['pool'],source['manifest_sha256'],codec,GOALS,seed=42)
    if sampler.binding != source:
        raise ValueError('Original accepted TRAIN source differs')
    binding = dict(parent=c['parent'],source_binding=source,weights_role='verification_only',protocol='owned_document_progress_paired25M_v1')
    if legacy:
        return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42)
    return DocumentProgressTrainer(parent,sampler,binding,batch=48,device='cuda',seed=42,arm=arm)


def capacity(trainer,payload):
    window = dict(payload['window'],original_body_tokens=payload['original_record']['body_tokens'])
    labels = progress_targets([window])[0]
    trainer.optimizer.zero_grad(set_to_none=True)
    before = dict(model=host(trainer.model.state_dict()),head=host(trainer.progress_head.state_dict()),RNG=host(rng_state()))
    torch.cuda.reset_peak_memory_stats()
    ids = torch.tensor([window['input_ids']]*48,device='cuda')
    targets = torch.tensor([window['target_ids']]*48,device='cuda')
    fractions = torch.tensor([labels]*48,device='cuda',dtype=torch.float32)
    if ids.shape != (48,1024) or int(targets[0].ne(-100).sum()) != 512:
        raise ValueError('Original maximum48x1024 and512 selected teachers required')
    enabled = trainer.spec['progress_arm'] == 'document_progress'
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
        hidden = right_padded_hidden(trainer.model,ids)
        selected = targets.ne(-100)
        ce = F.cross_entropy(trainer.model.lm_head(hidden[selected]).float(),targets[selected])
        auxiliary = progress_loss(trainer.progress_head(hidden[selected]),fractions[selected])
        loss = ce+COEFFICIENT*(auxiliary if enabled else auxiliary*0.)
        loss.backward()
    gradient = torch.nn.utils.clip_grad_norm_(trainer.all_parameters if enabled else list(trainer.model.parameters()),1.,error_if_nonfinite=True)
    torch.cuda.synchronize()
    unchanged = (equal_state(before['model'],host(trainer.model.state_dict()))
        and equal_state(before['head'],host(trainer.progress_head.state_dict()))
        and equal_state(before['RNG'],host(rng_state())))
    if (not all(torch.isfinite(v) for v in (ce,auxiliary,loss)) or not 0 < float(gradient) < float('inf')
            or not unchanged or trainer.optimizer.state or trainer.counters['update'] != 0):
        raise ValueError('Finite capacity backward/no Adam/no weights or RNG mutation required')
    result = dict(passed=True,shape=[48,1024],main_teachers=24576,scalar_labels=24576,
        optimizer_updates=0,loss=float(loss.detach()),gradient_norm=float(gradient),
        weights_RNG_unchanged=unchanged,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
        original_body_tokens=window['original_body_tokens'])
    trainer.optimizer.zero_grad(set_to_none=True)
    return result


def run(pin):
    c = inspect(pin)
    RUN.mkdir(parents=True,exist_ok=True)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    job = dict(status='starting',**identity(),started_at=now(),config_sha256=pin,cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json',job)
    started = result = None
    updates = teachers = 0
    forecasts,arm_results,capacities = {},{},{}
    def check(*args):
        if args or (started is not None and time.monotonic()-started+c['prior_technical_GPU_seconds'] > 180):
            raise TimeoutError('Original cumulative180s technical ceiling exceeded')
    def beat(stage):
        check()
        job.update(status='running',stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def learn(trainer):
        nonlocal updates,teachers
        check()
        row = trainer.step()
        updates += 1
        teachers += row['CE_targets_this_update']
        return row
    def dispose(trainer):
        trainer.sampler.handle.close()
    def clear():
        gc.collect()
        torch.cuda.empty_cache()
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM,check)
            signal.signal(signal.SIGINT,check)
            memory = configure_resident_memory(0)
            parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
            payload = json.loads(Path(c['capacity_payload']['path']).read_text())
            plain = [i for i in payload['window']['input_ids'] if 8 <= i < 4096]
            ids = torch.tensor([[2]+plain[:63],[2]+plain[63:126]],device='cuda')
            # BOTH maximum backwards precede the FIRST Adam update anywhere.
            initial_core = initial_rng = None
            for arm in ARMS:
                beat(arm+'_capacity_FIRST_no_Adam')
                trainer = build(c,parent,arm)
                zero = host(trainer.state_dict())
                if initial_core is None:
                    initial_core,initial_rng = zero['model'],zero['RNG']
                elif not equal_state(initial_core,zero['model']) or not equal_state(initial_rng,zero['RNG']):
                    raise ValueError('Both fresh core weights/RNG must be exact before capacity')
                if (zero['spec']['native_parameters'] != 10001152 or zero['spec']['train_only_parameters'] != 256
                        or zero['spec']['total_training_parameters'] != 10001408):
                    raise ValueError('Actual training/native parameter count differs')
                trainer.save(RUN/(arm+'_verification_zero.pt'))
                capacities[arm] = capacity(trainer,payload)
                job['capacities'] = capacities
                atomic_json(RUN/'job.json',job)
                if capacities[arm]['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']:
                    raise ValueError('Maximum shape exceeds resident allowance')
                dispose(trainer)
                del trainer,zero
                clear()
            beat('control_native3')
            trainer = build(c,parent,'native_CE_control')
            snapshots,control_rows = [],[]
            for _ in range(3):
                control_rows.append(learn(trainer))
                snapshots.append(host(trainer.state_dict()))
            dispose(trainer)
            del trainer
            clear()
            trainer = build(c,parent,legacy=True)
            if not equal_state(initial_core,host(trainer.model.state_dict())) or not equal_state(initial_rng,host(rng_state())):
                raise ValueError('Actual native initial weights/RNG changed')
            for i in range(3):
                row = learn(trainer)
                checks = native_subchecks(snapshots[i],host(trainer.state_dict()),control_rows[i],row)
                job.setdefault('control_native3_subchecks',[]).append(checks)
                atomic_json(RUN/'job.json',job)
                if not all(checks.values()):
                    raise ValueError('Actual original-coordinate control/native3 mismatch: '+repr(checks))
            dispose(trainer)
            del trainer,snapshots,control_rows
            clear()
            paired_clocks = None
            for arm in ARMS:
                beat(arm+'_continuous6')
                trainer = build(c,parent,arm)
                history = [learn(trainer) for _ in range(6)]
                expected = host(trainer.state_dict())
                if equal_state(initial_core,expected['model']):
                    raise ValueError('No core learning in actual6')
                if arm == 'document_progress' and (not all(r['head_gradient_abs_max_after_clip'] > 0 for r in history)
                        or not all(r['head_weight_abs_max'] > 0 for r in history)):
                    raise ValueError('Scalar head did not learn on every actual update')
                dispose(trainer)
                del trainer
                clear()
                trainer = build(c,parent,arm)
                actual = [learn(trainer) for _ in range(3)]
                trainer.save(RUN/(arm+'_verification_split.pt'))
                dispose(trainer)
                del trainer
                clear()
                trainer = build(c,parent,arm)
                trainer.load(RUN/(arm+'_verification_split.pt'))
                actual.extend(learn(trainer) for _ in range(3))
                strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
                if (not equal_state(expected,host(trainer.state_dict()))
                        or not equal_state([strip(r) for r in history],[strip(r) for r in actual])):
                    raise ValueError('Actual BOTH arms6vs3+save3 fullstate/history must be exact: '+arm)
                snapshot = RUN/(arm+'_verification6_before_cache.pt')
                trainer.save(snapshot)
                arm_results[arm] = dict(full_state_history_resume_exact=True,
                    verification6_snapshot=dict(path=str(snapshot),sha256=sha256(snapshot)),actual6_history=history)
                job['arms'] = arm_results
                beat(arm+'_actual6_native_FP32_cache')
                arm_results[arm]['active_cache'] = cache_gate(trainer.model,ids)
                atomic_json(RUN/'job.json',job)
                if not arm_results[arm]['active_cache']['passed']:
                    raise ValueError('Original native actual6 cache gate failed: '+arm)
                beat(arm+'_ALL32_timings')
                timings = [learn(trainer) for _ in range(32)]
                arm_results[arm]['all32_timings'] = timings
                forecasts[arm] = forecast(timings)
                arm_results[arm]['scientific_forecast_seconds'] = forecasts[arm]
                state = host(trainer.state_dict())
                keys = ('source_teachers','source_EOS','supervised_tokens','CE_input_tokens','physical_input_tokens',
                    'original_body_bytes','token_digest','progress_label_positions','progress_target_digest','progress_target_sum')
                clocks = dict(sampler=state['sampler'],counters={k:state['counters'][k] for k in keys})
                if paired_clocks is None:
                    paired_clocks = clocks
                elif not equal_state(paired_clocks,clocks):
                    raise ValueError('Both actual38 original source/teacher/scalar label streams differ')
                trainer.save(RUN/(arm+'_verification_final.pt'))
                dispose(trainer)
                del trainer,expected,state
                clear()
                atomic_json(RUN/'job.json',job)
                check()
            result = dict(status='complete',passed=True,capacities=capacities,memory_policy=memory,
                initial_native_weights_sha256=weights_digest(dict(model=initial_core)),
                actual_parameter_counts=dict(native=10001152,train_only=256,training=10001408),
                arms=arm_results,scientific_forecast_each_seconds=forecasts,
                scientific_forecast_paired_seconds=sum(forecasts.values()),paired38_stream_clocks_exact=True)
    except Exception as error:
        result = dict(status='failed',passed=False,error_type=type(error).__name__,error=str(error),
            traceback=traceback.format_exc(),failed_stage=job.get('stage'),capacities=capacities,arms=arm_results)
    finally:
        elapsed = 0 if started is None else time.monotonic()-started
        if result is None:
            result = dict(status='failed',passed=False,error='No terminal evidence')
        if elapsed+c['prior_technical_GPU_seconds'] > 180 or elapsed+c['prior_total_GPU_seconds'] > 4800:
            result.update(status='failed',passed=False,error='Original cumulative GPU interval exceeded')
        result.update(config_sha256=pin,actual_identity=identity(),GPU_occupancy_seconds=elapsed,
            prior_completed_science_GPU_seconds=c['prior_completed_science_GPU_seconds'],
            cumulative_technical_GPU_seconds=elapsed+c['prior_technical_GPU_seconds'],
            cumulative_total_GPU_seconds=elapsed+c['prior_total_GPU_seconds'],cumulative_GPU_ledger_closed=True,
            control_native3_subchecks=job.get('control_native3_subchecks',[]),verification_optimizer_updates=updates,
            verification_main_CE_positions=teachers,scientific_teacher_positions=0,DEV_opened=False,TEST_opened=False,
            Base_qualified=False,Base_adopted=False,science_budget_eligible=budget_eligible(result['passed'],forecasts,elapsed))
        job.update(status=result['status'],ended_at=now(),GPU_occupancy_seconds=elapsed,
            cumulative_technical_GPU_seconds=result['cumulative_technical_GPU_seconds'],
            cumulative_total_GPU_seconds=result['cumulative_total_GPU_seconds'],cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json',result)
        atomic_json(RUN/'job.json',job)
    print(json.dumps({k:result.get(k) for k in ('status','passed','GPU_occupancy_seconds','cumulative_technical_GPU_seconds',
        'cumulative_total_GPU_seconds','scientific_forecast_paired_seconds','science_budget_eligible','failed_stage','error')}),flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('inspect','observe-ui','run'))
    parser.add_argument('--config-sha256',required=True)
    args = parser.parse_args()
    if args.action == 'inspect':
        inspect(args.config_sha256)
        print('Paired25M native scalar progress preflight passed; no CUDA allocation')
    elif args.action == 'observe-ui':
        inspect(args.config_sha256)
        print(json.dumps(observe_ui()))
    else:
        run(args.config_sha256)
