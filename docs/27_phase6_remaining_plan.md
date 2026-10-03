# Phase 6③以降: 再開時の実行計画

更新: 2026-10-03。①データ拡充と②WSD/長時間学習準備は[完了済み](26_phase6_preparation_completion.md)。ユーザーの資源活用・高速化の指定で③を再開し、[実装・凍結比較・実CLI](28_phase6_performance.md)に従い測定中。**③の検証・commit後に停止し、④生成/変換・⑤本学習設定の凍結・500M以上の本学習は開始しない。** 本書の④⑤以降の予算は将来の提案であり、再開時に固定する。品質閾値と完全一致の要求は維持する。

## 出発点と、今回繰り返さない作業

採用候補はT4K / NoQK-Norm / AdamW / LR 0.002、10,001,152 parameters、context 1024。モデルconfigは[候補台帳](../reports/phase5/candidate_configs.json)、実装・データの証拠は[独立監査](../reports/phase6/completion_audit.json)を正とする。Python 3.12.7の全実行を`uv run --frozen`経由にし、GPU作業はWSL 2 / Ubuntu / RTX 4090で行う。

| 項目 | 確認済み | 次回に必要なこと |
|---|---|---|
| データ | train 756,087,912 unique stream tokens、Web 100%、全raw/cluster/shard監査 | 現在のhashと保存先を確認。追加取得・再構築は通常の再開条件にしない |
| WSD | stable 200 vs 100+100、decay 100 vs 50+50、全state・履歴完全一致 | batch/backend/実装変更後に同じ厳密検証を通す |
| GPU設定 | eager/math、FP32 parameters＋BF16、batch 8 / accumulation 1 | NoNorm/mathの最大安定batch・compiled/mathは未測定。実運用の容量と最速設定を測る |
| 過去の速度 | Phase 5採用構成の定常中央値121,139 tokens/s、peak allocated約3.866 GiB | 拡張shard/WSDで再測定。Phase 4のNorm/default最大batch 64・約44万tokens/sを流用しない |
| 資源 | 準備完了時のLinux空き950,875,688,960 bytes、data約15.43GB、CUDA run約1.45GB | 開始時に再確認。data容量はraw約2.15GBを含まないapparent bytes |
| 品質・配布 | Phase 5のgreedy EOS 0/80、反復54/80、sampling Unicode 2/240 | 未達を維持。NoNorm HF/GGUF adapterも未実装 |

復元済みTokenizer/pilot、Phase 3 export、Phase 5比較、完了済み①②を再実行しない。新jobの前にWindows/Linux process、GPU compute一覧、job status、PID/boot ID/start ticks、lock、checkpoint SHAとsource snapshotを照合し、二重起動を防ぐ。

## ③ 容量・高速化: 安全に速い運用設定を選ぶ

目的はVRAM使用率と実速度を測り、保存・評価・再開が成立する運用設定を決めること。最大容量と最速batchを別に記録する。VRAMを埋めることだけを採用基準にしない。

採用model config・拡張shard・WSD・batch/backend/compileを固定する[scripts/phase6_performance.py](../scripts/phase6_performance.py)と[独立監査](../scripts/audit_phase6_performance.py)を実装した。凍結比較と実CLIは[③の詳細](28_phase6_performance.md)。既存の[scripts/benchmark_training.py](../scripts/benchmark_training.py)はPhase 4のNorm config / pilot / cosine用で、[準備verifier](../scripts/verify_phase6_preparation.py)は①②のbatch 8/math専用として保持する。旧reportを上書きせず、backend実効・cache分離を含む新規runで検証する。

比較は同じmodel/Tokenizer/data hash、context、precision、optimizer、seedを保つ。実験configには短いprobeと最終確認の予算を別記する。提案する探索順は以下。

1. eager/math batch 8を基準に、16、32…と倍増してOOM境界を見つけ、中間値を探索する。単一backendの容量probeは最大16設定とし、境界が見つからなければ「測定範囲内の安定上限」と記録する。
2. compiled/mathはまずbatch 8で厳密resumeを確認する。通過した場合だけ、mathで速かったbatchと容量付近を比較する。compile/defaultの既知の失敗を同じ条件で繰り返さない。修正を試す場合は原因・変更点・対照・打切り条件を先に固定する。
3. 各backendの最速候補と容量上限を、cold startとは別の**3×200完了更新**で確認する。有限loss/gradient/weights/optimizer、保存・評価、失敗理由と全metricsを保持する。
4. 採用する各構成でstable 200 vs 100+100、decay 100 vs 50+50のtoken列/loss/LR/model/optimizer/scheduler/RNG/sampler全state完全一致、元stableの不変性と継続一致を確認する。未通過の高速経路は採用しない。

測定値は初回起動/compile時間、定常tokens/s・更新時間分布、data wait、total wall time、peak allocated/reserved・driver側VRAM、GPU利用率、checkpoint容量・保存時間、評価時peak/時間。容量probeは固定した小dev sample（例: 4文書＋1 prompt/8 new tokens）を使用し、全文評価や400生成とは区別する。最速設定を選ぶ際に、実際の評価batchと保存で必要なVRAM余裕も確認する。MFUを出す場合はFLOP算定方法を記録し、GPU利用率をMFUと表示しない。

**完了条件**: 有限値・厳密再開・3回の運用確認を通過した最大安定値と最速値、採用理由、失敗、容量余裕、更新数・effective tokens/updateを保存する。③の結果は速度・再現性の証拠であり、生成品質の達成ではない。将来成果物: `batch_performance_report.json`、`batch_choice.md`、設定ごとのraw logs/checkpoints/source snapshots。

## ④ 生成・変換: 既知の失敗を切り分ける

採用NoNormのnative prefill/cache一致とEOS=3の停止契約を確認する。Phase 5のcheckpointと生成IDを起点に、Unicode破綻・反復・EOS未到達の具体例を保存し、decode/cache/停止実装の問題とモデル出力を区別する。

比較は固定Base dev 80 prompt×5条件の400生成を使い、greedy・抑制なし診断・sampling seeds 42/43/44を別集計する。生成制約やdecode修正は同一checkpoint・prompt・seed・最大長で比較し、抑制による改善をモデルの能力と混同しない。変更候補は最大2案の対照として先に固定し、効果がなければ結果を保存して保留する。文法等のrubricは実施範囲・採点者・分母を明示し、自動flagを文法70%達成の証拠にしない。

NoNormのHF/native float GGUF adapterを実装・検証する。外部SentencePieceによるID契約、float logits parity、cache、停止を既定の数値条件で確認する。変換が成立しない場合は原因と修復予算、保存済みNorm対照への構成見直しを記録する。構成を変える場合は③の容量/再開と公平な品質比較も再確認する。学習後の量子化品質・容量・独立ローカル検証はPhase 8として残す。

拡張devは**89,416文書 / 164,344,743 body bytes**で、Phase 5 pilotの924文書とは母集団が異なる。新corpusのBPB基準を別に作り、全文採点時間と400生成の時間を実測する。Phase 5の約5.4分/400生成を、新dev全文を含む評価全体の保証にしない。小sample probeを最終dev評価として扱わず、testは選定に使わない。

**完了条件**: native/cache/停止と変換の実装契約を確認し、400生成の失敗・対照結果、未達品質、次の修復または学習による検証方針を残す。Base品質目標の達成は本学習後に判断する。将来成果物: `generation_diagnostics.json`、`nonorm_export_parity_report.json`、修復・採否記録。

## ⑤ 本学習設定・予算を凍結し、500Mから段階評価する

③のbatchでeffective tokens/updateと更新数が変わるため、Phase 5のLR 0.002を無条件に最適値としない。採用batchで小予算の安定性を確認し、変更が必要なら一要因の対照・token/byte/GPU時間予算・打切り条件を先に固定する。比較予算は③の測定から見積もり、長期開始前にconfigへ保存する。

凍結項目はmodel/Tokenizer/data/source hash、seed、backend/compile/precision、micro/effective batch・accumulation、LR/warmup/weight decay/clipping、stable終端予算、各観測点とdecay枝の追加予算・minimum LR ratio、保存/評価間隔・保持checkpoint数、空き容量上限、予定反復、実CLIとrestart command。stable終端は10B系列の計画予算として固定し、各地点は`--stop-after`で区切る。丸め後の実tokens/updatesも記録する。

| 累積stable tokens | 現train streamへの露出（算術値） | 確認すること |
|---:|---:|---|
| 500M | 約0.66回 | 拡張corpusでの初期BPB、Unicode・反復・停止、有限値と保存再開 |
| 1B | 約1.32回 | 同一devでの改善、paired CI、文法、生成長と失敗率 |
| 2B | 約2.65回 | 継続価値。過去355M modelが取得できなければ直接比較未実施と明記 |
| 5B | 約6.61回 | 本命1構成、10Bまでの追加時間/容量、データ反復の影響 |
| 10B | 約13.23回 | Base v1の固定評価、checkpoint/config/Tokenizer/manifest/model card |

本系列は拡張trainの新規初期化から開始し、Phase 5終端cosine checkpointの予算を変更して延長しない。各観測点のWSD decayは別runへ分岐し、stable累積tokensと枝の追加tokens/bytes/GPU時間を分ける。既存CLIでは`--schedule-updates`は**global update数**で、decay枝の終端は分岐元update＋`--decay-updates`。通常resumeは凍結した全引数を維持する。

既存WSDはstableのLRを終端によらず維持できるが、**stable予算の延長forkは未実装**。現在の通常resumeはbudget/source/data変更を拒否し、`--branch-from`はdecay専用である。20B/50Bへ延長するPhase 9では、明示的な継続forkの仕様・履歴・全state検証が必要。追加corpusでも現在のPhase 6 dev/testを保護する入力・provenance機能が必要で、現builderのPhase 1 pilot保護だけで継承済みとは扱わない。変更系列を同一runの通常resumeにしない。

**完了条件**: 凍結config、実起動/再開command、GPU排他、PID/boot/start ticks、log・heartbeat・source snapshot・checkpoint SHAと復旧手順を保存し、500M以降を段階評価する。意味のある実装・測定・観測点ごとにstatus/reportを更新して指定Git名義でcommitし、pushしない。発散・非有限・再開不一致は修復まで停止、品質退行は原因と対照を記録する。10B到達を自動的な品質合格としない。

将来成果物: 本学習run config、scaling checkpoints、`base_scaling_report.json`、`base_v1_evaluation.md`、model card。これらは未作成。Base文法70%以上等の[凍結目標](15_project_roadmap.md#品質目標と判断ルール)を維持する。ChatはPhase 7、量子化/配布はPhase 8、20B・条件付き50BはPhase 9の別系列。

## 時間と再開入口

現候補のPhase 5実測による参考computeは500M約1.15時間、10B約22.93時間。これは純粋な学習の算術値で、③④の実装・検証、新dev全文評価、cold compile、保存、decay枝、修復を含まない。作業全体の完了時刻は③の測定後に更新する。[現在の予算](24_phase6_plan.md#暫定のcompute見積もり)

次回は[最新状態](autonomous_status.md)、本書、[引継ぎ](windows_handoff.md)を読み、process/source/dataの確認から始める。③の既存studyを確認して重複起動せず、検証・commit後に停止する。④以降・本学習は開始しない。準備の中断復旧と別出力への読み取り監査は[実CLI](26_phase6_preparation_completion.md#実cliと再開)にある。
