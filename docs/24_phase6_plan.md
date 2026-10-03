# Phase 6: Base本学習の準備と段階評価計画

更新: 2026-10-03。[Phase 5](23_phase5_completion.md)は完了し、現在はPhase 6前で停止中。この文書は次回の準備・判断順を定める計画であり、学習開始や数値予算の凍結を意味しない。ユーザーの再開指定後に進める。

## 目的と出発点

拡張した日本語train corpusで約10Mモデルをスクラッチ学習し、短文生成を測定した`JMicro-10M-Base-v1`を残す。500M→1B→2B→5B→10Bで評価し、データ反復・能力・追加GPU時間を根拠に継続を判断する。10Bまで到達したことと品質目標の達成を分ける。Chat学習はPhase 7で行う。

現在の候補は **T4K / QK-Normなし / AdamW / LR 0.002**。語彙4,096、hidden 256、13層、FFN 640、4Q/2KV、context 1024、tied embedding、10,001,152 parameters。[候補configと実checkpoint](../reports/phase5/candidate_configs.json)、[採否理由](../reports/phase5/candidate_selection_review.md)を参照する。RMSNormとRoPEは維持し、Q/Kのhead次元Normだけを省略する。

Phase 5のdev BPBは1.221443、定常速度121,139 tokens/s。これはpilot反復・math / batch 8の実測。greedy EOS0/80、反復54/80、sampling Unicode破綻2/240で品質目標は未達。NoQK-NormのHF/GGUF adapterは未実装。NormありT4Kは対照として保存するが、今回は本学習候補を1つ選んでいる。候補の採否を変える場合は理由と対照結果を残す。

## 開始前に揃える条件

| 順序 | 作業 | 完了の証拠・開始条件 |
|---:|---|---|
| 1 | 実行状態・成果物の確認 | 既存process/job/lock、公開Tokenizer hash、選択config、checkpoint、core sourceを照合。重複GPU jobを起動しない。 |
| 2 | 拡張corpusの段階取得・shard化 | source/revision/条件・取得上限・保存先を記録。train/dev/testと固定suiteの混入を防ぎ、unique docs/bytes/独自Tokenizer tokens・dedup・source配合・予定反復をmanifestへ保存。pilotと新corpusの評価を分ける。 |
| 3 | 必要なtrainer機能の実装 | WSD、stable/decay分岐、必要なら複数source mixtureを実装する。未実装CLIを起動例として書かない。window/教師maskと累積lossの契約を維持。 |
| 4 | 正確な再開と分岐の検証 | 採用候補・実shard・採用backendで連続と中断再開のtoken列/loss/全stateを照合。WSD分岐のモデル・optimizer・RNG・samplerを保存し、評価枝が継続枝を変更しないことを検証。 |
| 5 | 速度・最大安定batchの再測定 | mathの容量、compiled/math等の候補を比較し、有限forward/backward、厳密resume、3×200更新と評価/保存、peak VRAM、cold compile、定常速度、data waitを記録。Phase 4のdefault最大batchを流用しない。 |
| 6 | 推論・生成の課題を切り分け | 採用構成のnative prefill/cacheと停止ID契約を確認。Unicode破綻・反復・停止の実例を保存し、生成制約等の修正は同じ固定dev条件で対照評価。NoNorm変換経路の実装計画と検証条件を明示し、変換が成立しない場合は保存済みNorm対照への見直しを判断。 |
| 7 | config・予算・永続実行の凍結 | measured batch/effective tokens、LR/warmup、stable/decay token予算、mixture/seed、保存/評価間隔、追加枝compute、容量上限、実CLI/restart commandをrun configへ保存。GPU job/PID/boot/start ticks・log・source snapshot・checkpoint SHAを記録。 |

全量50〜100Bの取得を最初の500M開始条件にしない。各段階に必要な取得範囲を先に決める。unique量が予算より少なければ反復倍率を明記し、同じpilotの反復を新規データのscalingと呼ばない。拡張dataでのBPBとPhase 5のpilot BPBは母集団が違うため、そのまま数値差を改善量にしない。

## Scheduler・batch・継続の扱い

長期系列にはWSD（warmup→stable→decay）を採用する方針。stable checkpointを継続の正本とし、各評価点のdecay枝は独立runとして保存する。枝ごとにtokens、更新数、GPU時間、source/config/dataと分岐元を記録する。追加予算はstable枝へ与え、終了したdecay枝をstableの履歴として扱わない。

Phase 5の100M終端は凍結cosineの比較結果であり、総step数だけを変更して本系列へ延長しない。選択するのはarchitecture/Tokenizer/LRで、拡張train corpusの本系列は新規初期化する。batchを増やすと更新数と最適化条件が変わるため、LR 0.002を無条件に最適値としない。採用batchで小予算の安定性・学習曲線を確認してから本設定を固定する。

WSD、mixture、NoNorm HF/GGUF adapterは未実装。stable/decayの数値配分、拡張sourceの実量・配合、本学習batch/backendは未凍結。これらを実装済み・実測済みと表示しない。学習後export/量子化の正式なparity・品質検証はPhase 8の必須条件として維持する。

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

選択候補のPhase 5定常中央値121,139 tokens/sを使った算術値。新corpus・batch/backend・WSDの速度保証ではなく、評価/保存/取得/修復・cold start・decay枝を除く。最終予算は開始前の再測定で更新する。

| 系列tokens | 参考compute時間 |
|---:|---:|
| 500M | 約1.15時間 |
| 1B | 約2.29時間 |
| 2B | 約4.59時間 |
| 5B | 約11.47時間 |
| 10B | 約22.93時間 |

同じ固定400生成のNoNorm評価workerはPhase 5で約5.4分/回だった。拡張devの採点時間、保存間隔、枝の回数を別加算する。uint16 streamは2 bytes/tokenにindex/raw/一時fileを加え、checkpointは保持個数×実file容量、cache/venvは別枠。空き容量は開始時に再確認する。[完了時の実測資源](../reports/phase5/resource_budget.json)

## 次回の実行入口と成果物

次回は`AGENTS.md`、[現在の状態](autonomous_status.md)、本書、[Windows/WSL手順](windows_handoff.md)を読み、既存jobと未実装項目から確認する。復元済みのTokenizer学習・Phase 3全export・Phase 4全測定を無条件に繰り返さない。

既存CLIの確認は学習を起動しない:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --help
```

WSDの実CLIと長期run configが未作成のため、本書には本学習の起動commandを置かない。実装とgate通過後に、正確な起動・再開commandをrun記録とhandoffへ追加する。

予定成果物は拡張corpus manifest/shards、準備gate report、凍結run config、stable/decay checkpointと台帳、`base_scaling_report.json`、`base_v1_evaluation.md`、model card。これらは今後作成するもの。現在の停止境界はPhase 5完了のまま維持する。
