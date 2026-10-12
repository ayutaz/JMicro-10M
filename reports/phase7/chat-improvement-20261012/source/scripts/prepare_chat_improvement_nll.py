"""Freeze common NLL targets before learning; no model forward/TEST access."""
from collections import Counter
import json
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.assistant_sampler import AssistantSampler
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_improvement_train import DATA,RPC,RUN,WEIGHTS,dump_jsonl


def records(path):return [json.loads(line) for line in path.read_text().splitlines()]


def main():
    assert not (DATA/'nll_fixed.jsonl').exists(),'Fixed NLL targets are immutable'
    manifest=json.loads((DATA/'manifest.json').read_text())
    assert sha256(DATA/'train.jsonl')==manifest['train']['sha256']
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    c0=records(RPC/'train.jsonl');c1=records(DATA/'train.jsonl');dev=records(DATA/'dev.jsonl')
    sampler=AssistantSampler(c0,tok,1024,42);by_id={r['doc_id']:r for r in c0}
    windows=random.Random(1311120).sample(sampler.windows,112);fixed=[]
    for w in windows:
        original=by_id[w['doc_id']];messages=json.loads(original['messages_json'])[:w['target_message_index']+1]
        fixed.append(dict(id=f"nll-C0-{w['doc_id']}-{w['target_message_index']}",dataset='C0_TRAIN',split='train',
            source_doc_id=w['doc_id'],source_target_message_index=w['target_message_index'],messages=messages))
    for category in WEIGHTS:
        selected=random.Random(f'1311121:{category}').sample([r for r in c1 if r['category']==category],16)
        for r in selected:
            fixed.append(dict(id='nll-C1-'+r['doc_id'],dataset='C1_TRAIN',split='train',category=category,
                source_doc_id=r['doc_id'],source_target_message_index=r['target_message_indices'][0],messages=r['messages']))
    for c in dev:
        fixed.append(dict(id='nll-newDEV-'+c['id'],dataset='new_DEV',split='dev',source_doc_id=c['id'],
            messages=c['messages']+[dict(role='assistant',content=c['expected_reply'])]))
    rpcdev=records(RPC/'dev.jsonl')
    assert all(r['split']=='dev' for r in rpcdev)
    for r in rpcdev:
        messages=json.loads(r['messages_json'])
        for index,m in enumerate(messages):
            if m['role']!='assistant':continue
            fixed.append(dict(id=f"nll-RPCDEV-{r['doc_id']}-{index}",dataset='RPC_DEV',split='dev',
                source_doc_id=r['doc_id'],source_target_message_index=index,messages=messages[:index+1]))
    counts=Counter(r['dataset'] for r in fixed)
    assert dict(counts)==dict(C0_TRAIN=112,C1_TRAIN=112,new_DEV=80,RPC_DEV=2250)
    assert len({r['id'] for r in fixed})==len(fixed)
    statistics={k:Counter() for k in counts}
    for r in fixed:
        windows=list(tok.sft_windows(r['messages'],context=1025));window=windows[-1]
        assert window['target_message_index']==len(r['messages'])-1
        labels=[i for i in window['labels'] if i!=-100]
        assert labels[-1]==7 and all(i>=8 for i in labels[:-1]) and 2<=len(labels)<=65
        gold=r['messages'][-1].get('text',r['messages'][-1].get('content'))
        assert tok.decode(labels[:-1])==gold
        r['teachers']=len(labels);r['body_bytes']=len(gold.encode('utf-8'))
        r['window_binding']=__import__('hashlib').sha256(json.dumps(window,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        statistics[r['dataset']].update(dict(Assistant_body_teachers=len(labels)-1,EOT_teachers=1,body_bytes=r['body_bytes'],
            valid_inputs=len(window['input_ids'])-1,removed_prior_turns=window['removed_turns']))
    dump_jsonl(DATA/'nll_fixed.jsonl',fixed)
    atomic_json(RUN/'nll_preparation.json',dict(created_at=now(),status='fixed_same_targets_for_both_arms_all_checkpoints',
        source_sha256=sha256(Path(__file__)),path=str(DATA/'nll_fixed.jsonl'),sha256=sha256(DATA/'nll_fixed.jsonl'),
        sources={str(p):sha256(p) for p in (RPC/'train.jsonl',RPC/'dev.jsonl',DATA/'train.jsonl',DATA/'dev.jsonl')},
        counts=dict(counts),statistics={k:dict(v) for k,v in statistics.items()},
        C1_TRAIN_category_counts=dict(Counter(r['category'] for r in fixed if r['dataset']=='C1_TRAIN')),
        original_train_has_112_fixed_target_ids=True,body_and_EOT_separate=True,
        comparisons='Only compare losses on same dataset/target texts and bytes; different TRAIN distributions are not quality rankings',
        new_DEV_training=False,protected_TEST_used=False,GPU_learning_tokens=0))
    print(json.dumps(dict(counts=dict(counts),path=str(DATA/'nll_fixed.jsonl'),sha256=sha256(DATA/'nll_fixed.jsonl'))))

if __name__=='__main__':main()
