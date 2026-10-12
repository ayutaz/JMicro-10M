"""Validate independently authored DEV only AFTER immutable TRAIN freeze."""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_generalization_train import DATA,RUN,dump_jsonl


def main():
    manifest=read_json(DATA/'manifest.json')
    assert manifest['status']=='reviewed_TRAIN_frozen_before_new_DEV'
    assert sha256(DATA/'train.jsonl')==manifest['train']['sha256']
    assert not (DATA/'dev.jsonl').exists(),'DEV immutable; retain any completed version'
    authored=read_json(DATA/'dev_authored.json')
    assert authored['created_at']>manifest['created_at']
    assert authored['train_manifest_sha256']==sha256(DATA/'manifest.json')
    assert authored['reviewer']=='Codex nonblind' and authored['all_scripts_and_gold_reviewed']
    cases=authored['cases'];tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    assert len(cases)==len({c['id'] for c in cases})==len({c['family_id'] for c in cases})==80
    assert all(c['split']=='dev' for c in cases)
    assert len(Counter(c['category'] for c in cases))==10 and all(v==8 for v in Counter(c['category'] for c in cases).values())
    for c in cases:
        assert [m['role'] for m in c['messages']]==['user' if i%2==0 else 'assistant' for i in range(len(c['messages']))]
        assert len(c['messages'])%2==1 and c['messages'][-1]['role']=='user'
        assert all(m['content'] and '\ufffd' not in m['content'] for m in c['messages'])
        for text in [m['content'] for m in c['messages'] if m['role']=='assistant']+[c['expected_reply']]:
            ids=tok.encode(text);assert 2<=len(ids)+1<=65 and tok.decode(ids)==text
        ids,removed=tok.chat_prompt(c['messages'],960);assert removed==0;c['prompt_tokens']=len(ids)
        assert len(c['gold_review_rationale'])>=12
    own=[c for c in cases if len(c['messages'])>1]
    counts=Counter(sum(m['role']=='user' for m in c['messages']) for c in own)
    assert len(own)==24 and dict(counts)=={2:15,3:7,4:2} and sum(k*v for k,v in counts.items())==59
    train_questions={json.loads(l)['messages'][-2]['text'] for l in (DATA/'train.jsonl').read_text().splitlines()}
    assert not any(c['messages'][-1]['content'] in train_questions for c in cases)
    dump_jsonl(DATA/'dev.jsonl',cases)
    report=dict(created_at=now(),status='DEV_authored_after_TRAIN_and_gold_checked',source_sha256=sha256(Path(__file__)),
        authored_path=str(DATA/'dev_authored.json'),authored_sha256=sha256(DATA/'dev_authored.json'),
        train_manifest_sha256=sha256(DATA/'manifest.json'),train_sha256=manifest['train']['sha256'],
        dev_path=str(DATA/'dev.jsonl'),dev_sha256=sha256(DATA/'dev.jsonl'),families=80,own_families=24,
        own_responses=59,own_lengths=dict(counts),categories=dict(Counter(c['category'] for c in cases)),
        new_DEV_will_not_be_used_for_learning=True,protected_TEST_used=False,independent_human_review=False,
        all_gold_Codex_nonblind_review=True,GPU_learning_tokens=0)
    atomic_json(RUN/'dev_preparation.json',report)
    print(json.dumps(dict(dev_sha256=report['dev_sha256'],families=80,own_responses=59)))


if __name__=='__main__':main()
