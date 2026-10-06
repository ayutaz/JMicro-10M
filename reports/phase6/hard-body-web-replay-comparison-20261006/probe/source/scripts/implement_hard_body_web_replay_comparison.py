"""Own one hard-gold replay experiment, preserving every frozen predecessor."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT
from prepare_hard_body_web_replay import once, write


CONTRACT = '''def source_contract():
    old,base,parent,control,ev,positive,original=component_control.source_contract()
    p=read_json(PROPOSAL)
    prepared=read_json(ROOT/'reports/phase6/hard_body_web_replay_trainer_preparation.json')
    check_reference(prepared['proposal']);check_reference(prepared['tests']);check_reference(prepared['initial_failure'])
    for ref in (*p['mandatory_quality_control'].values(),*p['primary_supervision_control'].values(),
            p['parent'],p['previous_completed_component_study'],p['resident_preparation']):check_reference(ref)
    for path,digest in prepared['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen hard-target prototype differs')
    completion=read_json(Path(p['previous_completed_component_study']['path']))
    auxiliary=p['auxiliary_policy']
    if (p['parent']!=old['parent'] or p['frozen_reference_teacher']!=old['parent']
            or p['main_teacher_quotas']!=GOALS or p['source_order']!=list(SOURCE_ORDER)
            or prepared['auxiliary_policy']!=POLICY or p['main_shapes']!=old['shapes']
            or p['main_ordinary_CE_teacher_tokens']!=TOTAL or p['inherited_actual_LR']!=.00001
            or auxiliary['kind']!='parent-mass-weighted-gold-body-non-EOS-CE'
            or any(auxiliary[k]!=POLICY[k] for k in ('coefficient','temperature','reference_context','reference_batch','every_completed_update'))
            or p['expected_auxiliary_input_tokens']!=25133056 or p['expected_auxiliary_hard_body_target_positions']!=25026383
            or p['expected_combined_student_input_tokens']!=125665280 or p['expected_total_hard_teacher_positions']!=125026383
            or p['total_new_GPU_ceiling_seconds']!=CEILING or p['newly_prepared_source_tokens']
            or p['settings_sweep_allowed'] or p['alternate_order_allowed'] or p['automatic_long_extension_allowed']
            or p['Base_adopted'] or p['Base_complete'] or p['Chat_started'] or p['quantization_started']
            or p['protected_test_used'] or not p['quality_criteria_unchanged']
            or p['previous_related_KL_studies_GPU_seconds']!=completion['cumulative_related_GPU_seconds']):
        raise ValueError('One fixed inherited100M CE plus hard gold Web-body replay required')
    for key in ('config','result','review','notes','generation','checkpoint'):
        if p['mandatory_quality_control'][key]!=read_json(component_control.PROPOSAL)['control'][key]:
            raise ValueError('Mandatory stronger staged quality control differs')
    job=read_json(MECHANISM_RUN/'job.json');r=read_json(MECHANISM_RUN/'compare-result.json')
    review=read_json(Path(p['primary_supervision_control']['review']['path']))
    cp=r['checkpoints'][MECHANISM_ARM]
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=p['primary_supervision_control']['result']['sha256']
            or cp['additional_supervised_tokens']!=TOTAL or cp['reference_input_tokens']!=25133056
            or cp['reference_soft_target_body_positions']!=25026383
            or dict(path=cp['checkpoint'],sha256=cp['checkpoint_sha256'])!=p['primary_supervision_control']['checkpoint']):
        raise ValueError('Actual completed conditionalKL supervision control required')
    return old,base,parent,control,ev,positive,original


'''


def main():
    outputs = {}
    runner = (ROOT/'scripts/run_eos_decoupled_web_kl_comparison.py').read_text()
    runner = once(runner, '"""Same fullstate, staged100M and replay windows; omit only the EOS-mass KL component."""',
        '"""Same staged100M and replay windows; replace conditional soft targets with gold words."""')
    runner = runner.replace('from eos_decoupled_resident_web_kl_trainer import WebKLTrainer,KIND',
        'from hard_body_resident_web_replay_trainer import HardBodyReplayTrainer,KIND\nimport run_eos_decoupled_web_kl_comparison as component_control')
    runner = runner.replace('from eos_decoupled_web_kl_preservation import POLICY', 'from hard_body_web_replay import POLICY')
    runner = runner.replace('WebKLTrainer(', 'HardBodyReplayTrainer(')
    runner = runner.replace('eos-decoupled-web-kl-comparison-20261006', 'hard-body-web-replay-comparison-20261006')
    for old,new in (('eos_decoupled_web_kl_comparison','hard_body_web_replay_comparison'),
            ('eos_decoupled_web_kl_probe','hard_body_web_replay_probe'),
            ('eos_decoupled_web_kl_trainer_preparation','hard_body_web_replay_trainer_preparation'),
            ('prepare_eos_decoupled_web_kl_content_review','prepare_hard_body_web_replay_content_review'),
            ('KL_policy','auxiliary_policy'), ('KL_state','hard_replay_state'), ('reference_KL_loss','reference_body_CE_loss'),
            ('reference_soft_target_body_positions','reference_hard_body_target_positions'),
            ('reference_soft_positions','reference_hard_positions')):
        runner = runner.replace(old,new)
    runner = once(runner, 'import run_hard_body_web_replay_comparison as component_control',
        'import run_eos_decoupled_web_kl_comparison as component_control')
    runner = once(runner, "ARM='eos_decoupled_web_kl'\nMECHANISM_RUN=ROOT/'reports/phase6/web-kl-comparison-v3-20261006'",
        "ARM='hard_body_web_replay'\nMECHANISM_RUN=ROOT/'reports/phase6/eos-decoupled-web-kl-comparison-20261006'\nMECHANISM_ARM='eos_decoupled_web_kl'\n\n\ndef control_history_key(key):\n    return 'reference_soft_target_body_positions' if key=='reference_hard_body_target_positions' else key")
    start = runner.index('SOURCES=tuple(')
    end = runner.index('reference,check_reference=',start)
    runner = runner[:start]+'''SOURCES=tuple(dict.fromkeys((
    'scripts/implement_hard_body_web_replay_comparison.py','scripts/hard_body_web_replay.py',
    'scripts/hard_body_web_replay_trainer.py','scripts/hard_body_resident_web_replay_trainer.py',
    'scripts/prepare_hard_body_web_replay.py','scripts/record_hard_body_web_replay_preparation.py',
    'scripts/run_hard_body_web_replay_comparison.py','scripts/run_hard_body_web_replay_comparison.ps1',
    'scripts/review_hard_body_web_replay_comparison.py','scripts/prepare_hard_body_web_replay_content_review.py',
    'scripts/hard_body_web_replay_accounting.py','tests/test_hard_body_web_replay.py',
    'tests/test_hard_body_web_replay_trainer.py','tests/test_hard_body_web_replay_comparison.py',
    *component_control.SOURCES)))
'''+runner[end:]
    start = runner.index('def source_contract():')
    end = runner.index('def prepare_probe():',start)
    runner = runner[:start]+CONTRACT+runner[end:]
    runner = runner.replace("p['previous_related_study_all_GPU_seconds']", "p['previous_related_KL_studies_GPU_seconds']")
    runner = runner.replace("p['control']", "p['mandatory_quality_control']")
    runner = runner.replace("p['mechanism_full_KL']", "p['primary_supervision_control']")
    runner = runner.replace('frozen-parent Web body KL replay', 'parent-mass-weighted gold Web body CE replay')
    runner = runner.replace('CE+parentKL', 'CE+goldWebReplay').replace('measured100M_CE_parentKL_frozen','measured100M_CE_goldWebReplay_frozen')
    runner = runner.replace('actual_web_KL_resume_timing_complete','actual_gold_Web_replay_resume_timing_complete')
    runner = runner.replace('web_KL_CE100M_and_cached_stagedCE100M_complete','gold_Web_replay_CE100M_and_cached_stagedCE100M_complete')
    runner = runner.replace("old_full[k]['web_kl']", "old_full[k][MECHANISM_ARM]")
    runner = runner.replace('Cached fullKL mechanism evidence differs','Cached conditionalKL supervision evidence differs')
    runner = once(runner, "any(not equal_state(a[k],b[k]) for a,b in zip(r['timing']['histories'],previous['timing']['histories'],strict=True) for k in keys)",
        "any(not equal_state(a[k],b[control_history_key(k)]) for a,b in zip(r['timing']['histories'],previous['timing']['histories'],strict=True) for k in keys)")
    runner = once(runner, "'reference_non_EOS_teacher_probability_mass','reference_input_tokens', 'reference_hard_body_target_positions',",
        "'combined_hard_teacher_positions','reference_non_EOS_teacher_probability_mass','reference_input_tokens', 'reference_hard_body_target_positions',")
    runner = once(runner, "reference_hard_body_target_positions=trainer.replay.body_positions,\n                        combined_student_physical_input_tokens=",
        "reference_hard_body_target_positions=trainer.reference_hard_body_teacher_tokens,\n                        combined_hard_teacher_positions=TOTAL+trainer.reference_hard_body_teacher_tokens,\n                        combined_student_physical_input_tokens=")
    runner = once(runner, '                    atomic_json(progress,result); del trainer;',
        "                    if trainer.reference_hard_body_teacher_tokens!=25026383 or trainer.replay.physical_input_tokens!=25133056:\n"
        "                        raise ValueError('Same fixed replay hard-target positions required')\n"
        '                    atomic_json(progress,result); del trainer;')
    runner = once(runner, "                    reused_control=True,Base_adopted=False,",
        "                    scientific_auxiliary_hard_body_teacher_tokens=result['checkpoints'][ARM]['reference_hard_body_target_positions'],\n"
        "                    scientific_combined_hard_teacher_positions=result['checkpoints'][ARM]['combined_hard_teacher_positions'],\n"
        "                    reused_control=True,Base_adopted=False,")
    outputs['scripts/run_hard_body_web_replay_comparison.py'] = runner
    ps = (ROOT/'scripts/run_eos_decoupled_web_kl_comparison.ps1').read_text()
    ps = ps.replace('eos-decoupled-web-kl-', 'hard-body-web-replay-').replace('run_eos_decoupled_web_kl_comparison', 'run_hard_body_web_replay_comparison').replace('Web KL', 'gold-body Web replay')
    outputs['scripts/run_hard_body_web_replay_comparison.ps1'] = ps
    accountant = (ROOT/'scripts/eos_decoupled_web_kl_accounting.py').read_text()
    for old,new in (('eos_decoupled_web_kl_preservation','hard_body_web_replay'),
            ('KL_state','hard_replay_state'),('KL_policy','auxiliary_policy'),('KL_sources','auxiliary_sources'),
            ('reference_soft_target_body_positions','reference_hard_body_target_positions')):
        accountant = accountant.replace(old,new)
    accountant = once(accountant, '    mass=extra[',
        "    hard=extra['hard_body_teacher_tokens']\n"
        "    if type(hard) is not int or hard!=replay['body_positions'] or record['combined_hard_teacher_positions']!=record['additional_supervised_tokens']+hard:\n"
        "        raise ValueError('Measured hard-target terminal ledger differs')\n"
        "    for row in history:\n"
        "        if row['combined_hard_teacher_positions']!=row['additional_teacher_tokens']+row['reference_hard_body_target_positions']:\n"
        "            raise ValueError('Hard teacher positions must be separate from probability mass')\n"
        '    mass=extra[')
    accountant = accountant.replace('labels=\'Main CE teachers and auxiliary distribution targets are separate; not equal total supervision with cached control.\'',
        "labels='Main100M ordinary CE and auxiliary gold-body hard targets are separate. Same physical replay windows as conditionalKL, but different gold-word supervision; additional corpus0.'")
    accountant = once(accountant, 'return dict(reference_non_EOS_teacher_probability_mass=mass,',
        "return dict(reference_hard_body_teacher_tokens=hard,combined_hard_teacher_positions=record['combined_hard_teacher_positions'],reference_non_EOS_teacher_probability_mass=mass,")
    outputs['scripts/hard_body_web_replay_accounting.py'] = accountant
    reviewer = (ROOT/'scripts/review_eos_decoupled_web_kl_comparison.py').read_text()
    for old,new in (('run_eos_decoupled_web_kl_comparison','run_hard_body_web_replay_comparison'),
            ('eos_decoupled_web_kl_accounting','hard_body_web_replay_accounting'),
            ('eos_decoupled_web_kl_notes','hard_body_web_replay_notes'),
            ('eos_decoupled_web_kl_comparison_review','hard_body_web_replay_comparison_review'),
            ('reference_soft_target_body_positions','reference_hard_body_target_positions'),
            ('verification_reference_soft_positions','verification_reference_hard_positions')):
        reviewer = reviewer.replace(old,new)
    reviewer = reviewer.replace("full_result[k]['web_kl']", "full_result[k][study.MECHANISM_ARM]")
    reviewer = reviewer.replace("study.MECHANISM_RUN/'web_kl/training/metrics.jsonl'", "study.MECHANISM_RUN/study.MECHANISM_ARM/'training/metrics.jsonl'")
    reviewer = reviewer.replace("study.MECHANISM_RUN/'evaluation/web_kl/evaluation/generation.json'", "study.MECHANISM_RUN/f'evaluation/{study.MECHANISM_ARM}/evaluation/generation.json'")
    reviewer = reviewer.replace("ROOT/'reports/phase6/web_kl_notes.json'", "ROOT/'reports/phase6/eos_decoupled_web_kl_notes.json'")
    reviewer = reviewer.replace("ROOT/'reports/phase6/web_kl_comparison_v3_review.json'", "ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_review.json'")
    reviewer = reviewer.replace("['summaries']['web_kl']", "['summaries'][study.MECHANISM_ARM]")
    reviewer = once(reviewer, 'any(not equal_state(a[k],b[k]) for a,b in zip(history,full_history,strict=True) for k in keys)',
        'any(not equal_state(a[k],b[study.control_history_key(k)]) for a,b in zip(history,full_history,strict=True) for k in keys)')
    reviewer = reviewer.replace('fullKL', 'conditionalKL')
    reviewer = reviewer.replace('web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed', 'gold_Web_replay_CE100M_all80_and_cached_stagedCE100M_reviewed')
    reviewer = once(reviewer, "primary_comparison='staged-CE-plus-parent-Web-KL-vs-cached-staged-CE'",
        "primary_comparison='gold-body-CE-replay-vs-cached-conditionalKL-same-inputs',quality_comparison_baseline='mandatory stronger stagedCE'")
    reviewer = once(reviewer, '        new_scientific_teacher_tokens=study.TOTAL,',
        "        new_scientific_auxiliary_hard_body_teacher_tokens=record['reference_hard_body_target_positions'],\n"
        "        new_scientific_combined_hard_teacher_positions=record['combined_hard_teacher_positions'],\n"
        '        new_scientific_teacher_tokens=study.TOTAL,')
    start = reviewer.index("        limitations='Additional separately counted")
    end = reviewer.index("\n    atomic_json(",start)
    reviewer = reviewer[:start]+"        limitations='Gold words replace conditional soft distributions on identical replay windows, with identical frozen parent mass weights and non-EOS vocabulary. Main100M ordinary CE plus separately counted auxiliary gold-body teachers; not equal supervision/information to conditionalKL or plain stagedCE. New corpus0, train overlaps. One seed/nonblind repeated fixeddev; independent seed/full dev/protected test/adoption pending.')"+reviewer[end:]
    outputs['scripts/review_hard_body_web_replay_comparison.py'] = reviewer
    content = (ROOT/'scripts/prepare_eos_decoupled_web_kl_content_review.py').read_text()
    content = content.replace('run_eos_decoupled_web_kl_comparison','run_hard_body_web_replay_comparison')
    content = content.replace('eos_decoupled_web_kl_notes.json','hard_body_web_replay_notes.json')
    content = content.replace("study.MECHANISM_RUN/'evaluation/web_kl/evaluation/generation.json'", "study.MECHANISM_RUN/f'evaluation/{study.MECHANISM_ARM}/evaluation/generation.json'")
    content = content.replace("ROOT/'reports/phase6/web_kl_notes.json'", "ROOT/'reports/phase6/eos_decoupled_web_kl_notes.json'")
    content = content.replace('fullKL peer', 'conditionalKL peer')
    outputs['scripts/prepare_hard_body_web_replay_content_review.py'] = content
    # Compute and validate all transforms before creating any generated source.
    for relative, text in outputs.items():
        if relative.endswith('.py'):
            compile(text, relative, 'exec')
        if (ROOT/relative).exists():
            raise ValueError(f'Preserve own generated output: {relative}')
    for relative, text in outputs.items():
        write(relative,text)
    print('Own gold-body runner/reviewer/accountant/durablePS generated; no GPU started')


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
