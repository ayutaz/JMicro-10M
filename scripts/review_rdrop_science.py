"""All80 raw-bound content and original gates; no mixed suite/TEST reader."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
import torch
from jmicro.experiment import sha256, now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_boundary import load_dev_suite
from jmicro.phase5 import equal_state
from base_fim_pilot_protocol import validate_body, validate_raw, notes_scores
from rdrop_target_batch_trainer import committed_state
from rdrop_science_protocol import (
    matched_original,validate_history,validate_evaluation,summarize,pilot_quality,paired_history)
from phase6_performance import alive
from run_rdrop_science import CONFIG, RUN


def read(path):
    return json.loads(Path(path).read_text())


def reference_content(ev, raw_path, notes_path, suite, codec):
    raw_path, notes_path = Path(raw_path), Path(notes_path)
    raw = read(raw_path)
    if raw != ev['generation']:
        raise ValueError('Original cached raw generation differs')
    validate_body(ev['body'])
    validate_raw(raw['outputs'], codec, suite)
    scores = notes_scores(raw['outputs'], read(notes_path), sha256(raw_path))
    return scores


def review(template=False):
    c = read(CONFIG)
    if any(sha256(ROOT / path) != pin for path, pin in c['sources'].items()):
        raise ValueError('Frozen review/scientific source changed')
    job, result = read(RUN / 'job.json'), read(RUN / 'result.json')
    if (alive(job) or job['status'] != 'complete' or result['status'] != 'complete'
            or job['config_sha256'] != sha256(CONFIG) or result['config_sha256'] != sha256(CONFIG)
            or not job['cumulative_GPU_ledger_closed']
            or not 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= c['scientific_GPU_cap_seconds']
            or result['cumulative_total_GPU_seconds'] != result['GPU_occupancy_seconds'] + c['carried_total_GPU_seconds']
            or c['total_GPU_cap_seconds'] is not None):
        raise ValueError('Actual exited bounded scientific learning/evaluation required')
    record, ev = result['training'], result['evaluation']
    if sha256(Path(record['checkpoint'])) != record['checkpoint_sha256']:
        raise ValueError('Actual typed checkpoint changed')
    state = torch.load(record['checkpoint'], map_location='cpu', weights_only=False)
    if (not committed_state(state) or state['binding'] != result['binding'] or state['binding'] != record['binding']
            or state['counters'] != record['counters'] or state['counters']['supervised_tokens'] != 25000000
            or state['spec']['rdrop_arm'] != 'normalized_rdrop'
            or state['spec']['native_parameters'] != 10001152):
        raise ValueError('Genuine original25M native RDrop numerical state required')
    rows = [json.loads(line) for line in (RUN / 'metrics.jsonl').read_text().splitlines()]
    physical = validate_history(rows, state)
    control_state = torch.load(c['control_checkpoint']['path'], map_location='cpu', weights_only=False)
    checks = matched_original(state,control_state)
    paired_history(rows,[json.loads(line) for line in Path(c['control_metrics']['path']).read_text().splitlines()])
    if checks != record['original_CE_match'] or not all(checks.values()):
        raise ValueError('Exact original CE stream/cursor/control comparison differs')
    codec = Tokenizer(c['tokenizer']['path'])
    suite = load_dev_suite(c['DEV_manifest']['path'], c['DEV_manifest']['sha256'])
    validate_evaluation(ev, codec, suite)
    raw_path = RUN / 'evaluation/generation.json'
    if read(raw_path) != ev['generation']:
        raise ValueError('Actual new raw generation differs')
    notes_path = RUN / 'notes.json'
    if template:
        if notes_path.exists():
            raise ValueError('Preserve existing individual notes')
        atomic_json(notes_path, dict(reviewer='Codex nonblind; all80 require individual content reading',
            independent_human_blind=False, generation_sha256=sha256(raw_path),
            notes=[[r['id'], None, None, None, None, ''] for r in ev['generation']['outputs']]))
        print('Unscored80 template created; no quality adoption')
        return
    candidate_scores = notes_scores(ev['generation']['outputs'], read(notes_path), sha256(raw_path))
    refs = c['references']
    for r in refs.values():
        if sha256(Path(r['path'])) != r['sha256']:
            raise ValueError('Original baseline reference changed')
    control = read(refs['cached_control_result']['path'])['results']['CE']['evaluation']
    control_scores = reference_content(control, refs['cached_control_raw']['path'], refs['cached_control_notes']['path'], suite, codec)
    strong_result = read(refs['strong_result']['path'])
    strong = strong_result['evaluations']['source_order']
    strong_raw = Path(refs['strong_result']['path']).parent / 'evaluation/source_order/evaluation/generation.json'
    strong_scores = reference_content(strong, strong_raw, refs['strong_notes']['path'], suite, codec)
    historical = read(refs['historical_Web']['path'])
    matched = read(c['control_result']['path'])['evaluation']
    matched_scores = reference_content(matched,c['control_raw']['path'],c['control_notes']['path'],suite,codec)
    quality = pilot_quality(matched,control,strong,historical,ev,matched_scores,control_scores,strong_scores,candidate_scores)
    summary = summarize(ev, candidate_scores)
    completed = dict(status='original25M_rdrop_all80_reviewed', created_at=now(),
        config_sha256=sha256(CONFIG), result_sha256=sha256(RUN / 'result.json'),
        notes_sha256=sha256(notes_path), summary=summary, quality=quality,
        original_CE_match=checks, all80_individually_read=True, independent_human_blind=False,
        scientific_CE_teachers=25000000, reused_control_CE_teachers=25000000,
        total_hardgold_CE_evaluations=state['counters']['total_CE_teacher_evaluations'],
        consistency_pairs=state['counters']['consistency_pairs'],
        physical_rollup=physical, GPU_seconds=result['GPU_occupancy_seconds'], technical_GPU_seconds=c['technical_GPU_seconds'],
        fixed_condition_closed=not quality['eligible_for_separately_defined_main_comparison'], eligible_for_separately_defined_main_comparison=quality['eligible_for_separately_defined_main_comparison'],
        main_qualification_completed=False, independent_learning_completed=False, fullDEV_completed=False, new_sealedTEST_completed=False,
        Base_qualified=False, Base_adopted=False, full_four_item_goal_complete=False, TEST_opened=False,
        limitations='Known repeated nonblind DEV; one mature-parent learned seed. Qualified recipe still requires genuinely fresh whole-pipeline independent learning/fullDEV/all440/new sealedTEST/adoption.')
    atomic_json(RUN / 'review.json', completed)
    print(json.dumps(dict(summary=summary, eligible_for_separately_defined_main_comparison=quality['eligible_for_separately_defined_main_comparison']), ensure_ascii=False), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template', action='store_true')
    args = parser.parse_args()
    review(args.template)
