"""Preserve exited paired Base evidence and identical-text ratings; no adoption."""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from base_headwise_gate_model import ARMS,POLICY as GATE_POLICY
from base_headwise_gate_trainer import KIND,OPT_KIND,OPT_POLICY
from review_base_headwise_gate import CONFIG,RUN,POLICY,load_policy,notes_path,raw_path,audit_terminal

PHASE=ROOT/'reports/phase6'
PREPARATION=PHASE/'base_headwise_gate_closeout_preparation.json'
REVIEW=PHASE/'base_headwise_gate_comparison_review.json'
COMPLETION=PHASE/'base_headwise_gate_comparison_completion.json'
MANIFEST=PHASE/'base_headwise_gate_comparison_evidence_manifest.json'
BUNDLE=PHASE/'base_headwise_gate_comparison_evidence.tar.gz'
REUSE=PHASE/'base_headwise_gate_rating_reuse.json'


def ref(path):return dict(path=str(path),sha256=sha256(path))


def checked(reference):
    path=Path(reference['path'])
    if sha256(path)!=reference['sha256']:raise ValueError('Frozen historical evidence differs: '+path.name)
    return read_json(path)


def load_history(references):
    result=[]
    for reference in references:
        rows=checked(reference['raw'])['outputs'];notes=checked(reference['notes'])['notes']
        by_id={r['id']:r for r in rows};scores={r[0]:r[1:5] for r in notes}
        if len(rows)!=80 or len(by_id)!=80 or len(notes)!=80 or set(scores)!=set(by_id):
            raise ValueError('All80 unique historical raw-bound ratings required')
        result.append((reference['name'],by_id,scores))
    return result


def rating_reuse(rows,notes,history):
    current={r[0]:r[1:5] for r in notes['notes']}
    if len(rows)!=80 or len(notes['notes'])!=80 or len(current)!=80 or set(current)!={r['id'] for r in rows}:
        raise ValueError('All80 unique current individual ratings required')
    selected,differences=[],[]
    for row in rows:
        matches=[(name,scores[row['id']]) for name,old,scores in history if row['id'] in old
            and all(old[row['id']][key]==row[key] for key in ('id','prefix','text','stop_reason'))]
        if not matches:continue
        name,scores=matches[0]
        if current[row['id']]!=scores:raise ValueError('Previously rated identical text score differs: '+row['id'])
        selected.append(dict(id=row['id'],reference=name,scores=scores))
        differences.extend(dict(id=row['id'],selected_reference=name,selected_scores=scores,
            other_reference=other,other_scores=old) for other,old in matches[1:] if old!=scores)
    return dict(selected=selected,legacy_score_differences_preserved=differences)


def prospective_history(c):
    proposal=checked(c['proposal']);previous=checked(proposal['references']['previous'])
    old=checked(previous['exact_text_rating_reuse']);references=old['references']
    priority=['cached_CE','middle_supervision','sam','on_policy_teacher','confidence_penalty',
        'native_teacher_KD','native_hint','sigsoftmax']
    if old['fixed_reference_priority']!=priority or [r['name'] for r in references]!=priority:
        raise ValueError('Preserve fixed historical priority without outcome selection')
    references=[*references,dict(name='ademamix',raw=dict(
        path=str(PHASE/'base-ademamix-comparison-20261007/evaluation/ademamix/evaluation/generation.json'),
        sha256=previous['generation_sha256']),notes=previous['notes'])]
    return references,previous


def require_exited(c):
    job=read_json(RUN/'job.json')
    if alive(job) or job['status']!='complete':
        raise ValueError('Scientific process must finish and exit before archive')
    result=read_json(RUN/'result.json');audit_terminal(job,result,c,sha256(CONFIG),False)
    if not all(result['common_CE_checks'].values()) or not all(
            all(checks.values()) for checks in result['cached_CE_checks'].values()):
        raise ValueError('Exact paired/cached original stream checks required')
    return result


def prepare():
    if PREPARATION.exists():raise ValueError('Preserve prospective paired closeout')
    c,policy=load_policy();job=read_json(RUN/'job.json')
    if not alive(job) or job['status']!='running':raise ValueError('Actual same scientific job must be live')
    protected=(COMPLETION,MANIFEST,BUNDLE,REUSE)
    if any(path.exists() for path in (*protected,*(raw_path(a) for a in ARMS))):
        raise ValueError('Prepare fixed rating lineage before current generation outcomes')
    try:require_exited(c)
    except ValueError as error:
        refusal=str(error)
        if refusal!='Scientific process must finish and exit before archive':raise
    else:raise ValueError('Live science accepted as complete')
    references,previous=prospective_history(c);history=load_history(references)
    # The previously read AdEMAMix80 is a protocol fixture, not this study's content.
    rows=checked(references[-1]['raw'])['outputs'];notes=checked(references[-1]['notes'])
    fixture=rating_reuse(rows,notes,history)
    if len(fixture['selected'])!=80:raise ValueError('Actual old80 full rating lineage fixture failed')
    edited=deepcopy(notes);edited['notes'][0][1]=(edited['notes'][0][1]+1)%3
    try:rating_reuse(rows,edited,history)
    except ValueError as error:
        changed_refusal=str(error)
        if not changed_refusal.startswith('Previously rated identical text score differs: '):raise
    else:raise ValueError('Changed identical text rating accepted')
    atomic_json(PREPARATION,dict(created_at=now(),status='paired_closeout_prepared_not_completion',
        source=ref(Path(__file__)),config_sha256=sha256(CONFIG),policy_sha256=sha256(POLICY),
        actual_live_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        live_closeout_rejected=refusal,no_terminal_artifacts_written=not any(p.exists() for p in protected),
        historical_fixture_selected=len(fixture['selected']),historical_fixture_differences=len(fixture['legacy_score_differences_preserved']),
        changed_identical_historical_rating_rejected=changed_refusal,
        references=references,fixed_reference_priority=[r['name'] for r in references],
        candidate_additional_last_reference='Completed current static_half notes, for exact id/prefix/text/stop only; both current80 still individually read',
        historical_notes_changed=False,new_candidate160_read=0,GPU_seconds=0,
        Base_complete=False,Chat_started=False,quantization_started=False))
    print('Live paired closeout refused; fixed old80 lineage/changed-score refusal verified; current160 read0/GPU0')


def main():
    temporary=BUNDLE.with_suffix('.tmp')
    if any(path.exists() for path in (COMPLETION,MANIFEST,BUNDLE,REUSE,temporary)):
        raise ValueError('Preserve completed/interrupted archive; inspect before retrying')
    c,policy=load_policy();result=require_exited(c)
    preparation=read_json(PREPARATION)
    if (preparation['source']!=ref(Path(__file__)) or preparation['config_sha256']!=sha256(CONFIG)
            or preparation['policy_sha256']!=sha256(POLICY) or not preparation['no_terminal_artifacts_written']):
        raise ValueError('Prospective closeout/rating lineage evidence differs')
    review=read_json(REVIEW)
    if (review['config_sha256']!=sha256(CONFIG) or review['policy_sha256']!=sha256(POLICY)
            or review['result_sha256']!=sha256(RUN/'result.json') or review['GPU_seconds']!=result['GPU_occupancy_seconds']
            or review['scientific_CE_teacher_tokens']!=200000000 or review['all160_individually_read'] is not True
            or review['quality_criteria_unchanged'] is not True or any(review[k] is not False for k in
                ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
        raise ValueError('Complete original all160 content review required; no Base adoption here')
    eligible=(all(q['passed'] for q in review['quality_comparisons'].values())
        and all(review['absolute_dev_screen'].values()) and all(review['original_Web'].values()))
    if type(review['eligible_for_final_Base_validation']) is not bool or eligible!=review['eligible_for_final_Base_validation']:
        raise ValueError('All unchanged original quality gates must determine qualification')
    references=preparation['references'];history=load_history(references);reuse={}
    for arm in ARMS:
        trained=result['results'][arm]['training'];notes=read_json(notes_path(arm))
        if (trained['scientific_CE_teacher_tokens']!=100000000 or trained['gate_arm']!=arm
                or trained['gate_policy']!=GATE_POLICY or trained['spec']['kind']!=KIND
                or trained['spec']['optimizer_policy']!=OPT_KIND
                or trained['spec']['optimizer_recipe']!=json.loads(json.dumps(OPT_POLICY))
                or review['notes_sha256'][arm]!=sha256(notes_path(arm)) or notes['generation_sha256']!=sha256(raw_path(arm))):
            raise ValueError('Raw-bound completed exact100M gate arm required')
        reuse[arm]=dict(**rating_reuse(read_json(raw_path(arm))['outputs'],notes,history),
            raw=ref(raw_path(arm)),notes=ref(notes_path(arm)))
        if arm=='static_half':
            # Same current text receives the same score across arms after old priority.
            history.append(('current_static_half',{r['id']:r for r in read_json(raw_path(arm))['outputs']},
                {r[0]:r[1:5] for r in notes['notes']}))
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:model=json.load(response)
    if (not alive(ui) or model['busy'] or model['checkpoint_sha256']!=c['parent']['sha256']
            or model['training_tokens']!=10000007168):raise ValueError('Original idle10B UI actual identity/HTTP must be restored')
    launcher=PHASE/'base-headwise-gate-comparison-launcher-20261007'
    launched=read_json(launcher/'result.json')
    if launched.get('status')!='complete' or launched.get('exit_code')!=0:
        raise ValueError('Completed durable launcher required')
    required=('base_headwise_gate_proposal.json','base_headwise_gate_preparation_v2.json',
        'base_headwise_gate_parent_CPU_parity.json','base_headwise_gate_parent_CPU_preparation_initial_failure.json',
        'base_headwise_gate_CPU_tests_v2.xml','base_headwise_gate_model_tests.xml',
        'base_headwise_gate_model_tests_initial.xml','base_headwise_gate_trainer_tests_initial_failure.xml',
        'base_headwise_gate_workflow_tests.xml','base_headwise_gate_run_tests.xml',
        'base_headwise_gate_run_tests_initial_failure.xml','base_headwise_gate_workflow_preparation.json',
        'base_headwise_gate_probe_completion.json','base_headwise_gate_active_job.json')
    files=[CONFIG,POLICY,REVIEW,PREPARATION,Path(__file__),ROOT/'configs/phase6/base_headwise_gate_probe.json',
        *[PHASE/name for name in required],*[notes_path(a) for a in ARMS],
        *[launcher/name for name in ('launcher.json','result.json','stdout.log','stderr.log')]]
    for arm in ARMS:
        notes=read_json(notes_path(arm))
        if notes.get('observations'):
            observation=Path(notes['observations']['path']).resolve()
            if not observation.is_relative_to(PHASE.resolve()) or sha256(observation)!=notes['observations']['sha256']:
                raise ValueError('Individual observation identity differs')
            files.append(observation)
    for folder in (RUN,PHASE/'base-headwise-gate-probe-20261007',
            PHASE/'base-headwise-gate-probe-launcher-20261007',PHASE/'base-headwise-gate-preparation-v1'):
        files.extend(path for path in sorted(folder.rglob('*')) if path.is_file()
            and path.suffix in ('.json','.jsonl','.py','.ps1','.xml','.log','.lock','.txt'))
    files=list(dict.fromkeys(files))
    if any(not path.is_file() for path in files):raise ValueError('Required portable evidence missing; do not partially archive')
    atomic_json(REUSE,dict(created_at=now(),references=references,
        fixed_reference_priority=preparation['fixed_reference_priority'],arms=reuse,
        historical_notes_changed=False,all_current160_individually_read=True,independent_human_blind=False,GPU_seconds=0,
        scope='Exact text rating consistency, not independent human or new quality evaluation'))
    files.append(REUSE)
    entries=[dict(path=path.relative_to(ROOT).as_posix(),bytes=path.stat().st_size,sha256=sha256(path)) for path in files]
    atomic_json(MANIFEST,dict(created_at=now(),files=entries,tensor_or_corpus_included=False,full_checkpoints_preserved_native=True))
    with tarfile.open(temporary,'w:gz') as archive:
        for path in (*files,MANIFEST):archive.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(BUNDLE)
    record=dict(created_at=now(),status='paired_gate200M_review_complete_final_validation_pending' if eligible else 'paired_gate200M_review_complete_rejected',
        actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        scientific_CE_teacher_tokens=200000000,scientific_updates={a:result['results'][a]['training']['counters']['update'] for a in ARMS},
        checkpoints={a:dict(path=result['results'][a]['training']['checkpoint'],sha256=result['results'][a]['training']['checkpoint_sha256']) for a in ARMS},
        gate_policy=GATE_POLICY,optimizer_kind=OPT_KIND,optimizer_recipe=OPT_POLICY,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],GPU_cap_seconds=c['GPU_budget_seconds'],
        probe_GPU_seconds=c['probe_GPU_seconds'],total_GPU_seconds_including_probe=result['total_GPU_seconds_including_probe'],
        config_sha256=sha256(CONFIG),review=ref(REVIEW),notes={a:ref(notes_path(a)) for a in ARMS},
        exact_text_rating_reuse=ref(REUSE),all160_individually_read=True,independent_human_blind=False,
        reused_control_GPU_seconds=0,new_unique_corpus=0,added_physical_parameters_each=13312,
        study_parameters_each=10014464,summaries=review['summaries'],eligible_for_final_Base_validation=eligible,
        fixed_headwise_gate_condition_closed=not eligible,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        archive=dict(files=len(entries),bytes=sum(e['bytes'] for e in entries),manifest=ref(MANIFEST),
            compressed_bundle=dict(**ref(BUNDLE),bytes=BUNDLE.stat().st_size)),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_scored=False,final_seed_full_dev_test_adoption_pending=True,
        next_action='Qualified: independent learnedseed/fullDEV/protectedTEST/adoption before Base completion. Rejected: close fixed gate/init/gain/parent/source/LR/teacher/batch/backend/decoder/cap recipe without rescue. No Chat/quantization.')
    atomic_json(COMPLETION,record)
    print(json.dumps(dict(status=record['status'],GPU_seconds=record['GPU_occupancy_seconds'],archive_files=len(entries),UI_pid=ui['pid'])))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--prepare',action='store_true');args=parser.parse_args()
    prepare() if args.prepare else main()
