"""Native on-policy feedback comparison with all existing Base gates intact."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from jmicro.phase5 import equal_state
from base_on_policy_teacher_trainer import KIND
from base_on_policy_teacher_trainer import committed_state, RECIPE
from phase6_performance import alive
from run_base_on_policy_teacher import CONFIG, RUN, CONTROL, matched_control_checks
import review_natural_context_contrast as prior
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks

POLICY = ROOT/'configs/phase6/base_on_policy_teacher_review.json'
NOTES = ROOT/'reports/phase6/base_on_policy_teacher_notes.json'
RAW = RUN/'evaluation/on_policy_teacher/evaluation/generation.json'
HELPERS = ('scripts/review_base_on_policy_teacher.py','scripts/review_natural_context_contrast.py',
    'scripts/review_parameter_displacement_anchor.py','scripts/review_matched_story_study.py',
    'scripts/review_textbook_quantity_comparison.py','scripts/review_eos_5b_finish.py','scripts/run_eos_complete_100m.py')


def prepare():
    if POLICY.exists(): raise ValueError('Preserve fixed OnPolicyTeacher review policy')
    _, old = prior.load_policy()
    refs = {k:v for k,v in old['references'].items()}
    refs['cached_control_result'] = dict(path=str(CONTROL/'result.json'),sha256=sha256(CONTROL/'result.json'))
    refs['cached_control_notes'] = dict(path=str(ROOT/'reports/phase6/natural_context_contrast_CE_notes.json'),
        sha256=sha256(ROOT/'reports/phase6/natural_context_contrast_CE_notes.json'))
    refs['cached_control_raw'] = dict(path=str(CONTROL/'evaluation/CE/evaluation/generation.json'),
        sha256=sha256(CONTROL/'evaluation/CE/evaluation/generation.json'))
    atomic_json(POLICY,dict(created_at=now(),config_sha256=sha256(CONFIG),references=refs,
        strong_summary=old['strong_summary'], helper_sha256={name:sha256(ROOT/name) for name in HELPERS},
        criteria=old['criteria']+' Same original CE100M stream additionally required. Added current-student trajectories/native teacher distributions and extra compute separately counted; original gold inputs unchanged. All80 individual new observations.',
        scientific_results_read=False,Base_complete=False,Chat_started=False,quantization_started=False))
    print('OnPolicyTeacher quality policy frozen before science; criteria unchanged')


def load_policy():
    c,p = read_json(CONFIG),read_json(POLICY)
    if p['config_sha256'] != sha256(CONFIG): raise ValueError('Frozen OnPolicyTeacher config changed')
    for name,digest in {**c['source_sha256'],**p['helper_sha256']}.items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen quality source changed')
    for r in p['references'].values(): prior.checked_reference(r)
    return c,p


def audit_state(state, record, c):
    counters=state['counters']; steps=counters['update']; opt=state['optimizer']; aux=state['on_policy_teacher']
    if (not committed_state(state) or state['kind']!=KIND or state['binding']!=record['binding'] or
        state['spec']['optimizer_policy']!='fresh_equal_AdamW_both_arms' or
        state['spec']['batch']!=48 or state['spec']['seed']!=42 or state['spec']['contrast'] or
        state['spec']['on_policy_teacher']!=RECIPE or c['on_policy_teacher_recipe']!=RECIPE or
        state['spec']['teacher']!=c['teacher'] or state['lineage']['teacher']!=c['teacher'] or
        state['model_config']['expected_parameter_count']!=10001152 or
        counters['supervised_tokens']!=100000000 or counters['source_teachers']!=c['goals'] or
        counters!=record['counters'] or not equal_state(state['sampler'],record['sampler']) or
        state['lineage']['parent']!=c['parent'] or counters['auxiliary_pairs'] or counters['auxiliary_input_tokens'] or steps<=0 or
        aux!=record['on_policy_teacher'] or not 0<aux['rollout_batches']<=aux['scheduled_batches'] or
        not 0<aux['sequences']<=8*aux['rollout_batches'] or
        aux['distribution_positions']!=record['scientific_distribution_positions'] or
        not 0<aux['distribution_positions']<=aux['teacher_valid_inputs'] or
        aux['teacher_valid_inputs']!=aux['student_scoring_valid_inputs'] or
        aux['teacher_physical_inputs']!=aux['student_scoring_physical_inputs'] or
        any(type(n) is not int or n<0 for n in aux['source_positions'].values()) or
        record['teacher_immutable_checks']!=dict(weights_unchanged=True,eval_no_grad=True,student_only_optimizer=True) or
        any(g['lr']!=1e-5 or g['weight_decay']!=.1 for g in opt['param_groups'])):
        raise ValueError('Exact native original100M/current-student feedback committed state required')


def audit_rollout_history(history,final):
    """Reconstruct sampled positions/input costs/digest from actual saved IDs."""
    count=dict(rollout_batches=0,sequences=0,distribution_positions=0,generated_body_positions=0,generated_EOS=0,
        rollout_valid_inputs=0,rollout_physical_inputs=0,student_scoring_valid_inputs=0,student_scoring_physical_inputs=0,
        teacher_valid_inputs=0,teacher_physical_inputs=0,source_positions=dict(web=0,textbook=0,story=0))
    digest='0'*64
    for update,row in sorted(history.items()):
        records=row['rollout_records']
        if not all(math.isfinite(row[k]) for k in ('CE_loss','teacher_feedback_KL','combined_loss','gradient_norm')):
            raise ValueError('Finite committed CE/feedback/gradient history required')
        if records:
            if update%16 or len(records)>8 or row['current_student_update_for_rollout']!=update-1:
                raise ValueError('Current student at fixed scheduled updates required')
            scored=[];lengths=[]
            for r in records:
                p,g=r['prompt'],r['generated']
                if (r['source'] not in ('textbook','story') or not 2<=len(p)<=17 or p[0]!=2 or any(t<8 for t in p[1:]) or
                    not 1<=len(g)<=32 or any(t!=3 and t<8 for t in g) or 3 in g[:-1] or r['EOS_stopped']!=(g[-1]==3) or
                    not any(a[0]==r['index_byte_position'] and a[1]==r['index_record_sha256'] and a[2]==1 for a in row['draw_trace'])):
                    raise ValueError('Original TRAIN head/actual sampled body/firstEOS history required')
                count['source_positions'][r['source']]+=len(g);count['generated_EOS']+=g.count(3)
                count['generated_body_positions']+=sum(t>=8 for t in g);lengths.append(len(g));scored.append(len(p)+len(g)-1)
            count['rollout_batches']+=1;count['sequences']+=len(records);count['distribution_positions']+=sum(lengths)
            count['rollout_valid_inputs']+=sum(len(r['prompt'])+len(r['generated'])-1 for r in records)
            count['rollout_physical_inputs']+=len(records)*(max(len(r['prompt']) for r in records)+max(lengths)-1)
            for prefix in ('student_scoring','teacher'):
                count[prefix+'_valid_inputs']+=sum(scored);count[prefix+'_physical_inputs']+=len(records)*max(scored)
            digest=hashlib.sha256(bytes.fromhex(digest)+json.dumps(records,sort_keys=True).encode()).hexdigest()
        if row['distribution_positions_this_update']!=sum(len(r['generated']) for r in records):
            raise ValueError('Actual generated-position count differs')
        if any(row['on_policy_teacher'][k]!=v for k,v in count.items()) or row['on_policy_teacher']['digest']!=digest:
            raise ValueError('Committed auxiliary costs/source/positions/digest differ from actual IDs')
    if any(final[k]!=v for k,v in count.items()) or final['digest']!=digest:
        raise ValueError('Terminal auxiliary history differs')


def review(template=False):
    c,p = load_policy(); job,result = read_json(RUN/'job.json'),read_json(RUN/'result.json')
    if (alive(job) or job['status'] != 'complete' or result['status'] != 'complete' or
            result['config_sha256'] != job['config_sha256'] or result['config_sha256'] != sha256(CONFIG) or
            result['actual_identity'] != {k:job[k] for k in ('pid','boot_id','start_ticks')} or
            not 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= c['GPU_budget_seconds'] or
            result['total_GPU_seconds_including_probe'] != result['GPU_occupancy_seconds']+c['probe_GPU_seconds'] or
            result['total_GPU_seconds_including_probe'] > 7200):
        raise ValueError('Actual exited bounded OnPolicyTeacher science required')
    record,ev = result['training'],result['evaluation']
    if sha256(Path(record['checkpoint'])) != record['checkpoint_sha256']: raise ValueError('Native checkpoint SHA changed')
    state = torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    audit_state(state,record,c)
    control = read_json(Path(p['references']['cached_control_result']['path']))['results']['CE']
    checks = matched_control_checks(record,control['training'])
    if checks != result['common_CE_checks'] or not all(checks.values()): raise ValueError('Same original100M source/sampler differs')
    # Every completed update is checked once; discarded post-checkpoint attempts remain in their own logs.
    history = {}
    for path in sorted((RUN/'on_policy_teacher').glob('metrics-*.jsonl'),key=lambda p:p.stat().st_mtime_ns):
        for line in path.read_text().splitlines():
            row = json.loads(line)
            if row['update'] <= state['counters']['update']: history[row['update']] = row
    if sorted(history) != list(range(1,state['counters']['update']+1)) or any(
            not 0 <= r['CE_loss'] < float('inf') or r['lr'] != 1e-5 for r in history.values()):
        raise ValueError('Complete finite committed-update history required')
    if not equal_state({k:history[steps][k] for k in state['counters']},state['counters']) if (steps:=state['counters']['update']) else True:
        raise ValueError('Final history/committed state counters differ')
    if history[steps]['on_policy_teacher'] != state['on_policy_teacher']:
        raise ValueError('Final committed teacher-feedback history differs')
    audit_rollout_history(history,state['on_policy_teacher'])
    if template:
        if NOTES.exists(): raise ValueError('Preserve existing individual notes')
        atomic_json(NOTES,dict(reviewer='Codex nonblind; all80 require individual reading',independent_human_blind=False,
            generation_sha256=sha256(RAW),notes=[[r['id'],None,None,None,None,''] for r in read_json(RAW)['outputs']]))
        print('Unscored OnPolicyTeacher80 template; no quality pass claimed'); return
    base = read_json(Path(p['references']['original_config']['path']))
    old = read_json(Path(p['references']['strong_result']['path']))
    strong_ev = old['evaluations']['source_order']
    strong_raw = Path(p['references']['strong_result']['path']).parent/'evaluation/source_order/evaluation/generation.json'
    strong,ss = content('strong_staged',strong_ev,old['checkpoints']['source_order'],base,strong_raw,Path(p['references']['strong_notes']['path']))
    candidate,cs = content('on_policy_teacher',ev,record,c,RAW,NOTES)
    cached,oscores = content('cached_CE',control['evaluation'],control['training'],c,
        Path(p['references']['cached_control_raw']['path']),Path(p['references']['cached_control_notes']['path']))
    if strong != p['strong_summary']: raise ValueError('Strong baseline changed')
    matched = quality_gates(control['evaluation'],ev,oscores,cs,'on_policy_teacher_vs_cached_CE')
    relative = quality_gates(strong_ev,ev,ss,cs,'on_policy_teacher_vs_strong')
    s = candidate
    absolute = dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,
        appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,
        repetition_at_most18=s['rates']['repetition']<=18,
        no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    historical = adoption_checks(read_json(Path(p['references']['historical_Web']['path'])),ev)
    eligible = matched['passed'] and relative['passed'] and all(absolute.values()) and all(historical.values())
    output = dict(status='OnPolicyTeacher_native100M_and_all80_reviewed',created_at=now(),
        config_sha256=sha256(CONFIG),result_sha256=sha256(RUN/'result.json'),policy_sha256=sha256(POLICY),
        summaries=dict(on_policy_teacher=candidate,CE=cached,strong_staged=strong),matched_objective_quality=matched,
        quality_comparison=relative,absolute_dev_screen=absolute,original_Web=historical,
        eligible_for_final_Base_validation=eligible,scientific_CE_teacher_tokens=100000000,
        reused_control_teacher_tokens=100000000,GPU_seconds=result['GPU_occupancy_seconds'],
        probe_GPU_seconds=c['probe_GPU_seconds'],on_policy_teacher=state['on_policy_teacher'],all80_individually_read=True,independent_human_blind=False,
        notes_sha256=sha256(NOTES),Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_scored=False,
        limitations='Single learned seed; repeated nonblind DEV; additional autoregressive/teacher compute and distribution supervision. Teacher is unadopted and not universally correct; no new corpus or capacity proof. Independent learnedseed/fullDEV/protectedTEST/adoption remain required.')
    atomic_json(ROOT/'reports/phase6/base_on_policy_teacher_comparison_review.json',output)
    print(json.dumps(dict(summary=candidate,eligible_for_final_Base_validation=eligible),ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(); parser.add_argument('--prepare',action='store_true'); parser.add_argument('--template',action='store_true')
    args=parser.parse_args(); prepare() if args.prepare else review(args.template)
