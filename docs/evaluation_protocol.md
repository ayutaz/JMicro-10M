# 評価方法と結果の読み方

更新: 2026-10-18 JST。

最新SFTの全1,973応答は確認済みで、候補は不採用です。評価が完了したことと、Base/Chatの正式品質条件を満たしたことを区別します。

## 現在の評価条件

最新診断は学習前後の教材128応答、未知値32、質問構造32、16会話の実履歴48応答、計240。回帰確認は既存7組×219と公開100ケースの200応答、計1,733です。合計1,973に1,400件の新しい判定と573件の厳密な実履歴/raw判定再利用を含みます。

BF16/math、greedy、最大32生成token、抑制IDは0/1/2/4/5/6、停止はEOT7/EOS3です。各suiteの抑制なし対照も保存します。最大token到達は自然停止と数えません。自己履歴には実際のAssistant本文を入れ、空応答・誤答・壊れたUTF8も記録から消しません。

## 内容と機械的な検査

文法・関連性・文脈を0/1/2で個別に判定し、要求値が含まれることと、回答全体が成立することを区別します。停止、反復、空、役割漏れ、raw UTF8、履歴切断は別に集計します。損失や単語一致だけで内容成立を推定しません。

Codex非blind評価は独立した人手blind評価ではありません。固定DEVの件数を一般利用全体の精度と解釈せず、bootstrapの単位・seed・分母を各結果へ残します。最新の旧モデル比較は教師集合と学習量も違うため、単独要因の因果効果ではありません。

## BaseのBPBと元の品質条件

`BPB = 本文NLL総和 / (ln(2) × 採点したcanonical UTF-8 bytes総数)`。本文は一回だけ数え、EOSを別集計します。CRLF/CRをLFへ統一しU+0000を除き、他のUnicode・空白を暗黙に正規化しません。異なるTokenizerのperplexityを直接比較しません。

元Base DEV80の条件は文法≥56、一貫性≥27、適切完結≥27、EOS≥37、規定反復≤18、空/役割/Unicode失敗0。相対差・CI・BPB/strong/historical保持等も必要です。これらの一部や小集合の暗記だけを正式採用へ読み替えません。

## 固定suiteとTEST

v1の[protocol.json](../configs/evaluation/protocol.json)は80 DEV/20 TEST、64token等の元契約を保存しています。後続SFTの32token条件や、Base標準400/長文40の抑制ID差を上書きして揃えません。評価時に混在fileを開いてからfilterする旧経路へ戻さず、DEV専用manifest/readerを使います。

元TESTにはCPU解析履歴があり、新しい封印TESTが必要です。全文DEV/全440接続部品の36 CPU checksは、資格ある最新モデルの実全文評価・全内容判定の代替ではありません。独立全工程・人手blind・最終TESTの未達を保持します。[最新結果165](165_chat_two_attribute_diagnosis_results.md) / [残課題](10_next_steps.md)。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/evaluation_protocol.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="bpbとtokenizer比較"></a>
<a id="v1契約と後続実験を区別する"></a>
<a id="人手rubric"></a>
<a id="採用基準とデータbucket"></a>
<a id="数値一致seed統計"></a>
<a id="最新評価の範囲と制約"></a>
<a id="現行のbase採否と読取り境界"></a>
<a id="生成条件"></a>
<a id="自動失敗指標の定義"></a>
<a id="評価仕様と現行の適用"></a>
<a id="評価対象とsplit"></a>
