"""Historical Web fullstate route vs cached original10B route; equal100M teachers."""
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
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state,restore_rng
from historical_parent_condition_trainer import HistoricalParentTrainer,historical_web_cursor
from audit_base_parent_baselines import metadata as parent_metadata
import run_original_web_retention_comparison as previous
import run_mature_base_condition_comparison as mature
from condition_relation_language import RelationLanguageTrainView
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive,identity,finite_state
from run_eos_short_pilot import equal_state
import run_condition_source_learning as prior
import run_condition_transfer_comparison as control_study
import run_condition_source_ranking as ranking
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/historical-parent-condition-comparison-v3-20261006'
CONFIG=ROOT/'configs/phase6/historical_parent_condition_comparison_v3.json'
PROBE_CONFIG=ROOT/'configs/phase6/historical_parent_condition_probe_v3.json'
PROPOSAL=ROOT/'reports/phase6/historical_parent_condition_comparison_v3_proposal.json'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006')
PREP_RUN=ROOT/'reports/phase6/condition-relation-language-20261006'
TOTAL=100000000
CEILING=900
ARM='historical_parent'
KIND='historical_Web_parent_inherited_condition_100M'
GOALS=dict(web=75000000,story=5000000,ordinary_textbook=10000000,conditional_textbook=10000000)
SOURCES=tuple(dict.fromkeys(('scripts/run_historical_parent_condition_comparison_v3.py','scripts/run_historical_parent_condition_comparison_v3.ps1',
    'scripts/review_historical_parent_condition_comparison_v3.py','scripts/historical_parent_condition_trainer.py',
    'scripts/audit_base_parent_baselines.py','tests/test_historical_parent_condition.py','tests/test_historical_parent_comparison_v3.py',
    'tests/test_base_parent_baselines.py',*previous.SOURCES)))
reference,check_reference=prior.reference,prior.check_reference
latest,reconcile,detail=prior.latest,prior.reconcile,prior.detail


def inherited_lr_preserved(value):
    return math.isclose(value, .00001, rel_tol=1e-10)


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
    checks['no_reheat'] = all(inherited_lr_preserved(r['lr']) for h in histories for r in h)
    if not all(checks.values()): raise ValueError('CUDA resume full-state mismatch: ' + repr(checks))
    result = dict(passed=True, checks=checks, histories=histories, config_sha256=config_sha,
        GPU_optimizer_updates=8, verification_teacher_tokens=teachers)
    atomic_json(record, result); return result



def cpu_state(value):
    if isinstance(value,torch.Tensor):return value.detach().cpu()
    if isinstance(value,dict):return {k:cpu_state(v) for k,v in value.items()}
    if isinstance(value,list):return [cpu_state(v) for v in value]
    if isinstance(value,tuple):return tuple(cpu_state(v) for v in value)
    return value


def source_contract():
    old,base,_,_,_,positive,original=previous.inspect(previous.CONFIG)
    p=read_json(PROPOSAL)
    for ref in p['references'].values():check_reference(ref)
    check_reference(p['parent'])
    audit=read_json(Path(p['references']['parent_audit']['path']))
    result=read_json(previous.RUN/'compare-result.json');review=read_json(previous.RUN/'review.json')
    control=result['checkpoints']['original_web'];ev=result['evaluations']['original_web']
    if (p['quotas']!=GOALS or p['new_scientific_teacher_tokens']!=TOTAL or p['reused_control_teacher_tokens']!=TOTAL
            or p['new_GPU_ceiling_seconds']!=CEILING or p['actual_inherited_LR']!=.00001
            or p['Base_adopted'] or p['Base_complete'] or p['Chat_started'] or p['quantization_started']
            or p['protected_test_used'] or not p['quality_criteria_unchanged'] or p['source']!=old['positive_data']
            or audit['historical_parent_training_matches'] or p['parent']!=audit['states']['historicalWeb']['checkpoint']
            or p['parent_actual_metadata']!=audit['states']['historicalWeb']
            or review['result_sha256']!=sha256(previous.RUN/'compare-result.json')
            or control['additional_supervised_tokens']!=TOTAL or control['source_teachers']!=GOALS
            or control['checkpoint_sha256']!=ev['checkpoint_sha256'] or control['binding']!=ev['binding']
            or review['summaries']['original_web']['notes_sha256']!=sha256(ROOT/'reports/phase6/original_web_retention_notes.json')):
        raise ValueError('Preselected historical inherited route and actual cached original10B control required')
    parent=torch.load(p['parent']['path'],map_location='cpu',weights_only=False)
    expected={k:v for k,v in p['parent_actual_metadata'].items() if k!='checkpoint'}
    if parent_metadata(parent)!=expected:raise ValueError('Actual historical fullstate differs from fixed audit')
    historical_web_cursor(parent)
    old=copy.deepcopy(old);old['parent']=p['parent']
    return old,base,parent,control,ev,positive,original


def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,control,_,positive,original=source_contract()
    c=dict(research_kind=KIND,phase='probe',parent=old['parent'],original_config=old['original_config'],pool=old['pool'],
        accepted_compact_index=old['accepted_compact_index'],positive_data=old['positive_data'],
        original_web=dict(path=str(original.directory),manifest_sha256=sha256(original.directory/'manifest.json')),
        arms={ARM:GOALS},outcome_weights={ARM:1},teachers_per_new_arm=TOTAL,total_comparison_teachers=2*TOTAL,
        peak_lr=.00001,optimizer_policy='inherit',shapes=old['shapes'],GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,
        failed_probe_GPU_seconds=read_json(PROPOSAL)['failed_probe_GPU_seconds'],
        loss='ordinary original body+EOS CE, outcome weight1',
        sampler_policy='Continue actual historical sampler/web cursor without reset and actual terminalLR0.00001 without reheat. Same fresh seed42 short streams and100M quota; parent Web amount/order/Adam/RNG/scheduler and LR differ from original10B control, not pure LR causality.',
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        references=dict(proposal=reference(PROPOSAL),diagnostic=reference(ROOT/'reports/phase6/base_parent_baseline_audit.json'),
            control_config=reference(previous.CONFIG),control_result=reference(previous.RUN/'compare-result.json'),control_review=reference(previous.RUN/'review.json'),
            control_notes=reference(ROOT/'reports/phase6/original_web_retention_notes.json'),
            control_generation=reference(previous.RUN/'evaluation/original_web/evaluation/generation.json'),
            original_manifest=reference(original.directory/'manifest.json'),original_recipe=reference(ROOT/'configs/phase6/base_10b.json'),
            manifest=reference(DATA/'manifest.json'),arrays=reference(DATA/'train.npz'),content_review=reference(DATA/'content-review.json'),
            content_notes=reference(DATA/'content-notes.json'),source_cases=reference(DATA/'transfer-probes.json'),
            retention_cases=reference(DATA/'retention-probes.json'),source_text=reference(DATA/'train-source.json')),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        quality_criteria_unchanged=True,old_numerical7_preserved=True,Base_adopted=False,Chat_adopted=False,
        quantization_started=False,protected_test_used=False,requested_five_steps_complete=False,scientific_teacher_tokens=0,created_at=now())
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print('Historical fullstate inherited100M probe frozen; science not started',flush=True)


def scope(c):
    if (c['research_kind']!=KIND or c['arms']!={ARM:GOALS} or c['outcome_weights']!={ARM:1}
            or c['teachers_per_new_arm']!=TOTAL or c['total_comparison_teachers']!=2*TOTAL or c['total_new_GPU_ceiling_seconds']!=CEILING
            or c['failed_probe_GPU_seconds']!=read_json(PROPOSAL)['failed_probe_GPU_seconds']
            or c['peak_lr']!=.00001 or c['optimizer_policy']!='inherit'
            or c['shapes']!=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16')
            or c['loss']!='ordinary original body+EOS CE, outcome weight1' or c['Base_adopted'] or c['Chat_adopted']
            or c['quantization_started'] or c['protected_test_used'] or c['requested_five_steps_complete'] or not c['quality_criteria_unchanged']):
        raise ValueError('Same100M weight1 original-Web scope differs')


def inspect(path):
    c=read_json(path);scope(c);old,base,parent,control,ev,positive,original=source_contract()
    if c['implementation']!=implementation_hashes() or c['source_sha256']!={p:sha256(ROOT/p) for p in SOURCES}:raise ValueError('Frozen comparison source differs')
    for ref in (*c['references'].values(),c['parent'],c['original_config'],c['accepted_compact_index'],c['reused_control_checkpoint']):check_reference(ref)
    if (c['parent']!=old['parent'] or c['pool']!=old['pool'] or c['shapes']!=old['shapes']
            or c['positive_data']!=dict(path=str(DATA),manifest_sha256=positive.manifest_sha256)
            or c['reused_control_checkpoint']!=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256'])
            or c['original_web']!=dict(path=str(original.directory),manifest_sha256=sha256(original.directory/'manifest.json'))):
        raise ValueError('Same actual parent/material/control binding differs')
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Actual comparison live; no duplicate GPU')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120:raise ValueError('Probe scope differs')
    elif path==CONFIG:
        measured=probe_evidence();timing,estimate=estimate_training(measured)
        if (c['phase']!='scientific' or c['probe_config_sha256']!=sha256(PROBE_CONFIG) or c['probe_result_sha256']!=sha256(RUN/'probe/result.json')
                or c['verification_GPU_seconds']!=measured['GPU_seconds']+c['failed_probe_GPU_seconds'] or c['verification_teacher_tokens']!=measured['verification_teacher_tokens']
                or c['measured_timing']!=timing or c['estimated_GPU_seconds_with_margin']!=estimate
                or not math.isclose(c['GPU_budget_seconds']+measured['GPU_seconds']+c['failed_probe_GPU_seconds'],CEILING,abs_tol=1e-9) or estimate+measured['GPU_seconds']+c['failed_probe_GPU_seconds']>CEILING):
            raise ValueError('Actual measured bounded science differs')
    else:raise ValueError('Only frozen comparison configs allowed')
    return c,base,parent,control,ev,positive,original


def probe_evidence():
    job=read_json(RUN/'probe/job.json');r=read_json(RUN/'probe/result.json')
    if (job['status']!='complete' or alive(job) or not r['passed'] or r['config_sha256']!=sha256(PROBE_CONFIG)
            or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
            or not r['gate']['passed'] or not all(r['gate']['checks'].values())):raise ValueError('Actual original-Web CUDA resume/timing required')
    return r


def estimate_training(measured):
    record=measured['timing'];rows=record['histories']
    if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 for r in rows):raise ValueError('Actual32 continuous timings required')
    step=statistics.median(r['seconds'] for r in rows[8:]);teachers=record['verification_teacher_tokens']/32
    updates=math.ceil(TOTAL/teachers);warm=max(0.,sum(r['seconds'] for r in rows[:8])-8*step)
    save=(math.ceil(updates/250)+1)*record['terminal_save_seconds'];total=updates*step+warm+save
    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total),total*1.3+300+50


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c,*_=inspect(PROBE_CONFIG);c=copy.deepcopy(c);r=probe_evidence();timing,estimate=estimate_training(r)
    if estimate+r['GPU_seconds']+c['failed_probe_GPU_seconds']>CEILING:raise ValueError('Measured science exceeds900s; retain evidence')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        verification_GPU_seconds=r['GPU_seconds']+c['failed_probe_GPU_seconds'],verification_teacher_tokens=r['verification_teacher_tokens'],GPU_budget_seconds=CEILING-r['GPU_seconds']-c['failed_probe_GPU_seconds'],
        measured_timing=timing,estimated_GPU_seconds_with_margin=estimate,save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='measured100M_historical_parent_frozen',timing=timing,estimate=estimate)),flush=True)


def binding(c,path):
    return dict(config_sha256=sha256(path),arm=ARM,parent=c['parent'],short_manifest_sha256=c['pool']['manifest_sha256'],teacher_goals=GOALS,
        optimizer_policy='inherit',peak_lr=.00001,loss=c['loss'],study_kind=KIND,sampler_policy=c['sampler_policy'],outcome_weight=1,
        positive_manifest_sha256=c['positive_data']['manifest_sha256'],original_web=c['original_web'])


def trainer_for(parent,pool,positive,original,b,device='cuda',context=1024,batch=32):
    return HistoricalParentTrainer(parent,pool,original,positive,GOALS,b,device,context,batch)


def summarize_transfer(rows,prepared):
    cases=prepared['cases'];ranking.validate_scores(rows,cases);keyed={r['index']:r for r in rows}
    pairs=[]
    for family in prepared['families']:
        f=family['index'];subset=[c for c in cases if c['family']==f]
        if len(subset)!=4 or {(c['branch'],c['candidate']) for c in subset}!={(b,k) for b in (0,1) for k in (0,1)}:raise ValueError('Complete two-condition family required')
        indexed={(c['branch'],c['candidate']):keyed[c['index']] for c in subset}
        for metric in ranking.METRICS:
            margins=[ranking.metric_value(indexed[(b,0)],metric)-ranking.metric_value(indexed[(b,1)],metric) for b in (0,1)]
            credit=[.5 if abs(m)<=1e-9 else float(m>0 if b==0 else m<0) for b,m in enumerate(margins)]
            pairs.append(dict(family=f,id=family['id'],split=family['split'],category=family['category'],metric=metric,
                credits=credit,margins=margins,both_correct=credit==[1.,1.],same_unique_candidate=margins[0]*margins[1]>0,
                context_margin_shift=margins[0]-margins[1]))
    aggregate={}
    for metric in ranking.METRICS:
        aggregate[metric]={}
        for split in ('all128','lexical_holdout','structural_holdout'):
            selected=[p for p in pairs if p['metric']==metric and (split=='all128' or p['split']==split)]
            aggregate[metric][split]=dict(families=len(selected),accuracy=sum(sum(p['credits']) for p in selected)/2/len(selected),
                both_correct=sum(p['both_correct'] for p in selected),same_unique_candidate=sum(p['same_unique_candidate'] for p in selected),
                aligned_context_margin_shift=sum(p['context_margin_shift']>0 for p in selected))
    return dict(aggregate=aggregate,pairs=pairs)


def transfer_scores(c,arm,checkpoint,heartbeat,check,suite='bridge'):
    cases_key='source_cases' if suite=='bridge' else 'retention_cases'
    folder=RUN/'transfer'/suite/arm;terminal=folder/'result.json';cfg=sha256(CONFIG);cases_sha=c['references'][cases_key]['sha256']
    check_reference(checkpoint)
    if terminal.exists():
        saved=read_json(terminal)
        if saved['config_sha256']!=cfg or saved['checkpoint_sha256']!=checkpoint['sha256'] or saved['cases_sha256']!=cases_sha:raise ValueError('Saved transfer binding differs')
        return saved
    prepared=read_json(Path(c['references'][cases_key]['path']));before_rng=rng_state()
    state=torch.load(checkpoint['path'],map_location='cpu',weights_only=False);model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
    before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()};scorer=NativeLikelihood(model,None,'cuda','bf16',16)
    hook=model.register_forward_pre_hook(lambda *_:check());rows=[]
    try:
        with sdpa_kernel(SDPBackend.MATH):
            for start in range(0,512,16):
                cases=prepared['cases'][start:start+16];path=folder/f'{start:04d}.json';check()
                if path.exists():
                    saved=read_json(path)
                    if saved['config_sha256']!=cfg or saved['checkpoint_sha256']!=checkpoint['sha256'] or saved['cases_sha256']!=cases_sha:raise ValueError('Saved transfer request differs')
                    scored=saved['rows']
                else:
                    scored=[dict(index=case['index'],**r) for case,r in zip(cases,scorer.score_encoded(cases),strict=True)]
                    ranking.validate_scores(scored,cases);atomic_json(path,dict(config_sha256=cfg,checkpoint_sha256=checkpoint['sha256'],cases_sha256=cases_sha,rows=scored))
                ranking.validate_scores(scored,cases);rows.extend(scored);heartbeat(arm+'-transfer128',completed_requests=len(rows),total_requests=512)
        checks=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training)
    finally:hook.remove();restore_rng(before_rng)
    checks['RNG_restored']=equal_state(before_rng,rng_state())
    if not all(checks.values()):raise ValueError('Read-only transfer scoring altered weights/RNG')
    result=dict(config_sha256=cfg,checkpoint_sha256=checkpoint['sha256'],cases_sha256=cases_sha,checks=checks,
        summary=summarize_transfer(rows,prepared),evaluated_requests=512,optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
        suite=suite,limitations='Local generated state entailment, shared generator rules, one learned seed; not independent natural-language quality. Original128 retention are not newly held-out grammar after language replacement.')
    atomic_json(terminal,result);del state,model,before,scorer;gc.collect();torch.cuda.empty_cache();return result


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG; c,base,parent,control,control_ev,positive,original=inspect(path)
    output=RUN/'probe' if probe else RUN; output.mkdir(parents=True,exist_ok=True)
    jp=output/'job.json'; old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(path): raise ValueError('Prior job binding differs')
    if old.get('status')=='complete': print('Completed comparison retained; no duplicate GPU'); return
    prior_seconds=old.get('GPU_elapsed_seconds',0.); started,stopped=[None],[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),started_at=old.get('started_at',now()),
        GPU_elapsed_seconds=prior_seconds,Base_adopted=False,protected_test_used=False,
        restart_command=f"scripts/run_historical_parent_condition_comparison_v3.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM): signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]: raise InterruptedError('Interrupted; completed updates retained')
        if started[0] is not None and prior_seconds+time.monotonic()-started[0]>c['GPU_budget_seconds']: raise TimeoutError('Cumulative comparison GPU budget exhausted')
    def heartbeat(stage,**values):
        check(); job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None: job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True); heartbeat('setup')
        for relative in (*SOURCES,*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative; target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes(): raise ValueError('Source snapshot differs')
            if not target.exists(): shutil.copyfile(ROOT/relative,target)
        check_reference(c['accepted_compact_index']); pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']); pool.index=CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused: raise ValueError('Index must be reused')
        b=binding(c,path)
        def build(): return trainer_for(parent,pool,positive,original,b)
        with gpu_lock('cuda'):
            started[0]=time.monotonic(); heartbeat('gpu')
            if probe:
                initial=build()
                preservation=dict(model=equal_state(cpu_state(initial.model.state_dict()),cpu_state(parent['model'])),
                    optimizer=equal_state(cpu_state(initial.optimizer.state_dict()),cpu_state(parent['optimizer'])),
                    scheduler=equal_state(initial.scheduler.state_dict(),parent['scheduler']),
                    RNG=equal_state(rng_state(),parent['rng']),
                    actual_Web_cursor=equal_state(initial.sampler.streams['web'].state_dict()['sampler'],historical_web_cursor(parent)),
                    parent_sampler_lineage=equal_state(initial.lineage['actual_parent_sampler'],parent['sampler']),
                    actual_LR=[g['lr'] for g in initial.optimizer.param_groups]==[.00001,.00001])
                if not all(preservation.values()):raise ValueError('Initial historical model/Adam/scheduler/RNG/cursor/LR not preserved')
                atomic_json(output/'initial-parent-preservation.json',preservation)
                del initial;gc.collect();torch.cuda.empty_cache()
                gate=resume_gate(build,output/'resume-gate',sha256(path),check)
                folder=output/'timing'; folder.mkdir(parents=True,exist_ok=True); trainer=build(); cp=latest(folder)
                if cp is not None: trainer.load(cp)
                log=folder/'metrics.jsonl'; reconcile(log,trainer.update,parent['update'])
                with log.open('a',buffering=1) as stream:
                    while trainer.update-parent['update']<32:
                        try: check()
                        except (InterruptedError,TimeoutError): trainer.save(folder/'checkpoint.pt'); raise
                        row=trainer.step(); stream.write(json.dumps(row,allow_nan=False)+'\n')
                        if trainer.sampler.position%8==0: heartbeat('timing',completed_updates=trainer.sampler.position)
                cp=folder/'checkpoint.pt'; saved_seconds=trainer.save(cp); rows=[json.loads(s) for s in log.read_text().splitlines()]
                if any(not equal_state(row[k],reference_row[k]) for row,reference_row in zip(rows[:4],gate['histories'][0],strict=True)
                        for k in ('loss','gradient_norm','lr','token_digest','source_teachers')): raise ValueError('Probe trajectories differ')
                timing=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                    terminal_save_seconds=saved_seconds,checkpoint=str(cp),checkpoint_sha256=sha256(cp))
                result=dict(status='actual_historical_parent_resume_timing_complete',passed=True,gate=gate,timing=timing,
                    config_sha256=sha256(path),verification_teacher_tokens=gate['verification_teacher_tokens']+timing['verification_teacher_tokens'],
                    GPU_optimizer_updates=40,scientific_teacher_tokens=0,weights_discarded_for_science=True,initial_parent_preservation=preservation)
                del trainer; gc.collect(); torch.cuda.empty_cache()
            else:
                progress=output/'progress-result.json'
                result=read_json(progress) if progress.exists() else dict(checkpoints=dict(control=control),evaluations=dict(control=control_ev))
                if result['checkpoints']['control']!=control or result['evaluations']['control']!=control_ev: raise ValueError('Reused control changed')
                if ARM not in result['checkpoints']:
                    folder=output/ARM/'training'; folder.mkdir(parents=True,exist_ok=True); trainer=build(); cp=latest(folder)
                    if cp is not None: trainer.load(cp)
                    log=folder/'metrics.jsonl'; seconds=reconcile(log,trainer.update,parent['update'])
                    with log.open('a',buffering=1) as stream:
                        while trainer.sampler.source_teachers!=GOALS:
                            try: check()
                            except (InterruptedError,TimeoutError): trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt'); raise
                            row=trainer.step(); seconds+=row['seconds']; stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if trainer.sampler.position%20==0: heartbeat('training',teachers=row['additional_teacher_tokens'],teacher_budget=TOTAL,source_teachers=row['source_teachers'],loss=row['loss'])
                            if trainer.sampler.position%250==0: trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                    cp=folder/f'checkpoint-{trainer.update:08d}.pt'; trainer.save(cp); result['checkpoints'][ARM]=detail(trainer,cp,b,seconds)
                    atomic_json(progress,result); del trainer; gc.collect(); torch.cuda.empty_cache()
                if ARM not in result['evaluations']:
                    evaluation.RUN=output/'evaluation'; dev=Shard(Path(base['dev_shards']),'dev'); tok=Tokenizer(ROOT/base['tokenizer'])
                    result['evaluations'][ARM]=evaluation.evaluate(ARM,result['checkpoints'][ARM],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-prior_seconds)
                    atomic_json(progress,result)
                reused=read_json(previous.RUN/'compare-result.json')
                result.setdefault('transfer',dict(control=reused['transfer']['original_web']))
                result.setdefault('retention',dict(control=reused['retention']['original_web']))
                if (result['transfer']['control']!=reused['transfer']['original_web']
                        or result['retention']['control']!=reused['retention']['original_web']):
                    raise ValueError('Cached same-weight control128 bridge/retention differs')
                checkpoint=dict(path=result['checkpoints'][ARM]['checkpoint'],sha256=result['checkpoints'][ARM]['checkpoint_sha256'])
                for suite,key in (('bridge','transfer'),('retention','retention')):
                    if ARM not in result[key]:
                        result[key][ARM]=transfer_scores(c,ARM,checkpoint,heartbeat,check,suite)
                        atomic_json(progress,result)
                result.update(status='historical_parent100M_and_reused_original10B_route100M_complete',
                    config_sha256=sha256(path),scientific_teacher_tokens=TOTAL,total_comparison_teachers=2*TOTAL,
                    reused_control=True,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
            check(); elapsed=prior_seconds+time.monotonic()-started[0]; result['GPU_seconds']=elapsed
            job.update(status='complete',stage='complete',completed_at=now(),GPU_elapsed_seconds=elapsed)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
    except BaseException as error:
        job.update(status='failed',error=repr(error)); raise
    finally:
        if started[0] is not None and job['status']!='complete': job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser(); modes=p.add_mutually_exclusive_group()
    for mode in ('prepare-probe','preflight-probe','probe','freeze','inspect'): modes.add_argument('--'+mode,action='store_true')
    args=p.parse_args()
    if args.prepare_probe: prepare_probe()
    elif args.preflight_probe: inspect(PROBE_CONFIG)
    elif args.freeze: freeze()
    elif args.inspect: inspect(CONFIG)
    else: run(args.probe)
