"""First saved8.15M vs completed100M; bounded read-only evaluation."""
import argparse
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import shutil
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state,restore_rng
from jmicro.eos_pilot import TrainView
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import alive,identity
from run_eos_short_pilot import equal_state
from cached_three_source_index import CachedThreeSourceIndex
from story_weight_trainer import GenreStream
from condition_positive_trainer import PositiveStream
import run_original_web_retention_comparison as previous
import run_complete_text_comparison as evaluation
import run_condition_source_ranking as ranking

RUN=ROOT/'reports/phase6/early-exposure-comparison-20261006'
CONFIG=ROOT/'configs/phase6/early_exposure_comparison.json'
PROPOSAL=ROOT/'reports/phase6/early_exposure_comparison_proposal.json'
ARM='early8M';LIMIT=450
SOURCES=tuple(dict.fromkeys(('scripts/run_early_exposure_comparison.py','scripts/run_early_exposure_comparison.ps1',
    'scripts/review_early_exposure_comparison.py','tests/test_early_exposure_comparison.py',*previous.SOURCES)))
reference,check_reference=previous.reference,previous.check_reference
summarize_transfer=previous.summarize_transfer


def scope(c):
    if (c['research_kind']!='earliest_saved8M_vs_nested100M_read_only' or c['GPU_limit_seconds']!=LIMIT
            or c['new_scientific_teacher_tokens'] or c['optimizer_updates'] or c['reused_scientific_trajectory_tokens']!=100000000
            or c['early']['additional_teachers']!=8150782 or c['early']['additional_inputs']!=8192000
            or c['early']['update']!=305426 or c['early']['sampler_position']!=250
            or not c['quality_criteria_unchanged'] or c['Base_adopted'] or c['Chat_started']
            or c['quantization_started'] or c['protected_test_used']):
        raise ValueError('Read-only first saved checkpoint scope differs')


def early_contract(s,inventory):
    if (s['update']!=inventory['update'] or s['sampler']['position']!=250
            or s['supervised_tokens']-s['lineage']['parent_supervised_tokens']!=inventory['additional_teachers']
            or s['tokens']-s['lineage']['parent_tokens']!=inventory['additional_inputs']
            or s['sampler']['source_teachers']!=inventory['source_teachers']
            or sum(s['sampler']['source_teachers'].values())!=inventory['additional_teachers']
            or s['study_binding']!=inventory['study_binding']
            or s['spec']['research_kind']!=previous.KIND or s['spec']['outcome_weight']!=1
            or not s['lineage']['no_reheat'] or any(g['lr']!=.0002 for g in s['optimizer']['param_groups'])):
        raise ValueError('Actual saved250-update inherited checkpoint differs')


def prepare():
    if CONFIG.exists():inspect();return
    old,_,_,_,_,_,_=previous.inspect(previous.CONFIG)
    p=read_json(PROPOSAL)
    for key in ('completed_result','endpoint_diagnostic','gradient_diagnostic'):check_reference(p[key])
    check_reference(p['early']['checkpoint'])
    if p['new_GPU_ceiling_seconds']!=LIMIT or p['new_scientific_teacher_tokens'] or p['optimizer_updates']:
        raise ValueError('Bounded read-only exposure proposal required')
    references={k:p[k] for k in ('completed_result','endpoint_diagnostic','gradient_diagnostic')}
    references.update(proposal=reference(PROPOSAL),inventory=reference(ROOT/'reports/phase6/original_Web_early_checkpoint_inventory.json'),
        original_config=old['original_config'],original_study_config=reference(previous.CONFIG),
        final_review=reference(ROOT/'reports/phase6/original_web_retention_comparison_review.json'),
        final_notes=reference(ROOT/'reports/phase6/original_web_retention_notes.json'),
        final_generation=reference(previous.RUN/'evaluation/original_web/evaluation/generation.json'),
        fixed_train_samples=reference(ROOT/'reports/phase6/source-gradient-interference-20261006/samples.json'),
        source_cases=old['references']['source_cases'],retention_cases=old['references']['retention_cases'])
    c=dict(research_kind='earliest_saved8M_vs_nested100M_read_only',early=p['early'],references=references,
        GPU_limit_seconds=LIMIT,new_scientific_teacher_tokens=0,optimizer_updates=0,reused_scientific_trajectory_tokens=100000000,
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        quality_criteria_unchanged=True,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,created_at=now())
    scope(c);atomic_json(CONFIG,c);inspect();print('Frozen earliest saved checkpoint; read-only GPU450s/no learning')


def inspect():
    c=read_json(CONFIG);scope(c)
    if c['source_sha256']!={p:sha256(ROOT/p) for p in SOURCES} or c['implementation']!=implementation_hashes():
        raise ValueError('Frozen evaluator sources differ')
    for ref in (*c['references'].values(),c['early']['checkpoint']):check_reference(ref)
    if read_json(Path(c['references']['inventory']['path']))!=c['early']:raise ValueError('Early inventory differs')
    old,base,parent,_,_,positive,original=previous.inspect(previous.CONFIG)
    r=read_json(Path(c['references']['completed_result']['path']))
    saved=torch.load(c['early']['checkpoint']['path'],map_location='cpu',weights_only=False);early_contract(saved,c['early'])
    if saved['study_binding']['config_sha256']!=sha256(previous.CONFIG):raise ValueError('Actual trajectory binding differs')
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual evaluation live; no duplicate')
    return c,base,r,old,positive,original


def binding(c):
    return dict(config_sha256=sha256(CONFIG),arm=ARM,checkpoint=c['early']['checkpoint'],
        training_binding=c['early']['study_binding'],evaluation_only=True,optimizer_updates=0)


def loss_parts(ce,y):
    if torch.any((y<8)&(y!=-100)&(y!=3)) or not torch.any(y==3) or not torch.any(y>=8):
        raise ValueError('Complete body/EOS teacher masks required')
    if not torch.isfinite(ce[y!=-100]).all():raise ValueError('Finite scored CE required')
    return dict(full_CE=float(ce[y!=-100].mean()),body_CE=float(ce[y>=8].mean()),EOS_CE=float(ce[y==3].mean()),
        teachers=int((y!=-100).sum()),body_teachers=int((y>=8).sum()),EOS_teachers=int((y==3).sum()))


def fixed_train_fit(c,old,positive,original,heartbeat,check):
    target=RUN/'fixed-train-fit.json';cfg=sha256(CONFIG);sample_ref=c['references']['fixed_train_samples']
    if target.exists():
        r=read_json(target)
        if r['config_sha256']!=cfg or r['samples_sha256']!=sample_ref['sha256']:raise ValueError('Saved fit binding differs')
        return r
    check_reference(old['accepted_compact_index']);pool=TrainView(old['pool']['pool'],old['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused:raise ValueError('Accepted cache must be reused')
    sample=read_json(Path(sample_ref['path']));seed=sample['seed'];context=sample['context'];batch=sample['batch']
    streams=dict(story=GenreStream(pool,'story',seed),ordinary_textbook=GenreStream(pool,'textbook',seed),
                 conditional_textbook=PositiveStream(positive,seed))
    before_rng=rng_state();s=torch.load(c['early']['checkpoint']['path'],map_location='cpu',weights_only=False)
    model=JMicroModel(s['model_config']).to('cuda').eval();model.load_state_dict(s['model'],strict=True);rows=[]
    try:
        with torch.inference_mode(),sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
            for meta in sample['rows']:
                check();source=meta['source'];xs,ys=[],[]
                if source!='web':streams[source].load_state_dict(meta['cursor_before'])
                for index in range(batch):
                    if source=='web':
                        offset=meta['original_Web_blocks'][index]*context
                        x=np.asarray(original.tokens[offset:offset+context],dtype=np.int64).copy()
                        y=np.asarray(original.tokens[offset+1:offset+context+1],dtype=np.int64).copy();y[y==2]=-100
                    else:x,y,*_=streams[source].block(context)
                    xs.append(x);ys.append(y)
                x=np.stack(xs);y=np.stack(ys)
                if (hashlib.sha256(x.astype('<i8').tobytes()).hexdigest()!=meta['input_sha256']
                        or hashlib.sha256(y.astype('<i8').tobytes()).hexdigest()!=meta['target_sha256']):
                    raise ValueError('Identical fixed train input/teachers required')
                x=torch.from_numpy(x).to('cuda');y=torch.from_numpy(y).to('cuda')
                logits=model(x,training_fast_path=True).logits
                ce=F.cross_entropy(logits.flatten(0,1),y.flatten(),ignore_index=-100,reduction='none').view_as(y)
                parts=loss_parts(ce,y)
                if parts['teachers']!=meta['teachers'] or parts['EOS_teachers']!=meta['EOS_teachers']:raise ValueError('Same counted teachers required')
                rows.append(dict(source=source,draw=meta['draw'],input_sha256=meta['input_sha256'],target_sha256=meta['target_sha256'],**parts))
                heartbeat('fixed-train-fit',completed_batches=len(rows));del x,y,logits,ce
        checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),s['model'][k]) for k,v in model.state_dict().items()),
                    no_gradients=all(p.grad is None for p in model.parameters()))
    finally:restore_rng(before_rng)
    checks['RNG_restored']=equal_state(before_rng,rng_state())
    if not all(checks.values()) or len(rows)!=16:raise ValueError('Read-only fixed16 fit required')
    r=dict(config_sha256=cfg,checkpoint_sha256=c['early']['checkpoint']['sha256'],samples_sha256=sample_ref['sha256'],rows=rows,checks=checks,
        optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False)
    atomic_json(target,r);del s,model;gc.collect();torch.cuda.empty_cache();return r


def transfer_scores(c,arm,checkpoint,heartbeat,check,suite='bridge'):
    cases_key='source_cases' if suite=='bridge' else 'retention_cases'
    folder=RUN/'transfer'/suite/arm;terminal=folder/'result.json';cfg=sha256(CONFIG);cases_sha=c['references'][cases_key]['sha256']
    check_reference(checkpoint)
    if terminal.exists():
        saved=read_json(terminal)
        if saved['config_sha256']!=cfg or saved['checkpoint_sha256']!=checkpoint['sha256'] or saved['cases_sha256']!=cases_sha:raise ValueError('Saved transfer binding differs')
        return saved
    prepared=read_json(Path(c['references'][cases_key]['path']));before_rng=rng_state()
    state=torch.load(checkpoint['path'],map_location='cpu',weights_only=False);model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
    before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()};scorer=NativeLikelihood(model,None,'cuda','bf16',16)
    hook=model.register_forward_pre_hook(lambda *_:check());rows=[]
    try:
        with sdpa_kernel(SDPBackend.MATH):
            for start in range(0,512,16):
                cases=prepared['cases'][start:start+16];path=folder/f'{start:04d}.json';check()
                if path.exists():
                    saved=read_json(path)
                    if saved['config_sha256']!=cfg or saved['checkpoint_sha256']!=checkpoint['sha256'] or saved['cases_sha256']!=cases_sha:raise ValueError('Saved transfer request differs')
                    scored=saved['rows']
                else:
                    scored=[dict(index=case['index'],**r) for case,r in zip(cases,scorer.score_encoded(cases),strict=True)]
                    ranking.validate_scores(scored,cases);atomic_json(path,dict(config_sha256=cfg,checkpoint_sha256=checkpoint['sha256'],cases_sha256=cases_sha,rows=scored))
                ranking.validate_scores(scored,cases);rows.extend(scored);heartbeat(arm+'-transfer128',completed_requests=len(rows),total_requests=512)
        checks=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training)
    finally:hook.remove();restore_rng(before_rng)
    checks['RNG_restored']=equal_state(before_rng,rng_state())
    if not all(checks.values()):raise ValueError('Read-only transfer scoring altered weights/RNG')
    result=dict(config_sha256=cfg,checkpoint_sha256=checkpoint['sha256'],cases_sha256=cases_sha,checks=checks,
        summary=summarize_transfer(rows,prepared),evaluated_requests=512,optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
        suite=suite,limitations='Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement.')
    atomic_json(terminal,result);del state,model,before,scorer;gc.collect();torch.cuda.empty_cache();return result



def run():
    c,base,prior,old,positive,original=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json'
    previous_job=read_json(jp) if jp.exists() else {}
    if previous_job.get('status')=='complete':print('Completed read-only exposure comparison retained');return
    if previous_job and previous_job['config_sha256']!=sha256(CONFIG):raise ValueError('Prior job binding differs')
    prior_seconds=previous_job.get('GPU_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),GPU_seconds=prior_seconds,started_at=previous_job.get('started_at',now()),
        restart_command='scripts/run_early_exposure_comparison.ps1 -Worker',optimizer_updates=0,scientific_teacher_tokens=0)
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Read-only evaluation interrupted')
        if started[0] is not None and prior_seconds+time.monotonic()-started[0]>LIMIT:raise TimeoutError('GPU450s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for relative in (*SOURCES,*c['implementation'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Frozen source snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        record=dict(checkpoint=c['early']['checkpoint']['path'],checkpoint_sha256=c['early']['checkpoint']['sha256'],binding=binding(c),
            additional_supervised_tokens=c['early']['additional_teachers'],additional_input_tokens=c['early']['additional_inputs'],read_only=True)
        progress=RUN/'progress-result.json'
        result=read_json(progress) if progress.exists() else dict(checkpoints={ARM:record,'final100M':prior['checkpoints'][previous.ARM]},
            evaluations={'final100M':prior['evaluations'][previous.ARM]},
            transfer={'final100M':prior['transfer'][previous.ARM]},retention={'final100M':prior['retention'][previous.ARM]})
        if result['checkpoints'][ARM]!=record or result['evaluations']['final100M']!=prior['evaluations'][previous.ARM]:raise ValueError('Early/final records differ')
        with gpu_lock('cuda'):
            started[0]=time.monotonic();before=rng_state()
            try:
                if ARM not in result['evaluations']:
                    evaluation.RUN=RUN/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                    result['evaluations'][ARM]=evaluation.evaluate(ARM,record,dev,tok,base,record['binding'],heartbeat,check,started[0]+LIMIT-prior_seconds)
                    atomic_json(progress,result)
                for suite,key in (('bridge','transfer'),('retention','retention')):
                    if ARM not in result[key]:
                        result[key][ARM]=transfer_scores(c,ARM,c['early']['checkpoint'],heartbeat,check,suite);atomic_json(progress,result)
                if 'fixed_train_fit' not in result:
                    result['fixed_train_fit']=fixed_train_fit(c,old,positive,original,heartbeat,check);atomic_json(progress,result)
            finally:restore_rng(before)
            if not equal_state(before,rng_state()):raise ValueError('Evaluation RNG not restored')
            check();elapsed=prior_seconds+time.monotonic()-started[0]
            result.update(status='earliest_saved8M_and_reused_nested100M_evaluation_complete',config_sha256=sha256(CONFIG),GPU_seconds=elapsed,
                optimizer_updates=0,scientific_teacher_tokens=0,reused_scientific_trajectory_tokens=100000000,RNG_restored=True,
                Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
            atomic_json(RUN/'compare-result.json',result);job.update(status='complete',stage='complete',GPU_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--preflight',action='store_true');a=p.parse_args()
    if a.prepare:prepare()
    elif a.preflight:inspect()
    else:run()
