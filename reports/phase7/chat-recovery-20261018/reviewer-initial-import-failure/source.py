"""Validate every diagnostic raw row and bind literal reviews before analysis."""
from collections import defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from chat_quality_100 import ROOT,read,save,sha,now
from jmicro.tokenizer import Tokenizer

RUN=ROOT/'reports/phase7/chat-recovery-20261018'


def bind(row):
    return hashlib.sha256(json.dumps(row,ensure_ascii=False,sort_keys=True).encode()).hexdigest()


def validate_reply(tok,messages,response):
    ids,removed=tok.chat_prompt(messages,992)
    assert removed==response['removed_turns']==0 and ids==response['prompt_ids']
    assert len(ids)==response['prompt_tokens'] and response['full_history_retained']
    generated=response['generated_ids'];assert len(generated)==response['generated_tokens']<=32
    assert response['max_new_tokens']==32 and all(i not in (0,1,2,4,5,6) for i in generated)
    raw=tok.decode_bytes(generated);assert raw.hex()==response['raw_bytes_hex']
    assert raw.decode('utf-8',errors='replace')==response['text']
    try:raw.decode('utf-8');valid=True
    except UnicodeDecodeError:valid=False
    assert valid==response['valid_utf8']
    expected='eot' if generated[-1]==7 else 'eos' if generated[-1]==3 else 'max_new_tokens'
    assert expected==response['stop_reason'] and (expected!='max_new_tokens' or len(generated)==32)


def judgments(path,count):
    out={}
    for line in path.read_text(encoding='utf-8').splitlines():
        i,g,r,c,f,reason=line.split('\t');i=int(i)
        assert i not in out and g in '012' and r in '012' and c in '012' and f in '01' and len(reason)>=12
        v=dict(grammar=int(g),relevance=int(r),context=int(c),factual_correct=f=='1',rationale=reason)
        v['task_pass']=g==r==c=='2'
        assert not v['task_pass'] or v['factual_correct']
        out[i]=v
    assert set(out)==set(range(count))
    return out


def ci(vector):
    x=np.asarray(vector,dtype=float);rng=np.random.default_rng(42)
    samples=x[rng.integers(0,len(x),size=(2000,len(x)))].mean(1)
    return dict(n=len(x),mean=float(x.mean()),CI95=np.percentile(samples,[2.5,97.5]).tolist(),bootstrap_unit='family' if len(x)==20 else 'case')


def main():
    target=RUN/'diagnostic_analysis.json';assert not target.exists()
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    directory=RUN/'history';protocol=read(directory/'protocol.json');families=read(directory/'families.json')['families']
    assert protocol['source_sha256']==sha(ROOT/'scripts/chat_history_factor_diagnostic.py')
    assert protocol['families_sha256']==sha(directory/'families.json')
    prefix=read(directory/'prefix.json');assert prefix['status']=='complete' and len(prefix['rows'])==100
    prefix_notes={}
    for line in (directory/'prefix_authored.tsv').read_text(encoding='utf-8').splitlines():
        i,reason=line.split('\t');i=int(i);assert i not in prefix_notes and len(reason)>=12;prefix_notes[i]=reason
    assert set(prefix_notes)==set(range(100))
    for k,f in enumerate(families):
        history=[]
        for turn,user in enumerate(f['users'],1):
            row=prefix['rows'][k*5+turn-1];history.append(dict(role='user',content=user))
            assert row['id']==f['id'] and row['turn']==turn and row['request']['messages']==history
            validate_reply(tok,history,row['answer']['response'])
            history.append(dict(role='assistant',content=row['answer']['response']['text']))
            if turn in (2,5):assert prefix['histories'][f['id']][str(turn)]==history
    inputs=read(directory/'inputs.json');assert inputs['prefix_sha256']==sha(directory/'prefix.json')
    assert len(inputs['rows'])==160
    raw=read(directory/'raw.json');assert raw['status']=='complete_pending_all_literal_review' and len(raw['rows'])==320
    assert raw['inputs_sha256']==sha(directory/'inputs.json')
    manual=judgments(directory/'final_authored.tsv',320);notes=[]
    for i,row in enumerate(raw['rows']):
        arm='C0' if i<160 else 'C1';inp=inputs['rows'][i%160]
        assert row['arm']==arm and row['input_id']==inp['id'] and row['request']['messages']==inp['messages'] and row['expected']==inp['expected']
        validate_reply(tok,inp['messages'],row['answer']['response'])
        notes.append(dict(index=i,arm=arm,input_id=inp['id'],family=inp['family'],query_turn=inp['query_turn'],field_count=inp['field_count'],
            history_quality=inp['history_quality'],raw_row_sha256=bind(row),**manual[i]))
    save(directory/'notes.json',dict(created_at=now(),raw_sha256=sha(directory/'raw.json'),authored_sha256=sha(directory/'final_authored.tsv'),
        prefix_authored_sha256=sha(directory/'prefix_authored.tsv'),prefix_reasons=[dict(index=i,raw_row_sha256=bind(prefix['rows'][i]),rationale=prefix_notes[i]) for i in range(100)],
        judgments=notes,reviewer='Codex nonblind, not independent human',all_raw_prompt_IDs_bytes_histories_verified=True))
    cells=[]
    for arm in ('C0','C1'):
        for turn in (3,6):
            for fields in ('one','two'):
                for quality in ('gold','actual'):
                    selected=[n for n in notes if (n['arm'],n['query_turn'],n['field_count'],n['history_quality'])==(arm,turn,fields,quality)]
                    assert len(selected)==20
                    cells.append(dict(arm=arm,query_turn=turn,fields=fields,history=quality,n=20,task_pass=sum(n['task_pass'] for n in selected),
                        factual_correct=sum(n['factual_correct'] for n in selected)))
    effects={}
    for arm in ('C0','C1'):
        effects[arm]={}
        for factor,left,right in [('history_quality','gold','actual'),('query_turn',3,6),('field_count','one','two')]:
            vectors=[]
            for f in families:
                selected=[n for n in notes if n['arm']==arm and n['family']==f['id']]
                a=[n['task_pass'] for n in selected if n[factor]==left];b=[n['task_pass'] for n in selected if n[factor]==right]
                assert len(a)==len(b)==4;vectors.append(sum(a)/4-sum(b)/4)
            effects[arm][f'{factor}:{left}-{right}']=ci(vectors)
    nll=read(directory/'likelihood.json');assert nll['status']=='complete' and len(nll['rows'])==640
    nll_by_key={}
    for i,row in enumerate(nll['rows']):
        arm='C0' if i<320 else 'C1';inp=inputs['rows'][(i%320)//2];kind='correct' if i%2==0 else 'wrong'
        assert (row['arm'],row['input_id'],row['candidate'])==(arm,inp['id'],kind)
        prompt,removed=tok.chat_prompt(inp['messages'],992);assert removed==0 and prompt==row['prompt_ids']
        ids=tok.encode(inp[kind])+[7];assert row['target_ids']==ids and row['text']==inp[kind]
        lp=row['token_logprobs'];assert len(lp)==len(ids) and all(math.isfinite(x) and x<=0 for x in lp)
        assert abs(sum(lp)-row['sequence_logprob'])<1e-4 and abs(-sum(lp[:-1])/len(lp[:-1])-row['body_NLL'])<1e-5
        assert abs(-lp[-1]-row['EOT_NLL'])<1e-6
        nll_by_key[arm,inp['id'],kind]=row
    nll_summary=[]
    for arm in ('C0','C1'):
        for quality in ('gold','actual'):
            subset=[i for i in inputs['rows'] if i['history_quality']==quality]
            correct=[nll_by_key[arm,i['id'],'correct'] for i in subset]
            wrong=[nll_by_key[arm,i['id'],'wrong'] for i in subset]
            nll_summary.append(dict(arm=arm,history=quality,n=80,correct_body_NLL=float(np.mean([r['body_NLL'] for r in correct])),
                divergence_correct_rank1=sum(r['divergence_rank']==1 for r in correct),
                divergence_correct_rank_top10=sum(r['divergence_rank']<=10 for r in correct),
                divergence_correct_over_wrong=sum(a['divergence_logprob']>b['divergence_logprob'] for a,b in zip(correct,wrong))))
    old=ROOT/'reports/phase7/chat-quality-100-20261017'
    a=[n for n in read(RUN/'control100/notes.json')['all200_literal_judgments'] if n['final']]
    b=[n for n in read(old/'notes.json')['all200_literal_judgments'] if n['final']]
    assert [n['id'] for n in a]==[n['id'] for n in b]
    comparison=ci([int(y['task_pass'])-int(x['task_pass']) for x,y in zip(a,b)])
    plain=read(RUN/'plain_raw.json');assert plain['status']=='complete_pending_literal_review' and len(plain['rows'])==120
    cases=read(RUN/'plain_cases.json')['rows'];plain_notes={}
    for line in (RUN/'plain_authored.tsv').read_text(encoding='utf-8').splitlines():
        i,v,reason=line.split('\t');i=int(i);assert i not in plain_notes and v in '01' and len(reason)>=12
        plain_notes[i]=dict(value_correct=v=='1',rationale=reason)
    assert set(plain_notes)==set(range(120))
    plain_summary=[]
    for i,row in enumerate(plain['rows']):
        assert row['case']==cases[i%40] and row['arm']==('Base','C0','C1')[i//40]
        assert row['prompt_ids']==[2]+tok.encode(row['case']['prefix'])
        assert tok.decode_bytes(row['generated_ids']).hex()==row['raw_bytes_hex']
        assert tok.decode_bytes(row['generated_ids']).decode('utf-8',errors='replace')==row['text']
        plain_notes[i].update(index=i,raw_row_sha256=bind(row),arm=row['arm'],kind=row['case']['kind'])
    for arm in ('Base','C0','C1'):
        for kind in ('copy','arithmetic','binding','correction','literal'):
            subset=[r for r in plain_notes.values() if (r['arm'],r['kind'])==(arm,kind)]
            plain_summary.append(dict(arm=arm,kind=kind,n=8,value_correct=sum(r['value_correct'] for r in subset)))
    save(RUN/'plain_notes.json',dict(created_at=now(),raw_sha256=sha(RUN/'plain_raw.json'),authored_sha256=sha(RUN/'plain_authored.tsv'),judgments=list(plain_notes.values()),
        definition='Copy/literal: first completed quoted span only; other tasks: meaningful correct requested value across continuation, not keyword presence; full prose quality not counted',
        full_natural_chat_success_not_measured=True,reviewer='Codex nonblind, not independent human'))
    with (directory/'responses.csv').open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['index','arm','input_id','expected','response','grammar','relevance','context','factual_correct','task_pass','rationale','messages'])
        for row,n in zip(raw['rows'],notes):writer.writerow([n['index'],n['arm'],n['input_id'],row['expected'],row['answer']['response']['text'],n['grammar'],n['relevance'],n['context'],n['factual_correct'],n['task_pass'],n['rationale'],json.dumps(row['request']['messages'],ensure_ascii=False)])
    report=dict(created_at=now(),status='control100_history420_plain120_all_literal_reviewed_NLL640_validated',
        control100_C1_minus_C0=comparison,history_cells=cells,history_family_effects=effects,likelihood_summary=nll_summary,plain_summary=plain_summary,
        source_sha256=sha(__file__),history_notes_sha256=sha(directory/'notes.json'),plain_notes_sha256=sha(RUN/'plain_notes.json'),
        counts=dict(new_control=200,prefix=100,history_finals=320,plain=120,conditional_NLL=640),
        no_training_or_GPU=True,scope='Diagnosis completed; prospective SFT and new evaluation still required')
    save(target,report)
    print(json.dumps(report,ensure_ascii=False))


if __name__=='__main__':main()
