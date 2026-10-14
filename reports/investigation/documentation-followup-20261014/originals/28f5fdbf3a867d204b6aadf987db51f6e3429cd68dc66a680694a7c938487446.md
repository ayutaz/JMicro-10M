# Phase 2完了記録

履歴の位置付け（2026-10-03）: 本文の件数・hash・未実施・次の作業は実施当時の記録。現在は[Phase 0〜4が完了](21_phase4_completion.md)し、ユーザー指定により停止中。[最新状態](autonomous_status.md)を優先する。過去のreport・snapshotは上書きしない。

2026-10-02、M1 iMac・16GB上のCPUで実施。Phase 3の前提として、同一train-only sampleからSentencePiece Unigram + byte fallbackの4096／8192語彙を学習・検証した。モデル本体の学習は実施していない。

## 成果物と契約

`artifacts/phase2/{4096,8192}/`に`tokenizer.model`、`tokenizer.vocab`、`special_tokens.json`、`tokenizer_wrapper.json`、`training_metadata.json`を保存した。artifactはGit管理外で、入力sample・モデル・依存lockのSHA-256を記録する。

- [契約・再学習検証](../reports/phase2/tokenizer_contract_report.json)
- [全6候補の引数・結果](../reports/phase2/tokenizer_training_candidates.json)
- [全corpusの圧縮率・会話token計数](../reports/phase2/tokenizer_comparison.json)
- [共通codecと会話処理](../src/jmicro/tokenizer.py)、[学習・比較処理](../src/jmicro/phase2.py)

sampleはPhase 1の2,444文書・対話、本文4,499,689 bytes。sample file SHA-256は`2bd5f104d0931e883a891f64bbcd0392cabd7259d3cfc5cd8a693f7f1acf54e6`。語彙数を固定したままcoverage 0.9995／0.999／0.995を各語彙で試し、全6候補が合格した。採用coverageは両方0.9995。4k／8kの勝者は選ばず、GPUでの品質比較へ渡す。

PAD／UNK／BOS／EOS／SYSTEM／USER／ASSISTANT／EOTは順にID 0〜7、byte piecesは256個。identity正規化、dummy prefixなし、余分な空白の削除なし。共通前処理はCRLF／CRをLFへ変換し、NULを除く。それ以外のUnicodeを保持する。

改行・タブなどASCII space以外のwhitespace、文字そのものの`▁`、`<`はUTF-8 byte piecesで表現する。通常のspanをUnigramへ通し、decodeはpieceをbytesへ戻してからUTF-8を検証する。この処理で本文中の`<|assistant|>`等を構造IDと区別する。**直接の`SentencePieceProcessor.encode/decode`ではなく、このwrapperが学習・推論の契約**となる。

学習時も同じ境界で文書をspanへ分けた。protected文字は予約byte piecesで表現し、通常pieceの学習から省く。sampleの文書順は共通で、trainerへ渡したspan数・最大長・引数を記録する。空白のみのspanは学習対象から省くが、本文encodeでは保持する。

CPU 1 thread、入力shuffleなしで学習。同じ機械で再学習し、出力prefixを除いたModelProtoの完全一致を確認した。使用版SentencePiece 0.2.2にはtrainerのrandom_seed項目がないため、未対応のseed引数は渡していない。別OS・別versionでの再学習一致は保証せず、Windowsでは学習済みartifactを引き継ぐ。

前処理golden 30件と追加3件、全sample、採用corpus全22,998件のround-tripを確認。全256 byte値の復元、lone surrogate・未decode bytesの拒否、生成bytesの不正UTF-8検出、固定seedで作った未出現Unicode・制御文字の追加テストも通る。

## 比較結果

domainは現在のpilotのWeb／会話bucketで比較。bytes/tokenは本文の合計bytes÷合計tokensで、構造IDを含まない。byte率にはprotected文字のbyte表現も含む。UTF-8の複数byteを「複数文字」と数えない。

| 語彙 | Web bytes/token | 会話 bytes/token | Webが1024以内 | 会話が1024以内 | 会話総系列tokens | Assistant教師tokens |
|---|---:|---:|---:|---:|---:|---:|
| 4096 | 3.9207 | 4.4855 | 99.98% | 100% | 1,496,446 | 705,467 |
| 8192 | 4.7865 | 5.4406 | 100% | 100% | 1,250,640 | 581,149 |

Webのcontext計数はBOS／EOS込み、会話はBOS／role／各EOT込み。表は全splitの観測量で、学習実績ではない。詳細reportにはtokens/document、chars/token、byte token率・byteで表現された文字率と分布を保存する。Web4kでは19,998文書のうち4文書が1024を超える。

Assistant本文と直後のEOTだけを教師とし、logits[:-1]がlabels[1:]を予測する。45,051個のAssistant応答をそれぞれ一度だけ教師にするwindowを作り、過去のAssistantをmaskしたwindowの教師総数が元の対話の教師総数と一致した。履歴が長い場合は古いUser／Assistantの完結turnから除き、最新発話を途中で切らない。

## 再実行

```sh
uv sync --frozen --extra ml
uv run --frozen --extra ml scripts/prepare_phase2.py
uv run --frozen --extra ml scripts/prepare_phase2.py --measure-only
```

最初のcommandはPhase 1の固定sampleとcorpusが必要。2番目は学習候補と比較reportを再作成し、3番目は既存artifactのhashを確認して計数のみを行う。GPU、CUDA、RTX 4090は不要。BPB・会話品質・生成のUnicode成功率は学習済みモデルで後続評価する。
