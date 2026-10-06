"""Own GPU runner/reviewer versions; do not mutate earlier frozen studies."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT


def once(text,old,new):
    if text.count(old)!=1:raise ValueError('Source anchor differs: '+old[:60])
    return text.replace(old,new,1)


def function(text,name,new):
    start=text.index('def '+name+'(')
    end=text.find('\ndef ',start+4)
    if end<0:raise ValueError('Function boundary absent')
    return text[:start]+new.rstrip()+'\n\n'+text[end:]


def main():
    text=(ROOT/'scripts/run_source_order_condition_comparison.py').read_text()
    text=once(text,'from source_order_condition_trainer import SourceOrderHistoricalTrainer,SOURCE_ORDER',
        'from source_order_condition_trainer import SOURCE_ORDER\nfrom web_kl_condition_trainer import WebKLTrainer,KIND\nfrom web_kl_preservation import POLICY\nimport source_order_budget_evidence as budget_evidence')
    text=once(text,'import run_historical_parent_condition_comparison_v3 as cached','import run_source_order_condition_comparison_v2 as cached')
    text=text.replace('source-order-condition-comparison-20261006','web-kl-comparison-20261006')
    text=text.replace('source_order_condition_comparison.json','web_kl_comparison.json').replace('source_order_condition_probe.json','web_kl_probe.json')
    text=text.replace('source_order_condition_comparison_proposal.json','web_kl_comparison_proposal.json')
    text=once(text,"ARM='source_order'\nKIND='historical_parent_source_order_100M'","ARM='web_kl'")
    start=text.index('SOURCES=tuple(');end=text.index('reference,check_reference',start)
    text=text[:start]+"SOURCES=tuple(dict.fromkeys(('scripts/run_web_kl_comparison.py','scripts/run_web_kl_comparison.ps1',\n    'scripts/review_web_kl_comparison.py','scripts/prepare_web_kl_content_review.py','scripts/web_kl_condition_trainer.py',\n    'scripts/web_kl_preservation.py','tests/test_web_kl_condition_trainer.py','tests/test_web_kl_preservation.py',\n    'tests/test_web_kl_comparison.py',*cached.SOURCES)))\n"+text[end:]
    text=function(text,'source_contract', '''def source_contract():
    old,base,parent,_,_,positive,original=cached.source_contract()
    p=read_json(PROPOSAL)
    for ref in (*p['control'].values(),p['parent'],p['diagnostic'],p['CPU_prototype_tests']):check_reference(ref)
    preparation=ROOT/'reports/phase6/web_kl_trainer_preparation.json'
    prepared=read_json(preparation)
    for path,digest in {**p['source_sha256'],**prepared['source_sha256']}.items():
        if sha256(ROOT/path)!=digest:raise ValueError('Frozen KL prototype/preparation differs')
    if (p['parent']!=old['parent'] or p['frozen_reference_teacher']!=old['parent']
            or p['main_teacher_quotas']!=GOALS or p['source_order']!=list(SOURCE_ORDER)
            or p['KL_policy']!=POLICY or p['main_shapes']!=old['shapes']
            or p['main_ordinary_CE_teacher_tokens']!=TOTAL or p['inherited_actual_LR']!=.00001
            or p['total_new_GPU_ceiling_seconds']!=CEILING or p['newly_prepared_source_tokens']
            or p['settings_sweep_allowed'] or p['alternate_order_allowed'] or p['automatic_long_extension_allowed']
            or p['Base_adopted'] or p['Base_complete'] or p['Chat_started'] or p['quantization_started']
            or p['protected_test_used'] or not p['quality_criteria_unchanged']):
        raise ValueError('One fixed inherited100M CE plus parent Web KL condition required')
    job=read_json(cached.RUN/'job.json');r=read_json(cached.RUN/'compare-result.json')
    review=read_json(Path(p['control']['review']['path']))
    control=r['checkpoints']['source_order'];ev=r['evaluations']['source_order']
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(cached.RUN/'compare-result.json')
            or control['additional_supervised_tokens']!=TOTAL or control['source_teachers']!=GOALS
            or control['checkpoint_sha256']!=ev['checkpoint_sha256'] or control['binding']!=ev['binding']
            or dict(path=control['checkpoint'],sha256=control['checkpoint_sha256'])!=p['control']['checkpoint']
            or review['summaries']['source_order']['notes_sha256']!=p['control']['notes']['sha256']):
        raise ValueError('Cached complete staged CE100M control required')
    return old,base,parent,control,ev,positive,original''')
    text=once(text,"'scripts/web_kl_preservation.py','tests/test_web_kl_condition_trainer.py'", "'scripts/web_kl_preservation.py','scripts/web_kl_comparison_accounting.py','tests/test_web_kl_condition_trainer.py'")
    text=function(text,'prepare_probe', '''def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,control,_,_,_=source_contract()
    c=copy.deepcopy(read_json(cached.PROBE_CONFIG));p=read_json(PROPOSAL)
    c.update(research_kind=KIND,phase='probe',arms={ARM:GOALS},outcome_weights={ARM:1},KL_policy=POLICY,
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,failed_probe_GPU_seconds=0,
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        source_order=list(SOURCE_ORDER),created_at=now(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        sampler_policy='Same historical fullstate/actualLR.00001/main staged100M streams as cached control, plus separately counted frozen-parent Web body KL replay. Main and reference cursors separate; no reheat/reset/new corpus.')
    c['references'].update(proposal=reference(PROPOSAL),control_config=p['control']['config'],control_result=p['control']['result'],
        control_review=p['control']['review'],control_notes=p['control']['notes'],control_generation=p['control']['generation'],
        KL_preparation=reference(ROOT/'reports/phase6/web_kl_trainer_preparation.json'),nontraining_timing=reference(budget_evidence.PATH))
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print('Own combined CE+parentKL CUDA probe frozen; no scientific training yet',flush=True)''')
    text=once(text,"    if (c['research_kind']!=KIND", "    if (c['KL_policy']!=POLICY or c['research_kind']!=KIND")
    text=once(text,"'update', 'spec', 'model_config', 'pilot_binding', 'study_binding')", "'update', 'spec', 'model_config', 'pilot_binding', 'study_binding', 'KL_state')")
    text=once(text,"'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass'):",
        "'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass', 'ordinary_CE_loss', 'reference_KL_loss',\n                'reference_input_tokens', 'reference_soft_target_body_positions', 'reference_ignored_positions', 'reference_digest', 'combined_student_physical_input_tokens'):")
    text=once(text,'    teachers = 0','    teachers = 0; reference_inputs=reference_positions=0')
    text=once(text,'        teachers += trainer.supervised_tokens - before','        teachers += trainer.supervised_tokens - before\n        reference_inputs+=trainer.replay.physical_input_tokens;reference_positions+=trainer.replay.body_positions')
    text=once(text,'        GPU_optimizer_updates=8, verification_teacher_tokens=teachers)',
        '        GPU_optimizer_updates=8, verification_teacher_tokens=teachers,verification_reference_input_tokens=reference_inputs,verification_reference_soft_positions=reference_positions)')
    text=once(text,'    updates=math.ceil(TOTAL/teachers);warm=', '    updates=3068;warm=')
    text=once(text,'    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total),total*1.3+300+50',
        "    evidence=budget_evidence.inspect();reserve=evidence['nontraining_reserve_seconds']\n    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total,\n        reference_input_tokens=updates*8*1024,nontraining_reserve_seconds=reserve,nontraining_evidence_sha256=sha256(budget_evidence.PATH)),(total+reserve)*1.3+50")
    text=once(text,'        positive_manifest_sha256=', '        KL_policy=c[\'KL_policy\'],reference_teacher=c[\'parent\'],positive_manifest_sha256=')
    text=once(text,"        verification_GPU_seconds=r['GPU_seconds']+c['failed_probe_GPU_seconds'],verification_teacher_tokens=r['verification_teacher_tokens'],GPU_budget_seconds=", "        verification_GPU_seconds=r['GPU_seconds']+c['failed_probe_GPU_seconds'],verification_teacher_tokens=r['verification_teacher_tokens'],\n        verification_reference_input_tokens=r['verification_reference_input_tokens'],verification_reference_soft_positions=r['verification_reference_soft_positions'],GPU_budget_seconds=")
    text=once(text,"                or c['measured_timing']!=timing", "                or c['verification_reference_input_tokens']!=measured['verification_reference_input_tokens'] or c['verification_reference_soft_positions']!=measured['verification_reference_soft_positions']\n                or c['measured_timing']!=timing")
    text=once(text,'return SourceOrderHistoricalTrainer(parent,pool,positive,original,b,device,context,batch)',
        'return WebKLTrainer(parent,pool,original,positive,GOALS,b,device,context,batch)') if 'return SourceOrderHistoricalTrainer(parent,pool,positive,original,b,device,context,batch)' in text else once(text,'return SourceOrderHistoricalTrainer(parent,pool,original,positive,GOALS,b,device,context,batch)',
        'return WebKLTrainer(parent,pool,original,positive,GOALS,b,device,context,batch)')
    text=once(text,"                    actual_LR=[g['lr'] for g in initial.optimizer.param_groups]==[.00001,.00001])",
        "                    actual_LR=[g['lr'] for g in initial.optimizer.param_groups]==[.00001,.00001],\n                    frozen_teacher_weights=equal_state(cpu_state(initial.reference_teacher.state_dict()),cpu_state(parent['model'])),\n                    frozen_teacher_eval_no_grad=not initial.reference_teacher.training and all(not p.requires_grad and p.grad is None for p in initial.reference_teacher.parameters()),\n                    reference_Web_cursor=equal_state(initial.replay.stream.state_dict()['sampler'],historical_web_cursor(parent)))")
    text=once(text,"                    terminal_save_seconds=saved_seconds,checkpoint=str(cp),checkpoint_sha256=sha256(cp))",
        "                    terminal_save_seconds=saved_seconds,checkpoint=str(cp),checkpoint_sha256=sha256(cp),\n                    reference_input_tokens=trainer.replay.physical_input_tokens,reference_soft_positions=trainer.replay.body_positions)")
    text=once(text,"                    GPU_optimizer_updates=40,scientific_teacher_tokens=0,weights_discarded_for_science=True,initial_parent_preservation=preservation)",
        "                    GPU_optimizer_updates=40,scientific_teacher_tokens=0,weights_discarded_for_science=True,initial_parent_preservation=preservation,\n                    verification_reference_input_tokens=gate['verification_reference_input_tokens']+timing['reference_input_tokens'],\n                    verification_reference_soft_positions=gate['verification_reference_soft_positions']+timing['reference_soft_positions'])")
    text=once(text,"                    atomic_json(progress,result); del trainer; gc.collect(); torch.cuda.empty_cache()",
        "                    result['checkpoints'][ARM].update(reference_replay=trainer.replay.state_dict(),reference_teacher_weight_digest=trainer.teacher_digest,\n                        reference_input_tokens=trainer.replay.physical_input_tokens,reference_soft_target_body_positions=trainer.replay.body_positions,\n                        combined_student_physical_input_tokens=result['checkpoints'][ARM]['additional_input_tokens']+trainer.replay.physical_input_tokens,KL_policy=POLICY)\n                    atomic_json(progress,result); del trainer; gc.collect(); torch.cuda.empty_cache()")
    text=text.replace("['historical_parent']","['source_order']")
    text=text.replace('scripts/run_source_order_condition_comparison.ps1','scripts/run_web_kl_comparison.ps1')
    text=once(text,"                    reused_control=True,Base_adopted=False", "                    reference_input_tokens=result['checkpoints'][ARM]['reference_input_tokens'],\n                    reference_soft_target_body_positions=result['checkpoints'][ARM]['reference_soft_target_body_positions'],\n                    reused_control=True,Base_adopted=False")
    text=text.replace('actual_source_order_resume_timing_complete','actual_web_KL_resume_timing_complete').replace('source_order100M_and_cached_same_parent_mixed100M_complete','web_KL_CE100M_and_cached_stagedCE100M_complete').replace('measured100M_source_order_frozen','measured100M_CE_parentKL_frozen')
    files={'scripts/run_web_kl_comparison.py':text}
    ps=(ROOT/'scripts/run_source_order_condition_comparison.ps1').read_text().replace('source-order-condition-','web-kl-').replace('run_source_order_condition_comparison.py','run_web_kl_comparison.py')
    files['scripts/run_web_kl_comparison.ps1']=ps
    review=(ROOT/'scripts/review_source_order_condition_comparison_v2.py').read_text()
    review=review.replace('import run_source_order_condition_comparison_v2 as study','import run_web_kl_comparison as study\nfrom web_kl_comparison_accounting import audit_reference')
    review=review.replace("'reports/phase6/historical_parent_condition_notes.json'","'reports/phase6/source_order_condition_notes.json'")
    review=review.replace('reports/phase6/source_order_condition_notes.json\'\n','reports/phase6/web_kl_notes.json\'\n') if False else review
    review=once(review,"else ROOT / 'reports/phase6/source_order_condition_notes.json'", "else ROOT / 'reports/phase6/web_kl_notes.json'")
    review=review.replace('evaluation/historical_parent/evaluation/generation.json','evaluation/source_order/evaluation/generation.json')
    review=review.replace("['historical_parent']","['source_order']")
    review=once(review,'    retained = retained_sources(parent, state, previous_state)', '    retained = retained_sources(parent, state, previous_state)\n    auxiliary = audit_reference(parent,state,record,history,c)')
    review=once(review,'original_Web=original, retained_source_checks=retained,','original_Web=original, retained_source_checks=retained,reference_accounting=auxiliary,')
    review=review.replace('source_order_condition_comparison_v2_review.json','web_kl_comparison_review.json')
    review=review.replace('staged-source-order-vs-interleaved-same-parent-same-teachers','staged-CE-plus-parent-Web-KL-vs-cached-staged-CE')
    review=once(review,"        verification_GPU_seconds=probe['GPU_seconds'],", "        verification_reference_input_tokens=probe['verification_reference_input_tokens'],\n        verification_reference_soft_positions=probe['verification_reference_soft_positions'],verification_GPU_seconds=probe['GPU_seconds'],")
    review=once(review,"        limitations='One learned seed;", "        limitations='Additional separately counted Web reference soft targets; not equal total supervision or pure isolated objective effect. One learned seed;")
    review=review.replace('source_order100M_all80_and_cached_same_parent_mixed100M_reviewed','web_KL_CE100M_all80_and_cached_stagedCE100M_reviewed')
    review=review.replace('Same parent/model/Adam/RNG/scheduler/actualLR and four source streams/terminal cursors/teacher quotas, cross-source ordering differs. Stage boundaries may share an update; source recency and gradient-update grouping change together.', 'Same parent/model/Adam/RNG/scheduler/actualLR and four primary streams/terminal cursors/ordinaryCE quotas/order. Adds frozen-parent distribution targets on separately counted overlapping trainWeb replay.')
    files['scripts/review_web_kl_comparison.py']=review
    post=(ROOT/'scripts/prepare_source_order_content_review_v2.py').read_text().replace('import run_source_order_condition_comparison_v2 as study','import run_web_kl_comparison as study')
    post=post.replace("'reports/phase6/source_order_condition_notes.json'","'reports/phase6/web_kl_notes.json'")
    anchor="    saved,refs=previous.lookup()"
    post=once(post,anchor,anchor+'''
    stage_notes=ROOT/'reports/phase6/source_order_condition_notes.json'
    stage_raw=study.cached.RUN/'evaluation/source_order/evaluation/generation.json'
    generation,notes=read_json(stage_raw),read_json(stage_notes)
    validate_notes(generation['outputs'],notes,sha256(stage_raw))
    indexed={n[0]:n for n in notes['notes']}
    for row in generation['outputs']:
        k=key(row);note=indexed[row['id']]
        if k in saved and saved[k]!=note:raise ValueError('Conflicting exact staged peer notes')
        saved[k]=note
    refs.append(dict(notes=study.reference(stage_notes),generation=study.reference(stage_raw)))''')
    post=once(post,"control_raw=study.cached.RUN/'evaluation/historical_parent/evaluation/generation.json'", "control_raw=study.cached.cached.RUN/'evaluation/historical_parent/evaluation/generation.json'")
    files['scripts/prepare_web_kl_content_review.py']=post
    for name,body in files.items():
        path=ROOT/name
        if path.exists() and path.read_text()!=body:raise ValueError('Preserve existing own source')
        path.write_text(body,encoding='utf-8',newline='\n')
    print('Own combined CE+KL runner/reviewer/PS prepared; old code unchanged; no GPU execution')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
