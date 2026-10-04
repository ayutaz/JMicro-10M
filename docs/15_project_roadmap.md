# JMicro-10M フェーズ別実行計画

2026-10-04最新: 次計画1・2（明示stable延長・総5B学習）を[完了](../reports/phase6/base_5b_review.json)。同じ10M/既存12.23B train、追加3.10B科学tokensと別524,288検証tokens、最後約5%decayを含む総5,000,003,584。CPU6tests/実CUDA全state再開一致、連続・有限更新、parent不変、GPU75分43秒で上限内。品質は未評価で元Base/Chat基準は維持。記録・commit後停止し、次は未実行のstep3全文dev/固定生成比較。10B/Chat/sweepへ自動移行しない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: ユーザーが次計画1・2（継続処理実装と総5B学習）を再開。[5B実行計画](35_base_5b_execution.md)。stable1.9Bから予算のみを延長する明示fork、Web100%、最終約5%decay、元品質基準を維持。学習完了/report/commitで止め、step3全文評価と10B/Chatは未開始。学習量到達と品質達成を区別する。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: [低学習率の計画1〜3を完了](../reports/phase6/eos_low_lr_100m_review.json)。旧ログ/3保存点の調査、同じ元2BからLR曲線0.1倍の各100M、同じ全文89,416dev/各400生成を実行。BPB Web0.972969/short0.974799で元2B0.982882を改善、固定EOS0→27/80/反復55→41、生成失敗0。原mixture/全文/増量gateは全合格、12関連testsと実CUDA全state再開一致、GPU35分41秒で45分上限内。ただし意味反復/文脈誤りが残りBase/Chat品質基準は未達。report/commit後停止し、5B/Chat/自動sweepは未開始。[実状態](autonomous_status.md)。以下は経過履歴。

2026-10-04最新: [完結単位の各100M対照と全文評価を完了](../reports/phase6/eos_complete_100m_review.json)。固定自然EOS0→24/80、補助0→42/80、自動mixture gate合格。ただし意味誤り/反復が残り、両100M枝の全文BPBは元2Bより悪化。短文枝は診断候補として保持し、元2Bを基準にする。原Base/Chat品質目標は未達、WebのUnicode退行により5B条件も未達。関連24 tests成功/実CUDA全state再開一致、全GPU job実終了、累積GPU55分5秒で原45分予算超過を記録。report/commit後に停止し、5B/Chat/自動sweepは開始しない。以下の計画のみ/未実行は履歴。[実状態](autonomous_status.md)。

2026-10-04次の[計画を更新](27_phase6_remaining_plan.md)：32〜64-token完結単位を準備し同じ2B親からWeb対short20%を各100Mで1回比較、固定80/dev256と補助短文80、採用条件は維持。比較/必要な全文評価で一区切り。Web100Mに重大退行がなければ、別のWeb100% stable延長forkで総5Bを検討し、5B結果から10B/必要Base品質/Chatへ進む。mixture採用gateとBase/Chat品質目標を分け、失敗を消さない。今回は計画のみ、100M/5Bの実行は未開始。[提案と予算](../reports/phase6/eos_next_plan.json)。以下は履歴。

2026-10-04短文混合の[対照学習を完了](../reports/phase6/eos_short_pilot_review.json)。同じ2B親から各25,001,984 input tokens、Web対短文20.0524%混合。固定80 greedy64のEOSは両方0/80、反復62→54/80、共通dev256 BPB1.068518→1.069161（+0.06025%）。EOS改善gate未達で短文条件を未採用、conditional全文再評価を省略。対照実験として完了し元2B基準/両新checkpointを保持、report/commitで停止。5B/Chat未開始。次の32〜64-token完結単位比較は未起動案で、pool/予算凍結を先に行う。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04 EOS調査を完了：[実測と改善案](../reports/phase6/eos_2b_review.json)。真の末尾EOS argmax35/256→46/256と改善するが、同じ20ケースのgreedyは512 tokensでも停止0/20/反復20/20。penalty1.1は停止5/20（435〜491 tokens）/反復20/20で解決には足りない。固定64-token基準は維持。次の比較案は短い完結train文書20%混合と既存Webの25Mずつ2枝、改善確認後に手元12.23Bを使う5B学習へ増量。学習比較/5Bは未開始。全件監査を繰り返さず、[実状態](autonomous_status.md)を参照する。以下の停止境界/実行中記録は履歴。

2026-10-04最新: [実train12.23Bデータ整備とユーザー指定2B学習・既存評価を完了](../reports/phase6/base_2b_10b_data_review.json)。同じ約10Mモデルで、減衰込み総2Bを実行。既存dev BPB1.022491→0.982882、greedy反復66/80→60/80、EOS0/80。品質目標は未達のままreport/commitして停止する。5B/10B/Chat・decoder比較は未起動。以下の学習中・旧停止境界の説明は履歴。[実状態](autonomous_status.md)。

2026-10-04: [ローカルデータ整備](32_local_10b_corpus.md)は実train12.23B tokensで完了。ユーザー指示で過剰な独立再照合を省き、構築時の全件検査・独立raw再構築・実train loader合格を採用し、独立全件audit未完了を明記した。さらにユーザーが2B学習を指定し、同じ約10Mモデルを新データで別runとしてGPU学習中。減衰込み総2B、既存protected dev/生成比較、report/commitで停止する。5B/10B/Chat・生成方法の対照比較は未起動。[現在の実状態](autonomous_status.md)。

2026-10-03: 500M後の反復/EOS/data調査も完了。[判断と比較](../reports/phase6/repetition_diagnosis_review.md)。EOS教師漏れは確認されず、文書末尾予測は改善し、反復は131Mから多い。decay後は70/80→66/80。原因をデータ量へ確定せず、次の対照を提案して停止。追加学習/1Bは未開始。

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新結果](../reports/phase6/base_500m_review.json)。

作成日: 2026-10-02。最終更新: 2026-10-03（Phase 6①〜⑤の準備完了・次回本学習の計画と凍結予算を更新）。根拠は[プロジェクト目的](01_project_goal.md)、[設計](03_architecture.md)、[技術調査](11_technical_research_gaps.md)、[Phase 0完了記録](16_phase0_completion.md)、[Phase 1完了記録](17_phase1_completion.md)。既存の**確定**方針から逆算した計画であり、将来の成果物名・未凍結の実行値は**提案**である。品質目標・評価契約はPhase 5で凍結済みで、結果を見て緩めない。

## 最終的に実現すること

約10Mパラメータの日本語専用モデルをランダム初期化から学習し、日本語短文生成と2〜数ターンの雑談をローカルで実行する。コーパス選別、独自Tokenizer、Base事前学習、Dialogue mid-training、Assistant-only SFT、量子化までを再現可能なpipelineとして残す。

最終成果物は次の三つに分ける。

1. `JMicro-10M-Base`: 日本語短文生成の基準モデルと評価結果。
2. `JMicro-10M-Chat`: 関連した短い返答、話題継続、文脈維持、停止を評価した会話モデル。
3. 再現・利用一式: 学習コード、config、Tokenizer、データmanifest、再開可能checkpoint、量子化artifact、ローカル実行手順、実験台帳。

目標規模は9.5M〜10.1M parameters、初期contextは1024 tokens。5〜10MB級は量子化配布の目標であり、Tokenizer等を含む実容量、推論メモリ、品質を測って達成を判断する。高度な推論・コード生成・長文RAGは今回の成功条件へ加えない。

## 現在地と計画の使い方

2026-10-02にiMac上のPhase 0を実施し、uv管理の開発基盤、準備run、環境記録、評価仕様・固定suiteを作成した。[Phase 0完了記録](16_phase0_completion.md)を参照する。モデル・Tokenizer・学習前exportはPhase 2〜3で実装・検証済み。学習器と4090 benchmarkはPhase 4で完了した。本学習と学習後の品質・配布検証は未実施。文献で確認した内容を実機検証の完了として扱わない。

**Phase 0〜5、Phase 6①〜⑤の準備と500M評価が完了。1B前で停止**。[Tokenizer完了記録](18_phase2_completion.md)、[モデル・export完了記録](19_phase3_completion.md)、[Phase 4実機結果](21_phase4_completion.md)を参照する。Phase 5のoverfit・10M smoke・100M比較と候補選定も完了した。[完了記録](23_phase5_completion.md)を参照する。Web 19,998文書と3,000対話を採用し、cluster単位のtrain/dev/test、trainだけのTokenizer用sample約4.50MBを作成した。source台帳・manifest schema・全件復元・6成果物の再生成一致・20件の内容レビューを[完了記録](17_phase1_completion.md)にまとめた。

Phase 0の22件のテスト成功と54ファイルの準備run snapshot検証を記録済み。Base/Chat各100件（各dev 80/test 20）、前処理golden 30件、手動採点例11件を利用する。Phase 3完了時には全48テスト、両モデル×3 backendの実CLI 6件、79 source filesとruntime source 3,673 filesの監査が成功した。Phase 3までのデータは小規模pilot。4k/8k Tokenizerは学習済みで、両モデルのCPU検証も完了。Phase 4では64 tests、GPU検証checkpointとeager最大安定batch T8K 57 / T4K 64を確認した。Phase 6①②では756M unique train stream tokensの拡張corpus全件監査、WSDの73 GPU checks、全74 tests / skip 0を確認した。50〜100B master全量と完成したBase/Chat重みはまだない。

Pythonは`.python-version`の3.12.7、依存変更は`uv add`、環境再構築は`uv sync --frozen`、実行は`uv run --frozen`で統一する。データ処理時は`--extra data`（PyArrow、datasketch、fsspec、aiohttp）、Tokenizer・モデル検証時は`--extra ml`を指定する。両extraを同時に使う処理では両方を指定する。GPU/CUDA互換性はPhase 4で確認済み。

Phase 0〜5とPhase 6①〜⑤の成果物は各完了記録に実pathを示す。[①②の完了記録](26_phase6_preparation_completion.md)にあるcorpus/shards・WSD検証checkpoint・reportは存在する。本学習の凍結configは[version2](../configs/phase6/base_frozen.json)として検証済み。scaling checkpoint・Base/Chat完成artifactは**今後作成するもの**で、準備検証artifactと区別する。コードは`src/`、設定は`configs/`、検証は`tests/`、実行入口は`scripts/`を基本とする。小さな比較結果・判断記録は`reports/<run_id>/`、大型データ・重みは[外部データ領域](07_environment.md)へ置く。`docs`には仕様、計画、成果物への参照を残す。

別PCで再開する時は[Windows/WSL＋RTX 4090の手順](windows_handoff.md)を入口とする。新規PCではコードと固定Hub成果物を復元して環境を確認する。Phase 5・Phase 6①〜⑤と文書更新のコミットは未pushなので、最新のWindows正本も引き継ぐ。復元済みPCでは完了作業を繰り返さず、③の完了commit `a7d26e1`、④⑤の`93c7d1d`とsource/dataを確認し、本学習の再開指定まで停止する。

各フェーズは、成果物が作られ、完了条件を証拠で確認した時に完了とする。条件を満たさない場合は修正・再比較へ戻り、未達事項を次フェーズへ黙って持ち越さない。現在の凍結予算は⑤の693,666 tokens/sを基準に500M約12分・10B約4時間の純学習算術値。500Mの独立decayと全文dev/400生成を含め約24分、10Bまでの全5枝/評価は約5時間21分。起動/compile/保存/人手確認/実装/修復は別で、日付の締切を保証しない。

## 全体の順序

| Phase | 状態 | 実行環境 | 目的 | フェーズ終了時のゴール | 前提 |
|---:|---|---|---|---|---|
| 0 | 完了 | iMac | 成功条件と実験の契約を固める | 設定・記録・評価仕様を作成し検証済み | [完了記録](16_phase0_completion.md) |
| 1 | 完了 | iMac | 目的に合うデータを追跡可能にする | 小規模Base corpusと会話pilot、独立した評価splitを用意する | [完了記録](17_phase1_completion.md) |
| 2 | 完了・[証拠](18_phase2_completion.md) | iMac | 日本語を小語彙で安定して表現する | 同じsampleで学習した4k/8k Tokenizerが契約を満たす | 1のsample・split |
| 3 | 完了・[証拠](19_phase3_completion.md) | iMac / CPU | 10Mモデルと推論経路を成立させる | 正しいモデル・cache・HF/float GGUF経路を確認する | 2 |
| 4 | 完了・[実機証拠](21_phase4_completion.md) | Windows/WSL＋RTX 4090 | 長時間学習の再現性と実行可能性を確かめる | 保存再開・実shard学習・4090速度と予算を検証した | 1〜3 |
| 5 | 完了 | Windows/WSL・RTX 4090 | 小予算で有望な候補を選ぶ | overfit、10M smoke、100M比較から最大2候補を選ぶ | 4 |
| 6 | 準備①〜⑤・500M完了、1B以降未着手 | Windows/WSL・RTX 4090 | 日本語Baseの能力を段階的に伸ばす | 500M→1B→2B→5B→10Bで評価し、Base v1を固定する | 5、[準備完了証拠](30_phase6_readiness_execution.md) |
| 7 | 未着手 | Windows/WSL・RTX 4090 | Baseを短文雑談モデルへ仕上げる | mid-trainingとSFTの効果を分離し、Chat v1を評価する | 6、1の会話pilot |
| 8 | 未着手 | 学習PC・独立したローカル検証環境 | ローカルで使える成果物を完成させる | Base/Chatと量子化版を独立環境で実行・再現できる | 7、3のexport経路 |
| 9 | 未着手・50Bは条件付き | Windows/WSL・RTX 4090 | 追加学習に継続価値があるか検証する | 20B、条件付き50Bの効果と限界を報告する | 6、追加予算の見積もり |
| 10 | 未着手・後半研究 | ローカル中心、後半にVast.ai並列比較 | baselineを越える追加研究を行う | 共有・蒸留・hybrid・規模比較の採否を証拠で決める | 8、固定したbaseline |

Phase 0〜8を最初の完結した開発系列とする。Phase 9は20Bの評価と、改善継続時のみ50Bへ進む系列。Phase 10は後半研究であり、最初のChat完成を待たせない。

Phase 1の会話pilotは準備済みで、拡張と評価準備をBase学習と並行して進める。Phase 6で10B Baseが成立すればPhase 7へ進め、20B・50BをChat開始の前提にしない。単一4090ではGPU実験を順番に実施し、CPUでのデータ整理・評価準備を並行する。

**確定（実行場所）**: Phase 0〜3はiMacで実施し、Phase 4からWindows/WSL＋RTX 4090へ移行済み。Phase 4のNorm/default eager運用上限はT8K 57 / T4K 64。Phase 6③ではNoNormのreference/math最大45、compiled/math最大53、compiled Flash最大111を検証。最速はFlash＋compile reduce-overhead batch 32、694,521 tokens/sで、容量上限と最高速度を分ける。[高速化完了記録](29_phase6_performance_completion.md)、[移行成果物・確認条件](07_environment.md)

## 高速に完成させる進め方

**確定（優先方針）**: ユーザーは完成までの時間短縮を優先する。Windows/WSLへの切替とPhase 4は完了した。Phase 5の候補選定まで完了し、Phase 6①〜⑤と500M評価が完了・1B前で停止。Phase 3をGPUで最初からやり直すことは移行の前提にしない。

Phase 3の最終検証一式はM1 iMac上で24.62秒。これは実装後の検証時間で、コード作成・修正、Tokenizer学習、runtime初回build、docs更新を含まない。作業全体の約25分と区別し、GPUへの変更で実装時間まで短縮すると見積もらない。[実測report](../reports/phase3/export_parity_report.json)

Phase 4は以下の順で実施済み。新規環境への移行・実装変更時にもこの検証順を使う。すべてのPhase 4完了条件は維持する。

1. **移行・CUDA確認**: GitのコードとGit管理外のTokenizer/pilotを引き継ぎ、hash/ID一致、GPU/driver/PyTorch/BF16を確認する。Macのnative binaryや仮想環境はコピーしない。
2. **最小の学習経路**: 検証済みモデルを使い、AdamW/BF16、uint16 shard、本文NLL/BPB・生成評価、checkpointを実装する。まず小batchでfiniteな1 stepまで成立させる。
3. **保存再開の検証**: 同じ環境で連続200 stepsと100→保存→再開100 stepsを比較し、消費token列・loss・weightsを確認する。
4. **速度と最大batchの実測**: batchを倍増して境界を見つけ、中間値で最大安定値を測る。compile初回と定常速度、backend、syntheticと実shardのI/O、評価・保存時のVRAMも記録する。最大安定batchと最高速度のbatchは両方残す。

変更した箇所と関連gateを検証し、関係のないPhase 1取得・Tokenizer再学習・CPU GGUF全検証を繰り返さない。artifactを変更した場合、移行先で数値差が出た場合、学習済みモデルを配布する場合は対応する検証を再実行する。

最初のChat完成に必要なPhase 0〜8を優先し、20B/条件付き50B、Muon等の追加比較、hybrid、クラウド並列研究はbaseline成立後に進める。小探索では主要因を一つずつ比較し、総当たりを前提にしない。データは次の段階で使う量から準備し、master corpus全量取得を学習開始の条件にしない。

**時間見積もり**: 「学習開始まで1〜2日、初版Chatまで1〜3週間」は会話中の粗い仮見積もりで、確定scheduleへ採用しない。実装作業時間とGPU計算時間を別々に記録する。変更後の採用設定で検証済みのPhase 6③のtokens/secから`残りtokens / tokens/sec + 評価・保存・比較runの時間`を計算し、段階ごとに更新する。品質の修正が必要な場合は追加実験を別に見積もる。

## Phase 0: 成功条件・環境・実験管理

**状態**: 完了。詳細な実path・検証範囲は[完了記録](16_phase0_completion.md)と[完了監査](../reports/phase0/completion_audit.json)を参照する。以下は実施した内容で、Windowsの実機確認はPhase 4へ残す。

実施時点のhashとsnapshotは履歴として保存する。計画やREADMEの更新で現fileが変わった場合も、過去runのsnapshotと監査を上書きしない。Tokenizer/data入力のartifact hashは作成前のため`null`で、各フェーズの完成後に実fileを記録する。

**目的**: 学習できたことと、狙った短文対話が成立したことを区別して判定できるようにする。

**ゴール**: runを再構築できる記録形式と、結果を見る前に固定した評価仕様がある。

作業:

- リポジトリ骨格、依存version固定、run ID、artifact naming、seed管理、config schemaを作る。
- iMac側の環境を記録し、Windows/WSL用の依存設定と移行手順を用意する。WSL 3.xの実導入version、GPU、driver、OS、PyTorch/CUDA、ストレージの実機確認は切替時に行う。
- Base評価、Chat評価、tokenizer契約、数値誤差、停止ID、公開対象のデータbucketを仕様化する。
- Base completionとChat各100件の独自prompt suiteを作成し、各dev 80件・最終test 20件へ分けた。Chatは挨拶、感情応答、質問返し、訂正、2〜数ターンの文脈を含む。

**成果物（作成済み）**: [experiment schema](../schemas/experiment_schema.json)、[iMac環境記録](../reports/phase0/environment.json)、[評価仕様](evaluation_protocol.md)、[固定promptとsplit](../eval/README.md)、[実行入口](../scripts/experiment.py)、`pyproject.toml`・`uv.lock`・`.python-version`。

**完了条件**: 同じrun IDからcode commit、config、依存環境、データ/Tokenizer hashを特定できる。Chat rubric、BPB分母、generation設定、dev/testの用途が明記される。評価例を手で採点し、ルールの曖昧さを修正する。

**次へ進む判断**: iMac上の設計・データpilot・Tokenizer・CPU実装検証は進められる。4090の実機記録は移行時のgateとし、Phase 4のGPU検証と学習開始前に確認する。

## Phase 1: データの小規模pilotと評価split

**状態**: 完了。[実施結果・実path・限界](17_phase1_completion.md)、[全件検証](../reports/phase1/verification.json)、[再生成一致](../reports/phase1/reproducibility.json)を参照する。Phase 0の共通前処理を使い、[処理コード](../src/jmicro/data.py)と[実行入口](../scripts/prepare_phase1.py)を作成した。

**目的**: 日本語短文・雑談へ容量を使い、出所不明の混合や評価漏洩を避ける。

**ゴール**: 100M探索まで使う小規模corpusと、Chatに使える会話候補の実量・品質が分かる。

取得に使用したsource:

| source | 確認したrevision・条件 | pilotでの扱い |
|---|---|---|
| FineWeb2 Edu Japanese / `small_tokens_cleaned` | revision `180ca004c6a89b590daaad86cb062a07a5353c69`。配布READMEにODC-By v1.0とCommon Crawl利用条件を記載 | 小規模Web pilotに採用。READMEで先頭0〜9,999行と10,000〜19,999行の重複を告知しているため、先頭10,000行を避け、取得後にも重複を検査する |
| RealPersonaChat | revision `28d0b6b3865b29cabc26c230a2db37cdf315e937`。LICENSEはCC BY-SA 4.0 | 会話pilotに採用。Webとは別bucketで出所・条件を記録し、persona・人口統計metadataは学習入力へ含めない |

根拠: [FineWeb2 Edu Japaneseの固定revision README](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese/blob/180ca004c6a89b590daaad86cb062a07a5353c69/README.md)、[RealPersonaChatの固定revision LICENSE](https://github.com/nu-dialogue/real-persona-chat/blob/28d0b6b3865b29cabc26c230a2db37cdf315e937/LICENSE)。取得済みmetadata・形式確認用previewは`data/phase1/source_metadata/`に保存した（Git管理外）。調査metadataは処理入力へ流用せず、固定revision原fileを取得してpilotとsplitを作成した。証拠のURL・revision・取得file hashはsource台帳へ固定済み。

**実施した取得範囲**: [config](../configs/data/pilot.json)へschema、保存先、容量上限、選択方法を固定し、Web 20,000文書、会話3,000対話を取得した。採用はWeb 19,998文書、会話3,000対話、合計42,647,826 canonical UTF-8 bytes。取得数とfilter後の採用数を分け、unique量・反復回数・実際の学習tokensを別に報告する。100M tokensの探索に不足する場合は取得範囲の拡張または明示した反復で対応し、unique 100M tokensを取得済みとは扱わない。

実施項目:

1. source台帳とdocument/dialogue manifestのschemaを作り、source/subset/revision・利用条件・raw/canonical hash・cluster・splitを記録できるようにする。
2. 確認済みrevisionを台帳へ固定し、少量sampleの取得範囲・容量上限・保存先を決めて本文を取得する。viewer previewのrevisionと固定revisionを混同しない。巨大データ全量の取得は先行しない。
3. sampleを共通前処理、filter、dedupへ通し、train/dev/testを固定する。Phase 0の`eval/`はモデルの固定生成suiteであり、新しいcorpus splitとは別管理する。
4. trainだけからTokenizer学習sampleを選ぶ。4k/8kで同じdocument集合・順序・hashを使えるようにする。
5. 使用条件を満たす短文会話候補で1k〜10k対話のpilotを作り、件数・応答長・turn数・品質をreportする。教師tokensはPhase 2で実計数する。

作業:

- [データ設計](05_dataset.md)に従ってsource/subset/revision、利用条件、raw/canonical hash、品質、splitを持つmanifestを作る。未確認sourceは採用を保留する。
- FineWeb2 Edu Japanese等から小subsetを取り、弱い前処理、言語・品質filter、日本語向けexact/near/cross-dataset dedupをpilotする。
- duplicate cluster単位でtrain/dev/testを分離してからTokenizer学習sampleを選ぶ。
- 使用条件を満たす候補から1k〜10k対話のpilotを作る。speakerの向き、personaの扱い、tree復元、window化前のsplitを確認する。
- domain別bytes、短文比率、会話長、品質のsample目視を記録する。会話の定型挨拶を文書重複と同じ基準で一律削除しない。

**成果物（作成済み）**: `data/phase1/processed/`の`dataset_manifest.parquet`、`split_manifest.json`、`corpus.jsonl`、`tokenizer_sample.jsonl`。data/dialogue report・レビュー・検証・再生成比較は`reports/phase1/`。[詳細・checksum・再生成手順](17_phase1_completion.md)

**完了条件**: 任意の採用文書・対話をsourceとsplitへ追跡できる。既知重複とtrain/eval間の検出重複を除外し、未検出の限界も記録する。対話件数、unique bytes、応答文字数、turn数の分布が分かる。1024-token内に収まる割合と教師token数はPhase 2で計測・追記する。

**次へ進む判断**: 会話候補が不足する場合は独自会話例でmask/評価の開発を進めつつ候補を追加する。量の不足を、同じ少数対話を反復した見かけのtokensで解決したことにしない。

## Phase 2: 4k/8k Tokenizerと会話形式

**状態**: 完了。[実施結果・artifact・再現手順](18_phase2_completion.md)。同一sampleで全6coverage候補が合格し、両語彙で0.9995を採用。外部codecのgolden・全corpus round-tripと会話token量を実計数した。

**目的**: 小語彙でも日本語・記号を扱い、学習とローカル推論で同じID列を使う。

**ゴール**: 語彙4096/8192の二つのSentencePiece Unigram + byte fallback artifactと、共通の入出力契約がある。

作業:

- 同じtrain sampleでcoverage候補を比較し、必須文字・256 byte pieces・8特殊tokenを含む予算を確認する。
- 正規化、空白、改行、タブ、結合文字、顔文字、未知文字のgolden例を固定する。
- role/EOTを構造IDとして挿入し、本文中の同じ文字列表記と区別する。学習後の語彙追加を避ける。
- domain別chars/token、bytes/token、fallback率、context超過率と会話の総/教師tokensを測る。

**成果物**: 4k/8kの`tokenizer.model`、設定・sample hash、`special_tokens.json`、`tokenizer_contract_report.json`、`tokenizer_comparison.json`。

**完了条件**: piece数と特殊IDが期待値と一致し、golden例が定義したcanonical textへround-tripする。全byte piecesと異常入力を検証する。同じartifactでencode結果が再現でき、再学習時の一致範囲も記録される。

**次へ進む判断**: 圧縮率だけで勝者を決めず、両候補をPhase 5へ渡す。4kが予算内で成立しない場合はcoverage/前処理を再検討し、語彙数を黙って変更しない。[詳細仕様](13_tokenizer_dialogue_data_research.md)

## Phase 3: モデル・cache・学習前export

**状態**: 完了。[実施結果・artifact・再現手順](19_phase3_completion.md)。両モデルの実parameter数・forward/backward・1024までのcache、公式HF・native float GGUF、Q8/Q4の読込生成を検証。内蔵Tokenizerに不一致があるため外部SentencePiece経路を採用した。

**目的**: 10M予算と正しい因果生成を満たし、長期学習後に推論形式で詰まるのを防ぐ。

**ゴール**: T8K/T4Kがforward/backward・cache生成・保存読込でき、配布経路の計算とTokenizerを検証できる。

作業:

- RMSNorm、RoPE、GQA、head間gain共有QK-Norm、SwiGLU、tied embeddingを実装する。
- parameter count、未来参照遮断、GQA mapping、padding、finite gradientを検証する。
- prefill、1-token decode、chunk decode、長さの違うcacheで全系列logitsとの一致を検証する。
- ランダム重みをHF参照モデル、float GGUFへ写し、同じ入力IDsでlogits/cacheを比較する。
- 内蔵Tokenizerのgolden parityとEOT停止を検証する。不一致なら外部SentencePieceでencode/decodeする呼び出し経路を実装する。
- Q8/Q4候補で読込・生成、tensor別量子化型、FFN幅576/640でのfallbackと実容量を確認する。

**成果物**: T4K/T8K config、`model_contract_report.json`、`export_parity_report.json`、実行可能な推論入口。

**完了条件**: 提案仕様のQK-NormありでT8K=9,772,800、T4K=10,002,816 parameters。cache/因果性の検証が通り、floatの数値差が事前定義した許容値内。選んだ配布経路で学習時と同じTokenizer契約を再現できる。

**次へ進む判断**: 外部SentencePiece経路ならその依存も配布計画へ含める。汎用GGUF CLIへの互換性は別項目として記録する。ランダム重みの量子化成功は会話品質の成功を意味しない。[モデル仕様](12_training_implementation_research.md)、[export仕様](14_evaluation_deployment_research.md)

## Phase 4: 学習器・shard・再開・4090 benchmark

**状態**: 2026-10-03に完了。WSL 3.0.1.0 / Ubuntu WSL 2 / RTX 4090でCUDA/BF16確認と64 tests / skip 0、両モデルの200 vs 100+100完全一致、全dev・固定生成suite、最大batch・backend/compile・予算を実測・監査した。[完了記録と測定の制約](21_phase4_completion.md)を参照する。Phase 5も[完了](23_phase5_completion.md)し、Phase 6①〜⑤と500M評価が完了・1B前で停止。

**目的**: 長期runを失わず、実際の計算・ストレージ予算に収める。

**ゴール**: 実shardでの学習・中断再開が成立し、以降の実験時間を実測から見積もれる。

作業:

- `uint16` shard、document index、checksum、mmap loader、決定的shuffle/mixture samplerを作る。
- GPU実機検証の前にWindows PCのWSL 3.x/Linuxへ切り替え、同じcommit/config、Tokenizer、sample、hashを引き継いでCUDA動作を確認する。
- AdamW、FP32 parameter + BF16 autocastを基準にloss、gradient accumulation、schedulerを実装する。
- model/optimizer/scheduler/RNG、消費済みデータ位置、tokens/steps、全hashを保存する。optimizer更新境界で保存し、一時fileからのatomic renameを行う。
- Phase 0の準備run記録を基に、学習runの開始/完了/失敗、checkpoint、metricsのschemaと台帳を追加する。準備runの`tokens_seen=0`を学習結果として流用しない。
- Baseの本文NLL取得、window/strideの採点、BPBと生成suiteの実行を実装する。共通bytes・本文を一度だけ採点することを検証し、Phase 5の比較前に評価runnerを使えるようにする。
- 連続200 stepsと100 steps→保存→再開100 stepsを同一環境で比較する。
- T4K/T8Kのsynthetic/実shardでmicro batchを最大安定値まで増やし、compile、backend、data wait、peak VRAM、保存時間を測る。micro batchとeffective batchを区別する。

**成果物**: 実機`environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`、復元可能checkpoint。

**完了条件**: Windows/WSLへ移行済みで、CUDA動作と引継ぎartifactの一致を確認する。再開前後の消費token列が一致し、loss/weightsが同一環境で許容誤差内。累積lossの正規化、shard境界、評価によるRNG干渉を検証済み。BPB runnerの本文一度採点・共通bytes分母と固定生成suiteの実行を確認する。compile初回と定常速度を分け、実shardで運用できる最大安定batchと速度が分かる。

**次へ進む判断**: `予定tokens / 実測tokens/sec + 評価・保存・停止・分岐の時間`で100M/1B/10B/20B/50Bを見積もる。raw、一時領域、4k/8k shards、checkpointの容量を合算する。予算外ならまずbatch/I/O/探索本数を調整し、実験条件を台帳へ記録する。

## Phase 5: overfit・10M smoke・100M比較

**状態**: 2026-10-03に完了。4本の100Mと補助予算を評価し、T4K / NoQK-Norm / LR 0.002を1候補に選定。全68 tests / skip 0、CUDA厳密resumeと独立監査が成功。品質の未達も[完了記録](23_phase5_completion.md)へ保存し、Phase 6①〜⑤と500M評価が完了・1B前で停止。

**目的**: 実装不備を小予算で見つけ、長期学習へ渡す候補を根拠で選ぶ。

**ゴール**: 100M時点で発散しない候補を最大2つ選べる。

作業:

- 小データ100件のoverfitでloss低下と学習例の再現を確認し、別runで10M-token smokeを行う。
- 100MでT4K/T8Kを比較する。次にQK-Norm有無、LR、必要ならMuon+AdamWを、一度に一つの主要因だけ変えて比較する。全組合せの総当たりは前提にしない。
- 同じvalidation文書のBPB、共通短文window、生成失敗、実時間、処理bytes、更新回数を保存する。
- 同一tokens、同一学習bytes、同一GPU時間の条件を区別する。補助比較は対応するcheckpointまたは別runで行い、条件が揃わない結果へ同じラベルを付けない。

**成果物**: `smoke_report.json`、`tokenizer_model_comparison.json`、候補config、`candidate_selection.md`。

**完了条件**: finite loss/gradient、保存再開、EOS生成の検証が通る。BPBの改善と失敗率の推移を比較でき、候補選定理由・棄却理由を記録する。100Mで自然な雑談が完成することは要求しない。

**次へ進む判断**: 候補がすべて発散・悪化する場合はデータ、mask、LR、batchを切り分けてPhase 2〜4へ戻る。BPB差が小さい場合は速度・fallback・生成失敗・推論互換性を含めて最大2候補を残す。

## Phase 6: 500M〜10B Base v1

**状態**: 準備①〜⑤と500M stable/decay/評価は完了し、1B前で停止。756M unique train stream tokensのcorpus全監査とWSD stable/decayのCUDA全state再開一致を確認した。[準備完了記録](26_phase6_preparation_completion.md)。③はFlash＋compile batch 32、694,521 tokens/s、独立1286 checks・cold再開26 checks・79 testsを通過し、証拠は`a7d26e1`へcommit済み。④の生成/全文dev/CPU精度profileによる学習済み変換と⑤のLR3候補/厳密cold再開/設定version2凍結も`93c7d1d`で完了した。[高速化完了記録](29_phase6_performance_completion.md)。今後は[段階評価/gate](24_phase6_plan.md)と[残りの実行計画](27_phase6_remaining_plan.md)に沿い、ユーザーの再開指定後に凍結条件を照合して500Mの新規Base学習を始める。

**目的**: 約10Mで日本語短文生成がどこまで成立するかを測り、Chatの土台を作る。

次回の一区切りは[拡張データでの500M学習・評価計画](27_phase6_remaining_plan.md#次回の一区切り-拡張データで500mを学習評価する)。500M stableと独立decay、固定dev比較・report・commitまでを提案し、そこで停止して1B以降の判断を残す。今回は計画作成のみで本学習を開始しない。

**ゴール**: 5Bまでに本命1モデルへ集約し、10Bの`JMicro-10M-Base-v1`と固定評価を残す。

| 累積tokens | 目的・判断 | 残すもの |
|---:|---|---|
| 500M | 初期改善と反復悪化の確認 | checkpoint、BPB/生成/速度 |
| 1B | 日本語生成の立ち上がり、候補最大2つ | 比較表、候補更新理由 |
| 2B | 過去355M/約2B経験との観察点整理 | 規模・Tokenizer・データ差を明記した記録 |
| 5B | 本命1つの決定 | 選定reportと継続config |
| 10B | Base v1の固定評価 | weights、Tokenizer、model card、全評価 |

作業:

- pilotで検証済みの処理を拡張し、50〜100B master corpus候補を段階的に構築する。実取得/利用可能量と独自Tokenizerのunique量を報告し、候補目標量と混同しない。
- 各段階に必要なshardsから用意し、未使用全量の処理を10B開始の前提にしない。
- BPB、短文品質、反復、EOS、Unicode、追加GPU時間を段階ごとに記録する。
- 固定mixtureのscaling系列を残す。目的に合わせたmixture変更は別条件として記録する。
- Phase 5でWSDを採用し、Phase 6②でstable/decayの実装・CUDA全state再開/分岐完全一致を確認済み。本学習のbatch/backend/数値配分は[version2](../configs/phase6/base_frozen.json)へ凍結済み。継続stable枝と評価decay枝を区別して追加computeも計上する。20B/50Bへのstable予算延長forkは未実装で、通常resumeでは予算を変更しない。

**成果物**: 段階checkpoint、`base_scaling_report.json`、`base_v1_evaluation.md`、継続用checkpoint、master corpus manifest。

**完了条件**: 本命の10B checkpointを再構築・再開でき、固定suiteとheld-out corpusの結果がある。短文の文法・関連性と破綻例を人手で確認し、[品質目標](#品質目標と判断ルール)の達成/未達を明示する。過去モデルのartifactがない場合は直接比較を未実施と明記する。

**次へ進む判断**: Baseの日本語生成が成立すればPhase 7へ進む。成立しない場合は量だけを増やさず、日常短文mixture等の対照実験を行う。修正後も未達なら容量・データの限界として報告し、成功扱いにしない。

## Phase 7: Dialogue mid-trainingとAssistant-only SFT

**目的**: 流暢な続きを生成するBaseから、入力に関連した短い応答で会話を続けるChatへ移す。

**ゴール**: 文法・関連性・2〜数ターンの文脈・停止を評価した`JMicro-10M-Chat-v1`を作る。

作業:

- Phase 1の会話pilotを拡張し、sourceごとのunique対話/bytes/総tokens/Assistant教師tokens/反復回数を固定する。
- Dialogue mid-trainingのmixture、loss範囲、LR、pilot予算と拡張上限を開始前にconfigへ記録する。
- 主系列はBase→mid-training→SFT。小規模なBase→SFT対照を残し、mid-trainingの効果を分離する。
- role metadataからAssistant本文+EOTの教師maskを作る。shift、PAD、教師0件、長い対話の古い完了turn切り捨てを検証する。
- SFTの累積総系列10M→30M→100M tokensを候補とし、毎段階devで比較する。教師token数とunique量は別記録し、悪化時は100Mまで強制継続しない。
- Base、mid-training後、SFT後を同じ固定prompt/seedで比較する。greedyと複数seed sampling、人手rubricと自動失敗率を分ける。
- Phase 0の固定履歴suiteに加え、モデル生成を履歴へ戻す2〜数ターンのrolloutと自動失敗flagを実装する。モデル名を伏せた人手評価と評価者一致率を記録する。

**成果物**: 会話manifest、`assistant_mask_report.json`、各段階checkpoint、`chat_ablation_report.json`、`chat_v1_evaluation.md`。

**完了条件**: mask/停止の検証が通り、独立した対話splitで評価済み。採用checkpointがdev上で関連性・文脈を改善し、反復・役割混同・空応答・停止失敗・Base流暢性の退行を報告する。最後に未使用testで品質目標を判定する。

**次へ進む判断**: 最良checkpointを選びPhase 8へ。未達なら応答長/品質/mixture/LR/反復回数を一要因ずつ見直す。蒸留を使う場合はcorpus-only baselineと別系列にする。

## Phase 8: 量子化・ローカル実行・再現手順

**目的**: 学習結果を手元で使える形にし、容量と品質の実際のtradeoffを示す。

**ゴール**: Base/Chatのfloat版と採用量子化版を、学習環境以外でも手順から起動できる。

作業:

- 学習済み重みでPhase 3のHF/float GGUF parityとcache/停止を再実行する。
- Q8とQ4候補を比較し、tensor別実型、file容量、Tokenizer込み全artifact、RSS、cacheメモリを測る。
- 対象CPU/OS/threadsを明記し、load、初回token時間、prefill/decode、応答総時間のp50/p95を測る。context1024は生成分も含めて管理する。
- floatとの差をBPB、人手関連性/文脈、Unicode、反復、role/停止で確認する。
- model card、採用source一覧、帰属、既知の限界、hash、runtime commit、量子化設定、実行/再現コマンドを揃える。

**成果物**: Base/Chat artifacts、`quantization_report.json`、`local_inference_report.json`、`reproduction_guide.md`、配布manifest。

**完了条件**: 独立環境でBase completionと2〜数ターンのChatが動く。学習時と同じencode/decode、EOT/EOS停止が成立し、量子化の退行を品質条件内に収める。全容量・速度・必要依存を実測値として提示する。

**次へ進む判断**: Q4が品質を満たさなければQ8/混合精度も比較する。5〜10MB級へ収まらない場合はサイズ目標未達を明記し、形式/precisionの追加検証を残す。artifactを用意したことと品質・容量目標達成を区別する。外部公開・Hub uploadはこの文書作成では実行しない。

## Phase 9: 20Bと条件付き50Bのscaling

**目的**: 固定10Mモデルへ追加学習する価値と、容量/データ反復の限界を確認する。

**ゴール**: 10B対20Bの差を測ってBase v2を評価し、50Bへの進行/停止を根拠で決める。

作業:

- stable予算延長の明示forkと履歴・全state検証を実装してから継続用checkpointで20Bへ進み、固定mixture・同じ評価条件で10Bと比較する。通常resumeで終端budgetを変更しない。
- document単位のpaired bootstrapでBPB差と95%信頼区間を記録し、短文品質、失敗率、uniqueデータ露出と追加GPU時間を併記する。
- 50Bは20Bでも改善継続があり、生成失敗が悪化せず、追加時間/ストレージが予算内の場合のみ進む。
- 新Baseが有望なら同じChat手順を適用してv1と比較し、Phase 8の学習済みexport/量子化評価も再実行する。

**成果物**: `base_v2_evaluation.md`、`scaling_extension_decision.md`、実施した場合の50B checkpointと限界report。

**完了条件**: 20Bの比較と50B Go/No-Goを記録する。50Bを実施した場合は評価まで完了する。実施しない判断にも改善量、信頼区間、失敗率、予算の証拠を付ける。

**次へ進む判断**: 小さい改善しか残らない/悪化する場合は停止し、データ適合性またはPhase 10の比較へ移る。decay済み評価枝とstable継続枝の履歴を混同しない。

## Phase 10: 追加研究とVast.ai並列比較

**目的**: 完成したTransformer baselineと比較して、能力密度・計算効率をさらに改善する。

**ゴール**: 変更ごとに同じ目的・評価条件で採用/棄却を判断できる。

優先順はLayer Sharing（12 unique/24 logical）、teacher応答テキスト蒸留、ReLU²、Mamba2+Attention、Conv+Attention、5M/10M/25M/50M/100M規模比較。各実験では「改善したいmetric、parameter/compute予算、同一条件、採用基準」を先に記録する。異なるTokenizer間のlogitsをindexで直接KL比較しない。

Vast.aiはローカルで検証済みの独立runを並列化する後半用途に限定する。利用時の価格で再見積もりし、既存方針の上限$1,000に対して実験別計算時間・storage・失敗時費用を計上する。この計画作成で課金jobを開始しない。

**成果物**: 追加研究proposal、対照run、`research_comparison.md`、費用/速度/品質の台帳。

**完了条件**: 実施した各変更をbaselineと比較し、採否・限界を記録する。採用案は再現性、Chat評価、export、量子化まで再検証する。候補全部の実施を最初のBase/Chat完成条件にはしない。

**次へ進む判断**: 品質または速度が事前の採用基準を満たす変更だけを次の比較へ進める。改善が不明確な変更は結果を保存して保留し、追加computeで得られる情報と費用から再実験の優先度を決める。

## 品質目標と判断ルール

技術的完了と能力目標を別に管理する。Phase 8までのartifact・検証が揃っても、以下が未達なら「目的を達成した」とは記載せず、未達metricと次の対照実験を残す。

以下の数値はPhase 5の100M候補の結果を見る前に、初期提案を維持して**凍結済み**。10Mで達成できると実証した値ではない。Phase 0でsuiteと採点例を定め、Phase 5のdev/pilot評価では未達もそのまま記録する。変更理由と旧値を記録し、最終testを見て閾値を下げない。量子化の退行幅はfloat dev評価後、量子化候補選定前に別途固定する。[凍結の記録](22_phase5_plan.md#公平な評価と候補選定)

| 目的 | 判定方法・初期目標 | 判定するフェーズ |
|---|---|---|
| 日本語短文生成 | Base completionの文法2/2が70%以上。文字/記号の破綻と反復も別集計 | 6 |
| 入力に関連する短い雑談 | Chatの文法・関連性が両方2/2の応答が70%以上。文字数分布も併記 | 7 |
| 2〜数ターンの文脈維持 | 2〜4ターンsuiteで直前の条件/訂正を保持し、文脈2/2が60%以上 | 7 |
| 会話の停止と役割 | 停止成功95%以上、空応答5%以下、役割漏出1%以下、Unicode破綻は固定suiteで0件 | 7・8 |
| 量子化して使える | 全artifact容量5〜10MB級を目標に、floatとのBPB/品質/失敗率差を報告。許容退行幅はfloat dev評価後、量子化候補選定前に固定 | 8 |
| 長期学習の継続価値 | BPB改善幅（10B BPB − 20B BPB）の95%信頼区間の下限が0を越え、生成失敗に重大退行がなく追加予算内なら50B候補 | 9 |

停止等の失敗率はgeneration抑制設定を併記し、ID列で測る。人手評価はモデル名を伏せ、文法/関連性/文脈を各0/1/2で採点する。率は分母とsample数を付け、全体だけでなくcategory別も報告する。関連性が伸びても反復が増える等の重大退行は採用判断へ反映する。

品質条件はdevで選定し、独立testで最終確認する。testで未達なら結果を報告し、次の改訂では新たな未使用testを用意する。[評価の詳細](14_evaluation_deployment_research.md)

## 横断して残す記録と最初の着手順

全runでcode commit、config、依存version、Tokenizer/data hash、seed、tokens seen、unique docs/bytes/tokens、更新数、micro/effective batch、wall time、失敗理由を残す。SFTでは総系列tokensとAssistant教師tokens、WSDでは分岐ごとの履歴を分ける。比較する条件を変えたら別run IDにする。

Phase 0〜4の骨格・データpilot・Tokenizer・両モデル/cache/export・Windows/WSL移行・学習器・評価・保存再開・実機速度は完了済み。Phase 5のoverfit/smoke・4本の100M比較・候補選定が完了し、Phase 6①〜⑤と500M評価が完了・1B前で停止。巨大コーパス全量取得、50B開始、追加hybridを先行しない。

具体的な着手checklistは[次の実装タスク](10_next_steps.md)、各技術判断の根拠と実測待ち項目は[追加調査](11_technical_research_gaps.md)を参照する。
