"""Native same100M optimizer comparison, preserving every existing Base quality gate."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from jmicro.phase5 import equal_state
from base_native_teacher_KD_committed import KIND, committed_state, RECIPE
from phase6_performance import alive
from run_base_native_teacher_KD_science import CONFIG, RUN, CONTROL, matched_control_checks
import review_natural_context_contrast as prior
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks

POLICY = ROOT/'configs/phase6/base_native_teacher_KD_science_review.json'
NOTES = ROOT/'reports/phase6/base_native_teacher_KD_science_notes.json'
RAW = RUN/'evaluation/native_teacher_KD/evaluation/generation.json'
HELPERS = ('scripts/review_base_native_teacher_KD_science.py','scripts/review_natural_context_contrast.py',
    'scripts/review_parameter_displacement_anchor.py','scripts/review_matched_story_study.py',
    'scripts/review_textbook_quantity_comparison.py','scripts/review_eos_5b_finish.py','scripts/run_eos_complete_100m.py')


def prepare():
    if POLICY.exists(): raise ValueError('Preserve fixed native_teacher_KD review policy')
    _, old = prior.load_policy()
    refs = {k:v for k,v in old['references'].items()}
    refs['cached_control_result'] = dict(path=str(CONTROL/'result.json'),sha256=sha256(CONTROL/'result.json'))
    refs['cached_control_notes'] = dict(path=str(ROOT/'reports/phase6/natural_context_contrast_CE_notes.json'),
        sha256=sha256(ROOT/'reports/phase6/natural_context_contrast_CE_notes.json'))
    refs['cached_control_raw'] = dict(path=str(CONTROL/'evaluation/CE/evaluation/generation.json'),
        sha256=sha256(CONTROL/'evaluation/CE/evaluation/generation.json'))
    atomic_json(POLICY,dict(created_at=now(),config_sha256=sha256(CONFIG),references=refs,
        strong_summary=old['strong_summary'], helper_sha256={name:sha256(ROOT/name) for name in HELPERS},
        criteria=old['criteria']+' Same cached CE100M additionally required; original full-vocab native short-prefix KD math; separately reconsidered prospective resource plan. Extra25M predictive positions/teacher compute differ. All80 individual new observations.',
        scientific_results_read=False,Base_complete=False,Chat_started=False,quantization_started=False))
    print('native_teacher_KD quality policy frozen before science; criteria unchanged')


def load_policy():
    c,p = read_json(CONFIG),read_json(POLICY)
    if p['config_sha256'] != sha256(CONFIG): raise ValueError('Frozen native_teacher_KD config changed')
    for name,digest in {**c['source_sha256'],**p['helper_sha256']}.items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen quality source changed')
    for r in p['references'].values(): prior.checked_reference(r)
    return c,p


def audit_state(state,record,c):
    counters=state['counters']; steps=counters['update']; opt=state['optimizer']
    if (not committed_state(state) or state['kind']!=KIND or state['binding']!=record['binding'] or
        state['spec']['optimizer_policy']!='fresh_equal_AdamW_both_arms' or state['spec']['prospective_KD_study']!=RECIPE or c['native_teacher_KD_recipe']!=RECIPE or
        state['spec']['batch']!=48 or state['spec']['seed']!=42 or state['spec']['contrast'] or
        state['model_config']['expected_parameter_count']!=10001152 or counters['supervised_tokens']!=100000000 or
        counters['source_teachers']!=c['goals'] or counters!=record['counters'] or state['native_teacher_KD']!=record['native_teacher_KD'] or
        record['scientific_KD_distribution_positions']!=25000000 or
        not all(record.get(k) is True for k in ('teacher_unchanged','teacher_eval_no_grad','optimizer_student_only')) or
        state['spec']['teacher']!=c['teacher'] or state['binding']['teacher']!=c['teacher'] or
        not equal_state(state['sampler'],record['sampler']) or
        state['lineage']['parent']!=c['parent'] or steps<=0 or len(opt['state'])!=sum(len(g['params']) for g in opt['param_groups']) or
        any(g['lr']!=1e-5 or g['weight_decay']!=.1 for g in opt['param_groups'])):
        raise ValueError('Exact complete original100M/middle-head committed state required')


def review(template=False):
    c,p = load_policy(); job,result = read_json(RUN/'job.json'),read_json(RUN/'result.json')
    if (alive(job) or job['status'] != 'complete' or result['status'] != 'complete' or
            result['config_sha256'] != job['config_sha256'] or result['config_sha256'] != sha256(CONFIG) or
            result['actual_identity'] != {k:job[k] for k in ('pid','boot_id','start_ticks')} or
            not 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= c['GPU_budget_seconds'] or
            result['total_GPU_seconds_including_probe'] != result['GPU_occupancy_seconds']+c['probe_GPU_seconds'] or
            result['total_GPU_seconds_including_probe'] > 4800):
        raise ValueError('Actual exited bounded native_teacher_KD science required')
    record,ev = result['training'],result['evaluation']
    if sha256(Path(record['checkpoint'])) != record['checkpoint_sha256']: raise ValueError('Native checkpoint SHA changed')
    state = torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    audit_state(state,record,c)
    control = read_json(Path(p['references']['cached_control_result']['path']))['results']['CE']
    checks = matched_control_checks(record,control['training'])
    if checks != result['common_CE_checks'] or not all(checks.values()): raise ValueError('Same original100M source/sampler differs')
    # Every completed update is checked once; discarded post-checkpoint attempts remain in their own logs.
    history = {}
    for path in sorted((RUN/'native_teacher_KD').glob('metrics-*.jsonl'),key=lambda p:p.stat().st_mtime_ns):
        for line in path.read_text().splitlines():
            row = json.loads(line)
            if row['update'] <= state['counters']['update']: history[row['update']] = row
    if sorted(history) != list(range(1,state['counters']['update']+1)) or any(
            not 0 <= r['CE_loss'] < float('inf') or r['lr'] != 1e-5 for r in history.values()):
        raise ValueError('Complete finite committed-update history required')
    if not equal_state({k:history[steps][k] for k in state['counters']},state['counters']) if (steps:=state['counters']['update']) else True:
        raise ValueError('Final history/committed state counters differ')
    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','KD_loss','combined_loss','gradient_norm')) or
            abs(r['combined_loss']-(r['CE_loss']+r['KD_loss']))>2e-6 or r['committed_update'] is not True or
            r['native_teacher_KD']['updates']!=u or
            r['native_teacher_KD']['teacher_positions']!=sum(r['source_teachers'][g] for g in ('textbook','story')) or
            r['native_teacher_KD']['source_positions']!={g:(r['source_teachers'][g] if g in ('textbook','story') else 0) for g in ('web','textbook','story')} or
            not 0<=r['KD_targets_this_update']<=r['CE_targets_this_update']
            for u,r in history.items()): raise ValueError('Finite committed original CE/dense short-KD full history required')
    if template:
        if NOTES.exists(): raise ValueError('Preserve existing individual notes')
        atomic_json(NOTES,dict(reviewer='Codex nonblind; all80 require individual reading',independent_human_blind=False,
            generation_sha256=sha256(RAW),notes=[[r['id'],None,None,None,None,''] for r in read_json(RAW)['outputs']]))
        print('Unscored native_teacher_KD80 template; no quality pass claimed'); return
    base = read_json(Path(p['references']['original_config']['path']))
    old = read_json(Path(p['references']['strong_result']['path']))
    strong_ev = old['evaluations']['source_order']
    strong_raw = Path(p['references']['strong_result']['path']).parent/'evaluation/source_order/evaluation/generation.json'
    strong,ss = content('strong_staged',strong_ev,old['checkpoints']['source_order'],base,strong_raw,Path(p['references']['strong_notes']['path']))
    candidate,cs = content('native_teacher_KD',ev,record,c,RAW,NOTES)
    cached,oscores = content('cached_CE',control['evaluation'],control['training'],c,
        Path(p['references']['cached_control_raw']['path']),Path(p['references']['cached_control_notes']['path']))
    if strong != p['strong_summary']: raise ValueError('Strong baseline changed')
    matched = quality_gates(control['evaluation'],ev,oscores,cs,'native_teacher_KD_vs_cached_CE')
    relative = quality_gates(strong_ev,ev,ss,cs,'native_teacher_KD_vs_strong')
    s = candidate
    absolute = dict(grammar_at_least56=s['grammar2']>=56,coherence_at_least27=s['coherent']>=27,
        appropriate_at_least27=s['appropriate']>=27,EOS_at_least37=s['rates']['eos']>=37,
        repetition_at_most18=s['rates']['repetition']<=18,
        no_empty_role_unicode=all(s['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    historical = adoption_checks(read_json(Path(p['references']['historical_Web']['path'])),ev)
    eligible = matched['passed'] and relative['passed'] and all(absolute.values()) and all(historical.values())
    output = dict(status='native_teacher_KD_native100M_and_all80_reviewed',created_at=now(),
        config_sha256=sha256(CONFIG),result_sha256=sha256(RUN/'result.json'),policy_sha256=sha256(POLICY),
        summaries=dict(native_teacher_KD=candidate,CE=cached,strong_staged=strong),matched_objective_quality=matched,
        quality_comparison=relative,absolute_dev_screen=absolute,original_Web=historical,
        eligible_for_final_Base_validation=eligible,scientific_CE_teacher_tokens=100000000,
        reused_control_teacher_tokens=100000000,GPU_seconds=result['GPU_occupancy_seconds'],
        probe_GPU_seconds=c['probe_GPU_seconds'],native_teacher_KD=state['native_teacher_KD'],scientific_KD_distribution_positions=25000000,all80_individually_read=True,independent_human_blind=False,
        notes_sha256=sha256(NOTES),Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_scored=False,
        limitations='Single seed and mature-parent native dense-KD resource study; repeated nonblind DEV; extra25M predictive targets and frozen teacher compute; same original100M gold. No new unique corpus or capacity proof. Independent learnedseed/full DEV/protected TEST/adoption remain required.')
    atomic_json(ROOT/'reports/phase6/base_native_teacher_KD_science_comparison_review.json',output)
    print(json.dumps(dict(summary=candidate,eligible_for_final_Base_validation=eligible),ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(); parser.add_argument('--prepare',action='store_true'); parser.add_argument('--template',action='store_true')
    args=parser.parse_args(); prepare() if args.prepare else review(args.template)
