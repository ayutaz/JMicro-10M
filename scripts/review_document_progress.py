"""Review ALL160 newly generated outputs and ALL paired numerical history."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from jmicro.document_progress import ARMS
from jmicro.experiment import sha256,now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_boundary import load_dev_suite
from document_progress_trainer import committed_state
from document_progress_science_protocol import validate_history,matched_original,validate_evaluation,summarize,pilot_quality
from base_fim_pilot_protocol import validate_body,validate_raw,notes_scores
from phase6_performance import alive
from run_document_progress import CONFIG,RUN,binding


def read(path):
    return json.loads(Path(path).read_text())


def reference_content(ev,raw_path,notes_path,suite,codec):
    if read(raw_path) != ev['generation']:
        raise ValueError('Original reference raw generation differs')
    validate_body(ev['body'])
    validate_raw(ev['generation']['outputs'],codec,suite)
    return notes_scores(ev['generation']['outputs'],read(notes_path),sha256(Path(raw_path)))


def review(template=False):
    c = read(CONFIG)
    pin = sha256(CONFIG)
    if any(sha256(ROOT/path) != digest for path,digest in c['sources'].items()):
        raise ValueError('Frozen science/reviewer sources differ')
    job,result = read(RUN/'job.json'),read(RUN/'result.json')
    if (alive(job) or job['status'] != 'complete' or result['status'] != 'complete'
            or job['config_sha256'] != pin or result['config_sha256'] != pin
            or job['cumulative_GPU_ledger_closed'] is not True
            or not 0 < job['GPU_occupancy_seconds'] == result['GPU_occupancy_seconds'] <= c['science_GPU_cap_total']
            or result['cumulative_total_GPU_seconds'] != c['carried_total_GPU_seconds']+result['GPU_occupancy_seconds']
            or result['cumulative_total_GPU_seconds'] > 4800):
        raise ValueError('Actual exited paired science with closed ALL cumulative cost required')
    codec = Tokenizer(c['tokenizer']['path'])
    suite = load_dev_suite(c['DEV_manifest']['path'],c['DEV_manifest']['sha256'])
    states,histories,scores,summaries = {},{},{},{}
    for arm in ARMS:
        record,ev = result['arms'][arm]['training'],result['arms'][arm]['evaluation']
        expected_binding = binding(c,pin,arm)
        if (record['binding'] != expected_binding or result['arms'][arm]['binding'] != expected_binding
                or not 0 < result['arm_GPU_seconds'][arm] <= c['science_GPU_caps_each'][arm]
                or sha256(Path(record['checkpoint'])) != record['checkpoint_sha256']):
            raise ValueError('Exact scientific arm, checkpoint and bounded actual time required')
        state = torch.load(record['checkpoint'],map_location='cpu',weights_only=False)
        if (not committed_state(state) or state['binding'] != expected_binding
                or state['spec']['progress_arm'] != arm or state['counters'] != record['counters']
                or state['counters']['supervised_tokens'] != 25000000
                or state['spec']['native_parameters'] != 10001152 or state['spec']['total_training_parameters'] != 10001408):
            raise ValueError('Genuine paired25M finite native/head/Adam/source terminal state required')
        rows = [json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        if validate_history(rows,state) != record['physical_rollup']:
            raise ValueError('All original main/scalar/physical history differs')
        states[arm],histories[arm] = state,rows
        validate_evaluation(ev,codec,suite)
        if ev['checkpoint_sha256'] != record['checkpoint_sha256'] or ev['binding'] != expected_binding:
            raise ValueError('Scientific terminal weights must bind actual DEV evaluation')
        raw_path,notes_path = RUN/arm/'evaluation/generation.json',RUN/arm/'notes.json'
        if read(raw_path) != ev['generation']:
            raise ValueError('Actual new raw generation differs')
        if template:
            if notes_path.exists():
                raise ValueError('Preserve existing individual review notes')
            atomic_json(notes_path,dict(reviewer='Codex nonblind; each of ALL80 requires fresh individual reading',
                independent_human_blind=False,generation_sha256=sha256(raw_path),
                notes=[[r['id'],None,None,None,None,''] for r in ev['generation']['outputs']]))
        else:
            scores[arm] = notes_scores(ev['generation']['outputs'],read(notes_path),sha256(raw_path))
            summaries[arm] = summarize(ev,scores[arm])
    checks = matched_original(states['document_progress'],states['native_CE_control'])
    if checks != result['paired_original_match'] or not all(checks.values()):
        raise ValueError('Actual terminal paired original source/label fullstream differs')
    keys = ('update','supervised_tokens','source_teachers','source_EOS','physical_input_tokens','CE_input_tokens',
        'original_body_bytes','token_digest','progress_label_positions','progress_zero_EOS_labels',
        'progress_source_labels','progress_target_sum','progress_target_digest','draw_trace','lr')
    if len(histories[ARMS[0]]) != len(histories[ARMS[1]]) or any(a[k] != b[k]
            for a,b in zip(histories[ARMS[0]],histories[ARMS[1]],strict=True) for k in keys):
        raise ValueError('Every paired update main/scalar/source cursor must match')
    if template:
        print('Two unscored80 templates created; no quality adoption')
        return
    refs = c['references']
    for row in refs.values():
        if sha256(Path(row['path'])) != row['sha256']:
            raise ValueError('Original baseline metadata changed')
    cached = read(refs['cached_control_result']['path'])['results']['CE']['evaluation']
    cached_scores = reference_content(cached,refs['cached_control_raw']['path'],refs['cached_control_notes']['path'],suite,codec)
    strong = read(refs['strong_result']['path'])['evaluations']['source_order']
    strong_raw = Path(refs['strong_result']['path']).parent/'evaluation/source_order/evaluation/generation.json'
    strong_scores = reference_content(strong,strong_raw,refs['strong_notes']['path'],suite,codec)
    historical = read(refs['historical_Web']['path'])
    quality = pilot_quality(result['arms'][ARMS[0]]['evaluation'],cached,strong,historical,
        result['arms'][ARMS[1]]['evaluation'],scores[ARMS[0]],cached_scores,strong_scores,scores[ARMS[1]])
    out = dict(status='paired25M_ALL160_content_and_allstate_history_reviewed',created_at=now(),
        config_sha256=pin,result_sha256=sha256(RUN/'result.json'),summaries=summaries,quality=quality,
        notes_sha256={arm:sha256(RUN/arm/'notes.json') for arm in ARMS},paired_original_match=checks,
        all160_individually_read=True,independent_human_blind=False,
        scientific_main_teachers_new_total=50000000,candidate_additional_scalar_learning_labels=25000000,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],cumulative_total_GPU_seconds=result['cumulative_total_GPU_seconds'],
        fixed_condition_closed=not quality['eligible_for_separately_defined_main_comparison'],
        main_qualification_completed=False,independent_learning_completed=False,fullDEV_completed=False,
        new_sealedTEST_completed=False,Base_qualified=False,Base_adopted=False,full_four_item_goal_complete=False,
        TEST_opened=False,limits='Repeated nonblind DEV and one mature parent. Pilot is not qualification or independent pipeline evidence.')
    atomic_json(RUN/'review.json',out)
    print(json.dumps(dict(summaries=summaries,quality=quality),ensure_ascii=False),flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template',action='store_true')
    review(parser.parse_args().template)
