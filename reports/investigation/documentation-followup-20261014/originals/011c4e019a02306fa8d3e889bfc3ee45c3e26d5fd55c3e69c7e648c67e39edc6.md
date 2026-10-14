# 直接10B学習の実行準備完了

2026-10-04。ユーザー指定のstep1「10B用の実行設定を準備し、保存再開とGPU動作を確認する」を完了した。**専用config/schema/起動処理を凍結し、関連14testsと実RTX4090での保存再開一致を確認した。本学習は未開始。** [保存証拠26項目](../reports/phase6/base_10b_preparation_review.json)、[完了証拠](../reports/phase6/base_10b_preparation_completion_audit.json)、[次回計画](39_learning_scale_and_generation_plan.md)。検証の成功は10B学習完了や品質改善の証拠ではない。

## 実行設定

`configs/phase6/base_10b.json`と対応するconst schema、`scripts/run_base_10b.py`、`scripts/run_base_10b.sh`、準備結果のCPU reviewerを追加した。既存のcore/model/shards/lock/Tokenizer、stable-extension、旧5B runnerは変更せず、凍結した保存再開・学習処理を再利用する。

| 項目 | 設定 |
|---|---|
| 親 | 保存stable4.75B / update144959 |
| 親SHA | 916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5 |
| stable終端 | 9,500,000,256 tokens / update289917 |
| 最終decay | 15,259 updates、LR0.002から0.0002 |
| 最終到達点 | 10,000,007,168 tokens / update305176 |
| 予定追加科学学習 | 5,249,990,656 tokens |
| データ | 既存train12,225,819,077 tokens、Web100%、epoch0内 |
| 計算 | uv Python3.12.7、WSL2/RTX4090、batch32/context1024/BF16/Flash/compile |
| 予算 | 科学学習と準備検証の累積GPU9,000秒、別評価予約1,800秒 |
| 保存 | 1,000更新ごと＋区間終端、optimizer/scheduler/RNG/cursor/counterを保持 |

減衰済みfinal5B/5.1Bを通常resumeして予算やLRを変えず、stable親からの明示forkとして継続する。7.5Bの専用decay・中間全文評価は省く。旧final5BとWeb/短文5.1B重みは保持する。出力はLinux `reports/phase6/base-10b-20261004/`、科学checkpointは将来の同run/stable・decay配下。空き約545GB、必要最低空き200GiB、予定checkpoint容量約20.4GB、run出力上限32GiBの設定で十分な余裕がある。全コーパスの再抽出・重複照合・再監査は行っていない。

## 保存再開とGPU確認

関連14testsはfailure/error/skip0。明示modeの必須・排他性、引数なしshellの検証専用動作、10B予算、旧output衝突拒否、データ周回拒否、準備なし学習拒否、既存stable-extensionの全state保存再開等を確認した。CPU小型fixture testsはモデル品質の証拠ではない。

実CUDAでは、同じ親・実train loader・実batch32/context1024で、stable-extensionとdecayの各経路を連続4updates対2updates＋保存＋再開2updatesで比較した。合計16 optimizer updates / 524,288検証input tokens、科学学習input tokensは0。gateは4-updateの減衰経路を確認したもので、将来のproduction15,259-update decayを実行したという意味ではない。

重み、Adam、scheduler、Python/NumPy/Torch/CUDA RNG、sampler位置、消費tokens/本文bytes、lineage等の保存state全項目が完全一致。loss/gradient normは有限、loss/LR/token digest/消費tokensの履歴も一致。親LR0.002からjumpせず、stable/decayの境界とfloorを確認した。tied embedding/outputは一つのparameterとして数え、10,001,152 parametersを保持している。

検証GPU lock内の実時間19.217秒、上限600秒以内。永続Windows launcher29620/Linux459、boot077f04cc-5ba2-4da6-87d3-778c8c756de7/start_ticks9675をactual processへ照合し、終了後も保存記録をCPUで確認した。job complete、両processは終了、GPU compute processなし。実環境はPython3.12.7、Torch2.14.1+cu130、RTX4090、WSL2。環境変更・依存更新は不要だった。

## 準備結果と起動コマンド

run内に`preparation-job.json`、`preparation.json`、`cuda-resume-gate.json`、verification checkpoints、source snapshot、environment、pipeline.logを保存した。引数なしshellを実行して`already_complete / mode=verify`が返り、GPU検証を再実行せず、本学習のstable/decay/result/jobを作らないことも確認した。

検証専用のコマンドは次のとおり。完了済みなので通常は再実行不要。

```bash
bash scripts/run_base_10b.sh --verify-only
```

今後、次段階の本学習を実行する場合の専用コマンドは次のとおり。

```bash
bash scripts/run_base_10b.sh --train
```

shellはuv run --frozenと必要extrasを使用し、同じlaunch lock/GPU lock・PID/boot/start ticks・累積GPU予算を保持する。凍結source/config/tests/親hashと成功した準備結果を実行時に確認し、valid latest checkpointから再開する。科学学習を開始するには明示modeが必要で、今回は起動していない。将来の本学習は保存検証の19.217秒もGPU予算へ含める。

この依頼は準備結果・状態記録の保存とlocal commitで終了する。10B本学習、全文品質評価、短文仕上げ、UTF8制約、20B/50B/Chatは未実行。次の具体的な作業はこの設定を使った本学習である。
