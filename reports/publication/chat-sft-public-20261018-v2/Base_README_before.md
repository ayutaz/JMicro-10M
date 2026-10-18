---
language:
- ja
pipeline_tag: text-generation
library_name: pytorch
tags:
- jmicro
- research
- experimental
- gated
inference: false
---
# JMicro-10M 研究モデル保存版

約1,000万パラメータの日本語Baseモデルをスクラッチ学習した研究の保存版です。
今後、改善案を思いついたときに重み・実装・設定・評価・失敗理由を確認するために残しています。
**Baseの品質目標は未達です。完成した会話モデルではありません。学習は停止中です。**

リポジトリはpublic、ファイルへのアクセス申請はmanual（手動承認）です。
承認はモデルの品質保証や利用・再配布ライセンスの自動付与を意味しません。

## 保存したモデル

すべて10,001,152 parameters、語彙4096、context1024の同じnative構成です。
10Mはモデルの重みの数で、10B/2Bは各系列の学習量です。別系列の学習量を合算しません。

| フォルダ | 何を残したか | 注意点 |
|---|---|---|
| `models/web-10b` | 元のローカルWebUIで使用した10B入力tokensモデル | 反復・一貫性・停止に課題あり |
| `models/staged-10p6b` | 約10.6B入力tokensのsource-order研究系列 | 一貫性23/80、適切完結26/80。採用基準未達 |
| `models/teacher-decay-2b` | 最後の教師量正規化weight decay、正確に2B教師 | BPB改善でも一貫性3/80。固定条件は不採用 |

各フォルダにnative `model.safetensors`、`jmicro_config.json`、`training_state.pt`、
出所・元checkpoint SHA256・正確な学習量を記録した`provenance.json`があります。
training_stateはoptimizer・scheduler・RNG等の学習状態です。samplerとデータは除いています。
モデル重みは元checkpointから無損失で保存し、CPU再読込・全重み一致・forward一致を確認しています。
HF Transformers形式への変換・量子化・追加学習は今回行っていません。

## 調査と試行錯誤を読む

- [全体記録](project/docs/125_project_retrospective.md): データ、Tokenizer、WSL、学習高速化、EOS、反復、日本語評価、目的関数、構成、最新不採用まで。
- [最新の状態](project/docs/autonomous_status.md)、[最新比較](project/docs/123_base_teacher_decay_2b_results.md)。
- [将来の再開計画](project/docs/124_base_recovery_plan.md)、[文書一覧](project/docs/README.md)。
- [実験値の機械可読記録](project/docs/retrospective/experiment_records.json): 保存済み4,815 JSON報告の原キー・指標・採否・SHA256。記録数は独立実験数ではありません。
- [評価の要約](research/evaluation_summary.json)、[不採用判断](research/decision.json)。
- `project/src`、`project/scripts`、`project/configs`、`project/schemas`、`project/uv.lock`: 当時の実装と固定環境。

原文書中のreports/data/artifactsへのリンクとローカル絶対pathは元研究環境の参照です。
この保存版はraw報告・生成全件・全実験のcheckpoint・データセットを複製するものではありません。
過去文書の「実行中」「次は」は当時の記録であり、現在の開始指示ではありません。

## ローカルでモデルを読み込む

手動承認後、Hugging Faceのローカル認証を設定し、Pythonはuvから実行してください。
まず`huggingface_hub.snapshot_download("japanese-data-analyze/JMicro-10M-research-archive")`で
このリポジトリを取得します。認証tokenはコードへ直接書かないでください。
取得したフォルダの`project`へ移動し、固定環境を復元します。

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
uv run --frozen --extra hub --extra data --extra ml --extra export ../inspect_model.py --model staged-10p6b
```

`inspect_model.py`はCPUでモデルとTokenizerを読み込み、短い入力のforwardを確認します。
native `jmicro.model.JMicroModel.load`と`jmicro.tokenizer.Tokenizer`を使用してください。
generic AutoTokenizerやraw SentencePieceだけではprotected-byte契約を再現できません。

## 保存範囲と未達

データセット・shard・tokenized stream・sampler内の文書は含めていません。
新しい教材での学習や重みの調査は可能ですが、元と厳密に同じ地点から再開するには
元データ、sampler状態、実行環境の復元が必要です。`training_state.pt`はその完全な代替ではありません。
最終採用Base、独立学習seed確認、最新候補の全文DEV/protectedTEST、Chat、最終量子化は未完了です。
繰り返し確認したDEVとCodexの非blind評価を、独立人間評価とは扱いません。

モデル・Tokenizerに一括した新しいライセンスを付与していません。
教材の出所・条件は保存した文書と設定へ残しています。FineWeb2 Edu Japanese/
FineWeb2/Common Crawl、物語・textbook等の出所を保持し、データのライセンスをモデルの
権利全般の保証として扱いません。既公開pilot/Tokenizer bundleと今回のモデル保存版は別です。

全公開ファイルのサイズとSHA256は`archive_manifest.json`と`SHA256SUMS`に記録しています。
