"""Freeze one future-target objective with unchanged original100M comparison."""
import json
from pathlib import Path
import sys
import time
import xml.etree.ElementTree as ET

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,now,sha256
from jmicro.training import atomic_json
from jmicro.model import JMicroModel
from phase6_performance import alive
from base_next_two_token_trainer import NextTwoHead,COEFFICIENT,AUXILIARY_SEED


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    started=time.monotonic();phase=ROOT/'reports/phase6';target=phase/'base_next_two_token_proposal.json'
    if target.exists():raise ValueError('Preserve single next-two proposal')
    closed_path=phase/'base_attention_saturation_completion.json';closed=json.loads(closed_path.read_text())
    if (closed['broad_saturation_at_both_learned_endpoints'] or not closed['fixed_diagnostic_closed']
            or alive(closed['actual_identity'])):raise ValueError('Actual closed negative attention assay required')
    tests=phase/'base_next_two_token_trainer_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites)!=5 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Actual five next-two CPU protocol checks required')
    old=json.loads((ROOT/'configs/phase6/base_label_smoothing_probe.json').read_text())
    parent=torch.load(old['parent']['path'],map_location='cpu',weights_only=False)
    with torch.device('meta'):
        native=JMicroModel(parent['model_config']);auxiliary=NextTwoHead(parent['model_config'])
    native_count=sum(p.numel() for p in native.parameters());aux_count=sum(p.numel() for p in auxiliary.parameters())
    if native_count!=10001152 or aux_count!=688896:raise ValueError('Actual native and train-only contextual block counts differ')
    marker='native_original_TRAIN_CE_next_two_contextual_auxiliary_v1'
    examined=0;matches=[]
    excluded={'base_next_two_token_trainer.py',Path(__file__).name}
    for folder,pattern in ((ROOT/'scripts','*.py'),(ROOT/'configs/phase6','*.json')):
        for candidate in folder.glob(pattern):
            if candidate.name in excluded:continue
            examined+=1
            if marker in candidate.read_text():matches.append(candidate.relative_to(ROOT).as_posix())
    if matches:raise ValueError('Potential previously registered future-head objective: '+repr(matches))
    result=dict(created_at=now(),status='fixed_next_two_auxiliary_proposal_CPU_verified_not_GPU_learning',
        previous_attention_completion=ref(closed_path),CPU_tests=ref(tests),
        source_references={name:ref(ROOT/name) for name in ('scripts/base_next_two_token_trainer.py',
            'scripts/prepare_base_next_two_token_proposal.py','tests/test_base_next_two_token_trainer.py',
            'src/jmicro/model.py','scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py')},
        parent=old['parent'],parent_size=old['parent_size'],parent_mtime_ns=old['parent_mtime_ns'],
        source_binding=old['source_binding'],tokenizer_sha256=old['tokenizer_sha256'],
        goals=old['goals'],payload=old['payload'],original_target_positions=100000000,
        control=dict(run=str(phase/'natural-context-contrast-comparison-20261007/CE'),
            checkpoint_sha256='f691a7587c03c51293a2e77889307da0efa18d2349c13e4f77439fd339586967',
            notes=ref(phase/'natural_context_contrast_CE_notes.json'),reused_without_GPU_or_regrading=True),
        research_question='Can gold supervision of the next-two token from the current original context encourage transferable sequential features while preserving the unchanged mature native next-token Base?',
        hypothesis='The learned model may fit local next-token likelihood without developing enough reusable context features. Future-gold supervision is a distinct objective from failed InfoNCE/ranking/UL/dropout/uniform smoothing; not a claim that this is the unique cause.',
        mechanism=dict(next_token_CE_weight=1.,next_two_CE_weight=COEFFICIENT,
            head='One fresh train-only native contextual Block plus final RMSNorm on the original final hidden sequence; shared native tied LM output matrix',
            auxiliary_seed=AUXILIARY_SEED,mask='Both current and following original target unmasked in same original1024/512 window; last target, overlap, padding, after-EOS and clipped goal targets excluded',
            teacher_policy='Only accepted original TRAIN gold; no generated targets, fabricated labels, dev/test, Chat roles or repeated Tokenizer training'),
        parameters=dict(native= native_count,train_only=aux_count,total_training=native_count+aux_count,
            deployed_native_unchanged=True,inference_hooks_or_auxiliary_heads=0),
        initialization='Same actual mature10B parent native tensors and inference/RNG as CE, fresh AdamW1e-5 WD.1 constant. Auxiliary CPU-only local seed/init preserves native CPU/CUDA RNG; include head parameters in one global clip/Adam.',
        accounting='Original100M/source75M20M5M/whole-body+EOS/windows/masks/bytes/input/physical/digest/full sampler/updates/LR equal cached CE. Next-two valid positions and EOS/body bytes/source counts, coefficient0.1 target mass and auxiliary physical hidden positions are additional, separately reported; future labels reuse original gold and are not independent new data. Total label/compute budgets differ from control; not evidence of superiority per equal total supervised positions.',
        batch=48,seed=42,CPU_preparation_cap_seconds=30,GPU_probe_cap_seconds=180,
        maximum_scientific_GPU_seconds=3965,
        science_budget_rule='Only after own CUDA/BF16 finite full shape, all native+aux model/Adam/scheduler/RNG/sampler/counters/history4 continuous versus2 saved/resumed2 and actual stable batch48: ceil(100M/measured_median_original_teacher_speed*1.3+900)<=3965. Freeze science cap from actual measurements; no cap increase or new control GPU.',
        probe_timing='Fixed3 warmup and32 timed original full-source updates, all included; exact first4 original stream and initialization/inference parity against original CE. Worst original1024/512 shape with real Adam state and90percent resident. No additional favourable timing subset or repeat.',
        evaluation='Same fixed DEV common256/472055bytes, BOS2/plain native greedy64 all80, semantics192/JBLiMP331/JCQA1119; every new80 individually read and raw-bound. Cached control80/strong/history unchanged.',
        research_and_adoption='Unchanged relative coherence+8 and positive paired CI, EOS/rep nonworsening,1percent BPB/no errors versus cached CE; also unchanged strong/absolute/historical Web. Only eligible quality candidate proceeds to independent learned seed/full DEV/protected TEST/adoption; researcher marker or native code is not Base completion.',
        failure_policy='One next-two contextual head/coefficient0.1. On failed protocol/budget/transfer, close this fixed condition. No horizon/coefficient/head sharing/architecture/LR/source/parent/epoch/teacher rescue or automatic extension.',
        completion='Persisted exited native GPU100M, exact all original and auxiliary state/counters, own real CUDA resume, same fixed metrics and all80 content, unchanged gate review, evidence archive/UI restoration/local commit. Stop and notify only actual qualified Base; no Chat/quantization.',
        literature=dict(url='https://arxiv.org/html/2404.19737v1',
            evidence='Primary paper reports improved induction in some small children-story settings; also worse small300M-scale code models and disappearing benefits with books mixture.',
            limitations='Their sizes include nonembedding parameter labels, training may use up to90epochs and a test-metric epoch oracle, and parameter-matched trunk/head allocation differs. Not10M total Japanese evidence, no protected-test tuning/epoch oracle or exact replication here.'),
        local_novelty_scope=dict(top_level_files_examined=examined,exact_marker_matches=matches),
        implementation_status='Core train-only head/trainer and five CPU checks implemented. Dedicated CUDA probe, scientific runner/evaluator/reviewer not yet implemented; do not invoke absent commands.',
        actual_GPU_learning_seconds=0,scientific_teacher_positions=0,new_model_quality_evaluations=0,
        preparation_CPU_seconds=time.monotonic()-started,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Implement own persisted next-two CUDA probe with real native inference/RNG, full auxiliary state resume, original control stream parity and all32 timings; measure before science runner/config freeze.')
    if result['preparation_CPU_seconds']>30:raise TimeoutError('Fixed CPU30s preparation exceeded')
    atomic_json(target,result)
    print(json.dumps(dict(status=result['status'],parameters=result['parameters'],CPU_seconds=result['preparation_CPU_seconds'],GPU_learning=0)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
