"""Freeze one EOS-component ablation and retain the stronger staged quality baseline."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import copy
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from eos_decoupled_web_kl_preservation import POLICY

SOURCES = ('scripts/eos_decoupled_web_kl_preservation.py','scripts/eos_decoupled_web_kl_condition_trainer.py',
    'scripts/eos_decoupled_resident_web_kl_trainer.py','scripts/prepare_eos_decoupled_web_kl.py',
    'scripts/propose_eos_decoupled_web_kl_comparison.py','tests/test_eos_decoupled_web_kl_preservation.py',
    'tests/test_eos_decoupled_web_kl_condition_trainer.py')


def ref(relative):
    path = ROOT/relative
    return dict(path=str(path),sha256=sha256(path))


def main():
    diagnostic = read_json(ROOT/'reports/phase6/web_kl_EOS_component_diagnostic.json')
    if diagnostic['windows'] != 16 or diagnostic['soft_body_positions'] != 16320 or diagnostic['GPU_seconds'] or diagnostic['CPU_elapsed_seconds'] > 180:
        raise ValueError('Actual fixed CPU diagnostic required')
    for path,digest in diagnostic['source_sha256'].items():
        if sha256(ROOT/path) != digest:
            raise ValueError('Preserve actual diagnostic implementation')
    old = ROOT/'reports/phase6/web_kl_comparison_proposal.json'
    p = copy.deepcopy(read_json(old))
    completion = read_json(ROOT/'reports/phase6/web_kl_comparison_completion.json')
    p.update(status='conditional_non_EOS_KL_CPU_prototype_verified_GPU_not_started',created_at=now(),
        rationale='The failed full parent-KL pilot retains natural-body BPB but regresses EOS40 vs76 and coherence9 vs23. Fixed16 train-window decomposition finds stagedEOS mass mean .010818 vs parent .001814; fullKL directly penalizes EOS-mass changes. Test only removal of that Bernoulli component while retaining the exact (1-parentEOS)*conditional non-EOS KL. Small train/CPU evidence is not sole-cause or quality proof.',
        diagnostic=ref('reports/phase6/web_kl_EOS_component_diagnostic.json'),
        KL_policy=POLICY,source_sha256={path:sha256(ROOT/path) for path in SOURCES},
        CPU_prototype_tests=ref('reports/phase6/eos_decoupled_web_kl_prototype_tests.xml'),
        initial_test_failure=ref('reports/phase6/eos_decoupled_web_kl_prototype_initial_failure.xml'),
        previous_proposal=ref('reports/phase6/web_kl_comparison_proposal.json'),
        previous_related_completed_study=ref('reports/phase6/web_kl_comparison_completion.json'),
        previous_related_study_all_GPU_seconds=completion['all_GPU_seconds'],
        primary_mechanism_comparison='New conditional non-EOS KL vs cached full parentKL; same parent/model/Adam/RNG/scheduler/LR/order/100M CE/main and auxiliary input windows. Removing the Bernoulli EOS component also reduces supervised probability mass, which is reported separately.',
        quality_screen_baseline='Original staged CE control remains mandatory: coherence23+8, pairedCI lower>0, EOS>=76, repetition<=2, same BPB1percent; also all absolute and historicalWeb guards. Do not substitute the poorer fullKL9/40/22 result to ease adoption.',
        reference_probability_mass_accounting='Record cumulative parent non-EOS probability mass over all masked body targets separately in history/checkpoints/reviews. Never count discarded EOS probability mass as new CE/corpus tokens.',
        primary_effect_not_isolated_from_probability_mass='Same100M CE/referenceinput25,133,056 and body position windows for the mechanism comparator; removed EOS component changes target probability mass. The staged CE quality baseline has no auxiliary replay and is not equal total supervision.',
        new_research_GPU_ceiling_seconds=900,
        previous_related_GPU_is_not_current_verification='Previous study401.475919s remains reported as prior evidence/cost; the new fixed objective-component comparison has its own900s bound, actualCUDA probe and unchanged margin. Never enlarge a failed/repaired run cap.',
        next_action='Implement own runner/reviewer/durablePS, reference probability-mass accounting and two cached controls. Preserve stronger original staged quality screen. Inspect existing processes, verify actualCUDA full continuous4 vs2+2 including new mass and both samplers, measure32 combined timings/save and freeze100M science only within900 new GPU seconds. No coefficient/temperature/order/source/LR/batch sweeps.')
    p.pop('registered_preexisting_configs_checked',None)
    p.pop('registered_preexisting_KL_matches',None)
    p['novelty_limit'] = 'One EOS objective-component ablation of the actual failed parent-KL study; no broad config/corpus search.'
    run = ROOT/'reports/phase6/web-kl-comparison-v3-20261006'
    p['mechanism_full_KL'] = dict(config=ref('configs/phase6/web_kl_comparison_v3.json'),
        result=ref('reports/phase6/web-kl-comparison-v3-20261006/compare-result.json'),
        review=ref('reports/phase6/web_kl_comparison_v3_review.json'),
        notes=ref('reports/phase6/web_kl_notes.json'),
        generation=ref('reports/phase6/web-kl-comparison-v3-20261006/evaluation/web_kl/evaluation/generation.json'),
        checkpoint=completion['checkpoint'],
        history=ref('reports/phase6/web-kl-comparison-v3-20261006/web_kl/training/metrics.jsonl'))
    p['required_before_science'].append('Actual CUDA restart gate includes retained probability-mass ledger; no teacher/student EOS objective coupling introduced by implementation.')
    p['terminal_evidence'].extend([
        'All3068 main and reference input digests/counters/cursors equal cached fullKL; losses/gradients/time may differ by design.',
        'Report fullKL mechanism difference and stagedCE quality screen separately; all preexisting stronger quality requirements remain mandatory.',
        'Record parent non-EOS teacher probability mass with exact save/resume accounting; no new corpus volume.'])
    target = ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_proposal.json'
    prepared = ROOT/'reports/phase6/eos_decoupled_web_kl_trainer_preparation.json'
    if target.exists() or prepared.exists():
        raise ValueError('Preserve frozen own proposal/preparation')
    atomic_json(target,p)
    atomic_json(prepared,dict(status='actual_CPU_math_and_fullstate_fixture_passed_not_GPU_quality_evidence',created_at=now(),
        proposal=ref('reports/phase6/eos_decoupled_web_kl_comparison_proposal.json'),
        diagnostic=ref('reports/phase6/web_kl_EOS_component_diagnostic.json'),
        tests=p['CPU_prototype_tests'],source_sha256=p['source_sha256'],
        CPU_fixture=dict(continuous4_vs2plus2_all_state_equal=True,main_input_tokens=96,reference_input_tokens=64,
            parent_Adam_model_RNG_and_actualLR_preserved=True,frozen_teacher_verified=True,
            new_probability_mass_saved_resumed_and_history_equal=True),
        initial_failure='Identical logits produced -1.8694e-8 KL from subtracting FP32 normalizers; preserved XML. Compute teacher conditional logsoftmax directly, preserving the exact mathematical component and exact-zero identical-logit check. Tests not weakened.',
        actual_GPU_seconds=0,actual_scientific_teacher_tokens=0,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        next_action=p['next_action']))
    print('One conditional non-EOS KL comparison proposed; cached fullKL for mechanism, stronger stagedCE for quality; no GPU/science started')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
