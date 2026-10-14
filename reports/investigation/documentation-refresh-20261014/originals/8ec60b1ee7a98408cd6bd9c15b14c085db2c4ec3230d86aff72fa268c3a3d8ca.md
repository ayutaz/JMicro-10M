# 同source・長さ/EOS一致教材の準備結果

2026-10-05 JST。[計画61](61_condition_preservation_next_plan.md)段階1〜4のうち、明記された**教材準備不成立の停止分岐**を実行した。段階1・2の実証拠と段階4の判断を保存し、段階3の学習・一次評価および条件付き全文評価は開始しない。学習比較が完了したという意味ではない。

## 結果と判断

| 項目 | 従来条件・対照 | 追加選別・候補 |
|---|---:|---:|
| 準備tokens | 20,000,028 | 20,000,028 |
| whole documents | 71,268 | 71,268 |
| body平均tokens | 278.631251 | 278.631251 |
| body長の最小/25%/中央値/75%/最大 | 70/242/276/314/512 | 70/242/276/314/512 |
| EOS / 1000tokens | 3.563395 | 3.563395 |
| body bytes | 83,700,142 | 83,456,687 |
| 固定random40全文の弱例 | 21/40 | 12/40 |

tokens量だけでなく、文書長の全並びとBOS/EOS位置も一致した。共有文書10,155を明記し、互いに独立なpoolとは扱わない。候補の弱例は対照より少ないが、計画の学習開始条件「候補10/40以下」が未達。sampleを引き直す・条件を緩める・選別器をこの40例に合わせて直すことはせず、候補を準備段階で不採用とした。

この21→12は一人のCodexによる非blind sample診断で、全poolの意味品質向上や統計的有意差の証拠ではない。**新しい学習tokensは科学0・検証0、GPU学習/評価0**。モデル精度・EOS・反復が改善したという結果は得ていない。元の10Bモデルと過去の比較結果はそのまま保存する。

## 実施した内容

段階1では保存済み旧/新160生成の個別診断、教材40全文を再利用し、人物・数量/時刻・否定/因果・反復の42実例を整理した。既存教材だけで具体的欠陥が確認でき、追加32例の抽出は不要と判断した。評価prefix・正解・生成文を学習データへ移していない。

段階2では既存200M poolの翻訳train499,066全文/140,036,743tokensのみを使用した。sourceは`shibatch/TinyStories-JA`、revision`155b4e5842076c90e07a4934d5b68410fe21f65f`、既存train4ファイルに由来する共通base/family holdout/ローカル完全一致除外後のstream。再取得・再tokenize・主Web12.23Bの再走査を省いた。公式validation/testを取得せず、全文を切断・複製せずに長さ別quotaをそろえた。

候補は根拠の薄い教訓・一般化、同じ話者の自己応答、文/長い節の反復、局所の人物/話題の弱い接続を追加除外した。残った適格供給は86,847,717tokens。選別器は意味の正しさを保証せず、結びや話題・対話比率も変えるため純粋な意味品質の因果比較とも断定しない。

builder seed202610061、sample seed202610062を固定した。各40は同じ文書slotの無作為抽出で再抽出なし。全80に全文と具体的な個別理由を保存した。架空・擬人化・失敗/悲しい結末だけでは弱例にしない。

## 残った問題の具体例

| 候補sample index（0始まり） | 欠陥 |
|---:|---|
| 30 | 男の子が「ツルを驚かせようと近づく」直後、母が「わざと驚かせようとしたわけじゃない」と意図を否定する |
| 32 | ポケットから出た果物が虫になり、果物の所在を説明しないまま同じ果物を食べる |
| 38 | 犬を遠ざけるため投げた石を、拾い戻す描写なしに元の場所へ返す |
| 14 | 欲しかったおもちゃを得る体験を描かず、価値がなかったという判断へ移る |

これらは局所の単語接続や反復除外だけでは捉えられない、意図の否定・対象の所在・出来事と結論の関係である。一方、候補の擬人化された魚や木、失敗が具体的に回収された話は、現実と違う設定や成功しない結末だけでは弱例としなかった。

## 計算量・証拠・停止

WSL2/Linux disk、uv管理Python3.12.7で実行。12 CPU workersで旧tokensをdecodeして選別し、本文の再tokenizeを省いた。段階1＋builder実時間13.752109秒でCPU処理上限1800秒以内。新poolとsampleの証拠照合0.770125秒。意味診断・実装時間はこの処理時間と別である。

関連CPU4tests成功。新しいBOS/EOS・hash・source・固定sample・全80理由を含む101の証拠条件を確認した。これはモデル品質の合格ではなく、保存した準備結果が実データと一致する確認。条件付き全文・新CUDA再開確認・100M runner/configの凍結は、準備が不成立なので行っていない。実施していない項目を合格扱いしない。

- [保存失敗診断](../reports/phase6/condition_preservation_diagnosis.json)、[準備量とbinding](../reports/phase6/condition_preservation_ready.json)、[builder実process/job](../reports/phase6/condition_preservation_prepare_job.json)。
- [全80原文付き内容診断・準備gate](../reports/phase6/condition_preservation_data_review.json)、[個別notes](../reports/phase6/condition_preservation_source_notes.json)、[関連tests](../reports/phase6/condition_preservation_tests.xml)。
- [採否](../reports/phase6/condition_preservation_judgment.json)、[準備失敗分岐の完了・UI実確認](../reports/phase6/condition_preservation_completion.json)。

大容量教材は`/home/aihub_ubuntu/jmicro-data/phase6/condition-preservation-20261005/{control,refined}/`、Linux実行記録は`reports/phase6/condition-preservation-100m-20261005/`。名前に100mがあるが学習したことを意味しない。両manifest/shards/index/sample、selector/builder凍結copy、全ready/diagnosis/jobを保持する。Gitには可搬な証拠とコードを保存し、shardsは含めない。

元10B UIは今回GPU jobを開始しなかったため停止せず、完了確認でactual PID/boot/start_ticksとHTTPの親SHA・10,000,007,168tokens・busy=falseを照合する。[UI](http://127.0.0.1:7860)は元10Bである。関連checksと文書同期を確認してlocal commitで停止し、pushしない。

## 次回案

次の目的は、学習開始に足る意味品質の教材を成立させること。意図/否定と物の所在の欠陥を、今回確認した40例と分離したtrain診断例で検出できるか先に測る。selectorの検出範囲・正しい架空話の誤除外・候補供給量を固定比較し、ルールを凍結してから未確認の各40を新seedで一度だけ確認する。既に見た40を改修後の受け入れ評価へ再利用すると選別の偏りが生じるため避ける。

未確認sampleで元の準備条件を満たせた場合に、同じ元10Bから各100M・日本語/全160内容・原採用条件の限定比較を提案する。今回はその改修・新sample・学習を開始しない。データ増量や学習量増加の無効性、10Mの容量限界は未確定。Base/Chatの品質目標、独立全corpus監査未完了、人手blind/保護test未実施を維持する。500M/1B延長・20B/50B/Chatへ自動移行しない。
