"""Define a finite packed-history ablation without changing the failed recipe."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import json
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_source_gradient_attribution import original_UI
import diagnose_source_gradient_attribution as prior


def main():
    c=prior.inspect();r=read_json(prior.RUN/'result.json');job=read_json(prior.RUN/'job.json')
    completion_path=ROOT/'reports/phase6/source_gradient_attribution_completion.json';completion=read_json(completion_path)
    destination=ROOT/'reports/phase6/document_context_ablation_proposal.json'
    if destination.exists():raise ValueError('Preserve original finite context hypothesis')
    if (job['status']!='complete' or alive(job) or completion['result']['sha256']!=sha256(prior.RUN/'result.json')
            or r['new_teacher_tokens'] or r['optimizer_updates'] or not r['RNG_restored']):
        raise ValueError('Actual no-learning attribution completion required')
    summaries=completion['summaries'];a=summaries['original_fullparent'];b=summaries['completed_masked_mixed']
    ui=original_UI()
    proposal=dict(status='defined_readonly_context_ablation_not_implemented_not_launched',created_at=now(),
        trigger=prior.reference(completion_path),
        evidence=dict(conditional_teacher_fraction=b['groups']['conditional_total']['teacher_fraction'],
            original_conditional_CE=a['groups']['conditional_total']['teacher_weighted_CE'],
            completed_conditional_CE=b['groups']['conditional_total']['teacher_weighted_CE'],
            original_conditional_EOS_CE=a['groups']['conditional_EOS']['teacher_weighted_CE'],
            completed_conditional_EOS_CE=b['groups']['conditional_EOS']['teacher_weighted_CE'],
            original_conditional_gradient_total_squared_norm_contribution=a['groups']['conditional_total']['median_contribution_to_total_squared_norm'],
            completed_conditional_gradient_total_squared_norm_contribution=b['groups']['conditional_total']['median_contribution_to_total_squared_norm']),
        interpretation='Conditional source has1.77percent of these actual labels but initially about20.59percent median contribution to total gradient squared norm, '
            'then fits its TRAIN body/EOS closely while natural generation remains rejected. Label count alone does not establish insufficient optimization dose. '
            'Do not automatically normalize/reweight CE or restart a ratio/EOS/mask sweep. Source coverage, packing dependence and generalization remain distinct possibilities.',
        question='Does the completed model rely on other documents in the packed TRAIN history to achieve its low conditional outcome/EOS loss?',
        hypothesis='The original unpadded1024 blocks contain multiple BOS-marked documents but causal attention has no document boundary reset. '
            'Compare existing full causal history with same-document causal history at identical fixed inputs/targets/positions. '
            'An isolated prompt at generation has no previous packed documents. Cross-document reliance is a testable context mismatch, not a proven cause.',
        frozen_checkpoints=c['checkpoints'],
        fixed_inputs=dict(samples=c['references']['samples'],metadata=c['references']['samples_metadata'],
            logical_batch=32,microbatch=8,context=1024,consecutive_TRAIN_batches_per_model=16),
        cached_full_causal_reference=prior.reference(prior.RUN/'result.json'),
        source_config=prior.reference(prior.CONFIG),
        sole_new_forward='Native learned model/BF16/math eval. For each sequence define document_id=cumsum(input_id==BOS2). '
            'Allowed keys are causal keys with the same document_id as the query. The leading partial document is its own segment. '
            'Keep original absolute RoPE positions, all input IDs, body/EOS labels, logical denominator and8-sequence numeric chunks unchanged. '
            'No parameter, vocabulary, role, target mask, source ratio, source text, CE coefficient, sampler or decoder changes.',
        reference_reuse='Reuse all32 existing full-causal point CE/group counts unchanged. No full old-model/old-suite GPU reevaluation. '
            'One first8-sequence control per fixed checkpoint must verify custom full-causal path equals the native existing fast path before interpreting isolated scores.',
        numerical_protocol='CPU actual small-model control allclose atol1e-6/rtol1e-6 and boundary isolation/noninterference/correct causal direction. '
            'Own BF16 control allclose atol.02/rtol.002, record maximum absolute/RMS differences and native-vs-custom CE difference. '
            'Both paths at first8 only; all16 ablation deltas use cached native original scores and retain any numeric difference as a limitation. '
            'A failed control ends this assay; do not widen tolerances.',
        read_only='No optimizer construction/step or autograd graph. Verify actual weights unchanged/grad absent/eval/finite/RNG restored, '
            'all identical input/group counts/teacher denominators and frozen references. Persist actual PID/boot/start/log/task positions; '
            'inspect existing jobs before launch and restore original UI afterwards.',
        summaries='Report all32 fixed point deltas and teacher-weighted group CE differences, conditional outcome/EOS separately, '
            'per-point direction counts and descriptive min/median/max. All16 shared input batches are correlated local TRAIN evidence, not independent natural-language quality.',
        CPU_preparation_ceiling_seconds=15,total_new_GPU_ceiling_seconds=30,optimizer_updates=0,new_teacher_tokens=0,
        descriptive_marker=dict(completed_conditional_CE_increase_at_least_nats=.1,completed_logical_batches_with_increase_at_least_nats=.1,
            completed_batches_at_least=12,learned_endpoint_only_not_parent_selection=True),
        completion='Actual all16 isolated point evaluations at both fixed checkpoints/control checks/all deltas/readonly invariant/terminal/UI/portable evidence/commit. '
            'No new learning, generation rescoring, protected test or Base adoption.',
        followup='Only if the predeclared TRAIN dependence marker is supported, define a separate paired Base learning comparison of packed attention policies. '
            'Both learning arms must use identical inputs/masked targets/source quotas/model/Adam/LR and the same measured numerical batch/backend, own CUDA resume/timing/finite-budget checks, '
            'and all unchanged strong-relative/absolute/historicalWeb quality gates. Cached old Flash/compile trajectory cannot be the sole matched numeric control. '
            'If the marker is unsupported, finish this packing hypothesis without a training/packing/source/mask variant.',
        failure='End the one fixed assay on readiness/numeric/source/budget failure; no input/endpoint reselection or tolerance/weight/ratio/mask/source/LR/decoder sweep.',
        original_UI=ui,quality_criteria_unchanged=True,protected_test_used=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        next_action='Implement the native document-boundary causal forward, meaningful CPU isolation/control tests and persistent bounded read-only runner before any CUDA.')
    atomic_json(destination,proposal)
    prefix='''TRAIN勾配診断の解釈と一つの文書境界context仮説を定義（2026-10-06 JST）。前診断は6bae3d1へ保存。Baseのみ継続/実完成時に通知・停止、Chat/Dialogue/SFT/量子化なし。

固定TRAIN16で条件文の実教師比1.772%に対し元親の全勾配二乗への寄与中央値20.594%、終端0.344%。本文CE2.159→.197/EOS6.615→.008565で学習例はよく予測されるが、自然な生成80は一貫性11/EOS22/反復35で不採用。教師比だけでloss希釈や学習不足を確定せず、reference-mass再重み付けは起動しない。既文学+Web/Wikipedia/自然story/別public source等の失敗も保持し、無制限のsource/filter探索へ戻らない。

document_context_ablation_proposal.jsonで元causal packingの文書間historyへの依存を局所診断する。元親/前mask-mixed終端と同TRAIN16/同IDs・mask教師・絶対RoPE位置・logical32/micro8を固定し、BOS2ごとのsame-document causal attentionだけを変えたread-only forwardを比較。元全32CEは再利用、各checkpoint先頭8のみowned control一致確認。CPU準備15秒/GPU全30秒/optimizer・新学習教師0、native forward/境界隔離・未来遮断/元path一致CPUtest/永続runnerを先に用意。未実装・未起動、同学習実験やBase採用ではない。終端conditional平均CE増分>=.1natsかつ増分>=.1のbatch>=12/16の事前局所markerが支持された場合だけ、別の数値条件を両armで揃えたattention-policy学習比較を定義する。未支持なら当packing仮説で新学習せず終了。元strong/absolute/歴史Web保持・旧失敗/Phase0–3/数値7失敗は維持、独立学習seed/full dev/protected test/採用は未達。WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    progress_path=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(progress_path)
    progress.update(status='Base_only_TRAIN_attribution_complete_document_context_ablation_defined',updated_at=now(),
        document_context_ablation_proposal=prior.reference(destination),next_action=proposal['next_action'],Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(progress_path,progress)
    print(json.dumps(dict(status=proposal['status'],completed_conditional_EOS_CE=proposal['evidence']['completed_conditional_EOS_CE'],
        original_conditional_gradient_share=proposal['evidence']['original_conditional_gradient_total_squared_norm_contribution'])))


if __name__=='__main__':main()
