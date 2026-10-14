"""Read-only CPU audit of an immutable checkpoint and its exact log prefix.

No corpus/DEV/TEST/model forward or GPU. Compare a saved native CE checkpoint
at the same update when available; never mutate the running scientific job.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'src'), str(ROOT / 'scripts')]
import torch
from jmicro.experiment import sha256, now
from jmicro.phase5 import equal_state
from context_likelihood_trainer import committed_state
from context_likelihood_science_protocol import validate_history, matched_original


def audit(candidate, candidate_pin, control, control_pin, metrics, output):
    started = time.monotonic()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or output.exists():
        raise ValueError('Fresh read-only CPU evidence path and explicit empty CUDA required')
    if sha256(candidate) != candidate_pin or sha256(control) != control_pin:
        raise ValueError('Externally pinned immutable checkpoints required')
    state = torch.load(candidate, map_location='cpu', weights_only=False)
    old = torch.load(control, map_location='cpu', weights_only=False)
    if (not committed_state(state) or state['binding']['weights_role'] != 'scientific_context_likelihood'
            or state['binding']['probe_weights_used'] is not False
            or state['counters']['update'] != old['counters']['update']):
        raise ValueError('Actual same-update scientific and original control state required')
    count = state['counters']['update']
    rows = []
    prefix_sha = hashlib.sha256()
    with metrics.open('rb') as handle:
        for _ in range(count):
            raw = handle.readline()
            if not raw or not raw.endswith(b'\n'):
                raise ValueError('Complete immutable metrics prefix required')
            rows.append(json.loads(raw))
            prefix_sha.update(raw)
    physical = validate_history(rows, state)
    checks = matched_original(state, old, physical['CE_physical_inputs'])
    if not all(checks.values()):
        raise ValueError('Actual original CE control pairing differs')
    if sha256(candidate) != candidate_pin or sha256(control) != control_pin:
        raise ValueError('Checkpoint changed during CPU audit')
    result = dict(status='same_update_original_control_full_state_and_metrics_prefix_CPU_audited',
        observed_at=now(), checkpoint=dict(path=str(candidate), sha256=candidate_pin),
        original_control=dict(path=str(control), sha256=control_pin), completed_updates=count,
        original_main_teacher_positions=state['counters']['supervised_tokens'],
        repeated_auxiliary_likelihood_targets=state['counters']['auxiliary_target_evaluations'],
        auxiliary_pairs=state['counters']['auxiliary_pairs'], FIFO_entries=len(state['context_FIFO']['entries']),
        FIFO_committed_anchors=state['context_FIFO']['committed_anchors'],
        FIFO_sha256=hashlib.sha256(json.dumps(state['context_FIFO'], sort_keys=True).encode()).hexdigest(),
        full_original_control_checks=checks, physical_rollup=physical,
        original_source_teachers=state['counters']['source_teachers'], original_source_EOS=state['counters']['source_EOS'],
        actual_models_differ=not equal_state(state['model'], old['model']),
        native_Adam_scheduler_RNG_FIFO_counters_finite=True,
        metrics_prefix_sha256=prefix_sha.hexdigest(), auditor_sha256=sha256(Path(__file__)),
        CPU_wall_seconds=time.monotonic() - started, new_GPU_seconds=0, new_optimizer_updates=0,
        new_model_quality_evaluations=0, corpus_opened=False, DEV_opened=False, TEST_opened=False,
        independent_learning_evidence=False, Base_adopted=False,
        limitations='A saved numerical prefix with preserved main stream, not scientific completion or quality improvement.')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'completed_updates', 'original_main_teacher_positions',
        'auxiliary_pairs', 'CPU_wall_seconds', 'new_GPU_seconds')}), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('candidate', 'control', 'metrics', 'output'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--candidate-sha256', required=True)
    parser.add_argument('--control-sha256', required=True)
    args = parser.parse_args()
    audit(args.candidate, args.candidate_sha256, args.control, args.control_sha256, args.metrics, args.output)
