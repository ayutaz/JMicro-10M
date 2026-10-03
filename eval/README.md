# 固定評価データ v1

利用状況（2026-10-03）: Phase 4に続きPhase 5のsmoke/100M候補でもBase dev 80件×5条件（抑制あり/なしgreedy、sampling seeds 42/43/44）の400出力を取得し、生成ID/flagを独立照合した。選定NoNormのgreedy EOS 0/80・反復54/80、sampling Unicode 2/240で品質目標は未達。[Phase 5完了記録](../docs/23_phase5_completion.md)。固定testとChat suiteはモデル評価に未使用。Phase 6①では固定suiteの検出された混入clusterを学習corpusから除外し、②の4 dev文書採点はcorpus側の状態保全確認で、固定生成suiteの新しい品質実験ではない。[準備完了証拠](../docs/26_phase6_preparation_completion.md)

この評価例はプロジェクト用に独自作成したもので、学習データではない。Base 100件・Chat 100件をそれぞれ10 categoryに分け、categoryごとにdev 8件/test 2件、合計dev 80件/test 20件とした。ID・file hash・split membershipは[split_manifest.json](split_manifest.json)へ固定する。

- [base.jsonl](base.jsonl): 自然文completion。日常、文法、短編、会話、描写、数字、固有名詞、句読点、短期文脈、常識。
- [chat.jsonl](chat.jsonl): 挨拶、感情、日常、質問返し、曖昧発話、役割境界、記号、訂正、話題継続、文脈。
- [rubric_examples.json](rubric_examples.json): 文法/関連性/文脈の0/1/2を区別する11件の手動採点例。Codexが設計時に採点した架空応答で、実モデルの結果や第三者人手評価ではない。
- [tokenizer_golden.json](tokenizer_golden.json): 30件の共通前処理の期待値。Tokenizer encode/decode・byte piecesの実検証はPhase 2で完了済み。

`family_id`で関連例のsplitを管理する。現v1はケースごとに別familyを付与し、全入力のexact重複は自動検査済み。意味的なnear-duplicateの完全排除は保証しない。今後同じcaseの言い換えを増やす場合は同じfamilyにし、splitを跨がせない。

Chatの履歴は最後がUser、途中はUser/Assistant交互。70件は1発話の入力、30件は2〜4 User turnsの固定履歴。固定履歴での最終応答評価と、モデルの出力を履歴に戻して複数turnを続けるrolloutは別の条件とし、後者はPhase 7で加える。

`checks`は意味上の確認事項で、唯一の正答文字列ではない。関連した短い表現を許容し、長さを得点へ自動加点しない。devを設定選定へ使い、testは最終確認用とする。testを見て調整した次版には新しい未使用testを用意する。

詳細は[評価仕様](../docs/evaluation_protocol.md)を参照する。
