# 現在の状態

最終更新: 2026-10-13 JST。**直近の4項目の実験・検証は完了し、不採用として閉鎖。Base/Chatは未完成・未採用、追加研究・学習は停止中。** 最新の依頼は文書と計画の更新のみで、新規教材・診断・生成評価・再採点・学習を再開していない。

[最終結果136](136_chat_generalization_results.md)、[完了監査](../reports/phase7/chat-generalization-20261013/completion.json)、[現行の改善計画135](135_chat_problem_solution_plan.md)を先に読む。計画128/131/133は終了済み実験の事前登録で、現在の開始手順ではない。

## 現在地

| 項目 | 保存証拠が示す状態 |
|---|---|
| モデル | native10,001,152 parameters、context1024、Tokenizer4096。既存9.5M〜10.1M予算を維持 |
| Phase0〜5 | 基盤構築と限定比較を完了。[Phase4](21_phase4_completion.md)、[Phase5](23_phase5_completion.md) |
| Phase6 Base | 元10Bと追加比較は学習・評価済みだが、日本語生成品質と最終採用証拠は未達。[結果123](123_base_teacher_decay_2b_results.md) |
| Phase7 Chat | 限定SFT128、教材比較131、汎化比較133はいずれも不合格で閉鎖。正式Chat採用未達 |
| 最新実学習 | D1 3,641更新・1,899,562 Assistant本文+EOT教師。B=1,899,555を完全応答単位で7超過し登録0〜64内 |
| 対照 | D0は一致する旧C1の3,636更新・1,899,555教師を出典付き再利用。D0新学習0、独立学習seedの証拠ではない |
| 全評価 | 14評価セット・3,066理由付き内容判断・固定NLL7点、保存状態/実教師列/選定/分岐を監査済み |
| 採否 | D0/D1とも不合格、合格候補なし。Base/Chat未採用 |
| 回復・保持・sampling | 回復条件不成立、保持/samplingは候補なしで未実行・品質未確認。閉じた比較の必須残作業ではない |
| padding | 別24GPU確認更新完了。動的条件内の全state再開は一致、固定との差は数値gate不合格で不採用 |
| 最新比較GPU | 2,117.569秒（35.293分）/21,600秒。失敗予測12.108秒も保存。過去全実験の合計ではない |
| 次の実行 | 計画135の教材recipe比較を最大1件として提案中・未実行。別の明示再開と実行前契約が必要 |

## 最新の最終品質

内容は文法・関連性とも2、自己生成文脈は24会話の最終turnで文脈2。新旧は今回の未使用DEVと既存回帰DEVを指す。

| 指標 | D0 新 | D1 新 | D0 旧 | D1 旧 | 元の基準 |
|---|---:|---:|---:|---:|---|
| 内容 /80 | 16 | 12 | 18 | 15 | 新旧それぞれ56以上 |
| 自己生成文脈 /24 | 5 | 3 | 4 | 1 | 新旧それぞれ15以上 |
| 正しい提供履歴の対応文脈 /24 | 6 | 5 | 4 | 2 | 回復分岐は新旧15以上 |
| 固定自然停止 /80 | 79 | 80 | 79 | 79 | 新旧76以上 |
| 自己生成自然停止 /59 | 55 | 59 | 57 | 59 | 新旧57以上 |

[最終比較](../reports/phase7/chat-generalization-20261013/selection.json)が採否の正本。D1は停止・反復の機械gateを通るが、内容と文脈が不足する。最終新の文法2は62/80、そのうち50件は関連性2未満。内容のD1−D0差は新−5.0ポイント、95%CI −15.0〜+6.25で、改善は実証されない。CIが0を含むため、一般的な悪化の統計的確定も主張しない。

D1固定TRAIN112target本文NLLは親3.148497→最終0.001136、新DEV80は3.058625→4.818918、RPC DEV本文BPBは1.351262→1.943257。[全保存点解析](../reports/phase7/chat-generalization-20261013/final_analysis.json)。教材適合と未知入力への汎化が離れていることは確認できる。意味構造・分布差・過適合は仮説で、全TRAIN暗記、Base単独原因、10M容量限界は未確定。RPCのChat形式BPBは正式Base保持を代用しない。

## 完了した検証と未確認の品質

[実行履歴134](134_chat_generalization_execution.md)は各時点の観察、[結果136](136_chat_generalization_results.md)とcompletionが最終状態。保存/再開・実教師消費・全stateの技術監査と20件のCPU gate確認は通過したが、モデルの完成を証明するものではない。各回答はCodex非blindによる判断で、独立人間確認ではない。280sampleの教材QAを全TRAINの意味品質認証へ読み替えない。

独立学習seed43、人間blind、全文DEV、全400生成＋長文40、最終継続suite、選定封印後のprotectedTEST、Base/Chat正式採用は未確認。独立全corpus監査や過去の数値7失敗も未解消のまま保持する。保存点や同一会話のturnを独立標本に水増ししない。

## process・UIと保全

最新の科学completionは2026-10-12T20:32:10Z（JST翌日05:32）に、対象jobの終端・実process終了・GPU台帳と元10B UIを確認した。UI観測identityはPID235826、boot `4052bfc5-3850-44e4-9123-d34a9e19f36e`、start_ticks47993707。親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、Tokenizer一致、busy=false。**これは当時の生存証拠で、今回の文書更新で現在の稼働を再確認したものではない。**

元[WebUI](http://127.0.0.1:7860)は差し替えず保持する。終了済みの学習・最終評価・paddingを再起動しない。現在の実process/lock/HTTP確認が必要になるのは、明示的な実行再開やUI操作時。[引継ぎ](windows_handoff.md)にパスと確認順を記載した。

D1最終checkpointはWSL `reports/phase7/chat-generalization-20261013/D1/checkpoint-00003641.pt`、SHA `aa84a1dc3fbbf1c264ebd9327ecc7183bf3d88c606e01bd0f82bb5351945aed6`。重み・教材実体・全stateをWSLに保全し、Gitには実装/config/評価metadata/理由付き判断を保存する。[354fileの保存一覧](../reports/phase7/chat-generalization-20261013/final_archive.json)、[保存確認](../reports/phase7/chat-generalization-20261013/final_delivery_checks.json)。結果保存commitは `ed3aa29`。今回の文書更新commitは `git log -1` で確認できる。自動pushなし。

## 既存系列と公開履歴

最新Base teacher-decay2BはBPB1.106386→1.090316に対し一貫性3→3、適切完結7→5、反復27→27、Unicode0→1（各80）で不採用。[Base完了](../reports/phase6/base_teacher_decay_2b_completion.json)。元UI10B・別staged約10.6B・teacher-decay2B・後続SFTを同じ重みや同じ学習量として扱わない。

2026-10-09の[研究モデル保存版126](126_model_archive.md)は主要3系列のpublic/manual gated公開の保存記録。データセットとsamplerは除外し、元checkpointの厳密再開代替ではない。後続Chat重みの公開は行っていない。[公開report](../reports/publication/model_archive_20261009.json)。当時のGitHub push許可はその納品に限る。[全体記録125](125_project_retrospective.md)、[固定revisionの詳細台帳](retrospective/README.md)。

更新前の文面は[今回の履歴保存](../reports/investigation/documentation_plan_refresh_20261013/baseline.json)と[以前の状態履歴](autonomous_status_history_20261008.md)へ保持した。原raw・採点・失敗・凍結source/configを変更しない。
