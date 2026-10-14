# Baseの実験結果を探す

2026-10-15最新閉鎖: [cross-GQA signed-map100M](../reports/phase6/cross-gqa-map-science-20261015/completion.json)は元CE全stream/base config＋宣言した52scalar構造差・全state/history・全80個別notesまで確認し不採用。元native10,001,152対候補10,001,204、文法60/80でも一貫性2/80・完結2/80・EOS18/80・反復47/80で元gate未達。旧query-headwise output gateとは別機構だが今回の固定map/係数/normalization/親/seed/decoder/予算は閉鎖し救済しない。次案は索引だけでなく原proposal/trainer/resultで既存条件との実差分を確認する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と4項目goalは未達。以下は当時の履歴。

2026-10-15最新閉鎖: [sentence-copy確率減衰100M](../reports/phase6/pseudo-repetition-science-20261015/completion.json)は全17,698更新/全state/対照一致・全80内容reviewまで完了し不採用。原rollout4gram ULとは正のdetach確率目標と合成全句copy入力が異なるが、今回の固定variantは反復31/80・一貫性2/80・適切完結3/80で未達。係数/decay/copy/文境界/親/seed/decoder/予算を変更して再試行しない。前のcontext likelihood/FIMも閉鎖のまま。索引の語句検索だけで新規性を判断せず、原proposal/trainer/resultsと照合して別案を1件選定する。4項目goalの独立学習/fullDEV/新TEST/採用はまだ未達。

2026-10-15追補: 最新の閉じた条件は[context likelihood100M](../reports/phase6/context-likelihood-science-20261015/completion.json)。全80 raw-bound notes・数値監査を含め不採用で、独立学習/fullDEV/新TEST/採用の資格なし。直前のfresh FIMも[不採用閉鎖](../reports/phase6/base-fim-pilot-20261015/completion.json)。どちらも固定条件の係数/親/seed/予算/decoder救済をしない。20261008索引はこの後続比較を含まない検索補助であり、原proposal/trainer/resultとの照合が必要。4項目Base goalはactiveで次の別介入を選定する。以下は文書限定だった時点の履歴。

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

Baseの最新固定不採用は143/144、前回teacher-decayは123。後続Chat136/138/141も不採用。20261008索引は当時の検索補助で、144や後続Chatまでの網羅的な現行監査ではない。今回は索引生成・全corpus scan・旧GPU再評価を実行しない。次案は原proposal/trainer/結果を対応付け、検索語がないことだけで未検証と断定しない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

現在の実状態は `autonomous_status.md` の先頭と、対象jobの実PID/boot/startを確認する。旧計画の「次は…」を、新しい実行指示と解釈しない。

過去の条件を再提案する前に、WSL native repoで `uv run --frozen --extra hub --extra data --extra ml --extra export scripts/index_base_experiments.py --query キーワード` を実行する。例: `larger_material`、`initialization`、`wikipedia`。日時付き索引 `reports/phase6/base_experiment_index_20261008.json` は小さいproposal/completion/review/active_job報告のパス、原SHA、status、閉鎖等のフラグ、要約だけを保存する。

索引は観測時点の検索補助。報告に欠ける量やstatusは推測せず、rawや1MiBを超える報告・全corpus・重みは読み込まない。省略対象はskippedへ列挙する。実行判断時には原報告を参照し、更新済みファイルや稼働中processを再確認する。採点、品質条件、過去の不採用を変更しない。

2026-10-08の参照例: `larger_material_v3_completion.json` はWeb95/story5の500M対2B準備が固定64中11弱>上限10で不採用。`base_gradient_accumulation_pilot_completion.json` は同94.16M教師の勾配蓄積比較が不採用。その後の初期化比較とteacher-decay比較も終了した。最新は結果123の累積2B teacher-decay不採用・一時停止で、次回計画は124。古い索引を最新結果の網羅的な証拠と扱わない。

生成済み索引は同名で上書きしない。新たな結果を集約する場合は日時の異なる後続索引を作り、原報告を保存する。Baseの品質・独立学習seed・fullDEV・protectedTEST・採用が揃うまで未完成。Chat/SFT/量子化はユーザーが再開するまで進めない。
