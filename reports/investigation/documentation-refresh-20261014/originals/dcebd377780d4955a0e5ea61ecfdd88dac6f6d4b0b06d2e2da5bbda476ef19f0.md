# EOS・反復・UTF8改善の1〜3：実行結果

2026-10-04。ユーザー指定の①表示末尾処理、②同じ完成5Bから各100Mの対照学習、③原評価・内容確認を完了。**短文仕上げで自然EOSと反復は改善したが、samplingのraw Unicode失敗2件により最終採用gateは不合格。短文重みは診断用として保持する。** 表示処理は独立に改善できた。Base/Chatの実用品質達成とは扱わず、10B/Chat/追加loss/decoder sweep前で停止する。

## 目的と判定

目的は、max-token上限で切れたUTF8末尾を安全に表示し、短い完結文20%の低LR仕上げが5Bの自然停止と反復に転移するか、同じWeb対照で確認すること。[計画](37_eos_repetition_utf8_improvement_plan.md)の原raw評価・採用条件を保持した。[保存証拠の確認](../reports/phase6/eos_5b_finish_review.json)44項目成功、[内容確認](../reports/phase6/eos_5b_content_review.json)、[Unicode診断](../reports/phase6/eos_5b_finish_unicode_review.json)。保存stateの検証成功と品質gateの不合格は別の結果である。

## 1. 表示末尾処理

`src/jmicro/text_display.py`のstrict incremental UTF8 helperをtorch/HF/GGUF共通の結果処理に接続した。通常の`text/display_text`は完成文字だけを表示し、`raw_text`、generated IDs/bytes、raw validityとstop reasonを保存する。max-tokenの未完成末尾1〜3bytesだけを保留し、`truncated_utf8_tail`とpending bytesを返す。途中の不正bytesや不完全EOS/EOTはerrorとして残す。強制EOS、追加生成、Tokenizer変更はない。

[旧5Bの保存400件](../reports/phase6/text_display_verification.json)で398正常textは不変、同じbase-070の2件の末尾e6a5だけを表示から除けた。元raw Unicode失敗2件とmax-token停止は保持した。関連33testsの失敗・error・skipは0。backend接続はmock controller/codec testsで確認した範囲であり、新重みの全backend/export/量子化評価ではない。

## 2. 同じ5Bから低LR各100M

モデルは10,001,152 parameters、準備済みtrainは12,225,819,077 tokensで変更なし。親はfinal5B update152588、5,000,003,584 input tokens。同じmodel/Adam moments/RNG/Web cursorを新しい二枝へforkし、seed42、peak LR0.0002を2,900 updates維持、152 updatesで0.00002へcosine decay。batch32/context1024、uv/WSL2/RTX4090/BF16/Flash/compileを使用した。

各3,052 updates、追加100,007,936 input tokens、最終update155640/累積5,100,011,520。科学合計200,015,872 tokens。実CUDA連続4対2+保存再開2の全state/history一致を混合・schedule境界で確認した8 updates/262,144 tokensは別計上した。両枝の全更新は有限・連続で、最終checkpointにoptimizer/scheduler/Python・NumPy・Torch・CUDA RNG/両sampler cursor/消費counterを保存した。

Web対照は100,007,936 Web tokens。短文条件はWeb80,019,456＋short19,988,480 tokens（19.9869%）。既存accepted445,501完結単位/21,000,010 tokensを再利用し、短文poolはepoch0で周回なし。dev/testを学習せず、全コーパスの再抽出・重複照合・独立全件監査は追加しなかった。学習区間の実時間はWeb160.883秒、short149.772秒で、checkpoint IOを含む。

## 3. 原評価・内容確認

同じ保護dev89,416文書、164,344,743本文bytes、42,003,934本文tokensでcommon-byte BPBを評価。context1024/stride512/batch16、Math CUDA BF16/FP32 CE。固定dev80 prompt、greedy64-token上限、EOS bias/penalty/強制停止なし。以下の自然EOS・反復は元の固定指標で、BPBは小さいほど良い。

| 条件 | 全文dev BPB | 固定自然EOS | 固定反復 | 固定raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 親5B | 0.964484 | 0/80 | 59/80 | 1/80 |
| Web100M仕上げ | 0.958092 | 0/80 | 57/80 | 0/80 |
| 短文20%・100M仕上げ | 0.959011 | 13/80 | 51/80 | 0/80 |

短文の全文BPBは新Web対照比+0.095894%、元の+1%条件内。両仕上げは親BPBより改善したが、データ量・LR曲線等の効果を混同せず、短文の比較効果は同じ新Web対照との比較で判断する。

抑制あり・なしgreedyとsampling3seeds（42/43/44、temperature0.8/top_p0.9）、計400の条件keysは親と同一。screen/finalの固定80 generated IDsも一致した。

| 条件 | 全400自然EOS | 全400反復 | raw Unicode失敗 | empty / role漏れ |
|---|---:|---:|---:|---:|
| 親5B | 5/400 | 122/400 | 2/400 | 0 / 0 |
| Web仕上げ | 13/400 | 121/400 | 0/400 | 0 / 0 |
| 短文仕上げ | 129/400 | 103/400 | 2/400 | 0 / 0 |

screenは全5条件合格し両枝全文へ進んだ。全文のBPBとIDs条件は合格したが、短文の全400 raw Unicode0条件は不合格。親に失敗があることを許容数の増加に使わない。増量gateもWebは合格、短文は同じ新失敗条件で不合格。品質目標は両方未達である。

短文の失敗は次の2件。保存bytesをproduction helperに通したCPU診断のみで、GPU再推論はしていない。

- base-039、sampling seed43：byte30〜31にinvalid start byte。文章途中の不正UTF8で、末尾処理では修復せずerror/raw failureを残す。
- base-084、sampling seed42：64-token上限のbyte212〜213に未完成末尾。表示helperは末尾1byteを保留できるが、raw failureと上限停止は残す。

既存補助80のEOSは親0→Web0→短文28、反復35→35→27。教師文末EOS argmaxは0→0→45、平均NLL3.724968→3.718323→1.093626。補助の改善は元固定評価の代わりに使わない。教師文末の値と自由生成軌道のEOS順位は別で、保存軌道診断は最小順位の要約であり全step配列ではない。

短文の固定全80、自然停止129件の116種類の全文、補助自然停止28件、Web自然停止13件を読んだ。靴を履く、乾いた靴下を履く、水を入れて飲む等の短く文脈に合う停止はある。一方、2+1を2個とする、1時間休憩後の時刻を誤る、甘いものを食べない条件に反する、二回・言い換え反復も残る。元の三回完全一致の反復判定を変えていない。自然停止増加を正答率改善と同一視せず、独立人手blind採点・testは未実施。

## 保存・終了点と次回案

GPU lock内の累積実時間2,253.853秒（37分34秒）、上限3,000秒以内。これはsetup/IO等を含む実時間でkernel時間ではない。job complete、actual Linux464/Windows21524終了、GPU compute processなし。runはLinux `reports/phase6/eos-5b-finish-100m-20261004/`。ログ、凍結config/source、全文/生成、resume gate、全旧成果物を保持する。完了jobの`bash scripts/run_eos_5b_finish.sh`を再実行しない。

| 保存重み（run相対） | SHA256 |
|---|---|
| web/checkpoint-00155640.pt | c1b83c8e03f653af378797fbfea604ea33aec2134a6fea936ea0bb2157a9e0bb |
| short20/checkpoint-00155640.pt | 19a960feb5b809c277cd710f23765e14d27099502153561ba437eee20dd42d54 |

親final5B SHA `1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a`は不変。表示修正は保持し、短文重みは未採用の診断候補として保存する。今回の1〜3の実行・報告を完了して停止した。

次回は途中不正UTF8と末尾切断を別々に扱う単一のUTF8制約付きdecoding案を、同じ保存重み・元64上限・元raw400指標で比較することが候補。EOS/EOTは完全なUTF8境界だけで許す案でも、上限での未完成末尾は別途扱う必要がある。raw Unicode0、自然EOS/反復/BPBの元条件を保持し、表示だけの補正を採用成功に数えない。反復・意味品質には既存計画のCE対sequence unlikelihood各25M案もあるが、新loss/rollout/resume検証と予算凍結が必要。いずれも提案であり今回実装・起動せず、10B/Chatへ自動移行しない。
