"""Bounded 10% story fork, saved matched controls, CPU review, and eligible full evaluation."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.eos_pilot import TrainView
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, rng_state, seed_all
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.model import JMicroModel
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.japanese_evaluation import NativeLikelihood, repetition_metrics, clustered_ci
from phase6_performance import identity, alive, finite_state
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot
import evaluate_complete_text_full as previous_full
from run_eos_5b_finish import evaluate as evaluate_full
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment, growth_checks
from compare_base_5b import summarize
from review_eos_5b_finish import validate_rows
from evaluate_japanese_base import evaluate_long

CONFIG = ROOT / 'configs/phase6/story10_10b_100m.json'
SCHEMA = ROOT / 'schemas/configs/phase6/story10_10b_100m.schema.json'
RUN = ROOT / 'reports/phase6/story10-10b-100m-20261005'
OLD = ROOT / 'reports/phase6/complete-text-10b-100m-20261004'
SOURCES = tuple(dict.fromkeys(('scripts/run_story10_comparison.py', 'scripts/run_story10_comparison.ps1',
                              *comparison.SOURCES, *previous_full.SOURCES)))


def selection_checks(control, candidate, control_scores, candidate_scores):
    assert set(control_scores) == set(candidate_scores) and len(control_scores) == 80
    difference = np.array([int(candidate_scores[k]['coherence'] == 2) -
                           int(control_scores[k]['coherence'] == 2) for k in sorted(control_scores)])
    rng = np.random.default_rng(42)
    interval = np.quantile(difference[rng.integers(0, 80, size=(2000, 80))].mean(axis=1), [.025, .975]).tolist()
    original = adoption_checks(control, candidate)
    checks = dict(original_mixture=original, coherence_gain_at_least8=int(difference.sum()) >= 8,
                  paired_coherence_CI_lower_above0=interval[0] > 0,
                  coherence_difference_count=int(difference.sum()), paired_CI95=interval)
    checks['eligible_for_full'] = all(original.values()) and checks['coherence_gain_at_least8'] and checks['paired_coherence_CI_lower_above0']
    return checks


def freeze():
    assert not (RUN / 'screen-job.json').exists(), 'Do not refreeze a started job'
    old = read_json(comparison.PLAN)
    verified = read_json(OLD / 'review.json')
    assert verified['status'] == 'passed' and all(verified['checks'].values())
    assert old['implementation'] == implementation_hashes()
    parent = torch.load(old['parent']['path'], map_location='cpu', weights_only=False)
    assert sha256(Path(old['parent']['path'])) == old['parent']['sha256']
    assert (parent['update'], parent['tokens']) == (305176, 10000007168) and finite_state(parent)
    assert parent['implementation_sha256'] == old['implementation']
    assert all(math.isclose(g['lr'], .0002, rel_tol=1e-6) for g in parent['optimizer']['param_groups'])
    [suite] = list(ET.parse(RUN / 'tests.xml').getroot().iter('testsuite'))
    assert int(suite.attrib['tests']) >= 5 and all(int(suite.attrib[k]) == 0 for k in ('errors', 'failures', 'skipped'))
    reference = {}
    for key, path in {'screen': OLD / 'web/evaluation/result.json',
                      'content': OLD / 'content-review.json',
                      'full': OLD / 'conditional-full-r1/web-full.json',
                      'full_review': OLD / 'conditional-full-r1/review.json',
                      'resume_gate': OLD / 'resume-gate.json',
                      'parent_body': ROOT / 'reports/phase6/base-10b-comparison-20261004/full-dev.json',
                      'parent_generation': ROOT / 'reports/phase6/base-10b-comparison-20261004/generation.json'}.items():
        reference[key] = dict(path=str(path), sha256=sha256(path))
    assert read_json(Path(reference['full_review']['path']))['status'] == 'passed'
    config = dict(version=1, scope='Authorized plan49 stages1–3; stage1 10%100M then conditional judgment',
                  output=str(RUN.relative_to(ROOT)), parent=old['parent'],
                  web_shards=old['web_shards'], web_manifest_sha256=old['web_manifest_sha256'],
                  dev_shards=old['dev_shards'], dev_manifest_sha256=old['dev_manifest_sha256'],
                  tokenizer=old['tokenizer'], tokenizer_sha256=old['tokenizer_sha256'], suite_sha256=old['suite_sha256'],
                  pool=old['arms']['coherent20'], evaluation=old['evaluation'],
                  arms={'coherent10': dict(short_updates=305)},
                  updates_per_arm=3052, stable_updates=2900, decay_updates=152, tokens_per_update=32768,
                  tokens_per_arm=100007936, final_update=308228, final_tokens=10100015104, peak_lr=.0002,
                  screen_gpu_budget_seconds=900, full_gpu_budget_seconds=1800,
                  reference=reference, implementation=implementation_hashes(),
                  source_sha256={p: sha256(ROOT / p) for p in SOURCES}, tests_sha256=sha256(RUN / 'tests.xml'),
                  gates=old['gates'], parent_BPB_maximum_regression=.001, protected_test_used=False, created_at=now())
    write_json(CONFIG, config)
    write_json(SCHEMA, dict(type='object', additionalProperties=False, required=list(config),
                           properties={k: {'const': v} for k, v in config.items()}))
    print('Frozen one100M 10% arm; prior Web/20% results preserved; zero GPU work', flush=True)


def load_config():
    config = read_json(CONFIG)
    validate(config, read_json(SCHEMA))
    assert config['implementation'] == implementation_hashes()
    assert config['source_sha256'] == {p: sha256(ROOT / p) for p in SOURCES}
    for ref in config['reference'].values():
        assert sha256(Path(ref['path'])) == ref['sha256']
    for path, digest in ((ROOT / config['tokenizer'], config['tokenizer_sha256']),
                         (ROOT / 'eval/base.jsonl', config['suite_sha256']),
                         (Path(config['dev_shards']) / 'manifest.json', config['dev_manifest_sha256']),
                         (Path(config['pool']['pool']) / 'manifest.json', config['pool']['manifest_sha256']),
                         (ROOT / config['evaluation']['config'], config['evaluation']['config_sha256']),
                         (ROOT / config['evaluation']['semantic_suite'], config['evaluation']['semantic_sha256']),
                         (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'), config['evaluation']['data_manifest_sha256']),
                         (RUN / 'tests.xml', config['tests_sha256'])):
        assert sha256(path) == digest
    return config


def train(parent, web, pool, config, binding, heartbeat, check):
    directory = RUN / 'coherent10'
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / 'result.json'
    if path.exists():
        result = read_json(path)
        assert result['binding'] == binding and sha256(Path(result['checkpoint'])) == result['checkpoint_sha256']
        return result
    schedule = dict(parent_update=parent['update'], stable_updates=config['stable_updates'], decay_updates=config['decay_updates'])
    trainer = LowLRPilotTrainer(parent, web, pool, pilot.routes(3052, 305), schedule, binding)
    log_path = directory / 'metrics.jsonl'
    if (directory / 'latest.json').exists():
        last = read_json(directory / 'latest.json')
        assert sha256(Path(last['path'])) == last['sha256']
        trainer.load(last['path'])
        if log_path.exists():
            rows = [json.loads(line) for line in log_path.read_text().splitlines()]
            if rows and rows[-1]['update'] > trainer.update:
                shutil.copyfile(log_path, directory / f'metrics-before-resume-{time.time_ns()}.jsonl')
                log_path.write_text(''.join(json.dumps(row) + '\n' for row in rows if row['update'] <= trainer.update))
    previous = read_json(directory / 'progress.json').get('training_seconds', 0) if (directory / 'progress.json').exists() else 0
    started = time.monotonic()
    with log_path.open('a', buffering=1) as log:
        while trainer.update < config['final_update']:
            try:
                check()
            except (InterruptedError, TimeoutError):
                trainer.save(directory / f'checkpoint-{trainer.update:08d}.pt')
                raise
            row = trainer.step()
            assert math.isfinite(row['loss']) and math.isfinite(row['gradient_norm'])
            log.write(json.dumps(row, allow_nan=False) + '\n')
            local = trainer.update - parent['update']
            if local == 1 or local % 100 == 0:
                heartbeat('coherent10-train', updates_completed=local, loss=row['loss'], tokens_per_second=row['tokens_per_second'])
                write_json(directory / 'progress.json', dict(training_seconds=previous + time.monotonic() - started))
                print(json.dumps(row), flush=True)
            if local % 500 == 0:
                trainer.save(directory / f'checkpoint-{trainer.update:08d}.pt')
    checkpoint = directory / f'checkpoint-{trainer.update:08d}.pt'
    trainer.save(checkpoint)
    assert trainer.tokens == config['final_tokens'] and trainer.sampler.short.epoch == 0
    assert trainer.sampler.source_tokens == {'web': 90013696, 'short': 9994240}
    result = dict(status='complete', binding=binding, checkpoint=str(checkpoint), checkpoint_sha256=sha256(checkpoint),
                  update=trainer.update, tokens=trainer.tokens, additional_input_tokens=trainer.tokens-parent['tokens'],
                  training_seconds=previous+time.monotonic()-started, source_tokens=trainer.sampler.source_tokens,
                  source_eos_teachers=trainer.sampler.source_eos, sampler=trainer.sampler.state_dict())
    write_json(path, result)
    del trainer
    gc.collect(); torch.cuda.empty_cache()
    return result


def run_gpu(mode):
    config = load_config()
    output = RUN if mode == 'screen' else RUN / 'full'
    output.mkdir(parents=True, exist_ok=True)
    binding = dict(config_sha256=sha256(CONFIG), parent=config['parent'], peak_lr=config['peak_lr'],
                   implementation=config['implementation'], source_sha256=config['source_sha256'], arm='coherent10',
                   short_manifest_sha256=config['pool']['manifest_sha256'])
    if mode == 'full':
        review = read_json(RUN / 'review.json')
        assert review['status'] == 'passed' and review['selection']['eligible_for_full']
        binding['review_sha256'] = sha256(RUN / 'review.json')
    job_path = output / (mode + '-job.json')
    old = read_json(job_path) if job_path.exists() else {}
    if old:
        assert not alive(old), 'Actual process live; do not duplicate'
        assert old['binding'] == binding
        if old['status'] == 'complete':
            print('Completed job; reuse results', flush=True); return
    stopped = [False]; started = [None]; prior = old.get('gpu_elapsed_seconds', 0)
    budget = config[mode + '_gpu_budget_seconds']
    job = dict(status='starting', **identity(), binding=binding, started_at=old.get('started_at', now()),
               gpu_elapsed_seconds=prior, restart_command=f'scripts/run_story10_comparison.ps1 -Mode {mode}')
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('Stop requested; saved stages retained')
        if started[0] is not None and prior+time.monotonic()-started[0] > budget:
            raise TimeoutError('Frozen cumulative GPU budget exhausted')
    def heartbeat(stage, **extra):
        check(); job.update(stage=stage, heartbeat_at=now(), **extra)
        if started[0] is not None: job['gpu_elapsed_seconds'] = prior+time.monotonic()-started[0]
        atomic_json(job_path, job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES, str(CONFIG.relative_to(ROOT))):
            target = output / 'source' / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/relative).read_bytes()
            else: shutil.copyfile(ROOT/relative, target)
        dev = Shard(Path(config['dev_shards']), 'dev'); tok = Tokenizer(ROOT/config['tokenizer'])
        seed_all(42); torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started[0] = time.monotonic(); deadline = started[0]+budget-prior
            if mode == 'screen':
                assert sha256(Path(config['parent']['path'])) == config['parent']['sha256']
                parent = torch.load(config['parent']['path'], map_location='cpu', weights_only=False)
                web = TrainView(config['web_shards'], config['web_manifest_sha256'])
                pool = TrainView(config['pool']['pool'], config['pool']['manifest_sha256'], check_stream=True)
                # One bounded actual mixed-source save/resume check; no old environment/throughput studies.
                pilot.PilotTrainer = LowLRPilotTrainer
                heartbeat('resume-gate')
                gate = pilot.exact_gate(parent, web, pool, binding, RUN, check)
                trained = train(parent, web, pool, config, binding, heartbeat, check)
                comparison.RUN = RUN
                evaluated = comparison.evaluate('coherent10', trained, dev, tok, config, binding, heartbeat, check, deadline)
                control = read_json(Path(config['reference']['screen']['path']))
                result = dict(status='complete_pending_content_review', binding=binding, trained=trained,
                              screen_BPB=evaluated['body']['bpb'], rates=evaluated['greedy_rates'],
                              diagnostics=evaluated['diagnostics'], mixture=adoption_checks(control, evaluated),
                              scientific_tokens=100007936, verification_tokens=gate['input_tokens'], resume_gate=gate,
                              protected_test_used=False, GPU_seconds=prior+time.monotonic()-started[0], completed_at=now())
                write_json(RUN/'result.json', result)
            else:
                trained = read_json(RUN/'result.json')['trained']
                record = evaluate_full(Path(trained['checkpoint']), dev, tok, None, output/'candidate-full.json', binding, heartbeat, check, full=True)
                control = read_json(Path(config['reference']['full']['path']))
                parent_body = read_json(Path(config['reference']['parent_body']['path']))['body']
                parent_generation = read_json(Path(config['reference']['parent_generation']['path']))['generation']
                require_alignment(record['body'], record['generation'], parent_body, parent_generation)
                require_alignment(record['body'], record['generation'], control['body'], control['generation'])
                model_state = torch.load(trained['checkpoint'], map_location='cpu', weights_only=False)
                model = JMicroModel(model_state['model_config']).to('cuda').eval()
                model.load_state_dict(model_state['model'], strict=True); bound_evaluation_cache(model)
                before = rng_state(); hook = model.register_forward_pre_hook(lambda *_: check())
                with sdpa_kernel(SDPBackend.MATH):
                    long = evaluate_long(NativeLikelihood(model, tok, batch=16), read_json(ROOT/config['evaluation']['config']),
                                         output, json.dumps(binding, sort_keys=True), deadline)
                hook.remove(); assert long['complete'] and pilot.equal_state(before, rng_state()); check()
                candidate = summarize('coherent10', trained['tokens'], record['body'], record['generation'])
                parent = summarize('parent10B', 10000007168, parent_body, parent_generation)
                checks = dict(mixture=adoption_checks(control, record), parent_growth=growth_checks(candidate, parent))
                result = dict(status='complete', binding=binding, summary=candidate, parent=parent, long_generation=long,
                              checks=checks, candidate_passes_all_full_conditions=all(checks['mixture'].values()) and all(checks['parent_growth'].values()),
                              control_reused=config['reference']['full'], additional_training_tokens=0, protected_test_used=False,
                              quality_targets_achieved=False, independent_human_blind='not performed',
                              GPU_seconds=prior+time.monotonic()-started[0], completed_at=now())
                write_json(output/'result.json', result)
            heartbeat('complete'); job.update(status='complete', completed_at=now())
            print(json.dumps({k: result[k] for k in result if k in ('status','screen_BPB','rates','mixture','checks','candidate_passes_all_full_conditions','GPU_seconds')}), flush=True)
    except BaseException as error:
        job.update(status='failed', error_type=type(error).__name__, error=str(error)); raise
    finally:
        if started[0] is not None: job['gpu_elapsed_seconds'] = prior+time.monotonic()-started[0]
        atomic_json(job_path, job)


def review_screen():
    config = load_config(); result = read_json(RUN/'result.json'); job = read_json(RUN/'screen-job.json')
    assert job['status'] == 'complete' and not alive(job)
    evaluation = read_json(RUN/'coherent10/evaluation/result.json')
    rows = evaluation['generation']['outputs']; tok = Tokenizer(ROOT/config['tokenizer'])
    validate_rows(rows, tok)
    annotations = read_json(RUN/'annotations.json')
    assert annotations['generation_sha256'] == sha256(RUN/'coherent10/evaluation/generation.json')
    scores = {r[0]: dict(grammar=r[1], relevance=r[2], coherence=r[3], completion=r[4], rationale=r[5]) for r in annotations['scores']}
    assert len(scores) == len(annotations['scores']) == len(rows) == 80 and set(scores) == {r['id'] for r in rows}
    for row in rows:
        score = scores[row['id']]
        assert all(score[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and score['completion'] in (0,1) and score['rationale']
        assert not score['completion'] or row['stop_reason'] == 'stop_id'
    control = read_json(Path(config['reference']['screen']['path']))
    control_scores = {r['id']: r for r in read_json(Path(config['reference']['content']['path']))['rows'] if r['arm']=='web'}
    selection = selection_checks(control, evaluation, control_scores, scores)
    trained = result['trained']; assert sha256(Path(trained['checkpoint'])) == trained['checkpoint_sha256']
    state = torch.load(trained['checkpoint'], map_location='cpu', weights_only=False)
    history = [json.loads(line) for line in (RUN/'coherent10/metrics.jsonl').read_text().splitlines()]
    assert finite_state(state) and state['pilot_binding'] == result['binding'] == evaluation['binding']
    assert state['update'] == 308228 and state['tokens'] == 10100015104
    assert len(history) == 3052 and [r['update'] for r in history] == list(range(305177,308229))
    assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history)
    assert state['sampler']['source_tokens'] == {'web':90013696, 'short':9994240} and state['sampler']['short']['epoch'] == 0
    assert all(k in state for k in ('model','optimizer','scheduler','rng','sampler','tokens','token_digest'))
    assert result['GPU_seconds'] <= config['screen_gpu_budget_seconds'] and result['verification_tokens'] == 262144
    assert result['resume_gate']['passed'] and all(result['resume_gate']['checks'].values())
    assert evaluation['evaluation_RNG_isolated'] and all(evaluation['diagnostics'][t]['complete'] for t in config['evaluation']['tasks'])
    diagnostics = {}
    for task in config['evaluation']['tasks']:
        a = {r['id']:r for r in read_json(OLD/'web/evaluation'/(task+'.json'))['rows']}
        b = {r['id']:r for r in read_json(RUN/'coherent10/evaluation'/(task+'.json'))['rows']}
        assert set(a) == set(b)
        diagnostics[task] = clustered_ci([dict(id=k, family=a[k].get('family',k), difference=b[k]['credit']-a[k]['credit']) for k in a], key='difference')
    summary = {k+'_score2': sum(r[k]==2 for r in scores.values()) for k in ('grammar','relevance','coherence')}
    summary.update(appropriate_EOS=sum(r['completion'] for r in scores.values()), count=80)
    review = dict(status='passed', checked_at=now(), config_sha256=sha256(CONFIG), screen_sha256=sha256(RUN/'result.json'),
                  summary=summary, selection=selection, paired_diagnostics=diagnostics,
                  scientific_tokens=100007936, verification_tokens=262144, protected_test_used=False,
                  independent_human_blind='not performed', quality_targets_achieved=False,
                  rows=[dict(row, **scores[row['id']], repetition_details=repetition_metrics(row)) for row in rows],
                  reviewer_source_sha256=sha256(Path(__file__)))
    write_json(RUN/'review.json', review)
    print(json.dumps({k:v for k,v in review.items() if k != 'rows'}, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=('freeze','screen','full','review','probe'), default='screen')
    args = parser.parse_args()
    assert sys.version_info[:3] == (3,12,7); torch.set_num_threads(2)
    if args.mode == 'freeze': freeze()
    elif args.mode == 'review': review_screen()
    elif args.mode == 'probe':
        load_config()
        for path in (RUN/'screen-job.json',RUN/'full/full-job.json'):
            if path.exists(): assert not alive(read_json(path)), 'Actual comparison job live; no duplicate launch'
        print('Frozen config valid; no live comparison job')
    else: run_gpu(args.mode)


if __name__ == '__main__': main()
