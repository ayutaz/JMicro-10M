"""Build an isolated hint workflow from the executed native KD infrastructure.

Prepare all exact substitutions before writing; never edit the old workflows.
NativeHintTrainer contains the new, already CPU-tested math and commit protocol.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PENDING={}


def once(text,old,new):
    if text.count(old)!=1: raise ValueError('Expected one source block: '+old[:100])
    return text.replace(old,new)


def renamed(path):
    return ((ROOT/path).read_text()
        .replace('base_native_teacher_KD_trainer','OLD_FINITE_KD_HELPER')
        .replace('base_native_teacher_KD_science','base_native_hint')
        .replace('base-native-teacher-KD-science','base-native-hint')
        .replace('base_native_teacher_KD_committed','base_native_hint_trainer')
        .replace('CommittedNativeTeacherKDTrainer','NativeHintTrainer')
        .replace('native_teacher_KD','native_hint')
        .replace('KD_distribution_positions','hint_positions')
        .replace('KD_targets_this_update','hint_positions_this_update')
        .replace('KD_loss','hint_loss')
        .replace('OLD_FINITE_KD_HELPER','base_native_teacher_KD_trainer'))


def save(path,text):
    target=ROOT/path
    if target.exists() or path in PENDING: raise ValueError('Preserve native hint source: '+path)
    PENDING[path]=text


def main():
    probe=renamed('scripts/probe_base_native_teacher_KD_science.py')
    probe=once(probe,'from base_native_teacher_KD_trainer import predictive_KL',
        'from base_native_hint_trainer import hidden_with_hint, hint_loss')
    probe=once(probe,"PROPOSAL = ROOT/'reports/phase6/base_native_hint_proposal.json'",
        "PROPOSAL = ROOT/'reports/phase6/base_native_hint_proposal_v2.json'")
    first=probe.index('SOURCES = ('); end=probe.index('\ndef ref(',first)
    probe=probe[:first]+'''SOURCES = ('scripts/base_native_hint_trainer.py','scripts/base_native_teacher_KD_trainer.py',
    'scripts/probe_base_native_hint.py','scripts/probe_base_native_hint.ps1',
    'tests/test_base_native_hint_trainer.py','tests/test_natural_context_contrast_corpus.py',
    'scripts/prepare_base_native_hint_workflow.py','scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/phase6_performance.py','src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock')

''' +probe[end:]
    probe=once(probe,"old = read_json(ROOT/'configs/phase6/base_native_hint_probe_v2.json')",
        "old = read_json(ROOT/'configs/phase6/base_native_teacher_KD_science_comparison.json')")
    probe=probe.replace('!= 19 or any','!= 13 or any').replace(
        'Nineteen actual unchanged-math and committed-boundary CPU checks required','Thirteen actual native hint CPU checks required')
    first=probe.index('    references={}');end=probe.index('    fields = (',first)
    probe=probe[:first]+'''    proposal=read_json(PROPOSAL)
    proof_path=ROOT/'reports/phase6/base_native_hint_CPU_preparation.json'
    proof=read_json(proof_path)
    if (proposal['recipe']!=RECIPE or proof['recipe']!=RECIPE or
        proof['proposal']!=ref(PROPOSAL) or proof['CPU_result']!=dict(path=str(tests),sha256=sha256(tests),passed=13,seconds=proof['CPU_result']['seconds']) or
        proposal['implementation']['trainer_source']!=ref(ROOT/'scripts/base_native_hint_trainer.py') or
        proposal['implementation']['CPU_tests_source']!=ref(ROOT/'tests/test_base_native_hint_trainer.py') or
        any(proposal[k]!=old[k] for k in ('parent','teacher','source_binding','goals')) or
        proposal['resource']['total_GPU_cap_seconds']!=4800 or proposal['resource']['probe_GPU_cap_seconds']!=180):
        raise ValueError('Predeclared same native hint and passed CPU identities required')
''' +probe[end:]
    probe=once(probe,'proposal=ref(PROPOSAL), CPU_tests=ref(tests),',
        'proposal=ref(PROPOSAL), CPU_tests=ref(tests), CPU_preparation=ref(proof_path),')
    probe=once(probe,"for name in ('proposal','CPU_tests','payload','control_CE','control_result'):",
        "for name in ('proposal','CPU_tests','CPU_preparation','payload','control_CE','control_result'):")
    probe=once(probe,'memory = configure_resident_memory(13047812096)',
        'memory = configure_resident_memory(13161375744)')
    first=probe.index('            before=host(t.model.state_dict())');end=probe.index('            states, logs = [], []',first)
    probe=probe[:first]+'''            before=host(t.model.state_dict());selected=targets.ne(-100)
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                with torch.no_grad(): _,q=hidden_with_hint(t.teacher,ids,teacher_only=True)
                final,middle=hidden_with_hint(t.model,ids)
                logits=t.model.lm_head(t.model.model.norm(final[selected])).float()
                ce=F.cross_entropy(logits,targets[selected]);auxiliary=hint_loss(middle[selected],q[selected],int(selected.sum()))
                combined=ce+RECIPE['coefficient']*auxiliary
            combined.backward();gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(selected.sum()),
                hint_positions=int(selected.sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,unchanged_weights=equal_state(before,host(t.model.state_dict())),
                CE_loss=float(ce.detach()),hint_loss=float(auxiliary.detach()),combined_loss=float(combined.detach()),gradient_norm=float(gradient),
                teacher_blocks=6,teacher_upper_blocks_and_head_used=False,
                scope='Artificial all-hint upper-bound shape; not relabeled Web or scientific gold')
            initial['teacher_unchanged_after_stress']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())
            if not capacity['unchanged_weights'] or not all(math.isfinite(capacity[k]) for k in ('CE_loss','hint_loss','combined_loss','gradient_norm')) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite native original CE/middle hints worst shape required')
            del t,before,ids,targets,selected,final,middle,logits,q,ce,auxiliary,combined; clear()
''' +probe[end:]
    probe=probe.replace('separate prospective resource plan','native middle-feature hint protocol')
    save('scripts/probe_base_native_hint.py',probe)
    save('scripts/probe_base_native_hint.ps1',renamed('scripts/probe_base_native_teacher_KD_science.ps1'))

    runner=renamed('scripts/run_base_native_teacher_KD_science.py')
    runner=once(runner,"failure='One fixed new resource study; no further cap/teacher/coefficient/temperature/LR/source/parent/batch/backend/decoder rescue or automatic extension. Resume only valid completed updates within same cumulative budget.'",
        "failure='One fixed middle-layer normalized hint study; no layer/coefficient/normalization/adapter/teacher/LR/source/parent/batch/backend/decoder/cap rescue. Resume only completed updates within the same cumulative budget.'")
    save('scripts/run_base_native_hint.py',runner)
    save('scripts/run_base_native_hint.ps1',renamed('scripts/run_base_native_teacher_KD_science.ps1'))
    save('tests/test_base_native_hint_run.py',renamed('tests/test_base_native_teacher_KD_science_run.py'))

    reviewer=renamed('scripts/review_base_native_teacher_KD_science.py')
    reviewer=once(reviewer,"state['spec']['prospective_KD_study']!=RECIPE", "state['spec']['native_hint']!=RECIPE")
    reviewer=reviewer.replace("['native_hint']['teacher_positions']","['native_hint']['positions']")
    reviewer=once(reviewer,
        'original full-vocab native short-prefix KD math; separately reconsidered prospective resource plan. Extra25M predictive positions/teacher compute differ. All80 individual new observations.',
        'same original gold with native frozen block6 unit-feature hints. Extra25M hint positions and six-block teacher compute differ. All80 individual observations; denseKD comparison secondary only.')
    reviewer=once(reviewer,"    atomic_json(POLICY,dict(created_at=now(),config_sha256=sha256(CONFIG),references=refs,",
        "    dense=ROOT/'reports/phase6/base-native-teacher-KD-science-comparison-20261007'\n"
        "    refs['cached_dense_KD_result']=dict(path=str(dense/'result.json'),sha256=sha256(dense/'result.json'))\n"
        "    refs['cached_dense_KD_notes']=dict(path=str(ROOT/'reports/phase6/base_native_teacher_KD_science_notes.json'),sha256=sha256(ROOT/'reports/phase6/base_native_teacher_KD_science_notes.json'))\n"
        "    refs['cached_dense_KD_raw']=dict(path=str(dense/'evaluation/native_teacher_KD/evaluation/generation.json'),sha256=sha256(dense/'evaluation/native_teacher_KD/evaluation/generation.json'))\n"
        "    atomic_json(POLICY,dict(created_at=now(),config_sha256=sha256(CONFIG),references=refs,")
    reviewer=once(reviewer,"    if strong != p['strong_summary']: raise ValueError('Strong baseline changed')",
        "    dense=read_json(Path(p['references']['cached_dense_KD_result']['path']))\n"
        "    dense_summary,dense_scores=content('cached_dense_KD',dense['evaluation'],dense['training'],c,\n"
        "        Path(p['references']['cached_dense_KD_raw']['path']),Path(p['references']['cached_dense_KD_notes']['path']))\n"
        "    secondary=quality_gates(dense['evaluation'],ev,dense_scores,cs,'native_hint_vs_dense_KD_secondary')\n"
        "    if strong != p['strong_summary']: raise ValueError('Strong baseline changed')")
    reviewer=once(reviewer,'summaries=dict(native_hint=candidate,CE=cached,strong_staged=strong),matched_objective_quality=matched,',
        'summaries=dict(native_hint=candidate,CE=cached,strong_staged=strong,cached_dense_KD=dense_summary),secondary_dense_KD_comparison=secondary,matched_objective_quality=matched,')
    reviewer=once(reviewer,"            not 0<=r['hint_positions_this_update']<=r['CE_targets_this_update']",
        "            not 0<=r['hint_positions_this_update']<=r['CE_targets_this_update'] or not 0<=r['hint_loss']<=2 or\n"
        "            not math.isfinite(r['native_hint']['angular_penalty_sum'])")
    reviewer=reviewer.replace('original100M/middle-head','original100M/short middle hints').replace(
        'dense short-KD','short middle-hint').replace('Single seed and mature-parent native dense-KD resource study;',
        'Single mature-parent native middle-feature hint seed;').replace('extra25M predictive targets','extra25M hint targets')
    save('scripts/review_base_native_hint.py',reviewer)

    launch=renamed('scripts/record_base_native_teacher_KD_science_launch.py')
    launch=launch.replace('actual_native_dense_KD_CUDA_gate_passed_native100M_science_live',
        'actual_native_middle_hint_CUDA_gate_passed_native100M_science_live').replace('short distribution25M','short hint25M')
    save('scripts/record_base_native_hint_launch.py',launch)
    for path,text in PENDING.items():
        target=ROOT/path; target.parent.mkdir(parents=True,exist_ok=True); target.write_text(text)
    print('Prepared isolated native hint probe/science/reviewer/launch and runner checks; GPU0')


if __name__=='__main__':
    main()
