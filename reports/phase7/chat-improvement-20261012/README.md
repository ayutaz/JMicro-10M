# 計画131・教材改善比較の証拠

ユーザーの段階0–5再開で実行した限定比較。実際の状態は[記録132](../../../docs/132_chat_improvement_execution.md)と[status](../../../docs/autonomous_status.md)を先に参照する。全14suite・3,066内容判断、共通NLL7点と両条件の最終学習state監査を完了。最終候補はなく、不合格で閉鎖。Base/Chatは未完成・未採用。

- [実行config](../../../configs/phase7/chat-improvement-20261012.json): 元10B親、Tokenizer、native10,001,152 parameters、各1,899,555教師、同一の教師量schedule、6時間GPU上限、18sourceを凍結。
- [教材準備](train_preparation.json)、[全280sample確認](train_content_review_final.json)、[元挨拶対確認](natural_source_content_review.json): 自作教材を中心としたrecipe。全TRAINの独立人間認証ではない。
- [新DEV準備](dev_preparation.json)、[DEV監査](dev_audit.json)、[NLL準備](nll_preparation.json): TRAIN凍結後に作成。新80family、自己生成24会話59応答、固定NLL2554target。TESTを使わない。
- [消費量dry-run](consumption_dry_run.json)、[実family量](actual_family_consumption.json): CPUの数量/順序/長さ確認。学習・品質の証拠ではない。
- [native CUDA probe](native_probe.json)、[全state再開gate](native_resume_gate.json): full nativeで有限BF16と連続/保存再開の完全一致を確認。技術成立を品質成立へ読み替えない。
- [不合格の初期評価見積もり](evaluation_forecast_failed_cold_per_response.json)、[事前の測定方式修正](forecast_method_revision.json)、[再見積もり](evaluation_forecast.json): 初回初期化を各応答に掛けた過大推計を本学習前に分離計測。件数・係数・上限・gateは維持。
- [親/旧DEVの再利用](parent_old_reuse.json)、[binding正規化](parent_reuse_binding_normalization.json)、[停止・修正の記録](incidents.json): 再利用の来歴と元版を保持。新しい独立GPU評価として数えない。
- [中間の全レビュー監査](intermediate_review_audit.json)、[両条件の中間比較](intermediate_screen.json)、[続行判断](intermediate_decision.json)、[採点済み内容の再集計](intermediate_analysis.json): B/3時点は全screen不合格。最終予算での成功は未確認。
- [教材構造の静的確認](curriculum_structure_inspection.json): gold前置き、最後のtargetだけの教師、共通説明文型と失敗との関係。原因を確定した単一要因比較ではない。

`evaluation/{arm}/{point}/{new|old}/greedy/`にはraw result、全219のnotes/review、手動authored.tsv、実履歴・IDs・bytesに結び付けたpacketを保持する。抑制/無抑制や別保存点の完全一致だけを、来歴付きで採点再利用する。新旧suite、保存点、同じ24familyの複数turnを独立標本として合算しない。

`NLL/{arm}/{point}.json`には同じ2554targetの本文/EOT損失と本文bytesを保持する。比較は同じ文章ごとに行い、教材源間のlossの大小で品質を順位付けしない。

学習済み全state/checkpointとデータセットはWSL/data環境に残し、Gitには入れない。[最終state C0](C0/training_audit.json)・[C1](C1/training_audit.json)、[最終採否](selection.json)、[全点再集計](final_analysis.json)、[完了監査](completion.json)、[Git bytes照合](final_git_verification.json)で根拠を追える。合格候補なしのため保持/samplingは省略・未確認。GPU累積4,247.635852秒（70.794分）/6時間。元UIは実process/HTTPで再確認。次は[未実行計画133](../../../docs/133_chat_generalization_followup_plan.md)で、追加実験は明示再開待ち。C2回復、効率、独立学習seed43、人間blind、fullDEV、protectedTEST、採用、量子化、公開へ自動移行しない。
