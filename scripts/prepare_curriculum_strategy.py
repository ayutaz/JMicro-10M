"""Bounded source-family-separated10M pilot; no corpus-wide duplicate audit."""
import argparse
from collections import Counter
import json
from pathlib import Path
import random
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from jmicro.curriculum_strategy import select, family_split
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.shards import build_shards
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/curriculum-strategy-20261005')
RUN=ROOT/'reports/phase6/curriculum-strategy-20261005'
TOK=ROOT/'artifacts/phase2/4096/tokenizer.model'


def prepare():
    RUN.mkdir(parents=True,exist_ok=True);DATA.mkdir(parents=True,exist_ok=True)
    path=RUN/'prepare-job.json'
    if path.exists():
        old=read_json(path);assert not alive(old)
        if old['status']=='complete':print('Completed preparation retained');return
        raise ValueError('Inspect failed preparation; do not overwrite its evidence')
    base=read_json(ROOT/'configs/phase6/narrative_comparison.json')
    story=read_json(ROOT/'configs/phase6/amount_story_study.json')['pool']
    sources=dict(story=dict(directory=story['pool'],sha256=story['manifest_sha256']),
        web=dict(directory='/home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards',sha256='2d7b3d0b21fa9267c8f3bf8121f1a156f68f843c9676c2b2b004b01ab77d30de'))
    targets=(dict(short=1000000,narrative=4000000,general=5000000) if DATA.name.endswith('-v3')
             else dict(short=2000000,narrative=5000000,general=3000000) if DATA.name.endswith('-v2')
             else dict(short=4000000,narrative=3000000,general=3000000))
    binding=dict(sources=sources,train_prepared_targets=targets,dev_fraction=.05,
        CPU_budget_seconds=600,max_index_rows_per_source=700000,seed=202610082,
        selector_sha256=sha256(ROOT/'src/jmicro/curriculum_strategy.py'),builder_sha256=sha256(Path(__file__)))
    start=time.monotonic();job=dict(status='running',**identity(),binding=binding,started_at=now());counts=Counter();totals=Counter()
    def heartbeat(stage):
        if time.monotonic()-start>600:raise TimeoutError('600s CPU preparation budget exhausted')
        job.update(stage=stage,heartbeat_at=now(),counts=dict(counts),tokens=dict(totals),seconds=time.monotonic()-start)
        atomic_json(path,job)
    try:
        tok=Tokenizer(TOK);assert sha256(TOK)==base['tokenizer_sha256']
        known=set();heads=set();records=[];families={};protected=[]
        if DATA.name.endswith('-v3'):
            old_sample=read_json(DATA.with_name('curriculum-strategy-20261005-v2')/'sample64.json')
            known.update(r['canonical_sha256'] for r in old_sample)
        for p in ('eval/base.jsonl','eval/japanese_semantics_v2_1.jsonl'):
            for line in (ROOT/p).read_text().splitlines():
                r=json.loads(line);protected.extend(v for k,v in r.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>12)
        for source,entry in sources.items():
            directory=Path(entry['directory']);assert sha256(directory/'manifest.json')==entry['sha256']
            stream=np.memmap(directory/'train.bin',dtype='<u2',mode='r')
            with (directory/'train.index.jsonl').open() as index:
                for line in index:
                    counts[source+'_rows']+=1
                    if counts[source+'_rows']>700000:break
                    row=json.loads(line)
                    if source=='web' and row.get('source')!='web':continue
                    size=row['body_tokens']
                    if not (40<=size<=128 if source=='story' else 96<=size<=384):continue
                    text=tok.decode_bytes(stream[row['offset']+1:row['offset']+1+size].tolist()).decode('utf-8')
                    unit=select(text,size,source)
                    if not unit:continue
                    group=unit['group']
                    family=(source+':'+row['parent_id']) if source=='story' else 'web:'+str(row.get('source_start',row['offset']))
                    split=family_split(family)
                    # At most one literal document per source family AND normalized first sentence.
                    if family in families or unit['canonical_sha256'] in known or unit['family_head'] in heads:continue
                    if totals[split+'_'+group]>=(targets[group] if split=='train' else int(targets[group]*.05)):continue
                    if any(p in text for p in protected):continue
                    known.add(unit['canonical_sha256']);heads.add(unit['family_head']);families[family]=split
                    record=dict(unit,doc_id='curriculum-'+unit['canonical_sha256'][:20],id='curriculum-'+unit['canonical_sha256'][:20],
                        kind='web',split=split,bucket=group,source=source,source_family=family,
                        source_manifest_sha256=entry['sha256'],source_metadata=row,source_offset=row['offset'],body_tokens=size,
                        source_previously_in_parent_web_training=(source=='web'))
                    records.append(record);totals[split+'_'+group]+=size+2
                    if len(records)%1000==0:heartbeat(source)
                    active=('short','narrative') if source=='story' else ('general',)
                    if all(totals[s+'_'+g]>=targets[g]*(1 if s=='train' else .05) for s in ('train','dev') for g in active):break
        heartbeat('supply-check')
        assert all(totals['train_'+g]>=n for g,n in targets.items()),dict(totals)
        assert all(totals['dev_'+g]>=int(n*.05) for g,n in targets.items()),dict(totals)
        assert not {r['source_family'] for r in records if r['split']=='train'} & {r['source_family'] for r in records if r['split']=='dev'}
        corpus=DATA/'curriculum.jsonl';corpus.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
        heartbeat('build-shards');manifest=build_shards(corpus,TOK,DATA/'shards')
        sample=[];rng=random.Random(202610082)
        for group,n in [('short',24),('narrative',24),('general',16)]:
            sample.extend(rng.sample([r for r in records if r['split']=='train' and r['group']==group],n))
        write_json(DATA/'sample64.json',sample)
        write_json(DATA/'dev32.json',random.Random(202610083).sample([r for r in records if r['split']=='dev'],32))
        metadata=dict(status='prepared_pending_content_review',binding=binding,pool=str(DATA/'shards'),
            manifest_sha256=sha256(DATA/'shards/manifest.json'),corpus_sha256=sha256(corpus),
            sample_sha256=sha256(DATA/'sample64.json'),splits=manifest['splits'],tokens_by_group=dict(totals),
            documents_by_source=dict(Counter(r['source'] for r in records)),structures=dict(Counter('quote' if '「' in r['text'] else 'conditional' if any(w in r['text'] for w in ('なら','場合','もし')) else 'other' for r in records)),
            family_split='source parent_id/Web source_start; one document per family and normalized first sentence',
            overlap_audit='local exact/family/head only; no completed full old-corpus near-duplicate audit',
            source_history='Web was part of original train; auxiliary dev is not wholly unseen by10B parent. Official dev remains separate.',
            source_provenance={s:read_json(Path(e['directory'])/'manifest.json').get('source',read_json(Path(e['directory'])/'manifest.json').get('binding')) for s,e in sources.items()},
            CPU_seconds=time.monotonic()-start,protected_test_used=False,created_at=now())
        write_json(DATA/'ready.json',metadata);write_json(RUN/'ready.json',metadata)
        heartbeat('complete');job.update(status='complete',completed_at=now());print(json.dumps(metadata,ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:job['seconds']=time.monotonic()-start;atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--revision',choices=('v1','v2','v3'),default='v1');a=p.parse_args()
    if a.revision!='v1':
        DATA=DATA.with_name(DATA.name+'-'+a.revision);RUN=RUN.with_name(RUN.name+'-'+a.revision)
    prepare()
