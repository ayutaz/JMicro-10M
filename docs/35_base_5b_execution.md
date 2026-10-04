# 次計画1・2：10Mモデルを総5Bまで学習

2026-10-04完了：[実際の保存記録](../reports/phase6/base_5b_review.json)、[完了証拠](../reports/phase6/base_5b_completion_audit.json)。総5,000,003,584 tokens、追加3,099,983,872科学tokens、別524,288検証tokens。6testsと実CUDA全state再開一致、連続94,604科学updates、parent不変、全97科学checkpoint保持。GPU4,543.110秒で7,200秒以内、実job終了。final decay/checkpoint-00152588.pt、SHA1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a。5B品質は未評価。記録/local commitで停止。以下は凍結した実行計画であり、完成jobの再実行指示ではない。

2026-10-04。ユーザー指定範囲は継続処理の実装・凍結・保存再開確認と5B学習。全文評価・Chatは次の段階。元2B/低LR100M/短文枝を含む全旧成果物を保持する。

| 条件 | 固定値 |
|---|---|
| モデル | 10,001,152 parameters、Tokenizer/構造を保持 |
| データ | 既存train12,225,819,077 tokens、Web100%、dev/testを学習しない |
| 開始点 | stable update57,984 /1,900,019,712 tokens |
| stable終端 | update144,959 /4,750,016,512 tokens |
| decay | 7,629 updates、約5%を最寄りupdateへ丸める |
| 総終端 | update152,588 /5,000,003,584 tokens |
| 追加科学学習 | 3,099,983,872 tokens |
| 学習率 | stable親と同じ0.002、最後cosineで0.0002へ |
| 実行 | uv/WSL/RTX4090、BF16、FP32parameters、Flash、compile reduce-overhead、batch32/context1024 |
| 保存・ログ | completed1,000updatesごと保存、50updatesごとheartbeat、全checkpoint保持 |
| 検証予算 | CUDA16updates/524,288tokens、科学学習と別計上 |
| GPU上限 | 累積7,200秒、空き200GiB以上、出力想定20GiB以内 |
| 概算 | pure約75分、保存等込み80〜100分。CPU実装時間は別 |

予測精度と生成失敗の元増量gateは[低LR100M比較](../reports/phase6/eos_low_lr_100m_review.json)で合格。完成decay枝を通常resumeで延ばさず、stable親のmodel/Adam/scheduler/RNG/sampler/counterを継承する。予算以外の変更を新extension APIは拒否し、通常resumeの設定凍結は維持。core sourceを変更せず旧checkpointのsource bindingを保存する。

低LR0.0002が成功したのは完成decay2Bから追加100Mする別条件。長期stableの最適値とは一般化しない。今回の親はactualLR0.002であり、その値を維持することで再開時のLR jumpを発生させない。科学追加tokensには途中stableと最終decayを両方含める。短文21M poolを反復混合しない。

関連6CPUtestsと実CUDAの連続4対2+保存再開2でstate/historyを照合する。CUDAはstable延長と4update decayの2経路、合計16updates。production decay7,629とは区別する。core scheduler/optimizerの演算は同じ。builder/既存accepted loaderを再利用し、全件重複照合/Tokenizer再学習/バッチ再benchmarkを行わない。

凍結configは[base_5b.json](../configs/phase6/base_5b.json)。runはLinux `reports/phase6/base-5b-20261004/`。Windows hidden launcherでWSLを保持し、bashのlaunch lockとGPU lockを使用する。job.jsonのPID/boot/start_ticksとactual processを照合。中断時は最新checksum確認済みcheckpointから同じconfigで再開し、未確定metrics区間を履歴として保持する。再開commandは`bash scripts/run_base_5b.sh`。予算終了は同じ条件で反復retryせず記録する。

完成証拠は実CUDAgate、連続した科学更新metrics、両stage result、final checkpointの全学習state/finite値/実token数、元parent hash不変、actual job終了。報告とcommit後停止する。5B全文BPB/EOS/反復/人手品質は未評価で、学習完了を品質改善とは主張しない。次は同じ保護dev/固定生成で元2Bと低LRWeb100Mを比較するstep3。
