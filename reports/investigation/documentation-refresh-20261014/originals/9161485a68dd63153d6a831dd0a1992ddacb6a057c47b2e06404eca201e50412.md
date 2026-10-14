# Phase 6③ 高速化・資源活用の完了記録

完了: 2026-10-03（日本時間）。今回のユーザー指定はVRAM等の資源活用とtorch.compile等の高速化の調査・不足対応。①②の成果を保持し、③の実装・実測・再開・監査を完了した。**④生成/変換・⑤長期設定・500M以上の本学習は未開始で、ここで停止する。Phase 6全体やBase/Chat品質の完了ではない。**

## 採用と確認した容量

T4K NoNorm / 10,001,152 parameters / WSL 2 / RTX 4090 / Python 3.12.7・uv / PyTorch 2.14.1・CUDA 13.0を使用。FP32 parameters＋BF16、context 1024、fused AdamW、WSD。採用は**Flash / compile reduce-overhead / fullgraph・static / deterministic / batch 32・accumulation 1**、32,768 input tokens/update。

| 項目 | 実測・判断 |
|---|---|
| 定常速度・3回中央値 | 694,521 tokens/s。最速reference/math batch 16の127,772に対して5.436倍 |
| 選択設定のsave/評価込みVRAM | allocated 5.73 GiB、reserved 6.59 GiB、driver peak 7.53 GiB |
| 最大安定容量 | Flash/compile batch 111、112 OOM。111は3×200・評価/save・厳密再開を通過 |
| 容量設定のdriver peak | 23.42/23.99 GiB、97.64%。allocator cap 94%の測定条件 |
| 容量設定の速度 | 649,563 tokens/s。最速には32を選定 |
| CPU/data供給 | 選択設定のdata wait 0.55%。起動時の全index読み込み・hash検証は定常時間と分ける |
| 速度換算 | 500M約12分、10B約4時間の純学習算術値。全文評価・保存・compile・枝・調整を含まない |

[選定理由](../reports/phase6/batch_choice.md)、[全結果](../reports/phase6/batch_performance_report.json)、[要約・token台帳](../reports/phase6/performance_summary.json)。driver使用率は選択設定で最大95%、容量設定で最大98%を観測。2秒sampleはstartupも含み、MFUや理論性能の達成とは表示しない。通常allocator/固定shapeの有限探索で、未測定mode・任意環境の最大性能を保証しない。

## 実装・修正と検証

固定長/PADなしの学習専用causal経路で明示maskとGPU値によるPython分岐を除いた。cache/padding/labelsはこの経路から拒否し、既存の推論・export経路を保った。CPUで参照logits/loss/全gradient・causalityを比較し、全79 tests / skip・failure・error 0を確認した。

compile mode/fullgraph/staticとdeterministicをCLI/specへbindした。Inductor cacheをbackend/dtype/deterministic別に分離し、構築時にDynamoのmemory cacheをresetする。実CUDA updateのATen演算を記録し、CUDA Graph replayはworkerが出力したbackend固有code/SHAと実compiled graph呼び出しで補う。初回v1/v2の検査不足・cache取り違えは失敗として保持し、採用証拠へ混ぜない。[調査と変更の詳細](28_phase6_performance.md)。

runnerの9設定でstable 200 vs 100+100、decay 100 vs 50+50、全state・loss/LR/token列/bytes/digest・親の不変性・元継続を検証した。採用/容量の6設定は各3×200完了更新・小sample評価・保存を通過。**独立監査1286 checksは全成功**。採用batch 32では空のcompiler cacheから100→200を新runで再開し、連続200と**26 checks完全一致**。元run全filesも不変。

[独立監査](../reports/phase6/performance_completion_audit.json)、[cold-cache再開](../reports/phase6/performance_cold_resume_report.json)、[79 tests](../reports/phase6/performance_tests.xml)、[失敗保持](../reports/phase6/performance_failures.json)。監査の初回の生成output数の誤判定も保持し、既存APIの1 prompt×2 greedy outputsに合わせて修正した。sampleは4 dev文書＋1 prompt×2 outputs/各最大8 tokensで、全文品質評価ではない。

v3のunique raw metricsに**10,005 completed updates / 414,298,112 input tokens**、cold resumeに100 updates / 3,276,800 additional input tokensを記録。別々の新規性能runで、一つの長期Baseではない。未完了OOM更新や診断v1/v2の入力をこの値に含めない。

## 保存先・終了と次の境界

- Windowsコード/Git正本はworkspace、Linux実行コピーは`~/src/japanese-tiny-llm-10m`。Linuxの古いGit HEADよりsource snapshot/hashを正本として照合する。
- v3: Linux `reports/phase6/performance-20261003-v3`。job terminal complete、Windows launcher 24452、Linux supervisor 426 / boot `37666cd9-cd78-41c1-a0cb-39c21d108047` / start ticks 78847は終了確認済み。
- cold resume: Linux `reports/phase6/performance-cold-resume-20261003`。terminal complete、Windows launcher 17308、Linux supervisor 620 / 同boot / start ticks 361156は終了確認済み。
- raw metrics/requests/results/checkpoints/compiled code/snapshotは各runに保持。通常compiler cacheはLinux `artifacts/compile-cache`、cold cacheはcold runの`empty-cache`。旧①②snapshotと過去reportsを保持する。

GPU compute processなしを独立監査で確認した。旧73 reportsとuv.lockのbyte保持、current docs/CLI/WSL同期は[文書・履歴監査](../reports/phase6/performance_documentation_audit.json)で確認する。Gitは`yousan <ka1357amnbpdr@gmail.com>`でcommitし、pushしない。

本学習のbatch/LR/WSD長期配分は未凍結。生成のEOS/反復/Unicode、NoNorm HF/GGUF adapterは未解決の④として残す。⑤を経た後のBase→Chat→量子化は[残りの計画](27_phase6_remaining_plan.md)と[roadmap](15_project_roadmap.md)に従う。今回完了した速度・保存再開を品質目標達成の証拠へ流用しない。
