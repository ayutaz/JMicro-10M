# 学習計画

更新: 2026-10-14 JST。研究・教材準備・診断・生成評価・学習は停止中。[最新結果141](141_chat_lr_comparison_results.md)、[状態](autonomous_status.md)、[ロードマップ](15_project_roadmap.md)。Base/Chat未完成・未採用。

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
