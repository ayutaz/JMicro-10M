# Phase 3完了記録

履歴の位置付け（2026-10-03）: 本文の件数・hash・未実施・次の作業は実施当時の記録。現在は[Phase 0〜4が完了](21_phase4_completion.md)し、ユーザー指定により停止中。[最新状態](autonomous_status.md)を優先する。過去のreport・snapshotは上書きしない。

2026-10-02、M1 iMac・16GB上でT4K／T8Kのモデル実装、cache、保存読込、HF／float GGUF、Q8／Q4候補、推論入口を検証した。重みはseed 42のランダム初期化で、モデルの学習・optimizer更新は行っていない。停止検証には別の合成重みfixtureを使った。

最終の検証一式は24.62秒。実装・修正・Tokenizer学習・runtime初回build・docs更新を含む作業時間とは区別する。Phase 3完了時点では次にWindows/WSLへ移行する計画だった。その後Phase 4を完了した。[完成までの時間短縮を優先した最新計画](15_project_roadmap.md#高速に完成させる進め方)

## モデルと数値一致

[実装](../src/jmicro/model.py)はRMSNorm、half-split RoPE、4Q／2KV GQA、head間gain共有のQ/K RMSNorm、SwiGLU、共有embeddingを持つ。Q/Kは正規化後にRoPEを適用し、cacheは変換済みKとVを保持する。paddingとは別に各系列の有効token位置を数え、chunk decodeは絶対位置で因果maskを作る。

| モデル | 実parameter数 | 層数／FFN幅 | native float logitsの最大絶対差 |
|---|---:|---|---:|
| T4K | 10,002,816 | 13／640 | 約3.04e-6 |
| T8K | 9,772,800 | 12／576 | 約2.86e-6 |

数値gateは事前のFP32仕様`atol=1e-5, rtol=1e-4`を維持した。実装間の比較後に閾値を緩めていない。次を確認した。

- 未来tokenを変えても過去logitsは完全一致。GQAはQ head 0／1→KV0、2／3→KV1の手計算参照と一致。
- 有効長が違うbatch、途中のpadding、単独系列との一致、prefill／1-token／chunk cacheが一致。
- 1024-token全系列と37／173／300／1／512／1-tokenに分けたcacheが一致。1024を超える入力は拒否する。
- Assistantだけのshift済みloss、全parameterの有限gradient、共有embedding、保存読込を確認。
- 公式Transformers 5.18.0のQwen3 eager実装へ同じ重みをstrictに読み込み、prefill／cache／HFディスク再読込を比較。
- HF safetensorsから公式GGUF tensor名mapでQwen3 float GGUFを作り、実llama.cppの全位置logitsとcached decodeを比較。

証拠は[モデル契約report](../reports/phase3/model_contract_report.json)、[export・Tokenizer・量子化report](../reports/phase3/export_parity_report.json)、[完了監査](../reports/phase3/completion_audit.json)。全48テストと、両モデル×3 backendの実CLI 6件が成功。小規模の単体テストだけでなく、両モデルの実構成で長さ1024まで検証した。

## 配布Tokenizerと停止

llama.cpp内蔵SPMはgolden 33件のID一致がT4K 29件、T8K 30件で、共通契約を満たさなかった。**外部SentencePiece wrapperでencodeし、構造IDを挿入してnativeのtoken入力APIへ渡す経路を採用**。出力も同じwrapperでdecodeし、不正UTF-8を検出する。

HFは`AutoModelForCausalLM`でweightsを読める。独自Tokenizerは[共通codec](../src/jmicro/tokenizer.py)で扱い、Qwen既定の`AutoTokenizer`には置き換えない。HF artifactはmodel config・safetensors・SentencePiece model・wrapper設定・special IDs・generation config・形式説明用chat templateを含む。テンプレートを文字列にrenderして一括encodeする方法は本文中のrole表記を区別できないため、推論入口はmessageごとに本文encodeと構造ID挿入を行う。

ChatはEOT=7／EOS=3、BaseはEOS=3で停止。PAD／UNK／BOS／role開始IDは生成時に抑制する。nativeのEOG metadataと実際の停止controllerを確認し、さらに合成重みfixtureから実greedy argmaxでEOT／EOSを出して、torch／HF／GGUFすべてが1 tokenで止まることを検証した。fixtureの停止は会話品質の評価ではない。

GGUFの内蔵Tokenizerを使う汎用`llama-completion`は`-no-cnv`で起動・生成したが、Tokenizer契約に互換性がないため正式な入口にしない。runtimeのTokenizer差をreportへ残し、変換成功と入出力の一致を分けて判定した。

## 量子化の実容量

すべて実llama.cppのquantizerで作成し、native読込と8-token上限の生成を確認。表のMBは10進。artifact列はGGUFに外部Tokenizer・HF側の設定等を足した容量で、Python環境・native runtime binary・研究reportを含まない。

| モデル | 形式 | GGUF MB | Tokenizer・設定込み MB | FFN downの実型 |
|---|---|---:|---:|---|
| T4K | Q8_0 | 10.747 | 10.807 | Q8_0 ×13 |
| T4K | Q4_0 | 6.020 | 6.080 | Q4_0 ×13 |
| T4K | Q4_K_M | 6.706 | 6.765 | Q8_0 ×6、Q5_0 ×7 |
| T8K | Q8_0 | 10.604 | 10.738 | Q8_0 ×12 |
| T8K | Q4_0 | 6.262 | 6.396 | Q4_0 ×12 |
| T8K | Q4_K_M | 6.866 | 7.000 | Q8_0 ×6、Q5_0 ×6 |

幅576／640のdown projectionは256要素K-quant blockに揃わず、Q4_K_Mでは実際にfallbackする。NormはF32を残し、tied embeddingも精度選択で別型になる。全tensorの型・shape・bytesとquantizer logのhashをreportに保存した。output weightは別保存せず、embeddingを共有する。

Q4候補は5〜10MB級の配布目標に収まるが、品質の採用判断は学習後。ランダム重みの生成は機械経路の確認で、日本語会話の成立を示さない。RSS・CPU速度・量子化後BPB／会話品質はPhase 8で測る。

## 再現と推論入口

```sh
uv sync --frozen --extra data --extra ml --extra export
uv run --frozen --extra ml --extra export scripts/build_runtime.py --fetch
uv run --frozen --extra ml --extra export scripts/verify_phase3.py
uv run --frozen --extra ml --extra export scripts/check_inference_cli.py
uv run --frozen --extra data --extra ml --extra export pytest -q --junitxml=reports/phase3/tests.xml
```

native buildにはCMakeとC++17 compilerが必要。公開llama.cppをcommit `46ca246de9bb1c35269722a6240d37d9dfd79cad`へ固定し、archive hash・bridge source／binary・quantizer binaryとbuild commandをreceiptへ記録した。archive展開では埋込Git表示が親repoを拾うため、revision証拠はreceiptを使う。CPU 2 threads、F32 K/V cache、flash attentionなしで比較した。Mac binaryはWindowsへコピーせず、Linux上で再buildする。

```sh
uv run --frozen --extra ml --extra export scripts/infer.py \
  --backend gguf --artifact artifacts/phase3/t8k/model-q4_0.gguf \
  --tokenizer artifacts/phase2/8192/tokenizer.model \
  --prompt 'こんにちは' --max-new-tokens 16
```

`--backend torch --artifact artifacts/phase3/t8k/torch`、または`--backend hf --artifact artifacts/phase3/t8k/hf`でも同じcodecを使う。Chatは`--prompt`の代わりに`--messages messages.json`を渡す。JSONは`[{"role":"user","text":"こんにちは"}]`等のmessage配列。生成分を含めて1024以内にし、Chat履歴が長ければ古い完結turnを削除してprefillする。最新User／systemが単独で収まらない場合は発話を切らずエラーにする。

モデルとTokenizerのchecksumを入口で照合する。artifactは`artifacts/phase3/{t4k,t8k}/`、大型weights・logits・runtimeはGit管理外。再現にはPhase 1データとPhase 2 artifactが必要で、CPU検証結果と固定hashをWindowsへ引き継ぐ。

完了監査は現在のsource snapshot、test XML、report、実artifact、native logitsと固定revisionのsourceを照合する。既存の準備run形式は`phase=0, kind=preparation, tokens_seen=0`のままで、Phase 3の学習実績としては扱わない。

保存済みの監査はPhase 3完了時点のsource snapshotに対応する。以後の計画/docs更新で現在のsourceが変わっても、過去のsnapshotとreportは履歴として保持する。新しく監査する場合は新しいsource snapshotを用意する。Windows移行確認ではhash/ID・CUDA等の関連gateを確認し、このnative CPU全検証の再実行は必須にしない。

```sh
uv run --frozen --extra ml --extra export scripts/experiment.py prepare-run \
  --name phase3-complete --tokenizer-artifact artifacts/phase2/8192/tokenizer.model \
  --dataset-manifest data/phase1/processed/dataset_manifest.parquet
uv run --frozen --extra ml --extra export scripts/audit_phase3.py --snapshot reports/<表示されたrun_id>
```

次はPhase 4。Windows／WSL＋RTX 4090へ切り替え、CUDA・BF16・shard・学習器・保存再開・最大安定micro batchを実測する。iMac上のbackward検査は実装の検証であり、本学習を開始したことにはしない。
