"""Durable NEW control/candidate25M pilot; original native inference and TEST isolation."""
import argparse
import json
import os
from pathlib import Path
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from jmicro.document_progress import ARMS,POLICY
from jmicro.experiment import sha256,now
from jmicro.training import atomic_json,gpu_lock
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_boundary import load_dev_suite
from document_progress_trainer import DocumentProgressTrainer,committed_state
from document_progress_science_protocol import science_budget,validate_history,matched_original
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from evaluate_context_likelihood import evaluate
from phase6_performance import identity,alive
from probe_context_likelihood import weights_digest,passed_tests
from probe_document_progress import GOALS,observe_ui

RUN = ROOT/'reports/phase6/document-progress-science-20261015'
PREP = ROOT/'reports/phase6/document-progress-preparation-20261015'
PROBE = ROOT/'reports/phase6/document-progress-probe-20261015'
CONFIG = ROOT/'configs/phase6/document_progress_science_20261015.json'
SOURCES = ('scripts/run_document_progress.py','scripts/run_document_progress.ps1',
    'scripts/document_progress_science_protocol.py','scripts/review_document_progress.py',
    'tests/test_document_progress_science.py','scripts/evaluate_context_likelihood.py',
    'scripts/base_fim_pilot_protocol.py','scripts/isolated_base_evaluation.py',
    'scripts/independent_map_science_protocol.py','scripts/review_matched_story_study.py',
    'scripts/run_eos_complete_100m.py','src/jmicro/evaluation_boundary.py',
    'src/jmicro/evaluation_choice_boundary.py','src/jmicro/isolated_japanese_scoring.py',
    'src/jmicro/evaluation_memory.py','src/jmicro/japanese_evaluation.py','src/jmicro/readiness.py','src/jmicro/shards.py')


def ref(path):
    return dict(path=str(path),sha256=sha256(path))


def binding(c,pin,arm):
    return dict(config_sha256=pin,parent=c['parent'],source_binding=c['source_binding'],
        training_seed=42,weights_role='scientific_document_progress25M',arm=arm,probe_weights_used=False)


def build(c,b,arm):
    parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    codec = Tokenizer(c['tokenizer']['path'])
    source = c['source_binding']
    sampler = OriginalTrainCorpusSampler(source['pool'],source['manifest_sha256'],codec,GOALS,seed=42)
    if sampler.binding != source:
        raise ValueError('Accepted original TRAIN identity differs')
    return DocumentProgressTrainer(parent,sampler,b,batch=48,device='cuda',seed=42,arm=arm)


def freeze():
    if CONFIG.exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve an already frozen/started paired pilot')
    probe,job = (json.loads((PROBE/name).read_text()) for name in ('result.json','job.json'))
    if alive(job) or job['status'] != 'complete':
        raise ValueError('Actual exited owned paired gate required')
    budgets = science_budget(probe)
    pc = ROOT/'configs/phase6/document_progress_probe_20261015.json'
    p = json.loads(pc.read_text())
    if probe['config_sha256'] != sha256(pc):
        raise ValueError('Owned paired CUDA config changed')
    for path,pin in p['sources'].items():
        if sha256(ROOT/path) != pin:
            raise ValueError('Actual verified source differs: '+path)
    workflow = PREP/'science_CPU_tests.xml'
    passed_tests(workflow,28)
    old = json.loads(Path(p['accepted_config']['path']).read_text())
    previous = json.loads((ROOT/'configs/phase6/independent_map_science_20261015.json').read_text())
    for row in previous['references'].values():
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Original baseline metadata changed')
    c = dict(kind='frozen_native_document_progress_paired25M_science_v1',created_at=now(),
        proposal=p['proposal'],probe_config=ref(pc),probe_result=ref(PROBE/'result.json'),
        parent=p['parent'],parent_size=old['parent_size'],parent_mtime_ns=old['parent_mtime_ns'],
        tokenizer=p['tokenizer'],source_binding=old['source_binding'],goals=GOALS,arms=list(ARMS),
        batch=48,seed=42,main_teacher_goal_each=25000000,recipe=POLICY,
        initial_native_weights_sha256=probe['initial_native_weights_sha256'],
        native_parameters=10001152,train_only_parameters=256,training_parameters=10001408,
        science_GPU_caps_each=budgets,science_GPU_cap_total=sum(budgets.values()),
        carried_total_GPU_seconds=probe['cumulative_total_GPU_seconds'],
        carried_technical_GPU_seconds=probe['cumulative_technical_GPU_seconds'],
        carried_completed_science_GPU_seconds=probe['prior_completed_science_GPU_seconds'],
        total_GPU_cap_seconds=4800,worst_measured_peak_bytes=max(r['peak_VRAM_bytes'] for r in probe['capacities'].values()),
        references=previous['references'],strong_summary=previous['strong_summary'],
        DEV_manifest=previous['DEV_manifest'],DEV_shards=previous['DEV_shards'],
        Japanese_manifest=previous['Japanese_manifest'],unigram=previous['unigram'],
        sources={**p['sources'],**{path:sha256(ROOT/path) for path in SOURCES}},CPU_workflow_tests=ref(workflow),
        checkpoints_every_updates=500,heartbeat_every_updates=20,quality_criteria_unchanged=True,
        matched_control='NEW native_CE_control25M; cached100M is separate reference only',
        failure='Close fixed condition on data/numeric/state/resource/quality failure; no objective/teacher/parent/seed/decoder/budget rescue.',
        scope='Pilot only; main qualification then genuinely fresh whole-pipeline seed43/fullDEV/all440/new sealedTEST/adoption still required.',
        TEST_prepared=False,Base_qualified=False,Base_adopted=False)
    load_dev_suite(c['DEV_manifest']['path'],c['DEV_manifest']['sha256'])
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='paired_science_contract_frozen_not_started',caps_each=budgets,
        carried_seconds=c['carried_total_GPU_seconds'],maximum_total=c['carried_total_GPU_seconds']+sum(budgets.values()))),flush=True)


def inspect():
    c = json.loads(CONFIG.read_text())
    if (c['kind'] != 'frozen_native_document_progress_paired25M_science_v1' or c['recipe'] != POLICY
            or c['arms'] != list(ARMS) or c['batch'] != 48 or c['seed'] != 42 or c['goals'] != GOALS
            or c['main_teacher_goal_each'] != 25000000 or c['native_parameters'] != 10001152
            or c['train_only_parameters'] != 256 or c['training_parameters'] != 10001408
            or c['total_GPU_cap_seconds'] != 4800 or c['TEST_prepared'] is not False
            or c['Base_adopted'] is not False or c['quality_criteria_unchanged'] is not True):
        raise ValueError('Exact original-native paired25M fixed objective/quality/scope required')
    for path,pin in c['sources'].items():
        if sha256(ROOT/path) != pin:
            raise ValueError('Frozen source differs: '+path)
    for key in ('proposal','probe_config','probe_result','tokenizer','CPU_workflow_tests'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']:
            raise ValueError('Frozen evidence differs: '+key)
    probe = json.loads(Path(c['probe_result']['path']).read_text())
    if (science_budget(probe) != c['science_GPU_caps_each']
            or sum(c['science_GPU_caps_each'].values()) != c['science_GPU_cap_total']
            or c['carried_total_GPU_seconds'] != probe['cumulative_total_GPU_seconds']
            or c['carried_technical_GPU_seconds'] != probe['cumulative_technical_GPU_seconds']
            or c['carried_total_GPU_seconds']+c['science_GPU_cap_total'] > 4800):
        raise ValueError('Original ALL prior cost and actual measured per-arm budgets required')
    stat = Path(c['parent']['path']).stat()
    if (stat.st_size != c['parent_size'] or stat.st_mtime_ns != c['parent_mtime_ns']
            or c['parent']['sha256'] != '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Previously verified original parent identity differs')
    for row in c['references'].values():
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Original baseline metadata differs')
    if (RUN/'job.json').exists():
        job = json.loads((RUN/'job.json').read_text())
        if (alive(job) or job['status'] != 'interrupted' or not job['cumulative_GPU_ledger_closed']
                or job['config_sha256'] != sha256(CONFIG)
                or job['GPU_occupancy_seconds'] >= c['science_GPU_cap_total']):
            raise ValueError('Only actual stopped signal interruption with closed remaining ledger may resume')
    return c


class StopRequested(Exception):
    pass


def run():
    c = inspect()
    pin = sha256(CONFIG)
    RUN.mkdir(parents=True,exist_ok=True)
    previous = json.loads((RUN/'job.json').read_text()) if (RUN/'job.json').exists() else None
    prior = previous['GPU_occupancy_seconds'] if previous else 0.
    arm_times = previous['arm_GPU_seconds'].copy() if previous else dict.fromkeys(ARMS,0.)
    job = dict(status='starting',**identity(),started_at=now(),config_sha256=pin,
        GPU_occupancy_seconds=prior,arm_GPU_seconds=arm_times.copy(),cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json',job)
    started = armed = None
    trainer = log = arm = None
    completed = {}
    def elapsed():
        return prior+(time.monotonic()-started if started is not None else 0.)
    def current_arm_seconds():
        return arm_times[arm]+(time.monotonic()-armed if armed is not None else 0.)
    def check():
        if (elapsed() > c['science_GPU_cap_total'] or elapsed()+c['carried_total_GPU_seconds'] > 4800
                or (arm is not None and current_arm_seconds() > c['science_GPU_caps_each'][arm])):
            raise TimeoutError('Frozen per-arm or original cumulative GPU budget exhausted; no extension')
    def stop(*args):
        raise StopRequested('External signal; retain completed-update checkpoint and EVERY spent second')
    def beat(stage,**extra):
        check()
        times = arm_times.copy()
        if arm is not None:
            times[arm] = current_arm_seconds()
        job.update(stage=stage,arm=arm,heartbeat_at=now(),GPU_occupancy_seconds=elapsed(),arm_GPU_seconds=times,**extra)
        atomic_json(RUN/'job.json',job)
    def save():
        path = RUN/arm/f"checkpoint-{trainer.counters['update']:08d}.pt"
        trainer.save(path)
        latest = dict(path=str(path),sha256=sha256(path),binding=trainer.binding,update=trainer.counters['update'])
        atomic_json(RUN/arm/'latest.json',latest)
        return latest
    try:
        torch.set_num_threads(2)
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.signal(signal.SIGTERM,stop)
            signal.signal(signal.SIGINT,stop)
            configure_resident_memory(c['worst_measured_peak_bytes'])
            job['status'] = 'running'
            for next_arm in ARMS:
                output = RUN/next_arm
                output.mkdir(parents=True,exist_ok=True)
                if (output/'result.json').exists():
                    record = json.loads((output/'result.json').read_text())
                    if (not previous or record['config_sha256'] != pin or record['status'] != 'complete'
                            or record['binding'] != binding(c,pin,next_arm)
                            or sha256(Path(record['training']['checkpoint'])) != record['training']['checkpoint_sha256']):
                        raise ValueError('Previously completed arm must retain exact scientific evidence')
                    completed[next_arm] = record
                    continue
                arm,armed = next_arm,time.monotonic()
                trainer = build(c,binding(c,pin,arm),arm)
                metrics = output/'metrics.jsonl'
                if (output/'latest.json').exists():
                    latest = json.loads((output/'latest.json').read_text())
                    if latest['binding'] != trainer.binding or sha256(Path(latest['path'])) != latest['sha256']:
                        raise ValueError('Exact completed-update checkpoint required')
                    trainer.load(latest['path'])
                    rows = [json.loads(line) for line in metrics.read_text().splitlines()] if metrics.exists() else []
                    retained = [r for r in rows if r['update'] <= trainer.counters['update']]
                    validate_history(retained,trainer.state_dict())
                    if len(retained) != len(rows):
                        atomic_json(output/f'discarded-post-checkpoint-{job["pid"]}.json',dict(rows=rows[len(retained):]))
                        metrics.write_text(''.join(json.dumps(row)+'\n' for row in retained))
                else:
                    if (metrics.exists() or (previous and previous.get('arm') == arm)
                            or weights_digest(trainer.state_dict()) != c['initial_native_weights_sha256']
                            or torch.count_nonzero(trainer.progress_head.weight)):
                        raise ValueError('NEW science starts from original native parent/zero head, never verification weights')
                    save()
                log = metrics.open('a',buffering=1)
                while not trainer.sampler.exhausted:
                    check()
                    row = trainer.step()
                    log.write(json.dumps(row)+'\n')
                    if row['update'] % 500 == 0:
                        save()
                    if row['update'] % 20 == 0:
                        beat('learning',update=row['update'],main_teacher_positions=row['supervised_tokens'])
                log.close()
                log = None
                latest = save()
                state = host(trainer.state_dict())
                rows = [json.loads(line) for line in metrics.read_text().splitlines()]
                rollup = validate_history(rows,state)
                if (state['counters']['supervised_tokens'] != 25000000 or state['sampler']['consumed'] != GOALS
                        or not committed_state(state)):
                    raise ValueError('Genuine original25M finite completed-update state required')
                training = dict(status='complete',checkpoint=latest['path'],checkpoint_sha256=latest['sha256'],
                    binding=trainer.binding,counters=state['counters'],physical_rollup=rollup,
                    model_config=state['model_config'],spec=state['spec'],lineage=state['lineage'])
                atomic_json(output/'training.json',training)
                beat('evaluation',update=state['counters']['update'],main_teacher_positions=25000000)
                ev = evaluate(trainer,c,training,output/'evaluation',beat,check)
                check()
                record = dict(status='complete',config_sha256=pin,binding=trainer.binding,training=training,evaluation=ev,
                    GPU_occupancy_seconds=current_arm_seconds(),scientific_main_teachers=25000000,
                    scalar_learning_labels=state['counters']['progress_learning_positions'],TEST_opened=False,Base_adopted=False)
                atomic_json(output/'result.json',record)
                completed[arm] = record
                arm_times[arm] = current_arm_seconds()
                trainer.sampler.handle.close()
                del trainer,state,rows
                trainer = None
                arm = armed = None
                torch.cuda.empty_cache()
            states = {a:torch.load(completed[a]['training']['checkpoint'],map_location='cpu',weights_only=False) for a in ARMS}
            checks = matched_original(states['document_progress'],states['native_CE_control'])
            if not all(checks.values()):
                raise ValueError('Actual NEW25M paired main/scalar/source full streams differ')
            check()
            result = dict(status='complete',config_sha256=pin,actual_identity=identity(),arms=completed,paired_original_match=checks,
                scientific_main_teachers_new_total=50000000,additional_scalar_learning_labels=25000000,
                GPU_occupancy_seconds=elapsed(),arm_GPU_seconds=arm_times,
                carried_total_GPU_seconds=c['carried_total_GPU_seconds'],content_review_completed=False,
                TEST_opened=False,Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False)
            result['cumulative_total_GPU_seconds'] = result['GPU_occupancy_seconds']+c['carried_total_GPU_seconds']
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_occupancy_seconds=result['GPU_occupancy_seconds'],
                arm_GPU_seconds=arm_times,cumulative_GPU_ledger_closed=True)
            atomic_json(RUN/'job.json',job)
            print('Paired25M learning and DEV-only evaluation complete; ALL160 individual content reviews pending',flush=True)
    except BaseException as error:
        if log is not None:
            log.close()
        if trainer is not None and not trainer._step_in_progress:
            try:
                save()
            except Exception:
                pass
        if arm is not None:
            arm_times[arm] = current_arm_seconds()
        job.update(status='interrupted' if isinstance(error,StopRequested) else 'failed',ended_at=now(),
            GPU_occupancy_seconds=elapsed(),arm_GPU_seconds=arm_times,cumulative_GPU_ledger_closed=True,
            error_type=type(error).__name__,error=str(error))
        atomic_json(RUN/'job.json',job)
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('freeze','inspect','observe-ui','run'))
    args = parser.parse_args()
    if args.action == 'freeze':
        freeze()
    elif args.action == 'inspect':
        inspect()
        print('Paired native25M scientific preflight passed; no GPU')
    elif args.action == 'observe-ui':
        inspect()
        print(json.dumps(observe_ui()))
    else:
        run()
