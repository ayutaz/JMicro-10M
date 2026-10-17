# 評価仕様と現行の適用

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV80の絶対条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、規定反復≤18、empty/role/Unicode失敗0。相対一貫性差≥8、paired CI95下限>0、BPB/strong/cached/historical保持も必要。最終TEST停止95%は別条件であり、DEVのEOS37/80で代替しない。総trainable9.5M〜10.1M、参照10,001,152を維持し、日本語領域・元品質を勝手に狭めたり下げたりしない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

## 最新評価の範囲と制約

同25M nativeCE対照とRDrop候補の元主教師streamを照合済み。二回forwardのphysical streamは倍になり、学習torch RNGはdropoutのため対照と意図的に異なる。腕内の保存再開ではRNGを含む全state一致が必要。全80個別理由はCodex非blindであり、人間blindではない。

全文DEVは89416文書/42003934本文token/164344743bytes、context1024/stride512/batch16/limitNoneを固定し本文一度/EOS別集計。36 CPU checksは合成fixtureで、実全文評価は未実行。標準440 suiteは特殊ID0,1,2,4,5,6を抑制、pilot80は7も抑制。設定差を消して同条件と主張しない。Python open監査をnative OS sandboxと記載しない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## v1契約と後続実験を区別する

前回Chat139は4suite×219応答×7点の28セット/6,132内容判断とNLL7点×2,634 target。各suiteは固定履歴80、抑制なし80、自己生成履歴24会話59turn。原品質を維持し、最終t3の全回帰・内容56/80・自己文脈15/24・停止76/80と57/59・empty上限4/2・role/raw Unicode/履歴削除0、対照比反復非増加、新DEV family paired CI下限>0を判定して不採用。実験別の分母とguardは[凍結139](139_chat_lr_comparison_plan.md)を参照し、v1の文脈30問へ混ぜない。

Chatの全内容判断はCodex非blind。独立人間blind、fresh学習seed43、正式保持、全文DEV・最終suite、選定封印後TESTと正式採用は未確認。既存のhuman_scoresのnullをCodex評価で上書きしない。

元Chat TEST20行は139準備時にCPU構文解析した。学習・GPU評価への使用0だが未参照とは呼ばない。将来の有資格Chat最終確認には新たな封印TESTが必要。元Base TESTはそのChat事故では解析していないが、後続144のBase readerでTEST20 promptがCPU解析された。未参照とは呼ばない。raw EOT/EOS/反復/不正UTF8/置換文字を維持し、制約decodeと表示policyは別に記録する。

以下は凍結v1の設計契約・式・rubricと、その時点の基盤検証。途中の利用状況や計画は現在の採否・再開許可ではない。

## 評価対象とsplit

Baseは100件の自然文completion、Chatは100件の短文対話。各10 category、dev 80件/test 20件。family単位でsplitし、manifestのID・hashが不一致なら比較を止める。Tokenizer学習・事前学習・SFTに評価本文を入れない。Phase 1のcorpus validation/testはこの独自生成suiteとは別に固定する。

開発時はdevで設定・checkpointを選ぶ。最終testの結果を見て閾値を下げない。testで未達なら報告し、次の改訂は新しい未使用testを用意する。小さいtestの率は分母・件数・category別結果と信頼区間を併記し、0件失敗を未知入力にも失敗しない保証として使わない。

Phase 6拡張corpusのdev/testはPhase 1 pilotと別manifestで固定した。新devは89,416文書 / 164,344,743 canonical body bytes。全splitを構造監査したが、testをモデル評価・候補選定に使っていない。②の4 dev文書CUDA採点は評価の状態保全検証で、全文品質評価ではない。新dev同士の推移を比較し、pilot BPBとの差を改善量にしない。[次回の評価計画](27_phase6_remaining_plan.md)

## BPBとTokenizer比較

共通前処理はCRLF/CRをLFへ統一し、U+0000を除去する。他の空白・タブ・Unicode表記は保持し、壊れたUTF-8を拒否する。NFKC/NFCを暗黙適用しない。rawとcanonicalの両方のhash/byte数を残す。期待値は[golden例](../eval/tokenizer_golden.json)へ固定。

`BPB = 本文NLL総和 / (ln(2) × 採点したcanonical UTF-8 bytes総数)`。NLLは自然対数、分子・分母を文書集合で合算する。BOSを条件に最初の本文tokenから採点し、全本文をちょうど一度採点する。BOS/PAD/role/EOT/EOSのlossは本文BPBから除外、EOS lossは別記録。空文書は分母0として採点集合から外し、除外数を記録する。

contextは1024、長文の初期stride案は512。window間でscore済み位置を二重計上しない。文書境界へBOSを入れ、無関係な文書の履歴を混ぜない。4k/8kは同じ評価文書を使う。両方が収まる共通text windowの比較と、各1024-token contextの運用比較を別条件にする。学習tokens固定・学習bytes固定・GPU時間固定を区別し、token perplexityをTokenizer間で直接比較しない。

Phase 4でモデルNLL、1024/stride 512採点、本文一度採点、EOS分離、共通bytes、共通短文32 window、固定Base dev 80×5条件を実装・実GPU検証した。dev 924文書 / 共通1,633,458 bytes、test未使用。[評価契約report](../reports/phase4/base_evaluation_contract_report.json)。これは小さい検証checkpointの結果で、100M品質比較ではない。

## 生成条件

- 固定suiteはgreedy、seed 42、最大64 new tokens。
- sampling suiteはtemperature 0.8、top-p 0.9、seed 42/43/44で別集計。
- Baseの主停止IDはEOS=3、ChatはEOT=7またはEOS=3。
- 本文生成時はPAD/UNK/BOS/System/User/Assistant（0/1/2/4/5/6）を抑制する標準条件と、抑制なし診断条件を分ける。
- prompt+生成の上限は1024。超過時は古い完了turnから削除して再prefill。最後のUserだけで予算に収まらない入力は除外理由を記録し、黙って意味を切り捨てない。
- 会話bodyを別encodeし、role/EOTを構造IDとして挿入する。本文中の同じ文字列を構造として扱わない。

Chat固定履歴の30件は2〜4 User turns、うち`context` categoryは3〜4 turns。既存Assistant本文は評価例の固定条件である。これだけで実際に複数turnを続けられるとは判断しない。後続の限定SFTではモデル生成を戻す実履歴24会話59turnを評価済み。v1固定履歴と各実験の分母は別に保存する。

## 人手rubric

| 指標 | 0：破綻 | 1：部分的成立 | 2：成立 |
|---|---|---|---|
| 文法 | 文意を読み取れない、空応答 | 助詞/接続等に不自然さがあるが概ね読める | 自然に読める日本語短文 |
| 関連性 | 入力と無関係 | 相づちのみ、話題を一部拾うが逸れる | 入力の内容に沿う応答/質問 |
| 文脈 | 前turnの条件/訂正を失う | 一部保持するが曖昧または誤りを含む | 必要な条件/訂正を保持する |

文法と関連性はすべてのChat応答へ採点する。文脈は`correction/followup/context`の30件を対象にし、対象外は`null`で分母から外す。Baseの主目標は文法で、prefixとの関連性も補助記録する。数字・常識の正答と文法を混同しない。

反復、矛盾、role漏出、停止失敗、Unicode破綻、空応答は得点と独立したflag。文法・関連性が良くても反復flagは立つ。自然な短文を高く評価し、長い返答を自動優遇しない。

[11件の採点例](../eval/rubric_examples.json)で、関連した返答/部分的逸脱/無関係、訂正保持/曖昧/訂正失敗を手動で区別した。設計時のCodexによる採点であり、独立した人間の一致率は未測定。Phase 7でモデル名を伏せて人手評価し、一部20%を複数評価者で重複採点して一致率を残す。LLM judgeは使用する場合も補助として名・version・promptを保存する。

## 自動失敗指標の定義

停止成功は上限に達する前にEOT/EOSで止まった応答の割合。停止IDだけの空応答は停止成功にも空応答にも計数する。role漏出はdecodeで消える前の出力ID列で禁止role 4/5/6を検出する。抑制なし結果も残し、抑制による0件とモデルの能力を区別する。

空応答は空白を除いた本文が空のもの。Unicode破綻はraw byte列が不正UTF-8、または入力由来でないreplacement文字を出したもの。Tokenizer APIが置換して隠す前のbyte列も確認する。

反復flagの初期自動定義は、2文字以上の同じ本文substringが連続3回以上。4文字n-gramの`1 − unique/total`も診断値として保存するが、単独で合否閾値にしない。通常の会話上の反復との誤検知を人手sampleで確認する。文字数、bytes、tokens、返答長p50/p95を併記する。

Base生成runnerは停止・role ID・UTF-8・空応答・反復と生成長を記録する。document paired bootstrapと生成ID/flag照合はPhase 5で実施済み。後続Chatのrubric/実履歴評価は実行済み。独立人間blindと人間による誤検知確認は未確認。Phase 4のgreedy EOS停止は両モデル0/80で品質目標は未達。実装のPASSをモデル品質のPASSとして扱わない。

## 数値一致・seed・統計

初期許容値はFP32参照logits `atol=1e-5, rtol=1e-4`、BF16 logits `atol=0.05, rtol=0.02`。strict FP32 resumeはweights `1e-7/1e-6`、loss `1e-6/1e-5`。consumed token IDsとparameter countは完全一致を要求する。参照FP32ではTF32を無効化する。

これらは機械可読protocolへ固定した数値契約。新backendの比較でも失敗runを通す目的で緩めない。同一CUDA/backendでの採用学習経路は全state完全一致を確認する。Phase 4のBF16同一環境resumeは全stateが完全一致し、compile logitsも既定の合成atol/rtolを維持して通過した。同一hardware/version/backend内の再開を対象とし、iMac/CUDA間のbitwise一致は要求しない。

training seed 42、greedy seed 42、sampling seedsとbootstrap seedはconfigへ記録する。training/generation/bootstrapでRNGを分離し、評価が学習RNGを進めないようにする。Python/NumPy/PyTorch/CUDAとpilot block samplerの状態はcheckpointへ保存済み。評価RNG保全も実CUDAで検証した。Phase 6②では拡張shardのWSD stable/decay再開と元枝不変性をCUDA全state完全一致で確認し、4文書のdev評価前後のRNG/model/modeも保全した。全74 tests / skip 0、73 GPU checks。budgetを変える通常resumeは許可せず、decayは独立runでglobal更新数と追加枝tokensを分ける。この当時の準備では複数source mixture samplerとstable予算延長forkは未実装だった。後続の明示forkとChat document samplerは別の実装・証拠を持つ。

BPB差は同一document、会話差は同一prompt/dialogueを対応付け、paired bootstrap 2000回、seed 42、95%信頼区間を初期仕様とする。tokenを独立sampleとして扱わない。greedyとsamplingの率、category別結果を別記録する。

## 採用基準とデータbucket

初期目標はBase文法2率70%、Chat文法・関連性とも2の率70%、対象会話の文脈2率60%、停止95%以上、空応答5%以下、role漏出1%以下、固定suiteのUnicode破綻0件。Phase 5の100M結果を見る前に採用基準を凍結済み。量子化の許容退行幅はfloat dev評価後・量子化候補選定前に固定し、現時点では未決定。

sourceは`commercial_strict/commercial_web/sharealike`を分離管理し、条件不明は`excluded`。非商用等の研究限定データを使う場合は別runとして明示し、配布候補へ自動混入させない。Phase 1で固定source/subsetの条件を記録した。Phase 4のBaseはWeb bucketだけを選び、会話/sharealikeを混ぜていない。追加sourceの採用条件は拡張時に確認する。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="現行のbase採否と読取り境界"></a>
