"""Define one fresh equal-parameter FFN comparison before implementation/GPU."""
import copy
import sys
import time
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    started = time.monotonic()
    output = ROOT / 'reports/phase6/base_relu_squared_proposal.json'
    if output.exists():
        raise ValueError('Preserve prospective FFN proposal')
    phase = ROOT / 'reports/phase6'
    old = read_json(phase / 'base_kv_allocation_proposal.json')
    closed = read_json(phase / 'base_kv_allocation_probe_completion.json')
    if (not closed['fixed_300M_allocation_protocol_closed'] or closed['science_budget_eligible']
            or closed['scientific_teacher_positions'] or alive(closed['actual_identity'])):
        raise ValueError('Old MHA allocation remains closed, untrained and absent')
    native = copy.deepcopy(old['variants']['GQA'])
    with torch.device('meta'):
        count = sum(p.numel() for p in JMicroModel(native).parameters())
    if count != 10001152 or native['intermediate_size'] != 640:
        raise ValueError('Original native GQA/FFN640 count required')
    if 3 * 256 * 640 != 2 * 256 * 960:
        raise ValueError('Exact FFN matrix budget required')
    references = {}
    for name in ('base_recurrent_compute_novelty_review.json', 'base_kv_allocation_proposal.json',
                 'base_kv_allocation_probe_completion.json', 'base_kv_allocation_bucketed_completion.json',
                 'base_completed_objective_studies_v3_20261007.json'):
        path = phase / name
        references[name] = dict(path=str(path), sha256=sha256(path))
    elapsed = time.monotonic() - started
    if elapsed > 30:
        raise TimeoutError('Prospective preparation30s exhausted')
    atomic_json(output, dict(created_at=now(), status='prospective_fresh_equal_parameter_FFN_comparison',
        question='Does two-projection squared-ReLU improve Japanese Base learning over SwiGLU at the exact same10M parameter and300M original-gold budget?',
        primary_source=dict(url='https://arxiv.org/html/2109.08668v2',
            sections='3 Squared ReLU/Figure6 and A.7 insertion/ablation',
            meaning='Primary isolated activation and GLU comparisons motivate a test. Full Primer includes QKV convolution; no4X speedup or Japanese10M success is inferred.'),
        novelty='No squared-ReLU FFN training code/config/completion found. Different FFN function and parameter topology, not old MHA/KV or gated recurrence tuning.',
        variants=dict(SwiGLU=native, ReLU_squared=dict(activation='relu_squared',
            intermediate_size=960, expected_parameter_count=10001152,
            formula='down_proj(relu(up_proj(x))**2)', projections=2, bias=False)),
        unique_parameters_per_arm=count, physical_blocks=13, logical_invocations=13,
        paired_initialization='Fresh seed42 native scaffold; identical non-FFN weights. Replace candidate FFNs with independently seeded fresh normal(.02) matrices in a CPU fork_rng, preserving scaffold RNG. No learned parent or probe weights.',
        source_binding=old['source_binding'], tokenizer='artifacts/phase2/4096/tokenizer.model',
        tokenizer_sha256='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318',
        goals=dict(web=225000000, textbook=60000000, story=15000000),
        original_gold_per_arm=300000000, scientific_gold_across_arms=600000000,
        new_unique_dataset_tokens=0, sampler='CEOnlyOriginalSampler, original full-unit1024/512 windows and body+EOS once',
        optimizer=dict(kind='fresh_AdamW', peak_lr=.002, final_lr=1e-5, warmup_gold=5000000,
            schedule='end-of-completed-update gold-position warmup then cosine', weight_decay=.1,
            gradient_clip=1., seed=42, batch=80),
        resource=dict(CPU_preparation_cap_seconds=30, probe_GPU_cap_seconds=180,
            total_GPU_cap_seconds=14400, fixed_batch=80, warmup_updates=3, timed_updates=32,
            forecast='For each arm use total seconds / total original targets across all32 measured updates; ceil(300M*seconds_per_target*1.3+900), add actual probe; reject above14400. Timing is an early bounded estimate, not actual completion time.',
            rationale='Separate prospective FFN study. Old paired GQA/MHA forecast12145.5s exceeded its9000s and stays closed/untrained. New4h cap is fixed before this implementation/probe; it does not reopen MHA or assert this FFN fits.'),
        required_before_science=['Actual exact10M counts/paired non-FFN initialization and independently checked activation/gradients',
            'Full/padded/causal/fast/cache and tagged checkpoint factory; no stock export claim',
            'Both original source masks/EOS/counters/schedule and saved4vs2+2 full-state/history CPU',
            'Persistent runner/evaluator/reviewer implemented before GPU learning',
            'Own CUDA4vs2save+2 per arm,80x1024/512 finite BF16 backward, all32 timing and measured budget'],
        evaluation='Same commonDEV256/472055bytes, semantics192/JBLiMP331/JCQA1119 and original BOS/native greedy64/EOS3 all80 per arm. Read all160 and retain old identical ratings. Native factory must reconstruct correct FFN.',
        controls='Fresh paired SwiGLU control required. Mature cached100M/strong/historical Web only additional quality references, never substitutes for fresh control.',
        selection='Existing relative+8 coherent/paired95%lower>0/EOS and repetition nonworsening/BPB/errors, strong staged, absolute and historical Web gates unchanged. All must qualify before independent trainedseed/fullDEV/protectedTEST/adoption.',
        failure='One exact two-projection960 architecture. No activation/gain/norm/bias/convolution/width/LR/source/Tokenizer/seed/checkpoint/batch/precision/backend/cap rescue or automatic extension. No positive claim from train loss, random weights or timing.',
        limitations='Changes FFN function and latent width jointly while exactly matching parameters. Fresh300M is an initial research comparison, not sufficient training assumed or proof of10M capacity. One seed and reused nonblind DEV cannot establish final quality.',
        references=references, CPU_preparation_seconds=elapsed,
        implementation=dict(model=False, trainer=False, evaluator=False, GPU_workflow=False),
        new_GPU_seconds=0, scientific_gold_tokens=0, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False,
        next_action='Implement tagged paired model/trainer and meaningful CPU invariants; implement durable typed GPU workflow only after CPU passes. No scientific launch from proposal alone.'))
    print('Prospective fresh equal10M FFN study fixed; old MHA closure retained; new GPU0')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
