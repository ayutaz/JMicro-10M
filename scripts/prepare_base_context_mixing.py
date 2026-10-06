"""Freeze a bounded original-gold history-mixing comparison after CPU checks."""
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive


def main():
    phase = ROOT/'reports/phase6'
    target = phase/'base_context_mixing_proposal.json'
    if target.exists(): raise ValueError('Preserve the fixed history-mixing proposal')
    tests = phase/'base_context_mixing_trainer_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) != 9 or any(
            int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Nine actual CPU checks required')
    finished = read_json(phase/'base_muon_comparison_completion.json')
    muon_job = read_json(phase/'base-muon-comparison-20261007/job.json')
    if (muon_job['status'] != 'complete' or alive(muon_job) or
            finished['eligible_for_final_Base_validation'] or not finished['fixed_Muon_condition_closed']):
        raise ValueError('Finish and close the previous actual scientific condition first')
    previous = read_json(ROOT/'configs/phase6/base_muon_comparison.json')
    references = {}
    for name in ('base_muon_comparison_review.json','base_muon_comparison_completion.json',
                 'base_decode_cached_evidence_review.json','root_cause_summary.json',
                 'sequence_objective_comparison_review.json','sequence_objective_low_alpha_review.json',
                 'sequence_objective_diagnostic_completion.json','base_preference_comparison_review.json',
                 'base_generalization_diagnostic_review.json','base_next_two_token_comparison_review.json'):
        path = phase/name
        record = read_json(path)
        references[name] = dict(path=str(path), sha256=sha256(path), status=record['status'])
    sources = ('scripts/base_context_mixing_trainer.py','scripts/prepare_base_context_mixing.py',
               'tests/test_base_context_mixing_trainer.py','scripts/natural_context_contrast_corpus.py',
               'scripts/natural_context_contrast_trainer.py','src/jmicro/model.py','uv.lock')
    proposal = dict(created_at=now(), status='CPU_protocol_verified_GPU_comparison_not_started',
        previous_goal_turn='Progress: Muon100M terminal, all80 scored, rejected, UI restored, local commit423fba4.',
        hypothesis='Does training on a small proportion of model-predicted history, while retaining original gold labels, reduce native greedy repetition and improve coherent continuations?',
        rationale='Cached FP32 and BF16 generation both repeat; raw numerical failures remain failures. Do not rerun that diagnosis. Previous sequence UL penalized generated repeats; this mechanism instead changes CE conditioning inputs and supplies original gold next-token gradients.',
        mechanism=dict(prediction_passes=1, mixing_probability=.05,
            prediction='No-gradient clean-context greedy prediction restricted to IDs>=8',
            shift='Prediction at input position j-1 may replace original body input position j',
            boundaries='Preserve input position0, PAD and all original special IDs; no new EOS/BOS or fragment',
            supervision='Every original body/EOS target stays unchanged, supervised exactly once',
            RNG='Dedicated CPU Generator; full state restored with model/AdamW/scheduler/global RNG/sampler',
            objective='Original-gold CE given the mixed history; no UL, contrastive loss, distillation or added head'),
        parent=previous['parent'], source_binding=previous['source_binding'], goals=previous['goals'],
        tokenizer=previous['tokenizer'], tokenizer_sha256=previous['tokenizer_sha256'], batch=48, seed=42,
        optimizer='Fresh AdamW lr1e-5/weight_decay0.1; constant scheduler, matching cached CE',
        native_parameters=10001152, extra_parameters=0, original_gold_teacher_tokens=100000000,
        extra_supervised_targets=0, new_unique_dataset_tokens=0,
        cached_control=dict(path=str(ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/result.json'),
            sha256=sha256(ROOT/'reports/phase6/natural-context-contrast-comparison-20261007/result.json'),
            no_GPU_rerun=True, no_rescoring=True),
        budgets=dict(CPU_preparation_seconds=60, CUDA_probe_seconds=180, total_GPU_seconds=7200,
            science_budget='Ceil(100M/measured median original teachers per second*1.3+900); plus actual probe must fit total cap',
            accounting='Prediction forwards/input positions are additional compute, not teachers; original clean CE input/digest and full sampler match cached CE. Report mixed-input digest and actual replacements separately.'),
        acceptance='Native CUDA/BF16 worst1024/512 batch48 finite forward/backward and full continuous4 vs2+save/resume+2, including dedicated mixing RNG, exact source and committed history, before any science. Then complete100M, common256-document BPB, Japanese192/331/1119 and all80 individually read raw-bound continuations. All matched CE/strong/absolute/historical Web gates unchanged. Only qualified candidates proceed to independent trainedseed/full DEV/protected final TEST/adoption.',
        failure='Close failed finite/state/budget or final quality condition. No mixing probability/pass/decoder/LR/source/parent/batch/teacher/cap rescue or automatic extension.',
        primary_sources=['https://arxiv.org/abs/1906.04331','https://aclanthology.org/P19-2049/','https://arxiv.org/abs/1511.05101'],
        limitations='Fixed greedy one-pass variant, not a full sequential sampled rollout or a likelihood-consistent objective. Replaced histories can contradict original gold, especially names/numbers; byte-piece replacements may lack a standalone valid UTF8 rendering. Papers on other tasks do not prove Japanese10M benefit. One seed/mature parent/repeated nonblind DEV. Additional compute differs from cached CE.',
        references=references, source_sha256={s:sha256(ROOT/s) for s in sources},
        CPU_tests=dict(path=str(tests),sha256=sha256(tests),passed=9),
        initial_fixture_failure=dict(path=str(phase/'base_context_mixing_initial_fixture_failure_tests.xml'),
            sha256=sha256(phase/'base_context_mixing_initial_fixture_failure_tests.xml'),
            cause='Repeated-character tied random fixture copied all selected inputs; no changed-input coverage. Preserved failed receipt; stress predictor now has stronger attention output while preserving tied weights and the original assertion.'),
        actual_GPU_seconds=0, scientific_teacher_tokens=0, protected_test_used=False,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        next_action='Implement one durable bounded CUDA probe/launcher and science/reviewer commands; freeze their configs before executing. GPU training is not authorized by unimplemented commands alone.')
    atomic_json(target, proposal)
    print(json.dumps(dict(status=proposal['status'],CPU_tests=9,GPU_seconds=0,total_future_GPU_cap_seconds=7200)))


if __name__=='__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
