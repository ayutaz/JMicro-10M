"""CPU evidence audit for the conditional final10B comparison, preserving failed quality gates."""
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from jmicro.japanese_evaluation import repetition_metrics
from phase6_performance import alive
from evaluate_complete_text_full import CONFIG,OUTPUT,SOURCES,selected_candidate
from run_complete_text_comparison import RUN,PLAN
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from run_eos_complete_100m import adoption_checks
from review_eos_5b_finish import validate_rows

def main():
    config=read_json(CONFIG);job=read_json(OUTPUT/'job.json');result=read_json(OUTPUT/'result.json')
    checks={}
    def require(key,value):
        checks[key]=bool(value);assert value,key
    require('actual_job_complete_and_exited',job['status']=='complete' and not alive(job))
    require('frozen_binding',result['binding']==job['binding'] and result['binding']['config_sha256']==sha256(CONFIG))
    require('unchanged_sources',config['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES} and config['implementation']==implementation_hashes())
    require('screen_bound_and_passed',sha256(PLAN)==config['primary_config_sha256'] and sha256(RUN/'review.json')==config['review_sha256'] and selected_candidate(read_json(RUN/'review.json'))==config['candidate'])
    require('GPU_budget',result['GPU_seconds']<=job['gpu_elapsed_seconds']<=config['gpu_budget_seconds']==3000)
    require('no_extra_learning_test_or_quality_claim',result['additional_training_tokens']==0 and not result['protected_test_used'] and not result['quality_targets_achieved'])
    suites=list(ET.parse(RUN/'conditional-tests.xml').getroot().iter('testsuite'))
    require('14_related_CPU_tests',sum(int(s.attrib.get('tests',0)) for s in suites)==14 and not any(int(s.attrib.get(k,0)) for s in suites for k in ('errors','failures','skipped')))
    tok=Tokenizer(ROOT/config['tokenizer'])
    require('tokenizer_dev_suite_frozen',sha256(ROOT/config['tokenizer'])==config['tokenizer_sha256'] and sha256(Path(config['dev_shards'])/'manifest.json')==config['dev_manifest_sha256'] and sha256(ROOT/'eval/base.jsonl')==config['suite_sha256'])
    parent_body=read_json(config['parent_body']['path'])['body'];parent_generation=read_json(config['parent_generation']['path'])['generation']
    require('parent_results_preserved',all(sha256(Path(config[k]['path']))==config[k]['sha256'] for k in ('parent_body','parent_generation')))
    summaries={};full={};failures={};raw_hashes={}
    cases=[json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()]
    counts={};selected=[]
    for case in cases:
        if case['split']=='dev' and counts.get(case['category'],0)<2:
            selected.append(case['id']);counts[case['category']]=counts.get(case['category'],0)+1
    for arm,detail in config['arms'].items():
        path=OUTPUT/(arm+'-full.json');record=read_json(path);full[arm]=record
        require(arm+'_checkpoint_binding',sha256(Path(detail['checkpoint']))==detail['sha256']==record['checkpoint_sha256'] and record['binding']=={**result['binding'],'arm':arm,'checkpoint_sha256':detail['sha256']})
        require(arm+'_RNG_isolation',record['evaluation_RNG_isolated'])
        body=record['body'];generation=record['generation']
        require_alignment(body,generation,parent_body,parent_generation)
        require(arm+'_exact_dev_and400_alignment',True)
        require(arm+'_full_body_accounting',len(body['rows'])==body['documents']==89416 and body['body_bytes']==164344743 and body['body_tokens']==42003934 and all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows']))
        require(arm+'_finite_common_byte_BPB',math.isfinite(body['bpb']) and all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
        validate_rows(generation['outputs'],tok);require(arm+'_all400_flags_from_raw_IDs',True)
        summaries[arm]=summarize(arm,10100015104,body,generation)
        fixed={r['id']:r for r in generation['outputs'] if r['decoding']=='greedy' and r['suppressed']}
        require(arm+'_same_primary80_IDs',all(fixed[r['id']]['generated_ids']==r['generated_ids'] for r in read_json(RUN/arm/'evaluation/generation.json')['outputs']))
        long=read_json(OUTPUT/arm/'long-generation.json')
        require(arm+'_long_binding',long['binding']==json.dumps(record['binding'],sort_keys=True))
        require(arm+'_long40_same_requests',long['complete'] and [(r['id'],r['max_new_tokens']) for r in long['rows']]==[(i,m) for m in (128,512) for i in selected])
        for row in long['rows']:
            ids=row['generated_ids'];require(arm+'_long_raw_ID_scope',0<len(ids)<=row['max_new_tokens'] and 3 not in ids[:-1])
            raw=tok.decode_bytes(ids)
            try:raw.decode('utf-8');valid=True
            except UnicodeDecodeError:valid=False
            assert row['valid_utf8']==valid
            assert row['stop_reason']==('stop_id' if ids[-1]==3 else 'max_new_tokens')
            assert repetition_metrics(row)==row['metrics']
        require(arm+'_long_raw_metrics_recomputed',True)
        for maximum in (128,512):
            group=[r for r in long['rows'] if r['max_new_tokens']==maximum]
            saved=long['summary'][str(maximum)]
            require(arm+'_long'+str(maximum)+'_summary_recomputed',
              saved['count']==saved['expected']==len(group)==20 and
              saved['natural_eos']==sum(r['metrics']['natural_eos'] for r in group) and
              saved['same_sentence_repeat']==sum(r['metrics']['same_sentence_reappears'] for r in group) and
              saved['raw_utf8_failure']==sum(r['metrics']['raw_utf8_failure'] for r in group) and
              math.isclose(saved['mean_char4_repeat'],sum(r['metrics']['char_4gram_repeat'] for r in group)/20,rel_tol=1e-12))
        require(arm+'_long_saved_summary_bound',result['long_generation'][arm]['complete'] and result['long_generation'][arm]['conditions']==long['summary'])
        failures[arm]=[{k:r[k] for k in ('id','decoding','suppressed','seed','stop_reason','generated_ids','text')} for r in generation['outputs'] if not r['valid_utf8']]
        raw_hashes[arm]={'full_sha256':sha256(path),'long_sha256':sha256(OUTPUT/arm/'long-generation.json')}
    require('saved_summaries_recomputed',result['summary']==summaries)
    parent=summarize('parent10B',10000007168,parent_body,parent_generation)
    require('parent_summary_recomputed',parent==result['parent'])
    candidate=config['candidate'];mixture=adoption_checks(full['web'],full[candidate])
    growth=growth_checks(summaries[candidate],parent)
    require('original_quality_conditions_recomputed',mixture==result['checks']['original_full_mixture'] and growth==result['checks']['parent_growth'] and result['candidate_passes_all_full_conditions']==(all(mixture.values()) and all(growth.values())))
    review=dict(status='passed',checked_at=now(),checks=checks,summary=summaries,long_generation=result['long_generation'],
      candidate_checks=result['checks'],candidate_passes_all_full_conditions=result['candidate_passes_all_full_conditions'],
      quality_targets_achieved=False,independent_human_blind='not performed',additional_training_tokens=0,protected_test_used=False,
      GPU_seconds=result['GPU_seconds'],raw_unicode_failures=failures,raw_hashes=raw_hashes,
      reviewer_source_sha256=sha256(Path(__file__)),completion_scope='Stage3 comparison including prespecified eligible full evaluation; report/commit/UI restoration still required')
    write_json(OUTPUT/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k not in ('raw_unicode_failures','raw_hashes')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
