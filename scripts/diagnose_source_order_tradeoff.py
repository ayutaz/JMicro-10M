"""Read existing paired dev losses only; no model/data loading or rescoring."""
import json
import math
from pathlib import Path
import statistics
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive

PROPOSAL=ROOT/'reports/phase6/source_order_followup_diagnostic_proposal.json'
OUTPUT=ROOT/'reports/phase6/source_order_followup_diagnostic.json'


def pair_bodies(control,new):
    if control['split']!='dev' or new['split']!='dev':raise ValueError('Dev only')
    a,b=control['rows'],new['rows']
    if len(a)!=len(b) or len({r['doc_id'] for r in a})!=len(a):raise ValueError('Complete unique pairs required')
    out=[]
    for x,y in zip(a,b,strict=True):
        if any(x[k]!=y[k] for k in ('doc_id','body_tokens','body_bytes','scored_body_tokens')):
            raise ValueError('Different paired targets')
        if (x['body_tokens']!=x['scored_body_tokens'] or x['body_tokens']<=0 or x['body_bytes']<=0
                or any(not math.isfinite(r[k]) or r[k]<0 for r in (x,y) for k in ('body_nll','eos_nll'))):
            raise ValueError('Complete finite scored body and EOS required')
        out.append(dict(doc_id=x['doc_id'],body_tokens=x['body_tokens'],body_bytes=x['body_bytes'],
            control_body_nll=x['body_nll'],new_body_nll=y['body_nll'],body_nll_delta=y['body_nll']-x['body_nll'],
            control_EOS_nll=x['eos_nll'],new_EOS_nll=y['eos_nll'],EOS_nll_delta=y['eos_nll']-x['eos_nll']))
    for body in (control,new):
        if (body['documents']!=len(body['rows']) or body['body_bytes']!=sum(r['body_bytes'] for r in body['rows'])
                or body['body_tokens']!=sum(r['body_tokens'] for r in body['rows'])
                or not math.isclose(body['body_nll'],sum(r['body_nll'] for r in body['rows']),abs_tol=1e-7)
                or not math.isclose(body['eos_nll'],sum(r['eos_nll'] for r in body['rows']),abs_tol=1e-7)
                or not math.isclose(body['bpb'],body['body_nll']/math.log(2)/body['body_bytes'],rel_tol=1e-12)):
            raise ValueError('Reported common-byte body totals differ')
    return out


def summarize(rows):
    def counts(key):
        return dict(improved=sum(r[key]<0 for r in rows),worsened=sum(r[key]>0 for r in rows),
                    unchanged=sum(r[key]==0 for r in rows))
    total_bytes=sum(r['body_bytes'] for r in rows)
    values={}
    for arm in ('control','new'):
        eos=[r[arm+'_EOS_nll'] for r in rows]
        values[arm]=dict(BPB=sum(r[arm+'_body_nll'] for r in rows)/math.log(2)/total_bytes,
            gold_EOS_mean_NLL=statistics.mean(eos),
            gold_EOS_arithmetic_mean_probability=statistics.mean(math.exp(-v) for v in eos))
    return dict(documents=len(rows),body_bytes=total_bytes,body_tokens=sum(r['body_tokens'] for r in rows),
        body_tokens_min=min(r['body_tokens'] for r in rows),body_tokens_max=max(r['body_tokens'] for r in rows),
        body_NLL_change=counts('body_nll_delta'),gold_EOS_NLL_change=counts('EOS_nll_delta'),
        body_worse_EOS_better=sum(r['body_nll_delta']>0 and r['EOS_nll_delta']<0 for r in rows),
        control=values['control'],new=values['new'])


def main():
    started=time.monotonic()
    if OUTPUT.exists():raise ValueError('Preserve completed diagnostic')
    p=read_json(PROPOSAL)
    if (p['CPU_budget_seconds']!=30 or p['GPU_budget_seconds'] or p['scientific_teacher_tokens']
            or not p['no_new_training'] or not p['no_threshold_change']):raise ValueError('Fixed CPU-only scope required')
    for ref in p['references'].values():
        if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Frozen reference changed')
    result_path=Path(p['references']['comparison']['path']);r=read_json(result_path)
    review=read_json(Path(p['references']['review']['path']));job=read_json(result_path.parent/'job.json')
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(result_path)
            or r['protected_test_used'] or r['Base_adopted']):raise ValueError('Completed rejected Base-dev evidence required')
    control,new=r['evaluations']['control'],r['evaluations']['source_order']
    pairs=pair_bodies(control['body'],new['body'])
    if len(pairs)!=256 or summarize(pairs)['body_bytes']!=472055:raise ValueError('All256 common-byte targets required')
    ordered=sorted(pairs,key=lambda row:(row['body_tokens'],row['doc_id']))
    quartiles=[dict(quartile=i+1,**summarize(ordered[i*64:(i+1)*64])) for i in range(4)]
    notes={}
    for arm,name in (('control','historical_parent_condition_notes.json'),('source_order','source_order_condition_notes.json')):
        path=ROOT/'reports/phase6'/name;n=read_json(path)
        rows=r['evaluations'][arm]['generation']['outputs']
        by_id={v[0]:v for v in n['notes']}
        if (len(rows)!=80 or len(by_id)!=80 or set(by_id)!={v['id'] for v in rows}
                or sha256(path)!=review['summaries'][arm]['notes_sha256']):raise ValueError('All80 existing notes required')
        notes[arm]=by_id
    changes=[dict(id=k,control=notes['control'][k][1:5],new=notes['source_order'][k][1:5]) for k in notes['control']]
    elapsed=time.monotonic()-started
    if elapsed>30:raise TimeoutError('CPU diagnostic budget exhausted')
    report=dict(status='all256_paired_body_goldEOS_and_existing80_notes_complete',created_at=now(),
        proposal=dict(path=str(PROPOSAL),sha256=sha256(PROPOSAL)),references=p['references'],
        source_sha256={v:sha256(ROOT/v) for v in ('scripts/diagnose_source_order_tradeoff.py','tests/test_source_order_tradeoff.py')},
        CPU_seconds=elapsed,GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,
        common_byte_summary=summarize(pairs),fixed_length_quartiles=quartiles,paired_documents=pairs,
        Japanese_changes={k:dict(control=review['summaries']['control']['Japanese'][k],new=review['summaries']['source_order']['Japanese'][k])
            for k in ('semantics','jblimp','jcqa')},existing_content_scores=review['summaries'],paired_existing_content_changes=changes,
        independent_human_blind=False,Base_adopted=False,Base_complete=False,Chat_started=False,quantization_started=False,
        protected_test_used=False,quality_criteria_unchanged=True,
        limitations='Gold EOS is teacher-forced at the true document end, not at generated early stops. EOS probability improvement does not prove appropriate completion. Quartiles are descriptive, not independent tests; existing nonblind content judgments are reused without rescoring. Source recency/forgetting remain hypotheses, not a unique mechanism.')
    atomic_json(OUTPUT,report)
    print(json.dumps(dict(summary=report['common_byte_summary'],quartiles=quartiles,CPU_seconds=elapsed)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
