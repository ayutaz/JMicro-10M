# 固定評価データと現在の利用状況

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](../docs/144_base_document_balance_results.md) / [前回Chat結果141](../docs/141_chat_lr_comparison_results.md) / [次の計画145](../docs/145_post_rejection_next_plan.md) / [今回更新146](../docs/146_documentation_followup.md)。

v1 Base/Chat各DEV80/TEST20の原suite/hashは維持する。既存Base greedy80と内容reviewは混在suite全行をJSON解析してからDEVを抽出するため、元Base TEST20 promptを未参照とは呼べない。旧protected_test_used=falseはGPU TEST採点なしの記録で、CPU未開封の証明ではない。旧sourceと結果を保全し、将来のDEV経路はTESTファイルを開かない契約にする。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 更新前の本文・契約（当時の記録）

## 未参照と利用済みを区別する

元v1のBase/Chat各DEV80/TEST20とsplit/hashは不変。Chat DEVは後続SFTで利用済み。元Chat TEST20行も139のCPU準備で構文解析した事故があり、未参照とは呼ばない。学習・GPU評価には使用していない。将来有資格Chat確認には新たな封印TESTが必要。元Base TESTはそのChat事故では解析していないが、後続144のBase readerでCPU解析された。今回の文書更新でもdataset/TESTを解析・採点しない。

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
