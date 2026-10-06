"""Actual source-quota learning and all160 content evidence, unchanged gates."""
import argparse
import json
import math
from pathlib import Path
import sys
import tarfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from run_eos_short_pilot import equal_state, rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
import run_story_weight_comparison as study


def notes_path(arm): return ROOT / f'reports/phase6/story_weight_{arm}_notes.json'


def point(arm, template=False):
    c, base, _ = study.inspect(study.CONFIG)
    result = read_json(study.RUN / 'progress-result.json')
    ev = result['evaluations'][arm]; trained = result['checkpoints'][arm]; rows = ev['generation']['outputs']
    if ev['checkpoint_sha256'] != trained['checkpoint_sha256'] or ev['binding'] != trained['binding']:
        raise ValueError('Evaluation/actual checkpoint differs')
    validate_rows(rows, Tokenizer(ROOT / base['tokenizer']))
    cases = {r['id']: r for r in (json.loads(s) for s in (ROOT / 'eval/base.jsonl').read_text().splitlines()) if r['split'] == 'dev'}
    if len(rows) != 80 or {r['id'] for r in rows} != set(cases) or any(r['prefix'] != cases[r['id']]['prefix'] for r in rows):
        raise ValueError('Fixed80 dev coverage differs')
    if ev['greedy_rates'] != rate(rows) or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']:
        raise ValueError('Raw rates/evaluation scope differs')
    raw = study.RUN / 'evaluation' / arm / 'evaluation/generation.json'
    if read_json(raw) != ev['generation']: raise ValueError('Raw generation differs')
    path = notes_path(arm)
    if template:
        if path.exists(): raise ValueError('Keep existing content notes')
        write_json(path, dict(reviewer='Codex nonblind; all80 individually read', independent_human_blind=False,
            generation_sha256=sha256(raw), notes=[[r['id'], None, None, None, None, ''] for r in rows]))
        return
    scores = validate_notes(rows, read_json(path), sha256(raw))
    body = ev['body']
    if (body['documents'] != len(body['rows']) or body['documents'] != 256 or body['body_bytes'] != 472055
            or body['body_tokens'] != 122343
            or any(r['body_tokens'] != r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'], sum(r['body_nll'] for r in body['rows']) / math.log(2) / 472055, rel_tol=1e-12)):
        raise ValueError('Common byte body scoring differs')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count'] != n for k, n in
           dict(semantics=192, jblimp=331, jcqa=1119).items()):
        raise ValueError('Japanese evaluation incomplete')
    summary = dict(BPB=body['bpb'], rates=ev['greedy_rates'],
        grammar2=sum(s['grammar'] == 2 for s in scores.values()), relevance2=sum(s['relevance'] == 2 for s in scores.values()),
        coherent=sum(s['coherence'] == 2 for s in scores.values()), appropriate=sum(s['completion'] for s in scores.values()),
        Japanese={k: ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics', 'jblimp', 'jcqa')},
        new_teacher_tokens=study.TOTAL, source_teacher_tokens=c['arms'][arm],
        generation_sha256=sha256(raw), notes_sha256=sha256(path), Base_adopted=False, independent_human_blind=False)
    write_json(study.RUN / (arm + '-content-review.json'), summary)
    return summary, scores


def audit():
    c, base, parent = study.inspect(study.CONFIG); job = read_json(study.RUN / 'job.json')
    result = read_json(study.RUN / 'compare-result.json'); probe = study.probe_evidence()
    if (job['status'] != 'complete' or alive(job) or result['config_sha256'] != sha256(study.CONFIG)
            or result['GPU_seconds'] != job['GPU_elapsed_seconds'] or job['GPU_elapsed_seconds'] > c['GPU_budget_seconds']
            or result['GPU_seconds'] + probe['GPU_seconds'] > study.CEILING
            or result['scientific_teacher_tokens'] != 2 * study.TOTAL or result['protected_test_used']
            or set(result['checkpoints']) != set(study.GOALS) or set(result['evaluations']) != set(study.GOALS)):
        raise ValueError('Actual learning terminal/budget/scope incomplete')
    summaries, scores, annotations = {}, {}, {}
    for arm in study.GOALS:
        record = result['checkpoints'][arm]; cp = Path(record['checkpoint']); study.check_reference(dict(path=str(cp), sha256=record['checkpoint_sha256']))
        state = torch.load(cp, map_location='cpu', weights_only=False)
        rows = [json.loads(s) for s in (study.RUN / arm / 'training/metrics.jsonl').read_text().splitlines()]
        sampler = state['sampler']
        if (not finite_state(state) or state['study_binding'] != record['binding']
                or state['study_binding'] != study.binding(c, study.CONFIG, arm)
                or state['supervised_tokens'] != parent['supervised_tokens'] + study.TOTAL
                or sampler['source_teachers'] != study.GOALS[arm]
                or not equal_state(state['lineage']['actual_parent_sampler'], parent['sampler'])
                or not equal_state(state['lineage']['parent_scheduler'], parent['scheduler'])
                or state['lineage']['parent'] != c['parent'] or not state['lineage']['no_reheat']
                or state['spec']['lr'] != .0002 or state['spec']['scheduler'] != 'wsd'
                or any(not math.isclose(g['lr'], .0002, rel_tol=1e-10) for g in state['optimizer']['param_groups'])):
            raise ValueError('Actual quota/parent/Adam schedule evidence differs')
        if (len(rows) != state['update'] - parent['update'] or len(rows) != sampler['position']
                or [r['update'] for r in rows] != list(range(parent['update'] + 1, state['update'] + 1))
                or any(not math.isfinite(r['loss']) or not math.isfinite(r['gradient_norm']) or r['lr'] != .0002 for r in rows)
                or rows[-1]['token_digest'] != state['token_digest']
                or rows[-1]['supervised_tokens'] != state['supervised_tokens']
                or state['tokens'] - parent['tokens'] != sum(sampler['source_tokens'].values())
                or state['tokens'] - parent['tokens'] != len(rows) * 32768
                or state['body_bytes'] - parent['body_bytes'] != sum(sampler['source_body_bytes'].values())
                or record['additional_supervised_tokens'] != study.TOTAL
                or record['additional_input_tokens'] != state['tokens'] - parent['tokens']):
            raise ValueError('Completed update/input/teacher/body-byte/digest evidence differs')
        summaries[arm], scores[arm] = point(arm)
        annotations[arm] = dict(notes=read_json(notes_path(arm))['notes'], notes_sha256=sha256(notes_path(arm)),
            generation_sha256=summaries[arm]['generation_sha256'])
    evs = result['evaluations']
    if ([(r['doc_id'], r['body_tokens'], r['body_bytes']) for r in evs['control']['body']['rows']]
            != [(r['doc_id'], r['body_tokens'], r['body_bytes']) for r in evs['story20']['body']['rows']]):
        raise ValueError('Heldout bytes/documents differ between arms')
    quality = quality_gates(evs['control'], evs['story20'], scores['control'], scores['story20'], 'content')
    absolute, original = {}, {}
    for arm, s in summaries.items():
        absolute[arm] = dict(grammar_at_least56=s['grammar2'] >= 56, coherence_at_least27=s['coherent'] >= 27,
            appropriate_at_least27=s['appropriate'] >= 27, EOS_at_least37=s['rates']['eos'] >= 37,
            repetition_at_most18=s['rates']['repetition'] <= 18,
            no_empty_role_unicode=all(s['rates'][k] == 0 for k in ('empty', 'role_leak', 'unicode_failure')))
        study.check_reference(base['reference']['web_screen'])
        original[arm] = adoption_checks(read_json(Path(base['reference']['web_screen']['path'])), evs[arm])
    write_json(study.RUN / 'annotations.json', dict(reviewer='Codex nonblind', independent_human_blind=False, arms=annotations))
    review = dict(status='same_material_story_weights_actual200M_all160_evidence_complete', summaries=summaries,
        quality_comparison=quality, absolute_dev_screen=absolute, original_Web=original,
        eligible_for_final_Base_validation={arm: all(absolute[arm].values()) and all(original[arm].values()) for arm in study.GOALS},
        new_scientific_teacher_tokens=2 * study.TOTAL, verification_teacher_tokens=probe['verification_teacher_tokens'],
        GPU_seconds=result['GPU_seconds'], verification_GPU_seconds=probe['GPU_seconds'],
        result_sha256=sha256(study.RUN / 'compare-result.json'), annotations_sha256=sha256(study.RUN / 'annotations.json'),
        Base_adopted=False, Chat_adopted=False, protected_test_used=False, independent_human_blind=False,
        quality_criteria_unchanged=True, old_numerical7_preserved=True, requested_five_steps_complete=False, created_at=now())
    write_json(study.RUN / 'review.json', review)
    write_json(ROOT / 'reports/phase6/story_weight_comparison_review.json', review)
    print(json.dumps(review, ensure_ascii=False), flush=True)


def archive():
    study.inspect(study.CONFIG); review = read_json(study.RUN / 'review.json'); job = read_json(study.RUN / 'job.json')
    if job['status'] != 'complete' or alive(job) or review['result_sha256'] != sha256(study.RUN / 'compare-result.json'):
        raise ValueError('Only completed raw-bound review can be archived')
    archive = ROOT / 'reports/phase6/story-weight-comparison-20261006_evidence.tar.gz'
    if archive.exists(): raise ValueError('Archive is immutable')
    paths = {p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in ('.json', '.jsonl', '.py', '.ps1', '.xml', '.lock')}
    paths.update((study.CONFIG, study.PROBE_CONFIG, study.PREPARATION, Path(__file__),
                  ROOT / 'reports/phase6/story_weight_comparison_tests.xml', *(notes_path(arm) for arm in study.GOALS)))
    entries = [dict(path=p.relative_to(ROOT).as_posix(), sha256=sha256(p), bytes=p.stat().st_size) for p in sorted(paths)]
    temporary = archive.with_suffix('.tmp')
    with tarfile.open(temporary, 'w:gz', compresslevel=1) as stream:
        for path in sorted(paths): stream.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(archive)
    write_json(ROOT / 'reports/phase6/story_weight_comparison_evidence_manifest.json', dict(entries=entries,
        text_files=len(entries), uncompressed_bytes=sum(e['bytes'] for e in entries),
        archive=dict(path=str(archive), sha256=sha256(archive), bytes=archive.stat().st_size), checkpoint_tensors_included=False))
    print(json.dumps(dict(archive=str(archive), sha256=sha256(archive))), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    p = argparse.ArgumentParser(); p.add_argument('--arm', choices=tuple(study.GOALS)); mode = p.add_mutually_exclusive_group()
    mode.add_argument('--template', action='store_true'); mode.add_argument('--point', action='store_true'); mode.add_argument('--archive', action='store_true')
    args = p.parse_args()
    if args.template or args.point:
        if not args.arm: p.error('--arm required for point/template')
        point(args.arm, args.template)
    elif args.archive: archive()
    else: audit()
