"""Exact existing TRAIN32, three named checkpoints, FP32 read-only displacement."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,rng_state,restore_rng
from jmicro.eos_pilot import TrainView
from jmicro.model import JMicroModel
from phase6_performance import identity,alive
from run_eos_short_pilot import equal_state
from finite_parameter_displacement import recover_batch,directional_dot,summarize_displacement

PROPOSAL=ROOT/'reports/phase6/finite_parameter_displacement_proposal.json'
CONFIG=ROOT/'configs/phase6/finite_parameter_displacement.json'
RUN=ROOT/'reports/phase6/finite-parameter-displacement-20261006'
SOURCES=('scripts/finite_parameter_displacement.py','scripts/diagnose_finite_parameter_displacement.py',
    'scripts/diagnose_finite_parameter_displacement.ps1','tests/test_finite_parameter_displacement.py')


def reference(path):return dict(path=str(path),sha256=sha256(path))


def check_reference(record):
    if sha256(Path(record['path']))!=record['sha256']:
        raise ValueError('Frozen reference differs: '+record['path'])


def inspect():
    c=read_json(CONFIG)
    if (c['source_sha256']!={p:sha256(ROOT/p) for p in SOURCES}
            or c['GPU_ceiling_seconds']!=120 or c['scientific_teacher_tokens'] or c['optimizer_updates']
            or c['dtype']!='float32' or c['backend']!='math' or c['batch']!=8 or c['context']!=1024
            or c['fixed_web_batches']!=4 or not c['quality_criteria_unchanged'] or c['protected_test_used']):
        raise ValueError('Original finite-displacement protocol differs')
    for record in (*c['refs'].values(),*c['checkpoints'].values()):check_reference(record)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):
        raise ValueError('Actual live displacement job; do not duplicate')
    endpoint_job=read_json(ROOT/'reports/phase6/weight-average-comparison-20261006/job.json')
    if endpoint_job['status']!='complete' or alive(endpoint_job):
        raise ValueError('Previous midpoint must actually have completed')
    return c


def prepare():
    if CONFIG.exists():inspect();print('Existing frozen assay retained');return
    RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'preparation-job.json'
    if jp.exists():raise ValueError('Preserve partial source preparation; no input reroll')
    p=read_json(PROPOSAL)
    for key in ('trigger','cached_midpoint_curve','earlier_first_order_source_assay','fixed_TRAIN_samples'):
        check_reference(p[key])
    if (p['GPU_ceiling_seconds']!=120 or p['scientific_teacher_tokens'] or p['optimizer_updates']
            or p['descriptive_markers']!=dict(Web_harm_nats_per_body_token_at_least=.02,batches_at_least=3,
                nonlinear_residual_fraction_of_positive_actual_change_at_least=.5)):
        raise ValueError('Predeclared no-learning proposal required')
    tests=ROOT/'reports/phase6/finite_parameter_displacement_tests.xml';suite=ET.parse(tests).getroot().find('testsuite')
    if int(suite.attrib['tests'])!=3 or any(int(suite.attrib[k]) for k in ('errors','failures','skipped')):
        raise ValueError('Three passing fixed-block/gradient/statistic CPU checks required')
    started=time.monotonic();job=dict(status='preparing',**identity(),started_at=now(),CPU_ceiling_seconds=30,
        GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0)
    atomic_json(jp,job)
    try:
        source_config=ROOT/'configs/phase6/source_order_condition_comparison_v2.json';source=read_json(source_config)
        web=TrainView(source['original_web']['path'],source['original_web']['manifest_sha256'])
        metadata=read_json(Path(p['fixed_TRAIN_samples']['path']))
        rows=sorted((r for r in metadata['rows'] if r['source']=='web'),key=lambda r:r['draw'])
        if [r['draw'] for r in rows]!=list(range(4)) or any(len(r['original_Web_blocks'])!=8 for r in rows):
            raise ValueError('Original four fixed Web batches required')
        arrays={}
        for row in rows:
            x,y=recover_batch(web.tokens,web.byte_lengths,row)
            arrays['x'+str(row['draw'])]=x;arrays['y'+str(row['draw'])]=y
        array_path=RUN/'fixed-TRAIN-inputs.npz';np.savez_compressed(array_path,**arrays)
        checkpoints=dict(mixed=p['checkpoints']['control'],midpoint=p['midpoint'],staged=p['checkpoints']['source_order'])
        for ref in checkpoints.values():check_reference(ref)
        elapsed=time.monotonic()-started
        if elapsed>30:raise TimeoutError('CPU preparation30s exhausted')
        refs={k:p[k] for k in ('trigger','cached_midpoint_curve','earlier_first_order_source_assay','fixed_TRAIN_samples')}
        refs.update(proposal=reference(PROPOSAL),source_config=reference(source_config),fixed_inputs=reference(array_path),CPU_tests=reference(tests))
        for relative in ('src/jmicro/model.py','src/jmicro/training.py','src/jmicro/eos_pilot.py','uv.lock'):
            refs[relative]=reference(ROOT/relative)
        config=dict(kind='read_only_fixed_TRAIN_finite_displacement_v1',created_at=now(),refs=refs,checkpoints=checkpoints,
            source_sha256={p:sha256(ROOT/p) for p in SOURCES},GPU_ceiling_seconds=120,CPU_preparation_seconds=elapsed,
            dtype='float32',backend='math',dot_accumulation='float64',context=1024,batch=8,fixed_web_batches=4,
            rows=rows,original_web=source['original_web'],original_stream_size_mtime_ns=[(web.directory/'train.bin').stat().st_size,(web.directory/'train.bin').stat().st_mtime_ns],
            parameter_count=10001152,markers=p['descriptive_markers'],optimizer_updates=0,scientific_teacher_tokens=0,
            quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,
            Chat_started=False,quantization_started=False)
        atomic_json(CONFIG,config);job.update(status='complete',CPU_seconds=elapsed,completed_at=now(),config_sha256=sha256(CONFIG))
        atomic_json(jp,job)
        print(json.dumps(dict(status='four_original_TRAIN_batches_frozen',CPU_seconds=elapsed,
            input_positions=32768,body_teacher_positions=sum(r['body_teachers'] for r in rows),scientific_teacher_tokens=0,GPU_seconds=0)))
    except BaseException as error:
        job.update(status='failed_preserve_partial',error=repr(error),CPU_seconds=time.monotonic()-started)
        atomic_json(jp,job);raise


def run():
    c=inspect();jp=RUN/'job.json';old=read_json(jp) if jp.exists() else {}
    if old.get('status')=='complete':print('Completed displacement assay retained');return
    cfg=sha256(CONFIG)
    if old and old['config_sha256']!=cfg:raise ValueError('Interrupted assay identity differs')
    previous=old.get('GPU_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=cfg,started_at=now(),GPU_seconds=previous,
        scientific_teacher_tokens=0,optimizer_updates=0,restart_command='scripts/diagnose_finite_parameter_displacement.ps1 -Worker')
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Read-only assay interrupted; complete points retained')
        if started[0] is not None and previous+time.monotonic()-started[0]>120:
            raise TimeoutError('Cumulative GPU120s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        with np.load(Path(c['refs']['fixed_inputs']['path']),allow_pickle=False) as arrays:
            inputs={i:(torch.from_numpy(arrays['x'+str(i)].copy()),torch.from_numpy(arrays['y'+str(i)].copy())) for i in range(4)}
        stream=Path(c['original_web']['path'])/'train.bin';stat=stream.stat()
        if [stat.st_size,stat.st_mtime_ns]!=c['original_stream_size_mtime_ns']:
            raise ValueError('Original immutable TRAIN stream identity changed')
        source=RUN/'source'
        for relative in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            destination=source/relative;destination.parent.mkdir(parents=True,exist_ok=True)
            if destination.exists() and destination.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Source snapshot differs')
            if not destination.exists():shutil.copyfile(ROOT/relative,destination)
        endpoint=torch.load(c['checkpoints']['staged']['path'],map_location='cpu',weights_only=False)
        observations={};model_checks={}
        with gpu_lock('cuda'):
            started[0]=time.monotonic();before_rng=rng_state();heartbeat('GPU')
            try:
                for arm,ref in c['checkpoints'].items():
                    check();state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                    if state['model_config']!=endpoint['model_config']:raise ValueError('Same named architecture required')
                    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                    named=list(model.named_parameters());parameters=[v for _,v in named]
                    if sum(p.numel() for p in parameters)!=c['parameter_count'] or len(parameters)!=119:
                        raise ValueError('Count tied embedding only once, all119 original parameters')
                    directions=[endpoint['model'][k].to('cuda')-v.detach() for k,v in named] if arm=='mixed' else None
                    before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()};points=[]
                    hook=model.register_forward_pre_hook(lambda *_:check())
                    try:
                        for draw in range(4):
                            path=RUN/f'points/{arm}/{draw:02d}.json';binding=dict(config_sha256=cfg,checkpoint_sha256=ref['sha256'],draw=draw)
                            if path.exists():
                                point=read_json(path)
                                if point['binding']!=binding:raise ValueError('Saved point binding differs')
                            else:
                                x,y=inputs[draw];x=x.to('cuda');y=y.to('cuda')
                                # Identical full causal unpadded1024 input in every arm. No cache/AMP/compile.
                                with torch.set_grad_enabled(arm=='mixed'),sdpa_kernel(SDPBackend.MATH):
                                    logits=model(x).logits
                                    if logits.dtype!=torch.float32 or not torch.isfinite(logits).all():
                                        raise ValueError('Actual FP32 finite logits required')
                                    ce=F.cross_entropy(logits.flatten(0,1),y.flatten(),ignore_index=-100,reduction='none').view_as(y)
                                    body=ce[y>=8].mean();eos=ce[y==3].mean()
                                if not torch.isfinite(body) or not torch.isfinite(eos):raise ValueError('Finite separate body/EOS loss required')
                                point=dict(binding=binding,body_CE=float(body.detach()),EOS_CE=float(eos.detach()),
                                    metadata=c['rows'][draw],finite_forward=True,optimizer_updates=0)
                                if arm=='mixed':
                                    gradients=torch.autograd.grad(body,parameters)
                                    point.update(directional_body_gradient=directional_dot(gradients,directions),
                                        gradient_norm=math_norm(gradients),direction_norm=math_norm(directions),
                                        finite_gradients=True,unique_parameters=len(parameters))
                                    del gradients
                                atomic_json(path,point);del x,y,logits,ce,body,eos
                            points.append(point);heartbeat(arm,completed_batches=len(points),total_batches=4)
                        checks=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),
                            no_parameter_gradients=all(p.grad is None for p in parameters),eval_mode=not model.training,
                            all_parameters_FP32=all(p.dtype==torch.float32 for p in parameters))
                        if not all(checks.values()):raise ValueError('Actual model modified during read-only assay')
                        observations[arm]=points;model_checks[arm]=checks
                    finally:hook.remove()
                    del state,model,named,parameters,directions,before;gc.collect();torch.cuda.empty_cache()
            finally:restore_rng(before_rng)
            if not equal_state(before_rng,rng_state()):raise ValueError('Assay RNG restoration failed')
            rows=[]
            for draw in range(4):
                a,m,b=[observations[k][draw] for k in ('mixed','midpoint','staged')]
                rows.append(dict(draw=draw,**summarize_displacement(a['body_CE'],m['body_CE'],b['body_CE'],a['directional_body_gradient'])))
            markers=dict(harm_batches=sum(r['harm_marker'] for r in rows),nonlinear_half_or_more_batches=sum(r['nonlinear_half_or_more_marker'] for r in rows),
                first_order_predicts_increase_batches=sum(r['first_order_predicts_increase'] for r in rows))
            check();result=dict(status='all_four_TRAIN_batches_three_models_finite_displacement_complete',created_at=now(),
                config_sha256=cfg,observations=observations,model_checks=model_checks,RNG_restored=True,rows=rows,markers=markers,
                GPU_seconds=previous+time.monotonic()-started[0],GPU_ceiling_seconds=120,
                input_positions_per_model=32768,unique_fixed_TRAIN_input_positions=32768,
                observed_body_teacher_positions_per_model=sum(r['body_teachers'] for r in c['rows']),
                observed_EOS_positions_per_model=sum(r['EOS_teachers'] for r in c['rows']),
                optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
                quality_criteria_unchanged=True,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
                limitations=read_json(PROPOSAL)['interpretation'])
            atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/finite_parameter_displacement_result.json',result)
        job.update(status='complete',completed_at=now(),GPU_seconds=previous+time.monotonic()-started[0]);atomic_json(jp,job)
        print(json.dumps(dict(status=job['status'],markers=markers,GPU_seconds=job['GPU_seconds'],rows=rows)))
    except BaseException as error:
        job.update(status='failed_or_interrupted',error=repr(error),ended_at=now(),
            GPU_seconds=previous+(time.monotonic()-started[0] if started[0] is not None else 0))
        atomic_json(jp,job);raise


def math_norm(values):
    return float(torch.stack([v.detach().double().square().sum() for v in values]).sum().sqrt())


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();parser.add_argument('--prepare',action='store_true');parser.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.prepare:prepare()
    elif args.inspect:print(dict(status='preflight_complete',GPU_ceiling=inspect()['GPU_ceiling_seconds']))
    else:run()
