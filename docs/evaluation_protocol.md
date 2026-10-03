# 評価仕様 v1

実装状況更新: 2026-10-03。機械可読protocolの閾値・split・数値許容値は維持する。Base評価は実装済み、Chat品質評価・人手採点・bootstrapは未実施。[現在の実測](21_phase4_completion.md)

作成: 2026-10-02、Phase 0。機械可読の正本は[protocol.json](../configs/evaluation/protocol.json)、入力は[固定評価データ](../eval/README.md)。設計契約を固定する資料であり、モデル性能の評価結果ではない。

## 評価対象とsplit

Baseは100件の自然文completion、Chatは100件の短文対話。各10 category、dev 80件/test 20件。family単位でsplitし、manifestのID・hashが不一致なら比較を止める。Tokenizer学習・事前学習・SFTに評価本文を入れない。Phase 1のcorpus validation/testはこの独自生成suiteとは別に固定する。

開発時はdevで設定・checkpointを選ぶ。最終testの結果を見て閾値を下げない。testで未達なら報告し、次の改訂は新しい未使用testを用意する。小さいtestの率は分母・件数・category別結果と信頼区間を併記し、0件失敗を未知入力にも失敗しない保証として使わない。

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

Chat固定履歴の30件は2〜4 User turns、うち`context` categoryは3〜4 turns。既存Assistant本文は評価例の固定条件である。これだけで実際に複数turnを続けられるとは判断しない。Phase 7でモデル生成を履歴へ戻すrolloutを追加し、dialogue全体の失敗も測る。

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

Base生成runnerは停止・role ID・UTF-8・空応答・反復と生成長を記録する。Chatのrubric/rollout、人手による誤検知確認、paired bootstrapはPhase 5〜7で行う。Phase 4のgreedy EOS停止は両モデル0/80で品質目標は未達。実装のPASSをモデル品質のPASSとして扱わない。

## 数値一致・seed・統計

初期許容値はFP32参照logits `atol=1e-5, rtol=1e-4`、BF16 logits `atol=0.05, rtol=0.02`。strict FP32 resumeはweights `1e-7/1e-6`、loss `1e-6/1e-5`。consumed token IDsとparameter countは完全一致を要求する。参照FP32ではTF32を無効化する。

これらは検証前の提案。採用backendのbaselineを測って比較前に調整・固定し、失敗runの後にそのrunを通す目的で緩めない。Phase 4のBF16同一環境resumeは全stateが完全一致し、compile logitsも既定の合成atol/rtolを維持して通過した。同一hardware/version/backend内の再開を対象とし、iMac/CUDA間のbitwise一致は要求しない。

training seed 42、greedy seed 42、sampling seedsとbootstrap seedはconfigへ記録する。training/generation/bootstrapでRNGを分離し、評価が学習RNGを進めないようにする。Python/NumPy/PyTorch/CUDAとpilot block samplerの状態はcheckpointへ保存済み。評価RNG保全も実CUDAで検証した。複数source mixture samplerは未実装。

BPB差は同一document、会話差は同一prompt/dialogueを対応付け、paired bootstrap 2000回、seed 42、95%信頼区間を初期仕様とする。tokenを独立sampleとして扱わない。greedyとsamplingの率、category別結果を別記録する。

## 採用基準とデータbucket

初期目標はBase文法2率70%、Chat文法・関連性とも2の率70%、対象会話の文脈2率60%、停止95%以上、空応答5%以下、role漏出1%以下、固定suiteのUnicode破綻0件。Phase 5までにdev/pilotで採用基準を固定する。量子化の許容退行幅はfloat dev評価後・量子化候補選定前に固定し、現時点では未決定。

sourceは`commercial_strict/commercial_web/sharealike`を分離管理し、条件不明は`excluded`。非商用等の研究限定データを使う場合は別runとして明示し、配布候補へ自動混入させない。Phase 1で固定source/subsetの条件を記録した。Phase 4のBaseはWeb bucketだけを選び、会話/sharealikeを混ぜていない。追加sourceの採用条件は拡張時に確認する。
