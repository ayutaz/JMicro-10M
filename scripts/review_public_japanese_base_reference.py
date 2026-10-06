"""Foreign codec audit, complete80 content scores, and bounded reference closeout."""
import csv
import json
from pathlib import Path
import statistics
import sys
import tarfile
import time
from urllib.request import urlopen

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from run_public_japanese_base_reference import RUN, PLAN, RECOVERY, load_inputs
from review_textbook_quantity_comparison import validate_notes

OBSERVATIONS = ROOT / 'reports/phase6/public_japanese_base_reference_observations.tsv'
NOTES = ROOT / 'reports/phase6/public_japanese_base_reference_notes.json'
REVIEW = ROOT / 'reports/phase6/public_japanese_base_reference_review.json'
MANIFEST = ROOT / 'reports/phase6/public_japanese_base_reference_evidence_manifest.json'
ARCHIVE = ROOT / 'reports/phase6/public_japanese_base_reference_evidence.tar.gz'
CONTROL = ROOT / 'reports/phase6/natural-context-contrast-comparison-20261007/evaluation/CE/evaluation/generation.json'


def lengths(rows, ids_key):
    return dict(body_characters=sum(len(r['text']) for r in rows),
        body_utf8_bytes=sum(len(r['text'].encode()) for r in rows),
        median_characters=statistics.median(len(r['text']) for r in rows),
        emitted_token_positions=sum(len(r[ids_key]) for r in rows))


def main():
    started = time.monotonic()
    if REVIEW.exists(): raise ValueError('Preserve completed reference review')
    p, job, result = read_json(PLAN), read_json(RUN / 'job.json'), read_json(RUN / 'result.json')
    recovery, tokenizer, cases, suppressed = load_inputs()
    if (alive(job) or job['status'] != 'complete' or result['status'] != 'complete' or
            job['plan_sha256'] != result['plan_sha256'] or result['plan_sha256'] != sha256(PLAN) or
            result['actual_identity'] != {k: job[k] for k in ('pid', 'boot_id', 'start_ticks')} or
            not 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= 180 or
            result['optimizer_updates'] or result['student_training_tokens'] or result['protected_test_scored'] or
            cases != p['cases'] or result['generation_sha256'] != sha256(RUN / 'generation.json')):
        raise ValueError('Bounded exited full80 reference evidence required')
    rows = read_json(RUN / 'generation.json')
    if len(rows) != 80 or [r['id'] for r in rows] != [c['id'] for c in cases]:
        raise ValueError('Exactly original DEV80 required')
    for row, case in zip(rows, cases):
        ids = row['generated_ids']
        if (row['prefix'] != case['prefix'] or row['input_ids'] != case['input_ids'] or
                row['normalized_prefix'] != case['normalized_prefix'] or
                not 0 < len(ids) <= 64 or any(type(i) is not int or i < 0 or i >= 32000 or i in suppressed for i in ids) or
                p['EOS'] in ids[:-1] or row['EOS'] != (ids[-1] == p['EOS'])):
            raise ValueError('Raw original-prefix/foreign token accounting differs')
        body = ids[:-1] if row['EOS'] else ids
        if (tokenizer.decode(body, skip_special_tokens=False, clean_up_tokenization_spaces=False) != row['text'] or
                tokenizer.decode(ids, skip_special_tokens=False, clean_up_tokenization_spaces=False) != row['raw_decoded_with_EOS'] or
                row['generated_tokens'] != len(ids) or row['body_tokens'] != len(body) or
                row['utf8_bytes'] != len(row['text'].encode()) or row['characters'] != len(row['text']) or
                row['stopped_by'] != ('stop_id' if row['EOS'] else 'max_tokens')):
            raise ValueError('Foreign decoder/length/stop reconstruction differs')
    with OBSERVATIONS.open(encoding='utf-8', newline='') as handle:
        observed = list(csv.DictReader(handle, delimiter='\t'))
    notes = dict(created_at=now(), reviewer='Codex nonblind; all80 individually read', independent_human_blind=False,
        generation_sha256=result['generation_sha256'], observations_sha256=sha256(OBSERVATIONS),
        notes=[[r['id'], *[int(r[k]) for k in ('grammar', 'relevance', 'coherence', 'completion')], r['rationale']] for r in observed])
    scores = validate_notes([dict(**r, stop_reason=r['stopped_by']) for r in rows], notes, result['generation_sha256'])
    atomic_json(NOTES, notes)
    summary = dict(grammar2=sum(s['grammar'] == 2 for s in scores.values()),
        relevance2=sum(s['relevance'] == 2 for s in scores.values()), coherent=sum(s['coherence'] == 2 for s in scores.values()),
        appropriate=sum(s['completion'] for s in scores.values()), EOS=sum(r['EOS'] for r in rows),
        repetition=sum(r['repetition'] for r in rows),
        **{k: sum(r[k] for r in rows) for k in ('empty', 'unicode_failure', 'role_leak')})
    old_review = read_json(ROOT / 'reports/phase6/base_next_two_token_comparison_review.json')
    control = read_json(CONTROL)['outputs']
    if (sha256(CONTROL) != old_review['summaries']['CE']['generation_sha256'] or
            {r['id']: r['prefix'] for r in control} != {r['id']: r['prefix'] for r in rows}):
        raise ValueError('Cached actual native control differs')
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    with urlopen('http://127.0.0.1:7860/api/model', timeout=3) as handle:
        model = json.load(handle)
    expected_parent = '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
    if (not alive(ui) or model['checkpoint_sha256'] != expected_parent or
            model['training_tokens'] != 10000007168 or model['busy'] or
            ui['model']['checkpoint_sha256'] != expected_parent):
        raise ValueError('Original native10B UI must actually be restored')
    absolute = dict(grammar_at_least56=summary['grammar2'] >= 56, coherence_at_least27=summary['coherent'] >= 27,
        appropriate_at_least27=summary['appropriate'] >= 27, EOS_at_least37=summary['EOS'] >= 37,
        repetition_at_most18=summary['repetition'] <= 18,
        no_empty_role_unicode=all(summary[k] == 0 for k in ('empty', 'unicode_failure', 'role_leak')))
    review = dict(status='public_Japanese_Base_reference_all80_read_and_closed', created_at=now(),
        repository=p['repository'], revision=p['revision'], actual_parameters=p['actual_parameters'],
        native_parameters=10001152, actual_identity=result['actual_identity'], actual_process_absent=True,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'], plan_sha256=sha256(PLAN),
        result_sha256=sha256(RUN / 'result.json'), generation_sha256=sha256(RUN / 'generation.json'),
        notes_sha256=sha256(NOTES), observations_sha256=sha256(OBSERVATIONS), all80_individually_read=True,
        foreign_codec_reconstruction_all80_passed=True, rubric='Existing grammar/relevance/coherence/completion; stop_id alone is not appropriate completion.',
        foreign_summary=summary, foreign_lengths=lengths(rows, 'generated_ids'),
        native_CE_cached_summary=old_review['summaries']['CE'], native_CE_lengths=lengths(control, 'generated_ids'),
        native_control_generation_sha256=sha256(CONTROL), native_control_GPU_rerun_seconds=0,
        foreign_absolute_generation_screen=absolute, reference_passes_generation_screen=all(absolute.values()),
        prefix_normalization_changed=p['normalization_changed'], prefix_UNK_tokens=p['prefix_UNK_tokens'],
        interpretation='This separately pretrained Japanese Base also repeats frequently under this single BOS/plain/greedy64-foreign-token protocol. It does not establish a native training bug or a10M capacity ceiling. No native training improvement or adoption is measured.',
        limitations=p['limitations'] + ' Foreign64 tokens produce a different byte length; not matched continuation length. Only generation is compared, no foreign BPB/Japanese choice scores. No independent human review.',
        decision='Close this one reference without model/prompt/decoder/token-budget rescue. Preserve native quality gates and prior rejected branches.',
        original_UI=dict(actual_identity={k: ui[k] for k in ('pid', 'boot_id', 'start_ticks')}, HTTP=model),
        student_optimizer_updates=0, student_new_training_tokens=0, protected_test_scored=False,
        eligible_for_final_Base_validation=False, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, quality_criteria_unchanged=True,
        CPU_review_wall_seconds=time.monotonic() - started)
    atomic_json(REVIEW, review)
    paths = [OBSERVATIONS, NOTES, REVIEW, PLAN, RUN / 'job.json', RUN / 'result.json', RUN / 'generation.json',
             RECOVERY / 'job.json', RECOVERY / 'proposal.json', RECOVERY / 'result.json',
             ROOT / 'scripts/prepare_public_japanese_base_reference.py', ROOT / 'scripts/run_public_japanese_base_reference.py',
             ROOT / 'scripts/run_public_japanese_base_reference.ps1', Path(__file__)]
    archive_files = [dict(path=str(path.relative_to(ROOT)).replace('\\', '/'), sha256=sha256(path), bytes=path.stat().st_size) for path in paths]
    atomic_json(MANIFEST, dict(created_at=now(), files=archive_files, model_weights_in_archive=False, model_weight_recovery=read_json(RECOVERY / 'result.json')))
    with tarfile.open(ARCHIVE, 'w:gz') as archive:
        for path in [*paths, MANIFEST]: archive.add(path, arcname=str(path.relative_to(ROOT)))
    print(json.dumps(dict(summary=summary, foreign_lengths=review['foreign_lengths'], native_lengths=review['native_CE_lengths'],
        GPU_seconds=result['GPU_occupancy_seconds'], archive_bytes=ARCHIVE.stat().st_size, archive_sha256=sha256(ARCHIVE), Base_complete=False), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
