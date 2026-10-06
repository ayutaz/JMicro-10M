"""Fixed TRAIN64 on-policy continuation pairs/gradients, zero optimizer updates."""
import argparse
import gc
import hashlib
import json
import math
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
from base_preference_loss import collate_continuations,continuation_logps,dpo_loss

RUN=ROOT/'reports/phase6/base-preference-diagnostic-20261006'
CONFIG=ROOT/'configs/phase6/base_preference_diagnostic.json'
PROPOSAL=ROOT/'reports/phase6/livedoor_base_comparison_proposal.json'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/base-preference-diagnostic-20261006')
SOURCES=('scripts/diagnose_base_preference.py','scripts/diagnose_base_preference.ps1','scripts/base_preference_loss.py','tests/test_base_preference_loss.py')
BLOCKED=(0,1,2,4,5,6,7)


def reference(q):return dict(path=str(q),sha256=sha256(q))


def check_reference(ref):
    if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Frozen diagnostic reference differs: '+ref['path'])


def prepare():
    if CONFIG.exists():inspect();return
    start=time.monotonic();p=read_json(PROPOSAL);ready=read_json(Path(p['source_ready']['path']));review=read_json(Path(p['source_content_review']['path']))
    if not review['passed'] or review['weak_documents']>10:raise ValueError('Accepted original TRAIN news sample required')
    sample=Path(ready['sample']['path']);check_reference(ready['sample']);source=read_json(sample)
    tests=ROOT/'reports/phase6/base_preference_loss_tests.xml';suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=2 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):raise ValueError('Actual prompt/shift/reference/gradient tests required')
    old=read_json(Path(p['cached_control_config']['path']));base=read_json(Path(old['original_config']['path']));tok=Tokenizer(ROOT/base['tokenizer']);cases=[]
    if len(source)!=64 or len({r['doc_id'] for r in source})!=64:raise ValueError('Original fixed TRAIN64 required')
    for row in source:
        ids=tok.encode(row['text']);raw=row['text'].encode('utf-8')
        if row['split']!='train' or len(ids)!=row['body_tokens'] or tok.decode_bytes(ids)!=raw or hashlib.sha256(raw).hexdigest()!=row['canonical_sha256']:
            raise ValueError('Original TRAIN body/provenance differs')
        cut=max(8,len(ids)//4)
        while True:
            try:prefix=tok.decode_bytes(ids[:cut]).decode('utf-8');break
            except UnicodeDecodeError:cut+=1
        if cut>=len(ids):raise ValueError('Nonempty exact original suffix required')
        cases.append(dict(id=row['doc_id'],source_family=row['source_family'],split='train',category=row['category'],
            source_text_sha256=row['canonical_sha256'],source_URL=row['source_URL'],original_article_sha256=row['original_article_sha256'],
            prompt_ids=[2,*ids[:cut]],chosen_ids=[*ids[cut:],3],prefix=prefix,original_body_ids=ids))
    DATA.mkdir(parents=True,exist_ok=True);packet=DATA/'cases.json';atomic_json(packet,cases)
    c=dict(kind='role_free_Base_fixed_reference_pair_gradient_diagnostic_v1',parent=p['original_parent'],cases=reference(packet),
        references=dict(proposal=reference(PROPOSAL),source_ready=p['source_ready'],source_review=p['source_content_review'],sample=ready['sample'],CPU_tests=reference(tests)),
        tokenizer=reference(ROOT/base['tokenizer']),source_sha256={s:sha256(ROOT/s) for s in SOURCES},implementation=implementation_hashes(),
        case_count=64,prefix_rule='Original body first quarter, minimum8 tokens; advance only to valid UTF8 token boundary; original remaining whole paragraph plus EOS.',
        rejected_rule='Original d18 native parent on-policy greedy64, EOS3 and original blocked IDs; never hand-edit or reroll.',
        beta=.1,gradient_batch=8,model_parameters=10001152,precision='bf16',backend='math',GPU_budget_seconds=180,CPU_preparation_seconds=time.monotonic()-start,
        scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        papers=['https://arxiv.org/abs/2305.18290','https://huggingface.co/docs/trl/dpo_trainer'],
        completion='All64 original train pairs and raw generation/reference scores; fixed-reference DPO versus chosen-CE gradient geometry and read-only proof. Individually review generated pairs before any learning. No source/beta/LR/decoder/parent reroll.',
        limitations='Source accepted at64-sample level includes8 weak originals; chosen suffix is not automatically a better continuation. Unequal sequence lengths and source genre matter. TRAIN-only/one model/nonblind/one beta; no general quality or KL-preservation guarantee. Old numerical7 failures preserved.')
    if c['CPU_preparation_seconds']>30:raise TimeoutError('CPU30s exhausted')
    atomic_json(CONFIG,c);inspect();print(dict(status='Base_pair_diagnostic_frozen',CPU_seconds=c['CPU_preparation_seconds'],GPU_seconds=0))


def inspect():
    c=read_json(CONFIG)
    if (c['case_count']!=64 or c['beta']!=.1 or c['gradient_batch']!=8 or c['GPU_budget_seconds']!=180
            or c['implementation']!=implementation_hashes() or c['optimizer_updates'] or c['scientific_teacher_tokens']
            or any(c[k] for k in ('Base_complete','Chat_started','quantization_started','protected_test_used'))):raise ValueError('Fixed diagnostic scope differs')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen diagnostic source differs: '+name)
    for ref in (c['parent'],c['cases'],c['tokenizer'],*c['references'].values()):check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual live diagnostic; no duplicate')
    return c


def rollout(model,prompt,check):
    ids=[];cache=None;current=torch.tensor([prompt],device='cuda');reason='max_new_tokens'
    with torch.inference_mode():
        for _ in range(64):
            check()
            with autocast('cuda','bf16'):out=model(current,cache=cache,use_cache=True)
            cache=out.cache;scores=out.logits[0,-1].clone();scores[list(BLOCKED)]=-torch.inf
            token=int(scores.argmax());ids.append(token)
            if token==3:reason='stop_id';break
            current=torch.tensor([[token]],device='cuda')
    return ids,reason


def repeat_marker(ids):
    grams=[tuple(ids[i:i+4]) for i in range(len(ids)-3)]
    return dict(repeated4gram_positions=len(grams)-len(set(grams)),total4gram_positions=len(grams))


def gradient_vector(model):
    parts=[]
    for parameter in model.parameters():
        if parameter.grad is None or not bool(torch.isfinite(parameter.grad).all()):raise ValueError('Every unique native parameter needs finite gradient')
        parts.append(parameter.grad.detach().reshape(-1).cpu().clone())
    return torch.cat(parts)


def run():
    c=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json'
    if jp.exists():raise ValueError('Preserve one-shot diagnostic; documented failure required for repair')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0,
        restart_command='scripts/diagnose_base_preference.ps1 -Worker; terminal one-shot requires documented repair')
    atomic_json(jp,job);started=None;stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Preference diagnostic interrupted')
        if started is not None and time.monotonic()-started>180:raise TimeoutError('Readonly diagnostic180s exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for name in (*c['source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        cases=read_json(Path(c['cases']['path']));tok=Tokenizer(Path(c['tokenizer']['path']));state=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        with gpu_lock('cuda'),sdpa_kernel(SDPBackend.MATH):
            started=time.monotonic();job['status']='running';before_rng=rng_state()
            model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
            if sum(p.numel() for p in model.parameters())!=10001152:raise ValueError('Native tied10M required')
            rows=[]
            for index,row in enumerate(cases):
                generated,reason=rollout(model,row['prompt_ids'],check);raw=tok.decode_bytes([v for v in generated if v!=3])
                try:text=raw.decode('utf-8');valid=True
                except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
                result=dict(row,rejected_ids=generated,stop_reason=reason,rejected_text=text,rejected_bytes_hex=raw.hex(),valid_UTF8=valid,**repeat_marker(generated))
                rows.append(result);atomic_json(DATA/'partial-pairs.json',rows)
                if (index+1)%8==0:heartbeat('original_parent_TRAIN64_greedy',completed_cases=index+1)
            pairs_path=DATA/'pairs.json';atomic_json(pairs_path,rows);reference_scores=[];dpo_total=0.;ce_nll=0.;positive_tokens=0
            ce_gradient=torch.zeros(10001152);dpo_gradient=torch.zeros(10001152)
            for start in range(0,64,8):
                batch=rows[start:start+8];x,y,mask=collate_continuations(batch,'cuda');n=len(batch);heartbeat('fixed_reference_pair_gradients',completed_pairs=start)
                with torch.no_grad(),autocast('cuda','bf16'):
                    ref,count=continuation_logps(model(x,attention_mask=mask).logits,y)
                model.zero_grad(set_to_none=True)
                with autocast('cuda','bf16'):policy,_=continuation_logps(model(x,attention_mask=mask).logits,y)
                if not torch.equal(ref,policy.detach()):raise ValueError('Unchanged policy/reference must yield same sequence sums')
                loss,margin=dpo_loss(policy[:n],policy[n:],ref[:n],ref[n:],c['beta'])
                if not bool(margin.eq(0).all()) or not math.isclose(float(loss.detach()),math.log(2),rel_tol=1e-6):raise ValueError('Initial ratio-centered loss differs')
                loss.backward();dpo_gradient+=gradient_vector(model)*(n/64);dpo_total+=float(loss.detach())*n/64
                model.zero_grad(set_to_none=True)
                with autocast('cuda','bf16'):chosen,_=continuation_logps(model(x[:n],attention_mask=mask[:n]).logits,y[:n])
                loss_ce=-chosen.sum()/count[:n].sum();loss_ce.backward()
                token_count=int(count[:n].sum());ce_gradient+=gradient_vector(model)*token_count;positive_tokens+=token_count;ce_nll+=float(-chosen.detach().sum())
                reference_scores.extend(dict(id=row['id'],chosen_logp=float(ref[i]),rejected_logp=float(ref[n+i]),chosen_tokens=int(count[i]),rejected_tokens=int(count[n+i])) for i,row in enumerate(batch))
                model.zero_grad(set_to_none=True);del x,y,mask,ref,policy,chosen,loss,loss_ce;gc.collect();torch.cuda.empty_cache()
            ce_gradient/=positive_tokens;a=ce_gradient.double();b=dpo_gradient.double();aa=float(a.dot(a));bb=float(b.dot(b));ab=float(a.dot(b))
            if min(aa,bb)<=0 or not all(math.isfinite(v) for v in (aa,bb,ab)):raise ValueError('Finite nonzero actual CE/DPO gradients required')
            checks=dict(weights_unchanged=all(torch.equal(v.detach().cpu(),state['model'][k]) for k,v in model.state_dict().items()),
                no_final_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training,parent_file_unchanged=sha256(Path(c['parent']['path']))==c['parent']['sha256'])
            restore_rng(before_rng);checks['RNG_restored']=equal_state(before_rng,rng_state())
            if not all(checks.values()):raise ValueError('Readonly gradient diagnostic changed model/RNG')
            elapsed=time.monotonic()-started
            result=dict(status='actual_TRAIN64_preference_pair_and_gradient_diagnostic_complete_pending_content',created_at=now(),config_sha256=sha256(CONFIG),
                parent=c['parent'],pairs=reference(pairs_path),case_count=64,reference_scores=reference_scores,
                completion_EOS=sum(r['stop_reason']=='stop_id' for r in rows),repeated4gram_marker=sum(r['repeated4gram_positions']>0 for r in rows),
                candidate_heavy_repeat_at_least8_positions=sum(r['repeated4gram_positions']>=8 for r in rows),valid_UTF8=sum(r['valid_UTF8'] for r in rows),
                mean_DPO_loss=dpo_total,chosen_CE_nats=ce_nll/positive_tokens,chosen_scored_teacher_positions=positive_tokens,
                geometry=dict(CE_norm=math.sqrt(aa),DPO_norm=math.sqrt(bb),DPO_to_CE_norm=math.sqrt(bb/aa),cosine=ab/math.sqrt(aa*bb),
                    initial_DPO_margin_descent_direction=-bb,chosen_CE_directional_derivative_along_negative_DPO_gradient=-ab),
                readonly_checks=checks,GPU_seconds=elapsed,optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,
                Chat_started=False,quantization_started=False,protected_test_used=False,old_numerical7_failures_preserved=True,limitations=c['limitations'])
            atomic_json(RUN/'result.json',result);job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as exc:job.update(status='failed_or_interrupted',error=repr(exc));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group();m.add_argument('--prepare',action='store_true');m.add_argument('--inspect',action='store_true');args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Readonly Base preference diagnostic valid; learning0')
    else:run()
