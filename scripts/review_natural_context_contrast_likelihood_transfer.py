"""Validate all nine same-suffix sections and record paired byte-weighted effects."""
import json
import math
from pathlib import Path
import sys

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from run_natural_context_contrast_likelihood_transfer import RUN,CONFIG,VIEWS,tasks_for


def review():
    c,r,j=(read_json(p) for p in (CONFIG,RUN/'result.json',RUN/'job.json'))
    if (j['status']!='complete' or r['status']!='complete' or alive(j)
            or r['actual_identity']!={k:j[k] for k in ('pid','boot_id','start_ticks')}
            or r['config_sha256']!=sha256(CONFIG) or j['config_sha256']!=sha256(CONFIG)
            or not 0<r['GPU_occupancy_seconds']<=60 or r['GPU_occupancy_seconds']!=j['GPU_occupancy_seconds']
            or r['new_teacher_tokens'] or r['optimizer_updates']):
        raise ValueError('Actual bounded readonly terminal process required')
    for ref in (c['cases'],c['source_cases'],c['source_config'],c['proposal']):
        if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Frozen source differs')
    if any(sha256(ROOT/p)!=h for p,h in c['source_sha256'].items()):raise ValueError('Frozen scoring code differs')
    rows=read_json(Path(c['cases']['path']))['rows'];ids=[x['doc_id'] for x in rows]
    if len(ids)!=64 or len(set(ids))!=64 or set(r['results'])!={'original','CE','contrast'}:
        raise ValueError('All three models on exact64 paired suffixes required')
    values={};summaries={}
    expected_tasks={v:tasks_for(rows,v) for v in VIEWS}
    for arm,views in r['results'].items():
        if set(views)!=set(VIEWS):raise ValueError('All three context views required')
        values[arm]={};summaries[arm]={}
        for view,s in views.items():
            if (s['checkpoint']!=c['checkpoints'][arm] or s['input_cases_sha256']!=c['cases']['sha256']
                    or s['EOS_scored_positions'] or not s['EOS_in_vocabulary_normalization']
                    or s['context']!=1024 or s['target_stride']!=512 or [x['doc_id'] for x in s['rows']]!=ids):
                raise ValueError('Same checkpoint/input/mask/window contract required')
            for i,(case,score) in enumerate(zip(rows,s['rows'],strict=True)):
                tasks=[t for t in expected_tasks[view] if t['row']==i]
                if (score['body_tokens']!=len(case['suffix_ids']) or score['body_bytes']!=case['suffix_bytes']
                        or score['scored_tokens']!=score['body_tokens'] or len(score['windows'])!=len(tasks)):
                    raise ValueError('Every common suffix target/byte required')
                for task,window in zip(tasks,score['windows'],strict=True):
                    if any(window[k]!=task[k] for k in ('suffix_first','suffix_last','original_input_start','prefix_doc_id')):
                        raise ValueError('Exact original context and target positions required')
                    if (window['input_tokens']!=len(task['input_ids']) or window['scored_tokens']!=task['suffix_last']-task['suffix_first']
                            or not math.isfinite(window['nll']) or window['nll']<0):
                        raise ValueError('Finite complete original-window NLL required')
                if not math.isclose(score['nll'],sum(w['nll'] for w in score['windows']),abs_tol=1e-9):
                    raise ValueError('Actual window NLL sum differs')
            nll=sum(x['nll'] for x in s['rows']);byte_count=sum(x['suffix_bytes'] for x in rows)
            if (not math.isclose(nll,s['body_nll'],abs_tol=1e-9) or s['body_bytes']!=byte_count
                    or s['body_tokens']!=sum(len(x['suffix_ids']) for x in rows)
                    or not math.isclose(s['BPB'],nll/(byte_count*math.log(2)),abs_tol=1e-12)):
                raise ValueError('Common suffix-byte weighted BPB accounting differs')
            values[arm][view]=np.asarray([x['nll'] for x in s['rows']])
            summaries[arm][view]={k:s[k] for k in ('BPB','body_nll','body_bytes','body_tokens')}
    denominator=np.asarray([x['suffix_bytes'] for x in rows])*math.log(2)
    samples=np.random.default_rng(42).integers(0,64,size=(2000,64))
    def paired(delta):
        boot=delta[samples].sum(1)/denominator[samples].sum(1)
        return dict(point_BPB=float(delta.sum()/denominator.sum()),CI95_BPB=np.quantile(boot,[.025,.975]).tolist(),
            unit='64 paired documents, byte-weighted ratio',raw_delta_nll=dict(zip(ids,delta.tolist())))
    benefit={arm:{view+'_minus_matched':paired(v[view]-v['matched']) for view in ('cyclic','BOS_only')}
             for arm,v in values.items()}
    difference={}
    for control,candidate in (('original','CE'),('CE','contrast'),('original','contrast')):
        difference[candidate+'_minus_'+control]={view:paired(values[candidate][view]-values[control][view]) for view in VIEWS}
        difference[candidate+'_minus_'+control]['cyclic_context_benefit_change']=paired(
            (values[candidate]['cyclic']-values[candidate]['matched'])-(values[control]['cyclic']-values[control]['matched']))
    report=dict(status='all9_fixed_suffix_likelihood_sections_reviewed',created_at=now(),
        reviewer_sha256=sha256(Path(__file__)),result_sha256=sha256(RUN/'result.json'),config_sha256=sha256(CONFIG),
        actual_identity=r['actual_identity'],GPU_occupancy_seconds=r['GPU_occupancy_seconds'],
        summaries=summaries,prefix_benefit=benefit,paired_model_differences=difference,
        conclusion='All three models benefit from observed prefixes. Contrast improves embedding association but does not improve matched-suffix prediction relative to CE on this fixed64 packet; its context-benefit change is small. Do not equate retrieval with autoregressive accuracy or infer complete absence of context use.',
        new_teacher_tokens=0,optimizer_updates=0,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,one_shot_diagnostic_closed=True,
        limitations='Retrospective repeated DEV64, lexical/topic associations, unknown near-family dependencies and one learned seed. Three views share64 suffixes; bootstrap documents, not192 independent cases. Suffix-only BPB is not the historical full DEV guard. No factual-foil or free-generation quality is established.',
        next_action='Do not reopen failed CE/contrast or likelihood ranking by retuning. Audit whether input/output embedding coupling and a fixed10M parameter reallocation constitute an untested architecture mechanism before any training; existing tokenizer and architecture failures remain evidence, not reasons to automatically launch a sweep.')
    if (RUN/'review.json').exists():raise ValueError('Preserve original review')
    atomic_json(RUN/'review.json',report)
    atomic_json(ROOT/'reports/phase6/natural_context_contrast_likelihood_transfer_review.json',report)
    print(json.dumps(dict(summaries=summaries,contrast_minus_CE={v:{k:d[k] for k in ('point_BPB','CI95_BPB')}
        for v,d in difference['contrast_minus_CE'].items()})))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    review()
