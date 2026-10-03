# Phase 6④⑤: 生成・変換と本学習設定の確定

開始: 2026-10-03。ユーザーの「2まで計画を立てて進めてください」は、直前の計画の1.生成・変換確認、2.本学習設定確定を実行する指定。Phase 6④⑤を進め、検証・commit後に停止する。500M以上のBase scaling、Chat学習、学習後の量子化品質・公開は開始しない。

## 固定した比較と完了条件

1. Phase 5採用NoNorm checkpointのSHA、公開T4K Tokenizer、固定Base dev 80 promptとprotocolをbindする。連続forwardと1-token/chunk cache、EOS=3停止を確認。greedy/抑制なし/sampling seeds42/43/44の400生成でEOS・反復・Unicodeの生成IDと原因を残す。必要な修正は最大2案、同じcheckpoint/prompt/seed/長さで対照する。強制停止hookはcontroller検証に限り、品質改善に数えない。
2. NoNormのHF/Llamaとnative float GGUF adapterを実装する。HFはhalf-split RoPE、GGUF LlamaはQ/K rowを公式変換と同じ順序へ変える。固定protocolのFP32 logits許容誤差、短系列/1024・prefill/cache・tied embedding・Tokenizer外部ID・本物の出力からのEOS停止を確認。既存Norm/Qwen3経路とPhase 0〜3 reportは保持する。
3. 新dev89,416文書・164,344,743 body bytesを全文採点し、新corpusのBPB基準と実時間を記録する。batch評価を追加する場合は既存scalarの全本文採点・EOS分離・padding/position契約との一致を検証する。testはモデル選定へ使わない。
4. ③のFlash＋compile reduce-overhead / batch32・context1024・32,768 input tokens/updateを長期候補とする。LRは0.001/0.002/0.003の一要因3候補に限定し、各2,000更新（65,536,000 input tokens）・同じseed/data/sample、warmup200、WSD stableを比較する。dev固定256文書のcommon-byte BPBと有限loss/gradient/optimizer、末尾lossを比較。各100追加decay更新を別runへ分けて評価し、親の不変性を確認。発散・非有限は停止し失敗保持。採用はdecay dev BPBが最良の安定候補、既知の品質未達は維持する。追加sweepは行わない。
5. 変更後sourceでstable400 vs200+200・decay100 vs50+50の全state・履歴完全一致、親不変性・元継続、採用設定のcold-cache再開200→400を新runで確認する。warmup200を越えるstable予算を使う。③の旧sourceチェックを新sourceの再開証拠へ流用しない。
6. 採用LR・batch・model/Tokenizer/data/source hash、warmup・WSD終端/枝予算・seed・保存/評価間隔・保持数・容量上限・起動/再開CLIとGPU排他/PID/boot/start ticks/log/heartbeatを固定する。stableは10Bのglobal更新数で凍結し、500M等の観測点はstop-afterで区切る。純学習・保存/全文評価/生成/decay枝/compileを別計上し、本学習は起動しない。

## 保存する証拠

全文評価の前に固定dev先頭32文書でscalarとbatchのBPB差が0.001以下であることを確認する。この許容値は実測前に固定する。両経路のCEはFP32へ変換してから加算し、過去のBF16加算reportは上書きせず、新しい評価基準として明示する。CPUで本文/EOSの全件採点・padding・状態不変性も検証する。

`reports/phase6/generation_diagnostics.json`、`nonorm_export_parity_report.json`、`readiness_stability_report.json`、`base_launch_plan.json`と`configs/phase6/base_frozen.json`、最終監査・status・採否を保存する。raw logs/checkpoints/export/source snapshotsはLinux `reports/phase6/readiness-20261003/`へ保持。長いGPU処理は永続supervisorとcheckpointで復旧する。各起動前に既存jobと実GPU compute一覧を確認し、重複起動しない。

Python3.12.7の全実行はuv run --frozen。依存変更が必要ならuv add、復元はuv sync --frozen。HF/GGUF変換の一次資料は固定[llama.cpp Llama converter](https://github.com/ggml-org/llama.cpp/blob/46ca246de9bb1c35269722a6240d37d9dfd79cad/conversion/llama.py)とローカル固定Transformersを照合する。③実測の69.5万tokens/sは見積もりの起点で、④⑤の実装・検証時間の保証ではない。
