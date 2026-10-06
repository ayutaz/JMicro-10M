"""Paired descriptive TRAIN loss by stage; no forward pass or rescue selection."""
import json
import math
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive

SOURCES=('web','story','ordinary_textbook','conditional_textbook')
CANDIDATE=ROOT/'reports/phase6/readout-adapter-comparison-v3-20261006'
CONTROL=ROOT/'reports/phase6/parameter-displacement-anchor-v3-20261006'
DESTINATION=ROOT/'reports/phase6/readout_source_stage_analysis.json'


def paired_stages(candidate,control):
    if not candidate or len(candidate)!=len(control):raise ValueError('All paired completed updates required')
    previous=dict.fromkeys(SOURCES,0);groups={g:[] for g in SOURCES};mixed=[]
    for index,(a,b) in enumerate(zip(candidate,control,strict=True)):
        for key in ('update','source_teachers','source_eos','source_input_tokens','source_body_bytes','token_digest','focus_token_digest'):
            if a[key]!=b[key]:raise ValueError('Same actual batch target/input/source required: '+key)
        if index and a['update']!=candidate[index-1]['update']+1:raise ValueError('Completed update gap')
        if any(not math.isfinite(row['CE_loss']) for row in (a,b)):raise ValueError('Finite actual CE required')
        delta={g:a['source_teachers'][g]-previous[g] for g in SOURCES}
        if any(n<0 for n in delta.values()) or sum(delta.values())<=0:raise ValueError('Monotonic positive teacher counts required')
        active=[g for g,n in delta.items() if n]
        record=dict(update=a['update'],teachers=sum(delta.values()),source_teachers=delta,
            candidate_CE=a['CE_loss'],control_CE=b['CE_loss'])
        (groups[active[0]] if len(active)==1 else mixed).append(record)
        previous=a['source_teachers'].copy()
    def summary(rows):
        if not rows:return dict(updates=0,teachers=0)
        def averages(part):
            teachers=sum(r['teachers'] for r in part)
            values={k:sum(r[k]*r['teachers'] for r in part)/teachers for k in ('candidate_CE','control_CE')}
            return dict(teachers=teachers,**values,difference=values['candidate_CE']-values['control_CE'])
        return dict(updates=len(rows),teachers=sum(r['teachers'] for r in rows),whole=averages(rows),
            first_at_most32=averages(rows[:32]),last_at_most32=averages(rows[-32:]))
    return dict(exclusive_source_stages={g:summary(rows) for g,rows in groups.items()},
        mixed_transition_batches=summary(mixed),total_updates=len(candidate),source_teachers=previous,
        total_teachers=sum(previous.values()),all_scientific_batches_paired=True)


def main():
    start=time.monotonic()
    if DESTINATION.exists():raise ValueError('Preserve original posthoc stage analysis')
    for folder in (CANDIDATE,CONTROL):
        job=read_json(folder/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('Actually terminal experiments required')
    paths=[CANDIDATE/'readout_adapter/training/metrics.jsonl',CONTROL/'matched_staged_CE/training/metrics.jsonl']
    rows=[[json.loads(line) for line in q.read_text().splitlines()] for q in paths]
    result=paired_stages(*rows)
    if result['total_teachers']!=100000000 or result['total_updates']!=3068:raise ValueError('Original completed100M contract required')
    for q in (CANDIDATE/'review.json',CONTROL/'review.json'):
        if read_json(q)['eligible_for_final_Base_validation']:raise ValueError('Preserve rejected comparison')
    seconds=time.monotonic()-start
    if seconds>30:raise TimeoutError('Read-only CPU30s stage analysis exhausted')
    report=dict(status='readout_source_stages_descriptively_analyzed',created_at=now(),**result,
        CPU_seconds=seconds,CPU_ceiling_seconds=30,GPU_seconds=0,new_teacher_tokens=0,
        references={str(q.relative_to(ROOT)):dict(path=str(q),sha256=sha256(q)) for q in (*paths,CANDIDATE/'review.json',CONTROL/'review.json')},
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        limitations='Posthoc observed training losses, same complete batches; fresh readout Adam vs inherited native Adam confounds architecture-only attribution. Mixed transition losses are not assigned to one source. Not dev quality, perplexity comparison across corpora, causal proof, or checkpoint selection.',
        next_action='End fixed nonlinear-readout recipe. Define a bounded genuinely authored Japanese news material pilot, fixed64 content review before any GPU learning; retain all current quality gates.')
    atomic_json(DESTINATION,report)
    print(json.dumps(dict(CPU_seconds=seconds,stages=report['exclusive_source_stages']),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
