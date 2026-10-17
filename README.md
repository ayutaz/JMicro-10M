# JMicro-10M

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](docs/148_latest_base_and_documentation.md) / [現在の計画145](docs/145_post_rejection_next_plan.md) / [文書一覧](docs/README.md) / [全件カタログ](docs/document_catalog.md)。

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

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

## 現在の作業と次の計画

今回は全ドキュメントの更新です。DEV readerの隔離と全文CPU評価部品は準備済みですが、正式な独立学習・全文評価・最終TESTの接続と実証は残っています。将来の研究再開時は、既存の結果を根拠に新しい比較を最大1件定義します。[計画145](docs/145_post_rejection_next_plan.md)。

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
