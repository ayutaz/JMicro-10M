"""Bounded32-token paired DEV evaluation; no old mixed reader or TEST path."""
import hashlib
import json
import math
from pathlib import Path
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.chat_evaluation import generate_reply, rollout_dialogue, summarize_chat
from jmicro.model import JMicroModel
from jmicro.training import atomic_json, isolated_evaluation, autocast, rng_state
from jmicro.phase5 import equal_state
from jmicro.experiment import now, read_json
from chat_natural_contract import RUN, BUDGET, SUITES, read_dev, require_ref, ref, stage


def windows(c, tok):
    rows = []
    for line in require_ref(c['NLL']).read_text().splitlines():
        row = json.loads(line)
        assert row['split'] in ('train','dev') and 'TEST' not in row['dataset']
        w = list(tok.sft_windows(row['messages'], 1025))[-1]
        y = np.asarray(w['labels'][1:])
        assert w['removed_turns'] == 0 and 2 <= int((y != -100).sum()) <= 32
        rows.append((row, np.asarray(w['input_ids'][:-1]), y))
    assert len(rows) == 208
    return rows


def nll_batch(model, rows):
    x = np.zeros((32,1024),dtype=np.int64)
    y = np.full_like(x,-100)
    for i, (_,ids,labels) in enumerate(rows):
        x[i,:len(ids)], y[i,:len(labels)] = ids, labels
    tx, ty = torch.from_numpy(x).cuda(), torch.from_numpy(y).cuda()
    with isolated_evaluation(model), sdpa_kernel(SDPBackend.MATH), autocast('cuda','bf16'):
        logits = model(tx,attention_mask=tx.ne(0)).logits
        losses = F.cross_entropy(logits.float().reshape(-1,4096),ty.reshape(-1),ignore_index=-100,reduction='none').reshape(32,1024)
    assert torch.isfinite(losses).all()
    return [dict(id=r['id'], dataset=r['dataset'], body_NLL=float(losses[i][ty[i]>=8].sum()),
                 EOT_NLL=float(losses[i][ty[i]==7].sum()), body_teachers=int((ty[i]>=8).sum()),
                 EOT_teachers=1, body_bytes=len(r['messages'][-1].get('text',r['messages'][-1].get('content','')).encode()))
            for i,(r,_,_) in enumerate(rows)]


def fixed_nll(model, c, tok, arm, point, checkpoint_ref, check):
    path = RUN / 'NLL' / arm / f'{point}.json'
    binding = dict(config_sha256=c['config_sha256'], checkpoint=checkpoint_ref, targets=c['NLL'])
    if path.exists():
        done = read_json(path)
        assert done['binding'] == binding and done['status'] == 'complete'
        return
    rows, losses = windows(c,tok), []
    before = rng_state()
    for start in range(0,len(rows),32):
        check()
        losses.extend(nll_batch(model,rows[start:start+32]))
    assert equal_state(before,rng_state())
    summaries = {}
    for dataset in sorted({r['dataset'] for r in losses}):
        selected = [r for r in losses if r['dataset'] == dataset]
        sums = {k:sum(r[k] for r in selected) for k in ('body_NLL','EOT_NLL','body_teachers','EOT_teachers','body_bytes')}
        summaries[dataset] = dict(sums, body_mean_NLL=sums['body_NLL']/sums['body_teachers'],
                                 EOT_mean_NLL=sums['EOT_NLL']/sums['EOT_teachers'])
    atomic_json(path,dict(status='complete',binding=binding,targets=losses,summaries=summaries,
        evaluation_RNG_isolated=True, protected_TEST_used=False, completed_at=now()))


def diagnostic(model,c,tok,arm,point,checkpoint_ref,check):
    cases,_ = read_dev(c['suites']['new'])
    selected = cases[::8]
    assert len(selected) == 10
    outputs = []
    for case in selected:
        row = generate_reply(model,tok,case['messages'],'cuda','bf16',32,True,check)
        outputs.append(dict(case=case,response=row))
    atomic_json(RUN/'diagnostics'/arm/f'{point}.json',dict(checkpoint=checkpoint_ref,config_sha256=c['config_sha256'],
        outputs=outputs, primary_selection=False, max_new_tokens=32, protected_TEST_used=False))


def final_suite(model,c,tok,arm,suite,checkpoint_ref,check,beat):
    cases,contexts = read_dev(c['suites'][suite])
    directory = RUN/'evaluation'/arm/suite
    binding = dict(config_sha256=c['config_sha256'],checkpoint=checkpoint_ref,suite=c['suites'][suite],
                   max_new_tokens=32,dtype='bf16',backend='math',decoding='greedy',seed=42,
                   history_policy='provided80 + unsuppressed80 + own_history59',protected_TEST_used=False)
    target, progress = directory/'result.json', directory/'progress.json'
    if target.exists():
        done=read_json(target); assert done['binding']==binding and done['status']=='raw_complete'
        return
    saved=read_json(progress) if progress.exists() else dict(binding=binding,provided={},rollouts={})
    assert saved['binding']==binding
    before=rng_state()
    for suppressed in (True,False):
        mode='suppressed' if suppressed else 'unsuppressed'
        for case in cases:
            uid=mode+'-'+case['id']
            if uid in saved['provided']:
                continue
            check()
            row=generate_reply(model,tok,case['messages'],'cuda','bf16',32,suppressed,check)
            row.update({k:case[k] for k in ('id','family_id','category','split','messages','checks')})
            saved['provided'][uid]=row
            atomic_json(progress,saved)
            if len(saved['provided'])%20==0:
                beat(arm=arm,suite=suite,provided=len(saved['provided']))
    for case in contexts:
        if case['id'] in saved['rollouts']:
            continue
        check()
        saved['rollouts'][case['id']]=rollout_dialogue(model,tok,case,'cuda','bf16',32,check)
        atomic_json(progress,saved)
        beat(arm=arm,suite=suite,own_families=len(saved['rollouts']))
    assert equal_state(before,rng_state())
    assert len(saved['provided'])==160 and len(saved['rollouts'])==24
    assert sum(len(r['replies']) for r in saved['rollouts'].values())==59
    primary=[saved['provided']['suppressed-'+case['id']] for case in cases]
    controls=[saved['provided']['unsuppressed-'+case['id']] for case in cases]
    own=[r for rollout in saved['rollouts'].values() for r in rollout['replies']]
    atomic_json(target,dict(status='raw_complete',binding=binding,outputs=saved['provided'],rollouts=saved['rollouts'],
        primary=summarize_chat(primary),unsuppressed=summarize_chat(controls),own_history=summarize_chat(own),
        evaluation_RNG_isolated=True, all219_content_reviews_pending=True,
        protected_TEST_used=False, Chat_adopted=False, completed_at=now()))
    print(json.dumps(dict(arm=arm,suite=suite,raw_outputs=219,primary=summarize_chat(primary)),ensure_ascii=False),flush=True)


def evaluate_all(c,tok,stopped):
    with stage('evaluation',c['config_sha256']) as (left,beat):
        def check():
            if stopped[0] or left()<20:
                raise InterruptedError('Stop at a completed output boundary')
        for arm in ('C0','C1'):
            result=read_json(RUN/arm/'result.json')
            assert result['status']=='learning_complete' and result['config_sha256']==c['config_sha256']
            value=result['checkpoint']; require_ref(value)
            state=torch.load(value['path'],map_location='cpu',weights_only=False)
            assert BUDGET<=state['supervised_tokens']<=BUDGET+31
            assert state['implementation_sha256']==c['implementation']
            assert state['spec']['teacher_chat']['data_binding']==c['arms'][arm]['sampler_binding']
            model=JMicroModel(state['model_config']).cuda()
            model.load_state_dict(state['model'],strict=True);model.eval().requires_grad_(False)
            assert sum(p.numel() for p in model.parameters())==10001152
            assert all(bool(torch.isfinite(p).all()) for p in model.parameters())
            del state
            with sdpa_kernel(SDPBackend.MATH):
                for suite in SUITES:
                    final_suite(model,c,tok,arm,suite,value,check,beat)
            del model
            __import__('gc').collect();torch.cuda.empty_cache()
    atomic_json(RUN/'evaluation_raw_complete.json',dict(status='all2190_raw_complete_pending_individual_content_review',
        config_sha256=c['config_sha256'], responses=2190, completed_at=now(), protected_TEST_used=False,
        Chat_adopted=False, whole_five_stage_goal_complete=False))
