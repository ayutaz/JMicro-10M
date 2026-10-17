# 研究モデルのHugging Face保存

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

2026-10-09の主要3Base系列・Tokenizer・数値学習状態の保存契約1544 files/396038805 bytes/revision853d52d2323653331b610249912fbe25615615fcは歴史記録。dataset/sampler除外。後続Chat/ScaleGrad/RDropはこの保存に含まれない。今回はHub照会・変更・公開を行っていない。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

## 保存する3系列

すべて10,001,152 parameters、Tokenizer4096、context1024のnativeモデル。同じモデル規模でも、学習履歴と品質は異なる。

| フォルダ | 正確な学習量 | 選んだ理由 |
|---|---|---|
| `models/web-10b` | 入力10,000,007,168 / 教師9,978,838,479 tokens | 元のローカルWebUIで利用した基準モデル |
| `models/staged-10p6b` | 入力10,600,546,304 / 教師10,577,786,961 tokens | source-order系列。一貫性23/80・適切完結26/80の比較的良かった研究条件 |
| `models/teacher-decay-2b` | 正確に2,000,000,000教師 / CE入力2,053,285,089 tokens | 最後の教師量正規化weight decay比較。不採用の条件も保存 |

元checkpoint SHA256:

- web-10b: `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`
- staged-10p6b: `fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae`
- teacher-decay-2b: `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442`

stagedはhistorical-parent対照の`6d901b...`ではなく、source-order候補の`fb43f2...`。元10B、最新2Bとも区別する。採用済みBaseは存在せず、これらは未達・不採用を含む研究モデルである。

## 含めるものと含めないもの

各モデルにnative `model.safetensors`、`jmicro_config.json`、`training_state.pt`、`provenance.json`を保存する。Tokenizerは全モデル共通で、公開版4kのSHA256 `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`を保持する。HF Transformers形式への変換、量子化、追加学習は行わない。

`training_state.pt`はoptimizer・scheduler・RNG・学習量等の数値状態を明示的なキー一覧から取り出したもの。samplerにはデータ読み込み途中のtoken列等が含まれ得るため、samplerと元checkpointそのものはアップロードしない。元checkpointはWSLに保持し、公開版にそのSHA256と元pathを記録する。

学習データセット、processed corpus、shard、tokenized stream、raw source archive、全実験の中間checkpoint、認証情報は含めない。原データとsamplerがないため、この保存版だけで元の厳密な中断再開はできない。重みの確認と新しい教材による将来の実験の出発点には利用できる。

調査・試行錯誤を参照するため、当時の`src/scripts/configs/schemas`、uv固定環境、原文書と[公開保存版の全体記録125](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive/blob/main/project/docs/125_project_retrospective.md)、保存済み4,815 JSON報告の指標・採否・原SHA256を含む機械可読の記録も保存する。Gitの全履歴・全raw reportを複製するものではなく、文書内の原reports/data絶対pathやリンクは元環境への参照として残る。機械可読記録の数を独立実験数とせず、重複したGPU時間や教師量を合算しない。

学習停止と今回の記録保存の関係も区別する。以前のREADME整理・GitHub push依頼は一度途中で停止され、Hugging Face保存時点では未完了だった。その後の「すべてpushして」という明示依頼で文書とGitHub保存を再開した。Hugging Faceのモデル公開とGitHubの文書保存は別の成果物として確認する。

## 確認方法

作成スクリプトは[scripts/archive_hub_models.py](../scripts/archive_hub_models.py)。WSLのCPUで元checkpointの記録済みSHA256、parameter数、保存後の全重みの完全一致、有限かつ一致するforward、Tokenizerの保護byteを含むroundtripを確認する。新しいGPU品質評価や再採点はしない。

公開は空のprivate repoへmanual gateを設定してからアップロードし、全ファイルのサイズとリモートのSHA256またはGit blob SHA1がローカルと一致した後にpublicへ変更する。匿名APIでも`private=false` / `gated=manual`を確認し、匿名での重み取得が401または403となることを確認する。

公開版の`archive_manifest.json`と`SHA256SUMS`にファイルごとのhashを保存。publication reportにはHub revision、設定、全ファイルの照合結果、元checkpointと学習量を保存する。承認方式は[Hugging Face公式説明](https://huggingface.co/docs/hub/models-gated)、APIは[HfApi.update_repo_settings](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.update_repo_settings)を参照。

## 将来確認するとき

手動承認後、プロジェクトのuv環境から取得する。認証済みの所有者はそのまま取得できる。

```sh
uv run --frozen --extra hub hf download japanese-data-analyze/JMicro-10M-research-archive --local-dir artifacts/research-archive
```

取得先の`project`で固定環境を復元し、付属の確認コマンドを実行する:

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
uv run --frozen --extra hub --extra data --extra ml --extra export ../inspect_model.py --model staged-10p6b
```

モデルは`jmicro.model.JMicroModel.load`、Tokenizerは`jmicro.tokenizer.Tokenizer`を使用する。汎用AutoTokenizerだけではprotected-byte契約を再現できない。保存版には新たな一括ライセンスを付与していない。アクセス承認と、モデルや元教材の権利・再配布条件は別に扱う。

元の重み・学習データ・履歴の所在は[Windows/WSL引継ぎ](windows_handoff.md)、今後の改善条件は[計画124](124_base_recovery_plan.md)。現在の停止境界と10M維持、日本語Base品質の未達、Chat/量子化の未開始を変更しない。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="当時の資料保存手順"></a>
