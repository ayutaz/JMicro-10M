"""Review final10B saved full-dev, raw400 outputs and content notes on CPU."""
import argparse
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from phase6_performance import alive
from compare_base_10b import SOURCES, growth_checks, require_alignment
from compare_base_5b import summarize
from review_eos_5b_finish import validate_rows


def review(plan_path, content_path):
    plan = read_json(plan_path)
    run = ROOT / plan['output']
    job = read_json(run / 'job.json')
    assert job['status'] == 'complete' and not alive(job), 'Evaluation must have completed and exited'
    result = read_json(run / 'result.json')
    checks = {}
    def require(key, condition):
        checks[key] = bool(condition)
        assert condition, key
    require('actual_job_complete_and_exited', True)
    require('same_frozen_binding', result['binding'] == job['binding'] and result['binding']['plan_sha256'] == sha256(plan_path))
    require('unchanged_source_core_and_training_review', implementation_hashes() == plan['implementation'] and
            all(sha256(ROOT / p) == digest for p,digest in plan['source_sha256'].items()) and
            set(plan['source_sha256']) == set(SOURCES) and
            sha256(Path(plan['training_review']['path'])) == plan['training_review']['sha256'])
    training = read_json(Path(plan['training_review']['path']))
    require('actual10B_saved_training_bound', all(training['checks'].values()) and
            training['total_training_input_tokens'] == plan['checkpoint_tokens'] == 10000007168 and
            training['stages']['decay']['update'] == plan['checkpoint_update'] == 305176 and
            training['stages']['decay']['sha256'] == plan['checkpoint_sha256'])
    require('checkpoint_hash_unchanged', result['checkpoint_unchanged'] and sha256(Path(plan['checkpoint'])) == plan['checkpoint_sha256'])
    require('saved_references_unchanged', all(sha256(Path(r['path'])) == r['sha256'] for r in plan['references'].values()))
    require('evaluation_state_isolated', result['evaluation_state_isolated'])
    require('cumulative_GPU_budget_respected', job['gpu_elapsed_seconds'] <= plan['GPU_budget_seconds'] == 1800)
    body_record, gen_record = read_json(run / 'full-dev.json'), read_json(run / 'generation.json')
    require('saved_stage_bindings_match', body_record['binding'] == gen_record['binding'] == result['binding'] and
            body_record['checkpoint_sha256'] == gen_record['checkpoint_sha256'] == plan['checkpoint_sha256'])
    body, generation = body_record['body'], gen_record['generation']
    require('same_full_dev_body_exactly_once', body['documents'] == plan['documents'] == 89416 and
            body['body_bytes'] == plan['body_bytes'] == 164344743 and body['body_tokens'] == plan['body_tokens'] == 42003934 and
            all(r['body_tokens'] == r['scored_body_tokens'] for r in body['rows']))
    require('finite_BPB_and_NLL', math.isfinite(body['bpb']) and all(math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows']))
    require('BPB_from_common_body_bytes', math.isclose(body['bpb'], sum(r['body_nll'] for r in body['rows']) / math.log(2) / body['body_bytes'], rel_tol=1e-12))
    tok = Tokenizer(ROOT / plan['tokenizer'])
    require('frozen_tokenizer_dev_manifest_and_suite', sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256'] and
            sha256(Path(plan['dev_shards']) / 'manifest.json') == plan['dev_manifest_sha256'] and
            generation['suite_sha256'] == sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256'])
    rows = generation['outputs']
    require('same400_dev_generation_protocol', len(rows) == plan['generation_outputs'] == 400 and
            generation['max_new_tokens'] == 64 and generation['temperature'] == .8 and generation['top_p'] == .9 and
            generation['sampling_evaluated'] and all(r['split'] == 'dev' for r in rows))
    validate_rows(rows, tok)
    require('all_flags_match_raw_generated_IDs', True)
    failures = []
    for row in rows:
        if row['valid_utf8']:
            continue
        detail = {k: row[k] for k in ('id', 'decoding', 'suppressed', 'seed', 'stop_reason', 'generated_ids', 'text')}
        raw = tok.decode_bytes(row['generated_ids']) if 1 not in row['generated_ids'] else b''
        try:
            raw.decode('utf-8')
            detail.update(reason='unknown token ID', incomplete_tail=False)
        except UnicodeDecodeError as exc:
            detail.update(reason=exc.reason, byte_start=exc.start, byte_end=exc.end,
                byte_count=len(raw), last_bytes_hex=raw[-12:].hex(),
                at_generation_cap=len(row['generated_ids']) == 64,
                incomplete_tail=exc.end == len(raw) and exc.reason == 'unexpected end of data')
        failures.append(detail)
    refs = {k: read_json(Path(v['path'])) for k,v in plan['references'].items()}
    conditions = {
        'base2B': (2000027648, refs['base2B_body']['body'], refs['base2B_generation']['generation']),
        'base5B': (5000003584, refs['base5B_body']['body'], refs['base5B_generation']['generation']),
        'web5_1B': (5100011520, refs['web5_1B_full']['body'], refs['web5_1B_full']['generation']),
        'short5_1B_reference_only': (5100011520, refs['short5_1B_reference_only']['body'], refs['short5_1B_reference_only']['generation']),
        'base10B': (plan['checkpoint_tokens'], body, generation),
    }
    for _, old_body, old_gen in conditions.values():
        require_alignment(body, generation, old_body, old_gen)
    table = {k: summarize(k, *v) for k,v in conditions.items()}
    require('same_dev_and400_keys_and_all_summaries', table == result['conditions'] and result['same_full_dev_and400_generation_keys'])
    current = table['base10B']
    gates = {k: growth_checks(current, table[k]) for k in ('base5B', 'web5_1B')}
    require('original_safety_and_best_web_gate_recomputed', gates == result['growth_checks'] and
            all(v for g in gates.values() for v in g.values()) == result['growth_gate_passed_against_both'] and
            (current['full_dev_BPB'] < table['web5_1B']['full_dev_BPB']) == result['BPB_improves_best_web'] and
            result['automatic_candidate_gate_passed'] == (result['growth_gate_passed_against_both'] and result['BPB_improves_best_web']) and
            plan['growth_rules'] == {'maximum_BPB_regression': .001, 'fixed_repetition_increase_must_be_less_than': 8,
                'raw_unicode_empty_role_must_be_zero': True, 'BPB_must_improve_best_web': True})
    differences = {k: {'BPB_difference': current['full_dev_BPB'] - table[k]['full_dev_BPB'],
        'BPB_relative_change_percent': 100 * (current['full_dev_BPB'] / table[k]['full_dev_BPB'] - 1),
        'fixed_EOS_difference': current['fixed80']['eos'] - table[k]['fixed80']['eos'],
        'fixed_repetition_difference': current['fixed80']['repetition'] - table[k]['fixed80']['repetition']} for k in gates}
    require('reported_differences_recomputed', differences == result['differences'])
    fixed = [r for r in rows if r['decoding'] == 'greedy' and r['suppressed']]
    natural = [r for r in rows if r['stop_reason'] == 'stop_id']
    content = read_json(content_path)
    packet = read_json(run / 'aligned-content.json')
    require('all80_content_review_bound', content['reviewed_ids'] == [r['id'] for r in fixed] == [c['id'] for c in packet['cases']] and
            content['aligned_content_sha256'] == sha256(run / 'aligned-content.json') and
            [r['id'] for r in content['cases']] == content['reviewed_ids'] and all(r['note'] for r in content['cases']))
    require('all_natural_stops_review_bound', read_json(run / 'natural-stops.json')['outputs'] == natural and
            content['natural_stops_sha256'] == sha256(run / 'natural-stops.json') and
            content['reviewed_natural_stop_indices'] == list(range(len(natural))))
    require('content_review_not_blind_human_or_test', not content['blind_human_score'] and not content['test_used'] and
            not content['quality_targets_achieved'] and plan['quality_criteria_unchanged'])
    test_path = ROOT / 'reports/phase6/base_10b_comparison_tests.xml'
    suites = list(ET.parse(test_path).getroot().iter('testsuite'))
    require('23_targeted_CPU_tests_passed', sum(int(s.attrib['tests']) for s in suites) == 23 and
            all(int(s.attrib.get(k, '0')) == 0 for s in suites for k in ('failures', 'errors', 'skipped')))
    require('no_training_test_or_quality_claim', result['references_reused_without_GPU'] and result['additional_training_tokens'] == 0 and
            not result['test_split_used'] and not result['quality_targets_achieved'])
    result.update(status='verified_same_protocol_10B_quality_evaluation_complete', checks=checks,
        gpu_elapsed_seconds=job['gpu_elapsed_seconds'], body_seconds=body['seconds'], generation_seconds=gen_record['seconds'],
        checkpoint=plan['checkpoint'], checkpoint_sha256=plan['checkpoint_sha256'], verified_at=now(),
        unicode_failures=failures, content_review_sha256=sha256(content_path),
        raw_evidence={'full_dev_sha256': sha256(run / 'full-dev.json'), 'generation_sha256': sha256(run / 'generation.json'),
                      'result_sha256': sha256(run / 'result.json')},
        tests={'path': str(test_path), 'sha256': sha256(test_path), 'tests': 23},
        reviewer_source_sha256={p: sha256(ROOT / p) for p in ('scripts/review_base_10b_comparison.py', 'scripts/review_eos_5b_finish.py')},
        stop_before=['additional_training', 'EOS_finishing', 'decoder_experiments', 'Chat', '20B', '50B'])
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/base_10b_comparison.json')
    parser.add_argument('--content', type=Path, default=ROOT / 'reports/phase6/base_10b_content_review.json')
    args = parser.parse_args()
    result = review(args.plan, args.content)
    write_json(ROOT / 'reports/phase6/base_10b_comparison_review.json', result)
    print(json.dumps({'status': result['status'], 'checks': result['checks'], 'conditions': result['conditions']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
