# Baseの実験結果を探す

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

## 最新までの入口

| 比較・部品 | 原記録 | 判断 |
|---|---|---|
| 第一回RDrop25M | [completion](../reports/phase6/rdrop-science-20261016/completion.json)・[review](../reports/phase6/rdrop-science-20261016/review.json) | 全80/全4,420履歴、不採用 |
| ScaleGrad25M | [completion](../reports/phase6/scalegrad-science-20261015/completion.json) | 文法/反復は改善、一貫性/適切完結/BPB等未達 |
| 進行長補助25M | [completion](../reports/phase6/document-progress-science-20261015/completion.json) | paired対照/候補、内容改善なし |
| 全文DEV部品 | [CPU completion](../reports/phase6/isolated-full-dev-preparation-20261015/completion.json) | 合成36 checks、実全文/440内容は未実行 |
| 上限解除前の選定監査 | [decision](../reports/phase6/post-scalegrad-selection-20261015/decision.json)・[primary fit](../reports/phase6/post-scalegrad-selection-20261015/primary_fit_review.json) | 当時の資源/根拠判断。NEFTuneは未選定 |
| 文書長重み100M | [144](144_base_document_balance_results.md) | 不採用 |
| 限定SFT低LR | [141](141_chat_lr_comparison_results.md) | 不採用 |

9層256/FFN1040、6層384/FFN832の構成配分はconfigs/phase6/architecture_comparison.jsonとreports/phase6/architecture_comparison_review.jsonに300M比較が存在する。以下の固定索引の検索語がないことは、未検証の証明ではない。proposal/trainer/結果を対応付ける。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

現在の実状態は `autonomous_status.md` の先頭と、対象jobの実PID/boot/startを確認する。旧計画の「次は…」を、新しい実行指示と解釈しない。

過去の条件を再提案する前に、WSL native repoで `uv run --frozen --extra hub --extra data --extra ml --extra export scripts/index_base_experiments.py --query キーワード` を実行する。例: `larger_material`、`initialization`、`wikipedia`。日時付き索引 `reports/phase6/base_experiment_index_20261008.json` は小さいproposal/completion/review/active_job報告のパス、原SHA、status、閉鎖等のフラグ、要約だけを保存する。

索引は観測時点の検索補助。報告に欠ける量やstatusは推測せず、rawや1MiBを超える報告・全corpus・重みは読み込まない。省略対象はskippedへ列挙する。実行判断時には原報告を参照し、更新済みファイルや稼働中processを再確認する。採点、品質条件、過去の不採用を変更しない。

2026-10-08の参照例: `larger_material_v3_completion.json` はWeb95/story5の500M対2B準備が固定64中11弱>上限10で不採用。`base_gradient_accumulation_pilot_completion.json` は同94.16M教師の勾配蓄積比較が不採用。その後の初期化比較とteacher-decay比較も終了した。最新は結果123の累積2B teacher-decay不採用・一時停止で、次回計画は124。古い索引を最新結果の網羅的な証拠と扱わない。

生成済み索引は同名で上書きしない。新たな結果を集約する場合は日時の異なる後続索引を作り、原報告を保存する。Baseの品質・独立学習seed・fullDEV・protectedTEST・採用が揃うまで未完成。Chat/SFT/量子化はユーザーが再開するまで進めない。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="当時の資料保存手順"></a>
