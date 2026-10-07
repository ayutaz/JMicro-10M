"""Archive exited fresh paired2B residual evidence and fixed ratings; no Base adoption."""
import argparse
from copy import deepcopy
import json
from pathlib import Path
import sys
import tarfile
import urllib.request

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from base_parallel_residual_model import ARMS, POLICY as RESIDUAL_POLICY
from base_parallel_residual_trainer import KIND
from base_parallel_residual_evaluation import validate_record
from review_base_parallel_residual import CONFIG, RUN, POLICY, load_policy, notes_path, raw_path, audit_terminal
from complete_base_headwise_gate import ref, checked, load_history, rating_reuse
from base_output_mixture_model import ARMS as PREVIOUS_ARMS
from probe_base_parallel_residual import passed_tests

PHASE = ROOT / 'reports/phase6'
PREPARATION = PHASE / 'base_parallel_residual_closeout_preparation.json'
REVIEW = PHASE / 'base_parallel_residual_comparison_review.json'
COMPLETION = PHASE / 'base_parallel_residual_comparison_completion.json'
MANIFEST = PHASE / 'base_parallel_residual_comparison_evidence_manifest.json'
BUNDLE = PHASE / 'base_parallel_residual_comparison_evidence.tar.gz'
REUSE = PHASE / 'base_parallel_residual_rating_reuse.json'
HELPER = ROOT / 'scripts/complete_base_headwise_gate.py'
PRIORITY = ['cached_CE', 'middle_supervision', 'sam', 'on_policy_teacher',
            'confidence_penalty', 'native_teacher_KD', 'native_hint', 'sigsoftmax', 'ademamix',
            'headwise_static_half', 'headwise_query_headwise']


def qualification(review):
    if (set(review['quality_comparisons']) != {'new_sequential', 'strong', 'cached_native'}
            or set(review['absolute_dev_screen']) != {'grammar_at_least56', 'coherence_at_least27',
                'appropriate_at_least27', 'EOS_at_least37', 'repetition_at_most18', 'no_empty_role_unicode'}
            or set(review['original_Web']) != {'EOS_at_least8_more', 'repetition_no_worse',
                'no_empty_role_unicode', 'BPB_degradation_at_most1percent', 'no_punctuation_only_stops'}):
        raise ValueError('Every original matched/strong/cached/absolute/historical guard required')
    values = [*[v['passed'] for v in review['quality_comparisons'].values()],
              *review['absolute_dev_screen'].values(), *review['original_Web'].values()]
    if any(type(v) is not bool for v in values):
        raise ValueError('Actual boolean original quality decisions required')
    eligible = all(values)
    if type(review['eligible_for_final_Base_validation']) is not bool or eligible != review['eligible_for_final_Base_validation']:
        raise ValueError('Unchanged full conjunction must determine qualification')
    return eligible


def validate_completed_arm(c, arm, trained):
    validate_record(arm, trained)
    expected_class = 'ParallelResidualModel' if arm == 'parallel' else 'JMicroModel'
    if (trained['status'] != 'complete' or trained['scientific_CE_teacher_tokens'] != 2000000000
            or trained['counters']['supervised_tokens'] != 2000000000
            or trained['counters']['source_teachers'] != c['goals']
            or trained['model_config'] != c['variants'][arm]
            or trained['residual_model_class'] != expected_class or trained['residual_policy'] != RESIDUAL_POLICY
            or trained['spec']['kind'] != KIND or trained['spec']['actual_unique_parameters'] != 10001152
            or trained['scheduler']['tokens'] != 2000000000 or trained['scheduler']['last_lr'] != c['optimizer']['final_lr']
            or trained['lineage']['parent'] is not None
            or trained['lineage']['learned_parent_weights_used'] is not False
            or trained['lineage']['probe_weights_used'] is not False):
        raise ValueError('Exact fresh same10M each2B terminal required')


def require_exited(c):
    job = read_json(RUN / 'job.json')
    if alive(job) or job['status'] != 'complete':
        raise ValueError('Scientific process must finish and exit before archive')
    result = read_json(RUN / 'result.json')
    audit_terminal(job, result, c, sha256(CONFIG), False)
    if (not all(result['common_CE_checks'].values()) or result['cached_CE_stream_matched'] is not False):
        raise ValueError('Exact fresh paired2B stream and explicitly quality-only mature100M reference required')
    return result


def prepare():
    if PREPARATION.exists():
        raise ValueError('Preserve prospective closeout preparation')
    c, _ = load_policy()
    tests = PHASE / 'base_parallel_residual_closeout_tests.xml'
    passed_tests(tests, 4)
    job = read_json(RUN / 'job.json')
    if not alive(job) or job['status'] != 'running':
        raise ValueError('Same actual science process must be live')
    if any(p.exists() for p in (COMPLETION, MANIFEST, BUNDLE, REUSE, *(raw_path(a) for a in ARMS))):
        raise ValueError('Fix rating lineage before current generation outcomes')
    try:
        require_exited(c)
    except ValueError as error:
        refusal = str(error)
        if refusal != 'Scientific process must finish and exit before archive':
            raise
    else:
        raise ValueError('Live science accepted as complete')
    previous = read_json(PHASE / 'base_output_mixture_comparison_completion.json')
    old = checked(previous['exact_text_rating_reuse'])
    references = deepcopy(old['references'])
    if old['fixed_reference_priority'] != PRIORITY or [r['name'] for r in references] != PRIORITY:
        raise ValueError('Historical rating priority differs')
    for arm in PREVIOUS_ARMS:
        references.append(dict(name='output_' + arm, raw=old['arms'][arm]['raw'], notes=old['arms'][arm]['notes']))
    history = load_history(references)
    rows, notes = checked(references[0]['raw'])['outputs'], checked(references[0]['notes'])
    fixture = rating_reuse(rows, notes, history)
    if len(fixture['selected']) != 80:
        raise ValueError('Historical80 rating consistency fixture failed')
    edited = deepcopy(notes)
    edited['notes'][0][1] = (edited['notes'][0][1] + 1) % 3
    try:
        rating_reuse(rows, edited, history)
    except ValueError as error:
        if not str(error).startswith('Previously rated identical text score differs: '):
            raise
    else:
        raise ValueError('Changed identical historical rating accepted')
    atomic_json(PREPARATION, dict(created_at=now(), source=ref(Path(__file__)), helper=ref(HELPER),
        CPU_tests=ref(tests), test_source=ref(ROOT / 'tests/test_base_parallel_residual_closeout.py'),
        config_sha256=sha256(CONFIG), policy_sha256=sha256(POLICY),
        status='closeout_prepared_not_completion', actual_live_identity={k: job[k] for k in ('pid', 'boot_id', 'start_ticks')},
        references=references, fixed_reference_priority=[r['name'] for r in references],
        live_closeout_rejected=refusal, historical_fixture_selected=80,
        historical_fixture_differences=len(fixture['legacy_score_differences_preserved']),
        changed_identical_historical_rating_rejected=True, historical_notes_changed=False,
        current_candidate_additional_last_reference='Completed current sequential2B notes; exact id/prefix/text/stop only, both current80 individually read',
        current160_individually_read=0, GPU_seconds=0, Base_complete=False, Chat_started=False, quantization_started=False))
    print('Live closeout refused; historical80/changed-score refusal verified; current160 read0/GPU0')


def main():
    temporary = BUNDLE.with_suffix('.tmp')
    if any(p.exists() for p in (COMPLETION, MANIFEST, BUNDLE, REUSE, temporary)):
        raise ValueError('Preserve previous or interrupted closeout; inspect before retrying')
    c, _ = load_policy()
    result = require_exited(c)
    prep = read_json(PREPARATION)
    if (prep['source'] != ref(Path(__file__)) or prep['helper'] != ref(HELPER)
            or prep['CPU_tests'] != ref(PHASE / 'base_parallel_residual_closeout_tests.xml')
            or prep['test_source'] != ref(ROOT / 'tests/test_base_parallel_residual_closeout.py')
            or prep['config_sha256'] != sha256(CONFIG) or prep['policy_sha256'] != sha256(POLICY)):
        raise ValueError('Prospective closeout evidence changed')
    review = read_json(REVIEW)
    if (review['config_sha256'] != sha256(CONFIG) or review['policy_sha256'] != sha256(POLICY)
            or review['result_sha256'] != sha256(RUN / 'result.json')
            or review['GPU_seconds'] != result['GPU_occupancy_seconds']
            or review['scientific_CE_teacher_tokens'] != 4000000000
            or review['all160_individually_read'] is not True or review['quality_criteria_unchanged'] is not True
            or any(review[k] is not False for k in ('Base_complete', 'Base_adopted', 'Chat_started', 'quantization_started', 'protected_test_scored'))):
        raise ValueError('Full unchanged raw-bound all160 review required')
    eligible = qualification(review)
    history, reuse = load_history(prep['references']), {}
    for arm in ARMS:
        trained, notes = result['results'][arm]['training'], read_json(notes_path(arm))
        validate_completed_arm(c, arm, trained)
        if (review['notes_sha256'][arm] != sha256(notes_path(arm))
                or notes['generation_sha256'] != sha256(raw_path(arm))):
            raise ValueError('Raw-bound fresh each2B residual contents required')
        rows = read_json(raw_path(arm))['outputs']
        reuse[arm] = dict(**rating_reuse(rows, notes, history), raw=ref(raw_path(arm)), notes=ref(notes_path(arm)))
        history.append(('current_' + arm, {r['id']: r for r in rows}, {r[0]: r[1:5] for r in notes['notes']}))
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=10) as response:
        model = json.load(response)
    original = checked(c['evaluation_reference_config'])['parent']
    if not alive(ui) or model['busy'] or model['checkpoint_sha256'] != original['sha256'] or model['training_tokens'] != 10000007168:
        raise ValueError('Original idle10B UI must be restored')
    launcher = PHASE / 'base-parallel-residual-comparison-launcher-20261007'
    launched = read_json(launcher / 'result.json')
    if launched.get('status') != 'complete' or launched.get('exit_code') != 0:
        raise ValueError('Completed durable launcher required')
    files = [CONFIG, POLICY, REVIEW, PREPARATION, Path(__file__), HELPER, *[notes_path(a) for a in ARMS]]
    correction = checked(c['validator_correction'])
    files.append(Path(correction['old_trainer']['path']))
    files.append(PHASE / 'base-parallel-residual-probe-20261007/source/tests/test_base_parallel_residual_trainer.py')
    files.append(ROOT / 'tests/test_base_parallel_residual_closeout.py')
    files.extend(ROOT / name for name in c['source_sha256'])
    files.extend(PHASE.glob('base_parallel_residual*.json'))
    files.extend(PHASE.glob('base_parallel_residual*.xml'))
    for arm in ARMS:
        observation = read_json(notes_path(arm)).get('observations')
        if observation:
            path = Path(observation['path']).resolve()
            if not path.is_relative_to(PHASE.resolve()) or sha256(path) != observation['sha256']:
                raise ValueError('Individual observation identity differs')
            files.append(path)
    for folder in (RUN, launcher, PHASE / 'base-parallel-residual-probe-20261007', PHASE / 'base-parallel-residual-probe-launcher-20261007'):
        files.extend(p for p in sorted(folder.rglob('*')) if p.is_file() and p.suffix in ('.json', '.jsonl', '.xml', '.log', '.txt'))
    files = list(dict.fromkeys(files))
    if any(not p.is_file() for p in files):
        raise ValueError('Required evidence missing; no partial archive')
    atomic_json(REUSE, dict(created_at=now(), references=prep['references'], fixed_reference_priority=prep['fixed_reference_priority'],
        arms=reuse, historical_notes_changed=False, all_current160_individually_read=True, independent_human_blind=False, GPU_seconds=0))
    files.append(REUSE)
    entries = [dict(path=p.relative_to(ROOT).as_posix(), bytes=p.stat().st_size, sha256=sha256(p)) for p in files]
    atomic_json(MANIFEST, dict(created_at=now(), files=entries, tensor_or_corpus_included=False, full_checkpoints_preserved_native=True))
    with tarfile.open(temporary, 'w:gz', compresslevel=1) as archive:
        for path in (*files, MANIFEST):
            archive.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(BUNDLE)
    atomic_json(COMPLETION, dict(created_at=now(), status='fresh_paired_residual4B_review_complete',
        actual_identity=result['actual_identity'], actual_process_absent_verified=True, scientific_CE_teacher_tokens=4000000000,
        checkpoints={a: dict(path=result['results'][a]['training']['checkpoint'], sha256=result['results'][a]['training']['checkpoint_sha256']) for a in ARMS},
        residual_policy=RESIDUAL_POLICY, study_parameters_each=10001152, added_physical_parameters_each=0,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'], GPU_cap_seconds=c['GPU_budget_seconds'],
        total_GPU_seconds_including_probe=result['total_GPU_seconds_including_probe'], config_sha256=sha256(CONFIG),
        review=ref(REVIEW), exact_text_rating_reuse=ref(REUSE), summaries=review['summaries'],
        eligible_for_final_Base_validation=eligible, fixed_parallel_residual_condition_closed=not eligible,
        archive=dict(files=len(entries), bytes=sum(e['bytes'] for e in entries), manifest=ref(MANIFEST), bundle=ref(BUNDLE)),
        UI_restored=dict(identity={k: ui[k] for k in ('pid', 'boot_id', 'start_ticks')}, actual_alive=True, model=model),
        all160_individually_read=True, independent_human_blind=False, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_scored=False, quality_criteria_unchanged=True,
        next_action='Only a qualified candidate proceeds to independent learnedseed/fullDEV/protectedTEST/adoption; otherwise close this fixed recipe without tuning rescue. No Chat or quantization.'))
    print(json.dumps(dict(eligible=eligible, GPU_seconds=result['GPU_occupancy_seconds'], archive_files=len(entries))))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare', action='store_true')
    args = parser.parse_args()
    prepare() if args.prepare else main()
