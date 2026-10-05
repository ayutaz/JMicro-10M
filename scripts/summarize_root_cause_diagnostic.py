"""Bind portable diagnostic evidence; retain numerical failures and sample bias."""
import gzip
import hashlib
import json
from pathlib import Path
import statistics as st
import sys
import urllib.request

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes

P=ROOT/'reports/phase6'
R=P/'root-cause-20261005'


def main():
    contract=read_json(R/'contract.json');job=read_json(R/'job.json');precision=read_json(R/'precision-job.json')
    assert job['status']==precision['status']=='complete'
    assert job['gpu_job_seconds']+precision['gpu_job_seconds']<600
    assert job['scientific_training_tokens']==job['optimizer_updates']==0
    assert contract['implementation']==implementation_hashes()
    for n,d in contract['files'].items():assert sha256(R/n)==d
    cases=read_json(R/'cases.json');corpus=read_json(R/'corpus.json');notes=read_json(P/'root_cause_corpus_notes.json')
    assert len(cases)==32 and len(corpus)==len(notes)==128
    assert all(r['split']=='train' for r in cases+corpus)
    for row in corpus:
        assert hashlib.sha256(row['text'].encode()).hexdigest()==row['text_sha256']
        assert row['roundtrip'] and row['end_ids'][0]==3
    codec=read_json(R/'codec.json')
    assert all(r['lossless'] for v in codec.values() for r in v['samples'])
    model_summary={};raw={}
    for name,entry in contract['checkpoints'].items():
        assert sha256(Path(entry['path']))==entry['sha256']
        assert sha256(R/f'{name}.json')==job['result_sha256'][f'{name}.json']
        assert sha256(R/f'{name}-precision.json')==precision['result_sha256'][f'{name}-precision.json']
        result=read_json(R/f'{name}.json');pr=read_json(R/f'{name}-precision.json')
        assert len(result['teacher'])==len(pr['endings'])==len(pr['fp32_greedy'])==32
        assert set(result['generation'])=={'greedy','sampling-42','sampling-43','sampling-44'}
        assert all(len(rows)==32 for rows in result['generation'].values())
        teacher={x['id']:x for x in result['teacher']}
        for rows in result['generation'].values():
            assert {r['id'] for r in rows}=={r['id'] for r in cases}
            for r in rows:
                assert len(r['steps'])==len(r['generated_ids'])<=64
                assert (r['generated_ids'][-1]==3)==(r['stop_reason']=='eos')
                assert all(0<=s['eos_probability']<=1 and s['eos_rank']>=1 for s in r['steps'])
        groups={}
        for source in ['web','story200m','compact']:
            t=[x for x in result['teacher'] if x['source']==source]
            pe=[x for x in pr['endings'] if x['source']==source]
            def counts(rows):
                rows=[x for x in rows if x['source']==source]
                return dict(n=len(rows),eos=sum(x['stop_reason']=='eos' for x in rows),
                    repeated_4gram=sum(x['first_repeated_4gram'] is not None for x in rows),
                    exact_gold=sum(x.get('exact_gold',False) for x in rows),
                    interpretation='4gram marker is not old severity metric or semantic failure; exact gold is memorization, not sole natural generation gate')
            groups[source]=dict(n=len(t),teacher_eos_arithmetic_mean=st.mean(x['ending']['eos_probability'] for x in t),
                teacher_eos_median_rank=st.median(x['ending']['eos_rank'] for x in t),
                teacher_eos_top1=sum(x['ending']['eos_rank']==1 for x in t),
                teacher_top1_mean=st.mean(x['teacher_top1_fraction'] for x in t),
                fp32_teacher_eos_top1=sum(x['fp32']['eos_rank']==1 for x in pe),
                bf16_full_cache_eos_rank_changes=sum(x['bf16']['eos_rank']!=x['bf16_cached']['eos_rank'] for x in pe),
                generation={k:counts(rows) for k,rows in result['generation'].items()},fp32_greedy=counts(pr['fp32_greedy']),
                gold_longer_than64=sum(len(x['gold_ids'])>64 for x in cases if x['source']==source))
        examples=[]
        for i in [0,4,8,9,15,16,17]:
            g=result['generation']['greedy'][i]; t=teacher[g['id']]
            onset=g['first_repeated_4gram']
            examples.append(dict(id=g['id'],prefix=g['prefix'],text=g['text'],ending=t['ending'],
                previous_context_ending=t['previous_context_ending'],first_token_departure=g['first_token_departure'],
                first_distribution=g['steps'][0],last_distribution=g['steps'][-1],
                repetition=onset,distribution_at_repetition=g['steps'][onset['end_step']] if onset else None))
        model_summary[name]=dict(training_tokens=result['training_tokens'],update=result['update'],checkpoint=entry,groups=groups,
            mean_probability_total_variation=st.mean(x['mean_total_variation'] for x in pr['endings']),
            max_probability_total_variation=max(x['max_total_variation'] for x in pr['endings']),
            max_teacher_mean_nll_delta=max(abs(x['fp32_teacher_nll']-x['bf16_teacher_nll']) for x in pr['endings']),
            fp32_bf16_teacher_eos_top1_changes=sum((x['fp32']['eos_rank']==1)!=(x['bf16']['eos_rank']==1) for x in pr['endings']),
            greedy_exact_precision_agreement=sum(a['generated_ids']==b['generated_ids'] for a,b in zip(result['generation']['greedy'],pr['fp32_greedy'])),
            examples=examples)
        raw[f'{name}.json']=result;raw[f'{name}-precision.json']=pr
    # gzip stores exact original JSON bytes inside a single deterministic envelope.
    serialized={name:(R/name).read_text() for name in raw}
    payload=json.dumps(serialized,ensure_ascii=False,separators=(',',':')).encode()
    bundle=P/'root_cause_traces.json.gz'
    bundle.write_bytes(gzip.compress(payload,compresslevel=6,mtime=0))
    restored=json.loads(gzip.decompress(bundle.read_bytes()))
    assert all(hashlib.sha256(restored[n].encode()).hexdigest()==sha256(R/n) for n in serialized)
    numerical=read_json(R/'numeric.json')
    review=[]
    for i,(r,note) in enumerate(zip(corpus,notes)):
        source=r['source']
        if source=='story200m':source='SimpleStories-JA' if r['offset']<59963449 else 'TinyStories-JA translation'
        review.append(dict(index=i,id=r['id'],text_sha256=r['text_sha256'],source=source,body_tokens=r['body_tokens'],
            full_text_review=True,note=note,independent_human_blind=False))
    atomic_json(P/'root_cause_corpus_review.json',dict(rows=review,corpus_sha256=sha256(R/'corpus.json'),
        notes_sha256=sha256(P/'root_cause_corpus_notes.json'),reviewer='Codex full-text nonblind content diagnosis',
        caveat='biased token-offset/length-stratified128 train samples; no population prevalence claim',
        manifest_based_eos_per1000_supervised={k:1000*v['prepared']['documents']/(v['prepared']['tokens']-v['prepared']['documents']) for k,v in contract['pools'].items()},
        suspicious_examples=[review[i] for i in [6,8,10,24,26,34,45,47,52,54,70,87,96,107,115,118,121,123]],
        full_corpus_quality_certified=False))
    summary=dict(status='diagnostic_scope_complete_quality_unmet',created_at=now(),models=model_summary,
        numeric_failed_checks={k:v for k,v in numerical['checks'].items() if not v['passed']},
        numeric_passed_checks=[k for k,v in numerical['checks'].items() if v['passed']],
        gpu_job_seconds=job['gpu_job_seconds']+precision['gpu_job_seconds'],new_training_tokens=0,optimizer_updates=0,
        new_bf16_generations=384,new_fp32_generations=96,train_case_count=32,full_text_corpus_review=128,
        scope='user-facing1-3 / plan70 internal0-2',quality_targets_achieved=False,protected_test_used=False,
        contract_sha256=sha256(R/'contract.json'),raw_bundle_sha256=sha256(bundle),raw_source_sha256={n:sha256(R/n) for n in raw},
        limitations=['train diagnostic, not held-out score','Web gold tails above64 make EOS absence alone censored',
            'first exact token departure is not semantic failure','BF16 raw tolerance failures remain failures; original/mixed FP32 has same EOS/repetition counts, story marker differs by one',
            'story source/length/quality not independent','current candidate full Flash gradient/HF not repeated; original10B audited',
            'capacity/Adam/optimization not isolated; no new learning','4gram marker also finds valid repeated phrases'])
    atomic_json(P/'root_cause_summary.json',summary)
    ui=read_json(ROOT/'reports/local/webui/server.json')
    assert ui['status']=='running'
    assert Path('/proc/sys/kernel/random/boot_id').read_text().strip()==ui['boot_id']
    assert int(Path(f'/proc/{ui["pid"]}/stat').read_text().split()[21])==int(ui['start_ticks'])
    for j in (job,precision):
        pid=j['identity']['pid']
        assert not Path(f'/proc/{pid}').exists()
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response:model=json.load(response)
    assert model['checkpoint_sha256']==contract['checkpoints']['original']['sha256'] and not model['busy']
    completion=dict(status='completed_authorized_diagnostic_scope',created_at=now(),ui_identity=ui,ui_model=model,
        training_job_absent=True,precision_job_absent=True,original_checkpoints_unchanged=True,
        cpu_tests=4,thresholds_unchanged=True,numeric_all_passed=False,
        summary_sha256=sha256(P/'root_cause_summary.json'),review_sha256=sha256(P/'root_cause_corpus_review.json'),
        compressed_raw_roundtrip_exact=True,new_training_tokens=0,quality_targets_achieved=False,
        next_training_started=False,push_performed=False)
    atomic_json(P/'root_cause_completion.json',completion)
    print(json.dumps(dict(status=completion['status'],gpu_job_seconds=summary['gpu_job_seconds'],ui_pid=ui['pid'],
                         failed_numeric_checks=list(summary['numeric_failed_checks'])),ensure_ascii=False),flush=True)


if __name__=='__main__':main()
