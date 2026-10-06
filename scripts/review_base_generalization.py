"""Readonly evidence and predefined memorization/domain diagnostic flags."""
import hashlib
import json
import math
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive
from base_generalization_diagnostic import summarize
from record_base_generalization_content import validate_notes
from diagnose_base_preference import BLOCKED,repeat_marker
import diagnose_base_generalization as study


def main():
    c=study.inspect();r=read_json(study.RUN/'result.json');job=read_json(study.RUN/'job.json');cases=read_json(Path(c['cases']['path']));tok=Tokenizer(Path(c['tokenizer']['path']))
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
            or r['config_sha256']!=sha256(study.CONFIG) or set(r['arms'])!=set(study.ARMS)
            or r['optimizer_updates'] or r['scientific_teacher_tokens']):raise ValueError('Actually terminal bounded four-endpoint readonly diagnostic required')
    summaries={};scored={};raw_rows={}
    for arm in study.ARMS:
        v=r['arms'][arm]
        if (v['checkpoint']!=c['parents'][arm] or v['config_sha256']!=sha256(study.CONFIG) or not all(v['readonly_checks'].values())
                or v['optimizer_updates'] or v['scientific_teacher_tokens']):raise ValueError('Actual readonly checkpoint evidence differs')
        for split in ('train','dev'):
            part=v['scores'][split]
            if (len(part['rows'])!=len(cases[split]) or part['summary']!=summarize(part['rows'])
                    or [(row['id'],row['body_tokens'],row['body_bytes'],row['completion_teacher_tokens']) for row in part['rows']]
                       !=[(row['id'],row['chosen_body_tokens'],row['chosen_body_bytes'],len(row['chosen_ids'])) for row in cases[split]]
                    or any(not math.isfinite(row[k]) for row in part['rows'] for k in ('completion_nll','body_nll','EOS_nll'))):
                raise ValueError('All exact common-byte completion score rows required')
        study.check_reference(v['generation']);raw=Path(v['generation']['path']);generation=read_json(raw);rows=generation['outputs']
        if (generation['config_sha256']!=sha256(study.CONFIG) or generation['checkpoint']!=c['parents'][arm]
                or [(row['id'],row['prefix']) for row in rows]!=[(row['id'],row['prefix']) for row in cases['dev'][:16]]):
            raise ValueError('All same original DEV16 greedy cases required')
        for row in rows:
            ids=row['generated_ids'];body=tok.decode_bytes([v for v in ids if v!=3])
            try:body.decode('utf-8');valid=True
            except UnicodeDecodeError:valid=False
            if (not 1<=len(ids)<=64 or any(v in BLOCKED for v in ids) or row['split']!='dev' or row['raw_bytes_hex']!=body.hex()
                    or row['text']!=body.decode('utf-8',errors='replace') or row['valid_UTF8']!=valid
                    or row['stop_reason']!=('stop_id' if ids[-1]==3 else 'max_new_tokens') or 3 in ids[:-1]
                    or any(row[k]!=v for k,v in repeat_marker(ids).items())):raise ValueError('Actual unchanged native decoder/raw bytes required')
        notes=read_json(study.RUN/arm/'content-notes.json');scores=validate_notes(rows,notes,sha256(raw))
        if notes['raw_row_sha256']!={row['id']:hashlib.sha256(json.dumps(row,sort_keys=True,ensure_ascii=False).encode()).hexdigest() for row in rows}:
            raise ValueError('Every original row signature required')
        summaries[arm]=dict(train=v['scores']['train']['summary'],dev=v['scores']['dev']['summary'],
            grammar2=sum(s['grammar']==2 for s in scores.values()),relevance2=sum(s['relevance']==2 for s in scores.values()),
            coherent=sum(s['coherence']==2 for s in scores.values()),appropriate=sum(s['completion'] for s in scores.values()),
            EOS=sum(row['stop_reason']=='stop_id' for row in rows),heavy_repeat_at_least8=sum(row['repeated4gram_positions']>=8 for row in rows),
            repeated4gram_any=sum(row['repeated4gram_positions']>0 for row in rows),Unicode_failures=sum(not row['valid_UTF8'] for row in rows),
            notes=study.reference(study.RUN/arm/'content-notes.json'))
        scored[arm]=scores;raw_rows[arm]=rows
    flags={};paired={};baseline=summaries['actual_shared_Web6M'];rng=np.random.default_rng(42)
    indices=rng.integers(0,64,size=(2000,64))
    parent=r['arms']['actual_shared_Web6M']['scores']['dev']['rows'];den=np.array([v['body_bytes'] for v in parent]);parent_nll=np.array([v['body_nll'] for v in parent])
    old_review=read_json(Path(c['references']['previous_review']['path']))
    for arm,key in (('chosen_CE_terminal','chosen_CE'),('chosen_CE_DPO_terminal','chosen_CE_DPO')):
        s=summaries[arm];broad=old_review['summaries'][key];delta=np.array([v['body_nll'] for v in r['arms'][arm]['scores']['dev']['rows']])-parent_nll
        ci=np.quantile(delta[indices].sum(-1)/math.log(2)/den[indices].sum(-1),[.025,.975]).tolist()
        flags[arm]=dict(memorization_signal=s['train']['completion_CE_nats']<=baseline['train']['completion_CE_nats']*.5 and s['dev']['body_BPB']>=baseline['dev']['body_BPB'],
            domain_specialization_signal=s['dev']['body_BPB']<=baseline['dev']['body_BPB']*.99 and s['coherent']>=baseline['coherent']+4 and broad['coherent'] in (4,6))
        paired[arm]=dict(DEV_body_BPB_difference=s['dev']['body_BPB']-baseline['dev']['body_BPB'],paired_byte_weighted_CI95=ci,
            train_CE_ratio=s['train']['completion_CE_nats']/baseline['train']['completion_CE_nats'],DEV_coherent_difference=s['coherent']-baseline['coherent'],existing_broad_Base80=broad)
    report=dict(status='source_local_generalization_all64_content_reviewed',created_at=now(),config_sha256=sha256(study.CONFIG),
        result=study.reference(study.RUN/'result.json'),summaries=summaries,diagnostic_flags=flags,paired_comparisons=paired,
        all64_individually_read=True,independent_human_blind=False,DEV_count=64,greedy_count_per_arm=16,
        GPU_seconds=r['GPU_seconds'],optimizer_updates=0,scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        counts=c['counts'],DEV_exact_text_overlap_with_selected56=c['DEV_exact_text_overlap_with_selected56'],DEV_exact_text_overlap_with_news5050=c['DEV_exact_text_overlap_with_news5050'],
        limitations=c['limitations'],next_action='End this readonly diagnostic. Preserve failed fixed recipes and old gates. Use observed TRAIN/DEV transfer evidence to define a genuinely new bounded training mechanism; no source/coefficient/epoch/LR/checkpoint rescue.')
    destination=study.RUN/'review.json'
    if destination.exists():raise ValueError('Preserve original source-local diagnosis')
    atomic_json(destination,report);atomic_json(ROOT/'reports/phase6/base_generalization_diagnostic_review.json',report)
    print(dict(summaries=summaries,diagnostic_flags=flags))


if __name__=='__main__':main()
