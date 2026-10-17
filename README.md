# JMicro-10M

2026-10-18実行中: [切り分け結果159](docs/159_chat_recovery_diagnosis_results.md)。新規800応答を全件確認しました。同100ケースの総合成立は対照12→現行22/100ですが、二情報の回答や訂正・継続会話は未解決です。「4まで」の目標に沿って、新しい対照SFTと未知入力・実会話の評価へ進めます。学習・最終判定は未完了です。

2026-10-18調査・次計画: [失敗原因と改善計画158](docs/158_chat_quality_investigation_and_next_plan.md)。追加著作TRAIN全2,048件を照合し、固定した提示順・集合時刻だけの訂正・加算だけの計算・32種類の転記対象を確認しました。次は対照モデルの同100ケース評価と、履歴・質問位置・情報数を分ける診断を先行します。新しい生成・学習は未開始、候補は未採用です。

2026-10-17品質診断: 現行Chatを[100ケース・200応答で評価](docs/157_chat_quality_100_results.md)。最終回答の総合成立22/100、簡単な計算0/10、6応答目の記憶・訂正0/20。同じ返答が3回以上続く会話は11/20でした。[全回答CSV](reports/phase7/chat-quality-100-20261017/responses.csv)。今回の固定診断の結果で、一般的な利用全体の精度推定ではありません。

2026-10-17追試: ユーザー報告の「返答が同じ文へ固まる」を7864の実ブラウザー6応答会話で再現しました。入力と履歴は正しく送られており、モデル自身の反復です。短い会話の確認だけでは継続会話の安定性を確認できていませんでした。会話品質は未解決・未採用です。[再現結果](docs/156_answer_curriculum_results.md#後続の実ブラウザー確認同文への固定を再現)。画面は実際のモデル名を表示するよう修正しました。

2026-10-17最終結果: [回答学習の5段階を完了](docs/156_answer_curriculum_results.md)。参考比較・教材点検・少数診断・新対照SFT・全2,628応答と実UI会話まで確認しました。新80問の内容は11→17/80ですが差の95%CIは−3.75〜+17.50ポイント、元会話は18→16/80で、今回の候補は改善未実証・品質不採用です。[候補を試す7864](http://127.0.0.1:7864) / [対照7865](http://127.0.0.1:7865)。返信は既定32トークン、16/32/64選択。以下は各時点の経過です。

2026-10-17 12:16 UTC: 両SFTと全2,628応答の生成が完了し、元Base画面も復帰しました。内容採点は876件まで完了、残り1,752件を確認中です。新80問は対照11→候補17/80ですが、正式品質の改善・採用は未判定です。[候補7864](http://127.0.0.1:7864) / [対照7865](http://127.0.0.1:7865) / [詳細155](docs/155_answer_curriculum_execution_status.md)。

2026-10-17 12:12 UTC: 新しい対照・候補のSFTと保存状態照合、各10応答の実チャット確認を完了しました。[候補Chat7864](http://127.0.0.1:7864) / [対照7865](http://127.0.0.1:7865)。全2,628応答の内容比較は進行中で、正式品質の改善・採用は未判定です。[実行状況155](docs/155_answer_curriculum_execution_status.md)。以下は以前の経過です。

2026-10-17 11:32 UTC: [回答教材SFT155](docs/155_answer_curriculum_execution_status.md)は40技術更新と全state保存再開に合格し、新対照モデルの本学習を開始しました。旧時間枠の不足は[154](docs/154_curriculum_resource_replan.md)に失敗と明示訂正を保存しています。新しい5段階goalはactiveで、候補学習・全2,628内容比較・新UI会話は未完了。以下の「準備中」は以前の経過です。

2026-10-17現在: 新しい[回答学習計画151](docs/151_answer_learning_execution_plan.md)は段階1〜3を完了、改善教材のSFTと未知入力・実会話確認（4/5）は実行準備中です。[診断結果152](docs/152_answer_learning_diagnosis_results.md) / [次比較153](docs/153_answer_curriculum_comparison.md)。32件のTRAIN応答は再現できましたが、未知入力の改善や正式採用はまだ示していません。以下の旧計画149・最初のSFTの記述は各時点の履歴です。

更新: 2026-10-17 JST。文書更新は645b3d09で完了。その後、ユーザーの指示でチャットSFT・動作確認へ方針を変更しました。Baseの事前学習と最初のチャットSFTは終了済みで、現在は学習済みChatを実際に試せます。正式なBase/Chat品質基準は未達です。

**[Chatを試す：http://127.0.0.1:7861](http://127.0.0.1:7861)** — 元10B BaseへRealPersonaChatで3周SFTした10Mモデル。短い返答と履歴を試せます。今回の新たな再学習はなく、既存の学習済みモデルをCPU FP32で利用できるローカル画面です。[操作と実例](docs/43_local_webui.md)。

[次のSFT計画149](docs/149_chat_sft_next_plan.md) / [Baseの残課題145](docs/145_post_rejection_next_plan.md) / [文書一覧](docs/README.md) / [全件カタログ](docs/document_catalog.md)。

約1,000万パラメータで自然な日本語の続きを生成し、その後に短い会話を行うモデルを目指す研究プロジェクトです。モデル・Tokenizer・学習評価基盤をスクラッチで構築しています。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

[RDrop完了記録](reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

| DEV80指標 | 同25M対照 | RDrop候補 | 元絶対条件 |
|---|---:|---:|---:|
| 文法成立 | 44 | 47 | ≥56 |
| 一貫性成立 | 1 | 3 | ≥27 |
| 適切な完結 | 3 | 6 | ≥27 |
| EOS停止 | 11 | 19 | ≥37 |
| 規定反復 | 53 | 49 | ≤18 |

意味の循環や因果・数量の誤りは残っています。EOS/反復flagだけの改善を能力完成とせず、この固定recipeは不採用です。10Mの限界や単独原因が証明されたわけではありません。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。今回のチャット動作確認は、新しいユーザー指示に基づく。

## 現在の作業と次の計画

現在の依頼は[新計画151](docs/151_answer_learning_execution_plan.md)の5までの実行です。参考比較・教材点検・32件の学習診断は完了。公開教材の個別点検と著作した根拠付き対話を組み合わせ、[比較153](docs/153_answer_curriculum_comparison.md)の配合をCPUで計測しています。新しい主SFT、全2,628応答の比較、新UI会話は未実施です。前回149の試行は[結果150](docs/150_chat_natural_sft_results.md)として完了し、改善未実証で閉鎖済みです。

直前のChat実動作確認では、最初のSFTモデルで5会話10応答を確認し、全10応答がEOTで自然停止しました。挨拶・食べ物の好みなどへの返答は成立しますが、名前の記憶や入力の復唱に失敗が残ります。元の正式品質基準を変更したり、短い動作確認を正式採用へ読み替えたりはしていません。[動作確認記録](reports/phase7/chat-demo-20261017/notes.json)。Baseの残課題は[計画145](docs/145_post_rejection_next_plan.md)に保全しています。

## 基盤と履歴

native10,001,152 parameters、13層/hidden256/FFN640/GQA4Q2KV、Tokenizer4096、context1024です。モデル/Tokenizer、WSLでの実学習、全state保存再開、各種評価は実装済みです。

Baseの文書長重み、進行長補助、ScaleGrad、今回RDrop、およびSFT141までの固定比較は不採用です。[総覧125](docs/125_project_retrospective.md)・[実験検索](docs/base_experiment_lookup.md)から原記録をたどれます。

## 保存したモデル

2026-10-09の[Hugging Face研究保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)は、web-10b/staged-10p6b/teacher-decay-2bの当時の3系列です。ダウンロードは手動承認、dataset/samplerは含まず、後続候補の公開ではありません。[保存契約126](docs/126_model_archive.md)。10B/2Bは各系列の学習量で、パラメータ数は10Mです。

## ローカルで試す

元10B Base用の[WebUI](http://127.0.0.1:7860)を使います。[操作43](docs/43_local_webui.md)と[Windows/WSL引継ぎ](docs/windows_handoff.md)を参照してください。Git cloneに重み・大容量dataは含まれません。

## 開発環境

WindowsがGit正本、WSL2/Linux disk/RTX4090が実行環境。Python3.12.7をuvで管理し、全Pythonをuv run --frozenから実行します。欠損時の復元は[引継ぎ](docs/windows_handoff.md)、運用ルールは[AGENTS.md](AGENTS.md)。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="前回のchat比較141"></a>
<a id="成立した基盤と残る課題"></a>
<a id="最新baseの結果"></a>
