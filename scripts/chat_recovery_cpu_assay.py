"""Owned CPU-only likelihood and plain-prefix assays; no training or corpus reader."""
import argparse
import gc
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import time
import sys
from pathlib import Path
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from chat_quality_100 import ROOT,read,save,sha,now
from answer_curriculum_chat_demo import Engine,CONFIG
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer,SUPPRESS_IDS
from jmicro.chat_evaluation import decode_reply

RUN=ROOT/'reports/phase7/chat-recovery-20261018'


def prepare():
    assert not (RUN/'cpu_assay_protocol.json').exists()
    rows=[]
    def add(kind,prefix,answer):
        rows.append(dict(id=f'{kind}-{sum(r["kind"]==kind for r in rows)+1:02}',kind=kind,prefix=prefix,answer=answer))
    for value in ('四','七','12','25','3,200','18:40','水','西'):
        add('copy',f'紙に書いた値は「{value}」です。同じ値を書き写すと「',value)
    for a,op,b in [(1,'+',3),(2,'+',4),(5,'+',2),(3,'+',6),(6,'-',2),(8,'-',3),(9,'-',1),(7,'-',4)]:
        word='足す' if op=='+' else '引く';answer=a+b if op=='+' else a-b
        add('arithmetic',f'{a}{word}{b}は',str(answer))
    for a,b,item in [('右','左','桃'),('上','下','本'),('赤','青','皿'),('東','西','鍵'),('兄','姉','地図'),('父','母','傘'),('朝','夜','読書'),('先','後','掃除')]:
        add('binding',f'{a}には{item}、{b}には別の物があります。{item}があるのは',a)
    for field,old,new in [('糸の色','青','赤'),('行き先','駅','港'),('使う紙の枚数','二枚','五枚'),('予約日','月曜','水曜'),('集合時刻','二時','四時'),('渡す相手','父','姉'),('買う果物','桃','梨'),('本の場所','棚','机')]:
        add('correction',f'{field}は{old}でした。{new}へ変更しました。今の{field}は',new)
    for value in ('R-48','note_6','06:25','4,800','dog','東→南','白い花','丸 / 星'):
        add('literal',f'文字列「{value}」をそのまま書くと「',value)
    assert len(rows)==40
    save(RUN/'plain_cases.json',dict(created_at=now(),rows=rows))
    save(RUN/'cpu_assay_protocol.json',dict(created_at=now(),source_sha256=sha(__file__),
        history_inputs_sha256=sha(RUN/'history/inputs.json'),plain_cases_sha256=sha(RUN/'plain_cases.json'),
        existing_config_sha256=sha(CONFIG),CPU_only=True,device='cpu',precision='fp32',backend='math',threads=2,
        NLL_candidate_count=640,plain_generations=120,max_new_tokens=32,NLL_limit_seconds=7200,plain_limit_seconds=3600,
        primary='Existing C0/C1 on identical frozen chat prompts; plain-format Base/C0/C1 only auxiliary',
        nll='Full vocabulary unsuppressed teacher forcing, body and EOT separately; lengths and first divergence retained',
        plain='Same BOS plus raw body prefix for every model; no chat roles; native six suppressed IDs, stop3/7',
        no_training=True,no_new_TEST=True))


def load(arm):
    if arm in ('C0','C1'):
        engine=Engine(arm);return engine.model,engine.tok,engine.info
    c=read(CONFIG);parent=Path(c['parent']['path']);assert sha(parent)==c['parent']['sha256']
    state=torch.load(parent,map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']);model.load_state_dict(state['model'],strict=True)
    model.eval().requires_grad_(False);tok=Tokenizer(c['tokenizer']['path'])
    assert sum(p.numel() for p in model.parameters())==10001152
    return model,tok,dict(checkpoint_sha256=sha(parent),parameters=10001152,format='plain_completion')


def bound():
    p=read(RUN/'cpu_assay_protocol.json')
    assert p['source_sha256']==sha(__file__) and p['existing_config_sha256']==sha(CONFIG)
    assert p['history_inputs_sha256']==sha(RUN/'history/inputs.json') and p['plain_cases_sha256']==sha(RUN/'plain_cases.json')
    assert not torch.cuda.is_available()
    torch.set_num_threads(2)
    return p


def likelihood():
    p=bound();target=RUN/'history/likelihood.json';assert not target.exists()
    started=time.monotonic();out=dict(status='running',created_at=now(),protocol_sha256=sha(RUN/'cpu_assay_protocol.json'),rows=[],models={})
    save(target,out)
    try:
        for arm in ('C0','C1'):
            model,tok,metadata=load(arm);out['models'][arm]=metadata
            with torch.inference_mode(),sdpa_kernel(SDPBackend.MATH):
                for row in read(RUN/'history/inputs.json')['rows']:
                    assert time.monotonic()-started<7200
                    prompt,removed=tok.chat_prompt(row['messages'],992);assert removed==0
                    correct=tok.encode(row['correct'])+[7];wrong=tok.encode(row['wrong'])+[7]
                    divergence=next(i for i,(a,b) in enumerate(zip(correct,wrong)) if a!=b)
                    for kind,ids,other in [('correct',correct,wrong),('wrong',wrong,correct)]:
                        assert len(ids)<=32 and len(prompt)+len(ids)<=1024
                        x=torch.tensor([prompt+ids[:-1]])
                        logits=model(x).logits[0,len(prompt)-1:].float()
                        logp=logits.log_softmax(-1);labels=torch.tensor(ids)
                        values=logp.gather(1,labels[:,None]).squeeze(1)
                        assert bool(torch.isfinite(values).all())
                        score=logits[divergence];rank=int((score>score[ids[divergence]]).sum())+1
                        out['rows'].append(dict(arm=arm,input_id=row['id'],candidate=kind,text=row[kind],prompt_ids=prompt,
                            target_ids=ids,body_tokens=len(ids)-1,token_logprobs=values.tolist(),body_NLL=float(-values[:-1].mean()),
                            EOT_NLL=float(-values[-1]),sequence_logprob=float(values.sum()),first_divergence=divergence,
                            divergence_target_id=ids[divergence],divergence_other_id=other[divergence],
                            divergence_logprob=float(values[divergence]),divergence_rank=rank))
                    save(target,out)
            del model;gc.collect()
        assert len(out['rows'])==640
        out.update(status='complete',CPU_wall_seconds=time.monotonic()-started)
    except BaseException as error:
        out.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(target,out)


def plain():
    p=bound();target=RUN/'plain_raw.json';assert not target.exists()
    started=time.monotonic();out=dict(status='running',created_at=now(),protocol_sha256=sha(RUN/'cpu_assay_protocol.json'),rows=[],models={})
    save(target,out)
    try:
        for arm in ('Base','C0','C1'):
            model,tok,metadata=load(arm);out['models'][arm]=metadata
            with torch.inference_mode(),sdpa_kernel(SDPBackend.MATH):
                for row in read(RUN/'plain_cases.json')['rows']:
                    assert time.monotonic()-started<3600
                    prompt=[2]+tok.encode(row['prefix']);ids=[];cache=None;current=torch.tensor([prompt])
                    for _ in range(32):
                        result=model(current,cache=cache,use_cache=True);cache=result.cache
                        scores=result.logits[0,-1].float().clone();assert bool(torch.isfinite(scores).all())
                        scores[list(SUPPRESS_IDS)]=-torch.inf;token=int(scores.argmax());ids.append(token)
                        if token in (3,7):break
                        current=torch.tensor([[token]])
                    out['rows'].append(dict(arm=arm,case=row,generated_ids=ids,prompt_ids=prompt,
                        stop='eot' if ids[-1]==7 else 'eos' if ids[-1]==3 else 'max_new_tokens',**decode_reply(tok,ids)))
                    save(target,out)
            del model;gc.collect()
        assert len(out['rows'])==120
        out.update(status='complete_pending_literal_review',CPU_wall_seconds=time.monotonic()-started)
    except BaseException as error:
        out.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(target,out)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','likelihood','plain']);args=parser.parse_args()
    if args.mode=='prepare':prepare()
    elif args.mode=='likelihood':likelihood()
    else:plain()
