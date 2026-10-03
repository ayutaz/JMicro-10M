# 準備完了後の実行計画: Base本学習からChat・量子化まで

更新: 2026-10-03。Phase 0〜5とPhase 6①〜⑤の準備は完了。③は`a7d26e1`、④⑤は`93c7d1d`へcommit済み。[現在の状態](autonomous_status.md)、[④⑤の実測と停止記録](30_phase6_readiness_execution.md)。**計画1〜5の実行をユーザーが再開し、500M stable・独立decay・全文dev/400生成比較を完了した。現在は1B前で停止している。**

## 現在の実行: ローカル10Bデータセットの整備

2026-10-04更新: 実train12.23Bの整備は[ユーザー指定の検証範囲で完了](../reports/phase6/corpus_10b_ready_review.json)。過剰な独立再照合を停止し、構築時の検査・全raw再構築・実train loader合格を採用する。さらにユーザーが2B学習を指定し、新データの別runをGPUで実行中。最後の約5%減衰を含む総2Bで既存dev/生成比較を行い停止する。[現在の状態](autonomous_status.md)。以下の学習前停止・2B/5Bデータ増量案は履歴。

ユーザー指定により、下記2B/5Bの計画を[約10Bの取得・構築・監査](32_local_10b_corpus.md)へ更新して実行を開始した。10BはT4Kで測った学習用データ量で、10Mモデルのサイズや消費学習tokensではない。処理はWSL内のdiskへ置き、旧heldoutと過去成果物を保護する。全件監査/report/commit後に学習前で停止する。以下は以前の計画履歴。

## 次回の一区切り: 学習用データを2Bへ拡張する

2026-10-03のユーザー訂正に従い、次に取り組む対象をデータセット量の拡張へ変更する。仮説は「現在の学習用756,087,912 stream tokensでは、データの量・多様性が不足している可能性がある」。最初の完了目標は、品質処理後にT4Kで測った学習用stream tokensが合計2,000,000,000以上となること。追加2Bではなく合計2Bで、dev/testは含めず、同じ文書の周回を増量に数えない。5Bは後続の段階目標とする。モデルは10,001,152パラメータのまま。公開コーパスの規模、整備済みデータ量、モデルが消費した学習量を別々に記録する。

**今回は計画の訂正のみ。取得・データ構築・推論・学習は開始しない。次回のデータ整備を実行する際も、監査・報告・commitを一区切りにして学習開始前で停止する。** 生成方法の比較と短文mixture案は保留し、このデータ拡張の前提条件にしない。過去の計画・監査結果を実行済みの証拠として書き換えない。

| 順序 | 次回の作業 | 完了・判断条件 |
|---:|---|---|
| 1 | 既存job、保存先、Windows物理diskとWSL filesystemの空き容量、取得/構築CLIを確認する | 重複jobなし。raw・中間DB/JSON・shards・監査用一時領域を別計上し、処理時間と容量の予算を開始前に記録 |
| 2 | 固定FineWeb2 Edu Japaneseから追加取得する別config/manifestを作る | 既存revision、Tokenizer、品質filterを維持。初回計画の8files/最大16files・4.4GB上限では不足するため、凍結configを変更せず新しい条件を保存 |
| 3 | 新しいdirectoryへ構築し、既存trainと追加文書を一緒に重複除去する | 既存dev/test、pilotのheldout、固定評価suiteを保護し、検出された混入clusterを除外。既存raw/expanded-v2/shardsは保持 |
| 4 | train量・文書数・bytes・長さ/品質/source構成と全shardを監査する | train合計2B以上、hash/Tokenizer往復/index/token列整合、split分離を検証。完了しなければ未達と記録し、基準を緩めない |
| 5 | 準備結果、実時間/容量、残る偏り、次の学習比較案を報告してcommitする | 新manifest/hashとjob終了を保存し停止。2Bのデータ準備を2B学習完了や品質改善へ読み替えない |

取得量の暫定見積りは、現在8filesから756Mを得た比率で合計約22filesが2B、約53filesが5B。追加分の重複や品質除外で収率は変わるため保証ではない。次回2B整備の取得上限案は合計32files・raw10GB、後続5B案は合計64files・raw20GBとする。既取得分も上限へ含め、上限到達で目標未達なら部分成果と実測を保存して停止し、無制限に追加取得しない。中間成果物はrawより大きいため、このraw上限だけを必要disk容量としない。構築/監査の時間上限は少量の追加処理による実測後、全量処理の前に固定する。未実装の大規模処理・heldout保護・再開機能があれば先に実装し、関連検証を行う。

同じ短文subsetの追加では文書の多様性や短い完結文の比率が十分変わらない可能性もある。量だけで質が改善すると確定せず、分布を監査して報告する。2B整備後の学習では、学習tokens/同一dev/生成条件を揃えた旧データと拡張データの対照を別計画で定義し、データ量と学習量の影響を区別する。データ変更を既存stableの通常resumeへ混ぜず、新系列のlineageと全state再開を検証する。元のBase品質基準は維持する。

## 保留した案: 学習済み10Mモデルの生成方法を比較する

以下は以前の計画の履歴。現在の次回優先作業は上記のデータ拡張であり、この比較を先に開始しない。

2026-10-03の計画依頼。反復/EOS/dataの[調査は16cc38dで完了](../reports/phase6/repetition_diagnosis_review.md)。モデル規模は10,001,152パラメータ（約10M）のまま。500Mは学習したinput token数のmilestoneで、モデル規模ではない。比較に使うcheckpointは500,006,912 tokensのstable学習＋25,001,984 tokensのdecay後、合計525,008,896 input tokensを学習した10Mモデルである。

次回のゴールは、この学習済み10Mモデルの同じ重みを使い、反復抑制が文章の改善につながるかを測り、比較report・人手評価用packetを残してcommitし停止すること。[固定する比較条件と予算](../reports/phase6/repetition_decoder_plan.json)、[計画の16項目照合・WSL同期・234既存files保持](../reports/phase6/repetition_decoder_plan_audit.json)。これは計画の確認で、比較codeや生成品質の検証結果ではない。今回は計画作成のみで、推論・学習・データ変更を開始しない。以下の500M計画は実行前の履歴として保持する。

| 順序 | 次回の作業 | 終了時に確認すること |
|---:|---|---|
| 1 | 既存process・checkpoint/Tokenizer/suite/protocol/source hashを照合し、別の比較CLIと永続runnerを実装する | GPU重複なし、有限値・model/RNG不変、同じdecoderの再現、log/部分結果/予算を保った再開。凍結trainer/evaluator/configと過去結果を保持 |
| 2 | 同じdecay500Mで反復抑制1.0対1.1、dev80、greedy＋sampling3seedsを比較する | 各320、計640outputs。reference320の全generated IDsが既存reportと一致。64-token上限・temp0.8/top_p0.9・EOS3・元の抑制IDsを固定 |
| 3 | 反復/EOS/Unicode/role/emptyと長さ、同じpromptの改善・悪化、95% CIを集計する | sampling3seedsを同じpromptにまとめたcluster bootstrap、2000回/seed42。EOSを強制せず、文字化けや意味の反復を隠さない |
| 4 | 各10categoryの最初2dev casesを使い、20組/40文章のblind人手評価packetを作る | A/Bをseed42で匿名化しmappingを分離、文法・関連性0/1/2と意味の反復を点検。独立人手評価がなければ未実施と明記 |
| 5 | 改善・副作用・未達を報告し、statusを更新してcommitする | 比較結果と時間/hash/job終了の証拠、次の判断を記録して停止。短文mixture学習や1Bへ自動移行しない |

反復抑制1.1は、生成済みbody token IDの重複を一度だけ扱い、正logitを1.1で割り、負logitに1.1を掛ける。promptとspecial IDs0〜7は対象外。EOSへ直接加点したり、停止文字列や最小/最大長を変更したりしない。1.0は元の演算を完全に通す。BF16の元score dtype・sampling手順を保持する。比較機能はまだ未実装なので、次回は実装・検証してから起動する。

referenceはgreedy反復66/80・EOS0/80、sampling反復11/240・EOS1/240・Unicode失敗1/240。自動改善候補の目安はgreedy反復が8件以上減る（58/80以下）、sampling反復/EOSが悪化せず、candidate320のUnicode/role/empty失敗0件。これはdecoder候補の比較基準であり、既存のBase文法70%・EOS停止95%等の凍結品質基準を緩めない。20件のpacketと自動flagだけでBase合格や文章の自然さを宣言しない。

GPU推論の累積上限は15分。既存400生成367秒から計640は約10分の算術見積りで、CUDA probe/再開も同じ上限へ計上する。実装・検証・report込みは30〜60分の目安、人手評価や予期しない修復は別。上限で未完了なら部分結果と原因を保存して停止し、予算をリセットして再試行しない。同じ重みのdecoder比較なので、既存全文dev BPB1.022491はそのまま参照し、全文採点を繰り返さない。

実行はWSL2/Ubuntu/RTX4090、Python3.12.7を必要なextras付き`uv run --frozen`から起動する。学習の最速batch32/Flash/compile/BF16/fused AdamWは変更しない。推論batch化はreference全IDs一致を維持できる場合に限り同じ予算内で扱い、VRAM容量を埋めるための別研究は追加しない。

### その結果を見てからの学習比較案（次回のscope外）

反復抑制で文法が崩れる、意味の反復や停止未達が残る場合には、短い完全文書の教師を増やす対照を別の一区切りとして準備する。同じstable500Mをparentとし、原trainの既存decayを対照A、短文mixtureをBとする。Bはtrainの128body tokens以下の完全文書を使い、input tokensの20%を短文に割り当てる案（前回の未定義な「20%文書」を具体化した提案）。文の途中へEOSを付けず、dev/testや新sourceを使わない。

各armは763更新/25,001,984 input tokens、同じdecay schedule/seed42。optimizer/RNGのparent stateを保持し、Bの新samplerを別のlineageとして記録する。異なるdataでsampler位置まで同じとは主張しない。別loader/trainerを先に実装し、原data対照の互換性・有限値・厳密保存再開を確認する。凍結coreは変更しない。

対照Aの実条件・parent/全stateが一致すれば既存学習/評価を再利用し、無駄な再学習を避ける。A再生成が必要なら、前回の2arm/GPU20分案は全文評価2回だけで約25分必要なため予算を改めて凍結する。Aを再利用できる場合の後続案はCUDA再開gate5分＋Bの学習/全文dev/400生成20分上限、CPU準備・人手評価は別計上。現段階ではdata/実装/起動条件は未準備で、採否条件とともに次の独立計画で確定する。EOS密度と短文内容が同時に変わるのでEOSだけの因果効果にはしない。1Bの判断はその後とする。

## 次回の一区切り: 拡張データで500Mを学習・評価する

実行後の更新: 2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [実測](../reports/phase6/base_500m_review.json)。以下は実行前に固定した計画を保持する。

現在の判断: 生成反復とUnicode破綻に退行があるため、単純な1B延長を推奨しない。まず既存artifactのEOS教師量・文書長/短文promptの違い・反復・decoding差を調べ、対照・予算・終了条件を定義してから次の実験を提案する。今回は追加実験へ進まず、指定の1〜5を完了して停止する。

2026-10-03の次回計画依頼に基づく提案。次回のゴールは、準備済み拡張trainを使った500M Baseと独立decay枝を保存し、現在の100Mモデルと同じdevで比較して報告すること。**次回は500Mの評価・記録・commitを一区切りにして停止する計画とし、1B以降はその結果を踏まえた後続段階とする。今回の依頼は計画作成で、本学習は開始しない。**

| 順序 | 実施すること | 終了時に確認すること |
|---:|---|---|
| 1 | 既存process/checkpoint、source/data/runtime hash、GPU、空き容量を確認しprepareする | 重複jobなし、有効な再開点か新規runかを識別、凍結条件一致、最低空き200 GiB |
| 2 | seed42で新規初期化し、拡張trainで15,259 stable更新 | 500,006,912 input tokens、finite loss/gradient、全state checkpointと消費列・ログを保存 |
| 3 | stable終端から別directoryへ763更新の独立decay枝 | 終端global16,022、追加25,001,984 tokens、元stable不変、次回の継続点を保持 |
| 4 | decay終端の全文devと固定400生成を評価する | 同一89,416 dev文書のBPB、同一prompt/seed/上限のEOS・反復・Unicode・生成本文と時間 |
| 5 | 比較・失敗・改善候補・次の判断をreport/statusへ保存してcommitする | stable/decayのcheckpoint SHA、実tokens/bytes/GPU時間、基準との差、1B継続か原因調査かを報告し停止 |

データはpilotの18,022文書・T4K約8.398M stream tokensから、1,604,292文書・756,087,912 stream tokensへ約90倍に拡張済み。前回100Mの約11.91周に対し、新500M stableは約0.66周、独立decayを含む系列は約0.69周の算術露出になる。raw再取得やTokenizer再学習は開始条件にしない。データ量不足は仮説であり、今回はデータ・学習予算・scheduleも変わるため、結果だけでデータ量の因果効果を確定しない。

比較基準は現在の100M checkpointを同じ拡張devで測ったBPB **1.2441264716**、固定生成のgreedy EOS **0/80**・反復 **48/80**、全400出力のUnicode **0/400**。生成はdecoding条件別に集計し、文法・関連性は生成本文で確認する。旧pilot BPBとの単純差を改善量にせず、testは使わない。人手採点を実施できなければ未実施と残し、自動判定を人手評価へ読み替えない。

未統合のpaired CI/人手rubric集約は、次回の比較report作成に必要な実装と検証として別計上する。データ量だけの対照実験は今回の500M系列へ追加せず、結果が停滞・退行した場合に対照・予算・終了条件を定義して提案する。品質の達成基準は既存protocolを維持する。

学習＋独立decay＋機械評価は現実測から約24分。compile/保存/起動確認、比較reportの実装、内容確認、修復時間は別で、全作業の完了時刻は保証しない。失敗時は有効checkpointと原因を保持して修復し、同条件で再開する。有限値/hash/再開/容量に問題があるまま1Bへ進めない。

実出力はLinux `reports/phase6/base-20261003/`配下の`stable/`、`decay-500M/`、`evaluation-500M/full-dev.json`・`generation.json`、supervisor/log/snapshot。比較要約は今後作成する `reports/phase6/base_500m_review.json` と `base_500m_review.md`を提案する。checkpoint等の大型artifactはLinuxへ保持し、検証した小reportとstatusをGitへ保存する。

## 完了済みの準備と証拠

| 作業 | 検証結果 | 正本 |
|---|---|---|
| ①拡張データ | T4K train 756,087,912 unique stream tokens、1,604,292文書、Web100%。全raw/cluster/shard監査、dev/test分離 | [①②完了記録](26_phase6_preparation_completion.md) |
| ②WSD・保存再開 | stable/独立decay、model/optimizer/scheduler/RNG/sampler・token消費のCUDA完全一致 | [①②のGPU監査](../reports/phase6/completion_audit.json) |
| ③高速化・容量 | Flash＋compile reduce-overhead、batch32、694,521 tokens/s。最大stable batch111、112 OOM。32が111より速い | [③完了記録](29_phase6_performance_completion.md) |
| ④生成・全文評価 | 400生成360.684秒。greedy EOS0/80・反復48/80、Unicode0/400で品質未達。全文dev89,416文書、BPB1.2441264716、336.292秒 | [生成](../reports/phase6/generation_diagnostics.json)、[全文dev](../reports/phase6/expanded_dev_baseline.json) |
| ④学習済み変換 | NoNorm HF/Llama・GGUF/Llama。CPU精度profileで元の短/1024・full/cacheの全12比較、実CLI/重み監査149 checks成功 | [数値比較](../reports/phase6/nonorm_export_parity_report.json)、[独立CLI監査](../reports/phase6/readiness_export_audit.json) |
| ⑤設定凍結 | LR3候補から0.002採用。厳密50/cold25 checks完全一致、独立GPU106 checks、全90 tests成功 | [安定性](../reports/phase6/readiness_stability_report.json)、[設定version2](../configs/phase6/base_frozen.json)、[総合37 checks](../reports/phase6/readiness_gate_audit.json) |

GPU準備runの合計245,760,000 input tokensは独立した有限比較の台帳で、一つのBase本学習ではない。Phase 6全体の完了には10BのBase成果物と評価が必要で、①〜⑤完了と区別する。

CPU推論profileはFP32の重み/activation/cache/logitsとFP64累積を使い、成果物metadataから専用runtimeを適用する。stock runtimeでの実行を拒否し、未修正stock CPU/CUDA FP32の失敗を保持する。精度profileの成功をGPU学習速度や生成品質の改善へ読み替えない。学習のCUDA/BF16経路は変更していない。

## 再開時の最初の確認

ユーザーが本学習を再開した後、以下を確認してから500Mへ進む。

1. Windowsコード正本とLinux実行コピーのsource/hashを照合する。Linuxの旧Git HEADだけで現在の実装を判断しない。
2. 実GPU compute一覧、既存run/job、PID/boot ID/start ticks、GPU排他lock、checkpoint/latest.jsonを照合し、重複起動を防ぐ。
3. [凍結設定](../configs/phase6/base_frozen.json)のmodel・Tokenizer・shard manifest・source・検証artifact・runtime receiptを検証する。入力を変更する場合は新条件で必要なgateを再検証する。
4. 空き容量200 GiB以上、run出力上限100 GiB、checkpoint全保持の予算を確認する。データ再取得・Tokenizer再学習・完了済み比較を通常の再開条件にしない。
5. `run_base.py`のprepareで500M commandを確認する。新規Baseはseed42のランダム初期化から始め、Phase 5終端や準備比較のcheckpointを初期状態へresumeしない。

Python3.12.7の全実行は必要なextra付き`uv run --frozen`。依存変更は`uv add`、復元は`uv sync --frozen`。学習はWSL2/Ubuntu/RTX4090、Git identityは`yousan <ka1357amnbpdr@gmail.com>`。

## 500Mから10Bまでの段階評価

凍結条件はcontext1024、batch32、accumulation1、32,768 input tokens/update、FP32 parameters/BF16、fused AdamW、Flash/compile reduce-overhead/fullgraph/static/deterministic、LR0.002、warmup200、WSD global305,176更新。save1,000更新ごと・log50更新ごと。各観測点の独立decay枝は更新数の5%を切り上げ、最低LR比0.1。

| stable観測点 | global更新数 | 丸め後stable input tokens | 独立decay更新数 | decay終端global更新数 | 次へ進む判断 |
|---:|---:|---:|---:|---:|---|
| 500M | 15,259 | 500,006,912 | 763 | 16,022 | 有限loss/gradient・保存/再開・全文BPB・Unicode/反復/EOSを確認 |
| 1B | 30,518 | 1,000,013,824 | 1,526 | 32,044 | 同一dev文書のBPB差/paired CI、生成失敗と文法rubricを確認 |
| 2B | 61,036 | 2,000,027,648 | 3,052 | 64,088 | 継続価値と追加時間を判断。過去355M artifactがなければ直接比較未実施と明記 |
| 5B | 152,588 | 5,000,003,584 | 7,630 | 160,218 | 本命1構成と10Bまでの継続方針を固定。品質停滞に応じた対照は別系列 |
| 10B | 305,176 | 10,000,007,168 | 15,259 | 320,435 | Base v1の再開可能checkpoint・固定評価・model card、品質達成/未達を保存 |

各観測点のstableを保存し、別directoryへ独立decay枝を作る。そのdecay済みcheckpointに対して全文dev89,416文書と固定Base dev80 prompt×5条件の400生成を行う。次のstableは元のstable checkpointから同じglobal予算で継続し、decay枝をstable履歴へ戻さない。stable/枝ごとにtokens・教師tokens・body bytes・digest・GPU時間・親hashを記録する。

新dev全文の基準はBPB1.2441264716。同じ文書集合・前処理・CE精度・windowで比較し、旧pilot BPB1.221443との差を改善量にしない。文法などのblind人手採点は未実施。既存bootstrapを用いた段階間paired CI・人手rubricの集約は`run_base.py`の自動処理へ未統合で、必要なreport作成を別途実装・検証する。自動flagや合成停止fixtureを品質合格へ数えない。

モデル選定はdevだけで行い、testは最終確認まで保持する。発散・非有限・再開不一致・hash不一致・容量不足なら原因と有効checkpointを保存して修復する。重大な品質退行は対照条件を定義して調べ、閾値を下げない。10B到達だけでChatへ移行せず、[凍結品質目標](15_project_roadmap.md#品質目標と判断ルール)と日本語生成の成立を確認する。

## 実CLIと中断復旧

実commandの正本は[起動/復旧計画](../reports/phase6/base_launch_plan.json)。下記はWSLのproject rootでの確認で、本学習を起動しない。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003
```

**本学習再開が指定された後の実行例**。今回は実行しない。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003 --operation stable --execute
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003 --operation decay --execute
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003 --operation evaluate --execute
```

中断時はsupervisor.json・log・PID/boot/start ticksと実processを照合し、有効なlatest.json/checkpoint SHAを確認して同じcommandを再実行する。CLIがcheckpoint境界へ戻して再開し、500M完了後の1Bでは`--target 1B`へ変える。global終端305,176を変更せず、checkpointのない既存directoryを新規初期化しない。long GPU jobは排他/永続supervisor/heartbeat/source snapshot/checkpointで保持する。

500M+の実起動は未実施。prepare・未達gateでの拒否・有限準備runの実GPU再開は検証済みで、将来の長期run完了とは区別する。`launch_enabled=true`は技術条件の成立で、停止境界を解除しない。

## 実測に基づく予算と容量

⑤の採用LR0.002 runの定常速度693,666 tokens/sを使う。[凍結値](../configs/phase6/base_frozen.json)は③の694,521 tokens/sと別の測定予算である。

| 計上するもの | 算術値/実測 | 範囲 |
|---|---|---|
| stable500M | 約12分 | 学習のみ。独立decay・評価・保存・起動を含まない |
| 500M＋独立decay＋全文dev/400生成1回 | 約24分 | 現測定からの算術値。compile/保存/filesystem変動は別 |
| stable10B | 約4時間 | 累積stable系列のみ |
| 5観測点の独立decay全枝 | 約22.2分 | stableへの追加compute |
| 5回の全文dev＋400生成 | 約58.1分 | 336.292秒＋360.684秒/回。生成長による変動あり |
| 上記10Bまでの合計 | 約5時間21分＋その他の時間 | compile/起動/保存/人手評価/修復を除く。完成時刻の保証ではない |
| checkpoint | 推定347件・41,702,694,225 bytes | 全保持。run上限100 GiB、最低空き200 GiB |

最終checkpoint1件のsave0.435秒、compile込み初回update1.987秒は観測値で、cold compile上限や全保存の保証ではない。raw/data・venv/cache・一時領域は別計上し、開始時に実filesystemの空きを確認する。756M train streamは500M約0.66回、10B約13.23回の算術露出。反復量を新規データ量へ読み替えない。

## Base後の未実装・未検証と条件

| 次の系列 | 着手前に必要なこと | 完了の証拠 |
|---|---|---|
| Phase7 Chat | Dialogue mid-training/SFT trainer・Assistant本文＋EOT教師mask・shift・教師0件/turn切断・保存再開を実装して小予算で検証 | 関連性/文脈/停止、rolloutと人手評価、dev選定後の独立test |
| Phase8 量子化/ローカル | 本学習済みBase/Chatのfloat parityを再検証し、候補比較前に退行許容幅を固定 | Q8/Q4の実型・BPB/生成品質差・weights/全artifact容量・CPU RSS/応答時間・独立環境起動 |
| データ追加/mixture | 現Phase6 dev/testの保護・provenance継承と複数source loaderを実装。取得上限と変更系列予算を固定 | 旧heldoutを保護した新manifest/hash、source別量、変更後の再開/公平比較 |
| Phase9 20B/条件付き50B | stable予算延長の明示fork・履歴・全state再開を実装。通常resumeで予算変更しない | 10B→20Bのcommon-byte BPB差と95%CI、重大生成退行なし、追加予算内なら50B候補 |
| Phase10 追加研究 | 対照、改善metric、予算、採用/打切り条件を事前に定義 | Layer Sharing/蒸留/ReLU²/hybrid/規模比較の独立report |

現在の`--branch-from`はdecay専用。stable延長fork・mixture・Chat trainer・量子化後品質は未実装/未検証。初期Web100%の500M開始に50〜100B master全量取得を要求しない。ローカルで進め、外部の有料GPUや公開は別途の指定が必要。

意味のある実装・測定・観測点ごとにreport/statusを更新して指定名義でcommitし、pushしない。今回は文書/計画更新を検証・commitして停止する。
