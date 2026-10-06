"""Prepare a single owned positive-anchor comparison, preserving frozen prior studies."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once,write
from implement_context_outcome_ranking_comparison import replace_function


def main():
    outputs={}
    runner=(ROOT/'scripts/run_context_outcome_ranking_comparison.py').read_text()
    runner=runner.replace('context-outcome-ranking-comparison-20261006','anchored-context-outcome-comparison-20261006')
    runner=runner.replace('run_context_outcome_ranking_comparison','run_anchored_context_outcome_comparison')
    runner=runner.replace('context_outcome_ranking_comparison.json','anchored_context_outcome_comparison.json')
    runner=runner.replace('context_outcome_ranking_probe.json','anchored_context_outcome_probe.json')
    runner=runner.replace('context_outcome_ranking_proposal.json','anchored_context_outcome_proposal.json')
    runner=once(runner,'from context_outcome_ranking_resident_trainer import ContextOutcomeRankingTrainer,KIND',
        'from anchored_context_outcome_resident_trainer import AnchoredContextOutcomeTrainer,KIND\n'
        'from anchored_context_outcome import POLICY as ANCHOR_POLICY')
    runner=runner.replace('ContextOutcomeRankingTrainer(', 'AnchoredContextOutcomeTrainer(')
    runner=once(runner,'import run_eos_decoupled_web_kl_comparison as base_study',
        'import run_context_outcome_ranking_comparison as base_study')
    runner=once(runner,"ARM='context_outcome_ranking'","ARM='anchored_context_outcome'")
    start=runner.index('SOURCES=tuple(');end=runner.index('reference,check_reference=',start)
    own=('scripts/implement_anchored_context_outcome_comparison.py','scripts/anchored_context_outcome.py',
        'scripts/prepare_anchored_context_outcome_trainer.py','scripts/anchored_context_outcome_trainer.py',
        'scripts/anchored_context_outcome_resident_trainer.py','scripts/run_anchored_context_outcome_comparison.py',
        'scripts/run_anchored_context_outcome_comparison.ps1','scripts/anchored_context_outcome_accounting.py',
        'scripts/review_anchored_context_outcome_comparison.py','scripts/prepare_anchored_context_outcome_content_review.py',
        'tests/test_anchored_context_outcome.py','tests/test_anchored_context_outcome_trainer.py',
        'tests/test_anchored_context_outcome_comparison.py')
    runner=runner[:start]+f'SOURCES=tuple(dict.fromkeys((*{own!r},*base_study.SOURCES)))\n'+runner[end:]
    runner=replace_function(runner,'source_contract','ranking_view', '''def source_contract():
    old,base,parent,control,ev,positive,original=base_study.inspect(base_study.CONFIG)
    p=read_json(PROPOSAL);prep_path=ROOT/'reports/phase6/anchored_context_outcome_preparation.json'
    prep=read_json(prep_path)
    for ref in (*p['trigger'].values(),*p['reused_ranking_control'].values()):
        if isinstance(ref,dict) and set(ref)=={'path','sha256'}:check_reference(ref)
    check_reference(p['stronger_staged_CE_quality_control']);check_reference(p['fixed_pair_inputs']['manifest'])
    check_reference(prep['proposal']);check_reference(prep['CPU_tests'])
    for path,digest in prep['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Prepared positive anchor prototype differs')
    if (p['parent']!=old['parent'] or p['fixed_main']['quotas']!=GOALS
            or p['fixed_main']['ordinary_CE_teachers']!=TOTAL
            or p['fixed_main']['shape']!=old['shapes'] or p['fixed_Web_reference']['policy']!=POLICY
            or p['fixed_pair_inputs']['manifest']!=old['ranking_inputs']
            or p['fixed_pair_inputs']['policy']!=RANKING_POLICY
            or p['positive_anchor']['coefficient']!=1 or p['positive_anchor']['ranking_coefficient']!=1
            or p['positive_anchor']['temperature']!=1 or p['new_total_GPU_ceiling_seconds']!=CEILING
            or p['Base_complete'] or p['protected_test_used'] or p['Chat_started'] or p['quantization_started']
            or prep['GPU_training_seconds'] or prep['scientific_teacher_tokens']
            or prep['CPU_passed_tests']!=4 or not prep['quality_criteria_unchanged']):
        raise ValueError('One fixed positive likelihood anchor proposal required')
    mechanism_job=read_json(MECHANISM_RUN/'job.json')
    if mechanism_job['status']!='complete' or alive(mechanism_job):raise ValueError('Ranking control must be terminal')
    ranking_view(p['fixed_pair_inputs']['manifest'])
    return old,base,parent,control,ev,positive,original
''')
    runner=replace_function(runner,'prepare_probe','scope', '''def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,control,_,_,_=source_contract();p=read_json(PROPOSAL)
    c=copy.deepcopy(old)
    c.update(research_kind=KIND,phase='probe',arms={ARM:GOALS},outcome_weights={ARM:1},KL_policy=POLICY,
        ranking_policy=RANKING_POLICY,ranking_inputs=p['fixed_pair_inputs']['manifest'],positive_anchor_policy=ANCHOR_POLICY,
        quality_screen_baseline=QUALITY_BASELINE,previous_related_study_GPU_seconds=p['earlier_related_GPU_seconds_preserved'],
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,prior_probe_GPU_seconds=PRIOR_GPU,
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        source_order=list(SOURCE_ORDER),created_at=now(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        sampler_policy='Same full parent/main100M CE/Web KL/TRAIN pair windows as ranking control; one positive nonEOS CE anchor, no extra input/corpus/reset/reheat.')
    c['references'].update(proposal=reference(PROPOSAL),
        positive_anchor_preparation=reference(ROOT/'reports/phase6/anchored_context_outcome_preparation.json'),
        ranking_inputs=p['fixed_pair_inputs']['manifest'],
        diagnostic=p['trigger']['absolute_likelihood_analysis'],
        mechanism_config=reference(base_study.CONFIG),mechanism_result=reference(MECHANISM_RUN/'compare-result.json'),
        mechanism_review=p['reused_ranking_control']['review'],
        mechanism_completion=p['reused_ranking_control']['completion'],
        previous_related_completion=p['reused_ranking_control']['completion'])
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print('Owned positive-anchor CUDA probe frozen; scientific training not started',flush=True)
''')
    runner=once(runner,"c['ranking_inputs']!=read_json(PROPOSAL)['ranking_inputs']",
        "c['ranking_inputs']!=read_json(PROPOSAL)['fixed_pair_inputs']['manifest'] or c['positive_anchor_policy']!=ANCHOR_POLICY")
    runner=once(runner,"view=ranking_view(read_json(PROPOSAL)['ranking_inputs'])",
        "view=ranking_view(read_json(PROPOSAL)['fixed_pair_inputs']['manifest'])")
    runner=once(runner,"'KL_state','ranking_state')","'KL_state','ranking_state','positive_anchor_state')")
    runner=once(runner,"'ranking_loss','ranking_family_indices'",
        "'positive_anchor_loss','combined_pair_loss','positive_anchor_body_teacher_tokens','combined_hard_teacher_positions',\n                'ranking_loss','ranking_family_indices'")
    runner=once(runner,'verification_ranking=sum_ranking(ranking_totals))',
        "verification_ranking=sum_ranking(ranking_totals),verification_positive_anchor_teacher_tokens=sum(row['gold_body_scored_positions'] for row in ranking_totals))")
    runner=once(runner,"ranking_policy=c['ranking_policy'],ranking_inputs=c['ranking_inputs'],KL_policy=c['KL_policy']",
        "positive_anchor_policy=c['positive_anchor_policy'],ranking_policy=c['ranking_policy'],ranking_inputs=c['ranking_inputs'],KL_policy=c['KL_policy']")
    runner=once(runner,"verification_ranking=ranking_counts(trainer))",
        "verification_ranking=ranking_counts(trainer),positive_anchor_teacher_tokens=trainer.positive_anchor_body_teacher_tokens)")
    runner=once(runner,"verification_ranking=sum_ranking([gate['verification_ranking'],timing['verification_ranking']]))",
        "verification_ranking=sum_ranking([gate['verification_ranking'],timing['verification_ranking']]),\n                    verification_positive_anchor_teacher_tokens=gate['verification_positive_anchor_teacher_tokens']+timing['positive_anchor_teacher_tokens'])")
    runner=once(runner,"ranking_exposure=ranking_counts(trainer),KL_policy=POLICY)",
        "ranking_exposure=ranking_counts(trainer),KL_policy=POLICY,\n                        positive_anchor_policy=ANCHOR_POLICY,positive_anchor_body_teacher_tokens=trainer.positive_anchor_body_teacher_tokens,\n                        combined_hard_teacher_positions=TOTAL+trainer.positive_anchor_body_teacher_tokens)")
    runner=once(runner,"ranking_exposure=result['checkpoints'][ARM]['ranking_exposure'],new_original_corpus_tokens=0,",
        "ranking_exposure=result['checkpoints'][ARM]['ranking_exposure'],new_original_corpus_tokens=0,\n                    positive_anchor_body_teacher_tokens=result['checkpoints'][ARM]['positive_anchor_body_teacher_tokens'],\n                    combined_hard_teacher_positions=result['checkpoints'][ARM]['combined_hard_teacher_positions'],")
    runner=once(runner,"'reference_soft_target_body_positions','reference_digest')",
        "'reference_soft_target_body_positions','reference_digest','reference_non_EOS_teacher_probability_mass',\n          'ranking_family_indices','ranking_digest','ranking_relational_choice_labels','ranking_valid_input_tokens','ranking_physical_input_positions',\n          'ranking_gold_body_scored_positions','ranking_foil_body_scored_positions','ranking_gold_body_scored_bytes','ranking_foil_body_scored_bytes',\n          'combined_student_physical_input_tokens','combined_student_valid_input_tokens')")
    runner=once(runner,"    return r\n\n\ndef estimate_training(measured):", '''    positive=r['gate']['verification_positive_anchor_teacher_tokens']+r['timing']['positive_anchor_teacher_tokens']
    if r['verification_positive_anchor_teacher_tokens']!=positive or positive!=expected['gold_body_scored_positions']:
        raise ValueError('Actual completed positive anchor verification teachers differ')
    return r


def estimate_training(measured):''')
    runner=runner.replace('actual_three_loss_context_ranking_resume_timing_complete','actual_positive_anchor_full_resume_timing_complete')
    runner=runner.replace('web_KL_CE100M_and_cached_stagedCE100M_complete','positive_anchor100M_and_cached_strong_stagedCE_complete')
    runner=runner.replace('measured100M_CE_parentKL_frozen','measured_positive_anchor100M_frozen')
    outputs['scripts/run_anchored_context_outcome_comparison.py']=runner
    ps=(ROOT/'scripts/run_context_outcome_ranking_comparison.ps1').read_text()
    ps=ps.replace('context-outcome-ranking-','anchored-context-outcome-').replace('run_context_outcome_ranking_comparison','run_anchored_context_outcome_comparison').replace('context outcome ranking','positive outcome likelihood anchor')
    outputs['scripts/run_anchored_context_outcome_comparison.ps1']=ps
    outputs['scripts/anchored_context_outcome_accounting.py']='''"""Separate new hard teachers from fixed main/Web/ranking exposure ledgers."""
import math
from anchored_context_outcome import POLICY
from context_outcome_ranking_accounting import audit_reference,audit_ranking


def audit_anchor(parent,state,record,history,config):
    extra=state['positive_anchor_state'];count=extra['body_teacher_tokens']
    if (config['positive_anchor_policy']!=POLICY or extra['policy']!=POLICY
            or state['spec']['positive_anchor_policy']!=POLICY or state['lineage']['positive_anchor_policy']!=POLICY
            or extra['input_binding']!=state['ranking_state']['input_binding']
            or record['positive_anchor_policy']!=POLICY
            or count!=state['ranking_state']['sampler']['gold_body_scored_positions']
            or record['positive_anchor_body_teacher_tokens']!=count
            or record['combined_hard_teacher_positions']!=state['supervised_tokens']-parent['supervised_tokens']+count):
        raise ValueError('Positive likelihood hard teacher policy/input/terminal count differs')
    for row in history:
        if (row['positive_anchor_body_teacher_tokens']!=row['ranking_gold_body_scored_positions']
                or row['combined_hard_teacher_positions']!=row['additional_teacher_tokens']+row['positive_anchor_body_teacher_tokens']
                or not all(math.isfinite(row[k]) for k in ('positive_anchor_loss','combined_pair_loss','ranking_loss'))
                or row['positive_anchor_loss']<0 or row['ranking_loss']<0
                or not math.isclose(row['combined_pair_loss'],row['ranking_loss']+row['positive_anchor_loss'],rel_tol=1e-6,abs_tol=1e-6)
                or not math.isclose(row['loss'],row['ordinary_CE_loss']+row['reference_KL_loss']+row['combined_pair_loss'],rel_tol=1e-12)):
            raise ValueError('Completed positive likelihood/combined teacher history differs')
    if not history or history[-1]['positive_anchor_body_teacher_tokens']!=count:
        raise ValueError('Positive likelihood completed history missing')
    return dict(positive_anchor_body_teacher_tokens=count,combined_hard_teacher_positions=record['combined_hard_teacher_positions'],
        foil_hard_teacher_positions=0,new_original_corpus_tokens=0,extra_input_positions_relative_to_ranking_control=0,
        all_completed_positive_teacher_and_loss_rows_verified=True)
'''
    reviewer=(ROOT/'scripts/review_context_outcome_ranking_comparison.py').read_text()
    reviewer=reviewer.replace('run_context_outcome_ranking_comparison','run_anchored_context_outcome_comparison')
    reviewer=reviewer.replace('context_outcome_ranking_accounting','anchored_context_outcome_accounting')
    reviewer=reviewer.replace('context_outcome_ranking_notes.json','anchored_context_outcome_notes.json')
    reviewer=reviewer.replace('context_outcome_ranking_comparison_review.json','anchored_context_outcome_comparison_review.json')
    reviewer=once(reviewer,'import audit_reference,audit_ranking','import audit_reference,audit_ranking,audit_anchor')
    reviewer=once(reviewer,'    relational = audit_ranking(parent,state,record,history,c)',
        '    relational = audit_ranking(parent,state,record,history,c)\n    anchored = audit_anchor(parent,state,record,history,c)')
    reviewer=once(reviewer,"'reference_digest','reference_non_EOS_teacher_probability_mass')",
        "'reference_digest','reference_non_EOS_teacher_probability_mass',\n        'ranking_family_indices','ranking_digest','ranking_relational_choice_labels','ranking_valid_input_tokens','ranking_physical_input_positions',\n        'ranking_gold_body_scored_positions','ranking_foil_body_scored_positions','ranking_gold_body_scored_bytes','ranking_foil_body_scored_bytes',\n        'combined_student_physical_input_tokens','combined_student_valid_input_tokens')")
    reviewer=once(reviewer,"b['combined_student_physical_input_tokens'] for a,b", "b['main_and_Web_reference_physical_input_tokens'] for a,b")
    reviewer=reviewer.replace('eos_decoupled_web_kl_notes.json','context_outcome_ranking_notes.json')
    reviewer=reviewer.replace('eos_decoupled_web_kl_comparison_review.json','context_outcome_ranking_comparison_review.json')
    reviewer=once(reviewer,'reference_accounting=auxiliary,ranking_accounting=relational,',
        'reference_accounting=auxiliary,ranking_accounting=relational,positive_anchor_accounting=anchored,\n        all3068_main_Web_and_ranking_input_protocols_equal=True,')
    reviewer=once(reviewer,"verification_ranking_exposure=probe['verification_ranking'],",
        "verification_ranking_exposure=probe['verification_ranking'],verification_positive_anchor_teacher_tokens=probe['verification_positive_anchor_teacher_tokens'],")
    reviewer=reviewer.replace('web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed','positive_anchor100M_all80_and_strong_stagedCE_reviewed')
    reviewer=reviewer.replace('staged-CE-plus-parent-Web-KL-vs-cached-staged-CE','positive-anchor-plus-ranking-Web-KL-vs-strong-staged-CE')
    reviewer=reviewer.replace('Extra TRAIN opposite-context ranking pairs/foil/gold body exposures and relational labels are separate, not equal input/supervision/time to control.',
        'Pair exposure is identical to the completed ranking mechanism control but adds positive hard teachers. Strong stagedCE remains the quality control. No equality of supervision/time is claimed.')
    outputs['scripts/review_anchored_context_outcome_comparison.py']=reviewer
    content=(ROOT/'scripts/prepare_context_outcome_ranking_content_review.py').read_text()
    content=content.replace('run_context_outcome_ranking_comparison','run_anchored_context_outcome_comparison').replace('context_outcome_ranking_notes.json','anchored_context_outcome_notes.json')
    content=content.replace('eos_decoupled_web_kl_notes.json','context_outcome_ranking_notes.json')
    outputs['scripts/prepare_anchored_context_outcome_content_review.py']=content
    for relative,text in outputs.items():
        if relative.endswith('.py'):compile(text,relative,'exec')
        if (ROOT/relative).exists():raise ValueError('Preserve owned positive-anchor source: '+relative)
    for relative,text in outputs.items():write(relative,text)
    print('Owned positive-anchor runner/accountant/reviewer/launcher prepared; GPU not started.')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
