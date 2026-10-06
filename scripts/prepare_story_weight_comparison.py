"""Bound a single CE mixture comparison; prepare evidence, never launch learning."""
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json, implementation_hashes
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive
import run_broad_context_diagnostic as diagnostic


def main():
    started = time.monotonic(); torch.set_num_threads(2)
    c, _ = diagnostic.inspect()
    job = read_json(diagnostic.RUN / 'job.json')
    review_path = ROOT / 'reports/phase6/broad_context_diagnostic_review.json'
    review = read_json(review_path)
    if job['status'] != 'complete' or alive(job) or any(v['local_context_dependence_marker'] for v in review['summary'].values()):
        raise ValueError('This preparation is specifically the measured no-context-marker branch')
    if review['result_sha256'] != sha256(diagnostic.RUN / 'result.json'):
        raise ValueError('Diagnostic result binding differs')
    diagnostic.check_reference(c['references']['compact_index'])
    view = TrainView(c['pool']['pool'], c['pool']['manifest_sha256'])
    view.index = CachedThreeSourceIndex(view)
    if not view.index.cache_reused:
        raise ValueError('Refuse original index scan')
    supply = {}
    for tag, genre in enumerate(diagnostic.GENRES):
        selected = view.index.sources == tag
        lengths = view.index.lengths[selected].astype(np.int64)
        count = int(selected.sum())
        supply[genre] = dict(documents=count, body_tokens=int(lengths.sum()),
            EOS_teacher_tokens=count, body_plus_EOS_teacher_tokens=int(lengths.sum()) + count,
            serialized_BOS_body_EOS_tokens=int(lengths.sum()) + 2 * count)
    if sum(v['serialized_BOS_body_EOS_tokens'] for v in supply.values()) != c['prepared_tokens']:
        raise ValueError('Source supply does not sum to original material')
    ref = c['checkpoints']['twoB']; diagnostic.check_reference(ref)
    parent = torch.load(ref['path'], map_location='cpu', weights_only=False)
    lrs = [float(g['lr']) for g in parent['optimizer']['param_groups']]
    if (not lrs or any(abs(lr - .0002) > 1e-10 for lr in lrs)
            or parent['supervised_tokens'] != 2020000000
            or parent['pilot_binding']['short_manifest_sha256'] != c['pool']['manifest_sha256']):
        raise ValueError('Actual common parent/terminal LR/pool differs')
    arms = dict(control=dict(web=75000000, textbook=20000000, story=5000000),
                story20=dict(web=60000000, textbook=20000000, story=20000000))
    for goals in arms.values():
        if sum(goals.values()) != 100000000 or any(supply[g]['body_plus_EOS_teacher_tokens'] < n for g, n in goals.items()):
            raise ValueError('Train source supply below proposed teacher quota')
    elapsed = time.monotonic() - started
    if elapsed > 300:
        raise TimeoutError('CPU300s preparation limit exhausted')
    result = dict(status='source_supply_and_actual_parent_ready_training_command_missing',
        created_at=now(), hypothesis='With the broad material held fixed, increase story teacher weight5%->20% at the expense of Web75%->60%, keeping textbook20%, to test everyday continuation/subject relation learning.',
        references=dict(context_review=dict(path=str(review_path), sha256=sha256(review_path)),
            context_config=dict(path=str(diagnostic.CONFIG), sha256=sha256(diagnostic.CONFIG))),
        parent=ref, parent_teacher_tokens=parent['supervised_tokens'], parent_input_tokens=parent['tokens'],
        parent_sampler=parent['sampler'], terminal_parent_learning_rates=lrs,
        material=c['pool'], prepared_tokens=c['prepared_tokens'], source_supply=supply,
        accepted_compact_index=c['references']['compact_index'], index_reused=True, original_index_rescan=False,
        proposed_arms_teacher_tokens=arms, scientific_total_new_teacher_tokens=200000000,
        loss='CE body+EOS only; no sequence unlikelihood, no decoding-policy change',
        optimizer_policy='Both inherit identical actual parent model/Adam/RNG; constant inherited terminal LR0.0002, no reheat; no optimizer updates until measured CUDA gates.',
        sampler_policy='Explicit experimental fork into per-genre document shuffles, same initial seed/order in both arms. Preserve original sampler as parent lineage; do not claim the new mixture keeps its old mixed block cursor. Save new samplers at completed updates.',
        shapes=dict(context=1024, batch=32, accumulation=1, backend='flash', compile_mode='reduce-overhead', dtype='bf16'),
        CUDA_verification_budget_seconds=120, total_new_GPU_budget_seconds=1800,
        freeze_condition='Implement matched sampler/trainer/runner/reviewer; continuous4 vs2+2 full-state CUDA and finite results on both arms; measured total including verification/training/evaluations must fit1800s before scientific recipe freeze.',
        completion_condition='Both actual100M teacher arms; common-byte dev256/Japanese/fixed80 per arm and all160 raw-bound content reviews; unchanged relative/absolute/original-Web gates; persisted evidence/actual terminal processes/UI restoration/local commit.',
        parent_evaluation_reuse='Existing2B+20M evaluation is parent retention reference only; both new100M arms must really train and evaluate, not reuse it as a matched scientific control.',
        failure_branch='If original quality gates remain unmet, reject; no blind ratio sweep or automatic5B/10B extension. Select the next single hypothesis from raw failures.',
        implementation=implementation_hashes(), preparation_script_sha256=sha256(Path(__file__)),
        actual_CPU_seconds=elapsed, actual_GPU_seconds=0, actual_optimizer_updates=0,
        scientific_teacher_tokens_consumed=0, training_command_implemented=False, scientific_config_frozen=False,
        quality_criteria_unchanged=True, old_numerical7_preserved=True, Base_adopted=False,
        Chat_adopted=False, protected_test_used=False, requested_five_steps_complete=False,
        interpretation='New explicit mixture research, not a claim that an old quality extension gate passed. Same prepared material quantity; only teacher mixture changes. Source quality/global dedup and causal sufficiency remain unproven.')
    path = ROOT / 'reports/phase6/story_weight_comparison_preparation.json'
    if path.exists():
        raise ValueError('Preparation record already exists; inspect instead of overwriting')
    atomic_json(path, result)
    print(json.dumps(dict(status=result['status'], source_supply=supply, terminal_LR=lrs,
        CPU_seconds=elapsed, new_scientific_GPU=0)), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
