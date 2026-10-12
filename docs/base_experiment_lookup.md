# Baseの実験結果を探す

2026-10-13更新: Baseの最新不採用は[123](123_base_teacher_decay_2b_results.md)、後続Chat比較の最終不採用は[136](136_chat_generalization_results.md)。次の教材提案は[135](135_chat_problem_solution_plan.md)、Base復旧の代替経路は[124](124_base_recovery_plan.md)で、現在は文書更新のみ・追加実験停止中。下の20261008索引は当時のBase検索補助で、後続Chatを含む最新全件一覧ではない。

文書更新では保存済み小reportを参照し、下の索引生成commandやGPU/data診断を新たに実行しない。既存の[全体記録125](125_project_retrospective.md)と固定revision詳細台帳、最新status/各completionを用途に応じて区別する。

現在の実状態は `autonomous_status.md` の先頭と、対象jobの実PID/boot/startを確認する。旧計画の「次は…」を、新しい実行指示と解釈しない。

過去の条件を再提案する前に、WSL native repoで `uv run --frozen --extra hub --extra data --extra ml --extra export scripts/index_base_experiments.py --query キーワード` を実行する。例: `larger_material`、`initialization`、`wikipedia`。日時付き索引 `reports/phase6/base_experiment_index_20261008.json` は小さいproposal/completion/review/active_job報告のパス、原SHA、status、閉鎖等のフラグ、要約だけを保存する。

索引は観測時点の検索補助。報告に欠ける量やstatusは推測せず、rawや1MiBを超える報告・全corpus・重みは読み込まない。省略対象はskippedへ列挙する。実行判断時には原報告を参照し、更新済みファイルや稼働中processを再確認する。採点、品質条件、過去の不採用を変更しない。

2026-10-08の参照例: `larger_material_v3_completion.json` はWeb95/story5の500M対2B準備が固定64中11弱>上限10で不採用。`base_gradient_accumulation_pilot_completion.json` は同94.16M教師の勾配蓄積比較が不採用。その後の初期化比較とteacher-decay比較も終了した。最新は結果123の累積2B teacher-decay不採用・一時停止で、次回計画は124。古い索引を最新結果の網羅的な証拠と扱わない。

生成済み索引は同名で上書きしない。新たな結果を集約する場合は日時の異なる後続索引を作り、原報告を保存する。Baseの品質・独立学習seed・fullDEV・protectedTEST・採用が揃うまで未完成。Chat/SFT/量子化はユーザーが再開するまで進めない。
