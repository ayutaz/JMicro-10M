"""One-shot independent workflow generation; preserves all historical sources."""
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parents[1]


def once(text,old,new):
    if text.count(old)!=1: raise ValueError('Expected one source block: '+old[:100])
    return text.replace(old,new)


def renamed(path):
    text = ((ROOT/path).read_text().replace('base_sam','base_middle_supervision')
        .replace('base-sam','base-middle-supervision').replace('SAMTrainer','MiddleSupervisionTrainer')
        .replace('sam_backward','middle_supervision_backward')
        .replace('SAM','middle_supervision').replace('7200','4800'))
    return re.sub(r'\bsam\b','middle_supervision',text)


def save(path,text):
    p=ROOT/path
    if p.exists(): raise ValueError('Preserve independent middle workflow: '+path)
    p.write_text(text)


def main():
    probe=renamed('scripts/probe_base_sam.py')
    probe=once(probe,'committed_state, middle_supervision_backward, RECIPE','committed_state, middle_losses, RECIPE')
    probe=probe.replace('!= 9 or any','!= 11 or any').replace('Nine actual CPU middle_supervision protocol checks required','Eleven actual CPU middle-supervision protocol checks required')
    probe=once(probe,"    'tests/test_base_middle_supervision_trainer.py', 'scripts/prepare_base_middle_supervision_workflow.py',", "    'tests/test_base_middle_supervision_trainer.py', 'scripts/prepare_base_middle_supervision_workflow.py',")
    start=probe.index('    references = {}'); end=probe.index('    atomic_json(PROPOSAL, proposal)',start)
    probe=probe[:start]+'''    references = {}
    for name in ('base_failure_route_synthesis.json','base_sam_comparison_completion.json',
                 'base_on_policy_teacher_comparison_completion.json','base_next_two_token_comparison_completion.json',
                 'base_gradient_precision_completion.json'):
        references[name]=ref(ROOT/'reports/phase6'/name)
    proposal=dict(created_at=now(),question='Does supervising the original next token at one native middle layer improve full-depth Japanese Base generalization?',
        prior_turn='progress: SAM100M/all Japanese/all80 content rejected and committed b010368; scientific process721383 absent.',
        references=references,
        novelty='Inspected proposal/completion/source registry: no native intermediate-layer original next-token CE found. Old next-two MTP used final hidden plus a fresh train-only Block/norm for future targets; this uses unchanged current gold at native layer6/13 through shared final norm/head. No teacher, perturbation, representation pairing, extra layer or learned head. Novelty is not evidence of causation or success.',
        primary_sources=['https://aclanthology.org/2024.acl-long.681/','https://aclanthology.org/2024.acl-long.681.pdf'],
        literature_limit='LayerSkip4.1.2 shares one LM head for early-layer CE but also uses layer dropout, normalized multi-layer weights and curriculum. Its authors report that all-layer losses every iteration can reduce last-layer accuracy. This isolated single-middle CE, fixed0.1, no dropout/curriculum/early-exit inference is an exploratory ablation, not an exact reproduction or proven Japanese10M remedy.',
        recipe=RECIPE,parent=old['parent'],source_binding=old['source_binding'],goals=old['goals'],
        batch=48,seed=42,native_parameters=10001152,extra_parameters=0,original_teachers=100000000,
        middle_gold_evaluations=100000000,new_unique_dataset_tokens=0,control_reused_GPU_seconds=0,
        total_GPU_cap_seconds=4800,probe_GPU_cap_seconds=180,CPU_checks=ref(tests),
        accounting='One original decoder forward and source/body/EOS/mask stream counted once. Same100M positions projected at middle layer separately count100M repeated gold head evaluations, not extra inputs, new data or unique corpus. Single backward/Adam update for finalCE+0.1middleCE; no inference changes.',
        acceptance='CPU independent masked CE/combined-gradient formula, original final gradient parity, auxiliary gradient reaches embedding/early layers/shared norm/head and not later layers; full state/save-resume/source. Actual CUDA4 vs2+2, all48x1024 finite gradients/memory, all32 step times. Forecast ceil17698*mean32seconds*1.3+900 plus actual probe <=4800. Same cachedCE stream/fullsampler; native DEV256/commonbyte/Japanese192,331,1119/all80; all unchanged matched/strong/absolute/historicalWeb gates. Qualified candidate only gets independent trainedseed/fullDEV/protected finalTEST/adoption.',
        failure='Close this fixed layer/coefficient condition on finite/state/gradient/budget or quality failure. No auxiliary coefficient/layer/curriculum/dropout/LR/parent/data/batch/decoder/cap rescue or automatic extension.',
        limitations='One conservative-LR mature-parent transition, repeated fixed nonblind DEV, extra shared-head compute. An isolated loss change may worsen full-depth quality; negative result does not prove all deep supervision or data increases ineffective.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
''' + probe[end:]
    start=probe.index('            selected=targets.ne(-100)');end=probe.index('            states, logs = [], []',start)
    probe=probe[:start]+'''            before=host(t.model.state_dict())
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                ce,auxiliary,combined=middle_losses(t.model,ids,targets)
            combined.backward()
            gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(targets.ne(-100).sum()),
                middle_gold_evaluations=int(targets.ne(-100).sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,unchanged_weights=equal_state(before,host(t.model.state_dict())),
                CE_loss=float(ce.detach()),middle_CE_loss=float(auxiliary.detach()),combined_loss=float(combined.detach()),
                gradient_norm=float(gradient),decoder_forwards=1)
            if not capacity['unchanged_weights'] or not all(math.isfinite(capacity[k]) for k in ('CE_loss','middle_CE_loss','combined_loss','gradient_norm')) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite single-forward shared middle-head worst shape required')
            del t,before,ids,targets,ce,auxiliary,combined; clear()
''' +probe[end:]
    probe=once(probe,"verification_repeated_teacher_evaluations=sum(r.get('repeated_teacher_positions_this_update',0)","verification_middle_gold_evaluations=sum(r.get('middle_gold_evaluations_this_update',0)")
    save('scripts/probe_base_middle_supervision.py',probe)
    for source in ('scripts/probe_base_sam.ps1','scripts/run_base_sam.ps1'):
        save(source.replace('base_sam','base_middle_supervision'),renamed(source))
    run=renamed('scripts/run_base_sam.py')
    run=run.replace("optimizer='fresh_AdamW_after_same_batch_full_parameter_middle_supervision',middle_supervision_recipe=RECIPE", "optimizer='fresh_AdamW_lr1e-5_wd0.1_constant',middle_supervision_recipe=RECIPE")
    run=run.replace('scientific_repeated_teacher_evaluations=100000000','scientific_middle_gold_evaluations=100000000')
    run=run.replace('One fixed optimizer transition; no rho/adaptive/period/LR/source/parent/batch/teacher/cap rescue','One fixed middle-supervision condition; no coefficient/layer/curriculum/dropout/LR/source/parent/batch/cap rescue')
    save('scripts/run_base_middle_supervision.py',run)
    review=renamed('scripts/review_base_sam.py')
    review=once(review,'import json\n','import json\nimport math\n')
    review=review.replace('only optimizer transition differs','only added middle-layer loss differs')
    start=review.index('    if any(not all(math.isfinite(r[k])');end=review.index('    if template:',start)
    review=review[:start]+'''    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','middle_CE_loss','combined_loss','gradient_norm')) or
            abs(r['combined_loss']-(r['CE_loss']+.1*r['middle_CE_loss']))>2e-6 or
            r['middle_supervision']!=dict(updates=u,middle_gold_evaluations=r['supervised_tokens']) or
            r['middle_gold_evaluations_this_update']!=r['CE_targets_this_update'] or r['decoder_forwards_this_update']!=1
            for u,r in history.items()): raise ValueError('Actual finite combined CE/same-gold middle-head history required')
''' +review[end:]
    review=review.replace('scientific_repeated_teacher_evaluations','scientific_middle_gold_evaluations')
    review=review.replace('mature-parent optimizer transition','mature-parent single-middle-loss transition').replace('second same-batch gradient and extra compute differ','middle original-gold supervision and extra head compute differ')
    review=review.replace('restored original100M/middle_supervision two-pass','original100M/middle-head')
    save('scripts/review_base_middle_supervision.py',review)
    save('tests/test_base_middle_supervision_run.py',renamed('tests/test_base_sam_run.py'))
    print('Separate middle-supervision workflow created; GPU/configs/results0')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
