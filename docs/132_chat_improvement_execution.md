# 計画131・教材改善比較の実行記録

開始: 2026-10-12 JST。ユーザーのgoal「5まで進めてください」により、[計画131](131_chat_improvement_execution_plan.md)の段階0–5を明示再開した。保全、C1教材/新DEVの準備、教師量runnerと技術gate、C0/C1学習、全評価、結果報告まで。C2履歴回復・効率比較・独立seed/最終採用・量子化・公開は範囲外。

## 最終結果（2026-10-12 JST）

**計画131の段階0–5の実作業を終え、最終C0/C1はいずれも不合格・不採用。Base/Chatの完成ではない。** 各条件でAssistant本文+EOTを1,899,555教師tokens、超過0まで学習し、全14suite・3,066応答をCodex非blindで内容確認した。新規GPU生成は2,847応答、親の旧suite219応答はhashと実履歴を検証した過去結果の再利用。固定NLLは同じ2,554targetを7点で評価した。最終点t3だけで採否を決め、中間点を後から候補に替えない。

| 最終点の指標 | C0新 | C1新 | C0旧 | C1旧 | 元の合格条件 |
|---|---:|---:|---:|---:|---|
| 文法2 /80 | 44 | 62 | 52 | 58 | 単独では採否にしない |
| 文法・関連性同時2 /80 | 11 | 15 | 20 | 18 | 56以上 |
| 自生成履歴の最終文脈2 /24 | 4 | 2 | 5 | 4 | 15以上 |
| 固定80の自然停止 | 70 | 77 | 76 | 79 | 76以上 |
| 自生成59turnの自然停止 | 45 | 59 | 53 | 57 | 57以上 |
| 固定80の反復 | 11 | 3 | 5 | 1 | C1はC0を増やさない |
| 自生成59turnの反復 | 16 | 0 | 8 | 3 | C1はC0を増やさない |

最終4suiteとも空応答・役割漏れ・raw Unicode破損・履歴削除は0。C1の停止と反復は改善したが、回答内容と文脈保持が未達。C1新の文法2の62応答中47は関連性2未満で、流暢さを正答と混同しない。新旧両suiteの絶対screenを通った候補はなく、事前の分岐に従い候補向けBase保持・samplingは省略した。保持合格やsampling品質確認とは扱わない。

[最終比較と全gate](../reports/phase7/chat-improvement-20261012/selection.json)、[全点再集計](../reports/phase7/chat-improvement-20261012/final_analysis.json)、[完了監査](../reports/phase7/chat-improvement-20261012/completion.json)、[証拠の入口](../reports/phase7/chat-improvement-20261012/README.md)を参照する。完了監査は全保存state/実消費列、凍結source、全rawと採点のbinding、共通NLL、終端GPU台帳、実processと元UIを照合する。Git保存後のbytes照合は [final_git_verification.json](../reports/phase7/chat-improvement-20261012/final_git_verification.json) に記録する。監査は品質改善を認証するものではない。

### 学習量と中間点

同じ元WebUI10B親、Tokenizer、native10,001,152 parameters、seed42、教師量基準scheduleと最終予算で比較した。C0は3,647更新、C1は3,636更新。最終checkpoint SHAはC0 `165523836f212fb59be32b7d0f42276b2eed968cb4c896b82b01a84a73540734`、C1 `fbdd68d23e4fbf9d0990f84fb6b36886ecef52fb87ff508d07d165055e3e6ce9`。全stateはWSLに保持し、Gitには重み・教材を入れない。

| 保存点 | C0新 同時2/文脈2 | C1新 同時2/文脈2 | C0旧 同時2/文脈2 | C1旧 同時2/文脈2 |
|---|---|---|---|---|
| 親t0 | 2/80・1/24 | 同じ親 | 0/80・0/24 | 同じ親 |
| t1（B/3） | 5/80・2/24 | 15/80・4/24 | 10/80・4/24 | 11/80・1/24 |
| t2（2B/3） | 8/80・2/24 | 11/80・5/24 | 13/80・4/24 | 16/80・4/24 |
| t3（B） | 11/80・4/24 | 15/80・2/24 | 20/80・5/24 | 18/80・4/24 |

C1の文脈保持は学習量に伴って単調改善しなかった。親と各保存点は同じfamilyの反復測定で、3,066を独立した3,066問とは扱わない。自己生成24familyは固定80の部分集合で、別の独立評価でもない。人間blind・独立学習seed・fullDEV・protectedTESTは未実施。

最終のfamily単位paired bootstrap（2,000回、seed42）によるC1−C0差は、新DEVの同時2が+5.0 percentage points、95%CI [-5.0,+15.0]、最終文脈2が−8.33 points、CI [-29.17,+12.5]。旧DEVでは同時2が−2.5 points、CI [-15.0,+10.0]、文脈2が−4.17 points、CI [-20.83,+12.5]。文法の改善から内容全般の優位を主張できない。

### 固定NLLと汎化の問題

本文/EOTは別集計。同じdatasetの同じtarget間でのみ比較する。C1 TRAINの固定112targetは7分類×16のsampleであり、全TRAINの品質認証ではない。

| 点 | C1 TRAIN本文mean NLL | 新DEV本文mean NLL | RPC DEV本文BPB | 新DEV EOT mean NLL |
|---|---:|---:|---:|---:|
| 親t0 | 3.376225 | 3.596389 | 1.351262 | 17.445359 |
| C0 t1 | 2.944270 | 2.286895 | 0.900070 | 1.734327 |
| C0 t2 | 2.994673 | 2.354254 | 0.896292 | 1.469583 |
| C0 t3 | 3.038075 | 2.373619 | 0.898193 | 1.562778 |
| C1 t1 | 0.00042255 | 3.345770 | 1.725132 | 1.223238 |
| C1 t2 | 0.00010575 | 3.588812 | 1.802019 | 1.544896 |
| C1 t3 | 0.00000628 | 3.883688 | 1.900805 | 1.494148 |

C1は固定TRAINの損失をほぼゼロにできたが、新DEV本文NLLはt1→t3で悪化し、最終では親より高い。RPC DEV本文BPBも親より約40.7%高い。テンプレートへの過適合・分布のずれと整合する観察であるが、単独原因の実証ではない。RPCのChat形式NLLをBase保持の正式suiteの代わりにしない。C0のDEV NLLはC1より低いが自由生成の回答内容は不合格で、NLLだけで採用しない。

### 実際の失敗と改善方針

C1 t3新の提供履歴では、11枚という条件に「用意する予定は8枚です。」、土曜日への訂正に「今の予定は金曜日です。」、星の道への変更に「次に『花の道』を練習します。」と古い条件を返した。自己生成履歴では、直前に「明日は母と水族館へ行く予定です。」と正しく返していても、誰と行くかに「あなたと水族館へ行く予定です。」と答えた。どんぐりをどんぶりへ置き換え、その誤りを次turnでも維持する例もある。レモンの直接回答や土曜日への回復の成功例も保存し、失敗だけを抽出した評価にしない。

[教材構造の確認](../reports/phase7/chat-improvement-20261012/curriculum_structure_inspection.json)では、名前の紹介とgold Assistantの受け答えを前置きし、最後のAssistant targetだけを教師にする構造を確認した。前置きはinputとして参照できるが直接教師にはならない。DEVには名前紹介のない最初の質問や、正解履歴と異なる自己発話がある。共通説明文型への依存、first-turn教師不足、slot表記や構造のずれ、誤発話の持越しが次の検証仮説。mask/shiftの不具合や10Mの容量限界を確定した証拠ではない。

次は[改善計画133](133_chat_generalization_followup_plan.md)に従い、名前紹介を必要としないfirst-turn・自然な言い換え・短い直接回答を含む教材へ改訂する比較を最優先にする。正しい提供履歴での基準到達後に、誤った自己発話からの回復を別比較にする。今回のDEVや失敗回答をそのままTRAINへ移さない。4周目やLR/architectureの同時変更を自動追加しない。

### 時間・実装・保存上の限界

失敗分を含めたGPU累積は **4,247.635851961秒（70.794分）/6時間上限**。probe27.120089203秒、resume48.474963176秒、C0学習1,590.072084565秒、C1学習1,354.728570122秒、評価1,227.240144895秒。手動内容レビューとCPU監査の経過時間はこのGPU時間とは別。全14entryは終端状態で、追加実験は起動しない。

C0のphysical tokens189,890,560に対しpadding159,444,187（約83.97%）、C1は161,185,792に対し約94.93%がpadding。教師予算の一致はGPU費用や有効入力量の一致ではない。効率改善は教師順・完全応答group・scheduleを保った別の検証課題で、今回の品質比較に混ぜない。

初回のcold評価時間の過大見積もり、親旧suiteの再利用binding不一致、CounterのJSON key型、保存snapshotの改行差は[incidents.json](../reports/phase7/chat-improvement-20261012/incidents.json)に原版・停止・修正と限界を記録した。gateを弱めず、凍結18sourceは変更しなかった。親再利用失敗時のlauncher stdout/stderrはretryで上書きされ、原ログ全文が残るとは主張しない。全state再開と最終監査は技術成立の証拠で、モデル品質の証拠ではない。

段階0–5の比較を閉じる。完了監査2026-10-12T03:00:36Zで元10B WebUIの実PID198864・boot4052bfc5-3850-44e4-9123-d34a9e19f36e・start ticks41628469とHTTP親SHA/Tokenizer/parameters/busy=falseを確認した。この観察は将来の生存証拠ではない。C2、padding比較、独立seed43、人間blind、fullDEV、protectedTEST、採用、量子化、外部公開・pushは未実施。次の計画は作成のみで、実行は新しい明示再開待ち。

## 実行途中の履歴（以下は記載時点の観察）

2026-10-12T02:45Z更新: **両条件の学習、全予定greedy生成と共通NLL、全state/実消費量監査が完了**。C0は3,647更新、C1は3,636更新、どちらもAssistant本文+EOT教師1,899,555、超過0。最終checkpoint SHAはC0 `165523836f212fb59be32b7d0f42276b2eed968cb4c896b82b01a84a73540734`、C1 `fbdd68d23e4fbf9d0990f84fb6b36886ecef52fb87ff508d07d165055e3e6ce9`。全14suiteの内容レビューのうち11suiteを完了し、残りはC1 t2旧・t3新旧の3suite。段階5、最終paired比較、採否の完了監査は未完了。開始時点・学習中の記述は以下の履歴として保持する。

| 完了した追加内容レビュー | 新/旧 | 固定文法2 | 固定文法・関連性同時2 /80 | 自生成最終文脈2 /24 |
|---|---|---:|---:|---:|
| C0 t2（2B/3） | 新 | 32 | 8 | 2 |
| C0 t2 | 旧 | 42 | 13 | 4 |
| C0 t3（B） | 新 | 44 | 11 | 4 |
| C0 t3 | 旧 | 52 | 20 | 5 |
| C1 t2 | 新 | 54 | 11 | 5 |

この5suiteは全219応答のraw/実履歴を検証し、必要な新規採点をすべてCodex非blindで記入した。実履歴・checks・raw IDs/bytes/text等の全fingerprintが一致する既存判断と同suiteの無抑制controlだけを出典付きで再利用し、未確認の内容を自動採点していない。C0最終新旧も絶対screen未達。C1 t2新の内容はt1の15/80から11/80へ低下しており、追加学習による単調な改善は認められない。人名・挨拶の反復や自発話の誤りの継続を保存する。最終C1の採否は残る内容レビュー完了後に決める。

GPU台帳の全14entryが終端状態になり、失敗分を含めた累積課金対象時間は **4,247.635851961秒（70.794分）/6時間上限**。内訳はprobe27.120089203秒、resume48.474963176秒、C0学習1,590.072084565秒、C1学習1,354.728570122秒、評価1,227.240144895秒。学習state監査はAdam全param step、教師量schedule、Python/NumPy/Torch/CUDA RNG、samplerの最終cursor、全checkpoint hashと消費列を確認してpassed、品質判定は含まない。`remainder-chain/result.json`はGPU完了・内容レビュー待ちを示す。元UIはHTTPで親10B SHA、10,001,152parameters、共通Tokenizer SHA、busy=falseを再確認した。記録PIDを将来の生存証拠にはしない。

段階0を開始。Windows Git HEAD `f78646185db3f818792e5cb87e2331ef6028e06f`は開始時clean。WSL2 Ubuntuが稼働し、RTX4090 24,564MiB、使用975MiB、utilization1%、Linux data環境の空き880GBを確認した。元UIは実PID142855、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、10,001,152parameters、busy=falseで現在稼働を確認。science/trainingの重複processはない。

`nvidia-smi`はWSLの既定PATH外で、`/usr/lib/wsl/lib/nvidia-smi`を用いる。WSLにrgはなく、この確認だけgrepへfallbackした。uvは既存0.9.0。環境を再構築したりpackageを追加したりしない。

最初は親/Tokenizer/既存TRAIN/DEVのhashとactive processを証拠に保存し、TRAIN教材設計を先に固定する。新DEVの具体例はTRAIN設計固定後に別のartifactとして作成し、教材へ転用しない。今回の比較はまだ学習0、Base/Chat未採用。

以後の実数量、技術gate、checkpoint、raw/全内容レビュー、停止理由を追記する。開始記録だけを段階5の完了証拠にはしない。

## 教材準備とCPU技術確認

同じparent/Tokenizerを保った専用 `TeacherBudgetSampler` / `TeacherChatTrainer` を追加した。教師512を下限として完全応答を積み、全microbatchのCE sumを実教師数で割る。教師量midpoint LR、完全EOTの最終超過、選択targetの検証、全state保存/再開を実装した。更新途中の例外後は不完全stateの保存/継続を拒否し、完了checkpointの読み込みから再開する。

WSLのuv/Python3.12.7で、新しいCPUテスト3件が通過した。連続/再開のmodel・optimizer・scheduler・RNG・sampler・counters・消費列digestの完全一致、1行/2行microbatch分割の損失/重みが定義した数値許容差内で一致すること、更新途中停止と無効保存拒否、値域・語順・訂正・名前だけの制約を確認。CPUの小構成fixtureであり、native CUDA学習や品質の証拠ではない。

TRAIN設計のsource hashを各候補の作成前に保存し、新DEVの具体例をまだ作成/読込みしていない。最初の候補は約63.5万教師と応答長の偏りで不合格。自然文の内容確認で、教師mask外のAssistant履歴にも人間の体験が残ることを検出し、原文の会話対から根拠が成立する部分だけを選ぶ別版にした。時刻順序、消費品を借りる設定、Userと引用人物の別名、名前だけの回答も修正した。各候補JSONとデータはWSLで保全し、改善効果とは扱わない。

v6の7分類×40=280targetをCodex非blindで確認し、7件を修正対象とした。[v6レビュー](../reports/phase7/chat-improvement-20261012/train_content_review_v6.json)。人物を「使わない」とする訂正説明、休憩を作業として扱う設定、資料室で料理する設定を修正し、該当familyの値域/説明文型を点検した。助数詞・漢数字/算用数字の表記も条件と整合させた。別seedの固定280targetを再確認し、全件pass。[最終sample確認](../reports/phase7/chat-improvement-20261012/train_content_review_final.json)。元source挨拶49会話対を追加で全件読み、こんにちは→こんばんはの1例をsource familyごと除外した。[自然文部分の確認](../reports/phase7/chat-improvement-20261012/natural_source_content_review.json)。独立人間blindや全TRAINの人間認証ではない。

最終TRAINを **39,655 target、1周660,080 Assistant本文+EOT教師** として凍結した。SHA256 `8eff5223949829922558f51b99b59cad2b52a4a0bc7ef7f03cd7d6fe586d2b82`、WSL data `phase7/chat-improvement-20261012/train.jsonl`。[準備記録](../reports/phase7/chat-improvement-20261012/train_preparation.json)。分類別教師比は提案にほぼ一致し、各分類の最大family比4.7%以内、共通2–65教師/応答、prepared長さTV約0.037/EOT割合差約0.367percentage point。近いslot/表記/応答長派生を別familyへ水増しせず、元sourceの挨拶も一つのnear familyへ集約した。

**教材の偏り**: ほぼ自作の制御会話で、日常30%も主に自作。元source由来は48挨拶target/230教師tokensだけで、豊富な人間同士の自然会話を選別できたとは主張しない。応答本文の種類は6,510、最頻本文は753targetに出現する。同じ本文を異なる履歴で学ぶ出現量であり、66万の独立した新情報ではない。正しい条件回答/役割を優先したrecipe全体の比較として扱い、新旧DEVの自然会話を含む元絶対gateを維持する。

CPU sampler dry-runでは実消費量の教師比、EOT、長さ、更新数差5%以内、累積AdamW decay係数差0.1%以内、最大target出現3回を確認する。候補ごとの旧dry-runは別名で保持し、最終TRAINに対する結果を[consumption_dry_run](../reports/phase7/chat-improvement-20261012/consumption_dry_run.json)へ保存する。これは順序/counter/scheduleの確認であり、GPUの速度見込み/有限BF16/保存再開gateはまだ未実施。

## TRAIN凍結後のDEVと実行入口

TRAINを凍結後、新しい80family（10分類×8）を作成した。訂正/後続/文脈の24familyは自生成履歴でも評価し、2turn15・3turn7・4turn2で59応答。TRAINと具体的な質問/構造/組合せを変えた独立著作で、全script/goldをCodex作者が非blindで確認した。独立人間認証ではない。[DEV準備](../reports/phase7/chat-improvement-20261012/dev_preparation.json)、[監査](../reports/phase7/chat-improvement-20261012/dev_audit.json)。全履歴と最悪64token/turnでもcontext内。最終質問の完全一致0、文字3gramの表層flag0、最大Jaccard0.353。表層検査は意味の独立性の保証ではなく、親のWeb corpusも再走査していない。

固定NLLをC0 TRAIN112・C1 TRAIN112（7分類×16）・新DEV80・RPC DEV2250、合計2554targetとして保存した。[NLL準備](../reports/phase7/chat-improvement-20261012/nll_preparation.json)。同じ対象を両条件/全保存点で測り、本文/EOTを分離する。異なる教材分布間のloss大小で品質を順位付けしない。新DEVのgold履歴NLLは自生成履歴の成立とは別。

専用runner、評価入口、6時間の共有GPU ledger、全state再開、hidden durable Windows worker、実process/lock/UI busy/容量のlaunch gateを実装した。凍結前CPU preflightのpath型不一致と、元UIが生存中にGPU lockを保持する正規動作の扱いを修正し、不採用configを別名で保存した。UIによるlockは実PID/boot/start・HTTP親SHA/busy・kernel lock holderが一致した場合だけ停止対象とする。本学習前にprobe/完全再開gate/全評価の時間見込みを必須とした。

native CUDA probe18更新を完了。[probe](../reports/phase7/chat-improvement-20261012/native_probe.json)。両条件の本学習の保守見積もりはC0約2,190秒/C1約1,871秒で各3,600秒以内。最大割当約16.22GB、実消費予定の全更新が1/2microbatchで、probeも両方を確認。budget1の最終1応答・EOTと空PAD行もfinite。検証教師8,458、本比較学習教師0。

native CUDA保存再開4条件（C0/C1×通常/epoch境界・最終部分更新）も通過。[gate](../reports/phase7/chat-improvement-20261012/native_resume_gate.json)。各条件のmodel/optimizer/scheduler/RNG/sampler/counters/digest/lineage/specと損失・勾配・LR履歴が全てbit一致。合計32検証更新は主比較学習に含めない。probe実計上27.12秒、resumeはledgerの実時間を参照する。

凍結configは[実行recipe](../configs/phase7/chat-improvement-20261012.json)、source snapshotはreport内sourceに保存。TRAINは今後も再生成しない。

## 時間見込みと本比較の開始

最初の評価forecastは11,418秒で10,800秒を超え、本学習を止めた。初回の推論初期化時間を全応答に掛ける式だった。[不合格見積もり](../reports/phase7/chat-improvement-20261012/evaluation_forecast_failed_cold_per_response.json)。本学習前に、初回/継続の分離計測と初期化のstageごとの加算へ変更する手続きを固定した。[測定方式変更](../reports/phase7/chat-improvement-20261012/forecast_method_revision.json)。評価件数4,380の最悪64token、係数1.5、保存/起動等600秒、GPU枠は維持する。TRAIN・native training・decoding・絶対品質gateは変更しない。

11回の生成と固定32×1024 NLLの初回/継続計測で、評価の保守見積もり7,740.84秒となり枠内に収まった。[再測定](../reports/phase7/chat-improvement-20261012/evaluation_forecast.json)。これは実測に基づく見込みで、実GPU台帳の上限を解除しない。元親/旧suiteの219件は親/Tokenizer/suite/generation core source・全履歴/IDs/bytesと旧notesを検証し再利用した。[再利用根拠](../reports/phase7/chat-improvement-20261012/parent_old_reuse.json)。新しい独立評価やGPU再生成として数えない。

実消費順序からC1のfamily比も再構成し、最大1.4202%・最大target3回を確認した。[実family量](../reports/phase7/chat-improvement-20261012/actual_family_consumption.json)。CPU dry-runの終端cursorとseed42 epoch順を使った数量の監査で、品質証拠ではない。

両条件のB/3到達まで本学習を開始した。完了更新を250更新ごと/到達点で全state保存する。まず両条件の同じ到達点で新DEVと共通NLLを確認し、その後の判断を記録する。本学習進行中、全予算の品質評価/段階5完了/採用は未確認。

## B/3の実評価と続行判断

両条件は同じB=1,899,555でfresh開始し、C0は1,216更新/633,290教師、C1は1,211更新/633,216教師で最初の到達点を保存した。完全応答/EOTを保つ更新単位による74教師の差で、epoch回数の比較ではない。各条件の新旧suite219ずつ、親の新suite219もraw全履歴・IDs・bytesを検証し、内容をCodex非blindで採点した。抑制/無抑制の同じrawと全文履歴は明示的なfingerprintで採点を再利用し、異なる自発話の履歴は別に確認した。

| B/3の内容 | C0既存雑談 | C1条件回答教材 | 必要 |
|---|---:|---:|---:|
| 新DEV 文法・関連性ともに2 | 5/80 | 15/80 | 56/80 |
| 新DEV 自生成最終文脈2 | 2/24 | 4/24 | 15/24 |
| 旧DEV 文法・関連性ともに2 | 10/80 | 11/80 | 56/80 |
| 旧DEV 自生成最終文脈2 | 4/24 | 1/24 | 15/24 |

全4screen不合格。新DEV jointのC1−C0は+12.5percentage points、family paired95%CI[+2.5,+22.5]。新最終文脈の差のCIも含めた全比較は[中間比較](../reports/phase7/chat-improvement-20261012/intermediate_screen.json)に保存する。この信号は非blind探索で、内容/文脈の両方が合格したとは扱わない。

共通NLL2554targetをC0/C1/親で全取得した。同じC1 TRAIN112targetの本文平均NLLはC1で0.000423とほぼ暗記した一方、新DEVでは3.34577。自然会話RPC DEVの同じ155,582bytesの本文BPBは親1.35126、C0 0.90007、C1 1.72513。新DEV本文BPBは親1.16824、C0 0.74287、C1 1.08683。分布の異なる教材間のlossで順位をつけず、同一対象文で比較する。C1の教材適合と汎化不足、自然会話の分布への悪化を記録し、全予算での結果は未確認とした。

C1には名前のない「さん」、教材の説明文型の流用、旧条件への回帰、場所/個数/人物の型を取り違える応答が残った。例: Userの画用紙を写真と誤って答え、その自発話を次turnでも引き継いだ。逆に自生成で最新11枚へ更新できた例もあった。旧suiteにはC1のraw UTF8失敗1件があり、表示修復やdecoding変更で消していない。[続行判断](../reports/phase7/chat-improvement-20261012/intermediate_decision.json)で、改善信号の最終測定に価値があるとして両条件を凍結Bまで続行した。TRAIN・gate・architectureを変更せず、t3だけを最終候補条件に使う。

親の旧suiteを再利用する際、binding内部に追加した来歴/歴史的fieldとfrozen evaluatorの完全一致assertが合わず、親の新suite219生成後に停止した。実GPU時間は失敗stageにも計上し、raw/notesの元版を保全した上で、再利用の来歴をbindingの外に保持して正規化した。[正規化検証](../reports/phase7/chat-improvement-20261012/parent_reuse_binding_normalization.json)。全raw/実履歴/採点の不変をCPUで確認し、再実行では生成を繰り返さず不足NLLだけ取得した。追加CPU比較ではJSON保存による文字数histogramの数値key→文字列key変換を正規化して照合する。frozen trainer/evaluator/reviewer本体は変更していない。

現在はt1の全stateからt3へ両条件を続行中。段階3–5、最終全レビュー、採否・条件付き保持/sampling、完了監査はまだ完了していない。

中間監査では6suite×219=1,314の全判断と3checkpoint×2,554の同一NLL対象をraw/hash/実履歴/再利用元に結び付けて確認した。[中間監査](../reports/phase7/chat-improvement-20261012/intermediate_review_audit.json)。新DEVのC1文法2は61件、そのうち関連性2未満は46件。24の同じfamilyで提供履歴/自生成最終の文脈2はC1 7/4、C0 4/2で、両方の不足が残る。[採点済み記録の再集計](../reports/phase7/chat-improvement-20261012/intermediate_analysis.json)。正解語からの自動採点ではない。

実行source snapshotをWindowsからWSLへ戻す際、旧Tokenizer実装の混在改行をLFへ揃えると凍結hashが変わることをCPU監査で検出した。凍結実行sourceとWindows保存snapshotは原hashのままで、変わったのはWSLの保存コピーだけだった。保存コピーをbyteのまま戻し、18source hashを再確認した。report/source・raw・configはGitのtext正規化対象から外し、過去の凍結sourceを編集せずにそのbyteを保存する。

### 教材構造から分かった追加の仮説

凍結済み[教材生成のrender](../src/jmicro/chat_curriculum.py)を静的に確認した。自作daily/direct/negation/clarification/speakerには、名前を名乗るUserと「はい。どうぞ」等の正しいAssistantの前置きが付く。correction/contextにも正しいAssistantの確認文を含む。全自作targetは最後のAssistantだけを教師にし、これらの先行Assistantは条件入力のみで、予測対象ではない。これはmaskのバグではなく教材設計の選択だが、前置きなしで新しい話題を投げられる最初の応答や、誤った自発話からの回復を十分に教えたとは言えない。

説明を求めるdirectの正解には「お話で『答え』と説明されているためです」が共通で付く。DEVで根拠のない同じ説明だけが返る例や名前のない敬称が出たことと整合する。ただしこの構造だけが原因と確定した比較ではない。最終TRAINの意味/役割の正解を確認した280sample passは、前置き・文型・語彙への汎化を保証しない。

次の教材比較を計画する場合は、会話の最初から教師にするtarget、名前未提示の会話、異なる自然な言い回しを設計に含める。与えられた条件が同じでも余分な説明を付けない短い正解、答えの種類（人/場所/時間/数）の区別、自然会話の多様性を優先する。現在の新DEVの文面や誤答をそのまま教材へコピーせず、別の未使用DEVと別familyで検証する。これらは後続の仮説・計画で、現在の凍結TRAINへ変更を加えていない。[構造の確認記録](../reports/phase7/chat-improvement-20261012/curriculum_structure_inspection.json)。

## 最終教師予算への到達

C0は2026-10-12T02:19:56ZにBまでの学習を完了した。3,647更新、Assistant教師1,899,555、EOT121,098、非PAD入力30,446,373、physical入力189,890,560。最後は193教師の完全応答groupで、超過0。最終state SHA256 `165523836f212fb59be32b7d0f42276b2eed968cb4c896b82b01a84a73540734`、WSL `C0/checkpoint-00003647.pt`。これは学習の完了で、最終品質の合格ではない。

同じnative workerはC1のt1全stateを読み込んでBまで続行中。root PIDは共有するので、C0のjobがlearning_completeでも全worker終了前に別GPU評価を起動しない。追加のWindows durable chainが既存学習workerの実PID/startと正常終了/元UI復帰を待ち、両条件のCPU全state/数量監査を通過後、frozen wrapperでC0→C1の全保存点評価を順に行う。chain sourceは起動時SHAに結び付けた。生成完了も全内容採点の完了とは分ける。

全state監査はversion2、model/optimizer/scheduler、Python/NumPy/Torch/CUDA RNG、sampler/counters/digest、lineage/spec/manifestを確認し、各parameterのAdam step数、scheduler更新とLR、完了更新の消費量を実metrics/CPU dry-runと照合する。CPUでcheckpointを検証し、監査に失敗した場合はその後のGPU評価を開始しない。元のfrozen training/evaluation sourceを変更する修理ではない。
