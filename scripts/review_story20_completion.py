"""Audit actual plan52 stages1–4, including its entered paired500M branch.

This does not rerun GPU work or mutate frozen primary/full reviews. Every saved
review is bound to its inputs, then delivery and runtime evidence are checked.
"""
import json
import math
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from review_eos_5b_finish import validate_rows
import run_story20_low_lr as screen
import run_story20_budget as study
from run_story10_comparison import selection_checks


def test_count(path):
    suites = list(ET.parse(path).getroot().iter('testsuite'))
    assert all(int(s.attrib[k]) == 0 for s in suites for k in ('errors', 'failures', 'skipped'))
    return sum(int(s.attrib['tests']) for s in suites)


def main():
    assert sys.version_info[:3] == (3, 12, 7)
    torch.set_num_threads(2)
    config = screen.load_config()
    budget = study.load_config()
    checks, sources = {}, {}

    def require(name, value):
        checks[name] = bool(value)
        assert value, name

    def remember(path):
        path = Path(path)
        sources[str(path)] = sha256(path)

    def exited(path, seconds):
        job = read_json(path)
        require(str(path.relative_to(ROOT)) + '_actual_complete_exited', job['status'] == 'complete' and not alive(job))
        require(str(path.relative_to(ROOT)) + '_budget', job['gpu_elapsed_seconds'] <= seconds)
        remember(path)
        return job

    def bound_full(module, expected_pass=None):
        directory = module.RUN / 'full'
        review = read_json(directory / 'review.json')
        result = read_json(directory / 'result.json')
        job = exited(directory / 'full-job.json', module.load_config()['full_gpu_budget_seconds'])
        require(str(directory.relative_to(ROOT)) + '_30_actual_checks_bound',
                review['status'] == 'passed' and len(review['checks']) == 30 and all(review['checks'].values())
                and review['result_sha256'] == sha256(directory / 'result.json')
                and review['reviewer_sha256'] == sha256(ROOT / 'scripts/review_story20_execution.py'))
        for path, digest in review['sources'].items():
            require('full_source_' + path, sha256(Path(path)) == digest)
        require(str(directory.relative_to(ROOT)) + '_original_gates_no_learning',
                result['additional_training_tokens'] == 0 and result['binding'] == job['binding']
                and result['binding']['plan_sha256'] == sha256(module.CONFIG)
                and result['binding']['review_sha256'] == sha256(module.RUN / 'review.json')
                and result['GPU_seconds'] <= job['gpu_elapsed_seconds']
                and not result['protected_test_used'] and not result['quality_targets_achieved'])
        if module is study:
            from evaluate_story20_budget_full import CONFIG as full_config, SCHEMA as full_schema, load_config
            _, plan = load_config()
            require('500M_full_separate_frozen_plan_and_sources',
                    result['binding']['full_plan_sha256'] == sha256(full_config)
                    and result['binding']['source_sha256'] == plan['sources']
                    and plan['additional_training_tokens'] == 0 and not plan['protected_test_used'])
            for relative, digest in plan['sources'].items():
                require('500M_full_saved_source_' + relative,
                        sha256(directory / 'source' / relative) == digest)
            remember(full_config)
            remember(full_schema)
        if expected_pass is not None:
            require(str(directory.relative_to(ROOT)) + '_entry_pass', result['candidate_passes_all_full_conditions'] == expected_pass)
        remember(directory / 'review.json')
        remember(directory / 'result.json')
        return result

    first = read_json(screen.RUN / 'result.json')
    primary = read_json(screen.RUN / 'review.json')
    job = exited(screen.RUN / 'screen-job.json', config['screen_gpu_budget_seconds'])
    require('100M_actual_config_result_content_binding', primary['status'] == 'passed'
            and primary['config_sha256'] == sha256(screen.CONFIG)
            and primary['screen_sha256'] == sha256(screen.RUN / 'result.json') and first['binding'] == job['binding'])
    require('20_relevant_tests', test_count(screen.RUN / 'tests.xml') == 20)
    require('100M_actual25_CUDA_resume_checks', first['resume_gate']['passed']
            and len(first['resume_gate']['checks']) == 25 and all(first['resume_gate']['checks'].values())
            and first['verification_tokens'] == 262144 and first['scientific_tokens'] == 100007936)
    trained = first['trained']
    evaluation = read_json(screen.RUN / 'coherent20/evaluation/result.json')
    require('100M_actual_saved_finite_state', trained['checkpoint_sha256'] == sha256(Path(trained['checkpoint']))
            == evaluation['checkpoint_sha256'])
    state = torch.load(trained['checkpoint'], map_location='cpu', weights_only=False)
    require('100M_counters_full_resume_state', finite_state(state) and state['tokens'] == 10100015104
            and state['update'] == 308228 and all(k in state for k in ('optimizer', 'scheduler', 'rng', 'sampler')))
    del state
    history = [json.loads(line) for line in (screen.RUN / 'coherent20/metrics.jsonl').read_text().splitlines()]
    require('100M_contiguous_finite_schedule_and_counts', len(history) == 3052
            and [r['update'] for r in history] == list(range(305177, 308229))
            and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history)
            and history[0]['lr'] == .0001 and math.isclose(history[-1]['lr'], .00001, rel_tol=.001)
            and trained['source_tokens'] == dict(web=80019456, short=19988480) and trained['sampler']['short']['epoch'] == 0)
    normal = ROOT / 'reports/phase6/complete-text-10b-100m-20261004/coherent20/metrics.jsonl'
    require('100M_same_input_as_normalLR20', json.loads(normal.read_text().splitlines()[-1])['token_digest'] == history[-1]['token_digest'])
    control = read_json(Path(config['reference']['screen']['path']))
    body = evaluation['body']
    require('100M_common256_complete_BPB_protocol', len(body['rows']) == body['documents'] == 256
            and body['body_bytes'] == 472055 and body['body_tokens'] == 122343
            and [(r['doc_id'], r['body_bytes'], r['body_tokens']) for r in body['rows']]
            == [(r['doc_id'], r['body_bytes'], r['body_tokens']) for r in control['body']['rows']]
            and all(body[k] == control['body'][k] for k in ('context', 'stride', 'batch', 'evaluator', 'teacher_scope'))
            and all(r['body_tokens'] == r['scored_body_tokens'] and math.isfinite(r['body_nll']) and math.isfinite(r['eos_nll']) for r in body['rows'])
            and math.isclose(body['bpb'], sum(r['body_nll'] for r in body['rows']) / math.log(2) / body['body_bytes'], rel_tol=1e-12))
    require('100M_complete_Japanese_tasks_and_saved_control', first['control_reused'] == config['reference']
            and read_json(Path(config['reference']['control_config']['path']))['peak_lr'] == .0001
            and evaluation['evaluation_RNG_isolated']
            and all(evaluation['diagnostics'][task]['complete'] and evaluation['diagnostics'][task]['count'] == n
                    for task, n in {'semantics': 192, 'jblimp': 331, 'jcqa': 1119}.items()))
    reference_scores = {r['id']: r for r in read_json(Path(config['reference']['content']['path']))['scored_outputs']['web']}
    tok = Tokenizer(ROOT / config['tokenizer'])
    validate_rows(evaluation['generation']['outputs'], tok)
    actual = {r['id']: r for r in evaluation['generation']['outputs']}
    cases = {r['id']: r for r in (json.loads(line) for line in (ROOT / 'eval/base.jsonl').read_text().splitlines()) if r['split'] == 'dev'}
    require('100M_exact_dev80_prefixes', set(actual) == set(cases)
            and all(r['prefix'] == cases[k]['prefix'] for k, r in actual.items()))
    require('100M_all80_content_bound', len(primary['rows']) == len(actual) == 80
            and all(r['generated_ids'] == actual[r['id']]['generated_ids'] and r['text'] == actual[r['id']]['text'] and r['rationale'] for r in primary['rows']))
    require('100M_original_selection_recomputed', selection_checks(control, evaluation, reference_scores,
            {r['id']: r for r in primary['rows']}) == primary['selection'] and primary['selection']['eligible_for_full'])
    initial_full = bound_full(screen, True)

    pool = Path(budget['pool']['pool'])
    ready = read_json(pool / 'ready.json')
    content = read_json(pool / 'content-review.json')
    builder = read_json(pool.parent / 'job.json')
    manifest = read_json(pool / 'manifest.json')
    samples = read_json(pool / 'samples.json')
    require('pool_actual_builder_complete_exited', builder['status'] == 'complete' and not alive(builder) and builder['elapsed_seconds'] <= 1800)
    require('pool_actual_source_exhaustion_counts', ready['source_exhausted'] and not ready['target_reached']
            and ready['totals'] == builder['counts'] and ready['totals']['tokens'] == 59963449
            and ready['totals']['documents'] == 662857 and len(manifest['files_used']) == 4
            and ready['source_train_only'] and ready['parent_split_disjoint'])
    require('pool40_inspection_bound_and_reuse_disclosed', content['accepted_for_experiment']
            and content['pool_manifest_sha256'] == ready['manifest_sha256'] == sha256(pool / 'manifest.json')
            and content['samples_sha256'] == sha256(pool / 'samples.json')
            and content['reviewed_samples'] == len(samples) == 40
            and content['reviewed_generation_ids'] == [s['generation_id'] for s in samples]
            and content['planned_story_input_tokens'] == 99975168
            and math.isclose(content['planned_exposure_ratio'], 99975168 / 59963449, rel_tol=1e-12)
            and not content['quality_targets_achieved'])
    # Check only the new small pool, not the independently unaudited12.23B Web corpus.
    require('new_pool_stream_index_tokenbyte_hashes', (pool / 'train.bin').stat().st_size == 2 * ready['totals']['tokens']
            and sha256(pool / 'train.bin') == manifest['splits']['train']['stream_sha256']
            and sha256(pool / 'train.index.jsonl') == manifest['splits']['train']['index_sha256']
            and sha256(pool / 'token_bytes.json') == manifest['token_bytes_sha256'])
    for path in (pool / 'ready.json', pool / 'content-review.json', pool / 'manifest.json', pool / 'samples.json', pool.parent / 'job.json'):
        remember(path)

    result = read_json(study.RUN / 'result.json')
    reviewed = read_json(study.RUN / 'review.json')
    final_job = exited(study.RUN / 'screen-job.json', budget['screen_gpu_budget_seconds'])
    require('26_relevant_budget_tests', test_count(study.RUN / 'tests.xml') == 26)
    require('500M_primary_all_checks_bound', reviewed['status'] == 'passed' and len(reviewed['checks']) >= 35
            and all(reviewed['checks'].values()) and reviewed['config_sha256'] == sha256(study.CONFIG)
            and reviewed['result_sha256'] == sha256(study.RUN / 'result.json')
            and reviewed['reviewer_sha256'] == sha256(ROOT / 'scripts/review_story20_budget.py')
            and result['binding'] == final_job['binding'] and result['GPU_seconds'] <= final_job['gpu_elapsed_seconds'])
    require('paired500M_actual_scientific_and_resume_counts', result['scientific_tokens'] == 1000013824
            and result['verification_tokens'] == 262144 and result['resume_gate']['passed']
            and all(result['resume_gate']['checks'].values()) and not result['protected_test_used'])
    annotations = read_json(study.RUN / 'annotations.json')
    for arm in budget['arms']:
        for label in ('intermediate100M', 'result'):
            ev_path = study.RUN / 'evaluation' / label / arm / 'evaluation'
            ev = read_json(ev_path / 'result.json')
            scored = reviewed['scored_outputs'][arm][label]
            rows = ev['generation']['outputs']
            entries = {r[0]: r for r in annotations['scores'][arm][label]}
            require(arm + '_' + label + '_80_raw_ratings_bound', len(rows) == len(scored) == 80
                    and annotations['generation_sha256'][arm][label] == sha256(ev_path / 'generation.json')
                    and all(a['id'] == b['id'] and a['generated_ids'] == b['generated_ids']
                            and a['text'] == b['text'] and b['rationale'] for a, b in zip(rows, scored))
                    and len(entries) == 80 and all(entries[r['id']][1:] ==
                            [r['grammar'], r['relevance'], r['coherence'], r['completion'], r['rationale']] for r in scored))
            require(arm + '_' + label + '_complete_Japanese_diagnostics', ev['evaluation_RNG_isolated']
                    and all(ev['diagnostics'][task]['complete'] and ev['diagnostics'][task]['count'] == n
                            for task, n in {'semantics': 192, 'jblimp': 331, 'jcqa': 1119}.items()))
            remember(ev_path / 'result.json')
            remember(ev_path / 'generation.json')
    for label in ('intermediate100M', 'result'):
        evaluation_pair = {a: read_json(study.RUN / 'evaluation' / label / a / 'evaluation/result.json') for a in budget['arms']}
        score_pair = {a: {r['id']: r for r in reviewed['scored_outputs'][a][label]} for a in budget['arms']}
        require(label + '_original_selection_recomputed', reviewed['selection'][label] == selection_checks(
                evaluation_pair['web'], evaluation_pair['coherent20'], score_pair['web'], score_pair['coherent20']))

    eligible = reviewed['eligible_for_full']
    final_full = bound_full(study) if eligible else None
    if not eligible:
        require('ineligible500M_full_not_launched', not (study.RUN / 'full/full-job.json').exists())
    decision = read_json(ROOT / 'reports/phase6/story20_judgment.json')
    accepted = eligible and final_full['candidate_passes_all_full_conditions']
    require('stage4_actual_decision_and_next_proposal', decision['stage4_status'] == 'complete'
            and decision['candidate500M_passes_acceptance'] == accepted
            and decision['primary_review_sha256'] == sha256(study.RUN / 'review.json')
            and decision['full_review_sha256'] == (sha256(study.RUN / 'full/review.json') if eligible else None)
            and all(decision['next_proposal'].get(k) for k in ('purpose', 'comparison', 'budgets', 'completion_condition'))
            and not decision['next_proposal']['executed'] and not decision['quality_targets_achieved']
            and decision['stop_after_delivery'] and decision['report_sha256'] == sha256(ROOT / 'docs/53_story20_low_lr_judgment.md'))
    server = read_json(ROOT / 'reports/local/webui/server.json')
    require('actual_original_UI_identity_live', server['status'] == 'running' and alive(server))
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=5) as response:
        model = json.load(response)
    require('HTTP_original10B_UI_restored', model['checkpoint_sha256'] == config['parent']['sha256']
            and model['training_tokens'] == 10000007168 and not model['busy'])
    documents = ('AGENTS.md', 'README.md', 'docs/autonomous_status.md', 'docs/15_project_roadmap.md',
                 'docs/windows_handoff.md', 'docs/52_story20_low_lr_execution.md', 'docs/53_story20_low_lr_judgment.md')
    for relative in documents:
        require('delivery_' + relative, (ROOT / relative).is_file())
        remember(ROOT / relative)
    for module in (screen, study):
        for path in (module.CONFIG, module.RUN / 'result.json', module.RUN / 'review.json', module.RUN / 'tests.xml'):
            remember(path)
    remember(ROOT / 'reports/phase6/story20_judgment.json')
    remember(study.RUN / 'annotations.json')
    evidence = dict(status='passed', scope='Plan52 actual stages1–4 including entered paired500M branch',
                    checked_at=now(), checks=checks, sources=sources, reviewer_sha256=sha256(Path(__file__)),
                    scientific_tokens=1100021760, verification_tokens=524288,
                    GPU_seconds=first['GPU_seconds'] + initial_full['GPU_seconds'] + result['GPU_seconds']
                    + (final_full['GPU_seconds'] if eligible else 0),
                    conditional500M_performed=True, conditional500M_full_performed=eligible,
                    candidate500M_passes_acceptance=accepted, quality_targets_achieved=False,
                    protected_test_used=False, independent_human_blind='not performed', original_UI=model,
                    UI_identity={k: server[k] for k in ('pid', 'boot_id', 'start_ticks', 'ready_at')},
                    remaining_delivery='Verify final local commit, clean worktree and bound evidence hashes before marking goal complete')
    write_json(ROOT / 'reports/phase6/story20_execution_completion.json', evidence)
    print(json.dumps({k: v for k, v in evidence.items() if k not in ('sources', 'original_UI')}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
