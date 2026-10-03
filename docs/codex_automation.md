# Codexによる環境整備・学習・改善の自動化

確認日: 2026-10-03。現在はFull accessが実効policyへ反映済みで、ユーザー側のrunner起動は不要。停止指定はrunnerを起動しても維持し、Phase 5を始めるにはユーザーの再開指定が必要。CLI 0.159.3の実helpとOpenAI公式資料を照合した。

ユーザー指定（2026-10-02）: 本プロジェクトの環境整備・実装・学習・評価・改善をCodexに継続して任せる。作業内容と実測結果は`autonomous_status.md`、方針はrootの`AGENTS.md`へ残す。2026-10-03にPhase 4の学習pipelineと実GPU検証が完了した。ユーザーの追加指定によりPhase 4で停止し、Phase 5は再開待ち。

## このアプリで続ける

初回にモードが表示されない場合はSettings → General → Permissionsで有効化し、その後に入力欄下の権限メニューで選択する。[公式のモード選択](https://learn.chatgpt.com/docs/permission-modes)。入力欄下に選択肢がある場合は**Full access**へ変更する。公式の対応設定は`approval_policy = "never"`と`sandbox_mode = "danger-full-access"`。[OpenAI公式の権限説明](https://learn.chatgpt.com/docs/sandboxing)

Workのnetwork設定が提供されている場合は、Settings → Data controls → Work network accessでAllow public internet accessを有効にする。管理対象の環境で選択肢が無効な場合は管理者側のpolicy変更が必要。ユーザー設定は管理policyを上書きできない。変更が反映された実行環境で続きを進める。

当初の制限された会話ではグローバル設定を変更できなかった。2026-10-03にユーザーのFull access選択が実効policyへ反映され、会話内からWSL・network・CUDAにアクセスできた。グローバルconfigは変更していない。project内の設定fileは実行中セッションの権限を変更しない。

## CLIのプロジェクト用profile

通常のPowerShellでproject rootから実行:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_codex_autonomous_profile.ps1
codex --profile jmicro_autonomous --cd . "AGENTS.mdとdocs/autonomous_status.mdに従い、環境整備から学習・評価・改善まで継続してください"
```

installerは既存グローバルconfigを変更せず、`$CODEX_HOME/jmicro_autonomous.config.toml`（未指定時は`%USERPROFILE%\.codex\`）へproject専用profileを作成する。同名profileが異なる場合はbackupを残す。今回確認したCLI 0.159.3の`--profile`は`<name>.config.toml`を重ねる仕様。既存のmodel選択・ログインを引き継ぐ。実際のCLI helpと[公式設定説明](https://learn.chatgpt.com/docs/config-file/config-reference)を再開時にも確認する。

CLIの設定はアプリの既存会話を変更しない。管理policyやWindowsの管理者権限を回避するものでもない。WSL導入/driver更新のOS側昇格、再起動、Linux初回ユーザー作成、初回ログインは外部操作として残る場合がある。

## 無人の継続runner

Codex CLIと保存済みログインを利用する。通常端末で:

```powershell
uv run --frozen scripts/run_codex_autonomous.py --max-turns 20
```

WSL内でCLIを利用できる場合はLinuxコピーで:

```sh
uv run --frozen scripts/run_codex_autonomous.py --max-turns 20
```

runnerはprofileのinstallなしでも、起動するCodexに`approval_policy=never`と`danger-full-access`を指定する。制限された会話から権限拡張用に起動する手段には使わない。Full accessが反映された環境または通常端末から実行する。表示だけの確認は`--dry-run`。

各回のCodexが実装・学習・検証を行い、`continue`なら次の回を開始する。`complete`、外部操作が必要な`needs_user`、CLIエラー、20回の起動上限で終了する。上限終了はproject完了を意味しない。無制限retryや無制限の改善探索は行わず、同じcommandで状態fileから続けられる。1回の作業時間やCodex accountの利用上限はrunnerが解除できない。[公式non-interactive実行](https://learn.chatgpt.com/docs/non-interactive-mode)

`reports/automation/<UTC-id>/`に各回のprompt、JSONL events、stderr、最終JSON、最新resultを保存する。exit codeは0=要求達成、2=runner/CLIエラー、3=外部操作待ち、4=起動回数上限。`runner.lock`で二重runnerを防ぐ。強制終了後にlockが残った場合は記録されたPIDの終了を確認してから除去する。学習jobの二重起動はagentがcheckpoint/run記録とPIDを確認して避ける。

コードの継続runnerと、長時間GPU学習のcheckpoint/監視/再開は別の機能。GPU側はPhase 4で排他lock、PID/boot ID/start ticks、stage/run記録、atomic checkpointとhashを実装し、hiddenのWindows `wsl.exe` supervisorで検証jobを保持した。スリープ・再起動・ログイン切れで永続実行は保証せず、中断時はcompleted-update checkpointから再開する。

Pythonの実行はrunner・テスト・一時スクリプトを含め`uv run --frozen`経由に統一する。Python 3.12.7が未導入なら`uv python install 3.12.7`で導入し、依存は`uv sync --frozen`で復元する。固定環境を取得できない場合はblockerを記録し、system Pythonへ切り替えない。

## 実施した検証

`uv run --frozen python -m unittest discover -s tests -p test_codex_automation.py -v`で再実行できる5件のstubテストが成功。実Codexを呼ばないローカルstub subprocessで、継続結果の引継ぎ、終了条件、CLI失敗時の診断、二重起動防止を確認した。dry-run/profile previewと各fileの構文も確認。このstub結果だけでは実Codex/GPU成功を証明しない。後続のPhase 4では全64 tests / skip 0と実GPU学習・保存再開・評価・容量測定を完了した。[実機証拠](21_phase4_completion.md)。

初回stub検証はuv統一前の履歴。現在の再実行は`uv run --frozen python -m unittest discover -s tests -p test_codex_automation.py -v`を使う。
