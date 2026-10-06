"""Review projected100M against closed controls; no new GPU or relaxed gates."""
import argparse
import json
import math
from pathlib import Path
import sys

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from natural_context_contrast_projection import KIND,HEAD_SEED
from run_natural_context_contrast_projection import (CONFIG,RUN,CONTROL,matched_control_checks,finite_projected_state)
from phase6_performance import alive
from jmicro.phase5 import equal_state
import review_natural_context_contrast as prior
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_natural_context_semantic_clusters import validate_cached,require_same_inputs,summary,paired
from teacher_semantic_signal import dev_cases

POLICY=ROOT/'configs/phase6/natural_context_contrast_projection_review.json'
NOTES=ROOT/'reports/phase6/natural_context_contrast_projection_notes.json'
RAW=RUN/'evaluation/projection/evaluation/generation.json'
HELPERS=('scripts/review_natural_context_contrast_projection.py',
    'scripts/review_natural_context_contrast.py','scripts/review_parameter_displacement_anchor.py',
    'scripts/review_matched_story_study.py','scripts/run_eos_complete_100m.py',
    'scripts/review_eos_5b_finish.py','scripts/review_textbook_quantity_comparison.py',
    'scripts/review_natural_context_semantic_clusters.py','scripts/review_teacher_semantic_signal.py',
    'scripts/teacher_semantic_signal.py','scripts/review_chat_base_retention.py')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def prepare():
    if POLICY.exists():raise ValueError('Preserve frozen projection review policy')
    old,policy=prior.load_policy();c=read_json(CONFIG)
    review=ROOT/'reports/phase6/natural_context_contrast_comparison_review.json'
    reviewed=read_json(review)
    if not reviewed['all160_individually_read'] or any(reviewed['eligible_for_final_Base_validation'].values()):
        raise ValueError('Preserve actual closed, individually reviewed controls')
    if any(c[k]!=old[k] for k in ('parent','source_binding','batch','seed','goals','suite_sha256','evaluation')):
        raise ValueError('Cached controls must share actual scientific parent/source/evaluation')
    references=dict(previous_policy=ref(prior.POLICY),previous_review=ref(review),
        previous_result=ref(CONTROL/'result.json'),previous_config=ref(prior.CONFIG))
    for arm in prior.ARMS:
        references['notes_'+arm]=ref(prior.notes_path(arm))
        references['generation_'+arm]=ref(prior.raw_path(arm))
        references['semantics_'+arm]=ref(CONTROL/f'evaluation/{arm}/evaluation/semantics.json')
    atomic_json(POLICY,dict(created_at=now(),scientific_config_sha256=sha256(CONFIG),references=references,
        helper_sha256={p:sha256(ROOT/p) for p in HELPERS},
        original_references=policy['references'],strong_summary=policy['strong_summary'],
        criteria='Same strong relative, absolute Base and historical Web gates. Projection also qualifies against both cached CE and direct-feature controls. All80 new raw-bound observations; reuse old160. Independent learned seed/full DEV/protected final TEST/adoption remain required.',
        scientific_results_read=False,new_GPU_seconds=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False))
    print(json.dumps(dict(status='projection_review_policy_frozen',scientific_results_read=False,new_GPU_seconds=0)))


def load_policy():
    c,p=read_json(CONFIG),read_json(POLICY)
    if p['scientific_config_sha256']!=sha256(CONFIG):raise ValueError('Scientific projection config changed')
    for name,digest in {**c['source_sha256'],**p['helper_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen review/scientific source changed: '+name)
    for reference in (*p['references'].values(),*p['original_references'].values()):prior.checked_reference(reference)
    prior.load_policy()
    return c,p


def audit_terminal(job,result,c,digest,live):
    if live:raise ValueError('Actual scientific process must exit before final projection review')
    expected={'CE','contrast'}
    common=result.get('common_CE_checks',{})
    if (job['status']!='complete' or result['status']!='complete'
            or job['config_sha256']!=digest or result['config_sha256']!=digest
            or result['actual_identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not 0<result['GPU_occupancy_seconds']==job['GPU_occupancy_seconds']<=c['GPU_budget_seconds']
            or result['scientific_CE_teacher_tokens']!=c['CE_tokens_per_arm']
            or result['reused_control_CE_teachers']!=200000000 or result['reused_control_GPU_seconds']!=0
            or set(result['results'])!={'projection'} or set(common)!=expected
            or any(set(checks)!=set(matched_control_checks(result['results']['projection']['training'],
                    result['results']['projection']['training'])) or any(v is not True for v in checks.values()) for checks in common.values())
            or any(result[k] is not False for k in ('Base_complete','Chat_started','quantization_started'))):
        raise ValueError('Actual bounded exited Base-only projected100M terminal required')


HISTORY_KEYS=('update','supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
    'auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens','original_body_bytes','token_digest','auxiliary_digest')


def committed_history(paths,terminal):
    """Read small training logs once; replace rolled-back updates by later attempts."""
    rows={};observed=0;torn_tails=[]
    # Durable names include native start_ticks; creation order survives PID reuse.
    paths=sorted(paths,key=lambda p:int(p.stem.rsplit('-',1)[1]))
    for path in paths:
        previous=0
        with path.open() as stream:
            for line in stream:
                try:row=json.loads(line)
                except json.JSONDecodeError:
                    if not line.endswith('\n') and not stream.read(1):
                        torn_tails.append(dict(path=str(path),uncommitted_tail_bytes=len(line.encode())))
                        break
                    raise ValueError('Malformed newline-terminated actual history row')
                observed+=1
                update=row['update']
                if type(update) is not int or update<=previous:raise ValueError('Each actual attempt must have increasing completed updates')
                previous=update
                required=('CE_loss','contrast_loss','combined_loss','auxiliary_gradient_norm','train_only_head_gradient_norm','gradient_norm','seconds','data_wait_seconds','lr')
                if (any(not math.isfinite(row[k]) for k in required) or row['lr']!=1e-5
                        or not math.isclose(row['combined_loss'],row['CE_loss']+.1*row['contrast_loss'],rel_tol=1e-6,abs_tol=1e-6)
                        or row['CE_targets_this_update']<=0 or row['auxiliary_pairs_this_update']<0):
                    raise ValueError('Actual finite original CE/projected objective history required')
                used=row['auxiliary_pairs_this_update']
                if used and (used<2 or row['auxiliary_gradient_norm']<=0 or row['train_only_head_gradient_norm']<=0):
                    raise ValueError('Actual paired auxiliary update requires shared/head gradients')
                if not used and any(row[k]!=0 for k in ('contrast_loss','auxiliary_gradient_norm','train_only_head_gradient_norm','auxiliary_inputs_this_update')):
                    raise ValueError('Pair-ineligible original windows must retain only CE')
                if update<=terminal['update']:
                    rows[update]={**{k:row[k] for k in HISTORY_KEYS},'head_updated':bool(used),
                        'CE_targets_this_update':row['CE_targets_this_update'],
                        'auxiliary_inputs_this_update':row['auxiliary_inputs_this_update'],
                        'physical_inputs_this_update':row['physical_inputs_this_update'],'auxiliary_pairs_this_update':used}
    if set(rows)!=set(range(1,terminal['update']+1)) or any(not equal_state(rows[terminal['update']][k],terminal[k]) for k in HISTORY_KEYS):
        raise ValueError('Complete committed history and terminal counters/digests required')
    previous=dict(supervised_tokens=0,auxiliary_input_tokens=0,physical_input_tokens=0,auxiliary_pairs=0)
    for update in range(1,terminal['update']+1):
        row=rows[update]
        for counter,increment in (('supervised_tokens','CE_targets_this_update'),('auxiliary_input_tokens','auxiliary_inputs_this_update'),
                                  ('physical_input_tokens','physical_inputs_this_update'),('auxiliary_pairs','auxiliary_pairs_this_update')):
            if row[counter]-previous[counter]!=row[increment]:raise ValueError('Completed update teacher/auxiliary/physical accounting differs')
            previous[counter]=row[counter]
        if sum(row['source_teachers'].values())!=row['supervised_tokens']:raise ValueError('Per-source teacher accounting differs')
    return dict(committed_updates=len(rows),head_updates=sum(r['head_updated'] for r in rows.values()),
        observed_completed_attempt_updates=observed,rolled_back_or_replayed_log_rows=observed-len(rows),
        uncommitted_torn_tails=torn_tails,raw_metrics={str(p):sha256(p) for p in paths})


def audit_checkpoint(state,record,c,digest,history):
    spec,sampler,counters=state['spec'],state['sampler'],state['counters']
    binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=digest,
        weights_role='scientific_projection',sources=c['source_sha256'])
    geometry=dict(width=256,output_width=128,activation='ReLU',bias=False,head_seed=HEAD_SEED,train_only=True,separate_state=True)
    if (state['kind']!=KIND or spec['kind']!=KIND or state['binding']!=binding or record['binding']!=binding
            or record['status']!='complete' or counters!=record['counters'] or not equal_state(sampler,record['sampler'])
            or record['scientific_CE_teacher_tokens']!=c['CE_tokens_per_arm'] or counters['supervised_tokens']!=c['CE_tokens_per_arm']
            or counters['source_teachers']!=c['goals'] or sampler['consumed']!=c['goals'] or sampler['goals']!=c['goals']
            or sampler['binding']!=c['source_binding'] or spec['goals']!=c['goals']
            or state['lineage']['parent']!=c['parent'] or state['lineage']['weights_role']!='scientific_projection'
            or state['lineage']['parent_supervised_tokens']!=record['parent_CE_teacher_tokens']
            or not state['lineage']['train_only_head_discarded_at_native_evaluation']
            or spec['batch']!=c['batch'] or spec['seed']!=sampler['seed'] or spec['seed']!=c['seed']
            or spec['contrast'] is not True or spec['temperature']!=.1 or spec['coefficient']!=.1
            or spec['lr']!=1e-5 or spec['weight_decay']!=.1 or spec['scheduler']!='constant'
            or spec['optimizer_policy']!='fresh_equal_AdamW_both_arms' or spec['dtype']!='bf16' or spec['backend']!='flash'
            or spec['projection']!=geometry or spec['native_parameters']!=10001152 or spec['train_only_parameters']!=98304
            or spec['clipping_policy']!='joint_native_and_train_only_head_norm1'
            or not all(k in state for k in ('model','projector','optimizer','scheduler','RNG','sampler'))
            or counters['update']<=0 or history['committed_updates']!=counters['update']
            or not 0<history['head_updates']<=counters['update'] or not finite_projected_state(state)
            or state['scheduler']['last_epoch']!=counters['update'] or counters['auxiliary_pairs']<=0
            or counters['auxiliary_input_tokens']<=0 or counters['physical_input_tokens']<counters['CE_input_tokens']+counters['auxiliary_input_tokens']):
        raise ValueError('Completed projection native/head/full-state accounting differs')
    head=state['projector']
    if (set(head)!={'0.weight','2.weight'} or tuple(head['0.weight'].shape)!=(256,256)
            or tuple(head['2.weight'].shape)!=(128,256) or any('projector' in k for k in state['model'])
            or not torch.equal(state['model']['model.embed_tokens.weight'],state['model']['lm_head.weight'])):
        raise ValueError('Separate fixed head and native tied weights required')
    rng=state['RNG']
    if (set(rng)!={'python','numpy','torch','cuda'} or len(rng['cuda'])!=1
            or any(not isinstance(t,torch.Tensor) or t.dtype!=torch.uint8 or t.ndim!=1 for t in [rng['torch'],*rng['cuda']])):
        raise ValueError('Saved CPU and actual single-CUDA RNG states required')
    with torch.random.fork_rng(devices=[]):model=JMicroModel(state['model_config'])
    model.load_state_dict(state['model'],strict=True)
    native=list(model.parameters());head_shapes=[(256,256),(128,256)]
    if sum(p.numel() for p in native)!=10001152:raise ValueError('Native10M architecture required')
    groups=state['optimizer']['param_groups']
    if len(groups)!=1 or groups[0]['lr']!=1e-5 or groups[0]['weight_decay']!=.1:
        raise ValueError('One joint fresh fixed AdamW group required')
    ids=groups[0]['params'];moments=state['optimizer']['state'];shapes=[tuple(p.shape) for p in native]+head_shapes
    if len(ids)!=len(shapes) or len(set(ids))!=len(ids) or set(moments)!=set(ids):raise ValueError('All unique native/head optimizer states required')
    for i,(key,shape) in enumerate(zip(ids,shapes,strict=True)):
        expected=counters['update'] if i<len(native) else history['head_updates']
        row=moments[key]
        if (float(row['step'])!=expected or tuple(row['exp_avg'].shape)!=shape or tuple(row['exp_avg_sq'].shape)!=shape):
            raise ValueError('Native Adam steps and eligible-pair head Adam steps must match actual committed history')
    del model
    return dict(completed_updates=counters['update'],head_optimizer_updates=history['head_updates'],
        CE_teacher_tokens=counters['supervised_tokens'],native_parameters=10001152,train_only_parameters=98304,
        training_parameters=10099456,native_vocabulary_uses_head=False,
        **{k:counters[k] for k in ('source_teachers','source_EOS','CE_input_tokens','auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens','original_body_bytes')},
        source_draws=sampler['draws'],source_windows=sampler['windows_emitted'],additional_unique_supply_claimed=False)


def template():
    load_policy()
    if NOTES.exists():raise ValueError('Preserve existing individual notes')
    trained=read_json(RUN/'projection/train-result.json');ev=read_json(RUN/'evaluation/projection/evaluation/result.json')
    if (trained['status']!='complete' or ev['binding']!=trained['binding'] or ev['checkpoint_sha256']!=trained['checkpoint_sha256']
            or read_json(RAW)!=ev['generation'] or len(ev['generation']['outputs'])!=80):
        raise ValueError('All80 checkpoint-bound completed native outputs required')
    atomic_json(NOTES,dict(reviewer='Codex nonblind; each new continuation requires individual reading',
        independent_human_blind=False,generation_sha256=sha256(RAW),
        notes=[[r['id'],None,None,None,None,''] for r in ev['generation']['outputs']]))
    print(json.dumps(dict(status='new80_unscored',path=str(NOTES))))


def record(observations):
    c,_=load_policy();observations=observations.resolve()
    if not observations.is_relative_to(ROOT/'reports/phase6'):raise ValueError('Repository phase6 observations required')
    rows=read_json(RAW)['outputs'];validate_rows(rows,Tokenizer(ROOT/c['tokenizer']))
    notes=[]
    for line in observations.read_text(encoding='utf-8').splitlines():
        fields=line.split('\t')
        if len(fields)!=6:raise ValueError('One six-field observation per continuation required')
        notes.append([fields[0],*(int(v) for v in fields[1:5]),fields[5]])
    document=dict(created_at=now(),reviewer='Codex nonblind; all80 individually read',
        independent_human_blind=False,generation_sha256=sha256(RAW),notes=notes,
        observations=ref(observations),recorder_sha256=sha256(Path(__file__)))
    validate_notes(rows,document,sha256(RAW))
    if NOTES.exists():
        old=read_json(NOTES)
        if old['generation_sha256']!=sha256(RAW) or len(old['notes'])!=80 or any(n[1:5]!=[None]*4 or n[5] for n in old['notes']):
            raise ValueError('Preserve previously scored or differently bound notes')
    candidate=NOTES.with_suffix('.candidate.json')
    if candidate.exists():raise ValueError('Inspect existing interrupted candidate notes')
    atomic_json(candidate,document)
    try:
        trained=read_json(RUN/'projection/train-result.json');ev=read_json(RUN/'evaluation/projection/evaluation/result.json')
        detail,_=content('projection',ev,trained,c,RAW,candidate)
        atomic_json(NOTES,document)
    finally:candidate.unlink()
    detail.update(scope='new80_content_only_final_comparison_pending',individually_read=80,
        independent_human_blind=False,Base_complete=False,scientific_CE_teacher_tokens=trained['scientific_CE_teacher_tokens'])
    atomic_json(ROOT/'reports/phase6/natural_context_contrast_projection_content_review.json',detail)
    print(json.dumps(detail,ensure_ascii=False))


def review():
    c,p=load_policy();job=read_json(RUN/'job.json')
    if alive(job) or job['status']!='complete':raise ValueError('Scientific process must finish and exit before final review')
    result=read_json(RUN/'result.json');digest=sha256(CONFIG)
    audit_terminal(job,result,c,digest,False)
    probe=read_json(prior.checked_reference(c['probe_result']))
    if not probe['passed'] or not all(probe['initial_checks'].values()) or not all(probe['resume_checks'].values()):
        raise ValueError('Actual projected native/head CUDA initialization/full-state resume evidence required')
    record=result['results']['projection']['training'];ev=result['results']['projection']['evaluation']
    if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:raise ValueError('Terminal native/head checkpoint changed')
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    history=committed_history(list((RUN/'projection').glob('metrics-*.jsonl')),state['counters'])
    account=audit_checkpoint(state,record,c,digest,history)
    controls=read_json(prior.checked_reference(p['references']['previous_result']))['results']
    common={a:matched_control_checks(record,controls[a]['training']) for a in prior.ARMS}
    if not all(all(v is True for v in checks.values()) for checks in common.values()):raise ValueError('Same full CE accounting/source sampler required against both cached controls')
    del state
    summaries,scores={},{}
    summaries['projection'],scores['projection']=content('projection',ev,record,c,RAW,NOTES)
    previous=read_json(prior.checked_reference(p['references']['previous_review']))
    for arm in prior.ARMS:
        summaries[arm],scores[arm]=content(arm,controls[arm]['evaluation'],controls[arm]['training'],c,
            Path(p['references']['generation_'+arm]['path']),Path(p['references']['notes_'+arm]['path']))
        if summaries[arm]!=previous['summaries'][arm]:raise ValueError('Existing individually reviewed control content changed')
    strong_result=read_json(Path(p['original_references']['strong_result']['path']))
    strong=strong_result['evaluations']['source_order']
    strong_raw=Path(p['original_references']['strong_result']['path']).parent/'evaluation/source_order/evaluation/generation.json'
    base=read_json(Path(p['original_references']['original_config']['path']))
    summaries['strong_staged'],scores['strong_staged']=content('strong_staged',strong,strong_result['checkpoints']['source_order'],base,
        strong_raw,Path(p['original_references']['strong_notes']['path']))
    if summaries['strong_staged']!=p['strong_summary']:raise ValueError('Original strong content changed')
    evaluations={a:controls[a]['evaluation'] for a in prior.ARMS}|{'strong_staged':strong}
    for name,control in evaluations.items():
        if ([(r['id'],r['prefix']) for r in ev['generation']['outputs']]!=[(r['id'],r['prefix']) for r in control['generation']['outputs']]
                or [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in ev['body']['rows']]!=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in control['body']['rows']]):
            raise ValueError('Same complete fixed80 prefixes and common256 body bytes required: '+name)
    quality={a:quality_gates(control,ev,scores[a],scores['projection'],'content') for a,control in evaluations.items()}
    s=summaries['projection']
    absolute=dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,
        appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,
        repetition_at_most18=s['rates']['repetition']<=18,
        no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(read_json(Path(p['original_references']['historical_Web']['path'])),ev)
    # Supplement repeated-DEV accuracy with exact input identity and paired CIs.
    source=ROOT/c['evaluation']['semantic_suite']
    if sha256(source)!=c['evaluation']['semantic_sha256']:raise ValueError('Same Japanese semantic suite required')
    original_rows,_=dev_cases(source)
    native_semantics=validate_cached(read_json(RUN/'evaluation/projection/evaluation/semantics.json'),record)
    require_same_inputs(original_rows,native_semantics)
    semantic_report=dict(projection=summary(native_semantics),paired={})
    from review_chat_base_retention import paired_bpb
    bpb={}
    for arm in prior.ARMS:
        cached=validate_cached(read_json(Path(p['references']['semantics_'+arm]['path'])),controls[arm]['training'])
        require_same_inputs(original_rows,cached)
        semantic_report['paired'][arm]=paired(cached,native_semantics)
        bpb[arm]=paired_bpb(controls[arm]['evaluation']['body'],ev['body'])
        bpb[arm]['direction']='projection minus completed '+arm+'; positive means worse'
    eligible=all(q['passed'] for q in quality.values()) and all(absolute.values()) and all(original.values())
    report=dict(status='new80_and_reused160_projection_comparison_reviewed',created_at=now(),config_sha256=digest,
        review_policy_sha256=sha256(POLICY),result_sha256=sha256(RUN/'result.json'),summaries=summaries,
        strong_and_matched_quality=quality,absolute_dev_screen=absolute,historical_Web=original,
        paired_common_byte_BPB=bpb,exact_content_semantics=semantic_report,
        eligible_for_final_Base_validation=eligible,accounting=account,history=history,common_CE_checks=common,
        new_scientific_CE_teacher_tokens=100000000,reused_control_CE_teachers=200000000,reused_control_GPU_seconds=0,
        probe_verification_updates=probe['verification_updates'],probe_verification_CE_teachers=probe['verification_CE_teacher_tokens'],
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],new80_individually_read=True,reused160_individually_read=True,
        independent_human_blind=False,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
        final_seed_full_dev_test_adoption_pending=True,
        limitations='Single learned seed, repeated nonblind DEV, head parameters/auxiliary compute differ. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored.',
        next_action='Only a qualified fixed projection candidate advances to independent learned seed/full DEV/protected final TEST/adoption. Otherwise close this fixed mechanism without head/seed/LR/coefficient/source/checkpoint/epoch rescue. Notify/stop at completed Base; no Chat or quantization.')
    if (RUN/'review.json').exists():raise ValueError('Preserve completed projection review')
    atomic_json(RUN/'review.json',report)
    atomic_json(ROOT/'reports/phase6/natural_context_contrast_projection_comparison_review.json',report)
    print(json.dumps(dict(summary=s,eligible=eligible),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--template',action='store_true')
    group.add_argument('--record',type=Path);args=parser.parse_args()
    if args.prepare:prepare()
    elif args.template:template()
    elif args.record:record(args.record)
    else:review()
