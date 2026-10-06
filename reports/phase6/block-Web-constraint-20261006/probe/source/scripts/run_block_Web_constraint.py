"""Fixed20 accepted boundaries, owned CUDA evidence and persistent Base study."""
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import argparse
import copy
import gc
import json
import math
from pathlib import Path
import signal
import shutil
import statistics
import sys
import time
import xml.etree.ElementTree as ET
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from block_Web_constraint import BlockWebTrainer,KIND
from finite_Web_constraint import ConstraintRejected
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
import run_finite_Web_constraint as original
import run_interleaved_outcome_order as old
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/block-Web-constraint-20261006'
PROPOSAL=ROOT/'reports/phase6/block_Web_constraint_proposal.json'
PROBE_CONFIG=ROOT/'configs/phase6/block_Web_constraint_probe.json'
CONFIG=ROOT/'configs/phase6/block_Web_constraint.json'
ARM='block_Web_constraint'
SOURCES=('scripts/block_Web_constraint.py','scripts/run_block_Web_constraint.py',
    'scripts/run_block_Web_constraint.ps1','tests/test_block_Web_constraint.py')
reference,check_reference=original.reference,original.check_reference


def prepare():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    started=time.monotonic();p=read_json(PROPOSAL);c=copy.deepcopy(original.inspect(original.PROBE_CONFIG))
    if p['kind']!=KIND or p['block_updates']!=20 or p['implemented'] or p['launched'] or p['Base_complete']:
        raise ValueError('Fixed, unlaunched block proposal required')
    suites=list(ET.parse(ROOT/'reports/phase6/block_Web_constraint_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Actual4 block protocol tests required')
    c['old_source_sha256'].update(c['source_sha256'])
    c['references'].update(proposal=reference(PROPOSAL),CPU_tests=reference(ROOT/'reports/phase6/block_Web_constraint_tests.xml'),
        original_probe=reference(original.RUN/'probe/result.json'),compiled_terminal=p['references']['compiled_budget_failure'])
    probe=original.probe_evidence();elapsed=time.monotonic()-started
    if elapsed>60:raise TimeoutError('CPU preparation60s exhausted')
    c.update(research_kind=KIND,phase='probe',block_updates=20,source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=2400,previous_related_GPU_seconds=p['previous_related_GPU_seconds'],
        CPU_preparation_seconds=elapsed,cached_original_body_NLL=probe['reference_body_NLL'],
        cached_unchanged_projector_control=probe['projection_control'],
        does_not_satisfy_old_per_update_contract=True,constraint_scope='Accepted20-update boundaries only; intermediate tentative updates may violate loss ceiling.')
    atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='block_Web_prepared',CPU_seconds=elapsed,GPU_seconds=0)),flush=True)


def inspect(path):
    c=read_json(path)
    if (c['research_kind']!=KIND or c['block_updates']!=20 or c['remaining_updates']!=3068
            or c['total_new_GPU_ceiling_seconds']!=2400 or c['peak_lr']!=.00001 or c['body_ceiling_multiplier']!=1.01
            or c['projection_interior_margin_relative']!=1e-5 or c['backtracks']!=[.5,.25,.125]
            or c['implementation']!=implementation_hashes() or not c['does_not_satisfy_old_per_update_contract']
            or c['Base_complete'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started'] or c['protected_test_used']):
        raise ValueError('Frozen block scope/source policy differs')
    for s,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/s)!=digest:raise ValueError('Frozen source differs '+s)
    for ref in (*c['references'].values(),c['parent'],c['memory'],c['accepted_compact_index'],c['original_config']):check_reference(ref)
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Actual duplicate process')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120:raise ValueError('Own120s probe required')
    elif path==CONFIG:
        r=probe_evidence();estimate=estimate_training(r)
        if (c['phase']!='scientific' or c['reference_body_NLL']!=r['reference_body_NLL']
                or c['probe_config_sha256']!=sha256(PROBE_CONFIG) or c['probe_result_sha256']!=sha256(RUN/'probe/result.json')
                or c['estimated_GPU_seconds_with_margin']!=estimate
                or estimate+r['GPU_seconds']+c['previous_related_GPU_seconds']>2400
                or not math.isclose(c['GPU_budget_seconds']+r['GPU_seconds']+c['previous_related_GPU_seconds'],2400,abs_tol=1e-9)):
            raise ValueError('Measured block budget differs')
    else:raise ValueError('Only own fixed configs allowed')
    return c


def estimate_training(r):
    rows=r['timing']['histories'];source=statistics.median(v['seconds'] for v in rows[40:])
    raw=read_json(original.RUN/'probe/result.json')
    # Original unchanged MATH oracle timings already measured. Fixed worst
    # five forwards+one full gradient reserved once per block, not per update.
    oracle=5*max(raw['oracle_timings']['forward_only_seconds'])+max(raw['oracle_timings']['gradient_seconds'])
    block_overhead=max(max(0.,v['block_GPU_seconds']-sum(x['seconds'] for x in rows[i-19:i+1])) for i,v in enumerate(rows) if 'block_GPU_seconds' in v)
    warm=max(0.,sum(v['seconds'] for v in rows[:40])-40*source)
    blocks=math.ceil(3068/20)
    return (3068*source+warm+blocks*(oracle+block_overhead+r['timing']['terminal_save_seconds']))*1.3+200


def probe_evidence():
    r=read_json(RUN/'probe/result.json');job=read_json(RUN/'probe/job.json')
    if (job['status']!='complete' or alive(job) or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
            or r['config_sha256']!=sha256(PROBE_CONFIG) or not r['passed'] or not all(r['initial_checks'].values())
            or not all(r['gate']['checks'].values()) or not r['cached_projector_control_reused_without_new_GPU']):
        raise ValueError('Actual owned block CUDA evidence required')
    return r


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c=copy.deepcopy(inspect(PROBE_CONFIG));r=probe_evidence();estimate=estimate_training(r)
    total=estimate+r['GPU_seconds']+c['previous_related_GPU_seconds']
    if total>2400:raise ValueError('Measured block worst-case exceeds2400s, no launch')
    c.update(phase='scientific',reference_body_NLL=r['reference_body_NLL'],probe_config_sha256=sha256(PROBE_CONFIG),
        probe_result_sha256=sha256(RUN/'probe/result.json'),estimated_GPU_seconds_with_margin=estimate,
        verification_GPU_seconds=r['GPU_seconds'],verification_teacher_tokens=r['verification_source_CE_teacher_tokens'],
        GPU_budget_seconds=2400-r['GPU_seconds']-c['previous_related_GPU_seconds'],save_every_accepted_block=True)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='block_science_frozen',estimated_total_seconds=total)),flush=True)


def binding(c,path):
    return dict(config_sha256=sha256(path),arm=ARM,parent=c['parent'],study_kind=KIND,
        target_rule='original staged conditional outcome+EOS mask',optimizer_policy='inherited_Adam_block_boundary_finite_NLL_projection',
        memory=c['memory'],body_ceiling_multiplier=1.01,block_updates=20,peak_lr=.00001)


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c=inspect(path);output=RUN/'probe' if probe else RUN
    output.mkdir(parents=True,exist_ok=True);jp=output/'job.json';previous=read_json(jp) if jp.exists() else {}
    if previous.get('status')=='complete':print('Completed block study retained');return
    if previous and previous['config_sha256']!=sha256(path):raise ValueError('Interrupted config differs')
    prior_seconds=previous.get('GPU_elapsed_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),GPU_elapsed_seconds=prior_seconds,started_at=now(),
        restart_command=f"scripts/run_block_Web_constraint.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Tentative block rolled back; resume accepted boundary')
        if started[0] is not None and prior_seconds+time.monotonic()-started[0]>c['GPU_budget_seconds']:raise TimeoutError('Cumulative block GPU budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for s in (*c['source_sha256'],*c['old_source_sha256'],*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/s;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/s).read_bytes():raise ValueError('Original source snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/s,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);pool,web,positive=old.data(c)
        memory=torch.load(c['memory']['path'],map_location='cpu',weights_only=False);b=binding(c,path)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();heartbeat('GPU');progress=output/'progress-result.json'
            result=read_json(progress) if progress.exists() else {}
            reference_ce=c.get('reference_body_NLL',result.get('reference_body_NLL'))
            def build():return BlockWebTrainer(parent,pool,web,positive,c['teacher_goals'],b,memory,c['memory_binding'],reference_ce=reference_ce)
            if probe:
                if 'initial_checks' not in result:
                    t=build();reference_ce=t.reference_ce
                    checks=dict(model=equal_state(old.prior.cpu_state(t.model.state_dict()),parent['model']),
                        optimizer=equal_state(old.prior.cpu_state(t.optimizer.state_dict()),parent['optimizer']),
                        scheduler=equal_state(t.scheduler.state_dict(),parent['scheduler']),RNG=equal_state(rng_state(),parent['rng']),
                        Web_cursor=equal_state(t.sampler.streams['web'].sampler.state_dict(),parent['sampler']['web']),
                        actual_LR=all(g['lr']==.00001 for g in t.optimizer.param_groups),
                        same_original_memory_NLL=reference_ce==c['cached_original_body_NLL'])
                    if not all(checks.values()):raise ValueError('Original inherited state differs')
                    result.update(initial_checks=checks,reference_body_NLL=reference_ce,setup_oracle_counts=t.setup_oracle_counts)
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                if 'gate' not in result:
                    states=[];histories=[];teachers=0;aux=[]
                    for route in ('continuous','resumed'):
                        t=build();rows=[]
                        for i in range(2):
                            rows+=t.block(check)
                            if route=='resumed' and i==0:
                                t.save(output/'split.pt');del t;gc.collect();torch.cuda.empty_cache();t=build();t.load(output/'split.pt')
                        t.save(output/(route+'.pt'));states.append(torch.load(output/(route+'.pt'),map_location='cpu',weights_only=False))
                        histories.append(rows);teachers+=t.supervised_tokens-parent['supervised_tokens'];aux.append(t.auxiliary)
                        del t;gc.collect();torch.cuda.empty_cache()
                    checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
                    for key in set().union(*(row.keys() for row in histories[0]))-{'seconds','data_wait_seconds','tokens_per_second','block_GPU_seconds'}:
                        checks['history_'+key]=equal_state([r.get(key) for r in histories[0]],[r.get(key) for r in histories[1]])
                    checks.update(finite=all(finite_state(s) for s in states),actual_LR=all(r['lr']==.00001 for h in histories for r in h),
                        boundary_loss_bounded=all(r['boundary_constraint']['final_body_NLL']<=reference_ce*1.01 for h in histories for r in h),
                        two_full20_update_blocks=all(len(h)==40 and sum('block_GPU_seconds' in r for r in h)==2 for h in histories))
                    if not all(checks.values()):raise ValueError('Own CUDA block resume differs '+repr(checks))
                    result['gate']=dict(checks=checks,histories=histories,verification_teacher_tokens=teachers,auxiliary=aux,GPU_optimizer_updates=80)
                    atomic_json(progress,result);del states;gc.collect()
                if 'timing' not in result:
                    folder=output/'timing';folder.mkdir(parents=True,exist_ok=True);t=build();rows=[]
                    for _ in range(4):
                        rows+=t.block(check);heartbeat('block-timing',completed_updates=t.update-parent['update'])
                    seconds=t.save(folder/'checkpoint.pt')
                    if not finite_state(torch.load(folder/'checkpoint.pt',map_location='cpu',weights_only=False)):raise ValueError('Nonfinite timing state')
                    result['timing']=dict(histories=rows,terminal_save_seconds=seconds,verification_teacher_tokens=t.supervised_tokens-parent['supervised_tokens'],auxiliary=t.auxiliary)
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                result.update(passed=True,GPU_optimizer_updates=160,
                    verification_source_CE_teacher_tokens=result['gate']['verification_teacher_tokens']+result['timing']['verification_teacher_tokens'],
                    scientific_source_CE_teacher_tokens=0,cached_projector_control_reused_without_new_GPU=True,
                    cached_projector_control=c['cached_unchanged_projector_control'],all_probe_weights_discarded_for_science=True)
            else:
                if 'checkpoint' not in result and 'finite_rejection' not in result:
                    folder=output/ARM/'training';folder.mkdir(parents=True,exist_ok=True);t=build();cp=old.prior.latest(folder)
                    if cp is not None:t.load(cp)
                    log=folder/'metrics.jsonl';old.prior.reconcile(log,t.update,parent['update'])
                    expected=[json.loads(s) for s in Path(c['references']['staged_metrics']['path']).read_text().splitlines()]
                    with log.open('a',buffering=1) as stream:
                        while t.sampler.source_teachers!=c['teacher_goals']:
                            try:rows=t.block(check)
                            except ConstraintRejected:
                                cp=folder/f'checkpoint-{t.update:08d}.pt';t.save(cp)
                                result['finite_rejection']=dict(last_rejection=t.last_rejection,last_valid_checkpoint=reference(cp),
                                    accepted_source_updates=t.update-parent['update'],accepted_source_CE_teacher_tokens=t.supervised_tokens-parent['supervised_tokens'],accepted_auxiliary=t.auxiliary,whole_block_restored=True)
                                break
                            except (InterruptedError,TimeoutError):
                                cp=folder/f'checkpoint-{t.update:08d}.pt';t.save(cp);job['discarded_tentative_block']=t.last_rejection;raise
                            for row in rows:
                                if row['reference_token_digest']!=expected[row['update']-parent['update']-1]['token_digest']:raise ValueError('Original full staged reference differs')
                                stream.write(json.dumps(row,allow_nan=False)+'\n')
                            cp=folder/f'checkpoint-{t.update:08d}.pt';t.save(cp)
                            heartbeat('block-constrained-Base-training',completed_updates=t.update-parent['update'],total_updates=3068,
                                actual_teachers=t.supervised_tokens-parent['supervised_tokens'],loss=rows[-1]['loss'],boundary_constraint=t.last_constraint,auxiliary=t.auxiliary)
                    if 'finite_rejection' not in result:
                        ledger=read_json(Path(c['references']['reference_input_ledger']['path']))
                        if (t.update-parent['update']!=3068 or t.supervised_tokens-parent['supervised_tokens']!=91641755
                                or t.sampler.actual!=ledger['actual_source_accounting'] or t.sampler.source_digests!=ledger['source_digests']
                                or not equal_state(t.sampler.reference_state(),ledger['staged_reference_sampler'])):raise ValueError('Whole original staged source ledger differs')
                        result['checkpoint']=dict(checkpoint=str(cp),checkpoint_sha256=sha256(cp),binding=b,updates=3068,
                            additional_supervised_tokens=t.supervised_tokens-parent['supervised_tokens'],additional_input_tokens=t.tokens-parent['tokens'],
                            actual_source_accounting=t.sampler.actual,sampler=t.sampler.state_dict(),source_digests=t.sampler.source_digests,
                            token_digest=t.token_digest,reference_token_digest=t.sampler.reference_token_digest,
                            auxiliary=t.auxiliary,last_constraint=t.last_constraint,constraint_scope='Accepted block boundaries only')
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                if 'finite_rejection' not in result and 'evaluation' not in result:
                    base=read_json(Path(c['original_config']['path']));evaluation.RUN=output/'evaluation'
                    result['evaluation']=evaluation.evaluate(ARM,result['checkpoint'],Shard(Path(base['dev_shards']),'dev'),Tokenizer(ROOT/base['tokenizer']),base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-prior_seconds)
                    atomic_json(progress,result)
            check();elapsed=prior_seconds+time.monotonic()-started[0]
            result.update(status='block_probe_complete' if probe else ('block_rejection_branch_complete' if 'finite_rejection' in result else 'block_GPU_complete_pending_all80_content'),
                config_sha256=sha256(path),GPU_seconds=elapsed,Base_complete=False,Base_adopted=False,Chat_started=False,
                quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,constraint_scope=c['constraint_scope'])
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
            job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();m=p.add_mutually_exclusive_group()
    for mode in ('prepare','preflight-probe','probe','freeze','inspect'):m.add_argument('--'+mode,action='store_true')
    a=p.parse_args()
    if a.prepare:prepare()
    elif a.preflight_probe:inspect(PROBE_CONFIG)
    elif a.freeze:freeze()
    elif a.inspect:inspect(CONFIG)
    else:run(a.probe)
