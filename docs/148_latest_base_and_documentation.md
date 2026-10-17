# 最新Base結果と全文書更新（2026-10-17）

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 第一回RDrop科学比較の結果

元10B親/fresh AdamW、同native10,001,152、同TRAIN/25M主教師/batch48/seed42、平均二view CE＋.5×対称KL。dropout.1はembedding/attention-output/MLP-outputの学習時のみ。4,420更新、hardgold CE評価50M、consistency pairs25M。追加unique教材50Mではない。推論モデル/decoderは元native。

| 指標（80件） | nativeCE25M対照 | RDrop25M | 元絶対条件 |
|---|---:|---:|---:|
| 文法2 | 44 | 47 | ≥56 |
| 一貫性2 | 1 | 3 | ≥27 |
| 適切な完結 | 3 | 6 | ≥27 |
| EOS | 11 | 19 | ≥37 |
| 規定反復 | 53 | 49 | ≤18 |

BPB0.9927168290617072→1.0279654060355414、3.5507181848775993%悪化。対応一貫性差+2/80・CI95[0,.0625]は+8/下限>0未達。全5絶対品質/停止/反復gateと元保持guardに不合格。empty/role/Unicode等0だけでは合格しない。

全80のraw/個別理由、全4,420履歴/型付き全stateを確認。元主streamは対照一致。二viewのphysical streamは倍で、dropoutのため学習torch RNGは対照と意図的に異なる。腕内保存再開のRNGを含む全state一致を維持した。Codex非blindであり独立人間blindではない。KL単独の因果効果や全RDrop/10Mの不可能を示す結果ではない。

固定条件は不採用で閉鎖。係数/dropout/教師/親/seed/decoder/品質閾値を後から変更して救済しない。意味の循環、因果/数量誤りが残る。

## 資源と保存

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

今回の科学GPU777.297899876954秒。継承台帳は技術169.2456279549515＋科学4241.304908989929＝総4410.55053694488秒。これは対象継承台帳の範囲で、全プロジェクトの歴史GPU総計ではない。今回runは実行前にcap1757秒を固定し、その範囲内で終了した。

科学commit cf113068。全weights/Adam/RNG/sampler/metricsはWSL、checkpoint-00004420.pt SHA e9154a2d5b8e385c978e597c8b65d3c73dc882680bbf143422d9acb363aa0c73。18小portable記録の同hash保全は原portable_artifactsを参照する。

RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。

## Base完成までの不足

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

## 今回の全文書更新

更新前976パスの全Git管理Markdown/RSTを棚卸しし、現行34文書を最新化、148を追加した。日付付き/固定履歴284・以前の原文copy658（計942パス）は当時のbytesを保持する。旧本文の内容hash別copyは既存を再利用し、不足36件のみ追加した。今回以前の全文はbaselineのsnapshot列からたどれる。長い追記型の進捗は現行入口から整理し、旧文書中の全見出しanchorも保持する。

[全件カタログ](document_catalog.md) / [更新前baseline](../reports/investigation/documentation-refresh-20261017/baseline.json) / [保存・リンク・同期の検証](../reports/investigation/documentation-refresh-20261017/verification.json) / [Git納品確認](../reports/investigation/documentation-refresh-20261017/commit_verification.json)。検証recordは実チェック後に保存する。

今回の文書更新は学習・推論・GPU・data/TEST・外部公開を実行しない。旧「4まで」の目標は未達のまま解除済み。文書納品をBase/Chat完成にしない。今後の詳細は[計画145](145_post_rejection_next_plan.md)。
