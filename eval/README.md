# 固定評価データ v1

利用状況（2026-10-03）: Phase 4ではBase dev 80件について抑制ありgreedy・抑制なしgreedy・sampling seeds 42/43/44の400出力を各モデルで取得した。固定testとChat suiteは未使用。検証checkpointのEOS停止は0/80で、品質目標達成ではない。[評価report](../reports/phase4/base_evaluation_contract_report.json)

この評価例はプロジェクト用に独自作成したもので、学習データではない。Base 100件・Chat 100件をそれぞれ10 categoryに分け、categoryごとにdev 8件/test 2件、合計dev 80件/test 20件とした。ID・file hash・split membershipは[split_manifest.json](split_manifest.json)へ固定する。

- [base.jsonl](base.jsonl): 自然文completion。日常、文法、短編、会話、描写、数字、固有名詞、句読点、短期文脈、常識。
- [chat.jsonl](chat.jsonl): 挨拶、感情、日常、質問返し、曖昧発話、役割境界、記号、訂正、話題継続、文脈。
- [rubric_examples.json](rubric_examples.json): 文法/関連性/文脈の0/1/2を区別する11件の手動採点例。Codexが設計時に採点した架空応答で、実モデルの結果や第三者人手評価ではない。
- [tokenizer_golden.json](tokenizer_golden.json): 30件の共通前処理の期待値。Tokenizer encode/decode・byte piecesの実検証はPhase 2で完了済み。

`family_id`で関連例のsplitを管理する。現v1はケースごとに別familyを付与し、全入力のexact重複は自動検査済み。意味的なnear-duplicateの完全排除は保証しない。今後同じcaseの言い換えを増やす場合は同じfamilyにし、splitを跨がせない。

Chatの履歴は最後がUser、途中はUser/Assistant交互。70件は1発話の入力、30件は2〜4 User turnsの固定履歴。固定履歴での最終応答評価と、モデルの出力を履歴に戻して複数turnを続けるrolloutは別の条件とし、後者はPhase 7で加える。

`checks`は意味上の確認事項で、唯一の正答文字列ではない。関連した短い表現を許容し、長さを得点へ自動加点しない。devを設定選定へ使い、testは最終確認用とする。testを見て調整した次版には新しい未使用testを用意する。

詳細は[評価仕様](../docs/evaluation_protocol.md)を参照する。
