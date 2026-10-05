"""Conditional stage3: two new10M configurations, reuse matched current300M.

Preparation is allowed only after the material study supplies real learning
and content evidence. Never alter the running/frozen material experiment.
"""
import argparse
import copy
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer,atomic_json,gpu_lock,implementation_hashes,seed_all
from phase6_performance import identity,alive,finite_state
from resume_curriculum_strategy import BootstrapStrategyTrainer
import run_material_comparison as material
import run_curriculum_strategy as strategy
import run_packing_study as packing
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/architecture-comparison-20261006'
CONFIG=ROOT/'configs/phase6/architecture_comparison.json'
MATERIAL_RUN=material.RUN
PROPOSAL=ROOT/'reports/phase6/strategy_architecture_proposal.json'
SOURCES=('scripts/run_architecture_comparison.py','scripts/run_architecture_comparison.ps1',
    'scripts/run_material_comparison.py','scripts/resume_curriculum_strategy.py',
    'scripts/run_curriculum_strategy.py','scripts/run_packing_study.py','scripts/run_complete_text_comparison.py',
    'src/jmicro/curriculum_strategy.py','src/jmicro/natural_learning.py','src/jmicro/packing_study.py')


def eligible(review):
    """Gold prediction learns while practical unseen completion remains unmet.

    This is a research transition, never a weaker Base adoption criterion.
    """
    trained=review['summaries']['wikipedia']['auxiliary']['train32-wikipedia']
    initial=review['baseline']['train32-wikipedia']
    return (review['status']=='stage2_learning_and_content_evidence_complete'
        and not review['gates']['wikipedia']['adopted']
        and trained['teacher_NLL']<initial['teacher_NLL']
        and trained['teacher_top1_fraction']>initial['teacher_top1_fraction'])


def validate_parent(state,config,count):
    assert state['update']==state['tokens']==state['supervised_tokens']==0 and not state['optimizer']['state']
    assert state['model_config']==config and finite_state(state)
    assert torch.equal(state['model']['lm_head.weight'],state['model']['model.embed_tokens.weight'])
    assert sum(t.numel() for k,t in state['model'].items() if k!='lm_head.weight')==count
    assert state['spec']['context']==1024 and state['spec']['batch']==32
    assert state['spec']['accumulation']==1 and state['spec']['dtype']=='bf16' and state['spec']['warmup']==200


def freeze():
    if CONFIG.exists():load_config();print('Frozen architecture comparison retained');return
    base=material.load_config();review=read_json(MATERIAL_RUN/'review.json')
    assert eligible(review),'Conditional architecture evidence not satisfied; no GPU job created'
    job=read_json(MATERIAL_RUN/'job.json');assert job['status']=='complete' and not alive(job)
    result=read_json(MATERIAL_RUN/'compare-result.json');proposal=read_json(PROPOSAL)
    c={k:copy.deepcopy(base[k]) for k in ('web_shards','web_manifest_sha256','dev_shards','dev_manifest_sha256',
        'tokenizer','tokenizer_sha256','suite_sha256','evaluation','reference','goals','peak_lr','warmup_updates',
        'optimizer_policy','initialization','isolated_batch','diagnostic_train_budget_seconds','mixed_train_budget_seconds','schedule','reference_sha256')}
    arms={k:copy.deepcopy(proposal['candidates'][k]) for k in ('fewer_layers_more_FFN','wider_fewer_layers')}
    for entry in arms.values():
        model=JMicroModel(entry['model_config']);assert sum(p.numel() for p in model.parameters())==entry['parameters'];del model
    parent=torch.load(base['parent']['path'],map_location='cpu',weights_only=False);material.validate_parent(parent)
    c.update(version=1,scope='User five items stage3: maximum two new10M architectures, current matched300M reused',
        pool=copy.deepcopy(base['arms']['wikipedia']),arms=arms,parent_spec=parent['spec'],seed=42,
        gpu_budget_seconds=3600,reused_current=result['checkpoints']['wikipedia'],
        material_config_sha256=sha256(material.CONFIG),material_review_sha256=sha256(MATERIAL_RUN/'review.json'),
        material_result_sha256=sha256(MATERIAL_RUN/'compare-result.json'),proposal_sha256=sha256(PROPOSAL),
        implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        interpretation='Fresh models from same initialization seed, same10M material, Tokenizer, batch32, warmup200 and each300M teachers. Depth/width/FFN allocation differ together; not isolated capacity proof.',
        selection='Compare unchanged practical quality and common BPB plus Japanese tasks, paired raw80 content and GPU time. Best research recipe is not automatically an accepted Base.',
        scientific_teacher_tokens_new=600000000,reused_teacher_tokens=300000000,
        quality_criteria_unchanged=True,protected_test_used=False,created_at=now())
    RUN.mkdir(parents=True,exist_ok=True)
    for p,h in c['reference_sha256'].items():
        assert sha256(MATERIAL_RUN/'reference'/p)==h
        dest=RUN/'reference'/p;dest.parent.mkdir(exist_ok=True);shutil.copyfile(MATERIAL_RUN/'reference'/p,dest)
    write_json(CONFIG,c);print(json.dumps(dict(status='frozen',candidates={k:v['parameters'] for k,v in arms.items()},current_reused=True)),flush=True)


def load_config():
    material.load_config();c=read_json(CONFIG)
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES} and c['implementation']==implementation_hashes()
    for p,h in [(material.CONFIG,c['material_config_sha256']),(MATERIAL_RUN/'review.json',c['material_review_sha256']),
        (MATERIAL_RUN/'compare-result.json',c['material_result_sha256']),(PROPOSAL,c['proposal_sha256']),
        (Path(c['pool']['pool'])/'manifest.json',c['pool']['manifest_sha256']),
        *[(RUN/'reference'/p,h) for p,h in c['reference_sha256'].items()]]:assert sha256(p)==h
    return c


def new_parent(arm,entry,c,web,device='cuda'):
    # Trainer.save writes latest.json beside the file. Keep zero-update
    # parents out of the arm's resumable training directory.
    path=RUN/'parents'/arm/'initial-fresh.pt'
    if not path.exists():
        trainer=Trainer(entry['model_config'],web,copy.deepcopy(c['parent_spec']),device);trainer.save(path)
        del trainer;gc.collect();torch.cuda.empty_cache()
    state=torch.load(path,map_location='cpu',weights_only=False);validate_parent(state,entry['model_config'],entry['parameters'])
    return state,dict(path=str(path),sha256=sha256(path),update=0,tokens_seen=0)


def run():
    c=load_config();path=RUN/'job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['config_sha256']==sha256(CONFIG) and not alive(old)
        if old['status']=='complete':print('Completed architecture study retained');return
    prior=old.get('gpu_elapsed_seconds',0);start=[None];stop=[False]
    job=dict(status='running',**identity(),config_sha256=sha256(CONFIG),started_at=now(),gpu_elapsed_seconds=prior,
        restart_command='scripts/run_architecture_comparison.ps1 -Worker',requested_scope_complete=False)
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Stop requested; full completed-update checkpoint retained')
        if start[0] is not None and prior+time.monotonic()-start[0]>3600:raise TimeoutError('Architecture study3600s GPU budget exhausted')
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
        web=TrainView(c['web_shards'],c['web_manifest_sha256']);short=Shard(Path(c['pool']['pool']),'train')
        dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer'])
        strategy.RUN=RUN;strategy.StrategyTrainer=BootstrapStrategyTrainer
        packing.RUN=RUN;packing.PackingTrainer=BootstrapStrategyTrainer;evaluation.RUN=RUN/'evaluation';material.RUN=RUN
        trained={};evaluated={};aux={};gates={};baselines={}
        with gpu_lock('cuda'):
            start[0]=time.monotonic()
            for arm,entry in c['arms'].items():
                parent,parent_entry=new_parent(arm,entry,c,web)
                baselines[arm]=material.auxiliary(dict(checkpoint=parent_entry['path'],checkpoint_sha256=parent_entry['sha256']),c,
                    'initial-'+arm,['dev32','train32-wikipedia'],heartbeat,check)
                b=dict(config_sha256=sha256(CONFIG),parent=parent_entry,peak_lr=.002,warmup_updates=200,
                    optimizer_policy='fresh',initialization='new-random',arm=arm,isolated_batch=256,
                    short_manifest_sha256=c['pool']['manifest_sha256'],actual_parent_path=parent_entry['path'])
                gates[arm]=strategy.resume_gate(parent,web,short,b,check,heartbeat)
                trained[arm]=packing.train(parent,web,short,c,b,arm,'shuffle',c['goals'],heartbeat,check)
                evaluated[arm]=evaluation.evaluate(arm,trained[arm],dev,tok,c,trained[arm]['binding'],heartbeat,check,start[0]+3600-prior)
                aux[arm]=material.auxiliary(trained[arm],c,arm,['dev32','train32-wikipedia'],heartbeat,check)
                write_json(RUN/'progress-result.json',dict(checkpoints=trained,evaluations=evaluated,auxiliary=aux))
                del parent;gc.collect();torch.cuda.empty_cache()
            result=dict(status='complete_pending_content_review',config_sha256=sha256(CONFIG),checkpoints=trained,evaluations=evaluated,
                auxiliary=aux,baselines=baselines,reused_current=c['reused_current'],
                scientific_teacher_tokens_new=sum(d['additional_supervised_tokens'] for d in trained.values()),reused_current_teacher_tokens=300000000,
                valid_input_tokens_new=sum(d['additional_input_tokens'] for d in trained.values()),physical_input_tokens_new=sum(d['physical_input_tokens'] for d in trained.values()),
                verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in gates.values()),gpu_seconds=prior+time.monotonic()-start[0],
                protected_test_used=False,requested_five_steps_complete=False,completed_at=now())
            assert result['scientific_teacher_tokens_new']==600000000
            write_json(RUN/'compare-result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');a=p.parse_args()
    freeze() if a.freeze else run()
