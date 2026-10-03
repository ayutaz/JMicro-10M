# Phase 5: 目的・ゴール・実行計画

2026-10-03、ユーザーがPhase 5の計画から完了までを指示し、Phase 4での停止を解除した。今回の区切りはPhase 5完了。Phase 6の本学習は起動しない。

## 目的と最終成果物

小予算で学習実装の問題を発見し、本学習へ進める候補を根拠で最大2つ選ぶ。100M時点の自然な雑談完成は要求しない。既存のBase/Chat品質目標は維持し、達成したと誤記しない。

成果物はoverfit/smoke/comparison report、実験config、各runのmetrics/checkpoint/source snapshot、候補選定理由・棄却理由、Phase 6への引継ぎ、完了監査。集約reportと判断はGit保存し、大型成果物はWSLの永続領域へ保持する。

## 固定条件

- 公開pilot/Tokenizerの固定revision/hashを使用。trainだけで学習し、corpus devと固定Base dev 80件で選定する。test、Chat suiteは使用しない。
- seed 42、AdamW betas 0.9/0.95、eps 1e-8、decay 0.1（Norm除外、共有embeddingを含む行列）、clip 1、FP32 weights/BF16 autocast、context 1024、warmup/cosineを基準にする。
- 主比較はmicro batch 8、accumulation 1、effective 8,192 tokens/update、eager/math-only。100Mで約12,208更新を確保するため、最大容量batchとは異なる小探索設定を採用する。compile/defaultとeager/defaultはbatch 8の厳密再開一致を満たさず棄却した。初期weights・読込直後weights・消費列は一致し、defaultの更新6で重み差約3.9e-5、math-onlyでは差0を観測した。失敗runと診断を保持し、math-onlyで200 vs 100+100を再検証する。許容値は緩めない。
- 同じ凍結予算内で中断・再開し、schedule/source/data/configを途中で変えない。学習率・QK-Norm以外は対照と同一にする。
- pilotはT8K約6.88M/T4K約8.40M unique stream tokens。100Mはpilot反復の比較であり、新規100M corpusや大規模データのscaling結果と呼ばない。unique量・epoch・消費bytesを併記する。

## 実験順と事前の合格条件

| 段階 | 予算・設定 | 合格条件 |
|---|---|---|
| 実装検証 | QK-Normなし候補、batched評価、同一環境resume | 関連CPU testsがskipなしで通り、CUDA有限値、token列・loss・全state再開一致 |
| 100件overfit | T8K、train 100文書、文書単位sampler、context 256、batch 8、LR 0.002、最大6,000更新（12.288M padded input slots、実教師tokenを別記） | 同じtrain文書の本文NLL/token ≤0.5、teacher-forced正解率 ≥90%、train例の32-token prefixから16-token完全一致率 ≥50%、本文末尾からのEOS argmax正解率 ≥50% |
| 10M smoke | T8K、全Web train、context 1024、batch 8、1,221更新（10,002,432 tokens） | 全loss/gradient有限、loss低下、初期重みよりdev BPB改善、保存再開一致、生成runnerが正常。固定suiteの自発EOS停止率は診断として残す |
| 100M主比較 | T8K/T4K各12,208更新（100,007,936 tokens）、LR 0.002、warmup 200 | dev BPB改善、非発散、同じdev文書・bytes・共通短文window・固定生成条件で比較可能 |
| QK-Norm比較 | 主比較で有望な一方のみQK-Normなし、同じ100M予算 | 正規化だけを変え、BPB・速度・生成失敗・推論経路の制約を比較 |
| LR比較 | 上記で有望な構成のLR 0.001、同じ100M予算 | LRだけを変え、採否と理由を記録。0.003追加は発散/未改善の修復が必要な場合に限定 |

overfitのprefix/末尾は固定したtrain文書だけから選び、対象件数・ID・hash・採点可能なtoken数を記録する。損失低下だけで「memorize成功」としない。未達なら原因を切り分け、閾値を緩めず別runで修復する。追加予算は修復理由と設定を開始前に記録する。

修復記録（2026-10-03）: `run-20261003-math`の固定連結block overfitは6,000更新でloss約0.002でも文書単独NLL/token 3.206、teacher accuracy 65.4%、continuation 2%、EOS 69%となり不合格。blockの前後contextを覚えた疑いがあり、train 100文書をそれぞれ独立したbody/EOS windowで学習するsamplerへ変更する。windowの重複contextとpaddingは教師対象外、各epochで本文とEOSを一度ずつ教える。通常のsmoke/100Mは元のblock samplerを維持する。修復runは新規初期化・同じ6,000更新上限・同じ基準とし、変更sourceでT8K/T4Kと文書samplerの厳密resumeを再確認する。旧run/checkpoint/reportは保存する。

## 公平な評価と候補選定

全dev文書の本文を一度採点し、共通canonical bytesを分母にBPBを計算する。EOS NLLは分離。共通短文32 windowでも比較する。固定Base devは抑制ありgreedy・抑制なしgreedy・sampling 3 seeds（0.8/0.9）を各80件、計400出力。生成ID・Unicode・反復・role・空応答・停止を記録する。

主値は同一stream-token予算。補助として保存checkpointの消費body bytesとGPU更新時間から近い予算点を選び、差・実tokens・更新数を併記する。これは近似予算合わせで、同一文書順・厳密同一bytes/timeとは呼ばない。条件が揃わない場合は未実施と明記する。評価時間とcompile初回を学習更新時間から分離する。

候補はdev BPB、共通短文BPB、同じ文書のpaired bootstrap差、生成失敗、速度、Tokenizer fallback、checkpoint再現性、推論互換性から選ぶ。BPB差が不明確なら最大2候補を残す。QK-NormなしはQwen3参照/exportへそのまま写せないため、未実装の配布経路を採用リスクとして記載する。MuonはAdamWが安定して改善する場合、この段階では実装・比較を追加せず、その判断理由を残す。

devで使う将来の品質目標は既存protocolのBase文法70%、Chat文法・関連性70%、文脈60%、停止95%以上等を維持する。数値を変更せず、100M候補の結果を見る前にprotocolのtargets.statusをfrozenへ変更した。量子化の許容退行幅はfloat品質評価後・候補選定前に別途固定する。Phase 5の機械的gateと将来の品質目標を区別し、最終testを見て基準を変更しない。

## 予算・永続実行・終了

事前の100M×4候補compute見積もり約30分はPhase 4の大batch/default速度を用いた算術値。採用したmath-only / batch 8のsmoke 650更新時点では定常中央値117,172 tokens/sで、100M一本約14.23分、4本約56.9分へ更新した。実時間は各runで再計測する。評価、保存、実装、overfit、修復は別加算。100Mは別の累積scheduleで新規初期化し、10M smoke重みを無断で流用しない。phase5 run directoryにjob PID/boot ID/start ticks、stage、log、凍結plan、checkpoint SHAを保存し、単一GPU排他で順次実行する。

全gateと成果物を現在の状態から監査し、候補config、`candidate_selection.md`、`completion_audit.json`を保存・コミットする。100Mの結果がすべて悪化する場合は原因修復へ戻り、候補選定を成功扱いにしない。Phase 6の拡張データ・長期schedulerは引継ぎ事項として残す。

## 長期schedulerの選択と引継ぎ

Phase 6の延長可能な本学習にはWSD（warmup→stable→decay）を採用する方針を固定する。stableの継続checkpointと、各予算点で分岐する評価用decay checkpointを分け、分岐computeを計上する。Phase 5の100Mは比較条件を揃えた凍結cosine scheduleであり、その最終optimizer stateへ予算だけを足して本学習を継続しない。候補選定はarchitecture/Tokenizer/LRの選択であり、次の拡張corpusで本学習を新規初期化する。

WSD自体は現在のtrainerへ未実装。Phase 6の再開時に実装・保存再開・stable/decay分岐のstate検証を行い、拡張corpusの規模と実測速度からwarmup/stable/decayのtoken予算を凍結してからGPU本学習を開始する。今回の停止境界に従い、その実装と本学習は起動しない。math-onlyでの本学習batch容量も別途実測する。Phase 4のdefault-backend最大batchをそのままmath-onlyの保証として扱わない。
