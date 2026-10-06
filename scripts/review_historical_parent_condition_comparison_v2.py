"""Raw-bound all320 content, exact completed teacher accounting and unchanged gates."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive, finite_state
from run_eos_short_pilot import equal_state, rate
from review_eos_5b_finish import validate_rows
from review_textbook_quantity_comparison import validate_notes
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks
import run_historical_parent_condition_comparison_v2 as study

POINTS = ('control', study.ARM)


def notes_path(arm):
    return ROOT / 'reports/phase6/original_web_retention_notes.json' if arm == 'control' else ROOT / 'reports/phase6/historical_parent_condition_notes.json'


def point(arm, base, record, ev, template=False):
    raw = study.previous.RUN / 'evaluation/original_web/evaluation/generation.json' if arm == 'control' else study.RUN / f'evaluation/{arm}/evaluation/generation.json'
    rows = ev['generation']['outputs']
    if (ev['binding'] != record['binding'] or ev['checkpoint_sha256'] != record['checkpoint_sha256']
            or read_json(raw) != ev['generation'] or ev['greedy_rates'] != rate(rows)
            or ev['protected_test_used'] or not ev['evaluation_RNG_isolated']):
        raise ValueError('Actual raw generation/binding required')
    validate_rows(rows, Tokenizer(ROOT / base['tokenizer']))
    cases = {r['id']:r for r in (json.loads(s) for s in (ROOT / 'eval/base.jsonl').read_text().splitlines()) if r['split'] == 'dev'}
    if len(rows) != 80 or {r['id'] for r in rows} != set(cases) or any(r['prefix'] != cases[r['id']]['prefix'] for r in rows):
        raise ValueError('Fixed originaldev80 differs')
    if template:
        path = notes_path(arm)
        if path.exists(): raise ValueError('Preserve existing notes')
        atomic_json(path, dict(reviewer='Codex nonblind; all80 individually read', independent_human_blind=False,
            generation_sha256=sha256(raw), notes=[[r['id'],None,None,None,None,''] for r in rows]))
        return
    scores = validate_notes(rows, read_json(notes_path(arm)), sha256(raw)); body = ev['body']
    if (body['documents'] != 256 or len(body['rows']) != 256 or body['body_bytes'] != 472055 or body['body_tokens'] != 122343
            or any(r['body_tokens'] != r['scored_body_tokens'] or not math.isfinite(r['body_nll']) for r in body['rows'])
            or not math.isclose(body['bpb'], sum(r['body_nll'] for r in body['rows']) / math.log(2) / 472055, rel_tol=1e-12)):
        raise ValueError('Common-byte full256 body dev required')
    if any(not ev['diagnostics'][k]['complete'] or ev['diagnostics'][k]['count'] != n for k,n in dict(semantics=192,jblimp=331,jcqa=1119).items()):
        raise ValueError('All Japanese diagnostics required')
    return dict(BPB=body['bpb'], rates=ev['greedy_rates'], grammar2=sum(v['grammar']==2 for v in scores.values()),
        relevance2=sum(v['relevance']==2 for v in scores.values()), coherent=sum(v['coherence']==2 for v in scores.values()),
        appropriate=sum(v['completion'] for v in scores.values()), generation_sha256=sha256(raw), notes_sha256=sha256(notes_path(arm)),
        Japanese={k:ev['diagnostics'][k]['primary']['accuracy']['point'] for k in ('semantics','jblimp','jcqa')},
        additional_teacher_tokens=record['additional_supervised_tokens'], independent_human_blind=False), scores


def accounting(parent, state, history, goals):
    sampler = state['sampler']
    if (not finite_state(state) or sampler['source_teachers'] != goals
            or state['supervised_tokens'] - parent['supervised_tokens'] != sum(goals.values())
            or state['lineage']['parent_update'] != parent['update'] or state['lineage']['parent_tokens'] != parent['tokens']
            or state['lineage']['parent_supervised_tokens'] != parent['supervised_tokens']
            or state['lineage']['parent_body_bytes'] != parent['body_bytes']
            or not equal_state(state['lineage']['actual_parent_sampler'], parent['sampler'])
            or not equal_state(state['lineage']['parent_scheduler'], parent['scheduler'])
            or not state['lineage']['no_reheat'] or state['spec']['research_kind'] != study.KIND
            or state['spec']['outcome_weight'] != 1 or state['spec']['lr'] != .00001
            or any(not math.isclose(g['lr'], .00001, rel_tol=1e-10) for g in state['optimizer']['param_groups'])):
        raise ValueError('Actual inherited finite fullstate differs')
    if (len(history) != sampler['position'] or len(history) != state['update'] - parent['update']
            or [r['update'] for r in history] != list(range(parent['update']+1, state['update']+1))
            or not history or any(not math.isfinite(r['loss']) or not math.isfinite(r['gradient_norm']) or r['lr'] != .00001 for r in history)
            or history[-1]['token_digest'] != state['token_digest'] or history[-1]['focus_token_digest'] != state['focus_token_digest']
            or state['tokens'] - parent['tokens'] != len(history) * state['spec']['batch'] * state['spec']['context']
            or state['tokens'] - parent['tokens'] != sum(sampler['source_tokens'].values())
            or state['body_bytes'] - parent['body_bytes'] != sum(sampler['source_body_bytes'].values())
            or state['weighted_teacher_mass'] != sum(goals.values()) or state['focus_teacher_tokens'] != sum(sampler['source_focus_teachers'].values())
            or any(sampler[key][g] for g,n in goals.items() if not n for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'))):
        raise ValueError('Completed history or inactive-source accounting differs')


def retained_sources(parent, state, control):
    sampler, other = state['sampler'], control['sampler']
    for source in ('story', 'ordinary_textbook', 'conditional_textbook'):
        if not equal_state(sampler['streams'][source], other['streams'][source]):
            raise ValueError('Unchanged short source terminal cursor differs')
        for key in ('source_teachers', 'source_eos', 'source_tokens', 'source_body_bytes', 'source_focus_teachers'):
            if sampler[key][source] != other[key][source]:
                raise ValueError('Unchanged short source accounting differs')
    web = sampler['streams']['web']
    if (web['kind'] != 'actual-parent-Web-block-cursor-v1'
            or web['manifest_sha256'] != parent['shard_manifest_sha256']):
        raise ValueError('Actual original Web source differs')
    initial, final = study.historical_web_cursor(parent), web['sampler']
    if any(initial[key] != final[key] for key in ('seed', 'context', 'blocks')):
        raise ValueError('Original Web sampler recipe differs')
    delta = ((final['epoch'] - initial['epoch']) * initial['blocks']
             + final['position'] - initial['position'])
    if delta < 0 or delta * initial['context'] != sampler['source_tokens']['web']:
        raise ValueError('Actual original Web cursor advance differs')
    return dict(short_source_cursors_and_accounting_equal=True,
                original_Web_cursor_retained=True, Web_blocks_consumed=delta)


def audit(template=False):
    c, base, parent, control, control_ev, _, _ = study.inspect(study.CONFIG)
    path = study.RUN / ('progress-result.json' if template else 'compare-result.json')
    r = read_json(path)
    if set(r['evaluations']) != set(POINTS):
        raise ValueError('New and cached control evaluations required')
    if template:
        point(study.ARM, base, r['checkpoints'][study.ARM], r['evaluations'][study.ARM], True)
        return
    job, probe = read_json(study.RUN / 'job.json'), study.probe_evidence()
    if (job['status'] != 'complete' or alive(job) or r['config_sha256'] != sha256(study.CONFIG)
            or r['GPU_seconds'] != job['GPU_elapsed_seconds']
            or r['GPU_seconds'] + probe['GPU_seconds'] + c['failed_probe_GPU_seconds'] > study.CEILING
            or r['scientific_teacher_tokens'] != study.TOTAL or r['total_comparison_teachers'] != 2 * study.TOTAL
            or r['checkpoints']['control'] != control or r['evaluations']['control'] != control_ev
            or not r['reused_control'] or r['protected_test_used'] or r['Base_adopted']
            or r['Chat_started'] or r['quantization_started']):
        raise ValueError('Terminal bounded Base-only new100M and reused100M required')
    record = r['checkpoints'][study.ARM]
    study.check_reference(dict(path=record['checkpoint'], sha256=record['checkpoint_sha256']))
    state = torch.load(record['checkpoint'], map_location='cpu', weights_only=False)
    history = [json.loads(s) for s in (study.RUN / study.ARM / 'training/metrics.jsonl').read_text().splitlines()]
    accounting(parent, state, history, study.GOALS)
    if (state['study_binding'] != study.binding(c, study.CONFIG) or state['study_binding'] != record['binding']
            or state['lineage']['parent'] != c['parent'] or record['additional_supervised_tokens'] != study.TOTAL
            or record['additional_input_tokens'] != state['tokens'] - parent['tokens']
            or state['spec']['original_web_manifest_sha256'] != c['original_web']['manifest_sha256']
            or state['spec']['historical_trainer_sha256'] != c['source_sha256']['scripts/historical_parent_condition_trainer.py']):
        raise ValueError('Completed fork identity differs')
    study.check_reference(c['reused_control_checkpoint'])
    previous_state = torch.load(control['checkpoint'], map_location='cpu', weights_only=False)
    retained = retained_sources(parent, state, previous_state)
    del state, previous_state
    summaries, scores = {}, {}
    for arm in POINTS:
        summaries[arm], scores[arm] = point(arm, base, r['checkpoints'][arm], r['evaluations'][arm])
    old = read_json(Path(c['references']['control_review']['path']))['summaries']['original_web']
    if summaries['control'] != old:
        raise ValueError('Reviewed original Web control changed')
    study.check_reference(base['reference']['web_screen'])
    web = read_json(Path(base['reference']['web_screen']['path']))
    targets = lambda ev: [(v['doc_id'], v['body_tokens'], v['body_bytes']) for v in ev['body']['rows']]
    if any(targets(ev) != targets(web) for ev in r['evaluations'].values()):
        raise ValueError('Common-byte targets differ')
    comparison = quality_gates(control_ev, r['evaluations'][study.ARM], scores['control'], scores[study.ARM], 'content')
    s = summaries[study.ARM]
    absolute = dict(grammar_at_least56=s['grammar2'] >= 56, coherence_at_least27=s['coherent'] >= 27,
                    appropriate_at_least27=s['appropriate'] >= 27, EOS_at_least37=s['rates']['eos'] >= 37,
                    repetition_at_most18=s['rates']['repetition'] <= 18,
                    no_empty_role_unicode=all(s['rates'][k] == 0 for k in ('empty', 'role_leak', 'unicode_failure')))
    original = adoption_checks(web, r['evaluations'][study.ARM])
    reused = read_json(study.previous.RUN / 'compare-result.json')
    for suite, key in (('bridge', 'transfer'), ('retention', 'retention')):
        records = r[key]
        if (set(records) != {'control', study.ARM}
                or records['control'] != reused[key]['original_web']):
            raise ValueError('Raw cached original control128 differs')
        case_key = 'source_cases' if suite == 'bridge' else 'retention_cases'
        prepared = read_json(Path(c['references'][case_key]['path']))
        t = records[study.ARM]
        if (t['config_sha256'] != sha256(study.CONFIG) or t['checkpoint_sha256'] != record['checkpoint_sha256']
                or t['cases_sha256'] != c['references'][case_key]['sha256'] or not all(t['checks'].values())
                or t['evaluated_requests'] != 512 or t['optimizer_updates'] or t['scientific_teacher_tokens'] or t['protected_test_used']):
            raise ValueError('Read-only128 binding differs')
        rows = []
        for start in range(0, 512, 16):
            batch = read_json(study.RUN / f'transfer/{suite}/{study.ARM}/{start:04d}.json')
            if any(batch[k] != t[k] for k in ('config_sha256', 'checkpoint_sha256', 'cases_sha256')):
                raise ValueError('Raw transfer batch differs')
            study.ranking.validate_scores(batch['rows'], prepared['cases'][start:start+16])
            rows.extend(batch['rows'])
        if t['summary'] != study.summarize_transfer(rows, prepared):
            raise ValueError('Raw transfer aggregation differs')
    report = dict(status='historical_parent100M_all80_and_reused_original10B_route100M_reviewed', created_at=now(),
        summaries=summaries, primary_comparison='historical_parent_route-vs-original10B_route', quality_comparison=comparison,
        absolute_dev_screen=absolute, original_Web=original, retained_source_checks=retained,
        eligible_for_final_Base_validation=all(absolute.values()) and all(original.values()) and comparison['passed'],
        transfer_aggregates={arm:t['summary']['aggregate'] for arm,t in r['transfer'].items()},
        retention_aggregates={arm:t['summary']['aggregate'] for arm,t in r['retention'].items()},
        new_scientific_teacher_tokens=study.TOTAL, reused_control_teacher_tokens=study.TOTAL,
        verification_teacher_tokens=probe['verification_teacher_tokens'], GPU_seconds=r['GPU_seconds'],
        verification_GPU_seconds=probe['GPU_seconds'], failed_probe_GPU_seconds=c['failed_probe_GPU_seconds'], result_sha256=sha256(path),
        Base_adopted=False, Chat_started=False, quantization_started=False, protected_test_used=False,
        independent_human_blind=False, quality_criteria_unchanged=True, old_numerical7_preserved=True,
        limitations='One learned seed; nonblind repeated fixeddev. Parent Web exposure/model/Adam/RNG/scheduler/LR and continued Web cursor differ together, not isolated parent-weight or LR causality. Three short sources unchanged. Shared-generator bridge is local; old128 retention overlaps training forms. Independent seed/full dev/protected test/adoption pending.')
    atomic_json(study.RUN / 'review.json', report)
    atomic_json(ROOT / 'reports/phase6/historical_parent_condition_comparison_v2_review.json', report)
    print(json.dumps(report, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    p = argparse.ArgumentParser(); p.add_argument('--template', action='store_true')
    audit(p.parse_args().template)

