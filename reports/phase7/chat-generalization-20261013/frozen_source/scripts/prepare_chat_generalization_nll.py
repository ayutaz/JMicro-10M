"""Same frozen 2554 targets for every point; TRAIN and DEV labelled separately."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_generalization_train import DATA,D0,RUN,WEIGHTS,dump_jsonl


def main():
    assert not (DATA/'nll_fixed.jsonl').exists()
    manifest=read_json(DATA/'manifest.json');assert sha256(DATA/'train.jsonl')==manifest['train']['sha256']
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');fixed=[]
    for name,path in (('D0',D0/'train.jsonl'),('D1',DATA/'train.jsonl')):
        records=[json.loads(l) for l in path.read_text().splitlines()]
        assert all(r['split']=='train' for r in records)
        for category in WEIGHTS:
            rows=random.Random('133-NLL-'+name+'-'+category).sample([r for r in records if r['category']==category],16)
            for r in rows:
                fixed.append(dict(id='nll-'+name+'-'+r['doc_id'],dataset=name+'_TRAIN',split='train',category=category,
                    source_doc_id=r['doc_id'],source_target_message_index=r['target_message_indices'][0],messages=r['messages']))
    for c in [json.loads(l) for l in (DATA/'dev.jsonl').read_text().splitlines()]:
        fixed.append(dict(id='nll-newDEV-'+c['id'],dataset='new_DEV',split='dev',source_doc_id=c['id'],
            messages=c['messages']+[dict(role='assistant',content=c['expected_reply'])]))
    # Reuse accepted prepared RPC targets, rather than rescan its corpus.
    old_fixed=D0/'nll_fixed.jsonl'
    accepted=read_json(ROOT/'reports/phase7/chat-improvement-20261012/nll_preparation.json')
    assert sha256(old_fixed)==accepted['sha256']
    for line in old_fixed.read_text().splitlines():
        r=json.loads(line)
        if r['dataset']=='RPC_DEV':
            assert r['split']=='dev';fixed.append(r)
    assert dict(Counter(r['dataset'] for r in fixed))==dict(D0_TRAIN=112,D1_TRAIN=112,new_DEV=80,RPC_DEV=2250)
    assert len({r['id'] for r in fixed})==2554
    sums={k:Counter() for k in ('D0_TRAIN','D1_TRAIN','new_DEV','RPC_DEV')}
    for r in fixed:
        window=list(tok.sft_windows(r['messages'],context=1025))[-1]
        assert window['target_message_index']==len(r['messages'])-1
        labels=[i for i in window['labels'] if i!=-100]
        body=r['messages'][-1].get('text',r['messages'][-1].get('content'))
        assert labels[-1]==7 and 2<=len(labels)<=65 and tok.decode(labels[:-1])==body
        r.update(teachers=len(labels),body_bytes=len(body.encode('utf-8')),
            window_binding=hashlib.sha256(json.dumps(window,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
        sums[r['dataset']].update(Assistant_body_teachers=len(labels)-1,EOT_teachers=1,
            body_bytes=r['body_bytes'],valid_inputs=len(window['input_ids'])-1,removed_prior_turns=window['removed_turns'])
    dump_jsonl(DATA/'nll_fixed.jsonl',fixed)
    atomic_json(RUN/'nll_preparation.json',dict(created_at=now(),status='common_targets_frozen',
        path=str(DATA/'nll_fixed.jsonl'),sha256=sha256(DATA/'nll_fixed.jsonl'),source_sha256=sha256(Path(__file__)),
        accepted_RPC_target_source_sha256=accepted['sha256'],counts=dict(Counter(r['dataset'] for r in fixed)),
        statistics={k:dict(v) for k,v in sums.items()},body_and_EOT_separate=True,
        new_DEV_training=False,protected_TEST_used=False,GPU_learning_tokens=0))
    print('2554 common NLL targets frozen')


if __name__=='__main__':main()
