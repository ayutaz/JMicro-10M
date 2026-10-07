"""Create one independent confidence-penalty workflow without altering prior evidence."""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]


def once(text,old,new):
    if text.count(old)!=1: raise ValueError('Expected exactly one source block: '+old[:100])
    return text.replace(old,new)


def renamed(path):
    return ((ROOT/path).read_text().replace('base_middle_supervision','base_confidence_penalty')
        .replace('base-middle-supervision','base-confidence-penalty')
        .replace('MiddleSupervisionTrainer','ConfidencePenaltyTrainer')
        .replace('middle_supervision','confidence_penalty')
        .replace('middle_gold_evaluations','confidence_positions')
        .replace('middle_losses','confidence_losses'))


def save(path,text):
    target=ROOT/path
    if target.exists(): raise ValueError('Preserve separate confidence workflow: '+path)
    target.write_text(text)


def main():
    probe=renamed('scripts/probe_base_middle_supervision.py')
    probe=probe.replace('!= 11 or any','!= 13 or any').replace('Eleven actual CPU middle-supervision protocol checks required','Thirteen actual CPU confidence-penalty protocol checks required')
    start=probe.index('    references = {}'); end=probe.index('    atomic_json(PROPOSAL, proposal)',start)
    probe=probe[:start]+'''    references = {}
    for name in ('base_failure_route_synthesis.json','base_recent_objective_failure_synthesis.json',
                 'base_middle_supervision_comparison_completion.json','base_label_smoothing_comparison_completion.json',
                 'base_sam_comparison_completion.json','base_on_policy_teacher_comparison_completion.json'):
        references[name]=ref(ROOT/'reports/phase6'/name)
    proposal=dict(created_at=now(),question='Does fixed negative prediction entropy improve native Japanese Base continuation quality at the same original100M gold budget?',
        prior_turn='Boundary-confirmation-only turn was no progress; middle100M/all80 rejected and committed40ac32c before it. No live scientific GPU job at preparation.',
        references=references,
        novelty='Registry and trainer inspection found no implemented fixed KL(student prediction||full native uniform) confidence loss. Closed uniform label smoothing used0.9CE+0.1uniform cross-entropy/opposite KL(uniform||prediction). This keeps original CE coefficient1 and adds0.1 reverse-uniform KL. The numerical0.1 does not imply equal regularization strength. Not a repeat of softened gold, teacher KL, middle-head CE or weight perturbation.',
        primary_sources=['https://arxiv.org/abs/1701.06548','https://arxiv.org/html/1701.06548v1'],
        literature_limit='Pereyra et al.2017 sections3/3.2 motivate negative entropy and reversed uniform KL; Penn Treebank language-model experiments are not Japanese10M continuation evidence or an exact reproduction. Coefficient0.1 is one fixed conservative exploratory choice, not an asserted literature optimum. Calibration has not been proven the cause; at a saturated delta the entropy-only gradient also vanishes.',
        recipe=RECIPE,parent=old['parent'],source_binding=old['source_binding'],goals=old['goals'],
        batch=48,seed=42,native_parameters=10001152,extra_parameters=0,original_teachers=100000000,
        confidence_positions=100000000,new_unique_dataset_tokens=0,control_reused_GPU_seconds=0,
        total_GPU_cap_seconds=4800,probe_GPU_cap_seconds=180,CPU_checks=ref(tests),
        accounting='One native decoder/head forward; same hard-gold body/EOS/input/mask stream counted once. KL(p||uniform)=log4096-H(p) evaluated at those same100M positions; it is not new labels, data or extra teacher forwards. Original mean CE+0.1mean KL, one backward and Adam update; unchanged inference.',
        acceptance='Independent analytic CE/KL/logit-gradient/sign/mask/bounds/shift tests; native final CE/gradient parity; full state and original source/save-resume. Actual CUDA4 vs2+2 and all48x1024 finite backward/memory;32 actual postwarmup times, exact17698-update mean forecast*1.3+900 plus actual probe<=4800. Reuse cachedCE and require fullstream/sampler; commonDEV256/Japanese192,331,1119/all80 and unchanged matched/strong/absolute/historicalWeb gates. Only a qualified candidate gets independent trainedseed/fullDEV/protected finalTEST/adoption.',
        failure='Close this fixed condition on numeric/state/stream/budget or quality failure. No coefficient/temperature/annealing/threshold/LR/parent/data/batch/decoder/cap rescue or automatic extension.',
        limitations='One conservative-LR mature-parent transition and repeatedly used nonblind DEV. Entropy regularization can worsen hard-gold prediction and EOS. Failure does not prove all entropy objectives, different data or learning amounts ineffective.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
''' +probe[end:]
    start=probe.index('            before=host(t.model.state_dict())'); end=probe.index('            states, logs = [], []',start)
    probe=probe[:start]+'''            before=host(t.model.state_dict())
            with sdpa_kernel(SDPBackend.FLASH_ATTENTION),torch.autocast('cuda',dtype=torch.bfloat16):
                ce,penalty,combined,entropy=confidence_losses(t.model,ids,targets)
            combined.backward()
            gradient=torch.nn.utils.clip_grad_norm_(t.model.parameters(),1.,error_if_nonfinite=True)
            torch.cuda.synchronize()
            capacity=dict(context=1024,target_stride=512,batch=48,original_target_positions=int(targets.ne(-100).sum()),
                confidence_positions=int(targets.ne(-100).sum()),peak_VRAM_bytes=torch.cuda.max_memory_allocated(),
                optimizer_updates=0,unchanged_weights=equal_state(before,host(t.model.state_dict())),
                CE_loss=float(ce.detach()),confidence_KL_loss=float(penalty.detach()),prediction_entropy=float(entropy.detach()),combined_loss=float(combined.detach()),
                gradient_norm=float(gradient),decoder_forwards=1)
            if not capacity['unchanged_weights'] or not all(math.isfinite(capacity[k]) for k in ('CE_loss','confidence_KL_loss','prediction_entropy','combined_loss','gradient_norm')) or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Finite single-forward native confidence worst shape required')
            del t,before,ids,targets,ce,penalty,combined,entropy; clear()
''' +probe[end:]
    save('scripts/probe_base_confidence_penalty.py',probe)
    for name in ('probe','run'):
        save(f'scripts/{name}_base_confidence_penalty.ps1',renamed(f'scripts/{name}_base_middle_supervision.ps1'))
    run=renamed('scripts/run_base_middle_supervision.py')
    run=run.replace('One fixed middle-supervision condition; no coefficient/layer/curriculum/dropout/LR/source/parent/batch/cap rescue',
        'One fixed confidence condition; no coefficient/temperature/annealing/threshold/LR/source/parent/batch/decoder/cap rescue')
    save('scripts/run_base_confidence_penalty.py',run)
    review=renamed('scripts/review_base_middle_supervision.py')
    review=review.replace('only added middle-layer loss differs','only added native confidence loss differs')
    start=review.index('    if any(not all(math.isfinite(r[k])');end=review.index('    if template:',start)
    review=review[:start]+'''    if any(not all(math.isfinite(r[k]) for k in ('CE_loss','confidence_KL_loss','prediction_entropy','combined_loss','gradient_norm')) or
            abs(r['combined_loss']-(r['CE_loss']+.1*r['confidence_KL_loss']))>2e-6 or
            abs(r['confidence_KL_loss']+r['prediction_entropy']-math.log(4096))>2e-6 or
            not -2e-6<=r['confidence_KL_loss']<=math.log(4096)+2e-6 or
            r['confidence_penalty']!=dict(updates=u,positions=r['supervised_tokens']) or
            r['confidence_positions_this_update']!=r['CE_targets_this_update'] or r['decoder_forwards_this_update']!=1
            for u,r in history.items()): raise ValueError('Actual finite unchanged hard-gold CE+confidence KL history required')
''' +review[end:]
    review=review.replace('mature-parent single-middle-loss transition','mature-parent confidence-loss transition').replace('middle original-gold supervision and extra head compute differ','prediction entropy regularization differs; same hard gold and native head')
    save('scripts/review_base_confidence_penalty.py',review)
    save('tests/test_base_confidence_penalty_run.py',renamed('tests/test_base_middle_supervision_run.py'))
    record=renamed('scripts/record_base_middle_supervision_launch.py')
    record=record.replace('actual_middle_CUDA','actual_confidence_CUDA').replace('middle head100M','confidence positions100M')
    save('scripts/record_base_confidence_penalty_launch.py',record)
    print('Separate confidence workflow created; actual GPU/config/results0')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
