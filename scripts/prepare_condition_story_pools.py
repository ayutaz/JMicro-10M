"""Plan61 bounded same-source whole-document pool preparation; no retokenization."""
from collections import Counter,defaultdict
import json
import multiprocessing as mp
import os
from pathlib import Path
import shutil
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json
from jmicro.eos_pilot import TrainView
from jmicro.tokenizer import Tokenizer
from jmicro.complete_units import unit_hash
from jmicro.condition_story_quality import exclusion_reasons
from phase6_performance import identity,alive
from prepare_matched_story_pools import matched_quotas
import prepare_complete_units as decode

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-preservation-20261005')
SOURCE=Path('/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005/shards')
SEED=202610061;TARGET=20_000_000;BUDGET=1800

def worker_batch(batch):
    result=[]
    for record in batch:
        a,size=record['offset'],record['body_tokens']
        text=b''.join(decode._PIECES[i] for i in decode._TRAIN[a+1:a+1+size].tolist()).decode('utf-8').strip()
        assert unit_hash(text)==record['text_sha256']
        result.append((record,exclusion_reasons(text)))
    return result

def batches(check,counts):
    batch=[]
    for line in (SOURCE/'train.index.jsonl').open():
        record=json.loads(line)
        if record['source']!='translation':continue
        assert record['split']=='train' and int(record['family'][:8],16)%100!=0
        batch.append(record);counts['translation_rows_read']+=1
        if len(batch)==256:check();yield batch;batch=[]
    if batch:yield batch

def main():
    assert sys.version_info[:3]==(3,12,7)
    DATA.mkdir(parents=True,exist_ok=True);ready_source=read_json(SOURCE/'ready.json')
    assert ready_source['source_train_only'] and ready_source['whole_original_documents'] and not ready_source['official_validation_test_acquired']
    binding=dict(source_pool=str(SOURCE),source_manifest_sha256=sha256(SOURCE/'manifest.json'),
        source_ready_sha256=sha256(SOURCE/'ready.json'),source_diagnosis_sha256=sha256(DATA/'diagnosis.json'),
        revision='155b4e5842076c90e07a4934d5b68410fe21f65f',source='shibatch/TinyStories-JA',
        builder_sha256=sha256(Path(__file__)),selector_sha256=sha256(ROOT/'src/jmicro/condition_story_quality.py'),
        target_tokens=TARGET,seed=SEED,budget_seconds=BUDGET,
        scope='Prepared translation-only train stream after unchanged common base selector/family/local exclusion; candidate adds frozen heuristic exclusions')
    job_path=DATA/'prepare-job.json'
    if job_path.exists():
        prior=read_json(job_path);assert not alive(prior) and prior['binding']==binding
        if prior['status']=='complete':print(json.dumps(read_json(DATA/'ready.json')));return
        raise RuntimeError('Retained incomplete preparation; inspect actual failure, no identical retry')
    earlier=read_json(DATA/'diagnosis.json')['CPU_seconds']
    started=time.monotonic();counts=Counter();reasons=Counter();original=defaultdict(list);eligible=defaultdict(list)
    job=dict(status='running',**identity(),binding=binding,started_at=now())
    def check():
        if earlier+time.monotonic()-started>BUDGET:raise TimeoutError('1800s preparation exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,elapsed_seconds=earlier+time.monotonic()-started,heartbeat_at=now(),counts=dict(counts),**extra)
        atomic_json(job_path,job);print(json.dumps(dict(stage=stage,seconds=job['elapsed_seconds'],**extra)),flush=True)
    try:
        heartbeat('setup');view=TrainView(str(SOURCE),binding['source_manifest_sha256'],check_stream=True)
        for relative in ('scripts/prepare_condition_story_pools.py','src/jmicro/condition_story_quality.py'):
            target=DATA/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/relative,target)
        last=time.monotonic()
        with mp.get_context('fork').Pool(12,initializer=decode.worker_init,initargs=(str(ROOT/'artifacts/phase2/4096/tokenizer.model'),str(SOURCE/'train.bin'))) as workers:
            for classified in workers.imap(worker_batch,batches(check,counts),chunksize=1):
                check()
                for record,defects in classified:
                    size=record['body_tokens'];original[size].append(record);reasons.update(defects)
                    if not defects:eligible[size].append(record)
                if time.monotonic()-last>10:heartbeat('classify',classified=sum(map(len,original.values())),eligible=sum(map(len,eligible.values())));last=time.monotonic()
        population={s:len(v) for s,v in original.items()};good={s:len(v) for s,v in eligible.items()}
        quota=matched_quotas(population,good,target=TARGET)
        amount=sum((s+2)*n for s,n in quota.items());docs=sum(quota.values())
        supply=dict(population=population,eligible_histogram=good,matched_histogram=quota,
            eligible_tokens=sum((s+2)*n for s,n in good.items()),target_tokens=TARGET,possible_tokens=amount,
            exclusion_counts=dict(reasons),translation_rows_classified=sum(population.values()))
        write_json(DATA/'supply-diagnostic.json',supply)
        assert amount>=TARGET, 'Matched20M supply not met; report preparation failure without GPU'
        rng=np.random.default_rng(SEED);chosen={a:{} for a in ('control','refined')}
        for size,n in sorted(quota.items()):
            if not n:continue
            for arm,pop in [('control',original[size]),('refined',eligible[size])]:
                chosen[arm][size]=[pop[int(i)] for i in rng.choice(len(pop),size=n,replace=False)]
        sizes=np.asarray([s for s,n in sorted(quota.items()) for _ in range(n)],dtype=np.int16);rng.shuffle(sizes)
        sample_positions=set(int(i) for i in np.random.default_rng(SEED+1).choice(docs,40,replace=False))
        tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');pools={};totals={};selected_hashes={}
        for arm in chosen:
            directory=DATA/arm;directory.mkdir(exist_ok=True);position=Counter();stats=Counter();samples=[];hashes=set()
            with (directory/'train.partial.bin').open('wb') as stream,(directory/'train.index.partial.jsonl').open('w') as index:
                for number,length in enumerate(sizes):
                    check();size=int(length);record=chosen[arm][size][position[size]];position[size]+=1
                    start=record['offset'];ids=view.tokens[start:start+size+2]
                    assert len(ids)==size+2 and ids[0]==2 and ids[-1]==3 and record['text_sha256'] not in hashes
                    hashes.add(record['text_sha256']);stream.write(ids.tobytes())
                    entry=dict(record,source_offset=start,offset=stats['tokens'],slot=number,source_manifest_sha256=binding['source_manifest_sha256'])
                    index.write(json.dumps(entry,ensure_ascii=False)+'\n');stats.update(tokens=size+2,documents=1,body_bytes=record['bytes'])
                    if number in sample_positions:samples.append(dict(entry,text=tok.decode_bytes(ids[1:-1].tolist()).decode('utf-8').strip()))
                stream.flush();index.flush();os.fsync(stream.fileno());os.fsync(index.fileno())
            os.replace(directory/'train.partial.bin',directory/'train.bin');os.replace(directory/'train.index.partial.jsonl',directory/'train.index.jsonl')
            shutil.copyfile(SOURCE/'token_bytes.json',directory/'token_bytes.json')
            manifest=dict(version=1,dtype='<u2',kind='web',vocab_size=4096,tokenizer_sha256=sha256(ROOT/'artifacts/phase2/4096/tokenizer.model'),
                token_bytes_sha256=sha256(directory/'token_bytes.json'),binding=binding,arm=arm,
                packing='BOS/whole original translation/EOS; paired arms identical lengths and BOS/EOS positions',
                splits={'train':dict(stats,stream_sha256=sha256(directory/'train.bin'),index_sha256=sha256(directory/'train.index.jsonl'),index_format='jsonl')})
            write_json(directory/'manifest.json',manifest);write_json(directory/'samples.json',dict(seed=SEED+1,method='uniform40 document slots; paired identical lengths; no reroll',rows=samples))
            pools[arm]=dict(pool=str(directory),manifest_sha256=sha256(directory/'manifest.json'));totals[arm]=dict(stats);selected_hashes[arm]=hashes
            heartbeat(arm+'-saved',tokens=stats['tokens'])
        mean=sum(s*n for s,n in quota.items())/docs
        ready=dict(status='ready_pending_content_review',binding=binding,pools=pools,totals=totals,supply=supply,
            body_tokens_mean=mean,body_length_quantiles=np.quantile(sizes,[0,.25,.5,.75,1]).tolist(),EOS_per_1000_tokens=1000*docs/amount,
            matched_quantity_length_sequence_EOS_positions=True,source_train_only=True,whole_original_stories=True,
            official_validation_test_acquired=False,common_base_selection_and_holdout_preserved=True,
            control_candidate_shared_documents=len(selected_hashes['control']&selected_hashes['refined']),
            interpretation='Same-source heuristic subset contrast; action ending/topic/dialogue composition also changes; not a semantic-quality causal certificate',
            independent_full_corpus_audit=False,independent_human_blind=False,seconds=earlier+time.monotonic()-started)
        assert totals['control']['tokens']==totals['refined']['tokens']==amount
        write_json(DATA/'ready.json',ready);heartbeat('complete',tokens_per_pool=amount);job.update(status='complete',completed_at=now())
    except BaseException as error:job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:job['elapsed_seconds']=earlier+time.monotonic()-started;atomic_json(job_path,job)

if __name__=='__main__':main()
