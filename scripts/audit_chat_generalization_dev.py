"""Bounded DEV/this-TRAIN overlap and protocol audit; no model/GPU forward."""
from collections import Counter
import json
from pathlib import Path
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-generalization-20261013')
RUN=ROOT/'reports/phase7/chat-generalization-20261013'

def grams(text):
    text=re.sub(r'[\s。、？！?！「」『』,.!]+','',text)
    return {text[i:i+3] for i in range(max(0,len(text)-2))}

def main():
    train=[json.loads(l) for l in (DATA/'train.jsonl').read_text().splitlines()]
    dev=[json.loads(l) for l in (DATA/'dev.jsonl').read_text().splitlines()]
    manifest=json.loads((DATA/'manifest.json').read_text())
    assert sha256(DATA/'train.jsonl')==manifest['train']['sha256']
    assert manifest['created_at']<json.loads((RUN/'dev_preparation.json').read_text())['created_at']
    unique={}
    for record in train:
        question=record['messages'][-2]['text'];canonical=question
        state=record.get('grounding',{}).get('state',{})
        for value in sorted(set(state.values()),key=lambda v:len(str(v)),reverse=True):
            if isinstance(value,str) and value not in ('arabic','kanji'):
                canonical=canonical.replace(value,'□')
        unique.setdefault(canonical,dict(family=record['family'],example_id=record['doc_id'],question=question,grams=grams(canonical)))
    checks=[]
    for case in dev:
        final=case['messages'][-1]['content'];g=grams(re.sub(r'\d+','□',final));nearest=[]
        for template,row in unique.items():
            score=len(g & row['grams'])/len(g | row['grams']) if g|row['grams'] else 1.
            nearest.append((score,template,row))
        nearest.sort(key=lambda x:x[0],reverse=True)
        score,template,row=nearest[0]
        assert final not in {r['messages'][-2]['text'] for r in train}
        checks.append(dict(id=case['id'],nearest_surface_Jaccard=score,
            nearest_TRAIN_family=row['family'],nearest_TRAIN_id=row['example_id'],
            exact_final_question=False,surface_similarity_flag=score>=.65,
            manual_structure_review='New authored wording and turn structure/combinations; shared ability is intentional. Not simply substituted TRAIN slots.'))
    token=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    for c in dev:
        roles=[m['role'] for m in c['messages']]
        assert roles==['user' if i%2==0 else 'assistant' for i in range(len(roles))]
        _,removed=token.chat_prompt(c['messages'],960);assert removed==0
        # Worst-case 4*64 generated tokens still leave the actual User turns.
        user_budget=sum(len(token.encode(m['content']))+2 for m in c['messages'] if m['role']=='user')
        assert user_budget+64*sum(m['role']=='user' for m in c['messages'])+16<1024
    own=[c for c in dev if len(c['messages'])>1]
    lengths=Counter(sum(m['role']=='user' for m in c['messages']) for c in own)
    assert len(dev)==80 and len({c['family_id'] for c in dev})==80 and len(own)==24 and sum(k*v for k,v in lengths.items())==59
    assert all(c['split']=='dev' for c in dev) and all(v==8 for v in Counter(c['category'] for c in dev).values())
    flagged=[r for r in checks if r['surface_similarity_flag']]
    report=dict(created_at=now(),status='protocol_valid_surface_screen_completed_manual_review_recorded',
        train_sha256=manifest['train']['sha256'],dev_sha256=sha256(DATA/'dev.jsonl'),source_sha256=sha256(Path(__file__)),
        families=80,own_families=24,own_responses=59,own_lengths=dict(lengths),source_template_count=len(unique),
        exact_final_question_overlap=0,surface_flags=len(flagged),max_surface_Jaccard=max(r['nearest_surface_Jaccard'] for r in checks),
        cases=checks,provided_and_worst_case_own_history_fit=True,
        limitations='Character ngrams are a surface screening aid, not semantic independence certification; only this frozen D1 TRAIN was scanned. Parent pretraining corpus was not rescanned.',
        gold_content_review='Codex author reviewed all 80 scripts and gold histories/replies; nonblind, not independent human review.',
        all_TRAIN_or_web_corpus_deduplicated=False,old_TEST_content_parsed=False,protected_TEST_used=False,new_DEV_training=False,GPU_learning_tokens=0)
    atomic_json(RUN/'dev_audit.json',report)
    print(json.dumps({k:report[k] for k in ('status','source_template_count','exact_final_question_overlap','surface_flags','max_surface_Jaccard')}))

if __name__=='__main__':main()
