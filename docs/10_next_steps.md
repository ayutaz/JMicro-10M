# 次回のチェックリスト

最終更新: 2026-10-05 JST。[最新結果65](65_condition_selector_v2_preparation_results.md)、[実行64](64_condition_selector_v2_execution.md)、[status](autonomous_status.md)を正とする。四項目は教材準備不成立の停止分岐まで完了。新100M/一次/全文は未起動で、学習比較が完了したとは扱わない。

## 今回の完了

- [x] 過去の確認教材と重ならないtrain32全文を固定抽出し、全個別理由を保存。
- [x] selector v2の検出範囲/誤除外/限界を記録。開発弱例12のうち9を除外、正しい例4も除外。開発32を独立評価と扱わない。
- [x] 関連5tests成功、selector/builderを3273e77で固定してから受け入れpoolを準備。
- [x] 同source両20,000,072tokens/71,268全文、量/長さ全並び/BOS/EOS位置一致、共有10,232を記録。
- [x] 既知教材/開発32のhash集合152を両poolから除外。再取得・再tokenize・主Web全走査なし。
- [x] 未確認から固定random40各を一度だけ抽出し、全80原文・個別理由を保存。
- [x] 対照弱例12/候補14、「対照より少ない」「候補10/40以下」の両準備gate不合格を保持。再抽出・受け入れ後の再改修なし。
- [x] 101data evidencechecks/13終了checks成功。証拠の成功と準備品質失敗を区別。
- [x] 準備失敗分岐に従い、各100M/config/runtime凍結/新CUDA/日本語と全160/条件付き全文は未実施と記録。科学0/検証0。
- [x] 採否・結果65・限界と次案、元UI actual identity/HTTPを保存。元UIは停止していない。

Windows/Linux同期とverified local commitをGit実状態で確認して停止。文書のチェック印だけを証拠としない。旧結果60/63、Phase0〜3、全source/raw/weights/checkpoint・原品質条件は保持。

## 次回案（未開始）

意味を個別に確認できる小さなwhole-doc教材による同量学習比較を設計する。準備量と反復回数を独立に記録し、同source/文長/EOSの対照と未確認評価を使う。今回の20M準備gateは変更せず、別の実験契約として提案する。設計・新教材・GPUは今回未開始。

開発用例の数字を未確認教材・モデル品質と取り違えない。データ増量/追加学習の無効性や10Mの容量限界は未確定。Base/Chat未達、独立人手blind/主Web全件監査/保護test未実施を保持。500M/1B/20B/50B/Chat/量子化/公開へ自動移行しない。
