"""Review original100M plus next-two auxiliary against cached CE; unchanged Base gates."""
import argparse
import json
import math
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from base_next_two_token_trainer import KIND,COEFFICIENT,NextTwoHead,AUXILIARY_SEED
from run_base_next_two_token import (CONFIG,RUN,CONTROL,matched_control_checks,finite_next_two_state)
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

ARMS=('CE',)

POLICY=ROOT/'configs/phase6/base_next_two_token_review.json'
NOTES=ROOT/'reports/phase6/base_next_two_token_notes.json'
RAW=RUN/'evaluation/next_two/evaluation/generation.json'
HELPERS=('scripts/review_base_next_two_token.py',
    'scripts/review_natural_context_contrast.py','scripts/review_parameter_displacement_anchor.py',
    'scripts/review_matched_story_study.py','scripts/run_eos_complete_100m.py',
    'scripts/review_eos_5b_finish.py','scripts/review_textbook_quantity_comparison.py',
    'scripts/review_natural_context_semantic_clusters.py','scripts/review_teacher_semantic_signal.py',
    'scripts/teacher_semantic_signal.py','scripts/review_chat_base_retention.py')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def prepare():
    if POLICY.exists():raise ValueError('Preserve frozen next_two review policy')
    old,policy=prior.load_policy();c=read_json(CONFIG)
    tests=ROOT/'reports/phase6/base_next_two_token_review_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites)<12 or any(
            int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Successful CPU reviewer protocol evidence required')
    review=ROOT/'reports/phase6/natural_context_contrast_comparison_review.json'
    reviewed=read_json(review)
    if not reviewed['all160_individually_read'] or any(reviewed['eligible_for_final_Base_validation'].values()):
        raise ValueError('Preserve actual closed, individually reviewed controls')
    if any(c[k]!=old[k] for k in ('parent','source_binding','batch','seed','goals','suite_sha256','evaluation')):
        raise ValueError('Cached controls must share actual scientific parent/source/evaluation')
    references=dict(previous_policy=ref(prior.POLICY),previous_review=ref(review),
        previous_result=ref(CONTROL/'result.json'),previous_config=ref(prior.CONFIG),
        CPU_review_tests=ref(tests),CPU_review_test_source=ref(ROOT/'tests/test_base_next_two_token_review.py'))
    for arm in ARMS:
        references['notes_'+arm]=ref(prior.notes_path(arm))
        references['generation_'+arm]=ref(prior.raw_path(arm))
        references['semantics_'+arm]=ref(CONTROL/f'evaluation/{arm}/evaluation/semantics.json')
    atomic_json(POLICY,dict(created_at=now(),scientific_config_sha256=sha256(CONFIG),references=references,
        helper_sha256={p:sha256(ROOT/p) for p in HELPERS},
        original_references=policy['references'],strong_summary=policy['strong_summary'],
        criteria='Same strong relative, absolute Base and historical Web gates. Next-two objective qualifies against cached original CE. All80 new raw-bound observations; reuse old80 CE. Independent learned seed/full DEV/protected final TEST/adoption remain required.',
        scientific_results_read=False,new_GPU_seconds=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False))
    print(json.dumps(dict(status='next_two_review_policy_frozen',scientific_results_read=False,new_GPU_seconds=0)))


def load_policy():
    c,p=read_json(CONFIG),read_json(POLICY)
    if p['scientific_config_sha256']!=sha256(CONFIG):raise ValueError('Scientific next_two config changed')
    for name,digest in {**c['source_sha256'],**p['helper_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen review/scientific source changed: '+name)
    for reference in (*p['references'].values(),*p['original_references'].values()):prior.checked_reference(reference)
    prior.load_policy()
    return c,p


def audit_terminal(job,result,c,digest,live):
    if live:raise ValueError('Actual scientific process must exit before final next_two review')
    expected={'CE'}
    common=result.get('common_CE_checks',{})
    if (job['status']!='complete' or result['status']!='complete'
            or job['config_sha256']!=digest or result['config_sha256']!=digest
            or result['actual_identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not 0<result['GPU_occupancy_seconds']==job['GPU_occupancy_seconds']<=c['GPU_budget_seconds']
            or result['scientific_CE_teacher_tokens']!=c['CE_tokens_per_arm']
            or result['reused_control_CE_teachers']!=100000000 or result['reused_control_GPU_seconds']!=0
            or set(result['results'])!={'next_two'} or set(common)!=expected
            or any(set(checks)!=set(matched_control_checks(result['results']['next_two']['training'],
                    result['results']['next_two']['training'])) or any(v is not True for v in checks.values()) for checks in common.values())
            or any(result[k] is not False for k in ('Base_complete','Chat_started','quantization_started'))):
        raise ValueError('Actual bounded exited Base-only next_two100M terminal required')


HISTORY_KEYS=('update','supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
    'auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens','original_body_bytes','token_digest','auxiliary_digest',
    'next_two_teacher_positions','next_two_EOS_targets','next_two_body_bytes','next_two_target_mass',
    'auxiliary_physical_hidden_positions','source_next_two_teachers','source_next_two_EOS')


def committed_history(paths,terminal):
    rows={};observed=0;torn=[]
    for path in sorted(paths,key=lambda p:int(p.stem.rsplit('-',1)[1])):
        previous_update=0
        with path.open() as stream:
            for line in stream:
                try:row=json.loads(line)
                except json.JSONDecodeError:
                    if not line.endswith('\n') and not stream.read(1):
                        torn.append(dict(path=str(path),uncommitted_tail_bytes=len(line.encode())));break
                    raise ValueError('Malformed newline-terminated actual history')
                observed+=1;update=row['update']
                if type(update) is not int or update<=previous_update:raise ValueError('Increasing completed update history required')
                previous_update=update
                numeric=('CE_loss','next_two_CE_loss','combined_loss','next_two_head_gradient_norm','gradient_norm','seconds','data_wait_seconds','lr')
                n2=row['next_two_teacher_positions']
                if (any(not math.isfinite(row[k]) for k in numeric) or row['lr']!=1e-5
                        or row['next_two_coefficient']!=COEFFICIENT
                        or not math.isclose(row['combined_loss'],row['CE_loss']+COEFFICIENT*row['next_two_CE_loss'],rel_tol=1e-6,abs_tol=1e-6)
                        or n2!=sum(row['source_next_two_teachers'].values()) or not 0<=n2<=row['supervised_tokens']
                        or row['next_two_target_mass']!=COEFFICIENT*n2
                        or row['next_two_EOS_targets']!=sum(row['source_next_two_EOS'].values())
                        or row['CE_targets_this_update']<=0 or not 0<=row['next_two_targets_this_update']<=row['CE_targets_this_update']
                        or row['gradient_norm']<=0 or row['seconds']<=0 or row['data_wait_seconds']<0
                        or (row['next_two_targets_this_update']>0 and row['next_two_head_gradient_norm']<=0)
                        or row['auxiliary_input_tokens'] or row['auxiliary_pairs'] or row['auxiliary_inputs_this_update']
                        or row['auxiliary_digest']!='0'*64):
                    raise ValueError('Finite original/next-two loss and separate teacher accounting required')
                if update<=terminal['update']:rows[update]={**{k:row[k] for k in HISTORY_KEYS},
                    'CE_targets_this_update':row['CE_targets_this_update'],'next_two_targets_this_update':row['next_two_targets_this_update'],
                    'physical_inputs_this_update':row['physical_inputs_this_update']}
    if set(rows)!=set(range(1,terminal['update']+1)) or any(not equal_state(rows[terminal['update']][k],terminal[k]) for k in HISTORY_KEYS):
        raise ValueError('Complete committed history and terminal original/auxiliary counters required')
    previous=dict(supervised_tokens=0,next_two_teacher_positions=0,physical_input_tokens=0)
    for update in range(1,terminal['update']+1):
        row=rows[update]
        for counter,increment in (('supervised_tokens','CE_targets_this_update'),('next_two_teacher_positions','next_two_targets_this_update'),('physical_input_tokens','physical_inputs_this_update')):
            if row[counter]-previous[counter]!=row[increment]:raise ValueError('Committed original/auxiliary/physical increments differ')
            previous[counter]=row[counter]
        if sum(row['source_teachers'].values())!=row['supervised_tokens'] or row['physical_input_tokens']<row['CE_input_tokens']:
            raise ValueError('Original source/physical denominator differs')
    return dict(committed_updates=len(rows),optimizer_updates=len(rows),observed_completed_attempt_updates=observed,
        auxiliary_optimizer_updates=sum(row['next_two_targets_this_update']>0 for row in rows.values()),
        rolled_back_or_replayed_log_rows=observed-len(rows),uncommitted_torn_tails=torn,raw_metrics={str(p):sha256(p) for p in paths})


def audit_checkpoint(state,record,c,digest,history):
    spec,sampler,counters=state['spec'],state['sampler'],state['counters']
    binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=digest,
        weights_role='scientific_next_two',sources=c['source_sha256'])
    if (state['kind']!=KIND or spec['kind']!=KIND or state['binding']!=binding or record['binding']!=binding
            or record['status']!='complete' or counters!=record['counters'] or not equal_state(sampler,record['sampler'])
            or record['scientific_CE_teacher_tokens']!=c['CE_tokens_per_arm'] or counters['supervised_tokens']!=c['CE_tokens_per_arm']
            or counters['source_teachers']!=c['goals'] or sampler['consumed']!=c['goals'] or sampler['goals']!=c['goals']
            or sampler['binding']!=c['source_binding'] or spec['goals']!=c['goals']
            or state['lineage']['parent']!=c['parent'] or state['lineage']['weights_role']!='scientific_next_two'
            or state['lineage']['parent_supervised_tokens']!=record['parent_CE_teacher_tokens']
            or spec['batch']!=c['batch'] or spec['seed']!=sampler['seed'] or spec['seed']!=c['seed']
            or spec['contrast'] is not False or spec['lr']!=1e-5 or spec['weight_decay']!=.1 or spec['scheduler']!='constant'
            or spec['optimizer_policy']!='fresh_equal_AdamW_both_arms' or spec['dtype']!='bf16' or spec['backend']!='flash'
            or spec['next_two_coefficient']!=COEFFICIENT or spec['auxiliary_seed']!=AUXILIARY_SEED
            or spec['native_parameters']!=10001152 or spec['train_only_parameters']!=688896 or spec['total_training_parameters']!=10690048
            or spec['auxiliary_policy']!='one_native_contextual_block_and_final_RMS_on_original_hidden_shared_native_unembedding'
            or spec['auxiliary_mask']!='current_original_target_and_next_original_target_both_unmasked_same_window'
            or spec['inference_policy']!='original_native_model_only_no_auxiliary_head_no_decode_changes'
            or set(state)!=set(('kind','spec','binding','lineage','model_config','model','optimizer','scheduler','RNG','sampler','counters','auxiliary_model'))
            or counters['update']<=0 or history['committed_updates']!=counters['update'] or history['optimizer_updates']!=counters['update']
            or not finite_next_two_state(state) or state['scheduler']['last_epoch']!=counters['update']
            or counters['physical_input_tokens']<counters['CE_input_tokens']):
        raise ValueError('Completed native/auxiliary full-state and objective accounting differs')
    if (not torch.equal(state['model']['model.embed_tokens.weight'],state['model']['lm_head.weight'])
            or state['model_config']['qk_norm_type']!='none' or any('future_head' in k for k in state['model'])):
        raise ValueError('Unchanged native tied NoNorm inference parameters required')
    rng=state['RNG']
    if (set(rng)!={'python','numpy','torch','cuda'} or len(rng['cuda'])!=1
            or any(not isinstance(t,torch.Tensor) or t.dtype!=torch.uint8 or t.ndim!=1 for t in [rng['torch'],*rng['cuda']])):
        raise ValueError('Saved CPU and actual single-CUDA RNG required')
    with torch.random.fork_rng(devices=[]):
        model=JMicroModel(state['model_config']);auxiliary=NextTwoHead(state['model_config'])
    model.load_state_dict(state['model'],strict=True);auxiliary.load_state_dict(state['auxiliary_model'],strict=True)
    native=list(model.parameters());extra=list(auxiliary.parameters())
    if sum(p.numel() for p in native)!=10001152 or sum(p.numel() for p in extra)!=688896:raise ValueError('Actual native and train-only architecture counts required')
    groups=state['optimizer']['param_groups']
    if len(groups)!=1 or groups[0]['lr']!=1e-5 or groups[0]['weight_decay']!=.1:raise ValueError('One fresh native-plus-auxiliary AdamW group required')
    ids=groups[0]['params'];moments=state['optimizer']['state'];shapes=[tuple(p.shape) for p in [*native,*extra]]
    if len(ids)!=len(shapes) or len(set(ids))!=len(ids) or set(moments)!=set(ids):raise ValueError('All unique native and auxiliary optimizer moments required')
    for index,(key,shape) in enumerate(zip(ids,shapes,strict=True)):
        row=moments[key]
        expected_steps=counters['update'] if index<len(native) else history['auxiliary_optimizer_updates']
        if float(row['step'])!=expected_steps or tuple(row['exp_avg'].shape)!=shape or tuple(row['exp_avg_sq'].shape)!=shape:
            raise ValueError('Every native/auxiliary Adam step must match committed history')
    return dict(completed_updates=counters['update'],optimizer_updates=history['optimizer_updates'],
        auxiliary_optimizer_updates=history['auxiliary_optimizer_updates'],
        CE_teacher_tokens=counters['supervised_tokens'],native_parameters=10001152,train_only_parameters=688896,
        training_parameters=10690048,next_two_coefficient=COEFFICIENT,native_inference_changed=False,
        **{k:counters[k] for k in HISTORY_KEYS if k not in ('update','token_digest','auxiliary_digest')},
        source_draws=sampler['draws'],source_windows=sampler['windows_emitted'],additional_unique_supply_claimed=False)


def template():
    load_policy()
    if NOTES.exists():raise ValueError('Preserve existing individual notes')
    trained=read_json(RUN/'next_two/train-result.json');ev=read_json(RUN/'evaluation/next_two/evaluation/result.json')
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
        trained=read_json(RUN/'next_two/train-result.json');ev=read_json(RUN/'evaluation/next_two/evaluation/result.json')
        detail,_=content('next_two',ev,trained,c,RAW,candidate)
        atomic_json(NOTES,document)
    finally:candidate.unlink()
    detail.update(scope='new80_content_only_final_comparison_pending',individually_read=80,
        independent_human_blind=False,Base_complete=False,scientific_CE_teacher_tokens=trained['scientific_CE_teacher_tokens'])
    atomic_json(ROOT/'reports/phase6/base_next_two_token_content_review.json',detail)
    print(json.dumps(detail,ensure_ascii=False))


def review():
    c,p=load_policy();job=read_json(RUN/'job.json')
    if alive(job) or job['status']!='complete':raise ValueError('Scientific process must finish and exit before final review')
    result=read_json(RUN/'result.json');digest=sha256(CONFIG)
    audit_terminal(job,result,c,digest,False)
    probe=read_json(prior.checked_reference(c['probe_result']))
    if not probe['passed'] or not all(probe['initial_checks'].values()) or not all(probe['all_resume_and_source_checks'].values()):
        raise ValueError('Actual native/next_two CUDA initialization/full-state resume evidence required')
    record=result['results']['next_two']['training'];ev=result['results']['next_two']['evaluation']
    if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:raise ValueError('Terminal native checkpoint changed')
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    history=committed_history(list((RUN/'next_two').glob('metrics-*.jsonl')),state['counters'])
    account=audit_checkpoint(state,record,c,digest,history)
    controls=read_json(prior.checked_reference(p['references']['previous_result']))['results']
    common={a:matched_control_checks(record,controls[a]['training']) for a in ARMS}
    if not all(all(v is True for v in checks.values()) for checks in common.values()):raise ValueError('Same full CE accounting/source sampler required against cached ordinary CE')
    del state
    summaries,scores={},{}
    summaries['next_two'],scores['next_two']=content('next_two',ev,record,c,RAW,NOTES)
    previous=read_json(prior.checked_reference(p['references']['previous_review']))
    for arm in ARMS:
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
    evaluations={a:controls[a]['evaluation'] for a in ARMS}|{'strong_staged':strong}
    for name,control in evaluations.items():
        if ([(r['id'],r['prefix']) for r in ev['generation']['outputs']]!=[(r['id'],r['prefix']) for r in control['generation']['outputs']]
                or [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in ev['body']['rows']]!=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in control['body']['rows']]):
            raise ValueError('Same complete fixed80 prefixes and common256 body bytes required: '+name)
    quality={a:quality_gates(control,ev,scores[a],scores['next_two'],'content') for a,control in evaluations.items()}
    s=summaries['next_two']
    absolute=dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,
        appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,
        repetition_at_most18=s['rates']['repetition']<=18,
        no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    original=adoption_checks(read_json(Path(p['original_references']['historical_Web']['path'])),ev)
    # Supplement repeated-DEV accuracy with exact input identity and paired CIs.
    source=ROOT/c['evaluation']['semantic_suite']
    if sha256(source)!=c['evaluation']['semantic_sha256']:raise ValueError('Same Japanese semantic suite required')
    original_rows,_=dev_cases(source)
    native_semantics=validate_cached(read_json(RUN/'evaluation/next_two/evaluation/semantics.json'),record)
    require_same_inputs(original_rows,native_semantics)
    semantic_report=dict(next_two=summary(native_semantics),paired={})
    from review_chat_base_retention import paired_bpb
    bpb={}
    for arm in ARMS:
        cached=validate_cached(read_json(Path(p['references']['semantics_'+arm]['path'])),controls[arm]['training'])
        require_same_inputs(original_rows,cached)
        semantic_report['paired'][arm]=paired(cached,native_semantics)
        bpb[arm]=paired_bpb(controls[arm]['evaluation']['body'],ev['body'])
        bpb[arm]['direction']='next_two minus completed '+arm+'; positive means worse'
    eligible=all(q['passed'] for q in quality.values()) and all(absolute.values()) and all(original.values())
    report=dict(status='new80_and_reused80_next_two_comparison_reviewed',created_at=now(),config_sha256=digest,
        review_policy_sha256=sha256(POLICY),result_sha256=sha256(RUN/'result.json'),summaries=summaries,
        strong_and_matched_quality=quality,absolute_dev_screen=absolute,historical_Web=original,
        paired_common_byte_BPB=bpb,exact_content_semantics=semantic_report,
        eligible_for_final_Base_validation=eligible,accounting=account,history=history,common_CE_checks=common,
        new_scientific_CE_teacher_tokens=100000000,reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,
        probe_verification_updates=probe['verification_updates'],probe_verification_CE_teachers=probe['verification_original_teacher_positions'],
        probe_verification_next_two_positions=probe['verification_next_two_positions'],
        scientific_next_two_positions=account['next_two_teacher_positions'],
        total_scientific_label_positions=100000000+account['next_two_teacher_positions'],
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],new80_individually_read=True,reused80_individually_read=True,
        independent_human_blind=False,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
        final_seed_full_dev_test_adoption_pending=True,
        limitations='Single learned seed, repeated nonblind DEV, same native parameters/CE input and teacher stream; additional future gold positions, train-only parameters and GPU overhead differ; not equal-total-label efficiency. Semantic input identity uses exact-content clusters; other template correlations remain. Body256 bootstrap is paired byte-weighted, not whole-corpus or independent-seed confirmation. No new unique supply from repeated draws. DEV task loader may decode suite JSON but no protected TEST cases are scored.',
        next_action='Only a qualified fixed next_two candidate advances to independent learned seed/full DEV/protected final TEST/adoption. Otherwise close this fixed mechanism without horizon/coefficient/head/LR/source/checkpoint/epoch rescue. Notify/stop at completed Base; no Chat or quantization.')
    if (RUN/'review.json').exists():raise ValueError('Preserve completed next_two review')
    atomic_json(RUN/'review.json',report)
    atomic_json(ROOT/'reports/phase6/base_next_two_token_comparison_review.json',report)
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
