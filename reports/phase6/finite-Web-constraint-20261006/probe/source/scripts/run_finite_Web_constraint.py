"""Bounded finite Web-body constraint, own measured CUDA and rejection branch."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import signal
import shutil
import statistics
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from finite_Web_constraint import FiniteWebTrainer,BodyOracle,constrain,ConstraintRejected,KIND
from interleaved_outcome_trainer import InterleavedOutcomeSampler
from historical_parent_condition_trainer import historical_web_cursor
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
import run_interleaved_outcome_order as old
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/finite-Web-constraint-20261006'
PROPOSAL=ROOT/'reports/phase6/finite_Web_constraint_proposal.json'
PROBE_CONFIG=ROOT/'configs/phase6/finite_Web_constraint_probe.json'
CONFIG=ROOT/'configs/phase6/finite_Web_constraint.json'
ARM='finite_Web_constraint';CEILING=2400;PROBE_CEILING=120
SOURCES=('scripts/finite_Web_constraint.py','scripts/run_finite_Web_constraint.py',
         'scripts/run_finite_Web_constraint.ps1','tests/test_finite_Web_constraint.py')
reference,check_reference=old.reference,old.check_reference


def prepare():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    started=time.monotonic();p=read_json(PROPOSAL);previous=old.inspect(old.CONFIG)
    if (p['kind']!=KIND or p['CE_teacher_tokens']!=91641755 or p['total_new_GPU_ceiling_seconds']!=2400
            or p['probe_GPU_ceiling_seconds']!=120 or p['implemented'] or p['launched'] or p['Base_complete']
            or p['new_CE_teacher_tokens_so_far'] or p['GPU_seconds_so_far']):raise ValueError('Fixed finite-loss proposal required')
    for ref in (*p['references'].values(),p['parent']):check_reference(ref)
    suites=list(ET.parse(ROOT/'reports/phase6/finite_Web_constraint_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Four actual CPU constraint/rollback/fullstate checks required')
    c={k:copy.deepcopy(previous[k]) for k in ('parent','pool','original_web','positive_data','original_config','accepted_compact_index',
        'teacher_goals','references','old_source_sha256','implementation','remaining_updates')}
    c['old_source_sha256'].update(previous['source_sha256'])
    pool,original,positive=old.data(c)
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    samples=torch.load(p['references']['cached_TRAIN_packet']['path'],map_location='cpu',weights_only=False)
    metadata=read_json(Path(p['references']['cached_TRAIN_metadata']['path']))
    if len(samples)!=16 or metadata['split']!='train':raise ValueError('Exactly existing16 TRAIN batches required')
    xs=[];ys=[];indices=[]
    for batch_index,batch in enumerate(samples):
        meta=metadata['rows'][batch_index]
        if (batch['routes']!=meta['actual_source_routes'] or batch['x'].shape!=(32,1024) or batch['y'].shape!=(32,1024)
                or __import__('hashlib').sha256(batch['x'].numpy().astype('<i8').tobytes()).hexdigest()!=meta['input_sha256']
                or __import__('hashlib').sha256(batch['y'].numpy().astype('<i8').tobytes()).hexdigest()!=meta['target_sha256']):
            raise ValueError('Actual cached TRAIN input/target/routes differ')
        for row_index,genre in enumerate(batch['routes']):
            if genre=='web':
                xs.append(batch['x'][row_index]);ys.append(batch['y'][row_index]);indices.append([batch_index,row_index])
                if len(xs)==32:break
        if len(xs)==32:break
    if len(xs)!=32:raise ValueError('Fixed first32 Web windows unavailable')
    memory=dict(x=torch.stack(xs),y=torch.stack(ys));body=memory['y'].ge(8)
    sampler=InterleavedOutcomeSampler(pool,original,positive,historical_web_cursor(parent),c['teacher_goals'],reference_policy='staged')
    sampler.reference_token_digest=parent['token_digest'];x,y,_,_=sampler.batch(32)
    if sampler.last_genres!=['web']*32 or not torch.equal(x,memory['x']) or not torch.equal(y,memory['y']):
        raise ValueError('Memory must equal original staged initial Web windows, not new corpus')
    RUN.mkdir(parents=True,exist_ok=True);mp=RUN/'memory.pt'
    if mp.exists():raise ValueError('Preserve original memory packet')
    torch.save(memory,mp)
    header=dict(selection=indices,rows=32,context=1024,microbatch=8,body_teachers=int(body.sum()),physical_input_tokens=32768,
        common_body_bytes=int(pool.byte_lengths[memory['y'][body].numpy()].sum()),
        input_sha256=__import__('hashlib').sha256(memory['x'].numpy().astype('<i8').tobytes()).hexdigest(),
        raw_target_sha256=__import__('hashlib').sha256(memory['y'].numpy().astype('<i8').tobytes()).hexdigest(),
        parent=c['parent'],cached_samples=p['references']['cached_TRAIN_packet'],cached_metadata=p['references']['cached_TRAIN_metadata'],
        exact_original_staged_initial_Web_input_targets=True,cache_reused=True,new_source_scans=0)
    atomic_json(RUN/'memory.json',header)
    staged_result=Path(c['references']['control_result']['path']);staged=read_json(staged_result)
    staged_metrics=staged_result.parent/'source_order/training/metrics.jsonl'
    expected=[json.loads(s) for s in staged_metrics.read_text().splitlines()]
    if len(expected)!=3068 or [r['update'] for r in expected]!=list(range(parent['update']+1,parent['update']+3069)):
        raise ValueError('Completed original staged reference history required')
    masked=read_json(Path(p['references']['original_masked_staged_control']['path']))
    control=dict(path=masked['checkpoint']['checkpoint'],sha256=masked['checkpoint']['checkpoint_sha256'])
    c['references'].update(proposal=reference(PROPOSAL),CPU_tests=reference(ROOT/'reports/phase6/finite_Web_constraint_tests.xml'),
        memory_header=reference(RUN/'memory.json'),staged_metrics=reference(staged_metrics),
        masked_staged_control=p['references']['original_masked_staged_control'],masked_staged_review=p['references']['original_masked_staged_review'],
        masked_staged_notes=p['references']['original_masked_staged_notes'],reference_input_ledger=p['references']['accepted_input_ledger'])
    elapsed=time.monotonic()-started
    if elapsed>60:raise TimeoutError('Own CPU preparation60s exhausted')
    c.update(research_kind=KIND,phase='probe',source_sha256={s:sha256(ROOT/s) for s in SOURCES},memory=reference(mp),
        memory_binding=header,violating_numerical_control=control,GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,
        CPU_preparation_seconds=elapsed,peak_lr=.00001,body_ceiling_multiplier=1.01,
        projection_interior_margin_relative=1e-5,backtracks=[.5,.25,.125],quality_criteria_unchanged=True,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='finite_Web_constraint_prepared',CPU_seconds=elapsed,memory_header=header,new_GPU_seconds=0)),flush=True)


def inspect(path):
    c=read_json(path)
    if (c['research_kind']!=KIND or c['remaining_updates']!=3068 or c['total_new_GPU_ceiling_seconds']!=2400
            or c['peak_lr']!=.00001 or c['body_ceiling_multiplier']!=1.01 or c['projection_interior_margin_relative']!=1e-5
            or c['backtracks']!=[.5,.25,.125] or c['implementation']!=implementation_hashes()
            or c['Base_complete'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started']
            or c['protected_test_used'] or not c['quality_criteria_unchanged']):raise ValueError('Frozen finite Web scope differs')
    for relative,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/relative)!=digest:raise ValueError('Frozen source differs: '+relative)
    for ref in (*c['references'].values(),c['parent'],c['memory'],c['violating_numerical_control'],c['accepted_compact_index'],c['original_config']):check_reference(ref)
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Actual live job; no duplicate')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120:raise ValueError('Own120s probe required')
    elif path==CONFIG:
        r=probe_evidence();estimate=estimate_training(r)
        if (c['phase']!='scientific' or c['probe_result_sha256']!=sha256(RUN/'probe/result.json')
                or c['probe_config_sha256']!=sha256(PROBE_CONFIG) or c['reference_body_NLL']!=r['reference_body_NLL']
                or c['estimated_GPU_seconds_with_margin']!=estimate or estimate+r['GPU_seconds']>2400
                or c['verification_GPU_seconds']!=r['GPU_seconds'] or not math.isclose(c['GPU_budget_seconds']+r['GPU_seconds'],2400,abs_tol=1e-9)):
            raise ValueError('Own worst-case measured cumulative budget differs')
    else:raise ValueError('Only fixed probe/science paths allowed')
    return c


def estimate_training(r):
    rows=r['timing']['histories']
    if len(rows)!=32 or any(not math.isfinite(v['seconds']) or v['seconds']<=0 for v in rows):raise ValueError('Own32 real steps required')
    # Already includes one oracle and transaction. Deliberately reserve all
    # five forward-only checks plus one complete oracle gradient per update.
    step=statistics.median(v['seconds'] for v in rows[8:])
    forward=max(r['oracle_timings']['forward_only_seconds']);gradient=max(r['oracle_timings']['gradient_seconds'])
    worst=step+5*forward+gradient
    warm=max(0.,sum(v['seconds'] for v in rows[:8])-8*step)
    saves=(math.ceil(3068/250)+1)*r['timing']['terminal_save_seconds']
    return (3068*worst+warm+saves)*1.3+200


def probe_evidence():
    r=read_json(RUN/'probe/result.json');job=read_json(RUN/'probe/job.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
            or r['config_sha256']!=sha256(PROBE_CONFIG) or not r['passed'] or not all(r['initial_checks'].values())
            or not all(r['gate']['checks'].values()) or not r['projection_control']['accepted']
            or not r['projection_control']['projected']):raise ValueError('Own actual finite/resume/projector evidence required')
    return r


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c=copy.deepcopy(inspect(PROBE_CONFIG));r=probe_evidence();estimate=estimate_training(r)
    if estimate+r['GPU_seconds']>2400:raise ValueError('Measured worst-case exceeds2400s; do not launch or weaken budget')
    c.update(phase='scientific',reference_body_NLL=r['reference_body_NLL'],probe_config_sha256=sha256(PROBE_CONFIG),
        probe_result_sha256=sha256(RUN/'probe/result.json'),estimated_GPU_seconds_with_margin=estimate,
        verification_GPU_seconds=r['GPU_seconds'],verification_teacher_tokens=r['verification_source_CE_teacher_tokens'],
        GPU_budget_seconds=2400-r['GPU_seconds'],save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='finite_constraint_science_frozen',worst_estimated_seconds=estimate)),flush=True)


def binding(c,path):
    return dict(config_sha256=sha256(path),arm=ARM,parent=c['parent'],study_kind=KIND,
        target_rule='original staged conditional outcome+EOS mask',optimizer_policy='inherited_Adam_with_finite_body_NLL_projection',
        memory=c['memory'],body_ceiling_multiplier=1.01,peak_lr=.00001)


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c=inspect(path);output=RUN/'probe' if probe else RUN
    output.mkdir(parents=True,exist_ok=True);jp=output/'job.json';prior=read_json(jp) if jp.exists() else {}
    if prior and prior['config_sha256']!=sha256(path):raise ValueError('Interrupted config differs')
    if prior.get('status')=='complete':print('Completed finite constraint run retained');return
    previous=prior.get('GPU_elapsed_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),GPU_elapsed_seconds=previous,started_at=now(),
        restart_command=f"scripts/run_finite_Web_constraint.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Interrupted; accepted completed updates retained')
        if started[0] is not None and previous+time.monotonic()-started[0]>c['GPU_budget_seconds']:raise TimeoutError('Cumulative finite-loss GPU budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for relative in (*c['source_sha256'],*c['old_source_sha256'],*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Frozen snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);pool,original,positive=old.data(c)
        memory=torch.load(c['memory']['path'],map_location='cpu',weights_only=False);b=binding(c,path)
        base=read_json(Path(c['original_config']['path']))
        with gpu_lock('cuda'):
            started[0]=time.monotonic();heartbeat('GPU');progress=output/'progress-result.json'
            result=read_json(progress) if progress.exists() else {}
            reference_ce=c.get('reference_body_NLL',result.get('reference_body_NLL'))
            def build():return FiniteWebTrainer(parent,pool,original,positive,c['teacher_goals'],b,memory,c['memory_binding'],reference_ce=reference_ce)
            if probe:
                if 'initial_checks' not in result:
                    t=build();reference_ce=t.reference_ce
                    checks=dict(model=equal_state(old.prior.cpu_state(t.model.state_dict()),parent['model']),
                        optimizer=equal_state(old.prior.cpu_state(t.optimizer.state_dict()),parent['optimizer']),
                        scheduler=equal_state(t.scheduler.state_dict(),parent['scheduler']),RNG=equal_state(rng_state(),parent['rng']),
                        actual_Web_cursor=equal_state(t.sampler.streams['web'].sampler.state_dict(),parent['sampler']['web']),
                        actual_LR=all(g['lr']==.00001 for g in t.optimizer.param_groups),
                        baseline_finite=math.isfinite(reference_ce) and reference_ce>0)
                    if not all(checks.values()):raise ValueError('Initial fullstate/reference differs')
                    result.update(initial_checks=checks,reference_body_NLL=reference_ce,reference_setup_observations=t.setup_oracle_counts)
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                if 'gate' not in result:
                    states=[];histories=[];teachers=0;aux=[]
                    for route in ('continuous','resumed'):
                        t=build();rows=[]
                        for i in range(8):
                            check();rows.append(t.step())
                            if route=='resumed' and i==3:
                                t.save(output/'split.pt');del t;gc.collect();torch.cuda.empty_cache();t=build();t.load(output/'split.pt')
                        t.save(output/(route+'.pt'));states.append(torch.load(output/(route+'.pt'),map_location='cpu',weights_only=False))
                        teachers+=t.supervised_tokens-parent['supervised_tokens'];aux.append(t.auxiliary);histories.append(rows)
                        del t;gc.collect();torch.cuda.empty_cache()
                    checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
                    for key in set(histories[0][0])-{'seconds','data_wait_seconds','tokens_per_second'}:
                        checks['history_'+key]=equal_state([r[key] for r in histories[0]],[r[key] for r in histories[1]])
                    checks.update(finite=all(finite_state(s) for s in states),all_actual_LR=all(row['lr']==.00001 for h in histories for row in h),
                        all_finite_body_bounds=all(row['constraint']['final_body_NLL']<=reference_ce*1.01 for h in histories for row in h),
                        original_staged_Web_first=all(row['actual_source_routes']==['web']*32 for h in histories for row in h))
                    if not all(checks.values()):raise ValueError('Own actual CUDA fullstate resume differs: '+repr(checks))
                    result['gate']=dict(passed=True,checks=checks,histories=histories,verification_teacher_tokens=teachers,auxiliary=aux,GPU_optimizer_updates=16)
                    atomic_json(progress,result);del states;gc.collect()
                if 'timing' not in result:
                    folder=output/'timing';folder.mkdir(parents=True,exist_ok=True);t=build();cp=old.prior.latest(folder)
                    if cp is not None:t.load(cp)
                    log=folder/'metrics.jsonl';old.prior.reconcile(log,t.update,parent['update'])
                    with log.open('a',buffering=1) as stream:
                        while t.update-parent['update']<32:
                            try:check()
                            except (InterruptedError,TimeoutError):t.save(folder/'checkpoint.pt');raise
                            row=t.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if (t.update-parent['update'])%8==0:heartbeat('finite-constraint-timing',completed_updates=t.update-parent['update'])
                    saved=t.save(folder/'checkpoint.pt');rows=[json.loads(s) for s in log.read_text().splitlines()]
                    if not finite_state(torch.load(folder/'checkpoint.pt',map_location='cpu',weights_only=False)):raise ValueError('Nonfinite own actual timing state')
                    result['timing']=dict(histories=rows,terminal_save_seconds=saved,checkpoint=reference(folder/'checkpoint.pt'),
                        verification_teacher_tokens=t.supervised_tokens-parent['supervised_tokens'],auxiliary=t.auxiliary)
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                if 'projection_control' not in result:
                    m=JMicroModel(parent['model_config']).to('cuda');m.load_state_dict(parent['model']);before=[p.detach().clone() for p in m.parameters()]
                    selected=torch.load(c['violating_numerical_control']['path'],map_location='cpu',weights_only=False);m.load_state_dict(selected['model'])
                    oracle=BodyOracle(m,memory,8);value,_=oracle.measure()
                    if value<=reference_ce*1.01:raise ValueError('Fixed stored control does not violate memory bound; no source/packet/CP rescue')
                    check();control=constrain(list(m.parameters()),before,oracle,reference_ce)
                    if not control['projected'] or not control['accepted']:raise ValueError('Own real finite projector control failed')
                    result['projection_control']=dict(control,stored_checkpoint=c['violating_numerical_control'],
                        initial_stored_body_NLL=value,auxiliary=oracle.stats,diagnostic_weights_not_adopted_or_saved=True,
                        original_checkpoint_file_unchanged=sha256(Path(c['violating_numerical_control']['path']))==c['violating_numerical_control']['sha256'])
                    atomic_json(progress,result);del selected,before,m,oracle;gc.collect();torch.cuda.empty_cache()
                if 'oracle_timings' not in result:
                    m=JMicroModel(parent['model_config']).to('cuda');m.load_state_dict(parent['model']);oracle=BodyOracle(m,memory,8)
                    forwards=[];gradients=[]
                    for i in range(4):
                        check();oracle.measure();forwards.append(oracle.last_seconds)
                        oracle.measure(True);gradients.append(oracle.last_seconds)
                    result['oracle_timings']=dict(forward_only_seconds=forwards,gradient_seconds=gradients,auxiliary=oracle.stats)
                    atomic_json(progress,result);del m,oracle;gc.collect();torch.cuda.empty_cache()
                result.update(passed=True,GPU_optimizer_updates=48,
                    verification_source_CE_teacher_tokens=result['gate']['verification_teacher_tokens']+result['timing']['verification_teacher_tokens'],
                    scientific_source_CE_teacher_tokens=0,all_probe_weights_discarded_for_science=True)
            else:
                if 'checkpoint' not in result:
                    folder=output/ARM/'training';folder.mkdir(parents=True,exist_ok=True);t=build();cp=old.prior.latest(folder)
                    if cp is not None:t.load(cp)
                    log=folder/'metrics.jsonl';seconds=old.prior.reconcile(log,t.update,parent['update'])
                    expected=[json.loads(s) for s in Path(c['references']['staged_metrics']['path']).read_text().splitlines()]
                    with log.open('a',buffering=1) as stream:
                        while t.sampler.source_teachers!=c['teacher_goals']:
                            try:check();row=t.step()
                            except ConstraintRejected:
                                t.save(folder/f'checkpoint-{t.update:08d}.pt')
                                result['finite_rejection']=dict(last_rejection=t.last_rejection,last_valid_checkpoint=reference(folder/f'checkpoint-{t.update:08d}.pt'),
                                    accepted_source_updates=t.update-parent['update'],accepted_source_CE_teacher_tokens=t.supervised_tokens-parent['supervised_tokens'],
                                    accepted_auxiliary=t.auxiliary,last_completed_states_restored=True)
                                break
                            except (InterruptedError,TimeoutError):t.save(folder/f'checkpoint-{t.update:08d}.pt');raise
                            reference_row=expected[t.update-parent['update']-1]
                            if row['reference_token_digest']!=reference_row['token_digest']:raise ValueError('Original staged full reference input/target differs')
                            seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if (t.update-parent['update'])%20==0:heartbeat('finite-constrained-Base-training',completed_updates=t.update-parent['update'],total_updates=3068,
                                actual_teachers=row['additional_teacher_tokens'],loss=row['loss'],constraint=row['constraint'],auxiliary=row['auxiliary'])
                            if (t.update-parent['update'])%250==0:t.save(folder/f'checkpoint-{t.update:08d}.pt')
                    if 'finite_rejection' not in result:
                        ledger=read_json(Path(c['references']['reference_input_ledger']['path']));t.save(folder/f'checkpoint-{t.update:08d}.pt')
                        if (t.update-parent['update']!=3068 or t.supervised_tokens-parent['supervised_tokens']!=91641755
                                or t.sampler.actual!=ledger['actual_source_accounting'] or t.sampler.source_digests!=ledger['source_digests']
                                or not equal_state(t.sampler.reference_state(),ledger['staged_reference_sampler'])):raise ValueError('Whole accepted staged CE/source ledger differs')
                        cp=folder/f'checkpoint-{t.update:08d}.pt'
                        result['checkpoint']=dict(checkpoint=str(cp),checkpoint_sha256=sha256(cp),binding=b,updates=3068,
                            additional_supervised_tokens=t.supervised_tokens-parent['supervised_tokens'],additional_input_tokens=t.tokens-parent['tokens'],
                            actual_source_accounting=t.sampler.actual,sampler=t.sampler.state_dict(),source_digests=t.sampler.source_digests,
                            token_digest=t.token_digest,reference_token_digest=t.sampler.reference_token_digest,training_seconds=seconds,
                            auxiliary=t.auxiliary,last_constraint=t.last_constraint)
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                if 'finite_rejection' not in result and 'evaluation' not in result:
                    evaluation.RUN=output/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                    result['evaluation']=evaluation.evaluate(ARM,result['checkpoint'],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-previous)
                    atomic_json(progress,result)
            check();elapsed=previous+time.monotonic()-started[0]
            status='finite_constraint_probe_complete' if probe else ('finite_constraint_rejected_update_branch_complete' if 'finite_rejection' in result else 'finite_constraint_GPU_complete_pending_all80_content')
            result.update(status=status,config_sha256=sha256(path),GPU_seconds=elapsed,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
            job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);parser=argparse.ArgumentParser();modes=parser.add_mutually_exclusive_group()
    for mode in ('prepare','preflight-probe','probe','freeze','inspect'):modes.add_argument('--'+mode,action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.preflight_probe:inspect(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run(args.probe)
