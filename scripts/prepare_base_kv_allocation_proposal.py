"""Define one fresh approximately10M attention/FFN allocation comparison."""
import copy
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, sha256, now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive


def ref(path):
    return dict(path=str(path), sha256=sha256(path))


def main():
    started = time.monotonic()
    phase = ROOT/'reports/phase6'
    run = phase/'base-kv-head-gradient-diagnostic-20261007'
    target = phase/'base_kv_allocation_proposal.json'
    if target.exists():
        raise ValueError('Preserve fixed allocation proposal')
    config_path = ROOT/'configs/phase6/base_kv_head_gradient_diagnostic.json'
    c = json.loads(config_path.read_text())
    r = json.loads((run/'result.json').read_text())
    job = json.loads((run/'job.json').read_text())
    if (job['status'] != 'complete' or alive(job) or not r['severe_interference_at_both_endpoints']
            or not all(all(e['native_checks'].values()) for e in r['endpoints'].values())
            or r['diagnostic_target_positions'] != 5064
            or r['optimizer_updates'] != 0 or r['scientific_CE_teachers'] != 0):
        raise ValueError('Actual terminal unchanged native head diagnostic required')
    base = torch.load(c['checkpoints']['parent']['path'], map_location='cpu', weights_only=False)['model_config']
    variants = dict(GQA=copy.deepcopy(base), MHA=copy.deepcopy(base))
    variants['MHA'].update(num_key_value_heads=4, intermediate_size=560,
        name='JMicro-10M-MHA4-FFN560-proposal', status='CPU_parameter_count_only')
    counts = {}
    for name, model_config in variants.items():
        with torch.device('meta'):
            model = JMicroModel(model_config)
        count = sum(p.numel() for p in model.parameters())
        if not 9900000 <= count <= 10100000:
            raise ValueError('Approximately10M total unique parameters required')
        model_config['expected_parameter_count'] = count
        counts[name] = count
        del model
    source = {}
    for name, endpoint in r['endpoints'].items():
        source[name] = {}
        for genre, s in endpoint['sources'].items():
            negative = [g for g in s['groups'] if min(
                g['combined']['first_head_norm']**2+g['combined']['dot'],
                g['combined']['second_head_norm']**2+g['combined']['dot']) < 0]
            source[name][genre] = dict(cosine=s['cosine'], cancellation_ratio=s['cancellation_ratio'],
                locally_opposed_groups=s['locally_opposed_groups'], native_sum_opposes_one_head=len(negative),
                shared_groups=len(s['groups']))
    if any(z['native_sum_opposes_one_head'] for e in source.values() for z in e.values()):
        raise ValueError('Inspect new head descent-direction evidence; fixed proposal assumption differs')
    proposal = dict(created_at=now(), status='fixed_attention_allocation_proposal_CPU_counted_not_GPU_learning',
        diagnostic=ref(run/'result.json'), diagnostic_config=ref(config_path), evidence_synthesis=c['evidence_synthesis'],
        proposal_source=ref(Path(__file__)), head_conflict_marker=source,
        causal_limit='Opposition/cancellation are local observations, but the summed gradient supports both head paths in all26 group/source aggregates. This does not justify head-PCGrad, prove GQA causality or guarantee MHA quality.',
        research_question='Does allocating parameters to four independent K/V heads instead of two shared heads improve unseen coherent Japanese generation at approximately10M total parameters and matched fresh data/training budgets?',
        variants=variants, actual_CPU_meta_parameter_counts=counts,
        parameter_count_difference=counts['MHA']-counts['GQA'], parameter_relative_difference=counts['MHA']/counts['GQA']-1,
        interpretation='Joint attention-versus-FFN allocation: KV2/FFN640 versus KV4/FFN560. Same13 layers/hidden256/query4/head64/Tokenizer4096/NoNorm/SwiGLU/RoPE1024/tied embeddings. Not isolated KV causality or exactly equal parameter count.',
        initialization='Both fresh seed42 models and fresh AdamW; no mature10B or rejected weights. Different parameter shapes change random draws; same seed does not imply identical initial tensors.',
        source_binding=c['source_binding'],
        data_policy='Same accepted2B original TRAIN/manifest and verified index identity. Same index-byte sampler and exact225M Web/60M textbook/15M story original body+EOS positions per arm. No dev/test learning, new corpus/Tokenizer training or full-corpus/dedup scans.',
        source_preparation='Implement CE-only sampling that preserves original index draws/body SHA/windows/masks/teacher positions while avoiding unused observed-pair extraction. Both fresh arms use its distinct explicit sampler protocol; no full-sampler identity claim against old InfoNCE metadata.',
        primary_teacher_tokens_per_arm=300000000, total_new_teacher_tokens=600000000, reused_old100M_control=False,
        accounting='Prepared2B unique supply differs from300M drawn positions per arm. Match same tokenizer/inputs/masks/source/EOS/bytes/physical/digest/full sampler between new arms; report native parameters and GPU cost separately.',
        optimizer=dict(kind='AdamW', peak_lr=.002, weight_decay=.1, gradient_clip=1., seed=42,
            schedule='Warmup by5M original gold positions; cosine over remaining295M to1e-5. LR follows committed target count, not guessed updates.'),
        probe=dict(total_GPU_cap_seconds=180, candidate_batches=[48,64,80,96,112], warmup_steps=3, timed_steps=5,
            worst_input_context=1024, worst_teacher_stride=512, resident_fraction=.9,
            required='Both native CUDA/BF16 finite forward/backward and own full continuous4 versus2+save/resume+2. Measure teacher and physical throughput separately. Stop larger candidates after first OOM; choose fastest measured common stable batch by combined predicted cost; discard probe weights.'),
        absolute_all_new_GPU_ceiling_seconds=9000,
        science_budget_rule='After actual probe only: sum ceil(300M/measured_median_original_teachers_per_second*1.3+900) for both arms plus actual prototype GPU <=9000s. Otherwise do not launch or raise the cap.',
        CPU_preparation_ceiling_seconds=30,
        evaluation='Same fixed DEV common256/472055bytes, BOS2/plain/greedy64 all80 per fresh arm, semantics192/JBLiMP331/JCQA1119. Old controls/strong/historical Web remain references, not fresh architecture controls. Individually read all160 new outputs under frozen unchanged rubric.',
        research_transition='Same relative coherence+8 and positive paired CI, EOS/rep nonworsening, relative1percent BPB and no empty-role-Unicode against fresh GQA. Research signal only: unchanged strong/absolute/historical Web and final independent seed/full DEV/protected TEST/adoption still required for Base.',
        final_Base_criteria_unchanged=True, protected_test_used=False, independent_human_review=False,
        failure_policy='One MHA4/FFN560 configuration. No KV/head/FFN/depth/width/Tokenizer/LR/source/checkpoint/epoch rescue or automatic teacher extension. Close allocation if research transfer screen fails. A positive signal needs a separate measured continuation contract, never automatic Base adoption.',
        completion='Actual exited bounded two-arm300M jobs, exact teacher/full native state/source accounting, own CUDA resume, fixed evaluations and all160 individual contents, comparisons/decision, negative evidence/UI restoration/local commit. Code/random weights/probe do not complete the study or Base.',
        literature=[dict(url='https://aclanthology.org/2023.emnlp-main.298/',
            meaning='Primary GQA efficiency/quality comparison at other scales; not proof of JMicro harm.'),
            dict(url='https://arxiv.org/abs/2001.06782',
            meaning='PCGrad concerns distinct task objectives; same-loss head paths and zero harmful sum-direction counts do not support automatic application.')],
        required_before_GPU_learning=['CE-only source parity and meaningful CPU state checks',
            'Own fresh trainer/runner/evaluator/reviewer and durable launcher',
            'Measured CUDA/BF16 stable batch and full save/resume for both native architectures',
            'Freeze science source/config/budget after actual protocol passes and process inspection'],
        implementation_status='Scientific commands not yet implemented; do not invoke nonexistent commands.',
        actual_GPU_learning_seconds=0, actual_scientific_teacher_tokens=0, actual_new_model_quality_evaluations=0,
        preparation_CPU_seconds=time.monotonic()-started, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False,
        next_action='Implement CE-only original source and fresh token-schedule trainer; verify source gold/byte identity and full state on CPU. Then implement durable paired-architecture CUDA probe. Do not start science from this proposal alone.')
    if proposal['preparation_CPU_seconds'] > 30:
        raise TimeoutError('Fixed CPU preparation budget exceeded')
    atomic_json(target, proposal)
    print(json.dumps(dict(status=proposal['status'], parameters=counts,
        parameter_difference=proposal['parameter_count_difference'], CPU_seconds=proposal['preparation_CPU_seconds'], new_GPU_learning=0)))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
