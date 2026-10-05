"""Equal whole-story token-length sequences, EOS positions, quantity and exposure."""
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
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from jmicro.story_quality import improved_story
from jmicro.complete_units import unit_hash
from phase6_performance import identity,alive
import prepare_complete_units as decode
from prepare_complete_document_pool import limited_batches

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/matched-story-content-20261005')
TARGET=25_000_000
MINIMUM=20_000_000
SEED=20261005


def worker_batch(task):
    _,batch=task;rows=[]
    for a,b in batch:
        ids=decode._TRAIN[a+1:b].tolist()
        text=b''.join(decode._PIECES[i] for i in ids).decode('utf-8').strip()
        rows.append((a,b,bool(improved_story(text,len(ids)))))
    return rows


def matched_quotas(original,eligible,target=TARGET):
    capacity=sum((size+2)*count for size,count in eligible.items())
    wanted=min(target,capacity)
    def quotas(ratio):return {size:min(eligible.get(size,0),int(np.ceil(count*ratio))) for size,count in original.items()}
    low,high=0.,1.
    for _ in range(48):
        middle=(low+high)/2
        if sum((s+2)*n for s,n in quotas(middle).items())<wanted:low=middle
        else:high=middle
    result=quotas(high)
    assert all(result[s]<=eligible.get(s,0) and result[s]<=original[s] for s in result)
    return result


def main():
    assert sys.version_info[:3]==(3,12,7)
    old=read_json(ROOT/'configs/phase6/story20_low_lr_10b_500m.json');source=old['pool']
    binding=dict(source=source,target_tokens=TARGET,minimum_tokens=MINIMUM,seed=SEED,
                 builder_sha256=sha256(Path(__file__)),selector_sha256=sha256(ROOT/'src/jmicro/story_quality.py'))
    DATA.mkdir(parents=True,exist_ok=True);path=DATA/'job.json';prior=read_json(path) if path.exists() else {}
    if prior:
        assert prior['binding']==binding and not alive(prior)
        if prior['status']=='complete':print(json.dumps(read_json(DATA/'ready.json')));return
        raise RuntimeError('Failed preparation retained; inspect actual cause before another attempt')
    started=time.monotonic();job=dict(status='running',**identity(),binding=binding,started_at=now());counts=Counter()
    def check():
        if time.monotonic()-started>1800:raise TimeoutError('Bounded matched preparation exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,elapsed_seconds=time.monotonic()-started,heartbeat_at=now(),counts=dict(counts),**extra);atomic_json(path,job)
        print(json.dumps(dict(stage=stage,seconds=job['elapsed_seconds'],**extra)),flush=True)
    try:
        heartbeat('setup');view=TrainView(source['pool'],source['manifest_sha256'],check_stream=True)
        for name in ('scripts/prepare_matched_story_pools.py','src/jmicro/story_quality.py'):
            target=DATA/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        original=defaultdict(list);eligible=defaultdict(list);last=0
        with mp.get_context('fork').Pool(12,initializer=decode.worker_init,initargs=(str(ROOT/old['tokenizer']),str(view.directory/'train.bin'))) as workers:
            for rows in workers.imap(worker_batch,limited_batches(view,'story',check,counts),chunksize=1):
                for a,b,good in rows:
                    size=b-a-1;original[size].append((a,b))
                    if good:eligible[size].append((a,b))
                if time.monotonic()-last>10:heartbeat('classify',classified=sum(map(len,original.values())),eligible=sum(map(len,eligible.values())));last=time.monotonic()
        old_hist={s:len(rows) for s,rows in original.items()};good_hist={s:len(rows) for s,rows in eligible.items()}
        quota=matched_quotas(old_hist,good_hist);amount=sum((s+2)*n for s,n in quota.items());docs=sum(quota.values())
        old_mean=sum(s*n for s,n in old_hist.items())/sum(old_hist.values());mean=sum(s*n for s,n in quota.items())/docs
        assert amount>=MINIMUM and abs(mean/old_mean-1)<=.05,(amount,mean,old_mean)
        rng=np.random.default_rng(SEED);chosen={a:{} for a in ('control','refined')}
        for size,n in sorted(quota.items()):
            if not n:continue
            for arm,population in (('control',original[size]),('refined',eligible[size])):
                chosen[arm][size]=[population[int(i)] for i in rng.choice(len(population),size=n,replace=False)]
        sizes=np.asarray([s for s,n in sorted(quota.items()) for _ in range(n)],dtype=np.int16);rng.shuffle(sizes)
        sample_positions=set(int(i) for i in np.random.default_rng(SEED+1).choice(docs,size=40,replace=False));totals={};pools={}
        tok=Tokenizer(ROOT/old['tokenizer'])
        for arm in chosen:
            output=DATA/arm;output.mkdir(exist_ok=True);stats=Counter();samples=[];position=Counter()
            with (output/'train.partial.bin').open('wb') as stream,(output/'train.index.partial.jsonl').open('w') as index:
                for number,length in enumerate(sizes):
                    size=int(length);a,b=chosen[arm][size][position[size]];position[size]+=1
                    ids=view.tokens[a:b+1];assert ids[0]==2 and ids[-1]==3 and len(ids)==size+2
                    stream.write(ids.tobytes());record=dict(source_start=a,source_end=b,offset=stats['tokens'],body_tokens=size,split='train',source='public_story_train',slot=number)
                    index.write(json.dumps(record)+'\n');stats.update(tokens=len(ids),documents=1)
                    if number in sample_positions:
                        text=tok.decode_bytes(ids[1:-1].tolist()).decode('utf-8').strip()
                        samples.append(dict(record,text=text,text_sha256=unit_hash(text)))
                    if number%50000==0:heartbeat(arm+'-write',documents=number)
                stream.flush();index.flush();os.fsync(stream.fileno());os.fsync(index.fileno())
            os.replace(output/'train.partial.bin',output/'train.bin');os.replace(output/'train.index.partial.jsonl',output/'train.index.jsonl')
            shutil.copyfile(view.directory/'token_bytes.json',output/'token_bytes.json')
            manifest=dict(version=1,dtype='<u2',kind='web',vocab_size=4096,tokenizer_sha256=old['tokenizer_sha256'],
                          token_bytes_sha256=sha256(output/'token_bytes.json'),binding=binding,arm=arm,
                          packing='BOS/original whole story/EOS; both arms identical length sequence and EOS/BOS positions',
                          splits={'train':dict(stats,stream_sha256=sha256(output/'train.bin'),index_sha256=sha256(output/'train.index.jsonl'),index_format='jsonl')})
            write_json(output/'manifest.json',manifest);write_json(output/'samples.json',dict(seed=SEED+1,method='uniform40 document slots; same slots and lengths across arms',rows=samples))
            pools[arm]=dict(pool=str(output),manifest_sha256=sha256(output/'manifest.json'));totals[arm]=dict(stats)
        assert totals['control']==totals['refined'] and totals['control']['tokens']==amount
        ready=dict(status='ready_pending_content_inspection',binding=binding,pools=pools,totals=totals,old_histogram=old_hist,
                   eligible_histogram=good_hist,matched_histogram=quota,body_tokens_mean=mean,old_body_tokens_mean=old_mean,
                   EOS_per_1000_tokens=1000*docs/amount,expected500M_exposure=99975168/amount,
                   matched_quantity_length_sequence_EOS_positions=True,source_train_only=True,whole_original_stories=True,
                   new_independent_unique_data=False,semantic_quality='Heuristic and sampled diagnosis only; independent certification absent',
                   control_candidate_overlap='Allowed; subset selection contrast, not independent-corpus comparison',seconds=time.monotonic()-started)
        write_json(DATA/'ready.json',ready);heartbeat('complete',tokens_per_pool=amount);job.update(status='complete',completed_at=now())
        print(json.dumps(ready),flush=True)
    except BaseException as error:job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:job['elapsed_seconds']=time.monotonic()-started;atomic_json(path,job)


if __name__=='__main__':main()
