# Windows / WSL 引継ぎ

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

## 最新の保存と最後の実行観測

RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。

最新RDrop checkpointはWSL reports/phase6/rdrop-science-20261016/checkpoint-00004420.pt、SHA256 e9154a2d5b8e385c978e597c8b65d3c73dc882680bbf143422d9acb363aa0c73。全model/Adam/RNG/sampler/counters/metricsを保全。元UIはこの候補でなく元10B親を使用する。

## 正本と保存場所

| 対象 | 場所・固定情報 |
|---|---|
| Git正本 | C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m。最新HEADはgit logで確認 |
| 実行コピー | /home/aihub_ubuntu/src/japanese-tiny-llm-10m |
| データ | /home/aihub_ubuntu/jmicro-data。重み・data・samplerはGit外 |
| Python | uv固定3.12.7、既存WSL2/Linux disk/RTX4090。package/driver情報は観測値 |
| Tokenizer | artifacts/phase2/4096/tokenizer.model、SHA a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318 |
| 元UI親 | reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt、SHA 410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290 |
| native model | 10,001,152 parameters、src/jmicro/model.py SHA298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83 |
| 最新portable証拠 | reports/phase6/rdrop-science-20261016/portable_artifacts.json。全stateの代用ではない |

## 復元と操作

既存環境では[WebUI操作43](43_local_webui.md)。操作時にserver記録と実PID/boot/start/HTTP/kernel lockを照合し、重複起動しない。元UIが停止している場合だけscripts/start_webui.ps1を使う。今回の文書作業では再起動しない。

欠損時だけ[Hub引継ぎ](huggingface_handoff.md)・[保存126](126_model_archive.md)のpinned取得/uv frozen復元を行う。公開保存にsampler/dataがないことを確認し、元checkpointの厳密再開を装わない。過去のChatとBase各系列も原pathのまま保全する。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="6-実装済みcliと次回の再開"></a>
<a id="git外で保全する重みと教材"></a>
<a id="前回chatと旧baseのgit外保全"></a>
<a id="前回chatの閉じたrunと当時のui"></a>
<a id="新pc欠損時だけ行う復元"></a>
<a id="明示的な実行再開後の順序"></a>
<a id="最新baseと最後の観測"></a>
<a id="閉じた最新runとui"></a>
