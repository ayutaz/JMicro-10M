"""Bounded read-only source gradients; no optimizer update or new learning."""
import argparse
import gc
import hashlib
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.eos_pilot import TrainView
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state,restore_rng
from cached_three_source_index import CachedThreeSourceIndex
from story_weight_trainer import GenreStream
from condition_positive_trainer import PositiveStream
from phase6_performance import alive,identity
from run_eos_short_pilot import equal_state
from source_gradient_geometry import cosine,body_from_full,adamw_direction
import run_original_web_retention_comparison as study

RUN=ROOT/'reports/phase6/source-gradient-interference-20261006'
CONFIG=ROOT/'configs/phase6/source_gradient_interference.json'
PROPOSAL=ROOT/'reports/phase6/source_gradient_interference_proposal.json'
SEED,CONTEXT,BATCH,DRAWS,LIMIT=2026100641,1024,8,4,120
SOURCES=('scripts/diagnose_source_gradient_interference.py','scripts/diagnose_source_gradient_interference.ps1',
    'scripts/source_gradient_geometry.py','tests/test_source_gradient_geometry.py')
QUOTAS=dict(web=.75,story=.05,ordinary_textbook=.1,conditional_textbook=.1)


def prepare():
    if CONFIG.exists():inspect();return
    c,_,_,_,_,_,_=study.inspect(study.CONFIG)
    p=read_json(PROPOSAL);r=read_json(study.RUN/'compare-result.json')
    for ref in (p['endpoint_diagnostic'],p['review']):study.check_reference(ref)
    if p['GPU_limit_seconds']!=LIMIT or p['new_scientific_teacher_tokens'] or p['optimizer_updates']:
        raise ValueError('Read-only GPU120s proposal required')
    original=r['checkpoints'][study.ARM]
    config=dict(status='frozen_read_only_not_started',seed=SEED,context=CONTEXT,batch=BATCH,draws_per_source=DRAWS,
        GPU_limit_seconds=LIMIT,new_scientific_teacher_tokens=0,optimizer_updates=0,
        checkpoints=dict(parent10B=c['parent'],retention100M=dict(path=original['checkpoint'],sha256=original['checkpoint_sha256'])),
        references=dict(proposal=study.reference(PROPOSAL),study_config=study.reference(study.CONFIG),
            study_result=study.reference(study.RUN/'compare-result.json'),endpoint_diagnostic=p['endpoint_diagnostic'],review=p['review']),
        frozen_study_sources=c['source_sha256'],source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        marker_cosine_at_most=-.05,marker_negative_batches_at_least=3,hypothetical_teacher_weights=QUOTAS,
        Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,created_at=now())
    atomic_json(CONFIG,config);inspect();print('Frozen read-only source-gradient diagnostic; no learning')


def inspect():
    c=read_json(CONFIG)
    if (c['source_sha256']!={p:sha256(ROOT/p) for p in SOURCES} or c['implementation']!=implementation_hashes()
            or c['frozen_study_sources']!={p:sha256(ROOT/p) for p in c['frozen_study_sources']}
            or (c['seed'],c['context'],c['batch'],c['draws_per_source'],c['GPU_limit_seconds'])!=(SEED,CONTEXT,BATCH,DRAWS,LIMIT)
            or c['new_scientific_teacher_tokens'] or c['optimizer_updates'] or c['hypothetical_teacher_weights']!=QUOTAS
            or c['marker_cosine_at_most']!=-.05 or c['marker_negative_batches_at_least']!=3
            or c['Base_adopted'] or c['Chat_started'] or c['quantization_started'] or c['protected_test_used']):
        raise ValueError('Frozen read-only diagnostic differs')
    for ref in (*c['references'].values(),*c['checkpoints'].values()):study.check_reference(ref)
    job=read_json(study.RUN/'job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Completed study required; no competing GPU job')
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual diagnostic live; no duplicate')
    return c


def samples(c):
    _,_,_,_,_,positive,original=study.source_contract()
    recipe=read_json(study.CONFIG);study.check_reference(recipe['accepted_compact_index'])
    pool=TrainView(recipe['pool']['pool'],recipe['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused or not np.array_equal(pool.byte_lengths,original.byte_lengths):
        raise ValueError('Accepted compact cache/common bytes required')
    streams=dict(story=GenreStream(pool,'story',SEED),ordinary_textbook=GenreStream(pool,'textbook',SEED),
                 conditional_textbook=PositiveStream(positive,SEED))
    selected=np.random.default_rng(SEED).choice((len(original.tokens)-1)//CONTEXT,size=BATCH*DRAWS,replace=False)
    tensors={};rows=[]
    for source in QUOTAS:
        for draw in range(DRAWS):
            xs,ys=[],[];indices=[];before=streams[source].state_dict() if source!='web' else None
            for sample in range(BATCH):
                if source=='web':
                    block=int(selected[draw*BATCH+sample]);indices.append(block);offset=block*CONTEXT
                    x=np.asarray(original.tokens[offset:offset+CONTEXT],dtype=np.int64).copy()
                    y=np.asarray(original.tokens[offset+1:offset+CONTEXT+1],dtype=np.int64).copy();y[y==2]=-100
                else:
                    x,y,*_=streams[source].block(CONTEXT)
                xs.append(x);ys.append(y)
            x=np.stack(xs);y=np.stack(ys)
            if np.any(x==0) or np.any((y<8)&(y!=-100)&(y!=3)) or not np.any(y==3):
                raise ValueError('Unpadded full body+EOS train sample required')
            tensors[(source,draw)]=(torch.from_numpy(x),torch.from_numpy(y))
            rows.append(dict(source=source,draw=draw,input_sha256=hashlib.sha256(x.astype('<i8').tobytes()).hexdigest(),
                target_sha256=hashlib.sha256(y.astype('<i8').tobytes()).hexdigest(),teachers=int(np.count_nonzero(y!=-100)),
                body_teachers=int(np.count_nonzero(y>=8)),EOS_teachers=int(np.count_nonzero(y==3)),
                body_bytes=int(pool.byte_lengths[y[y>=8]].sum()),original_Web_blocks=indices,cursor_before=before,
                cursor_after=streams[source].state_dict() if source!='web' else None))
    report=dict(seed=SEED,context=CONTEXT,batch=BATCH,draws=DRAWS,rows=rows,
        pool_manifest_sha256=recipe['pool']['manifest_sha256'],original_Web_manifest_sha256=recipe['original_web']['manifest_sha256'],
        conditional_manifest_sha256=positive.manifest_sha256,cache_reused=True,split='train')
    path=RUN/'samples.json'
    if path.exists() and read_json(path)!=report:raise ValueError('Saved fixed samples differ')
    atomic_json(path,report);return tensors,rows


def run():
    c=inspect();jp=RUN/'job.json';old=read_json(jp) if jp.exists() else {}
    if old.get('status')=='complete':print('Completed read-only diagnosis retained');return
    if old and old['config_sha256']!=sha256(CONFIG):raise ValueError('Saved job differs')
    RUN.mkdir(parents=True,exist_ok=True)
    previous_seconds=old.get('GPU_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=old.get('started_at',now()),
        GPU_seconds=previous_seconds,restart_command='scripts/diagnose_source_gradient_interference.ps1 -Worker',optimizer_updates=0)
    atomic_json(jp,job)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Read-only diagnosis interrupted')
        if started[0] is not None and previous_seconds+time.monotonic()-started[0]>LIMIT:raise TimeoutError('GPU120s exhausted')
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        inputs,metadata=samples(c);cfg=sha256(CONFIG);sample_sha=sha256(RUN/'samples.json')
        models={}
        with gpu_lock('cuda'):
            started[0]=time.monotonic();before_rng=rng_state()
            try:
                for arm,ref in c['checkpoints'].items():
                    check();state=torch.load(ref['path'],map_location='cpu',weights_only=False)
                    model=JMicroModel(state['model_config']).to('cuda');model.load_state_dict(state['model'],strict=True);model.train()
                    parameters=[p for p in model.parameters() if p.ndim>=2]+[p for p in model.parameters() if p.ndim<2]
                    records=[]
                    for draw in range(DRAWS):
                        path=RUN/f'points/{arm}/{draw:02d}.json'
                        if path.exists():
                            record=read_json(path)
                            if record['config_sha256']!=cfg or record['samples_sha256']!=sample_sha or record['checkpoint_sha256']!=ref['sha256']:
                                raise ValueError('Saved read-only point differs')
                        else:
                            gradients={};losses={};checks=[]
                            for source in QUOTAS:
                                check();x,y=inputs[(source,draw)];x=x.to('cuda');y=y.to('cuda')
                                with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                                    logits=model(x,training_fast_path=True).logits
                                    ce=F.cross_entropy(logits.flatten(0,1),y.flatten(),ignore_index=-100,reduction='none').view_as(y)
                                    full=ce[y!=-100].mean();eos=ce[y==3].mean()
                                teachers=int((y!=-100).sum());eos_count=int((y==3).sum())
                                fg=torch.cat([v.detach().flatten() for v in torch.autograd.grad(full,parameters,retain_graph=True)])
                                eg=torch.cat([v.detach().flatten() for v in torch.autograd.grad(eos,parameters)])
                                bg=body_from_full(fg,eg,teachers,eos_count)
                                checks.append(all(torch.isfinite(v).all().item() for v in (fg,eg,bg)))
                                gradients[source]=dict(full=fg,EOS=eg,body=bg)
                                losses[source]=dict(full_CE=float(full.detach()),EOS_CE=float(eos.detach()),teachers=teachers,EOS_teachers=eos_count)
                                del x,y,logits,ce,full,eos,fg,eg,bg
                            if not all(checks):raise ValueError('Nonfinite source gradients')
                            aggregate=sum(QUOTAS[s]*g['full'] for s,g in gradients.items())
                            direction=adamw_direction(parameters,aggregate,state['optimizer'])
                            record=dict(config_sha256=cfg,samples_sha256=sample_sha,checkpoint_sha256=ref['sha256'],draw=draw,
                                losses=losses,full_CE_pairs={a+'|'+b:cosine(gradients[a]['full'],gradients[b]['full']) for a,b in itertools.combinations(QUOTAS,2)},
                                body_pairs={a+'|'+b:cosine(gradients[a]['body'],gradients[b]['body']) for a,b in itertools.combinations(QUOTAS,2)},
                                body_EOS={s:cosine(g['body'],g['EOS']) for s,g in gradients.items()},
                                conditional_EOS_vs_Web_body=cosine(gradients['conditional_textbook']['EOS'],gradients['web']['body']),
                                hypothetical_quota_AdamW_first_order_loss_change={s:float(torch.dot(g['full'],-direction)) for s,g in gradients.items()},
                                checks=dict(finite_gradients=True,no_parameter_gradients=all(p.grad is None for p in parameters)),optimizer_updates=0)
                            atomic_json(path,record);del gradients,aggregate,direction
                        records.append(record);job.update(stage=arm,draws_complete=len(records),GPU_seconds=previous_seconds+time.monotonic()-started[0],heartbeat_at=now());atomic_json(jp,job)
                    checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),state['model'][k]) for k,v in model.state_dict().items()),
                        no_parameter_gradients=all(p.grad is None for p in parameters))
                    if not all(checks.values()):raise ValueError('Read-only gradient assay altered parameters')
                    conflicts={pair:sum(v['full_CE_pairs'][pair]['cosine'] is not None and v['full_CE_pairs'][pair]['cosine']<=-.05 for v in records)
                        for pair in records[0]['full_CE_pairs']}
                    rises={s:sum(v['hypothetical_quota_AdamW_first_order_loss_change'][s]>0 for v in records) for s in QUOTAS}
                    models[arm]=dict(checks=checks,records=records,negative_cosine_batches=conflicts,predicted_loss_rise_batches=rises,
                        source_conflict_marker=any(n>=3 for n in conflicts.values()) or any(n>=3 for n in rises.values()))
                    del state,model,parameters,records;gc.collect();torch.cuda.empty_cache()
            finally:restore_rng(before_rng)
            if not equal_state(before_rng,rng_state()):raise ValueError('RNG not restored')
            check();elapsed=previous_seconds+time.monotonic()-started[0]
            result=dict(status='actual_two_checkpoint_fixed_source_gradient_assay_complete',created_at=now(),models=models,
                config_sha256=cfg,samples_sha256=sample_sha,GPU_seconds=elapsed,optimizer_updates=0,scientific_teacher_tokens=0,
                full_CE_scored_teacher_tokens=2*sum(v['teachers'] for v in metadata),EOS_scored_teacher_tokens=2*sum(v['EOS_teachers'] for v in metadata),
                RNG_restored=True,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
                limitations='Four fixed train batches/source, two related checkpoints, not independent quality evidence or causality. Negative gradient geometry and hypothetical first-order inherited-AdamW loss change do not measure actual finite-step harm or guarantee projection helps. No optimizer created/updated; old quality scores unchanged.')
            atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/source_gradient_interference_diagnostic.json',result)
            job.update(status='complete',completed_at=now(),GPU_seconds=elapsed)
            print(dict(GPU_seconds=elapsed,models={a:{k:v[k] for k in ('source_conflict_marker','negative_cosine_batches','predicted_loss_rise_batches')} for a,v in models.items()}))
    except BaseException as error:
        job.update(status='failed',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_seconds']=previous_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--preflight',action='store_true');a=p.parse_args()
    if a.prepare:prepare()
    elif a.preflight:inspect()
    else:run()
