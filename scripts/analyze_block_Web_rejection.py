"""CPU analysis of actual finite rejection; no new CUDA, quality or rescue."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
import math
from pathlib import Path
import sys
import time
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive,finite_state
import run_block_Web_constraint as study


def main():
    started=time.monotonic();torch.set_num_threads(2);c=study.inspect(study.CONFIG)
    result=read_json(study.RUN/'compare-result.json');job=read_json(study.RUN/'job.json');rejected=result['finite_rejection']
    if job['status']!='complete' or alive(job) or result['GPU_seconds']!=job['GPU_elapsed_seconds']:raise ValueError('Actual terminated rejection required')
    study.check_reference(rejected['last_valid_checkpoint'])
    state=torch.load(rejected['last_valid_checkpoint']['path'],map_location='cpu',weights_only=False)
    log=study.RUN/study.ARM/'training/metrics.jsonl';history=[json.loads(s) for s in log.read_text().splitlines()]
    expected=[json.loads(s) for s in Path(c['references']['staged_metrics']['path']).read_text().splitlines()]
    accepted=rejected['accepted_source_updates'];aux=rejected['accepted_auxiliary'];decision=rejected['last_rejection']['decision']
    parent_update=state['lineage']['parent_update']
    if (state['lineage']['parent']!=c['parent'] or accepted!=len(history) or state['update']-parent_update!=accepted or accepted%20
            or rejected['accepted_source_CE_teacher_tokens']!=sum(state['sampler']['prefix_mask_accounting']['actual']['teachers'].values())
            or state['study_binding']!=study.binding(c,study.CONFIG) or not finite_state(state)
            or state['auxiliary']!=aux or history[-1]['accepted_auxiliary']!=aux
            or [r['update'] for r in history]!=list(range(parent_update+1,state['update']+1))
            or any(r['reference_token_digest']!=e['token_digest'] for r,e in zip(history,expected[:accepted],strict=True))
            or any(r['lr']!=.00001 or not math.isfinite(r['loss']) or not math.isfinite(r['gradient_norm']) for r in history)
            or aux['accepted_updates']!=accepted or aux['accepted_blocks']!=accepted//20):raise ValueError('Accepted partial ledger differs')
    boundaries=[r for r in history if 'block_GPU_seconds' in r]
    if len(boundaries)!=accepted//20 or any(not r['boundary_constraint']['accepted'] or r['boundary_constraint']['final_body_NLL']>c['reference_body_NLL']*1.01 for r in boundaries):
        raise ValueError('Accepted boundary constraint differs')
    if (decision['accepted'] or len(decision['trials'])!=5 or any(t['body_NLL']<=decision['ceiling_body_NLL'] for t in decision['trials'])
            or not rejected['whole_block_restored'] or rejected['last_rejection']['restored_last_completed_update']!=state['update']
            or state['last_constraint']!=boundaries[-1]['boundary_constraint']):raise ValueError('Actual failed proposals/rollback boundary differs')
    proposed=decision['proposed_body_NLL'];corrected=decision['trials'][1]['body_NLL'];ceiling=decision['ceiling_body_NLL']
    linear_corrected=proposed-decision['projection_coefficient']*decision['gradient_norm_squared']
    residual=corrected-linear_corrected;desired=proposed-linear_corrected;achieved=proposed-corrected
    before=state['last_constraint']['final_body_NLL'];last_trial=decision['trials'][-1]['body_NLL']
    proposal=read_json(study.PROPOSAL);old_proposal=read_json(ROOT/'reports/phase6/finite_Web_constraint_proposal.json')
    clarification=dict(raw_inherited_provenance_fields=['algorithm','required_before_science'],
        inherited_fields_equal_original=all(proposal[k]==old_proposal[k] for k in ('algorithm','required_before_science')),
        active_prelaunch_fields=['kind','block_updates','scope_difference','transaction','persistence','probe','measured_budget','no_rescue'],
        explanation='Raw block proposal accidentally retained the original per-update algorithm/prerequisite prose. Explicit block fields and prelaunch configs/trainer/CPU/CUDA evidence already define20-boundary operation. Raw records preserved; this clarification changes no experimental/quality threshold.',
        unchanged_quality_selection=proposal['selection']==old_proposal['selection'])
    if not clarification['inherited_fields_equal_original'] or not clarification['unchanged_quality_selection']:raise ValueError('Original quality/provenance changed')
    observations=rejected['last_rejection']['auxiliary_completed_calls'];exposures=rejected['last_rejection']['attempted_source_gradient_teacher_tokens']
    report=dict(status='fixed20_rejection_nonlinear_correction_residual_analyzed',created_at=now(),
        result=study.reference(study.RUN/'compare-result.json'),accepted_checkpoint=rejected['last_valid_checkpoint'],history=study.reference(log),
        accepted_source_updates=accepted,accepted_source_CE_teachers=rejected['accepted_source_CE_teacher_tokens'],
        accepted_source_by_genre=state['sampler']['prefix_mask_accounting']['actual']['teachers'],accepted_auxiliary=aux,
        rejected_source_gradient_teacher_exposures=exposures,rejected_auxiliary=observations,
        accepted_source_plus_auxiliary_gradient_teachers=rejected['accepted_source_CE_teacher_tokens']+aux['gradient_teacher_tokens'],
        all_science_accepted_and_rejected_gradient_teacher_exposures=rejected['accepted_source_CE_teacher_tokens']+aux['gradient_teacher_tokens']+exposures+observations['gradient_teacher_tokens'],
        own_probe_source_CE_teachers=c['verification_teacher_tokens'],
        safe_boundary_body_NLL=before,ceiling_body_NLL=ceiling,safe_boundary_slack=ceiling-before,
        proposed_body_NLL=proposed,linear_predicted_corrected_body_NLL=linear_corrected,actual_corrected_body_NLL=corrected,
        actual_positive_nonlinear_residual=residual,intended_linear_NLL_reduction=desired,actual_NLL_reduction=achieved,
        actual_fraction_of_intended_reduction=achieved/desired,interior_margin=c['reference_body_NLL']*1e-5,
        nonlinear_residual_to_margin_ratio=residual/(c['reference_body_NLL']*1e-5),
        final_fixed_backtrack_body_NLL=last_trial,final_backtrack_excess_above_ceiling=last_trial-ceiling,
        interpretation='Stored finite observations show the one-gradient correction undershot its linear target. All fixed corrected/backtracked proposals fail the actual limit; prior saved boundary remains feasible. This diagnoses this solver/trial set, not impossibility of every learning solution or model capacity/data quantity.',
        conditional_learning_reached=state['sampler']['prefix_mask_accounting']['actual']['teachers']['conditional_textbook']>0,
        all_original_staged_reference_rows_match=True,all_saved_boundary_losses_bounded=True,
        Base_quality_evaluation_performed=False,generated_content_review_count=0,protected_test_used=False,Base_complete=False,Base_adopted=False,
        Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,proposal_metadata_clarification=clarification,
        actual_science_GPU_seconds=result['GPU_seconds'],own_probe_GPU_seconds=c['verification_GPU_seconds'],previous_related_GPU_seconds=c['previous_related_GPU_seconds'],
        new_GPU_seconds=0,new_learning_teacher_tokens=0,
        next_action='End this fixed20/one-correction recipe. Research a distinct evidence-backed Base mechanism from the measured nonlinear solver residual and unreached conditional stage; no cadence/projector/backtrack/source/checkpoint rescue or quality-gate relaxation.')
    elapsed=time.monotonic()-started
    if elapsed>20:raise TimeoutError('CPU rejection analysis20s exhausted')
    report['CPU_seconds']=elapsed
    destination=ROOT/'reports/phase6/block_Web_constraint_failure_analysis.json'
    if destination.exists():raise ValueError('Preserve original rejection analysis')
    atomic_json(destination,report)
    prefix=f"固定20境界Baseの失敗原因を既存rawからCPU分析（2026-10-06 JST）。Base未完成・実完成時通知停止、Chat/Dialogue/SFT/量子化なし。\n\n受入{accepted}更新/{report['accepted_source_CE_teachers']}CE教師＋memory gradient{aux['gradient_teacher_tokens']}、拒否20更新/{exposures}source梯度＋memory gradient{observations['gradient_teacher_tokens']}別会計。全science梯度exposures{report['all_science_accepted_and_rejected_gradient_teacher_exposures']}、ownprobe{c['verification_teacher_tokens']}教師は別。最終安全NLL{before:.9f}、上限{ceiling:.9f}。単一gradientの線形予測{linear_corrected:.9f}に対して実修正後{corrected:.9f}、正の非線形残差{residual:.9f}/内側marginの{report['nonlinear_residual_to_margin_ratio']:.2f}倍。最後0.125の実NLL{last_trial:.9f}も上限を{last_trial-ceiling:.9f}超えるため規定通り全区切りrollback。単一修正/固定試行が不十分という局所TRAIN診断で、全学習解不存在やモデル容量/教材不足の証明ではない。条件教材の学習到達={report['conditional_learning_reached']}、全91,641,755/日本語・全80/品質評価は未達。分析CPU{elapsed:.6f}秒/20、新GPU/学習0。science193.647秒＋ownprobe33.679＋旧診断70.561=関連297.887秒/2400。\n\nraw proposalへ残った旧毎更新algorithm/prerequisite文言は元provenanceのまま保持し、事前に凍結したkind/block_updates/transaction/probe/budgetおよび実trainer/CPU/CUDAをactive20境界契約と明示。品質selectionは旧と完全一致、後から基準を変えて採用していない。次は固定分岐を終了し、この非線形残差と条件段階未到達の根拠から別のBase改善機構を研究・定義。cadence/projector/backtrack/source/CP救済sweepなし。元10B UI保持・WSL uv3.12.7/local commitのみ/pushなし、全旧失敗/数値7/Phase0–3保持。以下は過去の履歴。\n\n"
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status=report['status'],updated_at=now(),next_action=report['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['block_Web_constraint_failure_analysis']=study.reference(destination);atomic_json(p,progress)
    print(json.dumps(dict(status=report['status'],CPU_seconds=elapsed,residual=residual,conditional_reached=report['conditional_learning_reached']),ensure_ascii=False))


if __name__=='__main__':main()
