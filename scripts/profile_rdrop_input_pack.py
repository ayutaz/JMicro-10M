"""One known next batch, original packing only; no model or learning."""
import argparse
from collections import defaultdict
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'scripts')]
import torch
from jmicro.experiment import now, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_memory import configure_resident_memory
from natural_context_contrast_trainer import right_pad
from phase6_performance import alive, identity
from probe_context_likelihood import passed_tests

CONFIG = ROOT/'configs/phase6/rdrop_input_pack_profile_20261015.json'
RUN = ROOT/'reports/phase6/rdrop-input-pack-profile-20261015'
SCOPES = ('original_input_ID_packing', 'original_target_label_packing')


def scope():
    return dict(kind='owned_known_next48_original_input_pack_diagnostic_v1',
        checkpoint_update=6, next_update=7, input_shape=[48,583], main_teachers=6273,
        profiled_batches=1, warmup_batches=0, model_instantiated=False,
        forward_calls=0, backward_calls=0, optimizer_updates=0,
        scientific_teacher_positions=0, DEV_opened=False, TEST_opened=False,
        raw_text_or_ID_export=False, weights_saved=False, science_forecast=False,
        CPU_profiler_only=True, new_GPU_ceiling_seconds=5,
        prior_technical_GPU_seconds=136.72787685703952,
        prior_completed_science_GPU_seconds=2946.1623015810037,
        prior_total_GPU_seconds=3082.890178438043,
        original_technical_cap_seconds=180, original_total_GPU_cap_seconds=4800)


def assert_scope(c):
    if any(type(c.get(k)) is not type(v) or c[k] != v for k,v in scope().items()):
        raise ValueError('Exact ONE known-batch/no-model/no-forecast/carried budget scope required')


def cpu_oracle(rows):
    if not rows or any(not r['input_ids'] or len(r['input_ids']) != len(r['target_ids']) for r in rows):
        raise ValueError('Nonempty aligned original input/target rows required')
    width = max(len(r['input_ids']) for r in rows)
    ids = torch.tensor([r['input_ids']+[0]*(width-len(r['input_ids'])) for r in rows],dtype=torch.long)
    targets = torch.tensor([r['target_ids']+[-100]*(width-len(r['target_ids'])) for r in rows],dtype=torch.long)
    return ids,targets


def assert_known_next(state,rows,after,want):
    trace = [(r['index_byte_position'],r['index_record_sha256'],r['target_first'],
        r['target_end'],r['teacher_tokens']) for r in rows]
    stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],
        r['input_ids'],r['target_ids']) for r in rows]).encode()
    digest = hashlib.sha256(bytes.fromhex(state['counters']['token_digest'])+stream).hexdigest()
    if (state['counters']['update'] != 6 or want['update'] != 7 or len(rows) != 48
            or json.loads(json.dumps(trace)) != want['draw_trace']
            or digest != want['token_digest'] or after['consumed'] != want['source_teachers']
            or sum(r['teacher_tokens'] for r in rows) != 6273
            or any(sum(t != -100 for t in r['target_ids']) != r['teacher_tokens'] for r in rows)
            or want['CE_targets_this_update'] != 6273
            or want['main_physical_inputs_this_update'] != 48*583
            or max(len(r['input_ids']) for r in rows) != 583):
        raise ValueError('Exact saved6 next48 stream/digest/source clocks/shape required; no alternate batch')


def summarize(events):
    groups = defaultdict(lambda: dict(count=0,CPU_self_us=0.,CPU_inclusive_us=0.))
    for event in events:
        if str(event.device_type) != 'DeviceType.CPU':
            raise ValueError('CPU-only activity required; device timing inference excluded')
        parent = event
        while parent is not None and parent.name not in SCOPES:
            parent = parent.cpu_parent
        group = parent.name if parent is not None else 'outside_scopes'
        values = (float(event.self_cpu_time_total),float(event.cpu_time_total))
        if not all(math.isfinite(v) for v in values):
            raise ValueError('Finite unmodified profiler CPU durations required')
        row = groups[(group,event.name)]
        row['count'] += 1
        row['CPU_self_us'] += values[0]
        row['CPU_inclusive_us'] += values[1]
    return [dict(scope=s,name=n,**v) for (s,n),v in sorted(groups.items())]


def inspect(pin):
    if sha256(CONFIG) != pin:
        raise ValueError('External frozen config pin required')
    c = json.loads(CONFIG.read_text())
    assert_scope(c)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Frozen diagnostic source differs: '+path)
    for key in ('proposal','prior_completion','prior_result','prior_job','checkpoint','accepted_config','tokenizer'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Pinned diagnostic evidence differs: '+key)
    for row in c['CPU_tests']:
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('CPU scope evidence differs')
        passed_tests(row['path'],row['expected_tests'])
    prior = json.loads(Path(c['prior_completion']['path']).read_text())
    if (alive(prior['actual_terminal_and_UI_proof']['technical_identity'])
            or not prior['fixed_condition_closed'] or not prior['cumulative_GPU_ledger_closed']
            or prior['science_budget_eligible'] or not prior['technical_checks_passed']
            or any(prior[k] != c[v] for k,v in (
                ('cumulative_technical_GPU_seconds','prior_technical_GPU_seconds'),
                ('cumulative_completed_science_GPU_seconds','prior_completed_science_GPU_seconds'),
                ('cumulative_total_GPU_seconds','prior_total_GPU_seconds')))):
        raise ValueError('Exited closed analytic runtime and EVERY consumed second required')
    job = json.loads(Path(c['prior_job']['path']).read_text())
    if job['verification6_snapshot'] != c['checkpoint']:
        raise ValueError('Actual saved6 provenance required')
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot diagnostic exists; inspect actual identity, never duplicate')
    return c


def observe_ui():
    saved = json.loads((ROOT/'reports/local/webui/server.json').read_text())
    if not alive(saved):
        raise ValueError('Actual original UI identity required')
    with urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:
        ui = json.load(response)
    if (ui['busy'] or ui['parameters'] != 10001152
            or ui['checkpoint_sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
            or ui['tokenizer_sha256'] != 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'):
        raise ValueError('Original idle parent/Tokenizer HTTP required')
    stat = (Path.home()/'jmicro-data/gpu.lock').stat()
    inode = f'{os.major(stat.st_dev):02x}:{os.minor(stat.st_dev):02x}:{stat.st_ino}'
    locks = [r for r in Path('/proc/locks').read_text().splitlines()
        if inode in r and 'FLOCK' in r and f'WRITE {saved["pid"]} ' in r]
    if len(locks) != 1:
        raise ValueError('Actual original UI kernel FLOCK required')
    out = dict(observed_at=now(),identity=identity(saved['pid']),HTTP=ui,
        actual_lock_inode=inode,kernel_FLOCK=locks)
    atomic_json(ROOT/'reports/phase6/rdrop-input-pack-profile-launcher-20261015/UI_observation.json',out)
    return out


def run(pin):
    c = inspect(pin)
    RUN.mkdir(parents=True,exist_ok=True)
    torch.set_num_threads(2)
    old = json.loads(Path(c['accepted_config']['path']).read_text())
    source = old['source_binding']
    pool = Path(source['pool'])
    allowed = {Path(c[k]['path']).resolve() for k in ('checkpoint','prior_result','tokenizer')}
    allowed |= {pool/n for n in ('manifest.json','train.index.jsonl','train.bin',
        '.compact-index-'+source['manifest_sha256'][:16]+'/ready.json')}
    lock = Path.home()/'jmicro-data/gpu.lock'
    protected = (ROOT/'reports',ROOT/'eval',ROOT/'artifacts',Path.home()/'jmicro-data')
    writes = {lock,*[RUN/n for n in ('job.json','job.json.tmp','result.json','result.json.tmp')]}
    reads = []
    def audit(event,args):
        if event != 'open' or not isinstance(args[0],(str,bytes)):
            return
        path = Path(os.fsdecode(args[0])).resolve()
        if not any(path.is_relative_to(root) for root in protected):
            return
        writing = any(flag in (args[1] or '') for flag in 'wax+') or bool(
            args[2] & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC|os.O_APPEND))
        if path in writes and (writing or path == lock):
            return
        if writing or path not in allowed:
            raise ValueError('Outside known-batch read scope: '+str(path))
        reads.append(str(path))
    sys.addaudithook(audit)
    job = dict(status='starting_CPU_reconstruction',**identity(),started_at=now(),
        config_sha256=pin,cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json',job)
    started = None
    result = None
    def check(*args):
        elapsed = 0 if started is None else time.monotonic()-started
        if args or elapsed > 5 or elapsed+c['prior_technical_GPU_seconds'] > 180:
            raise TimeoutError('Single5s/original cumulative180 ceiling exceeded')
    try:
        state = torch.load(c['checkpoint']['path'],map_location='cpu',weights_only=False)
        if (state['binding']['weights_role'] != 'verification_only'
                or state['spec']['rdrop_arm'] != 'normalized_rdrop'
                or state['spec']['batch'] != 48 or state['spec']['native_parameters'] != 10001152):
            raise ValueError('Actual native verification-only analytic6 required')
        sampler = OriginalTrainCorpusSampler(pool,source['manifest_sha256'],
            Tokenizer(Path(c['tokenizer']['path'])),state['sampler']['goals'],seed=42)
        if sampler.binding != source or state['spec']['original_material_binding'] != source:
            raise ValueError('Accepted original material binding required')
        sampler.load_state_dict(state['sampler'])
        rows = sampler.take(48)
        want = json.loads(Path(c['prior_result']['path']).read_text())['all32_timings'][0]
        assert_known_next(state,rows,sampler.state_dict(),want)
        oracle_ids,oracle_targets = cpu_oracle(rows)
        del sampler,state
        before_CPU = torch.get_rng_state().clone()
        job.update(status='CPU_reconstructed_exact_known_update7',heartbeat_at=now())
        atomic_json(RUN/'job.json',job)
        with gpu_lock('cuda'):
            started = time.monotonic()
            for sig in (signal.SIGTERM,signal.SIGINT,signal.SIGALRM):
                signal.signal(sig,check)
            signal.setitimer(signal.ITIMER_REAL,5)
            memory = configure_resident_memory(0)
            before_CUDA = torch.cuda.get_rng_state().clone()
            torch.cuda.synchronize()
            walls = {}
            with torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU],
                    record_shapes=True,profile_memory=False,with_stack=False) as prof:
                for name in SCOPES:
                    measured = time.monotonic()
                    with torch.profiler.record_function(name):
                        if name == SCOPES[0]:
                            ids,lengths = right_pad([r['input_ids'] for r in rows],'cuda')
                        else:
                            targets = torch.full_like(ids,-100)
                            for i,row in enumerate(rows):
                                targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'],device='cuda')
                        torch.cuda.synchronize()
                    walls[name] = time.monotonic()-measured
            metrics = summarize(prof.events())
            checks = dict(ids_exact=torch.equal(ids.cpu(),oracle_ids),
                targets_exact=torch.equal(targets.cpu(),oracle_targets),
                lengths_exact=torch.equal(lengths.cpu(),torch.tensor([len(r['input_ids']) for r in rows])),
                selected_mask_exact=torch.equal(targets.ne(-100).cpu(),oracle_targets.ne(-100)),
                CPU_RNG_unchanged=torch.equal(before_CPU,torch.get_rng_state()),
                CUDA_RNG_unchanged=torch.equal(before_CUDA,torch.cuda.get_rng_state()))
            torch.cuda.synchronize()
            check()
            if not all(checks.values()):
                raise ValueError('Original packing/masks/RNG must match exactly')
            result = dict(status='complete',observation_complete=True,checks=checks,
                scoped_synchronized_wall_seconds=walls,CPU_operator_rows=metrics,memory_policy=memory,
                known_next_batch=dict(update=7,shape=list(ids.shape),teachers=6273,
                    exact_existing_stream_digest=want['token_digest']),
                limits='One cold instrumented CPU-only profile. CPU inclusive durations overlap and CUDA activity time is unmeasured. Not steady throughput, a unique bottleneck, speedup, Japanese quality or science eligibility. Prior analytic condition stays closed.')
    except Exception as error:
        result = dict(status='failed',observation_complete=False,error_type=type(error).__name__,
            error=str(error),traceback=traceback.format_exc())
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
        elapsed = 0. if started is None else time.monotonic()-started
        if result is None:
            result = dict(status='failed',observation_complete=False,error='No observation')
        if elapsed > 5 or elapsed+c['prior_technical_GPU_seconds'] > 180:
            result.update(status='failed',observation_complete=False,error='Original5/180 deadline exceeded')
        result.update(config_sha256=pin,actual_identity=identity(),GPU_occupancy_seconds=elapsed,
            cumulative_technical_GPU_seconds=elapsed+c['prior_technical_GPU_seconds'],
            cumulative_completed_science_GPU_seconds=c['prior_completed_science_GPU_seconds'],
            cumulative_total_GPU_seconds=elapsed+c['prior_total_GPU_seconds'],
            cumulative_GPU_ledger_closed=True,protected_Python_open_read_paths=sorted(set(reads)),
            new_TRAIN_sampler_draw_batches=1,known_already_measured_batch=True,
            model_instantiated=False,forward_calls=0,backward_calls=0,optimizer_updates=0,
            scientific_teacher_positions=0,DEV_opened=False,TEST_opened=False,
            raw_text_or_ID_export=False,weights_saved=False,science_forecast=False,
            Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False)
        job.update(status=result['status'],ended_at=now(),cumulative_GPU_ledger_closed=True,
            GPU_occupancy_seconds=elapsed,cumulative_total_GPU_seconds=result['cumulative_total_GPU_seconds'])
        atomic_json(RUN/'result.json',result)
        atomic_json(RUN/'job.json',job)
    print(json.dumps({k:result.get(k) for k in ('status','observation_complete',
        'GPU_occupancy_seconds','cumulative_total_GPU_seconds','error')}),flush=True)
    if not result['observation_complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('inspect','observe-ui','run'))
    parser.add_argument('--config-sha256',required=True)
    args = parser.parse_args()
    if args.action == 'run':
        run(args.config_sha256)
    elif args.action == 'observe-ui':
        inspect(args.config_sha256)
        print(json.dumps(observe_ui()),flush=True)
    else:
        inspect(args.config_sha256)
        print('Known batch input-only preflight passed; no CUDA/model/sampler draw')
