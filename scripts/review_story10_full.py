"""Inspect actual saved full/long outputs and unchanged adoption gates; no GPU work."""
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import repetition_metrics
from phase6_performance import alive
from run_story10_comparison import CONFIG, RUN, load_config
from compare_base_10b import require_alignment, growth_checks
from compare_base_5b import summarize
from run_eos_complete_100m import adoption_checks
from review_eos_5b_finish import validate_rows


def main():
    config=load_config(); output=RUN/'full'
    job=read_json(output/'full-job.json');result=read_json(output/'result.json')
    checks={}
    def require(name,value):
        checks[name]=bool(value)
        assert value,name
    require('actual_full_job_terminal_and_exited',job['status']=='complete' and not alive(job))
    require('full_binding_matches_config_and_screen_review',result['binding']==job['binding'] and
            result['binding']['config_sha256']==sha256(CONFIG) and
            result['binding']['review_sha256']==sha256(RUN/'review.json'))
    primary=read_json(RUN/'review.json')
    require('screen_eligible_and_review_bound',primary['status']=='passed' and primary['selection']['eligible_for_full'] and
            primary['screen_sha256']==sha256(RUN/'result.json'))
    require('bounded_full_GPU_budget',result['GPU_seconds']<=job['gpu_elapsed_seconds']<=1800)
    require('zero_additional_learning_and_no_test_or_quality_claim',result['additional_training_tokens']==0 and
            not result['protected_test_used'] and not result['quality_targets_achieved'])
    trained=read_json(RUN/'result.json')['trained']
    full_path=output/'candidate-full.json';record=read_json(full_path)
    require('actual_candidate_checkpoint_hash',record['binding']==result['binding'] and
            record['checkpoint_sha256']==trained['checkpoint_sha256']==sha256(Path(trained['checkpoint'])))
    body,generation=record['body'],record['generation']
    require('full_record_and_isolated_RNG',record['full'] and record['evaluation_RNG_isolated'])
    require('complete_full_body_common_coverage',len(body['rows'])==body['documents']==89416 and
            body['body_bytes']==164344743 and body['body_tokens']==42003934 and
            all(r['body_tokens']==r['scored_body_tokens'] for r in body['rows']))
    require('BPB_recomputed_from_finite_document_NLL',math.isfinite(body['bpb']) and
            all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']) and
            math.isclose(body['bpb'],sum(r['body_nll'] for r in body['rows'])/math.log(2)/body['body_bytes'],rel_tol=1e-12))
    control=read_json(Path(config['reference']['full']['path']))
    parent_body=read_json(Path(config['reference']['parent_body']['path']))['body']
    parent_generation=read_json(Path(config['reference']['parent_generation']['path']))['generation']
    require_alignment(body,generation,control['body'],control['generation'])
    require_alignment(body,generation,parent_body,parent_generation)
    require('same_document_IDs_bytes_and400_requests',True)
    require('saved_Web_control_reused_explicitly',result['control_reused']==config['reference']['full'])
    tokenizer=Tokenizer(ROOT/config['tokenizer']);validate_rows(generation['outputs'],tokenizer)
    require('all400_raw_ID_flags_verified',len(generation['outputs'])==400)
    fixed={r['id']:r for r in generation['outputs'] if r['decoding']=='greedy' and r['suppressed']}
    require('primary80_same_raw_generated_IDs',all(fixed[r['id']]['generated_ids']==r['generated_ids'] for r in primary['rows']))
    long_path=output/'long-generation.json';long=read_json(long_path)
    require('long_binding',long['binding']==json.dumps(result['binding'],sort_keys=True))
    counts={};selected=[]
    for line in (ROOT/'eval/base.jsonl').read_text().splitlines():
        case=json.loads(line)
        if case['split']=='dev' and counts.get(case['category'],0)<2:
            counts[case['category']]=counts.get(case['category'],0)+1;selected.append(case['id'])
    require('all40_long_requests_prespecified',long['complete'] and
            [(r['id'],r['max_new_tokens']) for r in long['rows']]==[(i,m) for m in (128,512) for i in selected])
    for row in long['rows']:
        ids=row['generated_ids'];assert 0<len(ids)<=row['max_new_tokens'] and 3 not in ids[:-1]
        raw=tokenizer.decode_bytes(ids)
        try:text=raw.decode('utf-8');valid=True
        except UnicodeDecodeError:text=raw.decode('utf-8',errors='replace');valid=False
        assert row['text']==text and row['valid_utf8']==valid
        assert row['stop_reason']==('stop_id' if ids[-1]==3 else 'max_new_tokens')
        assert repetition_metrics(row)==row['metrics']
    require('long_raw_text_stop_UTF8_and_metrics_recomputed',True)
    for maximum in (128,512):
        rows=[r for r in long['rows'] if r['max_new_tokens']==maximum];saved=long['summary'][str(maximum)]
        require('long'+str(maximum)+'_summary_from_raw_rows',saved['count']==saved['expected']==len(rows)==20 and
                saved['natural_eos']==sum(r['metrics']['natural_eos'] for r in rows) and
                saved['same_sentence_repeat']==sum(r['metrics']['same_sentence_reappears'] for r in rows) and
                saved['raw_utf8_failure']==sum(r['metrics']['raw_utf8_failure'] for r in rows) and
                math.isclose(saved['mean_char4_repeat'],sum(r['metrics']['char_4gram_repeat'] for r in rows)/20,rel_tol=1e-12))
    require('saved_long_summary_exactly_bound',result['long_generation']['complete'] and result['long_generation']['conditions']==long['summary'])
    candidate=summarize('coherent10',trained['tokens'],body,generation)
    parent=summarize('parent10B',10000007168,parent_body,parent_generation)
    require('candidate_and_parent_summaries_recomputed',candidate==result['summary'] and parent==result['parent'])
    actual={'mixture':adoption_checks(control,record),'parent_growth':growth_checks(candidate,parent)}
    require('original_gates_recomputed_without_weakening',actual==result['checks'] and
            result['candidate_passes_all_full_conditions']==(all(actual['mixture'].values()) and all(actual['parent_growth'].values())))
    review=dict(status='passed',checked_at=now(),checks=checks,summary=candidate,parent=parent,
                long_generation=result['long_generation'],adoption_checks=actual,
                candidate_passes_all_full_conditions=result['candidate_passes_all_full_conditions'],
                additional_training_tokens=0,protected_test_used=False,quality_targets_achieved=False,
                independent_human_blind='not performed',GPU_seconds=result['GPU_seconds'],
                full_sha256=sha256(full_path),long_sha256=sha256(long_path),reviewer_source_sha256=sha256(Path(__file__)))
    write_json(output/'review.json',review)
    print(json.dumps(review,ensure_ascii=False),flush=True)


if __name__=='__main__':main()
