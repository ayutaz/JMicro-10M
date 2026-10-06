"""Discarded common/pair CUDA restart and measured8 versus56 pair batches."""
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
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state
from base_preference_trainer import CommonWebTrainer,PairPreferenceTrainer,PairQuotaSampler,build_reference,KIND,LR
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
from probe_livedoor_base import host_state,resume_gate

RUN=ROOT/'reports/phase6/base-preference-comparison-20261006'
CONFIG=ROOT/'configs/phase6/base_preference_probe.json'
PROPOSAL=ROOT/'reports/phase6/base_preference_comparison_proposal.json'
SOURCES=('scripts/probe_base_preference.py','scripts/probe_base_preference.ps1','scripts/base_preference_trainer.py',
    'scripts/base_preference_loss.py','tests/test_base_preference_trainer.py')
OLD_SOURCES=('scripts/original_web_retention_trainer.py','scripts/condition_positive_trainer.py','scripts/condition_positive_loss.py',
    'scripts/phase6_performance.py','scripts/probe_livedoor_base.py','scripts/run_eos_short_pilot.py')


def reference(q):return dict(path=str(q),sha256=sha256(q))


def check_reference(ref):
    if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Frozen preference reference differs: '+ref['path'])


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();p=read_json(PROPOSAL);review=read_json(Path(p['diagnostic']['path']))
    if (p['kind']!=KIND or p['scientific_config_frozen'] or p['science_started'] or p['fixed_pair_count']!=56
            or p['shared_Web_positive_teacher_tokens']!=6000000 or p['positive_completion_teacher_tokens_per_arm']!=2000000
            or p['arms']!=dict(chosen_CE=dict(DPO_coefficient=0.),chosen_CE_DPO=dict(DPO_coefficient=.1))
            or not review['all64_individually_read'] or review['usable_preference_pairs']!=56
            or p['preferred_pair_ids']!=review['preferred_pair_ids']):raise ValueError('Actual original56 preference proposal required')
    tests=ROOT/'reports/phase6/base_preference_trainer_tests.xml';suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):raise ValueError('Actual inherited/two-objective resume/partial quota tests required')
    news=read_json(ROOT/'reports/phase6/livedoor_base_comparison_proposal.json');old=read_json(Path(news['cached_control_config']['path']))
    c=dict(kind=KIND,phase='own_CUDA_probe',parent=p['parent'],pairs=p['news_pairs'],preferred_pair_ids=p['preferred_pair_ids'],
        original_web=news['data']['original_web'],original_config=old['original_config'],references=dict(proposal=reference(PROPOSAL),content_review=p['diagnostic'],CPU_tests=reference(tests)),
        context=1024,Web_batch=32,Web_teacher_goal=6000000,pair_teacher_goal=2000000,pair_batch_candidates=[8,56],
        pair_backend='math',dtype='bf16',beta=.1,coefficients=[0.,.1],source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        old_source_sha256={s:sha256(ROOT/s) for s in OLD_SOURCES},implementation=implementation_hashes(),GPU_budget_seconds=180,total_new_study_GPU_ceiling_seconds=1800,
        validation='Common Web4vs2+2/32timing; actual finite DPO32timing at8 and56 pairs. Select maximum measured positive teacher/s, no duplicated within-batch pairs. Both selected objectives4vs2+2/fullstate/history; CE32timing, reuse selected DPO32. All verification parents/weights discarded.',
        diagnostic_GPU_seconds_separate=p['diagnostic_GPU_seconds_separate'],CPU_preparation_seconds=time.monotonic()-started,
        Base_complete=False,Base_adopted=False,protected_test_used=False,Chat_started=False,quantization_started=False,scientific_teacher_tokens=0)
    for ref in (c['parent'],c['pairs'],c['original_config'],*c['references'].values()):check_reference(ref)
    if c['CPU_preparation_seconds']>30:raise TimeoutError('CPU30s exhausted')
    atomic_json(CONFIG,c);inspect();print(dict(status='preference_native_CUDA_probe_frozen',GPU_seconds=0))


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!=KIND or c['phase']!='own_CUDA_probe' or c['context']!=1024 or c['Web_batch']!=32
            or c['Web_teacher_goal']!=6000000 or c['pair_teacher_goal']!=2000000 or c['pair_batch_candidates']!=[8,56]
            or c['coefficients']!=[0.,.1] or c['beta']!=.1 or c['pair_backend']!='math' or c['dtype']!='bf16'
            or c['GPU_budget_seconds']!=180 or c['total_new_study_GPU_ceiling_seconds']!=1800 or c['implementation']!=implementation_hashes()
            or c['scientific_teacher_tokens'] or any(c[k] for k in ('Base_complete','Base_adopted','protected_test_used','Chat_started','quantization_started'))):raise ValueError('Frozen preference CUDA scope differs')
    for name,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'],c['pairs'],c['original_config'],*c['references'].values()):check_reference(ref)
    if (RUN/'probe/job.json').exists() and alive(read_json(RUN/'probe/job.json')):raise ValueError('Actual live probe; no duplicate')
    return c


def pairs(c):
    rows=read_json(Path(c['pairs']['path']));mapping={r['id']:r for r in rows}
    result=[mapping[key] for key in c['preferred_pair_ids']]
    if len(result)!=56 or any(r['split']!='train' for r in result) or sum(len(r['chosen_ids']) for r in result)!=4565:raise ValueError('Actual fixed original56 TRAIN records required')
    return result


def timing(build,parent,folder,check,heartbeat):
    folder.mkdir(parents=True,exist_ok=True);trainer=build();rows=[];torch.cuda.reset_peak_memory_stats()
    with (folder/'metrics.jsonl').open('x',buffering=1) as stream:
        for i in range(32):
            check();row=trainer.step();rows.append(row);stream.write(json.dumps(row,allow_nan=False)+'\n')
            if (i+1)%8==0:heartbeat(folder.name+'-timing',completed_updates=i+1)
    cp=folder/'timing.pt';cost=trainer.save(cp);state=torch.load(cp,map_location='cpu',weights_only=False)
    if not finite_state(state):raise ValueError('Finite full timing state required')
    result=dict(histories=rows,terminal_save_seconds=cost,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
        completed_updates=32,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),checkpoint=reference(cp))
    del trainer;gc.collect();torch.cuda.empty_cache();return result


def summary(t):
    rows=t['histories'];step=statistics.median(r['seconds'] for r in rows[8:]);teachers=(rows[-1]['additional_teacher_tokens']-rows[7]['additional_teacher_tokens'])/24
    if len(rows)!=32 or teachers<=0 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 or r['lr']!=LR for r in rows):raise ValueError('32 finite inherited-LR timing rows required')
    return dict(step_seconds=step,teachers_per_update=teachers,teachers_per_second=teachers/step,
        warmup_seconds=max(0.,sum(r['seconds'] for r in rows[:8])-8*step),save_seconds=t['terminal_save_seconds'])


def estimate_training(r):
    common=summary(r['common_timing']);pair={arm:summary(t) for arm,t in r['selected_timings'].items()}
    updates=dict(common=math.ceil(6000000/common['teachers_per_update']),**{arm:math.ceil(2000000/t['teachers_per_update'])+7 for arm,t in pair.items()})
    training=updates['common']*common['step_seconds']+common['warmup_seconds']
    training+=(math.ceil(updates['common']/250)+1)*common['save_seconds']
    for arm,t in pair.items():training+=updates[arm]*t['step_seconds']+t['warmup_seconds']+(math.ceil(updates[arm]/250)+1)*t['save_seconds']
    cache=r['reference_cache_GPU_seconds']
    return dict(common=common,pair=pair,updates=updates,training_save_warmup_seconds=training,reference_cache_seconds=cache),1.3*(training+cache)+600


def run():
    c=inspect();folder=RUN/'probe';folder.mkdir(parents=True,exist_ok=True);jp=folder/'job.json'
    if jp.exists():raise ValueError('Preserve one-shot probe; documented repair required')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0,restart_command='scripts/probe_base_preference.ps1 -Worker; terminal one-shot requires documented repair')
    atomic_json(jp,job);started=None;stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Preference CUDA probe interrupted')
        if started is not None and time.monotonic()-started>180:raise TimeoutError('Own native preference CUDA180s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for name in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=folder/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);web=TrainView(c['original_web']['path'],c['original_web']['manifest_sha256']);records=pairs(c)
        b=dict(parent=c['parent'],config_sha256=sha256(CONFIG),phase='common_Web_probe',scientific=False)
        def common():return CommonWebTrainer(parent,web,6000000,b)
        with gpu_lock('cuda'):
            started=time.monotonic();job['status']='running';heartbeat('initial_native_inheritance');trainer=common()
            initial=dict(model=equal_state(host_state(trainer.model.state_dict()),parent['model']),Adam=equal_state(host_state(trainer.optimizer.state_dict()),parent['optimizer']),
                scheduler=equal_state(trainer.scheduler.state_dict(),parent['scheduler']),RNG=equal_state(rng_state(),parent['rng']),
                Web_cursor=equal_state(trainer.sampler.streams['web'].sampler.state_dict(),parent['sampler']['web']),
                native_tied10M=sum(p.numel() for p in trainer.model.parameters())==10001152 and trainer.model.lm_head.weight is trainer.model.model.embed_tokens.weight)
            if not all(initial.values()):raise ValueError('Actual native Web initial inheritance differs')
            del trainer;gc.collect();torch.cuda.empty_cache();gate=resume_gate(common,folder/'common-resume',check,parent)
            common_time=timing(common,parent,folder/'common',check,heartbeat);common_parent=torch.load(common_time['checkpoint']['path'],map_location='cpu',weights_only=False)
            pair_bind=dict(parent=common_time['checkpoint'],config_sha256=sha256(CONFIG),phase='discarded_pair_probe',scientific=False)
            surveys={};references={};cache_time=0.;cache_checks={};verification=gate['verification_teacher_tokens']+common_time['verification_teacher_tokens'];updates=40
            for batch in c['pair_batch_candidates']:
                heartbeat('reference-'+str(batch));trainer=CommonWebTrainer(common_parent,web,6000000,pair_bind);before=rng_state();stamp=time.monotonic()
                sampler=PairQuotaSampler(records,2000000,batch,web.byte_lengths,'unused');ref=build_reference(trainer.model,sampler,'cuda','bf16');cache_time+=time.monotonic()-stamp
                readonly=dict(weights_unchanged=equal_state(host_state(trainer.model.state_dict()),common_parent['model']),RNG_restored=equal_state(rng_state(),before),no_gradients=all(p.grad is None for p in trainer.model.parameters()))
                if not all(readonly.values()):raise ValueError('Readonly reference cache changed weights/RNG')
                cache_checks[str(batch)]=readonly;references[batch]=ref;atomic_json(folder/f'reference-{batch}.json',dict(parent=common_time['checkpoint'],reference=ref,checks=readonly))
                del trainer;gc.collect();torch.cuda.empty_cache()
                build=lambda batch=batch,ref=ref:PairPreferenceTrainer(common_parent,web,records,2000000,.1,ref,pair_bind,batch=batch)
                surveys[str(batch)]=timing(build,common_parent,folder/f'DPO-batch{batch}',check,heartbeat);verification+=surveys[str(batch)]['verification_teacher_tokens'];updates+=32
            selected=max(c['pair_batch_candidates'],key=lambda size:summary(surveys[str(size)])['teachers_per_second']);ref=references[selected];gates={};timings={}
            for name,coefficient in (('chosen_CE',0.),('chosen_CE_DPO',.1)):
                build=lambda coefficient=coefficient:PairPreferenceTrainer(common_parent,web,records,2000000,coefficient,ref,pair_bind,batch=selected)
                heartbeat(name+'-restart');gates[name]=resume_gate(build,folder/(name+'-resume'),check,common_parent);verification+=gates[name]['verification_teacher_tokens'];updates+=8
                if coefficient:timings[name]=surveys[str(selected)]
                else:timings[name]=timing(build,common_parent,folder/name,check,heartbeat);verification+=timings[name]['verification_teacher_tokens'];updates+=32
                for left,right in zip(timings[name]['histories'][:4],gates[name]['histories'][0],strict=True):
                    if any(not equal_state(left[k],right[k]) for k in left if k!='seconds'):raise ValueError('Timing and exact gate trajectory differ')
            fields=('token_digest','physical_input_tokens','valid_input_tokens','additional_teacher_tokens','CE_EOS','scored_chosen_positions','scored_rejected_positions','active_pair_exposures','auxiliary_digest','group')
            if any(a[k]!=b[k] for a,b in zip(*(t['histories'] for t in timings.values()),strict=True) for k in fields):raise ValueError('Both actual objectives must use identical input/label/exposure streams')
            result=dict(passed=True,config_sha256=sha256(CONFIG),initial_preservation=initial,common_gate=gate,common_timing=common_time,
                pair_surveys=surveys,selected_pair_batch=selected,selected_pair_gates=gates,selected_timings=timings,reference_readonly_checks=cache_checks,
                reference_cache_GPU_seconds=cache_time,verification_updates=updates,verification_teacher_tokens=verification,
                scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
            measured,estimate=estimate_training(result);elapsed=time.monotonic()-started
            result.update(measured_timing=measured,estimated_science_GPU_seconds=estimate,GPU_seconds=elapsed,estimated_total_new_study_GPU_seconds=estimate+elapsed)
            atomic_json(folder/'result.json',result);job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as exc:job.update(status='failed_or_interrupted',error=repr(exc));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true');args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Inherited preference CUDA probe valid; science0')
    else:run()
