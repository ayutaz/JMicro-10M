"""Generate owned runner/reviewer/accountant; never edit prior frozen studies."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once, write


def replace_function(text, name, next_name, replacement):
    start = text.index('def '+name+'(')
    end = text.index('def '+next_name+'(', start)
    return text[:start] + replacement.rstrip() + '\n\n\n' + text[end:]


def main():
    outputs = {}
    runner = (ROOT/'scripts/run_eos_decoupled_web_kl_comparison.py').read_text()
    runner = runner.replace('eos-decoupled-web-kl-comparison-20261006','context-outcome-ranking-comparison-20261006')
    runner = runner.replace('eos_decoupled_web_kl_comparison','context_outcome_ranking_comparison')
    runner = runner.replace('eos_decoupled_web_kl_probe.json','context_outcome_ranking_probe.json')
    runner = runner.replace('context_outcome_ranking_comparison_proposal.json','context_outcome_ranking_proposal.json')
    runner = once(runner,'from eos_decoupled_resident_web_kl_trainer import WebKLTrainer,KIND',
        'from context_outcome_ranking_resident_trainer import ContextOutcomeRankingTrainer,KIND\n'
        'from context_outcome_ranking import POLICY as RANKING_POLICY,RankingTrainView\n'
        'import run_eos_decoupled_web_kl_comparison as base_study')
    runner = once(runner,"ARM='eos_decoupled_web_kl'","ARM='context_outcome_ranking'")
    runner = once(runner,"MECHANISM_RUN=ROOT/'reports/phase6/web-kl-comparison-v3-20261006'",
        "MECHANISM_RUN=base_study.RUN\nMECHANISM_ARM=base_study.ARM")
    start = runner.index('SOURCES=tuple('); end = runner.index('reference,check_reference=',start)
    own = ('scripts/implement_context_outcome_ranking_comparison.py', 'scripts/context_outcome_ranking.py',
        'scripts/prepare_context_outcome_ranking_inputs.py', 'scripts/prepare_context_outcome_ranking_trainer.py',
        'scripts/context_outcome_ranking_trainer.py', 'scripts/context_outcome_ranking_resident_trainer.py',
        'scripts/run_context_outcome_ranking_comparison.py', 'scripts/run_context_outcome_ranking_comparison.ps1',
        'scripts/context_outcome_ranking_accounting.py', 'scripts/review_context_outcome_ranking_comparison.py',
        'scripts/prepare_context_outcome_ranking_content_review.py', 'tests/test_context_outcome_ranking.py',
        'tests/test_context_outcome_ranking_trainer.py', 'tests/test_context_outcome_ranking_comparison.py')
    runner = runner[:start]+f'SOURCES=tuple(dict.fromkeys((*{own!r},*base_study.SOURCES)))\n'+runner[end:]
    contract = '''def source_contract():
    old,base,parent,control,ev,positive,original=base_study.inspect(base_study.CONFIG)
    p=read_json(PROPOSAL);prep=read_json(Path(p['preparation']['path']))
    for key in ('trigger','preparation','mechanism_control_config','mechanism_control_completion',
                'mandatory_stronger_quality_control_config','ranking_inputs','resident_input_preparation'):
        check_reference(p[key])
    for ref in (prep['diagnostic'],prep['input_preparation'],prep['manifest'],prep['rows']):check_reference(ref)
    for path,digest in prep['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Prepared owned prototype differs')
    if (p['parent']!=old['parent'] or p['pool']!=old['pool'] or p['original_web']!=old['original_web']
            or p['positive_data']!=old['positive_data'] or p['fixed_primary']['quotas']!=GOALS
            or p['fixed_primary']['ordinary_CE_teachers']!=TOTAL
            or p['one_new_auxiliary']['coefficient']!=1 or p['one_new_auxiliary']['temperature']!=1
            or p['one_new_auxiliary']['families_per_update']!=2 or p['one_new_auxiliary']['context']!=256
            or p['proposed_new_GPU_ceiling_seconds']!=CEILING or p['Base_complete'] or p['protected_test_used']
            or prep['GPU_training_seconds'] or prep['scientific_teacher_tokens']
            or not prep['quality_criteria_unchanged']):raise ValueError('One fixed train-ranking100M proposal required')
    mechanism_job=read_json(MECHANISM_RUN/'job.json')
    if mechanism_job['status']!='complete' or alive(mechanism_job):raise ValueError('Mechanism control must be terminal')
    ranking_view(p['ranking_inputs'])
    return old,base,parent,control,ev,positive,original


def ranking_view(record):
    check_reference(record)
    return RankingTrainView(Path(record['path']).parent,record['sha256'])
'''
    runner = replace_function(runner,'source_contract','prepare_probe',contract)
    prepare = '''def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,control,_,_,_=source_contract();p=read_json(PROPOSAL)
    c=copy.deepcopy(old)
    previous=read_json(ROOT/'reports/phase6/hard_body_web_replay_comparison_completion.json')
    c.update(research_kind=KIND,phase='probe',arms={ARM:GOALS},outcome_weights={ARM:1},KL_policy=POLICY,
        ranking_policy=RANKING_POLICY,ranking_inputs=p['ranking_inputs'],
        quality_screen_baseline=QUALITY_BASELINE,previous_related_study_GPU_seconds=previous['cumulative_related_GPU_seconds'],
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,prior_probe_GPU_seconds=PRIOR_GPU,
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        source_order=list(SOURCE_ORDER),created_at=now(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        sampler_policy='Same inherited100M CE and conditional parent Web KL windows; separate TRAIN opposite-context ranking cursor/labels/exposures, no reheat/reset/new corpus.')
    c['references'].update(proposal=reference(PROPOSAL),ranking_preparation=p['preparation'],
        ranking_inputs=p['ranking_inputs'],diagnostic=p['trigger'],
        mechanism_config=reference(base_study.CONFIG),mechanism_result=reference(MECHANISM_RUN/'compare-result.json'),
        mechanism_review=reference(ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_review.json'),
        mechanism_completion=p['mechanism_control_completion'],
        previous_related_completion=reference(ROOT/'reports/phase6/hard_body_web_replay_comparison_completion.json'))
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print('Owned three-loss CUDA probe frozen; no scientific training yet',flush=True)
'''
    runner = replace_function(runner,'prepare_probe','scope',prepare)
    runner = once(runner,'def scope(c):\n',
        "def scope(c):\n    if c['ranking_policy']!=RANKING_POLICY or c['ranking_inputs']!=read_json(PROPOSAL)['ranking_inputs']:\n        raise ValueError('Fixed train-only ranking policy/input differs')\n")
    runner = runner.replace("'update', 'spec', 'model_config', 'pilot_binding', 'study_binding', 'KL_state')",
        "'update', 'spec', 'model_config', 'pilot_binding', 'study_binding', 'KL_state','ranking_state')")
    runner = once(runner,"'reference_non_EOS_teacher_probability_mass','reference_input_tokens', 'reference_soft_target_body_positions', 'reference_ignored_positions', 'reference_digest', 'combined_student_physical_input_tokens'):",
        "'reference_non_EOS_teacher_probability_mass','reference_input_tokens', 'reference_soft_target_body_positions', 'reference_ignored_positions', 'reference_digest', 'combined_student_physical_input_tokens',\n"
        "                'ranking_loss','ranking_family_indices','ranking_digest','ranking_relational_choice_labels','ranking_valid_input_tokens','ranking_physical_input_positions',\n"
        "                'ranking_gold_body_scored_positions','ranking_foil_body_scored_positions','ranking_gold_body_scored_bytes','ranking_foil_body_scored_bytes','combined_student_valid_input_tokens'):")
    runner = once(runner,'    reference_mass=0.','    reference_mass=0.;ranking_totals=[]')
    runner = once(runner,'        teachers += trainer.supervised_tokens - before',
        "        ranking_totals.append(ranking_counts(trainer))\n        teachers += trainer.supervised_tokens - before")
    runner = once(runner,'verification_reference_soft_positions=reference_positions)',
        'verification_reference_soft_positions=reference_positions,verification_ranking=sum_ranking(ranking_totals))')
    runner = once(runner,'def cpu_state(value):', '''def ranking_counts(trainer):
    sampler=trainer.ranking.state_dict()
    keys=('updates','families_seen','relational_choice_labels','valid_input_tokens','physical_input_positions',
          'gold_body_scored_positions','foil_body_scored_positions','gold_body_scored_bytes','foil_body_scored_bytes')
    return {k:sampler[k] for k in keys}


def sum_ranking(rows):
    return {k:sum(row[k] for row in rows) for k in rows[0]}


def cpu_state(value):''')
    runner = once(runner,'def trainer_for(parent,pool,positive,original,b,device=\'cuda\',context=1024,batch=32):\n    return WebKLTrainer(parent,pool,original,positive,GOALS,b,device,context,batch)',
        "def trainer_for(parent,pool,positive,original,b,device='cuda',context=1024,batch=32):\n"
        "    view=ranking_view(read_json(PROPOSAL)['ranking_inputs'])\n"
        '    return ContextOutcomeRankingTrainer(parent,pool,original,positive,GOALS,b,view,device,context,batch)')
    runner = once(runner,'    return r\n\n\ndef estimate_training(measured):',
        "    expected=sum_ranking([r['gate']['verification_ranking'],r['timing']['verification_ranking']])\n"
        "    if (r['verification_ranking']!=expected or expected['updates']!=40 or expected['families_seen']!=80\n"
        "            or expected['relational_choice_labels']!=160 or expected['physical_input_positions']!=40*8*256):\n"
        "        raise ValueError('Actual separate CUDA ranking verification ledgers differ')\n"
        '    return r\n\n\ndef estimate_training(measured):')
    runner = once(runner,"KL_policy=c['KL_policy'],reference_teacher=c['parent'],", "ranking_policy=c['ranking_policy'],ranking_inputs=c['ranking_inputs'],KL_policy=c['KL_policy'],reference_teacher=c['parent'],")
    runner = once(runner,'reference_soft_positions=trainer.replay.body_positions)',
        'reference_soft_positions=trainer.replay.body_positions,verification_ranking=ranking_counts(trainer))')
    runner = once(runner,"verification_reference_soft_positions=gate['verification_reference_soft_positions']+timing['reference_soft_positions'])",
        "verification_reference_soft_positions=gate['verification_reference_soft_positions']+timing['reference_soft_positions'],\n"
        "                    verification_ranking=sum_ranking([gate['verification_ranking'],timing['verification_ranking']]))")
    runner = runner.replace("old_full[k]['web_kl']", "old_full[k][MECHANISM_ARM]")
    runner = once(runner,"combined_student_physical_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens,KL_policy=POLICY)",
        "main_and_Web_reference_physical_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens,\n"
        "                        combined_student_physical_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens+trainer.ranking.physical_input_positions,\n"
        "                        combined_student_valid_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens+trainer.ranking.valid_input_tokens,\n"
        "                        ranking_policy=c['ranking_policy'],ranking_input_binding=trainer.ranking.view.binding,ranking_sampler=trainer.ranking.state_dict(),ranking_exposure=ranking_counts(trainer),KL_policy=POLICY)")
    runner = once(runner,'reused_control=True,Base_adopted=False,',
        "ranking_exposure=result['checkpoints'][ARM]['ranking_exposure'],new_original_corpus_tokens=0,\n                    reused_control=True,Base_adopted=False,")
    runner = runner.replace("status='actual_web_KL_resume_timing_complete'", "status='actual_three_loss_context_ranking_resume_timing_complete'")
    outputs['scripts/run_context_outcome_ranking_comparison.py'] = runner
    ps = (ROOT/'scripts/run_eos_decoupled_web_kl_comparison.ps1').read_text()
    ps = ps.replace('eos-decoupled-web-kl-','context-outcome-ranking-').replace('run_eos_decoupled_web_kl_comparison','run_context_outcome_ranking_comparison').replace('Web KL','context outcome ranking')
    outputs['scripts/run_context_outcome_ranking_comparison.ps1'] = ps
    accountant = (ROOT/'scripts/eos_decoupled_web_kl_accounting.py').read_text().replace('combined_student_physical_input_tokens','main_and_Web_reference_physical_input_tokens')
    accountant += '''

def audit_ranking(parent,state,record,history,config):
    from context_outcome_ranking import POLICY as RANK_POLICY,RankingTrainView,OutcomePairSampler
    from pathlib import Path
    inputs=config['ranking_inputs']; extra=state['ranking_state']
    view=RankingTrainView(Path(inputs['path']).parent,inputs['sha256'])
    if (extra['policy']!=RANK_POLICY or state['spec']['ranking_policy']!=RANK_POLICY
            or extra['input_binding']!=view.binding or record['ranking_input_binding']!=view.binding
            or record['ranking_policy']!=RANK_POLICY or extra['sampler']!=record['ranking_sampler']):
        raise ValueError('Ranking train-input/policy identity differs')
    sampler=OutcomePairSampler(view,2,42)
    keys=('relational_choice_labels','valid_input_tokens','physical_input_positions',
          'gold_body_scored_positions','foil_body_scored_positions','gold_body_scored_bytes','foil_body_scored_bytes')
    for row in history:
        _,_,_,selected=sampler.next()
        if (row['ranking_family_indices']!=selected or row['ranking_digest']!=sampler.digest
                or any(row['ranking_'+k]!=getattr(sampler,k) for k in keys)
                or row['combined_student_physical_input_tokens']!=row['main_and_Web_reference_physical_input_tokens']+sampler.physical_input_positions
                or row['combined_student_valid_input_tokens']!=row['main_and_Web_reference_physical_input_tokens']+sampler.valid_input_tokens):
            raise ValueError('Actual whole train-ranking history/input/labels/bytes differs')
    if sampler.state_dict()!=extra['sampler'] or sampler.updates!=state['update']-parent['update']:
        raise ValueError('Ranking completed fullstate/terminal counter differs')
    measured={k:getattr(sampler,k) for k in ('updates','families_seen',*keys)}
    if measured!=record['ranking_exposure']:
        raise ValueError('Ranking exposure disclosure differs')
    if record['combined_student_physical_input_tokens']!=record['main_and_Web_reference_physical_input_tokens']+sampler.physical_input_positions:
        raise ValueError('All3 terminal physical input ledgers differ')
    if record['combined_student_valid_input_tokens']!=record['main_and_Web_reference_physical_input_tokens']+sampler.valid_input_tokens:
        raise ValueError('All3 terminal valid input ledgers differ')
    return dict(all_completed_train_family_order_and_ledger_rows_verified=True,ranking_exposure=measured,
                combined_student_physical_input_tokens=record['combined_student_physical_input_tokens'],
                combined_student_valid_input_tokens=record['combined_student_valid_input_tokens'],
                ranking_ordinary_CE_teacher_tokens=0,ranking_soft_distribution_target_positions=0,
                new_original_corpus_tokens=0,quality_criteria_unchanged=True)
'''
    outputs['scripts/context_outcome_ranking_accounting.py'] = accountant
    reviewer = (ROOT/'scripts/review_eos_decoupled_web_kl_comparison.py').read_text()
    reviewer = reviewer.replace('run_eos_decoupled_web_kl_comparison','run_context_outcome_ranking_comparison').replace('eos_decoupled_web_kl_accounting','context_outcome_ranking_accounting').replace('eos_decoupled_web_kl_notes.json','context_outcome_ranking_notes.json').replace('eos_decoupled_web_kl_comparison_review.json','context_outcome_ranking_comparison_review.json')
    reviewer = reviewer.replace('import audit_reference','import audit_reference,audit_ranking')
    reviewer = once(reviewer,'    auxiliary = audit_reference(parent,state,record,history,c)',
        '    auxiliary = audit_reference(parent,state,record,history,c)\n    relational = audit_ranking(parent,state,record,history,c)')
    reviewer = reviewer.replace("full_result[k]['web_kl']", "full_result[k][study.MECHANISM_ARM]")
    reviewer = reviewer.replace("study.MECHANISM_RUN/'web_kl/training/metrics.jsonl'", "study.MECHANISM_RUN/study.MECHANISM_ARM/'training/metrics.jsonl'")
    reviewer = once(reviewer,"'reference_digest','combined_student_physical_input_tokens')", "'reference_digest','reference_non_EOS_teacher_probability_mass')")
    reviewer = once(reviewer,"    del state, previous_state,full_state", "    if any(a['main_and_Web_reference_physical_input_tokens']!=b['combined_student_physical_input_tokens'] for a,b in zip(history,full_history,strict=True)):\n        raise ValueError('All3068 main/Web reference physical positions differ')\n    del state, previous_state,full_state")
    reviewer = reviewer.replace("study.MECHANISM_RUN/'evaluation/web_kl/evaluation/generation.json'", "study.MECHANISM_RUN/f'evaluation/{study.MECHANISM_ARM}/evaluation/generation.json'")
    reviewer = reviewer.replace("ROOT/'reports/phase6/web_kl_notes.json'", "ROOT/'reports/phase6/eos_decoupled_web_kl_notes.json'")
    reviewer = reviewer.replace("ROOT/'reports/phase6/web_kl_comparison_v3_review.json'", "ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_review.json'").replace("['summaries']['web_kl']", "['summaries'][study.MECHANISM_ARM]")
    reviewer = once(reviewer,'reference_accounting=auxiliary,','reference_accounting=auxiliary,ranking_accounting=relational,')
    reviewer = once(reviewer,'        new_scientific_teacher_tokens=study.TOTAL,',
        "        verification_ranking_exposure=probe['verification_ranking'],\n        new_scientific_teacher_tokens=study.TOTAL,")
    start=reviewer.index("        limitations='Additional separately counted");end=reviewer.index('\n    atomic_json(',start)
    reviewer=reviewer[:start]+"        limitations='One100M mainCE with same parent/Adam/scheduler/RNG/LR/source quotas/order and same conditional parent Web KL windows. Extra TRAIN opposite-context ranking pairs/foil/gold body exposures and relational labels are separate, not equal input/supervision/time to control. No new corpus. Shared-generator local probes/nonblind repeated dev/one learned seed; independent seed/full dev/protected test/adoption pending.')"+reviewer[end:]
    outputs['scripts/review_context_outcome_ranking_comparison.py'] = reviewer
    content = (ROOT/'scripts/prepare_eos_decoupled_web_kl_content_review.py').read_text()
    content = content.replace('run_eos_decoupled_web_kl_comparison','run_context_outcome_ranking_comparison').replace('eos_decoupled_web_kl_notes.json','context_outcome_ranking_notes.json')
    content = content.replace("study.MECHANISM_RUN/'evaluation/web_kl/evaluation/generation.json'", "study.MECHANISM_RUN/f'evaluation/{study.MECHANISM_ARM}/evaluation/generation.json'").replace("ROOT/'reports/phase6/web_kl_notes.json'", "ROOT/'reports/phase6/eos_decoupled_web_kl_notes.json'")
    outputs['scripts/prepare_context_outcome_ranking_content_review.py'] = content
    for relative,text in outputs.items():
        if relative.endswith('.py'):compile(text,relative,'exec')
        if (ROOT/relative).exists():raise ValueError('Preserve owned generated source: '+relative)
    for relative,text in outputs.items():write(relative,text)
    print('Owned three-loss runner/reviewer/accountant/durable launcher generated; no GPU run started.')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
