"""Five-step scope stage1: exact matched200M low-LR branches; reuse reheat."""
import argparse
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
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,seed_all
from phase6_performance import identity,alive,finite_state
from run_strategy_extension import ExtensionTrainer
from probe_lr_history import probe
import run_strategy_extension as previous
import run_curriculum_strategy as strategy
import run_packing_study as packing
import run_complete_text_comparison as evaluation

OLD=previous.RUN
BASE=previous.BASE
RUN=ROOT/'reports/phase6/lr-recovery-20261006'
CONFIG=ROOT/'configs/phase6/lr_recovery.json'
SOURCES=('scripts/run_lr_recovery.py','scripts/run_lr_recovery.ps1','scripts/probe_lr_history.py','tests/test_lr_recovery.py')


def terminal_peak(parent):
    rates=[g['lr'] for g in parent['optimizer']['param_groups']]
    if not rates or not all(math.isfinite(x) and x>0 for x in rates):
        raise ValueError('Parent must have finite positive terminal rates')
    if not all(math.isclose(x,rates[0],rel_tol=1e-12) for x in rates):
        raise ValueError('Different group rates require an explicit comparison')
    return rates[0]


class ColdExtensionTrainer(ExtensionTrainer):
    def __init__(self,parent,web,short,mode,goals,binding,device='cuda'):
        peak=terminal_peak(parent)
        assert math.isclose(binding['peak_lr'],peak,rel_tol=1e-12)
        super().__init__(parent,web,short,mode,goals,binding,device)
        self.lineage.update(cold_schedule=dict(parent_actual_lr=peak,
            schedule='additional teachers90percent stable at terminal LR,10percent decay, no warmup',
            scope='LR-scale comparison, not isolated instantaneous reheat effect',
            source_sha256=sha256(Path(__file__))))
        self.lineage['stage_schedule']='Cold terminal-LR fork;90percent stable/10percent decay on additional200M, no warmup'
        assert all(g['lr']<=peak*(1+1e-12) for g in self.optimizer.param_groups)


def freeze():
    strategy.load_config();old_config=previous.load_config()
    if CONFIG.exists():load_config();return
    old=read_json(OLD/'compare-result.json');base=read_json(BASE/'compare-result.json')
    for path in (OLD/'job.json',BASE/'job.json'):
        record=read_json(path);assert record['status']=='complete' and not alive(record)
    parents={};peaks={}
    for arm,d in base['checkpoints'].items():
        path=Path(d['checkpoint']);assert sha256(path)==d['checkpoint_sha256']
        state=torch.load(path,map_location='cpu',weights_only=False);assert finite_state(state)
        peaks[arm]=terminal_peak(state)
        parents[arm]=dict(path=str(path),sha256=sha256(path),update=state['update'],tokens_seen=state['tokens'])
    config=dict(version=1,scope='User requested all five steps; this experiment only covers stage1',
        parents=parents,peak_lr=peaks,goals=dict(web=0,short=200000000),
        reference_sha256=sha256(OLD/'compare-result.json'),base_sha256=sha256(BASE/'compare-result.json'),
        previous_contract_sha256=sha256(previous.CONFIG),strategy_contract_sha256=sha256(strategy.CONFIG),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},gpu_budget_seconds=1800,train_budget_seconds=600,
        selection_rule='For recipe selection, prefer low LR only when common official BPB improves by at least1percent relative to reheat and no new empty/role/Unicode failures; inspect all80 content. This does not lower adoption or Base criteria.',
        quality_criteria_unchanged=True,protected_test_used=False,created_at=now())
    write_json(CONFIG,config);print(json.dumps(config),flush=True)


def load_config():
    strategy.load_config();previous.load_config();c=read_json(CONFIG)
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert sha256(OLD/'compare-result.json')==c['reference_sha256'] and sha256(BASE/'compare-result.json')==c['base_sha256']
    assert sha256(previous.CONFIG)==c['previous_contract_sha256'] and sha256(strategy.CONFIG)==c['strategy_contract_sha256']
    return c


def run():
    c=load_config();recipe=strategy.load_config();path=RUN/'job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['config_sha256']==sha256(CONFIG) and not alive(old)
        if old['status']=='complete':print('Completed LR experiment retained');return
    prior=old.get('gpu_elapsed_seconds',0);start=[None];stop=[False]
    job=dict(status='running',**identity(),config_sha256=sha256(CONFIG),started_at=now(),gpu_elapsed_seconds=prior,
        restart_command='scripts/run_lr_recovery.ps1 -Worker',requested_scope_complete=False)
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Stop requested; full completed-update checkpoint retained')
        if start[0] is not None and prior+time.monotonic()-start[0]>c['gpu_budget_seconds']:
            raise TimeoutError('LR comparison1800s GPU budget exhausted')
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
        web=TrainView(recipe['web_shards'],recipe['web_manifest_sha256']);short=Shard(Path(recipe['curriculum']['pool']),'train')
        dev=Shard(Path(recipe['dev_shards']),'dev');tok=Tokenizer(ROOT/recipe['tokenizer'])
        strategy.RUN=RUN;strategy.StrategyTrainer=ColdExtensionTrainer
        packing.RUN=RUN;packing.PackingTrainer=ColdExtensionTrainer;evaluation.RUN=RUN/'evaluation'
        trained={};evaluated={};aux={};gates={}
        with gpu_lock('cuda'):
            start[0]=time.monotonic()
            probe_start=time.monotonic()
            def probe_check():
                check()
                if time.monotonic()-probe_start>300:raise TimeoutError('Read-only history probe300s budget exhausted')
            probe(RUN,BASE,OLD,short,tok,recipe,probe_check,heartbeat)
            for arm,entry in c['parents'].items():
                assert sha256(Path(entry['path']))==entry['sha256']
                parent=torch.load(entry['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
                assert parent['sampler']['source_teachers']==dict(web=0,short=100000000)
                b=dict(config_sha256=sha256(CONFIG),parent=entry,peak_lr=c['peak_lr'][arm],warmup_updates=0,
                    optimizer_policy='inherit',initialization='trained100M-'+arm,arm=arm,isolated_batch=256,
                    actual_parent_path=entry['path'])
                gates[arm]=strategy.resume_gate(parent,web,short,b,check,heartbeat)
                arm_c=dict(recipe,peak_lr=b['peak_lr'],diagnostic_train_budget_seconds=600,mixed_train_budget_seconds=600)
                trained[arm]=packing.train(parent,web,short,arm_c,b,arm,'shuffle',c['goals'],heartbeat,check)
                evaluated[arm]=evaluation.evaluate(arm,trained[arm],dev,tok,recipe,trained[arm]['binding'],heartbeat,check,start[0]+1800-prior)
                aux[arm]=strategy.auxiliary(trained[arm],recipe,arm,heartbeat,check)
                write_json(RUN/'progress-result.json',dict(checkpoints=trained,evaluations=evaluated,auxiliary=aux))
                del parent;gc.collect();torch.cuda.empty_cache()
            result=dict(status='complete_pending_content_review',config_sha256=sha256(CONFIG),
                checkpoints=trained,evaluations=evaluated,auxiliary=aux,scientific_teacher_tokens=400000000,
                cumulative_teacher_tokens_per_strategy=300000000,
                verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in gates.values()),
                gpu_seconds=prior+time.monotonic()-start[0],protected_test_used=False,requested_five_steps_complete=False,completed_at=now())
            write_json(RUN/'compare-result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');a=p.parse_args()
    freeze() if a.freeze else run()
