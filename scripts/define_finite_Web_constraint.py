"""Define one finite functional constraint study from retained Base failures.

This is an owned nonlinear finite-loss extension, not an implementation or
performance guarantee of GEM/TRPO. No new model/source/rank sweep is allowed.
"""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import sys
from pathlib import Path
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now
from jmicro.training import atomic_json
from record_source_gradient_attribution import original_UI
import run_low_rank_base_comparison as previous


def main():
    path=ROOT/'reports/phase6/finite_Web_constraint_proposal.json'
    if path.exists():raise ValueError('Preserve original finite-loss proposal')
    c=previous.inspect(previous.CONFIG);done=read_json(ROOT/'reports/phase6/low_rank_base_v2_completion.json')
    if done['eligible_recipes'] or done['Base_complete']:raise ValueError('Actual unqualified Base comparison required')
    samples_config=read_json(ROOT/'configs/phase6/source_gradient_attribution.json')
    refs={
        'trigger':previous.reference(ROOT/'reports/phase6/low_rank_base_v2_completion.json'),
        'finite_nonlinarity':previous.reference(ROOT/'reports/phase6/finite_parameter_displacement_completion.json'),
        'shared_prefix_forgetting':previous.reference(ROOT/'reports/phase6/shared_prefix_web_loss_completion.json'),
        'soft_parameter_anchor_failure':previous.reference(ROOT/'reports/phase6/parameter_displacement_anchor_completion.json'),
        'original_masked_staged_control':previous.reference(ROOT/'reports/phase6/conditional-prefix-mask-20261006/compare-result.json'),
        'original_masked_staged_review':previous.reference(ROOT/'reports/phase6/conditional-prefix-mask-20261006/review.json'),
        'original_masked_staged_notes':previous.reference(ROOT/'reports/phase6/conditional-prefix-mask-20261006/content-notes.json'),
        'accepted_input_ledger':c['references']['reference_input_ledger'],
        'cached_TRAIN_packet':samples_config['references']['samples'],
        'cached_TRAIN_metadata':samples_config['references']['samples_metadata'],
        'cached_TRAIN_config':previous.reference(ROOT/'configs/phase6/source_gradient_attribution.json'),
    }
    # Fixed filenames are confirmed before use; no source/CP search based on
    # prospective quality is performed.
    for ref in refs.values():previous.check_reference(ref)
    ui=original_UI()
    proposal=dict(kind='finite_original_Web_TRAIN_body_NLL_constraint_projection_v1',created_at=now(),references=refs,
        primary_source='https://arxiv.org/abs/1706.08840',
        attribution='GEM formulates memory losses as inequality constraints and locally approximates them with gradient constraints. Our direct finite-loss oracle/Newton correction is a separate owned extension, not a claimed GEM reproduction or proven generalization guarantee.',
        measured_trigger=dict(rank4_vs_full_coherence=[3,10],rank4_vs_full_EOS=[13,23],rank4_vs_full_repetition=[64,37],
            nonlinear_displacement_fraction=[.9458055121206235,.9891869268641028],
            shared_prefix_Web_BPB=1.0136221079473724,original_guard_Web_BPB=.9715702494156145,
            masked_staged_Web_BPB=1.0868123573684936,masked_staged_coherence=35,masked_staged_EOS=79,masked_staged_repetition=1),
        hypothesis='Preserve the actual TRAIN Web prediction function while applying full-capacity staged outcome learning. A soft parameter penalty/frozen low-rank backbone did not enforce that constraint. Fixed small-memory fit is not held-out Web retention or natural quality.',
        parent=c['parent'],native_parameters=10001152,learning_order='Original full Web75M, story5M, ordinary10M, conditional10M reference staging',
        source_masks_inputs_quotas_unchanged=True,target_rule='Existing conditional outcome body+EOS only, other3 sources unchanged',
        CE_teacher_tokens=91641755,reference_teacher_tokens=100000000,physical_input_tokens=100532224,updates=3068,
        optimizer_policy='Original parent model/Adam/RNG/scheduler clock and permanent floor; actualLR0.00001. Projection is applied outside Adam; original moment proposal retained only for accepted completed updates.',
        comparison='Reuse the completed whole masked-staged recipe as historical uncontrolled functional-constraint reference. New complete candidate starts at original10.5B parent, not its already-forgetting90M prefix.',
        memory_selection='First32 Web rows in existing frozen16 TRAIN batches, in stored batch/row order. They are exact initial Web-stream windows already present in original staged75M control. No resampling, filtering, dev/test use or whole-source scan.',
        memory=dict(rows=32,context=1024,microbatch=8,dtype='fp32',backend='math',loss='Original body IDs>=8 only; exclude EOS/BOS/structural/ignored targets',
            reference='Original10.5B parent on exactly same bytes/teachers',ceiling_multiplier=1.01,projection_interior_margin_relative=1e-5),
        algorithm=[
            'Snapshot unique native weights, optimizer, RNG and sampler before one completed-update proposal; tied embedding/output counted once.',
            'Compute unchanged masked source CE and clipped AdamW proposal at actualLR0.00001.',
            'Measure actual FP32/math body NLL on fixed TRAIN memory. Accept immediately if <= original reference*1.01.',
            'If violated, compute ONE memory body gradient at the proposed weights. Correct along minus-gradient by (actualNLL-ceiling+reference*1e-5)/squared_gradient_norm. This additional supervised gradient is separately counted.',
            'Measure actual corrected finite NLL; if still violated, test only prescribed0.5/0.25/0.125 of this SINGLE-update corrected displacement from the last safe weights. No endpoint/checkpoint averaging or quality-selected LR sweep.',
            'Accept first finite feasible proposal, preserving original Adam/scheduler semantics and source/auxiliary accounting. If none is feasible or gradient nonfinite/zero: restore ALL last-completed states and terminate rejected branch; do not count an unaccepted source update or advance its sampler.',
        ],
        teacher_accounting='91,641,755 ordinary source-CE teachers if completed; separately count memory projection-gradient targets, finite-loss target observations, rejected-proposal source/auxiliary exposure and all physical input. Total gradient teachers may exceed CE budget. Never claim matched total supervision or equal GPU budget to cached control.',
        CPU_preparation_ceiling_seconds=60,probe_GPU_ceiling_seconds=120,total_new_GPU_ceiling_seconds=2400,
        required_before_science=['Implement trainer/fullstate persistence and native evaluator connections',
            'CPU tests for exact finite bound/projection/backtrack, unique tied weights and rejected all-state/cursor/RNG rollback, continuous/resumed actual model states',
            'Own actualCUDA8vs4+4 fullstate/finite/no-reheat and32timings; discarded probe weights/teachers separately counted',
            'Own actual FP32 oracle/projection gradient control on a preselected stored violating state; no generation/adoption of that diagnostic corrected state',
            'Freeze science only if measured worst-case3068*(source_step+5_oracle_forwards+1_memory_gradient)+saving,1.3margin+200eval reserve plus probe fit2400s'],
        completion='Actual accepted3068 source updates with whole91,641,755 CE teachers plus separately measured auxiliary teachers, or explicit finite rejection/rollback/budget branch. Only completed candidate gets unchanged dev256/Japanese192/331/1119/greedy80 and all80 raw-bound individual review. Terminal actual PID, original UI restoration, portable evidence and local commit.',
        quality_criteria_unchanged=True,protected_test_used=False,
        selection='Original strong full-staged coherence23+8 with pairedCI lower>0, EOS>=76/repetition<=2; absolute grammar56/coh27/appropriate27/EOS37/repetition<=18/errors0; original held-out WebBPB<=.9812859519097707. Only a qualified recipe permits independent learned seed/full dev/protected test/adoption.',
        failure_policy='End this sole functional constraint recipe; no memory/ceiling/margin/projector/LR/source/mask/order/CP/decoder salvage sweep or automatic training extension.',
        limitations=['Small fixed TRAIN memory can overfit and cannot guarantee held-out retention',
            'Projected gradient adds repeated TRAIN feedback/supervision; report its cost and do not attribute solely to clipping',
            'The completed one-seed nonblind Base failures do not prove a universal10M/LoRA capacity limit',
            'First-order memory prediction alone is not the finite acceptance oracle',
            'No natural quality or final adoption evidence exists for this new recipe'],
        GPU_seconds_so_far=0,new_CE_teacher_tokens_so_far=0,new_memory_projection_teacher_tokens_so_far=0,
        implemented=False,launched=False,original_UI=ui,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    atomic_json(path,proposal)
    prefix=f'''次のBase専用有限比較を定義: 実測Web TRAIN body NLLの制約（2026-10-06 JST）。未実装・未起動、newGPU/学習0、Base未完成・完成時通知停止、Chat/Dialogue/SFT/量子化なし。

rank4対full fresh Adamは全160/採否/終端/UI/224file可搬SHAをcb3c114へ保存し、両不採用。一貫性3対10、EOS13対23、反復64対37、BPB.972906対.973113。当比較598.744819GPU秒。rank4/LR/CP等の救済総当たりは行わない。前の有限変位診断ではWeb CE増分の94.6–98.9%が一次近似の外にあり、soft L2もWeb保持に失敗、stagedはprefix90M時点でBPB1.013622>.981286。次は関数の実損失を制約し、能力を落とす一律低ランク制限と区別する。[GEM一次資料](https://arxiv.org/abs/1706.08840)の記憶損失の不等式制約を参考にしたowned nonlinear extensionで、論文再現/成功保証ではない。

元10.5B親/model/Adam/RNG/scheduler/floor/actualLR.00001から、同Web75/story5/ordinary10/conditional10M referenceをstagedで始める。既conditional outcome+EOS mask/他source不変、完了時91,641,755 CE教師/100M reference/3068更新。旧masked-stage whole recipeのcoh35/EOS79/rep1/BPB1.086812を再利用。既固定TRAIN16から最初32 Web窓（元staged75Mにも含まれる）のbody-only FP32/math CEをoriginal基準の1.01以内に保つ。Adam提案後の有限値が超えた場合のみ、一回のWeb gradientによるNLL超過修正→実NLL確認→同一更新の0.5/.25/.125 backtrack。全不成立なら重み/Adam/RNG/samplerを直前完了状態へ戻して研究分岐終了、未受入教師を完了量へ足さない。追加Web gradient教師・forward観測・拒否試行・GPUを別会計し、旧対照と総教師量やGPUが同じとは称さない。固定TRAIN保持はheld-out Web保持や自然品質の証拠ではない。

先にCPUの厳密constraint/rollback/fullstate testsと永続runnerを実装。CPU60/ownCUDA8対4+4・32timing/projection数値control120秒、実測最悪3068*(source step+5 memoryforward+1 memorygradient)/保存×1.3+評価200秒とprobeが全2400秒内の場合だけscienceを凍結。完了candidateは同dev256/common bytes/Japanese/固定80を全内容判定、または明示数値/受入不能/予算の失敗分岐。強い旧相対/絶対/歴史Webの全gate不変、memory/bound/margin/LR等の救済sweepなし。独立学習seed/full dev/protected test/採用は未達。Phase0–3/数値7/旧全失敗保持、WSL uv3.12.7/local commitのみ/pushなし。以下は過去の履歴。

'''
    for relative in ('docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        p=ROOT/relative;p.write_text(prefix+p.read_text(encoding='utf-8-sig'),encoding='utf-8')
    p=ROOT/'reports/phase6/five_step_progress.json';progress=read_json(p)
    progress.update(status='finite_Web_constraint_defined_unimplemented_unstarted',updated_at=now(),
        next_action='Implement strict finite TRAIN Web body-NLL proposal/projection and all-state rejected-update rollback; own CPU/CUDA worst-case measured budget before any science.',
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False)
    progress['finite_Web_constraint_proposal']=previous.reference(path);atomic_json(p,progress)
    print('Defined one finite Web function constraint; no new GPU/training.')


if __name__=='__main__':main()
