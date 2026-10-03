# Phase 6: Base本学習の準備と段階評価計画

更新: 2026-10-03。[Phase 5](23_phase5_completion.md)は完了し、現在はPhase 6①②③完了で停止中（本学習未開始）。①データ拡充と②長時間学習準備は[事前の目的・完了条件](25_phase6_preparation.md)に従い完了した。[完了証拠](26_phase6_preparation_completion.md)。③容量/高速化の完了結果と再開後の④生成/変換→⑤設定・予算凍結は[残りの実行計画](27_phase6_remaining_plan.md)に具体化した。ユーザー指定の③資源活用・高速化は検証・commit済み（`a7d26e1`）。実装・実測は[③の完了](29_phase6_performance_completion.md)。④以降と本学習は開始しない。

## 目的と出発点

拡張した日本語train corpusで約10Mモデルをスクラッチ学習し、短文生成を測定した`JMicro-10M-Base-v1`を残す。500M→1B→2B→5B→10Bで評価し、データ反復・能力・追加GPU時間を根拠に継続を判断する。10Bまで到達したことと品質目標の達成を分ける。Chat学習はPhase 7で行う。

現在の候補は **T4K / QK-Normなし / AdamW / LR 0.002**。語彙4,096、hidden 256、13層、FFN 640、4Q/2KV、context 1024、tied embedding、10,001,152 parameters。[候補configと実checkpoint](../reports/phase5/candidate_configs.json)、[採否理由](../reports/phase5/candidate_selection_review.md)を参照する。RMSNormとRoPEは維持し、Q/Kのhead次元Normだけを省略する。

Phase 5のdev BPBは1.221443、定常速度121,139 tokens/s。これはpilot反復・math / batch 8の実測。greedy EOS0/80、反復54/80、sampling Unicode破綻2/240で品質目標は未達。NoQK-NormのHF/GGUF adapterは未実装。NormありT4Kは対照として保存するが、今回は本学習候補を1つ選んでいる。候補の採否を変える場合は理由と対照結果を残す。

## 開始前に揃える条件

この表のgate 1〜7は検証項目で、作業区分①〜⑤と同じ番号ではない。①はgate 2、②はgate 3/4と準備runの永続化、③はgate 5と変更後のgate 4、④はgate 6、⑤はgate 7に対応する。

| gate | 作業 | 現在の状態 | 完了の証拠・次回の条件 |
|---:|---|---|---|
| 1 | 実行状態・成果物の確認 | ①②③終了時に確認済み、各job前に再確認 | 既存process/job/lock、公開Tokenizer hash、選択config、checkpoint、core sourceを照合。重複GPU jobを起動しない。 |
| 2 | 拡張corpus・shard化 | ①完了 | 756,087,912 unique train stream tokens、Web 100%、dev/test分離。source/revision/条件・取得上限・全raw/cluster/shard監査と予定反復を[完了記録](26_phase6_preparation_completion.md)に保存。 |
| 3 | 必要なtrainer機能 | ②のWSD完了、mixture未実装 | stable/decay CLIは実装済み。初期Web単一sourceはmixture不要。必要時は明示変更系列として実装・検証し、window/教師maskと累積loss契約を維持する。 |
| 4 | 正確な再開・分岐 | ②と③の9設定で完全一致・採用設定のcold再開も完了 | 実拡張shardでstable 200 vs 100+100、decay 100 vs 50+50のtoken列/loss/LR/全state完全一致、元stable不変性・継続一致を確認済み。batch/backend/source変更後に再検証する。 |
| 5 | 速度・最大安定batch | ③完了（独立1286 checks・cold26 checks） | [完了記録](29_phase6_performance_completion.md)。NoNorm/拡張shard/WSDで実演算・cache分離、有限値、厳密再開/分岐、6設定の3×200更新・評価/saveを通過。最速Flash/compile batch 32=694,521 tokens/s、最大111・112 OOM。 |
| 6 | 生成・変換課題 | ④未着手、品質未達 | native prefill/cache・停止ID、Unicode/反復/EOSを同一dev 400生成で対照確認。NoNorm HF/GGUF adapterを実装・parity検証し、成立しない場合の修復予算またはNorm対照への見直しを記録する。 |
| 7 | 本学習設定・予算・永続実行 | 準備runは保存済み、⑤の長期凍結は未着手 | measured batch/effective tokens、LR/warmup、stable/decay数値予算、mixture/seed、保存/評価間隔・保持数、追加枝compute、容量上限、実CLI/restart commandを凍結。PID/boot/start ticks・log・snapshot・checkpoint SHAと復旧を保持する。 |

全量50〜100Bの取得を最初の500M開始条件にしない。各段階に必要な取得範囲を先に決める。unique量が予算より少なければ反復倍率を明記し、同じpilotの反復を新規データのscalingと呼ばない。拡張dataでのBPBとPhase 5のpilot BPBは母集団が違うため、そのまま数値差を改善量にしない。

## Scheduler・batch・継続の扱い

長期系列には実装済みのWSD（warmup→stable→decay）を採用する。stable checkpointを継続の正本とし、各評価点のdecay枝は独立runとして保存する。枝ごとにtokens、更新数、GPU時間、source/config/dataと分岐元を記録する。⑤でstable終端予算を先に凍結し、その範囲内の観測点を区切って継続する。終了したdecay枝をstableの履歴として扱わない。

`--branch-from`はdecay専用で、stable予算延長forkは未実装。通常resumeはbudget/source/data変更を拒否する。Phase 9の20B/50B延長や追加corpus/mixtureには、明示forkの履歴と全state検証を先に実装する。新corpusで現在のPhase 6 dev/testを保護する入力・provenanceも未実装として残す。[実装上の残り](27_phase6_remaining_plan.md)

Phase 5の100M終端は凍結cosineの比較結果であり、総step数だけを変更して本系列へ延長しない。選択するのはarchitecture/Tokenizer/LRで、拡張train corpusの本系列は新規初期化する。batchを増やすと更新数と最適化条件が変わるため、LR 0.002を無条件に最適値としない。採用batchで小予算の安定性・学習曲線を確認してから本設定を固定する。

WSD stable/decayは実装・CUDA全state再開一致を検証済み。複数source mixtureとNoNorm HF/GGUF adapterは未実装。拡張sourceは756M unique train stream tokens、初期配合はWeb 100%。長期stable/decayの数値配分と本学習batch/backendは未凍結。これらを実装済み・実測済みと表示しない。学習後export/量子化の正式なparity・品質検証はPhase 8の必須条件として維持する。

`configs/training/baseline.json`は初期の提案templateで、train CLIは自動読込しない。Phase 5の実行条件は凍結済みの`configs/phase5/plan.json`、候補の実configは上記reportを正とする。Phase 6のruntime configはgate通過後に別途作成し、初期templateのbatch-selection phaseやscheduler候補を本学習の確定値として流用しない。

## 段階評価と継続・停止判断

| 累積stable系列の観測点 | 目的 | 判断と保存 |
|---:|---|---|
| 500M | 新corpusでの初期改善・反復・停止を確認 | dev BPB、同じ固定80 prompt×5条件、生成ID/失敗率、unique量/反復、実時間。発散・非有限・再開不一致なら停止して修復。失敗率が悪化すれば原因を調べる。 |
| 1B | 日本語短文の立ち上がり | 同じdev文書のBPB差とpaired CI、文法rubric、文字数分布を保存。原則は現在の1候補を継続。対照を追加する必要が生じた場合だけ理由・予算を固定し、候補は最大2つ。 |
| 2B | 継続の価値と過去経験との比較点 | 同一条件の継続価値を測る。過去355M modelのartifactが取得できなければ直接比較は未実施と明記する。 |
| 5B | 本命構成と残り予算を判断 | 本命1構成、品質の到達/未達、追加10Bまでの時間/容量を保存。量だけを増やして解決しない場合は日常短文mixture等を別対照として比較する。 |
| 10B | Base v1の固定評価・成果物 | 再構築・再開可能なcheckpoint、model config、Tokenizer/data/source hash、model card、固定評価と失敗例を保存。目標未達なら未達と報告する。 |

観測点の評価checkpointはWSD decay枝とし、実際の枝tokensを併記する。stable系列の予算と枝の追加computeを混同しない。devで選定し、最終評価用testは選定に使わない。Base文法70%以上等の[凍結目標](15_project_roadmap.md#品質目標と判断ルール)を維持し、結果を見て基準を下げない。Chatの関連性・文脈・EOT停止はPhase 7の別検証であり、Base段階で達成済みにしない。

本命10Bの証拠を揃え、日本語生成が成立した場合はPhase 7へ進む。未達なら修復・対照実験または容量/データの限界として判断し、成功扱いで次へ進まない。20B・条件付き50BはPhase 9の系列であり、Phase 6の完了条件へ追加しない。

## 暫定のcompute見積もり

③の採用設定の定常中央値694,521 tokens/sを使った算術値。全文評価/保存/取得/修復・cold compile・decay枝・LR調整を除く。本学習configは未凍結で、実時間の保証ではない。[③の完了記録](29_phase6_performance_completion.md)。

| 系列tokens | 参考compute時間 |
|---:|---:|
| 500M | 約12分 |
| 1B | 約24分 |
| 2B | 約48分 |
| 5B | 約2時間 |
| 10B | 約4時間 |

同じ固定400生成のNoNorm評価workerはPhase 5で約5.4分/回だった。新devは89,416文書 / 164,344,743 body bytesで、pilot 924文書とは別母集団。拡張dev全文採点、保存間隔、枝の回数を別加算し、小sample probeを全文品質評価としない。uint16 streamは2 bytes/tokenにindex/raw/一時fileを加え、checkpointは保持個数×実file容量、cache/venvは別枠。準備完了時のLinux空きは950,875,688,960 bytesで、開始時に再確認する。[Phase 5速度](../reports/phase5/resource_budget.json)、[Phase 6準備の実測資源](../reports/phase6/completion_audit.json)

## 次回の実行入口と成果物

次回は`AGENTS.md`、[現在の状態](autonomous_status.md)、本書、[Windows/WSL手順](windows_handoff.md)を読み、既存jobと未実装項目から確認する。復元済みのTokenizer学習・Phase 3全export・Phase 4全測定を無条件に繰り返さない。

既存CLIの確認は学習を起動しない:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --help
```

WSDの実CLI・準備検証configと、採用config・拡張shardに対応する③用測定/厳密再開・独立監査の入口は実装済み。[③の実CLIと比較](28_phase6_performance.md)。長期run configは未凍結のため、本学習の起動commandは置かない。④⑤のgate通過後、正確な本学習の起動・再開commandをrun記録とhandoffへ追加する。

①②の拡張corpus manifest/shards、独立準備gate report、準備検証config、stable/decay検証checkpointと台帳は保存済み。[完了記録](26_phase6_preparation_completion.md)。本学習の凍結run config、scaling checkpoint、`base_scaling_report.json`、`base_v1_evaluation.md`とmodel cardは今後作成する。③の高速化・容量検証はcommit `a7d26e1`で完了。今回の計画更新で停止境界は変更しない。④以降へは進まない。

## batch 32候補の更新数と丸め（⑤で凍結する提案）

③の32,768 input tokens/updateを維持する場合の算術表。stable系列のglobal updateで、decay枝の追加tokensを含まない。本学習configの確定値ではなく、batch・accumulation変更時は再計算する。

| 目標input tokens | global updates | 丸め後input tokens | 純学習換算 |
|---:|---:|---:|---:|
| 500,000,000 | 15,259 | 500,006,912 | 12.0分 |
| 1,000,000,000 | 30,518 | 1,000,013,824 | 24.0分 |
| 2,000,000,000 | 61,036 | 2,000,027,648 | 48.0分 |
| 5,000,000,000 | 152,588 | 5,000,003,584 | 120.0分 |
| 10,000,000,000 | 305,176 | 10,000,007,168 | 240.0分 |

本文教師tokens/bytesはBOS等のmaskと実samplerから別計数する。500M→1B等の区間予算は累積値の差で計算し、枝と評価/保存を別に加算する。
