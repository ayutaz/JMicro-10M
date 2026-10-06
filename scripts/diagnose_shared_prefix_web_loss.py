"""One preselected fullstate, nativeBF16/math dev body score; no optimizer."""
import argparse
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
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,rng_state,restore_rng,implementation_hashes,synchronize
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.readiness import evaluate_batched
from jmicro.evaluation_memory import bound_evaluation_cache
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
from shared_prefix_web_loss import validate_body,decompose

PROPOSAL=ROOT/'reports/phase6/shared_prefix_web_loss_proposal.json'
CONFIG=ROOT/'configs/phase6/shared_prefix_web_loss.json'
RUN=ROOT/'reports/phase6/shared-prefix-web-loss-20261006'
SOURCES=('scripts/shared_prefix_web_loss.py','scripts/diagnose_shared_prefix_web_loss.py',
    'scripts/diagnose_shared_prefix_web_loss.ps1','tests/test_shared_prefix_web_loss.py',
    'src/jmicro/readiness.py','src/jmicro/evaluation_memory.py')


def reference(path):return dict(path=str(path),sha256=sha256(path))


def check_reference(ref):
    if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Frozen reference differs: '+ref['path'])


def common_body(body):
    validate_body(body)
    if body['documents']!=256 or body['body_tokens']!=122343 or body['body_bytes']!=472055:
        raise ValueError('Original complete256 common body required')
    return body


def prepare():
    if CONFIG.exists():inspect();return
    started=time.monotonic();p=read_json(PROPOSAL)
    if (p['total_new_GPU_ceiling_seconds']!=30 or p['CPU_preparation_ceiling_seconds']!=10
            or p['shared_update']!=323185 or p['optimizer_updates'] or p['new_teacher_tokens'] or p['protected_test_used']):
        raise ValueError('Fixed no-learning single-checkpoint proposal required')
    for ref in (p['trigger'],p['sole_new_checkpoint'],p['original_reference_input_ledger'],*p['cached_comparators'].values()):check_reference(ref)
    suites=list(ET.parse(ROOT/'reports/phase6/shared_prefix_web_loss_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Three passing accounting tests required')
    prior_config=ROOT/'configs/phase6/conditional_prefix_mask.json';old=read_json(prior_config)
    previous=read_json(ROOT/'reports/phase6/conditional-prefix-mask-20261006/job.json')
    if previous['status']!='complete' or alive(previous):raise ValueError('Previous actual science must be terminal')
    parent=torch.load(p['sole_new_checkpoint']['path'],map_location='cpu',weights_only=False)
    if (not finite_state(parent) or parent['update']!=323185
            or parent['sampler']['source_teachers']!=p['actual_prefix_reference_teachers']
            or parent['implementation_sha256']!=implementation_hashes()):raise ValueError('Fixed finite preconditional source state required')
    cached=dict(historical=common_body(read_json(Path(p['cached_comparators']['original_historical_Web']['path']))['body']),
        strong_staged=common_body(read_json(Path(p['cached_comparators']['strong_staged']['path']))['evaluations']['source_order']['body']),
        masked_suffix=common_body(read_json(Path(p['cached_comparators']['masked_suffix']['path']))['evaluation']['body']))
    alignment=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in cached['historical']['rows']]
    if any([(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in b['rows']]!=alignment for b in cached.values()):raise ValueError('Cached common256 alignment differs')
    RUN.mkdir(parents=True,exist_ok=True);atomic_json(RUN/'cached-bodies.json',cached)
    elapsed=time.monotonic()-started
    if elapsed>10:raise TimeoutError('CPU preparation10s exhausted')
    c=dict(proposal=reference(PROPOSAL),checkpoint=p['sole_new_checkpoint'],references=dict(trigger=p['trigger'],
        input_ledger=p['original_reference_input_ledger'],**p['cached_comparators'],prior_config=reference(prior_config),
        CPU_tests=reference(ROOT/'reports/phase6/shared_prefix_web_loss_tests.xml'),cached_bodies=reference(RUN/'cached-bodies.json')),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},implementation=implementation_hashes(),
        dev_shards=read_json(Path(old['original_config']['path']))['dev_shards'],GPU_ceiling_seconds=30,CPU_preparation_seconds=elapsed,
        dtype='bf16',backend='math',context=1024,batch=16,documents=256,optimizer_updates=0,new_teacher_tokens=0,
        checkpoint_selected_by_source_only=True,quality_criteria_unchanged=True,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,created_at=now())
    dev_manifest=Path(c['dev_shards'])/'manifest.json';c['references']['dev_manifest']=reference(dev_manifest)
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='single_shared_prefix_body_assay_frozen',CPU_seconds=elapsed)),flush=True)


def inspect():
    c=read_json(CONFIG);p=read_json(PROPOSAL)
    if (c['checkpoint']!=p['sole_new_checkpoint'] or c['source_sha256']!={s:sha256(ROOT/s) for s in SOURCES}
            or c['implementation']!=implementation_hashes() or c['GPU_ceiling_seconds']!=30 or c['dtype']!='bf16'
            or c['backend']!='math' or c['batch']!=16 or c['context']!=1024 or c['documents']!=256
            or c['optimizer_updates'] or c['new_teacher_tokens'] or c['protected_test_used']
            or c['Base_complete'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started']
            or not c['quality_criteria_unchanged']):raise ValueError('Frozen single shared-prefix assay differs')
    for ref in (c['checkpoint'],c['proposal'],*c['references'].values()):check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual live assay; no duplicate')
    return c


def run():
    c=inspect();jp=RUN/'job.json';old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(CONFIG):raise ValueError('Prior job binding differs')
    if old.get('status')=='complete':print('Original completed assay retained');return
    prior=old.get('GPU_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),GPU_seconds=prior,started_at=now(),
        restart_command='scripts/diagnose_shared_prefix_web_loss.ps1 -Worker')
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Interrupted read-only assay')
        if started[0] is not None and prior+time.monotonic()-started[0]>30:raise TimeoutError('Cumulative30s ceiling exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_seconds']=prior+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for relative in (*SOURCES,*c['implementation'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Frozen snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        state=torch.load(c['checkpoint']['path'],map_location='cpu',weights_only=False);dev=Shard(Path(c['dev_shards']),'dev')
        with gpu_lock('cuda'):
            started[0]=time.monotonic();before_rng=rng_state()
            body_path=RUN/'body.json'
            if body_path.exists():
                saved=read_json(body_path)
                if saved['config_sha256']!=sha256(CONFIG) or saved['checkpoint']!=c['checkpoint']:raise ValueError('Cached complete body differs')
                body=saved['body'];checks=saved['read_only_checks']
            else:
                try:
                    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                    memory=bound_evaluation_cache(model);before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
                    hook=model.register_forward_pre_hook(lambda *_:check())
                    with sdpa_kernel(SDPBackend.MATH):
                        body=evaluate_batched(model,dev,'cuda','bf16',limit=256,context=1024,batch=16,
                            progress=lambda done,total:heartbeat('shared-prefix-dev256',completed_tasks=done,total_tasks=total))
                    synchronize('cuda');hook.remove()
                    checks=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),
                        no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training,
                        finite_weights=all(torch.isfinite(v).all().item() for v in model.state_dict().values()))
                finally:restore_rng(before_rng)
                checks['RNG_restored']=equal_state(before_rng,rng_state())
                if not all(checks.values()):raise ValueError('Actual read-only state invariant failed')
                common_body(body);atomic_json(body_path,dict(body=body,read_only_checks=checks,checkpoint=c['checkpoint'],config_sha256=sha256(CONFIG),memory=memory))
            cached=read_json(RUN/'cached-bodies.json');cached['shared_prefix']=common_body(body);result=decompose(cached)
            check();elapsed=prior+time.monotonic()-started[0]
            result.update(status='one_shared_prefix_body_assay_complete',config_sha256=sha256(CONFIG),checkpoint=c['checkpoint'],read_only_checks=checks,
                GPU_seconds=elapsed,new_teacher_tokens=0,optimizer_updates=0,protected_test_used=False,quality_criteria_unchanged=True,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
            atomic_json(RUN/'result.json',result);job.update(status='complete',GPU_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_seconds']=prior+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true');a=p.parse_args()
    if a.prepare:prepare()
    elif a.inspect:inspect()
    else:run()
