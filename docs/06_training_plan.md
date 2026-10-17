# 学習計画

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新RDropは元10B親/fresh AdamW、LR1e-5・WD.1・batch48・seed42・同25M教師。2 stochastic viewsの平均CE＋.5×対称KL、学習時dropout.1で両viewへ勾配。固定recipeは品質不合格で閉鎖済み。全state保存再開の技術合格を品質合格へ置き換えない。独立seed43には親の事前学習を含む全pipelineが必要。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

## 実装済みと未確認

BaseのAdamW、warmup/cosine、WSD stable/decay、stable予算の明示fork、全state保存再開は実装・実学習済み。Assistant本文+EOTを教師とするdocument sampler、`TeacherChatTrainer`、固定教師量SFT、自己生成履歴評価も実装・実GPU実行済み。Chat trainer未実装・Chat学習未実施という旧説明は現在には適用しない。

独立学習seed43・人間blind・正式Base保持・fullDEV/最終suite・封印TEST・正式採用は未確認。CPU factoryや保存再開試験を独立学習・品質証拠にしない。nativeを旧stable+decay専用runnerへ偽装して渡さず、有資格時の接続は実装してから実行する。

当初のDialogue-oriented mid-trainingは未実施。明示再開された限定SFT比較と分けて記録し、正式Base採用・Chat完成後のpipelineを既に実施したことにしない。

## 閉じた比較

| 系列 | 実績と採否 |
|---|---|
| 元Web10B | 学習・保存・評価済み、Base品質未達。元WebUIで維持 |
| Base teacher-decay2B | BPB改善でも一貫性・完結・反復が未達、不採用。[123](123_base_teacher_decay_2b_results.md) |
| 教材汎化133 | 全14セット/3,066判断/NLL7点、不採用。[136](136_chat_generalization_results.md) |
| 意味多様性135 | 全21セット/4,599判断/NLL7点、不採用。[138](138_chat_semantic_diversity_results.md) |
| 低LR139 | 同TRAIN/親/seed/教師量で1e-4対3e-5。全28セット/6,132判断/NLL7点、不採用。[141](141_chat_lr_comparison_results.md) |

最新候補はcontext1024、batch32、accumulation1、BF16/math、compile=false、固定padding、学習seed42、fresh AdamW、登録B1,899,555。実3,646更新・1,899,557教師、25検証更新を本学習へ加算しない。上限33,600 GPU秒、実2,658.673秒。これは閉じた条件で、次実験の推奨LR・開始予算ではない。純入力・教師・padding込みphysical tokens/秒を区別する。

## 再開時の進め方

既存証拠から未回答の仮説を1件選び、変更点・対照・TRAIN/DEV/TEST・教師量・原品質・全評価費用・終了条件を凍結する。環境→trainer/evaluation→保存再開→安定batchを満たしてから実行し、一巡を不採用で終えたら報告・停止。終了済みrun、拒否padding、別LR/seed/予算で救済しない。

全stateにはmodel/optimizer/scheduler/Python・NumPy・Torch・CUDA RNG/sampler position/消費カウンタ・digestを保存する。完了updateでatomic保存し、同凍結条件で連続対再開を確認。通常resumeでsource/data/schedule/budgetを変更しない。長期jobはPID/boot/start、logs、GPU lock、累積台帳を保存する。

約10Mと原品質を維持する。Base復旧は[124](124_base_recovery_plan.md)の合格Baseで通知・停止。Chat/Dialogue/SFT、量子化、20B/50B、公開・有料cloudは別の範囲判断。大型モデル比較の過去案は現行の10M制約を変更しない。

Python3.12.7はすべて`uv run --frozen`。通常WSL extrasは`--extra hub --extra data --extra ml --extra export`、依存変更は`uv add`。[実行環境](07_environment.md)。当初の段階量・速度・Vast.ai案は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)へ保全した。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="更新前の本文契約当時の記録"></a>
