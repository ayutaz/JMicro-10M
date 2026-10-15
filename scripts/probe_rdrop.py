"""One owned normalized RDrop25M CUDA gate; carry all prior costs."""
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
from urllib.request import urlopen

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.rdrop import POLICY,two_view_objective
from jmicro.experiment import sha256,now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,rng_state
from rdrop_trainer import RDropTrainer
from document_progress_trainer import DocumentProgressTrainer
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host,right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from probe_context_likelihood import weights_digest,passed_tests
from probe_document_progress import cache_gate,GOALS

CONFIG = ROOT/'configs/phase6/rdrop_probe_20261015.json'
RUN = ROOT/'reports/phase6/rdrop-probe-20261015'


def scope():
    return dict(kind='owned_normalized_two_view_RDrop25M_CUDA_v1',batch=48,seed=42,policy=POLICY,
        GPU_ceiling_seconds=180,maximum_cumulative_GPU_seconds=4800,
        prior_technical_GPU_seconds=116.9417824720731,prior_completed_science_GPU_seconds=2946.1623015810037,
        prior_total_GPU_seconds=3063.104084053077,capacity_shape=[48,1024],retained_decoder_graphs=2,
        capacity_before_any_optimizer=True,native_parameters=10001152,training_parameters=10001152,
        train_only_parameters=0,timed_updates=32,continuous_updates=6,split_updates=[3,3],
        disabled_native_updates=3,cached_zero_head_control_updates=3,main_teacher_goal=25000000,goals=GOALS,
        evaluation_save_reserve_seconds=600,preserve_actual6_and_all_cache_subchecks=True,
        reuse_control_main_teachers=25000000,cached100M_is_matched25M_control=False,
        scientific_teacher_positions=0,TEST_prepared=False,Base_adopted=False)


def assert_scope(c):
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in scope().items()):
        raise ValueError('Exact retained-two-graph RDrop25M/original180/4800 scope required')


def forecast(rows):
    if (len(rows) != 32 or any(type(r.get('CE_targets_this_update')) is not int
            or r['CE_targets_this_update'] <= 0 or not isinstance(r.get('seconds'),(int,float))
            or not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in rows)):
        raise ValueError('ALL32 actual main-teacher counts and positive step durations required')
    return math.ceil(25000000*sum(r['seconds'] for r in rows)/sum(r['CE_targets_this_update'] for r in rows)*1.3+600)


def eligible(passed,science,new_seconds):
    return bool(passed and type(science) is int and science >= 600 and math.isfinite(new_seconds)
        and new_seconds >= 0 and new_seconds+scope()['prior_technical_GPU_seconds'] <= 180
        and science+new_seconds+scope()['prior_total_GPU_seconds'] <= 4800)


def original_match(actual,reference,row,want):
    checks = {k:equal_state(row[k],want[k]) for k in ('CE_loss','gradient_norm','token_digest',
        'source_teachers','source_EOS','physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr')}
    checks['model_config_exact'] = actual['model_config'] == reference['model_config']
    checks['original_weights_exact'] = equal_state(actual['model'],reference['model'])
    for key in ('sampler','scheduler','RNG'):
        checks[key+'_exact'] = equal_state(actual[key],reference[key])
    ag,rg = actual['optimizer']['param_groups'][0],reference['optimizer']['param_groups'][0]
    ids = rg['params'][:-1] if 'progress_head' in reference else rg['params']
    checks['original_Adam_coordinates_exact'] = len(ag['params']) == len(ids) and all(
        equal_state(actual['optimizer']['state'][a],reference['optimizer']['state'][b])
        for a,b in zip(ag['params'],ids,strict=True))
    checks['original_Adam_hyperparameters_exact'] = {k:v for k,v in ag.items() if k != 'params'} == {k:v for k,v in rg.items() if k != 'params'}
    if 'progress_head' in reference:
        checks['cached_protocol_head_zero_no_learning'] = bool(torch.count_nonzero(reference['progress_head']['weight']) == 0
            and reference['counters']['progress_learning_positions'] == 0)
        extra = reference['optimizer']['state'][rg['params'][-1]]
        checks['cached_protocol_head_Adam_zero'] = bool(torch.count_nonzero(extra['exp_avg']) == 0
            and torch.count_nonzero(extra['exp_avg_sq']) == 0 and float(extra['step']) == reference['counters']['update'])
    return checks


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('External frozen config hash required')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen source differs: '+path)
    for key in ('proposal','CPU_readiness','actual_CPU','accepted_config','capacity_payload','tokenizer',
            'prior_completion','cached_control_training','cached_control_config'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned evidence differs: '+key)
    ready = json.loads(Path(c['CPU_readiness']['path']).read_text())
    for path,digest in ready['artifacts_sha256'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('CPU milestone differs: '+path)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('CPU evidence differs')
        passed_tests(row['path'],row['expected_tests'])
    actual = json.loads(Path(c['actual_CPU']['path']).read_text())
    if (ready['CPU_unique_checks_total'] != 47 or not ready['CPU_both6_vs3_save3_ALL_state_history_stochastic_RNG_exact']
            or not ready['CPU_old_zero_head_CE_control4_all_original_Adam_coordinates_exact']
            or not actual['all_checks_passed'] or not all(actual['checks'].values())
            or actual['actual_native_parameters'] != 10001152 or actual['actual_training_parameters'] != 10001152):
        raise ValueError('Real parent/native inference/two graph/CPU state evidence required')
    prior = json.loads(Path(c['prior_completion']['path']).read_text())
    if (alive(prior['actual_terminal_and_UI_proof']['scientific_identity'])
            or not prior['cumulative_GPU_ledger_closed'] or not prior['fixed_condition_closed']
            or prior['cumulative_technical_GPU_seconds'] != c['prior_technical_GPU_seconds']
            or prior['cumulative_completed_science_GPU_seconds'] != c['prior_completed_science_GPU_seconds']
            or prior['cumulative_total_GPU_seconds'] != c['prior_total_GPU_seconds']):
        raise ValueError('Exited prior science and EVERY spent technical/science second required')
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    stat = Path(c['parent']['path']).stat()
    if (old['parent'] != c['parent'] or c['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or stat.st_size != old['parent_size'] or stat.st_mtime_ns != old['parent_mtime_ns']):
        raise ValueError('Accepted original parent hash binding and size/mtime required')
    cached = json.loads(Path(c['cached_control_training']['path']).read_text())
    cfg = json.loads(Path(c['cached_control_config']['path']).read_text())
    if (cached['spec']['progress_arm'] != 'native_CE_control' or cached['spec']['goals'] != GOALS
            or cached['spec']['batch'] != 48 or cached['spec']['seed'] != 42 or cached['spec']['contrast'] is not False
            or cached['counters']['supervised_tokens'] != 25000000 or cached['counters']['progress_learning_positions'] != 0
            or cfg['parent'] != c['parent'] or cfg['source_binding'] != old['source_binding']
            or cached['binding']['config_sha256'] != c['cached_control_config']['sha256']):
        raise ValueError('Exact prior native CE25M metadata, not a100M or active-head control required')
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot gate exists; inspect actual job, never duplicate')
    return c


def observe_ui():
    saved = json.loads((ROOT/'reports/local/webui/server.json').read_text())
    if not alive(saved):
        raise ValueError('Original UI is not actually alive')
    with urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:
        ui = json.load(response)
    if (ui['busy'] or ui['parameters'] != 10001152
            or ui['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or ui['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
        raise ValueError('Original idle native parent/Tokenizer HTTP required')
    stat = (Path(os.environ.get('JMICRO_DATA_ROOT',str(Path.home()/'jmicro-data')))/'gpu.lock').stat()
    inode = f'{os.major(stat.st_dev):02x}:{os.minor(stat.st_dev):02x}:{stat.st_ino}'
    rows = [r for r in Path('/proc/locks').read_text().splitlines()
        if inode in r and 'FLOCK' in r and f'WRITE {saved["pid"]} ' in r]
    if len(rows) != 1:
        raise ValueError('Actual original UI kernel FLOCK required')
    out = dict(observed_at=now(),identity=identity(saved['pid']),HTTP=ui,actual_lock_inode=inode,kernel_FLOCK=rows)
    atomic_json(ROOT/'reports/phase6/rdrop-probe-launcher-20261015/UI_observation.json',out)
    return out


def build(c,parent,arm='normalized_rdrop'):
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    source = old['source_binding']
    codec = Tokenizer(ROOT/old['tokenizer'])
    sampler = OriginalTrainCorpusSampler(source['pool'],source['manifest_sha256'],codec,GOALS,seed=42)
    if sampler.binding != source:
        raise ValueError('Original accepted TRAIN binding differs')
    binding = dict(parent=c['parent'],source_binding=source,weights_role='verification_only',protocol='owned_normalized_RDrop25M_v1')
    if arm == 'native':
        return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42)
    if arm == 'cached_zero_head_control':
        return DocumentProgressTrainer(parent,sampler,binding,batch=48,device='cuda',seed=42,arm='native_CE_control')
    return RDropTrainer(parent,sampler,binding,batch=48,device='cuda',seed=42,arm=arm)


def capacity(trainer,payload):
    window = payload['window']
    trainer.optimizer.zero_grad(set_to_none=True)
    before = host(trainer.model.state_dict())
    rng = host(rng_state())
    torch.cuda.reset_peak_memory_stats()
    ids = torch.tensor([window['input_ids']]*48,device='cuda')
    targets = torch.tensor([window['target_ids']]*48,device='cuda')
    selected = targets.ne(-100)
    if ids.shape != (48,1024) or int(selected.sum()) != 24576:
        raise ValueError('Original maximum48x1024 and512 selected targets each required')
    with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
        first = trainer.model.lm_head(right_padded_hidden(trainer.model,ids)[selected]).float()
        second = trainer.model.lm_head(right_padded_hidden(trainer.model,ids)[selected]).float()
        losses = two_view_objective(first,second,targets[selected])
        losses['combined_loss'].backward()
    norm = torch.nn.utils.clip_grad_norm_(trainer.model.parameters(),1.,error_if_nonfinite=True)
    torch.cuda.synchronize()
    checks = dict(finite_losses=all(bool(torch.isfinite(v)) for v in losses.values()),
        finite_nonzero_joint_gradient=0 < float(norm) < float('inf'),
        two_stochastic_views=not torch.equal(first,second),positive_symmetric_KL=float(losses['symmetric_KL']) > 0,
        dropout_RNG_advanced=not equal_state(rng,host(rng_state())),
        all_weights_unchanged=equal_state(before,host(trainer.model.state_dict())),
        Adam_zero=not trainer.optimizer.state and trainer.counters['update'] == 0)
    result = dict(passed=all(checks.values()),checks=checks,shape=[48,1024],retained_decoder_graphs=2,
        main_physical_input_tokens=49152,total_physical_input_tokens=98304,main_teachers=24576,
        total_CE_evaluations=49152,consistency_pairs=24576,optimizer_updates=0,
        losses={k:float(v.detach()) for k,v in losses.items()},gradient_norm=float(norm),
        peak_VRAM_bytes=torch.cuda.max_memory_allocated())
    trainer.optimizer.zero_grad(set_to_none=True)
    if not result['passed']:
        raise ValueError('Actual maximum two-view finite/backward/no-Adam checks failed: '+repr(checks))
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
    def check(*args):
        if args or (started is not None and time.monotonic()-started+c['prior_technical_GPU_seconds'] > 180):
            raise TimeoutError('Original cumulative180s technical ceiling exhausted')
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
            trainer = build(c,parent)
            initial = host(trainer.state_dict())
            initial_weights = weights_digest(initial)
            cached_config = json.loads(Path(c['cached_control_config']['path']).read_text())
            if (initial_weights != cached_config['initial_native_weights_sha256']
                    or initial['spec']['native_parameters'] != 10001152 or initial['spec']['training_parameters'] != 10001152):
                raise ValueError('Actual original native weights/count differ from cached CE25M protocol')
            trainer.save(RUN/'verification_zero.pt')
            job['capacity_requested'] = dict(shape=[48,1024],retained_decoder_graphs=2,before_any_Adam=True)
            beat('maximum_TWO_retained_graphs_FIRST_before_ANY_Adam')
            job['capacity'] = capacity(trainer,payload)
            atomic_json(RUN/'job.json',job)
            if job['capacity']['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']:
                raise ValueError('Two retained graph maximum exceeds resident allowance')
            trainer.sampler.handle.close()
            del trainer
            clear()
            beat('disabled_native3_then_original_and_cached_zero_head3')
            trainer = build(c,parent,'disabled_native')
            snapshots,rows = [],[]
            for _ in range(3):
                rows.append(learn(trainer))
                snapshots.append(host(trainer.state_dict()))
            trainer.sampler.handle.close()
            del trainer
            clear()
            for arm in ('native','cached_zero_head_control'):
                trainer = build(c,parent,arm)
                if (not equal_state(initial['model'],host(trainer.model.state_dict()))
                        or not equal_state(initial['RNG'],host(rng_state()))):
                    raise ValueError('Native/cached initial original weights or RNG differ')
                for i in range(3):
                    want = learn(trainer)
                    checks = original_match(snapshots[i],host(trainer.state_dict()),rows[i],want)
                    job.setdefault(arm+'3_subchecks',[]).append(checks)
                    atomic_json(RUN/'job.json',job)
                    if not all(checks.values()):
                        raise ValueError('Actual native/cached25M original-coordinate protocol differs: '+arm+repr(checks))
                trainer.sampler.handle.close()
                del trainer
                clear()
            del snapshots,rows
            beat('active_continuous6')
            trainer = build(c,parent)
            history = [learn(trainer) for _ in range(6)]
            expected = host(trainer.state_dict())
            if equal_state(initial['model'],expected['model']) or not all(r['symmetric_KL'] > 0
                    and r['different_view_positions_this_update'] > 0 for r in history):
                raise ValueError('No actual native learning or active two-view consistency')
            trainer.sampler.handle.close()
            del trainer
            clear()
            trainer = build(c,parent)
            actual = [learn(trainer) for _ in range(3)]
            trainer.save(RUN/'verification_split.pt')
            trainer.sampler.handle.close()
            del trainer
            clear()
            trainer = build(c,parent)
            trainer.load(RUN/'verification_split.pt')
            actual.extend(learn(trainer) for _ in range(3))
            strip = lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
            if (not equal_state(expected,host(trainer.state_dict()))
                    or not equal_state([strip(r) for r in history],[strip(r) for r in actual])):
                raise ValueError('Active6vs3+save3 ALL state/dropout RNG/source/history differs')
            job['full_state_history_resume_exact'] = True
            trainer.save(RUN/'verification6_before_cache.pt')
            job['verification6_snapshot'] = dict(path=str(RUN/'verification6_before_cache.pt'),sha256=sha256(RUN/'verification6_before_cache.pt'))
            beat('actual_saved6_native_FP32_cache_all_subchecks')
            job['active_cache'] = cache_gate(trainer.model,ids)
            atomic_json(RUN/'job.json',job)
            if not job['active_cache']['passed']:
                raise ValueError('Original actual6 native cache gate failed')
            beat('ALL32_original_main_teacher_timings')
            timings = [learn(trainer) for _ in range(32)]
            trainer.save(RUN/'verification_final.pt')
            result = dict(status='complete',passed=True,capacity=job['capacity'],memory_policy=memory,
                initial_native_weights_sha256=initial_weights,native_parameters=10001152,training_parameters=10001152,
                cached25M_original_coordinate_protocol_exact=True,full_state_history_resume_exact=True,
                actual6_history=history,active_cache=job['active_cache'],verification6_snapshot=job['verification6_snapshot'],
                all32_timings=timings,scientific_forecast_seconds=forecast(timings))
            trainer.sampler.handle.close()
            del trainer
            clear()
            check()
    except Exception as error:
        result = dict(status='failed',passed=False,error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc(),
            failed_stage=job.get('stage'),capacity_requested=job.get('capacity_requested'),capacity=job.get('capacity'),
            partial_peak_VRAM_bytes=torch.cuda.max_memory_allocated() if torch.cuda.is_initialized() else None,
            active_cache=job.get('active_cache'),verification6_snapshot=job.get('verification6_snapshot'))
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
            native3_subchecks=job.get('native3_subchecks',[]),cached_zero_head_control3_subchecks=job.get('cached_zero_head_control3_subchecks',[]),
            verification_optimizer_updates=updates,verification_main_CE_positions=teachers,scientific_teacher_positions=0,
            DEV_opened=False,TEST_opened=False,Base_qualified=False,Base_adopted=False,
            science_budget_eligible=eligible(result['passed'],result.get('scientific_forecast_seconds'),elapsed))
        job.update(status=result['status'],ended_at=now(),GPU_occupancy_seconds=elapsed,
            cumulative_technical_GPU_seconds=result['cumulative_technical_GPU_seconds'],
            cumulative_total_GPU_seconds=result['cumulative_total_GPU_seconds'],cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json',result)
        atomic_json(RUN/'job.json',job)
    print(json.dumps({k:result.get(k) for k in ('status','passed','GPU_occupancy_seconds','cumulative_technical_GPU_seconds',
        'cumulative_total_GPU_seconds','scientific_forecast_seconds','science_budget_eligible','failed_stage','error_type','error')}),flush=True)
    if not result['passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('inspect','observe-ui','run'))
    parser.add_argument('--config-sha256',required=True)
    args = parser.parse_args()
    if args.action == 'inspect':
        inspect(args.config_sha256)
        print('Owned normalized RDrop25M CUDA preflight passed; no CUDA allocation')
    elif args.action == 'observe-ui':
        inspect(args.config_sha256)
        print(json.dumps(observe_ui()))
    else:
        run(args.config_sha256)
