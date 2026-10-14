# Baseの実験結果を探す

更新: 2026-10-14 JST。最新の判断は[結果141](141_chat_lr_comparison_results.md)と[状態](autonomous_status.md)。Base/Chat未完成・未採用、追加研究・学習は停止中。現在は[全ドキュメント更新142](142_documentation_refresh.md)のみ。 Baseの最新固定不採用は[123](123_base_teacher_decay_2b_results.md)。後続Chatは[136](136_chat_generalization_results.md)→[138](138_chat_semantic_diversity_results.md)→[141](141_chat_lr_comparison_results.md)で閉鎖した。[全文書カタログ](document_catalog.md)と[全体125](125_project_retrospective.md)を入口にし、下の20261008索引を後続Chatまでの最新全件監査と扱わない。文書更新では索引再生成・GPU/data診断を実行しない。

## 当時の資料・保存手順

現在の実状態は `autonomous_status.md` の先頭と、対象jobの実PID/boot/startを確認する。旧計画の「次は…」を、新しい実行指示と解釈しない。

過去の条件を再提案する前に、WSL native repoで `uv run --frozen --extra hub --extra data --extra ml --extra export scripts/index_base_experiments.py --query キーワード` を実行する。例: `larger_material`、`initialization`、`wikipedia`。日時付き索引 `reports/phase6/base_experiment_index_20261008.json` は小さいproposal/completion/review/active_job報告のパス、原SHA、status、閉鎖等のフラグ、要約だけを保存する。

索引は観測時点の検索補助。報告に欠ける量やstatusは推測せず、rawや1MiBを超える報告・全corpus・重みは読み込まない。省略対象はskippedへ列挙する。実行判断時には原報告を参照し、更新済みファイルや稼働中processを再確認する。採点、品質条件、過去の不採用を変更しない。

2026-10-08の参照例: `larger_material_v3_completion.json` はWeb95/story5の500M対2B準備が固定64中11弱>上限10で不採用。`base_gradient_accumulation_pilot_completion.json` は同94.16M教師の勾配蓄積比較が不採用。その後の初期化比較とteacher-decay比較も終了した。最新は結果123の累積2B teacher-decay不採用・一時停止で、次回計画は124。古い索引を最新結果の網羅的な証拠と扱わない。

生成済み索引は同名で上書きしない。新たな結果を集約する場合は日時の異なる後続索引を作り、原報告を保存する。Baseの品質・独立学習seed・fullDEV・protectedTEST・採用が揃うまで未完成。Chat/SFT/量子化はユーザーが再開するまで進めない。
