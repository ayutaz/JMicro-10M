"""Prepare anonymized generation review and audit the bounded three-arm experiment."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import random
import sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.japanese_evaluation import repetition_metrics,clustered_ci
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive,finite_state
from inspect_complete_text_data import sample_documents
from run_complete_text_comparison import RUN,PLAN,POOL

RUBRIC=dict(grammar='0: broken syntax; 1: partial/awkward; 2: locally natural Japanese. Cap-ending byte fragment alone is not grammar0.',
            relevance='0: loses subject/condition/topic; 1: partial fit; 2: preserves supplied prefix and conditions.',
            coherence='0: strong loops/contradiction/incoherent development; 1: partly sensible but redundant or weak; 2: coherent meaningful development.',
            completion='0: not an appropriate learned content ending; 1: natural EOS with meaningful topic-relevant completion. Cap ending is0.',
            reviewer='single Codex diagnostic, not independent human quality certification')


def sample_pool():
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    rows=sample_documents(TrainView(POOL,sha256(POOL/'manifest.json')),tok,100,20261004)
    write_json(RUN/'data-inspection/stories.json',rows)
    print('\n'.join(json.dumps(dict(id=i,text=r['text']),ensure_ascii=False) for i,r in enumerate(rows)))


def packet():
    rows=[]
    for arm in ('web','short20','coherent20'):
        path=RUN/arm/'evaluation/generation.json'
        source=read_json(path)
        assert len(source['outputs'])==80
        for r in source['outputs']: rows.append(dict(r,arm=arm,source_sha256=sha256(path)))
    random.Random(20261004).shuffle(rows)
    mapping,anonymous={},[]
    for i,row in enumerate(rows):
        review_id=f'ct-{i:03d}'
        mapping[review_id]=dict(arm=row['arm'],id=row['id'],source_sha256=row['source_sha256'])
        anonymous.append({**{k:v for k,v in row.items() if k not in ('arm','source_sha256','binding')},'review_id':review_id})
    write_json(RUN/'content-mapping.json',mapping)
    write_json(RUN/'content-packet.json',dict(rubric=RUBRIC,rows=anonymous,
                independence='model names removed; Codex can access other experiment artifacts, not independent blind review'))
    print('Prepared240 anonymous texts; original raw outputs unchanged')


def finalize(annotation_path):
    plan=read_json(PLAN); result=read_json(RUN/'result.json')
    packet=read_json(RUN/'content-packet.json'); mapping=read_json(RUN/'content-mapping.json')
    annotations=read_json(annotation_path)
    assert annotations['packet_sha256']==sha256(RUN/'content-packet.json')
    scores={r[0]:r for r in annotations['scores']}
    assert len(scores)==len(annotations['scores'])==240 and set(scores)==set(mapping)
    rows=[]
    for text in packet['rows']:
        _,grammar,relevance,coherence,completion,note=scores[text['review_id']]
        assert all(v in (0,1,2) for v in (grammar,relevance,coherence)) and completion in (0,1) and note
        assert not completion or text['stop_reason']=='stop_id'
        rows.append(dict(text,**mapping[text['review_id']],grammar=grammar,relevance=relevance,coherence=coherence,
                         completion=completion,rationale=note,repetition_details=repetition_metrics(text)))
    summaries={}
    for arm in plan['arms']:
        group=[r for r in rows if r['arm']==arm]
        summaries[arm]=dict(count=len(group),**{key+'_score2':sum(r[key]==2 for r in group) for key in ('grammar','relevance','coherence')},
            appropriate_EOS=sum(r['completion'] for r in group),
            character4_repeat_mean=float(np.mean([r['repetition_details']['char_4gram_repeat'] for r in group])))
    checks={}
    control={r['id']:r for r in rows if r['arm']=='web'}
    rng=np.random.default_rng(42)
    for arm in ('short20','coherent20'):
        candidate={r['id']:r for r in rows if r['arm']==arm}
        assert set(candidate)==set(control) and len(candidate)==80
        difference=np.array([int(candidate[k]['coherence']==2)-int(control[k]['coherence']==2) for k in control])
        interval=np.quantile(difference[rng.integers(0,80,size=(2000,80))].mean(axis=1),[.025,.975]).tolist()
        frozen=result['mixture_checks'][arm]
        checks[arm]=dict(original_mixture_checks=frozen,coherence_gain_at_least8=int(difference.sum())>=8,
            paired_coherence_CI_lower_above0=interval[0]>0,coherence_difference_count=int(difference.sum()),paired_CI95=interval)
        checks[arm]['eligible_for_conditional_full']=all(frozen.values()) and checks[arm]['coherence_gain_at_least8'] and checks[arm]['paired_coherence_CI_lower_above0']
    write_json(RUN/'content-review.json',dict(rubric=RUBRIC,packet_sha256=annotations['packet_sha256'],rows=rows,
        summary=summaries,checks=checks,independent_human_blind='not performed',quality_targets_unchanged=True))
    evidence={}
    import xml.etree.ElementTree as ET
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    evidence['relevant_CPU_tests_pass']=sum(int(s.attrib.get('tests',0)) for s in suites)>=36 and not any(int(s.attrib.get(k,0)) for s in suites for k in ('failures','errors','skipped'))
    evidence['data_pool_25M_to_50M']=25_000_000<=read_json(POOL/'ready.json')['totals']['tokens']<=50_000_000
    evidence['data_inspection_100_each']=all(read_json(RUN/'data-inspection/result.json')['sources'][a]['count']==100 for a in ('web','short'))
    evidence['EOS_BOS_packing_checks']=all(read_json(RUN/'data-inspection/result.json')['boundary_checks'].values())
    evidence['actual_CUDA_exact_resume']=result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values())
    evidence['GPU_within_frozen_budget']=result['GPU_seconds']<=plan['gpu_budget_seconds']
    evidence['scientific_total_tokens']=result['scientific_training_input_tokens']==300023808
    evidence['verification_tokens_separate']=result['verification_training_input_tokens']==262144
    evidence['original_suite_and_protected_test']=plan['suite_sha256']==sha256(ROOT/'eval/base.jsonl') and not result['protected_test_used']
    evidence['all240_content_reviewed']=len(rows)==240
    for arm in plan['arms']:
        trained=result['arms'][arm]
        checkpoint=Path(trained['checkpoint'])
        state=torch.load(checkpoint,map_location='cpu',weights_only=False)
        history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        evidence[arm+'_checkpoint_and_binding']=sha256(checkpoint)==trained['checkpoint_sha256'] and state['pilot_binding']==trained['binding']
        evidence[arm+'_finite_model_optimizer']=finite_state(state)
        evidence[arm+'_matched_budget']=state['tokens']==10100015104 and state['update']==308228 and len(history)==3052 and [r['update'] for r in history]==list(range(305177,308229))
        evidence[arm+'_finite_loss_gradient']=all(np.isfinite(r['loss']) and np.isfinite(r['gradient_norm']) for r in history)
        expected_short=plan['arms'][arm]['short_updates']*32768
        evidence[arm+'_source_accounting_no_short_epoch']=state['sampler']['position']==3052 and state['sampler']['source_tokens']=={'web':100007936-expected_short,'short':expected_short} and state['sampler']['short']['epoch']==0
        evidence[arm+'_saved_resume_state']=all(k in state for k in ('model','optimizer','scheduler','rng','sampler','token_digest','lineage','tokens','supervised_tokens'))
        ev=read_json(RUN/arm/'evaluation/result.json')
        evidence[arm+'_evaluation_binding']=ev['checkpoint_sha256']==trained['checkpoint_sha256'] and ev['evaluation_RNG_isolated']
        evidence[arm+'_complete_diagnostics']=all(ev['diagnostics'][name]['complete'] for name in ('semantics','jblimp','jcqa')) and ev['diagnostics']['semantic_both_contexts']['total']==96
        del state
    job=read_json(RUN/'job.json')
    evidence['GPU_job_terminal_and_actual_process_exited']=job['status']=='complete' and not alive(job)
    review=dict(status='passed' if all(evidence.values()) else 'failed',checked_at=now(),checks=evidence,
        summaries=summaries,candidate_checks=checks,protected_test_used=False,
        completion_scope='stages1–3 only; experiment completion is separate from model adoption',
        full_evaluation_needed=any(c['eligible_for_conditional_full'] for c in checks.values()))
    write_json(RUN/'review.json',review)
    assert all(evidence.values()),{k:v for k,v in evidence.items() if not v}
    print(json.dumps(review,ensure_ascii=False,indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--sample-pool',action='store_true')
    parser.add_argument('--packet',action='store_true')
    parser.add_argument('--annotations',type=Path)
    parser.add_argument('--start',type=int,default=0)
    parser.add_argument('--count',type=int,default=30)
    args=parser.parse_args()
    if args.sample_pool: sample_pool()
    elif args.packet: packet()
    elif args.annotations: finalize(args.annotations)
    else:
        for row in read_json(RUN/'content-packet.json')['rows'][args.start:args.start+args.count]:
            print(json.dumps({k:row[k] for k in ('review_id','category','prefix','text','stop_reason')},ensure_ascii=False))
