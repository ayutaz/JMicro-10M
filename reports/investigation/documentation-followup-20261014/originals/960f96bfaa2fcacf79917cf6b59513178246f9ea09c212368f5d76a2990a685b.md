# 5B後のEOS・反復・UTF8末尾改善：調査と次回計画

2026-10-04。今回の依頼は調査と計画作成。保存済み結果のCPU再集計とUTF8 bufferingの確認を実施し、学習・GPU推論・production生成処理の変更は行っていない。[調査記録](../reports/phase6/eos_5b_improvement_research.json)、[機械可読の提案](../reports/phase6/eos_5b_improvement_plan.json)。以下は次回の実装・実行案であり、実行configや完成commandではない。

## 調査結果と優先順位

**第一候補は完成5Bから低LRで短い完結文20%の仕上げを、Web100%対照と各100Mで比較すること。UTF8の表示処理はCPUで先に直す。** 10Bへの単純延長、Tokenizer再学習、EOS損失の重み増加、反復損失追加、decoding変更を初回から同時に混ぜない。

| 観測 | 根拠 | 次の判断 |
|---|---|---|
| 5Bでも固定自然EOS0/80、反復59/80 | [5B比較](36_base_5b_comparison.md)。本文BPBは0.964484へ改善 | 一般Web増量だけでは今回の停止問題を解決していない |
| 正しい文末のEOS予測は改善している | 同じ89,416文書の保存済みEOS平均NLL：元2B2.302868、低LRWeb2.227720、5B2.223077、短文参考2.174987 | EOSが全く学習されていないとは言えない。自由生成の軌道と完結単位の分布を調べる。これらは教師文末の損失であり自由生成のEOS確率/順位ではない |
| 短い完結単位＋低LRの実測が有望 | 同じ2B親の各100MでWeb→short20：EOS0→27/80、反復55→41/80、全文BPB0.972969→0.974799（約+0.188%） | 5Bへの転移は未検証だが、未知の手法より先に同じ仕上げを一度試す |
| samplingは反復を減らすがEOSは少ない | 5Bの3seeds合計で反復4/240、EOS5/240。greedyは各59/80・0/80 | decodingによる効果と重みの改善を分ける。既存sampling条件を再利用し初回のparameter sweepはしない |
| 生成64上限でUTF8が切れた | base-070、末尾e6a5、raw170bytes。CPU incremental decoderは完成168bytesを出し残り2bytesを保留 | 表示の末尾処理で対処可能。ただしraw Unicode失敗とmax-token停止は維持し、EOS成功へ数え替えない |

以前の元2B調査でもgreedy20件は512tokensまでEOS0、penalty1.1でも512まで5件しか止まらず長い反復が残った。上限延長やpenaltyだけを第一の解決策にしない。今回の結果は2B診断を5Bで再実行したものではなく、保存記録を用いた判断。

文献でもgreedy等の選択方法により非停止が起こる事例が分析されている。ただし対象はRNNであり、このTransformerの原因を証明しない。[Welleck et al., EMNLP 2020](https://aclanthology.org/2020.emnlp-main.448/)。同じ重みでもdecodingで反復等が変わる研究がある。[Holtzman et al., ICLR 2020](https://arxiv.org/abs/1904.09751)。本計画の主な根拠は本プロジェクト内の対照実験であり、5Bでの改善は仮説。

## 1. UTF8末尾処理をCPUで実装する

現在の`src/jmicro/inference.py`はraw bytesを最後にstrict decodeし、失敗時はreplacement文字を表示する。Tokenizerは単一文字が複数byte tokensになる仕様で、各tokenを個別の文字としてdecodeできない。Tokenizer/語彙/既存lossless codecは変更しない。

推論結果の表示に共有helperを追加し、strict incremental UTF8 decoderで完成文字だけを出力する。途中の1〜3bytesはbufferに保持。EOS/EOT時はfinal=Trueで完結性を確認し、未完了ならerrorとして記録する。max_new_tokensで切れた場合だけ、最後の未完成文字を表示から除き、truncated_utf8_tailとpending bytesを記録する。上限を越える追加生成や強制EOSは行わない。[Python公式のIncrementalDecoder](https://docs.python.org/3.12/library/codecs.html#codecs.IncrementalDecoder.decode)は未完了入力を保持し、final時の未完了をerrorとして扱う。

raw generated IDs/bytes、raw_valid_utf8、stop_reasonは変更しない。text/display_textの契約を明示し、raw Unicode失敗率と表示UTF8の有効性を別fieldで保存。途中のinvalid continuation、surrogate、範囲外code point、unknown tokenを末尾切断として隠さない。これは表示の修正であり、5Bの既存不合格を合格に書き換えない。

CPU調査では保存済み400件中398件のtextが完全一致し、残り2件は同じbase-070の未完成2bytesだけを保留できた。日本語/emojiの途中1〜3bytesと不正UTF8の9probeも成功。今後の実装には、日本語・emoji・ASCII・全正常出力不変・上限切断・EOS/EOT時の未完成・途中不正bytes・unknown tokenの意味のあるunit testsを付ける。torch/HF/GGUFの結果は同じ外部codec/helperに通す。今回は新しいexport/量子化やGPUの全backend評価は不要。

まず表示修正で一区切りにする。raw自体の完結を必ず保証するUTF8制約付きdecodingは、数値選択を変える別案として保留。必要時は独立policy・raw評価として比較する。表示だけ直した候補を元のUnicode gate合格にしない。

## 2. 完成5Bを親にした低LRの各100M比較

親は`reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt`、SHA256 `1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a`。final5Bを通常resumeで増量せず、短い仕上げの明示forkを2枝作る。stable5B/元2B/旧短文枝を保存し、新しい5B枝を前回2BのWeb枝だけと比較しない。

| 項目 | 固定する案 |
|---|---|
| A：対照 | Web100%、100,007,936 input tokens |
| B：改善候補 | Web80%＋32〜64-token完結単位20%、100,007,936 input tokens |
| 共通親state | 同じ5B model/Adam moments/RNG/Web cursor。seed42、初期state hashを記録 |
| 学習率 | peak0.0002、2,900 stable updates＋152 cosine decay、最後0.00002。親actual最終0.0002からのjumpを避ける |
| batch/context | 既存安定batch32/context1024、uv/WSL/4090/BF16/Flash/compileを保持 |
| input予算 | 1update32,768tokens、各3,052updates、科学合計200,015,872tokens。各枝終了5,100,011,520累積tokens/update155,640 |
| 短文量 | 610updates/19,988,480tokens、実比率19.9869%。任意token切断でEOSを付けない |
| 評価変更 | なし。EOS bias/penalty/強制停止なし、raw64-token固定評価を保持 |

既存accepted poolは445,501完結単位、94,157 train親文書、21,000,010 input tokens。短文はこの仕上げに必要な約19.99Mだけ消費し、short sampler epoch0内。旧2Bの別試行での利用歴を保持するが5B親は短文EOS仕上げをしていない。既存pool/auxiliary-dev80をhash binding付きで再利用し、全コーパス監査・抽出・重複照合を再実行しない。dev/testをtrainへ入れず、同じparent splitを維持する。

`LowLRPilotTrainer`/`MixtureSampler`/accepted `TrainView`/screen/auxiliary評価を再利用。現在のrunnerは2B親のpath/update/tokens/判定基準が固定されているため、そのまま起動しない。5B親に対応するrunner/config/schemaと独立outputを実装してから凍結する。旧実験runnerやcore model/training/shardsを無用に変更しない。

親のfinal LRと元Web sampler構造を読込時に確認し、必要箇所のCPU checksと実CUDA連続4対2+保存再開2（8updates/262,144検証tokens）を実施する。混合経路・schedule境界・optimizer/RNG/両cursor/消費counterを照合。科学tokensとは別計上し、変更がない検証を広げ続けない。

## 3. 最小の診断と段階評価

親5Bの全文BPB/固定80/400生成は保存結果を再利用し再実行しない。まず既存補助dev80に対する親5Bのteacher EOS NLL/順位/argmaxとgreedyのEOS/反復を一度記録する。2B親の補助結果を5B親の数値とみなさない。

両100M終了後、同じdev256 BPB＋原固定80greedy＋既存補助80を評価する。補助の正しい文末EOS順位と自由生成各stepのEOS順位を区別して記録。末尾を正しく教える効果が出たか、反復が続いてEOSを選ばないか、空/句読点だけの早期停止へ退行したかを調べる。新suiteや512-token延長は最初の比較に追加しない。

**元のmixture screen gateを維持**：Bの固定自然EOSがAより8件以上多い、反復がA以下、empty/role/rawUnicode全0、dev256 BPBがA比+1%以内、句読点だけの停止なし。固定80の改善と補助80を置き換えない。

Aは元2Bとの元screen安全条件（固定反復+8未満、empty/role/rawUnicode0）と親5Bの固定反復+8未満を両方満たす場合に全文89,416dev/400生成へ進む。親5BのUnicode失敗を許容数の増加に使わない。Bはmixture screen合格時だけ全文/400へ進む。B合格かつAがscreen安全でないとき、比較に必要なAの全文本文BPBだけを実行し400生成は省く。最大2枝の全文評価としてGPU予算を確保する。

**全文gateも維持**：Bの全文BPBは同じ新A比+1%以内、screen/finalの固定80 generated IDs一致、全400のempty/role/rawUnicode0を要求する。従来の元2Bに対する新失敗なし条件と、今回の親5Bに対する退行を両方報告し、親に失敗があるから許容数を増やさない。表示補正によるUnicode0は採用条件に加算しない。

5Bの良い本文予測を失わないかも別途比較する。BPBが保存5B0.964484070比+0.001を越える、反復が親59から8件以上増える、新失敗が出る場合は、旧増量条件に従い10B継続候補にしない。mixtureの+1% gateと増量の+0.001 BPB gateは別の元条件であり混同しない。

全自然停止を内容確認し、早すぎる終了、数量/時刻/否定/因果の誤りを元5Bの同じpromptと照合して保存。元の三回完全一致反復指標を変えず、二回/意味反復の例も併記。独立人手blind評価やtestを未実施なら実用品質達成としない。文法70%・Chat停止95%等のロードマップ基準は維持する。

## 4. 失敗した場合の次案

| 結果 | 判断・次の提案 |
|---|---|
| Bが自然EOS/反復/BPB/raw失敗条件を満たす | 5B短文仕上げ候補を保存。内容誤りも含め報告し比較で停止。Chat/10Bを自動開始しない |
| EOSが改善しても内容誤り/意味反復が残る | 改善候補として保持し、数量・否定条件等の品質は未達と明記。停止率だけを品質達成としない |
| 補助だけ改善、固定80で不合格 | 学習した完結単位が元promptへ転移しない仮説。比率/LR sweepを続けず一度報告して停止 |
| rawUTF8末尾が残る | 表示修正は独立に採用可能、raw gateは不合格。必要なら次の別案でUTF8制約付きdecodingを原raw方式と比較 |
| 反復が支配的でBが不合格 | 次回提案として、同じ親/データ/予算のCE対CE＋sequence unlikelihoodを各約25Mで一度比較。今回は実装/実行しない |

Unlikelihoodは望ましくない反復へ割り当てる確率を下げる損失で、token/sequenceの両方式が提案されている。[Welleck et al., ICLR 2020](https://arxiv.org/abs/1908.04319)。本10Mでの効き目は未検証。もし次の比較へ進むなら、同じ短文CE条件から完全に繰り返された文/phraseのみをnegativeとするsequence方式を1条件（初期案係数0.1、最適値という根拠はない）に固定し、正しい本文・EOS/EOT・日本語byte piecesを単純な過去出現だけで罰しない。各763updates/25,001,984 input tokens、科学50,003,968にrollout推論tokens/timeを別計上、GPU累積上限900秒のscreen-only提案とする。新loss/rollout/samplerの実装と保存再開確認が必要で、係数や比率の自動sweep/追加全文評価はこの案に含めない。

EOSへの一律logit biasや損失重み増加は、空応答/途中停止を増やし得る仮説もあるため初回では選ばない。反復penaltyや同文反復による強制停止は提供時の補助策になり得るが、後者はrepetition_limitという停止理由にし自然EOSへ加算しない。ChatではAssistant body＋EOTの学習が別途必要であり、Base EOSの仕上げをChat停止95%の代用にしない。

## 予算・終了点

CPU小さなbinding/UTF8 probesは5分以内を目安にし、長い全件auditは行わない。pure200M科学学習は前回実測から約5分、screen/補助と合格した2枝の全文/400を含むGPUは約35〜45分、上限は累積3,000秒（50分）。新親補助診断・compile・resume gateもこの上限に含め、超過時に追加retryで続行せず記録する。GPU時間とCPU実装/内容確認時間は別で、実装・記録を含む作業全体は約1.5〜2.5時間の見積もり。

学習前に既存actual PID/boot/start ticks/checkpoint/GPU jobを確認し、新しいrunのlock・hidden Windows WSL launcher・job identity・ログ・latest checkpoint・source/config bindingを永続化する。中断は同じvalid checkpointから再開し重複起動しない。全旧成果物を保持。Pythonはすべてuv run --frozenと必要extrasから実行する。

次回の終了点は「表示末尾処理＋新5Bの各100M比較＋合格時の全文評価＋内容確認＋report/commit」。10B/Chat/unlikelihood/decoder sweepは自動開始しない。今回の調査と計画はここで完了し、実行jobはない。
