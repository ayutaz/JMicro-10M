"""One inherited native news fork; common Web prefix and control are reused."""
import argparse
import copy
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
from jmicro.training import atomic_json, implementation_hashes, gpu_lock
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from livedoor_base_trainer import NewsBaseTrainer, KIND, LR, SOURCE_ORDER
from phase6_performance import identity, alive, finite_state
import probe_livedoor_base as probe
import run_source_order_condition_comparison_v2 as prior
import run_complete_text_comparison as evaluation

RUN = probe.RUN
CONFIG = ROOT/'configs/phase6/livedoor_base_comparison.json'
PROPOSAL = probe.PROPOSAL
ARM = 'authored_news'
GOALS = dict(web=1428122, authored_news=25000000)
TOTAL = sum(GOALS.values())
REUSED = 73571878
CEILING = 1800
SOURCES = ('scripts/run_livedoor_base.py', 'scripts/run_livedoor_base.ps1',
    'scripts/review_livedoor_base.py', 'scripts/livedoor_base_accounting.py',
    'scripts/record_livedoor_base_content.py', 'tests/test_livedoor_base_science.py')
reference, check_reference = probe.reference, probe.check_reference


def measured_budget(result, previous_failure):
    timing, estimate = probe.estimate_training(result)
    used = result['GPU_seconds'] + previous_failure
    if not math.isfinite(used) or used < 0 or used + estimate > CEILING:
        raise ValueError('Measured probe plus scientific estimate exceeds1800s')
    return timing, estimate, used, CEILING-used


def probe_evidence():
    p = probe.inspect(); job = read_json(RUN/'probe/job.json'); r = read_json(RUN/'probe/result.json')
    if (job['status'] != 'complete' or alive(job) or not r['passed']
            or r['GPU_seconds'] != job['GPU_elapsed_seconds'] or r['GPU_seconds'] > 120
            or r['config_sha256'] != sha256(probe.CONFIG) or not all(r['initial_preservation'].values())
            or set(r['gates']) != {'original_Web', 'news_boundary_stress'}
            or any(not g['passed'] or not all(g['checks'].values()) for g in r['gates'].values())
            or r['verification_updates'] != 80):
        raise ValueError('Own completed both-source inherited CUDA/restart evidence required')
    timing, estimate, used, budget = measured_budget(r, p['previous_failed_GPU_seconds'])
    if timing != r['measured_timing'] or estimate != r['estimated_science_GPU_seconds']:
        raise ValueError('Own timing record differs')
    return p, r, timing, estimate, used, budget


def freeze():
    if CONFIG.exists(): inspect(); return
    started = time.monotonic(); p, r, timing, estimate, used, budget = probe_evidence()
    old = read_json(Path(p['references']['cached_control_config']['path']))
    tests = ROOT/'reports/phase6/livedoor_base_science_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 3 or any(int(s.attrib[k]) for s in suites for k in ('failures', 'errors', 'skipped')):
        raise ValueError('Actual budget/prefix/accounting CPU checks required')
    c = dict(research_kind=KIND, phase='scientific', parent=p['parent'], original_parent=p['original_parent'], data=p['data'],
        original_config=old['original_config'], original_web=p['data']['original_web'],
        teacher_goals=GOALS, source_order=list(SOURCE_ORDER), shapes=old['shapes'], LR=LR, unique_parameters=10001152,
        new_scientific_teacher_tokens=TOTAL, reused_prefix_teacher_tokens=REUSED, total_teacher_tokens_from_original_parent=TOTAL+REUSED,
        references=dict(old['references'], **p['references'], own_probe_config=reference(probe.CONFIG),
            own_probe_result=reference(RUN/'probe/result.json'), CPU_science_tests=reference(tests)),
        old_source_sha256={**p['old_source_sha256'], **p['source_sha256']}, source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        implementation=implementation_hashes(), verification_GPU_seconds=used, verification_teacher_tokens=r['verification_teacher_tokens'],
        measured_timing=timing, estimated_GPU_seconds_with_margin=estimate, GPU_budget_seconds=budget,
        save_every_updates=250, total_new_GPU_ceiling_seconds=CEILING, CPU_preparation_seconds=time.monotonic()-started,
        quality_criteria_unchanged=True, Base_complete=False, Base_adopted=False, protected_test_used=False, Chat_started=False, quantization_started=False)
    if c['CPU_preparation_seconds'] > 30: raise TimeoutError('CPU science freeze30s exhausted')
    atomic_json(CONFIG, c); inspect(); print(dict(status='news_science_frozen', estimated_total_GPU_seconds=used+estimate))


def inspect():
    c = read_json(CONFIG); p, r, timing, estimate, used, budget = probe_evidence()
    if (c['research_kind'] != KIND or c['phase'] != 'scientific' or c['parent'] != p['parent'] or c['original_parent'] != p['original_parent']
            or c['data'] != p['data'] or c['teacher_goals'] != GOALS or c['source_order'] != list(SOURCE_ORDER)
            or c['new_scientific_teacher_tokens'] != TOTAL or c['reused_prefix_teacher_tokens'] != REUSED
            or c['total_teacher_tokens_from_original_parent'] != 100000000 or c['LR'] != LR or c['unique_parameters'] != 10001152
            or c['shapes'] != dict(context=1024, batch=32, accumulation=1, backend='flash', compile_mode='reduce-overhead', dtype='bf16')
            or c['total_new_GPU_ceiling_seconds'] != CEILING or c['GPU_budget_seconds'] != budget or c['verification_GPU_seconds'] != used
            or c['verification_teacher_tokens'] != r['verification_teacher_tokens'] or c['measured_timing'] != timing
            or c['estimated_GPU_seconds_with_margin'] != estimate or c['implementation'] != implementation_hashes() or c['save_every_updates'] != 250
            or not c['quality_criteria_unchanged'] or any(c[k] for k in ('Base_complete', 'Base_adopted', 'protected_test_used', 'Chat_started', 'quantization_started'))):
        raise ValueError('Frozen native news scientific scope differs')
    for name, digest in {**c['old_source_sha256'], **c['source_sha256']}.items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'], c['original_parent'], c['original_config'], *c['references'].values()): check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')): raise ValueError('Actual live science; no duplicate')
    return c


def binding(c):
    return dict(config_sha256=sha256(CONFIG), arm=ARM, parent=c['parent'], original_parent=c['original_parent'],
        teacher_goals=GOALS.copy(), study_kind=KIND, optimizer_policy='inherit_native', scientific=True)


def common_web_continuation(rows, control_rows, parent):
    indexed = {v['update']:v for v in control_rows}; count = 0
    for row in rows:
        if row['source_teachers']['authored_news']: break
        old = indexed[row['update']]
        if (old['source_teachers']['web'] != REUSED+row['source_teachers']['web']
                or any(old['source_teachers'][k] for k in ('story', 'ordinary_textbook', 'conditional_textbook'))
                or any(row[k] != old[k] for k in ('tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest', 'focus_token_digest', 'lr', 'loss', 'gradient_norm'))):
            raise ValueError('Shared actual pure-Web continuation differs')
        count += 1
    if parent['sampler']['source_teachers']['web'] != REUSED: raise ValueError('Actual common-prefix ledger differs')
    return count


def run():
    c = inspect(); RUN.mkdir(parents=True, exist_ok=True); jp = RUN/'job.json'; old_job = read_json(jp) if jp.exists() else {}
    if old_job and old_job['config_sha256'] != sha256(CONFIG): raise ValueError('Interrupted recipe differs')
    if old_job.get('status') == 'complete': print('Completed science retained'); return
    previous = old_job.get('GPU_elapsed_seconds', 0.); started = None; stopped = [False]
    job = dict(status='setup', **identity(), config_sha256=sha256(CONFIG), started_at=old_job.get('started_at', now()),
        GPU_elapsed_seconds=previous, restart_command='scripts/run_livedoor_base.ps1 -Worker')
    for sig in (signal.SIGINT, signal.SIGTERM): signal.signal(sig, lambda *_:stopped.__setitem__(0, True))
    def check():
        if stopped[0]: raise InterruptedError('News science interrupted; completed updates saved')
        if started is not None and previous+time.monotonic()-started > c['GPU_budget_seconds']: raise TimeoutError('Cumulative news GPU budget exhausted')
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started is not None: job['GPU_elapsed_seconds'] = previous+time.monotonic()-started
        atomic_json(jp, job)
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False; torch.backends.cudnn.allow_tf32=False; heartbeat('setup')
        for relative in (*c['source_sha256'], *c['old_source_sha256'], CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/relative; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and target.read_bytes() != (ROOT/relative).read_bytes(): raise ValueError('Snapshot differs')
            if not target.exists(): shutil.copyfile(ROOT/relative, target)
        parent=torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
        web=TrainView(c['data']['original_web']['path'], c['data']['original_web']['manifest_sha256'])
        news=TrainView(c['data']['news_pool'], c['data']['news_manifest_sha256'])
        base=read_json(Path(c['original_config']['path'])); b=binding(c)
        with gpu_lock('cuda'):
            started=time.monotonic(); job['status']='running'; heartbeat('GPU')
            progress=RUN/'progress-result.json'; result=read_json(progress) if progress.exists() else dict(checkpoints={}, evaluations={}, transfer={}, retention={})
            if ARM not in result['checkpoints']:
                folder=RUN/ARM/'training'; folder.mkdir(parents=True, exist_ok=True)
                trainer=NewsBaseTrainer(parent, web, news, GOALS, b); checkpoint=prior.latest(folder)
                if checkpoint is not None: trainer.load(checkpoint)
                log=folder/'metrics.jsonl'; seconds=prior.reconcile(log, trainer.update, parent['update'])
                with log.open('a', buffering=1) as stream:
                    while trainer.sampler.source_teachers != GOALS:
                        try: check()
                        except (InterruptedError, TimeoutError): trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt'); raise
                        row=trainer.step(); seconds+=row['seconds']; stream.write(json.dumps(row, allow_nan=False)+'\n')
                        if trainer.sampler.position%20 == 0: heartbeat('native-news-Base-training', teachers=row['additional_teacher_tokens'], teacher_budget=TOTAL, loss=row['loss'], source_teachers=row['source_teachers'])
                        if trainer.sampler.position%250 == 0: trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                checkpoint=folder/f'checkpoint-{trainer.update:08d}.pt'; trainer.save(checkpoint)
                if not finite_state(torch.load(checkpoint, map_location='cpu', weights_only=False)): raise ValueError('Finite terminal state required')
                rows=[json.loads(s) for s in log.read_text().splitlines()]
                matched=common_web_continuation(rows, [json.loads(s) for s in Path(c['references']['cached_control_history']['path']).read_text().splitlines()], parent)
                result['checkpoints'][ARM]=dict(prior.detail(trainer, checkpoint, b, seconds), sampler=trainer.sampler.state_dict(),
                    source_body_bytes=trainer.sampler.source_body_bytes.copy(), token_digest=trainer.token_digest, model_config=trainer.model.config,
                    unique_parameters=sum(p.numel() for p in trainer.model.parameters()), reused_prefix_teacher_tokens=REUSED,
                    total_teacher_tokens_from_original_parent=100000000, pure_Web_continuation_matched_updates=matched)
                atomic_json(progress, result); del trainer; gc.collect(); torch.cuda.empty_cache()
            if ARM not in result['evaluations']:
                evaluation.RUN=RUN/'evaluation'; dev=Shard(Path(base['dev_shards']), 'dev'); tok=Tokenizer(ROOT/base['tokenizer'])
                result['evaluations'][ARM]=evaluation.evaluate(ARM, result['checkpoints'][ARM], dev, tok, base, b, heartbeat, check, started+c['GPU_budget_seconds']-previous)
                atomic_json(progress, result)
            prior.RUN=RUN; prior.CONFIG=CONFIG
            checkpoint=dict(path=result['checkpoints'][ARM]['checkpoint'], sha256=result['checkpoints'][ARM]['checkpoint_sha256'])
            for suite, key in (('bridge', 'transfer'), ('retention', 'retention')):
                if ARM not in result[key]:
                    result[key][ARM]=prior.transfer_scores(c, ARM, checkpoint, heartbeat, check, suite); atomic_json(progress, result)
            check(); elapsed=previous+time.monotonic()-started
            result.update(status='news100M_GPU_complete_pending_all80_content', config_sha256=sha256(CONFIG), GPU_seconds=elapsed,
                scientific_teacher_tokens=TOTAL, reused_prefix_teacher_tokens=REUSED, total_teacher_tokens_from_original_parent=100000000,
                reused_control=c['references']['cached_control_result'], evaluation_model_class='JMicroModel', exact_same_scientific_sources_as_control=False,
                Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_used=False, quality_criteria_unchanged=True)
            atomic_json(RUN/'compare-result.json', result); job.update(status='complete', GPU_elapsed_seconds=elapsed, completed_at=now())
    except BaseException as exc: job.update(status='failed_or_interrupted', error=repr(exc)); raise
    finally:
        if started is not None and job['status'] != 'complete': job['GPU_elapsed_seconds']=previous+time.monotonic()-started
        atomic_json(jp, job)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(); m=parser.add_mutually_exclusive_group(); m.add_argument('--freeze', action='store_true'); m.add_argument('--inspect', action='store_true')
    args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect(); print('Measured news science valid; GPU0')
    else: run()
