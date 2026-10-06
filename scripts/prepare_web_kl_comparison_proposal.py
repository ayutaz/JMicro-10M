"""Define one retention-objective comparison after the paired-loss diagnostic."""
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from web_kl_preservation import POLICY


def reference(path):return dict(path=str(path),sha256=sha256(path))


def main():
    target=ROOT/'reports/phase6/web_kl_comparison_proposal.json'
    if target.exists():raise ValueError('Preserve existing proposal')
    diagnostic=ROOT/'reports/phase6/source_order_followup_diagnostic.json'
    d=read_json(diagnostic); summary=d['common_byte_summary']
    if (d['GPU_seconds'] or d['scientific_teacher_tokens'] or d['CPU_seconds']>30
            or summary['documents']!=256 or summary['body_NLL_change']['worsened']!=256
            or summary['gold_EOS_NLL_change']['improved']!=216):
        raise ValueError('Actual broad body-loss/stop tradeoff required')
    c=read_json(ROOT/'configs/phase6/source_order_condition_comparison_v2.json')
    run=ROOT/'reports/phase6/source-order-condition-comparison-v2-20261006'
    job=read_json(run/'job.json');result=read_json(run/'compare-result.json');review=read_json(run/'review.json')
    if job['status']!='complete' or alive(job) or review['eligible_for_final_Base_validation']:
        raise ValueError('Actual completed rejected source-order control required')
    matches=[];checked=0
    for path in sorted((ROOT/'configs/phase6').glob('*.json')):
        checked+=1
        text=path.read_text().lower()
        if any(word in text for word in ('parent_to_student','frozen-parent-web-body-kl','kl_reference')):
            matches.append(path.relative_to(ROOT).as_posix())
    if matches:raise ValueError('Potential registered duplicate KL condition: '+repr(matches))
    cp=result['checkpoints']['source_order']; updates=cp['update']-320435
    proposal=dict(status='prototype_CPU_verified_GPU_not_started',created_at=now(),
        rationale='Same-teacher staged training improves EOS/coherence but all256 natural-dev body losses worsen, across all four length quartiles. Test whether a frozen parent distribution on actual train Web replay can retain body prediction while learning short-body EOS. Recency/forgetting is a hypothesis, not a proven sole cause.',
        literature=[dict(title='Learning without Forgetting',url='https://arxiv.org/abs/1606.09282',
            relevance='Old-output distillation motivates retention; original work is vision with a different protocol, not proof for JMicro.'),
            dict(title='Distill and Replay for Continual Language Learning',url='https://aclanthology.org/2020.coling-main.318/',
            relevance='Language-model-based NLU continual-learning framework combines distillation/replay. This proposal uses its general principle, not an exact replication or a guarantee for free Japanese generation.')],
        diagnostic=reference(diagnostic),parent=c['parent'],frozen_reference_teacher=c['parent'],
        control=dict(config=reference(ROOT/'configs/phase6/source_order_condition_comparison_v2.json'),
            result=reference(run/'compare-result.json'),review=reference(run/'review.json'),
            notes=reference(ROOT/'reports/phase6/source_order_condition_notes.json'),
            generation=reference(run/'evaluation/source_order/evaluation/generation.json'),
            checkpoint=dict(path=cp['checkpoint'],sha256=cp['checkpoint_sha256'])),
        main_teacher_quotas=c['arms']['source_order'],source_order=c['source_order'],main_ordinary_CE_teacher_tokens=100000000,
        inherited_actual_LR=.00001,optimizer_policy='inherit',main_shapes=c['shapes'],KL_policy=POLICY,
        reference_physical_input_tokens_if_same_updates=updates*8*1024,reference_soft_target_body_positions='Measure actual labels>=8; never add to ordinaryCE/new corpus totals',
        combined_training_accounting='100M ordinaryCE teachers plus separately counted soft-target Web positions; primary100,532,224 physicalinput plus25,133,056 referenceinput expected. Not an equal-total-supervision comparison or a pure isolated objective effect.',
        newly_prepared_source_tokens=0,replay_overlaps_primary_Web=True,
        total_new_GPU_ceiling_seconds=900,reused_control_GPU_seconds=0,
        settings_sweep_allowed=False,alternate_order_allowed=False,automatic_long_extension_allowed=False,
        required_before_science=['Own trainer/runner/reviewer/durablePS implemented',
            'Frozen teacher unchanged/eval/no gradients, same actual parent model/Adam/scheduler/RNG/main cursor/LR',
            'ActualCUDA continuous4 vs2+2 exact fullstate including replay cursor/digest/soft-position counters and finite combined gradients',
            '32 measured combined-update timings and actual save cost; freeze only if probe+science+full evaluation estimate<=900s',
            'Inspect real process identities; discard probe weights and reuse cached control results exactly'],
        terminal_evidence=['Exactly100M ordinaryCE and separate auxiliary counters; allfour primary source terminal states equal cached control',
            'Same256byte/192semantics/331JBLiMP/1119JCQA/80greedy64/bridge128/retention128',
            'Read all80 outputs; exact peer reuse only; same relative coherence+8/CI/EOS/repetition and BPB gates versus staged control',
            'Unchanged absolute grammar56/coherence27/appropriate27/EOS37/repetition<=18/noerror and historicalWeb1percent guard',
            'Actual terminal process absent/UI restored; portable evidence and local commit'],
        registered_preexisting_configs_checked=checked,registered_preexisting_KL_matches=matches,
        novelty_limit='Only registered phase6 top-level configs and textual implementation search; no proof about unregistered external experiments.',
        CPU_prototype_tests=reference(ROOT/'reports/phase6/web_kl_preservation_tests.xml'),
        initial_test_failure=reference(ROOT/'reports/phase6/web_kl_preservation_initial_test_failure.xml'),
        source_sha256={p:sha256(ROOT/p) for p in ('scripts/web_kl_preservation.py','tests/test_web_kl_preservation.py',
            'scripts/prepare_web_kl_comparison_proposal.py')},
        actual_GPU_seconds=0,actual_scientific_teacher_tokens=0,Base_adopted=False,Base_complete=False,
        Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True,
        next_action='Implement one combined CE+KL inherited trainer and own durable runner/reviewer; verify CPU state/counters then actualCUDA/probe budget before any100M science. No coefficient/batch/temperature/order/source/LR sweep.')
    atomic_json(target,proposal)
    print(json.dumps(dict(status=proposal['status'],reference_physical_input_tokens=proposal['reference_physical_input_tokens_if_same_updates'],
        existing_configs_checked=checked,GPU_seconds=0)))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
