# Chat-first SFT診断の実行記録

開始: 2026-10-10 JST。ユーザーの「5まで進めてください」に基づき、[計画128](128_chat_first_sft_plan.md)の保全・実装・1条件の学習・matched評価・結果報告までを再開した。Base/Chat採用、追加比較、量子化、公開は今回の到達範囲に含めない。

## 保全と準備

元WebUI10B checkpointは計画のSHA256 `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290` と一致。Tokenizerとfrozen model.pyも既存hashに一致した。WSLの準備済みRealPersonaChat manifestとTRAIN/DEVを再利用し、corpus再構築・新教材・Tokenizer再学習は行っていない。元UI実PID120460、HTTPの親hash/busy=false、RTX4090と約882GBの空き容量を確認した。

専用の `chat_first_contract.py`、SFT runner、masked batch probe、独立CUDA resume gate、matched Chat evaluator、rawに結び付いたcontent reviewerとWindowsの永続launcherを追加した。元の `require_adopted_base` と既存runnerの採用gateは変更していない。親は未採用、routeはdirect SFT、全parameterをfresh AdamWで更新する契約。

CPU preflightで2,688 TRAIN会話、40,366 windows/周、633,185 Assistant教師tokens/周、最終3周の121,098 windows/1,899,555教師/30,567,471直列tokensを確認した。初回parameter確認はstate_dictの共有embedding/output名を二重に数えて失敗したため、実モデルのParameterを一度ずつ数える方法へ修正。親・モデル構成は変更していない。失敗時の未実行configも保存した。

関連tests24件が合格。3周の完全EOT、末尾の空batch行、全sampler state、DEV混入拒否、既存採用gateとの分離、fresh optimizer/resume、Chatのraw/history/sampling契約を対象とした。Python compileとPowerShell launcherのsyntaxも確認した。CPU testsを実CUDA学習や品質の証拠とは扱わない。

## masked CUDA/BF16 batch測定

2 warmup+6 measured updatesでbatch8/16/32/64を測定した。probe実PID130650 / boot `4052bfc5-3850-44e4-9123-d34a9e19f36e` / start_ticks24385154は終端complete、exit0。追加GPU86.648秒。probe重みを本学習へ使用しない。

| batch | median Assistant教師tokens/秒 | 最大割当bytes |
|---:|---:|---:|
| 8 | 1,474.06 | 4,201,174,528 |
| 16 | 1,873.53 | 8,195,175,936 |
| 32 | 1,892.32 | 16,183,178,752 |

選定は32。最大batchを速度最良とは扱わない。詳細の全候補・rowはprobe reportを正とする。

最終configは [chat_first_sft.json](../configs/phase7/chat_first_sft.json)、SHA256 `ffdd5e72f3a9161b81853759fec87c9eaff8e2ad3af341da43ab33d57997d648`。seed42、BF16/math/document、accumulation1、context1024、LR1e-4、weight_decay0.01、TRAIN最大3周、実測batch32。学習用更新数と5% warmupをこのbatchに結び付けた。

## 現在の実行と次の行動

独立CUDA resume gateは完了・exit0。Windows worker35016、WSL実PID131049 / 同boot / start_ticks24398154、driver SHA256 `a6563575468098500b798760d7f464ee5b7a29cea364621ee21531892d03d145`。GPU21.418秒、連続4更新と2更新→保存→再開2更新のmodel/optimizer/scheduler/RNG/sampler/counters/消費列/履歴等19checksすべて一致。gate stateを本学習へ引き継がない。これらは終端までの観察であり、将来の稼働は実PID/identityとjobを再確認する。

学習前Baseのmatched Chat評価をWindows worker33892から開始した。次はその全219応答を取得し、fresh SFTを最大3周、checkpoint群の全評価・内容確認へ進む。probe/gate/Base対照を学習量へ加えない。各stageの完了後に記録を追記する。

今の準備・速度測定は会話品質の証拠ではなく、Base/Chatは未採用。学習・最終結果・全内容採点・停止報告は未完了。
