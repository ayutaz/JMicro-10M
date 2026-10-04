# Phase 6以降に残る作業

最終更新: 2026-10-04。実際の現在地は[status](autonomous_status.md)、今回の数値・採否条件は[直接10B計画](39_learning_scale_and_generation_plan.md)を正とする。以前の500M、2Bデータ拡張、7.5B案と当時の指示は[履歴](autonomous_history_20261004.md)へ保存した。

## 完了した範囲

Phase 0〜5、Phase 6①〜⑤、主要Webの総5,000,003,584 tokens学習、同じ5B親からWeb100%と短文20%を各100,007,936 tokens追加する比較を完了した。各仕上げモデルの累積は5,100,011,520 tokens。モデルは10,001,152 parametersであり、Bは学習tokensを表す。

準備済みtrainは12,225,819,077 tokens。builder/raw再構成/実loaderで利用を確認したが、独立全corpus監査は未完了のまま記録する。新規取得や全件再照合を10B学習の前提にしない。

[10B専用準備](40_base_10b_preparation.md)は完了。関連14 CPU tests、stable/decayの実CUDA連続対保存再開16更新、保存review26 checksが成功した。これは準備の証拠であり、ユーザー指定step2の科学学習とCPU保存確認19項目も完了した。[本学習結果](41_base_10b_training.md)。再開された同条件品質評価も完了。[品質結果](42_base_10b_quality_evaluation.md)。

## 直接10Bの学習・品質評価の完了状況

1. 実行設定の準備は完了。既存process、GPU lock、runとcheckpointを読み取り確認して二重起動を避ける。
2. 保存済みstable4.75B親から専用設定で9.5Bまで継続し、独立decayで総10,000,007,168 tokensへ到達済み。追加科学学習は5,249,990,656 tokens。7.5B専用decay・評価は省く。
3. 新10Bだけ同じ全文devと固定400生成で評価し、元5Bおよび最良Web5.1Bの保存評価と比較する。専用品質比較入口を実装し、同条件dev/400と全固定80・自然停止9件の内容確認を完了。CPU評価確認23項目成功。学習完了CPU reviewはscripts/review_base_10b_training.pyに実装し、実行中jobを完了扱いしないguardを確認済み。実際の終端保存stateと全科学metricsへ適用し、19項目成功した。
4. BPB、EOS、反復、raw Unicode、内容の誤り、学習量とGPU時間を報告してcommitし、停止する。到達tokensとBase品質達成を別に判定する。

中断復旧用コマンド履歴はWSL project rootで `bash scripts/run_base_10b.sh --train`。引数なし/`--verify-only`は準備確認で、科学学習を開始しない。今回のstep2学習と保存結果確認は完了し、report/commitで停止する。完了runを再起動しない。ユーザーが再開したstep3の全文/生成品質評価も完了し、追加学習は開始しない。

科学学習GPU上限9,000秒（準備検証19.217秒を含む）、評価予約1,800秒、合計10,800秒。学習区間約126分、評価込み145〜165分の見積もりで、実装・内容確認は別。[専用設定](../configs/phase6/base_10b.json)を変更せず、通常resumeで終端budgetを変更しない。

## EOS・反復・UTF8の後続候補

短文20%は固定EOS 0→13/80、反復57→51/80へ改善したが、全400 raw Unicode失敗2件で最終採用不合格だった。表示helperは採用済みで、raw失敗を成功に数えない。[比較結果](38_eos_5b_finish_results.md)

10Bが本文BPB改善と元の安全条件を満たした場合だけ、新10B親からWeb/短文20%を各100Mで一対比較する候補がある。完了済み5B比較を繰り返さず、比率/LR sweepを先行しない。UTF8制約付き推論は別条件として未実装で、元方式と同じ400生成・上限・seedで比較する。詳細は[計画](39_learning_scale_and_generation_plan.md)。これらは10B結果報告後の判断対象であり、今回の文書更新で開始しない。

## Base品質からChat・量子化へ

本文BPB改善だけで文法・意味・自然停止の合格とはしない。独立人手blind採点、保護test、Chat品質、新しい重みの量子化品質は未実施。[roadmapの品質目標](15_project_roadmap.md#品質目標と判断ルール)を維持する。

Baseの短文生成が成立したらDialogue mid-trainingとAssistant本文＋EOTだけを教師にするSFTを実装し、効果を分けて比較する。Chat trainerは未実装。Chat後に量子化・実容量・CPU速度・独立環境での品質を検証する。既存のNoNorm CPU精度profileの変換成功を、未評価の新重みの配布品質へ流用しない。

## 20B・50Bと追加研究

20B/50Bは現在の実行範囲に含めない。StableExtensionTrainerの明示forkは実装済みだが、新しい予算・data・履歴・再開検証を固定してから使う。50Bは20BのBPB改善差の95%信頼区間下限が0を超え、重大な生成退行がなく、実測追加予算内の場合だけ候補にする。

Tokenizer再学習、Muon、unlikelihood、architecture sweep、クラウド比較は先行しない。追加研究は比較対象・予算・終了条件を定め、有料クラウド、公開、他者への連絡には個別の指示が必要。Pythonはすべてuv、WSL/Linux data、checkpointと失敗証拠を保持し、local commitを行う。自動pushはしない。
