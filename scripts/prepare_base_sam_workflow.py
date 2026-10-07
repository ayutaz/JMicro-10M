"""Create a separately named, bounded two-pass SAM comparison from audited CE plumbing.

Does not modify old experiments or create/freeze GPU configs; run once under uv.
"""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]


def once(text,old,new):
    if text.count(old)!=1: raise ValueError('Expected one source block: '+old[:100])
    return text.replace(old,new)


def renamed(path):
    return (ROOT/path).read_text().replace('base_muon','base_sam').replace('base-muon','base-sam').replace('finite_muon_state','committed_state').replace('Muon','SAM').replace('muon','sam').replace('4800','7200')


def save(path,text):
    p=ROOT/path
    if p.exists(): raise ValueError('Preserve existing SAM workflow: '+path)
    p.write_text(text)


def main():
    probe=renamed('scripts/probe_base_muon.py').replace('SAMTrainer, finite_sam_state','SAMTrainer, committed_state, sam_backward, RECIPE')
    probe=once(probe,'from base_sam_trainer import SAMTrainer, committed_state','from base_sam_trainer import SAMTrainer, committed_state, sam_backward, RECIPE')
    probe=once(probe,"!= 7 or any", "!= 9 or any")
    probe=once(probe,'Seven actual CPU protocol checks required','Nine actual CPU SAM protocol checks required')
    start=probe.index('    references = {}'); end=probe.index('    atomic_json(PROPOSAL, proposal)',start)
    probe=probe[:start]+'''    references = {}
    for name in ('base_failure_route_synthesis.json','base_muon_comparison_completion.json',
                 'base_on_policy_teacher_comparison_completion.json','base_gradient_precision_completion.json'):
        path=ROOT/'reports/phase6'/name
        references[name]=ref(path)
    proposal=dict(created_at=now(),question='Does full-batch sharpness-aware CE optimization improve same-parent Japanese Base generalization and repetition while preserving Web quality?',
        prior_turn='progress: actual on-policy100M/all Japanese/all80 content rejection and portable closeout committed1530346; actual process718057 absent',
        references=references,
        novelty='Inspection of existing optimizer/objective proposals found AdamW, Muon, contrastive, dropout/smoothing and teacher feedback, but no full-parameter two-pass SAM. Unlike Muon it uses a second same-batch CE gradient at adversarially perturbed weights; unlike anchors/KL it has no reference model or parameter-location penalty. Exploratory mechanism, not a proven root cause.',
        primary_sources=['https://arxiv.org/abs/2010.01412','https://arxiv.org/abs/2110.08529','https://github.com/google-research/sam'],
        literature_limit='The NLP paper reports task finetuning/choice/QA gains on larger models. It does not prove free Japanese10M continuation quality; this is a local Base full-body/EOS study, no Chat/SFT.',
        recipe=RECIPE,parent=old['parent'],source_binding=old['source_binding'],goals=old['goals'],
        batch=48,seed=42,native_parameters=10001152,extra_parameters=0,original_teachers=100000000,
        repeated_SAM_teacher_evaluations=100000000,new_unique_dataset_tokens=0,control_reused_GPU_seconds=0,
        total_GPU_cap_seconds=7200,probe_GPU_cap_seconds=180,CPU_checks=ref(tests),
        accounting='Draw/CE source quotas, EOS/body/bytes/digest and sampler once; second evaluation of exact same inputs/targets is separate repeated teacher/valid/physical compute. Single optimizer update after exact FP32 restoration. No new data, teacher, auxiliary parameters or decoder changes.',
        acceptance='Actual CPU and CUDA continuous4 vs2-save-resume2/full state, two-pass worst48x1024 finite gradients/restoration before science. Forecast ceil(exact17698 updates*mean32 measured two-pass seconds*1.3+900) plus actual probe within7200. Same cachedCE100M source and fullsampler, same256 commonbyte/Japanese192,331,1119/all80 raw-bound content, unchanged matched/strong/absolute/historicalWeb gates. Only qualified candidate gets independent learnedseed/fullDEV/protected finalTEST/adoption.',
        failure='Close this one fixed condition on finite/state/radius/budget or quality failure. No rho/adaptive/period/optimizer/LR/parent/data/batch/decoder/cap rescue or extension.',
        limitations='One conservative-LR mature-parent transition, extra second-pass compute, repeated nonblind DEV. Negative result does not disprove all SAM; local fit/likelihood is not useful Base quality.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
''' + probe[end:]
    probe=once(probe,"    'tests/test_base_sam_trainer.py', 'scripts/natural_context_contrast_corpus.py',", "    'tests/test_base_sam_trainer.py', 'scripts/prepare_base_sam_workflow.py', 'scripts/natural_context_contrast_corpus.py',")
    first=probe.index('            with sdpa_kernel(SDPBackend.FLASH_ATTENTION)'); last=probe.index('            del t,hidden,loss,ids,targets; clear()',first)
    probe=probe[:first]+'''            selected=targets.ne(-100)
            def closure():
                with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                    return F.cross_entropy(t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float(),targets[selected])
            before=host(t.model.state_dict())
            measures=sam_backward(t.model,t.optimizer,closure)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(selected.sum()),
                repeated_target_positions=int(selected.sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,exact_restoration=equal_state(before,host(t.model.state_dict())),**measures)
            if not capacity['exact_restoration'] or not all(math.isfinite(measures[k]) for k in measures) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite SAM two-pass/restored resident worst shape required')
''' + probe[last:]
    probe=once(probe,'del t,hidden,loss,ids,targets; clear()','del t,before,ids,targets; clear()')
    probe=once(probe,'forecast = math.ceil(100000000/speed*1.3+900)',"forecast = math.ceil(17698/32*sum(r['seconds'] for r in histories['timing'][3:])*1.3+900)")
    probe=once(probe,"optimizer_state=states[0]['optimizer']['names'], scientific_teacher_positions=0,", "SAM=states[0]['SAM'], all32_timing_seconds=[r['seconds'] for r in histories['timing'][3:]],\n                verification_repeated_teacher_evaluations=sum(r.get('repeated_teacher_positions_this_update',0) for h in histories.values() for r in h), scientific_teacher_positions=0,")
    save('scripts/probe_base_sam.py',probe)
    save('scripts/probe_base_sam.ps1',renamed('scripts/probe_base_muon.ps1'))
    run=renamed('scripts/run_base_muon.py')
    run=once(run,'from base_sam_trainer import SAMTrainer, committed_state','from base_sam_trainer import SAMTrainer, committed_state, RECIPE')
    run=once(run,'budget = math.ceil(100000000/speed*1.3+900)',"times=probe['all32_timing_seconds']\n    if len(times)!=32 or any(not math.isfinite(x) or x<=0 for x in times): raise ValueError('All32 actual SAM step times required')\n    budget = math.ceil(17698/32*sum(times)*1.3+900)")
    run=once(run,"optimizer='official_SAM_hidden_matrix_match_rms_adamw_fresh_AdamW_tied_vocab_norms_lr1e-5_wd0.1_constant',", "optimizer='fresh_AdamW_after_same_batch_full_parameter_SAM',SAM_recipe=RECIPE,")
    run=once(run,"scientific_CE_teacher_tokens=100000000,counters=state['counters'],sampler=state['sampler'],spec=state['spec'],lineage=state['lineage'])", "scientific_CE_teacher_tokens=100000000,scientific_repeated_teacher_evaluations=100000000,SAM=state['SAM'],counters=state['counters'],sampler=state['sampler'],spec=state['spec'],lineage=state['lineage'])")
    run=once(run,"if t is not None and t.counters['source_teachers'] == t.sampler.consumed and t.counters['update'] == t.optimizer.completed_steps:", "if t is not None and not t._step_in_progress and t.counters['source_teachers'] == t.sampler.consumed and committed_state(host(t.state_dict())):")
    run=run.replace('no LR/momentum/NS/scaling/source/parent/batch/teacher/cap rescue','no rho/adaptive/period/LR/source/parent/batch/teacher/cap rescue')
    save('scripts/run_base_sam.py',run)
    save('scripts/run_base_sam.ps1',renamed('scripts/run_base_muon.ps1'))
    review=renamed('scripts/review_base_muon.py')
    review=once(review,'from base_sam_trainer import KIND, committed_state','from base_sam_trainer import KIND, committed_state, RECIPE')
    first=review.index('def audit_state('); last=review.index('\ndef review(',first)
    review=review[:first]+'''def audit_state(state,record,c):
    counters=state['counters']; steps=counters['update']; opt=state['optimizer']
    if (not committed_state(state) or state['kind']!=KIND or state['binding']!=record['binding'] or
        state['spec']['optimizer_policy']!='fresh_equal_AdamW_both_arms' or state['spec']['SAM']!=RECIPE or c['SAM_recipe']!=RECIPE or
        state['spec']['batch']!=48 or state['spec']['seed']!=42 or state['spec']['contrast'] or
        state['model_config']['expected_parameter_count']!=10001152 or counters['supervised_tokens']!=100000000 or
        counters['source_teachers']!=c['goals'] or counters!=record['counters'] or state['SAM']!=record['SAM'] or
        record['scientific_repeated_teacher_evaluations']!=100000000 or not equal_state(state['sampler'],record['sampler']) or
        state['lineage']['parent']!=c['parent'] or steps<=0 or len(opt['state'])!=sum(len(g['params']) for g in opt['param_groups']) or
        any(g['lr']!=1e-5 or g['weight_decay']!=.1 for g in opt['param_groups'])):
        raise ValueError('Exact complete restored original100M/SAM two-pass committed state required')

''' + review[last:]
    marker="    if template:\n"
    extra="""    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','perturbed_CE_loss','first_gradient_norm','gradient_norm','perturbation_L2')) or
            not 0<r['perturbation_L2']<=.05001 or r['SAM']!=dict(updates=u,repeated_teacher_positions=r['supervised_tokens'],repeated_valid_inputs=r['CE_input_tokens'],repeated_physical_inputs=r['physical_input_tokens']) or
            r['repeated_teacher_positions_this_update']!=r['CE_targets_this_update'] or r['repeated_physical_inputs_this_update']!=r['physical_inputs_this_update']
            for u,r in history.items()): raise ValueError('Actual finite same-batch second-pass history required')
"""
    review=once(review,marker,extra+marker)
    review=once(review,"probe_GPU_seconds=c['probe_GPU_seconds'],all80_individually_read=True", "probe_GPU_seconds=c['probe_GPU_seconds'],SAM=state['SAM'],scientific_repeated_teacher_evaluations=100000000,all80_individually_read=True")
    review=review.replace('heuristic update RMS and compute differ','second same-batch gradient and extra compute differ')
    save('scripts/review_base_sam.py',review)
    tests=renamed('tests/test_base_muon_run.py')
    start=tests.index('def test_measured_speed_');end=tests.index("@pytest.mark.parametrize('field'",start)
    tests=tests[:start]+'''def test_measured_mean32_times_requires_exact_fixed_forecast_and_total():
    valid=dict(median_original_teachers_per_second=50000,GPU_occupancy_seconds=15,
        all32_timing_seconds=[.1]*32,science_budget_seconds=3201,science_budget_eligible=True)
    assert science_budget(valid)==3201
    for speed in (0,-1,float('nan'),float('inf')):
        with pytest.raises(ValueError): science_budget(valid|{'median_original_teachers_per_second':speed})
    with pytest.raises(ValueError): science_budget(valid|{'all32_timing_seconds':[1.]*32,'science_budget_seconds':23908})


''' + tests[end:]
    tests=tests.replace('science_budget_seconds=3500,science_budget_eligible=True','all32_timing_seconds=[.1]*32,science_budget_seconds=3201,science_budget_eligible=True').replace("'science_budget_seconds':3501", "'science_budget_seconds':3202")
    tests+='''

@pytest.mark.parametrize('times',[[],[.1]*31,[.1]*33,[0.]*32,[float('nan')]*32])
def test_missing_partial_or_nonfinite_timing_not_evidence(times):
    row=dict(median_original_teachers_per_second=50000,GPU_occupancy_seconds=15,
        all32_timing_seconds=times,science_budget_seconds=3201,science_budget_eligible=True)
    with pytest.raises(ValueError): science_budget(row)
'''
    save('tests/test_base_sam_run.py',tests)
    print('Separate SAM workflow created; GPU/configs/results0')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
