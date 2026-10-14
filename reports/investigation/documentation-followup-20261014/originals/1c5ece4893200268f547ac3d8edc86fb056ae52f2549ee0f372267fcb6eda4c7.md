# 現在のチェックリスト

更新: 2026-10-14 JST。[最新結果141](141_chat_lr_comparison_results.md)、[状態](autonomous_status.md)、[ロードマップ](15_project_roadmap.md)を正とする。研究・学習は停止中。現在の依頼は[全ドキュメント更新142](142_documentation_refresh.md)。チェック印は証拠への案内で品質合格を意味しない。

## 固定方針

native10,001,152 parameters、9.5M〜10.1M、日本語Baseの原品質を維持。Base/Chat未完成・未採用。大型化・領域縮小・閾値変更で完成扱いにしない。Base単独原因・10M容量限界は未確定。

## 最新の閉じた比較139

- [x] 既存証拠からLR1件を選定し、同親/TRAIN/Tokenizer/seed/教師量/schedule/paddingで凍結。
- [x] 新DEVと既知3回帰、共通2,634 targetのNLLを分離。Chat TEST準備解析事故の原版/修正を保存。
- [x] 実CUDA25検証更新と時間gate、3,646更新/1,899,557教師の実学習、全3state/実入力・教師列を監査。
- [x] 全28セット/6,132判断/NLL7点、最終全原gate/paired CI/反復退行を判定。不合格・不採用。
- [x] 正式保持/sampling/独立seed43/人間blind/fullDEV/封印TEST/採用の7分岐を候補なしで未実行・品質未確認と記録。
- [x] 科学監査、結果141、小report保存と360ファイル/ローカル結果commit89275a8・納品commit09f338eの照合を完了。

## 正式完成に未確認の証拠

- [ ] 原品質と全保持条件を満たすrecipeの選定。
- [ ] fresh学習seed43と独立人間blind。生成乱数やCPU準備で代用しない。
- [ ] 独立corpus監査、正式保持、有資格sampling、全文DEV・全400生成＋長文40・最終継続suite。
- [ ] 選定封印後のTEST・正式採用・再現/復旧。Chatは新たな未使用封印TESTが必要。
- [ ] 採用floatモデルの量子化品質・実容量・独立環境での利用。

## 次の実行境界

全ドキュメント更新の検証・ローカル保存を終えて通知する。追加教材・旧run・再採点・GPU・別LR/seed/budgetを開始しない。Base復旧は[124](124_base_recovery_plan.md)の未再開の別経路で、合格Baseで通知・停止。新介入は既存証拠から1件の別契約が必要。

過去133/135のチェック全文と運用文書は[更新前baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)と[全文書カタログ](document_catalog.md)へ保全した。
