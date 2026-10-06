"""Bounded teacher-coverage research; historical quality extension gates stay intact."""
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
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,implementation_hashes,gpu_lock
from phase6_performance import alive,identity,finite_state
from run_eos_short_pilot import equal_state,rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from textbook_quantity_trainer import ThreeSourceTrainer,TAG_MAPPING
from extend_textbook_quantity_trainer import ExtendedCurveTrainer
from cached_three_source_index import CachedThreeSourceIndex
import run_textbook_quantity_comparison as old
import run_complete_text_comparison as evaluation
import run_textbook_coverage as original_coverage

RUN=ROOT/'reports/phase6/textbook-coverage-2b-20261006'
PROBE_CONFIG=ROOT/'configs/phase6/textbook_coverage_probe.json'
CONFIG=ROOT/'configs/phase6/textbook_coverage_2b_v2.json'
BASELINE='large-1000000000'
CANDIDATE='large-2000000000'
TARGET=2000000000
DECAY=20000000
CEILING=3000
UL_RUN=ROOT/'reports/phase6/sequence-objective-low-alpha-20261006'
SPEED_RUN=ROOT/'reports/phase6/textbook-coverage-save-cadence-20261006'
SOURCES=('scripts/run_textbook_coverage_v2.py','scripts/run_textbook_coverage_v2.ps1',
    'scripts/review_textbook_coverage_v2.py','scripts/cached_three_source_index.py',
    'scripts/extend_textbook_quantity_trainer.py','scripts/review_textbook_improved_base.py',
    'scripts/run_textbook_improved_base.py','scripts/run_textbook_coverage.py',
    'scripts/run_textbook_coverage.ps1','scripts/review_textbook_coverage.py',
    'scripts/measure_textbook_coverage_speed.py','scripts/measure_textbook_coverage_speed.ps1',*old.SOURCE_FILES)


def reference(path):
    return dict(path=str(path),sha256=sha256(path))


def cached_index_record(base):
    pool=base['pools']['large']
    path=Path(pool['pool'])/('.compact-index-'+pool['manifest_sha256'][:16])/'ready.json'
    if not path.exists():
        raise ValueError('Accepted compact index is missing; do not rescan the original13GB index')
    return path


def source_contract():
    base=old.load_config();job=read_json(old.RUN/'job.json');source=read_json(old.RUN/'compare-result.json')
    review=read_json(old.RUN/'review.json')
    assert job['status']=='complete' and not alive(job)
    assert review['status']=='matched500M_2B_all160_and_actual_learning_evidence_complete'
    assert review['result_sha256']==sha256(old.RUN/'compare-result.json')
    assert review['annotations_sha256']==sha256(old.RUN/'annotations.json')
    assert not review['protected_test_used'] and not review['Base_adopted']
    uj=read_json(UL_RUN/'job.json');ur=read_json(UL_RUN/'review.json')
    assert uj['status']=='complete' and not alive(uj)
    assert ur['status']=='matched_reused_CE_and_actual_low_alpha25M_all80_complete'
    assert ur['result_sha256']==sha256(UL_RUN/'compare-result.json')
    assert not ur['objective_comparison']['passed'] and not ur['practical']['absolute_screen_pass']
    record=source['stable'][BASELINE]
    assert record['additional_supervised_tokens']==1000000000
    assert sha256(Path(record['checkpoint']))==record['checkpoint_sha256']
    parent=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    assert finite_state(parent) and parent['pilot_binding']==record['binding']
    assert parent['spec']['curve_schedule']['mode']=='stable' and parent['spec']['curve_schedule']['teachers']==1000000000
    assert parent['spec']['curve_schedule']['no_reheat']
    assert parent['sampler']['source_teachers']==dict(web=0,short=1000000000)
    assert parent['sampler']['genre_tag_mapping']==TAG_MAPPING and parent['pilot_binding']['arm']=='large'
    cursor=parent['sampler']['short']
    assert cursor['epoch']==0 and 0<cursor['position']<cursor['blocks']
    assert parent['pilot_binding']['short_manifest_sha256']==base['pools']['large']['manifest_sha256']
    assert parent['pilot_binding']['peak_lr']==base['peak_lr']==.002
    ev=source['evaluations'][BASELINE];rows=ev['generation']['outputs']
    assert ev['checkpoint_sha256']==source['decay'][BASELINE]['checkpoint_sha256']
    assert ev['binding']==source['decay'][BASELINE]['binding'] and ev['evaluation_RNG_isolated']
    assert not ev['protected_test_used'] and ev['greedy_rates']==rate(rows)
    validate_rows(rows,Tokenizer(ROOT/base['tokenizer']))
    note=ROOT/'reports/phase6/textbook_quantity_large-1000000000_notes.json'
    raw=old.RUN/'evaluation'/BASELINE/'evaluation/generation.json'
    validate_notes(rows,read_json(note),sha256(raw))
    assert read_json(raw)==ev['generation']
    assert base['implementation']==parent['implementation_sha256']
    cached_index_record(base)
    return base,parent,source


def validate_scope(c):
    if (c['research_kind']!='same_material_teacher_coverage' or c['target_teachers']!=TARGET
            or c['decay_teacher_tokens']!=DECAY or c['parent_point']!=BASELINE
            or c['candidate_point']!=CANDIDATE or c['total_new_GPU_ceiling_seconds']!=CEILING
            or not c['quality_criteria_unchanged'] or c['protected_test_used'] or c['Base_adopted']
            or c['Chat_adopted'] or c['requested_five_steps_complete']
            or not c['historical_quality_extension_refusal_preserved']):
        raise ValueError('Coverage research scope/quality/heldout contract differs')


def prepare():
    raise ValueError('Version2 reuses immutable original CUDA gates; no new probe recipe')


def probe_evidence():
    original=original_coverage.probe_evidence()
    job=read_json(SPEED_RUN/'job.json');speed=read_json(SPEED_RUN/'result.json')
    assert job['status']=='complete' and not alive(job) and speed['passed']
    assert speed['status']=='paired_save_cadence_measurement_complete'
    assert speed['GPU_seconds']==job['GPU_elapsed_seconds']<=120
    assert speed['original_probe_config_sha256']==sha256(PROBE_CONFIG)
    assert speed['original_probe_result_sha256']==sha256(RUN/'probe/result.json')
    assert speed['source_sha256']==sha256(ROOT/'scripts/measure_textbook_coverage_speed.py')==sha256(SPEED_RUN/'source/measure_textbook_coverage_speed.py')
    assert speed['scientific_teacher_tokens']==0 and speed['weights_discarded_for_science']
    assert len(speed['checks'])==15 and all(speed['checks'].values())
    assert set(speed['records'])=={'continuous','save_every_update'}
    for route,record in speed['records'].items():
        cp=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
        assert sha256(Path(record['checkpoint']))==record['checkpoint_sha256'] and finite_state(cp)
        assert cp['pilot_binding']['config_sha256']==sha256(PROBE_CONFIG)
        rows=[json.loads(s) for s in (SPEED_RUN/route/'metrics.jsonl').read_text().splitlines()]
        assert rows==record['histories'] and len(rows)==record['GPU_optimizer_updates']==64
        assert cp['supervised_tokens']-1000000000==record['verification_teacher_tokens']
        assert cp['update']==rows[-1]['update']==30839 and cp['supervised_tokens']==rows[-1]['supervised_tokens']
        assert all(equal_state(row[k],old_row[k]) for row,old_row in zip(rows[:16],original['timing']['histories'],strict=True)
            for k in ('loss','gradient_norm','lr','token_digest','source_teachers','valid_input_tokens','physical_input_tokens'))
    assert speed['verification_teacher_tokens']==sum(r['verification_teacher_tokens'] for r in speed['records'].values())
    timing=dict(speed['records']['continuous'],mean_save_seconds=speed['records']['save_every_update']['save_seconds']/64,
        save_every_updates=250,timing_policy='64 uninterrupted actual updates;16 warmup counted,48 steady; amortize measured durable saves at scientific cadence250')
    return dict(original,timing=timing,GPU_seconds=original['GPU_seconds']+speed['GPU_seconds'],
        verification_teacher_tokens=original['verification_teacher_tokens']+speed['verification_teacher_tokens'],
        original_GPU_seconds=original['GPU_seconds'],save_cadence_GPU_seconds=speed['GPU_seconds'])


def estimate_training(timing,parent_teachers=1000000000):
    rows=timing['histories'];assert len(rows)==64 and timing['verification_teacher_tokens']>0
    assert all(math.isfinite(r['seconds']) and r['seconds']>0 for r in rows)
    seconds=statistics.median(r['seconds'] for r in rows[16:])
    teachers=timing['verification_teacher_tokens']/64
    updates=math.ceil((TARGET-parent_teachers)/teachers);decay_updates=math.ceil(DECAY/teachers)
    warmup=max(0.,sum(r['seconds'] for r in rows[:16])-16*seconds)
    saves=(math.ceil(updates/250)+math.ceil(decay_updates/250)+2)*timing['mean_save_seconds']
    assert math.isfinite(timing['mean_save_seconds']) and timing['mean_save_seconds']>=0 and timing['save_every_updates']==250
    raw=(updates+decay_updates)*seconds+warmup+saves
    return dict(step_seconds=seconds,teachers_per_update=teachers,stable_updates=updates,decay_updates=decay_updates,
                measured_updates=64,warmup_updates_counted=16,steady_updates=48,estimated_warmup_seconds=warmup,
                estimated_save_seconds=saves,estimated_step_seconds=raw),raw*1.3+480+60


def inspect(path):
    assert path==CONFIG,'Version2 scientific config only; original probe is immutable'
    c=read_json(path);validate_scope(c);base,parent,source=source_contract()
    for name in ('parent','original_config','source_result','source_review','source_annotations','prior_UL_review','control_notes','control_generation','cached_index_ready','timing_measurement_result','timing_measurement_job'):
        assert sha256(Path(c[name]['path']))==c[name]['sha256']
    assert c['parent']==reference(Path(source['stable'][BASELINE]['checkpoint']))
    assert c['pool']==base['pools']['large'] and c['prepared_tokens']==base['prepared_tokens']['large']
    assert c['actual_parent_cursor']==parent['sampler']['short'] and c['peak_lr']==base['peak_lr']
    assert c['implementation']==implementation_hashes() and c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert c['control_reused_without_training_or_evaluation']
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):
        raise ValueError('Actual coverage process is live; do not duplicate')
    if path==PROBE_CONFIG:
        assert c['phase']=='probe' and c['GPU_budget_seconds']==300
    else:
        assert path==CONFIG and c['phase']=='scientific'
        probe=probe_evidence();timing,estimate=estimate_training(probe['timing'])
        assert c['probe_config_sha256']==sha256(PROBE_CONFIG) and c['probe_result_sha256']==sha256(RUN/'probe/result.json')
        assert c['verification_GPU_seconds']==probe['GPU_seconds'] and c['verification_teacher_tokens']==probe['verification_teacher_tokens']
        assert c['measured_timings']==timing and c['estimate_with_margin']==estimate
        assert math.isclose(c['GPU_budget_seconds']+probe['GPU_seconds'],CEILING,abs_tol=1e-9)
        assert estimate+probe['GPU_seconds']<=CEILING
    return c,base,parent,source


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c,_,_,_=original_coverage.inspect(PROBE_CONFIG);c=copy.deepcopy(c)
    probe=probe_evidence();timing,estimate=estimate_training(probe['timing'])
    if estimate+probe['GPU_seconds']>CEILING:
        raise ValueError('Measured coverage study cannot fit versioned3000s ceiling')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        verification_GPU_seconds=probe['GPU_seconds'],verification_teacher_tokens=probe['verification_teacher_tokens'],
        GPU_budget_seconds=CEILING-probe['GPU_seconds'],measured_timings=timing,estimate_with_margin=estimate,
        total_new_GPU_ceiling_seconds=CEILING,recipe_version=2,
        budget_revision_reason='Original16-update every-save timing overestimated step cost; actual paired64-update cadence measurement binds continuous speed and amortized250-update durable saves; both measurements counted',
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        timing_measurement_result=reference(SPEED_RUN/'result.json'),timing_measurement_job=reference(SPEED_RUN/'job.json'))
    validate_scope(c)
    atomic_json(CONFIG,c);print(json.dumps(dict(status='measured coverage recipe frozen',timings=timing,estimate=estimate)),flush=True)


def stable_binding(c,path,parent):
    return dict(parent['pilot_binding'],config_sha256=sha256(path),
        curve_boundaries=[*parent['spec']['curve_schedule']['boundaries'],TARGET],
        stable_extension=dict(c['parent'],source_sha256=sha256(ROOT/'scripts/extend_textbook_quantity_trainer.py')))


def decay_binding(binding,parent,ref):
    return dict(binding,arm=CANDIDATE,curve_mode='decay',curve_boundaries=[DECAY],warmup_updates=0,
        optimizer_policy='inherit',initialization='stable-fork',parent=dict(ref,update=parent['update'],
            tokens_seen=parent['tokens'],supervised_tokens=parent['supervised_tokens']))


def resume_gate(build,folder,config_sha,check):
    path=folder/'result.json'
    if path.exists():
        kept=read_json(path);assert kept['passed'] and kept['config_sha256']==config_sha;return kept
    states=[];histories=[];teachers=inputs=0
    for route in ('continuous','resumed'):
        trainer=build();initial=trainer.supervised_tokens,trainer.tokens;rows=[]
        for i in range(4):
            check();rows.append(trainer.step())
            if route=='resumed' and i==1:
                split=folder/'split.pt';trainer.save(split)
                del trainer;gc.collect();torch.cuda.empty_cache();trainer=build();trainer.load(split)
        teachers+=trainer.supervised_tokens-initial[0];inputs+=trainer.tokens-initial[1]
        cp=folder/(route+'.pt');trainer.save(cp);states.append(torch.load(cp,map_location='cpu',weights_only=False));histories.append(rows)
        del trainer;gc.collect();torch.cuda.empty_cache()
    checks={key:equal_state(states[0][key],states[1][key]) for key in
        ('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes','token_digest','update','spec','model_config','pilot_binding')}
    for key in ('loss','gradient_norm','lr','token_digest','source_teachers','valid_input_tokens','physical_input_tokens'):
        checks['history_'+key]=all(equal_state(a[key],b[key]) for a,b in zip(*histories,strict=True))
    checks['finite']=all(finite_state(s) for s in states)
    assert all(checks.values()),checks
    result=dict(passed=True,checks=checks,histories=histories,config_sha256=config_sha,
        verification_teacher_tokens=teachers,verification_input_tokens=inputs,GPU_optimizer_updates=8)
    atomic_json(path,result);return result


def validate_timing(rows,parent,terminal):
    assert len(rows)==16 and [r['update'] for r in rows]==list(range(parent['update']+1,parent['update']+17))
    assert finite_state(terminal) and terminal['update']==rows[-1]['update']
    assert terminal['supervised_tokens']==rows[-1]['supervised_tokens']>parent['supervised_tokens']
    assert all(math.isfinite(r[k]) for r in rows for k in ('loss','gradient_norm','seconds','lr','data_wait_seconds'))
    assert all(r['seconds']>0 and 0<=r['data_wait_seconds']<=r['seconds'] and math.isclose(r['lr'],.002,rel_tol=1e-12) for r in rows)


def run(probe=False):
    assert not probe,'Version2 never repeats original verification updates'
    path=PROBE_CONFIG if probe else CONFIG;c,base,parent,source=inspect(path)
    directory=RUN/'probe' if probe else RUN;directory.mkdir(parents=True,exist_ok=True)
    jp=directory/'job.json';kept=read_json(jp) if jp.exists() else {}
    if kept:
        assert kept['config_sha256']==sha256(path) and not alive(kept)
        if kept['status']=='complete':print('Completed coverage job retained');return
    prior=kept.get('GPU_elapsed_seconds',0.);started=[None];stop=[False]
    job=dict(status='running',**identity(),config_sha256=sha256(path),started_at=kept.get('started_at',now()),
        GPU_elapsed_seconds=prior,Base_adopted=False,protected_test_used=False,
        restart_command=f"scripts/run_textbook_coverage_v2.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    def check():
        if stop[0]:raise InterruptedError('Stop requested; completed updates retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>c['GPU_budget_seconds']:
            raise TimeoutError('Cumulative measured coverage GPU budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(jp,job)
    def train(build,folder,total,label):
        trainer=build();folder.mkdir(parents=True,exist_ok=True);latest=old.latest_checkpoint(folder)
        if latest is not None:trainer.load(latest)
        log=folder/'metrics.jsonl';seconds=old.reconcile_metrics(log,trainer.update)
        with log.open('a',buffering=1) as stream:
            while trainer.sampler.source_teachers['short']<total:
                try:check()
                except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                row=trainer.step();seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                if trainer.update%100==0:heartbeat(label,teachers=trainer.sampler.source_teachers['short'],teacher_budget=total,loss=row['loss'])
                if trainer.update%250==0:trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
        cp=folder/f'checkpoint-{trainer.update:08d}.pt';trainer.save(cp)
        record=old.detail(trainer,cp,trainer.pilot_binding,seconds)
        del trainer;gc.collect();torch.cuda.empty_cache();return record
    try:
        heartbeat('setup');torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,path.relative_to(ROOT).as_posix()):
            target=directory/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        web=TrainView(base['web_shards'],base['web_manifest_sha256'])
        pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
        assert pool.index.cache_reused,'Use the accepted cached index; do not rescan corpus in this research'
        zero=torch.load(base['parent']['path'],map_location='cpu',weights_only=False);b=stable_binding(c,path,parent)
        def build():
            trainer=ExtendedCurveTrainer(zero,web,pool,'shuffle',dict(web=0,short=TARGET),b)
            trainer.load_extension(c['parent']['path']);return trainer
        with gpu_lock('cuda'):
            started[0]=time.monotonic()
            if probe:
                stable_gate=resume_gate(build,directory/'resume-gate/stable-extension',sha256(path),check)
                heartbeat('stable-extension-resume-verified')
                db=decay_binding(b,parent,c['parent'])
                def build_probe_decay():return ThreeSourceTrainer(copy.deepcopy(parent),web,pool,'shuffle',dict(web=0,short=DECAY),db)
                dg=resume_gate(build_probe_decay,directory/'resume-gate/decay',sha256(path),check)
                heartbeat('original1B-decay-resume-verified')
                folder=directory/'timing';folder.mkdir(exist_ok=True);trainer=build();latest=old.latest_checkpoint(folder)
                if latest is not None:trainer.load(latest)
                log=folder/'metrics.jsonl';old.reconcile_metrics(log,trainer.update)
                with log.open('a',buffering=1) as stream:
                    while trainer.update-parent['update']<16:
                        try:check()
                        except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                        row=trainer.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                        trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');heartbeat('continuous-stable-timing',completed_updates=trainer.update-parent['update'])
                cp=old.latest_checkpoint(folder);rows=[json.loads(s) for s in log.read_text().splitlines()]
                validate_timing(rows,parent,torch.load(cp,map_location='cpu',weights_only=False))
                timing=dict(histories=rows,GPU_optimizer_updates=16,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                    checkpoint=str(cp),checkpoint_sha256=sha256(cp))
                del trainer;gc.collect();torch.cuda.empty_cache()
                result=dict(status='actual_coverage_CUDA_resume_and_timing_complete',config_sha256=sha256(path),passed=True,
                    gates={'stable-extension':stable_gate,'decay':dg},timing=timing,
                    verification_teacher_tokens=stable_gate['verification_teacher_tokens']+dg['verification_teacher_tokens']+timing['verification_teacher_tokens'],
                    scientific_teacher_tokens=0,weights_discarded_for_science=True)
            else:
                progress_path=directory/'progress-result.json'
                result=read_json(progress_path) if progress_path.exists() else dict(
                    stable={BASELINE:source['stable'][BASELINE]},decay={BASELINE:source['decay'][BASELINE]},
                    evaluations={BASELINE:source['evaluations'][BASELINE]},control_reused=True)
                if CANDIDATE not in result['stable']:
                    record=train(build,directory/'stable',TARGET,'stable')
                    record['measured_stage_teachers']=TARGET-parent['sampler']['source_teachers']['short']
                    result['stable'][CANDIDATE]=record;atomic_json(progress_path,result)
                stable_record=result['stable'][CANDIDATE]
                stable=torch.load(stable_record['checkpoint'],map_location='cpu',weights_only=False)
                assert sha256(Path(stable_record['checkpoint']))==stable_record['checkpoint_sha256'] and finite_state(stable)
                db=decay_binding(b,stable,reference(Path(stable_record['checkpoint'])))
                def build_decay():return ThreeSourceTrainer(copy.deepcopy(stable),web,pool,'shuffle',dict(web=0,short=DECAY),db)
                if 'actual2B_decay_gate' not in result:
                    result['actual2B_decay_gate']=resume_gate(build_decay,directory/'resume-gate/decay',sha256(path),check)
                    atomic_json(progress_path,result);heartbeat('actual2B-decay-resume-verified')
                if CANDIDATE not in result['decay']:
                    result['decay'][CANDIDATE]=train(build_decay,directory/'decay',DECAY,'decay');atomic_json(progress_path,result)
                if CANDIDATE not in result['evaluations']:
                    evaluation.RUN=directory/'evaluation'
                    result['evaluations'][CANDIDATE]=evaluation.evaluate(CANDIDATE,result['decay'][CANDIDATE],
                        Shard(Path(base['dev_shards']),'dev'),Tokenizer(ROOT/base['tokenizer']),base,db,
                        heartbeat,check,started[0]+c['GPU_budget_seconds']-prior)
                    atomic_json(progress_path,result)
                result.update(status='coverage2B_learning_complete_pending_all80_content',config_sha256=sha256(path),
                    scientific_stable_teachers=TARGET-parent['sampler']['source_teachers']['short'],scientific_decay_teachers=DECAY,
                    additional_valid_input_tokens=stable_record['tokens']-parent['tokens']+result['decay'][CANDIDATE]['additional_input_tokens'],
                    additional_physical_input_tokens=stable_record['physical_input_tokens']-sum(parent['sampler']['source_physical_tokens'].values())+result['decay'][CANDIDATE]['physical_input_tokens'],
                    verification_teacher_tokens=c['verification_teacher_tokens']+result['actual2B_decay_gate']['verification_teacher_tokens'],
                    verification_GPU_seconds=c['verification_GPU_seconds'],
                    scientific_job_includes_actual2B_decay_verification=True,Base_adopted=False,Chat_adopted=False,
                    protected_test_used=False,requested_five_steps_complete=False)
            heartbeat('complete');job.update(status='complete',completed_at=now())
            elapsed=prior+time.monotonic()-started[0];job['GPU_elapsed_seconds']=elapsed;result['GPU_seconds']=elapsed
            atomic_json(directory/('result.json' if probe else 'compare-result.json'),result)
    except BaseException as error:
        job.update(status='failed',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group()
    for mode in ('freeze','inspect'):g.add_argument('--'+mode,action='store_true')
    args=p.parse_args()
    if args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run()
