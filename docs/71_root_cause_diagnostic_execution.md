# 根本原因診断の実行契約

2026-10-05 JST。ユーザーの「3まで進めてください」は説明した三項目（実装整合性、EOS/反復の発生点、教材適合性）を指す。計画70内部の段階0〜2に対応する。自然文記憶の追加学習（内部段階3）は含めない。

元10B、既存coherent20物語枝、混合shuffle候補の三重みを固定する。128全文は既存train streamのランダムtoken位置から文書境界まで復元する。Web/200M物語各64、長さ層別各16を優先し、その長さがないpoolの余枠は別長さで補う。token位置抽出は文書一様抽出ではなく長い文書/周辺に偏る。source内のWeb bucketは全indexを走査せず未分離。全corpus監査を再実行しない。

短いWeb8、物語8、既存compactの反転ペア16をtrainから固定、teacher文末EOSと自由生成を比較する。goldに一致しない最初のtokenは意味破綻と同一視しない。正解本文/自由生成のEOS確率・順位・entropy・top5・選択確率、4gram反復開始を保存し、原文を読む。原dev80の新再評価は行わず、過去greedy/samplingの実例・率は再利用する。ここでの三重み×32入力×四生成法は既存dev出力と異なる、teacherとの対に必要な診断。greedyとtemperature0.8/top-p0.9/seeds42/43/44、最大64を保持。延長128は今回予定せず、旧512の失敗証拠を再利用する。

元実重みで全32教師列、PAD/BOS masking、CUDA FP32 math、BF16 math、64/1024実streamのfull/cache/fast/独立HF、BF16 Flash/compiled Flash、代表三parameter gradientを測る。既存protocol FP32 atol1e-5/rtol1e-4、BF16 atol0.05/rtol0.02、FP32 CE atol1e-6/rtol1e-5、math full/fast gradient atol1e-7/rtol1e-6を結果前に固定する。BF16 gradientはfinite必須、norm/cosineを報告し新しい合格閾値は作らない。許容外は失敗として記録し、誤差規模・影響を診断する。既存CPU/save-resume/GGUF全検証を繰り返さない。optimizer stepは0、checkpointを変更しない。

GPU job占有上限600秒（compile含む）、新学習0。境界毎に残時間を確認し、超過でpartialを保存し停止、自動延長しない。UIを実identity照合で一時停止、単一GPU lockとjob PID/boot/start/logを保存、終了/失敗の双方で元UIへ復帰する。準備/原文確認/報告時間は占有予算とは別。

実行前 `reports/phase6/root-cause-20261005/contract.json` にcheckpoint/manifest/tokenizer/script/core/cases/corpus SHAを凍結する。可搬コピーは `reports/phase6/root_cause_*`。新しいdiagnostic helperを意味あるCPU testsで確認する。終了成果は経路不整合の有無、主原因候補順位と確率付き実例、未分離の原因、最小修正案、次二条件と不変の採用基準。報告・local commit・元UI復帰で停止。品質問題の解決や全プロジェクト完了を宣言しない。
