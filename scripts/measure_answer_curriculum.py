"""Freeze actual TRAIN, explicit aliases and both full teacher schedules on CPU."""
from collections import Counter
import gc
import json
from pathlib import Path
import time
import numpy as np
from answer_learning_common import ROOT,RUN,DATA,save,ref,bound,read_json,digest,now
from prepare_answer_curriculum import DIRECTORY,oracle
from jmicro.tokenizer import Tokenizer
from jmicro.teacher_chat_training import TeacherBudgetSampler,teacher_lr


def prepare():
    target=DIRECTORY/'manifest.json';assert not target.exists()
    assert not (DIRECTORY/'C1_TRAIN.jsonl').exists()
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    synthetic=read_json(RUN/'curriculum_synthetic_inventory.json')
    qa=read_json(RUN/'curriculum_variant_QA_review.json')
    assert qa['status']=='all32_rendered_variants_reviewed' and qa['inventory']==ref(RUN/'curriculum_synthetic_inventory.json')
    extra=[json.loads(line) for line in bound(synthetic['records']).read_text().splitlines()]
    for row in extra:assert oracle(row['family'],row['messages'])==row['messages'][-1]['text']
    source_counts=Counter();source_teachers=Counter();reviews=[];rejected_length=Counter()
    for source in ('dolly','aya'):
        review_path=RUN/f'{source}_QA_review.json';review=read_json(review_path);reviews.append(ref(review_path))
        samples={r['id']:r for r in read_json(bound(review['sample']))}
        for note in review['judgments']:
            if not note['accepted_for_next_recipe']:continue
            row=samples[note['id']]
            if row['target_teachers']>32:rejected_length[source]+=1;continue
            copied={k:v for k,v in row.items() if k not in ('id','stratum')}
            copied['semantic_original_id']=copied['doc_id'];extra.append(copied)
    assert len({r['doc_id'] for r in extra})==len(extra)
    seen=set()
    unique=[]
    for row in extra:
        key=digest(json.dumps(row['messages'],ensure_ascii=False,sort_keys=True))
        if key in seen:continue
        seen.add(key);unique.append(row)
        source_counts[row['source']]+=1;source_teachers[row['source']]+=row['target_teachers']
    extra=unique
    old=read_json(ROOT/'configs/phase7/chat-natural-sft-20261017.json')
    baseline=bound(old['arms']['C1']['records']);assert baseline.name=='C1_TRAIN.jsonl'
    base=[json.loads(line) for line in baseline.read_text().splitlines()]
    base_sampler=TeacherBudgetSampler(base,tok,1024,42,1000000,512,32)
    assert base_sampler.binding==old['arms']['C1']['sampler_binding'] and max(base_sampler.lengths)<=32
    baseline_teachers=sum(base_sampler.lengths);del base_sampler;gc.collect()
    copies=max(1,round(baseline_teachers/sum(source_teachers.values())))
    assert copies<=128,'Prospective recipe requires unreasonably many aliases; do not silently change sampling'
    prepared={'C0':base,'C1':list(base)}
    for i in range(copies):
        for row in extra:
            prepared['C1'].append(dict(row,doc_id=f"answer_curriculum_alias:{i:03}:"+row['doc_id'],
                semantic_original_id=row['doc_id'],explicit_repeat_alias=i))
    assert not any((DIRECTORY/f'{arm}_TRAIN.jsonl').exists() for arm in prepared)
    save(DIRECTORY/'supplement_unique_TRAIN.json',extra)
    preparation=dict(status='TRAIN_records_prepared_CPU_replay_pending',created_at=now(),
        plan=ref(ROOT/'docs/153_answer_curriculum_comparison.md'),baseline=old['arms']['C1']['records'],
        baseline_original_QA=old['TRAIN_QA'],synthetic_inventory=ref(RUN/'curriculum_synthetic_inventory.json'),
        synthetic_variant_QA=ref(RUN/'curriculum_variant_QA_review.json'),source_QA=reviews,
        extra_unique=ref(DIRECTORY/'supplement_unique_TRAIN.json'),unique_source_targets=dict(source_counts),
        unique_source_teachers=dict(source_teachers),accepted_but_too_long=dict(rejected_length),
        alias_copies=copies,baseline_teachers_per_pass=baseline_teachers,
        planned_supplement_teachers_per_pass=copies*sum(source_teachers.values()),
        alias_is_not_new_semantic_diversity=True,maximum_teacher_length=32,max_new_tokens=32,
        teacher_budget_per_arm=1000000,lr=1e-4,seed=42,new_TEST_created=False,arms={})
    for arm,rows in prepared.items():
        path=DIRECTORY/f'{arm}_TRAIN.jsonl'
        with path.open('x') as out:
            for row in rows:out.write(json.dumps(row,ensure_ascii=False)+'\n')
        preparation['arms'][arm]=dict(records=ref(path),documents=len(rows))
    save(RUN/'curriculum_TRAIN_preparation.json',preparation)
    print(dict(status='prepared',copies=copies,supplement_unique=len(extra),baseline_teachers=baseline_teachers,
        supplemental_teachers=copies*sum(source_teachers.values()),sources=dict(source_counts)),flush=True)


def replay():
    target=DIRECTORY/'manifest.json';assert not target.exists()
    preparation=read_json(RUN/'curriculum_TRAIN_preparation.json');summaries={}
    for arm in ('C0','C1'):
        output=RUN/f'curriculum_{arm}_CPU_replay.json'
        assert not output.exists(),'Inspect prior evidence instead of reopening a replay'
        started=time.monotonic();path=bound(preparation['arms'][arm]['records'])
        rows=[json.loads(line) for line in path.read_text().splitlines()];lookup={r['doc_id']:r for r in rows}
        sampler=TeacherBudgetSampler(rows,tok:=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model'),1024,42,1000000,512,32)
        source_supply=Counter();unique=set();semantic_seen=Counter();source_consumed=Counter();history=[]
        for w,n in zip(sampler.windows,sampler.lengths,strict=True):
            r=lookup[w['doc_id']];target_tokens=w['labels'][w['labels']!=-100]
            answer=r['messages'][w['target_message_index']]['text']
            assert 2<=n<=32 and target_tokens.tolist()==tok.encode(answer)+[7]
            assert np.all(w['labels'][:-n]==-100) and w['removed_turns']==0
            source_supply[r['source']]+=n;unique.add((r.get('semantic_original_id',r['doc_id']),w['target_message_index']))
        while sampler.teacher_tokens<1000000:
            before=sampler.teacher_tokens;position=sampler.position;epoch=sampler.epoch;order=sampler.order.copy();examples=sampler.examples
            batches,n,_=sampler.next_update();used=sampler.examples-examples
            indices=list(order[position:position+used]) if epoch==sampler.epoch else list(order[position:])+list(sampler.order[:sampler.position])
            assert len(indices)==used and sum(int(y.ne(-100).sum()) for _,y in batches)==n
            for i in indices:
                w=sampler.windows[int(i)];r=lookup[w['doc_id']]
                source_consumed[r['source']]+=sampler.lengths[int(i)]
                semantic_seen[(r.get('semantic_original_id',r['doc_id']),w['target_message_index'])]+=1
            assert all(x.shape==y.shape==(32,1024) for x,y in batches)
            history.append(dict(update=len(history)+1,teachers=sampler.teacher_tokens,teachers_this_update=n,
                microbatches=len(batches),lr=teacher_lr(before,n,1000000,1e-4)))
        assert sum(source_consumed.values())==sampler.teacher_tokens and sampler.teacher_tokens<=1000031
        terminal=sampler.state_dict();sampler.load_state_dict(terminal);assert sampler.state_dict()==terminal
        summary=dict(status='passed',records=ref(path),sampler_binding=sampler.binding,prepared_targets=len(sampler.windows),
            unique_semantic_targets=len(unique),teachers_per_pass=sum(sampler.lengths),source_supply=dict(source_supply),
            actual_consumed_source_teachers=dict(source_consumed),actual_consumed_source_fractions={k:v/sampler.teacher_tokens for k,v in source_consumed.items()},
            actual_supplement_fraction=sum(v for k,v in source_consumed.items() if k not in ('RPC','magpie'))/sampler.teacher_tokens,
            distinct_semantic_targets_consumed=len(semantic_seen),maximum_semantic_target_exposures=max(semantic_seen.values()),
            updates=len(history),actual_teachers=sampler.teacher_tokens,physical_microbatches=sum(r['microbatches'] for r in history),
            maximum_microbatches_per_update=max(r['microbatches'] for r in history),history=history,sampler_terminal=terminal,
            all_teacher_masks_and_complete_roundtrips=True,no_history_trim=True,terminal_sampler_roundtrip=True,
            CPU_seconds=time.monotonic()-started,created_at=now(),new_training_updates=0)
        save(output,summary);summaries[arm]=dict(records=ref(path),dry_run=ref(output),sampler_binding=sampler.binding,
            **{k:summary[k] for k in ('prepared_targets','unique_semantic_targets','teachers_per_pass','updates','actual_teachers',
                'physical_microbatches','actual_consumed_source_fractions','actual_supplement_fraction','maximum_semantic_target_exposures')})
        print(dict(arm=arm,**summaries[arm]),flush=True)
        del sampler,rows,lookup;gc.collect()
    save(target,dict(status='TRAIN_frozen_before_new_DEV',created_at=now(),preparation=ref(RUN/'curriculum_TRAIN_preparation.json'),
        arms=summaries,teacher_budget_per_arm=1000000,maximum_teacher_length=32,max_new_tokens=32,
        source_licensing='Retain inherited RPC/Magpie and Dolly CC-BY-SA3.0 / Aya Apache2.0 provenance; no distribution authorized',
        alias_is_not_new_semantic_diversity=True,new_TEST_created=False,semantic_quality_of_full_inherited_baseline_not_certified=True))
    save(RUN/'curriculum_TRAIN_manifest_ref.json',ref(target))


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','replay']);a=p.parse_args()
    {'prepare':prepare,'replay':replay}[a.mode]()
