# 固定評価データと現在の利用状況

更新: 2026-10-14 JST。[最新結果141](../docs/141_chat_lr_comparison_results.md)は全28セット・6,132判断・NLL7点、全原gateで不採用。Base/Chat未完成・未採用、再採点・生成評価・TEST利用は停止中。現在は[文書更新142](../docs/142_documentation_refresh.md)のみ。

## 未参照と利用済みを区別する

元v1のBase/Chat各DEV80/TEST20とsplit/hashは不変。Chat DEVは後続SFTで利用済み。元Chat TEST20行も139のCPU準備で構文解析した事故があり、未参照とは呼ばない。学習・GPU評価には使用していない。将来有資格Chat確認には新たな封印TESTが必要。元Base TESTはこの事故では解析していない。今回の文書更新でもdataset/TESTを解析・採点しない。

最新139は新DEVと138/133/元旧DEVの4suite。各固定履歴80・role抑制なし80・実自己履歴24会話59turnを別に保存した。既知12セット2,628判断の再利用は原prompt/履歴/token/bytes/checksまで同一の場合だけ。Codex非blindで、独立人間の成績ではない。

v1のhuman_scoresのnull、v2.1の[診断結果](../docs/46_japanese_base_evaluation_v2_results.md)、原raw・notes・停止/反復/Unicode失敗を保持。提供履歴と実自己発話履歴、DEV256/固定NLLと正式fullDEV、生成seedとfresh学習seedを混同しない。[現行適用と凍結評価契約](../docs/evaluation_protocol.md)。

## v1固定入力の契約

この評価例はプロジェクト用に独自作成したもので、学習データではない。Base 100件・Chat 100件をそれぞれ10 categoryに分け、categoryごとにdev 8件/test 2件、合計dev 80件/test 20件とした。ID・file hash・split membershipは[split_manifest.json](split_manifest.json)へ固定する。

- [base.jsonl](base.jsonl): 自然文completion。日常、文法、短編、会話、描写、数字、固有名詞、句読点、短期文脈、常識。
- [chat.jsonl](chat.jsonl): 挨拶、感情、日常、質問返し、曖昧発話、役割境界、記号、訂正、話題継続、文脈。
- [rubric_examples.json](rubric_examples.json): 文法/関連性/文脈の0/1/2を区別する11件の手動採点例。Codexが設計時に採点した架空応答で、実モデルの結果や第三者人手評価ではない。
- [tokenizer_golden.json](tokenizer_golden.json): 30件の共通前処理の期待値。Tokenizer encode/decode・byte piecesの実検証はPhase 2で完了済み。

`family_id`で関連例のsplitを管理する。現v1はケースごとに別familyを付与し、全入力のexact重複は自動検査済み。意味的なnear-duplicateの完全排除は保証しない。今後同じcaseの言い換えを増やす場合は同じfamilyにし、splitを跨がせない。

Chatの履歴は最後がUser、途中はUser/Assistant交互。70件は1発話の入力、30件は2〜4 User turnsの固定履歴。固定履歴での最終応答評価と、モデルの出力を履歴に戻して複数turnを続けるrolloutは別の条件とし、後続SFTの実自己履歴24会話59turnは実施済みで、実験別reportに別の分母を保持する。

`checks`は意味上の確認事項で、唯一の正答文字列ではない。関連した短い表現を許容し、長さを得点へ自動加点しない。devを設定選定へ使い、testは最終確認用とする。testを見て調整した次版には新しい未使用testを用意する。

詳細は[評価仕様](../docs/evaluation_protocol.md)を参照する。
