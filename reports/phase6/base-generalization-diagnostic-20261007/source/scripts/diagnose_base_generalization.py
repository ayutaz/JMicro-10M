"""Bounded readonly four-endpoint TRAIN56 versus source-local DEV64 diagnostic."""
import argparse
import gc
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state,restore_rng,autocast
from phase6_performance import identity,alive
from run_eos_short_pilot import equal_state
from base_generalization_diagnostic import select_dev,collate_positive,score_logits,summarize
from diagnose_base_preference import reference,check_reference,rollout,repeat_marker

RUN=ROOT/'reports/phase6/base-generalization-diagnostic-20261007'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/base-generalization-diagnostic-20261007')
CONFIG=ROOT/'configs/phase6/base_generalization_diagnostic.json'
PLAN=ROOT/'reports/phase6/base_preference_generalization_diagnostic_plan.json'
SOURCES=('scripts/diagnose_base_generalization.py','scripts/diagnose_base_generalization.ps1','scripts/base_generalization_diagnostic.py',
    'scripts/review_base_generalization.py','scripts/record_base_generalization_content.py','tests/test_base_generalization.py')
OLD_SOURCES=('scripts/prepare_livedoor_leads.py','scripts/base_preference_loss.py','scripts/diagnose_base_preference.py',
    'scripts/phase6_performance.py','scripts/run_eos_short_pilot.py')
ARMS=('original_d18','actual_shared_Web6M','chosen_CE_terminal','chosen_CE_DPO_terminal')
SEED=20261007


def prepare():
    if CONFIG.exists():inspect();return
    start=time.monotonic();plan=read_json(PLAN)
    if plan['kind']!='read_only_Base_train_memorization_vs_within_source_dev_transfer' or plan['budgets']!=dict(CPU_preparation_seconds=30,GPU_seconds=120,optimizer_updates=0,new_scientific_teacher_tokens=0):
        raise ValueError('Fixed bounded readonly diagnostic plan required')
    old_config=ROOT/'configs/phase6/base_preference_comparison.json';old=read_json(old_config)
    old_result=ROOT/'reports/phase6/base-preference-comparison-20261006/compare-result.json';r=read_json(old_result)
    old_review=ROOT/'reports/phase6/base_preference_comparison_review.json';review=read_json(old_review)
    if review['result_sha256']!=sha256(old_result) or any(review['eligible_for_final_Base_validation'].values()):raise ValueError('Actual failed fixed recipe review required')
    job=read_json(old_result.parent/'job.json')
    if job['status']!='complete' or alive(job):raise ValueError('Previous actual GPU must be complete and absent')
    parents=dict(original_d18=old['parent'],actual_shared_Web6M=r['shared_parent'])
    for arm,key in (('chosen_CE_terminal','chosen_CE'),('chosen_CE_DPO_terminal','chosen_CE_DPO')):
        v=r['checkpoints'][key];parents[arm]=dict(path=v['checkpoint'],sha256=v['checkpoint_sha256'])
    train_pairs=read_json(Path(old['pairs']['path']));mapping={v['id']:v for v in train_pairs};train=[mapping[key] for key in old['preferred_pair_ids']]
    source_ready=ROOT/'reports/phase6/livedoor-leads-20261006/ready.json';ready=read_json(source_ready)
    source_config=read_json(ROOT/'configs/phase6/livedoor_leads_preparation.json');tok_ref=reference(ROOT/source_config['tokenizer']);tok=Tokenizer(Path(tok_ref['path']))
    if tok_ref['sha256']!=source_config['tokenizer_sha256'] or len(train)!=56:raise ValueError('Actual original Tokenizer/TRAIN56 required')
    def check():
        if time.monotonic()-start>30:raise TimeoutError('Bounded DEV preparation CPU30s exhausted')
    check_reference(ready['archive']);dev,counts=select_dev(Path(ready['archive']['path']),tok,64,SEED,check)
    ids=read_json(Path(ready['heldout_article_ids']['path']));dev_ids={v['article_id'] for v in ids if v['split']=='dev'}
    if any(v['id'].removeprefix('livedoor-') not in dev_ids for v in dev):raise ValueError('Original cached DEV families required')
    train_ids={v['id'] for v in train};train_sha={v['source_text_sha256'] for v in train}
    index=read_json(Path(ready['pool'])/'train.index.json');all_train_sha={v['canonical_sha256'] for v in index}
    for v in train:
        v['chosen_body_tokens']=len(v['chosen_ids'])-1;v['chosen_body_bytes']=len(tok.decode_bytes(v['chosen_ids'][:-1]))
        if (v['split']!='train' or v['chosen_ids'][-1]!=3 or v['prompt_ids'][1:]+v['chosen_ids'][:-1]!=v['original_body_ids']
                or hashlib.sha256(tok.decode_bytes(v['original_body_ids'])).hexdigest()!=v['source_text_sha256']):raise ValueError('Original selected TRAIN continuation differs')
    if train_ids & {v['id'] for v in dev}:raise ValueError('Local TRAIN and DEV family overlap')
    DATA.mkdir(parents=True,exist_ok=True);packet=DATA/'cases.json';atomic_json(packet,dict(train=train,dev=dev))
    tests=ROOT/'reports/phase6/base_generalization_tests.xml';suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):raise ValueError('Actual selector/mask/byte-denominator CPU checks required')
    c=dict(kind=plan['kind'],phase='readonly',parents=parents,arms=list(ARMS),cases=reference(packet),tokenizer=tok_ref,seed=SEED,
        references=dict(plan=reference(PLAN),previous_config=reference(old_config),previous_result=reference(old_result),previous_review=reference(old_review),
            source_ready=reference(source_ready),archive=ready['archive'],heldout_ids=ready['heldout_article_ids'],TRAIN_pairs=old['pairs'],CPU_tests=reference(tests)),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},old_source_sha256={s:sha256(ROOT/s) for s in OLD_SOURCES},implementation=implementation_hashes(),
        counts=counts,TRAIN_count=56,DEV_count=64,greedy_DEV_count_per_arm=16,likelihood_batch=8,greedy_max_new_tokens=64,
        spans={k:max(len(v['prompt_ids'])+len(v['chosen_ids'])-1 for v in rows) for k,rows in (('train',train),('dev',dev))},
        DEV_positive_positions=sum(len(v['chosen_ids']) for v in dev),TRAIN_positive_positions=sum(len(v['chosen_ids']) for v in train),
        local_family_overlap=0,DEV_exact_text_overlap_with_selected56=sum(v['source_text_sha256'] in train_sha for v in dev),
        DEV_exact_text_overlap_with_news5050=sum(v['source_text_sha256'] in all_train_sha for v in dev),
        precision='bf16',backend='math',GPU_budget_seconds=120,CPU_preparation_seconds=time.monotonic()-start,
        optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        limitations='Source-local DEV article families separate from curated56; old Web global overlap uncertified. Existing paragraph rules condition the source population.16 nonblind greedy samples per arm, reused broad Base80 and earlier seven numerical failures retained. Diagnostic, not independent final Base qualification.')
    for ref in (*parents.values(),tok_ref,*c['references'].values()):check_reference(ref)
    check();atomic_json(CONFIG,c);inspect();print(dict(status='source_local_generalization_frozen',CPU_seconds=c['CPU_preparation_seconds'],DEV_counts=counts,GPU_seconds=0))


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!='read_only_Base_train_memorization_vs_within_source_dev_transfer' or c['phase']!='readonly' or c['arms']!=list(ARMS)
            or c['TRAIN_count']!=56 or c['DEV_count']!=64 or c['greedy_DEV_count_per_arm']!=16 or c['seed']!=SEED
            or c['likelihood_batch']!=8 or c['greedy_max_new_tokens']!=64 or c['precision']!='bf16' or c['backend']!='math'
            or c['GPU_budget_seconds']!=120 or c['implementation']!=implementation_hashes() or c['local_family_overlap']
            or c['optimizer_updates'] or c['scientific_teacher_tokens'] or any(c[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Frozen readonly source-local scope differs')
    for name,digest in {**c['source_sha256'],**c['old_source_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source differs: '+name)
    for ref in (*c['parents'].values(),c['tokenizer'],c['cases'],*c['references'].values()):check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual live diagnostic; no duplicate')
    return c


def run():
    c=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json'
    if jp.exists():raise ValueError('Preserve one-shot diagnostic; documented repair required')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0,
        restart_command='scripts/diagnose_base_generalization.ps1 -Worker; terminal one-shot requires documented repair')
    atomic_json(jp,job);started=None;stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Source-local diagnosis interrupted')
        if started is not None and time.monotonic()-started>120:raise TimeoutError('Readonly GPU120s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for name in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        cases=read_json(Path(c['cases']['path']));tok=Tokenizer(Path(c['tokenizer']['path']));results={}
        with gpu_lock('cuda'),sdpa_kernel(SDPBackend.MATH):
            started=time.monotonic();job['status']='running';heartbeat('GPU')
            for arm in ARMS:
                state=torch.load(c['parents'][arm]['path'],map_location='cpu',weights_only=False);before_rng=rng_state()
                model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                if (sum(p.numel() for p in model.parameters())!=10001152 or len(list(model.named_parameters()))!=119
                        or model.lm_head.weight is not model.model.embed_tokens.weight):raise ValueError('Original native tied10M required')
                scores={};generation=[]
                for split,rows in cases.items():
                    scored=[]
                    for start in range(0,len(rows),8):
                        heartbeat(arm+'-'+split+'-likelihood',completed_cases=start,total_cases=len(rows));batch=rows[start:start+8]
                        x,y,mask=collate_positive(batch,c['spans'][split]);x,y,mask=(v.to('cuda') for v in (x,y,mask))
                        with torch.inference_mode(),autocast('cuda','bf16'):logits=model(x,attention_mask=mask).logits
                        scored.extend(score_logits(logits,y,batch));del x,y,mask,logits
                        atomic_json(RUN/arm/(split+'-partial.json'),dict(config_sha256=sha256(CONFIG),checkpoint=c['parents'][arm],rows=scored))
                    scores[split]=dict(rows=scored,summary=summarize(scored))
                for index,row in enumerate(cases['dev'][:16]):
                    heartbeat(arm+'-DEV16-greedy',completed_cases=index,total_cases=16);generated,reason=rollout(model,row['prompt_ids'],check)
                    raw=tok.decode_bytes([v for v in generated if v!=3])
                    try:text=raw.decode('utf-8');valid=True
                    except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
                    generation.append(dict(id=row['id'],prefix=row['prefix'],split='dev',category=row['category'],generated_ids=generated,text=text,
                        raw_bytes_hex=raw.hex(),valid_UTF8=valid,stop_reason=reason,**repeat_marker(generated)))
                    atomic_json(RUN/arm/'generation.json',dict(config_sha256=sha256(CONFIG),checkpoint=c['parents'][arm],outputs=generation))
                checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),state['model'][k]) for k,v in model.state_dict().items()),
                    no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training,
                    parent_file_unchanged=sha256(Path(c['parents'][arm]['path']))==c['parents'][arm]['sha256'])
                restore_rng(before_rng);checks['RNG_restored']=equal_state(before_rng,rng_state())
                if not all(checks.values()):raise ValueError('Readonly scoring altered native weights/RNG')
                result=dict(config_sha256=sha256(CONFIG),checkpoint=c['parents'][arm],scores=scores,readonly_checks=checks,
                    generation=reference(RUN/arm/'generation.json'),optimizer_updates=0,scientific_teacher_tokens=0)
                atomic_json(RUN/arm/'result.json',result);results[arm]=result
                del model,state;gc.collect();torch.cuda.empty_cache()
            check();elapsed=time.monotonic()-started
            result=dict(status='source_local_generalization_GPU_complete_pending_all64_content',config_sha256=sha256(CONFIG),arms=results,
                GPU_seconds=elapsed,optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
                Chat_started=False,quantization_started=False,protected_test_used=False,old_numerical7_failures_preserved=True)
            atomic_json(RUN/'result.json',result);job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as exc:job.update(status='failed_or_interrupted',error=repr(exc));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true');args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Readonly source-local diagnostic valid; learning0')
    else:run()
