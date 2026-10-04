"""Check saved comparison data and generation flags, with zero GPU inference."""
import json
import math
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from phase6_performance import alive
from run_eos_short_pilot import rate


def main():
    plan_path = ROOT / 'configs/phase6/base_5b_comparison.json'
    plan = read_json(plan_path)
    run = ROOT / plan['output']
    job, result = read_json(run / 'job.json'), read_json(run / 'result.json')
    checks = {}
    def require(key, condition):
        checks[key] = bool(condition)
        assert condition, key
    require('actual_job_complete_and_exited', job['status'] == 'complete' and not alive(job))
    require('same_frozen_binding', result['binding'] == job['binding'] and result['binding']['plan_sha256'] == sha256(plan_path))
    require('unchanged_source_and_core', implementation_hashes() == plan['implementation'] and
            all(sha256(ROOT / p) == digest for p,digest in plan['source_sha256'].items()))
    require('checkpoint_hash_unchanged', sha256(Path(plan['checkpoint'])) == plan['checkpoint_sha256'])
    require('saved_references_unchanged', all(sha256(Path(r['path'])) == r['sha256'] for r in plan['references'].values()))
    require('evaluation_state_isolated', result['evaluation_state_isolated'])
    require('cumulative_GPU_budget_respected', job['gpu_elapsed_seconds'] <= plan['GPU_budget_seconds'])
    body_record, gen_record = read_json(run / 'full-dev.json'), read_json(run / 'generation.json')
    require('independent_saved_stage_bindings', body_record['binding'] == gen_record['binding'] == result['binding'])
    body, generation = body_record['body'], gen_record['generation']
    require('full_same_dev_body_exactly_once', body['documents'] == 89416 and body['body_bytes'] == 164344743 and
            body['body_tokens'] == 42003934 and all(r['body_tokens'] == r['scored_body_tokens'] for r in body['rows']))
    require('finite_BPB_and_NLL', math.isfinite(body['bpb']) and all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']))
    require('BPB_from_common_bytes', math.isclose(body['bpb'], sum(r['body_nll'] for r in body['rows']) / math.log(2) / body['body_bytes'], rel_tol=1e-12))
    tok = Tokenizer(ROOT / plan['tokenizer'])
    require('frozen_tokenizer_and_suite', sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256'] and
            generation['suite_sha256'] == sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256'])
    rows = generation['outputs']
    require('all400_generation_present', len(rows) == 400)
    unicode_failures = []
    for row in rows:
        ids = row['generated_ids']
        assert 0 < len(ids) <= 64
        raw = tok.decode_bytes(ids) if 1 not in ids else b''
        try:
            text, valid = raw.decode('utf-8'), 1 not in ids
        except UnicodeDecodeError as exc:
            text, valid = raw.decode('utf-8', errors='replace'), False
            unicode_failures.append(dict(id=row['id'], decoding=row['decoding'],
                suppressed=row['suppressed'], start=exc.start, end=exc.end,
                reason=exc.reason, byte_count=len(raw), last_bytes_hex=raw[-12:].hex(),
                last_token_ids=ids[-8:], at_generation_cap=len(ids) == 64,
                incomplete_tail=exc.end == len(raw) and exc.reason == 'unexpected end of data'))
        assert row['text'] == text and row['valid_utf8'] == valid
        assert row['role_leak'] == any(i in (4,5,6,7) for i in ids)
        assert row['empty_response'] == (not text.strip())
        assert row['repetition'] == bool(re.search(r'(.{2,}?)\1\1', text, flags=re.DOTALL))
        assert row['stop_reason'] == ('stop_id' if ids[-1] == 3 else 'max_new_tokens')
        assert 3 not in ids[:-1]
    require('all_flags_match_raw_generated_IDs', True)
    fixed = [r for r in rows if r['decoding'] == 'greedy' and r['suppressed']]
    require('same_fixed80_and400_summary', len(fixed) == 80 and
            result['conditions']['base5B']['fixed80'] == rate(fixed) and result['conditions']['base5B']['all400'] == rate(rows))
    require('original_alignment_and_quality_criteria_preserved', result['same_full_dev_and400_generation_keys'] and
            plan['quality_criteria_unchanged'] and not result['quality_targets_achieved'] and not result['test_split_used'])
    require('references_reused_without_new_training', result['references_reused_without_GPU'] and result['additional_training_tokens'] == 0)
    content_path = ROOT / 'reports/phase6/base_5b_content_review.json'
    content = read_json(content_path)
    require('saved_fixed80_content_review_complete', content['reviewed_ids'] == [r['id'] for r in fixed] and
            content['aligned_content_sha256'] == sha256(run / 'aligned-content.json') and
            not content['blind_human_score'] and not content['quality_targets_achieved'])
    result.update(status='verified_same_protocol_5B_comparison_complete', checks=checks,
                  gpu_elapsed_seconds=job['gpu_elapsed_seconds'], body_seconds=body['seconds'],
                  generation_seconds=gen_record['seconds'], checkpoint=plan['checkpoint'],
                  checkpoint_sha256=plan['checkpoint_sha256'], verified_at=now(),
                  unicode_failures=unicode_failures, content_review_sha256=sha256(content_path),
                  stop_before=['10B', 'Chat', 'mixture_sweep', 'decoder_sweep'])
    write_json(ROOT / 'reports/phase6/base_5b_comparison_review.json', result)
    print(json.dumps({'status': result['status'], 'checks': checks, 'conditions': result['conditions']}))


if __name__ == '__main__':
    main()
