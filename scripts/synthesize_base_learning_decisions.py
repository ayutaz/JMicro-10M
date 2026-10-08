"""Bounded CPU synthesis of existing learning evidence; no rerating or GPU."""
import hashlib
import json
import math
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src')]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json

PHASE = ROOT / 'reports/phase6'
OUTPUT = PHASE / 'base_learning_decision_table_20261008.json'
RUN = PHASE / 'base-parallel-residual-comparison-20261007/sequential'
REVIEWS = (
    'amount_learning_review', 'improved-base-5b-20261006_review',
    'textbook_quantity_comparison_review', 'textbook_coverage_2b_review',
    'story_weight_comparison_review', 'source_order_condition_comparison_v2_review',
    'base_parallel_residual_comparison_review',
)


def main():
    started = time.monotonic()
    if OUTPUT.exists():
        raise ValueError('Preserve completed synthesis')
    torch.set_num_threads(2)
    rows, references = [], {}
    for name in REVIEWS:
        path = PHASE / (name + '.json')
        review = read_json(path)
        references[name] = dict(path=str(path), sha256=sha256(path))
        summaries = review.get('summaries', {'candidate': review.get('summary')})
        for arm, value in summaries.items():
            if value is None:
                raise ValueError('Missing stored learning summary')
            rates = value['rates']
            rows.append(dict(review=name, arm=arm, prepared_material_tokens=value.get('prepared_tokens'),
                stable_teacher_tokens=value.get('stable_teachers'), decay_teacher_tokens=value.get('decay_teachers'),
                grammar2=value['grammar2'], coherence2=value['coherent'], appropriate_end=value['appropriate'],
                EOS=rates['eos'], automatic_repetition=rates['repetition'], BPB=value['BPB'],
                review_new_GPU_seconds=review.get('GPU_seconds', review.get('gpu_seconds')),
                GPU_scope='Whole review, shared across rows; do not sum or attribute to a single arm',
                all80_previously_reviewed=True, new_ratings=0, missing_budget_fields='unknown, not zero'))
    checkpoint = RUN / 'checkpoint-00010000.pt'
    baseline = torch.load(checkpoint, map_location='cpu', weights_only=False)
    c = baseline['counters']
    if c['update'] != 10000 or baseline['spec']['arm'] != 'sequential' or baseline['spec']['batch'] != 80:
        raise ValueError('Actual fixed native sequential first10000-update checkpoint required')
    history = RUN / 'metrics-31561-1498217.jsonl'
    count = prefix_bytes = 0
    total_time = wait_time = 0.
    min_teachers, max_teachers = math.inf, 0
    signature = hashlib.sha256()
    microbatches, grouped, group_lr, base_lr = [], [], [], []
    with history.open('rb') as stream:
        for line in stream:
            prefix_bytes += len(line)
            signature.update(line)
            value = json.loads(line)
            count += 1
            if value['update'] != count:
                raise ValueError('Ordered first10000 committed metrics required')
            n = value['CE_targets_this_update']
            microbatches.append(n)
            min_teachers, max_teachers = min(min_teachers,n), max(max_teachers,n)
            total_time += value['seconds']
            wait_time += value['data_wait_seconds']
            base_lr.append(value['lr'])
            if count % 4 == 0:
                grouped.append(sum(microbatches[-4:]))
                group_lr.append(value['lr'])
            if count == 10000:
                break
    if (count != 10000 or sum(microbatches) != c['supervised_tokens']
            or value['token_digest'] != c['token_digest']
            or value['source_teachers'] != c['source_teachers']):
        raise ValueError('Selected baseline checkpoint and prefix metrics differ')
    budget = math.ceil(total_time * 1.3 + 300)
    output = dict(status='existing_learning_table_and_actual_update_grouping_audit_complete', created_at=now(),
        references=references, rows=rows,
        actual_control_checkpoint=dict(path=str(checkpoint), sha256=sha256(checkpoint)),
        first10000_metrics=dict(path=str(history), prefix_lines=10000, prefix_sha256=signature.hexdigest(),
            whole_file_scanned=False, prefix_bytes=prefix_bytes),
        actual_control_counters=c, actual_control_spec=baseline['spec'],
        grouping_evidence=dict(microbatch_windows=80, microbatches=10000, teacher_tokens=c['supervised_tokens'],
            mean_teachers_per_update=c['supervised_tokens']/10000,
            min_teachers_per_update=min_teachers, max_teachers_per_update=max_teachers,
            proposed_accumulation=4, proposed_optimizer_updates=2500,
            mean_teachers_per_group=sum(grouped)/len(grouped), min_teachers_per_group=min(grouped),
            max_teachers_per_group=max(grouped), physical_to_teacher_ratio=c['physical_input_tokens']/c['supervised_tokens'],
            actual_recorded_microbatch_wall_seconds=total_time, actual_recorded_data_wait_seconds=wait_time,
            baseline_decoupled_weight_decay_factor=math.prod(1-.1*lr for lr in base_lr),
            counterfactual_grouped_weight_decay_factor=math.prod(1-.1*lr for lr in group_lr),
            counterfactual_caution='Decay arithmetic only; no grouped weights or quality measured. Momentum, clipping, update timing and noise also change.'),
        proposed_pilot_GPU_cap_seconds=budget, pilot_cap_limit_seconds=3600,
        measured_budget_eligible=budget<=3600,
        conclusions=[
            'Neither data quantity nor training quantity alone is a qualified Base recipe; BPB and free-generation quality diverge in the completed comparisons.',
            'Strong staged has23/80 coherent and26/80 appropriate, below27/80 for both; its Web BPB also fails the historical retention guard.',
            'Current first10000 native updates use fewer and variable teachers per AdamW step than historical packed32x1024 training. This is an observed optimization difference, not proof of the cause.',
            'Four-microbatch token-weighted accumulation is a distinct, not-yet-run learning comparison on the same exact original stream. It changes optimization grouping and therefore momentum, clipping and decay cadence together.',
            'The original-context and LF interventions remain closed; neither their diagnostic success nor six-example memorization qualifies Base.'
        ],
        next_action='Define one fresh sequential same-stream first10000-microbatch accumulation4 pilot against the existing actual10000-update checkpoint. No baseline retraining or new corpus; own CPU weighted-gradient tests, CUDA resume/capacity gate, exact stream digest/sampler/source counters, fixed256DEV and all80 raw content comparison before any longer proposal.',
        CPU_seconds=time.monotonic()-started, CPU_cap_seconds=30, GPU_seconds=0,
        new_scientific_teacher_tokens=0, new_ratings=0, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_scored=False,
        limits='Reused repeated fixedDEV and nonblind ratings, one trained seed. Cross-study rows differ in history/data/trainer and do not isolate causes. Prepared volume is not globally audited distinct or actually consumed volume. Null budgets stay unknown.')
    if output['CPU_seconds']>30:
        raise TimeoutError('Bounded CPU synthesis exceeded30seconds')
    atomic_json(OUTPUT,output)
    print(json.dumps(dict(status=output['status'], rows=len(rows), CPU_seconds=output['CPU_seconds'],
        teacher_tokens=c['supervised_tokens'], mean_teachers_per_update=c['supervised_tokens']/10000,
        microbatch_wall_seconds=total_time, proposed_pilot_GPU_cap_seconds=budget, eligible=budget<=3600)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
