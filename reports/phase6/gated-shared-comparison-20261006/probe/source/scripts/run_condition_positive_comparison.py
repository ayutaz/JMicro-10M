"""Bounded actual25M/arm matched positive-CE study; Base scope only."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, implementation_hashes, gpu_lock, rng_state
from phase6_performance import alive, identity, finite_state
from run_eos_short_pilot import equal_state
from cached_three_source_index import CachedThreeSourceIndex
from condition_positive_trainer import ConditionPositiveTrainer, PositiveTrainView
import run_story_weight_comparison as legacy
import run_complete_text_comparison as evaluation

RUN = ROOT / 'reports/phase6/condition-positive-comparison-20261006'
PROBE_CONFIG = ROOT / 'configs/phase6/condition_positive_probe.json'
CONFIG = ROOT / 'configs/phase6/condition_positive_comparison.json'
PREPARATION = ROOT / 'reports/phase6/source_condition_positive_preparation.json'
TOTAL = 25000000
CEILING = 1800
QUOTAS = dict(web=18750000, story=1250000, ordinary_textbook=2500000, conditional_textbook=2500000)
GOALS = dict(control=QUOTAS.copy(), positive4=QUOTAS.copy())
FACTORS = dict(control=1, positive4=4)
SOURCES = ('scripts/run_condition_positive_comparison.py', 'scripts/run_condition_positive_comparison.ps1',
    'scripts/story_weight_trainer.py', 'scripts/run_story_weight_comparison.py',
    'scripts/condition_positive_trainer.py', 'scripts/condition_positive_loss.py',
    'scripts/review_condition_positive_comparison.py', 'scripts/prepare_condition_positive_teachers.py',
    'scripts/cached_three_source_index.py',
    'scripts/textbook_quantity_trainer.py', *evaluation.SOURCES)
SOURCES = tuple(dict.fromkeys(SOURCES))


def reference(path): return dict(path=str(path), sha256=sha256(path))


def check_reference(ref):
    if sha256(Path(ref['path'])) != ref['sha256']:
        raise ValueError('Reference checksum differs: ' + ref['path'])


def source_contract():
    inherited, base, parent = legacy.source_contract()
    prep = copy.deepcopy(inherited)
    positive = read_json(PREPARATION)
    proposal_path = ROOT / 'reports/phase6/condition_positive_comparison_proposal.json'
    proposal = read_json(proposal_path)
    review_path = ROOT / 'reports/phase6/source-condition-pairs-v3-20261006/content-review.json'
    review = read_json(review_path)
    if (proposal['parent'] != dict(inherited['parent'], optimizer='inherit Adam/RNG; declared source-sampler fork with lineage', lr=.0002)
            or proposal['teachers_per_arm'] != TOTAL or proposal['teacher_quota_each_arm'] != QUOTAS
            or proposal['combined_GPU_ceiling_seconds'] != CEILING
            or proposal['arms'] != dict(ordinary_CE=dict(outcome_weight=1), positive_outcome_weighted_CE=dict(outcome_weight=4))
            or proposal['positive_data']['sha256'] != sha256(PREPARATION)
            or positive['actual_GPU_seconds'] != 0 or positive['scientific_teacher_tokens'] != 0
            or positive['newly_prepared_original_tokens'] != 0 or positive['documents'] != 512
            or not review['all64_read'] or review['weak_pairs'] != 8 or review['maximum_weak_pairs'] != 10
            or not review['training_pool_accepted']
            or review['notes_sha256'] != sha256(review_path.with_name('content-notes.tsv'))
            or review['source_pairs_sha256'] != sha256(review_path.with_name('source-pairs.json'))):
        raise ValueError('Accepted positive teacher preparation/proposal differs')
    positive_ref = dict(path=positive['data_path'], manifest_sha256=positive['manifest_sha256'])
    manifest = read_json(Path(positive_ref['path']) / 'manifest.json')
    check_reference(dict(path=str(Path(positive_ref['path']) / 'manifest.json'), sha256=positive_ref['manifest_sha256']))
    if (manifest['content_review_sha256'] != sha256(review_path)
            or manifest['original_pool_manifest_sha256'] != inherited['material']['manifest_sha256']
            or manifest['tokenizer_sha256'] != base['tokenizer_sha256']
            or manifest['documents'] != 512 or manifest['original_body_tokens'] != 71885
            or manifest['outcome_focus_body_targets'] != 18956 or manifest['known_weak_pilot_documents_with_focus_disabled'] != 8):
        raise ValueError('Original positive train manifest differs')
    prep.update(positive_data=positive_ref, positive_review=reference(review_path), proposal=reference(proposal_path),
                sampler_policy='Same four-stream seed42 and exact input/label/teacher quotas in both arms; old parent cursor retained as explicit fork lineage')
    return prep, base, parent

def validate_scope(c):
    if (c['research_kind'] != 'same_input_positive_outcome_CE' or c['arms'] != GOALS
            or c['teachers_per_arm'] != TOTAL or c['total_new_GPU_ceiling_seconds'] != CEILING
            or c['peak_lr'] != .0002 or c['optimizer_policy'] != 'inherit'
            or c['shapes'] != dict(context=1024, batch=32, accumulation=1, backend='flash', compile_mode='reduce-overhead', dtype='bf16')
            or c['outcome_weights'] != FACTORS or c['loss'] != 'normalized positive-outcome CE body+EOS' or c['protected_test_used'] or c['Base_adopted']
            or c['Chat_adopted'] or c['requested_five_steps_complete'] or not c['quality_criteria_unchanged']):
        raise ValueError('Positive-CE research scope changed')


def prepare_probe():
    if PROBE_CONFIG.exists(): inspect(PROBE_CONFIG); return
    prep, base, _ = source_contract()
    c = dict(research_kind='same_input_positive_outcome_CE', phase='probe', parent=prep['parent'],
        preparation=reference(PREPARATION), original_config=reference(ROOT / 'configs/phase6/textbook_quantity_comparison.json'),
        parent_quality_review=reference(ROOT / 'reports/phase6/textbook_coverage_2b_review.json'),
        parent_evaluation=reference(ROOT / 'reports/phase6/textbook-coverage-2b-20261006/compare-result.json'),
        pool=prep['material'], prepared_tokens=prep['prepared_tokens'], accepted_compact_index=prep['accepted_compact_index'],
        arms=GOALS, outcome_weights=FACTORS, positive_data=prep['positive_data'],
        positive_review=prep['positive_review'], proposal=prep['proposal'], teachers_per_arm=TOTAL, peak_lr=.0002, optimizer_policy='inherit', loss='normalized positive-outcome CE body+EOS',
        sampler_policy=prep['sampler_policy'], shapes=prep['shapes'],
        GPU_budget_seconds=120, total_new_GPU_ceiling_seconds=CEILING,
        probe_updates=dict(resume_per_arm=8, continuous_timing_per_arm=32, timing_warmup_updates=8),
        source_sha256={p: sha256(ROOT / p) for p in SOURCES}, implementation=implementation_hashes(),
        evaluation_binding=dict(dev_manifest_sha256=base['dev_manifest_sha256'], suite_sha256=base['suite_sha256'],
            config_sha256=base['evaluation']['config_sha256']),
        quality_criteria_unchanged=True, historical_quality_extension_refusal_preserved=True,
        old_numerical7_preserved=True, Base_adopted=False, Chat_adopted=False,
        protected_test_used=False, requested_five_steps_complete=False, scientific_teacher_tokens=0,
        created_at=now())
    validate_scope(c); atomic_json(PROBE_CONFIG, c); inspect(PROBE_CONFIG)
    print('Actual positive-CE probe recipe frozen; no science launched', flush=True)


def inspect(path):
    c = read_json(path); validate_scope(c)
    prep, base, parent = source_contract()
    if c['implementation'] != implementation_hashes() or c['source_sha256'] != {p: sha256(ROOT / p) for p in SOURCES}:
        raise ValueError('Frozen source differs')
    for name in ('parent', 'preparation', 'original_config', 'parent_quality_review', 'parent_evaluation', 'accepted_compact_index', 'positive_review', 'proposal'):
        check_reference(c[name])
    if c['parent'] != prep['parent'] or c['pool'] != prep['material'] or c['positive_data'] != prep['positive_data']:
        raise ValueError('Frozen actual parent/material differs')
    folder = RUN / 'probe' if path == PROBE_CONFIG else RUN
    if (folder / 'job.json').exists() and alive(read_json(folder / 'job.json')):
        raise ValueError('Actual positive-CE process is live; do not duplicate')
    if path == PROBE_CONFIG:
        if c['phase'] != 'probe' or c['GPU_budget_seconds'] != 120:
            raise ValueError('Probe budget differs')
    elif path == CONFIG:
        measurement = probe_evidence(); timing, estimate = estimate_training(measurement)
        if (c['phase'] != 'scientific' or c['probe_config_sha256'] != sha256(PROBE_CONFIG)
                or c['probe_result_sha256'] != sha256(RUN / 'probe/result.json')
                or c['verification_teacher_tokens'] != measurement['verification_teacher_tokens']
                or c['verification_GPU_seconds'] != measurement['GPU_seconds']
                or c['measured_timings'] != timing or c['estimated_GPU_seconds_with_margin'] != estimate
                or not math.isclose(c['GPU_budget_seconds'] + measurement['GPU_seconds'], CEILING, abs_tol=1e-9)
                or estimate + measurement['GPU_seconds'] > CEILING):
            raise ValueError('Measured scientific budget/binding differs')
    else: raise ValueError('Only frozen positive-CE configs accepted')
    return c, base, parent


def probe_evidence():
    job = read_json(RUN / 'probe/job.json'); result = read_json(RUN / 'probe/result.json')
    if (job['status'] != 'complete' or alive(job) or not result['passed']
            or result['config_sha256'] != sha256(PROBE_CONFIG) or result['GPU_seconds'] != job['GPU_elapsed_seconds']
            or result['GPU_seconds'] > 120 or result['scientific_teacher_tokens'] != 0
            or any(not g['passed'] or not all(g['checks'].values()) for g in result['gates'].values())):
        raise ValueError('Actual CUDA measurement incomplete')
    return result


def estimate_training(measurement):
    timing = {}; total = 0.
    for arm, record in measurement['timings'].items():
        rows = record['histories']
        if len(rows) != 32 or any(not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in rows):
            raise ValueError('Actual continuous timing rows missing/nonfinite')
        seconds = statistics.median(r['seconds'] for r in rows[8:])
        teachers = record['verification_teacher_tokens'] / 32
        updates = math.ceil(TOTAL / teachers)
        warm = max(0., sum(r['seconds'] for r in rows[:8]) - 8 * seconds)
        save = (math.ceil(updates / 250) + 1) * record['terminal_save_seconds']
        estimated = updates * seconds + warm + save
        timing[arm] = dict(steady_step_seconds=seconds, teachers_per_update=teachers, estimated_updates=updates,
            warmup_seconds=warm, save_seconds=save, estimated_training_seconds=estimated)
        total += estimated
    if set(timing) != set(GOALS): raise ValueError('Both measured arms required')
    return timing, total * 1.3 + 600


def freeze():
    if CONFIG.exists(): inspect(CONFIG); return
    c, _, _ = inspect(PROBE_CONFIG); c = copy.deepcopy(c)
    measurement = probe_evidence(); timing, estimate = estimate_training(measurement)
    if estimate + measurement['GPU_seconds'] > CEILING:
        raise ValueError('Measured study cannot fit unchanged1800s ceiling; retain evidence')
    c.update(phase='scientific', probe_config_sha256=sha256(PROBE_CONFIG),
        probe_result_sha256=sha256(RUN / 'probe/result.json'),
        verification_GPU_seconds=measurement['GPU_seconds'], verification_teacher_tokens=measurement['verification_teacher_tokens'],
        GPU_budget_seconds=CEILING - measurement['GPU_seconds'], measured_timings=timing,
        estimated_GPU_seconds_with_margin=estimate, save_every_updates=250)
    atomic_json(CONFIG, c); inspect(CONFIG)
    print(json.dumps(dict(status='measured_scientific_recipe_frozen', timings=timing,
        estimate=estimate, total_budget=CEILING)), flush=True)


def binding(c, path, arm):
    return dict(config_sha256=sha256(path), arm=arm, parent=c['parent'], short_manifest_sha256=c['pool']['manifest_sha256'],
        teacher_goals=c['arms'][arm], optimizer_policy='inherit', peak_lr=.0002, loss='normalized positive-outcome CE body+EOS',
        study_kind=c['research_kind'], sampler_policy=c['sampler_policy'],
        outcome_weight=FACTORS[arm], positive_manifest_sha256=c['positive_data']['manifest_sha256'])


def latest(folder):
    path = folder / 'latest.json'
    if not path.exists(): return None
    ref = read_json(path); target = Path(ref['path'])
    if target.resolve().parent != folder.resolve() or sha256(target) != ref['sha256']:
        raise ValueError('Durable latest checkpoint binding differs')
    return target


def reconcile(log, update, parent_update):
    rows = [json.loads(s) for s in log.read_text().splitlines()] if log.exists() else []
    retained = [r for r in rows if r['update'] <= update]
    discarded = [r for r in rows if r['update'] > update]
    if discarded:
        with (log.parent / 'uncheckpointed-replay.jsonl').open('a') as stream:
            for row in discarded: stream.write(json.dumps(dict(reason='not in last durable checkpoint; replay required', metric=row)) + '\n')
        log.write_text(''.join(json.dumps(r, allow_nan=False) + '\n' for r in retained))
    if [r['update'] for r in retained] != list(range(parent_update + 1, update + 1)):
        raise ValueError('Checkpoint/metrics completed-update coverage differs')
    return sum(r['seconds'] for r in retained)


def resume_gate(build, folder, config_sha, check):
    record = folder / 'result.json'
    if record.exists():
        saved = read_json(record)
        if saved['config_sha256'] != config_sha or not saved['passed']:
            raise ValueError('Prior CUDA gate differs')
        return saved
    folder.mkdir(parents=True, exist_ok=True); states, histories = [], []
    teachers = 0
    for route in ('continuous', 'resumed'):
        trainer = build(); before = trainer.supervised_tokens; rows = []
        for index in range(4):
            check(); rows.append(trainer.step())
            if route == 'resumed' and index == 1:
                path = folder / 'split.pt'; trainer.save(path)
                del trainer; gc.collect(); torch.cuda.empty_cache(); trainer = build(); trainer.load(path)
        teachers += trainer.supervised_tokens - before
        path = folder / (route + '.pt'); trainer.save(path)
        states.append(torch.load(path, map_location='cpu', weights_only=False)); histories.append(rows)
        del trainer; gc.collect(); torch.cuda.empty_cache()
    checks = {k: equal_state(states[0][k], states[1][k]) for k in
        ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'lineage', 'tokens', 'supervised_tokens',
         'body_bytes', 'token_digest', 'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass',
         'update', 'spec', 'model_config', 'pilot_binding', 'study_binding')}
    for key in ('loss', 'gradient_norm', 'lr', 'token_digest', 'source_teachers', 'source_eos', 'source_input_tokens', 'source_body_bytes', 'source_focus_teachers',
                'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass'):
        checks['history_' + key] = all(equal_state(a[key], b[key]) for a, b in zip(*histories, strict=True))
    checks['finite'] = all(finite_state(s) for s in states)
    checks['no_reheat'] = all(math.isclose(r['lr'], .0002, rel_tol=1e-10) for h in histories for r in h)
    if not all(checks.values()): raise ValueError('CUDA resume full-state mismatch: ' + repr(checks))
    result = dict(passed=True, checks=checks, histories=histories, config_sha256=config_sha,
        GPU_optimizer_updates=8, verification_teacher_tokens=teachers)
    atomic_json(record, result); return result


def detail(trainer, path, b, seconds):
    return dict(checkpoint=str(path), checkpoint_sha256=sha256(path), binding=b,
        update=trainer.update, tokens=trainer.tokens, supervised_tokens=trainer.supervised_tokens,
        additional_supervised_tokens=trainer.supervised_tokens - trainer.lineage['parent_supervised_tokens'],
        additional_input_tokens=trainer.tokens - trainer.lineage['parent_tokens'],
        source_teachers=trainer.sampler.source_teachers.copy(), source_eos=trainer.sampler.source_eos.copy(),
        source_input_tokens=trainer.sampler.source_tokens.copy(), source_focus_teachers=trainer.sampler.source_focus_teachers.copy(),
        focus_teacher_tokens=trainer.focus_teacher_tokens, focus_token_digest=trainer.focus_token_digest,
        weighted_teacher_mass=trainer.weighted_teacher_mass, outcome_weight=trainer.factor, training_seconds=seconds, completed_at=now())


def run(probe=False):
    path = PROBE_CONFIG if probe else CONFIG; c, base, parent = inspect(path)
    output = RUN / 'probe' if probe else RUN; output.mkdir(parents=True, exist_ok=True)
    jp = output / 'job.json'; old = read_json(jp) if jp.exists() else {}
    if old:
        if old['config_sha256'] != sha256(path): raise ValueError('Prior job recipe differs')
        if old['status'] == 'complete': print('Completed positive-CE job retained'); return
    prior = old.get('GPU_elapsed_seconds', 0.); started, stopped = [None], [False]
    job = dict(status='setup', **identity(), config_sha256=sha256(path), started_at=old.get('started_at', now()),
        GPU_elapsed_seconds=prior, Base_adopted=False, protected_test_used=False,
        restart_command=f"scripts/run_condition_positive_comparison.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('Stop requested; durable completed updates retained')
        if started[0] is not None and prior + time.monotonic() - started[0] > c['GPU_budget_seconds']:
            raise TimeoutError('Cumulative positive-CE GPU budget exhausted')
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started[0] is not None: job['GPU_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(jp, job)
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True); heartbeat('setup')
        for relative in (*SOURCES, *c['implementation'], path.relative_to(ROOT).as_posix()):
            target = output / 'source' / relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                if target.read_bytes() != (ROOT / relative).read_bytes(): raise ValueError('Frozen snapshot differs')
            else: shutil.copyfile(ROOT / relative, target)
        # This guard precedes the index constructor, so missing cache never triggers13GB parsing.
        check_reference(c['accepted_compact_index'])
        pool = TrainView(c['pool']['pool'], c['pool']['manifest_sha256']); pool.index = CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused: raise ValueError('Index must be reused')
        positive = PositiveTrainView(c['positive_data']['path'], c['positive_data']['manifest_sha256'])
        with gpu_lock('cuda'):
            started[0] = time.monotonic(); heartbeat('gpu')
            if probe:
                result = dict(status='actual_condition_positive_resume_and_timing_complete', gates={}, timings={},
                    config_sha256=sha256(path), scientific_teacher_tokens=0, weights_discarded_for_science=True)
                for arm in GOALS:
                    b = binding(c, path, arm)
                    def build(): return ConditionPositiveTrainer(parent, pool, positive, GOALS[arm], FACTORS[arm], b)
                    gate = resume_gate(build, output / arm / 'resume-gate', sha256(path), check)
                    result['gates'][arm] = gate
                    folder = output / arm / 'timing'; folder.mkdir(parents=True, exist_ok=True)
                    trainer = build(); cp = latest(folder)
                    if cp is not None: trainer.load(cp)
                    log = folder / 'metrics.jsonl'; reconcile(log, trainer.update, parent['update'])
                    with log.open('a', buffering=1) as stream:
                        while trainer.update - parent['update'] < 32:
                            try: check()
                            except (InterruptedError, TimeoutError): trainer.save(folder / 'checkpoint.pt'); raise
                            row = trainer.step(); stream.write(json.dumps(row, allow_nan=False) + '\n')
                            if (trainer.update - parent['update']) % 8 == 0:
                                heartbeat(arm + '-timing', completed_updates=trainer.update - parent['update'])
                    cp = folder / 'checkpoint.pt'; save_seconds = trainer.save(cp)
                    rows = [json.loads(s) for s in log.read_text().splitlines()]
                    if any(not equal_state(row[k], reference_row[k]) for row, reference_row in zip(rows[:4], gate['histories'][0], strict=True)
                           for k in ('loss', 'gradient_norm', 'lr', 'token_digest', 'source_teachers')):
                        raise ValueError('Gate/timing trajectories differ')
                    result['timings'][arm] = dict(histories=rows, verification_teacher_tokens=trainer.supervised_tokens - parent['supervised_tokens'],
                        terminal_save_seconds=save_seconds, checkpoint=str(cp), checkpoint_sha256=sha256(cp))
                    del trainer; gc.collect(); torch.cuda.empty_cache()
                result.update(passed=True, verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in result['gates'].values())
                    + sum(t['verification_teacher_tokens'] for t in result['timings'].values()), GPU_optimizer_updates=80)
            else:
                progress = output / 'progress-result.json'
                result = read_json(progress) if progress.exists() else dict(checkpoints={}, evaluations={})
                dev = Shard(Path(base['dev_shards']), 'dev'); tok = Tokenizer(ROOT / base['tokenizer'])
                for arm in GOALS:
                    b = binding(c, path, arm)
                    if arm not in result['checkpoints']:
                        folder = output / arm / 'training'; folder.mkdir(parents=True, exist_ok=True)
                        trainer = ConditionPositiveTrainer(parent, pool, positive, GOALS[arm], FACTORS[arm], b); cp = latest(folder)
                        if cp is not None: trainer.load(cp)
                        log = folder / 'metrics.jsonl'; seconds = reconcile(log, trainer.update, parent['update'])
                        with log.open('a', buffering=1) as stream:
                            while trainer.sampler.source_teachers != GOALS[arm]:
                                try: check()
                                except (InterruptedError, TimeoutError): trainer.save(folder / f'checkpoint-{trainer.update:08d}.pt'); raise
                                row = trainer.step(); seconds += row['seconds']; stream.write(json.dumps(row, allow_nan=False) + '\n')
                                if trainer.sampler.position % 20 == 0:
                                    heartbeat(arm + '-training', teachers=row['additional_teacher_tokens'], teacher_budget=TOTAL,
                                        source_teachers=row['source_teachers'], loss=row['loss'])
                                if trainer.sampler.position % 250 == 0: trainer.save(folder / f'checkpoint-{trainer.update:08d}.pt')
                        cp = folder / f'checkpoint-{trainer.update:08d}.pt'; trainer.save(cp)
                        result['checkpoints'][arm] = detail(trainer, cp, b, seconds); atomic_json(progress, result)
                        del trainer; gc.collect(); torch.cuda.empty_cache()
                    if arm not in result['evaluations']:
                        evaluation.RUN = output / 'evaluation'
                        result['evaluations'][arm] = evaluation.evaluate(arm, result['checkpoints'][arm], dev, tok, base, b,
                            heartbeat, check, started[0] + c['GPU_budget_seconds'] - prior)
                        atomic_json(progress, result)
                left = result['checkpoints']['control']; right = result['checkpoints']['positive4']
                matched = {k: equal_state(left[k], right[k]) for k in ('tokens', 'supervised_tokens', 'source_teachers', 'source_eos', 'source_input_tokens', 'source_focus_teachers', 'focus_teacher_tokens', 'focus_token_digest')}
                a = torch.load(left['checkpoint'], map_location='cpu', weights_only=False)
                z = torch.load(right['checkpoint'], map_location='cpu', weights_only=False)
                matched.update(input_label_digest=a['token_digest'] == z['token_digest'], sampler=equal_state(a['sampler'], z['sampler']))
                del a, z
                if not all(matched.values()): raise ValueError('Scientific arms did not match actual inputs/teachers')
                result['matched_input_teacher_checks'] = matched
                result.update(status='both_actual25M_learning_evaluations_complete_pending_all160_content',
                    config_sha256=sha256(path), scientific_teacher_tokens=2 * TOTAL,
                    verification_teacher_tokens=c['verification_teacher_tokens'], verification_GPU_seconds=c['verification_GPU_seconds'],
                    Base_adopted=False, Chat_adopted=False, protected_test_used=False, requested_five_steps_complete=False)
            check(); elapsed = prior + time.monotonic() - started[0]
            result['GPU_seconds'] = elapsed; job.update(status='complete', stage='complete', completed_at=now(), GPU_elapsed_seconds=elapsed)
            atomic_json(output / ('result.json' if probe else 'compare-result.json'), result)
    except BaseException as error:
        job.update(status='failed', error=repr(error)); raise
    finally:
        if started[0] is not None and job['status'] != 'complete': job['GPU_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(jp, job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser(); group = p.add_mutually_exclusive_group()
    for mode in ('prepare-probe', 'preflight-probe', 'probe', 'freeze', 'inspect'): group.add_argument('--' + mode, action='store_true')
    args = p.parse_args()
    if args.prepare_probe: prepare_probe()
    elif args.preflight_probe: inspect(PROBE_CONFIG)
    elif args.freeze: freeze()
    elif args.inspect: inspect(CONFIG)
    else: run(args.probe)
