# Phase 6④以降: 最新の実行計画

更新: 2026-10-03。①②は[完了済み](26_phase6_preparation_completion.md)、③も[完了](29_phase6_performance_completion.md)。採用はFlash/compile reduce-overhead、batch32、694,521 tokens/s。ユーザー指定で④生成/変換・⑤設定確定を再開し、[固定比較と途中結果](30_phase6_readiness_execution.md)を保存した。400生成・全文dev・3 LR比較・変更後sourceの厳密/cold再開に加え、CPU精度profileで元の全12変換比較と実CLI監査149 checks、全90 testsが成功。本設定をversion2へ凍結し、本学習前で停止する。品質閾値と完全一致の要求を維持する。

## 出発点と、今回繰り返さない作業

採用候補はT4K / NoQK-Norm / AdamW / LR 0.002、10,001,152 parameters、context 1024。モデルconfigは[候補台帳](../reports/phase5/candidate_configs.json)、実装・データの証拠は[独立監査](../reports/phase6/completion_audit.json)を正とする。Python 3.12.7の全実行を`uv run --frozen`経由にし、GPU作業はWSL 2 / Ubuntu / RTX 4090で行う。

| 項目 | 確認済み | 次回に必要なこと |
|---|---|---|
| データ | train 756,087,912 unique stream tokens、Web 100%、全raw/cluster/shard監査 | 現在のhashと保存先を確認。追加取得・再構築は通常の再開条件にしない |
| WSD | stable 200 vs 100+100、decay 100 vs 50+50、全state・履歴完全一致 | batch/backend/実装変更後に同じ厳密検証を通す |
| GPU設定 | Flash＋compile reduce-overhead、FP32 parameters＋BF16、batch 32 / accumulation 1、context 1024 | 32,768 input tokens/updateを長期候補とする。reference/math最大45、compiled/math最大53、Flash/compile最大111は容量記録として保持 |
| 最新速度・メモリ | 694,521 tokens/s、最速reference/math比5.436倍、save/小sample評価込みpeak allocated5.73 GiB・driver7.53 GiB | 全文dev採点・400生成・保存/枝を別計上し、長期LR安定性と予算を⑤で固定 |
| 資源 | 準備完了時のLinux空き950,875,688,960 bytes、data約15.43GB、CUDA run約1.45GB | 開始時に再確認。data容量はraw約2.15GBを含まないapparent bytes |
| 品質・配布 | Phase 5のgreedy EOS 0/80、反復54/80、sampling Unicode 2/240。今回も品質未達 | NoNorm HF/GGUF adapter・実ID生成/停止は成立。CPU精度profileで長系列も検証済み。過去の未達を保持し、次回は本学習で品質を測る |

復元済みTokenizer/pilot、Phase 3 export、Phase 5比較、完了済み①②③を再実行しない。新jobの前にWindows/Linux process、GPU compute一覧、job status、PID/boot ID/start ticks、lock、checkpoint SHAとsource snapshotを照合し、二重起動を防ぐ。

## ③ 容量・高速化: 完了済み

凍結した7設定の実演算比較と容量探索、9設定のstable/decay全state再開・親の不変性、最速/容量6設定の各3×200更新・小sample評価/saveを完了した。独立1286 checks・cold-cache再開26 checks・79 testsはすべて成功。最速はFlash＋compile reduce-overhead / batch 32、32,768 input tokens/update、694,521 tokens/s。reference/math最速比5.436倍。最大安定batch 111・112 OOM、driver peak97.64%だが、速度では32が上回った。

実在成果物は[全結果](../reports/phase6/batch_performance_report.json)、[選定理由](../reports/phase6/batch_choice.md)、[資源・速度要約](../reports/phase6/performance_summary.json)。raw logs/checkpoints/source snapshotsはLinuxの完了runに保持。[詳細・条件・失敗](28_phase6_performance.md)、[完了監査と保存先](29_phase6_performance_completion.md)。完了した測定を再実行しない。source/model/backend/batch/contextが変わる場合は、影響する容量・演算・厳密再開gateを新runで再検証する。③の速度検証は生成品質・長期LR最適性の達成ではない。

## 再開後の順序と完了条件

| 順序 | 作業 | 完了の証拠 |
|---|---|---|
| ④-1 | 既存NoNorm checkpoint・固定Base dev 80 promptをbindし、native/cache/停止IDと400生成の失敗を診断 | 生成ID・greedy/抑制なし/sampling別のEOS/反復/Unicode・原因と最大2案の対照結果 |
| ④-2 | NoNorm HF/native float GGUF adapterを実装し、新dev全文採点時間を測る | 外部SentencePieceのID、float logits/cache/停止parity、BPBと89,416文書の採点時間・400生成時間 |
| ⑤ | batch 32候補のLR安定性・WSD・保存/評価/枝の予算を固定 | 凍結configと起動/復旧CLI、丸め後tokens/updates、容量・監視・停止条件 |
| Phase 6本学習 | 新規初期化から500M→1B→2B→5B→10B | 観測点ごとのdev BPB/CI・生成/rubric・失敗例、stableとdecay枝の別台帳、Base v1のartifactと最終評価 |
| Phase 7→8 | Dialogue mid-training/Assistant本文＋EOT SFT→量子化・独立ローカル検証 | Chat関連性/文脈/停止、float/quantized品質差、実容量・RSS/応答時間、再現手順 |

今回は④⑤の検証・commitまでを進め、本学習前で停止する。数値設定は[base_frozen](../configs/phase6/base_frozen.json)と[起動/復旧計画](../reports/phase6/base_launch_plan.json)へ保存し、CPU精度profileの変換gateも成功した。`launch_enabled=true`だが今回は本学習を起動しない。Chat trainer/mixtureと学習後量子化は未実装・未検証。20B/条件付き50B・追加研究はPhase 9/10の別予算として維持する。

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

③の定常実測694,521 tokens/sによる参考computeは500M約12分、10B約4時間。純学習の算術値で、④⑤の実装・検証、新dev全文評価、cold compile、保存、decay枝、LR調整を含まない。本学習設定は凍結済みで、作業全体の完了時刻の保証ではない。[現在の予算](24_phase6_plan.md#暫定のcompute見積もり)

次回は[最新状態](autonomous_status.md)、本書、[引継ぎ](windows_handoff.md)を読み、process/source/dataの確認から始める。③のstudyとcold再開は終了済みで、完了した測定を重複起動しない。③の証拠は`a7d26e1`へcommit済み。④⑤の準備検証は完了し、本学習は再開指定を待つ。準備の中断復旧と別出力への読み取り監査は[実CLI](26_phase6_preparation_completion.md#実cliと再開)にある。
