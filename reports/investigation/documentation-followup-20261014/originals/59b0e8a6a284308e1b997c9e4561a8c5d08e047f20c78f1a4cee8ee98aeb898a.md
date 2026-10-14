# 現在の状態

2026-10-14 現行: [結果141](141_chat_lr_comparison_results.md)の低学習率比較は全28セット・6,132判断・NLL7点・全3保存状態・採否・予算と条件分岐の科学監査を完了し、不合格・不採用。S1最終内容20/18/19/15 of80、自己文脈5/5/5/1 of24、新内容差+8.75ポイント（95%CI −1.25〜+18.75）、反復退行と新自己生成Unicode失敗1。独立確認の全7分岐は候補なしで未実行・passed=false・品質未確認。Base/Chat未完成・未採用。文書・保全・ローカル納品はfinal_archive/final_delivery_checksで別に証明する。納品の最終commit照合までgoal完了を宣言せず、それを終えて停止する。追加GPU・教材準備・新条件は停止。今回GPU2,658.673158秒/33,600秒。科学監査2026-10-13T16:54:20Zの元UI PID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、HTTP親/Tokenizer/10M・busy=false・kernel lock一致。以下は再開時から途中までの履歴で、未完了数やPIDは現在の指示ではない。

2026-10-14 明示再開: goal「3まで進めてください」は直前回答の介入1件選定→10M/原品質で比較→有望条件だけ独立確認を再開する。[計画139](139_chat_lr_comparison_plan.md)。SFTのpeak LR1e-4→3e-5だけを変更し、同TRAIN/同親/教師量、新DEV＋既知3回帰を登録する。Base/Chat未採用、旧135の完了と不採用を保持。以下の停止状態は今回再開前の履歴。

最新実績（2026-10-14 JST）: [139](139_chat_lr_comparison_plan.md)/[実行140](140_chat_lr_comparison_execution.md)でLR3e-5候補のCUDA25検証更新と全評価予測10,732.271秒/14,400秒が通過。本学習をdurable workerで開始し、15:43:54Zに実PID304617/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start54912399の生存と600更新/312,871教師を観測。全レビューは13/28セット・2,847/6,132判断・NLL1/7点。元親新DEVは全219理由付き判断を確認。最終採否・3段階の完了は未確認。準備時の元Chat TEST20行解析事故は保存・訂正済みで、有資格時は新しい封印Chat TESTが必要。

保存点監査追記: t1=1,215更新/633,206教師、t2=2,430更新/1,266,627教師の実入力/教師digest・LR列・全stateを確認して通過。15:57:11Zに同学習PID304617の実生存と2,500更新/1,303,091教師を観測。生成品質は未確認、t3/残15suite/NLL6点/採否・分岐・納品を継続する。

最終更新: 2026-10-13 JST。**計画135の6段階を実行・監査し、教材候補S1を不合格・不採用で閉鎖した。Base/Chatは未完成・未採用。追加研究・教材準備・GPU診断・生成評価・学習は停止する。**

[最終結果138](138_chat_semantic_diversity_results.md)、[科学的完了監査](../reports/phase7/chat-semantic-diversity-20261013/completion.json)、[現行計画135](135_chat_problem_solution_plan.md)を先に読む。[実行137](137_chat_semantic_diversity_execution.md)は時点別履歴で、途中の「継続中」やPIDを再開指示に使わない。128/131/133/今回135の終了jobを再起動しない。

## 最新の実績と採否

| 項目 | 実際の証拠 |
|---|---|
| モデル | native10,001,152 parameters、context1024、Tokenizer4096。9.5M〜10.1M制約を維持 |
| S0対照 | 最新D1の同親/seed/教師量/schedule/全stateを照合した歴史3checkpoint。新学習0 |
| S1教材 | TRAIN41,529 target、660,109教師/周、280sample QA最終誤り0。独立人間/全TRAIN認証ではない |
| S1実学習 | 3,646更新・1,899,557 Assistant本文+EOT教師。登録Bを2超過し許容0〜64内。3保存点全state/実消費列監査通過 |
| 全評価 | 21セット・4,599理由付き内容判断、共通固定NLL7点×2,554 targetを監査。既知8セット1,752判断は出典付き再利用 |
| 技術確認 | CUDA probe9更新＋連続/保存再開16更新。検証25更新を本学習や品質証拠へ数えない |
| 最終採否 | S0/S1とも原品質gate未達。S1の未知内容改善CI下限も負。候補なし、不採用で閉鎖 |
| 分岐 | 保持/samplingは候補なしで未実行・passed=false・品質未確認。回復/効率は範囲外 |
| 今回GPU | 2,443.006571秒（40.717分）/21,600秒。S0過去学習/全研究の累計ではない |
| 保存 | 重み・samplerを含む全state・教材はWSL。小report/raw/全notes/config/実装/文書はローカルGit。自動push/公開なし |

| 最終品質 | S0 新 | S1 新 | S0 前回 | S1 前回 | S0 元旧 | S1 元旧 | 原条件 |
|---|---:|---:|---:|---:|---:|---:|---|
| 内容 /80 | 16 | 19 | 12 | 21 | 15 | 11 | 各56以上 |
| 自己生成文脈 /24 | 3 | 3 | 3 | 6 | 1 | 1 | 各15以上 |

主指標のS1−S0差は新+3.75ポイント、95%CI −8.75〜+16.25。前回DEVの差は正のCIだが、主指標/全回帰合格を代用しない。最終S1新の文法2は63/80、そのうち44件は関連性2未満。新自己生成反復0→1、元旧固定反復1→5、元旧Unicode失敗0→1も残る。原rawを修正・制約decodeして成功にしない。

固定S1 TRAIN本文NLLは親2.841439→0.008183、新DEVは2.664694→3.272796、RPC DEV BPBは1.351262→1.875353。教材適合と未知内容の汎化の隔たりを確認したが、全TRAIN暗記・Base単独原因・10M容量限界は未確定。RPCのChat形式BPBは正式Base保持を代用しない。

## 完了と未確認

ユーザーの「6まで進めてください」は1候補の比較→QA/凍結→新DEV＋既知2回帰→技術/予算gateと学習→全評価/条件付き保持→報告・停止の範囲で完了した。モデル完成・採用の完了ではない。[納品確認](../reports/phase7/chat-semantic-diversity-20261013/final_delivery_checks.json)。

内容判断はCodex非blind、QAは標本、対照は歴史state。独立学習seed43、人間blind、独立corpus監査、fullDEV/全400生成＋長文40/最終継続suite、選定封印後のprotectedTEST、正式Base/Chat採用は未確認。CPU準備や3生成seedで代用しない。

次の研究条件・追加教材・診断・学習は明示再開待ち。[135](135_chat_problem_solution_plan.md)末尾は提案のみで、新しい実行契約ではない。Base復旧を選ぶ場合は[124](124_base_recovery_plan.md)の固定品質とBase完成で通知・停止の境界を維持する。

## process・UIと保全

最終科学監査2026-10-13T09:44:20Zに元[WebUI](http://127.0.0.1:7860)の実PID292581/boot `4052bfc5-3850-44e4-9123-d34a9e19f36e`/start_ticks52504723、HTTP親/Tokenizer/10M一致、busy=false、kernel GPU lock一致、競合jobなしを確認した。これは当時の観測で、現在/将来の生存保証ではない。終了済みのpilot・学習・評価を再起動しない。[引継ぎ](windows_handoff.md)。

S1最終checkpointはWSL `reports/phase7/chat-semantic-diversity-20261013/S1/checkpoint-00003646.pt`、SHA `6ca25064fa4ccb6784a05fa5ade43bfdaa87aeb55f11458a233eaf32664fd2ea`。[保存一覧](../reports/phase7/chat-semantic-diversity-20261013/final_archive.json)。Git正本はWindows。最新納品commitは `git log -1`、内容保存commitは納品確認を参照する。

## 過去の結果・公開履歴

[前回136](136_chat_generalization_results.md)は全14suite/3,066判断/NLL7点・D1 3,641更新/1,899,562教師を完了し不採用。動的padding24検証更新も固定との数値差で不採用。今回と別runの証拠として保持する。

Base teacher-decay2BはBPB1.106386→1.090316でも一貫性3→3、適切完結7→5、反復27→27、Unicode0→1（各80）で不採用。[結果123](123_base_teacher_decay_2b_results.md)。元UI10B・別staged約10.6B・teacher-decay2B・後続SFTは別系列で、学習量を合算しない。

2026-10-09の[公開保存版126](126_model_archive.md)は主要3系列のpublic/manual gated保存。datasetとsamplerは除外し、厳密再開の代替ではない。後続Chat重みは公開していない。当時のGitHub push許可は当時の納品に限る。

更新前の全運用文書は[今回の履歴baseline](../reports/phase7/chat-semantic-diversity-20261013/documentation_history/baseline.json)、以前の全体経緯は[125](125_project_retrospective.md)と[詳細台帳](retrospective/README.md)に保全した。
