"""One shared native Web endpoint, then exactly matched Base CE versus CE+DPO."""
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
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json, implementation_hashes, gpu_lock, rng_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from base_preference_trainer import CommonWebTrainer, PairPreferenceTrainer, PairQuotaSampler, build_reference, KIND, LR
from base_preference_accounting import accounting, matched_exposure
from phase6_performance import identity, alive, finite_state
from run_eos_short_pilot import equal_state
from probe_livedoor_base import host_state
import probe_base_preference as probe
import run_source_order_condition_comparison_v2 as prior
import run_complete_text_comparison as evaluation

RUN = probe.RUN
CONFIG = ROOT/'configs/phase6/base_preference_comparison.json'
PROPOSAL = probe.PROPOSAL
COMMON, PAIR, TOTAL, CEILING = 6000000, 2000000, 10000000, 1800
ARMS = dict(chosen_CE=0., chosen_CE_DPO=.1)
SOURCES = ('scripts/run_base_preference_comparison.py', 'scripts/run_base_preference_comparison.ps1',
    'scripts/base_preference_accounting.py', 'scripts/review_base_preference_comparison.py',
    'scripts/record_base_preference_content.py', 'tests/test_base_preference_science.py')
EVALUATION_SOURCES = ('scripts/run_complete_text_comparison.py', 'scripts/run_source_order_condition_comparison_v2.py',
    'scripts/review_parameter_displacement_anchor.py', 'scripts/review_matched_story_study.py',
    'scripts/run_eos_complete_100m.py', 'scripts/review_textbook_quantity_comparison.py',
    'scripts/record_parameter_displacement_anchor_content.py')
reference, check_reference = probe.reference, probe.check_reference


def measured_budget(result):
    timing, estimate = probe.estimate_training(result)
    used = result['GPU_seconds']
    if not math.isfinite(used) or used < 0 or used + estimate > CEILING:
        raise ValueError('Own measured probe plus scientific estimate exceeds1800s')
    return timing, estimate, used, CEILING-used


def probe_evidence():
    p = probe.inspect(); job = read_json(RUN/'probe/job.json'); r = read_json(RUN/'probe/result.json')
    if (job['status'] != 'complete' or alive(job) or not r['passed']
            or r['GPU_seconds'] != job['GPU_elapsed_seconds'] or r['GPU_seconds'] > 180
            or r['config_sha256'] != sha256(probe.CONFIG) or not all(r['initial_preservation'].values())
            or not r['common_gate']['passed'] or not all(r['common_gate']['checks'].values())
            or set(r['selected_pair_gates']) != set(ARMS)
            or any(not g['passed'] or not all(g['checks'].values()) for g in r['selected_pair_gates'].values())
            or any(not all(checks.values()) for checks in r['reference_readonly_checks'].values())
            or r['selected_pair_batch'] not in p['pair_batch_candidates']
            or r['verification_updates'] != 152 or r['scientific_teacher_tokens'] != 0):
        raise ValueError('Own completed native CUDA/common and both-objective restart evidence required')
    matched_exposure(*(v['histories'] for v in r['selected_timings'].values()))
    timing, estimate, used, budget = measured_budget(r)
    if timing != r['measured_timing'] or estimate != r['estimated_science_GPU_seconds']:
        raise ValueError('Own measured timing differs')
    return p, r, timing, estimate, used, budget


def freeze():
    if CONFIG.exists(): inspect(); return
    started = time.monotonic(); p, r, timing, estimate, used, budget = probe_evidence()
    old_path = ROOT/'configs/phase6/source_order_condition_comparison_v2.json'; old = read_json(old_path)
    tests = ROOT/'reports/phase6/base_preference_science_tests.xml'; suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 3 or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped')):
        raise ValueError('Actual budget/common and both-branch accounting checks required')
    refs = dict(old['references'], own_probe_config=reference(probe.CONFIG), own_probe_result=reference(RUN/'probe/result.json'),
        CPU_science_tests=reference(tests), proposal=reference(PROPOSAL), content_review=p['references']['content_review'],
        strong_config=reference(old_path))
    # Selection uses the actual previously qualified strongest screen, not an upstream cached parent.
    refs['strong_result'] = reference(ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006/compare-result.json')
    refs['strong_notes'] = reference(ROOT/'reports/phase6/source_order_condition_notes.json')
    c = dict(kind=KIND, phase='scientific', parent=p['parent'], pairs=p['pairs'], preferred_pair_ids=p['preferred_pair_ids'],
        original_config=p['original_config'], original_web=p['original_web'], references=refs,
        common_teacher_tokens=COMMON, pair_teacher_tokens=PAIR, new_scientific_positive_teacher_tokens=TOTAL,
        teacher_tokens_per_arm=COMMON+PAIR, arms=ARMS, beta=.1, LR=LR, pair_batch=r['selected_pair_batch'],
        reference_policy='Exact readonly shared6M native endpoint; same full56 grouped BF16 math sums, cached once; no optimizer/RNG change.',
        old_source_sha256={**p['old_source_sha256'], **p['source_sha256'], **{s:sha256(ROOT/s) for s in EVALUATION_SOURCES}},
        source_sha256={s:sha256(ROOT/s) for s in SOURCES}, implementation=implementation_hashes(),
        verification_GPU_seconds=used, verification_teacher_tokens=r['verification_teacher_tokens'],
        diagnostic_GPU_seconds_separate=p['diagnostic_GPU_seconds_separate'], measured_timing=timing,
        estimated_GPU_seconds_with_margin=estimate, GPU_budget_seconds=budget, total_new_GPU_ceiling_seconds=CEILING,
        save_every_updates=250, CPU_preparation_seconds=time.monotonic()-started,
        quality_criteria_unchanged=True, Base_complete=False, Base_adopted=False, protected_test_used=False, Chat_started=False, quantization_started=False)
    if c['CPU_preparation_seconds'] > 30: raise TimeoutError('CPU scientific freeze30s exhausted')
    atomic_json(CONFIG, c); inspect(); print(dict(status='Base_preference_science_frozen', estimated_total_GPU_seconds=used+estimate))


def inspect():
    c = read_json(CONFIG); p, r, timing, estimate, used, budget = probe_evidence()
    if (c['kind'] != KIND or c['phase'] != 'scientific' or c['parent'] != p['parent'] or c['pairs'] != p['pairs']
            or c['preferred_pair_ids'] != p['preferred_pair_ids'] or c['original_web'] != p['original_web'] or c['original_config'] != p['original_config']
            or c['common_teacher_tokens'] != COMMON or c['pair_teacher_tokens'] != PAIR or c['new_scientific_positive_teacher_tokens'] != TOTAL
            or c['teacher_tokens_per_arm'] != COMMON+PAIR or c['arms'] != ARMS or c['beta'] != .1 or c['LR'] != LR
            or c['pair_batch'] != r['selected_pair_batch'] or c['implementation'] != implementation_hashes()
            or c['verification_GPU_seconds'] != used or c['GPU_budget_seconds'] != budget or c['total_new_GPU_ceiling_seconds'] != CEILING
            or c['measured_timing'] != timing or c['estimated_GPU_seconds_with_margin'] != estimate or c['save_every_updates'] != 250
            or not c['quality_criteria_unchanged'] or any(c[k] for k in ('Base_complete', 'Base_adopted', 'protected_test_used', 'Chat_started', 'quantization_started'))):
        raise ValueError('Frozen exact native Base preference scope differs')
    for name, digest in {**c['old_source_sha256'], **c['source_sha256']}.items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'], c['pairs'], c['original_config'], *c['references'].values()): check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')): raise ValueError('Actual live science; no duplicate')
    return c


def binding(c, arm, parent=None, cache=None):
    return dict(config_sha256=sha256(CONFIG), arm=arm, parent=parent or c['parent'], original_parent=c['parent'],
        reference_cache=cache, study_kind=KIND, optimizer_policy='inherit_native', scientific=True,
        positive_teacher_goal=COMMON if arm == 'common_Web' else PAIR, DPO_coefficient=ARMS.get(arm, 0.))


def detail(trainer, checkpoint, b, seconds):
    return dict(checkpoint=str(checkpoint), checkpoint_sha256=sha256(checkpoint), binding=b,
        update=trainer.update, tokens=trainer.tokens, supervised_tokens=trainer.supervised_tokens,
        additional_supervised_tokens=trainer.supervised_tokens-trainer.lineage['parent_supervised_tokens'],
        additional_input_tokens=trainer.tokens-trainer.lineage['parent_tokens'], sampler=trainer.sampler.state_dict(),
        token_digest=trainer.token_digest, focus_token_digest=trainer.focus_token_digest,
        training_seconds=seconds, unique_parameters=sum(p.numel() for p in trainer.model.parameters()))


def learn(build, parent, arm, goal, heartbeat, check):
    folder=RUN/arm/'training'; folder.mkdir(parents=True, exist_ok=True); trainer=build(); checkpoint=prior.latest(folder)
    if checkpoint is not None: trainer.load(checkpoint)
    log=folder/'metrics.jsonl'; seconds=prior.reconcile(log, trainer.update, parent['update'])
    common=arm == 'common_Web'
    with log.open('a', buffering=1) as stream:
        while (trainer.sampler.source_teachers['web'] if common else trainer.sampler.teachers) != goal:
            try: check()
            except (InterruptedError, TimeoutError): trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt'); raise
            row=trainer.step(); seconds+=row['seconds']; stream.write(json.dumps(row, allow_nan=False)+'\n')
            if trainer.sampler.position%20 == 0: heartbeat(arm+'-training', teachers=row['additional_teacher_tokens'], teacher_budget=goal, loss=row['loss'])
            if trainer.sampler.position%250 == 0: trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
    checkpoint=folder/f'checkpoint-{trainer.update:08d}.pt'; trainer.save(checkpoint)
    state=torch.load(checkpoint, map_location='cpu', weights_only=False)
    if not finite_state(state): raise ValueError('Finite full terminal state required')
    record=detail(trainer, checkpoint, trainer.binding, seconds)
    del trainer, state; gc.collect(); torch.cuda.empty_cache(); return record


def run():
    c=inspect(); RUN.mkdir(parents=True, exist_ok=True); jp=RUN/'job.json'; old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256'] != sha256(CONFIG): raise ValueError('Interrupted recipe differs')
    if old.get('status') == 'complete': print('Completed Base comparison retained'); return
    previous=old.get('GPU_elapsed_seconds', 0.); started=None; stopped=[False]
    job=dict(status='setup', **identity(), config_sha256=sha256(CONFIG), started_at=old.get('started_at', now()),
        GPU_elapsed_seconds=previous, restart_command='scripts/run_base_preference_comparison.ps1 -Worker')
    for sig in (signal.SIGINT, signal.SIGTERM): signal.signal(sig, lambda *_:stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('Base comparison interrupted; completed updates saved')
        if started is not None and previous+time.monotonic()-started > c['GPU_budget_seconds']: raise TimeoutError('Cumulative Base comparison budget exhausted')
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started is not None: job['GPU_elapsed_seconds']=previous+time.monotonic()-started
        atomic_json(jp, job)
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False; torch.backends.cudnn.allow_tf32=False; heartbeat('setup')
        for relative in (*c['source_sha256'], *c['old_source_sha256'], CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != (ROOT/relative).read_bytes(): raise ValueError('Frozen snapshot differs')
            if not target.exists(): shutil.copyfile(ROOT/relative, target)
        parent=torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        web=TrainView(c['original_web']['path'], c['original_web']['manifest_sha256']); pairs=probe.pairs(c)
        base=read_json(Path(c['original_config']['path'])); common_binding=binding(c, 'common_Web')
        with gpu_lock('cuda'):
            started=time.monotonic(); job['status']='running'; heartbeat('GPU')
            progress=RUN/'progress-result.json'; result=read_json(progress) if progress.exists() else dict(checkpoints={}, evaluations={}, transfer={}, retention={})
            if 'common_Web' not in result['checkpoints']:
                result['checkpoints']['common_Web']=learn(lambda:CommonWebTrainer(parent, web, COMMON, common_binding), parent, 'common_Web', COMMON, heartbeat, check)
                atomic_json(progress, result)
            common=result['checkpoints']['common_Web']; common_ref=dict(path=common['checkpoint'], sha256=common['checkpoint_sha256']); check_reference(common_ref)
            shared=torch.load(common_ref['path'], map_location='cpu', weights_only=False)
            cache_path=RUN/'shared-reference.json'
            if not cache_path.exists():
                heartbeat('readonly-shared6M-reference'); trainer=CommonWebTrainer(shared, web, COMMON, common_binding)
                before=rng_state(); cache=build_reference(trainer.model, PairQuotaSampler(pairs, PAIR, c['pair_batch'], web.byte_lengths, 'unused'), 'cuda', 'bf16')
                checks=dict(weights_unchanged=equal_state(host_state(trainer.model.state_dict()), shared['model']), RNG_restored=equal_state(rng_state(), before), no_gradients=all(p.grad is None for p in trainer.model.parameters()))
                if not all(checks.values()): raise ValueError('Readonly scientific reference modified weights/RNG')
                atomic_json(cache_path, dict(config_sha256=sha256(CONFIG), parent=common_ref, reference=cache, checks=checks, scientific_teacher_tokens=0, optimizer_updates=0))
                del trainer; gc.collect(); torch.cuda.empty_cache()
            cached=read_json(cache_path); cache_ref=reference(cache_path)
            if cached['parent'] != common_ref or cached['config_sha256'] != sha256(CONFIG) or not all(cached['checks'].values()): raise ValueError('Actual shared6M reference differs')
            result['reference_cache']=cache_ref; result['shared_parent']=common_ref
            for arm, coefficient in ARMS.items():
                b=binding(c, arm, common_ref, cache_ref)
                if arm not in result['checkpoints']:
                    result['checkpoints'][arm]=learn(lambda:PairPreferenceTrainer(shared, web, pairs, PAIR, coefficient, cached['reference'], b, batch=c['pair_batch']), shared, arm, PAIR, heartbeat, check)
                    atomic_json(progress, result)
            histories=[[json.loads(v) for v in (RUN/arm/'training/metrics.jsonl').read_text().splitlines()] for arm in ARMS]
            result['matched_exposure']=matched_exposure(*histories)
            for arm in ARMS:
                b=result['checkpoints'][arm]['binding']
                if arm not in result['evaluations']:
                    evaluation.RUN=RUN/'evaluation'
                    result['evaluations'][arm]=evaluation.evaluate(arm, result['checkpoints'][arm], Shard(Path(base['dev_shards']), 'dev'), Tokenizer(ROOT/base['tokenizer']), base, b, heartbeat, check, started+c['GPU_budget_seconds']-previous)
                    atomic_json(progress, result)
                prior.RUN=RUN; prior.CONFIG=CONFIG; record=result['checkpoints'][arm]; cp=dict(path=record['checkpoint'], sha256=record['checkpoint_sha256'])
                for suite, key in (('bridge', 'transfer'), ('retention', 'retention')):
                    if arm not in result[key]: result[key][arm]=prior.transfer_scores(c, arm, cp, heartbeat, check, suite); atomic_json(progress, result)
            check(); elapsed=previous+time.monotonic()-started
            result.update(status='Base_preference_GPU_complete_pending_all160_content', config_sha256=sha256(CONFIG), GPU_seconds=elapsed,
                scientific_positive_teacher_tokens=TOTAL, common_positive_teacher_tokens=COMMON, positive_teacher_tokens_per_arm=COMMON+PAIR,
                evaluation_model_class='JMicroModel', Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
                protected_test_used=False, quality_criteria_unchanged=True)
            atomic_json(RUN/'compare-result.json', result); job.update(status='complete', GPU_elapsed_seconds=elapsed, completed_at=now())
    except BaseException as exc: job.update(status='failed_or_interrupted', error=repr(exc)); raise
    finally:
        if started is not None and job['status'] != 'complete': job['GPU_elapsed_seconds']=previous+time.monotonic()-started
        atomic_json(jp, job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(); m=parser.add_mutually_exclusive_group(); m.add_argument('--freeze', action='store_true'); m.add_argument('--inspect', action='store_true'); args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect(); print('Measured Base preference science valid; GPU0')
    else: run()
