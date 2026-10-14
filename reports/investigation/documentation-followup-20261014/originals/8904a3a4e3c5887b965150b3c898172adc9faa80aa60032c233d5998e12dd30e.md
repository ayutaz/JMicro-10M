# 課題解決計画135の最新記録確認

2026-10-13 JST。[計画135](../../../docs/135_chat_problem_solution_plan.md)の更新に使った既存小記録を保存する。新しい学習・GPU診断・評価・教材生成・checkpoint状態監査は行っていない。

- [観察と出典hash](observations.json): t1中間比較、固定NLL、padding不採用、予定される未確認記録の有無。
- [D1 t2 result](D1_t2_result.json)、[checkpoint一覧](D1_t2_checkpoints.json)、[job記録](D1_t2_job.json): 既存WSL小記録のbyte一致コピー。checkpoint本体を監査・複製したものではない。
- [GPU台帳](GPU_ledger.json): 失敗分を含む既消費の観察時点コピー。予算をリセットしない。
- [launcher終端](D1_t2_launcher_result.json): Windows既存記録のコピー。exit0とUI復帰コマンドexit0は現在のUI生存証拠ではない。
- [文書の検証](verification.json): 出典コピーのhash、原model/config、今回更新した文書のローカルリンクと記載数値を確認する。

既存の採点はCodex非blindであり、独立した人間の評価ではない。t1の指標を最終採否へ読み替えない。Akebonoと指定GitHubの今回のWeb取得は成功せず、前者はアクセス不可、後者は取得時404だった。削除・非公開化の確定ではない。

公開一次資料は[HF Chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating)と[GKD論文](https://arxiv.org/abs/2306.13649v3)。訓練/推論の会話形式の整合と自己生成系列の分布差を考える参考で、本計画の介入効果を実証したものではない。
