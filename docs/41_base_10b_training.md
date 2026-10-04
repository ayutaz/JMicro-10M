# 直接10B学習の完了記録

2026-10-04 20:43 JST、WSL2 / RTX 4090で総 **10,000,007,168 input tokens / update305176** の学習を完了した。ユーザー指定のstep2（学習と保存結果確認）までの結果であり、10Bの全文dev・固定400生成・品質採否は未評価。[CPU保存確認19項目](../reports/phase6/base_10b_training_review.json)はすべて成功した。

## 学習量と保存結果

モデルは10,001,152 parameters、train poolは12,225,819,077 tokensのまま。新規データ取得や7.5Bの中間実験は行わず、保存stable4.75Bのmodel/Adam/RNG/Web cursorを保持して継続した。減衰済み5Bや独立5.1B枝の消費を合算していない。

| 区間 | 終端update | 累積input tokens | 今回の追加tokens | 定常tokens/秒 |
|---|---:|---:|---:|---:|
| 継続親stable4.75B | 144959 | 4,750,016,512 | — | — |
| stable | 289917 | 9,500,000,256 | 4,749,983,744 | 695,339 |
| 最終decay | 305176 | 10,000,007,168 | 500,006,912 | 694,288 |

今回の追加科学学習は **5,249,990,656 tokens**。準備CUDAの16更新/524,288検証tokensは別会計。GPU lock時間は準備19.217秒を含め **7,657.678秒（2時間7分38秒）** で、凍結上限9,000秒以内。定常速度はstage metricsの中央値であり、保存・起動を含む全区間の平均とは異なる。

保存先はLinux repo `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` 相対:

- 継続用stable: `reports/phase6/base-10b-20261004/stable/checkpoint-00289917.pt`、SHA256 `122a013c651bad258f1b374a268ee11e8c4dc6ad2e6859ec76804e6779fae8fb`。
- 評価用final: `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt`、SHA256 `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`。
- `job.json`、`result.json`、stage metrics/latest、pipeline log、source snapshotを同じrunへ保持。科学checkpointはstable146個・decay17個、準備を含むrun容量は20,496,920,424 bytesで32GiB上限以内。

学習は09:36Z開始、11:43:52Z終了。Linux PID427（boot `86a59ddc-4594-4dfb-81df-a4f1439c52b0` / start_ticks3212）とhidden Windows supervisor PID30148は終了済み。起動記録は[launcher](../reports/phase6/base_10b_launch.json)、完了と終了確認は[completion](../reports/phase6/base_10b_training_completion.json)に保存した。

## 高速化の実測と追加余地

現在はFlash Attention、`torch.compile` reduce-overhead/fullgraph/static shape、固定長PADなし学習経路、FP32 parameters/BF16 forward-backward、fused AdamW、batch32/context1024/accumulation1を使用。dataとcheckpointはLinux disk上で扱う。

過去の同一モデル/data/Tokenizer/precision比較では、最速reference/mathの127,772 tokens/秒に対して採用設定は694,521 tokens/秒で **5.436倍**。最大安定batch111は649,563 tokens/秒で、採用batch32より遅かった。batch32のdriver peakは約7.53GiB、batch111は約23.42GiB（97.64%）。VRAMを埋めることを速度の判断基準にしない。[速度・容量比較の実測](../reports/phase6/batch_choice.md)、[保存済み数値](../reports/phase6/performance_summary.json)。今回の長時間学習でも約694〜695k tokens/秒を維持した。

既存比較のdata waitは0.55%で、入力供給の改善だけによる増速余地は小さい。GPU使用率は今回終盤の観測で92〜93%だったが、理論計算性能を使い切ったという意味ではない。追加改善はkernel/compileやCPU供給の短いprofileから律速を確認し、一要因を変更して比較する必要がある。新設定の採用には速度改善と有限値・保存再開の確認が必要であり、今回の凍結科学runは変更しなかった。追加速度実験は未実施。

## 検証範囲と次の段階

専用CPU reviewerで、terminal job終了、凍結source/config/data/Tokenizer/親hash、元14testsとCUDA厳密再開証拠、全科学metricsの連続update・有限loss/勾配・LR・tokens、両終端の有限model/Adam・scheduler・RNG・sampler位置・digest、checkpoint保持、容量とGPU予算を確認した。GPU検証や全corpus再照合は繰り返していない。独立全12.23B corpus auditの未完了は保持する。

総10B到達は品質改善の証拠ではない。全文BPB、自然EOS、反復、raw Unicode、内容品質は未評価。独立人手blind/test、Chat、新重みの量子化も未実施。元の品質gateを維持する。

今回の指定どおり報告・local commitで停止する。次回step3を再開する場合は、新10Bだけ同じ全文dev89,416文書と固定400生成で測り、既存5B/最良Web5.1Bの結果と比較するための専用入口を整える。[条件と計画](39_learning_scale_and_generation_plan.md)。完了済みの`--train`を再学習の指示として使わない。
