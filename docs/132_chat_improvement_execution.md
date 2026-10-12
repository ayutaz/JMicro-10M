# 計画131・教材改善比較の実行記録

開始: 2026-10-12 JST。ユーザーのgoal「5まで進めてください」により、[計画131](131_chat_improvement_execution_plan.md)の段階0–5を明示再開した。保全、C1教材/新DEVの準備、教師量runnerと技術gate、C0/C1学習、全評価、結果報告まで。C2履歴回復・効率比較・独立seed/最終採用・量子化・公開は範囲外。

## 現在の実状態

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
