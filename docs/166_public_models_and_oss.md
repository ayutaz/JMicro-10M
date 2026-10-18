# 公開モデルとOSSコードの保存先

2026-10-18。Hugging FaceのBase 3系列と最新SFT研究モデルを、アクセス申請・ログイン不要で公開した。GitHubのコードはApache-2.0で公開した。学習済みの重み・Tokenizerには、今回新しい一括ライセンスを付与していない。

| 公開先 | 内容 |
|---|---|
| [Base研究保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive) | web-10b / staged-10p6b / teacher-decay-2b。以前のmanual gateを解除 |
| [最新SFT研究モデル](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018) | 二情報回答の診断で得た最終重み、Tokenizer、native実装、CPU読み込みコード、評価結果 |
| [GitHub](https://github.com/ayutaz/japanese-tiny-llm-10m) | ソースコード・学習条件・結果・研究記録。READMEから入手・実行手順を確認できる |

最新SFTは64教材の全文再現を達成したが、質問構造の変更15/32、実会話最終9/16、固定100ケースのタスク成立3/100だった。[全結果165](165_chat_two_attribute_diagnosis_results.md)の不採用判断を保持している。公開は品質採用や学習の再開を意味しない。

## 保存と検証

最新SFTのcheckpoint SHA256は`44128809acccf45fbfddcd8863a72af5a029d43a660e10b06ed73e4157aff553`。safetensorsへ無損失保存し、全state tensorの一致とCPU forwardの完全一致、専用Tokenizerのroundtrip、CPUでの生成を確認した。モデルのstateには共有embedding/outputの二つの名前があり、120 state entriesと119 unique parameter tensorsを区別して記録している。

公開した128ファイルは計41,732,706 bytes。HubのファイルサイズとLFS SHA256またはGit blob SHA1を全て照合した。最新SFTの全128ファイルとBase 3系列の重みは匿名でダウンロードし、SHA256との一致を確認した。ダウンロードしたSFTの読み込みコードをCPUで実行し、JSON本文とEOT停止を確認した。

元のcheckpoint pickle、optimizer、RNG、sampler、学習データセットは追加公開していない。元Base保存版に以前から含まれる数値学習状態は保持している。新学習・GPU実行は0。

検証記録は[publication reports](../reports/publication/chat-sft-public-20261018-v2/namespace_public.json)、[最新SFTの全ファイル照合](../reports/publication/chat-sft-public-20261018-v2/SFT_public.json)、[Baseの匿名取得](../reports/publication/chat-sft-public-20261018-v2/Base_public.json)を参照する。

## ライセンスと履歴

プロジェクトのコードへ[Apache License 2.0](../LICENSE)を適用し、[NOTICE](../NOTICE)で第三者の帰属を案内した。vendor内の元のApache-2.0/MITライセンスと出所は保持している。重み、Tokenizer、外部データの条件はコードのライセンスと区別する。

READMEは過去の進捗の羅列をやめ、概要、モデル入手先、CPU実行手順、現在の評価結果、実装と研究記録への入口へ整理した。以前のREADMEと過去の公開設定はGit履歴・原記録へ残っている。研究記録の日付時点の「未公開」「実行中」等を、現在の状態へ書き換えてはいない。

最初のローカル保存案にあったstate tensor数119の表記は、共有重みの別名を含む120 entriesと混同していたため、アップロード前に訂正した。元の科学学習・モデル重み・評価の変更はない。

GitHubのpublic切替直後、Git endpointが一度403/disabledを返して確認処理が停止した。原因は確定していない。その後の匿名APIはpublic/disabled=false、ページはHTTP200、匿名Gitのmainは公開commitと一致した。READMEの全bytesとApache-2.0の検出も匿名APIで確認した。[公開確認記録](../reports/publication/repository-public-20261018.json)。初回の補助PowerShellの空結果処理は、Gitの終了コードを明示検査するよう修正している。
