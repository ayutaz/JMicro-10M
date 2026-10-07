"""Actual paired gate fullstate/all160 review with unchanged Base guards."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from jmicro.phase5 import equal_state
from base_headwise_gate_model import ARMS,POLICY as GATE_POLICY
from base_headwise_gate_trainer import HeadwiseGateTrainer,KIND
from base_headwise_gate_evaluation import validate_record
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from run_base_headwise_gate import CONFIG,RUN,CONTROL
from probe_base_headwise_gate import source_checks
from phase6_performance import alive
import review_natural_context_contrast as prior
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks

POLICY=ROOT/'configs/phase6/base_headwise_gate_review.json'
HELPERS=('scripts/review_base_headwise_gate.py','scripts/review_natural_context_contrast.py',
    'scripts/review_parameter_displacement_anchor.py','scripts/review_matched_story_study.py',
    'scripts/review_textbook_quantity_comparison.py','scripts/review_eos_5b_finish.py','scripts/run_eos_complete_100m.py')


def notes_path(arm):return ROOT/f'reports/phase6/base_headwise_gate_{arm}_notes.json'


def raw_path(arm):return RUN/f'evaluation/{arm}/evaluation/generation.json'


def prepare():
    if POLICY.exists():raise ValueError('Preserve prospective paired gate quality policy')
    _,old=prior.load_policy();refs=dict(old['references'])
    for key,path in dict(cached_control_result=CONTROL/'result.json',
        cached_control_notes=ROOT/'reports/phase6/natural_context_contrast_CE_notes.json',
        cached_control_raw=CONTROL/'evaluation/CE/evaluation/generation.json').items():
        refs[key]=dict(path=str(path),sha256=sha256(path))
    atomic_json(POLICY,dict(created_at=now(),config_sha256=sha256(CONFIG),references=refs,
        strong_summary=old['strong_summary'],helper_sha256={name:sha256(ROOT/name) for name in HELPERS},
        criteria=old['criteria']+' Require new same-reparameterization static matched control; cached native CE is an additional reference, never its substitute. All160 individually raw-bound.',
        scientific_results_read=False,quality_criteria_unchanged=True,
        Base_complete=False,Chat_started=False,quantization_started=False))
    print('Paired gate quality policy frozen before science; original gates unchanged')


def load_policy():
    c,p=read_json(CONFIG),read_json(POLICY)
    if p['config_sha256']!=sha256(CONFIG):raise ValueError('Frozen paired gate config changed')
    for name,digest in {**c['source_sha256'],**p['helper_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen paired gate/review source changed: '+name)
    for reference in p['references'].values():prior.checked_reference(reference)
    return c,p


def audit_terminal(job,result,c,digest,live):
    if (live or job['status']!='complete' or result['status']!='complete'
            or job['config_sha256']!=digest or result['config_sha256']!=digest
            or result['actual_identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not 0<result['GPU_occupancy_seconds']==job['GPU_occupancy_seconds']<=c['GPU_budget_seconds']
            or not job.get('cumulative_GPU_ledger_closed',False)
            or result['total_GPU_seconds_including_probe']!=result['GPU_occupancy_seconds']+c['probe_GPU_seconds']
            or result['total_GPU_seconds_including_probe']>9000
            or result['scientific_CE_teacher_tokens']!=200000000 or set(result['results'])!=set(ARMS)
            or any(result[k] for k in ('Base_complete','Chat_started','quantization_started'))):
        raise ValueError('Actual exited bounded both100M Base-only science required')


def audit_state(state,record,c,arm,parent,codec):
    binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),
        weights_role='scientific_paired_headwise_gate',sources=c['source_sha256'])
    if (state.get('kind')!=KIND or state.get('binding')!=binding or record.get('binding')!=binding
            or record.get('status')!='complete' or record.get('scientific_CE_teacher_tokens')!=100000000
            or state['counters']['supervised_tokens']!=100000000
            or state['counters']['source_teachers']!=c['goals'] or state['counters']!=record['counters']
            or not equal_state(state['sampler'],record['sampler'])
            or any(state[k]!=record[k] for k in ('model_config','spec','lineage'))):
        raise ValueError('Complete exact typed gate100M record and source required')
    validate_record(arm,record)
    b=c['source_binding'];sampler=OriginalTrainCorpusSampler(b['pool'],b['manifest_sha256'],codec,c['goals'],42)
    if sampler.binding!=b:raise ValueError('Actual accepted sampler source differs')
    trainer=HeadwiseGateTrainer(parent,sampler,binding,arm,batch=48,device='cpu')
    trainer.validate_committed(state)
    if sum(p.numel() for p in trainer.model.parameters())!=10014464:
        raise ValueError('Actual unique paired study parameter count differs')


def audit_history(folder,state,arm):
    history={}
    for path in sorted(folder.glob('metrics-*.jsonl'),key=lambda p:p.stat().st_mtime_ns):
        for line in path.read_text().splitlines():
            row=json.loads(line)
            if row['update']<=state['counters']['update']:history[row['update']]=row
    steps=state['counters']['update']
    if sorted(history)!=list(range(1,steps+1)) or any(
            not math.isfinite(row['CE_loss']) or row['lr']!=1e-5
            or row['gate_arm']!=arm or row['gate_policy']!=GATE_POLICY['kind'] or not row['committed_update']
            for row in history.values()):
        raise ValueError('Every finite committed gate update required')
    if steps<=0 or not equal_state({k:history[steps][k] for k in state['counters']},state['counters']):
        raise ValueError('Last gate update/fullstate counters differ')


def review(template=False):
    torch.set_num_threads(2);c,p=load_policy();job,result=read_json(RUN/'job.json'),read_json(RUN/'result.json')
    audit_terminal(job,result,c,sha256(CONFIG),alive(job))
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);codec=Tokenizer(ROOT/c['tokenizer'])
    for arm in ARMS:
        record=result['results'][arm]['training']
        if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:raise ValueError('Gate checkpoint SHA changed')
        state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
        audit_state(state,record,c,arm,parent,codec);audit_history(RUN/arm,state,arm);del state
    common=source_checks(*(result['results'][arm]['training'] for arm in ARMS))
    cached=read_json(Path(p['references']['cached_control_result']['path']))['results']['CE']
    legacy={arm:source_checks(result['results'][arm]['training'],cached['training']) for arm in ARMS}
    if (common!=result['common_CE_checks'] or not all(common.values())
            or legacy!=result['cached_CE_checks'] or not all(all(v.values()) for v in legacy.values())):
        raise ValueError('Exact paired/cached original100M stream mismatch')
    if template:
        if any(notes_path(arm).exists() for arm in ARMS):raise ValueError('Preserve all individual notes')
        for arm in ARMS:
            atomic_json(notes_path(arm),dict(reviewer='Codex nonblind; each80 needs individual reading',independent_human_blind=False,
                generation_sha256=sha256(raw_path(arm)),notes=[[r['id'],None,None,None,None,''] for r in read_json(raw_path(arm))['outputs']]))
        print('Unscored all160 templates; no quality pass claimed');return
    base=read_json(Path(p['references']['original_config']['path']));old=read_json(Path(p['references']['strong_result']['path']))
    strong_ev=old['evaluations']['source_order'];strong_record=old['checkpoints']['source_order']
    strong_raw=Path(p['references']['strong_result']['path']).parent/'evaluation/source_order/evaluation/generation.json'
    strong,ss=content('strong_staged',strong_ev,strong_record,base,strong_raw,Path(p['references']['strong_notes']['path']))
    if strong!=p['strong_summary']:raise ValueError('Frozen strong staged reference changed')
    summaries=dict(strong_staged=strong);scores={}
    for arm in ARMS:
        entry=result['results'][arm]
        summaries[arm],scores[arm]=content(arm,entry['evaluation'],entry['training'],c,raw_path(arm),notes_path(arm))
    summaries['cached_CE'],cs=content('cached_CE',cached['evaluation'],cached['training'],c,
        Path(p['references']['cached_control_raw']['path']),Path(p['references']['cached_control_notes']['path']))
    candidate=result['results']['query_headwise']['evaluation'];candidate_scores=scores['query_headwise']
    comparisons=dict(
        new_static=quality_gates(result['results']['static_half']['evaluation'],candidate,scores['static_half'],candidate_scores,'query_gate_vs_new_static'),
        strong=quality_gates(strong_ev,candidate,ss,candidate_scores,'query_gate_vs_strong'),
        cached_native=quality_gates(cached['evaluation'],candidate,cs,candidate_scores,'query_gate_vs_cached_native'))
    s=summaries['query_headwise']
    absolute=dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,
        appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,repetition_at_most18=s['rates']['repetition']<=18,
        no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    historical=adoption_checks(read_json(Path(p['references']['historical_Web']['path'])),candidate)
    eligible=all(q['passed'] for q in comparisons.values()) and all(absolute.values()) and all(historical.values())
    output=dict(status='paired_headwise_gate100M_all160_reviewed',created_at=now(),config_sha256=sha256(CONFIG),
        result_sha256=sha256(RUN/'result.json'),policy_sha256=sha256(POLICY),summaries=summaries,
        quality_comparisons=comparisons,absolute_dev_screen=absolute,original_Web=historical,
        eligible_for_final_Base_validation=eligible,scientific_CE_teacher_tokens=200000000,
        reused_control_teacher_tokens=100000000,GPU_seconds=result['GPU_occupancy_seconds'],probe_GPU_seconds=c['probe_GPU_seconds'],
        all160_individually_read=True,independent_human_blind=False,notes_sha256={a:sha256(notes_path(a)) for a in ARMS},
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False,
        quality_criteria_unchanged=True,
        limitations='Single mature parent and training seed; altered parameterization/13312 added physical parameters, candidate gate learning freedom. Fixed repeated nonblind DEV, not independent human or final TEST. Independent learnedseed/fullDEV/protectedTEST/adoption pending.')
    destination=ROOT/'reports/phase6/base_headwise_gate_comparison_review.json'
    if destination.exists():raise ValueError('Preserve completed paired review')
    atomic_json(destination,output);print(json.dumps(dict(summary=s,eligible_for_final_Base_validation=eligible),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--prepare',action='store_true');group.add_argument('--template',action='store_true');args=parser.parse_args()
    prepare() if args.prepare else review(args.template)
