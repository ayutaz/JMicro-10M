"""Single controlled PAD-efficiency prototype within the original180s cap."""
import argparse
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
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,now,sha256
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock
from base_kv_allocation_trainer import CEOnlyOriginalSampler,FreshKVAllocationTrainer
from base_kv_allocation_bucketed import BucketedKVAllocationTrainer,grouped_backward
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive,finite_state
from probe_base_kv_allocation import worst_shape

CONFIG=ROOT/'configs/phase6/base_kv_allocation_bucketed_probe.json'
RUN=ROOT/'reports/phase6/base-kv-allocation-bucketed-probe-20261007'
SOURCES=('scripts/probe_base_kv_allocation_bucketed.py','scripts/probe_base_kv_allocation_bucketed.ps1',
    'scripts/base_kv_allocation_bucketed.py','tests/test_base_kv_allocation_bucketed.py',
    'scripts/base_kv_allocation_trainer.py','scripts/probe_base_kv_allocation.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_memory.py','scripts/phase6_performance.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock')


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def prepare():
    if CONFIG.exists() or (RUN/'job.json').exists():raise ValueError('Preserve single frozen speed prototype')
    old_path=ROOT/'configs/phase6/base_kv_allocation_probe.json'
    old=json.loads(old_path.read_text())
    completion_path=ROOT/'reports/phase6/base_kv_allocation_probe_completion.json'
    completed=json.loads(completion_path.read_text())
    if (not completed['fixed_300M_allocation_protocol_closed'] or alive(completed['actual_identity'])
            or completed['science_budget_eligible']):raise ValueError('Preserve actually closed flat budget decision')
    tests=ROOT/'reports/phase6/base_kv_allocation_bucketed_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Actual four objective/gradient/own resume CPU checks required')
    previous_seconds=completed['GPU_occupancy_seconds']
    c=dict(created_at=now(),old_config=ref(old_path),previous_completion=ref(completion_path),CPU_tests=ref(tests),
        sources={s:sha256(ROOT/s) for s in SOURCES},source_binding=old['source_binding'],
        variants=old['variants'],goals=old['goals'],tokenizer_sha256=old['tokenizer_sha256'],payload=old['payload'],
        batch=80,seed=42,warmup_steps=3,timed_steps=32,
        fixed_route_order=['GQA-flat','MHA-bucketed','GQA-bucketed','MHA-flat'],
        previous_GPU_seconds=previous_seconds,GPU_limit_seconds=math.floor(180-previous_seconds),
        absolute_total_prototype_GPU_cap=180,all_new_GPU_ceiling=9000,
        numerical_tolerance=dict(loss_absolute=.02,whole_gradient_relative_L2=.02),
        interpretation='Single operational improvement: group original logical batch by length, sum CE divided by original total teachers, then one global clip/Adam/token-schedule update. Native shapes, source draws, original gold positions and300M recipe unchanged. Different floating accumulation is explicitly checked, not called bit-identical CUDA.',
        sampling='Both routes use identical original logical updates; physical PAD work differs. All32 timing steps per route retained, no favourable subset or further timing extension.',
        failure_policy='If native numerical/own CUDA resume/original stream/budget fails, close this one prototype. No second bucket scheme, batch/cap/teacher/LR/source/epoch rescue.',
        scientific_teachers=0,Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='fixed_single_PAD_efficiency_prototype_GPU0',additional_GPU_cap=c['GPU_limit_seconds'])))


def inspect():
    c=json.loads(CONFIG.read_text())
    for key in ('old_config','previous_completion','CPU_tests','payload'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:raise ValueError('Frozen reference differs: '+key)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen source differs: '+path)
    if alive(json.loads(Path(c['previous_completion']['path']).read_text())['actual_identity']):
        raise ValueError('Previous native probe still alive')
    if (RUN/'job.json').exists():raise ValueError('Inspect attempted one-shot identity/results; no blind retry')
    return c


def run():
    c=inspect()
    if not torch.cuda.is_available():raise RuntimeError('Actual native WSL CUDA required')
    RUN.mkdir(parents=True,exist_ok=True)
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        scientific_teachers=0,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='Single bounded speed prototype: inspect preserved terminal/partial evidence; no blind rerun.')
    atomic_json(RUN/'job.json',job)
    started=None
    histories,timings,numerical,resume,capacity={},{},{},{},{}
    def check(*args):
        if args or (started is not None and time.monotonic()-started>c['GPU_limit_seconds']):
            raise TimeoutError('Remaining original180s prototype budget exhausted')
    def beat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def clear():
        gc.collect();torch.cuda.empty_cache()
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        codec=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
        if sha256(codec.path)!=c['tokenizer_sha256']:raise ValueError('Pinned tokenizer differs')
        binding=dict(prototype=ref(CONFIG),weights_role='verification_only')
        def source():
            s=CEOnlyOriginalSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],codec,c['goals'])
            if s.binding!=c['source_binding']:raise ValueError('Actual original TRAIN binding differs')
            return s
        def build(arm,bucketed=True):
            cls=BucketedKVAllocationTrainer if bucketed else FreshKVAllocationTrainer
            return cls(c['variants'][arm],source(),binding,batch=c['batch'])
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            dest=RUN/'source'/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,dest)
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGALRM,check);signal.alarm(c['GPU_limit_seconds'])
            memory=configure_resident_memory(0);job['status']='running'
            for arm in c['variants']:
                beat(arm+'-native-numerical-objective')
                t=build(arm);rows=source().take(c['batch'])
                ids,_=right_pad([r['input_ids'] for r in rows],'cuda')
                targets=torch.full(ids.shape,-100,dtype=torch.long)
                for i,row in enumerate(rows):targets[i,:len(row['target_ids'])]=torch.tensor(row['target_ids'])
                targets=targets.to('cuda');selected=targets.ne(-100)
                with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                    hidden=right_padded_hidden(t.model,ids)
                    loss=F.cross_entropy(t.model.lm_head(hidden[selected]).float(),targets[selected]);loss.backward()
                native_loss=float(loss.detach())
                expected={name:p.grad.detach().float().cpu().clone() for name,p in t.model.named_parameters()}
                t.model.zero_grad(set_to_none=True)
                del hidden,loss,ids,targets,selected;clear()
                actual,physical,groups=grouped_backward(t.model,rows,'cuda')
                numerator=denominator=0.
                for name,p in t.model.named_parameters():
                    if p.grad is None or not torch.isfinite(p.grad).all():raise ValueError('Finite all-native grouped gradients required')
                    grad=p.grad.detach().float().cpu()
                    numerator+=float((grad-expected[name]).double().square().sum())
                    denominator+=float(expected[name].double().square().sum())
                relative=math.sqrt(numerator/denominator)
                numerical[arm]=dict(loss_absolute_error=abs(actual-native_loss),whole_gradient_relative_L2=relative,
                    original_logical_teachers=sum(r['teacher_tokens'] for r in rows),length_groups=groups,
                    grouped_physical_inputs=physical,flat_physical_inputs=len(rows)*max(len(r['input_ids']) for r in rows),
                    passed=abs(actual-native_loss)<=c['numerical_tolerance']['loss_absolute'] and relative<=c['numerical_tolerance']['whole_gradient_relative_L2'])
                if not numerical[arm]['passed']:raise ValueError('Predeclared native CUDA numerical screen failed: '+repr(numerical[arm]))
                del t,expected,grad,rows;clear()
            for route in c['fixed_route_order']:
                arm,method=route.split('-');beat(route)
                t=build(arm,method=='bucketed');history=[];histories[route]=history
                for _ in range(c['warmup_steps']):check();history.append(t.step())
                measured=[]
                for _ in range(c['timed_steps']):check();row=t.step();history.append(row);measured.append(row)
                timings[route]=dict(median_original_teachers_per_second=statistics.median(r['CE_targets_this_update']/r['seconds'] for r in measured),
                    median_data_wait_seconds=statistics.median(r['data_wait_seconds'] for r in measured),
                    total_original_teacher_positions=sum(r['CE_targets_this_update'] for r in measured),
                    total_physical_inputs=sum(r['physical_inputs_this_update'] for r in measured),
                    total_timed_seconds=sum(r['seconds'] for r in measured),all_timed_steps=32,
                    terminal_original_sampler=host(t.sampler.state_dict()))
                del t;clear()
            stream_keys=('source_teachers','source_EOS','supervised_tokens','CE_input_tokens','original_body_bytes','token_digest','draw_trace','lr')
            for arm in c['variants']:
                if not equal_state(timings[arm+'-flat']['terminal_original_sampler'],timings[arm+'-bucketed']['terminal_original_sampler']):
                    raise ValueError('Full original sampler differs between speed routes')
                if not all(equal_state(a[k],b[k]) for a,b in zip(histories[arm+'-flat'],histories[arm+'-bucketed'],strict=True) for k in stream_keys):
                    raise ValueError('Original logical update gold/byte/EOS/source/LR stream differs')
            window=json.loads(Path(c['payload']['path']).read_text())['window']
            gate=RUN/'resume-gate';gate.mkdir(exist_ok=True)
            for arm in c['variants']:
                states,logs=[],[]
                for route in ('continuous','resumed'):
                    beat(arm+'-'+route);t=build(arm);history=[];histories[arm+'-'+route]=history
                    for index in range(4):
                        check();history.append(t.step())
                        if route=='resumed' and index==1:
                            t.save(gate/(arm+'-split.pt'));del t;clear();t=build(arm);t.load(gate/(arm+'-split.pt'))
                    if route=='continuous':capacity[arm]=worst_shape(t,window,c['batch'])
                    path=gate/(arm+'-'+route+'.pt');t.save(path)
                    states.append(torch.load(path,map_location='cpu',weights_only=False));logs.append(history)
                    del t;clear()
                checks={key:equal_state(states[0][key],states[1][key]) for key in states[0]}
                checks['finite']=all(finite_state(s) for s in states)
                checks['all_history_except_timing']=all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                    {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')}) for a,b in zip(*logs,strict=True))
                if not all(checks.values()):raise ValueError('Own grouped CUDA full resume differed: '+repr(checks))
                resume[arm]=dict(checks=checks,histories=logs,checkpoints={route:ref(gate/(arm+'-'+route+'.pt')) for route in ('continuous','resumed')})
                del states,logs;clear()
            if not all(equal_state(a[k],b[k]) for a,b in zip(resume['GQA']['histories'][0],resume['MHA']['histories'][0],strict=True) for k in stream_keys):
                raise ValueError('Grouped architecture original stream differs')
            check();elapsed=time.monotonic()-started
            total_probe=c['previous_GPU_seconds']+elapsed
            caps={arm:math.ceil(300000000/timings[arm+'-bucketed']['median_original_teachers_per_second']*1.3+900) for arm in c['variants']}
            forecast=total_probe+sum(caps.values())
            result=dict(status='complete',passed=True,actual_identity=identity(),config_sha256=sha256(CONFIG),
                memory_policy=memory,numerical=numerical,capacity=capacity,timings=timings,resume=resume,histories=histories,
                batch=c['batch'],all_original_logical_streams_identical=True,physical_padding_work_differs=True,
                full_original_source_sampler_identical=True,bit_identical_old_CUDA_update_claimed=False,
                GPU_occupancy_seconds=elapsed,total_actual_prototype_GPU_seconds=total_probe,
                science_caps_seconds=caps,forecast_all_new_GPU_seconds=forecast,science_budget_eligible=forecast<=9000,
                verification_updates=sum(len(h) for h in histories.values()),
                verification_teacher_positions=sum(r['CE_targets_this_update'] for h in histories.values() for r in h),
                scientific_teachers=0,probe_weights_used_for_science=False,Base_complete=False,
                Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
                next_action='If actual grouped source/resume/numerical/cap pass and forecast<=9000, implement/freeze same fresh paired300M science and all160 evaluation. Otherwise close this one operational prototype without cap/teacher/recipe rescue.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed);atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status='grouped_native_speed_prototype_complete',GPU_seconds=elapsed,total_prototype_GPU_seconds=total_probe,
                forecast_GPU_seconds=forecast,science_budget_eligible=result['science_budget_eligible'])))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),GPU_occupancy_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(RUN/'job.json',job);atomic_json(RUN/'failure-partial.json',dict(histories=histories,timings=timings,numerical=numerical,resume=resume,capacity=capacity))
        raise
    finally:signal.alarm(0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--prepare',action='store_true');g.add_argument('--inspect',action='store_true')
    args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Fixed one PAD-efficiency prototype inspected; GPU0')
    else:run()
