# 自律runnerの現在の運用

更新: 2026-10-14 JST。[状態](autonomous_status.md)、[AGENTS](../AGENTS.md)、[最新結果141](141_chat_lr_comparison_results.md)を読む。前の3項目の比較・条件分岐・納品は不採用で完了し、現在の目標は[ドキュメント更新142](142_documentation_refresh.md)のみ。研究・data準備・診断・評価・GPU学習は停止中。

## 実行範囲と完了を区別する

権限が利用可能でも、現在の依頼で許可された範囲を越えない。文書依頼を研究の再開として扱わず、古いrunning/PID/next_actionを起動指示にしない。通常判断で許可を繰り返し求める必要はないが、OS昇格・restart・credentials・有料cloud・外部送信/公開等はそれぞれの境界に従う。

`continue`は許可範囲の有用な作業が残る状態、`needs_user`は外部操作が必要、`complete`は依頼範囲を現在の証拠で完了した状態。比較・文書の完了をBase/Chatの正式採用へ読み替えない。条件付き独立確認は有資格候補なしなら未実行・品質未確認と記録する。

## 保存と再開

プロジェクトのrunnerは[scripts/run_codex_autonomous.py](../scripts/run_codex_autonomous.py)と[profile installer](../scripts/install_codex_autonomous_profile.ps1)。これらの準備・stub試験は実Codex/GPUの成功証拠ではない。runner/CLIの製品versionや設定は今回確認・変更していない。2026-10-03のCLI0.159.3・権限画面・profile例は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)の歴史資料として保全した。古い「環境から学習まで継続」のpromptを現在の依頼へ適用しない。

長期jobと無人runnerは別機能。再開する実jobがある場合はPID/boot/start・GPU lock・終端result・valid checkpointを照合し、同凍結条件の完了updateから再開する。観測timeoutだけで終了と扱わず同じhandleを確認し、終了したpilot/128/131/133/135/139は再起動しない。

Pythonはrunner・tests・one-offを含め`uv run --frozen`、Python3.12.7、通常WSL extras `--extra hub --extra data --extra ml --extra export`。source/data/config・logs・全state・消費カウンタを保存し、GPU診断・学習を文書更新の確認へ追加しない。

今回の文書更新は[全文書カタログ](document_catalog.md)、原byteの保全、現行説明とリンク、Windows/WSL一致、ローカルcommitの証拠で判断する。Git正本はWindows、identityは`yousan <ka1357amnbpdr@gmail.com>`。push/公開は今回の範囲に含まない。
