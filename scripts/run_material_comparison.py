"""Stage2: equal fresh300M, old curriculum vs new literal Wikipedia leads."""
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
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,implementation_hashes,seed_all
from phase6_performance import identity,alive,finite_state
from resume_curriculum_strategy import BootstrapStrategyTrainer
from run_generation_transfer import make_case
from run_root_cause_diagnostic import teacher,generate
import run_curriculum_strategy as strategy
import run_packing_study as packing
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/material-comparison-20261006'
CONFIG=ROOT/'configs/phase6/material_comparison.json'
NEW=Path('/home/aihub_ubuntu/jmicro-data/phase6/wikipedia-curriculum-20261006-v3')
NEW_RUN=ROOT/'reports/phase6/wikipedia-curriculum-20261006-v3'
SOURCES=('scripts/run_material_comparison.py','scripts/run_material_comparison.ps1',
    'scripts/resume_curriculum_strategy.py','scripts/run_curriculum_strategy.py',
    'scripts/run_packing_study.py','scripts/run_complete_text_comparison.py',
    'scripts/run_generation_transfer.py','scripts/run_root_cause_diagnostic.py',
    'src/jmicro/curriculum_strategy.py','src/jmicro/natural_learning.py','src/jmicro/packing_study.py')


def validate_parent(state):
    assert state['update']==state['tokens']==state['supervised_tokens']==0
    assert not state['optimizer']['state'] and finite_state(state)
    assert state['spec']['warmup']==200 and state['spec']['lr']==.002
    assert state['spec']['context']==1024 and state['spec']['batch']==32
    assert state['spec']['accumulation']==1 and state['spec']['dtype']=='bf16'
    assert state['spec']['compile'] and state['spec']['training_fast_path']
    assert torch.equal(state['model']['lm_head.weight'],state['model']['model.embed_tokens.weight'])
    assert sum(t.numel() for k,t in state['model'].items() if k!='lm_head.weight')==10001152


def freeze():
    if CONFIG.exists():load_config();print('Frozen material comparison retained');return
    recipe=strategy.load_config();ready=read_json(NEW/'ready.json');review=read_json(NEW_RUN/'content-review.json')
    assert review['passed'] and review['weak_documents']<=10 and len(review['reviews'])==64
    assert review['sample_sha256']==ready['sample_sha256']==sha256(NEW/'sample64.json')
    assert review['ready_sha256']==sha256(NEW/'ready.json')
    source_job=read_json(NEW_RUN/'prepare-job.json');assert source_job['status']=='complete' and not alive(source_job)
    parent_path=strategy.RUN/'initial-fresh.pt';parent=torch.load(parent_path,map_location='cpu',weights_only=False)
    validate_parent(parent)
    c={k:copy.deepcopy(recipe[k]) for k in ('web_shards','web_manifest_sha256','dev_shards','dev_manifest_sha256',
        'tokenizer','tokenizer_sha256','suite_sha256','evaluation','reference')}
    c.update(version=1,scope='User five-item objective, stage2 material comparison; not complete project',
        parent=dict(path=str(parent_path),sha256=sha256(parent_path),update=0,tokens_seen=0),
        arms=dict(control=dict(recipe['curriculum']),wikipedia=dict(pool=ready['pool'],manifest_sha256=ready['manifest_sha256'])),
        goals=dict(web=0,short=300000000),peak_lr=.002,warmup_updates=200,
        optimizer_policy='fresh',initialization='new-random',isolated_batch=256,
        diagnostic_train_budget_seconds=600,mixed_train_budget_seconds=600,gpu_budget_seconds=1800,
        preparation_sha256=sha256(NEW/'ready.json'),content_review_sha256=sha256(NEW_RUN/'content-review.json'),
        previous_recipe_sha256=sha256(strategy.CONFIG),implementation=implementation_hashes(),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        schedule='One continuous300M body/EOS teachers; first200updates warmup,90percent stable/10percent decay; no100M terminal/reheat',
        interpretation='Source/genre/length/EOS-density comparison, not amount-only. Same fresh weights/RNG/Adam seed, teacher budget and LR schedule.',
        selection='Inspect common Web BPB, threeJapanese tasks, all80 raw outputs and common heldout32. Material recipe preference is distinct from unchanged practical/Base adoption.',
        quality_criteria_unchanged=True,protected_test_used=False,created_at=now())
    RUN.mkdir(parents=True,exist_ok=True);reference=RUN/'reference';reference.mkdir(exist_ok=True)
    common=read_json(NEW/'dev32.json');assert len(common)==32
    known={r['canonical_sha256'] for r in common}
    for arm,entry in c['arms'].items():
        shard=Shard(Path(entry['pool']),'train')
        assert len(shard.tokens)>=10000000 and sha256(Path(entry['pool'])/'manifest.json')==entry['manifest_sha256']
        assert not known & {r['canonical_sha256'] for r in shard.index}
        data=NEW if arm=='wikipedia' else strategy.DATA
        sample=read_json(data/'sample64.json');assert len(sample)==64
        write_json(reference/('train32-'+arm+'.json'),sample[:32])
    write_json(reference/'dev32.json',common)
    c['reference_sha256']={p.name:sha256(p) for p in sorted(reference.glob('*.json'))}
    c['common_dev32_audit']='Exact hashes disjoint from both local train pools; Wikipedia article-family split; old-Web cross-corpus near-duplicate audit incomplete'
    write_json(CONFIG,c)
    print(json.dumps(dict(status='frozen',parent=c['parent'],arms=c['arms'],teachers=c['goals'],GPU_budget=1800)),flush=True)


def load_config():
    strategy.load_config();c=read_json(CONFIG)
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert c['implementation']==implementation_hashes() and sha256(strategy.CONFIG)==c['previous_recipe_sha256']
    for path,digest in [(NEW/'ready.json',c['preparation_sha256']),(NEW_RUN/'content-review.json',c['content_review_sha256']),
        (Path(c['parent']['path']),c['parent']['sha256']),*[(RUN/'reference'/p,h) for p,h in c['reference_sha256'].items()],
        *[(Path(e['pool'])/'manifest.json',e['manifest_sha256']) for e in c['arms'].values()]]:
        assert sha256(path)==digest
    return c


def auxiliary(detail,c,arm,groups,heartbeat,check):
    path=RUN/arm/'auxiliary.json'
    if path.exists():
        r=read_json(path);assert r['checkpoint_sha256']==detail['checkpoint_sha256'];return r
    state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
    memory=bound_evaluation_cache(model);tok=Tokenizer(ROOT/c['tokenizer']);results={}
    with sdpa_kernel(SDPBackend.MATH):
        for group in groups:
            records=read_json(RUN/'reference'/(group+'.json'));cases=[make_case(r,tok,'dev' if group=='dev32' else 'train') for r in records]
            rows=[];gold=[]
            for offset in range(0,32,16):
                check();heartbeat(arm+'-'+group);gold.extend(teacher(model,cases[offset:offset+16]))
                rows.extend(generate(model,cases[offset:offset+16],tok,None,64))
            results[group]=dict(cases_sha256=c['reference_sha256'][group+'.json'],teacher=gold,generation=rows,
                summary=dict(documents=32,EOS=sum(r['stop_reason']=='eos' for r in rows),
                    repeated4gram=sum(r['first_repeated_4gram'] is not None for r in rows),
                    teacher_NLL=sum(r['teacher_nll_mean'] for r in gold)/32,
                    teacher_top1_fraction=sum(r['teacher_top1_fraction'] for r in gold)/32))
    result=dict(checkpoint_sha256=detail['checkpoint_sha256'],results=results,memory=memory,
        source_history='Both science arms start at zero updates; commondev32 exact-disjoint local training and heldout article family. Global near duplicates not independently audited.')
    write_json(path,result);del model;gc.collect();torch.cuda.empty_cache();return result


def run():
    c=load_config();recipe=strategy.load_config();path=RUN/'job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['config_sha256']==sha256(CONFIG) and not alive(old)
        if old['status']=='complete':print('Completed material comparison retained');return
    prior=old.get('gpu_elapsed_seconds',0);start=[None];stop=[False]
    job=dict(status='running',**identity(),config_sha256=sha256(CONFIG),started_at=now(),gpu_elapsed_seconds=prior,
        restart_command='scripts/run_material_comparison.ps1 -Worker',requested_scope_complete=False)
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Stop requested; completed-update state retained')
        if start[0] is not None and prior+time.monotonic()-start[0]>c['gpu_budget_seconds']:raise TimeoutError('Material comparison1800s GPU budget exhausted')
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
        web=TrainView(c['web_shards'],c['web_manifest_sha256']);dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer'])
        packing.RUN=RUN;packing.PackingTrainer=BootstrapStrategyTrainer
        strategy.RUN=RUN;strategy.StrategyTrainer=BootstrapStrategyTrainer;evaluation.RUN=RUN/'evaluation'
        trained={};evaluated={};aux={};gates={}
        with gpu_lock('cuda'):
            start[0]=time.monotonic();initial=dict(checkpoint=c['parent']['path'],checkpoint_sha256=c['parent']['sha256'])
            baseline=auxiliary(initial,c,'initial',['dev32','train32-control','train32-wikipedia'],heartbeat,check)
            for arm,entry in c['arms'].items():
                parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);validate_parent(parent)
                short=Shard(Path(entry['pool']),'train')
                b=dict(config_sha256=sha256(CONFIG),parent=c['parent'],peak_lr=c['peak_lr'],warmup_updates=c['warmup_updates'],
                    optimizer_policy='fresh',initialization='new-random',arm=arm,isolated_batch=256,
                    short_manifest_sha256=entry['manifest_sha256'],actual_parent_path=c['parent']['path'])
                gates[arm]=strategy.resume_gate(parent,web,short,b,check,heartbeat)
                trained[arm]=packing.train(parent,web,short,c,b,arm,'shuffle',c['goals'],heartbeat,check)
                evaluated[arm]=evaluation.evaluate(arm,trained[arm],dev,tok,recipe,trained[arm]['binding'],heartbeat,check,start[0]+1800-prior)
                aux[arm]=auxiliary(trained[arm],c,arm,['dev32','train32-'+arm],heartbeat,check)
                write_json(RUN/'progress-result.json',dict(checkpoints=trained,evaluations=evaluated,auxiliary=aux))
                del parent;gc.collect();torch.cuda.empty_cache()
            result=dict(status='complete_pending_content_review',config_sha256=sha256(CONFIG),checkpoints=trained,evaluations=evaluated,
                auxiliary=aux,baseline=baseline,scientific_teacher_tokens=sum(d['additional_supervised_tokens'] for d in trained.values()),
                valid_input_tokens=sum(d['additional_input_tokens'] for d in trained.values()),physical_input_tokens=sum(d['physical_input_tokens'] for d in trained.values()),
                verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in gates.values()),
                gpu_seconds=prior+time.monotonic()-start[0],protected_test_used=False,requested_five_steps_complete=False,completed_at=now())
            assert result['scientific_teacher_tokens']==600000000
            write_json(RUN/'compare-result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');a=p.parse_args()
    freeze() if a.freeze else run()
