"""Conditional stage3: inherit each100M endpoint and add exact200M teachers."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.curriculum_strategy import StrategyTrainer
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, seed_all
from phase6_performance import identity, alive, finite_state
import run_curriculum_strategy as original
import run_packing_study as packing
import run_complete_text_comparison as evaluation

BASE=original.RUN
RUN=ROOT/'reports/phase6/curriculum-strategy-300m-20261005'
CONFIG=ROOT/'configs/phase6/strategy_extension.json'
SOURCES=('scripts/run_strategy_extension.py','scripts/run_strategy_extension.ps1','tests/test_strategy_extension.py')


class ExtensionTrainer(StrategyTrainer):
    def __init__(self,parent,web,short,mode,goals,binding,device='cuda'):
        assert binding['optimizer_policy']=='inherit' and binding['warmup_updates']==0
        assert parent['sampler']['mode']==mode=='shuffle'
        # Existing constructor expects a Web BlockSampler parent. Only adapt
        # that constructor input; preserve full100M parent provenance below.
        adapted=dict(parent,sampler=parent['sampler']['web'])
        super().__init__(adapted,web,short,mode,goals,binding,device)
        self.sampler.short.load_state_dict(parent['sampler']['short'])
        self.lineage.update(extension_parent_lineage=parent['lineage'],
            extension_parent_sampler=copy.deepcopy(parent['sampler']),
            extension_parent_scheduler=copy.deepcopy(parent['scheduler']),
            extension_parent_teacher_tokens=100000000,
            stage_schedule='Explicit reheat from100M decay endpoint;90percent stable/10percent decay on additional200M. No warmup restart.',
            extension_source_sha256=sha256(Path(__file__)))
        self._set_token_lr()


def freeze():
    c=original.load_config();baselines=read_json(BASE/'baselines.json')
    assert baselines['equal300M_pair_eligible']
    for path in ('job.json','baselines-job.json'):
        job=read_json(BASE/path);assert job['status']=='complete' and not alive(job)
    if CONFIG.exists():load_config();return
    result=read_json(BASE/'compare-result.json')
    prior=read_json(BASE/'job.json')['gpu_elapsed_seconds']+read_json(BASE/'baselines-job.json')['gpu_seconds']
    contract=dict(version=1,base_config_sha256=sha256(original.CONFIG),base_result_sha256=sha256(BASE/'compare-result.json'),
        eligibility_sha256=sha256(BASE/'baselines.json'),extension_rule_sha256=sha256(BASE/'extension-rule.json'),
        parents={a:dict(path=d['checkpoint'],sha256=d['checkpoint_sha256'],update=d['update'],tokens_seen=d['tokens']) for a,d in result['checkpoints'].items()},
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},goals=dict(web=0,short=200000000),
        cumulative_teacher_tokens_per_arm=300000000,prior_GPU_seconds=prior,
        cumulative_GPU_budget_seconds=c['gpu_budget_seconds'],train_GPU_budget_seconds=600,
        recipe='Same10M, material and order; inherited Adam/RNG/short cursor; original peaks, no repeat warmup, staged90/10 reheat. Not uninterrupted300M training.',
        stop='After both endpoints, full Japanese and all160 content; no further extension or stage4',created_at=now())
    write_json(CONFIG,contract)
    print(json.dumps(contract),flush=True)


def load_config():
    original.load_config();c=read_json(CONFIG)
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert sha256(original.CONFIG)==c['base_config_sha256']
    assert sha256(BASE/'compare-result.json')==c['base_result_sha256']
    assert sha256(BASE/'baselines.json')==c['eligibility_sha256']
    assert sha256(BASE/'extension-rule.json')==c['extension_rule_sha256']
    assert read_json(BASE/'baselines.json')['equal300M_pair_eligible']
    return c


def run():
    ext=load_config();c=original.load_config();path=RUN/'job.json'
    previous=read_json(path) if path.exists() else {}
    if previous:
        assert previous['config_sha256']==sha256(CONFIG) and not alive(previous)
        if previous['status']=='complete':print('Completed extension retained');return
    prior=previous.get('gpu_elapsed_seconds',0);start=[None];stop=[False]
    job=dict(status='starting',**identity(),config_sha256=sha256(CONFIG),started_at=now(),gpu_elapsed_seconds=prior,
        restart_command='scripts/run_strategy_extension.ps1 -Worker')
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Stop requested; checkpoint retained at completed update')
        if start[0] is not None and ext['prior_GPU_seconds']+prior+time.monotonic()-start[0]>ext['cumulative_GPU_budget_seconds']:
            raise TimeoutError('Stage3 total1800s GPU budget exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)
    try:
        heartbeat('setup');torch.set_num_threads(2);seed_all(42);torch.use_deterministic_algorithms(True)
        for p in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            dest=RUN/'source'/p;dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists():assert dest.read_bytes()==(ROOT/p).read_bytes()
            else:shutil.copyfile(ROOT/p,dest)
        web=TrainView(c['web_shards'],c['web_manifest_sha256']);short=Shard(Path(c['curriculum']['pool']),'train')
        dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer'])
        original.RUN=RUN;original.StrategyTrainer=ExtensionTrainer
        packing.RUN=RUN;packing.PackingTrainer=ExtensionTrainer;evaluation.RUN=RUN/'evaluation'
        checkpoints={};evaluations={};aux={};gates={}
        with gpu_lock('cuda'):
            start[0]=time.monotonic()
            for arm,entry in ext['parents'].items():
                assert sha256(Path(entry['path']))==entry['sha256']
                parent=torch.load(entry['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
                assert parent['sampler']['source_teachers']==dict(web=0,short=100000000)
                assert parent['supervised_tokens']-parent['lineage']['parent_supervised_tokens']==100000000
                b=dict(config_sha256=sha256(CONFIG),parent=entry,peak_lr=c['strategies'][arm]['peak_lr'],
                    warmup_updates=0,optimizer_policy='inherit',initialization='trained100M-'+arm,
                    arm=arm,isolated_batch=c['isolated_batch'],actual_parent_path=entry['path'])
                gates[arm]=original.resume_gate(parent,web,short,b,check,heartbeat)
                arm_c=dict(c,peak_lr=b['peak_lr'],diagnostic_train_budget_seconds=600,mixed_train_budget_seconds=600)
                checkpoints[arm]=packing.train(parent,web,short,arm_c,b,arm,'shuffle',ext['goals'],heartbeat,check)
                assert checkpoints[arm]['additional_supervised_tokens']==200000000
                deadline=start[0]+ext['cumulative_GPU_budget_seconds']-ext['prior_GPU_seconds']-prior
                evaluations[arm]=evaluation.evaluate(arm,checkpoints[arm],dev,tok,c,checkpoints[arm]['binding'],heartbeat,check,deadline)
                aux[arm]=original.auxiliary(checkpoints[arm],c,arm,heartbeat,check)
                write_json(RUN/'progress-result.json',dict(checkpoints=checkpoints,evaluations=evaluations,auxiliary=aux))
                del parent;gc.collect();torch.cuda.empty_cache()
            result=dict(status='complete_pending_content_review',config_sha256=sha256(CONFIG),
                checkpoints=checkpoints,evaluations=evaluations,auxiliary=aux,
                scientific_teacher_tokens=400000000,cumulative_scientific_teacher_tokens=600000000,
                verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in gates.values()),
                gpu_seconds=prior+time.monotonic()-start[0],prior_GPU_seconds=ext['prior_GPU_seconds'],
                protected_test_used=False,completed_at=now())
            write_json(RUN/'compare-result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');a=p.parse_args()
    freeze() if a.freeze else run()
