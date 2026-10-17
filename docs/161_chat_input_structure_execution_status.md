# 情報配置の対照SFTの実行状況

最新: 両腕学習・全3,466主応答・40途中・36実ブラウザー・全状態/全履歴・復帰の監査を完了した。候補は品質不採用。[最終結果162](162_chat_input_structure_sft_results.md)と[次の計画163](163_chat_next_capability_diagnosis_plan.md)を参照。以下は各時点の経過であり、過去の「未完了/実行中」は現在状態ではない。

2026-10-18。[事前方針160](160_chat_input_structure_sft_comparison.md)に基づき、新しい対照SFTと最終評価の準備を進めている。ユーザーの「4まで」の目標は継続中で、**両腕の学習・全3,466応答の内容確認・実ブラウザー会話・最終採否は未完了**。

## 確定した教材と実行条件

対照は前回候補C1の固定TRAINそのもの。新候補は著作2,048対象の入力配置だけを変え、69組のalias、通常会話・Aya・Dolly、全ての正答を維持する。全消費のCPU replayは**両腕1,929更新・正確1,000,000教師**で、教師token列・順序・更新境界・学習率・sourceの実教師数が厳密一致した。変更した入力の長さとsampler bindingは別に記録する。

新たなデータはWSLの`/home/aihub_ubuntu/jmicro-data/phase7/chat-recovery-20261018/input-v3`。全2,048件のUser本文に対する独立oracle、全教師ID一致、役割順・最終Assistantのみのマスク・完全32token以内・履歴非切断を確認した。全256のQA代表例を直接確認し、共通の近況・相槌の同一文は辞書参照で読んだ。3群ではreverseラベルが本文を変えないため、256件を256種類の独立構造や自然会話とは数えない。値と変形の全要因が独立に釣り合う教材でもない。[QA記録](../reports/phase7/chat-recovery-20261018/input-v3-preparation/TRAIN_pattern_review.json)。

未確定教材のQA中に二つの問題を修正した。最初のrendererでは訂正群の場所に「です」が重複した。別v2で256行だけを修正し、次に単語転記の依頼を「後で」と明記したv3で256行だけを修正した。直前の通常相槌が即時の一語命令違反に見えないようにしたものである。各旧source・データ・receipt・QA表示を保全し、差分と全ての正答の不変を確認した。本学習前の教材QAであり、失敗した科学条件の再実行や品質基準変更ではない。

TRAIN manifest確定後に新DEV80問を著作し、実会話24組は6応答2組・3応答3組・2応答19組、計59応答とした。旧6suiteを保全し、最終生成は7suite×219×2＋公開100caseの両腕400＝3,466応答。NLLは旧320対象に新DEV80・変形TRAIN32を加えた432対象について本文とEOTを別集計する。公開100caseの今回最終比較も両腕GPU BF16/mathで生成し、先のCPU FP32診断とは区別する。

元Base/fresh Adam/native10,001,152/seed42/LR1e-4/更新512教師/最大32×1024/BF16/math、主点100万教師、推論greedy32を維持した新configをfreezeした。技術600秒・学習各7,200秒・評価10,800秒の有限枠と元品質条件を維持する。最大32×1024の元実機証拠を再利用し、新データ経路の保存再開・全状態一致と全32技術更新の計時を科学開始前に確認する。

CPUではread境界・split/重複拒否・中断済み出力の再開・failed条件再起動拒否などの12workflow checksが合格した。fixtureの結果であり、GPU・数値学習・日本語品質の合格ではない。現在の元Base7860と既存C1/C0のHTTPはidleで正しいcheckpointだった。GPU owner・実FLOCK等の確認は専用launcherが開始直前に行う。

新しい学習を終えた後も、全状態・全履歴・全出力・実生成履歴と実ブラウザーを確認してから、改善と悪化の両方を判定する。目標の完了と候補の品質採用は区別し、現在の候補の不採用や正式Baseの残課題は保持する。

## 実機検証と本学習（2026-10-18）

新しい実CUDA検証が合格した。両腕16更新ずつの全計時と、連続2更新対1更新＋保存再開＋1更新の全state/非時間履歴を保存し、両腕36項目が一致した。全40技術更新のstage wallは35.203221秒。固定の全計時による学習予測はC0=3,836.123125秒、C1=2,317.316727秒、評価予測=3,719.765984秒で、事前上限以内だった。[実機gate](../reports/phase7/chat-recovery-20261018/input-structure-main/native_gate.json)。最大shapeの元証拠の再利用と新データ経路の実検証を区別する。

同じ実WSL PID515188/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start89989737、Windows worker18640/17:05:30.2377944Zで両腕の新学習を進めている。17:14:44Zの実観測ではC0=850更新・440,801教師。現在の生存・全凍結source一致・実kernel FLOCKを確認した。NVMLのraw観測は保存し、世界全体の唯一GPU peerの証明とはしない。C1学習・最終評価はこの時点では未着手。

起動親でPowerShellのWorker switchとworker変数の大小文字衝突が発生した。子は既に起動していたため、実Windows commandline/開始時刻とWSLの同一実processを検証して欠けたlauncher記録だけ復元した。重複起動・凍結source修正はしていない。[復元記録](../reports/phase7/chat-recovery-20261018/launcher/launcher.json)。この欠陥は保全し、閉鎖後の別launcherで修理する。

C0の25万教師時点の全10応答を厳密な32token raw/実履歴と個別理由で確認した。内容成立は1/10（必要な五枚）で、日時の紐付け・二属性・訂正・厳密表記の失敗が残る。主点は100万のまま。[途中notes](../reports/phase7/chat-recovery-20261018/input-structure-main/diagnostics/C0/250000_notes.json)。

最終採点は旧rawを各々の元configで検証し、実messages/checks/ID/bytes/stop等が全て同一の応答だけ既存理由付きnotesを再利用する。異なる履歴や競合する採点は新たに全文確認する。実ブラウザーは新CPUポート7866/7867で各3会話×6応答、計36応答を確認する準備を済ませたが、未実施である。全3,466主応答・40途中・36実ブラウザー・全履歴/全state・最終採否が残っており、goalはACTIVE。

## 対照学習・実ブラウザー確認（17:25UTC）

C0は1,929更新・正確1,000,000教師で完了した。全1,929実履歴がCPU replayの教師量/microbatch/LRと一致し、119 Adam step・全typed state有限性・RNG・終端sampler・source配合も照合した。実step1,062.237380秒、stage1,106.619771秒。[監査](../reports/phase7/chat-recovery-20261018/input-structure-main/C0/training_audit.json)。元Base/fresh Adamから新しく学習した結果を、旧C1とCPUで比較するとmodel/Adam/scheduler/RNG/sampler/全非時間履歴が厳密一致した。保存済み全fieldで異なるのは新manifestのhashだけだった。ファイル全体のhashは異なり、旧checkpointのコピーではない。これは同seedの数値再現で、独立Base全pipelineや品質採用ではない。[数値比較](../reports/phase7/chat-recovery-20261018/input-structure-main/C0/historical_numeric_comparison.json)。

新対照CPU UI http://127.0.0.1:7867 を実起動し、専用のheadless実ブラウザーで3会話×6応答を実施した。全18の送信履歴1/3/5/7/9/11件、actual Assistant本文、会話reset、DOM/API同一、既定32と16/32/64選択を確認した。全18をstrict raw/実履歴と個別理由で確認し、内容成立1/18、自然停止17/18だった。訂正群では「時刻は午後三時です。」が6回続き、午後四時半への訂正を保持できなかった。画面の記録とCDP通信を保存し、PNGも直接確認した。[実ブラウザー原結果](../reports/phase7/chat-recovery-20261018/input-structure-main/practical/C0/browser.json) / [全理由](../reports/phase7/chat-recovery-20261018/input-structure-main/practical/C0/notes.json)。

同じ実科学processはC1の新学習へ進んだ。C1の完了・実会話18応答・全主3,466応答とCI/回帰・採否はこの時点では未完了で、goalはACTIVEのまま。

## 両腕学習・全36実ブラウザー・途中40の確認完了

C1も1,929更新・正確1,000,000教師で完了した。実step1,065.322642秒、stage1,125.322494秒。全履歴・119 Adam step・全state有限性・RNG・終端samplerを照合し、両腕の正答教師列・順序・LR・source実配合・EOT105,392は一致、実入力はC0=11,303,918/C1=15,008,894で別記した。[候補の学習監査](../reports/phase7/chat-recovery-20261018/input-structure-main/C1/training_audit.json)。全40途中応答も個別理由付きnotesを完了、25万/50万の内容はC0=1/2、C1=1/1各10であり、主100万へ差し替えない。

新候補CPU UI http://127.0.0.1:7866 を実起動し、同じ実ブラウザーの3×6応答を実行した。全履歴/reset/DOM=API/既定32/PNGを照合し、全18個別notesを完了した。内容成立はC0=1/18→C1=3/18、自然停止17→18/18。ただし本の題名を麦茶と取り違え、訂正の初め5応答では古い午後三時が固定され、最後も新聞で確認するという未提示の行動へ移った。会話全体の安定性の改善や正式採用ではない。[候補の全18理由](../reports/phase7/chat-recovery-20261018/input-structure-main/practical/C1/notes.json)。この実会話はCPU FP32で、本比較のGPU BF16/mathと合算しない。

C0/newの全219は内容19/80・最終文脈7/24。C0/curriculum・previous_new・lrの全657は、旧rawを元configで厳密に検証した同一実履歴/ID/bytes等の理由付きnotesで全件照合した。計876/3,466の主内容確認が完了した時点で、C0の残3suite・公開100と全C1主評価は未完了。元同実科学processは全rawを生成中で、元Base UI復帰と終端の実確認もまだ必要。goalはACTIVE、採否は未確定。
