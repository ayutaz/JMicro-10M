"""CPU closeout of unchanged-parent2B decay comparison and original Base gates."""
import argparse
import json
from pathlib import Path
import sys
import urllib.request

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from jmicro.phase5 import equal_state
from base_teacher_decay_trainer import committed_decay,policy,KIND
from base_teacher_decay_2b_protocol import TOTAL,EXTRA,audit_terminal,audit_compact_history,common_stream
from run_base_teacher_decay_2b import CONFIG,RUN,checked,ref,study_binding
from phase6_performance import alive
from review_parameter_displacement_anchor import content
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
from review_base_teacher_decay_pilot import paired_summary

PHASE=ROOT/'reports/phase6'
OUTPUT=PHASE/'base_teacher_decay_2b_completion.json'
NOTES=PHASE/'base_teacher_decay_2b_candidate_notes.json'
RAW=RUN/'evaluation/candidate/evaluation/generation.json'


def main(template=False):
    if OUTPUT.exists(): raise ValueError('Preserve completed2B comparison')
    c=read_json(CONFIG);job=read_json(RUN/'job.json');result=read_json(RUN/'result.json')
    audit_terminal(job,result,c,sha256(CONFIG),alive(job))
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen continuation/review source differs: '+name)
    checked(c['proposal']);base=checked(c['base_config']);quality=checked(c['original_quality_policy'])
    for reference in c['quality_references'].values(): checked(reference)
    record=checked(result['training_record'])
    if (record['status']!='complete' or record['binding']!=study_binding(c) or result['binding']!=record['binding']
            or record['research_kind']!=KIND or record['parent_checkpoint']!=c['parent_checkpoint']
            or record['new_scientific_teacher_tokens']!=EXTRA or record['scientific_CE_teacher_tokens']!=TOTAL
            or result['parent_checkpoint']!=c['parent_checkpoint'] or result['control_checkpoint']!=c['control_checkpoint']
            or result['candidate_checkpoint']!=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256'])):
        raise ValueError('Separately bound unchanged-parent2B continuation record required')
    if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:
        raise ValueError('Actual terminal checkpoint differs')
    state=torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
    if sha256(Path(c['parent_checkpoint']['path']))!=c['parent_checkpoint']['sha256']:
        raise ValueError('Immutable learned pilot parent differs')
    parent=torch.load(c['parent_checkpoint']['path'],map_location='cpu',weights_only=False)
    if (not committed_decay(state) or not committed_decay(parent)
            or state['binding']!=c['checkpoint_binding'] or record['checkpoint_ancestry_binding']!=state['binding']
            or any(not equal_state(state[k],parent[k]) for k in ('spec','binding','lineage','model_config'))
            or state['decay']['policy']!=policy() or state['spec']['dtype']!='bf16' or state['spec']['backend']!='flash'
            or state['counters']!=record['counters'] or state['counters']!=result['counters']
            or parent['counters']!=c['parent_counters']
            or any(not equal_state(state[k],record[k]) for k in ('sampler','scheduler','spec','lineage','model_config','decay'))):
        raise ValueError('Exact finite committed2B state and unchanged learned recipe/ancestry required')
    control_record=checked(c['control_training_record'])
    checks=common_stream(state,control_record)
    if checks!=result['stream_checks'] or not all(checks.values()):
        raise ValueError('Same complete native2B original stream/scheduler required')
    paths=sorted(RUN.glob('metrics-*.jsonl'),key=lambda p:p.stat().st_mtime_ns)
    def rows():
        for path in paths:
            with path.open() as stream:
                for line in stream: yield json.loads(line)
    history=audit_compact_history(rows(),parent['counters'],state)
    del state,parent
    candidate=checked(result['candidate_evaluation']);control=checked(c['control_evaluation'])
    if (candidate['binding']!=record['binding'] or candidate['checkpoint_sha256']!=record['checkpoint_sha256']
            or read_json(RAW)!=candidate['generation'] or len(candidate['generation']['outputs'])!=80
            or candidate['protected_test_used'] or not candidate['evaluation_RNG_isolated']
            or any(not candidate['diagnostics'][k]['complete'] or candidate['diagnostics'][k]['count']!=n
                   for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items())):
        raise ValueError('All native fixedDEV/Japanese/80 checkpoint-bound outputs required')
    if template:
        if NOTES.exists(): raise ValueError('Preserve individual content notes')
        atomic_json(NOTES,dict(reviewer='Codex nonblind; all80 require individual reading',independent_human_blind=False,
            all80_individually_read=False,generation_sha256=sha256(RAW),
            notes=[[r['id'],None,None,None,None,''] for r in candidate['generation']['outputs']]))
        print('Unscored candidate80 template; original native2B control notes retained');return
    if read_json(NOTES).get('all80_individually_read') is not True:
        raise ValueError('All80 new continuations must be individually read')
    checked(c['control_raw']);checked(c['control_notes']);checked(c['related_completed_comparison'])
    a,aa=content('matched_native2B',control,control_record,base,Path(c['control_raw']['path']),Path(c['control_notes']['path']))
    b,bb=content('teacher_decay2B',candidate,record,base,RAW,NOTES)
    original=read_json(Path(quality['references']['original_config']['path']))
    strong_result=read_json(Path(quality['references']['strong_result']['path']))
    strong_ev=strong_result['evaluations']['source_order'];strong_record=strong_result['checkpoints']['source_order']
    strong_raw=Path(quality['references']['strong_result']['path']).parent/'evaluation/source_order/evaluation/generation.json'
    strong,ss=content('strong_staged',strong_ev,strong_record,original,strong_raw,Path(quality['references']['strong_notes']['path']))
    if strong!=quality['strong_summary']: raise ValueError('Original strong reference changed')
    cached=read_json(Path(quality['references']['cached_control_result']['path']))['results']['CE']
    cached_summary,cs=content('cached_CE',cached['evaluation'],cached['training'],base,
        Path(quality['references']['cached_control_raw']['path']),Path(quality['references']['cached_control_notes']['path']))
    comparisons=dict(matched_native=quality_gates(control,candidate,aa,bb,'decay_vs_fresh_native2B'),
        strong=quality_gates(strong_ev,candidate,ss,bb,'decay_vs_strong'),
        cached_native=quality_gates(cached['evaluation'],candidate,cs,bb,'decay_vs_cached_native'))
    absolute=dict(grammar_at_least56=b['grammar2']>=56,coherence_at_least27=b['coherent']>=27,
        appropriate_at_least27=b['appropriate']>=27,EOS_at_least37=b['rates']['eos']>=37,
        repetition_at_most18=b['rates']['repetition']<=18,
        no_empty_role_unicode=all(b['rates'][k]==0 for k in ('empty','role_leak','unicode_failure')))
    historical=adoption_checks(read_json(Path(quality['references']['historical_Web']['path'])),candidate)
    eligible=all(q['passed'] for q in comparisons.values()) and all(absolute.values()) and all(historical.values())
    launcher=read_json(PHASE/'base-teacher-decay-2b-launcher-20261008/result.json')
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response: model=json.load(response)
    if (launcher['status']!='complete' or launcher['exit_code'] or not launcher['UI_restore_command_succeeded']
            or not alive(ui) or model['busy'] or model['training_tokens']!=10000007168
            or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'):
        raise ValueError('Exited launcher and actual restored idle original10B UI required')
    atomic_json(OUTPUT,dict(status='same_parent_teacher_decay2B_all80_reviewed',created_at=now(),config=ref(CONFIG),
        result=ref(RUN/'result.json'),reviewer_source=ref(Path(__file__)),original_quality_policy=c['original_quality_policy'],
        summaries=dict(matched_native2B=a,candidate=b,strong_staged=strong,cached_CE=cached_summary),
        candidate_raw=ref(RAW),candidate_notes=ref(NOTES),control_raw=c['control_raw'],control_notes=c['control_notes'],
        paired_differences=paired_summary(control,candidate,aa,bb),quality_comparisons=comparisons,
        absolute_dev_screen=absolute,original_Web=historical,eligible_for_final_Base_validation=eligible,
        fixed_condition_closed=not eligible,compact_history=history,all80_new_individually_read=True,old_control80_original_notes_reused=True,
        independent_human_blind=False,scientific_cumulative_teacher_tokens=TOTAL,new_scientific_teacher_tokens=EXTRA,
        reused_control_teacher_tokens=TOTAL,verification_teacher_tokens=result['resume_gate']['verification_teacher_tokens'],
        GPU_seconds=result['GPU_seconds'],GPU_cap_seconds=c['GPU_cap_seconds'],prior_pilot_GPU_seconds=c['prior_pilot_GPU_seconds'],
        combined_GPU_seconds=result['combined_GPU_seconds'],process_exited=True,restored_UI_identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},
        restored_UI_model=model,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False,
        limits='One trained seed42, repeatedDEV and nonblind ratings. Same learned-parent continuation; original matched2B stream and extra strong/cached/history references kept distinct. No Base adoption here; independent trainedseed/fullDEV/protectedTEST/adoption still required.'))
    print(json.dumps(dict(status='2B_content_review_complete',summary=b,eligible_for_final_Base_validation=eligible,Base_complete=False)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--template',action='store_true')
    args=parser.parse_args();torch.set_num_threads(2);main(args.template)
