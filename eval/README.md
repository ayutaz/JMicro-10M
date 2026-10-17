# 固定評価データと現在の利用状況

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](../docs/148_latest_base_and_documentation.md) / [現在の計画145](../docs/145_post_rejection_next_plan.md) / [文書一覧](../docs/README.md) / [全件カタログ](../docs/document_catalog.md)。

新しいDEV経路はDEV専用artifact/manifest/readerを使う。旧混在eval/base.jsonlの全行解析後filterへ戻さない。既知DEVの隔離であり未知DEVを作った証拠ではない。正式全件suiteとpilot80の特殊ID抑制は異なるため、rawと設定差を残す。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

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

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="更新前の本文契約当時の記録"></a>
