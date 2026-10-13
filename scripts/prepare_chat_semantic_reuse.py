"""Actual latestD1 all-state control validation and exact NLL reuse.

Known-suite raw and notes are rebound separately after the new config freezes.
No model learning, GPU evaluation, score changes or independent seed claim.
"""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json, implementation_hashes
from phase6_performance import alive, finite_state
from chat_semantic_contract import RUN, OLD, B, SPEC, reference, require_ref


def prepare_control():
    path = RUN / 'historical_control_preparation.json'
    assert not path.exists(), 'Keep validated historical preparation'
    original_config = ROOT / 'configs/phase7/chat-generalization-20261013.json'
    from chat_generalization_contract import preflight as original_preflight
    c, _, _ = original_preflight(original_config)
    assert c['spec'] == SPEC and c['parameter_count'] == 10001152 and c['teacher_budget'] == B
    done = read_json(OLD / 'completion.json')
    assert done['requested_four_items_complete'] and done['config']['sha256'] == c['config_sha256']
    result = read_json(OLD / 'D1/result.json')
    job = read_json(OLD / 'D1/job.json')
    assert job['status'] == result['status'] == 'learning_complete' and not alive(job)
    assert job['config_sha256'] == result['config_sha256'] == c['config_sha256']
    dry = read_json(RUN / 'S0_dry_run.json')
    assert dry['source_sha256'] == c['arms']['D1']['records']['sha256']
    points = read_json(OLD / 'D1/checkpoints.json')
    assert set(points) == {'t1', 't2', 't3'}
    checks = {}
    for point, ref in points.items():
        state = torch.load(require_ref(ref), map_location='cpu', weights_only=False)
        assert state['implementation_sha256'] == implementation_hashes() == c['implementation']
        assert finite_state(state) and state['lineage']['kind'] == 'teacher-normalized-assistant-sft'
        assert state['lineage']['base_checkpoint'] == c['parent']
        assert state['spec']['teacher_chat']['data_binding'] == dry['sampler_binding']
        assert state['spec']['teacher_chat']['budget'] == B
        assert {key: state['spec'][key] for key in SPEC} == SPEC
        assert state['supervised_tokens'] == ref['Assistant_teachers'] and state['update'] == ref['update']
        assert all(key in state for key in ('model', 'optimizer', 'scheduler', 'rng', 'sampler'))
        expected_update = next(row['update'] for n, row in enumerate(dry['rows'])
                               if sum(item['teachers'] for item in dry['rows'][:n + 1]) >= ref['requested_teachers'])
        assert expected_update == state['update']
        checks[point] = dict(checkpoint=ref, finite_all_state=True, actual_complete_teacher_threshold=True,
                             all_state_preserved=True, update=state['update'], supervised_tokens=state['supervised_tokens'])
        del state
    assert points['t3']['update'] == dry['updates'] == 3641
    assert points['t3']['Assistant_teachers'] == dry['Assistant_teachers'] == 1899562
    atomic_json(path, dict(created_at=now(), passed=True, arm='S0', new_learning_updates=0,
                           original_config=reference(original_config), parent=c['parent'], spec=SPEC,
                           original_completion=reference(OLD / 'completion.json'),
                           original_job=reference(OLD / 'D1/job.json'), original_result=reference(OLD / 'D1/result.json'),
                           original_training_audit=reference(OLD / 'D1/training_audit.json'),
                           original_final_stream_audit=reference(OLD / 'D1/t3_audit.json'),
                           original_GPU_ledger=reference(OLD / 'GPU_ledger.json'),
                           checkpoints=points, actual_state_checks=checks, sampler_binding=dry['sampler_binding'],
                           native_probe=reference(OLD / 'native_probe.json'),
                           native_resume=reference(OLD / 'native_resume_gate.json'),
                           independent_trained_seed=False, new_GPU_quality_evidence=False))
    print('Historical latestD1 all3 actual states validated; new control learning0')


def reusable_nll(c, arm, point, ref, windows):
    if arm not in ('parent', 'S0'):
        return {}, []
    old_arm = 'parent' if arm == 'parent' else 'D1'
    old_point = 't0' if arm == 'parent' else point
    source = OLD / 'NLL' / old_arm / (old_point + '.json')
    value = read_json(source)
    assert value['status'] == 'complete' and value['binding']['checkpoint']['sha256'] == ref['sha256']
    old_config = read_json(ROOT / 'configs/phase7/chat-generalization-20261013.json')
    assert value['binding']['config_sha256'] == sha256(ROOT / 'configs/phase7/chat-generalization-20261013.json')
    assert value['binding']['fixed_targets'] == old_config['fixed_NLL']
    old_targets = [json.loads(line) for line in require_ref(old_config['fixed_NLL']).read_text().splitlines()]
    assert len(old_targets) == len(value['targets']) == 2554
    indexed = {row['id']: row for row in value['targets']}
    assert len(indexed) == 2554
    definition = {row['id']: row for row in old_targets}
    for name, summary in value['summaries'].items():
        rows = [row for row in value['targets'] if row['dataset'] == name]
        assert len(rows) == summary['targets']
        assert all(math.isfinite(row[key]) and row[key] >= 0 for row in rows for key in ('body_NLL', 'EOT_NLL'))
        for key in ('body_teachers', 'EOT_teachers', 'body_bytes'):
            assert sum(row[key] for row in rows) == summary[key]
        for key in ('body_NLL', 'EOT_NLL'):
            assert math.isclose(sum(row[key] for row in rows), summary[key], rel_tol=1e-12)
    reused = {}
    for target, _, _ in windows:
        if target['dataset'] not in ('S0_TRAIN', 'RPC_DEV'):
            continue
        old_id = target['historical_target']['id'] if target['dataset'] == 'S0_TRAIN' else target['id']
        old = definition[old_id]
        assert old['messages'] == target['messages'] and old['window_binding'] == target['window_binding']
        assert old['teachers'] == target['teachers'] and old['body_bytes'] == target['body_bytes']
        row = indexed[old_id]
        assert row['body_teachers'] + 1 == target['teachers'] and row['EOT_teachers'] == 1
        assert row['body_bytes'] == target['body_bytes']
        reused[target['id']] = dict(row, id=target['id'], dataset=target['dataset'])
    assert len(reused) == 2362
    return reused, [dict(source=reference(source), source_fixed_targets=old_config['fixed_NLL'],
                         targets=2362, exact_window_mask_and_bytes=True, new_GPU_NLL_targets_for_reuse=0,
                         alias='D1_TRAIN to S0_TRAIN with unchanged full token window; RPC unchanged',
                         independent_quality_confirmation=False)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--prepare', action='store_true', required=True)
    parser.parse_args()
    prepare_control()
