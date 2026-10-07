"""Preserve six completed studies and define one new output-probability comparison."""
import sys
from pathlib import Path
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    phase = ROOT / 'reports/phase6'
    companion = phase / 'base_completed_objective_studies_v2_20261007.json'
    proposal = phase / 'base_sigsoftmax_proposal.json'
    if companion.exists() or proposal.exists():
        raise ValueError('Preserve prospective evidence')
    rows = []
    control = strong = None
    for name in ('on_policy_teacher', 'sam', 'middle_supervision', 'confidence_penalty', 'native_teacher_KD', 'native_hint'):
        filename = 'base_native_teacher_KD_science_comparison_completion.json' if name == 'native_teacher_KD' else f'base_{name}_comparison_completion.json'
        path = phase / filename
        record = read_json(path)
        if (alive(record['actual_identity']) or record['scientific_CE_teacher_tokens'] != 100000000
                or record['eligible_for_final_Base_validation'] is not False
                or record['all80_individually_read'] is not True
                or any(record[k] is not False for k in ('Base_complete', 'Base_adopted', 'Chat_started', 'quantization_started', 'protected_test_scored'))):
            raise ValueError('Exited complete same100M quality rejections required')
        for key in ('review', 'notes'):
            reference = record[key]
            if sha256(Path(reference['path'])) != reference['sha256']:
                raise ValueError('Completed historical review/notes changed')
        review = read_json(Path(record['review']['path']))
        if control is None:
            control, strong = record['summaries']['CE'], record['summaries']['strong_staged']
        elif control != record['summaries']['CE'] or strong != record['summaries']['strong_staged']:
            raise ValueError('Common historical controls differ')
        rows.append(dict(arm=name, completion=ref(path), original_gold_tokens=100000000,
            summaries=record['summaries'][name], matched_gates=review['matched_objective_quality'],
            GPU_seconds_including_probe=record['total_GPU_seconds_including_probe'],
            eligible_for_final_Base_validation=False))
    atomic_json(companion, dict(created_at=now(), status='six_completed_same_gold_objective_conditions_quality_rejected',
        previous_snapshot=ref(phase / 'base_completed_objective_studies_20261007.json'),
        historical_route_inventory=ref(phase / 'base_failure_route_synthesis.json'),
        conditions=rows, cached_CE=control, strong_staged=strong,
        original_gold_exposures_across_conditions=600000000, new_unique_dataset_tokens=0,
        dataset_scope='Same matched100M stream repeated in six conditions; separately defined auxiliary positions are not interchangeable new corpus or hard labels.',
        historical_files_overwritten=False, historical_ratings_changed=False,
        old_resource_failures_preserved=True, output_KD_stop_and_repetition_effect_preserved=True,
        inference='No adopted Base; these objective changes did not meet the frozen quality gates. Neither general data futility nor a10M capacity ceiling is proved.',
        new_GPU_seconds=0, Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False))
    current = read_json(ROOT / 'configs/phase6/base_native_hint_comparison.json')
    atomic_json(proposal, dict(created_at=now(), status='prospective_fixed_output_link_comparison_before_implementation',
        question='Does changing the native single-softmax probability link to parameter-free sigsoftmax improve generalization of coherent Japanese prose at the same10M weights and original100M gold?',
        references={name: ref(phase / name) for name in (
            companion.name, 'base_native_hint_comparison_completion.json', 'base_native_teacher_KD_science_comparison_completion.json',
            'base_embedding_gradient_completion.json', 'base_failure_route_synthesis.json', 'base_capacity_reference_synthesis.json')},
        primary_sources=[
            dict(url='https://arxiv.org/abs/1711.03953', role='Single linear-softmax output representational bound; MoS motivation, not Japanese quality proof'),
            dict(url='https://proceedings.neurips.cc/paper/2018/file/9dcb88e0137649590b755372b040afad-Paper.pdf',
                 role='Sigsoftmax: exp(z)*sigmoid(z) normalized over vocabulary; no added parameters; English RNN results are not native Japanese decoder replication'),
            dict(url='https://ojs.aaai.org/index.php/AAAI/article/view/17608',
                 role='High log-probability rank is neither necessary nor sufficient for lower test perplexity; rank is not an acceptance proxy')],
        novelty='Existing studies test CE, entropy penalties, softened labels, distillation, optimizers, readout adapters and embedding gradient interference; no sigsoftmax output-link learning was found. This changes normalized model probabilities at training and evaluation, not an entropy addend or inference-only decoding rescue.',
        limitation='A256-dimensional linear head can restrict attainable distributions, but this is not evidence that its rank causes current repetitions. Sigsoftmax is an established hypothesis, not novel mathematics, and does not guarantee coherent prose.',
        recipe=dict(output_probability='normalize_exp_raw_logit_times_sigmoid_raw_logit',
            effective_logits='FP32_raw_z_plus_logsigmoid_raw_z_exactly_once',
            loss='mean_hard_original_body_and_EOS_NLL_under_sigsoftmax_probabilities',
            supervision='same_original100M_gold_positions_once', coefficient_or_temperature=None,
            bias_or_shift_added=False, extra_parameters=0, teacher=False, decoder_forwards=1,
            attention_link='original_scaled_dot_product_softmax_unchanged',
            output_only=True, optimizer='fresh_AdamW_lr1e-5_wd0.1_constant', clip_norm=1.),
        parent=current['parent'], tokenizer=current['tokenizer'], tokenizer_sha256=current['tokenizer_sha256'],
        source_binding=current['source_binding'], goals=current['goals'], batch=48, seed=42,
        native_parameters=10001152, output_link_metadata_required=True,
        accounting='No extra labels, teacher compute, auxiliary positions or new corpus. Same original sampler/source/body/EOS/masks/digest/counters/fullsampler; NLL uses the new distribution and is not mislabeled plain-softmax CE.',
        fixed_weight_greedy='z+logsigmoid(z) is strictly increasing in real arithmetic. At fixed weights there is no mathematical change to greedy token order. A posthoc link cannot solve greedy repetition; useful changes must come from actual learning. FP32 finite/tie behavior must be tested.',
        inference_contract='Tagged checkpoints require the sigsoftmax factory for full/cache/padded and likelihood paths; old original model.py/export bytes remain frozen. Ordinary-softmax loading or double-link application is rejected by the new official paths. No current UI replacement before qualified Base.',
        resource=dict(total_GPU_cap_seconds=4800, probe_GPU_cap_seconds=180, CPU_preparation_cap_seconds=30,
            forecast='All32 actual postwarmup full-step mean times exact17698 updates times1.3 plus900 evaluation seconds, ceil; add actual probe, reject above4800. No median forecast or altered cap after results.'),
        required_gates=[
            'Independent normalized probability/NLL/analytical gradient and extreme finite-logit tests',
            'Original tied parameters/statekeys/optimizer/RNG unchanged; same-weight greedy order and padded/full/cache linked logits parity',
            'Original source/gold/EOS/fullsampler and committed saved4vs2+2 CPU state/history with wrong output-link metadata rejection',
            'Implement typed native evaluation/load and persistent probe/science/reviewer before actual GPU',
            'Own actual CUDA4vs2save+2 fullstate/history,48x1024 finite backward/memory and all32 measured timing budget',
            'Freeze one configuration; original100M/commonDEV256/Japanese192/331/1119/greedy80, all80 individual content judgments and exact historical score preservation'],
        quality='Reuse cached ordinary-softmax CE100M; all matchedCE/strong/absolute/historicalWeb gates unchanged. No rank/BPB/trainfit-only adoption. Qualification before independent learnedseed/fullDEV/protected finalTEST/adoption.',
        failure='Close on numerics/resume/metadata/capacity/budget or quality failure; no shift/temperature/learned calibration/variant/parent/LR/source/batch/backend/decoder/cap rescue or automatic extension.',
        implementation=dict(model=False, trainer=False, CPU_tests_run=False, GPU_probe=False, science=False, evaluator=False),
        new_GPU_seconds=0, scientific_gold_tokens=0, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False,
        next_action='Implement link/model/trainer and meaningful CPU checks, then typed persistent GPU/evaluation workflow; do not launch missing commands or claim rank changes prove model quality.'))
    print('Six-study evidence saved unchanged; prospective sigsoftmax fixed-link comparison defined; GPU0')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
