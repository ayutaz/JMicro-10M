"""Audit the completed pilot on CPU; this neither scores prose nor adopts Base."""
import hashlib
import argparse
import json
import math
import os
from pathlib import Path
import sys
from datetime import datetime, timezone

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.phase5 import equal_state
from jmicro.experiment import ROOT, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from run_base_document_balance import RUN, CONFIG, matched_control_checks
from review_base_document_balance import load_policy, audit_state
from base_document_balance_trainer import committed_state


def native_count(state):
    tensors = state['model']
    assert torch.equal(tensors['lm_head.weight'], tensors['model.embed_tokens.weight'])
    # Host serialization may duplicate storage of the two tied state keys.
    # Count the shared native embedding once; no other native key is shared.
    return sum(t.numel() for name, t in tensors.items() if name != 'lm_head.weight')


def inspect_checkpoint():
    c, _ = load_policy()
    job = read_json(RUN/'job.json')
    assert job['config_sha256'] == sha256(CONFIG)
    checkpoint = Path(job['latest_checkpoint'])
    state = torch.load(checkpoint,map_location='cpu',weights_only=False)
    assert committed_state(state) and native_count(state) == 10001152
    assert state['binding']['config_sha256'] == sha256(CONFIG)
    assert state['binding']['sources'] == c['source_sha256']
    assert state['model_config']['expected_parameter_count'] == 10001152
    assert state['counters']['supervised_tokens'] <= 100000000
    proof=dict(status='current_saved_checkpoint_verified_on_CPU_quality_pending',
        observed_at=datetime.now(timezone.utc).isoformat(),
        checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),
        update=state['counters']['update'],original_teachers=state['counters']['supervised_tokens'],
        finite_model_Adam_and_committed_counters=True,native_parameters=10001152,
        sources_and_recipe_match=True,GPU_work=0,TEST_read=False,Base_adopted=False)
    destination=RUN/'checkpoint_audits'/f"checkpoint-{state['counters']['update']:08d}.json"
    if not destination.exists(): atomic_json(destination,proof)
    print(json.dumps(proof))


def verify_history(state):
    """All actual committed updates, not a tail or selected loss observations."""
    history = {}
    paths = sorted((RUN/'document_balance').glob('metrics-*.jsonl'), key=lambda p: p.stat().st_mtime_ns)
    final_update = state['counters']['update']
    discarded, duplicates = 0, 0
    for path in paths:
        with path.open() as stream:
            for line in stream:
                row = json.loads(line)
                update = row['update']
                if update > final_update:
                    discarded += 1
                    continue
                if update in history: duplicates += 1
                history[update] = row
    assert sorted(history) == list(range(1, final_update+1)), 'Missing actual committed updates'
    prior_total, prior_sources, prior_EOS = 0, dict(web=0,textbook=0,story=0), dict(web=0,textbook=0,story=0)
    seconds = input_positions = actual_gold = 0
    weight_ratio_min, weight_ratio_max = math.inf, 0.
    for update, row in sorted(history.items()):
        numeric = ('CE_loss','combined_loss','balance_mean_inverse_length','balance_weight_ratio','gradient_norm','seconds','lr')
        assert all(math.isfinite(row[k]) for k in numeric), ('Nonfinite metric', update)
        assert row['CE_loss'] >= 0 and row['combined_loss'] >= 0 and row['seconds'] > 0 and row['lr'] == 1e-5
        assert row['decoder_forwards_this_update'] == 1
        lengths, traces = row['original_document_teachers'], row['draw_trace']
        assert len(lengths) == len(traces) == row['original_windows_this_update']
        assert 1 <= len(lengths) <= 48 and all(type(n) is int and n >= 2 for n in lengths)
        counts = [t[4] for t in traces]
        assert all(type(n) is int and 0 < n <= 512 for n in counts)
        assert all(n <= length for n, length in zip(counts, lengths, strict=True))
        gold = sum(counts)
        assert gold == row['CE_targets_this_update'] == row['balance_positions_this_update']
        assert row['supervised_tokens'] == prior_total+gold
        assert row['document_balance'] == dict(updates=update, positions=row['supervised_tokens'])
        # Independent scalar arithmetic from the recorded whole-unit length and
        # selected original teachers, rather than trusting logged green checks.
        expected_mean = sum(n/length for n, length in zip(counts, lengths, strict=True))/gold
        expected_ratio = max(lengths)/min(lengths)
        assert math.isclose(row['balance_mean_inverse_length'], expected_mean, rel_tol=2e-6, abs_tol=1e-9), update
        assert math.isclose(row['balance_weight_ratio'], expected_ratio, rel_tol=2e-6, abs_tol=1e-6), update
        assert sum(row['source_teachers'].values()) == row['supervised_tokens']
        assert all(row['source_teachers'][g] >= prior_sources[g] and row['source_EOS'][g] >= prior_EOS[g] for g in prior_sources)
        assert 0 <= sum(row['source_EOS'][g]-prior_EOS[g] for g in prior_EOS) <= len(lengths)
        assert row['auxiliary_input_tokens'] == row['auxiliary_pairs'] == 0 and row['auxiliary_digest'] == '0'*64
        assert 1 <= row['maximum_CE_input_tokens_this_update'] <= 1024
        assert row['physical_inputs_this_update'] == len(lengths)*row['maximum_CE_input_tokens_this_update']
        assert row['CE_input_tokens']-input_positions <= row['physical_inputs_this_update']
        input_positions = row['CE_input_tokens']
        prior_total, prior_sources, prior_EOS = row['supervised_tokens'], row['source_teachers'], row['source_EOS']
        actual_gold += gold
        seconds += row['seconds']
        weight_ratio_min = min(weight_ratio_min, row['balance_weight_ratio'])
        weight_ratio_max = max(weight_ratio_max, row['balance_weight_ratio'])
    last = history[final_update]
    assert equal_state({k:last[k] for k in state['counters']}, state['counters'])
    assert actual_gold == 100000000
    return dict(all_committed_updates=final_update, actual_original_teacher_positions=actual_gold,
        all_document_length_weights_independently_checked=True,
        all_finite_loss_gradient_and_fixed_LR_checked=True, source_and_EOS_counters_monotonic=True,
        final_log_and_full_state_counters_equal=True, summed_update_seconds=seconds,
        observed_weight_ratio_min=weight_ratio_min, observed_weight_ratio_max=weight_ratio_max,
        discarded_post_checkpoint_updates=discarded, duplicate_attempts_preserved=duplicates,
        metrics_files=[dict(path=str(p),sha256=sha256(p)) for p in paths])


def main():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '': raise ValueError('Run this CPU audit with CUDA_VISIBLE_DEVICES empty')
    c, policy = load_policy()
    job, result = read_json(RUN/'job.json'), read_json(RUN/'result.json')
    assert job['status'] == result['status'] == 'complete' and not alive(job)
    assert result['actual_identity'] == {k:job[k] for k in ('pid','boot_id','start_ticks')}
    assert result['config_sha256'] == job['config_sha256'] == sha256(CONFIG)
    assert 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= c['GPU_budget_seconds']
    assert result['total_GPU_seconds_including_probe'] == result['GPU_occupancy_seconds']+c['probe_GPU_seconds'] <= 4800
    record = result['training']
    checkpoint = Path(record['checkpoint'])
    assert checkpoint.is_file() and sha256(checkpoint) == record['checkpoint_sha256']
    state = torch.load(checkpoint,map_location='cpu',weights_only=False)
    audit_state(state,record,c)
    assert native_count(state) == 10001152
    assert state['binding']['sources'] == c['source_sha256']
    checks = matched_control_checks(record,read_json(Path(c['control_CE']['path'])))
    assert all(checks.values()) and checks == result['common_CE_checks']
    history = verify_history(state)
    assert history['summed_update_seconds'] <= result['GPU_occupancy_seconds']
    proof = dict(passed=True,recorded_at=datetime.now(timezone.utc).isoformat(),
        status='completed_exact100M_pilot_numeric_stream_and_weight_audit_quality_pending',
        source=dict(path=str(Path(__file__)),sha256=sha256(Path(__file__))),
        result_sha256=sha256(RUN/'result.json'),config_sha256=sha256(CONFIG),
        full_checkpoint_sha256=record['checkpoint_sha256'],
        actual_exited_process_verified=True, matched_original_stream_and_full_sampler=checks,
        native_parameters=10001152, original_body_and_EOS_supervision_preserved=True,
        frozen_scientific_and_review_sources_checked=True,history=history,
        GPU_seconds=result['GPU_occupancy_seconds'],probe_GPU_seconds=c['probe_GPU_seconds'],
        own_GPU_work=0,protectedTEST_read=False,content_review_complete=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Individually read and score all80 raw outputs; apply unchanged policy. Qualified-only main comparison/independent seed/fullDEV/protectedTEST remain gated.')
    destination=RUN/'numeric_completion_audit.json'
    if destination.exists(): raise ValueError('Preserve completed numeric audit; do not repeat whole history scan')
    atomic_json(destination,proof)
    print(json.dumps(proof,ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser()
    parser.add_argument('--inspect-checkpoint',action='store_true')
    args=parser.parse_args()
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '': raise ValueError('CPU-only audit requires empty CUDA_VISIBLE_DEVICES')
    inspect_checkpoint() if args.inspect_checkpoint else main()
