"""Fix one new optimizer comparison before implementation or outcomes."""
import sys
from pathlib import Path
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src')]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json


def main():
    output = ROOT / 'reports/phase6/base_ademamix_proposal.json'
    if output.exists():
        raise ValueError('Preserve prospective recipe')
    old = read_json(ROOT / 'configs/phase6/base_muon_probe.json')
    atomic_json(output, dict(created_at=now(), status='prospective_new_dual_gradient_EMA_comparison',
        question='Does combining fast and slow gradient memories improve coherent Japanese prose while retaining Web quality, against the same-parent cached AdamW100M?',
        rationale='Seven recent objective interventions failed coherence and retention. Muon and SAM are completed different optimizer transformations. Search found no AdEMAMix/dual gradient EMA training. Negative old algorithms are not proof that all optimizer changes fail.',
        primary_sources=['https://arxiv.org/html/2409.03137v2',
                         'https://github.com/apple/ml-ademamix/blob/main/pytorch/ademamix.py'],
        evidence_scope='Paper section3/Algorithm1/A.1 and official implementation specify corrected fast EMA, uncorrected slow EMA and second-moment denominator. Other models/data report slower forgetting. This does not prove Japanese10M improvement or2x GPU speed.',
        parent=old['parent'], parent_size=old['parent_size'], parent_mtime_ns=old['parent_mtime_ns'],
        source_binding=old['source_binding'], goals=old['goals'], tokenizer=old['tokenizer'],
        tokenizer_sha256=old['tokenizer_sha256'], control_CE=old['control_CE'],
        native_parameters=10001152, extra_model_parameters=0, native_inference_unchanged=True,
        optimizer=dict(kind='fresh_all_parameter_AdEMAMix', lr=1e-5, weight_decay=.1,
            betas=[.9, .999, .9999], alpha=2., epsilon=1e-8,
            alpha_warmup_updates=1000, beta3_half_life_warmup_updates=1000,
            schedule='alpha linear0to2; beta3 interpolated half-life from beta1to.9999 as official formula including1e-8; thereafter fixed',
            slow_EMA_bias_correction=False, fast_EMA_bias_correction=True,
            choice='Official alpha2/betas defaults. Fixed1000-update transition fits the known17698-update stream; chosen before measurements, not tuned to quality. Same nominal LR/WD/clip as cached control; effective step magnitudes differ.'),
        seed=42, batch=48, original_gold_tokens=100000000,
        new_unique_dataset_tokens=0, TRAIN_only=True, accepted_data_rescan=False,
        resource=dict(CPU_proposal_cap_seconds=30, probe_GPU_cap_seconds=180,
            total_GPU_cap_seconds=4800, warmup_updates=3, timed_updates=32,
            forecast='ceil(100M*sum(all32stepseconds)/sum(all32gold)*1.3+900) plus actual probe <=4800. All steps count; no fastest subset/order-cache architecture claim.'),
        prerequisites=['Independent scalar/vector optimizer formula/alpha0AdamW/half-life/slow-no-bias verification',
            'All native parameters once; original masks/EOS/draws/full source identical; native tensors/logits/RNG initially equal',
            'CPU and own CUDA continuous4 versus2save+2 all model/optimizer/scheduler/RNG/sampler/counters/history',
            'Longer small-vector resume across1000 warmup boundary; wrong recipe/shape/step/nonfinite/partial-update refusal',
            'Persistent scientific runner/evaluator/reviewer before science and measured finite maximum1024/512 BF16 backward'],
        evaluation='Same commonDEV256/472055bytes and semantics192/JBLiMP331/JCQA1119/native greedy64/Base80 raw-bound individual content. Reuse actual cached100MCE, strong staged and historical Web. Preserve all matched/strong/absolute/retention criteria.',
        final_Base='Only a qualifying candidate proceeds to independent trained seed/full DEV/protected final TEST/adoption. Stop and notify on qualified Base completion.',
        failure='One exact recipe; no alpha/beta/warmup/LR/WD/parent/data/teacher/batch/precision/backend/decoder/cap rescue, automatic extension or reopening closed FFN/MHA.',
        limitations='One conservative-LR mature-parent transition, one seed/repeated nonblind DEV. Slow memory changes direction and magnitude; not isolated equal-norm updates or causal forgetting proof. No new source/data, Chat or quantization.',
        historical_evidence={name: dict(path=str(ROOT / 'reports/phase6' / name),
            sha256=sha256(ROOT / 'reports/phase6' / name)) for name in
            ('base_completed_objective_studies_v3_20261007.json', 'base_muon_comparison_completion.json',
             'base_sam_comparison_completion.json', 'base_storage_reader_completion_20261007.json')},
        implementation_complete=False, new_GPU_seconds=0, new_scientific_gold_tokens=0,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False,
        next_action='Implement optimizer/trainer and independent CPU/state checks; no learning launched by proposal.'))
    print('Prospective single AdEMAMix100M/4800s recipe; GPU0; Base incomplete')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
