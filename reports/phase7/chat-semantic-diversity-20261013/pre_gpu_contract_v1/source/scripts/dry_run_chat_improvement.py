"""Actual CPU sampler consumption and decay; no model forward or GPU use."""
from collections import Counter
import json
import math
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.chat_curriculum import WEIGHTS
from jmicro.experiment import ROOT,now,sha256
from jmicro.teacher_chat_training import TeacherBudgetSampler,teacher_lr
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json

RUN=ROOT/'reports/phase7/chat-improvement-20261012'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
RPC=Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
B=1899555

def consume(path,tok):
    records=[json.loads(l) for l in path.read_text().splitlines()]
    sampler=TeacherBudgetSampler(records,tok,1024,42,B,512,32)
    metadata={r['doc_id']:r for r in records};exposure=Counter();category=Counter();hist=Counter();logdecay=0.;rows=[]
    while sampler.teacher_tokens<B:
        position=sampler.position;epoch=sampler.epoch;before=sampler.teacher_tokens
        batches,n,_=sampler.next_update()
        assert n==sum(int(y.ne(-100).sum()) for _,y in batches)
        # Reconstruct precisely the same consumed order, including epoch edges.
        first=position;last=sampler.position
        segments=[]
        if sampler.epoch!=epoch:
            import numpy as np
            previous=np.random.default_rng(np.random.SeedSequence([42,epoch])).permutation(len(sampler.windows))
            segments.append(previous[first:]);first=0
        segments.append(sampler.order[first:last])
        for segment in segments:
            for index in segment:
                w=sampler.windows[int(index)];labels=w['labels'];length=int((labels!=-100).sum())
                exposure[(w['doc_id'],w['target_message_index'])]+=1
                category[metadata[w['doc_id']].get('category','original_RPC')]+=length
                hist[next(i for i,(lo,hi) in enumerate(((2,8),(9,16),(17,32),(33,65))) if lo<=length<=hi)]+=1
        lr=teacher_lr(before,n,B);logdecay+=math.log1p(-lr*.01)
        rows.append(dict(update=len(rows)+1,teachers=n,lr=lr,microbatches=len(batches)))
    assert sum(category.values())==sampler.teacher_tokens and sum(exposure.values())==sampler.examples
    return dict(source_sha256=sha256(path),sampler_binding=sampler.binding,windows=len(sampler.windows),updates=len(rows),
        Assistant_teachers=sampler.teacher_tokens,EOT_teachers=sampler.eot_teachers,EOT_fraction=sampler.eot_teachers/sampler.teacher_tokens,
        final_overshoot=sampler.teacher_tokens-B,valid_inputs=sampler.input_tokens,physical_inputs=sampler.physical_tokens,
        consumed_teacher_fractions={k:v/sampler.teacher_tokens for k,v in category.items()},
        length_bins=[hist[i] for i in range(4)],length_bin_fractions=[hist[i]/sampler.examples for i in range(4)],
        max_target_exposures=max(exposure.values()),decay_coefficient=math.exp(logdecay),
        log_decay=logdecay,microbatches=sum(r['microbatches'] for r in rows),rows=rows,
        sampler_terminal=sampler.state_dict())

def main():
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    train_path=DATA/('train.jsonl' if (DATA/'manifest.json').exists() else 'candidate.train.jsonl')
    c0=consume(RPC/'train.jsonl',tok);c1=consume(train_path,tok)
    countdiff=abs(c1['updates']/c0['updates']-1)
    decaydiff=abs(c1['decay_coefficient']/c0['decay_coefficient']-1)
    tv=sum(abs(a-b) for a,b in zip(c0['length_bin_fractions'],c1['length_bin_fractions']))/2
    eotdiff=abs(c1['EOT_fraction']-c0['EOT_fraction'])
    mixture_diff=max(abs(c1['consumed_teacher_fractions'][k]-w) for k,w in WEIGHTS.items())
    checks=dict(updates_relative_difference=countdiff<=.05,decay_relative_difference=decaydiff<=.001,
        actual_teacher_mixture=mixture_diff<=.01,actual_length_TV=tv<=.10,actual_EOT_match=eotdiff<=.01,
        final_whole_target_overshoot=all(0<=x['final_overshoot']<=64 for x in (c0,c1)),
        target_exposure_at_most_three=all(x['max_target_exposures']<=3 for x in (c0,c1)))
    for name,arm in (('C0',c0),('C1',c1)):
        atomic_json(RUN/f'{name}_dry_run.json',arm)
    report=dict(created_at=now(),status='passed' if all(checks.values()) else 'redesign_required',checks=checks,
        update_relative_difference=countdiff,decay_relative_difference=decaydiff,length_TV=tv,
        EOT_absolute_difference=eotdiff,mixture_max_absolute_difference=mixture_diff,
        C0={k:v for k,v in c0.items() if k not in ('rows','sampler_terminal')},
        C1={k:v for k,v in c1.items() if k not in ('rows','sampler_terminal')},
        GPU_learning_tokens=0,CPU_only=True,quality_evidence=False,new_DEV_used=False)
    atomic_json(RUN/'consumption_dry_run.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
