"""Bind actual CPU prototype evidence to the one previously recorded proposal."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import xml.etree.ElementTree as ET
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from hard_body_web_replay import POLICY

SOURCES = ('scripts/hard_body_web_replay.py', 'scripts/hard_body_web_replay_trainer.py',
    'scripts/hard_body_resident_web_replay_trainer.py', 'scripts/prepare_hard_body_web_replay.py',
    'scripts/record_hard_body_web_replay_preparation.py', 'tests/test_hard_body_web_replay.py',
    'tests/test_hard_body_web_replay_trainer.py')


def ref(relative):
    p = ROOT/relative
    return dict(path=str(p), sha256=sha256(p))


def main():
    proposal = ROOT/'reports/phase6/hard_body_web_replay_comparison_proposal.json'
    p = read_json(proposal)
    tests = ROOT/'reports/phase6/hard_body_web_replay_prototype_tests.xml'
    cases = list(ET.parse(tests).getroot().iter('testcase'))
    if len(cases) != 3 or any(c.find(k) is not None for c in cases for k in ('failure', 'error', 'skipped')):
        raise ValueError('All three actual CPU tests required')
    if p['main_ordinary_CE_teacher_tokens'] != 100000000 or p['settings_sweep_allowed'] or p['Base_complete']:
        raise ValueError('Preserve bounded Base-only proposal')
    target = ROOT/'reports/phase6/hard_body_web_replay_trainer_preparation.json'
    if target.exists():
        raise ValueError('Preserve own preparation')
    atomic_json(target, dict(status='actual_CPU_gold_CE_and_fullstate_fixture_passed_not_GPU_quality',
        created_at=now(), proposal=ref(proposal.relative_to(ROOT)), auxiliary_policy=POLICY,
        tests=ref(tests.relative_to(ROOT)), source_sha256={f:sha256(ROOT/f) for f in SOURCES},
        CPU_fixture=dict(continuous4_vs2plus2_all_state_equal=True, main_input_tokens=96,
            reference_input_tokens=64, parent_model_Adam_scheduler_RNG_actualLR_preserved=True,
            frozen_teacher_verified=True, separate_hard_targets_and_probability_mass_saved_resumed=True,
            all4_main_and_replay_input_protocols_equal_soft_control=True,
            corrupt_hard_target_count_and_soft_checkpoint_rejected=True),
        initial_failure=ref('reports/phase6/hard_body_web_replay_prototype_initial_failure.xml'),
        initial_failure_explanation='A generic teacher-body-logit permutation changed FP32 reduction rounding by9.5367431640625e-7; no production math changed. Retain original XML. Control teacher non-EOS mass exactly in FP32 with two different saturated body distributions, retain bitwise loss equality and exact-mass checks. Nondegenerate mass/actual-gold/mask/gradient tests also remain. No scientific acceptance changed.',
        CPU_test_seconds=sum(float(c.attrib['time']) for c in cases), actual_GPU_seconds=0,
        actual_scientific_teacher_tokens=0, newly_prepared_source_tokens=0,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        protected_test_used=False, quality_criteria_unchanged=True,
        next_action='Own runner/reviewer/durablePS and hard-target accounting; actualCUDA resume32 timings and save, then freeze only within new900s measured bound. Strong stagedCE quality screen remains mandatory.'))
    print('Actual CPU evidence and hard-target objective bound; no GPU work yet')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
