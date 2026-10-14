"""Durable declared same-budget cross-GQA architecture comparison; TEST unopened."""
import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
import torch
from jmicro.experiment import sha256, now
from jmicro.training import atomic_json, gpu_lock
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.evaluation_choice_boundary import load_choices
from jmicro.isolated_japanese_scoring import load_unigram
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from cross_gqa_map_trainer import CrossGQAMapTrainer, POLICY as RECIPE, committed_state
from cross_gqa_map_science_protocol import science_budget, matched_original, validate_history
from evaluate_context_likelihood import evaluate
from phase6_performance import identity, alive
from probe_context_likelihood import weights_digest, passed_tests

RUN = ROOT / 'reports/phase6/cross-gqa-map-science-20261015'
CONFIG = ROOT / 'configs/phase6/cross_gqa_map_science_20261015.json'
PROBE = ROOT / 'reports/phase6/cross-gqa-map-probe-20261015'
PREP = ROOT / 'reports/phase6/cross-gqa-map-preparation-20261015'
SOURCES = ('scripts/run_cross_gqa_map.py', 'scripts/run_cross_gqa_map.ps1',
    'scripts/review_cross_gqa_map.py', 'scripts/evaluate_context_likelihood.py',
    'scripts/cross_gqa_map_science_protocol.py', 'tests/test_cross_gqa_map_science.py',
    'src/jmicro/isolated_japanese_scoring.py', 'src/jmicro/evaluation_choice_boundary.py',
    'src/jmicro/evaluation_boundary.py', 'src/jmicro/evaluation_memory.py',
    'src/jmicro/japanese_evaluation.py', 'src/jmicro/readiness.py', 'src/jmicro/shards.py',
    'scripts/isolated_base_evaluation.py', 'scripts/base_fim_pilot_protocol.py',
    'scripts/review_matched_story_study.py', 'scripts/run_eos_complete_100m.py')


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def binding(c, pin):
    return dict(config_sha256=pin, parent=c['parent'], source_binding=c['source_binding'],
                training_seed=42, weights_role='scientific_cross_GQA_map', probe_weights_used=False)


def build(c, b):
    parent = torch.load(c['parent']['path'], map_location='cpu', weights_only=False)
    codec = Tokenizer(c['tokenizer']['path'])
    source = c['source_binding']
    sampler = OriginalTrainCorpusSampler(source['pool'], source['manifest_sha256'], codec, c['goals'], seed=42)
    if sampler.binding != source:
        raise ValueError('Accepted original TRAIN identity differs')
    return CrossGQAMapTrainer(parent, sampler, b, batch=48, device='cuda', seed=42)


def freeze():
    if CONFIG.exists() or (RUN / 'job.json').exists():
        raise ValueError('Preserve a frozen/started science contract')
    probe, job = (json.loads((PROBE / name).read_text()) for name in ('result.json', 'job.json'))
    if job['status'] != 'complete' or alive(job) or not probe['cumulative_GPU_ledger_closed']:
        raise ValueError('Actual completed and exited owned CUDA gate required')
    budget = science_budget(probe)
    pc = ROOT / 'configs/phase6/cross_gqa_map_probe_20261015.json'
    p = json.loads(pc.read_text())
    if probe['config_sha256'] != sha256(pc):
        raise ValueError('Actual owned CUDA configuration changed')
    for path, pin in p['sources'].items():
        if sha256(ROOT / path) != pin:
            raise ValueError('Actual CUDA-verified source changed: ' + path)
    workflow = PREP / 'science_CPU_tests.xml'
    passed_tests(workflow, 18)
    old = json.loads(Path(p['accepted_config']['path']).read_text())
    policy = json.loads((ROOT / 'configs/phase6/base_document_balance_review.json').read_text())
    references = dict(policy['references'])
    train_path = ROOT / 'reports/phase6/natural-context-contrast-comparison-20261007/CE/train-result.json'
    control = json.loads(train_path.read_text())
    cp = Path(control['checkpoint'])
    if sha256(cp) != control['checkpoint_sha256']:
        raise ValueError('Exact cached native CE control changed')
    state = torch.load(cp, map_location='cpu', weights_only=False)
    if (state['spec']['contrast'] or state['spec']['batch'] != 48 or state['spec']['seed'] != 42
            or state['counters']['supervised_tokens'] != 100000000
            or state['sampler']['binding'] != old['source_binding']):
        raise ValueError('Actual matched original CE100M protocol required')
    for row in references.values():
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Existing baseline reference changed')
    dev = ROOT / 'eval/isolated-base-dev-v1/base.dev.manifest.json'
    dev_pin = '6198b43df8f4cf389e9de74c038e2e93d18665413477b27359ab352a02f69fa7'
    load_dev_suite(dev, dev_pin)
    japanese = Path('/home/aihub_ubuntu/jmicro-data/evaluation-isolated-japanese-v1/japanese.dev.manifest.json')
    jp_pin = '06fcf2c18f086ee57c4f615e5ae765f568024912148bf94be891b1581e7edadd'
    for task in ('semantics', 'jblimp', 'jcqa'):
        load_choices(japanese, jp_pin, task)
    unigram = ROOT / 'reports/phase6/japanese-base-v2-20261004-r1/pilot/unigram.json'
    unigram_pin = '80708c01ae19d6049785dd31d1e48651e1f246122870355a9ab5ad662081d0a5'
    load_unigram(unigram, unigram_pin)
    c = dict(kind='frozen_native_original100M_cross_gqa_map_science_v1', created_at=now(),
        proposal=p['proposal'], probe_config=ref(pc), probe_result=ref(PROBE / 'result.json'),
        parent=p['parent'], tokenizer=p['tokenizer'], source_binding=old['source_binding'], goals=old['goals'],
        batch=48, seed=42, main_teacher_goal=100000000, recipe=RECIPE,
        initial_weights_sha256=p['initial_weights_sha256'],
        scientific_GPU_cap_seconds=budget, technical_GPU_seconds=probe['GPU_occupancy_seconds'],
        total_GPU_cap_seconds=4800, worst_measured_peak_bytes=probe['CE_capacity']['peak_VRAM_bytes'],
        native_reference_parameters=10001152, candidate_parameters=10001204,
        architecture_comparison='Original native CE baseline versus tagged cross-GQA map model with52 new zero-initialized scalars. Same original base config/weights/function, source and main CE; not identical inference architectures or equal physical parameter counts.',
        control_checkpoint=ref(cp), control_training=ref(train_path), references=references,
        strong_summary=policy['strong_summary'],
        DEV_manifest=dict(path=str(dev), sha256=dev_pin),
        DEV_shards=dict(path=old['dev_shards'], manifest_sha256=old['dev_manifest_sha256']),
        Japanese_manifest=dict(path=str(japanese), sha256=jp_pin), unigram=dict(path=str(unigram), sha256=unigram_pin),
        sources={**p['sources'], **{path: sha256(ROOT / path) for path in SOURCES}},
        CPU_workflow_tests=ref(workflow), checkpoints_every_updates=500, heartbeat_every_updates=20,
        scope='Base only. Qualified recipe precedes genuinely fresh whole-recipe seed43/fullDEV/all440/new sealedTEST/adoption.',
        failure='Fixed condition closes on data/numeric/state/budget/quality failure; no parameter/source/seed/parent/decoder/cap rescue.',
        quality_criteria_unchanged=True, TEST_prepared=False, Base_qualified=False, Base_adopted=False)
    atomic_json(CONFIG, c)
    print(json.dumps(dict(status='science_contract_frozen_not_started', main_teachers=100000000,
                         science_GPU_seconds=budget, total_limit_seconds=4800)), flush=True)


def inspect():
    c = json.loads(CONFIG.read_text())
    if (c['kind'] != 'frozen_native_original100M_cross_gqa_map_science_v1' or c['recipe'] != RECIPE
            or c['batch'] != 48 or c['seed'] != 42 or c['main_teacher_goal'] != 100000000
            or c['TEST_prepared'] is not False or c['Base_adopted'] is not False
            or c['total_GPU_cap_seconds'] != 4800
            or c['native_reference_parameters'] != 10001152 or c['candidate_parameters'] != 10001204):
        raise ValueError('Exact frozen Base scope required')
    for path, pin in c['sources'].items():
        if sha256(ROOT / path) != pin:
            raise ValueError('Frozen scientific source changed: ' + path)
    for key in ('proposal', 'probe_config', 'probe_result', 'parent', 'tokenizer', 'control_checkpoint', 'control_training'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Frozen science reference changed: ' + key)
    if science_budget(json.loads(Path(c['probe_result']['path']).read_text())) != c['scientific_GPU_cap_seconds']:
        raise ValueError('Measured science budget changed')
    for row in c['references'].values():
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Original baseline reference changed')
    load_dev_suite(c['DEV_manifest']['path'], c['DEV_manifest']['sha256'])
    if (RUN / 'job.json').exists():
        job = json.loads((RUN / 'job.json').read_text())
        if (alive(job) or job['status'] != 'interrupted' or not job['cumulative_GPU_ledger_closed']
                or job['config_sha256'] != sha256(CONFIG)
                or job['GPU_occupancy_seconds'] >= c['scientific_GPU_cap_seconds']):
            raise ValueError('Only a stopped valid interruption with closed remaining budget may resume')
    return c


class StopRequested(Exception):
    pass


def run():
    c = inspect()
    pin = sha256(CONFIG)
    b = binding(c, pin)
    RUN.mkdir(parents=True, exist_ok=True)
    previous = json.loads((RUN / 'job.json').read_text()) if (RUN / 'job.json').exists() else None
    prior = previous['GPU_occupancy_seconds'] if previous else 0
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=pin, binding=b,
        GPU_occupancy_seconds=prior, cumulative_GPU_ledger_closed=False, update=0, main_teacher_positions=0)
    atomic_json(RUN / 'job.json', job)
    started = None
    trainer = log = None
    def check():
        if started is not None and prior + time.monotonic() - started > c['scientific_GPU_cap_seconds']:
            raise TimeoutError('Frozen scientific GPU budget exhausted; no extension')
    def stop(*args):
        raise StopRequested('External signal; preserve completed-update state and exact budget')
    def beat(stage, **extra):
        check()
        job.update(stage=stage, heartbeat_at=now(), GPU_occupancy_seconds=prior + time.monotonic() - started, **extra)
        atomic_json(RUN / 'job.json', job)
    def save():
        path = RUN / f"checkpoint-{trainer.counters['update']:08d}.pt"
        trainer.save(path)
        latest = dict(path=str(path), sha256=sha256(path), binding=b, update=trainer.counters['update'])
        atomic_json(RUN / 'latest.json', latest)
        return latest
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM, stop)
            signal.signal(signal.SIGINT, stop)
            configure_resident_memory(c['worst_measured_peak_bytes'])
            job['status'] = 'running'
            trainer = build(c, b)
            metrics = RUN / 'metrics.jsonl'
            if (RUN / 'latest.json').exists():
                latest = json.loads((RUN / 'latest.json').read_text())
                if latest['binding'] != b or sha256(Path(latest['path'])) != latest['sha256']:
                    raise ValueError('Frozen valid checkpoint required')
                trainer.load(latest['path'])
                rows = [json.loads(line) for line in metrics.read_text().splitlines()] if metrics.exists() else []
                retained = [r for r in rows if r['update'] <= trainer.counters['update']]
                validate_history(retained, trainer.state_dict())
                if len(retained) != len(rows):
                    atomic_json(RUN / f"discarded-post-checkpoint-metrics-{job['pid']}.json", dict(rows=rows[len(retained):]))
                    metrics.write_text(''.join(json.dumps(row) + '\n' for row in retained))
            else:
                if previous or weights_digest(trainer.state_dict()) != c['initial_weights_sha256']:
                    raise ValueError('Science starts only from original parent, never verification weights')
                save()
            log = metrics.open('a', buffering=1)
            while not trainer.sampler.exhausted:
                check()
                row = trainer.step()
                log.write(json.dumps(row) + '\n')
                if row['update'] % 500 == 0:
                    save()
                if row['update'] % 20 == 0:
                    beat('learning', update=row['update'], main_teacher_positions=row['supervised_tokens'])
            log.close()
            log = None
            latest = save()
            state = host(trainer.state_dict())
            rows = [json.loads(line) for line in metrics.read_text().splitlines()]
            physical = validate_history(rows, state)
            control = torch.load(c['control_checkpoint']['path'], map_location='cpu', weights_only=False)
            checks = matched_original(state, control, physical['CE_physical_inputs'])
            if not all(checks.values()) or state['counters']['supervised_tokens'] != 100000000:
                raise ValueError('Terminal exact original100M/control stream differs')
            record = dict(status='complete', checkpoint=latest['path'], checkpoint_sha256=latest['sha256'], binding=b,
                counters=state['counters'], original_CE_match=checks, physical_rollup=physical,
                auxiliary_digest=state['counters']['auxiliary_digest'],
                model_config=state['model_config'], spec=state['spec'], lineage=state['lineage'])
            atomic_json(RUN / 'training.json', record)
            beat('evaluation')
            ev = evaluate(trainer, c, record, RUN / 'evaluation', beat, check)
            check()
            elapsed = prior + time.monotonic() - started
            result = dict(status='complete', config_sha256=pin, binding=b, actual_identity=identity(),
                training=record, evaluation=ev, scientific_CE_teacher_positions=100000000,
                GPU_occupancy_seconds=elapsed, total_GPU_seconds_including_probe=elapsed + c['technical_GPU_seconds'],
                content_review_completed=False, TEST_opened=False, Base_qualified=False, Base_adopted=False)
            atomic_json(RUN / 'result.json', result)
            job.update(status='complete', ended_at=now(), GPU_occupancy_seconds=elapsed,
                       cumulative_GPU_ledger_closed=True, update=trainer.counters['update'], main_teacher_positions=100000000)
            atomic_json(RUN / 'job.json', job)
            print('Original100M learning/isolated evaluation complete; all80 content review pending', flush=True)
    except BaseException as error:
        if log is not None:
            log.close()
        if trainer is not None and not trainer._step_in_progress:
            try:
                save()
            except Exception:
                pass
        elapsed = prior + (time.monotonic() - started if started is not None else 0)
        job.update(status='interrupted' if isinstance(error, StopRequested) else 'failed',
            error_type=type(error).__name__, error=str(error), ended_at=now(), GPU_occupancy_seconds=elapsed,
            cumulative_GPU_ledger_closed=True)
        atomic_json(RUN / 'job.json', job)
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('freeze', 'inspect', 'run'))
    args = parser.parse_args()
    if args.action == 'freeze':
        freeze()
    elif args.action == 'inspect':
        inspect()
        print('Frozen scientific preflight passed; no GPU')
    else:
        run()
