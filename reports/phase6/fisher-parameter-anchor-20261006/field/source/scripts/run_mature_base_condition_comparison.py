"""Three matched100M forks from the actual original10B-input Base; no Chat."""
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
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.training import atomic_json, implementation_hashes, gpu_lock, rng_state, restore_rng
from mature_condition_trainer import MatureConditionTrainer
from condition_transfer_curriculum import CurriculumTrainView
from condition_relation_language import RelationLanguageTrainView
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive, identity
from run_eos_short_pilot import equal_state
import run_condition_relation_comparison as previous
import run_complete_text_comparison as evaluation

RUN = ROOT / 'reports/phase6/mature-base-condition-comparison-20261006'
CONFIG = ROOT / 'configs/phase6/mature_base_condition_comparison.json'
PROBE_CONFIG = ROOT / 'configs/phase6/mature_base_condition_probe.json'
PROPOSAL = ROOT / 'reports/phase6/mature_base_condition_comparison_proposal.json'
TOTAL, CEILING = 100000000, 2400
KIND = 'mature_Base_matched_condition_100M'
MIXTURE = dict(web=75000000, story=5000000, ordinary_textbook=10000000, conditional_textbook=10000000)
ARMS = dict(web=dict(web=TOTAL, story=0, ordinary_textbook=0, conditional_textbook=0),
            curriculum=MIXTURE.copy(), relation=MIXTURE.copy())
SOURCES = tuple(dict.fromkeys(('scripts/run_mature_base_condition_comparison.py',
    'scripts/run_mature_base_condition_comparison.ps1', 'scripts/review_mature_base_condition_comparison.py',
    'scripts/mature_condition_trainer.py', *previous.SOURCES)))
reference, check_reference = previous.reference, previous.check_reference
latest, reconcile, resume_gate, detail = previous.latest, previous.reconcile, previous.resume_gate, previous.detail


def scope(c):
    if (c['research_kind'] != KIND or c['arms'] != ARMS or c['teachers_per_arm'] != TOTAL
            or c['scientific_teacher_tokens'] != 3 * TOTAL or c['total_new_GPU_ceiling_seconds'] != CEILING
            or c['peak_lr'] != .0002 or c['optimizer_policy'] != 'inherit' or c['outcome_weight'] != 1
            or c['shapes'] != dict(context=1024, batch=32, accumulation=1, backend='flash', compile_mode='reduce-overhead', dtype='bf16')
            or c['comparisons'] != ['curriculum-vs-web', 'relation-vs-web', 'relation-vs-curriculum-secondary']
            or c['Base_adopted'] or c['Chat_started'] or c['quantization_started'] or c['protected_test_used']
            or not c['quality_criteria_unchanged']):
        raise ValueError('Matched mature-parent Base-only scope differs')


def prepare_probe():
    if PROBE_CONFIG.exists(): inspect(PROBE_CONFIG); return
    proposal = read_json(PROPOSAL)
    for key in ('evidence', 'condition_pairs', 'parent_inventory', 'parent'):
        check_reference(proposal[key])
    if (proposal['comparison'] != dict(Web_only=ARMS['web'], curriculum=ARMS['curriculum'], relation=ARMS['relation'])
            or proposal['new_scientific_teachers'] != 3 * TOTAL
            or proposal['GPU_limit_seconds_including_probe'] != CEILING
            or proposal['Base_adopted'] or proposal['Chat_started'] or proposal['quantization_started']):
        raise ValueError('Predeclared mature-parent proposal differs')
    old = read_json(previous.CONFIG)
    refs = dict(proposal=reference(PROPOSAL), inventory=proposal['parent_inventory'],
        previous_config=reference(previous.CONFIG), previous_result=reference(previous.RUN / 'compare-result.json'),
        previous_review=reference(previous.RUN / 'review.json'), original_config=old['original_config'],
        compact_index=old['accepted_compact_index'])
    data = dict(curriculum=dict(path=str(previous.control_study.DATA),
        manifest_sha256=sha256(previous.control_study.DATA / 'manifest.json')),
        relation=dict(path=str(previous.DATA), manifest_sha256=sha256(previous.DATA / 'manifest.json')))
    for arm, record in data.items():
        folder = Path(record['path'])
        for name in ('manifest.json', 'train.npz', 'content-review.json', 'content-notes.json', 'train-source.json'):
            refs[arm + '_' + name] = reference(folder / name)
    for arm, folder in (('curriculum', previous.control_study.PREP_RUN), ('relation', previous.PREP_RUN)):
        refs[arm + '_ordinary_audit'] = reference(folder / 'ordinary-stream-audit.json')
    refs['source_cases'] = reference(previous.DATA / 'transfer-probes.json')
    refs['retention_cases'] = reference(previous.DATA / 'retention-probes.json')
    c = dict(research_kind=KIND, phase='probe', parent=proposal['parent'],
        parent_actual_metadata=proposal['parent_actual_metadata'], original_config=old['original_config'],
        pool=old['pool'], accepted_compact_index=old['accepted_compact_index'], positive_data=data,
        arms=ARMS, teachers_per_arm=TOTAL, scientific_teacher_tokens=3 * TOTAL,
        peak_lr=.0002, optimizer_policy='inherit', outcome_weight=1, shapes=old['shapes'],
        GPU_budget_seconds=120, total_new_GPU_ceiling_seconds=CEILING,
        loss='ordinary original body+EOS CE, outcome weight1',
        sampler_policy='Same actual10B-input parent model/Adam/RNG; fresh seed42 source fork; absent zero-quota streams; constantLR. Curriculum/relation original3 streams matched; Web adds25M instead of other sources.',
        comparisons=['curriculum-vs-web', 'relation-vs-web', 'relation-vs-curriculum-secondary'],
        references=refs, source_sha256={p:sha256(ROOT / p) for p in SOURCES}, implementation=implementation_hashes(),
        quality_criteria_unchanged=True, old_numerical7_preserved=True, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False, created_at=now())
    scope(c); atomic_json(PROBE_CONFIG, c); inspect(PROBE_CONFIG)
    print('Accepted source/actual10B fullstate preflight complete; probe recipe frozen, science not started', flush=True)


def inspect(path):
    c = read_json(path); scope(c)
    if c['source_sha256'] != {p:sha256(ROOT / p) for p in SOURCES} or c['implementation'] != implementation_hashes():
        raise ValueError('Frozen source implementation differs')
    for ref in (*c['references'].values(), c['parent'], c['original_config'], c['accepted_compact_index']):
        check_reference(ref)
    proposal = read_json(PROPOSAL)
    if c['parent'] != proposal['parent'] or c['parent_actual_metadata'] != proposal['parent_actual_metadata']:
        raise ValueError('Actual mature parent differs')
    old = read_json(previous.CONFIG)
    if c['pool'] != old['pool'] or c['accepted_compact_index'] != old['accepted_compact_index']:
        raise ValueError('Accepted cached ordinary pool differs')
    old_job, old_result, old_review = (read_json(previous.RUN / n) for n in ('job.json', 'compare-result.json', 'review.json'))
    if (old_job['status'] != 'complete' or alive(old_job)
            or old_review['result_sha256'] != sha256(previous.RUN / 'compare-result.json')
            or old_result['protected_test_used']):
        raise ValueError('Previous terminal evidence required')
    views = {}
    for arm, cls in (('curriculum', CurriculumTrainView), ('relation', RelationLanguageTrainView)):
        record = c['positive_data'][arm]
        views[arm] = cls(Path(record['path']), record['manifest_sha256'])
        for relative, digest in views[arm].manifest['source_sha256'].items():
            if sha256(ROOT / relative) != digest: raise ValueError('Accepted generated source changed')
        audit = read_json(Path(c['references'][arm + '_ordinary_audit']['path']))
        if not all(audit['checks'].values()) or audit['goals'] != MIXTURE or audit['generated_manifest_sha256'] != record['manifest_sha256']:
            raise ValueError('Existing exact original3 teacher audit missing')
    parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
    m = c['parent_actual_metadata']
    if (parent['implementation_sha256'] != implementation_hashes() or parent['update'] != m['update']
            or parent['tokens'] != m['input_tokens'] or parent['supervised_tokens'] != m['teacher_tokens']
            or [g['lr'] for g in parent['optimizer']['param_groups']] != m['actual_LRs']):
        raise ValueError('Actual inherited parent counters/Adam/core differ')
    original = read_json(Path(c['original_config']['path']))
    folder = RUN / 'probe' if path == PROBE_CONFIG else RUN
    if (folder / 'job.json').exists() and alive(read_json(folder / 'job.json')):
        raise ValueError('Existing mature comparison live; no duplicate GPU job')
    if path == PROBE_CONFIG:
        if c['phase'] != 'probe' or c['GPU_budget_seconds'] != 120: raise ValueError('Probe budget differs')
    elif path == CONFIG:
        r = probe_evidence(); timings, estimate = estimate_training(r)
        if (c['phase'] != 'scientific' or c['probe_config_sha256'] != sha256(PROBE_CONFIG)
                or c['probe_result_sha256'] != sha256(RUN / 'probe/result.json')
                or c['verification_GPU_seconds'] != r['GPU_seconds'] or c['verification_teacher_tokens'] != r['verification_teacher_tokens']
                or c['measured_timings'] != timings or c['estimated_GPU_seconds_with_margin'] != estimate
                or not math.isclose(c['GPU_budget_seconds'] + r['GPU_seconds'], CEILING, abs_tol=1e-9)
                or estimate + r['GPU_seconds'] > CEILING):
            raise ValueError('Measured science recipe/budget differs')
    else: raise ValueError('Only frozen study configs allowed')
    return c, original, parent, views


def probe_evidence():
    job, result = read_json(RUN / 'probe/job.json'), read_json(RUN / 'probe/result.json')
    if (job['status'] != 'complete' or alive(job) or not result['passed']
            or result['config_sha256'] != sha256(PROBE_CONFIG) or result['GPU_seconds'] != job['GPU_elapsed_seconds']
            or result['GPU_seconds'] > 120 or set(result['arms']) != set(ARMS)
            or any(not r['gate']['passed'] or not all(r['gate']['checks'].values()) for r in result['arms'].values())):
        raise ValueError('All3 actual CUDA resume/timing evidence required')
    return result


def estimate_training(measured):
    timings, total = {}, 0.
    if set(measured['arms']) != set(ARMS): raise ValueError('All3 measured arms required')
    for arm, record in measured['arms'].items():
        timing = record['timing']; rows = timing['histories']
        if len(rows) != 32 or any(not math.isfinite(r['seconds']) or r['seconds'] <= 0 for r in rows):
            raise ValueError('Actual32 continuous timings required')
        step = statistics.median(r['seconds'] for r in rows[8:]); teachers = timing['verification_teacher_tokens'] / 32
        if teachers <= 0: raise ValueError('Measured teachers required')
        updates = math.ceil(TOTAL / teachers); warm = max(0., sum(r['seconds'] for r in rows[:8]) - 8 * step)
        save = (math.ceil(updates / 250) + 1) * timing['terminal_save_seconds']
        estimate = updates * step + warm + save; total += estimate
        timings[arm] = dict(steady_step_seconds=step, teachers_per_update=teachers, estimated_updates=updates,
            warmup_seconds=warm, save_seconds=save, estimated_training_seconds=estimate)
    return timings, total * 1.3 + 1200 + 100


def freeze():
    if CONFIG.exists(): inspect(CONFIG); return
    c, *_ = inspect(PROBE_CONFIG); c = copy.deepcopy(c)
    r = probe_evidence(); timings, estimate = estimate_training(r)
    if estimate + r['GPU_seconds'] > CEILING: raise ValueError('Measured study exceeds unchanged2400s budget')
    c.update(phase='scientific', probe_config_sha256=sha256(PROBE_CONFIG), probe_result_sha256=sha256(RUN / 'probe/result.json'),
        verification_GPU_seconds=r['GPU_seconds'], verification_teacher_tokens=r['verification_teacher_tokens'],
        GPU_budget_seconds=CEILING - r['GPU_seconds'], measured_timings=timings, estimated_GPU_seconds_with_margin=estimate,
        save_every_updates=250)
    atomic_json(CONFIG, c); inspect(CONFIG); print(json.dumps(dict(status='actual_measured_3arm_recipe_frozen', timings=timings, estimate=estimate)), flush=True)


def binding(c, path, arm):
    return dict(config_sha256=sha256(path), arm=arm, parent=c['parent'], short_manifest_sha256=c['pool']['manifest_sha256'],
        teacher_goals=ARMS[arm] if arm in ARMS else dict.fromkeys(MIXTURE, 0), optimizer_policy='inherit', peak_lr=.0002,
        loss=c['loss'], study_kind=KIND, sampler_policy=c['sampler_policy'], outcome_weight=1,
        positive_manifest_sha256=c['positive_data'][arm]['manifest_sha256'] if arm in c['positive_data'] else None,
        role='read-only-unmodified-parent' if arm == 'parent10B' else 'matched100M-scientific-fork')


def transfer_scores(c, arm, checkpoint, heartbeat, check, suite):
    key = 'source_cases' if suite == 'bridge' else 'retention_cases'
    folder = RUN / 'transfer' / suite / arm; terminal = folder / 'result.json'
    bound = dict(config_sha256=sha256(CONFIG), checkpoint_sha256=checkpoint['sha256'], cases_sha256=c['references'][key]['sha256'])
    check_reference(checkpoint)
    if terminal.exists():
        saved = read_json(terminal)
        if any(saved[k] != v for k, v in bound.items()): raise ValueError('Saved transfer binding differs')
        return saved
    prepared = read_json(Path(c['references'][key]['path'])); before_rng = rng_state()
    state = torch.load(checkpoint['path'], map_location='cpu', weights_only=False)
    model = JMicroModel(state['model_config']).to('cuda').eval(); model.load_state_dict(state['model'], strict=True)
    before = {k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
    scorer = NativeLikelihood(model, None, 'cuda', 'bf16', 16); rows = []
    hook = model.register_forward_pre_hook(lambda *_:check())
    try:
        with sdpa_kernel(SDPBackend.MATH):
            for start in range(0, 512, 16):
                cases, path = prepared['cases'][start:start+16], folder / f'{start:04d}.json'; check()
                if path.exists():
                    saved = read_json(path)
                    if any(saved[k] != v for k,v in bound.items()): raise ValueError('Saved transfer batch differs')
                    scored = saved['rows']
                else:
                    scored = [dict(index=case['index'], **r) for case,r in zip(cases, scorer.score_encoded(cases), strict=True)]
                    previous.ranking.validate_scores(scored, cases); atomic_json(path, dict(**bound, rows=scored))
                previous.ranking.validate_scores(scored, cases); rows.extend(scored)
                heartbeat(arm + '-' + suite, completed_requests=len(rows))
        checks = dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),
            no_gradients=all(p.grad is None for p in model.parameters()), eval_mode=not model.training)
    finally: hook.remove(); restore_rng(before_rng)
    checks['RNG_restored'] = equal_state(before_rng, rng_state())
    if not all(checks.values()): raise ValueError('Read-only scoring changed state')
    result = dict(**bound, checks=checks, summary=previous.summarize_transfer(rows, prepared), evaluated_requests=512,
        optimizer_updates=0, scientific_teacher_tokens=0, protected_test_used=False, suite=suite,
        limitations='Shared-generator local probes are secondary. Original128 are retention, not new relation-grammar holdouts.')
    atomic_json(terminal, result); del model, state, before, scorer; gc.collect(); torch.cuda.empty_cache(); return result


def run(probe=False):
    path = PROBE_CONFIG if probe else CONFIG; c, base, parent, views = inspect(path)
    output = RUN / 'probe' if probe else RUN; output.mkdir(parents=True, exist_ok=True)
    jp = output / 'job.json'; old = read_json(jp) if jp.exists() else {}
    if old and old['config_sha256'] != sha256(path): raise ValueError('Prior job binding differs')
    if old.get('status') == 'complete': print('Completed study retained; no duplicate GPU'); return
    prior_seconds = old.get('GPU_elapsed_seconds', 0.); started, stopped = [None], [False]
    job = dict(status='setup', **identity(), config_sha256=sha256(path), started_at=old.get('started_at', now()),
        GPU_elapsed_seconds=prior_seconds, Base_adopted=False, protected_test_used=False,
        restart_command=f"scripts/run_mature_base_condition_comparison.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT, signal.SIGTERM): signal.signal(sig, lambda *_:stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('Interrupted; completed updates retained')
        if started[0] is not None and prior_seconds + time.monotonic() - started[0] > c['GPU_budget_seconds']:
            raise TimeoutError('Cumulative GPU budget exhausted')
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started[0] is not None: job['GPU_elapsed_seconds'] = prior_seconds + time.monotonic() - started[0]
        atomic_json(jp, job)
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True); heartbeat('setup')
        for relative in (*SOURCES, *c['implementation'], path.relative_to(ROOT).as_posix()):
            target = output / 'source' / relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != (ROOT / relative).read_bytes(): raise ValueError('Source snapshot differs')
            if not target.exists(): shutil.copyfile(ROOT / relative, target)
        pool = TrainView(c['pool']['pool'], c['pool']['manifest_sha256']); pool.index = CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused: raise ValueError('Accepted compact index must be reused')
        with gpu_lock('cuda'):
            started[0] = time.monotonic(); heartbeat('gpu')
            progress = output / 'progress-result.json'
            result = read_json(progress) if progress.exists() else dict(config_sha256=sha256(path), arms={} if probe else {}, checkpoints={}, evaluations={})
            if result['config_sha256'] != sha256(path): raise ValueError('Durable result binding differs')
            for arm in ARMS:
                b = binding(c, path, arm)
                def build():
                    return MatureConditionTrainer(parent, pool, views.get(arm), ARMS[arm], b)
                if probe:
                    if arm in result['arms']: continue
                    gate = resume_gate(build, output / arm / 'resume-gate', sha256(path), check)
                    folder = output / arm / 'timing'; folder.mkdir(parents=True, exist_ok=True)
                    trainer = build(); cp = latest(folder)
                    if cp is not None: trainer.load(cp)
                    log = folder / 'metrics.jsonl'; reconcile(log, trainer.update, parent['update'])
                    with log.open('a', buffering=1) as stream:
                        while trainer.sampler.position < 32:
                            try: check()
                            except (InterruptedError, TimeoutError): trainer.save(folder / 'checkpoint.pt'); raise
                            row = trainer.step(); stream.write(json.dumps(row, allow_nan=False) + '\n')
                            if trainer.sampler.position % 8 == 0: heartbeat(arm + '-timing', completed_updates=trainer.sampler.position)
                    cp = folder / 'checkpoint.pt'; save_seconds = trainer.save(cp)
                    rows = [json.loads(s) for s in log.read_text().splitlines()]
                    if any(not equal_state(row[k], old_row[k]) for row,old_row in zip(rows[:4], gate['histories'][0], strict=True)
                            for k in ('loss', 'gradient_norm', 'lr', 'token_digest', 'source_teachers')):
                        raise ValueError('Timing and gate trajectories differ')
                    result['arms'][arm] = dict(gate=gate, timing=dict(histories=rows,
                        verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                        terminal_save_seconds=save_seconds, checkpoint=str(cp), checkpoint_sha256=sha256(cp)))
                else:
                    if arm in result['checkpoints']: continue
                    folder = output / arm / 'training'; folder.mkdir(parents=True, exist_ok=True)
                    trainer = build(); cp = latest(folder)
                    if cp is not None: trainer.load(cp)
                    log = folder / 'metrics.jsonl'; seconds = reconcile(log, trainer.update, parent['update'])
                    with log.open('a', buffering=1) as stream:
                        while trainer.sampler.source_teachers != ARMS[arm]:
                            try: check()
                            except (InterruptedError, TimeoutError): trainer.save(folder / f'checkpoint-{trainer.update:08d}.pt'); raise
                            row = trainer.step(); seconds += row['seconds']; stream.write(json.dumps(row, allow_nan=False) + '\n')
                            if trainer.sampler.position % 20 == 0: heartbeat(arm + '-training', teachers=row['additional_teacher_tokens'], teacher_budget=TOTAL, loss=row['loss'])
                            if trainer.sampler.position % 250 == 0: trainer.save(folder / f'checkpoint-{trainer.update:08d}.pt')
                    cp = folder / f'checkpoint-{trainer.update:08d}.pt'; trainer.save(cp)
                    result['checkpoints'][arm] = detail(trainer, cp, b, seconds)
                atomic_json(progress, result); del trainer; gc.collect(); torch.cuda.empty_cache()
            if probe:
                result.update(passed=True, verification_teacher_tokens=sum(r['gate']['verification_teacher_tokens'] + r['timing']['verification_teacher_tokens'] for r in result['arms'].values()),
                    GPU_optimizer_updates=120, scientific_teacher_tokens=0, weights_discarded_for_science=True)
            else:
                result['checkpoints']['parent10B'] = dict(checkpoint=c['parent']['path'], checkpoint_sha256=c['parent']['sha256'],
                    binding=binding(c, path, 'parent10B'), additional_supervised_tokens=0, additional_input_tokens=0, read_only=True)
                evaluation.RUN = output / 'evaluation'; dev = Shard(Path(base['dev_shards']), 'dev'); tok = Tokenizer(ROOT / base['tokenizer'])
                for arm in ('parent10B', *ARMS):
                    if arm not in result['evaluations']:
                        record = result['checkpoints'][arm]
                        result['evaluations'][arm] = evaluation.evaluate(arm, record, dev, tok, base, record['binding'], heartbeat, check,
                            started[0] + c['GPU_budget_seconds'] - prior_seconds)
                        atomic_json(progress, result)
                result.setdefault('transfer', {})
                for suite in ('bridge', 'retention'):
                    result['transfer'].setdefault(suite, {})
                    for arm, record in result['checkpoints'].items():
                        if arm not in result['transfer'][suite]:
                            result['transfer'][suite][arm] = transfer_scores(c, arm, dict(path=record['checkpoint'], sha256=record['checkpoint_sha256']), heartbeat, check, suite)
                            atomic_json(progress, result)
                result.update(scientific_teacher_tokens=3 * TOTAL, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_used=False)
            check(); elapsed = prior_seconds + time.monotonic() - started[0]; result['GPU_seconds'] = elapsed
            job.update(status='complete', stage='complete', completed_at=now(), GPU_elapsed_seconds=elapsed)
            atomic_json(output / ('result.json' if probe else 'compare-result.json'), result)
    except BaseException as error:
        job.update(status='failed', error=repr(error)); raise
    finally:
        if started[0] is not None and job['status'] != 'complete': job['GPU_elapsed_seconds'] = prior_seconds + time.monotonic() - started[0]
        atomic_json(jp, job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p = argparse.ArgumentParser(); m = p.add_mutually_exclusive_group()
    for mode in ('prepare-probe', 'preflight-probe', 'probe', 'freeze', 'inspect'): m.add_argument('--' + mode, action='store_true')
    args = p.parse_args()
    if args.prepare_probe: prepare_probe()
    elif args.preflight_probe: inspect(PROBE_CONFIG)
    elif args.freeze: freeze()
    elif args.inspect: inspect(CONFIG)
    else: run(args.probe)
