# 自律runnerの現在の運用

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

## 実行範囲と目標状態を区別する

文書依頼を研究再開と扱わず、古いrunning/PID/next_actionを起動指示にしない。現在の目標は文書/計画の完了。以前の「6まで」は品質未達でblocked、ユーザーが解除済み。今回をその再開・達成としない。

`continue`は許可範囲の有用な作業が残る、`needs_user`は外部操作が必要、`complete`は依頼範囲が証拠で完了した状態。比較作業の完了とBase/Chatの正式採用は別。有資格候補なしの後続は未実行/品質未確認。

有効な長期process/sessionを実identityで確認したpollはverified wait。終了・handle不在が確認されるまで観測timeoutだけでrestartしない。結果の説明や未実行計画だけのturnは進捗ではない。真の同じ外部blockerが3連続goal turnで確認され、許可範囲で有用な作業ができなければgoalをblockedにする。最初のblockで完了/blocked/自主pauseにしない。userが解除・別目標へ変更したら旧確認を繰り返さない。

再開時の契約で一巡/定義済み複数比較と総予算を明記し、範囲内のroutine判断は再確認せず進める。未承認の新cycle、外部公開/送信、有料cloud、OS昇格等の境界は守る。

## 保存と再開

プロジェクトのrunnerは[scripts/run_codex_autonomous.py](../scripts/run_codex_autonomous.py)と[profile installer](../scripts/install_codex_autonomous_profile.ps1)。これらの準備・stub試験は実Codex/GPUの成功証拠ではない。runner/CLIの製品versionや設定は今回確認・変更していない。2026-10-03のCLI0.159.3・権限画面・profile例は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)の歴史資料として保全した。古い「環境から学習まで継続」のpromptを現在の依頼へ適用しない。

長期jobと無人runnerは別機能。再開する実jobがある場合はPID/boot/start・GPU lock・終端result・valid checkpointを照合し、同凍結条件の完了updateから再開する。観測timeoutだけで終了と扱わず同じhandleを確認し、終了したpilot/128/131/133/135/139/143は再起動しない。

Pythonはrunner・tests・one-offを含め`uv run --frozen`、Python3.12.7、通常WSL extras `--extra hub --extra data --extra ml --extra export`。source/data/config・logs・全state・消費カウンタを保存し、GPU診断・学習を文書更新の確認へ追加しない。

今回の文書更新は[全文書カタログ](document_catalog.md)、原byteの保全、現行説明とリンク、Windows/WSL一致、ローカルcommitの証拠で判断する。Git正本はWindows、identityは`yousan <ka1357amnbpdr@gmail.com>`。push/公開は今回の範囲に含まない。

<!-- Original heading aliases retained for historical incoming links. -->
<a id="実行範囲と完了を区別する"></a>
