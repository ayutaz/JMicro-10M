"""Same fullstate, staged100M and replay windows; omit only the EOS-mass KL component."""
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
from source_order_condition_trainer import SOURCE_ORDER
from context_outcome_ranking_resident_trainer import ContextOutcomeRankingTrainer,KIND
from context_outcome_ranking import POLICY as RANKING_POLICY,RankingTrainView
import run_eos_decoupled_web_kl_comparison as base_study
from eos_decoupled_web_kl_preservation import POLICY
import source_order_budget_evidence as budget_evidence
from historical_parent_condition_trainer import historical_web_cursor
import run_source_order_condition_comparison_v2 as cached
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

RUN=ROOT/'reports/phase6/context-outcome-ranking-comparison-20261006'
CONFIG=ROOT/'configs/phase6/context_outcome_ranking_comparison.json'
PROBE_CONFIG=ROOT/'configs/phase6/context_outcome_ranking_probe.json'
PROPOSAL=ROOT/'reports/phase6/context_outcome_ranking_proposal.json'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-relation-language-20261006')
PREP_RUN=ROOT/'reports/phase6/condition-relation-language-20261006'
TOTAL=100000000
CEILING=900
ARM='context_outcome_ranking'
MECHANISM_RUN=base_study.RUN
MECHANISM_ARM=base_study.ARM
QUALITY_BASELINE='cached-staged-CE23-EOS76-repetition2-all-original-gates'
GOALS=dict(web=75000000,story=5000000,ordinary_textbook=10000000,conditional_textbook=10000000)
FAILED_PROBE=ROOT/'reports/phase6/web_kl_initial_CUDA_failure.json'
RESIDENT_PROPOSAL=ROOT/'reports/phase6/web_kl_resident_repair_proposal.json'
PRIOR_GPU=0. # No GPU work for this distinct, newly frozen objective-component study yet.
SOURCES=tuple(dict.fromkeys((*('scripts/implement_context_outcome_ranking_comparison.py', 'scripts/context_outcome_ranking.py', 'scripts/prepare_context_outcome_ranking_inputs.py', 'scripts/prepare_context_outcome_ranking_trainer.py', 'scripts/context_outcome_ranking_trainer.py', 'scripts/context_outcome_ranking_resident_trainer.py', 'scripts/run_context_outcome_ranking_comparison.py', 'scripts/run_context_outcome_ranking_comparison.ps1', 'scripts/context_outcome_ranking_accounting.py', 'scripts/review_context_outcome_ranking_comparison.py', 'scripts/prepare_context_outcome_ranking_content_review.py', 'tests/test_context_outcome_ranking.py', 'tests/test_context_outcome_ranking_trainer.py', 'tests/test_context_outcome_ranking_comparison.py'),*base_study.SOURCES)))
reference,check_reference=prior.reference,prior.check_reference
latest,reconcile,detail=prior.latest,prior.reconcile,prior.detail


def performance_reference():
    return reference(ROOT/'reports/phase6/web_kl_resident_window_preparation.json')


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
    teachers = 0; reference_inputs=reference_positions=0
    reference_mass=0.;ranking_totals=[]
    for route in ('continuous', 'resumed'):
        trainer = build(); before = trainer.supervised_tokens; rows = []
        for index in range(4):
            check(); rows.append(trainer.step())
            if route == 'resumed' and index == 1:
                path = folder / 'split.pt'; trainer.save(path)
                del trainer; gc.collect(); torch.cuda.empty_cache(); trainer = build(); trainer.load(path)
        ranking_totals.append(ranking_counts(trainer))
        teachers += trainer.supervised_tokens - before
        reference_mass+=trainer.reference_non_EOS_teacher_mass
        reference_inputs+=trainer.replay.physical_input_tokens;reference_positions+=trainer.replay.body_positions
        path = folder / (route + '.pt'); trainer.save(path)
        states.append(torch.load(path, map_location='cpu', weights_only=False)); histories.append(rows)
        del trainer; gc.collect(); torch.cuda.empty_cache()
    checks = {k: equal_state(states[0][k], states[1][k]) for k in
        ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'lineage', 'tokens', 'supervised_tokens',
         'body_bytes', 'token_digest', 'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass',
         'update', 'spec', 'model_config', 'pilot_binding', 'study_binding', 'KL_state','ranking_state')}
    for key in ('loss', 'gradient_norm', 'lr', 'token_digest', 'source_teachers', 'source_eos', 'source_input_tokens', 'source_body_bytes', 'source_focus_teachers',
                'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass', 'ordinary_CE_loss', 'reference_KL_loss',
                'reference_non_EOS_teacher_probability_mass','reference_input_tokens', 'reference_soft_target_body_positions', 'reference_ignored_positions', 'reference_digest', 'combined_student_physical_input_tokens',
                'ranking_loss','ranking_family_indices','ranking_digest','ranking_relational_choice_labels','ranking_valid_input_tokens','ranking_physical_input_positions',
                'ranking_gold_body_scored_positions','ranking_foil_body_scored_positions','ranking_gold_body_scored_bytes','ranking_foil_body_scored_bytes','combined_student_valid_input_tokens'):
        checks['history_' + key] = all(equal_state(a[key], b[key]) for a, b in zip(*histories, strict=True))
    checks['finite'] = all(finite_state(s) for s in states)
    checks['no_reheat'] = all(inherited_lr_preserved(r['lr']) for h in histories for r in h)
    if not all(checks.values()): raise ValueError('CUDA resume full-state mismatch: ' + repr(checks))
    result = dict(passed=True, checks=checks, histories=histories, config_sha256=config_sha,
        verification_reference_non_EOS_teacher_probability_mass=reference_mass,GPU_optimizer_updates=8, verification_teacher_tokens=teachers,verification_reference_input_tokens=reference_inputs,verification_reference_soft_positions=reference_positions,verification_ranking=sum_ranking(ranking_totals))
    atomic_json(record, result); return result



def ranking_counts(trainer):
    sampler=trainer.ranking.state_dict()
    keys=('updates','families_seen','relational_choice_labels','valid_input_tokens','physical_input_positions',
          'gold_body_scored_positions','foil_body_scored_positions','gold_body_scored_bytes','foil_body_scored_bytes')
    return {k:sampler[k] for k in keys}


def sum_ranking(rows):
    return {k:sum(row[k] for row in rows) for k in rows[0]}


def cpu_state(value):
    if isinstance(value,torch.Tensor):return value.detach().cpu()
    if isinstance(value,dict):return {k:cpu_state(v) for k,v in value.items()}
    if isinstance(value,list):return [cpu_state(v) for v in value]
    if isinstance(value,tuple):return tuple(cpu_state(v) for v in value)
    return value


def source_contract():
    old,base,parent,control,ev,positive,original=base_study.inspect(base_study.CONFIG)
    p=read_json(PROPOSAL);prep=read_json(Path(p['preparation']['path']))
    for key in ('trigger','preparation','mechanism_control_config','mechanism_control_completion',
                'mandatory_stronger_quality_control_config','ranking_inputs','resident_input_preparation'):
        check_reference(p[key])
    for ref in (prep['diagnostic'],prep['input_preparation'],prep['manifest'],prep['rows']):check_reference(ref)
    for path,digest in prep['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Prepared owned prototype differs')
    if (p['parent']!=old['parent'] or p['pool']!=old['pool'] or p['original_web']!=old['original_web']
            or p['positive_data']!=old['positive_data'] or p['fixed_primary']['quotas']!=GOALS
            or p['fixed_primary']['ordinary_CE_teachers']!=TOTAL
            or p['one_new_auxiliary']['coefficient']!=1 or p['one_new_auxiliary']['temperature']!=1
            or p['one_new_auxiliary']['families_per_update']!=2 or p['one_new_auxiliary']['context']!=256
            or p['proposed_new_GPU_ceiling_seconds']!=CEILING or p['Base_complete'] or p['protected_test_used']
            or prep['GPU_training_seconds'] or prep['scientific_teacher_tokens']
            or not prep['quality_criteria_unchanged']):raise ValueError('One fixed train-ranking100M proposal required')
    mechanism_job=read_json(MECHANISM_RUN/'job.json')
    if mechanism_job['status']!='complete' or alive(mechanism_job):raise ValueError('Mechanism control must be terminal')
    ranking_view(p['ranking_inputs'])
    return old,base,parent,control,ev,positive,original


def ranking_view(record):
    check_reference(record)
    return RankingTrainView(Path(record['path']).parent,record['sha256'])


def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,control,_,_,_=source_contract();p=read_json(PROPOSAL)
    c=copy.deepcopy(old)
    previous=read_json(ROOT/'reports/phase6/hard_body_web_replay_comparison_completion.json')
    c.update(research_kind=KIND,phase='probe',arms={ARM:GOALS},outcome_weights={ARM:1},KL_policy=POLICY,
        ranking_policy=RANKING_POLICY,ranking_inputs=p['ranking_inputs'],
        quality_screen_baseline=QUALITY_BASELINE,previous_related_study_GPU_seconds=previous['cumulative_related_GPU_seconds'],
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,prior_probe_GPU_seconds=PRIOR_GPU,
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        source_order=list(SOURCE_ORDER),created_at=now(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        sampler_policy='Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus.')
    c['references'].update(proposal=reference(PROPOSAL),ranking_preparation=p['preparation'],
        ranking_inputs=p['ranking_inputs'],diagnostic=p['trigger'],
        mechanism_config=reference(base_study.CONFIG),mechanism_result=reference(MECHANISM_RUN/'compare-result.json'),
        mechanism_review=reference(ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_review.json'),
        mechanism_completion=p['mechanism_control_completion'],
        previous_related_completion=reference(ROOT/'reports/phase6/hard_body_web_replay_comparison_completion.json'))
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print('Owned three-loss CUDA probe frozen; no scientific training yet',flush=True)


def scope(c):
    if c['ranking_policy']!=RANKING_POLICY or c['ranking_inputs']!=read_json(PROPOSAL)['ranking_inputs']:
        raise ValueError('Fixed train-only ranking policy/input differs')
    if (c['quality_screen_baseline']!=QUALITY_BASELINE or c['KL_policy']!=POLICY or c['research_kind']!=KIND or c['arms']!={ARM:GOALS} or c['outcome_weights']!={ARM:1}
            or c['teachers_per_new_arm']!=TOTAL or c['total_comparison_teachers']!=2*TOTAL or c['total_new_GPU_ceiling_seconds']!=CEILING
            or c['prior_probe_GPU_seconds']!=PRIOR_GPU or c['source_order']!=list(SOURCE_ORDER)
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
                or c['verification_GPU_seconds']!=measured['GPU_seconds']+c['prior_probe_GPU_seconds'] or c['verification_teacher_tokens']!=measured['verification_teacher_tokens']
                or c['verification_reference_non_EOS_teacher_probability_mass']!=measured['verification_reference_non_EOS_teacher_probability_mass']
                or c['verification_reference_input_tokens']!=measured['verification_reference_input_tokens'] or c['verification_reference_soft_positions']!=measured['verification_reference_soft_positions']
                or c['measured_timing']!=timing or c['estimated_GPU_seconds_with_margin']!=estimate
                or not math.isclose(c['GPU_budget_seconds']+measured['GPU_seconds']+c['prior_probe_GPU_seconds'],CEILING,abs_tol=1e-9) or estimate+measured['GPU_seconds']+c['prior_probe_GPU_seconds']>CEILING):
            raise ValueError('Actual measured bounded science differs')
    else:raise ValueError('Only frozen comparison configs allowed')
    return c,base,parent,control,ev,positive,original


def probe_evidence():
    job=read_json(RUN/'probe/job.json');r=read_json(RUN/'probe/result.json')
    if (job['status']!='complete' or alive(job) or not r['passed'] or r['config_sha256']!=sha256(PROBE_CONFIG)
            or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120
            or not r['gate']['passed'] or not all(r['gate']['checks'].values())):raise ValueError('Actual original-Web CUDA resume/timing required')
    previous=read_json(MECHANISM_RUN/'probe/result.json')
    keys=('lr','token_digest','source_teachers','source_eos',
          'source_input_tokens','source_body_bytes','source_focus_teachers','reference_input_tokens','reference_soft_target_body_positions','reference_digest')
    if len(r['timing']['histories'])!=32 or len(previous['timing']['histories'])!=32:
        raise ValueError('All32 same-math update records required')
    if any(not equal_state(a[k],b[k]) for a,b in zip(r['timing']['histories'],previous['timing']['histories'],strict=True) for k in keys):
        raise ValueError('New objective changed actual main/reference input protocol')
    expected=sum_ranking([r['gate']['verification_ranking'],r['timing']['verification_ranking']])
    if (r['verification_ranking']!=expected or expected['updates']!=40 or expected['families_seen']!=80
            or expected['relational_choice_labels']!=160 or expected['physical_input_positions']!=40*8*256):
        raise ValueError('Actual separate CUDA ranking verification ledgers differ')
    return r


def estimate_training(measured):
    record=measured['timing'];rows=record['histories']
    if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 for r in rows):raise ValueError('Actual32 continuous timings required')
    step=statistics.median(r['seconds'] for r in rows[8:]);teachers=record['verification_teacher_tokens']/32
    updates=3068;warm=max(0.,sum(r['seconds'] for r in rows[:8])-8*step)
    save=(math.ceil(updates/250)+1)*record['terminal_save_seconds'];total=updates*step+warm+save
    evidence=budget_evidence.inspect();reserve=evidence['nontraining_reserve_seconds']
    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total,
        reference_input_tokens=updates*8*1024,nontraining_reserve_seconds=reserve,nontraining_evidence_sha256=sha256(budget_evidence.PATH)),(total+reserve)*1.3+50


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c,*_=inspect(PROBE_CONFIG);c=copy.deepcopy(c);r=probe_evidence();timing,estimate=estimate_training(r)
    if estimate+r['GPU_seconds']+c['prior_probe_GPU_seconds']>CEILING:raise ValueError('Measured science exceeds900s; retain evidence')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        verification_GPU_seconds=r['GPU_seconds']+c['prior_probe_GPU_seconds'],verification_teacher_tokens=r['verification_teacher_tokens'],
        verification_reference_non_EOS_teacher_probability_mass=r['verification_reference_non_EOS_teacher_probability_mass'],
        verification_reference_input_tokens=r['verification_reference_input_tokens'],verification_reference_soft_positions=r['verification_reference_soft_positions'],GPU_budget_seconds=CEILING-r['GPU_seconds']-c['prior_probe_GPU_seconds'],
        measured_timing=timing,estimated_GPU_seconds_with_margin=estimate,save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='measured100M_CE_parentKL_frozen',timing=timing,estimate=estimate)),flush=True)


def binding(c,path):
    return dict(config_sha256=sha256(path),arm=ARM,parent=c['parent'],short_manifest_sha256=c['pool']['manifest_sha256'],teacher_goals=GOALS,
        optimizer_policy='inherit',peak_lr=.00001,loss=c['loss'],study_kind=KIND,sampler_policy=c['sampler_policy'],outcome_weight=1,
        ranking_policy=c['ranking_policy'],ranking_inputs=c['ranking_inputs'],KL_policy=c['KL_policy'],reference_teacher=c['parent'],positive_manifest_sha256=c['positive_data']['manifest_sha256'],original_web=c['original_web'])


def trainer_for(parent,pool,positive,original,b,device='cuda',context=1024,batch=32):
    view=ranking_view(read_json(PROPOSAL)['ranking_inputs'])
    return ContextOutcomeRankingTrainer(parent,pool,original,positive,GOALS,b,view,device,context,batch)


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
        restart_command=f"scripts/run_context_outcome_ranking_comparison.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
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
                    actual_LR=[g['lr'] for g in initial.optimizer.param_groups]==[.00001,.00001],
                    frozen_teacher_weights=equal_state(cpu_state(initial.reference_teacher.state_dict()),cpu_state(parent['model'])),
                    frozen_teacher_eval_no_grad=not initial.reference_teacher.training and all(not p.requires_grad and p.grad is None for p in initial.reference_teacher.parameters()),
                    reference_Web_cursor=equal_state(initial.replay.stream.state_dict()['sampler'],historical_web_cursor(parent)))
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
                    terminal_save_seconds=saved_seconds,checkpoint=str(cp),checkpoint_sha256=sha256(cp),
                    reference_non_EOS_teacher_probability_mass=trainer.reference_non_EOS_teacher_mass,
                    reference_input_tokens=trainer.replay.physical_input_tokens,reference_soft_positions=trainer.replay.body_positions,verification_ranking=ranking_counts(trainer))
                result=dict(status='actual_three_loss_context_ranking_resume_timing_complete',passed=True,gate=gate,timing=timing,
                    config_sha256=sha256(path),verification_teacher_tokens=gate['verification_teacher_tokens']+timing['verification_teacher_tokens'],
                    GPU_optimizer_updates=40,scientific_teacher_tokens=0,weights_discarded_for_science=True,initial_parent_preservation=preservation,
                    verification_reference_non_EOS_teacher_probability_mass=gate['verification_reference_non_EOS_teacher_probability_mass']+timing['reference_non_EOS_teacher_probability_mass'],
                    verification_reference_input_tokens=gate['verification_reference_input_tokens']+timing['reference_input_tokens'],
                    verification_reference_soft_positions=gate['verification_reference_soft_positions']+timing['reference_soft_positions'],
                    verification_ranking=sum_ranking([gate['verification_ranking'],timing['verification_ranking']]))
                del trainer; gc.collect(); torch.cuda.empty_cache()
            else:
                progress=output/'progress-result.json'
                result=read_json(progress) if progress.exists() else dict(checkpoints=dict(control=control),evaluations=dict(control=control_ev))
                old_full=read_json(MECHANISM_RUN/'compare-result.json')
                mechanism_cached={k:old_full[k][MECHANISM_ARM] for k in ('checkpoints','evaluations','transfer','retention')}
                result.setdefault('mechanism_cached',mechanism_cached)
                if result['mechanism_cached']!=mechanism_cached:raise ValueError('Cached fullKL mechanism evidence differs')
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
                    result['checkpoints'][ARM].update(reference_non_EOS_teacher_probability_mass=trainer.reference_non_EOS_teacher_mass,reference_replay=trainer.replay.state_dict(),reference_teacher_weight_digest=trainer.teacher_digest,
                        reference_input_tokens=trainer.replay.physical_input_tokens,reference_soft_target_body_positions=trainer.replay.body_positions,
                        main_and_Web_reference_physical_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens,
                        combined_student_physical_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens+trainer.ranking.physical_input_positions,
                        combined_student_valid_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens+trainer.ranking.valid_input_tokens,
                        ranking_policy=c['ranking_policy'],ranking_input_binding=trainer.ranking.view.binding,ranking_sampler=trainer.ranking.state_dict(),ranking_exposure=ranking_counts(trainer),KL_policy=POLICY)
                    atomic_json(progress,result); del trainer; gc.collect(); torch.cuda.empty_cache()
                if ARM not in result['evaluations']:
                    evaluation.RUN=output/'evaluation'; dev=Shard(Path(base['dev_shards']),'dev'); tok=Tokenizer(ROOT/base['tokenizer'])
                    result['evaluations'][ARM]=evaluation.evaluate(ARM,result['checkpoints'][ARM],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-prior_seconds)
                    atomic_json(progress,result)
                reused=read_json(cached.RUN/'compare-result.json')
                result.setdefault('transfer',dict(control=reused['transfer']['source_order']))
                result.setdefault('retention',dict(control=reused['retention']['source_order']))
                if (result['transfer']['control']!=reused['transfer']['source_order']
                        or result['retention']['control']!=reused['retention']['source_order']):
                    raise ValueError('Cached same-weight control128 bridge/retention differs')
                checkpoint=dict(path=result['checkpoints'][ARM]['checkpoint'],sha256=result['checkpoints'][ARM]['checkpoint_sha256'])
                for suite,key in (('bridge','transfer'),('retention','retention')):
                    if ARM not in result[key]:
                        result[key][ARM]=transfer_scores(c,ARM,checkpoint,heartbeat,check,suite)
                        atomic_json(progress,result)
                result.update(status='web_KL_CE100M_and_cached_stagedCE100M_complete',
                    config_sha256=sha256(path),scientific_teacher_tokens=TOTAL,total_comparison_teachers=2*TOTAL,
                    reference_non_EOS_teacher_probability_mass=result['checkpoints'][ARM]['reference_non_EOS_teacher_probability_mass'],
                    previous_related_study_GPU_seconds=c['previous_related_study_GPU_seconds'],quality_screen_baseline=QUALITY_BASELINE,
                    mechanism_comparison_teacher_tokens=2*TOTAL,reference_input_tokens=result['checkpoints'][ARM]['reference_input_tokens'],
                    reference_soft_target_body_positions=result['checkpoints'][ARM]['reference_soft_target_body_positions'],
                    ranking_exposure=result['checkpoints'][ARM]['ranking_exposure'],new_original_corpus_tokens=0,
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
