"""Plan133 TRAIN revision; does not read DEV/TEST or modify closed runs."""
from collections import Counter,defaultdict
import json
from pathlib import Path
import random
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_generalization_curriculum import WEIGHTS,render_targets,semantic_check
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_improvement_train import content_binding,dump_jsonl,BOUNDS

RUN=ROOT/'reports/phase7/chat-generalization-20261013'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-generalization-20261013')
D0=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
TARGET=660000


def main():
    assert sys.version_info[:3]==(3,12,7)
    assert not (DATA/'manifest.json').exists(),'Frozen TRAIN retained'
    assert not (DATA/'dev.jsonl').exists(),'Design and TRAIN must precede new DEV'
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    sources={p:sha256(ROOT/p) for p in ('src/jmicro/chat_generalization_curriculum.py',
        'scripts/prepare_chat_generalization_train.py')}
    design=RUN/'train_design_freeze.json'
    if design.exists():assert read_json(design)['sources']==sources,'Version changed design before regenerating'
    else:atomic_json(design,dict(created_at=now(),sources=sources,mixture=WEIGHTS,
        minimum_teachers=650000,target_teachers=TARGET,maximum_family_fraction=.05,
        no_new_DEV_read=True,no_old_DEV_copied=True,
        changes=['mostly first-turn questions without identity preamble',
            'first/middle factual Assistant targets supervised as separate prefixes',
            'broader slot vocabulary and bounded paraphrases',
            'remove common explanation boilerplate; grounded direct bodies'],
        comparison='whole data recipe, not an identified single causal factor',
        independent_human_review=False))
    pools=defaultdict(list);seen=set();rejected=Counter()
    # Reuse previously accepted TRAIN greetings only; no rescan of RPC corpus.
    old=read_json(D0/'manifest.json');assert sha256(D0/'train.jsonl')==old['train']['sha256']
    for line in (D0/'train.jsonl').read_text().splitlines():
        r=json.loads(line)
        if r['source']=='RealPersonaChat-selected-unedited':
            assert r['category']=='daily';r=dict(r,doc_id='d1-'+r['doc_id'],target_kind='natural_first_turn')
            pools['daily'].append(r);seen.add(content_binding(r))
    for category in WEIGHTS:
        for index in range(24):
            for variant in range(4096):
                for r in render_targets(category,index,variant):
                    assert semantic_check(r)
                    body=r['messages'][-1]['text'];ids=tok.encode(body);n=len(ids)+1
                    if not 2<=n<=65:rejected['length']+=1;continue
                    if tok.decode(ids)!=body:rejected['roundtrip']+=1;continue
                    digest=content_binding(r)
                    if digest in seen:rejected['duplicate_messages']+=1;continue
                    seen.add(digest)
                    r.update(content_sha256=digest,teacher_tokens=n,
                        length_bin=next(i for i,(lo,hi) in enumerate(BOUNDS) if lo<=n<=hi))
                    pools[category].append(r)
            print(json.dumps(dict(stage='bounded_family_pool',category=category,index=index,
                accepted=len(pools[category])),ensure_ascii=False),flush=True)
    atomic_json(RUN/'train_pool_coverage.json',dict(created_at=now(),sources=sources,
        counts={k:len(v) for k,v in pools.items()},
        family_teachers={k:dict(Counter({f:sum(r['teacher_tokens'] for r in v if r['family']==f)
            for f in {r['family'] for r in v}})) for k,v in pools.items()},
        GPU_learning_tokens=0,new_DEV_created=False))
    # Choose balanced authored families; measure length/EOT differences rather
    # than truncate replies or fabricate reasoning to match token counts.
    selected=[];family_counts=defaultdict(Counter);categories=Counter()
    rng=random.Random(13342)
    for category,weight in WEIGHTS.items():
        quota=round(TARGET*weight);cap=int(quota*.047)
        records=list(pools[category]);rng.shuffle(records)
        preference=(.20,.7,4.,3.)
        records.sort(key=lambda r:rng.expovariate(preference[r['length_bin']]*(20. if len(r['messages'])==2 else 1.)))
        for r in records:
            if categories[category]>=quota:break
            if family_counts[category][r['family']]+r['teacher_tokens']>cap:continue
            selected.append(r);categories[category]+=r['teacher_tokens']
            family_counts[category][r['family']]+=r['teacher_tokens']
        assert categories[category]>=quota,(category,categories[category],quota)
    rng.shuffle(selected)
    for r in selected:
        assert r['split']=='train' and r['target_message_indices']==[len(r['messages'])-1]
        assert [m['role'] for m in r['messages']]==['user' if i%2==0 else 'assistant' for i in range(len(r['messages']))]
        assert all(m['text'] and '\ufffd' not in m['text'] and '<|im_' not in m['text'] for m in r['messages'])
        assert r['content_sha256']==content_binding(r)
    dump_jsonl(DATA/'candidate.train.jsonl',selected)
    packet=[]
    for category in WEIGHTS:
        rows=[r for r in selected if r['category']==category]
        packet.extend(random.Random('133-review-'+category).sample(rows,40))
    dump_jsonl(DATA/'train_review_packet.jsonl',packet)
    hist=Counter(r['length_bin'] for r in selected)
    report=dict(created_at=now(),status='candidate_pending_280_actual_content_reviews',sources=sources,
        path=str(DATA/'candidate.train.jsonl'),sha256=sha256(DATA/'candidate.train.jsonl'),
        targets=len(selected),teachers=sum(categories.values()),teacher_categories=dict(categories),
        category_fractions={k:v/sum(categories.values()) for k,v in categories.items()},
        family_statistics={k:dict(count=len(v),max_fraction=max(v.values())/categories[k]) for k,v in family_counts.items()},
        length_bins=[hist[i] for i in range(4)],length_bin_fractions=[hist[i]/len(selected) for i in range(4)],
        target_kinds=dict(Counter(r['target_kind'] for r in selected)),
        single_User_targets=sum(len(r['messages'])==2 for r in selected),
        exact_body_types=len({r['messages'][-1]['text'] for r in selected}),
        review_packet_sha256=sha256(DATA/'train_review_packet.jsonl'),rejections=dict(rejected),
        D0_TRAIN_sha256=old['train']['sha256'],new_DEV_created=False,GPU_learning_tokens=0,
        full_corpus_scan=False,independent_human_review=False)
    atomic_json(RUN/'train_candidate.json',report)
    print(json.dumps({k:v for k,v in report.items() if k not in ('sources','rejections')},ensure_ascii=False))


if __name__=='__main__':main()
