---
title: Akebono-10M-chat
emoji: 🌅
colorFrom: yellow
colorTo: red
sdk: static
app_file: index.html
license: apache-2.0
models:
- hisakata-ai/akebono-10m-chat
---

# Akebono-10M-chat

実験的な日本語モデルの試用画面です。Hugging Faceの無料Static Spaceで公開し、推論は利用者のブラウザー内のCPU / WASMで実行します。有料サーバー、GPU、外部推論APIは使いません。初回に約60 MBのモデルと実行ライブラリーを読み込みます。読み込み後の速度は利用者の端末によって変わります。

元モデルは [hisakata-ai/akebono-10m-chat](https://huggingface.co/hisakata-ai/akebono-10m-chat)、固定したcommitは `74b3a1739e6d16883177c6021b3c03a7d517c7fb` です。元v19の約9,965,824パラメータをFP32 ONNXへ変換しました。量子化や追加学習は行っていません。万能な会話AIではなく、不自然な返答、反復、否定や履歴の取り違えが残っています。既存評価では通常の全会話成立3/40、長会話0/12と報告されています。詳細と学習元の帰属は公開モデルおよび `MODEL_CARD.md` を参照してください。

## 操作

読み込みが終わったら文章を入力して「送信」を押します。Enterで送信、Shift + Enterで改行できます。「リセット」は生成を中断して、そのタブの会話を消します。ページの再読み込みでも会話は消えます。他のタブや利用者とは履歴を共有しません。

入力上限500文字。文脈は履歴込み512トークン、回答用に最低16トークンを確保します。長すぎる入力は履歴を変えず拒否し、入力や履歴を勝手に切り捨てません。生成はEND / EOS、128トークン、160文字に達した時点、または文脈上限で停止します。160文字に達するトークンまで復号するため、そのトークンに複数文字が含まれると160文字を少し超える場合があります。終了理由と形式検査を画面に表示します。

元のsystem / user / assistant / END形式、改行token ID8、END ID7、EOS ID3、greedy argmaxを保っています。反復ペナルティや応答補正、固定返答への置換はありません。特殊tokenや不正形式の生成は隠さず表示します。

## 会話の保持

会話はページのメモリーとそのページ専用Workerだけに保持します。入力をネットワークへ送信せず、会話ログ、Cookie、localStorage、sessionStorage、IndexedDB、履歴保存や分析用通信は実装していません。Spaceの配信基盤はモデル・ページなど静的ファイルへのアクセスを処理します。

## 変換と動作確認

ONNX入力長1、19、64、128、512で元Pythonとのlogits差を調べ、最大絶対差は約1.6e-5以内、各入力のargmaxは一致しました。WASMでは全12,288語彙、33件の符号化・復号、5件の会話についてtoken IDs、返答、終了理由、形式検査が一致しました。浮動小数点のbit単位の一致や、あらゆる入力で同じ生成になることを保証するものではありません。

実際のEdge / CPU WASMで5件の生成、猫・犬の会話の分離、リセット、生成中のリセット、再読み込み、入力と文脈上限の拒否を確認しています。挨拶は「こんにちは。今日は少し休もう。」、猫・犬への最初の返答はどちらも「いつも見かける所？」で、自然な応答とは言えません。動作確認は会話能力の評価とは別です。

## 実装とライセンス

モデル重み、学習済みtokenizer、自作アプリはApache-2.0です。第三者ライブラリーの既存ライセンスは維持します。`THIRD_PARTY_NOTICES.md` と各LICENSEを参照してください。

- ONNX Runtime Web 1.30.0、CPU WASM、1スレッド: https://github.com/microsoft/onnxruntime
- MLC web-tokenizers 0.1.6、既存SentencePiece WASM実装: https://github.com/mlc-ai/tokenizers-cpp
- 元Python実装、構造、学習元帰属、制約: https://huggingface.co/hisakata-ai/akebono-10m-chat
- アプリの推論ソース: `engine.mjs`、`worker.mjs`。UI: `main.js`、`index.html`、`styles.css`。

`model.onnx` SHA256: `c299600edd974d5b11c3320f9e24392e859716424b7d28dad668af5baf94ef56`

`tokenizer.model` SHA256: `b5578c547c593640cd412d66d094eaf8d8fc79eb2e9ddbacc041903f94eab63b`

各ファイルの容量とハッシュは `MANIFEST.json`、`SHA256SUMS` に記録しています。
