最新完了（2026-10-05 JST）: 契約75の準備・各100M比較・品質未達による拡大非実行まで完了、結果docs/79_narrative_diversity_results.md。公開原文10000/1,206,453準備tokens（物語9000/Web1000）、固定64内容弱10/64、CPU9tests成功。元同一10Bから従来自然1000対新原文10000を各Web80M/short20M教師で学習、日本語全評価/専用dev64/160個別内容完了。基本意味58.333→64.583%、BPB0.980130→0.984834、EOS30→7、反復31→27、一貫性6→3、適切完結6→2。候補不採用、50k/5Mへの拡大・追加500Mは未開始。科学200M/valid・physical200,966,144、CUDA再開8更新260,794別、GPU500.023秒。比較actual395310/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9106956終了・不在。元UI395857/同boot/start9157480とHTTP親SHA410f975d…/10,000,007,168/busy=false確認。可搬narrative_diversity JSON/tests/raw gzipとLinuxrun/data/両optimizer込み終端保持。最初の準備失敗、非blind内容判定、source/長さ/EOS密度の交絡、結果72の数値7失敗も保存。次案docs/80_generation_transfer_plan.mdは正解対自由生成・64/256停止位置の診断から変更を一つ選ぶ計画で未開始。今回の範囲は完了、verified local commit後停止。新data/GPU/20B/Chat/test/pushなし。以下は履歴。

最新完了（2026-10-05 JST）: 契約73を段階4の品質未達/拡大非実行分岐まで完了、結果74。Adam引継ぎ/初期化各8Mはtrain64/64 gold＋EOS成功、別名dev127/128・128/128（同32scene）。規則でinherit選択。元同一10Bの従来/自然各25M教師・全日本語/160個別内容を完了。一貫性0→7、適切完結0→8、EOS10→26、反復48→30、BPB0.982188→0.983213。候補改善はあるが全品質基準未達、増量9192/追加100Mは未使用、不採用。科学66M/valid66,334,768/physical89,325,568、CUDA再開16更新215,168教師別、GPU484.284秒、CPU4tests・実学習/評価/完了監査成功。両job完了・不在、元UI actual379377/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8917553とHTTP親SHA/tokens/busy確認。可搬natural_learning各JSON/原文gzipとLinuxrun保持。次案は名前置換ではない多様な完結文と同量各100M比較で未開始。結果72数値7失敗は保持。verified local commit後停止、追加準備/学習/20B/Chat/test/pushなし。以下の実行中記載は当時の履歴。

進捗（2026-10-05 JST）: 契約73の段階2完了、両Adam各8M教師でtrain64/64完全再現＋EOS。inherit別名dev127/128、fresh128/128（同じ32sceneなので一般汎化ではない）。規則でinherit選択、新規重みC不要。科学16M、検証215168別、GPU186.757秒、終端full resume/教師会計/有限値/原文評価監査成功。段階3 compare actual378856/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8887284が元10Bから従来/自然各25Mを実行中。全160個別内容と日本語評価後、全既存gate合格時のみ段階4追加100M。元UI一時停止、終端復帰。重複起動しない。

実行中（2026-10-05 JST）: ユーザーの「4まで進めてください」で契約73を再開。自然64全文3426tokens、自然train1000全文52791tokens、条件付き増量9192全文501559tokens、未学習128を固定。32日常sceneの因果/対象/完結と64実原文をCodex確認、CPU4tests成功。A/B Adam引継ぎ/fresh各8M教師、必要時新規初期化C8M。記憶gate合格後に元10Bから従来/自然混合各25M、全日本語と160内容評価、全品質gate合格時のみ追加100M/増量。GPU各段階600/1200/1200秒、検証教師別。actual job-diagnostic/compare/expandを確認して重複起動しない。元UIを一時停止し各job終端で復帰。結果72の数値7失敗は保持。全範囲の結果/採否/local commit後停止、20B/Chat/test/pushなし。

最新完了（2026-10-05 JST）: 契約71の三項目＝計画70内部0〜2を実診断、結果72。32 train入力・三実重み・BF16生成384/FP32生成96・教材128全文確認。元10BのFP32 full/causal CE・gradient同一、cache/独立HF許容内。ただしpadding1要素/BF16 logitの計7checks失敗を保持。FP32でもoriginal/mixedの自然16件loop/停止未達が残る。mixedの条件16は全greedy/samplingでgold+EOS完全再現、既存story枝は短物語8/8EOSで展開改善。EOS無効化だけでは説明できず、自然文の教材適合/汎化/loop分布を優先。品質未解決、学習0/optimizer更新0。GPU63.439708秒、CPU4tests成功。raw bundle/summary/全文理由/完了証拠はreports/phase6/root_cause_*、Linuxrunはroot-cause-20261005。両job完了・不在、元UI actual374638/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start8753669、HTTP元SHA410f975d…/10,000,007,168/busy=false確認。verified local commit後に停止。自然短文64のAdam引継ぎ/fresh各8M比較は提案で未開始。追加学習/20B/Chat/test/pushなし。以下の実行中/計画のみの記載は履歴。

実行中（2026-10-05 JST）: ユーザーの三項目の再開範囲は契約71（計画70内部段階0〜2）。実装整合性、EOS/反復確率、教材適合性を診断する。32 train入力・128全文・三checkpoint SHAを凍結、CPU4tests成功。GPU占有上限600秒、学習/optimizer更新0。自然文記憶や次の学習比較は範囲外。元UIを一時停止し、診断終端で元10B UIへ戻して結果・local commit後に停止。reports/phase6/root-cause-20261005/job.json のactual PID/boot/start/logを確認し、重複起動しない。

最新提案（2026-10-05 JST）: [根本調査計画70](70_root_cause_investigation_plan.md)。実装の経路差→EOS/反復の発生点→必要な自然文陽性対照→原因別小比較→条件付き同10M設計比較の順。既存証拠を再利用し、単純増量や再学習を結論にしない。今回は文献/source/保存結果の調査と計画のみ、実行は未開始。下記の結果69・元品質目標は維持する。

最新完了（2026-10-05 JST）: [実行68](68_packing_learning_execution.md)段階1〜3、[結果69](69_packing_learning_results.md)。同教材の連結/順序変更/文書単位を各25M教師で実学習しtrain75/100/100、新dev74/85/76。shuffleを選び元10BからWeb80M＋短文20Mの各100Mを比較、対照train71/dev54→候補99/76。ただし一般自由生成は両一貫性0/適切完結0、EOS2/2、反復65/53（各80）で候補不採用。新五終端の日本語/全400個別内容評価、旧dev参照、24CUDA再開625,842教師別会計、106終端証拠checks完了。科学275M教師。Base/Chat品質未達、Phase7へ移行せず、元10B UI復帰・verified local commitで停止。次の多様な自然短文教材比較は提案のみ。以下の歴史的記録・原Phase定義と品質条件を維持する。
最新（2026-10-05 JST）: [契約66](66_condition_learning_diagnostic_plan.md)の四段階を実行、[結果67](67_condition_learning_diagnostic_results.md)。両追加24,969,216tokensでtrain75/68・未見65/61、目標未達で条件付き100Mは未開始。文脈付きtrain100%と単独の差を実測。全日本語・160内容評価済み、EOS改善のみでは一貫性/BPB未達で両不採用。Base/Chat品質未達、元10B UIを復帰してverified local commitで停止。次の文書単位学習比較は提案のみ。以下のPhase定義・原品質条件と以前の結果を維持する。

# JMicro-10M フェーズ別実行計画

最新（2026-10-05 JST）: 結果63後の四項目は別train32でselector v2を改修/凍結し、同source各20M/未確認全80を診断。対照弱例12/候補14で両内容gate未達、準備失敗分岐の採否・報告・元10B UI確認まで完了して停止。新GPUなし。状態はdocs/autonomous_status.md、結果はdocs/65_condition_selector_v2_preparation_results.md。以下のPhase定義と元品質条件は維持する。

作成日: 2026-10-02。最終更新: 2026-10-05（10Bと各100M/500M比較・日本語評価の実状態へ更新）。根拠は[プロジェクト目的](01_project_goal.md)、[設計](03_architecture.md)、[技術調査](11_technical_research_gaps.md)、[Phase 0完了記録](16_phase0_completion.md)、[Phase 1完了記録](17_phase1_completion.md)。既存の**確定**方針から逆算した計画であり、将来の成果物名・未凍結の実行値は**提案**である。品質目標・評価契約はPhase 5で凍結済みで、結果を見て緩めない。

## 最終的に実現すること

約10Mパラメータの日本語専用モデルをランダム初期化から学習し、日本語短文生成と2〜数ターンの雑談をローカルで実行する。コーパス選別、独自Tokenizer、Base事前学習、Dialogue mid-training、Assistant-only SFT、量子化までを再現可能なpipelineとして残す。

最終成果物は次の三つに分ける。

1. `JMicro-10M-Base`: 日本語短文生成の基準モデルと評価結果。
2. `JMicro-10M-Chat`: 関連した短い返答、話題継続、文脈維持、停止を評価した会話モデル。
3. 再現・利用一式: 学習コード、config、Tokenizer、データmanifest、再開可能checkpoint、量子化artifact、ローカル実行手順、実験台帳。

目標規模は9.5M〜10.1M parameters、初期contextは1024 tokens。5〜10MB級は量子化配布の目標であり、Tokenizer等を含む実容量、推論メモリ、品質を測って達成を判断する。高度な推論・コード生成・長文RAGは今回の成功条件へ加えない。

## 現在地と計画の使い方

2026-10-05 JST: Phase0〜5と主要Web10B、追加教材/学習量比較は完了。最新は[selector v2準備結果65](65_condition_selector_v2_preparation_results.md)。同source各20Mの未確認40各で弱例12/40→14/40、両内容条件未達で準備失敗分岐を完了、新GPUなしで停止。最新科学学習は[結果60](60_dataset_expansion_results.md): 物語60M→200M・各追加1B、常識改善/一貫性EOS未達で不採用。Base/Chat未達、Phase7へ移行していない。

モデル10,001,152 parameters、Web準備12,225,819,077 tokens、物語準備200,000,192tokens。主系列とUIは10,000,007,168学習tokens、最新二枝は各11,000,020,992tokens。別枝の合計科学2,000,027,648と検証262,144を区別する。長さ/source/EOS密度差を保持し、量だけの効果や容量限界は未確定。

今回の範囲は[実行64](64_condition_selector_v2_execution.md)の四項目の準備失敗分岐まで完了した。別train32でv2を凍結し、各20,000,072-token教材・長さ全並び/BOS/EOS一致・未確認全80を診断した。条件未達で各100M/条件付き全文を起動しない。次回案は結果65。新たな小教材設計/data/GPU/20B/50B/Chat/test/pushは未開始。状態は[status](autonomous_status.md)、移行は[引継ぎ](windows_handoff.md)、確認は[checklist](10_next_steps.md)を正とする。

以下のPhase定義・品質目標は維持する。以前の現在地と次の実行案は[2026-10-05履歴](autonomous_history_20261005.md)、各実験の当時の計画は各番号の文書へ保持する。結果や提案を新jobの開始指示として扱わない。20B/50Bと有料cloud/公開は別範囲。

## 全体の順序

| Phase | 状態 | 実行環境 | 目的 | フェーズ終了時のゴール | 前提 |
|---:|---|---|---|---|---|
| 0 | 完了 | iMac | 成功条件と実験の契約を固める | 設定・記録・評価仕様を作成し検証済み | [完了記録](16_phase0_completion.md) |
| 1 | 完了 | iMac | 目的に合うデータを追跡可能にする | 小規模Base corpusと会話pilot、独立した評価splitを用意する | [完了記録](17_phase1_completion.md) |
| 2 | 完了・[証拠](18_phase2_completion.md) | iMac | 日本語を小語彙で安定して表現する | 同じsampleで学習した4k/8k Tokenizerが契約を満たす | 1のsample・split |
| 3 | 完了・[証拠](19_phase3_completion.md) | iMac / CPU | 10Mモデルと推論経路を成立させる | 正しいモデル・cache・HF/float GGUF経路を確認する | 2 |
| 4 | 完了・[実機証拠](21_phase4_completion.md) | Windows/WSL＋RTX 4090 | 長時間学習の再現性と実行可能性を確かめる | 保存再開・実shard学習・4090速度と予算を検証した | 1〜3 |
| 5 | 完了 | Windows/WSL・RTX 4090 | 小予算で有望な候補を選ぶ | overfit、10M smoke、100M比較から最大2候補を選ぶ | 4 |
| 6 | 主要10B・各100M/500M/1Bと200M教材比較完了、品質目標未達 | Windows/WSL・RTX 4090 | 日本語Baseの能力を段階的に伸ばす | 学習量・配合・生成/意味診断を比較し、Base品質を別判定する | 5、[準備証拠](30_phase6_readiness_execution.md)、[最新判断60](60_dataset_expansion_results.md)、[次案61](61_condition_preservation_next_plan.md) |
| 7 | 未着手 | Windows/WSL・RTX 4090 | Baseを短文雑談モデルへ仕上げる | mid-trainingとSFTの効果を分離し、Chat v1を評価する | 6、1の会話pilot |
| 8 | 未着手 | 学習PC・独立したローカル検証環境 | ローカルで使える成果物を完成させる | Base/Chatと量子化版を独立環境で実行・再現できる | 7、3のexport経路 |
| 9 | 未着手・50Bは条件付き | Windows/WSL・RTX 4090 | 追加学習に継続価値があるか検証する | 20B、条件付き50Bの効果と限界を報告する | 6、追加予算の見積もり |
| 10 | 未着手・後半研究 | ローカル中心、後半にVast.ai並列比較 | baselineを越える追加研究を行う | 共有・蒸留・hybrid・規模比較の採否を証拠で決める | 8、固定したbaseline |

Phase 0〜8を最初の完結した開発系列とする。Phase 9は20Bの評価と、改善継続時のみ50Bへ進む系列。Phase 10は後半研究であり、最初のChat完成を待たせない。

Phase 1の会話pilotは準備済みで、拡張と評価準備をBase学習と並行して進める。Phase 6で10B Baseが成立すればPhase 7へ進め、20B・50BをChat開始の前提にしない。単一4090ではGPU実験を順番に実施し、CPUでのデータ整理・評価準備を並行する。

**確定（実行場所）**: Phase 0〜3はiMacで実施し、Phase 4からWindows/WSL＋RTX 4090へ移行済み。Phase 4のNorm/default eager運用上限はT8K 57 / T4K 64。Phase 6③ではNoNormのreference/math最大45、compiled/math最大53、compiled Flash最大111を検証。最速はFlash＋compile reduce-overhead batch 32、694,521 tokens/sで、容量上限と最高速度を分ける。[高速化完了記録](29_phase6_performance_completion.md)、[移行成果物・確認条件](07_environment.md)

## 高速に完成させる進め方

**確定（優先方針）**: ユーザーは完成までの時間短縮を優先する。Windows/WSLへの切替とPhase 4は完了した。Phase 5の候補選定まで完了し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。Phase 3をGPUで最初からやり直すことは移行の前提にしない。

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

**状態**: 2026-10-03に完了。WSL 3.0.1.0 / Ubuntu WSL 2 / RTX 4090でCUDA/BF16確認と64 tests / skip 0、両モデルの200 vs 100+100完全一致、全dev・固定生成suite、最大batch・backend/compile・予算を実測・監査した。[完了記録と測定の制約](21_phase4_completion.md)を参照する。Phase 5も[完了](23_phase5_completion.md)し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。

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

**状態**: 2026-10-03に完了。4本の100Mと補助予算を評価し、T4K / NoQK-Norm / LR 0.002を1候補に選定。全68 tests / skip 0、CUDA厳密resumeと独立監査が成功。品質の未達も[完了記録](23_phase5_completion.md)へ保存し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。

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

**状態**: 主要Web10Bと同条件全文評価、日本語追加評価、100M/500M/1Bの配合・品質・学習量比較、短い物語pool200Mへの拡張と各1B比較を完了。最新の一次35/最終20evidencechecksは成功したが、Base/Chat品質は未達。旧研究候補の保存と最新候補の不採用を区別する。[最新結果60](60_dataset_expansion_results.md)、[次回案61](61_condition_preservation_next_plan.md)。最新学習速度は約676k〜683k tokens/s。原GPU基盤・再開・高速化の完了証拠を保持し再実行しない。

**目的**: 約10Mで日本語短文生成がどこまで成立するかを測り、Chatの土台を作る。

主系列10Bとその評価は完了済みで再起動しない。計画52の500M研究候補は元比較gateを通過したが実用品質未達、後続の教材内容/一定LR1B/200M教材比較は報告済み。最新結果は[60](60_dataset_expansion_results.md)。次回の一区切りは[提案61](61_condition_preservation_next_plan.md)の限定教材品質比較と採否・停止であり、文書更新では実行しない。

**ゴール**: 選定済み10M候補を直接10Bまで学習・評価し、10Bの`JMicro-10M-Base-v1`と固定評価を残す。

| 累積tokens | 目的・判断 | 残すもの |
|---:|---|---|
| 500M | 初期改善と反復悪化の確認 | checkpoint、BPB/生成/速度 |
| 1B | 日本語生成の立ち上がり、候補最大2つ | 比較表、候補更新理由 |
| 2B | 過去355M/約2B経験との観察点整理 | 規模・Tokenizer・データ差を明記した記録 |
| 5B | 本命1つの決定 | 選定reportと継続config |
| 10B | Base v1の固定評価 | weights、Tokenizer、model card、全評価 |

作業（500M〜10Bの学習・同条件評価は完了。品質未達は保持）:

- 既存12.23B trainを使う。50〜100B master候補全量の取得を先行せず、実量と目標を混同しない。
- 各段階に必要なshardsから用意し、未使用全量の処理を10B開始の前提にしない。
- BPB、短文品質、反復、EOS、Unicode、追加GPU時間を段階ごとに記録する。
- 固定mixtureのscaling系列を残す。目的に合わせたmixture変更は別条件として記録する。
- Phase 5でWSDを採用し、Phase 6②でstable/decayの実装・CUDA全state再開/分岐完全一致を確認済み。現在のbatch/backend/数値配分は[直接10B専用設定](../configs/phase6/base_10b.json)へ凍結済み。従来version2は保持する。継続stable枝と評価decay枝を区別して追加computeも計上する。StableExtensionTrainerの明示forkは実装・10B準備検証済み。20B/50Bには新しい予算・履歴・再開確認が必要で、通常resumeでは予算を変更しない。

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

- 実装済みstable予算延長forkについて新20Bの固定条件・履歴・全state検証を確認してから継続用checkpointで20Bへ進み、固定mixture・同じ評価条件で10Bと比較する。通常resumeで終端budgetを変更しない。
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

Phase 0〜4の骨格・データpilot・Tokenizer・両モデル/cache/export・Windows/WSL移行・学習器・評価・保存再開・実機速度は完了済み。Phase 5のoverfit/smoke・4本の100M比較・候補選定が完了し、Phase 6①〜⑤、5Bと各100M比較、10B準備が完了。本10B科学学習・保存確認・同条件品質評価は完了し、Base/Chat品質目標は未達。巨大コーパス全量取得、50B開始、追加hybridを先行しない。

具体的な着手checklistは[次の実装タスク](10_next_steps.md)、各技術判断の根拠と実測待ち項目は[追加調査](11_technical_research_gaps.md)を参照する。

## 2026-10-05追加: 長期の改善・完成計画

ユーザーの「もっと長期的な計画」に対する提案。今回は計画のみでデータ作成・GPU評価・学習は開始しない。契約75〜79の不採用判断と停止境界を維持する。次回の実行範囲を定めて再開する。本節は品質基準を変更する実験契約ではなく、Phase 6の未達からPhase 7・8、条件付きPhase 9・10までを接続する方針である。

### 出発点と到達点

現在は約10MパラメータのBaseを約10B入力tokens学習済みだが、自然な続き・反復・停止が未達。直近の各100M教師比較は意味評価58.333→64.583%に対し、一貫性6→3/80、適切完結6→2/80、EOS30→7/80だった。[結果79](79_narrative_diversity_results.md)の教材は量に加えてsource・長さ・EOS密度も変わり、これだけで「増量が無効」「容量不足」「精度全体が有意に悪化」とは結論できない。自然64文の記憶成功も、未見文への汎化を保証しない。[結果72](72_root_cause_diagnostic_results.md)の数値7失敗は未解決として残す。

最終目標は、**10Mを維持して、短い日本語を自然に完結できるBase、2〜4ターンの短い雑談ができるChat、量子化したローカル成果物**を作ること。汎用大規模LLM並みの知識や推論は完成条件に含めない。Base文法70%以上、Chat文法・関連性70%以上、文脈60%以上、停止95%以上等の既存目標を維持し、未達を完成と扱わない。全成果物5〜10MB級は目標であり、Tokenizer・runtimeを含む実測で確認する。

### 段階と判断条件

| 段階 | 目的・主な作業 | 完了条件・次の分岐 |
|---|---|---|
| 1. 根本原因の切り分け | 正解を与えた予測と自由生成を比較し、最初の意味逸脱、EOS順位、反復、64/256tokensの打切りを調べる。必要なlabel/mask/cache/数値経路を修正する | 有力仮説と対照条件を固定。[計画80](80_generation_transfer_plan.md)の診断後、EOS重み・文の長さ・教材内容のうち一つずつ比較する |
| 2. 日本語教材の再設計 | 日常の完結文、因果を持つ説明段落、良質な一般日本語を段階別に用意。引用・条件・否定・時系列・数・照応を含める | 内容確認、独立dev、実文書数・準備tokens・EOS密度を記録。小教材から広げられる供給を確認 |
| 3. 学習方法と構成の選定 | 現10Bからの追加学習と、良い教材で同じ10Mを最初から学習する方法を比較。必要時は同程度の10Mで深さ/幅/embedding配分を比較 | 未見文の生成・BPB・学習曲線・実時間から本学習候補を選ぶ。追加学習の失敗だけで容量限界を断定しない |
| 4. データ量と学習量の分離 | 教材量だけ変える比較と、同じ教材で学習量だけ増やす比較を行う | 独立教材の不足、繰返し学習の不足、品質/構成の問題のどれに投資するかを実測で決める |
| 5. 改善Baseの本学習 | 固定レシピで1B→2B→5B→10Bの節目を評価。効果に応じ良質な教材を2〜5B規模へ広げる | 生成品質とBPBの採用条件を満たすBaseを確定。伸びが止まれば同じレシピの増量を止める |
| 6. Chat化 | Base→SFTと、対話の中間学習→SFTを比較。Assistant本文＋EOTを教師にし、訂正/否定/2〜4ターンを評価 | Chat文法・関連性70%、文脈60%、停止95%等を達成。未達は原因別にBase/対話教材へ戻す |
| 7. 量子化とローカル利用 | float/HF/GGUFを照合しQ8/Q4を比較。WebUIに採用重みを接続しWindows側等でも確認 | 品質退行が事前の許容内、Unicode/停止正常、容量・RAM・応答時間を実測。再現手順と成果物を保存 |
| 8. 完成後の拡張 | 固定レシピの10B対20B、条件付き50B。必要時に蒸留や重み共有を別実験で検討 | 追加学習のBPB改善の信頼区間と生成品質・費用が既存条件を満たす場合だけ進む。20B/50Bは最初のChat完成の前提にしない |

### 比較の規模と研究の上限

**段階1:** 診断は学習0・GPU上限600秒案。原因別の学習比較は各条件100M body/EOS教師tokens、最大3組、計600Mまでを初期研究枠とする。1組ごとに結果を見て次の仮説を選び、全組を自動実行しない。100M比較の中間品質gate（一貫性・適切完結各27/80以上、EOS37/80以上、反復18/80以下等）は既存条件のまま。一つの失敗は次の仮説へ進む材料にするが、失敗した候補を採用したり、旧契約で条件付きだった追加500Mを開始したりしない。3組で改善根拠が出なければ同種のEOS微調整を終了し、段階2・3へ研究対象を変える。

**段階2:** 準備量はまず10〜50M、次に100M、500M、供給と効果が確認できたら2〜5Bを目安にする。2〜5Bは短物語だけの要求ではなく、一般日本語を含む教材全体の規模。既存Web約12.23Bと公開sourceを優先利用し、600B全量取得は行わない。SimpleStories-JAは合成教材であり、人手の自然文と区別する。文書数を名前置換で水増しせず、同じ物語系列・著者/sourceの漏れを分割時に扱う。新poolの必要な照合だけを行い、既存巨大コーパスの全面再照合は繰り返さない。固定sampleの内容確認は最大2回の選別改訂までとし、不合格ならsource/作り方を変更する。診断用に外していた引用・条件構文は長期教材全体から排除しない。

**段階3:** 追加学習対最初からの学習は各100M、根拠がある場合のみ各300Mへ伸ばす。過去10Bの履歴・optimizer・LRが異なるため、これは学習戦略の比較であり容量だけを検定する比較ではない。構成変更が必要なら追加候補は最大2つとし、現構成も含め同じ教材・新規初期化・同じ予算で比較する。現行4k Tokenizerと過去の8k比較を理由なくやり直さない。Tokenizer比較が必要なら共通byte BPBとtokens/bytes/GPU時間を併記する。候補選定と品質合格による採用は別に記録する。

**段階4:** 教材量の比較案は、source・長さ・EOS密度を揃えた入れ子の**100M対500M準備tokensを、各1B教師tokens学習**する二条件。学習量の比較案は、**同じ500M準備tokensで100M/500M/1B/2B教師tokens**の節目を測る。後者は同じ安定学習経路のcheckpointを再利用し、毎回最初から学習しない。教材量比較の500M側も条件が同じなら再利用する。この構成なら主経路は最大3B教師、評価用decay枝は例えば25M×4＝100Mを別会計とし、約3.1B以内の枠に収める。途中の正確な配分は実験前に固定する。

LRの違いを学習量の効果と取り違えないよう、共通の安定経路と同じ長さのdecay評価枝を分ける。準備tokens、実際に触れた文書/tokens、反復を含む教師tokens、valid入力tokens、physical tokensを別記し、概算のepoch数だけで比較しない。主要な比較点で全日本語評価と固定80件の内容評価を行い、間の進捗は小devで見る。結果の再採点や全suiteの不要な反復を避け、最終候補だけ別seedでも確認する。

**段階5:** 本学習前に採用レシピ・最大10B教師予算・評価点・退行/停滞による終了条件を固定する。1B/2B/5B/10Bは新経路の教師予算であり、現10Bから継続する場合は「親の約10B入力＋追加教師」を分けて表示する。研究として学習曲線を見ることと、品質合格として増量を承認することを混同しない。予算終了でも未達ならどの能力が伸びなかったかを報告し、データ・構成・目標の見直し案を出す。10M不可能と断定したり目標を無断で下げたりしない。

**段階6以降:** SFTの10M→30M→100Mは既存ロードマップ通り**総系列tokens**の候補節目で、Assistant教師tokensを別に計数する。Baseの自由生成が未達の状態でSFTだけで治る前提に進まない。量子化の退行上限はfloat devの後・候補選定前に固定する。外部公開、第三者への連絡、有料cloudは本計画の実行範囲に含めず別の指示に従う。参照用の大きい教師モデルを検討しても、学習対象の10Mは維持する。

### 評価・期間・見直し

BPB、意味/文法の選択式評価、自由生成の文法/関連性/一貫性/適切完結、EOS、反復、Unicodeを併用する。gold EOS尤度だけ改善しても自由生成が止まるとは限らない。64tokensの凍結評価は維持し、256tokensは打切りと本当の不停止を見分ける診断として別報告する。採点基準を先に固定し、可能ならモデル名を伏せた人手レビューを加える。これまでの非blind Codex評価を独立した人手評価とは記載しない。devで選定し、保護したtestは最終レシピ凍結後に一度使う。必要時は実験前に新しい未使用holdoutを確保する。

最初の研究サイクルは**4〜6週間を見直しの時間枠**とする案。前半に診断・教材・小規模の戦略比較、中盤に学習曲線とBase本学習、後半はBase合格時にChat/量子化へ進む。Base未達なら後半を教材/構成の再設計に使う。これは作業配分の提案であり品質達成や全Phase完成の納期ではない。各段階の予算到達時に得た証拠と残課題から次の範囲を決める。

直近100M教師の学習本体は約150〜163秒。現レシピの計画用速度を約0.60M教師tokens/秒と置くと、100M約3分、1B約28分、2B約56分、5B約2時間20分、10B約4時間40分が**学習本体だけ**の目安。評価・compile・保存・教材準備は別で、構成/長さ/batchが変われば再計測する。長期計画の不確実性は学習時間より良質な教材の供給・実装修正・内容評価に大きいため、それぞれに比較本数と完了条件を設ける。

### 計画の根拠と限界

[TinyStories](https://arxiv.org/abs/2305.07759)は小型モデルでも単純な英語物語で一貫した生成ができる例を示し、狭い教材から学ぶ方針の参考になる。ただし日本語10Mで本プロジェクトの目標が達成できる証拠ではない。[Chinchilla](https://arxiv.org/abs/2203.15556)の計算最適性の実験は70M〜16Bモデルを含む研究であり、10M日本語に「最低2〜5Bが必須」という閾値を与えない。教材量・学習量・構成を分けて測る方針はこれらを踏まえた本プロジェクトの提案である。

[非停止と復号の整合性の研究](https://aclanthology.org/2020.emnlp-main.448/)はgreedy等の復号で非停止が生じ得ることを示す。今回の原因を確定するものではなく、正解経路と自由生成、学習された停止と生成側の制限を分けて診断する根拠として用いる。

### 段階1〜3の再開と、300M後の次案（2026-10-05）

新しい実行目標「3までをより詳細の計画を立てて進めてください」は上記長期段階1〜3。詳細の凍結契約はdocs/80_generation_transfer_plan.md末尾、generation_transfer/curriculum_strategy/strategy_extension各configにある。昔の短期契約の不採用判断を変更しない。

段階1は学習0の実診断。新候補train32はgreedy64のEOS9から256のEOS28へ増え、上限による切断を一部確認。ただし公式Web dev32は両モデル256でもEOS0で、長さだけでは解決しなかった。段階2は短文供給不足v1と内容弱20/64のv2を保存し、v3で10,000,208準備tokens/73,260全文、dev500,319/3,690を確保。short1M/物語4M/Web5Mの組成、固定64の弱10/64。SimpleStories-JAは合成、残る擬人化/幻想/一部宣伝を限界として記録した。新pool内の局所family分割を既存全corpusの完全近重複保証とは呼ばない。

段階3の各100M実教師比較は、元10B追加対新規同10Mの学習戦略比較。BPB1.070892/1.413020、意味66.146/51.563%、EOS31/12、一貫性6/6、適切完結11/6（各80）。両候補の採用条件は未達。新教材dev32の学習前後に限れば、両条件でBPB・EOS・4gram再出現が改善し、事前の研究延長条件を満たした。Web補助devは親のtrain既知文書を含むので、公式未学習devの改善と区別する。

条件付き延長は各100MのAdam/RNG/文書shuffle cursorを引継ぎ、追加200Mで各累積300M。元peakへ戻す段階的reheatと追加区間90%stable/10%decay、warmupを再実行しない。これは連続300M学習とは異なる経路。全段階3のGPU上限1800秒と既存品質基準を維持し、両300Mの共通日本語と全160個別内容、採否・元UI復帰・local commitで今回停止する。100Mの準備tokensと反復を含む100M教師を混同しない。

**その後の計画は以下の提案であり未開始。**

1. 300Mの100M比をまず確認する。BPB/選択式だけ改善し、主体・時系列・否定・因果や自由生成が改善しなければ、同じ教材の大規模継続を優先しない。過去履歴/LRが異なるので、freshが弱いことを容量不足の証拠にしない。
2. 次の教材は幻想・擬人化・宣伝への残存偏りをsource/編集単位で減らし、日常の行動と結果、説明、数・否定・照応を保つ。現v3の受け入れ基準を事後に変更したり、失敗sampleを無限に抽き直したりせず、別source/別契約として作る。まず10〜50Mの供給・固定内容sampleを確認し、同じ総教師量で比較する。大量全面照合は行わない。
3. 良質な教材でgoldは学べるが未見生成が伸びない場合は、10M内の構成を比較する。現13層/幅256/FFN640（10,001,152）を対照に、9層/幅256/FFN1040（10,011,392）、6層/幅384/FFN832・heads6/KV3（9,982,848）を最大2候補とする。countsはCPU構築による計数だけで学習性能の証拠ではない。Tokenizer4096、GQA比2、head64、NoQKNorm、context1024、tied embeddingsを維持する。全条件を新規学習・同教材順序・同seed/teacher budget（案各300M）・同LR条件で比較し、構成ごとに安定batch/CUDA保存再開を確認。幅/深さ/embedding比が一緒に変わる候補の比較であり、単一要因の容量検定とは呼ばない。設定はreports/phase6/strategy_architecture_proposal.json、未起動。
4. 教材・学習戦略/構成に候補ができた段階で、段階4のデータ量と学習量を分ける比較へ進む。source/長さ/EOSを揃えた入れ子100M対500M準備tokensを各1B教師、同500M教材の100M/500M/1B/2B教師checkpointを比較する。100Mという数字が準備量か教師量かを全表で明示する。供給不足時は利用可能な規模へ実験契約を書き直し、未準備500Mを用意済みと扱わない。品質不合格候補を実用Baseへ採用しない。
5. 改善のあるレシピを選べたら1B→2B→5B→10B教師の本学習へ。Base品質を満たしてからChat/量子化に進む。20B/50B、test、公開、pushは今回の範囲外。

### 段階1〜3の実結果と、次の優先順位（2026-10-06 JST）

凍結契約80の長期段階1〜3は、根本診断・10M以上の教材pilot・各100Mから条件付き各300Mまでの戦略比較・採否・元UI復帰を完了。実装の完了と生成品質の達成は別で、両候補は不採用。上の「300M後の次案」の優先順位を、以下の実結果で更新する。新しい研究は未開始。

| 条件 | 準備教材tokens | 今回の累積本文/EOS教師 | 共通dev BPB↓ | 基本意味 | JBLiMP | JCQA | EOS/80 | 自動反復/80 | 一貫性/80 | 適切完結/80 | Unicode破綻/80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 元10Bから追加・100M | 10,000,208 | 100,000,000 | 1.070892 | 66.146% | 75.227% | 32.350% | 31 | 13 | 6 | 11 | 0 |
| 同10M新規・100M | 10,000,208 | 100,000,000 | 1.413020 | 51.563% | 74.018% | 25.648% | 12 | 16 | 6 | 6 | 0 |
| 元10Bから追加・300M | 同上 | 300,000,000 | 1.255773 | 55.729% | 75.529% | 26.899% | 31 | 5 | 8 | 15 | 1 |
| 同10M新規・300M | 同上 | 300,000,000 | 1.605410 | 49.479% | 71.299% | 26.542% | 22 | 2 | 5 | 13 | 1 |

同じ教材を繰り返した学習量比較であり、データセット固有量を増やした比較ではない。追加側の親は10,000,007,168入力tokensで、新規側の親は0更新/入力/教師、両者の歴史・LR・Adamも異なる。300Mは100M終端から元peakへ戻した追加200Mの段階的reheatで、連続300Mとの同一性は主張しない。自動反復カウンターの減少を、すべての意味的反復の解消とは扱わない。

100M→300Mで訓練中の損失は下がる一方、公式dev BPBと基本意味が悪化した。教材への過適応、一般分布の忘却、LR再加熱の影響が次の仮説であり、これだけで原因を確定しない。新規側も300Mで改善Baseにはならず、学習量不足が完全に否定されたとも10Mが不可能とも言わない。両条件とも既存一貫性/適切完結27以上・EOS37以上・raw Unicode0・BPB等の採用基準を満たさない。

次回の具体的な順序:

1. **損失とLRの切り分け。** 既存metrics/100M・300M重みを使い、同じ小train/devのBPBと、同じprefixの生成を並べる。必要な新GPU測定は小sampleのみとし全suiteを無用に反復しない。追加検証案は同じ100M重み/Adam/RNG/順序から、今回のreheat枝に対して終端LRを上限とする低LR枝を各同量200M教師で比較する。今回のreheat結果は再学習せず再利用する。仮説は「LRを戻した影響か、同じ教材を反復する影響か」、変更はLRだけ。実行前にbudget/scheduleと改善・終了条件を別契約で凍結。trainだけ改善してdevが悪化する条件を長期レシピへ選ばない。
2. **教材改訂の同量比較。** 現v3の幻想/擬人化/宣伝や、主体・数・因果の弱い教材を、別source/編集単位の自然な日常完結文・説明へ置き換える。まず10〜50M準備tokensと局所分割・固定64内容を確認する。新規学習の対照と改訂を同じ教師量・LRで比べ、増量と品質変更を区別する。現v3の閾値や失敗sampleを事後変更しない。旧巨大corpus全面照合は繰り返さない。
3. **10M構成の比較（条件付き）。** 良質な教材でgoldの学習は機能するが未見生成が伸びない場合、上記現13層256と提案9層256/6層384を全条件fresh・同教材/seed/teacher budgetで比較する。最大2新候補、各300Mは予算案で未起動。CPUによるパラメータ計数を能力の証拠にしない。
4. **固有データ量と学習量の分離。** 有望な教材・学習設定ができれば、入れ子100M対500M準備tokensを各1B教師で比較。同500M教材を100M/500M/1B/2B教師の節目で評価する。安定経路と同量decay評価枝を実行前に固定してLRによる交絡を減らす。供給・効果が出た後に良質な準備量を2〜5Bへ広げる。
5. **改善Base→Chat→量子化。** 品質を満たすレシピで本学習を進め、採用Baseを確定してから対話学習と量子化へ進む。品質達成までの期日は未確定。今回の停止境界を越えて自動開始しない。

科学教師は合計600,000,000、valid/physical入力604,504,064、実CUDA再開32 optimizer updates/検証教師1,040,748は別会計。段階3GPU1396.456秒（上限1800秒）、診断76.895秒（上限600秒）。CPU変更関連tests、実CUDA再開、全四終端の教師/LR/保存state/共通bytes評価、320個別内容と完了監査は成功。内容判定は非blind Codexで、独立人手認証は未実施。結果72の数値7失敗は残している。

可搬証拠はreports/phase6/generation_transfer_review.json、curriculum_strategy_ready/content_v2/v3・review/annotations、strategy_extension_eligibility/review/annotations、strategy_scope_completion.json、strategy_scope_evidence.json.gz（153members/32,891,478bytes）。全rawのsource/metrics/gold/generation/失敗/理由を保存し、checkpoint/shards/corpusはWSLへ保持。モデル・dataの設定/hashは三つの凍結configへ結び付く。元10B UIのactual444875/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start9599628、HTTP親SHA410f975d…/10,000,007,168/busy=falseを確認。科学396752/426421、基準429834、延長441415は終了・不在。local commit後に停止し、段階4・新構成学習・Chat・20B/50B・test・push/公開は未開始。

### 実行再開契約: 提示した項目1〜5（2026-10-06 JST）

ユーザーの「5まで進めてください」で、直前の五項目全体を再開する。1)同じ100M出発でLR切り分け、2)10〜50M教材改訂の同量比較、3)必要時の10M内構成比較、4)入れ子100M/500Mの教材量と同教材100M〜2B教師の学習量比較、5)改善Base本学習1B/2B/5B/10Bから、採用Base→Chat→量子化/ローカル検証までが実行対象。昔の段階1〜3の停止は今回の再開で解除される。診断や準備だけ、候補不採用だけでこの目標を完了としない。

1は既存100M/300M履歴を再利用し、固定train32/dev32の学習前後を測る（新科学学習0/診断GPU300秒以内）。元各100M重み・Adam・RNG・教材順序から、100M終端LR以下をpeakとする追加200Mを各条件実行（教師400M、同じ90%stable/10%decay、warmupなし、各学習600/比較評価1800秒）。既存reheat枝は再学習しない。実CUDA保存再開、公式dev256/全日本語と固定各80内容を確認し、train/dev悪化とLRを切り分ける。候補の採用gateを変更せず、LR選定と実用Base採用は別に記録する。

2は現教材の幻想/擬人化/宣伝や主体・数・因果の弱い部分を改善する。現v3や古いreportの閾値・原文・判定を変更しない。新source/編集単位を別versionで準備し、10〜50M pilotの局所exact/family分割と固定64内容を確認する。一度のsource/selector比較は準備CPU600秒×最大2改訂、同量の各300M以下教師/GPU1800秒枠として凍結し、失敗なら次のsource/仮説へ有効に進む。trainだけ改善する条件は本学習へ採用しない。引用/条件/否定/時間/数/照応を保持し、自然文と合成の由来を表示する。

3は良い教材でgoldは学べるが未見文が弱い時に、現13層256・提案9層256/6層384の最大2新構成を、全条件fresh・同Tokenizer/教材/seed/教師量/スケジュールで比較する。各300M教師を初期上限、構成ごとに実CUDA安定batch・連続/再開を確認。GPU各600秒学習＋共通評価、全比較3600秒枠を実行前に固定。容量不足を先に断定しない。

4は新しい固有教材100M/500Mの供給を実確認してから、source/長さ/EOSを揃えた入れ子の各1B教師比較を行う。同500M教材の安定経路100M/500M/1B/2B節目に同量decay評価枝を使う。基準を見て学習量を決め、量が用意できない場合はsource供給を改善して進める。旧巨大コーパス全量再照合は行わない。全初期研究は主経路約3B＋評価枝約100Mの案で、正確な量・計測時間・停止条件は準備後にconfigへ凍結する。準備量、実露出、教師量、valid/physical、EOS/bytes/時間を別会計とする。

5は選定したレシピの安定経路1B/2B/5B/10Bを評価し、Baseの既存品質目標を満たすまで教材/設定/構成の有効な次の仮説へ戻る。未達を達成として報告しない。採用Base後にChatの10M/30M/100M総系列tokens（Assistant教師別）、Assistant本文＋EOT、2〜4ターン/訂正/否定/停止を学習・評価。float/HF/GGUF parity、Q8/Q4品質/容量/速度、実WebUIと再現手順を揃える。技術的成果物だけで全目標達成としない。

実行中は永続job/PID/boot/start/ログ/checkpointとstage ledgerを保存し、各有意なmilestoneでchecks/status/local commit。GPU占有時にUIを停止しjob終端で元の採用UIを復帰する。保護testは既存ロードマップの最終レシピ凍結後の用途だけで、日常の教材選別に使わない。20B/50B・外部公開・push・有料cloudは別の範囲で今回自動開始しない。独立した人間のblind評価は未実施と表示し、実際に取得していない人間評価を作らない。
