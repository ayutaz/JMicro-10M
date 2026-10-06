"""Bind all64 actual source judgments; never turn generated prose into training."""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from phase6_performance import alive


def main(run,observations,output):
    job=read_json(run/'job.json');raw=read_json(run/'result.json');rows=raw['outputs']
    if job['status']!='complete' or alive(job) or len(rows)!=64 or raw['student_scientific_teacher_tokens'] or raw['optimizer_updates']:
        raise ValueError('Actual terminal teacher64 without student learning required')
    notes=[]
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=4:raise ValueError('Four fields per source observation required')
        name,weak,categories,reason=fields
        if weak not in ('0','1') or len(reason.strip())<12:raise ValueError('Explicit weak flag and individual rationale required')
        notes.append(dict(id=name,weak=bool(int(weak)),categories=categories.split('|'),rationale=reason))
    if len(notes)!=64 or len({n['id'] for n in notes})!=64 or {n['id'] for n in notes}!={r['id'] for r in rows}:
        raise ValueError('All64 raw source IDs require exactly one observation')
    keyed={n['id']:n for n in notes};counts=Counter(c for n in notes for c in n['categories'] if c!='none')
    if any(n['weak']!=(n['categories']!=['none']) for n in notes):raise ValueError('Weak flags/categories differ')
    for row in rows:
        if row['split']!='train':raise ValueError('Heldout source cannot be used')
        saved=read_json(run/'raw'/f'{row["id"]}.json')
        if saved!=row:raise ValueError('Raw individual teacher output changed')
        if row['teacher_stop']!='EOS' and not keyed[row['id']]['weak']:raise ValueError('Unfinished teacher cannot be retained')
    unresolved=sum('grammar' in n['categories'] and not n['weak'] for n in notes)
    weak=sum(n['weak'] for n in notes)
    generated_seconds=sum(r['seconds'] for r in raw['timings'])
    result=dict(status='actual_teacher64_content_review_complete',created_at=now(),run=str(run),
        result_sha256=sha256(run/'result.json'),observations=dict(path=str(observations),sha256=sha256(observations)),
        reviewer='Codex nonblind; all64 individually read',independent_human_blind=False,notes=notes,
        weak=weak,maximum_weak=10,unresolved_retained_grammar_errors=unresolved,categories=dict(counts),
        accepted=weak<=10 and unresolved==0,teacher_EOS_completed=raw['teacher_EOS_completed'],
        generated_student_body_tokens=raw['completed_student_body_tokens'],generated_teacher_tokens=raw['completed_teacher_generated_tokens'],
        inference_seconds=generated_seconds,GPU_seconds=raw['GPU_seconds'],peak_allocated_bytes=raw['peak_allocated_bytes'],
        raw_student_body_tokens_per_inference_second=raw['completed_student_body_tokens']/generated_seconds,
        extrapolated_raw10M_student_body_seconds=10_000_000*generated_seconds/raw['completed_student_body_tokens'],
        extrapolation='Raw batched8 inference timing only. Quality exclusions, packing, longer batches/contexts, loading, saving and synchronization can change throughput. No source10M has been prepared.',
        student_scientific_teacher_tokens=0,optimizer_updates=0,Chat_started=False,quantization_started=False,Base_adopted=False,protected_test_used=False,
        completion='Source quality feasibility only; accepted source pilot is not a trained or qualified student. Failed source must not enter student learning.')
    if output.exists():raise ValueError('Preserve completed source review')
    write_json(output,result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('notes','completion','extrapolation','observations')},ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python required')
    parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path,required=True);parser.add_argument('--observations',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    a=parser.parse_args();main(a.run,a.observations,a.output)
