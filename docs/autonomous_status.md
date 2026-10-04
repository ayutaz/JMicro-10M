# Codex継続作業の現在地

最終更新: 2026-10-04 18:36 JST。**ユーザーがstep2を再開し、直接10Bの本学習を開始した。現在stable継続中。** 今回は10B学習・保存結果の確認・報告・local commitで停止し、step3の全文/生成品質評価は開始しない。

[現在の計画](39_learning_scale_and_generation_plan.md)、[10B準備結果](40_base_10b_preparation.md)、[原ロードマップと品質条件](15_project_roadmap.md)、[引き継ぎ](windows_handoff.md)。過去の実行中メモ・停止境界・7.5B案は[2026-10-04までの履歴](autonomous_history_20261004.md)へ移した。旧メモのPIDやコマンドを現在の起動指示にしない。

## 実際に完了したこと

| 対象 | 実状態と証拠 |
|---|---|
| モデル | T4K / NoQK-Norm / 10,001,152 parameters。規模は10Mのまま |
| データ | train12,225,819,077 tokens整備済み。[受け入れ記録](../reports/phase6/corpus_10b_ready_review.json)。構築時確認・raw再構築・実loader成功、独立全件auditはユーザー指定で未完了 |
| 主系列学習 | 総5,000,003,584 input tokens。[学習確認](../reports/phase6/base_5b_review.json)、[全文と生成比較](36_base_5b_comparison.md) |
| 仕上げ比較 | 同じ5B親からWeb/短文20%を各100,007,936 tokens、各累積5,100,011,520。別モデルの消費を合算しない。[結果](38_eos_5b_finish_results.md) |
| UTF8表示 | 共通helper実装済み。上限の未完成末尾だけを表示から保留し、raw失敗と停止理由は保持 |
| 10B準備 | 専用config/schema/launcher凍結。14tests、実CUDA16updates/524,288検証tokensの全state/history一致、保存証拠26項目成功。[準備確認](../reports/phase6/base_10b_preparation_review.json) |
| 10B本学習 | WSLのscience job開始、stable継続中。現在のupdate/tokensはjob.jsonとmetrics.jsonlを正とする |
| 品質と後続 | Base/Chat品質未達。独立人手blind採点・test・Chat学習・新重みの量子化品質は未実施 |

## 現在の評価結果

同じ保護dev89,416文書/164,344,743本文bytesのBPB、固定dev80のgreedy64-token上限。BPBは小さいほど良い。

| モデル | 全文BPB | 固定自然EOS | 固定反復 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元2B | 0.982882 | 0/80 | 60/80 | 0/400 |
| 元5B | 0.964484 | 0/80 | 59/80 | 2/400 |
| Web仕上げ5.1B | 0.958092 | 0/80 | 57/80 | 0/400 |
| 短文仕上げ5.1B | 0.959011 | 13/80 | 51/80 | 2/400 |

短文の全400自然EOS129/反復103、Web13/121。短文の全文BPB悪化は対照比+0.095894%で許容内だが、raw Unicode2により最終採用gate不合格。1件は途中不正UTF8、1件はcap末尾切断。短文重みは診断用として保持する。Webの増量数値gateは合格、両モデルとも意味・数量・時刻・否定条件の誤りが残る。自然停止増加を正答率・実用品質の達成にしない。2B→5BにはLR曲線差もあり、全差を学習量だけの因果効果とは断定しない。

## 保存先と実行状態

コード/Git正本はWindows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。大容量データは `/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards`。固定Tokenizerは `artifacts/phase2/4096/tokenizer.model`。Pythonはuv管理3.12.7、WSL2/RTX4090/Torch2.14.1+cu130。

主要checkpointはLinux repo相対で次に保存されている。hashの正本は凍結configと各review。

- 長期継続用stable4.75B: `reports/phase6/base-5b-20261004/stable/checkpoint-00144959.pt`、SHA `916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5`。
- final5B: `reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt`。
- Web/短文5.1B: `reports/phase6/eos-5b-finish-100m-20261004/{web,short20}/checkpoint-00155640.pt`。
- 10B準備: `reports/phase6/base-10b-20261004/` のpreparation-job/preparation/cuda-resume-gate/environment/source/logとverification checkpoints。

10B準備jobはcomplete、検証GPU時間19.217秒。旧Linux459/Windows29620は終了履歴。科学jobは2026-10-04 09:36Z起動、Windows30148、Linux427、boot86a59ddc-4594-4dfb-81df-a4f1439c52b0/start_ticks3212。実process生存確認済み。永続runのjob.json/pipeline.logとstable/decay checkpointを保存する。[launcher記録](../reports/phase6/base_10b_launch.json)。準備commit4c3fbaf、文書整理commit e67f8d3。pushはしない。

## 次に行うことと終了点

直前チャットの番号に揃える。ユーザーは今回step2だけを指定したため、10B学習・保存state確認・報告とcommitで止め、品質評価や後続実験は始めない。

1. **実行設定準備: 完了。** 専用設定と保存再開確認を再実行する必要はない。
2. **本学習: 実行中。** 保存stable4.75Bから9.5B stable＋15,259-update decayで総10,000,007,168/update305176へ直接継続。追加科学5,249,990,656 tokens、7.5B中間実験・追加収集なし。
3. **同じ評価で比較: 未実行・今回のstep2指定外。** 新10Bだけ全文dev/400を測り、5Bと最良Web5.1Bの保存結果を再利用する。10B専用比較入口と学習完了reviewの表示対応は実行前に整える。準備reviewerは本学習完了や品質を判定するものではない。
4. **報告・local commit・停止。** 原raw品質条件を保持し、改善と残る課題を明示する。EOS仕上げ/UTF8制約は別の後続候補で、現在未起動。

次段階を実行する場合のWSL repo内コマンド:

```bash
bash scripts/run_base_10b.sh --train
```

起動前にactual PID/boot/start ticksとGPU lockを確認し、valid latestから再開する。引数なしと `--verify-only` は検証専用で、完了結果を再利用する。科学学習GPU上限9,000秒に準備19.217秒を含め、評価予約1,800秒は別。学習区間約126分、比較等込み145〜165分の目安で、実装・内容確認は別。20B/50B/Chat/UL/sweepへ自動移行しない。

## 前回の文書整理の検証（起動前の履歴）

[文書更新記録](../reports/phase6/documentation_refresh_20261004.json)に元13文書の完全保存、270内部リンク、凍結10B設定・学習source/lockの不変性、Windows/WSLの現行文書一致、科学run未開始を記録した。過去のreport6件はWindows正本に存在し、Linuxコピーに不足することも記録する。移行時はGit管理reportと大型raw evidenceの両方を引き継ぐ。文書整理当時はGPU学習・評価を実行せず、local commitで停止した。その後ユーザーがstep2を再開した。
