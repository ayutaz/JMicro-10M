"""Fix an independent fresh residual-connectivity comparison before GPU work."""
import copy
from pathlib import Path
import sys
import time
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive
from base_parallel_residual_model import POLICY, parallel_config, model_from_config


def main():
    started = time.monotonic()
    phase = ROOT/'reports/phase6'
    destination = phase/'base_parallel_residual_proposal.json'
    if destination.exists():
        raise ValueError('Preserve prospective residual comparison')
    previous = read_json(phase/'base_output_mixture_comparison_completion.json')
    if (previous['eligible_for_final_Base_validation'] or not previous['fixed_output_mixture_condition_closed']
            or alive(previous['actual_identity'])):
        raise ValueError('Previous exact MoC/MoS comparison must remain rejected and exited')
    old = read_json(phase/'base_kv_allocation_proposal.json')
    native = copy.deepcopy(old['variants']['GQA'])
    with torch.device('meta'):
        counts = {arm:sum(p.numel() for p in model_from_config(config).parameters())
                  for arm,config in dict(sequential=native,parallel=parallel_config(native)).items()}
    if set(counts.values()) != {10001152}:
        raise ValueError('Both exact native10M counts required')
    core = ROOT/'src/jmicro/model.py'
    if sha256(core) != '298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83':
        raise ValueError('Frozen native model bytes changed')
    references = {name:dict(path=str(phase/name),sha256=sha256(phase/name)) for name in (
        'base_output_mixture_comparison_completion.json','base_output_mixture_comparison_review.json',
        'architecture_comparison_review.json','base_capacity_reference_synthesis.json',
        'base_relu_squared_proposal.json','base_relu_squared_probe_completion.json',
        'base_kv_allocation_proposal.json','base_failure_route_synthesis.json')}
    elapsed = time.monotonic()-started
    if elapsed > 30:
        raise TimeoutError('Prospective CPU preparation30s exhausted')
    atomic_json(destination,dict(created_at=now(),status='prospective_fresh_residual_connectivity_comparison',
        question='Does parallel Attention/FFN connectivity improve Japanese Base learning at identical10M matrix, original2B gold and initialization budgets?',
        novelty='Completed depth/width/FFN allocation and learned MoC/MoS remain closed. No parallel residual block/config/training was found in registered sources/proposals. Change only the within-block FFN input; no width/depth/activation/normalization gain/teacher rescue.',
        primary_sources=['https://arxiv.org/html/2204.06745v1#S2.SS1.SSS2',
            'https://github.com/EleutherAI/gpt-neox/blob/main/megatron/model/transformer.py'],
        source_limitation='NeoX describes mainly distributed communication efficiency and comparable early losses. This single4090 RMSNorm/SwiGLU/GQA adaptation preserves native initialization; it is not a faithful20B reproduction or Japanese quality/speed proof.',
        variants=dict(sequential=native,parallel=parallel_config(native)),policy=POLICY,
        parameters_each=10001152,additional_parameters=0,physical_and_logical_blocks=13,
        initialization='Fresh seed42 native scaffold with identical every matrix/RMS gain; optimizer/RNG/sampler fresh. No learned parent or verification weights are used; initial predictions need not match across different functions.',
        source_binding=old['source_binding'],tokenizer='artifacts/phase2/4096/tokenizer.model',
        tokenizer_sha256='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318',
        goals=dict(web=1500000000,textbook=400000000,story=100000000),
        original_gold_each=2000000000,scientific_gold_total=4000000000,new_unique_corpus_tokens=0,
        sampler='Original full TRAIN body/EOS1024/512 windows with CEOnlyOriginalSampler; keep accepted binding/stat, no full13GB corpus scan',
        optimizer=dict(kind='fresh_AdamW',peak_lr=.002,final_lr=1e-5,warmup_gold=5000000,
            schedule='completed-update teacher-position warmup then cosine',weight_decay=.1,
            betas=[.9,.999],eps=1e-8,gradient_clip=1.,seed=42,batch=80),
        resource=dict(CPU_preparation_cap_seconds=30,own_probe_GPU_cap_seconds=180,
            total_GPU_cap_seconds=86400,fixed_batch=80,capacity_shape=[80,1024],stride=512,
            forecast='For each arm ceil(2B*SUM all32 postwarmup step seconds/SUM all32 original gold*1.3+900); sum plus own actual probe<=86400. Include data waits. No median-based forecast or budget rescue.',
            rationale='New24h maximum fixes a full fresh2B paired connectivity comparison before timing. Old MHA/ReLU_squared300M caps and refusals stay closed. This is a ceiling, not a measured completion estimate.',
            checkpoint_updates=2000,heartbeat_updates=20),
        required_before_science=['Independent block formula, identical full initial matrices/count/tie/RNG, causal/padded/fast/cache/tagged reconstruction CPU checks',
            'Fresh original sampler/trainer/typed evaluator/persistent own GPU probe/science/reviewer implemented before execution',
            'Both actual CUDA continuous4vs2save+2 full optimizer/schedule/RNG/sampler/history/finite checks',
            'Own80x1024/512 BF16/Flash finite backward/resident90percent and all32 timing within fixed24h',
            'Freeze scientific source/quality policy before any training outcomes'],
        evaluation='Each terminal2B: unchanged commonDEV256 bytes/all192-331-1119 Japanese/native greedy64/BOS2/EOS3/all80 each; all160 individually raw-bound',
        controls='New fresh sequential2B is mandatory. Completed mature CE/strong/historical Web are additional references, never substitute for fresh paired control.',
        selection='All original matched/strong/absolute/historical Web conditions unchanged, including coherence+8/paired95percent lower>0/grammar56/coherence27/completion27/EOS37/repetition<=18/no errors. Independent trainedseed/fullDEV/protectedTEST/adoption only for a qualified candidate.',
        failure='Close this exact parallel connectivity/init/source/LR/batch/backend/decoder/token/GPU-cap recipe if finite, budget or quality gates fail; no tied-norm/gain/layer-count/seed/parent/timing-window rescue or automatic extension.',
        limitations='One initialization/training seed and reused nonblind DEV. Same raw matrices differ in initial function, and same teacher counts differ in gradient dynamics. No prior evidence proves sequential FFN dependence causes repetition or that2B suffices.',
        references=references,CPU_preparation_seconds=elapsed,new_GPU_seconds=0,scientific_gold_tokens=0,
        trainer_implemented=False,evaluator_implemented=False,GPU_workflow_implemented=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        next_action='CPU model/protocol checks, then implement fresh trainer and typed durable workflow; own measured CUDA gate before prospective science freeze/launch.'))
    print('Fresh parallel residual contract fixed; both exact10M; GPU0/science0')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
