"""Separate prospective resource plan for unchanged, previously untrained native KD."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
PENDING={}


def once(text,old,new):
    if text.count(old)!=1: raise ValueError('Expected one source block: '+old[:100])
    return text.replace(old,new)


def renamed(path):
    return ((ROOT/path).read_text()
        .replace('scripts/base_middle_supervision_trainer.py','scripts/base_native_teacher_KD_committed.py')
        .replace('tests/test_base_middle_supervision_trainer.py','tests/test_base_native_teacher_KD_committed.py')
        .replace('base_middle_supervision','base_native_teacher_KD_science')
        .replace('base-middle-supervision','base-native-teacher-KD-science')
        .replace('MiddleSupervisionTrainer','CommittedNativeTeacherKDTrainer')
        .replace('middle_supervision','native_teacher_KD')
        .replace('middle_gold_evaluations','KD_distribution_positions'))


def save(path,text):
    target=ROOT/path
    if target.exists() or path in PENDING: raise ValueError('Preserve separate prospective KD study: '+path)
    PENDING[path]=text


def main():
    probe=renamed('scripts/probe_base_middle_supervision.py')
    probe=once(probe,'from base_native_teacher_KD_science_trainer import CommittedNativeTeacherKDTrainer, committed_state, middle_losses, RECIPE',
        'from base_native_teacher_KD_committed import CommittedNativeTeacherKDTrainer, committed_state, RECIPE\nfrom base_native_teacher_KD_trainer import predictive_KL')
    probe=once(probe,"    'tests/test_base_native_teacher_KD_committed.py',", "    'scripts/base_native_teacher_KD_trainer.py','tests/test_base_native_teacher_KD.py',\n    'tests/test_base_native_teacher_KD_committed.py',")
    probe=probe.replace('!= 11 or any','!= 19 or any').replace('Eleven actual CPU middle-supervision protocol checks required','Nineteen actual unchanged-math and committed-boundary CPU checks required')
    probe=once(probe,"old = read_json(ROOT/'configs/phase6/base_next_two_token_comparison.json')", "old = read_json(ROOT/'configs/phase6/base_native_teacher_KD_probe_v2.json')")
    start=probe.index('    references = {}');end=probe.index('    atomic_json(PROPOSAL, proposal)',start)
    probe=probe[:start]+'''    references={}
    for name in ('base_current_objective_evidence.json','base_native_teacher_KD_proposal.json',
                 'base_native_teacher_KD_probe_completion.json','base_native_teacher_KD_compile_completion.json',
                 'base_confidence_penalty_comparison_completion.json','base_on_policy_teacher_comparison_completion.json'):
        references[name]=ref(ROOT/'reports/phase6'/name)
    previous=read_json(ROOT/'reports/phase6/base_native_teacher_KD_proposal.json')
    evidence=read_json(ROOT/'reports/phase6/base_current_objective_evidence.json')
    proposal=dict(created_at=now(),question='Does unchanged dense native short gold-prefix predictive KD transfer useful generation while retaining original Web CE?',
        prior_turn='progress: confidence100M/allJapanese/all80 rejected and committed8eb62f1; scientific729058 absent. Four actual quality failures distinguished from never-trained denseKD.',
        references=references,recipe=RECIPE,parent=old['parent'],teacher=old['teacher'],
        teacher_quality=previous['evidence']['teacher_quality'],teacher_is_adopted_Base=False,
        source_binding=old['source_binding'],goals=old['goals'],batch=48,seed=42,
        native_parameters=10001152,extra_student_parameters=0,teacher_resident_parameters=10001152,
        original_gold_positions=100000000,KD_distribution_positions=25000000,new_unique_dataset_tokens=0,
        novelty='Not a new loss, new teacher or new algorithm. Earlier same eager full-vocabulary native KD passed CUDA/state but never entered science because its self-selected3600 resource plan failed. This is an explicit separate prospective resource-plan reconsideration; no old file or failure is overwritten or retroactively passed. Current user authorization covers local GPU;3600 was not a user lifetime budget.',
        resource_reconsideration=dict(old_total_cap=3600,old_closed=True,old_scientific_gold_positions=0,
            old_median_based_forecast=4029,old_exact_update_mean32_forecast=evidence['untrained_native_KD']['exact17698_mean32_forecast_seconds'],
            new_total_GPU_cap_seconds=4800,new_probe_GPU_cap_seconds=180,
            rationale='Later bounded100M studies used4800 total, including actual confidence1495s/middle1480s; old32 measured steps imply4489s conservative mean forecast. Keep one fixed new4800 plan before new gate/results; reject if new mean forecast plus actual probe exceeds it. This does not reuse discarded old probe weights or change numeric tolerances.'),
        distinction='On-policy279734 distribution positions trained on sampled student contexts; here25M original short-source gold-prefix positions. Closed online rollout, contrast/entropy/anchor routes are not retried. Compiler numeric failure remains failed; this is unchanged eager native math.',
        primary_sources=['https://proceedings.mlr.press/v80/furlanello18a.html'],
        literature_limit='Born Again Neural Networks studies identically parameterized teacher/student, including language modeling. Different language, data, teacher history and optimization; not an exact reproduction or Japanese10M success proof.',
        accounting='Original hard body/EOS CE100M counted once. Add teacher-to-student full4096 forward KL(T1/coefficient1), only textbook/story25M positions, normalized by all original gold positions in each update. Extra distribution targets and teacher valid/physical inputs/entropy/goldprob/KL are separate, not new hard labels or corpus. Student native inference unchanged; frozen teacher never optimized or stored as student weights.',
        acceptance='CPU frozen analytic KL/mask/teacher/source checks plus committed update safety/parity/full save-resume. Actual CUDA4 vs2+2 allstate/history/source/teacher immutable, max48x1024 finite backward/memory, all32 actual postwarmup times. ceil17698*mean32seconds*1.3+900 plus current probe<=4800. Original100M/fullsampler exactly matched to cachedCE; commonDEV256/Japanese192,331,1119/native80/all80 individual reasons and unchanged matched/strong/absolute/historicalWeb quality. Qualification before independent trainedseed/fullDEV/protected finalTEST/adoption.',
        failure='After this prospective reconsideration no further cap/teacher/coefficient/temperature/LR/parent/source/batch/shape/backend/decoder rescue or automatic extension. Keep original3600 and compiled numeric failures intact. Close this study on new gate/budget or quality failure.',
        limitations='Single mature student seed and different historically trained staged teacher;25M extra predictive supervision/teacher compute, repeatedly used nonblind DEV. No isolated data/architecture or capacity proof.',
        CPU_checks=ref(tests),Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
''' +probe[end:]
    probe=probe.replace("fields = ('parent','parent_size','parent_mtime_ns',", "fields = ('parent','parent_size','parent_mtime_ns','teacher','teacher_size','teacher_mtime_ns',")
    probe=once(probe,"    st = Path(p['parent']['path']).stat()\n    if (st.st_size, st.st_mtime_ns) != (p['parent_size'],p['parent_mtime_ns']): raise ValueError('Audited parent identity changed')", "    for name in ('parent','teacher'):\n        st=Path(p[name]['path']).stat()\n        if (st.st_size,st.st_mtime_ns)!=(p[name+'_size'],p[name+'_mtime_ns']): raise ValueError('Pinned checkpoint identity changed: '+name)")
    probe=once(probe,'memory = configure_resident_memory(11987593728)','memory = configure_resident_memory(13047812096)')
    probe=once(probe,"        parent = torch.load(p['parent']['path'], map_location='cpu', weights_only=False)", "        parent = torch.load(p['parent']['path'], map_location='cpu', weights_only=False)\n        teacher = torch.load(p['teacher']['path'], map_location='cpu', weights_only=False)")
    probe=once(probe,'            return (CommittedNativeTeacherKDTrainer if native_teacher_KD else NaturalCorpusTrainer)(parent,sampler,binding,batch=48,contrast=False)',
        "            if not native_teacher_KD: return NaturalCorpusTrainer(parent,sampler,binding,batch=48,contrast=False)\n            return CommittedNativeTeacherKDTrainer(parent,sampler,binding,teacher,p['teacher'],batch=48)")
    probe=once(probe,'            history = []; histories[\'timing\'] = history', "            initial.update(frozen_teacher_weights=equal_state(teacher['model'],host(t.teacher.state_dict())),\n                teacher_eval_no_grad=not t.teacher.training and all(not v.requires_grad for v in t.teacher.parameters()),\n                teacher_native_tied=t.teacher.lm_head.weight is t.teacher.model.embed_tokens.weight,\n                teacher_parameters=sum(v.numel() for v in t.teacher.parameters())==10001152,\n                student_optimizer_only={id(v) for g in t.optimizer.param_groups for v in g['params']}=={id(v) for v in t.model.parameters()})\n            history = []; histories['timing'] = history")
    probe=once(probe,"            speed = statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:])", "            speed = statistics.median(r['CE_targets_this_update']/r['seconds'] for r in history[3:])\n            initial['teacher_unchanged_after35']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())")
    start=probe.index('            before=host(t.model.state_dict())');end=probe.index('            states, logs = [], []',start)
    probe=probe[:start]+'''            before=host(t.model.state_dict());selected=targets.ne(-100)
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                with torch.no_grad(): q=t.teacher.lm_head(right_padded_hidden(t.teacher,ids)[selected]).float()
                logits=t.model.lm_head(right_padded_hidden(t.model,ids)[selected]).float()
                ce=F.cross_entropy(logits,targets[selected]);kl,_=predictive_KL(logits,q,targets[selected],int(selected.sum()))
                combined=ce+kl
            combined.backward();gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(selected.sum()),
                KD_distribution_positions=int(selected.sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,unchanged_weights=equal_state(before,host(t.model.state_dict())),
                CE_loss=float(ce.detach()),KD_loss=float(kl.detach()),combined_loss=float(combined.detach()),gradient_norm=float(gradient),
                scope='Artificial all-KD upper-bound shape; not relabeled Web or new scientific gold')
            initial['teacher_unchanged_after_stress']=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())
            if not capacity['unchanged_weights'] or not all(math.isfinite(capacity[k]) for k in ('CE_loss','KD_loss','combined_loss','gradient_norm')) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite native original CE/KD worst shape required')
            del t,before,ids,targets,selected,logits,q,ce,kl,combined; clear()
''' +probe[end:]
    probe=once(probe,"                t.save(RUN/(route+'.pt')); states.append(host(t.state_dict())); logs.append(history)",
        "                initial['teacher_unchanged_'+route]=equal_state(teacher['model'],host(t.teacher.state_dict())) and all(v.grad is None for v in t.teacher.parameters())\n                t.save(RUN/(route+'.pt')); states.append(host(t.state_dict())); logs.append(history)")
    probe=probe.replace("r.get('KD_distribution_positions_this_update',0)","r.get('KD_targets_this_update',0)")
    save('scripts/probe_base_native_teacher_KD_science.py',probe)
    for name in ('probe','run'):
        save(f'scripts/{name}_base_native_teacher_KD_science.ps1',renamed(f'scripts/{name}_base_middle_supervision.ps1'))
    run=renamed('scripts/run_base_middle_supervision.py')
    run=once(run,'from base_native_teacher_KD_science_trainer import CommittedNativeTeacherKDTrainer, committed_state, RECIPE',
        'from base_native_teacher_KD_committed import CommittedNativeTeacherKDTrainer, committed_state, RECIPE')
    run=once(run,"    'scripts/base_native_teacher_KD_committed.py',", "    'scripts/base_native_teacher_KD_trainer.py','scripts/base_native_teacher_KD_committed.py',")
    run=once(run,"('parent','parent_size','parent_mtime_ns','source_binding','goals',", "('parent','parent_size','parent_mtime_ns','teacher','teacher_size','teacher_mtime_ns','source_binding','goals',")
    run=once(run,"    st = Path(c['parent']['path']).stat()\n    if (st.st_size,st.st_mtime_ns) != (c['parent_size'],c['parent_mtime_ns']): raise ValueError('Audited parent changed')", "    for name in ('parent','teacher'):\n        st=Path(c[name]['path']).stat()\n        if (st.st_size,st.st_mtime_ns)!=(c[name+'_size'],c[name+'_mtime_ns']): raise ValueError('Pinned checkpoint changed: '+name)")
    run=once(run,"        parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)", "        parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)\n        teacher = torch.load(c['teacher']['path'],map_location='cpu',weights_only=False)")
    run=once(run,"binding = dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),", "binding = dict(parent=c['parent'],teacher=c['teacher'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),")
    run=once(run,'t = CommittedNativeTeacherKDTrainer(parent,sampler,binding,batch=48)', "t = CommittedNativeTeacherKDTrainer(parent,sampler,binding,teacher,c['teacher'],batch=48)")
    run=once(run,"                record = dict(status='complete',binding=binding,checkpoint=str(cp),checkpoint_sha256=sha256(cp),", "                teacher_unchanged=equal_state(teacher['model'],host(t.teacher.state_dict()))\n                teacher_frozen=not t.teacher.training and all(not v.requires_grad and v.grad is None for v in t.teacher.parameters())\n                optimizer_student_only={id(v) for g in t.optimizer.param_groups for v in g['params']}=={id(v) for v in t.model.parameters()}\n                if not teacher_unchanged or not teacher_frozen or not optimizer_student_only: raise ValueError('Actual frozen teacher and student-only optimizer required')\n                record = dict(status='complete',binding=binding,checkpoint=str(cp),checkpoint_sha256=sha256(cp),\n                    teacher_unchanged=teacher_unchanged,teacher_eval_no_grad=teacher_frozen,optimizer_student_only=optimizer_student_only,")
    run=run.replace('scientific_KD_distribution_positions=100000000','scientific_KD_distribution_positions=25000000')
    run=run.replace('One fixed middle-supervision condition; no coefficient/layer/curriculum/dropout/LR/source/parent/batch/cap rescue', 'One fixed new resource study; no further cap/teacher/coefficient/temperature/LR/source/parent/batch/backend/decoder rescue')
    save('scripts/run_base_native_teacher_KD_science.py',run)
    review=renamed('scripts/review_base_middle_supervision.py')
    review=once(review,'from base_native_teacher_KD_science_trainer import KIND, committed_state, RECIPE',
        'from base_native_teacher_KD_committed import KIND, committed_state, RECIPE')
    review=review.replace("state['spec']['native_teacher_KD']!=RECIPE", "state['spec']['prospective_KD_study']!=RECIPE")
    review=review.replace("record['scientific_KD_distribution_positions']!=100000000", "record['scientific_KD_distribution_positions']!=25000000")
    review=once(review,"        record['scientific_KD_distribution_positions']!=25000000 or not equal_state(state['sampler'],record['sampler']) or", "        record['scientific_KD_distribution_positions']!=25000000 or\n        not all(record.get(k) is True for k in ('teacher_unchanged','teacher_eval_no_grad','optimizer_student_only')) or\n        state['spec']['teacher']!=c['teacher'] or state['binding']['teacher']!=c['teacher'] or\n        not equal_state(state['sampler'],record['sampler']) or")
    review=review.replace('scientific_KD_distribution_positions=100000000','scientific_KD_distribution_positions=25000000')
    review=review.replace('only added middle-layer loss differs','original full-vocab native short-prefix KD math; separately reconsidered prospective resource plan. Extra25M predictive positions/teacher compute differ')
    start=review.index('    if any(not all(math.isfinite(r[k])');end=review.index('    if template:',start)
    review=review[:start]+'''    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','KD_loss','combined_loss','gradient_norm')) or
            abs(r['combined_loss']-(r['CE_loss']+r['KD_loss']))>2e-6 or r['committed_update'] is not True or
            r['native_teacher_KD']['updates']!=u or
            r['native_teacher_KD']['teacher_positions']!=sum(r['source_teachers'][g] for g in ('textbook','story')) or
            r['native_teacher_KD']['source_positions']!={g:(r['source_teachers'][g] if g in ('textbook','story') else 0) for g in ('web','textbook','story')} or
            not 0<=r['KD_targets_this_update']<=r['CE_targets_this_update']
            for u,r in history.items()): raise ValueError('Finite committed original CE/dense short-KD full history required')
''' +review[end:]
    review=review.replace('mature-parent single-middle-loss transition','mature-parent native dense-KD resource study').replace('middle original-gold supervision and extra head compute differ','extra25M predictive targets and frozen teacher compute; same original100M gold')
    save('scripts/review_base_native_teacher_KD_science.py',review)
    save('tests/test_base_native_teacher_KD_science_run.py',renamed('tests/test_base_middle_supervision_run.py'))
    launch=renamed('scripts/record_base_middle_supervision_launch.py')
    launch=once(launch,"        not result['capacity']['unchanged_weights'] or result['capacity']['decoder_forwards']!=1 or", "        not result['capacity']['unchanged_weights'] or")
    launch=launch.replace('scientific_KD_distribution_positions=100000000','scientific_KD_distribution_positions=25000000')
    launch=launch.replace('actual_middle_CUDA','actual_native_dense_KD_CUDA').replace('middle head100M','short distribution25M')
    launch=once(launch,"    paths.update(ROOT/name for name in (*p['source_sha256'],*c['source_sha256']) if 'base_native_teacher_KD_science' in name)", "    paths.update(ROOT/name for name in (*p['source_sha256'],*c['source_sha256']))")
    save('scripts/record_base_native_teacher_KD_science_launch.py',launch)
    for path,text in PENDING.items(): (ROOT/path).write_text(text)
    print('Separate native KD study workflow created; actual GPU/config/results0')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
