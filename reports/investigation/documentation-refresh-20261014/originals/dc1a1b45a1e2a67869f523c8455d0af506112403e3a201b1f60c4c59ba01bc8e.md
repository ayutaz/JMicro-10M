# 2026-10-03 環境復旧・Phase 4実装の履歴

この文書は途中経過を保存した履歴。権限・driver・未実装・次の作業の記述は各観測時点の状態で、現在の指示ではない。[現在の状態](autonomous_status.md)と[Phase 4完了記録](21_phase4_completion.md)を優先する。過去reportとsnapshotは変更しない。

以下は復旧・実装途中の履歴:

01:13〜01:25の会話内実測（2026-10-03 01:13〜01:25 JST。以下の旧blocker記録より優先）:

- ユーザーのFull access変更が実効policy `danger-full-access` / `never` / network enabledへ反映され、WSL一覧・Ubuntu起動・Linux GPU操作が成功。権限制御blockerは解消。
- 既存Linuxコピーを上書きせずsetupを再開。公開25 filesのhash検証成功（再復元0）、Python 3.12.7 / uv 0.9.0、PyTorch 2.14.1 / CUDA 13.0、RTX 4090 / Windows driver 616.92を確認。CUDA/BF16 tensor forward/backward finite。53 tests / skip 0と入力付きprepare→verify成功。Windowsにも`reports/phase4/environment.json` / `environment_tests.xml`をコピーした。
- `src/jmicro/shards.py` / `training.py`、`scripts/train.py`、training run schemaを実装。BaseのWebのみを明示してuint16 shard化し、train 18,022 docs / 6,884,183 stream tokens / 32,774,150 body bytes、dev 924 docs、test 1,052 docsを分離。会話/sharealikeはこのBase系列へ混ぜていない。
- shard hash/境界、epochをまたぐsampler再開、本文一度採点・共通bytes・EOS分離、loss正規化、評価RNG保全、保存再開について新規11 tests成功。既存53件とは別の追加検証。
- 実shard・context 1024・micro batch 2・FP32 parameters/BF16 autocastで連続200と100+100を実GPU比較。消費列digest、loss、全weightsが完全一致（最大差0）。各系列409,600 tokens。証拠: Linux `reports/phase4/resume-bf16-20261003/resume_report.json`。これはPhase 4検証runで、Base/Chat品質達成や長期本学習ではない。
- ユーザー指定のGit local identity `yousan <ka1357amnbpdr@gmail.com>`をWindows/WSL両方へ設定。意味のある検証済み変更を適度にコミットし、pushはしない。
- 次は評価CLIの実GPU結果、T4K shard、最大安定batch・backend/compile・synthetic/実shardの比較を実施する。最大batch・Phase 4全gate・Phase 5は未達。

00:37の外部runnerによる復元結果（2026-10-03 00:37 JSTの`reports/phase4/environment_recovery_20261003.json`を根拠とし、以下の旧観測より優先）:

- 通常端末からのrunnerではWSL 3.0.1.0、Ubuntu/WSL 2、Linux user `aihub_ubuntu`、Linuxコピー`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`を復元した。
- LinuxのPython 3.12.7/uv、固定Tokenizer/pilotを復元し、25 filesの検証・16 filesのLinux復元、関連CPU tests 39件/skip 0が成功。Windows側でも公開Tokenizer・corpusの配置を確認した。
- 00:37時点のWindows driverは552.12だったが、その後ユーザーが更新を実施。今回の`nvidia-smi`でRTX 4090、driver **616.92**、24,564 MiBを観測し、固定CUDA 13依存の580以上条件を満たした。driver互換条件のblockerは解消済み。CUDA/BF16・GPU学習・速度は引き続き未検証、本学習tokensは0。
- 更新後も、この会話は`workspace-write` / `approval_policy=never` / network restricted。WSL version 3.0.1.0は取得できるが、一覧・状態は`Wsl/EnumerateDistros/Service/E_ACCESSDENIED`。証拠は`reports/phase4/driver_update_recheck_20261003.json`。通常端末からのrunner再開が必要で、この会話から権限拡張runnerは起動しない。Windows上にPython/uv/WSLの実行プロセスとrunner lockを観測しなかったが、Linux側ジョブはアクセス不可のため確認できていない。
- ユーザー依頼でdriver更新と学習速度を公式資料から調査。`reports/phase4/driver_performance_research_20261003.json`に根拠・推奨・未実施の比較条件を保存。長期学習にはCUDA 13対応driverへの更新を推奨するが、driver単体の速度向上率は不明。552.12＋CUDA 12.4へのuv依存変更も候補で、古い構成でも`torch.compile`自体は利用できる。新旧構成ともGPU実測前に高速・安定と確定しない。

以前の会話内確認・準備の記録:

- Phase 0〜3完了はiMac上の記録。本学習tokensは0。Phase 4のtrainer/shards/評価runner/checkpoint再開は未実装。
- Windows作業root: `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。
- RTX 4090 24,564 MiB、NVIDIA driver 552.12、WSLパッケージ2.6.1.0を観測。公式latestで3.0.1を確認。
- 現セッションはworkspace-write、approval_policy=never、外部network制限。WSL一覧/起動はアクセス拒否、更新は接続不可、Hub/Python取得はsocketアクセス拒否。
- ユーザーはFull accessへ切替済みと報告。報告後の2026-10-03 00:01:57 JSTにもWSL一覧は`E_ACCESSDENIED`、Hugging Face接続は`WinError 10013`。この会話の実行環境では依然アクセス不可。証拠は`reports/phase4/full_access_recheck.json`。再度許可を求めず、実効権限が変わった会話/通常CLIから再開する。
- 今回の継続依頼後、2026-10-03 00:04:50 JSTにも再確認。実効policyは`workspace-write` / `approval_policy=never` / network restricted。`wsl --list --verbose`は`Wsl/EnumerateDistros/Service/E_ACCESSDENIED`、固定Hub commitの`artifact_manifest.json`取得は`WinError 10013`。WSL 2.6.1.0、RTX 4090、driver 552.12は変わらず、両Tokenizer・corpus・Parquet manifestは未配置。証拠は`reports/phase4/session_preflight_20261003.json`。同じ取得・更新の再試行や制限下からの権限拡張runner起動は行わず、外部操作待ち（`needs_user`）で停止した。
- 公開Tokenizer/pilotはまだローカルへ復元していない。Python 3.12.7/仮想環境も未構築。
- 固定Linux依存のCUDA runtimeは13.0.96。Windows driver 552.12はCUDA 13系の580以上条件を満たさない。
- 実測の証拠: `reports/phase4/windows_preflight.json`、`reports/phase4/wsl_setup.json`。これらはGit管理外。
- `setup_windows_wsl.ps1`と`setup_wsl_environment.sh`を用意し、構文とWindows確認モードを実行済み。Linuxセットアップは未実行。
- Codex CLI 0.159.3を確認。既存ユーザー設定はapproval_policy=neverで、sandbox_modeは未指定。プロジェクトはtrusted。グローバル設定は変更していない。
- 自律起動設定、profile installer、継続runnerを追加。権限を拡張したCodex起動と実学習はまだ実行していない。
- 継続runnerのstub subprocessによる5テストが成功（継続→完了、外部操作待ち、起動上限、CLI失敗、二重runner防止）。dry-run、profile preview、Python/TOML/JSON/PowerShell構文も確認。実Codex/GPU実行の成功を意味しない。追加分を含む全ML suiteは環境復元後に実行する。
- uv統一ルールに合わせ、README・自律runner手順/継続prompt・再開commandを更新し、WSL setupのdriver確認を`uv run --frozen --extra hub --extra data python`へ変更。system Pythonの存在確認/apt導入は不要になったため除去した。Git Bashの`bash -n`、直接Python呼出し・再開commandの静的確認、`git diff --check`は成功。`uv --cache-dir reports/local/uv-cache run --frozen --offline --no-python-downloads python -m unittest discover -s tests -p test_codex_automation.py -v`はPython 3.12.7未導入で起動前に停止し、今回テストは未実行。既存cacheは書込権限外なので確認用cacheをproject内へ指定した。固定Pythonを取得できる環境で`uv python install 3.12.7`、`uv sync --frozen`を実行してから上記testを再実行する。system Pythonへの代替は行っていない。
