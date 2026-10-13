"""Audit one fully saved point while the same frozen learning job continues."""
import argparse
import json
from pathlib import Path
import torch
from chat_lr_contract import RUN, B, SPEC, preflight, require_ref, reference
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json
from jmicro.model import JMicroModel
from phase6_performance import finite_state


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--point', choices=('t1', 't2', 't3'), required=True)
    args = p.parse_args()
    c, _, _ = preflight()
    directory = RUN / 'S1'
    ref = read_json(directory / 'checkpoints.json')[args.point]
    state = torch.load(require_ref(ref), map_location='cpu', weights_only=False)
    # Ignore only an in-flight non-newline log fragment, never a saved row.
    text = (directory / 'metrics.jsonl').read_bytes()
    metrics = [json.loads(line) for line in text.split(b'\n')[:-1] if line]
    saved = metrics[:ref['update']]
    dry = read_json(require_ref(c['candidate_consumption']))
    prior = [json.loads(line) for line in require_ref(c['historical_learning_metrics']).read_text().splitlines()]
    assert len(saved) == ref['update']
    count = 0
    for row, expected, control in zip(saved, dry['rows'][:ref['update']], prior[:ref['update']], strict=True):
        assert row['update'] == expected['update']
        assert (row['lr'], row['teachers_this_update'], row['microbatches']) == (expected['lr'], expected['teachers'], expected['microbatches'])
        assert row['token_digest'] == control['token_digest']
        assert all(row[key] == control[key] for key in ('assistant_teacher_tokens', 'EOT_teachers', 'valid_input_tokens', 'physical_input_tokens'))
        count += row['teachers_this_update']
    threshold = (B * int(args.point[1]) + 2) // 3
    assert saved[-1]['assistant_teacher_tokens'] == state['supervised_tokens'] == count == ref['Assistant_teachers']
    assert count >= threshold and (len(saved) == 1 or saved[-2]['assistant_teacher_tokens'] < threshold)
    assert state['implementation_sha256'] == c['implementation'] and finite_state(state)
    assert {key: state['spec'][key] for key in SPEC} == SPEC
    assert state['spec']['teacher_chat']['budget'] == B and state['spec']['teacher_chat']['data_binding'] == c['sampler_binding']
    assert state['lineage']['base_checkpoint'] == c['parent'] and state['lineage']['optimizer_policy'] == 'fresh'
    assert state['update'] == state['branch_updates'] == ref['update']
    assert state['token_digest'] == saved[-1]['token_digest']
    assert state['tokens'] == state['sampler']['input_tokens'] == saved[-1]['valid_input_tokens']
    assert state['sampler']['physical_tokens'] == saved[-1]['physical_input_tokens']
    assert state['optimizer']['state'] and all(int(row['step'].item()) == state['update'] for row in state['optimizer']['state'].values())
    assert state['scheduler']['last_epoch'] == state['update'] and state['scheduler']['_last_lr'] == [saved[-1]['lr']]
    assert set(state['rng']) == {'python', 'numpy', 'torch', 'cuda'}
    model = JMicroModel(state['model_config'])
    model.load_state_dict(state['model'], strict=True)
    assert sum(p.numel() for p in model.parameters()) == 10001152
    atomic_json(directory / ('audit-' + args.point + '.json'), dict(passed=True, completed_at=now(),
        checkpoint=ref, source=reference(Path(__file__)), config_sha256=c['config_sha256'],
        first_registered_threshold_update=True, actual_complete_state_finite=True,
        all_saved_input_label_digests_match_historical_control=True, exact_teacher_LR_microbatch_order=True,
        learning_updates=ref['update'], Assistant_teachers=count, GPU_updates=0, quality_evidence=False))
    print(f"{args.point} actual saved state and{ref['update']} update input/LR prefix passed; no quality claim")
