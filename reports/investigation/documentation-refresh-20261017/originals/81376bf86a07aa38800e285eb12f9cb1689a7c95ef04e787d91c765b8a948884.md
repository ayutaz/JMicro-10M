# 最新Base結果・目標の未達を踏まえた文書更新

2026-10-14 JST。ユーザーは前の「6まで」の目標を解除し、「ここまでの内容を踏まえてドキュメントをすべて最新にしてください、またここからの計画を立ててください」を新しい目標に設定した。今回の範囲は文書・計画・保存検証で、研究や学習の再開ではない。

## 更新する内容

- 最新Baseは[144](144_base_document_balance_results.md)、前回Chatは[141](141_chat_lr_comparison_results.md)と明確にする。両方とも不採用、Base/Chat未完成・未採用。
- 正確100M/17,698更新/全80/全stateと重みの監査を、生成の品質合格と区別する。独立学習・fullDEV・最終TESTが未実施の事実を保つ。
- 元Base TEST20 promptと元Chat TEST20行のCPU解析を区別して記録する。学習/GPU評価に使っていないことをCPU未開封の証拠にしない。
- 前の目標は未達・blockedになった後にユーザーが解除した。今回の文書更新を、前の目標の達成や次の研究cycleの再開と解釈しない。
- 古いUI PID/実行中/次回案を現在の生存・起動許可としない。最後の観測と、実行を必要時に確認する手順を分ける。

## 全文書と原文保全

対象は更新前のGit管理Markdown/RST **626パス**。現行33、日付付き/固定履歴282、既存原文copy311を棚卸しした。347件の内容hash別copyで全更新前bytesを保全。現行33文書を更新し、残る593パスは原文を維持する。追加2文書（145/146）を含む628パスと、今回の原文copy347パスをカタログから追跡する。[全文書カタログ](document_catalog.md)、[今回baseline](../reports/investigation/documentation-followup-20261014/baseline.json)。

現行文書は本文の現在判断を更新する。日付付きの計画・実験結果・固定台帳・科学報告は原文を保全し、古い数値・失敗を現在に合わせて書き換えない。過去の納品receiptはそのGit revisionの証拠で、現在文書のhashへ置き換えない。

## 今後の計画

[計画145](145_post_rejection_next_plan.md)に、評価の読取り分離、次仮説の選定条件、最小診断、同条件pilot、本比較、真にfreshな独立seed、全文DEV、新しい封印TEST・採用を整理した。次の介入・教材・教師量・GPU予算は未凍結。10M・原品質・日本語Base・合格Baseで通知停止の境界を維持する。

再開時は一巡の比較か、定義した比較数と総予算の範囲でBase完成を目指すかを明確にする。不採用の条件を閉じることと、「6まで」の目標を完成したことを混同しない。

## 確認と保存

全更新前パスと原文copyのhash、歴史文書の不変、科学report/config/sourceの不変、現行リンクと見出し、歴史文書から現行文書へのfragment、Windows/WSLの一致、Git保存内容を確認する。[検証結果](../reports/investigation/documentation-followup-20261014/verification.json)。最終納品の実commitとの照合は[commit確認](../reports/investigation/documentation-followup-20261014/commit_verification.json)に記録する。

この文書作業ではdataset/TEST/weightsを解析せず、GPU学習・生成・評価・UI診断/再起動・外部公開/pushを行わない。モデルの品質未達・独立corpus監査・人間blind等の未完了はそのまま残す。

原文copyに元からある末尾空白・改行はhash保全のため修正しない。Git attributesの末尾空白例外は今回のoriginals配下だけで、現行文書のdiff checksは通常のまま。準備helperのtracked-cleanチェックが自身の未追跡Pythonも拾った点と、執筆helperの文字列閉じを修正してから実行した。いずれも文書処理前の修理で、科学recordやdatasetの変更は0。
