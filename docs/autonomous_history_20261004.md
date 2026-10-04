# 2026年10月4日までの計画と進捗記録

この文書は現行文書を整理する前の記録を保存した履歴です。古い停止境界・実行中のPID・起動案は現在の指示ではありません。現在の状態は [autonomous_status.md](autonomous_status.md)、計画は [39_learning_scale_and_generation_plan.md](39_learning_scale_and_generation_plan.md) を参照してください。以下の本文はUTF8 LFで保存した元文書全体で、コードブロック内の相対リンクとコマンドは当時の表記です。

## README.md

UTF8 LF SHA256: 38b6332f09c5c295b3309085aeff2eeded6b40a3af7f1fb5410f93532a1c6233

`````markdown
# JMicro-10M

2026-10-04完了: [実train12.23Bのローカル整備](reports/phase6/corpus_10b_ready_review.json)と[新データでの2B学習・既存評価](reports/phase6/base_2b_10b_data_review.json)を終えて停止した。モデルは約10M、減衰込み総2,000,027,648学習tokens、全体約63分。同じdev BPB1.022491→0.982882、greedy反復66/80→60/80、EOS0/80の課題は残る。5B/10B/Chatは未開始。以下の開始時・旧500M記録は履歴。[現在の実状態](docs/autonomous_status.md)。

2026-10-04: [ローカル学習データを実train12.23B tokens整備](reports/phase6/corpus_10b_ready_review.json)。ユーザー指示で過剰な独立再照合を省き、構築時の全件確認と実loader合格を採用（独立全件auditは未完了と明記）。新データでユーザー指定の2B学習をWSL＋RTX4090で開始した。モデルは約10Mパラメータのまま。減衰込み2Bと既存dev/生成評価を終えて停止する。[現在の実状態](docs/autonomous_status.md)。

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新結果](reports/phase6/base_500m_review.json)。

日本語の短文生成と数ターンの雑談を目的に、約10Mの言語モデルをTokenizerからスクラッチ構築する。計画は[フェーズ別実行計画](docs/15_project_roadmap.md)、設計・調査一覧は[docs](docs/README.md)を参照。

Phase 0〜5が完了。データpilot、4k/8k Tokenizer、約10Mモデル、cache、HF/実float GGUFをiMacで検証し、WSL＋RTX 4090で学習器・保存再開・最大安定batch・評価を実測した。[Tokenizer完了記録](docs/18_phase2_completion.md)、[モデル・export完了記録](docs/19_phase3_completion.md)、[Phase 4完了記録](docs/21_phase4_completion.md)を参照する。Phase 4は小さいGPU検証runで、Base/Chatの本学習と能力目標は未達。Phase 5の候補選定と独立監査も終了し、Phase 6①〜⑤と500M学習・評価が完了し、1B前で停止中。

**別PCで続きを進める場合は[Windows/WSL＋RTX 4090の再開手順](docs/windows_handoff.md)から始める。** 固定成果物の復元、uv環境・CUDA確認、実装済みCLIと引継ぎ条件をまとめている。Phase 5・Phase 6①〜⑤と文書更新のコミットはローカル保存で、GitHubへpushしていない。新規cloneだけで最新コードが揃うとは限らない。

環境整備・学習・評価・改善をCodexへ継続して任せる場合は[自律実行の設定とrunner](docs/codex_automation.md)を参照する。次の担当の現在地は[継続作業の状態](docs/autonomous_status.md)、作業ルールは[AGENTS.md](AGENTS.md)。2026-10-03にFull accessが反映され、WSL・公開成果物復元・CUDA/BF16確認を通過した。

## 開発環境

TokenizerとpilotデータのHugging Face共有については[公開状態と取得手順](docs/huggingface_handoff.md)を参照する。[ライセンス・個人情報確認](docs/20_publication_review.md)を終え、出所・利用条件を付けた公開版の匿名取得・checksum検証が完了した。

Pythonと依存は`uv`で管理する。Pythonの実行は環境確認・自律runner・テスト・一時スクリプトも含め、必要なextraを付けた`uv run --frozen ...`に統一する。systemの`python`・`python3`・`py`を直接実行しない。`.python-version`は今回確認したPython 3.12.7、解決した依存versionと配布file hashは`uv.lock`へ固定。Python導入は`uv python install 3.12.7`、依存復元は`uv sync --frozen`、依存変更は`uv add`を使う。

```sh
uv sync --frozen --extra data --extra ml --extra export
uv run --frozen --extra data scripts/validate_phase0.py --output reports/local/phase0_validation.json
uv run --frozen --extra data --extra ml --extra export pytest -q
uv run --frozen --extra data scripts/experiment.py capture-environment --output reports/local/environment.json
uv run --frozen --extra data scripts/experiment.py prepare-run --name development
```

最後のcommandが表示するrunディレクトリを指定して検証する。

```sh
uv run --frozen --extra data scripts/experiment.py verify-run reports/<run_id>
```

新しい依存は用途に応じて追加する。

```sh
uv add <package>
uv add --dev <test-package>
uv add --optional data <data-package>
uv add --optional ml <ml-package>
```

`data` extraにはPyArrow、datasketch、fsspec、aiohttpを登録済み。Phase 1のデータ処理では`uv sync --frozen --extra data`と`uv run --frozen --extra data ...`を使う。

`ml` extraにはNumPy、SentencePiece、protobuf、PyTorch、Transformers、datasets、safetensorsを登録済み。GGUF作成・検査には`export` extraも使う。WSLではPython 3.12.7、PyTorch 2.14.1 / CUDA 13.0、Windows driver 616.92でCUDA/BF16を検証済み。環境を保持する通常のWSL実行では`--extra hub --extra data --extra ml --extra export`を付ける。

## 配置

| ディレクトリ | 内容 |
|---|---|
| `src/jmicro/` | 環境・データ・Tokenizer・モデル・shards・学習・評価・export・推論 |
| `configs/` | source台帳・pilot、T4K/T8K、学習候補、Tokenizer、評価、iMac/WSL設定 |
| `schemas/` | データrecord・準備run・学習run・設定・評価例のJSON Schema |
| `scripts/` | `uv run --frozen`で実行する入口 |
| `tests/` | 日本語dedup・split・話者対応・取得上限、BPB、前処理、snapshot検証 |
| `eval/` | Base/Chat各100件、dev/test manifest、採点・golden例 |
| `data/` | pilot・manifest用。拡張corpus/raw/shardsはWSL外部領域・Git管理外 |
| `reports/` | Phase 0〜5の履歴、Phase 6①〜⑤のデータ・GPU・評価・変換・設定監査、文書更新の検証 |
| `docs/` | 設計、技術調査、評価仕様、移行手順 |

評価方法は[evaluation_protocol.md](docs/evaluation_protocol.md)、環境切替は[windows_handoff.md](docs/windows_handoff.md)、Phase 0の結果は[完了記録](docs/16_phase0_completion.md)を参照。

データpilotの取得・再生成・検証は[dataの手順](data/README.md)を参照する。過去のPhase 0記録を上書きせず、現在の開発検証は`reports/local/`へ保存する。

## Tokenizer・モデル・ローカル推論

再実行と各backendの起動は[Phase 3完了記録](docs/19_phase3_completion.md#再現と推論入口)を参照する。GGUF内蔵TokenizerはID契約が一致しないため、正式な入口は外部SentencePiece wrapperを使う`uv run --frozen --extra ml --extra export scripts/infer.py`。モデルとTokenizerのhashを照合する。学習済みNoNormの変換は[④⑤の検証記録](docs/30_phase6_readiness_execution.md)を参照。CPU精度profileの全12比較は成功し、成果物metadataに従って専用runtimeを使用する。未修正stock FP32での失敗と品質未達は保持する。

## 次に進めること

①②の実量・GPU検証は[準備完了記録](docs/26_phase6_preparation_completion.md)、③の採用速度・容量・再開は[高速化完了記録](docs/29_phase6_performance_completion.md)を参照する。Flash＋compile reduce-overhead / batch 32で694,521 tokens/s、最速reference比5.436倍を検証した。④⑤も`93c7d1d`で完了し、batch32・LR0.002・WSD global305,176更新と保存/復旧/容量をversion2へ凍結した。現在は500M評価後で停止している。再開後の1B→2B→5B→10Bは[残りの計画](docs/27_phase6_remaining_plan.md)、段階評価は[Phase 6計画](docs/24_phase6_plan.md)に整理した。

Phase 5の100件overfit → 10M smoke → 100M比較・候補選定が完了し、Phase 6①〜⑤と500M学習・評価が完了し、1B前で停止中。[完了記録](docs/23_phase5_completion.md)を参照する。Tokenizer再学習・成果物再取得・完了済みPhase 4測定を繰り返す必要はない。[実測と制約](docs/21_phase4_completion.md)、[次の作業](docs/10_next_steps.md)を参照する。

Git管理対象はコード・設定・docs・小さな検証report。本文・Tokenizer・checkpointは管理外なので固定Hub成果物とLinux保存先を引き継ぐ。Phase 4は全64 tests、Phase 5は全68 tests、Phase 6①②は全74 tests（すべてskip 0）と73 GPU checksを確認した。最新の④⑤は全90 tests / skip・error・failure 0、学習済み変換12比較、独立CLI/重み149 checks、GPU準備106 checks、総合37 checksが成功した。[証拠](reports/phase6/readiness_gate_audit.json)。これらは各段階の実装・準備検証で、Base/Chat品質合格ではない。新規cloneにはartifactと必要なLinux成果物を別途復元する。

学習入口は`scripts/train.py`の`build-shards` / `train` / `evaluate`。`train`はCLI引数から設定を作り、`configs/training/baseline.json`を自動読込しない。AdamW＋warmup/cosine・WSD stable/decayは実装済み、Muon・Chat trainerは未実装。[利用例と保存再開](docs/windows_handoff.md#6-実装済みcliと次回の再開)を参照する。
`````

## AGENTS.md

UTF8 LF SHA256: ecaa662692070c2053b2ca4b7ac206b8ab32b54cfab6ca063fcbafda1c7679a8

`````markdown
# JMicro-10M development and training

- Latest completed scope (2026-10-04): requested chat step1 direct10B preparation is complete; docs/40_base_10b_preparation.md, reports/phase6/base_10b_preparation_review.json and completion audit prove it. Frozen configs/phase6/base_10b.json/schema/runner ready;14 targeted CPU tests and actual WSL4090 BF16/Flash16-update524288-token stable/decay save-resume gate pass all state/history. CPU saved evidence26 checks pass. GPU19.217sec/600; actual Linux459/Windows29620 exited, GPU idle; science inputtokens0 and no science output directories. Old stable/final5B/Web5.1B/short5.1B weights and core are unchanged. Shell default is verify-only; future science command bash scripts/run_base_10b.sh --train. Report/local commit and stop before scientific10B training/evaluation/EOS/UTF8/Chat/20B. Older active/live/not-ready notes below are history.

- Active authorization (2026-10-04): user explicitly requested step1 of the latest chat plan, preparation of direct10B execution settings. Implement/freeze configs/phase6/base_10b.json and run_base_10b.py/.sh; reuse saved4.75B stable, existing12.23B and unchanged training core. Execute targeted CPU checks and actualCUDA16-update/524288-token stable/decay exact save-resume verification only. Default shell mode is --verify-only; scientific10B training requires explicit --train and is outside this request. Persist verification process/locks/logs/checkpoints, review saved evidence, report/local commit and stop. No science train/evaluation/EOS/decoder/Chat/20B jobs now. Older planning and complete notes below are history.

- Latest scope (2026-10-04, plan revision): user prefers going directly to10B instead of intermediate7.5B. docs/39_learning_scale_and_generation_plan.md now proposes one explicit fork from saved4.75B stable to9.5B stable plus final0.5B decay, total10000007168 input tokens; new scientific5249990656 tokens. Use existing12225819077 train tokens, no new acquisition. Skip7.5B decay/full evaluation. Evaluate10B once against saved5B and5.1B Web with original raw gates; downstream EOS pair conditional on10B improvement, UTF8 policy separately labeled. This turn updates the plan only; no GPU job started, new execution config/schema/commands not ready. Report/local commit and stop. Earlier staged7.5B scopes below are superseded history.

- Latest scope (2026-10-04, planning only): user requested a next plan from completed results. docs/39_learning_scale_and_generation_plan.md proposes existing12.23B Web training to7.5B, then10B only after measured BPB improvement and original growth safety gates; one final-parent lowLR Web/short20 pair and one separately labeled UTF8 constrained decoder comparison. Preserve original raw-policy quality failures; constrained output never repairs learned raw gates. No new GPU training/inference or decoder implementation authorized by this planning turn. New run/config/schema/commands are not ready. Record plan/local commit and stop; do not restart finished launchers, acquire more corpus or start20B/50B/Chat/UL/sweeps. Earlier scopes below are history.

- Latest completed scope (2026-10-04): authorized EOS/UTF8 steps1-3 complete; see docs/38_eos_5b_finish_results.md and reports/phase6/eos_5b_finish_review.json. Production cap-tail display helper verified, each final5B fork trained100007936 tokens with separate262144 CUDA verification tokens; full BPB Web0.958091981/short0.959010736, fixed EOS0/13 and repetition57/51. Full400 short Unicode2 (one interior invalid, one cap tail) makes original full adoption/growth gate fail despite EOS129/400. Keep raw failures, old weights and new diagnostic checkpoints. GPU2253.853sec/3000, actual Linux464/Windows21524 exited, GPU idle. Quality targets not achieved; stop after final report/local commit. Do not restart finished runner or start10B/Chat/UL/decoder sweeps. Older authorization/live/planning notes below are history.

- Active authorization (2026-10-04): user explicitly requested steps1-3 through completion. Goal: implement/verify UTF8 cap-tail display handling, execute one final5B-parent equal lowLR Web/short20 pair100M each and eligible full evaluation/content review/report/commit. Use configs/phase6/eos_5b_finish_100m.json and bash scripts/run_eos_5b_finish.sh, GPU cumulative3000seconds. Preserve original raw EOS/repetition/Unicode and adoption/growth/quality gates; display repair is not learned stopping. Reuse accepted21M short pool/aux80 and saved5B full/fixed evidence, no old GPU evaluations or full corpus audit. Record8-update/262144-token CUDA resume gate separately from200015872 scientific tokens. Persist actual job identity/checkpoints/locks. Finish all authorized steps and stop before10B/Chat/UL/decoder sweeps. Older planning-only/complete/live notes below are history.

- Latest scope (2026-10-04, research/planning only): user requested investigation and plan for EOS/repetition/UTF8 improvement. docs/37_eos_repetition_utf8_improvement_plan.md and reports/phase6/eos_5b_improvement_plan.json propose CPU display buffering, then one matching lowLR0.0002 Web/short20 pair100M each from final5B, original raw metrics/gates and eligible full evaluation. Saved-evidence CPU research confirms398/400 valid outputs unchanged,2 identical cap-truncated tails buffered and9 boundary/error probes pass; saved true-ending EOS NLL5B2.223077 vs2B2.302868. Existing accepted445501-unit/21M pool is available. GPU inference/training0; production decoder/weights unchanged. Implementation/config/runner for this new5B finishing fork are not ready or started. Report/commit planning and stop; do not execute this proposal,10B/Chat/unlikelihood/decoder sweeps automatically. Older completed/active/stop notes below are history.

- Latest completed scope (2026-10-04): requested5B comparison is complete in reports/phase6/base_5b_comparison_review.json and docs/36_base_5b_comparison.md. Same89416 protected dev/common164344743 bodybytes and400 generation keys; references reused, new training0. BPB5B0.964484 improves original2B0.982882 and lowLRWeb0.972969, but fixed EOS0/80 and repetition59/80 vs60/55. Unicode1/80 and2/400 are the same base-070 greedy output under both suppression settings, truncated UTF8 at64-token cap; preserve these failures and original gates. Growth gate fails, usefulBase/Chat quality unachieved. All80 new fixed continuations reviewed with13 aligned qualitative examples, no blind human/test score. CPU saved-evidence checks pass, GPU788.433seconds within1800seconds, actual Linux477/Windows26484 exited and GPU compute list empty. Preserve all weights/results; report/commit and stop before10B/Chat/mixture/decoder sweeps. Do not rerun completed training/evaluation. Older active/stop/live notes below are history.

- Active authorization (2026-10-04): user requested the5B comparison. Freeze configs/phase6/base_5b_comparison.json, run bash scripts/compare_base_5b.sh on saved final5B weights, reuse completed2B/lowLRWeb/short20-reference evaluations, and score exactly the same89416 protected dev documents and400 fixed generations. No training or heldout mixing; original metrics/quality criteria preserved. GPU cumulative1800seconds; persist full-dev before generation, process identity/locks/logs/bindings. Review aligned content, report/commit and stop before10B/Chat/mixture/decoder sweeps. Older completed/stop/live notes below are history.

- Latest completed scope (2026-10-04): requested next-plan steps1,2 are verified in reports/phase6/base_5b_review.json and base_5b_completion_audit.json. Explicit stable-budget extension preserves the1.9B parent and all state; CPU6tests and actualCUDA16update/524,288-token stable/decay save-resume gates pass. Web100percent training reached global152,588/5,000,003,584 tokens, adding3,099,983,872 science tokens including7,629-update decay. All scientific updates contiguous/finite, final LR0.0002, original parent hash unchanged, all97 science checkpoints retained, GPU4543.110seconds within7200seconds. actual Linux450 and Windows28760 exited; GPU compute processes empty. Source/settings and earlier artifacts preserved. User explicitly requested current-code push; origin/main was verified at c68ff34. Finish completion report/commit and stop; do not rerun completed training, evaluate, start10B/Chat or sweep.5B quality remains unevaluated. Older active/live/stop notes below are history.

- Active authorization (2026-10-04): user requested next-plan steps1,2: implement/freeze explicit stable-budget extension, verify save/resume and train Web100percent to total5,000,003,584 input tokens. Use configs/phase6/base_5b.json and bash scripts/run_base_5b.sh; actual job identity/latest checkpoint are authoritative. Immutable stable1.9B parent, stableLR0.002 unchanged,7,629-update decay to0.0002; additional3,099,983,872 science tokens and separate524,288 verification tokens. GPU budget7,200seconds. Preserve earlier artifacts, WSL/uv/4090/existing data. Report/commit and stop after training, before step3 full evaluation,10B/Chat/sweeps. Older stop/completion/live notes below are history.

- Latest completed scope (2026-10-04): requested steps1,2,3 are verified in reports/phase6/eos_low_lr_100m_review.json. Three saved high-LR checkpoints show dev256 regression already by6.55M additional tokens. New matching peakLR0.0002 Web/short20 arms each100,007,936 tokens improve full BPB to0.972969/0.974799 vs original2B0.982882. Fixed EOS0→27/80, repetition55→41;400-generation empty/role/Unicode all0 in both. Original automatic mixture/full/growth gates pass; semantic repetition/context errors still prevent usefulBase/Chat adoption. Preserve original2B and all diagnostic branches. Scientific200,015,872 tokens plus separate262,144 actualCUDA resume verification;12 targeted tests pass. GPU2141.290seconds within2700second budget, actual Linux498/Windows27984 exited and GPU compute processes empty. Finish report/commit and stop; do not start5B/Chat/sweeps or rerun completed evaluation. Older active/live/stop notes below are history.

- Active authorization (2026-10-04): user requested execution of steps1,2,3: analyse existing high-LR logs/three saved checkpoint dev256 probes, run one matching Web/short20 pair of100M each with peakLR0.0002, and complete eligible full evaluation/content review/report/commit. Frozen plan configs/phase6/eos_low_lr_100m.json; run reports/phase6/eos-low-lr-100m-20261004; restart bash scripts/run_eos_low_lr.sh. Reuse the accepted complete-unit pool and frozen auxiliary dev; preserve old code/checkpoints. GPU2700seconds cumulative, scientific200,015,872 tokens plus separate262,144 resume verification. Keep original mixture/growth/quality criteria. Stop after1–3, before5B/Chat/sweeps. Older completed/stop notes below are history.

- Latest completed scope (2026-10-04): the authorized complete-unit paired100M comparison and eligible full evaluation are verified in reports/phase6/eos_complete_100m_review.json. Fixed EOS0/80→24/80, auxiliary0/80→42/80; fixed repetition50→49. Full dev BPB Web1.016473 / short1.017580; automatic mixture gates pass but semantic errors/repetition remain, so diagnostic weights are preserved and the original2B baseline is retained. Both full BPBs regress from original2B0.982882. No Base/Chat quality achievement or5B eligibility is claimed. Scientific200,015,872 input tokens plus separate262,144 verification;24 targeted tests pass. Original main remains interrupted, recovery complete and actual GPU/launcher processes exited; cumulative GPU3305.199seconds exceeds original2700second plan and is explicitly recorded. Do not restart completed jobs or start5B/Chat/sweeps. Finish report/commit and stop. Older active/planning/live notes below are history.

- Active authorization (2026-10-04): the user requested planning and execution of the next proposal. Implement and run one paired 100M Web/short20 comparison using complete 32–64-token train units and a frozen auxiliary dev suite, as specified in docs/27_phase6_remaining_plan.md and reports/phase6/eos_next_plan.json. Preserve the original fixed suite and adoption gates, separate verification compute, persist jobs/checkpoints, report and commit. Stop after this comparison and eligible full evaluations; 5B/Chat and automatic sweeps are outside this execution milestone. Older planning-only notes below are history.

- Latest scope (2026-10-04, planning only): the user requested the next plan based on the completed investigations. The proposal is docs/27_phase6_remaining_plan.md and reports/phase6/eos_next_plan.json: complete32-64-token train units, one paired100M Web/short20 comparison with unchanged fixed metrics plus auxiliary dev diagnostics, then a separately reviewed Web-only5B stable extension and roadmap Base/Chat milestones. Mixture adoption gates and original quality criteria stay intact. Builder/auxiliary suite/100M runner/reviewer and5B stable-extension are not implemented yet. No data/inference/training job is authorized by this planning-only turn; finish plan/report/commit. Older completed/proposal/live notes below are history.

- Latest completed scope (2026-10-04, EOS pilot): the requested two25M arms and fixed80 greedy/256-dev comparison are complete; see reports/phase6/eos_short_pilot_review.json and configs/phase6/eos_short_pilot.json. EOS remains0/80 in both; repetition62→54/80, BPB1.068518→1.069161 (+0.06025percent). EOS gain gate failed, so short20 is not adopted and conditional full dev/400 generation is skipped. Scientific50,003,968 input tokens, verification524,288 separately,337.027 cumulative GPU seconds. Both completed checkpoints and the unchanged2B parent are preserved; GPU processes exited. Report/commit and stop before5B/Chat/new sweeps. The proposed32-64-token complete-unit comparison is not started. Do not rerun completed training, verification or evaluation. Older authorization/proposal/live notes below are history.

- Latest result/authorization (2026-10-04, EOS investigation): the requested new2B diagnosis is complete in298.556 seconds, training updates0; see reports/phase6/eos_2b_review.json. Same256 true endings improve EOS argmax35→46;20-case raw greedy still stops0/20 by512, penalty1.1 stops5/20 only after long repetition. EOS supervision/controller work; EOS remains outranked on free-generation trajectories. Fixed64 evaluation and training artifacts remain unchanged. Do not rerun the completed diagnosis or full audits. The next short-complete-document25M-per-arm training comparison is a proposal requiring its own implemented/frozen experiment forks and budget before execution;5B scaling follows its EOS improvement review. Preserve original quality criteria. Older stop/live notes below are history.

- Current result/stop boundary (2026-10-04): local12.23B train-token preparation and the separately authorized new-data2B training/evaluation are complete. See reports/phase6/corpus_10b_ready_review.json and reports/phase6/base_2b_10b_data_review.json. Final checkpoint contains2,000,027,648 input tokens including decay. Existing dev BPB1.022491→0.982882, greedy repetition66/80→60/80, greedy EOS still0/80; quality targets remain unachieved. Stop after report/commit. Do not rerun completed validation/evaluation or start5B/10B/Chat/decoder experiments without a new user request. Older authorization and live-job notes below are history.

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. The roadmap defines milestones and evidence; the status file records the actual current state.

The user has authorized Codex to implement, run, evaluate, repair, and improve this project autonomously, including local GPU training and the required WSL environment preparation. Continue through routine implementation decisions and milestone transitions without asking for renewed permission. Respect the active tool permissions: authorization in this file cannot change the execution sandbox or managed policy.

- Target WSL package 3.x with a Linux distribution using WSL 2 and RTX 4090. Use Python 3.12.7 and uv; dependency changes use `uv add`. Preserve historical Phase 0–3 reports.
- Run all Python commands through uv, including setup probes, automation runners, tests, and one-off scripts: use `uv run --frozen ...` with the required extras. Install Python with `uv python install 3.12.7` and restore dependencies with `uv sync --frozen`. Do not invoke system `python`, `python3`, or `py` directly or install dependencies with pip. Python subprocesses may reuse `sys.executable` when the parent was launched through uv. If the pinned interpreter or dependencies are inaccessible, record the blocker instead of falling back to system Python.
- Recover the pinned public pilot/Tokenizer and verify hashes before use. Do not repeat Tokenizer training or Phase 3 export work unless new evidence requires it.
- Follow Phase 4 environment → shards/trainer/evaluation → save/resume → maximum stable batch. Then overfit/smoke/100M comparisons → Base → Chat → quantization/local validation. Follow the roadmap's measured-budget and improvement conditions for 20B/50B; additional research must have a defined comparison and completion condition.
- Implement missing training and evaluation commands before trying to run them. Proposed settings and random-weight CPU checks are not evidence of GPU training or useful model quality.
- Use train records for learning; keep dev/test and the fixed evaluation suites separate. Compare Tokenizers with common-byte BPB and clearly labeled token/byte/GPU-time budgets. Chat loss supervises Assistant body plus EOT.
- Save optimizer/scheduler/RNG/sampler position and consumed tokens at completed updates. Verify continuous vs resumed training before long runs. Use measured stable batch sizes and finite CUDA/BF16 forward/backward results.
- Persist long GPU jobs, logs, checkpoint paths, and process identity so a conversation ending does not lose training. Before starting a job, inspect existing processes and run records to avoid duplicate GPU jobs. Resume valid checkpoints after interruption.
- After each meaningful change or experiment, run relevant checks, fix failures, and update `docs/autonomous_status.md` with evidence, decisions, active jobs, and the next concrete action. Do not weaken acceptance criteria merely to pass a failed run.
- Stop for genuinely missing credentials, OS elevation/restart, inaccessible hardware, or exhausted account/runtime capacity, and record the exact blocker and restart command. Do not turn a transient error into repeated identical retries.
- Work on this project and its documented WSL/data environments. External publication, messages to other people, and paid cloud jobs need their own authorization. Do not expose authentication files or secrets in logs.
- Use repository-local Git identity `yousan <ka1357amnbpdr@gmail.com>`. Commit verified, meaningful changes at appropriate milestones; do not automatically push or publish.
- Latest authorization (2026-10-04): the user requested less redundant validation and faster progress to learning, and explicitly selected2B training. Stop the extra full independent corpus audit; preserve its partial evidence and user-requested cancellation rather than labeling it passed. Local10B preparation is accepted using completed builder checks, existing full raw reconstruction, and the actual unchanged train loader. See `reports/phase6/corpus_10b_ready_review.json`. Run the separately frozen `configs/phase6/base_2b_10b_data.json` on the new data, using the existing model/settings and fresh seed42. Its total budget is2,000,027,648 input tokens including final5percent decay (batch rounding). Preserve all old runs, use the existing protected dev/fixed generation evaluation, report/commit, and stop after2B. Do not start5B/10B, decoder/mixture comparisons or Chat. This supersedes the older preparation-only stop boundary below. Skip extra benchmarks and repeated all-file audits; retain necessary loader/checkpoint integrity and measured finite training checks.
- Current stop boundary (2026-10-03): The 500M milestone (`6cdd6b7`) and the authorized read-only repetition/EOS/data investigation are complete. See `reports/phase6/repetition_diagnosis_review.json` and `.md`: EOS is supervised, true ending prediction improves, repetition is already high at131M, decay reduces aggregate repeats, and data-length/sample-repetition increases are not observed. Causal training factors and precision effects remain unresolved. Stop after report/commit; do not start the proposed decoder/mixture experiments, replace data, train or extend to1B until the user resumes work.
- Active authorization (2026-10-03): prepare approximately10B training tokens locally for future use. Execute acquisition/build/full audit through uv in the WSL Linux filesystem using `configs/phase6/corpus_10b.json` and `docs/32_local_10b_corpus.md`. The earlier2B/5B plan is superseded by this10B dataset objective. Preserve old shards, all current heldout/evaluation data and historical evidence. Inspect the acquisition/preparation PID, boot ID and start ticks before any restart; valid checkpoints must be reused. Report/commit and stop before model training. Decoder/mixture experiments remain deferred. Model size remains10,001,152parameters; prepared dataset size and cumulative training tokens are separate quantities. Monitor host/WSL free capacity and expand the WSL disk if actually needed; keep bulk data and processing on the Linux filesystem.

For the non-interactive runner, return the requested JSON result. `continue` means useful authorized work remains; `needs_user` means an external action is necessary; `complete` requires actual evidence that the requested roadmap goals have been met. A completed code change alone is not project completion.
`````

## docs/README.md

UTF8 LF SHA256: 64c8bb286b85c71b5a96fa9250e11653933566f6b437fbc9bb903b59a43d6aad

`````markdown
# JMicro-10M 設計・調査ノート

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新結果](../reports/phase6/base_500m_review.json)。

このディレクトリは、日本語専用の約10Mパラメータ級Decoder-only Language Model `JMicro-10M` を、Tokenizerを含めてスクラッチ構築するための設計・調査記録である。

## 文書内のラベル

- **確定**: 会話でプロジェクト方針として合意した内容。
- **確認済み**: 添付config、本人の過去成果、または一次資料から確認した事実。
- **提案**: 現時点の推奨案。実測やA/Bテストで変更し得る。
- **要検証**: 会話中の調査で得たが、実装前に最新版・原典・ライセンスを再確認すべき内容。

## 現在の要約

- **確定**: 目標は「約10M parameters、日本語専用、短文生成と数ターンの雑談対話」。高度な推論や長文RAGではなく、狭い能力を高密度に持たせる。
- **確定**: Tokenizer、モデル重み、事前学習、Dialogue SFTまでスクラッチで構築する。
- **確定**: Phase 0〜3はiMac、Phase 4はWindows/WSL＋RTX 4090で完了。WSL package 3.0.1.0 / Ubuntu WSL 2を使用。Phase 4のNorm/default最大安定batchはeager T8K 57 / T4K 64。③でNoNorm/math最大batch 45、compiled/math最大53、Flash/compile最大111を確認。最速はFlash/compile batch 32、694,521 tokens/s。約8TBはユーザー計画で、Phase 6①②完了時のLinux空き実測は950,875,688,960 bytes（約950.9GB / 885.6GiB）。
- **選定済み（Phase 5の小予算比較）**: 本学習候補はT4K / NoQK-Norm / LR 0.002。hidden 256、13層、FFN 640、4Q/2KV GQA、SwiGLU、RoPE、RMSNorm、context 1024、tied embeddingで10,001,152 parameters。停止・反復・sampling UnicodeとNoNorm変換は未達・未対応。
- **実測済み**: 4k/8kの100M比較と近似bytes/time比較は完了。同一tokenと近い時間ではT4Kが有望、近いbytesではT8Kが僅かに良く、語彙の普遍的な優劣は断定しない。
- **確定**: 学習量は100M比較 → 500M → 1B → 2B → 5B → 10B → 20B → 50B tokensの段階評価。50Bは20B時点で改善が続く場合のみ実施する。
- **確定**: Vast.aiは初期開発には使わず、後半の並列比較・スケーリング実験に限定する。

着手順と各フェーズの目的・ゴール・成果物・完了条件は[フェーズ別実行計画](15_project_roadmap.md)を参照する。まず再現可能な最小pipeline、10B Base、Chat、量子化ローカル実行までを完成させる。20Bの比較と条件付き50B、追加アーキテクチャ研究は後続系列として判断する。

**完了範囲**: [4k/8k Tokenizer](18_phase2_completion.md)、[両モデル/cache/学習前export](19_phase3_completion.md)、GPU学習器・評価・再開・速度を検証済み。Phase 3重みはランダム初期化、Phase 4には小さい学習済み検証checkpointがある。Python 3.12.7、実行は`uv run --frozen`、依存変更は`uv add`。

**現在地**: [Phase 4の実GPU検証](21_phase4_completion.md)と[Phase 5の候補選定](23_phase5_completion.md)が完了し、Phase 6①〜⑤と500M学習・評価が完了し、1B前で停止中。Base/Chatの本学習・能力目標は未達。①②は756M unique train stream tokensとWSD stable/decayのCUDA完全一致、全74 tests / skip 0、73 GPU checksを確認した。[完了証拠](26_phase6_preparation_completion.md)。最新の状態は[継続記録](autonomous_status.md)、④⑤の準備検証も`93c7d1d`で完了し、再開後の本学習は[残りの実行計画](27_phase6_remaining_plan.md)を参照する。

**別PCでの再開入口**: [Windows/WSL＋RTX 4090の再開手順](windows_handoff.md)。GitHubの取得からHub成果物の復元、uv環境、CUDA確認、実装順までを順に実行できる。

**進め方**: 完成までの時間短縮を優先する。Phase 3の最終検証一式は実装後24.62秒で、実装・修正を含む作業時間とは別。Phase 3の再実装を移行条件にせず、既存artifactの引継ぎから進める。実装時間とGPU計算時間を分け、Phase 6③の実測694,521 tokens/sから純学習予算を更新済み。全文評価・保存・枝・調整を別計上し、完成時刻とは区別する。[詳細](15_project_roadmap.md#高速に完成させる進め方)

## 文書一覧

1. [01_project_goal.md](01_project_goal.md) — 目的、成功条件、過去モデルとの位置付け
2. [02_research_summary.md](02_research_summary.md) — 調査結果と採否の要約
3. [03_architecture.md](03_architecture.md) — モデル仕様、パラメータ予算、派生案
4. [04_tokenizer.md](04_tokenizer.md) — 4k/8k Tokenizer、特殊token、正規化
5. [05_dataset.md](05_dataset.md) — データ候補、ライセンス、50〜100B master corpus
6. [06_training_plan.md](06_training_plan.md) — 段階学習、SFT、Vast.ai方針
7. [07_environment.md](07_environment.md) — RTX 4090、WSL、8TB、shard配置
8. [08_evaluation.md](08_evaluation.md) — 評価、checkpoint、TDD、再現性
9. [09_prior_art_and_baselines.md](09_prior_art_and_baselines.md) — 25M/100M configと100M以下の公開モデル
10. [10_next_steps.md](10_next_steps.md) — フェーズ別計画に対応した実装checklist
11. [11_technical_research_gaps.md](11_technical_research_gaps.md) — 追加調査の入口、未解決課題、優先順位、検証gate
12. [12_training_implementation_research.md](12_training_implementation_research.md) — QK-Norm仕様、cache、parameter再計算、段階学習、4090 benchmark
13. [13_tokenizer_dialogue_data_research.md](13_tokenizer_dialogue_data_research.md) — 正規化、特殊token、4k語彙予算、会話データ候補、SFT、蒸留
14. [14_evaluation_deployment_research.md](14_evaluation_deployment_research.md) — BPBの実装、公平な比較、雑談評価、GGUF、量子化、CPU推論
15. [15_project_roadmap.md](15_project_roadmap.md) — 目標から逆算したフェーズ別計画、目的・ゴール・成果物・完了条件・進行判断
16. [16_phase0_completion.md](16_phase0_completion.md) — Phase 0の実施結果、要求ごとの証拠、検証範囲、次の着手
17. [17_phase1_completion.md](17_phase1_completion.md) — 実データpilot、manifest・split、会話品質、Tokenizer sample、再生成・完了監査
18. [18_phase2_completion.md](18_phase2_completion.md) — Tokenizer学習・入出力・会話tokensの実測
19. [19_phase3_completion.md](19_phase3_completion.md) — モデル/cache/HF/native GGUF/量子化の実測
20. [20_publication_review.md](20_publication_review.md) — 当時の公開前確認、ローカル情報除去
21. [21_phase4_completion.md](21_phase4_completion.md) — WSL/CUDA・学習器・保存再開・評価・容量・速度の実機証拠
22. [22_phase5_plan.md](22_phase5_plan.md) — Phase 5の目的・条件・予算・scheduler判断
23. [23_phase5_completion.md](23_phase5_completion.md) — overfit/smoke/100M比較・候補選定・品質未達・独立監査
24. [24_phase6_plan.md](24_phase6_plan.md) — gateの完了/未着手、500M〜10B段階評価・予算
25. [25_phase6_preparation.md](25_phase6_preparation.md) — ①②の事前の目的、凍結条件と停止境界
26. [26_phase6_preparation_completion.md](26_phase6_preparation_completion.md) — ①②の実量、全corpus/CUDA監査、保存先、実CLI
27. [27_phase6_remaining_plan.md](27_phase6_remaining_plan.md) — ①〜⑤の完了証拠、再開後の500M〜10B、Chat・量子化・拡張の条件
28. [28_phase6_performance.md](28_phase6_performance.md) — ③の実GPU高速化・backend実効確認・容量と厳密再開の比較
29. [29_phase6_performance_completion.md](29_phase6_performance_completion.md) — ③の採用速度・最大容量・厳密/cold再開・独立監査と停止記録
30. [30_phase6_readiness_execution.md](30_phase6_readiness_execution.md) — ④⑤の限定比較、CPU精度修復、正式検証・凍結設定・commitと停止記録

運用文書: [最新状態](autonomous_status.md)、[復旧履歴](autonomous_history_20261003.md)、[Windows/WSL引継ぎ](windows_handoff.md)、[固定Hub復元](huggingface_handoff.md)、[自律runner](codex_automation.md)、[評価仕様](evaluation_protocol.md)。[data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)に各保存領域の手順を記載する。

実行時の仕様は[評価仕様](evaluation_protocol.md)と[Windows/WSL移行手順](windows_handoff.md)を参照する。データとTokenizerの[Hugging Face公開版の取得手順](huggingface_handoff.md)も利用できる。

## 追加調査の要点（2026-10-02）

未実装のまま残っていた技術判断を、一次資料と公式コードから補足した。最初は[追加調査の入口](11_technical_research_gaps.md)を読む。

- **提案**: QK-NormをQwen3式のhead次元RMSNormとして具体化すると、T8Kは9,772,800、T4Kは10,002,816 parametersとなる。旧概算との差はgainの共有方式による。
- **提案**: SentencePieceの正規化と構造tokenの挿入方式を固定し、本文中の役割表記と構造IDを区別する。
- **提案**: BPBに加え、同一原文bytesと同一GPU時間での比較条件を用意する。
- **提案**: 長期学習前にランダム重みでHF／GGUF互換性を確認する。FFN幅576／640ではK-quantの型fallbackを確認する。
- **確認済み**: llama.cppの一般的なSentencePiece変換経路と独自Unigramの分割方式は同一ではない。内蔵Tokenizerへの互換性を検証し、必要なら外部SentencePieceでIDを作る経路を使う。
- **現在の判断**: 4090速度はPhase 4、会話教師token量はPhase 2で実測済み。Phase 5の候補選定は完了。雑談品質・学習後の量子化品質と、拡張corpus/長期予算での優位性は未達・未実証。

追加調査は学習・推論実験を実施した結果ではない。既存の確定方針を維持し、実装候補と検証条件を追加している。

## 重要な注意

公開データの「商用利用可能」は、データセット配布ライセンスだけで最終判断しない。Common Crawl由来データでは、データベースライセンスと各Web文書の著作権は別問題である。公開・販売前に、採用した各source subsetの利用条件、帰属表示、ShareAlike条件、削除要求対応を再確認する。本書は法的助言ではない。

最終更新: 2026-10-03。外部資料の調査日は各文書へ残し、研究候補と実装・実測結果を区別する。
`````

## docs/06_training_plan.md

UTF8 LF SHA256: 5f8fddf520cd1827302f251d7b30d1ae03007879b5e84d1828c2113ed8e59a01

`````markdown
# 学習計画

Phase 6①〜⑤の準備検証を完了し、`93c7d1d`へcommit済み（2026-10-03）。400生成・全文dev評価、学習済みNoNormのCPU推論精度profileによる全12変換比較、実CLI/重み監査149 checks、全90 testsが成功。本学習設定version2を凍結し、500M以上のBase本学習を開始せず停止中。

最終更新: 2026-10-03。AdamW＋warmup/cosine・WSD stable/decayは実装済み。Phase 6の長期schedulerはWSDを採用し、stable/decayは実装・CUDA検証済み。Muon・Chat trainerは未実装。train CLIは引数から設定を作り、baseline JSONを自動読込しない。現在のresumeは固定schedule/config/source/dataの変更を拒否するため、予算の延長を同一runの再開として扱わない。50Bは改善と予算条件を満たした場合のみ、外部の有料GPU実行は別途ユーザーの指示が必要。

## 全体像

①〜⑤の準備完了と未開始の本学習は[Phase 6計画](24_phase6_plan.md)、残る作業の目的・実装入口・完了条件は[再開時の実行計画](27_phase6_remaining_plan.md)を参照する。現在の選定候補は1つで、長期WSD/LR/保存/容量は[version2](../configs/phase6/base_frozen.json)へ凍結済み。`launch_enabled=true`は技術gateの成立であり、文書更新を学習再開の指定として扱わない。

プロジェクト全体の目的・ゴール・成果物・完了条件は[フェーズ別実行計画](15_project_roadmap.md)を参照する。本書は学習系列の設定とcheckpoint段階を扱う。10B BaseからChatへ分岐し、20B/50Bの終了をChat着手の前提にしない。

**現在地（2026-10-03）**: Phase 0〜5が完了。WSL＋RTX 4090で学習器・shard・BPB/生成評価・保存再開・最大安定batchを検証した。Phase 5のoverfit/smoke・4本の100M比較と独立監査も完了し、T4K / NoQK-Norm / LR 0.002を候補に選定した。Phase 6①〜⑤の準備完了で停止中（本学習未開始）。smokeはdev BPBが改善したが、抑制ありgreedy EOS 0/80・反復63/80で、本学習・Base/Chat品質目標は未達。実装時間とGPU計算時間を分け、③で採用したFlash＋compile reduce-overhead / batch 32の694,521 tokens/sから純学習予算を見積もる。全文dev336.292秒・400生成360.684秒、decay枝・保存・compileを別計上して⑤の予算へ保存した。[④⑤の検証](30_phase6_readiness_execution.md)。[高速化完了](29_phase6_performance_completion.md)。[詳細計画](22_phase5_plan.md)、[進め方](15_project_roadmap.md#高速に完成させる進め方)

```text
Tokenizer 4k / 8k・Phase 4実測は完了
        -> 100件overfit（合格）
        -> 10M-token smoke（合格）
        -> 100M T4K/T8K・Norm・LR比較（完了、Muon追加不要）
        -> Phase 6①756M unique train / ②WSD全state完全一致（完了）
        -> ③高速化/容量 -> ④生成/CPU変換精度 -> ⑤設定凍結（準備完了）
        -> 本学習前で停止中; ユーザー再開後に500Mから開始
        -> 500M / 1B 選定候補の日本語生成と継続価値を評価
        -> 2B 継続価値（過去355M artifactがなければ直接比較は未実施）
        -> 5B 本命を1つに決定
        -> 10B Base v1
             |-> Dialogue mid-training -> SFT -> Chat v1 -> 量子化/ローカル実行
             |-> 20B Base v2 -> 改善継続時のみ50B
                   -> 有望なら同じChat手順で再比較
```

## Checkpoint段階

**確定**: 少なくとも100M、500M、1B、2B、5B、10B、20B、50B tokensで保存する。10M-token smokeは本番系列とは分けてもよい。

| 段階 | 目的 | Go/No-Go |
|---:|---|---|
| 10M | pipeline、loss低下、生成、保存再開 | overfit/smokeが通る |
| 100M | 4k/8k、QK-Norm、LR、optimizer比較 | 発散せずBPB改善 |
| 500M | early scaling確認 | repetitionが悪化しない |
| 1B | 日本語生成の立ち上がり | 現在の1候補を継続。対照追加は理由・予算を固定し最大2つ |
| 2B | 過去の約2B-token経験との比較 | 継続価値を判定 |
| 5B | 本命architecture決定 | 1モデルへ集約 |
| 10B | Base v1完成 | 固定評価とartifact保存 |
| 20B | Base v2、本命 | 10Bとの差を統計比較 |
| 50B | 過学習/容量限界の研究 | 20Bでも改善時のみ |

## Optimizerとlearning rate

**Phase 5の決定**: AdamW、LR 0.002を本学習候補へ採用。LR 0.001は同一構成でBPB悪化、0.003は追加せず、Muonは安定したAdamWで候補を選べたため保留。batch/corpus変更後の安定性と長期最適性は未実証で、次回の準備で確認する。

**当初の比較案**:

- baselineはAdamW
- modern比較は2D hidden weightsへMuon、embedding/norm/scalarへAdamW
- 100M-token runでpeak LR `1e-3`, `2e-3`, `3e-3`程度を小さくsweep
- warmup、cosine decay、weight decay、gradient clippingをconfigへ明記
- validation BPB、gradient norm、loss curve、tokens/secで決める

最初からarchitecture、optimizer、data mixtureを同時に変えない。一度に一つの主要因を比較する。

**Phase 5での判断**: 小探索は終点固定cosine、本系列はWSDを採用する方針。継続用stable枝と評価用decay枝を分け、optimizer更新回数、effective batch、枝ごとのtokensとGPU時間を記録する。WSD実装・分岐のCUDA再開検証は①②で完了。③の速度・容量測定は完了。長期の数値予算は④の診断と⑤のLR安定性確認後に凍結する。Phase 5の100M終点を予算だけ変更して延長しない。[詳細計画](22_phase5_plan.md#長期schedulerの選択と引継ぎ)、[実装・段階学習調査](12_training_implementation_research.md)を参照する。

## Batchとperformance

**確定**: Phase 0〜3のiMac開発からWindows/WSL＋RTX 4090へ移行済み。本学習は容量上限と速度を測り、厳密再開を通過した最速micro batchを候補にする。Phase 4のeager/defaultの運用上限はT8K 57 / T4K 64、最高速度の測定点はcompile/default batch 8。Phase 5は厳密resumeのためeager/math、batch 8を採用し、100Mで約12,208更新を確保する。③でreference/math最大45、compiled/math最大53、compiled Flash最大111を検証し、最速のFlash＋compile reduce-overhead batch 32を採用した。32,768 input tokens/updateで、長期LR0.002/WSDは⑤でversion2へ凍結済み。[③の実測](29_phase6_performance_completion.md)。[移行・batch方針](07_environment.md)

**③で実施済み**: RTX 4090でmicro batchを倍増・境界探索し、容量上限と最高速度を別に確認した。batch 111のdriver peakは97.64%、batch 32の速度が最も高く、運用候補は32を選択した。以下の観測値をreportに保存した。

- tokens/sec
- GPU utilization
- VRAM usage
- step time
- GPU使用率の時系列（MFUは未測定で別項目）
- data wait time

OOM境界付近は中間値を試し、loss/backward/optimizerと実shardの運用まで含めて最大安定値を確認する。gradient accumulation後のeffective batch、LR、warmup、更新回数は別に管理する。小探索でbatchを小さくする場合は比較目的と理由をconfig/台帳へ残す。

Phase 4〜5のFlash-only/mask失敗は保持した。③で固定長・PADなし学習専用のmaskなしcausal経路とbackend別compile cacheを実装し、Flash＋reduce-overheadを実GPU検証した。選択設定のdata waitは0.55%。最大安定容量と最速設定は各3×200・保存/小sample評価・厳密再開を通過し、採用設定のcold-cache再開も完全一致。推論/cacheには従来の明示mask経路を使う。

## Dialogue mid-trainingとSFT

**確定**: Chat版はBase完成後に作る。

形式案:

```text
<|user|>
今日は仕事疲れた
<|eot|>
<|assistant|>
お疲れさま。今日は忙しかった？
<|eot|>
```

**提案**: SFTは10M、30M、100M dialogue tokensを比較し、lossはAssistant部分だけへ適用する。過剰なinstruction tuningでBaseの日本語流暢性を崩さないか確認する。

**提案（追加調査）**: 上記tokensは累積学習量であり、uniqueデータ量とは区別する。総系列tokensとAssistant教師tokensを両方記録し、Assistant本文直後のEOTも教師対象とする。データ候補、role割当、maskのshift、反復回数の扱いは[会話データ・SFT調査](13_tokenizer_dialogue_data_research.md)を参照する。

## Distillation

**提案**: scratch pretrainingのbaselineを先に完成し、その後teacher logitsまたは高品質synthetic responseによるdistillationを比較する。Distillationを使ってもstudent weightsがrandom initializationから学習される点は変わらないが、「純粋なcorpus-only scratch」とは結果を分けて報告する。

## Vast.ai

**確定**: 初期のTokenizer学習とモデル実装・CPU検証はiMacで完了。学習器・GPU検証はローカルRTX 4090で完了した。今後の500M〜20B、Dialogue SFTもローカルで進める。

Vast.aiは後半に限定する。

- 4k/8k × 複数architectureの並列化
- 5M/10M/25M/50M/100M scaling比較
- Transformer/Layer Sharing/Mamba/Conv hybridの並列run
- ローカルで有望と判明した設定の再現run

過去会話での上限予算は$1,000だが、価格は変動するため利用時に再見積もりする。目的は「単一runを外へ移す」ことではなく「独立実験を並列化する」こととする。

WSD stable予算の延長forkは未実装で、`--branch-from`はdecay専用。通常resumeでは終端budget・source・dataを変更できない。20B/50Bやmixture変更には明示forkの実装・履歴・厳密再開検証が必要。[継続の契約](27_phase6_remaining_plan.md)
`````

## docs/10_next_steps.md

UTF8 LF SHA256: 8b037ee2248f9597e1f0d5f388f4f89c7b5d83444be8a9ab022013a4eedd076e

`````markdown
# 次の実装タスク

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新結果](../reports/phase6/base_500m_review.json)。

この文書は[フェーズ別実行計画](15_project_roadmap.md)の着手checklistである。Phase番号、目的、ゴール、成果物、完了条件、Go/No-Goは同計画を正とし、技術仕様は03〜08と12〜14を参照する。2026-10-02にiMac上のPhase 0を実施した。[完了記録](16_phase0_completion.md)を参照する。Phase 1のcorpus・manifest・split・会話pilotも完了した。[完了記録](17_phase1_completion.md)を参照する。[Phase 2](18_phase2_completion.md)・[Phase 3](19_phase3_completion.md)も完了。本学習は未実施。Windows/WSL実機検証は[Phase 4](21_phase4_completion.md)で完了した。

**現在の境界**: [Phase 5](23_phase5_completion.md)は完了し、Phase 6①〜⑤と500M学習・評価が完了し、1B前で停止中。①②のcorpus/WSDと③の高速化・容量・厳密/cold再開を完了し、性能証拠は`a7d26e1`へcommit済み。④⑤の生成/変換確認・設定凍結も`93c7d1d`へcommit済み。次の着手候補は生成退行の原因調査。対照/予算/終了条件を定義し、ユーザーの再開指定を待つ。1Bへ自動継続しない。[③の完了](29_phase6_performance_completion.md)。Phase 4の学習器・評価・保存再開・最大安定batchは完了済み。Pythonは`uv run --frozen`、依存変更は`uv add`。

完成までの時間短縮を優先し、[移行 → 最小学習経路 → 保存再開 → 最大batch/速度実測](15_project_roadmap.md#高速に完成させる進め方)を完了した。新規PCでは[再開手順](windows_handoff.md)に従い、最新コードとGit管理外の固定Tokenizer/pilotを引き継ぐ。復元済みPCでは再取得・Phase 3の再実装は不要。実装時間とGPU計算時間を分け、実測した計算時間に評価・保存・比較・データ処理を加えて見積もる。

## Phase 0: 成功条件・環境・実験管理

- [x] `src/`、`configs/`、`tests/`、`scripts/`と実験台帳の骨格を作る。
- [x] iMac環境とuv管理の依存設定を記録し、Windows/WSL 3.x/Linuxへの移行手順を用意する（GPU実機記録はPhase 4）。
- [x] run/config/artifact schemaとhash記録を決める。
- [x] Base/Chat各100件の独自固定prompt、dev/test、rubric、generation条件、数値誤差の仕様を作る。

## Phase 1: 小規模データと会話pilot

- [x] FineWeb2 Edu JapaneseとRealPersonaChatの候補revision・配布条件・形式を確認し、調査metadataを保存する。
- [x] `uv add --optional data`でデータ処理用依存を登録し、lockする。
- [x] source台帳とdocument/dialogue manifest schemaを作る。
- [x] source/subset/revision・利用条件の証拠を台帳へ固定し、取得範囲・容量上限・保存先をconfigで決める。
- [x] 固定revisionから小規模本文データを取得する（Web20,000文書・会話3,000対話を取得、Web19,998文書と会話全件を採用）。
- [x] 小sampleへraw/canonical hash、品質、duplicate cluster、splitのmanifestを付ける。
- [x] FineWeb2 Edu Japanese等の小subsetをfilter/dedupし、cluster単位のsplitを固定する。
- [x] Tokenizer学習用sampleをtrainから作る。
- [x] 会話候補1k〜10k対話でspeaker/tree/品質と文字ベースの会話長を確認する（1024-token内の割合はPhase 2）。

## Phase 2: Tokenizer 4k/8k

[完了](18_phase2_completion.md)。同じsample、固定語彙数、全corpus round-tripと会話window教師計数を検証した。

- [x] 同じsampleでSentencePiece Unigram + byte fallbackを4096/8192語彙で学習する。
- [x] 正規化、空白/改行、特殊IDと本文/構造IDの区別をgolden例で検証する。
- [x] domain別圧縮率、fallback率、1024超過率を比較する。
- [x] 会話のunique量、総系列tokens、Assistant教師tokensを再計数する。

## Phase 3: Transformer・cache・学習前export

[完了](19_phase3_completion.md)。両実モデル、HFとnative float GGUF、Q8/Q4候補を検証した。

- [x] T8Kから実装し、RMSNorm/RoPE/GQA/QK-Norm/SwiGLU/tied embeddingを検証する。
- [x] T4Kへ展開し、parameter countがT8K 9,772,800、T4K 10,002,816であることを確認する（head間gain共有QK-Norm案）。
- [x] causal mask、padding、finite gradient、prefill/1-token/chunk cache一致を検証する。
- [x] ランダム重みでHF/float GGUF logitsとTokenizer契約を別々に確認する。
- [x] 必要なら外部SentencePiece経路を実装し、EOT停止と量子化型fallbackを確認する。

## Phase 4: 学習器・再開・4090実測

- [x] iMacから別のWindows＋RTX 4090 PCへ切り替え、WSL 3.x/Linuxで同じconfig/Tokenizer/sampleを復元する。
- [x] 実WSL version、distribution実行方式、GPU/driver、PyTorch/CUDAを記録し、hash/ID一致とCUDA動作を確認する。
- [x] `uint16` shards、document index、mmap loaderと消費済み位置の保存を作る。
- [x] AdamW/BF16 autocast、gradient accumulation、scheduler、checkpointを実装する。
- [x] 準備runから学習runへschema/台帳を拡張し、実際のtokens/steps、checkpoint、完了/失敗を記録する。
- [x] 本文NLL、window/stride、BPBとBase生成suiteのrunnerを実装・検証する。
- [x] 連続200 stepsと100 steps→保存→再開100 stepsのtoken列/loss/weightsを比較する。
- [x] syntheticと実shardでeager micro batchを最大安定値まで増やし、backend/compile、VRAM、data wait、速度を測る。
- [x] 100M〜50Bの時間とストレージを実測から見積もる。

[Phase 4実測・制約](21_phase4_completion.md)。Phase 5も完了し、Phase 6①〜⑤と500M学習・評価が完了し、1B前で停止中。

## Phase 5: 最小pipelineと100M探索

- [x] 100件overfit、10M-token smokeで学習・生成・保存再開を一周する（機械的gateに合格、停止・反復の品質未達はstatusへ記録）。
- [x] 100Mで4k/8k、QK-Norm、LRを一要因ずつ比較する。
- [x] Muon追加の必要性を判断する（AdamW全4比較が安定・改善し候補を選べたため、今回は追加しない）。
- [x] BPB、処理bytes/GPU時間、更新数、生成失敗を比較し、T4K / NoQK-Norm / LR 0.002の1候補を選定する。
- [x] dev/pilotを使い、品質閾値を最終test評価前に固定する（数値を維持し、100M結果前にtargets.statusをfrozenへ変更）。

## Phase 6: 500M〜10B Base v1

[段階評価とgate](24_phase6_plan.md)、[本学習以降の目的・完了条件](27_phase6_remaining_plan.md)。①〜⑤の準備と500M学習・評価が完了し、1B以降は次回再開後の作業。

- [x] 500M開始用corpusのsource/revision/取得上限・unique量・Web 100%配合・反復とdev/test分離を固定し、全raw/cluster/shardを監査する（756M unique train stream tokens）。
- [x] WSD stable/decay分岐を実装し、採用NoNorm・実shard・CUDA/BF16/mathで全state/loss/token列の完全一致を検証する。
- [x] ③ 採用NoNorm・拡張shard・WSDでmath/compiled-math/Flashの実演算・最大安定容量・最速値・厳密再開/分岐・6設定の3×200更新/評価/saveを確認。Flash＋compile batch 32=694,521 tokens/s、最大111、独立1286 checks・cold再開26 checks・全79 tests成功。[完了証拠](29_phase6_performance_completion.md)。
- [x] ④ NoNormのUnicode・反復・EOS停止、native/cacheとHF/GGUF変換を切り分け、固定dev 400生成で修正/対照・未達を記録する。
- [x] ⑤ 採用batchの安定性を確認してeffective batch/LR/WSD数値予算と実CLI/restart commandを凍結し、log/PID/boot/start ticks/checkpoint SHA、枝compute・保持数・容量上限を保存する。
- [x] 拡張trainの500M stable・独立763更新decay・全文dev/400生成比較を完了し、全state checkpointと監査reportを保存する。

- [ ] 500M/1B/2Bで段階評価し、5Bまでに本命1モデルを決める。
- [ ] 段階評価で必要と判断した場合にデータを追加する。現在のPhase 6 dev/test保護・変更系列のprovenanceを先に実装し、取得上限を固定する。50〜100B全量を500M開始条件にしない。
- [ ] 固定mixture系列と変更系列、継続stable枝と評価decay枝を区別する。
- [ ] 10B Base v1のartifactと固定評価を作り、日本語短文の達成/未達を記録する。

## Phase 7: Chat v1

- [ ] Dialogue mid-trainingのconfig/予算を固定し、Base→SFTの小対照も残す。
- [ ] Assistant本文+EOTのmask、shift、教師0件、turn単位の切り捨てを検証する。
- [ ] SFT累積総系列10M/30M/100M候補を比較し、教師tokens/unique量/反復を併記する。
- [ ] 固定対話で関連性、2〜数ターンの文脈、停止、反復、role、Unicodeを評価する。
- [ ] 固定履歴とは別にモデル生成を戻す複数turn rollout、自動失敗flag、人手評価・一致率を用意する。
- [ ] devで選んだChat v1を独立testで評価する。

## Phase 8: 量子化とローカル実行

- [ ] 学習済みBase/ChatでHF/float GGUF parityと停止を再確認する。
- [ ] Q8/Q4の品質差、tensor実型、weights/全artifact容量、RSS、CPU応答時間を測る。
- [ ] model card、hash、source/帰属、依存、再現/推論手順を揃える。
- [ ] 独立環境でBase completionとChatを起動し、容量/品質目標の達成を確認する。

## Phase 9: 20Bと条件付き50B

- [ ] stable予算延長の明示forkと履歴・全state再開検証を実装してから20Bへ進め、10Bとの差・信頼区間・追加予算を報告する。
- [ ] 改善継続と予算が成立する場合のみ50Bへ進む。
- [ ] 新BaseをChatへ採用する場合は同じSFT/量子化/配布検証を再実行する。

## Phase 10: 後半研究

- [ ] Layer Sharing、テキスト蒸留、ReLU²、Mamba2/Conv hybrid、規模比較を優先順に検討する。
- [ ] 各proposalで対照条件、改善metric、compute予算、採用基準を先に決める。
- [ ] Vast.aiはローカル検証済みの独立run並列化に限定し、利用時に再見積もりする。

## 完了した最初の一周と次回の境界

```text
Phase 0〜4: データ / Tokenizer / モデル / export / 学習器 / 評価 / GPU再開・実測は完了
  -> Phase 5は完了、Phase 6①〜⑤と500M学習・評価が完了し、1B前で停止中
  -> 100件overfit / 10M-token smokeは合格
  -> T4K/T8K・Norm・LRの100M比較、補助評価、候補選定も完了
  -> ①拡張corpus / ②WSD全state一致は完了
  -> ③容量・高速化・厳密/cold再開は完了
  -> ④400生成/全文dev/CPU精度profileの12比較と実CLI149 checksは完了
  -> ⑤LR3候補/厳密cold再開/設定version2凍結は完了（93c7d1d）
  -> 次回の再開指定後: 500M -> 独立decay/評価 -> 1B/2B/5B/10B
```

この一周は完了した。ユーザーの本学習再開指定後に、凍結source/data/runtimeと既存process/checkpointを照合し、新規初期化seed42で500Mから始める。Phase 5や準備runのcheckpointを本学習の初期状態へresumeしない。会話pilot・評価準備は早期から並行する。具体的な未解決事項と根拠は[追加技術調査](11_technical_research_gaps.md)、会話データは[Tokenizer・会話データ調査](13_tokenizer_dialogue_data_research.md)、推論経路は[評価・配布調査](14_evaluation_deployment_research.md)を参照する。
`````

## docs/15_project_roadmap.md

UTF8 LF SHA256: 1bad454d69812bc26c0379f6845322c7c14d68e4247bc48723c699113dd83fda

`````markdown
# JMicro-10M フェーズ別実行計画

2026-10-04最新: ユーザー指定のチャットstep1（10B実行設定準備）を[完了](40_base_10b_preparation.md)。専用config/schema/runner凍結、14tests/実CUDA16更新524288検証tokensの全state保存再開一致、保存証拠26項目成功。GPU19.217秒、actual jobs終了、科学tokens0。旧core/重み/品質条件を保持。本学習は明示--trainの次段階であり今回は未開始。report/local commitで停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: ユーザーが直前計画の①10B用設定準備を指定。専用config/runner/schemaを実装・凍結、関連14tests成功。saved4.75Bからの実CUDA保存再開確認のみ行い科学10B学習は未開始。既存データ/旧重み/coreを保持して準備report/local commitで停止。本学習には明示--trainが必要。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新（計画訂正のみ）: ユーザー指定で[次回案](39_learning_scale_and_generation_plan.md)の中間7.5Bを省き、既存12.23B trainで直接総10Bへ学習する方針へ更新。保存stable4.75Bから9.5B＋最終decay、追加科学5,249,990,656tokens。10Bで同じ全文/400と原raw条件を評価し、改善・合格時だけ新親EOS対照へ進む。データ収集ではなく学習量の拡大。GPU約145〜165分/上限3時間、計画更新/local commitのみで実行未開始。[実状態](autonomous_status.md)。以下の7.5B段階案は履歴。

2026-10-04最新（計画のみ）: [学習量拡大と生成改善の次回案](39_learning_scale_and_generation_plan.md)。既存12.23B trainで総7.5Bを比較し、改善と元raw増量安全条件を満たせば10B。最良新親の短文仕上げを一対、UTF8制約は別推論policyとして比較する。本文BPB・停止・反復・意味・raw Unicodeを分け、表示/制約成功を元学習gateの免除にしない。新run/config/command未作成、GPU学習/推論は開始せず計画/local commitで停止。20B/50B/Chat/UL/sweepなし。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: EOS/UTF8改善の1〜3を[完了](38_eos_5b_finish_results.md)。共通表示helper/33tests、同じ5Bから各100Mと別CUDA再開検証、両全文dev/400と全自然停止の内容確認を実行。固定EOS0→13/反復57→51、全文BPB対照比+0.095894%だが短文sampling rawUnicode2により原採用/増量gate不合格。意味誤りも残りBase/Chat品質未達、診断重みとして保持。GPU37分34秒/50分以内、actual jobs終了。report/local commitで停止し10B/Chat/UL/decoder sweep未開始。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: ユーザーが[改善計画](37_eos_repetition_utf8_improvement_plan.md)の1〜3を実行指定。UTF8末尾helperを実装/CPU確認し、final5Bの各100M低LRWeb/short20対照を実装・凍結、実CUDA再開gate後に学習/原screen/合格時の全文と内容確認へ進む。GPU上限50分、元品質/採用基準を保持し表示修正を学習効果に数えない。1〜3完了/report/commitで停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新（調査/計画のみ）: [EOS・反復・UTF8改善計画](37_eos_repetition_utf8_improvement_plan.md)。保存EOS損失は5Bで改善しても自由生成停止0。既存低LR短文比較の成功を根拠に、表示末尾処理と同じ5B親のWeb/short20各100M対照を次回案とする。元raw評価/採用条件/品質目標を維持し合格時のみ全文/400、GPU上限50分。CPU saved-artifact研究のみ完了、新学習/推論/production修正なし。計画を記録/commitして停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: step3の[5B比較を完了](36_base_5b_comparison.md)。同じ全文dev BPB0.964484で元2B比1.87%改善、固定EOS0/80/反復59/80、UTF8末尾切断1/80・全400で同じ例2件。元の新Unicode失敗なし条件を保持して増量gate不合格とする。内容確認でも数量/文脈誤り・意味反復が残りBase/Chat品質は未達。追加学習0、GPU13分8秒で30分以内、GPU job終了。記録/commitで停止し10B/Chat/sweepに移行しない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: ユーザー指定でstep3の[5B比較](../configs/phase6/base_5b_comparison.json)を再開。元2B/低LRWebの保存済み対照を再利用し、同じ全文devと400生成でfinal5Bを評価。short20はmixtureが違う参考条件。追加学習0、元品質基準維持、GPU上限30分。内容確認/report/commit後停止し10B/Chat/sweepへ進めない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: 次計画1・2（明示stable延長・総5B学習）を[完了](../reports/phase6/base_5b_review.json)。同じ10M/既存12.23B train、追加3.10B科学tokensと別524,288検証tokens、最後約5%decayを含む総5,000,003,584。CPU6tests/実CUDA全state再開一致、連続・有限更新、parent不変、GPU75分43秒で上限内。品質は未評価で元Base/Chat基準は維持。記録・commit後停止し、次は未実行のstep3全文dev/固定生成比較。10B/Chat/sweepへ自動移行しない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: ユーザーが次計画1・2（継続処理実装と総5B学習）を再開。[5B実行計画](35_base_5b_execution.md)。stable1.9Bから予算のみを延長する明示fork、Web100%、最終約5%decay、元品質基準を維持。学習完了/report/commitで止め、step3全文評価と10B/Chatは未開始。学習量到達と品質達成を区別する。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: [低学習率の計画1〜3を完了](../reports/phase6/eos_low_lr_100m_review.json)。旧ログ/3保存点の調査、同じ元2BからLR曲線0.1倍の各100M、同じ全文89,416dev/各400生成を実行。BPB Web0.972969/short0.974799で元2B0.982882を改善、固定EOS0→27/80/反復55→41、生成失敗0。原mixture/全文/増量gateは全合格、12関連testsと実CUDA全state再開一致、GPU35分41秒で45分上限内。ただし意味反復/文脈誤りが残りBase/Chat品質基準は未達。report/commit後停止し、5B/Chat/自動sweepは未開始。[実状態](autonomous_status.md)。以下は経過履歴。

2026-10-04最新: [完結単位の各100M対照と全文評価を完了](../reports/phase6/eos_complete_100m_review.json)。固定自然EOS0→24/80、補助0→42/80、自動mixture gate合格。ただし意味誤り/反復が残り、両100M枝の全文BPBは元2Bより悪化。短文枝は診断候補として保持し、元2Bを基準にする。原Base/Chat品質目標は未達、WebのUnicode退行により5B条件も未達。関連24 tests成功/実CUDA全state再開一致、全GPU job実終了、累積GPU55分5秒で原45分予算超過を記録。report/commit後に停止し、5B/Chat/自動sweepは開始しない。以下の計画のみ/未実行は履歴。[実状態](autonomous_status.md)。

2026-10-04次の[計画を更新](27_phase6_remaining_plan.md)：32〜64-token完結単位を準備し同じ2B親からWeb対short20%を各100Mで1回比較、固定80/dev256と補助短文80、採用条件は維持。比較/必要な全文評価で一区切り。Web100Mに重大退行がなければ、別のWeb100% stable延長forkで総5Bを検討し、5B結果から10B/必要Base品質/Chatへ進む。mixture採用gateとBase/Chat品質目標を分け、失敗を消さない。今回は計画のみ、100M/5Bの実行は未開始。[提案と予算](../reports/phase6/eos_next_plan.json)。以下は履歴。

2026-10-04短文混合の[対照学習を完了](../reports/phase6/eos_short_pilot_review.json)。同じ2B親から各25,001,984 input tokens、Web対短文20.0524%混合。固定80 greedy64のEOSは両方0/80、反復62→54/80、共通dev256 BPB1.068518→1.069161（+0.06025%）。EOS改善gate未達で短文条件を未採用、conditional全文再評価を省略。対照実験として完了し元2B基準/両新checkpointを保持、report/commitで停止。5B/Chat未開始。次の32〜64-token完結単位比較は未起動案で、pool/予算凍結を先に行う。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04 EOS調査を完了：[実測と改善案](../reports/phase6/eos_2b_review.json)。真の末尾EOS argmax35/256→46/256と改善するが、同じ20ケースのgreedyは512 tokensでも停止0/20/反復20/20。penalty1.1は停止5/20（435〜491 tokens）/反復20/20で解決には足りない。固定64-token基準は維持。次の比較案は短い完結train文書20%混合と既存Webの25Mずつ2枝、改善確認後に手元12.23Bを使う5B学習へ増量。学習比較/5Bは未開始。全件監査を繰り返さず、[実状態](autonomous_status.md)を参照する。以下の停止境界/実行中記録は履歴。

2026-10-04最新: [実train12.23Bデータ整備とユーザー指定2B学習・既存評価を完了](../reports/phase6/base_2b_10b_data_review.json)。同じ約10Mモデルで、減衰込み総2Bを実行。既存dev BPB1.022491→0.982882、greedy反復66/80→60/80、EOS0/80。品質目標は未達のままreport/commitして停止する。5B/10B/Chat・decoder比較は未起動。以下の学習中・旧停止境界の説明は履歴。[実状態](autonomous_status.md)。

2026-10-04: [ローカルデータ整備](32_local_10b_corpus.md)は実train12.23B tokensで完了。ユーザー指示で過剰な独立再照合を省き、構築時の全件検査・独立raw再構築・実train loader合格を採用し、独立全件audit未完了を明記した。さらにユーザーが2B学習を指定し、同じ約10Mモデルを新データで別runとしてGPU学習中。減衰込み総2B、既存protected dev/生成比較、report/commitで停止する。5B/10B/Chat・生成方法の対照比較は未起動。[現在の実状態](autonomous_status.md)。

2026-10-03: 500M後の反復/EOS/data調査も完了。[判断と比較](../reports/phase6/repetition_diagnosis_review.md)。EOS教師漏れは確認されず、文書末尾予測は改善し、反復は131Mから多い。decay後は70/80→66/80。原因をデータ量へ確定せず、次の対照を提案して停止。追加学習/1Bは未開始。

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新結果](../reports/phase6/base_500m_review.json)。

作成日: 2026-10-02。最終更新: 2026-10-03（Phase 6①〜⑤の準備完了・次回本学習の計画と凍結予算を更新）。根拠は[プロジェクト目的](01_project_goal.md)、[設計](03_architecture.md)、[技術調査](11_technical_research_gaps.md)、[Phase 0完了記録](16_phase0_completion.md)、[Phase 1完了記録](17_phase1_completion.md)。既存の**確定**方針から逆算した計画であり、将来の成果物名・未凍結の実行値は**提案**である。品質目標・評価契約はPhase 5で凍結済みで、結果を見て緩めない。

## 最終的に実現すること

約10Mパラメータの日本語専用モデルをランダム初期化から学習し、日本語短文生成と2〜数ターンの雑談をローカルで実行する。コーパス選別、独自Tokenizer、Base事前学習、Dialogue mid-training、Assistant-only SFT、量子化までを再現可能なpipelineとして残す。

最終成果物は次の三つに分ける。

1. `JMicro-10M-Base`: 日本語短文生成の基準モデルと評価結果。
2. `JMicro-10M-Chat`: 関連した短い返答、話題継続、文脈維持、停止を評価した会話モデル。
3. 再現・利用一式: 学習コード、config、Tokenizer、データmanifest、再開可能checkpoint、量子化artifact、ローカル実行手順、実験台帳。

目標規模は9.5M〜10.1M parameters、初期contextは1024 tokens。5〜10MB級は量子化配布の目標であり、Tokenizer等を含む実容量、推論メモリ、品質を測って達成を判断する。高度な推論・コード生成・長文RAGは今回の成功条件へ加えない。

## 現在地と計画の使い方

2026-10-02にiMac上のPhase 0を実施し、uv管理の開発基盤、準備run、環境記録、評価仕様・固定suiteを作成した。[Phase 0完了記録](16_phase0_completion.md)を参照する。モデル・Tokenizer・学習前exportはPhase 2〜3で実装・検証済み。学習器と4090 benchmarkはPhase 4で完了した。本学習と学習後の品質・配布検証は未実施。文献で確認した内容を実機検証の完了として扱わない。

**Phase 0〜5、Phase 6①〜⑤の準備と500M評価が完了。1B前で停止**。[Tokenizer完了記録](18_phase2_completion.md)、[モデル・export完了記録](19_phase3_completion.md)、[Phase 4実機結果](21_phase4_completion.md)を参照する。Phase 5のoverfit・10M smoke・100M比較と候補選定も完了した。[完了記録](23_phase5_completion.md)を参照する。Web 19,998文書と3,000対話を採用し、cluster単位のtrain/dev/test、trainだけのTokenizer用sample約4.50MBを作成した。source台帳・manifest schema・全件復元・6成果物の再生成一致・20件の内容レビューを[完了記録](17_phase1_completion.md)にまとめた。

Phase 0の22件のテスト成功と54ファイルの準備run snapshot検証を記録済み。Base/Chat各100件（各dev 80/test 20）、前処理golden 30件、手動採点例11件を利用する。Phase 3完了時には全48テスト、両モデル×3 backendの実CLI 6件、79 source filesとruntime source 3,673 filesの監査が成功した。Phase 3までのデータは小規模pilot。4k/8k Tokenizerは学習済みで、両モデルのCPU検証も完了。Phase 4では64 tests、GPU検証checkpointとeager最大安定batch T8K 57 / T4K 64を確認した。Phase 6①②では756M unique train stream tokensの拡張corpus全件監査、WSDの73 GPU checks、全74 tests / skip 0を確認した。50〜100B master全量と完成したBase/Chat重みはまだない。

Pythonは`.python-version`の3.12.7、依存変更は`uv add`、環境再構築は`uv sync --frozen`、実行は`uv run --frozen`で統一する。データ処理時は`--extra data`（PyArrow、datasketch、fsspec、aiohttp）、Tokenizer・モデル検証時は`--extra ml`を指定する。両extraを同時に使う処理では両方を指定する。GPU/CUDA互換性はPhase 4で確認済み。

Phase 0〜5とPhase 6①〜⑤の成果物は各完了記録に実pathを示す。[①②の完了記録](26_phase6_preparation_completion.md)にあるcorpus/shards・WSD検証checkpoint・reportは存在する。本学習の凍結configは[version2](../configs/phase6/base_frozen.json)として検証済み。scaling checkpoint・Base/Chat完成artifactは**今後作成するもの**で、準備検証artifactと区別する。コードは`src/`、設定は`configs/`、検証は`tests/`、実行入口は`scripts/`を基本とする。小さな比較結果・判断記録は`reports/<run_id>/`、大型データ・重みは[外部データ領域](07_environment.md)へ置く。`docs`には仕様、計画、成果物への参照を残す。

別PCで再開する時は[Windows/WSL＋RTX 4090の手順](windows_handoff.md)を入口とする。新規PCではコードと固定Hub成果物を復元して環境を確認する。Phase 5・Phase 6①〜⑤と文書更新のコミットは未pushなので、最新のWindows正本も引き継ぐ。復元済みPCでは完了作業を繰り返さず、③の完了commit `a7d26e1`、④⑤の`93c7d1d`とsource/dataを確認し、本学習の再開指定まで停止する。

各フェーズは、成果物が作られ、完了条件を証拠で確認した時に完了とする。条件を満たさない場合は修正・再比較へ戻り、未達事項を次フェーズへ黙って持ち越さない。現在の凍結予算は⑤の693,666 tokens/sを基準に500M約12分・10B約4時間の純学習算術値。500Mの独立decayと全文dev/400生成を含め約24分、10Bまでの全5枝/評価は約5時間21分。起動/compile/保存/人手確認/実装/修復は別で、日付の締切を保証しない。

## 全体の順序

| Phase | 状態 | 実行環境 | 目的 | フェーズ終了時のゴール | 前提 |
|---:|---|---|---|---|---|
| 0 | 完了 | iMac | 成功条件と実験の契約を固める | 設定・記録・評価仕様を作成し検証済み | [完了記録](16_phase0_completion.md) |
| 1 | 完了 | iMac | 目的に合うデータを追跡可能にする | 小規模Base corpusと会話pilot、独立した評価splitを用意する | [完了記録](17_phase1_completion.md) |
| 2 | 完了・[証拠](18_phase2_completion.md) | iMac | 日本語を小語彙で安定して表現する | 同じsampleで学習した4k/8k Tokenizerが契約を満たす | 1のsample・split |
| 3 | 完了・[証拠](19_phase3_completion.md) | iMac / CPU | 10Mモデルと推論経路を成立させる | 正しいモデル・cache・HF/float GGUF経路を確認する | 2 |
| 4 | 完了・[実機証拠](21_phase4_completion.md) | Windows/WSL＋RTX 4090 | 長時間学習の再現性と実行可能性を確かめる | 保存再開・実shard学習・4090速度と予算を検証した | 1〜3 |
| 5 | 完了 | Windows/WSL・RTX 4090 | 小予算で有望な候補を選ぶ | overfit、10M smoke、100M比較から最大2候補を選ぶ | 4 |
| 6 | 準備①〜⑤・500M完了、1B以降未着手 | Windows/WSL・RTX 4090 | 日本語Baseの能力を段階的に伸ばす | 500M→1B→2B→5B→10Bで評価し、Base v1を固定する | 5、[準備完了証拠](30_phase6_readiness_execution.md) |
| 7 | 未着手 | Windows/WSL・RTX 4090 | Baseを短文雑談モデルへ仕上げる | mid-trainingとSFTの効果を分離し、Chat v1を評価する | 6、1の会話pilot |
| 8 | 未着手 | 学習PC・独立したローカル検証環境 | ローカルで使える成果物を完成させる | Base/Chatと量子化版を独立環境で実行・再現できる | 7、3のexport経路 |
| 9 | 未着手・50Bは条件付き | Windows/WSL・RTX 4090 | 追加学習に継続価値があるか検証する | 20B、条件付き50Bの効果と限界を報告する | 6、追加予算の見積もり |
| 10 | 未着手・後半研究 | ローカル中心、後半にVast.ai並列比較 | baselineを越える追加研究を行う | 共有・蒸留・hybrid・規模比較の採否を証拠で決める | 8、固定したbaseline |

Phase 0〜8を最初の完結した開発系列とする。Phase 9は20Bの評価と、改善継続時のみ50Bへ進む系列。Phase 10は後半研究であり、最初のChat完成を待たせない。

Phase 1の会話pilotは準備済みで、拡張と評価準備をBase学習と並行して進める。Phase 6で10B Baseが成立すればPhase 7へ進め、20B・50BをChat開始の前提にしない。単一4090ではGPU実験を順番に実施し、CPUでのデータ整理・評価準備を並行する。

**確定（実行場所）**: Phase 0〜3はiMacで実施し、Phase 4からWindows/WSL＋RTX 4090へ移行済み。Phase 4のNorm/default eager運用上限はT8K 57 / T4K 64。Phase 6③ではNoNormのreference/math最大45、compiled/math最大53、compiled Flash最大111を検証。最速はFlash＋compile reduce-overhead batch 32、694,521 tokens/sで、容量上限と最高速度を分ける。[高速化完了記録](29_phase6_performance_completion.md)、[移行成果物・確認条件](07_environment.md)

## 高速に完成させる進め方

**確定（優先方針）**: ユーザーは完成までの時間短縮を優先する。Windows/WSLへの切替とPhase 4は完了した。Phase 5の候補選定まで完了し、Phase 6①〜⑤と500M評価が完了・1B前で停止。Phase 3をGPUで最初からやり直すことは移行の前提にしない。

Phase 3の最終検証一式はM1 iMac上で24.62秒。これは実装後の検証時間で、コード作成・修正、Tokenizer学習、runtime初回build、docs更新を含まない。作業全体の約25分と区別し、GPUへの変更で実装時間まで短縮すると見積もらない。[実測report](../reports/phase3/export_parity_report.json)

Phase 4は以下の順で実施済み。新規環境への移行・実装変更時にもこの検証順を使う。すべてのPhase 4完了条件は維持する。

1. **移行・CUDA確認**: GitのコードとGit管理外のTokenizer/pilotを引き継ぎ、hash/ID一致、GPU/driver/PyTorch/BF16を確認する。Macのnative binaryや仮想環境はコピーしない。
2. **最小の学習経路**: 検証済みモデルを使い、AdamW/BF16、uint16 shard、本文NLL/BPB・生成評価、checkpointを実装する。まず小batchでfiniteな1 stepまで成立させる。
3. **保存再開の検証**: 同じ環境で連続200 stepsと100→保存→再開100 stepsを比較し、消費token列・loss・weightsを確認する。
4. **速度と最大batchの実測**: batchを倍増して境界を見つけ、中間値で最大安定値を測る。compile初回と定常速度、backend、syntheticと実shardのI/O、評価・保存時のVRAMも記録する。最大安定batchと最高速度のbatchは両方残す。

変更した箇所と関連gateを検証し、関係のないPhase 1取得・Tokenizer再学習・CPU GGUF全検証を繰り返さない。artifactを変更した場合、移行先で数値差が出た場合、学習済みモデルを配布する場合は対応する検証を再実行する。

最初のChat完成に必要なPhase 0〜8を優先し、20B/条件付き50B、Muon等の追加比較、hybrid、クラウド並列研究はbaseline成立後に進める。小探索では主要因を一つずつ比較し、総当たりを前提にしない。データは次の段階で使う量から準備し、master corpus全量取得を学習開始の条件にしない。

**時間見積もり**: 「学習開始まで1〜2日、初版Chatまで1〜3週間」は会話中の粗い仮見積もりで、確定scheduleへ採用しない。実装作業時間とGPU計算時間を別々に記録する。変更後の採用設定で検証済みのPhase 6③のtokens/secから`残りtokens / tokens/sec + 評価・保存・比較runの時間`を計算し、段階ごとに更新する。品質の修正が必要な場合は追加実験を別に見積もる。

## Phase 0: 成功条件・環境・実験管理

**状態**: 完了。詳細な実path・検証範囲は[完了記録](16_phase0_completion.md)と[完了監査](../reports/phase0/completion_audit.json)を参照する。以下は実施した内容で、Windowsの実機確認はPhase 4へ残す。

実施時点のhashとsnapshotは履歴として保存する。計画やREADMEの更新で現fileが変わった場合も、過去runのsnapshotと監査を上書きしない。Tokenizer/data入力のartifact hashは作成前のため`null`で、各フェーズの完成後に実fileを記録する。

**目的**: 学習できたことと、狙った短文対話が成立したことを区別して判定できるようにする。

**ゴール**: runを再構築できる記録形式と、結果を見る前に固定した評価仕様がある。

作業:

- リポジトリ骨格、依存version固定、run ID、artifact naming、seed管理、config schemaを作る。
- iMac側の環境を記録し、Windows/WSL用の依存設定と移行手順を用意する。WSL 3.xの実導入version、GPU、driver、OS、PyTorch/CUDA、ストレージの実機確認は切替時に行う。
- Base評価、Chat評価、tokenizer契約、数値誤差、停止ID、公開対象のデータbucketを仕様化する。
- Base completionとChat各100件の独自prompt suiteを作成し、各dev 80件・最終test 20件へ分けた。Chatは挨拶、感情応答、質問返し、訂正、2〜数ターンの文脈を含む。

**成果物（作成済み）**: [experiment schema](../schemas/experiment_schema.json)、[iMac環境記録](../reports/phase0/environment.json)、[評価仕様](evaluation_protocol.md)、[固定promptとsplit](../eval/README.md)、[実行入口](../scripts/experiment.py)、`pyproject.toml`・`uv.lock`・`.python-version`。

**完了条件**: 同じrun IDからcode commit、config、依存環境、データ/Tokenizer hashを特定できる。Chat rubric、BPB分母、generation設定、dev/testの用途が明記される。評価例を手で採点し、ルールの曖昧さを修正する。

**次へ進む判断**: iMac上の設計・データpilot・Tokenizer・CPU実装検証は進められる。4090の実機記録は移行時のgateとし、Phase 4のGPU検証と学習開始前に確認する。

## Phase 1: データの小規模pilotと評価split

**状態**: 完了。[実施結果・実path・限界](17_phase1_completion.md)、[全件検証](../reports/phase1/verification.json)、[再生成一致](../reports/phase1/reproducibility.json)を参照する。Phase 0の共通前処理を使い、[処理コード](../src/jmicro/data.py)と[実行入口](../scripts/prepare_phase1.py)を作成した。

**目的**: 日本語短文・雑談へ容量を使い、出所不明の混合や評価漏洩を避ける。

**ゴール**: 100M探索まで使う小規模corpusと、Chatに使える会話候補の実量・品質が分かる。

取得に使用したsource:

| source | 確認したrevision・条件 | pilotでの扱い |
|---|---|---|
| FineWeb2 Edu Japanese / `small_tokens_cleaned` | revision `180ca004c6a89b590daaad86cb062a07a5353c69`。配布READMEにODC-By v1.0とCommon Crawl利用条件を記載 | 小規模Web pilotに採用。READMEで先頭0〜9,999行と10,000〜19,999行の重複を告知しているため、先頭10,000行を避け、取得後にも重複を検査する |
| RealPersonaChat | revision `28d0b6b3865b29cabc26c230a2db37cdf315e937`。LICENSEはCC BY-SA 4.0 | 会話pilotに採用。Webとは別bucketで出所・条件を記録し、persona・人口統計metadataは学習入力へ含めない |

根拠: [FineWeb2 Edu Japaneseの固定revision README](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese/blob/180ca004c6a89b590daaad86cb062a07a5353c69/README.md)、[RealPersonaChatの固定revision LICENSE](https://github.com/nu-dialogue/real-persona-chat/blob/28d0b6b3865b29cabc26c230a2db37cdf315e937/LICENSE)。取得済みmetadata・形式確認用previewは`data/phase1/source_metadata/`に保存した（Git管理外）。調査metadataは処理入力へ流用せず、固定revision原fileを取得してpilotとsplitを作成した。証拠のURL・revision・取得file hashはsource台帳へ固定済み。

**実施した取得範囲**: [config](../configs/data/pilot.json)へschema、保存先、容量上限、選択方法を固定し、Web 20,000文書、会話3,000対話を取得した。採用はWeb 19,998文書、会話3,000対話、合計42,647,826 canonical UTF-8 bytes。取得数とfilter後の採用数を分け、unique量・反復回数・実際の学習tokensを別に報告する。100M tokensの探索に不足する場合は取得範囲の拡張または明示した反復で対応し、unique 100M tokensを取得済みとは扱わない。

実施項目:

1. source台帳とdocument/dialogue manifestのschemaを作り、source/subset/revision・利用条件・raw/canonical hash・cluster・splitを記録できるようにする。
2. 確認済みrevisionを台帳へ固定し、少量sampleの取得範囲・容量上限・保存先を決めて本文を取得する。viewer previewのrevisionと固定revisionを混同しない。巨大データ全量の取得は先行しない。
3. sampleを共通前処理、filter、dedupへ通し、train/dev/testを固定する。Phase 0の`eval/`はモデルの固定生成suiteであり、新しいcorpus splitとは別管理する。
4. trainだけからTokenizer学習sampleを選ぶ。4k/8kで同じdocument集合・順序・hashを使えるようにする。
5. 使用条件を満たす短文会話候補で1k〜10k対話のpilotを作り、件数・応答長・turn数・品質をreportする。教師tokensはPhase 2で実計数する。

作業:

- [データ設計](05_dataset.md)に従ってsource/subset/revision、利用条件、raw/canonical hash、品質、splitを持つmanifestを作る。未確認sourceは採用を保留する。
- FineWeb2 Edu Japanese等から小subsetを取り、弱い前処理、言語・品質filter、日本語向けexact/near/cross-dataset dedupをpilotする。
- duplicate cluster単位でtrain/dev/testを分離してからTokenizer学習sampleを選ぶ。
- 使用条件を満たす候補から1k〜10k対話のpilotを作る。speakerの向き、personaの扱い、tree復元、window化前のsplitを確認する。
- domain別bytes、短文比率、会話長、品質のsample目視を記録する。会話の定型挨拶を文書重複と同じ基準で一律削除しない。

**成果物（作成済み）**: `data/phase1/processed/`の`dataset_manifest.parquet`、`split_manifest.json`、`corpus.jsonl`、`tokenizer_sample.jsonl`。data/dialogue report・レビュー・検証・再生成比較は`reports/phase1/`。[詳細・checksum・再生成手順](17_phase1_completion.md)

**完了条件**: 任意の採用文書・対話をsourceとsplitへ追跡できる。既知重複とtrain/eval間の検出重複を除外し、未検出の限界も記録する。対話件数、unique bytes、応答文字数、turn数の分布が分かる。1024-token内に収まる割合と教師token数はPhase 2で計測・追記する。

**次へ進む判断**: 会話候補が不足する場合は独自会話例でmask/評価の開発を進めつつ候補を追加する。量の不足を、同じ少数対話を反復した見かけのtokensで解決したことにしない。

## Phase 2: 4k/8k Tokenizerと会話形式

**状態**: 完了。[実施結果・artifact・再現手順](18_phase2_completion.md)。同一sampleで全6coverage候補が合格し、両語彙で0.9995を採用。外部codecのgolden・全corpus round-tripと会話token量を実計数した。

**目的**: 小語彙でも日本語・記号を扱い、学習とローカル推論で同じID列を使う。

**ゴール**: 語彙4096/8192の二つのSentencePiece Unigram + byte fallback artifactと、共通の入出力契約がある。

作業:

- 同じtrain sampleでcoverage候補を比較し、必須文字・256 byte pieces・8特殊tokenを含む予算を確認する。
- 正規化、空白、改行、タブ、結合文字、顔文字、未知文字のgolden例を固定する。
- role/EOTを構造IDとして挿入し、本文中の同じ文字列表記と区別する。学習後の語彙追加を避ける。
- domain別chars/token、bytes/token、fallback率、context超過率と会話の総/教師tokensを測る。

**成果物**: 4k/8kの`tokenizer.model`、設定・sample hash、`special_tokens.json`、`tokenizer_contract_report.json`、`tokenizer_comparison.json`。

**完了条件**: piece数と特殊IDが期待値と一致し、golden例が定義したcanonical textへround-tripする。全byte piecesと異常入力を検証する。同じartifactでencode結果が再現でき、再学習時の一致範囲も記録される。

**次へ進む判断**: 圧縮率だけで勝者を決めず、両候補をPhase 5へ渡す。4kが予算内で成立しない場合はcoverage/前処理を再検討し、語彙数を黙って変更しない。[詳細仕様](13_tokenizer_dialogue_data_research.md)

## Phase 3: モデル・cache・学習前export

**状態**: 完了。[実施結果・artifact・再現手順](19_phase3_completion.md)。両モデルの実parameter数・forward/backward・1024までのcache、公式HF・native float GGUF、Q8/Q4の読込生成を検証。内蔵Tokenizerに不一致があるため外部SentencePiece経路を採用した。

**目的**: 10M予算と正しい因果生成を満たし、長期学習後に推論形式で詰まるのを防ぐ。

**ゴール**: T8K/T4Kがforward/backward・cache生成・保存読込でき、配布経路の計算とTokenizerを検証できる。

作業:

- RMSNorm、RoPE、GQA、head間gain共有QK-Norm、SwiGLU、tied embeddingを実装する。
- parameter count、未来参照遮断、GQA mapping、padding、finite gradientを検証する。
- prefill、1-token decode、chunk decode、長さの違うcacheで全系列logitsとの一致を検証する。
- ランダム重みをHF参照モデル、float GGUFへ写し、同じ入力IDsでlogits/cacheを比較する。
- 内蔵Tokenizerのgolden parityとEOT停止を検証する。不一致なら外部SentencePieceでencode/decodeする呼び出し経路を実装する。
- Q8/Q4候補で読込・生成、tensor別量子化型、FFN幅576/640でのfallbackと実容量を確認する。

**成果物**: T4K/T8K config、`model_contract_report.json`、`export_parity_report.json`、実行可能な推論入口。

**完了条件**: 提案仕様のQK-NormありでT8K=9,772,800、T4K=10,002,816 parameters。cache/因果性の検証が通り、floatの数値差が事前定義した許容値内。選んだ配布経路で学習時と同じTokenizer契約を再現できる。

**次へ進む判断**: 外部SentencePiece経路ならその依存も配布計画へ含める。汎用GGUF CLIへの互換性は別項目として記録する。ランダム重みの量子化成功は会話品質の成功を意味しない。[モデル仕様](12_training_implementation_research.md)、[export仕様](14_evaluation_deployment_research.md)

## Phase 4: 学習器・shard・再開・4090 benchmark

**状態**: 2026-10-03に完了。WSL 3.0.1.0 / Ubuntu WSL 2 / RTX 4090でCUDA/BF16確認と64 tests / skip 0、両モデルの200 vs 100+100完全一致、全dev・固定生成suite、最大batch・backend/compile・予算を実測・監査した。[完了記録と測定の制約](21_phase4_completion.md)を参照する。Phase 5も[完了](23_phase5_completion.md)し、Phase 6①〜⑤と500M評価が完了・1B前で停止。

**目的**: 長期runを失わず、実際の計算・ストレージ予算に収める。

**ゴール**: 実shardでの学習・中断再開が成立し、以降の実験時間を実測から見積もれる。

作業:

- `uint16` shard、document index、checksum、mmap loader、決定的shuffle/mixture samplerを作る。
- GPU実機検証の前にWindows PCのWSL 3.x/Linuxへ切り替え、同じcommit/config、Tokenizer、sample、hashを引き継いでCUDA動作を確認する。
- AdamW、FP32 parameter + BF16 autocastを基準にloss、gradient accumulation、schedulerを実装する。
- model/optimizer/scheduler/RNG、消費済みデータ位置、tokens/steps、全hashを保存する。optimizer更新境界で保存し、一時fileからのatomic renameを行う。
- Phase 0の準備run記録を基に、学習runの開始/完了/失敗、checkpoint、metricsのschemaと台帳を追加する。準備runの`tokens_seen=0`を学習結果として流用しない。
- Baseの本文NLL取得、window/strideの採点、BPBと生成suiteの実行を実装する。共通bytes・本文を一度だけ採点することを検証し、Phase 5の比較前に評価runnerを使えるようにする。
- 連続200 stepsと100 steps→保存→再開100 stepsを同一環境で比較する。
- T4K/T8Kのsynthetic/実shardでmicro batchを最大安定値まで増やし、compile、backend、data wait、peak VRAM、保存時間を測る。micro batchとeffective batchを区別する。

**成果物**: 実機`environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`、復元可能checkpoint。

**完了条件**: Windows/WSLへ移行済みで、CUDA動作と引継ぎartifactの一致を確認する。再開前後の消費token列が一致し、loss/weightsが同一環境で許容誤差内。累積lossの正規化、shard境界、評価によるRNG干渉を検証済み。BPB runnerの本文一度採点・共通bytes分母と固定生成suiteの実行を確認する。compile初回と定常速度を分け、実shardで運用できる最大安定batchと速度が分かる。

**次へ進む判断**: `予定tokens / 実測tokens/sec + 評価・保存・停止・分岐の時間`で100M/1B/10B/20B/50Bを見積もる。raw、一時領域、4k/8k shards、checkpointの容量を合算する。予算外ならまずbatch/I/O/探索本数を調整し、実験条件を台帳へ記録する。

## Phase 5: overfit・10M smoke・100M比較

**状態**: 2026-10-03に完了。4本の100Mと補助予算を評価し、T4K / NoQK-Norm / LR 0.002を1候補に選定。全68 tests / skip 0、CUDA厳密resumeと独立監査が成功。品質の未達も[完了記録](23_phase5_completion.md)へ保存し、Phase 6①〜⑤と500M評価が完了・1B前で停止。

**目的**: 実装不備を小予算で見つけ、長期学習へ渡す候補を根拠で選ぶ。

**ゴール**: 100M時点で発散しない候補を最大2つ選べる。

作業:

- 小データ100件のoverfitでloss低下と学習例の再現を確認し、別runで10M-token smokeを行う。
- 100MでT4K/T8Kを比較する。次にQK-Norm有無、LR、必要ならMuon+AdamWを、一度に一つの主要因だけ変えて比較する。全組合せの総当たりは前提にしない。
- 同じvalidation文書のBPB、共通短文window、生成失敗、実時間、処理bytes、更新回数を保存する。
- 同一tokens、同一学習bytes、同一GPU時間の条件を区別する。補助比較は対応するcheckpointまたは別runで行い、条件が揃わない結果へ同じラベルを付けない。

**成果物**: `smoke_report.json`、`tokenizer_model_comparison.json`、候補config、`candidate_selection.md`。

**完了条件**: finite loss/gradient、保存再開、EOS生成の検証が通る。BPBの改善と失敗率の推移を比較でき、候補選定理由・棄却理由を記録する。100Mで自然な雑談が完成することは要求しない。

**次へ進む判断**: 候補がすべて発散・悪化する場合はデータ、mask、LR、batchを切り分けてPhase 2〜4へ戻る。BPB差が小さい場合は速度・fallback・生成失敗・推論互換性を含めて最大2候補を残す。

## Phase 6: 500M〜10B Base v1

**状態**: 準備①〜⑤と500M stable/decay/評価は完了し、1B前で停止。756M unique train stream tokensのcorpus全監査とWSD stable/decayのCUDA全state再開一致を確認した。[準備完了記録](26_phase6_preparation_completion.md)。③はFlash＋compile batch 32、694,521 tokens/s、独立1286 checks・cold再開26 checks・79 testsを通過し、証拠は`a7d26e1`へcommit済み。④の生成/全文dev/CPU精度profileによる学習済み変換と⑤のLR3候補/厳密cold再開/設定version2凍結も`93c7d1d`で完了した。[高速化完了記録](29_phase6_performance_completion.md)。今後は[段階評価/gate](24_phase6_plan.md)と[残りの実行計画](27_phase6_remaining_plan.md)に沿い、ユーザーの再開指定後に凍結条件を照合して500Mの新規Base学習を始める。

**目的**: 約10Mで日本語短文生成がどこまで成立するかを測り、Chatの土台を作る。

次回の一区切りは[拡張データでの500M学習・評価計画](27_phase6_remaining_plan.md#次回の一区切り-拡張データで500mを学習評価する)。500M stableと独立decay、固定dev比較・report・commitまでを提案し、そこで停止して1B以降の判断を残す。今回は計画作成のみで本学習を開始しない。

**ゴール**: 5Bまでに本命1モデルへ集約し、10Bの`JMicro-10M-Base-v1`と固定評価を残す。

| 累積tokens | 目的・判断 | 残すもの |
|---:|---|---|
| 500M | 初期改善と反復悪化の確認 | checkpoint、BPB/生成/速度 |
| 1B | 日本語生成の立ち上がり、候補最大2つ | 比較表、候補更新理由 |
| 2B | 過去355M/約2B経験との観察点整理 | 規模・Tokenizer・データ差を明記した記録 |
| 5B | 本命1つの決定 | 選定reportと継続config |
| 10B | Base v1の固定評価 | weights、Tokenizer、model card、全評価 |

作業:

- pilotで検証済みの処理を拡張し、50〜100B master corpus候補を段階的に構築する。実取得/利用可能量と独自Tokenizerのunique量を報告し、候補目標量と混同しない。
- 各段階に必要なshardsから用意し、未使用全量の処理を10B開始の前提にしない。
- BPB、短文品質、反復、EOS、Unicode、追加GPU時間を段階ごとに記録する。
- 固定mixtureのscaling系列を残す。目的に合わせたmixture変更は別条件として記録する。
- Phase 5でWSDを採用し、Phase 6②でstable/decayの実装・CUDA全state再開/分岐完全一致を確認済み。本学習のbatch/backend/数値配分は[version2](../configs/phase6/base_frozen.json)へ凍結済み。継続stable枝と評価decay枝を区別して追加computeも計上する。20B/50Bへのstable予算延長forkは未実装で、通常resumeでは予算を変更しない。

**成果物**: 段階checkpoint、`base_scaling_report.json`、`base_v1_evaluation.md`、継続用checkpoint、master corpus manifest。

**完了条件**: 本命の10B checkpointを再構築・再開でき、固定suiteとheld-out corpusの結果がある。短文の文法・関連性と破綻例を人手で確認し、[品質目標](#品質目標と判断ルール)の達成/未達を明示する。過去モデルのartifactがない場合は直接比較を未実施と明記する。

**次へ進む判断**: Baseの日本語生成が成立すればPhase 7へ進む。成立しない場合は量だけを増やさず、日常短文mixture等の対照実験を行う。修正後も未達なら容量・データの限界として報告し、成功扱いにしない。

## Phase 7: Dialogue mid-trainingとAssistant-only SFT

**目的**: 流暢な続きを生成するBaseから、入力に関連した短い応答で会話を続けるChatへ移す。

**ゴール**: 文法・関連性・2〜数ターンの文脈・停止を評価した`JMicro-10M-Chat-v1`を作る。

作業:

- Phase 1の会話pilotを拡張し、sourceごとのunique対話/bytes/総tokens/Assistant教師tokens/反復回数を固定する。
- Dialogue mid-trainingのmixture、loss範囲、LR、pilot予算と拡張上限を開始前にconfigへ記録する。
- 主系列はBase→mid-training→SFT。小規模なBase→SFT対照を残し、mid-trainingの効果を分離する。
- role metadataからAssistant本文+EOTの教師maskを作る。shift、PAD、教師0件、長い対話の古い完了turn切り捨てを検証する。
- SFTの累積総系列10M→30M→100M tokensを候補とし、毎段階devで比較する。教師token数とunique量は別記録し、悪化時は100Mまで強制継続しない。
- Base、mid-training後、SFT後を同じ固定prompt/seedで比較する。greedyと複数seed sampling、人手rubricと自動失敗率を分ける。
- Phase 0の固定履歴suiteに加え、モデル生成を履歴へ戻す2〜数ターンのrolloutと自動失敗flagを実装する。モデル名を伏せた人手評価と評価者一致率を記録する。

**成果物**: 会話manifest、`assistant_mask_report.json`、各段階checkpoint、`chat_ablation_report.json`、`chat_v1_evaluation.md`。

**完了条件**: mask/停止の検証が通り、独立した対話splitで評価済み。採用checkpointがdev上で関連性・文脈を改善し、反復・役割混同・空応答・停止失敗・Base流暢性の退行を報告する。最後に未使用testで品質目標を判定する。

**次へ進む判断**: 最良checkpointを選びPhase 8へ。未達なら応答長/品質/mixture/LR/反復回数を一要因ずつ見直す。蒸留を使う場合はcorpus-only baselineと別系列にする。

## Phase 8: 量子化・ローカル実行・再現手順

**目的**: 学習結果を手元で使える形にし、容量と品質の実際のtradeoffを示す。

**ゴール**: Base/Chatのfloat版と採用量子化版を、学習環境以外でも手順から起動できる。

作業:

- 学習済み重みでPhase 3のHF/float GGUF parityとcache/停止を再実行する。
- Q8とQ4候補を比較し、tensor別実型、file容量、Tokenizer込み全artifact、RSS、cacheメモリを測る。
- 対象CPU/OS/threadsを明記し、load、初回token時間、prefill/decode、応答総時間のp50/p95を測る。context1024は生成分も含めて管理する。
- floatとの差をBPB、人手関連性/文脈、Unicode、反復、role/停止で確認する。
- model card、採用source一覧、帰属、既知の限界、hash、runtime commit、量子化設定、実行/再現コマンドを揃える。

**成果物**: Base/Chat artifacts、`quantization_report.json`、`local_inference_report.json`、`reproduction_guide.md`、配布manifest。

**完了条件**: 独立環境でBase completionと2〜数ターンのChatが動く。学習時と同じencode/decode、EOT/EOS停止が成立し、量子化の退行を品質条件内に収める。全容量・速度・必要依存を実測値として提示する。

**次へ進む判断**: Q4が品質を満たさなければQ8/混合精度も比較する。5〜10MB級へ収まらない場合はサイズ目標未達を明記し、形式/precisionの追加検証を残す。artifactを用意したことと品質・容量目標達成を区別する。外部公開・Hub uploadはこの文書作成では実行しない。

## Phase 9: 20Bと条件付き50Bのscaling

**目的**: 固定10Mモデルへ追加学習する価値と、容量/データ反復の限界を確認する。

**ゴール**: 10B対20Bの差を測ってBase v2を評価し、50Bへの進行/停止を根拠で決める。

作業:

- stable予算延長の明示forkと履歴・全state検証を実装してから継続用checkpointで20Bへ進み、固定mixture・同じ評価条件で10Bと比較する。通常resumeで終端budgetを変更しない。
- document単位のpaired bootstrapでBPB差と95%信頼区間を記録し、短文品質、失敗率、uniqueデータ露出と追加GPU時間を併記する。
- 50Bは20Bでも改善継続があり、生成失敗が悪化せず、追加時間/ストレージが予算内の場合のみ進む。
- 新Baseが有望なら同じChat手順を適用してv1と比較し、Phase 8の学習済みexport/量子化評価も再実行する。

**成果物**: `base_v2_evaluation.md`、`scaling_extension_decision.md`、実施した場合の50B checkpointと限界report。

**完了条件**: 20Bの比較と50B Go/No-Goを記録する。50Bを実施した場合は評価まで完了する。実施しない判断にも改善量、信頼区間、失敗率、予算の証拠を付ける。

**次へ進む判断**: 小さい改善しか残らない/悪化する場合は停止し、データ適合性またはPhase 10の比較へ移る。decay済み評価枝とstable継続枝の履歴を混同しない。

## Phase 10: 追加研究とVast.ai並列比較

**目的**: 完成したTransformer baselineと比較して、能力密度・計算効率をさらに改善する。

**ゴール**: 変更ごとに同じ目的・評価条件で採用/棄却を判断できる。

優先順はLayer Sharing（12 unique/24 logical）、teacher応答テキスト蒸留、ReLU²、Mamba2+Attention、Conv+Attention、5M/10M/25M/50M/100M規模比較。各実験では「改善したいmetric、parameter/compute予算、同一条件、採用基準」を先に記録する。異なるTokenizer間のlogitsをindexで直接KL比較しない。

Vast.aiはローカルで検証済みの独立runを並列化する後半用途に限定する。利用時の価格で再見積もりし、既存方針の上限$1,000に対して実験別計算時間・storage・失敗時費用を計上する。この計画作成で課金jobを開始しない。

**成果物**: 追加研究proposal、対照run、`research_comparison.md`、費用/速度/品質の台帳。

**完了条件**: 実施した各変更をbaselineと比較し、採否・限界を記録する。採用案は再現性、Chat評価、export、量子化まで再検証する。候補全部の実施を最初のBase/Chat完成条件にはしない。

**次へ進む判断**: 品質または速度が事前の採用基準を満たす変更だけを次の比較へ進める。改善が不明確な変更は結果を保存して保留し、追加computeで得られる情報と費用から再実験の優先度を決める。

## 品質目標と判断ルール

技術的完了と能力目標を別に管理する。Phase 8までのartifact・検証が揃っても、以下が未達なら「目的を達成した」とは記載せず、未達metricと次の対照実験を残す。

以下の数値はPhase 5の100M候補の結果を見る前に、初期提案を維持して**凍結済み**。10Mで達成できると実証した値ではない。Phase 0でsuiteと採点例を定め、Phase 5のdev/pilot評価では未達もそのまま記録する。変更理由と旧値を記録し、最終testを見て閾値を下げない。量子化の退行幅はfloat dev評価後、量子化候補選定前に別途固定する。[凍結の記録](22_phase5_plan.md#公平な評価と候補選定)

| 目的 | 判定方法・初期目標 | 判定するフェーズ |
|---|---|---|
| 日本語短文生成 | Base completionの文法2/2が70%以上。文字/記号の破綻と反復も別集計 | 6 |
| 入力に関連する短い雑談 | Chatの文法・関連性が両方2/2の応答が70%以上。文字数分布も併記 | 7 |
| 2〜数ターンの文脈維持 | 2〜4ターンsuiteで直前の条件/訂正を保持し、文脈2/2が60%以上 | 7 |
| 会話の停止と役割 | 停止成功95%以上、空応答5%以下、役割漏出1%以下、Unicode破綻は固定suiteで0件 | 7・8 |
| 量子化して使える | 全artifact容量5〜10MB級を目標に、floatとのBPB/品質/失敗率差を報告。許容退行幅はfloat dev評価後、量子化候補選定前に固定 | 8 |
| 長期学習の継続価値 | BPB改善幅（10B BPB − 20B BPB）の95%信頼区間の下限が0を越え、生成失敗に重大退行がなく追加予算内なら50B候補 | 9 |

停止等の失敗率はgeneration抑制設定を併記し、ID列で測る。人手評価はモデル名を伏せ、文法/関連性/文脈を各0/1/2で採点する。率は分母とsample数を付け、全体だけでなくcategory別も報告する。関連性が伸びても反復が増える等の重大退行は採用判断へ反映する。

品質条件はdevで選定し、独立testで最終確認する。testで未達なら結果を報告し、次の改訂では新たな未使用testを用意する。[評価の詳細](14_evaluation_deployment_research.md)

## 横断して残す記録と最初の着手順

全runでcode commit、config、依存version、Tokenizer/data hash、seed、tokens seen、unique docs/bytes/tokens、更新数、micro/effective batch、wall time、失敗理由を残す。SFTでは総系列tokensとAssistant教師tokens、WSDでは分岐ごとの履歴を分ける。比較する条件を変えたら別run IDにする。

Phase 0〜4の骨格・データpilot・Tokenizer・両モデル/cache/export・Windows/WSL移行・学習器・評価・保存再開・実機速度は完了済み。Phase 5のoverfit/smoke・4本の100M比較・候補選定が完了し、Phase 6①〜⑤と500M評価が完了・1B前で停止。巨大コーパス全量取得、50B開始、追加hybridを先行しない。

具体的な着手checklistは[次の実装タスク](10_next_steps.md)、各技術判断の根拠と実測待ち項目は[追加調査](11_technical_research_gaps.md)を参照する。
`````

## docs/24_phase6_plan.md

UTF8 LF SHA256: d7a2fdcb040758b98f2799a5ffbf08a36088f75094856ca1086dc0e26ea27e44

`````markdown
# Phase 6: Base本学習の準備と段階評価計画

更新: 2026-10-03。[Phase 5](23_phase5_completion.md)とPhase 6①②③は完了。ユーザーが残り計画の最初の2項目を再開したため、④生成/変換→⑤設定・予算凍結を[固定実行計画](30_phase6_readiness_execution.md)に沿って検証済み。①②は[完了証拠](26_phase6_preparation_completion.md)、③は`a7d26e1`と[完了記録](29_phase6_performance_completion.md)を参照。④⑤は`93c7d1d`へcommit済み。現在は本学習前で停止しており、500M以上の本学習は開始しない。

## 目的と出発点

拡張した日本語train corpusで約10Mモデルをスクラッチ学習し、短文生成を測定した`JMicro-10M-Base-v1`を残す。500M→1B→2B→5B→10Bで評価し、データ反復・能力・追加GPU時間を根拠に継続を判断する。10Bまで到達したことと品質目標の達成を分ける。Chat学習はPhase 7で行う。

現在の候補は **T4K / QK-Normなし / AdamW / LR 0.002**。語彙4,096、hidden 256、13層、FFN 640、4Q/2KV、context 1024、tied embedding、10,001,152 parameters。[候補configと実checkpoint](../reports/phase5/candidate_configs.json)、[採否理由](../reports/phase5/candidate_selection_review.md)を参照する。RMSNormとRoPEは維持し、Q/Kのhead次元Normだけを省略する。

Phase 5のdev BPBは1.221443、定常速度121,139 tokens/s。これはpilot反復・math / batch 8の実測。greedy EOS0/80、反復54/80、sampling Unicode破綻2/240で品質目標は未達。NoNormのHF/Llama・GGUF/Llama adapterは実装済みで、3 backendの生成IDs・EOS/EOT停止は成功したが、学習済み1024系列はstock FP32で未合格だった。CPU精度profileの実推論へ修復し、元の全12比較と実CLI監査149 checksが成功。NormありT4Kの対照と過去reportを保持する。[今回の診断](30_phase6_readiness_execution.md)。

## 開始前に揃える条件

この表のgate 1〜7は検証項目で、作業区分①〜⑤と同じ番号ではない。①はgate 2、②はgate 3/4と準備runの永続化、③はgate 5と変更後のgate 4、④はgate 6、⑤はgate 7に対応する。

| gate | 作業 | 現在の状態 | 完了の証拠・次回の条件 |
|---:|---|---|---|
| 1 | 実行状態・成果物の確認 | ①②③終了時に確認済み、各job前に再確認 | 既存process/job/lock、公開Tokenizer hash、選択config、checkpoint、core sourceを照合。重複GPU jobを起動しない。 |
| 2 | 拡張corpus・shard化 | ①完了 | 756,087,912 unique train stream tokens、Web 100%、dev/test分離。source/revision/条件・取得上限・全raw/cluster/shard監査と予定反復を[完了記録](26_phase6_preparation_completion.md)に保存。 |
| 3 | 必要なtrainer機能 | ②のWSD完了、mixture未実装 | stable/decay CLIは実装済み。初期Web単一sourceはmixture不要。必要時は明示変更系列として実装・検証し、window/教師maskと累積loss契約を維持する。 |
| 4 | 正確な再開・分岐 | ②③に加え、④⑤変更後sourceの採用設定も完全一致 | stable400 vs200+200・decay100 vs50+50、cold200→400の全state/履歴・親不変性・元継続を実GPU検証、独立106 checks成功。source変更後は再検証する。 |
| 5 | 速度・最大安定batch | ③完了（独立1286 checks・cold26 checks） | [完了記録](29_phase6_performance_completion.md)。NoNorm/拡張shard/WSDで実演算・cache分離、有限値、厳密再開/分岐、6設定の3×200更新・評価/saveを通過。最速Flash/compile batch 32=694,521 tokens/s、最大111・112 OOM。 |
| 6 | 生成・変換課題 | ④検証済み、400生成/全文dev・CPU精度profileの全12数値比較成功 | [固定条件と途中結果](30_phase6_readiness_execution.md)。生成ids・実argmax停止は成功、長系列のTorch/HF/native数値差はCPU精度profileで解消。stockの失敗を保持。許容誤差・入力・比較を削って完了扱いにしない。 |
| 7 | 本学習設定・予算・永続実行 | ⑤version2へ凍結済み、本学習前で停止 | 3 LR各2,000＋100 decayから0.002を採用。全state/履歴・cold再開が一致し、[本設定](../configs/phase6/base_frozen.json)と[実CLI/復旧計画](../reports/phase6/base_launch_plan.json)を保存。CPU精度profileの変換gateも通過し`launch_enabled=true`。旧false設定と拒否証拠を保持し、今回は本学習を起動しない。 |

全量50〜100Bの取得を最初の500M開始条件にしない。各段階に必要な取得範囲を先に決める。unique量が予算より少なければ反復倍率を明記し、同じpilotの反復を新規データのscalingと呼ばない。拡張dataでのBPBとPhase 5のpilot BPBは母集団が違うため、そのまま数値差を改善量にしない。

## Scheduler・batch・継続の扱い

長期系列には実装済みのWSD（warmup→stable→decay）を採用する。stable checkpointを継続の正本とし、各評価点のdecay枝は独立runとして保存する。枝ごとにtokens、更新数、GPU時間、source/config/dataと分岐元を記録する。⑤でstable終端予算を先に凍結し、その範囲内の観測点を区切って継続する。終了したdecay枝をstableの履歴として扱わない。

`--branch-from`はdecay専用で、stable予算延長forkは未実装。通常resumeはbudget/source/data変更を拒否する。Phase 9の20B/50B延長や追加corpus/mixtureには、明示forkの履歴と全state検証を先に実装する。新corpusで現在のPhase 6 dev/testを保護する入力・provenanceも未実装として残す。[実装上の残り](27_phase6_remaining_plan.md)

Phase 5の100M終端は凍結cosineの比較結果であり、総step数だけを変更して本系列へ延長しない。選択するのはarchitecture/Tokenizer/LRで、拡張train corpusの本系列は新規初期化する。batchを増やすと更新数と最適化条件が変わるため、LR 0.002を無条件に最適値としない。採用batchで小予算の安定性・学習曲線を確認してから本設定を固定する。

WSD stable/decayは実装・CUDA全state再開一致を検証済み。複数source mixtureは未実装。NoNorm HF/GGUF adapterは実装済み、学習済み長系列の数値parityはCPU精度profileで検証済み。拡張sourceは756M unique train stream tokens、初期配合はWeb 100%。長期設定はversion2へ凍結済みで、本学習前で停止。学習後export/量子化の正式なparity・品質検証はPhase 8の必須条件として維持する。

`configs/training/baseline.json`は初期の提案templateで、train CLIは自動読込しない。Phase 5の実行条件は凍結済みの`configs/phase5/plan.json`、候補の実configは上記reportを正とする。Phase 6のruntime configはgate通過後に別途作成し、初期templateのbatch-selection phaseやscheduler候補を本学習の確定値として流用しない。

## 段階評価と継続・停止判断

| 累積stable系列の観測点 | 目的 | 判断と保存 |
|---:|---|---|
| 500M | 新corpusでの初期改善・反復・停止を確認 | dev BPB、同じ固定80 prompt×5条件、生成ID/失敗率、unique量/反復、実時間。発散・非有限・再開不一致なら停止して修復。失敗率が悪化すれば原因を調べる。 |
| 1B | 日本語短文の立ち上がり | 同じdev文書のBPB差とpaired CI、文法rubric、文字数分布を保存。原則は現在の1候補を継続。対照を追加する必要が生じた場合だけ理由・予算を固定し、候補は最大2つ。 |
| 2B | 継続の価値と過去経験との比較点 | 同一条件の継続価値を測る。過去355M modelのartifactが取得できなければ直接比較は未実施と明記する。 |
| 5B | 本命構成と残り予算を判断 | 本命1構成、品質の到達/未達、追加10Bまでの時間/容量を保存。量だけを増やして解決しない場合は日常短文mixture等を別対照として比較する。 |
| 10B | Base v1の固定評価・成果物 | 再構築・再開可能なcheckpoint、model config、Tokenizer/data/source hash、model card、固定評価と失敗例を保存。目標未達なら未達と報告する。 |

観測点の評価checkpointはWSD decay枝とし、実際の枝tokensを併記する。stable系列の予算と枝の追加computeを混同しない。devで選定し、最終評価用testは選定に使わない。Base文法70%以上等の[凍結目標](15_project_roadmap.md#品質目標と判断ルール)を維持し、結果を見て基準を下げない。Chatの関連性・文脈・EOT停止はPhase 7の別検証であり、Base段階で達成済みにしない。

本命10Bの証拠を揃え、日本語生成が成立した場合はPhase 7へ進む。未達なら修復・対照実験または容量/データの限界として判断し、成功扱いで次へ進まない。20B・条件付き50BはPhase 9の系列であり、Phase 6の完了条件へ追加しない。

## 暫定のcompute見積もり

③の採用設定の定常中央値694,521 tokens/sを使った算術値。全文評価/保存/取得/修復・cold compile・decay枝・LR調整を除く。本学習設定は凍結済みで、今回は起動しない。下表は純学習のみで、[全文評価/生成/枝を加えた実測予算](30_phase6_readiness_execution.md)を参照し、実時間の保証にはしない。[③の完了記録](29_phase6_performance_completion.md)。

| 系列tokens | 参考compute時間 |
|---:|---:|
| 500M | 約12分 |
| 1B | 約24分 |
| 2B | 約48分 |
| 5B | 約2時間 |
| 10B | 約4時間 |

同じ固定400生成のNoNorm評価workerはPhase 5で約5.4分/回だった。④⑤の現在sourceでは400生成360.684秒、拡張dev全文336.292秒を別計測した。新devは89,416文書 / 164,344,743 body bytesで、pilot 924文書とは別母集団。拡張dev全文採点、保存間隔、枝の回数を別加算し、小sample probeを全文品質評価としない。uint16 streamは2 bytes/tokenにindex/raw/一時fileを加え、checkpointは保持個数×実file容量、cache/venvは別枠。準備完了時のLinux空きは950,875,688,960 bytesで、開始時に再確認する。[Phase 5速度](../reports/phase5/resource_budget.json)、[Phase 6準備の実測資源](../reports/phase6/completion_audit.json)

## 次回の実行入口と成果物

次回は`AGENTS.md`、[現在の状態](autonomous_status.md)、本書、[Windows/WSL手順](windows_handoff.md)を読み、既存jobと未実装項目から確認する。復元済みのTokenizer学習・Phase 3全export・Phase 4全測定を無条件に繰り返さない。

既存CLIの確認は学習を起動しない:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --help
```

WSDの実CLI・準備検証config、③用測定/厳密再開・独立監査の入口は実装済み。[③の実CLIと比較](28_phase6_performance.md)。④⑤用の`phase6_readiness.py`と`verify_nonorm_export.py`を追加し、完了した実jobとsource/weights/logsを保持する。本学習の`run_base.py`はprepareが既定で、凍結configを照合し、実commandを[起動計画](../reports/phase6/base_launch_plan.json)へ固定済み。本学習は再開指定を待つ。

①②の拡張corpus/shards・監査・準備検証checkpointは[完了記録](26_phase6_preparation_completion.md)、③はcommit `a7d26e1`へ保存済み。④⑤の凍結run configと実起動/復旧計画も`93c7d1d`で作成・検証済み。scaling checkpoint、`base_scaling_report.json`、`base_v1_evaluation.md`とmodel cardは次の本学習で作る成果物であり、今回は開始しない。

## batch 32の保存した更新数と丸め（version2凍結済み・本学習前で停止）

⑤の3 LR比較・厳密/cold再開後に保存した32,768 input tokens/updateの算術表。stable系列のglobal updateで、decay枝の追加tokensを含まない。現行version2は`launch_enabled=true`で技術gateを満たすが、ユーザーの再開指定まで本学習を起動しない。旧false設定はversion1として保持する。

| 目標input tokens | global updates | 丸め後input tokens | 純学習換算 |
|---:|---:|---:|---:|
| 500,000,000 | 15,259 | 500,006,912 | 12.0分 |
| 1,000,000,000 | 30,518 | 1,000,013,824 | 24.0分 |
| 2,000,000,000 | 61,036 | 2,000,027,648 | 48.0分 |
| 5,000,000,000 | 152,588 | 5,000,003,584 | 120.0分 |
| 10,000,000,000 | 305,176 | 10,000,007,168 | 240.0分 |

本文教師tokens/bytesはBOS等のmaskと実samplerから別計数する。500M→1B等の区間予算は累積値の差で計算し、枝と評価/保存を別に加算する。
`````

## docs/27_phase6_remaining_plan.md

UTF8 LF SHA256: fcc35cbd5e39614f46f0766695447bfb37fc88d1d355f4a896b93a908ef114ad

`````markdown
# 準備完了後の実行計画: Base本学習からChat・量子化まで

## 低学習率の計画1〜3を完了・停止（2026-10-04）

[結果](../reports/phase6/eos_low_lr_100m_review.json)。①旧Webは追加6.55M時点からdev256退行、終盤decayで部分回復。②同じ元2B/データ/入力digest/Adam/RNGからLR曲線全体を10分の1へ変更、各100Mを実行。③同じ全文89,416dev/400生成で新Web BPB0.972969、新short0.974799を確認（元2B0.982882、旧高LR1.016473/1.017580）。固定EOS0→27/80、反復55→41、400 empty/role/Unicode両枝0。元mixture/全文/増量gate全合格、実CUDA全state再開一致、12関連tests成功、GPU35分41秒で45分上限内。

意味反復/文脈誤りは残り、独立人手blind/test/Chat未実施。原品質基準は保持して短文枝を実用品質として採用しない。補助短文のEOSは旧高LR42→低LR37/80、反復29→37なので全指標改善とはしない。原2B・高LR・新低LR重みをすべて保存。要求された1〜3をreport/commitで終え、5B/Chat/自動sweepへ移行しない。次の5Bは別段階のstable予算延長とdecay設計を凍結する必要がある。今回の曲線全体変更で再開瞬間だけの因果や長期最適LRを確定しない。以下は実行中/旧計画の履歴。

## 現在の実行: 低学習率の1〜3（2026-10-04）

ユーザーが次計画の1〜3を実行するよう指定。[実行config](../configs/phase6/eos_low_lr_100m.json)。①既存高LRログ＋保存済みWeb200/1600/2800更新をdev256だけで採点し退行時点を調べる。②同じ完成2B親/既存pool/aux80からLR0.0002のWeb/short20を各100M、旧0.002以外の条件は一致。③元screen gateに合う候補の全文/400と生成内容を確認し、元2B/旧100Mと比較してreport/commit。Web全文BPB対照はshort合格時必須。原mixture/増量/品質条件は変更しない。累積GPU45分上限、cache対策を初めから適用、科学200,015,872/検証262,144を別計上。単一LR候補を一度比較し5B/Chat/自動sweep前で停止。低LRが良いかは仮説であり結果で判断する。以下は経過履歴。

## 2026-10-04の100M比較を完了・次段階は停止

ユーザーによる実行再開後、下記100M計画を実装・実行・全文評価し、[結果](../reports/phase6/eos_complete_100m_review.json)へ保存。固定EOS0→24/80、補助0→42/80、固定反復50→49/80。全文dev BPB Web1.016473/short1.017580、短文full400 empty/role/Unicode0。自動採用gateは合格したが、意味誤り/反復が残り原品質基準未達なので診断候補として保存、元2Bを基準に保持する。両100M枝とも元2B全文BPB0.982882より悪く、WebのUnicode退行で5B条件を満たさない。単に停止率が改善したことを根拠に5Bを開始しない。

科学200,015,872 tokens/検証262,144 tokens、関連24 tests成功、実CUDA全state再開一致。評価cacheの減速から復旧しGPU合計3305.199秒、原45分見積/2700秒を超過。別1200秒復旧は1054.859秒、追加学習0、品質/科学比較条件は維持した。全job実終了。報告/commitで停止し、5B/Chat/自動sweepは未開始。次回は意味整合・反復と元2BからのBPB退行を含めて改善案を検討する。単位長と追加量を旧25Mから同時変更したため、旧結果との差では両要因を分離しない。以下の「今回は計画のみ」「未実装」は実行前の履歴として保持する。

## 2026-10-04の次回案: 終了単位を揃えた100M比較、その後5B

今回は計画作成のみ。学習/推論/データ抽出は開始していない。[機械可読の提案と根拠](../reports/phase6/eos_next_plan.json)、[現在の状態](autonomous_status.md)。以下の旧計画は履歴。モデルは10,001,152parametersのまま、一般Web trainは12.23B tokensを用意済みで、次の5B/10B消費予算に追加取得は不要。

根拠は[2B学習](../reports/phase6/base_2b_10b_data_review.json)、[EOS調査](../reports/phase6/eos_2b_review.json)、[25M対照](../reports/phase6/eos_short_pilot_review.json)。2Bでは全文dev BPB1.022491→0.982882と改善したがgreedy停止0/80。短文20%の25Mでは反復62→54/80、EOS NLL2.424873→2.331916だが停止0/80、BPBは対照比+0.06025%。EOS教師は1.684倍でも自由生成の停止に移らなかった。前回pool平均104.60/中央値107 tokens、64以下は712/47,844件（1.49%）。25Mは親2Bの約1.25%、短文露出5Mは約0.25%である。

**観測と仮説**: 教師漏れ/停止controllerの不具合は見つからず、EOSを選ぶと実際に停止する。原greedyは512 tokensでも0/20停止だったため、64-token制限や平均文書長だけを失敗の原因にしない。完結単位/短文生成の分布のずれ、追加学習量、greedyの反復feedbackを切り分ける。次回は長さ条件と総予算を変更するため、前回との差だけでどちらの因果効果かを判断しない。同じ100M予算のWeb controlで短文mixtureの効果を比較する。

| 次回の順序 | 作業 | 条件・予算・終了点 |
|---:|---|---|
| 1 | trainから32〜64-tokenの完結した文/段落単位を準備 | 元親文書のtrain membershipを継承。文として完結した境界を単位の終端と定義しEOSを教師にする。任意token切断は不可。21M以上の多様なinput tokensを用意し、712件の周回で埋めない。CPU処理上限600秒、未達なら部分量/理由を記録して学習前に止める |
| 2 | 新しい対照100Mと短文20%条件100Mを学習 | 同じ完成2B重み/Adam moments/RNG/Web cursor、同じLR/optimizer/context/batch/seed。各3,052更新/100,007,936 input tokens、2,900 stable＋152 decay。短文610更新/19,988,480 tokens（19.9869%）。合計200,015,872科学tokens、検証computeは別計上 |
| 3 | 固定評価と短文の補助診断 | 元のdev256/greedy80/64上限を維持。新dev補助80件は同じ完結単位の定義で既存devから作り、生成prefixと残り本文が64内に収まるよう学習前に固定する。train/testとは分離。EOS率だけでなく文法・早期終了・反復・EOS順位/NLLを記録 |
| 4 | 採否と次の段階を一度で決める | 下記の元mixture採用gateを維持。短文枝はgate合格時だけ全文89,416 dev/400生成。Web100MはBase増量判断に使うため、screenで重大退行がなければ全文評価。最大2枝と予算へ計上。report/commitで一区切り、比率/LR/損失重みの自動sweepはしない |

データ単位の変更を明示する。今回は元Web文書の最後だけを教師にする条件から、完結した文/段落を独立学習recordとして扱う条件へ変える。元文書のEOS位置と同じだとは主張しない。括弧・引用内の句点、数値/URL、箇条書き/断片、省略終端を保守的に除外し、少数例で単位の内容を確認する。正規化/Tokenizerは保持し、同一親文書の単位は同一split。重複除去は新しい小poolのexact本文と保護されたdev単位に限定し、12.23B全件near監査を再実行しない。poolの量/長さ/親文書数を記録し、恣意的な切断による偽の完結例を増やさない。

100Mではscheduleが変わるため、前回の完成25M Web controlをそのまま対照に使わない。両100M枝を新しく同じ2B親から作る。前回の32〜128pool/25M成果物は保持する。必要なbuilder/補助suite/100M runner/parameterized reviewerを実装してから起動し、存在しないcommandを実行済みとはしない。既存step/samplerは再利用し、変更箇所に必要な最小testsと短い実CUDA全state再開を確認する。長いGPU jobはPID/boot/start ticks/lock/log/latest checkpointを永続化し、valid checkpointから再開する。

**短文mixtureの採用条件は維持**: 元の固定80 greedyでWeb100Mより自然EOS停止が8件以上増え、反復が対照以下、empty/role/Unicode失敗0、共通dev256 BPBの悪化が対照比1%以内。空応答や句読点だけの早期停止を有用な改善にしない。補助80件は原因を調べる追加診断であり、元の固定suite/gateの代替にしない。EOS logit bias/強制終了/penaltyによる停止を学習成果に加算しない。

screen合格後の全文評価でも短文枝のBPBをWeb100M比1%以内に保ち、固定80のgenerated IDsがscreenと一致することを確認する。全400生成で元2Bに対する新しいempty/role/Unicode失敗があれば採用しない。fullの不合格をscreen合格で上書きしない。

| 次回の結果 | 判断 |
|---|---|
| 固定80と短文補助の両方で改善 | 有望な短文仕上げ枝として保存し全文評価。Base v1/Chat達成とは別。5B Baseへ同じ仕上げを適用する価値を記録 |
| 補助短文だけ改善、固定80は未達 | 完結単位を学ぶが既存promptへ転移しない仮説。混合を未採用とし、生成例/長さ/文法を記録。小さなmixture再調整を無制限に継続しない |
| 両方未改善または明らかな退行 | この100M/20%条件を棄却。EOSを増やすだけで解決とはせず、次の用途を短文response/EOT学習へ絞る案を残す。Web100MをBase増量の対照として評価し、失敗を消さない |

**Baseの5Bは次の独立した段階**: EOS8件増は短文mixtureの採用gateであり、Base全体の予測精度やChat停止95%の判定と混同しない。短文枝が不合格でも、Web100Mの全文dev/固定生成が重大退行しないならWeb100%の5B増量比較を検討できる。開始前にgo/no-goを記録し、直前の2Bに対する全文BPB悪化が数値比較の0.001 BPBを越える、固定80反復が8件以上増える、新しいempty/role/Unicode失敗が出る場合は進めない。この進行条件は能力達成基準の緩和ではなく、次の増量実験へ進む条件である。

5Bは保存済みstable1,900,019,712 tokens/update57,984から予算延長を明示した別forkで再開する。完成2Bのdecay枝やshort試行を通常resumeで延長しない。dataは既存Web12.23Bのまま。global144,959更新/4,750,016,512 stable tokensまで継続し、別の7,629-update decayでglobal152,588/5,000,003,584 tokensへ到達する。必要な追加学習は3,099,983,872 tokens。model/optimizer/scheduler/RNG/samplerと消費counterを維持するstable-budget延長処理は未実装なので、実装/短い全state再開確認後に凍結する。

5B主系列には未採用の短文mixtureを混ぜない。有望だった場合の短文仕上げは独立枝で、別予算を記録する。21Mのpilot poolを5B系列の20%に繰り返して一般データ増量と呼ばない。5B終了で全文BPB、greedy/sampling各条件のEOS/反復/Unicodeと生成内容を同じ評価で比較し、report/commitで再度一区切りにする。予測精度の改善が続き重大退行がなければ、その結果から10B案を立てる。5Bで品質目標未達なら未達と明記し、自動的に10B/20B/50Bへ延ばさない。

その後はroadmapのBase→Chatへ進む。Base文法70%等の元基準を保持し、必要なBase品質を確認してからDialogue mid-training/SFTを実装・比較する。ChatではAssistant body＋EOTを教師にする。停止95%以上/空5%以下/役割1%以下/固定suite Unicode0の最終基準を維持する。人手blind採点と未使用testが未実施なら、その能力達成を主張しない。Baseのopen continuation EOSとChatのresponse終端はそれぞれ報告する。

**時間見積り**: 現在の25M学習は1枝約45.5秒、定常655k〜707k tokens/s、全文dev＋400生成は約12分。100M対照2枝の純学習は約5分、元/補助生成とdev256を含めGPU10〜15分。Webだけ全文評価なら約25〜30分、短文枝も合格して2枝を全文評価する場合は約35〜40分（GPU上限案2700秒）。新poolのCPU上限10分、実装・内容確認・修復時間は別。5Bは追加3.10Bの純学習約73〜79分、compile/I/O/保存/全文評価を含め約90〜120分を目安とする。これは実測からの推定で、未実装処理の所要時間や完了時刻の保証ではない。WSL/4090、uv、BF16/Flash/compile batch32/context1024を継続し、完了済み環境/Tokenizer/全件監査は再実行しない。

背景として、RNNでは有限列を学習してもgreedy等の不完全decodingが停止しない場合が報告されている。[Welleck et al., EMNLP 2020](https://arxiv.org/abs/2002.02492)。同じ重みでもdecodingで反復等の生成品質が変わるという研究もある。[Holtzman et al., ICLR 2020](https://arxiv.org/abs/1904.09751)。これらは比較設計の背景であり、このTransformerの原因や上記改善の成功を証明するものではない。

---

以下は過去の計画・実行記録。

2026-10-04最新: 実train12.23Bのローカル整備と[新データでのユーザー指定2B学習・既存評価を完了](../reports/phase6/base_2b_10b_data_review.json)。同じdev BPB0.982882、greedy反復60/80/EOS0/80を記録し、report/commitして停止する。5B/10B/Chat/decoder比較は未開始。以下の実行中・学習前停止・2B/5Bデータ増量案は履歴。[現在の状態](autonomous_status.md)。

更新: 2026-10-03。Phase 0〜5とPhase 6①〜⑤の準備は完了。③は`a7d26e1`、④⑤は`93c7d1d`へcommit済み。[現在の状態](autonomous_status.md)、[④⑤の実測と停止記録](30_phase6_readiness_execution.md)。**計画1〜5の実行をユーザーが再開し、500M stable・独立decay・全文dev/400生成比較を完了した。現在は1B前で停止している。**

## 現在の実行: ローカル10Bデータセットの整備

2026-10-04更新: 実train12.23Bの整備は[ユーザー指定の検証範囲で完了](../reports/phase6/corpus_10b_ready_review.json)。過剰な独立再照合を停止し、構築時の検査・全raw再構築・実train loader合格を採用する。さらにユーザーが2B学習を指定し、新データの別runをGPUで実行中。最後の約5%減衰を含む総2Bで既存dev/生成比較を行い停止する。[現在の状態](autonomous_status.md)。以下の学習前停止・2B/5Bデータ増量案は履歴。

ユーザー指定により、下記2B/5Bの計画を[約10Bの取得・構築・監査](32_local_10b_corpus.md)へ更新して実行を開始した。10BはT4Kで測った学習用データ量で、10Mモデルのサイズや消費学習tokensではない。処理はWSL内のdiskへ置き、旧heldoutと過去成果物を保護する。全件監査/report/commit後に学習前で停止する。以下は以前の計画履歴。

## 次回の一区切り: 学習用データを2Bへ拡張する

2026-10-03のユーザー訂正に従い、次に取り組む対象をデータセット量の拡張へ変更する。仮説は「現在の学習用756,087,912 stream tokensでは、データの量・多様性が不足している可能性がある」。最初の完了目標は、品質処理後にT4Kで測った学習用stream tokensが合計2,000,000,000以上となること。追加2Bではなく合計2Bで、dev/testは含めず、同じ文書の周回を増量に数えない。5Bは後続の段階目標とする。モデルは10,001,152パラメータのまま。公開コーパスの規模、整備済みデータ量、モデルが消費した学習量を別々に記録する。

**今回は計画の訂正のみ。取得・データ構築・推論・学習は開始しない。次回のデータ整備を実行する際も、監査・報告・commitを一区切りにして学習開始前で停止する。** 生成方法の比較と短文mixture案は保留し、このデータ拡張の前提条件にしない。過去の計画・監査結果を実行済みの証拠として書き換えない。

| 順序 | 次回の作業 | 完了・判断条件 |
|---:|---|---|
| 1 | 既存job、保存先、Windows物理diskとWSL filesystemの空き容量、取得/構築CLIを確認する | 重複jobなし。raw・中間DB/JSON・shards・監査用一時領域を別計上し、処理時間と容量の予算を開始前に記録 |
| 2 | 固定FineWeb2 Edu Japaneseから追加取得する別config/manifestを作る | 既存revision、Tokenizer、品質filterを維持。初回計画の8files/最大16files・4.4GB上限では不足するため、凍結configを変更せず新しい条件を保存 |
| 3 | 新しいdirectoryへ構築し、既存trainと追加文書を一緒に重複除去する | 既存dev/test、pilotのheldout、固定評価suiteを保護し、検出された混入clusterを除外。既存raw/expanded-v2/shardsは保持 |
| 4 | train量・文書数・bytes・長さ/品質/source構成と全shardを監査する | train合計2B以上、hash/Tokenizer往復/index/token列整合、split分離を検証。完了しなければ未達と記録し、基準を緩めない |
| 5 | 準備結果、実時間/容量、残る偏り、次の学習比較案を報告してcommitする | 新manifest/hashとjob終了を保存し停止。2Bのデータ準備を2B学習完了や品質改善へ読み替えない |

取得量の暫定見積りは、現在8filesから756Mを得た比率で合計約22filesが2B、約53filesが5B。追加分の重複や品質除外で収率は変わるため保証ではない。次回2B整備の取得上限案は合計32files・raw10GB、後続5B案は合計64files・raw20GBとする。既取得分も上限へ含め、上限到達で目標未達なら部分成果と実測を保存して停止し、無制限に追加取得しない。中間成果物はrawより大きいため、このraw上限だけを必要disk容量としない。構築/監査の時間上限は少量の追加処理による実測後、全量処理の前に固定する。未実装の大規模処理・heldout保護・再開機能があれば先に実装し、関連検証を行う。

同じ短文subsetの追加では文書の多様性や短い完結文の比率が十分変わらない可能性もある。量だけで質が改善すると確定せず、分布を監査して報告する。2B整備後の学習では、学習tokens/同一dev/生成条件を揃えた旧データと拡張データの対照を別計画で定義し、データ量と学習量の影響を区別する。データ変更を既存stableの通常resumeへ混ぜず、新系列のlineageと全state再開を検証する。元のBase品質基準は維持する。

## 保留した案: 学習済み10Mモデルの生成方法を比較する

以下は以前の計画の履歴。現在の次回優先作業は上記のデータ拡張であり、この比較を先に開始しない。

2026-10-03の計画依頼。反復/EOS/dataの[調査は16cc38dで完了](../reports/phase6/repetition_diagnosis_review.md)。モデル規模は10,001,152パラメータ（約10M）のまま。500Mは学習したinput token数のmilestoneで、モデル規模ではない。比較に使うcheckpointは500,006,912 tokensのstable学習＋25,001,984 tokensのdecay後、合計525,008,896 input tokensを学習した10Mモデルである。

次回のゴールは、この学習済み10Mモデルの同じ重みを使い、反復抑制が文章の改善につながるかを測り、比較report・人手評価用packetを残してcommitし停止すること。[固定する比較条件と予算](../reports/phase6/repetition_decoder_plan.json)、[計画の16項目照合・WSL同期・234既存files保持](../reports/phase6/repetition_decoder_plan_audit.json)。これは計画の確認で、比較codeや生成品質の検証結果ではない。今回は計画作成のみで、推論・学習・データ変更を開始しない。以下の500M計画は実行前の履歴として保持する。

| 順序 | 次回の作業 | 終了時に確認すること |
|---:|---|---|
| 1 | 既存process・checkpoint/Tokenizer/suite/protocol/source hashを照合し、別の比較CLIと永続runnerを実装する | GPU重複なし、有限値・model/RNG不変、同じdecoderの再現、log/部分結果/予算を保った再開。凍結trainer/evaluator/configと過去結果を保持 |
| 2 | 同じdecay500Mで反復抑制1.0対1.1、dev80、greedy＋sampling3seedsを比較する | 各320、計640outputs。reference320の全generated IDsが既存reportと一致。64-token上限・temp0.8/top_p0.9・EOS3・元の抑制IDsを固定 |
| 3 | 反復/EOS/Unicode/role/emptyと長さ、同じpromptの改善・悪化、95% CIを集計する | sampling3seedsを同じpromptにまとめたcluster bootstrap、2000回/seed42。EOSを強制せず、文字化けや意味の反復を隠さない |
| 4 | 各10categoryの最初2dev casesを使い、20組/40文章のblind人手評価packetを作る | A/Bをseed42で匿名化しmappingを分離、文法・関連性0/1/2と意味の反復を点検。独立人手評価がなければ未実施と明記 |
| 5 | 改善・副作用・未達を報告し、statusを更新してcommitする | 比較結果と時間/hash/job終了の証拠、次の判断を記録して停止。短文mixture学習や1Bへ自動移行しない |

反復抑制1.1は、生成済みbody token IDの重複を一度だけ扱い、正logitを1.1で割り、負logitに1.1を掛ける。promptとspecial IDs0〜7は対象外。EOSへ直接加点したり、停止文字列や最小/最大長を変更したりしない。1.0は元の演算を完全に通す。BF16の元score dtype・sampling手順を保持する。比較機能はまだ未実装なので、次回は実装・検証してから起動する。

referenceはgreedy反復66/80・EOS0/80、sampling反復11/240・EOS1/240・Unicode失敗1/240。自動改善候補の目安はgreedy反復が8件以上減る（58/80以下）、sampling反復/EOSが悪化せず、candidate320のUnicode/role/empty失敗0件。これはdecoder候補の比較基準であり、既存のBase文法70%・EOS停止95%等の凍結品質基準を緩めない。20件のpacketと自動flagだけでBase合格や文章の自然さを宣言しない。

GPU推論の累積上限は15分。既存400生成367秒から計640は約10分の算術見積りで、CUDA probe/再開も同じ上限へ計上する。実装・検証・report込みは30〜60分の目安、人手評価や予期しない修復は別。上限で未完了なら部分結果と原因を保存して停止し、予算をリセットして再試行しない。同じ重みのdecoder比較なので、既存全文dev BPB1.022491はそのまま参照し、全文採点を繰り返さない。

実行はWSL2/Ubuntu/RTX4090、Python3.12.7を必要なextras付き`uv run --frozen`から起動する。学習の最速batch32/Flash/compile/BF16/fused AdamWは変更しない。推論batch化はreference全IDs一致を維持できる場合に限り同じ予算内で扱い、VRAM容量を埋めるための別研究は追加しない。

### その結果を見てからの学習比較案（次回のscope外）

反復抑制で文法が崩れる、意味の反復や停止未達が残る場合には、短い完全文書の教師を増やす対照を別の一区切りとして準備する。同じstable500Mをparentとし、原trainの既存decayを対照A、短文mixtureをBとする。Bはtrainの128body tokens以下の完全文書を使い、input tokensの20%を短文に割り当てる案（前回の未定義な「20%文書」を具体化した提案）。文の途中へEOSを付けず、dev/testや新sourceを使わない。

各armは763更新/25,001,984 input tokens、同じdecay schedule/seed42。optimizer/RNGのparent stateを保持し、Bの新samplerを別のlineageとして記録する。異なるdataでsampler位置まで同じとは主張しない。別loader/trainerを先に実装し、原data対照の互換性・有限値・厳密保存再開を確認する。凍結coreは変更しない。

対照Aの実条件・parent/全stateが一致すれば既存学習/評価を再利用し、無駄な再学習を避ける。A再生成が必要なら、前回の2arm/GPU20分案は全文評価2回だけで約25分必要なため予算を改めて凍結する。Aを再利用できる場合の後続案はCUDA再開gate5分＋Bの学習/全文dev/400生成20分上限、CPU準備・人手評価は別計上。現段階ではdata/実装/起動条件は未準備で、採否条件とともに次の独立計画で確定する。EOS密度と短文内容が同時に変わるのでEOSだけの因果効果にはしない。1Bの判断はその後とする。

## 次回の一区切り: 拡張データで500Mを学習・評価する

実行後の更新: 2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [実測](../reports/phase6/base_500m_review.json)。以下は実行前に固定した計画を保持する。

現在の判断: 生成反復とUnicode破綻に退行があるため、単純な1B延長を推奨しない。まず既存artifactのEOS教師量・文書長/短文promptの違い・反復・decoding差を調べ、対照・予算・終了条件を定義してから次の実験を提案する。今回は追加実験へ進まず、指定の1〜5を完了して停止する。

2026-10-03の次回計画依頼に基づく提案。次回のゴールは、準備済み拡張trainを使った500M Baseと独立decay枝を保存し、現在の100Mモデルと同じdevで比較して報告すること。**次回は500Mの評価・記録・commitを一区切りにして停止する計画とし、1B以降はその結果を踏まえた後続段階とする。今回の依頼は計画作成で、本学習は開始しない。**

| 順序 | 実施すること | 終了時に確認すること |
|---:|---|---|
| 1 | 既存process/checkpoint、source/data/runtime hash、GPU、空き容量を確認しprepareする | 重複jobなし、有効な再開点か新規runかを識別、凍結条件一致、最低空き200 GiB |
| 2 | seed42で新規初期化し、拡張trainで15,259 stable更新 | 500,006,912 input tokens、finite loss/gradient、全state checkpointと消費列・ログを保存 |
| 3 | stable終端から別directoryへ763更新の独立decay枝 | 終端global16,022、追加25,001,984 tokens、元stable不変、次回の継続点を保持 |
| 4 | decay終端の全文devと固定400生成を評価する | 同一89,416 dev文書のBPB、同一prompt/seed/上限のEOS・反復・Unicode・生成本文と時間 |
| 5 | 比較・失敗・改善候補・次の判断をreport/statusへ保存してcommitする | stable/decayのcheckpoint SHA、実tokens/bytes/GPU時間、基準との差、1B継続か原因調査かを報告し停止 |

データはpilotの18,022文書・T4K約8.398M stream tokensから、1,604,292文書・756,087,912 stream tokensへ約90倍に拡張済み。前回100Mの約11.91周に対し、新500M stableは約0.66周、独立decayを含む系列は約0.69周の算術露出になる。raw再取得やTokenizer再学習は開始条件にしない。データ量不足は仮説であり、今回はデータ・学習予算・scheduleも変わるため、結果だけでデータ量の因果効果を確定しない。

比較基準は現在の100M checkpointを同じ拡張devで測ったBPB **1.2441264716**、固定生成のgreedy EOS **0/80**・反復 **48/80**、全400出力のUnicode **0/400**。生成はdecoding条件別に集計し、文法・関連性は生成本文で確認する。旧pilot BPBとの単純差を改善量にせず、testは使わない。人手採点を実施できなければ未実施と残し、自動判定を人手評価へ読み替えない。

未統合のpaired CI/人手rubric集約は、次回の比較report作成に必要な実装と検証として別計上する。データ量だけの対照実験は今回の500M系列へ追加せず、結果が停滞・退行した場合に対照・予算・終了条件を定義して提案する。品質の達成基準は既存protocolを維持する。

学習＋独立decay＋機械評価は現実測から約24分。compile/保存/起動確認、比較reportの実装、内容確認、修復時間は別で、全作業の完了時刻は保証しない。失敗時は有効checkpointと原因を保持して修復し、同条件で再開する。有限値/hash/再開/容量に問題があるまま1Bへ進めない。

実出力はLinux `reports/phase6/base-20261003/`配下の`stable/`、`decay-500M/`、`evaluation-500M/full-dev.json`・`generation.json`、supervisor/log/snapshot。比較要約は今後作成する `reports/phase6/base_500m_review.json` と `base_500m_review.md`を提案する。checkpoint等の大型artifactはLinuxへ保持し、検証した小reportとstatusをGitへ保存する。

## 完了済みの準備と証拠

| 作業 | 検証結果 | 正本 |
|---|---|---|
| ①拡張データ | T4K train 756,087,912 unique stream tokens、1,604,292文書、Web100%。全raw/cluster/shard監査、dev/test分離 | [①②完了記録](26_phase6_preparation_completion.md) |
| ②WSD・保存再開 | stable/独立decay、model/optimizer/scheduler/RNG/sampler・token消費のCUDA完全一致 | [①②のGPU監査](../reports/phase6/completion_audit.json) |
| ③高速化・容量 | Flash＋compile reduce-overhead、batch32、694,521 tokens/s。最大stable batch111、112 OOM。32が111より速い | [③完了記録](29_phase6_performance_completion.md) |
| ④生成・全文評価 | 400生成360.684秒。greedy EOS0/80・反復48/80、Unicode0/400で品質未達。全文dev89,416文書、BPB1.2441264716、336.292秒 | [生成](../reports/phase6/generation_diagnostics.json)、[全文dev](../reports/phase6/expanded_dev_baseline.json) |
| ④学習済み変換 | NoNorm HF/Llama・GGUF/Llama。CPU精度profileで元の短/1024・full/cacheの全12比較、実CLI/重み監査149 checks成功 | [数値比較](../reports/phase6/nonorm_export_parity_report.json)、[独立CLI監査](../reports/phase6/readiness_export_audit.json) |
| ⑤設定凍結 | LR3候補から0.002採用。厳密50/cold25 checks完全一致、独立GPU106 checks、全90 tests成功 | [安定性](../reports/phase6/readiness_stability_report.json)、[設定version2](../configs/phase6/base_frozen.json)、[総合37 checks](../reports/phase6/readiness_gate_audit.json) |

GPU準備runの合計245,760,000 input tokensは独立した有限比較の台帳で、一つのBase本学習ではない。Phase 6全体の完了には10BのBase成果物と評価が必要で、①〜⑤完了と区別する。

CPU推論profileはFP32の重み/activation/cache/logitsとFP64累積を使い、成果物metadataから専用runtimeを適用する。stock runtimeでの実行を拒否し、未修正stock CPU/CUDA FP32の失敗を保持する。精度profileの成功をGPU学習速度や生成品質の改善へ読み替えない。学習のCUDA/BF16経路は変更していない。

## 再開時の最初の確認

ユーザーが本学習を再開した後、以下を確認してから500Mへ進む。

1. Windowsコード正本とLinux実行コピーのsource/hashを照合する。Linuxの旧Git HEADだけで現在の実装を判断しない。
2. 実GPU compute一覧、既存run/job、PID/boot ID/start ticks、GPU排他lock、checkpoint/latest.jsonを照合し、重複起動を防ぐ。
3. [凍結設定](../configs/phase6/base_frozen.json)のmodel・Tokenizer・shard manifest・source・検証artifact・runtime receiptを検証する。入力を変更する場合は新条件で必要なgateを再検証する。
4. 空き容量200 GiB以上、run出力上限100 GiB、checkpoint全保持の予算を確認する。データ再取得・Tokenizer再学習・完了済み比較を通常の再開条件にしない。
5. `run_base.py`のprepareで500M commandを確認する。新規Baseはseed42のランダム初期化から始め、Phase 5終端や準備比較のcheckpointを初期状態へresumeしない。

Python3.12.7の全実行は必要なextra付き`uv run --frozen`。依存変更は`uv add`、復元は`uv sync --frozen`。学習はWSL2/Ubuntu/RTX4090、Git identityは`yousan <ka1357amnbpdr@gmail.com>`。

## 500Mから10Bまでの段階評価

凍結条件はcontext1024、batch32、accumulation1、32,768 input tokens/update、FP32 parameters/BF16、fused AdamW、Flash/compile reduce-overhead/fullgraph/static/deterministic、LR0.002、warmup200、WSD global305,176更新。save1,000更新ごと・log50更新ごと。各観測点の独立decay枝は更新数の5%を切り上げ、最低LR比0.1。

| stable観測点 | global更新数 | 丸め後stable input tokens | 独立decay更新数 | decay終端global更新数 | 次へ進む判断 |
|---:|---:|---:|---:|---:|---|
| 500M | 15,259 | 500,006,912 | 763 | 16,022 | 有限loss/gradient・保存/再開・全文BPB・Unicode/反復/EOSを確認 |
| 1B | 30,518 | 1,000,013,824 | 1,526 | 32,044 | 同一dev文書のBPB差/paired CI、生成失敗と文法rubricを確認 |
| 2B | 61,036 | 2,000,027,648 | 3,052 | 64,088 | 継続価値と追加時間を判断。過去355M artifactがなければ直接比較未実施と明記 |
| 5B | 152,588 | 5,000,003,584 | 7,630 | 160,218 | 本命1構成と10Bまでの継続方針を固定。品質停滞に応じた対照は別系列 |
| 10B | 305,176 | 10,000,007,168 | 15,259 | 320,435 | Base v1の再開可能checkpoint・固定評価・model card、品質達成/未達を保存 |

各観測点のstableを保存し、別directoryへ独立decay枝を作る。そのdecay済みcheckpointに対して全文dev89,416文書と固定Base dev80 prompt×5条件の400生成を行う。次のstableは元のstable checkpointから同じglobal予算で継続し、decay枝をstable履歴へ戻さない。stable/枝ごとにtokens・教師tokens・body bytes・digest・GPU時間・親hashを記録する。

新dev全文の基準はBPB1.2441264716。同じ文書集合・前処理・CE精度・windowで比較し、旧pilot BPB1.221443との差を改善量にしない。文法などのblind人手採点は未実施。既存bootstrapを用いた段階間paired CI・人手rubricの集約は`run_base.py`の自動処理へ未統合で、必要なreport作成を別途実装・検証する。自動flagや合成停止fixtureを品質合格へ数えない。

モデル選定はdevだけで行い、testは最終確認まで保持する。発散・非有限・再開不一致・hash不一致・容量不足なら原因と有効checkpointを保存して修復する。重大な品質退行は対照条件を定義して調べ、閾値を下げない。10B到達だけでChatへ移行せず、[凍結品質目標](15_project_roadmap.md#品質目標と判断ルール)と日本語生成の成立を確認する。

## 実CLIと中断復旧

実commandの正本は[起動/復旧計画](../reports/phase6/base_launch_plan.json)。下記はWSLのproject rootでの確認で、本学習を起動しない。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003
```

**本学習再開が指定された後の実行例**。今回は実行しない。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003 --operation stable --execute
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003 --operation decay --execute
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_base.py --config configs/phase6/base_frozen.json --target 500M --output reports/phase6/base-20261003 --operation evaluate --execute
```

中断時はsupervisor.json・log・PID/boot/start ticksと実processを照合し、有効なlatest.json/checkpoint SHAを確認して同じcommandを再実行する。CLIがcheckpoint境界へ戻して再開し、500M完了後の1Bでは`--target 1B`へ変える。global終端305,176を変更せず、checkpointのない既存directoryを新規初期化しない。long GPU jobは排他/永続supervisor/heartbeat/source snapshot/checkpointで保持する。

500M+の実起動は未実施。prepare・未達gateでの拒否・有限準備runの実GPU再開は検証済みで、将来の長期run完了とは区別する。`launch_enabled=true`は技術条件の成立で、停止境界を解除しない。

## 実測に基づく予算と容量

⑤の採用LR0.002 runの定常速度693,666 tokens/sを使う。[凍結値](../configs/phase6/base_frozen.json)は③の694,521 tokens/sと別の測定予算である。

| 計上するもの | 算術値/実測 | 範囲 |
|---|---|---|
| stable500M | 約12分 | 学習のみ。独立decay・評価・保存・起動を含まない |
| 500M＋独立decay＋全文dev/400生成1回 | 約24分 | 現測定からの算術値。compile/保存/filesystem変動は別 |
| stable10B | 約4時間 | 累積stable系列のみ |
| 5観測点の独立decay全枝 | 約22.2分 | stableへの追加compute |
| 5回の全文dev＋400生成 | 約58.1分 | 336.292秒＋360.684秒/回。生成長による変動あり |
| 上記10Bまでの合計 | 約5時間21分＋その他の時間 | compile/起動/保存/人手評価/修復を除く。完成時刻の保証ではない |
| checkpoint | 推定347件・41,702,694,225 bytes | 全保持。run上限100 GiB、最低空き200 GiB |

最終checkpoint1件のsave0.435秒、compile込み初回update1.987秒は観測値で、cold compile上限や全保存の保証ではない。raw/data・venv/cache・一時領域は別計上し、開始時に実filesystemの空きを確認する。756M train streamは500M約0.66回、10B約13.23回の算術露出。反復量を新規データ量へ読み替えない。

## Base後の未実装・未検証と条件

| 次の系列 | 着手前に必要なこと | 完了の証拠 |
|---|---|---|
| Phase7 Chat | Dialogue mid-training/SFT trainer・Assistant本文＋EOT教師mask・shift・教師0件/turn切断・保存再開を実装して小予算で検証 | 関連性/文脈/停止、rolloutと人手評価、dev選定後の独立test |
| Phase8 量子化/ローカル | 本学習済みBase/Chatのfloat parityを再検証し、候補比較前に退行許容幅を固定 | Q8/Q4の実型・BPB/生成品質差・weights/全artifact容量・CPU RSS/応答時間・独立環境起動 |
| データ追加/mixture | 現Phase6 dev/testの保護・provenance継承と複数source loaderを実装。取得上限と変更系列予算を固定 | 旧heldoutを保護した新manifest/hash、source別量、変更後の再開/公平比較 |
| Phase9 20B/条件付き50B | stable予算延長の明示fork・履歴・全state再開を実装。通常resumeで予算変更しない | 10B→20Bのcommon-byte BPB差と95%CI、重大生成退行なし、追加予算内なら50B候補 |
| Phase10 追加研究 | 対照、改善metric、予算、採用/打切り条件を事前に定義 | Layer Sharing/蒸留/ReLU²/hybrid/規模比較の独立report |

現在の`--branch-from`はdecay専用。stable延長fork・mixture・Chat trainer・量子化後品質は未実装/未検証。初期Web100%の500M開始に50〜100B master全量取得を要求しない。ローカルで進め、外部の有料GPUや公開は別途の指定が必要。

意味のある実装・測定・観測点ごとにreport/statusを更新して指定名義でcommitし、pushしない。今回は文書/計画更新を検証・commitして停止する。
`````

## docs/39_learning_scale_and_generation_plan.md

UTF8 LF SHA256: 88ee4fa4eed0f1a4a01d29199f1107385a31320b3b9ba40cbb747fbe8b84d55b

`````markdown
# 学習量拡大とEOS 反復 UTF8改善の次回計画

実行準備の更新（2026-10-04）：ユーザー指定のstep1により[専用設定とGPU保存再開確認](40_base_10b_preparation.md)を完了。新config/schema/launcherは準備済み、14tests/実CUDA全state一致を確認した。本学習は未開始。今後の起動は `bash scripts/run_base_10b.sh --train`、引数なしは検証専用。

2026-10-04。ユーザーの訂正に従い、7.5Bの中間実験を省き、**既存12.23B train tokensを使って総10Bまで一度に学習し、そこで比較する計画**へ変更した。データセットは既に10Bを超えているため、新規収集ではなく学習する量を増やす。EOS・反復にはその後に短文仕上げを一度比較し、UTF8は別の推論方式として評価する。本学習・品質評価・decoder変更は未開始で、実CUDAは準備の保存再開検証だけを行った。[前回結果](38_eos_5b_finish_results.md)と[保存証拠](../reports/phase6/eos_5b_finish_review.json)を基準にする。

## 現在の根拠と未解決事項

モデルは10,001,152 parameters、準備済みtrainは12,225,819,077 tokens。主要Web学習は5,000,003,584 tokens、仕上げ各枝はそこから100,007,936 tokens追加した別モデル。二枝の消費を一モデルの累積へ足さない。新データを収集する前に、手元の未使用部分で学習量を増やせる。

| 条件 | 全文BPB | 固定EOS | 固定反復 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|
| 元2B | 0.982882 | 0/80 | 60/80 | 0/400 |
| 元5B | 0.964484 | 0/80 | 59/80 | 2/400 |
| 5BからWeb100M仕上げ | 0.958092 | 0/80 | 57/80 | 0/400 |
| 5Bから短文20%仕上げ | 0.959011 | 13/80 | 51/80 | 2/400 |

本文予測は改善しているが、自然停止と意味品質は十分でない。2B対5Bは学習率の減衰期間にも差があり、全差を学習量だけの効果とは断定しない。短文比較は同じ親・同じ追加量・同じLRであり、今回の条件では自然停止と反復への効果を確認できた。ただし途中不正UTF81件とcap末尾切断1件で最終採用不合格、数量・時刻・否定・文脈の誤りも残る。表示helperは採用済みだがraw品質を改善した証拠ではない。

## 1 総10Bまで直接学習する

目的は、一般Webの未使用データをさらに学習すると、現在より本文予測・内容が良くなるかを測ること。既存shards/Tokenizer/モデル/seed42/batch32/context1024を維持し、短文混合や新lossを入れない。

長期継続の親は、保存済み5B runのstable終端 `reports/phase6/base-5b-20261004/stable/checkpoint-00144959.pt`、4,750,016,512 tokens、SHA `916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5`。減衰済みfinal5Bや低LR100M枝のschedulerをそのまま通常resumeして増量しない。stable親のmodel/Adam/RNG/Web cursorを保持する明示forkを実装・凍結し、stable LR0.002から最後約5%だけ0.0002へ減衰させる。旧final5Bと両仕上げを保持する。

| 値 | 直接10B案 |
|---|---:|
| stable終端 | update289917 / 9,500,000,256 tokens |
| 独立decay | 15,259 updates / 500,006,912 tokens |
| final終端 | update305176 / 10,000,007,168 tokens |
| stable4.75B親からの追加科学学習 | 5,249,990,656 tokens |

1update32,768tokensに丸めた凍結設定値。専用config/schema/launcher/準備reviewerの実装と凍結は完了した。旧5B launcherは新実験の実行commandではない。既存stable-extension経路を再利用し、関連14testsとstable/decayの実CUDA連続対保存再開を確認済み。検証16updates/524,288tokensを科学tokensへ混ぜない。

stable4.75Bから9.5Bへ継続し、最後の独立decayで総10Bへ到達する。7.5B地点の専用decay・全文評価・仕上げ対照は行わない。定期checkpointと有限loss/勾配の監視は保持し、発散や実行予算超過時には停止する。

今回の追加科学学習は5,249,990,656 tokens。減衰前のstable4.75Bへ戻るため、単に「直近5.1Bから4.9B追加」ではない。旧final5Bのdecay区間は別枝として保持する。各枝のWeb cursor/epochを保存し、10Bは準備済み12.23B内で進める。枝間で再使用した区間は記録し、ユニークデータ量の増加に数えない。旧案にあった独立7.5B decayの374,996,992科学tokensと中間全文評価を省ける。

## 2 10Bを同じ評価で比較する

現在の最良Web仕上げBPB0.958091981と元5B0.964484070の保存評価を再利用し、新10Bだけ同じ保護dev89,416文書/164,344,743本文bytesと固定400生成で評価する。dev256は進捗診断に留め、全文BPBと比較しない。固定80 greedy64、抑制あり・なしとsampling3seedsの元条件を保持。EOS bias/penalty/強制停止を入れない。内容の改善・退行も同じpromptで読む。

10Bを後続の仕上げ候補として選ぶ条件は、全文BPBが現在の最良Web0.958091981より小さくなり、元の増量安全条件も満たすこと。原条件は全文BPB悪化+0.001以内、固定反復増加8件未満、全400のraw Unicode/empty/role失敗0、生成条件一致。元5Bと最良Webの両方に対して確認するので、固定反復は65/80未満を要求する。親にUnicode失敗があることや表示補正を免除理由にしない。これは10B到達後の採否基準であり、中間7.5Bの実行条件ではない。

改善が確認できない、raw失敗が出る場合は旧最良モデルと診断用10Bを保持して報告し、追加増量を止める。+0.001以内という安全条件だけで、改善がないままさらに増量しない。単一seedの観測差であり、統計的有意差や広い品質達成は断定しない。

10Bも同じ全文dev/400生成と内容で比較する。BPB改善だけでEOS・文法・正答率も改善したとは扱わない。退行時は最良の旧モデルを保持して報告し、20B/50B/データ再収集へ自動移行しない。今後データ量そのものを比較するなら、同じ学習tokens/曲線で小さいpoolの周回対大きいpoolの新規データを別実験にする必要がある。今回の主目的は既存pool内の学習量を増やす効果である。

## 3 最良の新モデルでEOS仕上げを一度比較する

2で採用可能な10Bモデルが得られた場合だけ、その同じfinal親から低LR Web100%対短文20%を各100,007,936 tokensで比較する。10Bが不合格なら、既に完了した5B親の同じ比較を繰り返さない。仕上げ実験は新10B親で一対だけ行う。

既存accepted21,000,010-token pool/補助80を再利用し、短文は19,988,480 tokensだけ消費する。新規収集・全件再照合・比率/LR sweepは追加しない。同じ親model/Adam/RNG/Web位置、peak0.0002→0.00002、3,052 updates/seed42を維持する。科学合計200,015,872 tokens、検証は別計上。

元screen gateを維持する。固定自然EOSが新Web対照より8件以上増える、反復が対照以下、raw Unicode/empty/role0、dev256 BPB悪化+1%以内、句読点だけの停止なし。合格枝だけ全文へ進み、全文BPB対照比+1%以内・固定screen/final IDs一致・全400 raw失敗0を要求する。Web全文生成の安全判定も元の条件を保持する。

自然停止を内容確認し、数量・時刻・否定・因果の誤り、二回や言い換え反復を記録する。元の三回完全一致の反復指標を変えず、補助80を元固定80の代わりにしない。独立人手blind採点やtestをしていない段階では、Base/Chat品質達成としない。停止率が悪い場合も比率やlossを次々変更せず、この一対で結論を出す。

## 4 UTF8を保証する推論方式を別条件で比較する

目的は、表示だけでなく生成raw bytesの途中不正と未完成末尾を減らすこと。新しい学習比較とは分けて、保存済み短文候補一つに対して元方式と単一のUTF8制約付き方式を比較する。新しい短文候補が得られなければ、現5B短文診断モデルを使い、元400生成は再利用する。

実装案は4096語彙の各tokenのbyte列についてUTF8状態遷移を事前計算し、現在の状態から不正になるtokenを選択対象から外すこと。EOS/EOTは完成境界だけで許す。未知ID等のlossless decode不能tokenの扱いを明記し、元方式と異なるpolicyとして記録する。末尾だけを保証するためには、残りのtoken枠内で完成状態に戻れる候補だけを許す到達可能性の確認も必要。上限を延ばしたり、後からbytesを削った結果をraw成功と数えたり、EOSを強制したりしない。

日本語・emojiの1〜3未完成bytes、途中invalid、surrogate/範囲外、EOS/EOT境界、残り枠での完結、Tokenizer特殊IDをCPUで確認する。4096語彙を毎step全部Python decodeする設計を避け、状態と残り枠ごとのmaskを事前計算する。再開にはこの新policyのsource/config/RNGを保存する。

元64-token上限と400のprompt/decoding/seed keysで新policyだけGPU生成する。raw Unicode/empty/role0と同じ重みの元EOS・反復に対する退行なしを、この推論方式の比較条件とする。変更されたIDs、EOS自然停止、max-token停止、maskによる選択変更数、生成速度を報告する。重みは不変なので本文BPBは保存値を再利用し、再採点しない。

これは推論方式の効果であり、元raw方式の学習gate不合格を合格へ書き換えない。raw方式と新policyの表を並べる。制約方式で文字化けが消えても意味や反復が残れば、その限界を報告して終了する。原Base/Chat品質条件は維持する。

## 予算と今回の終了点

実測定常約694k tokens/s、前回各100M対照・全文評価のGPU累積37分34秒を参考にした見積もり。CPU実装・内容確認・記録時間は別であり、完了時刻を保証する値ではない。

| 段階 | GPU等の見積もり | GPU累積上限案 |
|---|---|---:|
| 1と2 直接総10Bと比較 | 学習区間約126分、評価等込み145〜165分 | 10,800秒 |
| 3 新親のEOS対照 | 学習約5分、合格した全文等込み35〜45分 | 3,000秒 |
| 4 UTF8単一policy | 新400生成とpolicy処理で約7〜15分の仮見積もり | 900秒 |

全段階に進めた場合のGPU等は約3〜3.75時間、上限合計14,700秒（4時間5分）。未検証の制約policy速度は実装後に測定して見積もりを更新する。最初の実行区切りは1と2の総10B学習・全文/400・報告・commit。3は10Bの改善と元安全条件に依存し、全段階の実行を依頼された場合も不合格時の分岐を保持する。7.5Bの中間比較による停止区切りは設けない。

Pythonはすべてuv run --frozen＋必要extras、WSL2/4090/Linux data。起動前にactual PID/boot/start ticksとGPU lockを確認し、永続job/log/checkpoint/sourceを保存する。過剰な全データ照合や旧GPU評価の再実行はしない。各有意な結果でstatusを更新しlocal commit、pushはしない。

今回はユーザー指定の実行準備と状態記録の保存・commitで停止する。新run/config/schema/起動commandは準備済みだが、本学習は未開始。旧launcherを新予算のまま起動しない。20B/50B/Chat/Tokenizer再学習/unlikelihood/parameter sweepは今回の実行計画に含めない。
`````

## docs/autonomous_status.md

UTF8 LF SHA256: 9631ee4a7d231a040d0c4a82488a0998dc61e1d68520099b0f328aa6ab45c2b0

`````markdown
# Codex継続作業の現在地

## 10B用実行設定の準備を完了して停止（2026-10-04 step1）

[準備完了結果](40_base_10b_preparation.md)、[保存証拠26項目](../reports/phase6/base_10b_preparation_review.json)、[完了証拠](../reports/phase6/base_10b_preparation_completion_audit.json)。ユーザー指定の直前チャット①「10B用設定・保存再開・GPU確認」を完了した。専用config/schema/runner/launcherを凍結、関連14tests failure/error/skip0。実WSL2/RTX4090/Python3.12.7 uv/BF16/Flash/compile/batch32/context1024でstable-extensionとdecay各連続4対2+保存再開2、計16updates/524,288検証tokensの全state/history/finite checks成功。元core/model/shards/uv.lock/旧runnerは不変、親4.75Bと旧final5B・両5.1B主要重みのhashを保持した。

GPU19.217秒/準備上限600秒。preparation-job complete、actual Linux459/boot077f04cc-5ba2-4da6-87d3-778c8c756de7/start_ticks9675/Windows29620終了、GPU computeなし。run `reports/phase6/base-10b-20261004/` のpreparation.json/cuda-resume-gate.json/verification checkpoints/log/environment/sourceを保持。scienceのstable/decay/result/jobは存在せず、本学習消費tokens0。引数なしshellを一度実行しalready_complete/mode=verifyで終了、検証再実行や科学学習が始まらないことも確認した。

設定済みの科学到達点は9.5B stable＋15,259更新decay、総10,000,007,168/update305176、追加5,249,990,656tokens。予定checkpoint約20.4GB/上限32GiB、空き約545GB、既存train12.23B/epoch0を使う。新規データ取得・全コーパス再監査・旧GPU評価なし。準備検証19.217秒は将来の科学学習GPU累積上限9,000秒へ含め、評価予約1,800秒は別。原品質条件は維持し、検証成功を品質達成としない。

準備/report/local commitで停止。本学習の次段階commandはWSL repoで `bash scripts/run_base_10b.sh --train`、検証専用は `--verify-only`（完了済み）。科学10B/全文評価/短文仕上げ/UTF8制約/Chatは未実行。以下のactive/live/未実装notesは履歴。

## 10B用実行設定の準備を再開（2026-10-04 step1のみ）

ユーザーの「1を対応」に従い、直前チャットの①10B用設定の準備・保存再開/GPU確認だけを実行する。新 `configs/phase6/base_10b.json`、`scripts/run_base_10b.py` とshellを実装・凍結。親4.75B stableを保持し、科学追加5,249,990,656/最終10,000,007,168を予定。関連14 CPU tests成功・failure/error/skip0。旧core/既存5B runner/旧成果物は変更なし。GPU compute jobなし、WSL空き約545GBを確認した。

次は `bash scripts/run_base_10b.sh --verify-only` で実CUDA stable/decay各連続4対2+保存再開2、合計16updates/524,288検証tokensだけを確認する。本学習は開始しない。新shellの引数なしはverify-only、長期学習は明示 `--train` が必要。run `reports/phase6/base-10b-20261004/` のpreparation-job.json/actual PID・boot・start ticks/ログ/verification checkpointを永続化し、重複jobを避ける。準備結果のCPUreview・報告・local commit後に停止。以下は履歴。

## 中間7.5Bを省き直接10Bへ進む計画へ訂正（2026-10-04 計画のみ）

ユーザーの「中途半端に7.5Bにせずにいっきに10B」に従い、[次回計画](39_learning_scale_and_generation_plan.md)を更新。既存データは12,225,819,077 train tokensなので追加収集は不要で、増やす対象は累積学習量。保存stable4.75B/update144959から明示forkし、9.5B stable＋独立15,259-update decayで総10,000,007,168 tokens/update305176へ直接進む。今回の追加科学tokensは5,249,990,656。旧7.5Bの専用decay374,996,992tokensと全文/400評価は省く。定期checkpoint・有限loss/勾配・保存再開・GPU予算の監視は保持する。

最初の実行区切りは総10B学習と同じ全文dev/400・内容比較・報告・commit。学習区間約126分、評価等込み145〜165分、GPU上限案10,800秒。原raw採用/増量条件と最良Web BPB改善を10B後に確認し、合格時だけ新親EOS対照へ進む。UTF8制約の成功を元raw方式の学習成功へ置き換えない。全後続案まで進める場合GPU約3〜3.75時間、上限案14,700秒、CPU実装・内容確認は別。

今回は計画更新/local commitのみ、新GPU学習・推論・実行config/schema/launcher実装は未開始。旧完成runnerを新予算用に再実行しない。以下の7.5B段階案は今回のユーザー訂正前の履歴であり、今後の実行指示ではない。

## 学習量拡大を主軸にした次回計画を保存（2026-10-04 計画のみ）

ユーザーの「ここまでの内容を踏まえて計画」に従い、[次回計画](39_learning_scale_and_generation_plan.md)を作成。手元のtrain12.23Bを利用し①総7.5Bと同じ全文/400の比較、②BPB改善と元raw増量安全条件を満たした場合だけ総10B、③採用可能な新親で短文20%対Webの各100Mを一対、④保存重みの単一UTF8制約policyを元方式と別評価する案。データ収集・全件再照合・旧GPU評価を先に増やさない。文字制約の成功で元raw学習gateを合格に書き換えない。

長期親は保存stable4.75B/update144959/SHA916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5。final低LR枝の通常resumeではなく新しい明示fork。7.5Bはstable7.125B＋独立decay、10Bは合格時に7.125B stableから延長して9.5B＋独立decay。両段階に進む追加科学tokens合計5,624,987,648、検証と短文対照は別。GPU見積もり各80〜105分、全段階約3.5〜4.5時間/上限案4時間45分、CPU実装・内容確認は別。最初の実行区切りは7.5Bの学習・全文/400・報告・commit。

今回は計画と状態記録の保存/local commitのみ。新run/config/schema/実行commandは未作成、新学習・GPU推論・decoder実装は開始していない。旧完成launcherを再実行しない。20B/50B/Chat/UL/Tokenizer再学習/自動sweepは含めず停止する。以下は完了結果と以前の履歴。

## EOS・反復・末尾処理の1〜3を完了・停止（2026-10-04）

[最終結果](38_eos_5b_finish_results.md)、[保存証拠44項目](../reports/phase6/eos_5b_finish_review.json)、[完了証拠](../reports/phase6/eos_5b_finish_completion_audit.json)、[全自然停止の内容確認](../reports/phase6/eos_5b_content_review.json)。①production UTF8末尾helperを共通inferenceに接続し関連33tests失敗/skip0、旧400件398正常不変/2raw失敗保持。②同じfinal5Bから低LR Web/short20を各100,007,936 tokens、実CUDA再開8updates/262,144検証は別計上。両枝update155640/累積5,100,011,520、全3,052更新有限・連続、Adam/scheduler/RNG/両cursor等保存済み。準備train12.23B/10,001,152parametersは不変、短文は19,988,480tokensでpoolを周回しない。

③同じ全文dev89,416/本文164,344,743bytesでBPB親0.964484→Web0.958092/short0.959011。固定EOS0→0/13、反復59→57/51、両固定raw Unicode0。全400はWeb EOS13/反復121/Unicode0、short EOS129/反復103/Unicode2、両empty/role0。短文BPBは新対照比+0.095894%で許容内だが、元の全400 raw失敗0条件が不合格。短文重みは正式採用せず診断用として保持する。増量gateも短文不合格、Web数値gateは合格だがBase/Chat品質は両未達。自然EOSを正答率と混同せず、数量・時刻・否定・意味反復の誤りを記録。短文固定全80/自然停止129件の116種類、補助28、対照自然停止13を内容確認、blind採点/testは未実施。

[2件のCPU診断](../reports/phase6/eos_5b_finish_unicode_review.json)：base-039 sampling43は途中byte30のinvalid start byteで末尾helperでは直らない。base-084 sampling42は上限の未完成末尾1byteで表示だけ保留可。どちらもraw不合格のまま。GPU再推論・新学習・全コーパス再監査は追加なし。

GPU累積2,253.853秒（37分34秒）/上限3,000秒。job complete、actual Linux464/bootbf739e34-e9d0-4ed9-90a5-afc9f90897aa/start_ticks10237およびWindows21524は終了、GPU compute processなし。Linux run `reports/phase6/eos-5b-finish-100m-20261004/` の最終 `{web,short20}/checkpoint-00155640.pt` を保持。SHA Web `c1b83c8e03f653af378797fbfea604ea33aec2134a6fea936ea0bb2157a9e0bb`、short `19a960feb5b809c277cd710f23765e14d27099502153561ba437eee20dd42d54`、親SHA不変。学習区間実時間Web160.883/short149.772秒（IO含む）、科学合計200,015,872tokens。全旧成果物/ログ/凍結source/全文400/補助を保持。完了restart commandを再実行しない。

目的と指定終了点を達成し、最終report/local commitで停止。次回候補は保存重みで途中不正UTF8とcap末尾を分けた単一decoder制約比較、または元計画の反復loss対照であり、今回は未実装・未起動。10B/Chat/UL/自動sweepへ移行しない。以下のlive/未完了/計画のみの記述は履歴。

## EOS改善の1〜3を実行再開（2026-10-04）

③screen全gate合格、両枝全文評価中。元固定80でWeb→short20の自然EOS0→13、反復57→51、rawUnicode/empty/role両枝0。dev256 BPB悪化+0.108%で1%以内。既存補助80はEOS0→28、反復35→27、teacher EOS argmax0→45/NLL3.724968（親）→1.093626（short）。原固定指標を補助で置き換えない。[固定80の内容確認](../reports/phase6/eos_5b_fixed_content_review.json)を保存：13自然停止を含む全80を読み、数量誤り/文脈不一致/意味反復が残る。これは人手blind採点ではない。両100M完了記録とCPUreview準備を`dfbe0c1`でcommit。全文/400と保存stateのCPU確認、最終内容確認は継続する。現在Linux464の対照全文採点が13万/21万窓、GPU累積926秒で上限3000秒内、failureなし。以下は履歴。

②両科学学習完了、③評価中。[保存済み学習記録](../reports/phase6/eos_5b_finish_training_progress.json)。両枝update155640/累積5,100,011,520tokens、各追加100,007,936、合計200,015,872。pure学習Web160.883秒/short149.772秒。短文条件の内訳Web80,019,456/short19,988,480tokens、短文poolを周回しない。checkpointは新runの各`{web,short20}/checkpoint-00155640.pt`。Web固定EOS0/80・反復57・rawUnicode/empty/role0、補助EOS0/反復35。dev256 BPB Web0.989835741/short0.990903548（+0.108%、両全文ではない）。短文の自然EOS/反復等はまだ評価中、全文採否/内容確認/保存stateのCPUreviewは未完了。Linux464は継続しfailureなし。以下の学習中/起動前は履歴。

起動後の実状態：準備commit `37f2c1f`、関連33tests失敗/skip0、保存400件のproduction表示確認合格。hidden Windows21524/Linux464/bootbf739e34-e9d0-4ed9-90a5-afc9f90897aa/start_ticks10237をactual psへ照合して稼働を確認。実CUDA連続対保存再開8updates/262,144tokensの全state/history/finite checks合格、同じ5B親の補助80はEOS0/反復35/Unicode・empty・role0。現在Web100%学習を継続、local1800updates/追加58,982,400tokens、定常約694k tokens/s、GPU92%/VRAM7,645MiBを観測。GPU累積199秒、failureなし。以降job.json/checkpointを正本としlive source/configは変更しない。以下の「起動前」は準備履歴。

ユーザーが「1~3を目的とゴールを明確にして最後まで」と指定。目的はUTF8表示末尾の安全化と、5Bの自然EOS/反復を短文仕上げで改善できるか検証すること。終了点は①production末尾helperと関連checks、②同じfinal5Bから低LRWeb/short20を各100M、③原固定screen・合格時の全文評価・内容確認・結果/commit。結果が不合格でも元基準で判定し、実用品質を達成したと扱わない。

①`src/jmicro/text_display.py`を全backend共通のinference結果処理へ追加。text/display_textは完成文字だけ、raw_text/bytes/IDs/valid_utf8/stop_reasonは保持。max-token未完成尾だけ除き、途中不正/不完全EOS/EOTはerror記録、unknownは元codecの例外を保持。[保存400件の確認](../reports/phase6/text_display_verification.json)で398正常text不変、同じ2末尾失敗はraw不合格のまま。関連tests（torch/HF/GGUF共通結果処理はmockによるcontroller/codec tests、実backend重み比較ではない）を実行。

②③は`configs/phase6/eos_5b_finish_100m.json`/新runner/schemaを凍結して実行する。親final5B update152588/5,000,003,584tokens、actualLR0.0002、Web cursorをCPU読込確認。科学200,015,872＋検証262,144、GPU上限3,000秒、run `reports/phase6/eos-5b-finish-100m-20261004/`、restart `bash scripts/run_eos_5b_finish.sh`。親補助dev80は新たに測定、親全文/400は再利用、全データ監査なし。実CUDAgate/学習は起動前。次の行動は凍結checks/commit後に重複jobなしを確認してpersistent起動。全指定範囲完了後停止し10B/Chat/UL/sweepなし。以下は履歴。

## EOS・反復・UTF8改善の調査と計画を完了（2026-10-04、計画のみ）

ユーザー指定で[調査と次回計画](37_eos_repetition_utf8_improvement_plan.md)を作成。[保存記録のCPU調査](../reports/phase6/eos_5b_improvement_research.json)、[機械可読の提案](../reports/phase6/eos_5b_improvement_plan.json)。同じ全文devの保存EOS平均NLLは元2B2.302868→5B2.223077と改善する一方、自由生成の自然EOS0/80は未解決。教師文末のNLLを自由生成のEOS確率/順位と混同しない。生成400件は398正常text不変、同じbase-070の2件で末尾未完成2bytesだけをincremental decoderに保留可能とCPUで確認。日本語/emoji途中1〜3bytesと不正UTF8の9probe成功。これはproduction修正/モデル改善ではなく、旧rawUnicode2とmax-token停止を保持する研究結果。

次回案は①CPU表示末尾helperを実装、②同じfinal5B model/Adam/RNG/Web位置を親としてpeakLR0.0002のWeb100%対short20を各100,007,936tokens、③原固定80/dev256＋既存補助80で元gate、合格時だけ全文/400と内容を確認。科学200,015,872＋実CUDA再開8updates/262,144検証を別計上、GPU累積上限3,000秒/目安35〜45分、実装・記録を含め約1.5〜2.5時間。既存accepted短文445,501件/21,000,010tokensを再利用し新データ抽出・全コーパス照合は不要。rawEOS/反復/Unicodeと表示の効果を分離し、採用失敗を免除しない。UL/decoder制約/Chatは後続提案に留める。

今回のGPU推論0秒/追加学習0。新5B仕上げrunner/config/schemaと表示helperは未実装、実行jobなし。調査/計画/report/commitで停止。次に実行する場合は上記実装・凍結と必要な保存再開確認を済ませてから一対だけ比較し、記録で一区切り。10B/Chat/UL/自動sweepへ移行しない。以下は履歴。

## 5B比較を完了・停止（2026-10-04）

[比較結果](36_base_5b_comparison.md)、[保存証拠の確認](../reports/phase6/base_5b_comparison_review.json)、[内容確認](../reports/phase6/base_5b_content_review.json)。同じ10,001,152 parameters/準備済み12,225,819,077 train tokensを保持し、追加学習0。新たにfinal5Bだけを同じ89,416保護dev/164,344,743本文bytes/42,003,934本文tokensと固定400生成で評価。元2B/低LRWeb/short20の完成結果は再実行せず再利用した。全条件の文書・本文数・生成key一致、元Tokenizer/品質基準/反復指標を保持。

| 条件 | 累積学習input tokens | 全文dev BPB↓ | 固定EOS | 固定反復 | 固定Unicode失敗 |
|---|---:|---:|---:|---:|---:|
| 元2B | 2,000,027,648 | 0.982882 | 0/80 | 60/80 | 0/80 |
| 低LR Web100M | 2,100,035,584 | 0.972969 | 0/80 | 55/80 | 0/80 |
| 新5B Web100% | 5,000,003,584 | 0.964484 | 0/80 | 59/80 | 1/80 |
| 低LR short20・別mixtureの参考 | 2,100,035,584 | 0.974799 | 27/80 | 41/80 | 0/80 |

本文BPBは元2B比約1.87%、低LRWeb比約0.87%改善。生成品質全体の改善とは扱わない。5Bの全400 EOS5/反復122/Unicode2、empty/role0。Unicode2はbase-070の同じgreedy出力（抑制あり・なし）：64-token上限で末尾UTF8がe6a5の2bytesに切れ、strict decodeがbyte168〜170でunexpected end of data。途中bytesは有効。上限処理の原因が判明しても失敗は免除せず、元の新Unicode失敗なし条件が不合格。BPB/反復の増量数値条件は通るがgrowth gate全体は不合格、10Bへの自動移行はしない。

新固定80出力を全て読み、13例を元2B/低LRと照合保存。暗い部屋で電気をつける/外出前に靴を履く冒頭は改善、個数・時刻・否定条件・因果の誤りと意味反復は残る。三回完全一致の元指標がfalseでも二回/言い換え反復を確認。独立人手blind採点ではなく、Base/Chat品質目標は未達、test未使用。

GPU788.433秒（13分8秒）で1,800秒以内、全文本文377.329秒、生成409.343秒。job complete、actual Linux477/Windows26484終了、GPU compute processなし。run `reports/phase6/base-5b-comparison-20261004/` のfull-dev.json/generation.json/result.json/aligned-content.json/source/ログを保持、final5B SHA1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273aは不変。保存記録のCPU確認18項目成功。完了jobのrestart commandを再実行しない。依頼された比較/report/commitで停止。次回の優先課題はEOS・反復の改善とUTF8末尾処理であり、10B/Chat/mixture/decoder sweepは未開始。以下は履歴。

## 5Bの比較を再開（2026-10-04）

ユーザーが「比較を進めて」と指定。[固定config](../configs/phase6/base_5b_comparison.json)、[保存済み対照の照合](../reports/phase6/base_5b_comparison_preflight.json)。新しく評価するのはfinal5B checkpoint（SHA1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a）だけ。元2B/低LRWeb100Mの完成結果を再利用し、short20は別mixtureの参考として併記する。共通12.23B trainのデータ量は変えず、今回追加学習0。低LR枝は曲線が異なり、2B対5Bでも総予算に応じ最終5%decay期間が伸びるため、全差を学習量だけの因果効果と断定しない。

同じ保護dev89,416文書/164,344,743本文bytes/42,003,934本文tokens、context1024/stride512/batch16、CUDA BF16/Math/FP32 CEでBPBを比較。固定dev80prompt/64生成tokens、greedy抑制あり・なし＋sampling3seeds（42/43/44、temperature0.8/top_p0.9）、合計400。EOS bias/強制停止/penaltyなし。元suite/反復指標/品質基準を保持。全対照の同じ文書ID/本文token/byte数と400生成condition keysをCPUで照合成功、checkpoint hash/suite/Tokenizerも凍結。

run `reports/phase6/base-5b-comparison-20261004/`、restart `bash scripts/compare_base_5b.sh`。launch/GPU lockとactual PID/boot/start ticksを照合しliveなら重複起動しない。全文devを先に保存して生成と分離する。既存unused CUDA cache解放を同条件で再利用、重み/数値演算は変更しない。GPU上限累積1,800秒、評価推定15〜20分、実装/報告は別。完了後に同じ80promptの内容を確認し、report/commitで停止。10B/Chat/追加学習やsweepは実行しない。以下は履歴。

## 次計画1・2を完了：総5B学習・停止（2026-10-04）

[保存記録の確認結果](../reports/phase6/base_5b_review.json)、[完了証拠](../reports/phase6/base_5b_completion_audit.json)、[固定計画](35_base_5b_execution.md)。①予算だけを変更するstable延長処理を実装・凍結し、CPU6tests（失敗/skip0）と実CUDA16updates/524,288tokensのstable/decay両経路の連続4対2+保存再開2で全state/history一致。②同じ1.9B parentの重み/Adam/scheduler/RNG/データ位置からWeb100%を継続し、総5,000,003,584 input tokensへ到達した。新しい科学学習3,099,983,872 tokens、検証524,288は別計上。10,001,152 parameters、train12.23B、Tokenizer/core/設定は保持。sampler epoch0/position4,882,816、train blocksの周回なし。未使用dev/testを学習しない。

| 区間 | global updates | 累積input tokens | 今回の追加tokens | 定常速度tokens/s |
|---|---:|---:|---:|---:|
| stable終端 | 144,959 | 4,750,016,512 | 2,849,996,800 | 693,786 |
| 最終decay終端 | 152,588 | 5,000,003,584 | 249,987,072 | 694,098 |

科学94,604updatesのログは全て連続/有限値で、保存済みstateのupdate/token digest/教師tokens/本文bytes/scheduler/Adam step/cursorと一致。親actualLR0.002を維持し、最後7,629updatesで0.0002へ減衰。最終checkpointにはPython/NumPy/Torch/CUDA1device RNGも保存されていることを実CPU読込で確認した。教師tokens4,989,419,356、本文bytes19,436,638,948。元1.9B親SHAは不変。全97科学checkpointを保持、run出力12,538,319,395bytesで20GiB以内。

完成重みはLinux `reports/phase6/base-5b-20261004/decay/checkpoint-00152588.pt`、SHA `1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a`。継続用stableは同run/stable/checkpoint-00144959.pt、SHA `916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5`。科学pure学習4,494.293秒（74分54秒）、GPU累積4,543.110秒（75分43秒）、上限7,200秒以内。job complete、actual Linux450/Windows28760終了、GPU compute processなし。完了jobを再起動しない。

途中のユーザー指定「現時点のコードをpushして」に従い、`origin/main`へ`c68ff34`まで通常pushし、remote/local head一致を確認済み。同じpush依頼に基づき、学習完了記録も同じ`origin/main`へ反映して停止する。

1・2の範囲で停止。5B全文BPB、自然EOS、反復、意味/文法、人手blind/testは未評価。train lossの低下を品質改善と扱わない。次の具体的な作業はstep3の同じ保護dev/固定生成による元2B・低LRWeb100Mとの比較であり、今回開始していない。10B/Chat/sweepも未開始。以下の途中経過・旧stop/live notesは履歴。

## 次計画1・2：5B継続処理と学習を再開（2026-10-04）

途中経過（2026-10-04 06:55 UTC）：同じLinux450/boot76070d40-79fb-4edd-a970-8dbc1097cfde/start_ticks13218を毎回/procへ照合して継続を確認。global122,750/4,022,272,000 tokens、約694k tokens/s、GPU経過3,118.762秒、failureなし。終了後の保存記録確認commandは `uv run --frozen --extra hub --extra data --extra ml --extra export scripts/review_base_5b.py`（準備commit55a0f2c）。終了したjob、連続更新ログ、最終model/Adam/scheduler/RNG/sampler/counter、LR曲線、元親不変、token/GPU/保存容量を確認する。GPU再学習/全文評価/全件監査は追加しない。5Bはまだ学習中。

実装/configの準備commit `be4be0f`。hidden Windows28760/Linux450/boot76070d40-79fb-4edd-a970-8dbc1097cfde/start_ticks13218をactual psへ照合し起動。実CUDA stable/decay両経路の全state/history/finite checkが全合格（16updates/524,288検証tokens）。科学stable学習開始、global58,400/1,913,651,200 tokens、初期約614k〜651k tokens/s、GPU88%/VRAM7,644MiBを実測。runのjob.json/pipeline.log/cuda-resume-gate.jsonを正本としlive source/configは変更しない。Windows launcherがWSLを保持。5B到達はまだ未完了。

ユーザーが「1,2を計画を立てて進めて」と指定。[固定config](../configs/phase6/base_5b.json)、[実行計画](35_base_5b_execution.md)。stable1,900,019,712/update57,984（SHA4edcefa7c81e05aa9403e4dc642bbe783dc68be15f140f88098ab7b2fcd3a597）から新directoryへ明示fork。core trainer/model/shards/lockは変更せず、StableExtensionTrainerが予算だけの増加を許可。Adam/scheduler/RNG/sampler/counterを保持しstableLR0.002は親と同じ。低LR100M後継学習と長期stable継続は別条件。

stable global144,959/4,750,016,512 tokens、独立7,629-update decay後global152,588/5,000,003,584。追加科学3,099,983,872 tokens。約5%decayは最寄りupdate丸め、実割合をconfigに記録。CPU関連6tests成功・skip0、config/schema凍結。実CUDA16updates/524,288tokensでstable延長と短い4update decayの連続4対2+保存再開2を照合して本学習に入る。production decay7,629とgate4updatesを区別する。

起動前actual project/GPU jobなし、WSL空き約560GB。既存12.23BをTrainViewで使用し全件再監査なし。uv/WSL4090/BF16/FP32parameters/Flash/compile/batch32/context1024。科学pure推定75分、保存等込み80〜100分、GPU累積上限7,200秒、実装時間は別。run `reports/phase6/base-5b-20261004/`、再開 `bash scripts/run_base_5b.sh`。job.jsonと/proc PID/boot/start ticksを照合しliveなら重複起動しない。全completed checkpoint/log/source保持。

今回は1・2のみ。5B学習完了・記録・commitで停止し、step3全文dev/400生成、10B/Chat/sweepは開始しない。5B品質は未評価と記録する。以下は履歴。

## 依頼された低学習率計画1〜3を完了・停止（2026-10-04）

[最終結果・完了証拠](../reports/phase6/eos_low_lr_100m_review.json)。①旧高LRログ/保存済み3点を調査し、追加200更新（6.55M tokens）でdev256 BPB1.080079、1600更新1.084941、2800更新1.083227、終了1.049848を確認。元2Bの保存済み全文評価の同じ256文書の参考再集計は1.015857（batch配置の違いを注記）。最初の保存点で退行、終盤decayで部分回復。正確な最初の悪化updateは未観測。

②同じ元2B親/Adam moments/RNG/Web cursor/既存完結pool/aux80から、LR曲線全体だけを10分の1（peak0.0002/末端0.00002）にしたWeb/short20を各100,007,936 input tokens学習。両枝全3052更新のtoken digestとEOS教師数が旧対応枝と一致、実CUDA8更新の連続対保存再開が全state/historyで完全一致。科学200,015,872＋検証262,144を別計上。12関連tests成功・失敗/skip0。初期jumpだけを分離した比較ではなく、この単一seed/100M条件でLR曲線を下げる効果を測った結果。

③両枝を同じ89,416dev/164,344,743本文bytesと400生成で全文評価。以下のBPBは小さいほど良い。固定生成は元dev80/greedy/64上限、EOS bias・強制停止・penaltyなし。

| 条件 | 全文dev BPB | 固定自然EOS | 固定反復 | 全400 empty/role/Unicode |
|---|---:|---:|---:|---|
| 元2B基準 | 0.982882 | 0/80 | 60/80 | 0/0/0 |
| 旧高LR Web100M | 1.016473 | 0/80 | 50/80 | 対照全文BPBのみ・400未実施 |
| 旧高LR short20 100M | 1.017580 | 24/80 | 49/80 | 0/0/0 |
| 新低LR Web100M | 0.972969 | 0/80 | 55/80 | 0/0/0 |
| 新低LR short20 100M | 0.974799 | 27/80（33.75%） | 41/80 | 0/0/0 |

新short全文BPBは新Web比+0.18814%、元mixture/全文gate全合格。全400のEOSはWeb5/400・short225/400、反復119/400・84/400（複数decoding合計で固定80と混同しない）。補助EOSはWeb0/80・short37/80、短文teacher EOS NLL0.492/argmax66/80。補助は旧高LR short42/80から低下、反復29→37/80なので全指標改善とはしない。Web補助empty1も保持。補助の失敗を原固定suiteへ置き換えない。

全27自然停止を内容確認し、12例の意味反復/個数/時刻/文脈の誤りをgeneration-content-review.jsonへ保存。原三回完全一致反復指標は変更せず、見落とす二回/言い換え反復を例として併記。独立した人手blind採点ではない。元Base文法70%/Chat停止95%等の品質目標は未達、test/Chat未実施。改善した重みは候補として保存するが、実用品質として短文枝を採用しない。元2Bも保持。Webの元増量条件（全文BPB+0.001以内、固定反復+8未満、新empty/role/Unicodeなし）は全合格。ただし依頼範囲1〜3で止め、5B/Chat/自動sweepは開始しない。

完成重みはLinux `reports/phase6/eos-low-lr-100m-20261004/{web,short20}/checkpoint-00064088.pt`、各累積2,100,035,584 tokens。SHA Web660d646bc0f12d326ca3fdc5849877f51c5c42bd5aa37070712b6bf5be3b8598 / short64e232ce87576d9128ab65426a31a2fc2afb88e5ef31162dba608c60c1a4a141。pure学習160.932/149.528秒、定常690,619/693,787 tokens/s。累積GPU処理2141.290秒（35分41秒）、凍結2700秒以内。cache解放は各全文・生成で18回、数値演算/重み/評価条件は変更なし、全固定80 IDsもscreenと一致。観測reserved最大14,652,801,024bytesはforward間の観測値で、全kernel中の真のpeakとは区別する。旧core/Tokenizer/data/sourceは保持、全完了check合格。offline reviewerの単一optimizer groupという誤った仮定は、元親と同じ2 groupsを照合するよう修正し再照合成功（GPU再実行なし）。job complete、actual Linux498とhidden Windows27984終了、GPU compute processなしを確認。

次の行動はreport/commitで停止。5Bを行う場合は別段階としてstable checkpointからの予算延長/学習率/decayを凍結し、今回の完成decay枝を通常resumeで延ばさない。低LR短い継続の成功を全長期学習率の最適値と一般化しない。以下の実行中・旧結果・停止境界は履歴。

## 低学習率対照の1〜3を開始（2026-10-04）

③Web全文/400生成が完了。共通89,416dev/164,344,743bytes BPB0.9729687290810604、元2B0.9828815577636254・旧高LR1.016473459461069より改善。全文body採点380.659秒。固定EOS0/80/反復55、400全体EOS5/反復119/empty・role・Unicode全0。short20全文採点中。Web数値増量条件は満たすが、1〜3の実行境界に従い5B/Chatを開始しない。

②の両100Mと元/補助screen完了、③全文評価中。LR0.0002 Webはdev256 BPB1.004728/EOS0/80/反復55/Unicode0、short20はBPB1.006904/EOS27/80/反復41/Unicode0。固定mixture gate全合格、補助EOSはWeb0→short37/80。Web補助にempty1があることも保持（原固定gateを補助suiteで置き換えない）。旧LR0.002のWeb/short BPB1.049848/1.049828、短文EOS24/反復49に対し今回改善。Web全3052更新のtoken digestが旧Webと一致、同じ入力でstable train loss中央値2.873557→2.677854。自然EOS27件を全て内容確認し12例をgeneration-content-review.jsonへ保存：意味反復/文脈/個数/時刻の誤りが残り実用品質として未採用。元の三回完全一致反復指標を変更せず、見落とす二回/言い換え反復は例として記録。人手blind採点ではない。actual PID498のままWeb全文採点中、shortの全文/400も条件に従い続ける。runner/config/sourceは凍結状態を維持。

準備はe093bf4へcommit済み、12関連tests成功・skip0。hidden Windows27984/Linux498/boot a611e59d-22d2-4365-bfd8-446c6c51b98c/start_ticks8780でGPU jobを起動しactual psを確認。job.json/pipeline.logと有効なlatest checkpointを正本にする。①は終了：旧Web追加200更新（6,553,600tokens）dev256 BPB1.080079、1600更新1.084941、2800更新1.083227、終了3052更新1.049848。元2Bの保存済み全文評価の同じ256文書を追加GPUなしで再集計すると1.015857/472,055bytes（batch配置の違いを注記）。200更新の時点ですでに退行を観測、終盤decayで一部回復。正確な最初の退行stepやLRの因果効果は未確定。historical-analysis.json/3 probes/historical-parent-reference.jsonを保持。②は実CUDA全state再開gateを通りWeb低LR学習中。live processがある間はrunner/config/sourceを変更せず、このjobを監視する。

ユーザーが「1,2,3を計画を立てて進めて」と指定。[凍結config](../configs/phase6/eos_low_lr_100m.json)、run `reports/phase6/eos-low-lr-100m-20261004/`、restart `bash scripts/run_eos_low_lr.sh`。まず旧Web100Mログと保存済み200/1600/2800更新checkpointを同じdev256で採点し、退行の観測時点を記録する（追加学習0、全文再評価なし）。その後、同じ元2BからpeakLR0.0002のWeb/short20を各100,007,936 input tokens、2900 stable＋152 decayで学習。旧比較の0.002に対してLRだけ変更し、元の32〜64-token pool/aux80/optimizer moments/RNG/Web cursorを再利用する。科学200,015,872、実CUDA全state再開gate262,144は別計上。core/旧pilot/Tokenizer/過去成果物は変更しない。

採否は元固定80/dev256と同じmixture gate、Web screen-safe時だけ全文dev/400、short gate合格時だけ全文dev/400。shortが合格しWeb生成が不適格なら、Web全文BPBだけ対照として測る。元2B BPB+0.001/反復+8未満/新失敗なしの増量条件、原Base/Chat基準は維持。cache管理を最初から適用し、調査・学習・評価を合計GPU2700秒で制限、実際の消費と有効checkpointを保存する。CPU準備は既存poolの再利用と新LR経路の関連testsのみ。report/commit後停止し5B/Chat/sweepへ移行しない。以下は旧100M完了時の履歴。

## 完結単位100M対照を完了・停止（2026-10-04）

[最終結果と照合済み証拠](../reports/phase6/eos_complete_100m_review.json)。同じ完成2B親から各100,007,936 input tokens、合計200,015,872を学習。検証262,144 tokensは別計上。固定80/64上限はWeb EOS0/80、short20 EOS24/80（30%）、反復50→49/80、Unicode1→0。補助短文80はEOS0→42（52.5%）、反復51→29、真の終端EOS NLL4.046→0.449/argmax0→72。EOS bias/強制停止/penaltyを使わない自然停止の改善。

同じ89,416 dev/164,344,743本文bytesの全文BPBはWeb1.0164734594610705、short1.0175798867261283（対照比約+0.10885%）。短文full400はEOS232/400、反復101/400、empty/role/Unicode全0。400件は複数decoding条件の合計でありgreedy EOS30%と混同しない。元screen採用条件/全文BPB1%/固定80生成IDs一致/新規失敗0は合格。ただし内容確認で計算・時刻・文脈の誤りと意味反復が残り、実用品質としては未採用。元2B全文BPB0.9828815577636254より両枝が悪化し、Web screenのUnicode退行もあるので5Bへ進めない。原Base文法70%/Chat停止95%の品質目標は未達、人手blind/test/Chatは未実施。元2Bを基準として保持し、改善した短文重みを診断候補として保存。

完成重みはLinux run `reports/phase6/eos-complete-100m-20261004-r2/{web,short20}/checkpoint-00064088.pt`、各累積2,100,035,584 tokens。Web SHA837173885946c5a8953a717e7aa7d7993abf2ac09399e1ea150cbd8f85561eb2、short SHA6ccfa4e9957701ab860891a7efbeb55ebfd3e9c0fa45c0c1fb886e9cf1c67802。実CUDA8更新の連続/保存再開全state一致、関連22＋cache2 tests成功・skip0、offline reviewer完了チェック全合格。train pool445,501単位/21,000,010 tokensはWSL内に保持。学習定常約689k/694k tokens/s、各160.259/149.460秒。

評価の可変shapeによるunused CUDA cache膨張へ対応し、32 forwardごとの条件付きcache解放で全文採点を完了。数値演算/重み/入力/backendは変更せず、固定80生成IDsもscreenと完全一致。mainの中断2250.340秒は保持、別の凍結1200秒復旧は1054.859秒で完了。累積GPU3305.199秒（55分5秒）は原2700秒上限を超過し、`original_total_GPU_budget_respected:false`として記録。元上限達成とは扱わない。旧job/中断判断/log/checkpointsを保持し、`evaluation-recovery-job.json`のみcomplete。Linux439とWindows25296の実終了、GPU compute processなしを確認。復旧に追加学習はない。

次の境界はreport/commit後に停止。5B/Chat/自動sweep/完了評価の再実行はしない。次回検討は意味整合・反復と元2BからのBPB退行を含む品質改善であり、停止率だけで実用品質と判断しない。単一seed/この100M条件の結果であり、旧25Mとの差は単位長と量を同時変更したため個別因果を分離できない。以下の実行中/準備/計画のみ記述は履歴。

## 実行を再開: 完結単位100M対照（2026-10-04）

キャッシュ管理付きの復旧評価へ移行。fresh processでもnative CUDAの確保済みVRAMが再び24GiBへ増えて減速したため、旧PID447をidentity照合してSIGTERM、旧main jobはinterrupted/GPU2250.340秒のまま保存。新しい`jmicro.evaluation_memory`は32 forwardごとにreserved>8GiBかつ未使用>4GiBならunused cacheだけ解放し、weights/input/backend/採点条件を変更しない。2関連tests成功・skip0。`recover_eos_complete_evaluation.py`は同じ完成checkpointsと全screen/gateを再利用し、短文全文dev/400生成とWebの全文BPBのみを完了させる。[復旧config](../configs/phase6/eos_complete_evaluation_recovery.json)で別処理1200秒上限を凍結。元2700秒の計画は変更せず、累積超過の有無をreportで明示し、元上限超過を合格とは記録しない。科学予算/品質基準は維持し追加学習0。

現在のWindows launcher25296/Linux439/boot44655da4-5b8c-4da8-a7a5-47ae16b364c1/start_ticks270963、`evaluation-recovery-job.json`/evaluation-recovery.logが正本。restartは`bash scripts/run_eos_complete_evaluation_recovery.sh`。初期wrapper/SIGTERM判断/旧jobは保持。復旧334秒/199,680採点時点でcache解放3回、reserved最大観測8.49GiB、実GPU使用約6.46GiB。VRAM24GiB時の減速を回避している。mainは再起動せず、この復旧jobのactual process identity/完了成果物を確認する。未起動の旧full-BPB専用CLIは準備履歴。次は両枝の同じ全文BPB、shortのfull400と固定80 IDs、cache/GPU予算をreviewしreport/commitして停止。以下は経過履歴。

評価processを切り替えて再開中。旧PID453は全文採点205,824/213,432付近でVRAM24,057MiB/低い採点速度となったため、actual boot/PID/start ticksを照合して単一SIGTERM。2枝の完成100M checkpoints/固定・補助screen/CUDA gateは保持し、GPU消費1659.014秒を累積へ引き継ぐ。未完了の全文採点だけをfresh processでやり直す。Windows launcher26364/Linux447/boot44655da4-5b8c-4da8-a7a5-47ae16b364c1/start_ticks208235、restartは`bash scripts/run_eos_complete_evaluation_resume.sh`。元main runner/config/source hashを変更せず、wrapperで元のseed/TF32無効/決定性flagsを明示。初期VRAMは3,417MiBへ低下。学習由来のGPU allocation保持が影響した仮説は支持されるが、具体的cache機構はprofileしていない。旧job/中断snapshot/判断を`evaluation-process-restart.json`等へ保存、原GPU2700秒上限を維持する。次の対照BPBもfresh processで採点する。以下は切替前の経過。

2枝100M学習と固定/補助screenは完了。Web100Mは固定EOS0/80/反復50/80/Unicode1、短文100MはEOS24/80/反復49/80/Unicode0、dev256 BPB1.049848対1.049828。補助短文はEOS0→42/80/反復51→29/80、teacher EOS NLL4.046→0.449。短文は元改善gateを通り、main jobで短文の全文dev/400生成を評価中。一方WebのUnicode退行で通常の全文/5B進行は不適格。同予算での全文BPB1%比較に必要な対照BPBだけを[別config](../configs/phase6/eos_complete_100m_full_bpb.json)/`bash scripts/run_eos_complete_full_bpb.sh`でmain processの実終了後に測る。元main config/重み/80生成/科学予算と初期結果は変更せず、原累積GPU2700秒へ加算する。対照400生成・学習は再実行しない。

全24停止出力を内容確認し、玉2+1への「2個」、15時+1時間への「15時」、暖かい部屋の氷への寒い部屋の説明等、文脈制約の誤りと意味反復を`generation-content-review.json`に保存。EOS24件の改善は保持するが、元の「無意味な停止を採用しない」条件に従い実用品質を達成したとはしない。三回の完全一致を検出する既存反復指標は二回/言い換え反復を見落とすので、元指標を置き換えず生成例を併記する。人手blind採点/test/Chat/5Bは未実施。次は2枝の同じ全文BPBと短文full400失敗/IDsの確認、review/report/commitして停止。以下は起動時の履歴。

GPU比較を永続起動済み：Windows hidden launcher16164、Linux PID453/boot44655da4-5b8c-4da8-a7a5-47ae16b364c1/start_ticks39818、`reports/phase6/eos-complete-100m-20261004-r2/job.json`とpipeline.logを保存。起動時のactual ps/GPUを確認、stageはresume-gate。実装・学習前準備は713f497へcommit済み。valid completed-update checkpointのlatest.jsonから再開し、source/config bindingと累積GPU2700秒予算を保持。以下は起動前の経過。

学習前準備はr2で完了：[準備証拠](../reports/phase6/eos_complete_100m_preparation.json)。445,501単位/21,000,010 input tokens、94,157親文書、本文平均45.14（32〜64）tokens、exact重複2,031除去、8 CPU workers/4.578秒。22関連tests成功・skip0。最初16＋均等配置12のtrain単位、補助dev8の内容と元文書span/Tokenizer/BOS/EOSを少量確認し、content-review.jsonを保存。人手blind意味採点ではなく、元Webの文体/文脈依存は残る。r1の長い見出し/表記号を除外し、旧CPU-only pool/評価準備を保持。最終run/bulkは`eos-complete-100m-20261004-r2`。config/source snapshotも保存済み。次はCUDA全state保存再開gateと2枝学習。以下r1準備中の記録は履歴。

ユーザーが「次に案を計画を立てて実行して」と指定。[実行config](../configs/phase6/eos_complete_100m.json)で同じ2B親から各100,007,936 input tokensを新しく学習する。科学比較合計200,015,872、短文19,988,480（約20%）、2,900 stable＋152 decay更新。元dev256/固定80 greedy64を維持し、補助dev80を学習前に固定。EOS+8/80等の元gateと原Base/Chat品質基準を保持。CPU600秒/GPU2700秒上限、全文評価はWebのscreen非退行時とshort採用gate合格時、最大2枝。実行境界は比較/必要な全文評価/report/commitまでで5B/Chatは開始しない。

完結単位builder/100M runner/parameterized reviewerを実装。既存Trainer.step/BlockSampler/PilotTrainerと旧runnerの検証済み学習・評価関数を再利用し、core model/trainer/Tokenizer/既存corpusは変更しない。現在20関連tests成功・skip0。CPU poolワーカーが親のSIGTERM handlerを継承して終了処理が停止したため、親PID/boot/start ticks/8子PIDを照合しidle CPU childrenだけguarded SIGKILL、旧親はpreparedで正常終了した。worker initでsignalを既定へ戻し、親にcooperative handlerがある条件を関連testに追加した。GPUは未使用。

初回pool441,323単位/21,000,019 tokens/65,750親文書を抽出したが、事前内容確認で名詞断片・短い見出し混入を発見。単位filterを保守的な述語終端/短い見出し除外で修正し、学習前にr1へ作り直す。旧pool/job/cleanup記録は`reports/phase6/eos-complete-100m-20261004/`と同名bulk poolへ保持。新runは`reports/phase6/eos-complete-100m-20261004-r1/`、bulkは同名r1、`bash scripts/run_eos_complete_100m.sh`で有効な完成準備/checkpointを再利用。job.jsonのactual PID/boot/start ticksとlauncher記録を確認して重複起動しない。次はr1 poolの少量内容確認を保存し、実CUDA全state再開gate後に2枝学習・固定/補助評価へ進む。過去の計画のみ/完了記録は以下に保持。

## 次の計画を更新・実行は未開始（2026-10-04）

ユーザーの「ここまでの検証を踏まえた計画」に応じ、[次回100M対照と5B以降の計画](27_phase6_remaining_plan.md)と[提案JSON](../reports/phase6/eos_next_plan.json)を作成。今回の依頼は計画作成で、データ抽出/推論/学習は開始していない。EOS教師1.684倍でも停止0、32〜128poolの平均105と64以下1.49%、25M追加が親2Bの1.25%という実測を踏まえ、train内の完結した32〜64-token文/段落単位を21M以上準備してWeb対照と各100,007,936 input tokensで1回だけ比較する案。単位の終端は新しいrecordの定義であり、元Web記事のEOSと同じ位置とは主張しない。

各3,052更新（2,900 stable＋152 decay）、短文610更新/19,988,480 tokens、約20%混合。科学比較合計200,015,872 tokens。100Mではscheduleが異なるため旧25M controlをそのまま再利用しない。固定80 greedy/dev256に、trainと分離した補助短文dev80を追加して学習前に凍結。mixture採用gateはEOS+8/80/反復非悪化/empty-role-Unicode0/BPB+1%以内を維持。補助suiteで元の失敗を置き換えない。pool CPU上限案600秒、GPU上限案2700秒。screenは10〜15分、全文1枝なら25〜30分、2枝なら35〜40分がGPU推定で、実装時間は別。

次回の実行境界案はこの1回の比較/必要な全文評価/report/commitまで。不合格で小mixtureの自動sweepを続けない。短文gateはmixture採用を決める基準であり、Base増量やChat停止95%の判定とは分ける。Web100Mの全文/生成に重大退行がなければ、次の独立段階としてWeb100%の5B比較を検討する。保存済みstable1.900Bから明示的予算延長fork（未実装）で4.750B stable＋0.250B decay＝総5.000B、追加3.100B、学習/保存/評価90〜120分の案。元2B decayやshort枝を通常resumeで延ばさず、21M poolを主系列の20%に何十周も混ぜない。5B結果で10B/必要なBase品質/Chatへ進む判断を残し、元の70%文法/95%停止等の能力基準は維持する。

次の具体的作業は、完結単位builder/補助suite/100M runner/parameterized reviewerの実装とpool確認。既存step/sampler/Tokenizers/WSL設定を維持し、差分の最小checksと全state保存再開、actual process identity/latest checkpointを必要範囲で確認する。全件corpus再監査・追加一般データ取得は計画の前提にしない。以下の停止/実行中記録は履歴。

## 完了・停止: EOS短文混合の対照学習（2026-10-04）

ユーザー指定の改善計画を[凍結config](../configs/phase6/eos_short_pilot.json)で実行し、[実測・完了確認・次の案](../reports/phase6/eos_short_pilot_review.json)を保存。科学比較は同じ2B model/Adam moments/RNG/Web cursorから2枝を作り、各763更新/25,001,984 input tokens（725 stable＋38 decay）、合計50,003,968 tokens。両枝LR0.002から末尾減衰で0.0002。検証2回計16 GPU更新/524,288 input tokensは科学予算と分けた。各重みの累積学習量は2,025,029,632 tokensで、2枝の学習量を1モデルへ合算しない。

| 条件（各25M、同じ評価） | 64 tokens以内EOS | 反復 | dev256 BPB（小さいほど良い） | dev256平均EOS NLL |
|---|---:|---:|---:|---:|
| 従来Webのみ | 0/80 | 62/80 | 1.068518 | 2.424873 |
| 短文20.0524%混合 | 0/80 | 54/80 | 1.069161 | 2.331916 |

両条件Unicode/role/empty失敗0。短文条件は反復8件減、末尾EOS予測lossが低下したが、自然EOS停止の改善は0件。本文BPBは対照比+0.06025%とほぼ同等だが僅かに悪化した。このBPBは共通256 dev/472,055 body bytesで、既存全文89,416 devのBPB0.982882とは直接比較しない。

凍結改善gateの「EOS対照より8件以上増」が不合格で、反復非悪化/失敗0/BPB悪化1%以内は合格。短文20%条件を採用して解決済みとはせず、元2Bモデルを既存の基準として保持する。有望候補のみ全文dev/400生成という条件に従い、全文再評価は未実施。test採点/5B/Chat/追加sweepも未開始。実験の完了とモデル品質達成は区別する。

新poolは元trainのBOS/body/EOSを保持した32〜128-body-token文書47,844件/5,100,109 tokens、抽出5.443秒。句末記号に加え明らかな省略記号/続きを読む等の終端を除外。平均104.60/中央値107 tokensで、64以下は712件（約1.49%）しかない。意味完結性はblind人手採点で保証したものではない。mixingは153更新/5,013,504 short input tokens＋610更新/19,988,480 Web input tokens。実EOS教師数はWebのみ53,161、混合42,506＋47,025＝89,531で教師露出は増えたが、greedy停止は改善しなかった。データ量一般や全ての短文条件が無効という結論にはしない。

次の未起動案は十分に多様な32〜64-token完結単位をtrainから定義/準備して1回の25M treatment比較を行うこと。文/段落の単位と完結境界を明示し、712文書だけを何十周も繰り返したり任意token位置を切ってEOSを付けたりしない。同じparent/Web/settingsなら完成controlを再利用できる。gateと元Base/Chat品質基準は維持し、追加予算/データを凍結してから実行する。現poolの長さと固定64生成のずれは検証仮説で、停止失敗の単一因果原因として確定していない。

raw runはLinux `reports/phase6/eos-short-pilot-20261004-r1/`、job complete（PID487/boot58a2da81-1901-4608-99ee-ea8177369e7a/start_ticks28827）。旧95.1565秒を含むGPU累積337.027秒（5分37秒）、1800秒上限内。学習control45.425秒/short45.546秒、定常中央値655,336/658,177 tokens/s。Windows launcher25436/Linux jobは実終了、GPU計算job0。5 unit tests成功、実CUDA連続4対2+保存再開2（short/web/安定→減衰を含む）でmodel/optimizer/scheduler/RNG/sampler/counters/history全一致、元生成8件のIDsも再現。完成checkpoint2つの実hash/保存state/counters・全763更新finite・共通dev/body採点/80固定case/自然EOS IDを確認。元2B checkpoint SHAも不変。新データ全件監査は繰り返していない。

Web control重みは旧run `eos-short-pilot-20261004/web/checkpoint-00061799.pt`、SHA `a7a85bbe33ccf6f7bd6eadb0af2c80ed55aebf4e48bc070cff70a0cc91a0825f`。短文重みはr1 `short20/checkpoint-00061799.pt`、SHA `2cf8d81b709f25f6bddba68abcc3f954263010bd3ced6e72abc7a96b080c3abe`。checkpointへmodel/optimizer/scheduler/RNG/両source sampler/route位置/token/EOS counters/lineage/source bindingを保存。core model/training/shards sourceは変更せず、新しい `jmicro.eos_pilot`から既存Trainer.step/BlockSamplerを使用。Pythonは全てuv。

初回poolの省略終端を内容確認で発見し、short開始前にguarded SIGTERMで旧pipelineを停止。完成controlはsettings/module/parent/Web routes/short input0・cursor0を確認して再利用し再学習しなかった。未完了の80生成だけを再評価。旧計画/runner/job/log/pool/gateは保持し、fixed評価結果を見てから条件変更したものではない。初回8更新とr1の8検証更新も上記に含める。`bash scripts/run_eos_short_pilot.sh`は完了jobを再実行しない。対照実験を完了したためreport/commitで停止。以下は起動時の履歴。

### 起動経過（過去の実行中記録）

短文pool例に省略終端`...`が含まれたため、短文treatment前に単一のguarded SIGTERMで旧pipelineを停止し、元から省略された終端/続きを読む等の除外を追加。旧Web controlは763更新/25,001,984 tokensを完了済み、short input0/short cursor0を保存checkpointで確認して引き継ぎ、再学習しない。旧計画/runner/job/log/最初のpool/gateは保持。新版poolは47,844文書/5,100,109 tokens、5.304秒で抽出済み。句末filterに加えて明らかな省略を除外する5 tests成功。新poolによる実CUDA保存再開gateと元生成8件再現も成功した。

現在のLinux runは`reports/phase6/eos-short-pilot-20261004-r1/`、poolも同名r1。Windows hidden launcher25436、Linux487/boot58a2da81-1901-4608-99ee-ea8177369e7a/start_ticks28827。job.jsonはgeneration80/running（Web controlの固定80評価中）。本比較ではWeb controlの学習settings/source/parent/全Web routesとzero-shortをcheckpointで検証し、完成したcontrolを再利用する。途中で中断した生成評価のみ必要分を再実行する。旧95.1565秒もGPU累積上限へ加算し、2回のgate検証は科学比較50Mとは別に計524,288 input tokensと記録する。固定評価を見てから選択条件を変えたものではなく、元データ内容の確認でtreatment前に修正した。

ユーザーが上記改善計画の立案・実行・結果報告を指定。[凍結計画](../configs/phase6/eos_short_pilot.json)：元2B model/Adam moments/RNG/Web cursorから明示的に別forkを作り、両枝同じLR0.002を725更新、末尾38更新で0.0002へ減衰。各763更新/25,001,984 input tokens、対照2枝計50,003,968 tokens。短文混合枝の153更新/5,013,504 tokens（20.0524%）は既存trainの元から完結した32〜128-body-token文書、残りはWeb。EOS強制/加点/loss重み変更はしない。句末記号のfilterは意味品質を保証する人手採点ではない。

新しい`jmicro.eos_pilot`は既存Trainer.step/BlockSamplerを使い、2source cursor/混合位置/tokenとEOS実数/optimizer/scheduler/RNG/global counters/lineageを保存する。core model/train/shards sourceは変更しない。巨大train index/全件hashは再読しない軽量train mmapを採用し、既存builder/loaderの受入policyを継承。新短文poolは5.1M以上を180秒以内に抽出し、その小stream hashを確認する。追加依存なし、Pythonはuv。

route再開・EOS教師/BOS mask・chunk境界文書保持・schedule境界の4 unit testsは成功。GPU起動前の計算processは0件。実CUDA連続4 vs2+保存再開2（安定→減衰/short2+web2を含む、検証8更新262,144 input tokens）と元生成8ケース再現確認後、実対照学習へ進む。両枝は同じdev256/固定80 greedy64で評価し、EOSが対照より8件以上増加・反復非悪化・empty/role/Unicode0・BPB悪化1%以内の凍結改善gateを使う。中間改善判定であり元品質基準は変更しない。

Linux run `reports/phase6/eos-short-pilot-20261004/`、short pool `~/jmicro-data/phase6/eos-short-pilot-20261004/`、起動/再開は`bash scripts/run_eos_short_pilot.sh`。job.jsonのPID/boot/start_ticksを実/procへ照合しliveなら重複起動しない。valid latest checkpointから再開し、完了stageは繰り返さない。GPU累積1800秒上限。科学比較50M tokensとは別に検証更新を明記。有望候補のみ全文dev/400生成を採点し、結果・失敗も保存/report/commit。今回のgoalは対照実験の完了と結果報告で、5B/Chatは未開始。以下は過去の完了/停止/提案。

## 完了: 2BモデルのEOS原因調査（2026-10-04）

ユーザーの「まずEOS原因調査」により[限定計画](../reports/phase6/eos_2b_plan.json)を実施し、[結果と次の比較案](../reports/phase6/eos_2b_review.json)を保存。WSL/4090で298.556秒、学習更新0。旧調査と同じdev末尾256件/固定prefix80件、categoryごと2件の20prefixでgreedyと反復penalty1.1を512 tokensまで比較した。原greedyの最初64 IDsは保存済み評価と20/20件で完全一致。EOS3は抑制対象外、streamはBOS/body/EOSで、loss maskはBOSのみ。EOSが選ばれた5件は実際に停止し、停止controllerの不具合は見つからなかった。

| 同じ20 devケース | 64 tokens以内EOS | 512 tokens以内EOS | 最初64 tokensの反復 | 全出力の反復 |
|---|---:|---:|---:|---:|
| 原greedy | 0/20 | 0/20 | 17/20 | 20/20 |
| 反復penalty1.1 | 0/20 | 5/20 | 6/20 | 20/20 |

penaltyによる停止は435/452/478/485/491 tokensで、長い反復の後だった。EOSを強制/加点していないが、短く正常に終わる改善には足りないため、このdecoderを採用して解決済みとはしない。両条件Unicode/role失敗0。64-token固定評価は変更しない。原greedyは全10,240生成位置でEOSを選ばず、反復を続けた。制限を512へ延長するだけでは停止しない。

同じ真の末尾256件のEOS argmaxは旧35→新46件、平均EOS確率18.11%→21.52%。210/256件は実際の末尾でも続きを優先する。既存全文devのEOS NLLを再利用すると平均2.536982→2.302868、幾何平均確率7.91%→10.00%と改善している。8件だけのFP32/BF16末尾比較はargmax差0（全precision影響を排除する結果ではない）。EOS未学習/教師漏れの証拠はなく、直接観測された機構は生成中にEOSの順位が続きのtokenより低く、反復のfeedbackを続けること。新trainはmanifest上平均body470.41 tokens/EOS stream比率0.21168%。Web文書の終わりと短文完結の分布差は次の検証仮説で、単一の学習原因やデータ量だけの因果効果は未確定。

次の案は同じ2B checkpointから別experimentとして25Mずつの対照2枝（計50M、decay含む）：既存Webのみと、train内の元から完結した32〜128-body-token文書を20% input tokens混ぜた条件。恣意的な切断位置にEOSを追加せず、dev/testは学習に使わない。固定80 greedy/256 devの差を測り、有望な候補だけ既存全文dev/400生成を評価する。これは未起動の案で、実fork/保存再開・短文pool・丸めた予算を実装/凍結してから実行する。元の品質基準は維持。EOS改善確認後の増量案は5B消費tokensで、手元12.23B trainを使うため追加取得は不要。

Linux raw runは`reports/phase6/eos-diagnosis-2b-20261004-r1/`、jobはcomplete（PID613/boot0a914750-3adc-463c-8eb2-0f6e7d2cc45d/start_ticks5457）。process/GPU計算jobは終了。model tensors不変/checkpoint stat不変を確認し、元の2B checkpointを保持。decoderに関係する3 testsはuv経由で成功。初回setupは既存のCRLF正規化hashをraw hashとして比較した誤りでGPU開始前に終了し、既存implementation_hashesに合わせて修正。失敗jobとlogは元の`eos-diagnosis-2b-20261004/`に保持し、同じ失敗を再試行していない。新データ全件監査・旧GPU調査・全文dev再採点は実行していない。以下の停止境界と実行中説明は履歴。

最終更新: 2026-10-04（日本時間）。実測の正本はreportとWSLのrun/data、milestoneは[roadmap](15_project_roadmap.md)。

## 完了・停止: ローカル12.23Bデータと新データでの2B学習

2026-10-04: [2B学習・既存評価・保存を完了](../reports/phase6/base_2b_10b_data_review.json)。stable1,900,019,712＋decay100,007,936＝総2,000,027,648 input tokens、61,036更新。epoch0/位置1,953,152で終了。stable47分10秒、decay3分44秒、既存評価11分47秒、全体62分44秒。定常学習中央値707,318 tokens/s。最終checkpointのhash/counterとmodel/optimizer/scheduler/RNG/samplerを含む保存stateを確認。元stable親のhashはdecay後も一致。全63checkpointを保持した。全件再監査・再学習・再採点は実施しない。

旧500Mと同じdev89,416文書/164,344,743 body bytesでBPB1.022491→0.982882、約3.874%低下。固定400生成のcase/seed/decoding条件も同じで、greedy（抑制あり）は反復66/80→60/80、EOS0/80→0/80。sampling3seeds合計は反復11/240→2/240、EOS1/240→6/240、Unicode失敗1/240→0/240。予測性能は改善したが、greedy反復・停止の課題は残り、会話品質目標は未達。データと消費学習量が同時に変わったため、データ量だけの因果効果は確定しない。test採点・人手採点は未実施。

最終重みはWSLのreports/phase6/base-2b-10bdata-20261004/decay-2B/checkpoint-00061036.pt、SHA165f9c177961a82b3da1c5ab1d21a32078b35b02e594fb2eb09edd7dbd4ea183。stable親はstable/checkpoint-00057984.pt、SHA4edcefa7c81e05aa9403e4dc642bbe783dc68be15f140f88098ab7b2fcd3a597。最終supervisor.jsonはevaluate/complete（999/start_ticks2671925）。pipeline/supervisor/workerは終了しGPU計算jobなし。新shardsと旧成果物は保持。ユーザー指定の2Bに達したため停止し、5B/10B/Chat/decoder比較へ進まない。

以下は新run開始時とデータ整備・旧監査の経過記録。

2026-10-04: ユーザーの「過剰な検証や照合はしなくていい」「学習に早く入りたい」に従い、独立監査の残りを停止。最後の進捗は29/32band、raw128files/全29,208,256records再構築は済み。構築時の全32band重複処理・全export往復検査と、[実train loaderの合格](../reports/phase6/corpus_10b_loader_ready.json)で[ローカル10B整備を完了](../reports/phase6/corpus_10b_ready_review.json)。train12,225,819,077 tokens/25,879,667文書、dev/testは別。loader49.147秒、batch2×1024・sampler再現一致。独立全件監査は未完了のまま明記し、`job.json`のInterruptedError/failedは[ユーザー指定の監査停止](../reports/phase6/corpus_10b_validation_policy.json)によるもの。構築済みmanifestと凍結sourceは変更せず、再監査・再exportしない。

ユーザーは2B学習を明示指定。[新しい学習config](../configs/phase6/base_2b_10b_data.json)と[実GPU開始記録](../reports/phase6/base_2b_10b_data_start.json)。同じ約10M/NoNormモデルをseed42で別runに初期化し、旧500M重みは保持する。stable57,984更新＋decay3,052更新、総2,000,027,648 tokens（batch丸め、減衰も2B総予算内）。BF16/Flash＋compile reduce-overhead、batch32/context1024、途中保存1000更新ごと。実950更新/31,129,600tokens、finite loss3.5481・grad、約709k tokens/sを確認済み。まだ品質改善とはしない。

実行先`/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-2b-10bdata-20261004/`。Windows hidden launcher28168、pipeline shell472、stable supervisor482/start_ticks2372467、worker487/start_ticks2372547、boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`。正本は`supervisor.json`（operation移行後はPIDが変わる）。logはrun内`stable-2B-0.log`、全体は`reports/phase6/base_2b_10b_data_pipeline.log`。`scripts/run_base_2b_10b_data.sh`がstable→decay→既存protected dev/400生成評価を順に実行し、その後停止する。現在の実PIDを確認してから再開し、live時は重複起動しない。学習のみ約47〜48分＋既存評価約12分が目安、実測速度・保存で変動する。test/5B/10B/Chat/decoder比較は未起動。

以下はデータ整備・旧監査の経過記録。

2026-10-04 02:41 JST: [逐次near監査28/32band通過](../reports/phase6/corpus_10b_edges_audit_twenty_eight.json)。band0〜27の連続した完了logを確認。大group7,077件を含むband27は987.968秒（約16分28秒）で完了した。実PID1170053/boot/start_ticks1074573が記録と一致し、CPU時間が増加、完成export manifest SHAも不変。残り4band→全代表・全corpus/membership/split/token/index往復→terminal/PID終了→実train loaderを継続する。WSL空き619,283,476,480 bytes・RAM available約64GBを確認済みで拡張不要。全件合格・整備完了は未達、学習更新0。

2026-10-04 02:33 JST: [重複判定GPU化の実装・一次資料確認](../reports/phase6/corpus_10b_gpu_dedup_assessment.json)。現在は構築済みcorpusの独立監査で、27/32band完了、audit1170053のCPU時間が増加している。原処理はUTF-8文字5-gram集合の積/和をPythonで1組ずつ計算し、7,077件の大groupでは同一componentのskip前に最大25,038,426組。衝突のない整数IDへ変換し候補をGPUへまとめる方法は有力だが、変換・転送・精度境界・代表の一致・依存互換性を含むGPU実測は未実施。cuGraphの指定pair Jaccardは候補であり、このcorpusの速度保証とはしない。稼働中の凍結監査は継続し、GPU版への差し替え・再起動は行わない。将来比較は固定大group/実1M全32band、全候補・判定・代表一致、変換転送込み速度、限定pair probe180秒/採用目安2倍で閉じる。全件auditと実loaderは未完了、学習更新0。

2026-10-04 02:10 JST: [逐次near監査24/32band通過](../reports/phase6/corpus_10b_edges_audit_three_quarters.json)。band0〜23の連続した完了logを確認し、24段階はraw完了後7098.828秒（約118.3分、移行込み）。band23だけで967.156秒（約16.1分）かかり、band間の候補量・所要時間の差を実確認した。同じaudit1170053/boot/start_ticks1074573が実live、完成export manifest SHAは不変。24段階平均が残りも続く仮定のnear残は約39分だが、残り8bandも変動する。全代表・全corpus/membership/split/token/index往復・実loaderは別で未完了。全件合格とはしない。残り8bandを継続し、学習更新0。

2026-10-04 01:25 JST: [逐次near監査16/32band通過](../reports/phase6/corpus_10b_edges_audit_half.json)。band0〜15の連続した完了logを確認し、前半16段階はraw完了後4437.677秒（約74.0分、移行込み）。同じaudit1170053/boot/start_ticks1074573が実live、完成export manifest SHAは不変。前半平均が後半も続く仮定では残りnearは約1.23時間だが、後半の候補量は異なり、全代表・全corpus/membership/split/token/index照合と実loaderは別で未完了。途中結果を全件合格としない。後半16bandを継続し、学習更新0。

2026-10-04 00:50 JST: [逐次near監査8/32band通過](../reports/phase6/corpus_10b_edges_audit_quarter.json)。band0〜7の完了logが連続し、最初の8段階はraw完了後2344.360秒（約39.1分、移行込み）。同じaudit1170053/boot/start_ticks1074573が実live、完成export manifest SHAは不変。8段階平均が続く仮定で残りnear検証は約1.95時間だが、band候補量は変動し、後続の全代表・全membership/split/token/index往復と実loaderは別で未完了。全件合格とはしない。引き続き同じjobを監視し、学習更新0。

2026-10-04 00:30 JST: [序盤3bandの実測](../reports/phase6/corpus_10b_audit_early_timing.json)は374.910/208.675/515.511秒、平均366.366秒（約6.1分、最初はrawからの移行込み）。同じaudit1170053は実liveで、全32band中3個が完了。序盤平均が続くという仮定だけなら残りnear検証は約2.95時間だが、bandごとの候補量は異なり、後続の全token逐次再encode/byte/index/membership照合と実loaderの時間はまだ未測定。以前の全体残り3〜5時間という暫定値が上振れする可能性をユーザーへ説明した。24時間累積上限と全件受入条件を保持し、健康なjobを再起動しない。最終合格・整備完了は未達、学習更新0。

2026-10-04 00:18 JST: [逐次near重複監査の最初のband完了](../reports/phase6/corpus_10b_edges_audit_start.json)。全raw checkpoint後からband0完了まで374.910秒（約6分15秒、移行処理も含む）。全32band中1個の原逐次Jaccard検証を終え、同じaudit1170053/start_ticks1074573が実live。残り31band→全cluster/duplicate代表→全corpus/token/index往復→terminal/PID終了→実loaderは未完了。bandごとのgroup/candidate量が異なるため、この1個だけから全体速度や完了時刻を確定しない。原受入条件と完成exportを保持し、学習更新0。

2026-10-04 00:12 JST: [全128raw filesの独立再照合完了](../reports/phase6/corpus_10b_raw_audit_complete.json)。全29,208,256 records（raw29,009,357＋保護198,899）が取り込み完了件数と一致。原auditorのfull SQLite integrity_check、全raw hash/size、source payload/filter/protection、全signature、exact代表/eligibilityの比較を通過した。audit開始から3667.085秒には初期DB検査を含む。同じ1170053/boot/start_ticks1074573が実live、完成export manifest SHAは`856bf074...e0eb1`のまま。次は全32bandの逐次near検証・全代表→全membership/split/token往復→terminal/PID終了→実loader。これは途中の受入結果で、全件auditの合格・ローカル10B整備の完了とはしない。WSL空き619,283,693,568 bytes、RAM available約64GBで拡張不要。学習更新0。

2026-10-03 23:46 JST: [以前の大型成果物の保持確認](../reports/phase6/corpus_10b_prior_bulk_preserved.json)を実施。以前の固定reviewとconfigをWindows/WSL間で実hash照合してから、それらに記録された19 checkpoint（全stable/decay保存点とpilot）、旧pilot/expandedの両shard manifestと全train/dev/test stream/index/token byte table、保護用旧corpus、T4K Tokenizerの全37ファイル・9,058,888,985 bytesをWSLで再hashし完全一致。uint16 stream sizeも一致し、6.536秒で終了。[再現用checker](../reports/phase6/check_corpus_10b_prior_bulk.py)を保持。モデル読み込み・heldout採点・学習更新0。既存225小ファイルの保持確認を補う証拠で、新10Bの全件audit/実loaderの完了ではない。新audit1170053は引き続きliveで、全raw再構築を進める。

2026-10-03 23:37 JST: [初期DB検査通過・raw全件再構築へ移行](../reports/phase6/corpus_10b_raw_audit_progress.json)。同じaudit1170053/start_ticks1074573がlive。原auditorのfull SQLite integrity_checkがokを返し、保護198,899件と完了raw fileのsource/filter/payload/signature全比較を通過した位置で`audit_raw` checkpointが出た。観測は13/128files・3,136,181 records（保護を含む）、workers16。file00001→00006は約75.46秒/5files（約15.1秒/file）で、raw再構築の残りは同速度なら約30分。ただし後続32bands/全代表・全corpus/token列照合・実loaderは別で未完了、全件合格としない。次は全128files/29,208,256 recordsの再照合完了→全band検証→最終監査を継続する。

2026-10-03 23:21 JST: ユーザーの変換・保存高速化の質問に対し、[実train262,144文書/123,504,934 tokensの限定比較](../reports/phase6/corpus_10b_export_speed_probe.json)を実行。親で文書ごとにJSON生成する方式（16workers/batch128）と、worker側でJSON/tokenをまとめて返す方式（16workers/batch512）をABBA順で比較し、10.828/11.093秒→8.005/8.121秒、1.353/1.366倍。全本文/token/indexのSHA・文書/token/bytes件数が4回すべて一致、事前gate1.2倍を通過、180秒上限に対し42.136秒で終了。[再現用code](../reports/phase6/corpus_10b_export_speed_probe.py)を保持。基準は同じ出力を作るbuffered binary writerで、実export全体/全splitの速度や新pipelineの完成とは区別する。既定readonly SQLite接続はcache_size=-2000（約2MB）/mmap_size=0、page_size4096、page_count28,238,943。元auditの接続にもcache指定がなく、cache/mmap調整は別の実測候補（未採用・速度未測定）。live audit1170053は継続し、frozen code・完成export・全件監査基準を変更しない。完了見積りは現在暫定3〜5時間へ更新し、初期DB/後続全件照合速度が未確定で上振れし得ることをユーザーへ説明済み。

2026-10-03 23:10 JST: [全件監査v4の起動確認](../reports/phase6/corpus_10b_cached_audit_start.json)。元1106994は14:10:03 UTCにSIGINTによるterminal failedと累積9975.723秒を保存して実終了。watcherがjob-v3-retired.jsonを保持し、Linux1170053/同boot/start_ticks1074573の`bounded_feature_cache_audit_v4`を14:10:06 UTCに起動した。実/proc・旧PID消失・累積時間の完全引継ぎ・3 source snapshots全binding・完成export manifest SHA不変を確認。原逐次auditの全件checksを保持し、特徴量memoizationだけを検証済みcacheへ変更する。ログ`ten-billion/preparation-v4.log`、source`execution_v4_snapshot/`、出力`prepared-v2/`。WSL空き約581GiB。現在はauditの初期SQLite検査中、全件監査の合格と実loaderはまだ未完了。次はraw/signature→全32bands/代表→全membership/token列→terminal/PID終了→実loader→最終report/commit、学習前に停止する。以下の終了待機は解消済みの履歴。

2026-10-03 23:00 JST: [以前の225ファイル保持確認](../reports/phase6/corpus_10b_prior_files_preserved.json)。診断開始前の固定baseline SHA `241d5070...98ee`を確認し、Windowsの全225 source/config/evaluation/historical reportsの実hashが一致、missing/mismatch0。これは既存コード・小成果物の保持確認で、Linux bulk corpus/shards/checkpointや新10Bの全件auditの代用ではない。元1106994と終了待機watcher1169492は実/procでlive、cache auditへの移行はまだ終了待ち。

2026-10-03 22:54 JST: [終了の観測だけを再開](../reports/phase6/corpus_10b_handoff_resume.json)。元の5分timeout・送信済みSIGINT時刻・PID/boot/start ticks一致を必須に、シグナル再送0の常駐watcherを起動。Windows28320/Linux1169492の実identityを確認した。108GiB SQLiteの実読み取りが続くため、終了の観測は90分上限とし、元processの終了・terminal state・累積runtime保存を確認してからcache audit入口を起動する。元timeoutを別JSON、再開codeを別snapshotとして保持する。5 guard tests成功（実CLI branchでもSIGINT再送0/retired job保持を確認）。候補・全件audit・受入条件は変更しない。現在は元1106994の終了待ちで、監査完了/実loader確認は未達。

2026-10-03 22:52 JST: [監査引き継ぎ補助処理の待機上限](../reports/phase6/corpus_10b_handoff_timeout.json)。SIGINT後も元1106994が108GiB SQLiteの読み取り中で、5分の終了待機を超えたためwatcher1168675はterminal failedで終了し、replacementは起動していない。元PID/start ticks144729の実liveとCPU増加を確認、完成export/manifestは保持する。観測timeoutを元processの停止へ読み替えず、同じSIGINT/起動を反復しない。次は元processの実終了・terminal stateと累積runtimeを確認し、job-v3-retired.jsonを保存して`scripts/run_corpus_10b_cached_audit.sh`を直接起動する。全件audit・実loader・最終reportは未完了。外部操作を要するblockerではなく、既存processの終了待ち。

2026-10-03 22:46 JST: [export完成](../reports/phase6/corpus_10b_export_complete.json)。実train **12,225,819,077 stream tokens /25,879,667文書 /47,525,339,486 body bytes**。dev678,132,065 tokens/test679,399,996 tokensは別split。`prepared-v2/export-001/`とroot/shard manifestが完成し、target_met true、manifest件数・hash参照・全split uint16 byte sizes一致を確認。これはbuilder成果物で、独立全件auditと実loaderはまだ未完了。13:46:32 UTCにidentityを照合してv3へSIGINTを一度送信、元processはSQLite読み取り中のため終了待ち（実/procとCPU増加を確認）。終了と累積runtime保存後にwatcherがcache監査を起動する。5分以内に終了しない場合はwatcherが失敗記録を残すため、次は元processの実終了を待ち、完成exportを保持して監査入口へ移行する。元processがliveの間は再起動しない。完成後report/commitで学習前に停止する。

2026-10-03 22:35 JST: [監査引き継ぎwatcher](../reports/phase6/corpus_10b_handoff_watch.json)を常駐。Windows launcher28516、Linux1168675/同boot/start_ticks861194を実/procで確認、v3のexportは継続中。完成manifest・実train10B以上・shard件数一致・frozen source・元のPID/boot/start ticksとaudit stageを確認してから一度だけSIGINTを送り、終了と累積runtimeの保存を待つ。旧jobを別保存し、検証済みcache監査入口を起動する。90分の完成待機/5分の終了待機を超えたら失敗記録を残し、強制終了や自動再試行をしない。3 guard tests成功、liveで二重watcherのlock拒否も確認した。現在は完成export待ちで、引き継ぎ/全件auditの成功はまだ未確認。logは`ten-billion/audit-handoff.log`、statusは`prepared-v2/audit_handoff.json`。

最新観測（2026-10-03 22:31 JST）: 全32bandsのbuilder重複除去が完了し、同じv3 process1106994でexport中。[完了記録](../reports/phase6/corpus_10b_dedup_complete.json)で185,955,238候補組、707,772のband内検証済みspanning links、3808.713秒、groups/duplicates/result SHAを実成果物へ照合した（独立全件auditは未実施）。exportは約5.5分でtrain約3.37B tokens、約10.2M train tokens/s。変換残りは暫定15〜20分、独立全件監査・実loader・report/commitまで含む残りは暫定2〜4時間。後者は大規模audit速度が未実測のため確約しない。完成manifest/実train10B以上を確認後、検証済みcacheのaudit入口へ移行し、完成exportと累積実行予算を保持する。学習前に停止する。以下の途中観測は履歴として保持する。

最新の実行はexecution v3。元の取り込み・品質基準・独立逐次auditを保持し、後続LSHだけを8workersのband並列へ移行した。[実1M全32bands比較](../reports/phase6/corpus_10b_parallel_probe.json)で524,480候補coverage/全cluster/duplicate代表完全一致、30.004秒→9.135秒（3.285倍）。旧v2を実PID確認後にSIGINTで終了し、累積680.554秒・24files/5,630,035レコードのcheckpointを保持して再開した。元source snapshotとデータは保持し、追加実行codeを別snapshotへ保存する。

Windows launcher23824、Linux1106994/boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`/start_ticks144729は同じidentityでlive。全128raw filesのcommitと29,208,256 records（raw29,009,357＋保護198,899）を確認し、2026-10-03 12:20 UTC（21:20 JST）にstage parallel_external_lshへ移行した。[取り込み完了と実process確認](../reports/phase6/corpus_10b_ingestion.json)で全file receipt hash binding・file row合計/最終ID/ingest件数・signature size14,954,627,072bytesが一致。v3 ingestion2691.384秒、旧24filesは再処理しない。eligible28,998,779件を全32bands/8workersで検証中。workers1109198/1109201〜1109207の実PID/start ticks/CPUを確認。data rootは`ten-billion/prepared-v2/`、ログ`preparation-v3.log`、再開入口`scripts/run_corpus_10b_parallel.sh`。[移行と実装](32_local_10b_corpus.md#並列lshへの検証済み移行)。WSL空き約682GiBで拡張不要。token化・全件監査・実10Bの利用確認は未完了。次は全band完了/代表hash→export実token数→元の全件逐次audit→実ローダー→report/commit、学習前に停止する。

最終の[実学習用ローダー利用確認](32_local_10b_corpus.md#学習用ローダーでの最終利用確認)も実装した。未変更のShard/BlockSamplerでtrain batch2/context1024を作り、mask/bytes/再生一致を検証する（モデル作成・学習更新0）。小fixture3tests成功、未完了job/失敗auditでは拒否する。実10Bの確認はpipeline全件監査とprocess終了後に実行する。CPUの小fixtureを実10Bの完成へ読み替えない。

取り込み途中の残り時間見積り（履歴、取り込みは現在完了）の[読み取り専用実測](../reports/phase6/corpus_10b_eta_probe.json): committed prefix13,111,597件、eligible12,908,957件のband0に3,722,286候補組、最大group2,491件。180秒上限で実測39.530秒、sort10.056秒。先頭3,000組だけの検証0.698秒は無作為sampleでも全件検証でもなく、全体の速度へ断定的に外挿しない。現在のfile実測から取り込み残約30分。後続の重複除去・export・独立全件監査を含む完成は暫定6〜12時間だが、大規模の候補/check比とaudit速度が未確定で上振れし得る。全32bandsの実測へ進んだら更新する。24時間は累積実行上限で、完成予告ではない。token化と監査は未完了、学習未起動。

Jaccardのunion集合生成を同値の集合要素数式へ置き換える[限定比較](../reports/phase6/corpus_10b_jaccard_probe.json)も実施。実1M・全32bandsの全524,480組のfloat score列SHAと全代表が一致し、29.481秒→20.087秒（1.468倍）。事前の採用条件1.5倍未達のため不採用とし、live v3・元の独立逐次auditは変更していない。180秒上限の比較は終了、同じ比較の反復・閾値緩和はしない。[再現用code](../reports/phase6/corpus_10b_jaccard_probe.py)を保持する。

2026-10-03 13:03 UTC観測で本処理は30/32bands完了、残り23/27の実CPU時間は増加。[残り3bandsの全候補数](../reports/phase6/corpus_10b_pending_bands.json)は23,719,429 / 26,963,689 / 12,711,887組、最大group6,566 / 7,077 / 4,410件で、元builder2048・audit4096のcacheを超える。読み取り専用の[cache限定比較](../reports/phase6/corpus_10b_feature_cache_probe.json)では各groupの固定32,920組のfloat score列SHAが一致し、2.836 / 2.899 / 2.676倍。全group retentionのcharged bytesは約356 / 399 / 234MBで2GiB以下。新しい8192 entries/2GiB上限cacheは2tests成功だが本処理では未使用。採用前の実1M/全32bands/全代表の一致はまだpending。次にこの全件prefix照合と独立auditの統合検証を行い、既存の進行を失わない時点でauditの特徴量再計算だけを減らす判断をする。元の候補・Jaccard・独立逐次audit基準・frozen source・24時間累積予算は維持する。

監査cacheの[実1M・全32bands照合](../reports/phase6/corpus_10b_feature_cache_integration.json)も完了。全524,480組のfloat score列SHA `059a54...f7a9`・全1Mのcluster/duplicate代表が一致。original27.987秒/cache28.595秒で小groupは約2%遅いが、前記の大group限定2.676〜2.899倍という採用条件2倍を満たす。原auditの特徴量decoratorだけを8192 entries/2GiB上限へ替え、全raw再構築・全候補逐次Jaccard・全token/byte往復・old heldout保護・破損棄却を保持する[adapter](../src/jmicro/cached_corpus_audit.py)を追加。fixtureで同じchecks/split countsと失敗後のdecorator復元を確認し、全107tests成功/skip/failure/error0（fork warning8）。実live排他lockで新CLIの重複起動拒否も確認。 新入口は[scripts/run_corpus_10b_cached_audit.sh](../scripts/run_corpus_10b_cached_audit.sh)で、出力manifest/実train10B以上・old source snapshots・両実比較・process終了が必須。元のingest/dedup/exportを再実行せず、累積24時間予算と別execution_v4_snapshotを保持する。現在の本処理はまだv3で31/32bands完了、新入口は未起動。次は残りband→exportの実10B確認まで既存jobを継続し、完成exportを保持して監査入口へ移行する。

### 取得・初回構築の記録（履歴）

2026-10-03のユーザー依頼で、2B計画を約10Bのローカルデータ整備へ更新し、実行を再開した。[保存先・取得上限・実装・監査・停止条件](32_local_10b_corpus.md)。全bulk dataをWSLの`~/jmicro-data/phase6/ten-billion/`へ置き、Windowsとの境界越しデータ処理を避ける。WSL空き835GiB/Windows約2.5TBを確認し、現時点でdisk拡張は不要。原corpus/shards/heldoutを保持し、学習は開始しない。

取得Windows launcher24348、Linux933704/boot`0b330ec7-c11f-4bb3-be7c-cae9b868f4af`/start_ticks21313。構築v2 launcher7876、Linux1105089/同boot/start_ticks75979。取得は128files・約34.6GBを609.1秒で完了し、job terminal completeと実process終了を確認した。[取得記録](../reports/phase6/corpus_10b_acquisition.json)。構築v2は実/proc照合でlive、stageはingest。保護用198,899レコードの登録が完了し、実raw取り込みへ進んだ。最初の3raw filesのcommit/再開checkpointを確認し、100万超のレコードを処理した。[処理中の記録](../reports/phase6/corpus_10b_progress.json)。WSL空きは約800GiBで拡張不要。完了した初期8filesはhash確認してhardlink再利用。実tokensは構築後に確定するため、まだ10B用意済みではない。

旧待機job1104732は取り込み開始前に終了確認し、checkpointのatomic保存を加えたprepared-v2へ移行。旧job/snapshotを保持し、取得jobはそのまま継続。新規config/取得runner/SQLite file再開・external-sort LSH・streaming shard export・全件再構築auditを追加。元のtrainer/evaluator/shards/expanded_data/configと歴史的reportは変更しない。全105tests成功（skip/failure/error0、fork関連warning6件）。小fixtureでは旧dev/testのexact/near保護、再開末尾復旧、元LSH候補一致、全token往復と破損棄却を確認した。今後は取得完了→実file速度/容量の確認→全体構築/監査→report/status/commit。goalは10Bの整備全体で、raw取得やcode完了だけでは達成としない。

## 以前の次回計画: 学習用データを2Bへ拡張する（10B依頼で更新）

2026-10-03のユーザー訂正を反映。次に取り組むのは、整備済みtrain756,087,912 stream tokensを、同じT4Kで測った合計2B以上へ拡張すること。5Bは後続の段階目標。公開元の総量は十分に大きく、現在の準備量が少ないのは初回500M開始用の取得範囲へ限定したため。[取得・構築・監査・停止条件](27_phase6_remaining_plan.md#次回の一区切り-学習用データを2bへ拡張する)を更新した。既存dev/test・評価suite・過去データを保持し、別config/outputで追加取得と統合重複除去を行う計画。構築時間/容量は開始前の実測で予算を定める。次回実行の完了は2Bデータの監査・報告・commitまでで、学習は別計画とする。

今回は計画訂正のみで、取得・構築・GPU推論・学習を起動していない。モデルは10,001,152パラメータ、学習済み系列の消費量525,008,896 tokens、準備済みtrain756,087,912 tokensは変わらない。データ量不足は検証する仮説で、原因確定・品質改善の結果ではない。decoder/短文mixture比較は保留し、以下の旧計画と監査は当時の記録として保持する。

## 以前の次回案: 生成方法の比較（現在は保留）

計画作成依頼に従い、[次回の一区切り](27_phase6_remaining_plan.md#保留した案-学習済み10mモデルの生成方法を比較する)と[条件/予算/終了条件](../reports/phase6/repetition_decoder_plan.json)を記録した。[計画の16項目照合](../reports/phase6/repetition_decoder_plan_audit.json)でhash/実reference件数/7files同期/234既存files保持/未起動を確認する（比較codeや品質の合格ではない）。モデルは約10Mパラメータのまま、500Mは約5億input tokensの学習milestoneを指す。次回は同じdecay後checkpoint（合計525,008,896 input tokens学習）で反復抑制1.0/1.1、dev80×greedy＋sampling3seeds、計640outputsを比較する。reference320の全IDsを既存結果へ照合してから効果を判定する。GPU推論累積15分上限、実装・検証・報告込み30〜60分の目安。比較runnerは未実装で、先に別CLIと永続/再開・元decoder再現の検証を行う。

反復を8件以上減らすこと、sampling/EOSを悪化させないこと、candidateのUnicode/role/empty0件を自動改善候補の目安とし、元のBase品質基準は保持する。固定20組のblind人手評価packetを準備し、独立人手採点がない場合は未実施/文法・関連性未確定を残す。全文BPBの再採点は不要。同じ重みの生成方法の比較を、学習データの原因確定やモデルサイズ増加へ読み替えない。次回もreport/status/commitで停止し、短文mixture学習や1Bへ自動移行しない。今回の依頼では推論・学習・data変更を開始していない。

## 最新の調査: 反復退行・EOS・データ構成の調査完了、停止

ユーザー指定の反復悪化調査を[事前計画](../reports/phase6/repetition_diagnosis_plan.json)に沿って完了した。[判断と全比較](../reports/phase6/repetition_diagnosis_review.md)、[数値・binding・20項目監査](../reports/phase6/repetition_diagnosis_review.json)、[既存225 files保持](../reports/phase6/repetition_preservation.json)、[終了・同期・停止の監査](../reports/phase6/repetition_completion_audit.json)。学習更新0、GPU推論249.75秒/900秒上限、全102 tests成功/skip0。1B・新data・新trainerの学習・次回案を開始していない。

同じ80greedy反復は旧100M48→stable131M69→328M70→stable500M70→decay66。旧→最終は24件新規・6件解消、stable→decayは4件新規・8件解消。拡張モデルは131Mから反復が多く、decayが全体悪化の発生源という結果ではない。EOS教師はstable1,061,096回/0.2127%、旧0.2151%とほぼ同じで、BOSだけのmaskと実sampler/countersが完全一致する。全文同一devのEOS平均NLL3.00827→2.53698、同じ256文書末尾のEOS argmax30→35と改善する一方、80短prefix直後のEOS argmaxは0、最終の平均確率0.00247%。

全文trainの平均body464→469tokens、固定2,048文書/512文字sampleのregex反復は両方42（主に記号）。長さやsample反復の増加を主因にできない。拡張trainはWeb/commercial_web100%、128tokens以下は0.8505%。短い完結文の教師分布とgreedyの候補集中を有力な仮説として残すが、データ・露出・token予算・batch・schedule/backendが同時に変わる旧新比較で原因を確定しない。8case×旧/最終の生成IDsは完全再現、短FP32 full/cacheの全16probeは元許容内。BF16にはargmax差が各1位置あり、精度の影響と全context/backend同値は未解決として保持する。

Linux raw evidenceは`reports/phase6/repetition-diagnosis-20261003/`。CPU511/GPU570、Windows launcher23056/3468は完了し、jobのPID/boot/start_ticks・source/plan hash・log・sample/trace/testsを保持する。次の行動は停止。次回案は同じ重みのdecoder対照（最大640outputs/GPU15分）、必要なら短文mixtureの各25M-token対照（別loader/trainer実装と再開gate必須）で、元の品質基準・凍結codeを維持する。量不足が主因とは結論せず、1Bへ自動延長しない。

資源についてはWSL側で実測確認した。学習は速度優先のbatch32/Flash/compile/BF16/fused AdamW、約695k tokens/s、driver peak約7.5GiB。最大容量batch111はVRAM97.64%でも約650k tokens/sと遅く、32を採用する。data wait約0.5%でCPU入力供給が主要制約という証拠はない。使用容量を100%にする方針ではなく、検証した範囲で最速を採用している。調査推論は逐次greedy中心で学習と資源使用条件が異なる。

## 最新の結果: 500M学習・評価完了

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。

ユーザー指定の計画1〜5を実施した。[学習・評価監査と比較](../reports/phase6/base_500m_review.json)、[全80 greedy生成例](../reports/phase6/base_500m_review.md)、[preflight](../reports/phase6/base_500m_preflight.json)、[99 tests](../reports/phase6/base_500m_tests.json)。本文一度採点・同一89,416文書/164,344,743 bytes・FP32 CE・windowを検証した。document paired改善95% CIは[0.221163593157386, 0.22214939473619974]。これはdev文書のsampling不確実性で、学習seed変動やデータ量だけの因果効果ではない。

[指定範囲の完了監査](../reports/phase6/base_500m_completion_audit.json)で起動条件・実stable/decay・全文dev/400生成・過去証拠保持・job終了・停止境界を11項目照合した。学習/比較の独立監査25項目も通過した。生成退行は品質未達の結果として保持し、技術検証の成功へ混同しない。

stableは15,259更新/500,006,912 input tokens、decayは追加763更新/25,001,984 tokens。全state checkpointを保持し、parent SHA不変・全更新の有限値・保存間隔を監査した。stable SHA `775b14be60b755153fcfa03633e8a3a489fcddc6508db69f759b5547df57fbbf`、decay SHA `0a64cfc3ac18d411d0d2144d9d9c8185e7010872baf5247612dd365bd619514e`。Linux出力は`reports/phase6/base-20261003/`、stable/decay/evaluateのsupervisor・log・source snapshot・全checkpoint・raw評価を保持する。元のstableから同じglobal305,176更新のまま継続できる。

Windows launcher16200 / Linux pipeline465と各GPU stageは終了。`supervisor-{stable,decay,evaluate}-500M.json`・pipeline stateを保持し、完了した500Mを再起動しない。初回の非login shell uv PATH不足はGPU起動前の失敗で、専用入口へuser uv PATHを設定して修復した。失敗log/stateを`reports/local/`へ保持する。比較用の旧small reportはWindows正本からLinuxへ同期し、元のdeep evidenceは変更していない。

生成はgreedy反復48/80→66/80、sampling反復6/240→11/240、Unicode0/400→1/400で退行した。sampling EOSは0/240→1/240で、greedy EOSは0/80のまま。Unicode1件は64-token上限でmulti-byte列が途中終了したものだが、凍結metricの失敗として残す。[Codexによる20件の内容点検](../reports/phase6/base_500m_content_review.json)でも意味のある続きを展開せず反復する例を確認した。これはblind人手採点ではない。

次の行動は停止。1Bへの単純拡大は現時点で推奨せず、EOS教師量・文書長と短文promptの違い・反復傾向・greedy/sampling差を既存artifactで点検し、対照/予算/終了条件を定義してから次の実験を提案する。生成品質の未達・人手評価未実施を保持する。今回の結果をBase v1/Chat完成や新学習重みのexport/量子化合格にしない。以下の未起動/再開待ちは以前の準備・計画作成時点の履歴である。

## 以前の準備・計画作成記録（履歴）

文書・計画の更新依頼に基づき、README/実装checklist/技術状況/引継ぎと[残りの計画](27_phase6_remaining_plan.md)を93c7d1dの検証結果へ揃えた。次回は500M stable→独立decay→全文dev/400生成評価から開始し、1B/2B/5B/10Bを段階判断する。必要なpaired CI・人手採点の集約は未統合として明記した。今回の更新では学習・実験を開始せず、凍結code/config/protocol・過去report/snapshotを保持する。

[文書更新の監査](../reports/phase6/documentation_refresh_readiness_20261003.json)で25文書のWSL同期、実CLIと凍結値の一致、内部リンク、247の既存fileの保持と本学習未起動を確認する。

## 方針と停止境界

最新の依頼は次回計画の作成。[次回の500M計画](27_phase6_remaining_plan.md#次回の一区切り-拡張データで500mを学習評価する)に、約90倍へ拡張済みのtrain、新規500M stable・独立decay・同じdevでの比較、終了成果物を記載した。次回は500M評価/report/commitで停止する計画を提案し、1B以降は後続段階とする。データ不足は未確定の仮説で、学習量やscheduleも変わる比較をデータ量だけの因果効果にしない。今回は文書だけを更新し、学習は未起動。

Pythonは3.12.7/uv管理、全実行は`uv run --frozen`。依存変更は`uv add`、復元は`uv sync --frozen`。GPU学習はWSL 2 / Ubuntu / RTX 4090。Git local identityは`yousan <ka1357amnbpdr@gmail.com>`、検証済み変更をcommitし、push/公開しない。

**Phase 0〜5とPhase 6①〜⑤の準備は検証済み。ユーザー指定の「1.生成/変換確認、2.本学習設定確定」を実施し、最終監査37 checksを通過し、`93c7d1d`へcommitして停止済み。500M以上の本学習は未開始で、次の再開指定を待つ。** [今回の比較と完了条件](30_phase6_readiness_execution.md)、[③完了記録](29_phase6_performance_completion.md)。

## ③の実測と採用

採用はT4K NoNorm / 10,001,152 parameters、Flash＋torch.compile reduce-overhead / fullgraph・static / deterministic、context 1024、batch 32・accumulation 1、FP32 parameters＋BF16、fused AdamW、WSD。入力32,768 tokens/update。3×200完了更新の定常中央値は**694,521 tokens/s**、最速reference/math batch 16（127,772）比**5.436倍**。

最速設定のsave/小sample評価込みpeakはallocated 5.73 GiB、reserved 6.59 GiB、driver 7.53 GiB。data wait 0.55%。測定条件の最大安定batchは**111、112 OOM**。111は3×200・厳密再開・保存/評価を通過し、driver peak 23.42/23.99 GiB（97.64%）、速度649,563 tokens/s。VRAM容量上限と最高速度を分け、運用候補はより速い32を採用する。allocator cap 94%、固定shapeの有限探索であり、任意設定の理論最高性能を保証しない。

9設定のstable 200 vs 100+100・decay 100 vs 50+50はmodel/optimizer/scheduler/RNG/sampler、token/bytes/digest、loss/LR履歴、親の不変性・元継続が完全一致。6最速/容量設定の各3×200確認も完了。**独立監査1286 checks全成功、採用設定の空compiler cache再開26 checks完全一致、全79 tests / skip・failure・error 0**。小sample評価は4 dev文書＋1 prompt×2 greedy outputs/各最大8 tokensで、全文品質評価ではない。

v3のunique raw metricsは10,005 completed updates / 414,298,112 input tokens、cold再開は追加100 updates / 3,276,800 input tokens。別々の性能runで、一つの長期Baseではない。未完了OOM更新、診断v1/v2をこの台帳へ含めない。

- [全結果](../reports/phase6/batch_performance_report.json)、[採用理由](../reports/phase6/batch_choice.md)、[速度・資源・token要約](../reports/phase6/performance_summary.json)。
- [独立監査](../reports/phase6/performance_completion_audit.json)、[cold再開](../reports/phase6/performance_cold_resume_report.json)、[79 tests](../reports/phase6/performance_tests.xml)、[文書・旧成果保持監査](../reports/phase6/performance_documentation_audit.json)。
- [v1/v2失敗保持](../reports/phase6/performance_failures.json)、[監査初回の生成output数誤判定](../reports/phase6/performance_audit_initial_failure.json)。backend別cacheと実compiled code/呼び出し検証を修正した。監査は既存APIの2 greedy outputsを正しく確認し、GPU条件を変更していない。

## 保存先と終了したjob

Windowsコード/Git正本は`C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。Linuxの古いGit HEADだけで識別せず、snapshot/hashで照合する。

- v3: Linux `reports/phase6/performance-20261003-v3`、job terminal complete。Windows launcher 24452、Linux supervisor 426 / boot `37666cd9-cd78-41c1-a0cb-39c21d108047` / start ticks 78847は終了確認済み。
- cold再開: Linux `reports/phase6/performance-cold-resume-20261003`、terminal complete。Windows launcher 17308、Linux supervisor 620 / 同boot / start ticks 361156は終了確認済み。
- v1/v2はinvalidatedで診断snapshot/log/checkpointを保持し、launcher 18088/23060も終了。GPU compute processなし。完了したjobを再起動しない。
- raw metrics/requests/results/checkpoints/compiled code/snapshotは各runに保持。通常cacheはLinux `artifacts/compile-cache`、cold cacheはcold runの`empty-cache`。

## ①②と過去の成果を保持

①の固定FineWeb2 Edu Japaneseは8 files / 2,152,539,810 raw bytes。T4K train 1,604,292 docs / **756,087,912 unique stream tokens** / 2,946,200,160 body bytes、dev89,416/test89,485 docs。全raw/clusterとretained 1,783,193 docsのtoken/index/文字往復を独立監査済み。初期Web 100%、first500M約0.66回露出。巨大master全量の証拠ではない。rawは`~/jmicro-data/phase6/raw/`、corpus/shards/全監査は`~/jmicro-data/phase6/expanded-v2/`。

②のWSD stable/独立decay CLIとNoNorm/math batch 8の全state再開・分岐完全一致は73 GPU checks / 74 tests、独立55 checksで完了。12 checkpointsとsnapshotをLinux `reports/phase6/preparation-20261003/cuda/`へ保持。[①②完了記録](26_phase6_preparation_completion.md)。新sourceの通常resumeは旧checkpointを拒否する契約を維持し、旧sourceはsnapshotへ保持。旧73 reportsとuv.lockのbyte保持は総合監査で確認済み。

## 今回の④⑤: 検証済み・本学習前で停止

**固定の短/1024入力・元のcache分割・全12数値比較が成功し、本学習設定をversion2として再凍結した。** [変換結果](../reports/phase6/nonorm_export_parity_report.json)、[独立した実CLI/重み監査149 checks](../reports/phase6/readiness_export_audit.json)、[全90 tests / skip・failure・error 0](../reports/phase6/readiness_precision_tests.xml)。

採用したCPU推論profileは `cpu-f32-f64-accumulation-v1`。FP32の重み・activation・cache・logitsを維持し、Linear/attentionの積和、RMSNorm分散、softmaxの和をFP64で累積する。SiLU/default RoPEのtrigも精度を上げる。Torch/HFの通常実行とcacheは完全一致、native1024の最大差0.0000124574は固定atol1e-5＋rtol1e-4以内。成果物metadataから実推論CLIも同じprofileを適用し、対応しないstock runtimeを拒否する。runtimeはLinux `artifacts/runtime-stable-f32-v2`、archive/patch chain/binary/shared librariesをhashで照合する。CPU精度優先の経路で、stock FP32やCUDAの同精度を保証する結果ではない。

旧stock FP32の失敗、RoPE周波数だけを修復した失敗、CPU8設定とCUDA参照の失敗を保持する。第1層q_projからの誤差増幅を[159 stageで追跡](../reports/phase6/nonorm_cache_precision_trace.json)した。2つ目の修復案で累積精度を上げ、途中版の4要素の未達はtrig丸めの差を修復して解消した。[修復の採否と保持](../reports/phase6/nonorm_precision_repair_report.json)。許容値・入力・必要な比較・学習済み重みを変更して通過扱いにしていない。

GPU学習coreのmodel/shards/training/uv.lockとreadiness worker/evaluatorは変更していない。高速CUDA/BF16経路にはCPU profileを適用せず、LR比較・保存再開の実測を維持する。LR0.001/0.002/0.003は各2,000 stable＋独立100 decayで完了、固定dev256文書BPBは1.18776153/1.18404703/1.18739314。0.002を採用。新sourceのstable400/200+200・decay100/50+50は50 checks完全一致、cold200→400は25 checks完全一致、親全file不変・元継続も成功。[GPU独立106 checks](../reports/phase6/readiness_gpu_audit.json)。合計7,500 updates / 245,760,000 input tokensは複数の準備runの台帳で、本学習系列ではない。

400生成は360.684秒、Unicode0/400、greedy EOS0/80・反復48/80で品質未達。全文dev89,416文書 / 164,344,743 bytes / 42,003,934 body tokensを336.292秒で採点しBPB1.2441264716、scalar/batch差0.0000330177（事前許容0.001以内）。旧pilotの直接改善量や人手文法評価の合格にしない。新CPU profileのcontrollerは実argmaxからのEOS/EOT停止と3 backendのgreedy IDsを実CLIで検証し、合成停止fixtureをモデル品質へ数えない。

[本学習設定version2](../configs/phase6/base_frozen.json)はbatch32・accum1・context1024、32,768 input tokens/update、LR0.002、warmup200、seed42、Flash/compile reduce-overhead/fullgraph/static/deterministic、WSD global305,176更新（10B丸め）、各観測点5%独立decay・floor0.1。save1,000更新ごと・全checkpoint保持、推定347件/41,702,694,225 bytes、run上限100 GiB・最低空き200 GiB。[起動/復旧計画](../reports/phase6/base_launch_plan.json)。`launch_enabled=true`は技術gateの成立を示すが、今回は起動しない。先の起動不可設定は[version1](../configs/phase6/base_frozen_blocked_v1.json)と[実起動拒否証拠](../reports/phase6/base_launch_guard_report.json)へbyte保持した。

Linux deep evidenceは `reports/phase6/readiness-20261003/`、最終exportは同runの `export-stable-f32/`、source snapshot/logs/raw logits/weightsを保持する。GPU準備とCPU8設定のsupervisorはterminal complete、精度build/probe/正式検証/CLI/テストも終了。`93c7d1d`のcommit後にGPU compute processなし・Git cleanを確認した。完了したjobを再起動しない。

**次の行動は停止。ユーザーが再開した後に、凍結source/data/runtimeを照合し、既存process/checkpointを確認して500Mの新規Base学習から始める。** prepareが既定で、復旧は同じglobal予算のまま行う。500M/1B/2B/5B/10Bの段階評価、Chat trainer、mixture、Muon、学習後量子化品質は今回の範囲外・未実施として維持する。外部権限やdriver更新のblockerはない。

現在速度から500M約12分・10B約4時間は純学習の算術値。compile/startup/全文dev評価/400生成/保存/decay枝を含め、完成時刻の保証にしない。[予算](24_phase6_plan.md)。以前の状態は[Phase 5当時status](autonomous_status_phase5_20261003.md)と[復旧履歴](autonomous_history_20261003.md)に保持。
`````

## docs/windows_handoff.md

UTF8 LF SHA256: a9061ce70be5ecadb4cdebb3dfa0251b558d213c8baec99388b840481de09dcd

`````markdown
# 別PCで続きを進める: Windows / WSL / RTX 4090

2026-10-04最新: [10B設定準備step1完了](40_base_10b_preparation.md)。configs/phase6/base_10b.json/schema凍結、14tests/実CUDA全state再開一致（16updates/524288検証tokens）、GPU19.217秒。Linux459/Windows29620実終了、GPU computeなし、science outputsなし。run reports/phase6/base-10b-20261004/のprep/gate/checkpoints/source/logを保持。今後の本学習起動はbash scripts/run_base_10b.sh --train、引数なし/--verify-onlyは検証専用で完了済み結果を返す。今回の科学学習は未開始、準備report/local commitで停止。旧runnerを再利用起動しない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: step1の10B設定準備をユーザーが指定。新config configs/phase6/base_10b.json とbash scripts/run_base_10b.sh --verify-onlyを準備。引数なしもverify-only。run reports/phase6/base-10b-20261004/で検証16updates/524288tokensだけを実行し保存再開を確認する。科学学習は明示--trainの別範囲。job identity/lock/logを確認して重複起動しない。準備review/report/local commit後停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新（計画訂正のみ）: ユーザー指定で[直接総10Bの案](39_learning_scale_and_generation_plan.md)に変更、7.5B専用decay/全文評価を省く。親は旧5B stable/checkpoint-00144959.pt（4.75B）、既存12.23B内で9.5B stable＋独立decayを新しい明示forkとして実装・凍結する必要がある。追加科学5,249,990,656tokens、最後に同じ全文/400で比較。新run/config/schema/起動command未作成、新GPU jobは未起動。旧完成runnerを再実行しない。計画/local commitで停止。[実状態](autonomous_status.md)。以下の段階7.5B案は訂正前の履歴。

2026-10-04最新（計画のみ）: [総7.5Bと条件付き10Bの次回案](39_learning_scale_and_generation_plan.md)を保存。長期親は旧5B stable/checkpoint-00144959.pt、最終低LR枝の通常resumeではなく明示forkを新規実装・凍結する。既存12.23Bと旧全文/400を再利用し、raw安全gateと改善を確認して段階を進める。最後の新親短文対照とUTF8制約policy比較は別条件。新run/config/schema/起動commandは未作成、今回新GPU jobを起動していない。旧完成runnerを新予算用に再実行しない。計画/local commitで停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: EOS/UTF8改善1〜3は[完了・停止](38_eos_5b_finish_results.md)。Linux `reports/phase6/eos-5b-finish-100m-20261004/` job complete、actual Linux464/Windows21524終了、GPU computeなし。GPU2253.853/3000秒、同じ5Bから各100M/別262144検証、最終 `{web,short20}/checkpoint-00155640.pt` を保持。共通表示末尾helper/33tests/44項目保存確認成功。短文固定EOS13/80・反復51/80だが全400 rawUnicode2で原最終採用gate不合格、意味品質未達。途中invalidとcap未完成尾をCPU分類しraw失敗保持。完成runner `bash scripts/run_eos_5b_finish.sh` を再実行しない。全旧成果物/新診断checkpointを保持してreport/local commitで停止、10B/Chat/UL/sweep未開始。[実状態とSHA](autonomous_status.md)。以下は履歴。

2026-10-04最新: 改善計画1〜3をユーザーが再開。新実行config `configs/phase6/eos_5b_finish_100m.json`、run `reports/phase6/eos-5b-finish-100m-20261004/`、restart `bash scripts/run_eos_5b_finish.sh`。jobのactual PID/boot/start ticksを照合しliveなら重複起動しない。final5Bから同じ低LRの各100M、旧accepted short/auxと元raw評価を維持。表示helperは実装/CPU確認済み、GPU学習/評価はまだ起動前。全指定比較・内容確認・report/commit後10B/Chat/UL/sweep前で停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新（調査/計画のみ）: [EOS・反復・UTF8の次回案](37_eos_repetition_utf8_improvement_plan.md)を作成。保存済み評価のCPU再集計とUTF8 buffering probesのみ実施、GPU推論/学習0、production codec/weightsは不変、実行jobなし。次回はCPU表示helperとfinal5Bの低LRWeb/short20各100Mを実装・凍結する必要があり、旧2B runnerをそのまま起動しない。既存短文pool/auxと元rawgateを保持、GPU上限3000秒、完了後10B/Chat/UL/sweep前で停止。この提案の起動commandは未実装。今回は計画/report/commitで停止。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: [5B比較完了](36_base_5b_comparison.md)。Linux `reports/phase6/base-5b-comparison-20261004/` job complete、actual Linux477/Windows26484終了、GPU computeなし。GPU788.433秒/上限1800秒、追加学習0。全文BPB0.964484へ改善、固定EOS0/80/反復59/80/Unicode1/80、全400 Unicode2は同じbase-070末尾UTF8切断。元増量gate不合格、Base/Chat品質未達。保存済み結果のCPU reviewer18項目成功、全80内容確認と13例を保存。final5B/全対照weights/全文と生成を保持。完了launcherのrestartは再実行しない。比較/report/commitで停止、10B/Chat/新規学習/sweepなし。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: ユーザーが5B比較を再開。[config](../configs/phase6/base_5b_comparison.json)、run `reports/phase6/base-5b-comparison-20261004/`、restart `bash scripts/compare_base_5b.sh`。job.jsonのactual PID/boot/start ticksと/procを照合しliveなら重複起動しない。final5Bのみ同じdev89416/生成400を評価、元2B/低LRWeb/short20-reference結果は再実行しない。全文devと生成を別保存、source/weights/heldout保持、GPU累積1800秒。内容確認/report/commit後停止し新規学習/10B/Chat/sweepなし。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: 次計画1・2（継続処理と総5B学習）を[完了](../reports/phase6/base_5b_review.json)。Linux run `reports/phase6/base-5b-20261004/` job complete、actual Linux450/Windows28760終了、GPU computeなし。final decay/checkpoint-00152588.pt、SHA1d8e5274e1662063dedec355def1da3c9bcc972499a12b608c25c71b6758273a、総5,000,003,584tokens。継続用stable/checkpoint-00144959.ptも保持。追加科学3,099,983,872＋検証524,288、CPU6testsと実CUDA全state再開一致、GPU75分43秒で120分上限内。全旧成果物/97科学checkpointを保持。ユーザー指定のコードpushはc68ff34までorigin/mainへ完了。記録・local commit後停止し、完成job再実行/全文評価/10B/Chat/sweepは開始しない。5B品質は未評価。次は別範囲のstep3比較。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: 次計画1・2をユーザーが再開。[5B固定config](../configs/phase6/base_5b.json)、[実行計画](35_base_5b_execution.md)、run `reports/phase6/base-5b-20261004/`、restart `bash scripts/run_base_5b.sh`。actual job.json PID/boot/start ticksとlatest checkpointを照合しliveなら重複起動しない。stable1.9Bを別fork、LR0.002維持して総5B、最後約5%decay to0.0002。CPU6tests成功、実CUDA524,288検証後に追加3,099,983,872科学tokens。全旧成果物保持、uv/WSL4090/Linux data。学習/report/commitで停止し全文評価/10B/Chatへ進めない。5B品質は未判定。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: [低LRの1〜3を完了](../reports/phase6/eos_low_lr_100m_review.json)。Linux `reports/phase6/eos-low-lr-100m-20261004/`のjobはcomplete、actual Linux498/Windows27984終了・GPU compute processなし。各100M/元2Bからのfork、Web/short全文BPB0.972969/0.974799、EOS0/27、反復55/41、各400 empty/role/Unicode0。12 testsと実CUDA全state再開一致、GPU2141.290秒で2700秒内。全checkpoint/旧成果物を保持、完成重みは同run/{web,short20}/checkpoint-00064088.pt、SHA等は[実状態](autonomous_status.md)。意味誤り/反復が残るため原Base/Chat品質未達。元増量条件は通るが、この依頼は1〜3で停止する。完了jobのrestart commandは復旧履歴であり再実行指示ではない。report/commit後停止し5B/Chat/sweepを開始しない。以下は履歴。

2026-10-04最新: ユーザー指定の低LR計画1〜3を実行する。[config](../configs/phase6/eos_low_lr_100m.json)、run `reports/phase6/eos-low-lr-100m-20261004/`、restart `bash scripts/run_eos_low_lr.sh`。actual job PID/boot/start ticksとlauncherを照合し、liveなら重複起動しない。旧100Mと元2Bは保持し、学習率0.0002以外は同条件/各100M、既存pool/aux80を再利用。必要評価・report/commit後に停止して5B/Chatへ進めない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: [完結単位100M対照と必要な全文評価は完了](../reports/phase6/eos_complete_100m_review.json)。固定EOS0/80→24/80、補助EOS0→42/80。全文BPB Web1.016473/short1.017580、短文full400のempty/role/Unicode全0、24関連tests成功。意味誤り/反復と元2Bより悪いBPBが残るため元2B基準を保持、短文重みは診断候補。各累積2,100,035,584 tokens、Linux r2/{web,short20}/checkpoint-00064088.ptと全旧job/log/準備poolを保持。main job.jsonは中断履歴のまま、evaluation-recovery-job.jsonがcomplete。Linux439/Windows25296実終了・GPU compute processなしを確認済み。GPU合計3305.199秒、原2700秒超過を明記。再起動・再学習・再評価・5B/Chat/sweepはせず、report/commit後停止する。詳細/checkpoint SHA/次回論点は[実状態](autonomous_status.md)。以下のlive PIDとrestart commandsは履歴であり現在の起動指示ではない。

最終比較runは`reports/phase6/eos-complete-100m-20261004-r2/`、bulkも同名r2。Windows launcher16164/Linux453/boot44655da4-5b8c-4da8-a7a5-47ae16b364c1/start_ticks39818でGPU jobを起動済み。r1は学習前の内容修正で保持したCPU-only履歴。r2のjob.json・actual process identity・latest checkpointを正本とし、旧準備を再起動しない。学習前pool445,501単位/21,000,010 tokens、22 tests成功。[準備証拠](../reports/phase6/eos_complete_100m_preparation.json)。

2026-10-04実行再開: [完結単位100M対照config](../configs/phase6/eos_complete_100m.json)と`bash scripts/run_eos_complete_100m.sh`を使用。新run `reports/phase6/eos-complete-100m-20261004-r1/`のjob.json/boot/PID/start ticksとWindows launcher記録を照合し、liveなら重複起動しない。CPU事前確認で旧poolの名詞断片/見出しを除外してr1へ変更。旧CPU準備/guarded worker cleanupは保持、GPU学習開始前の変更であり結果を見て条件変更したものではない。20関連tests成功。比較・必要な全文評価・report/commit後に停止し、5B/Chatへ自動移行しない。[実状態](autonomous_status.md)。

2026-10-04最新の依頼は次の計画作成。[100M対照/5B以降の提案](27_phase6_remaining_plan.md)と[JSON予算](../reports/phase6/eos_next_plan.json)を保存し、実行は未開始。次の実行前に32〜64-token完結単位builder/補助dev80/100M runner/reviewerを実装し、actual pool/配置/phase budgetを凍結する。旧25M runnerは完成runを返す入口であり100Mを実行するcommandではない。5B stable予算延長forkも未実装。既存2B/25M成果物とcore sourceを保持し、完了job/全件監査を再起動しない。[実状態](autonomous_status.md)。以下は履歴。

2026-10-04短文混合の[対照実験も完了](../reports/phase6/eos_short_pilot_review.json)。Linux `reports/phase6/eos-short-pilot-20261004-r1/`はjob complete、実process/GPU jobなし。各25MでEOS0/80対0/80、反復62対54/80、dev256 BPB1.068518対1.069161。短文条件はEOS gate未達で未採用。Web controlは旧`eos-short-pilot-20261004/web/checkpoint-00061799.pt`を再学習せず厳密再利用、short重みはr1/short20同名checkpoint。旧jobのinterruptedはshort開始前の省略文filter修正のためで、初回pool/runner/plan/log/gateも保持。bulk short poolは`~/jmicro-data/phase6/eos-short-pilot-20261004-r1/`。元2B基準を保持し、完了pilot/診断/全文dev評価を再実行しない。次の32〜64-token比較/5B/Chatは未開始。[最新状態](autonomous_status.md)。以下は履歴。

2026-10-04 EOS調査も完了：[結果と次の比較案](../reports/phase6/eos_2b_review.json)。Linux `reports/phase6/eos-diagnosis-2b-20261004-r1/`のjob.jsonはcomplete、run.log/result/末尾probe/40 continuations/testsを保存。298.556秒、追加学習0、GPU計算job終了。EOS教師・停止controllerの不具合は見つからず、生成中にEOSより続きを優先する。原greedyは512でも0/20停止/20/20反復、penalty1.1も5/20の遅い停止で反復が残る。完了run/全文dev再評価を再起動しない。次の短い完結文を混ぜた対照学習案は未実装/未起動で、元2B checkpointを普通にresumeして実行する指示ではない。[最新状態](autonomous_status.md)。以下は履歴。

2026-10-04最新: [ローカル12.23Bデータと新データ2B学習・評価を完了して停止](../reports/phase6/base_2b_10b_data_review.json)。現在は再開・再評価しない。最終重みはLinux runのreports/phase6/base-2b-10bdata-20261004/decay-2B/checkpoint-00061036.pt、SHA165f9c177961a82b3da1c5ab1d21a32078b35b02e594fb2eb09edd7dbd4ea183。supervisor.jsonはevaluate/completeで、実project process/GPU計算jobは終了している。総学習2,000,027,648 tokens、同じdev BPB0.982882、greedy反復60/80/EOS0/80。旧データ・旧重み・全checkpoint・新shardsは保持する。以下の実行中の説明と再開commandは中断時の履歴で、完了runを繰り返す指示ではない。

現在は[整備済みの実train12.23Bデータ](32_local_10b_corpus.md)で、ユーザー指定の2B学習を実行中。構築・全export往復確認済みで、ユーザーが過剰な独立再照合の省略を指定したため、独立監査は29/32near bandで停止（全raw再構築済み）。実train loaderは49.147秒で合格。[整備完了記録](../reports/phase6/corpus_10b_ready_review.json)は全件audit未完了を明記する。

新shardsは`~/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards/`、新学習configは`configs/phase6/base_2b_10b_data.json`、runは`reports/phase6/base-2b-10bdata-20261004/`。`supervisor.json`と[実状態](autonomous_status.md)を/procのboot/PID/start_ticksへ照合し、liveなら重複起動しない。停止後の再開は`bash scripts/run_base_2b_10b_data.sh`で有効なcheckpointを再利用する。stable→decay→既存protected dev/400生成比較を順に進め、総2Bで停止する。旧corpus/shards/heldout/重みは保持し、新shardsを旧checkpointの通常resumeへ差し替えない。WSL約1TB/空き619GBで拡張不要。decoder/5B/10B/Chatは未起動。以下の停止境界は以前の履歴。

500M後の[反復/EOS/data調査](../reports/phase6/repetition_diagnosis_review.md)も完了し停止。追加学習/1Bは未開始。Linux `reports/phase6/repetition-diagnosis-20261003/`のsample・trace・log・job identity・testsを既存runとともに引き継ぐ。次回案のdecoder/mixture比較は未起動で、完了した500Mや診断jobを再実行しない。[最新状態](autonomous_status.md)。

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。 [最新状態](autonomous_status.md)。以下の初回復元・準備完了記録は履歴として保持する。

Phase 6①②③完了（2026-10-03）。④生成/変換と⑤本学習設定の確定もユーザー指定の範囲で検証済み。[今回の固定計画](30_phase6_readiness_execution.md)と[実状態](autonomous_status.md)を参照する。④⑤は`93c7d1d`へcommitして停止済みで、500M以上の本学習は開始しない。

最終更新: 2026-10-03。[Phase 4](21_phase4_completion.md)、[Phase 5](23_phase5_completion.md)、Phase 6①〜⑤の準備は完了。復元済みPCでは環境整備・Tokenizer学習・完了済み測定を繰り返さず、[現在の状態](autonomous_status.md)と既存job/checkpointを確認する。④⑤の限定比較と起動設定凍結も93c7d1dへcommitして終了した。Base/Chat本学習は未開始で、文書更新を学習再開の指定として扱わない。

## 引継ぎ先と現在地

| 項目 | 内容 |
|---|---|
| コード・docs・lockの正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m` |
| Linux実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| GitHub | [private repository](https://github.com/ayutaz/japanese-tiny-llm-10m)。Phase 5・Phase 6①〜⑤と文書更新のコミットは未push |
| 公開pilot / Tokenizer | [固定Hub repository](https://huggingface.co/datasets/japanese-data-analyze/japanese-tiny-llm-10m-artifacts)、約107MB |
| Hub commit | `0b1042979bf32899e24da30790e3ae6b239013c3` |
| manifest SHA-256 | `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09` |
| 実機環境 | WSL package 3.0.1.0 / Ubuntu WSL 2、RTX 4090、Windows driver 616.92 |
| Python / PyTorch | uv管理の3.12.7 / 2.14.1、CUDA 13.0 |
| 完了済み | Phase 0〜5とPhase 6①〜⑤の準備。pilot/Tokenizer、モデル/export、GPU学習器、100M候補選定、756M拡張corpus、WSD全state再開/分岐完全一致 |
| 現在の境界 | ③の証拠はa7d26e1へcommit済み。④⑤も93c7d1dで完了し、400生成/dev全文・NoNorm CPU変換精度、LR3候補・新source再開を検証済み。長期LR0.002と予算はversion2へ凍結済み、全12変換比較・実CLI149 checks・90 tests成功。本学習は開始しない。 |
| 未実施 | 長期Base本学習、Chat trainer、学習後の量子化品質 |

HubにはpilotとTokenizerがあり、モデル重み・shard・checkpointは含まない。Phase 4の検証checkpointはLinuxの`reports/phase4/gates-20261003/`、Phase 5は`reports/phase5/run-20261003-docoverfit/`、Phase 6準備の12 checkpointsは`reports/phase6/preparation-20261003/cuda/`へ保存してある。拡張raw/corpus/shardsは`~/jmicro-data/phase6/{raw,expanded-v2}/`で、Hub bundleには含まれない。新規PCへは必要なcheckpoint/logも別途引き継ぐ。旧driver/アクセス拒否の履歴は[復旧履歴](autonomous_history_20261003.md)へ分離した。

## 1. Windows側でWSLとGPUを確認

PowerShellの読み取り確認:

```powershell
wsl --version
wsl -l -v
nvidia-smi
```

WSL packageの3.xとdistributionの実行方式WSL 2は別に記録する。[MicrosoftのWSL手順](https://learn.microsoft.com/en-us/windows/wsl/install)。NVIDIA driverはWindows側へ導入し、WSLへLinux display driverを追加しない。[NVIDIAのWSL手順](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)

現在の616.92で固定CUDA 13の動作を実測済み。以前の552.12は解消したblockerで、現PCに更新操作は不要。新規PCでdriver条件を満たさない場合は[公式配布先](https://www.nvidia.com/Download/index.aspx)から更新し、driver表示だけでなくCUDA/BF16も確認する。[CUDAの互換条件](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html)

新規PCの環境準備が必要な場合のみ、Windows project rootから実行:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_windows_wsl.ps1
```

既存distributionを使い、ゼロの場合は導入・初回Linuxユーザー作成が必要。OS昇格/再起動を要求されたらその外部操作で停止する。既存のLinuxコピーはsetupで上書きしない。復元済みの現在のPCではsetupを再実行する必要はない。Linux内からのsetup再実行は以下（WSL Linux shell）:

```sh
cd ~/src/japanese-tiny-llm-10m
JMICRO_PROJECT_ROOT="$PWD" bash scripts/setup_wsl_environment.sh
```

Linuxのsetup.log/environment、Windowsのwsl_setup reportに結果を保存する。既存環境は構築済みで、CUDA/BF16、入力付きprepare/verify、Phase 4の全64 tests / skip 0を確認した。Phase 6①②は74 tests・73 GPU checks、最新③は79 tests・独立1286 checks・cold再開26 checks成功（全skip 0）。

## 2. Linux側でコードとuvを準備

新規PCでコードがない場合のみprivate repositoryを取得する。GitHub認証はLinux側でも確認する。clone先へWindowsの最新コミットを引き継ぐまで、GitHub mainだけを最新と仮定しない。既存treeの変更は保存し、resetや強制上書きをしない。

```sh
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
mkdir -p ~/src
git clone https://github.com/ayutaz/japanese-tiny-llm-10m.git ~/src/japanese-tiny-llm-10m
cd ~/src/japanese-tiny-llm-10m
git status -sb
git rev-parse HEAD
```

uv未導入なら[公式導入手順](https://docs.astral.sh/uv/getting-started/installation/)を使い、案内されたPATHを有効にする。project rootで:

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

Macのvenv/native binaryは移さない。すべてのPython実行は必要なextra付き`uv run --frozen`、依存変更は`uv add`。system Pythonやpipへ切り替えない。固定Python/依存が取得できなければ正確なblockerを記録する。

## 3. Hugging FaceからTokenizerとデータを復元

新規PCで不足する場合のみ、project rootで:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

匿名で全25 payloadとmanifestを検証してから16 filesを配置する。配置済みならrestored_filesは0。内容が違う既存fileは上書きせず停止する。取得cacheは`artifacts/hub-downloads/<commit>/`。

| 復元先 | 内容 |
|---|---|
| `artifacts/phase2/4096/`、`8192/` | model/vocab、special IDs、wrapper、metadata、各5 files |
| `data/phase1/processed/` | corpus、Parquet manifest、split、sample、二つのreport、計6 files |

採用corpusは22,998件、全source合計splitはtrain 20,710 / dev 1,074 / test 1,214。Phase 4 BaseではWebのみを選び、train 18,022 / dev 924 / test 1,052に分離。会話/sharealikeと固定evalはBaseへ混ぜない。SFTはAssistant本文＋EOTを教師対象にするが、Chat trainerは未実装。

公開Tokenizerは旧Mac版の保存先metadataだけを除去したためbyte hashが異なる。公開manifestのhashを使い、checkpoint/shardへbindする。旧ランダム重みexportを公開版と再比較する場合のみexportを作り直す。初回CUDA確認のためにTokenizer再学習・原データ再取得・Phase 3全作業を繰り返さない。[hashと取得の詳細](huggingface_handoff.md)

## 4. 契約とCUDA環境を確認

新規環境での検証は既存reportを上書きせず別directoryへ保存する:

```sh
mkdir -p reports/local/handoff
uv run --frozen --extra hub --extra data --extra ml --extra export pytest -q -ra
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/local/handoff/environment.json
```

Phase 4のsuiteは64 tests / skip 0、Phase 5は68、Phase 6①②完了時は74 tests / skip 0。[保存した結果](../reports/phase6/tests.xml)。artifact欠落によるskipを完了証拠にしない。CPU成功はCUDA学習・再開一致の代わりにならない。Linux/WSL、GPU/driver、cuda_available、BF16、Python/uv/lock/sourceをreportから確認する。`nvidia-smi`がPATHにない場合は`/usr/lib/wsl/lib/nvidia-smi`を確認する。

環境captureの`training_target.verified=false`は準備用ラベル。最終判定は[handoff report](../reports/phase4/handoff_report.json)と実GPU結果を使う。wheel変更が必要な新規環境ではuvでlockを更新し、新しい条件で検証する。現在の固定構成は動作済み。

## 5. 入力・run・checkpointを引き継ぐ

準備snapshotは`experiment.py prepare-run` / `verify-run`で記録できる。これはphase 0/kind preparationの記録で学習開始を意味しない。実学習は別の[training run schema](../schemas/training_run.schema.json)を使い、CLI引数・環境・PID・Git dirty・source snapshot・入力hash・statusをrun.jsonへ保存する。

checkpoint version 2は完了updateでmodel/optimizer/scheduler/Python・NumPy・torch・CUDA RNG/sampler positionとRNG/consumed tokens・教師tokens・body bytes/digest/config/data/source hashをatomic保存する。latest.jsonのSHAを確認し、partial metricsはcheckpoint境界へ戻して再開する。resumeはschedule/config/source/shardの変更を拒否する。LinuxコピーのGit HEADだけで実行コードを判断せず、snapshotとimplementation hashを照合する。

長時間GPU jobはhidden Windows wsl.exe supervisor、Linux job.jsonのPID/boot ID/start ticks/stage/logで保持した。GPUは`~/jmicro-data/gpu.lock`で排他。再開前にWindows/Linuxプロセス、GPU compute一覧、既存runを確認し、二重jobを起動しない。スリープ/再起動後は有効なcheckpointから再開し、会話終了だけで保存先を失わない。

## 6. 実装済みCLIと次回の再開

今回の①②は[準備完了記録](26_phase6_preparation_completion.md)と[独立監査](../reports/phase6/completion_audit.json)を正とする。WSL data rootの拡張corpusは756M unique train stream tokens、WSD stable/decayの実CUDA再開一致は成功済み。準備の中断復旧/読み取り再監査の実commandは完了記録に保存した。①②のjobは終了済み。③の別studyとcold再開も終了済み。[完了記録](29_phase6_performance_completion.md)に採用設定・監査・job identityを保存した。

開始条件は[Phase 6 gate](24_phase6_plan.md)と[今回の固定比較](30_phase6_readiness_execution.md)を参照する。④⑤の400生成/全文dev・3 LR比較・厳密/cold再開は終了し、[本設定](../configs/phase6/base_frozen.json)と[起動/復旧CLI](../reports/phase6/base_launch_plan.json)を保存した。長系列の固定数値gateはCPU精度profileで元の全12比較が成功し、実CLI監査149 checks・全90 testsが成功。version2は`launch_enabled=true`だが今回は本学習前で停止する。旧false設定と実起動拒否証拠は保持。完了した準備jobを再起動しない。Phase 4のNorm/pilot/cosine benchmarkをNoNorm/拡張shard/WSDの証拠へ流用しない。

`scripts/train.py`にbuild-shards/train/evaluateを実装済み。trainはCLI引数を使用し、baseline JSONを自動読込しない。AdamW＋warmup/cosine・WSD stable/decayは実装済み、Muon・Chat trainer・複数source mixtureは未実装。

以下のhelpは学習を起動せず確認できる:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --help
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py evaluate --help
```

下記200更新はCLI利用例で、overfit合格の証拠や本学習設定ではない。Phase 5の正式な予算・合格条件は[詳細計画](22_phase5_plan.md)へ固定済み。Phase 5 supervisorは終了済み。完了したPhase 5比較と③のstudyを重複起動しない。本学習は再開指定を待つ。文書単独の暗記検証には`--sampler document`を使用し、通常のsmoke/100Mはdefaultのblock samplerを使う。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py build-shards --tokenizer artifacts/phase2/8192/tokenizer.model --limit 100 --output "$HOME/jmicro-data/shards/t8k-overfit100"
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py train --model configs/models/t8k.json --shards "$HOME/jmicro-data/shards/t8k-overfit100" --output reports/phase5/overfit-example --phase 5 --device cuda --dtype bf16 --context 1024 --batch 2 --schedule-updates 200 --stop-after 100 --save-every 100
```

`--limit 100`は各splitの上限。dev/testをoverfit学習へ使わない。保存済みrunを再開する際は元の全引数・出力先を維持し、同じcommandへ`--resume /absolute/path/to/checkpoint.pt`と必要な`--stop-after`を追加する。`--schedule-updates`を途中で変えて予算を延長しない。

評価の形式（同じ入力にbindされた実在checkpointを指定）:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/train.py evaluate --checkpoint /absolute/path/to/checkpoint.pt --shards "$HOME/jmicro-data/shards/t8k-overfit100" --tokenizer artifacts/phase2/8192/tokenizer.model --split dev --output reports/local/overfit-evaluation.json
```

Phase 4 Norm/defaultのeager最大安定batchはT8K 57 / T4K 64、測定点の最高速度はcompile/default batch 8。Phase 5でdefault/compile-defaultは厳密resumeに失敗し、現候補はeager/math batch 8を採用した。③では学習専用causal経路・cache分離を修正し、NoNorm/math最大45、compiled/math最大53、compiled Flash最大111を実測・厳密再開検証した。最速はFlash/compile reduce-overhead batch 32=694,521 tokens/s。最大容量と最高速度を区別する。[③の完了](29_phase6_performance_completion.md)。Phase 4測定をそのまま有用なモデル品質として扱わない。[予算と制約](../reports/phase4/resource_budget.md)

## 次の担当へ渡す文面

```text
AGENTS.md、docs/autonomous_status.md、docs/15_project_roadmap.md、docs/windows_handoff.md、docs/24_phase6_plan.mdを読んでください。
Phase 0〜5とPhase 6①〜⑤の準備は完了しています。③の証拠はa7d26e1へcommit済みです。④⑤のCPU精度profile・実CLI・長期設定も93c7d1dでcommit済みです。本学習の再開指定まで停止し、完了したGPU studyを再実行しないでください。残る作業はdocs/27_phase6_remaining_plan.mdを参照してください。ユーザーの再開指定があるまで本学習を起動しないでください。
最新コードの正本はWindows workspaceで、最近のコミットは未pushです。Linux実行sourceはsnapshot/hashで確認してください。
固定公開Tokenizer/pilotは復元済み。Pythonは必ずuv run --frozen、依存変更はuv addを使ってください。
既存process/checkpointを確認し、docs/24_phase6_plan.mdとdocs/26_phase6_preparation_completion.mdに従って進め、同じjobを二重起動しないでください。
未達の品質目標を維持し、原データ再取得・Tokenizer再学習・Phase 3全作業・完了済みPhase 4測定を繰り返さないでください。
実測結果、失敗、次の作業をreport/statusへ保存し、指定Git名義で適度にコミットしてください。
```

## この手順の検証範囲

固定公開25 payload、Python/uv/WSL/GPU、CUDA/BF16、Phase 4の全64 testsと両モデルの再開/容量/速度、Phase 5の100M候補選定、Phase 6①②の全74 tests・73 GPU checksと拡張corpus全監査を現在のPCで確認済み。③の採用NoNormの容量・compiled/math/Flash速度・厳密/cold再開は検証済み（独立1286 checks、cold26 checks、79 tests）。長期予算はversion2へ凍結済み、CPU精度profileの全12比較・実CLI149 checks・全90 tests成功。新規PCや変更したruntimeでは必要な環境gateを改めて確認する。学習後のBase/Chat品質・quantizationは未検証。
`````

## docs/codex_automation.md

UTF8 LF SHA256: 58acd764d95b980beeced07ed3cac04d69852a5607d38f83bec0bc504bf5f983

`````markdown
# Codexによる環境整備・学習・改善の自動化

現在地（2026-10-03）: Phase 0〜5とPhase 6①〜⑤の準備は完了。③高速化・④生成/CPU変換精度・⑤設定凍結の検証を終え、93c7d1dへcommitして本学習前で停止中。[最新状態](autonomous_status.md)、[①②完了証拠](26_phase6_preparation_completion.md)、[再開後の計画](27_phase6_remaining_plan.md)を参照する。

確認日: 2026-10-03。Full accessが実効policyへ反映済みで、ユーザー側のrunner起動は不要。停止境界はAGENTS.mdと最新statusに従う。文書更新は本学習の再開指定ではなく、runnerの起動を次の学習開始条件にしない。以下のCLI 0.159.3の実helpとOpenAI公式資料の説明は当時の確認記録で、この文書更新では製品設定を再調査・変更していない。

ユーザー指定（2026-10-02）: 本プロジェクトの環境整備・実装・学習・評価・改善をCodexに継続して任せる。作業内容と実測結果は`autonomous_status.md`、方針はrootの`AGENTS.md`へ残す。Phase 4とPhase 5の指定範囲を完了した後、ユーザーがPhase 6①②を再開し、2026-10-03にその範囲も完了した。その後③〜⑤も完了し、現在は500M以上の本学習の再開指定を待つ。`complete`はその時の指定範囲を証拠で完了したことを示し、Base/Chat全体の完成とは区別する。

## このアプリで続ける

初回にモードが表示されない場合はSettings → General → Permissionsで有効化し、その後に入力欄下の権限メニューで選択する。[公式のモード選択](https://learn.chatgpt.com/docs/permission-modes)。入力欄下に選択肢がある場合は**Full access**へ変更する。公式の対応設定は`approval_policy = "never"`と`sandbox_mode = "danger-full-access"`。[OpenAI公式の権限説明](https://learn.chatgpt.com/docs/sandboxing)

Workのnetwork設定が提供されている場合は、Settings → Data controls → Work network accessでAllow public internet accessを有効にする。管理対象の環境で選択肢が無効な場合は管理者側のpolicy変更が必要。ユーザー設定は管理policyを上書きできない。変更が反映された実行環境で続きを進める。

当初の制限された会話ではグローバル設定を変更できなかった。2026-10-03にユーザーのFull access選択が実効policyへ反映され、会話内からWSL・network・CUDAにアクセスできた。グローバルconfigは変更していない。project内の設定fileは実行中セッションの権限を変更しない。

## CLIのプロジェクト用profile

通常のPowerShellでproject rootから実行:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install_codex_autonomous_profile.ps1
codex --profile jmicro_autonomous --cd . "AGENTS.mdとdocs/autonomous_status.mdに従い、環境整備から学習・評価・改善まで継続してください"
```

installerは既存グローバルconfigを変更せず、`$CODEX_HOME/jmicro_autonomous.config.toml`（未指定時は`%USERPROFILE%\.codex\`）へproject専用profileを作成する。同名profileが異なる場合はbackupを残す。今回確認したCLI 0.159.3の`--profile`は`<name>.config.toml`を重ねる仕様。既存のmodel選択・ログインを引き継ぐ。実際のCLI helpと[公式設定説明](https://learn.chatgpt.com/docs/config-file/config-reference)を再開時にも確認する。

CLIの設定はアプリの既存会話を変更しない。管理policyやWindowsの管理者権限を回避するものでもない。WSL導入/driver更新のOS側昇格、再起動、Linux初回ユーザー作成、初回ログインは外部操作として残る場合がある。

## 無人の継続runner

Codex CLIと保存済みログインを利用する。通常端末で:

```powershell
uv run --frozen scripts/run_codex_autonomous.py --max-turns 20
```

WSL内でCLIを利用できる場合はLinuxコピーで:

```sh
uv run --frozen scripts/run_codex_autonomous.py --max-turns 20
```

runnerはprofileのinstallなしでも、起動するCodexに`approval_policy=never`と`danger-full-access`を指定する。制限された会話から権限拡張用に起動する手段には使わない。Full accessが反映された環境または通常端末から実行する。表示だけの確認は`--dry-run`。

各回のCodexが実装・学習・検証を行い、`continue`なら次の回を開始する。`complete`、外部操作が必要な`needs_user`、CLIエラー、20回の起動上限で終了する。上限終了はproject完了を意味しない。無制限retryや無制限の改善探索は行わず、同じcommandで状態fileから続けられる。1回の作業時間やCodex accountの利用上限はrunnerが解除できない。[公式non-interactive実行](https://learn.chatgpt.com/docs/non-interactive-mode)

`reports/automation/<UTC-id>/`に各回のprompt、JSONL events、stderr、最終JSON、最新resultを保存する。exit codeは0=要求達成、2=runner/CLIエラー、3=外部操作待ち、4=起動回数上限。`runner.lock`で二重runnerを防ぐ。強制終了後にlockが残った場合は記録されたPIDの終了を確認してから除去する。学習jobの二重起動はagentがcheckpoint/run記録とPIDを確認して避ける。

コードの継続runnerと、長時間GPU学習のcheckpoint/監視/再開は別の機能。GPU側はPhase 4で排他lock、PID/boot ID/start ticks、stage/run記録、atomic checkpointとhashを実装し、hiddenのWindows `wsl.exe` supervisorで検証jobを保持した。スリープ・再起動・ログイン切れで永続実行は保証せず、中断時はcompleted-update checkpointから再開する。

Pythonの実行はrunner・テスト・一時スクリプトを含め`uv run --frozen`経由に統一する。Python 3.12.7が未導入なら`uv python install 3.12.7`で導入し、依存は`uv sync --frozen`で復元する。固定環境を取得できない場合はblockerを記録し、system Pythonへ切り替えない。

## 実施した検証

`uv run --frozen python -m unittest discover -s tests -p test_codex_automation.py -v`で再実行できる5件のstubテストが成功。実Codexを呼ばないローカルstub subprocessで、継続結果の引継ぎ、終了条件、CLI失敗時の診断、二重起動防止を確認した。dry-run/profile previewと各fileの構文も確認。このstub結果だけでは実Codex/GPU成功を証明しない。後続のPhase 4では全64 tests / skip 0と実GPU学習・保存再開・評価・容量測定を完了した。[実機証拠](21_phase4_completion.md)。

初回stub検証はuv統一前の履歴。現在の再実行は`uv run --frozen python -m unittest discover -s tests -p test_codex_automation.py -v`を使う。
`````

## reports/README.md

UTF8 LF SHA256: f20649d7572b7cfe565f59abb3304873350cdde601dee0ac8873bdca0597ff19

`````markdown
# 実験台帳と検証結果

`phase0/`にiMacの環境・準備検証・完了監査を記録する。`p0-<name>-<UTC>-<random>/`は学習を実行しない準備runのsnapshotで、`experiments.jsonl`に追記する。大型/機械依存のrun snapshotはGit管理外。

準備runは`kind=preparation,status=prepared,tokens_seen=0`。モデルconfigと学習済みTokenizer artifactを区別し、Phase 2前のTokenizer/data入力hashは`null`で未作成を示す。学習を実施した結果として扱わない。

snapshotにはcode/docs/config/eval/lockfile、各hash、環境、Git commitとdirty状態を含める。未コミット変更もsource snapshotから復元できる。既存runの変更はchecksum検証で検出する。Phase 4の学習runは別の`schemas/training_run.schema.json`を使用する。準備schemaや過去snapshotは書き換えない。

`phase1/`には実データpilotの統計、20件の内容レビュー、全件復元・split検証、再生成比較と完了監査を保存する。本文・原file・Parquet・大きなsplit membershipは`data/phase1/`のGit管理外領域に置き、reportのchecksumと[再生成手順](../data/README.md)から照合する。Phase 0の過去環境・監査を上書きせず、現在の開発検証には`reports/local/`等を使用する。

`phase2/`にはTokenizer契約・全coverage候補・全corpus計数、`phase3/`には両実モデルの契約、native export parity、量子化実型・容量、完了監査とテスト結果を保存する。これらPhase 2〜3のモデル重みはランダム初期化。Phase 4では別途GPU検証学習を実施したが、Base/Chat本学習は未実施。大型Tokenizer/weights/native runtimeは`artifacts/`のGit管理外で、reportのhashを照合する。詳細は[Phase 2](../docs/18_phase2_completion.md)、[Phase 3](../docs/19_phase3_completion.md)。

## Phase 4の実機証拠

`phase4/environment.json`、`handoff_report.json`、`resume_report.json`、`throughput_report.json`、`base_evaluation_contract_report.json`、`resource_budget.md`をGit保存した。handoffは全7 gate成功、全64 tests / skip 0、両モデルの全state resume一致。eager最大batchはT8K 57 / T4K 64、compiled容量は未探索、Flash-onlyの失敗は残す。

rawログ・source snapshot・checkpoint・生成出力はLinux実行コピーの`reports/phase4/gates-20261003/`に保持する。集約reportのraw path/SHAを照合し、Git cloneだけでraw checkpointまで復元できるとは扱わない。Phase 4終了時にはPhase 5は未開始だった。[完了記録](../docs/21_phase4_completion.md)

## Phase 5の実学習・比較証拠

`phase5/`にはoverfit/smoke、4本の100Mのtraining/evaluation audit、凍結plan、共通bytesと固定生成の集約、候補config、採用・棄却理由、独立監査、実測予算と停止確認を保存した。全68 tests / skip 0、4構成のCUDA厳密resume、overfit全5 gate、全比較と補助評価が成功。候補はT4K / NoQK-Norm / LR 0.002。停止・反復・sampling Unicodeの品質目標は未達で、Phase 5当時はNoNormのHF/GGUF adapterが未実装だった。現在は④でCPU精度profileによる学習済み変換を検証済み（下記④⑤）。[完了記録](../docs/23_phase5_completion.md)

raw evidenceはLinux checkoutの`reports/phase5/run-20261003-docoverfit/`へ保持する。GPU job/launcherは終了済み。自動生成の`candidate_selection.md`と`completion_audit.json`をそのまま保存し、詳細な採否レビューを`candidate_selection_review.md`へ分けた。Phase 6本学習は未開始。

将来のrunを再実行する場合は別directoryへ出力する。既存run/reportやPhase 0〜3のhashを更新で上書きしない。現在の文書検証等は`reports/local/`へ保存する。

## Phase 6①②の完了証拠と文書更新

以下の①②reportは[事前の目的・条件](../docs/25_phase6_preparation.md)に対応する。train 756,087,912 unique stream tokensの拡張corpusとWSD stable/独立decayを準備した。[完了記録](../docs/26_phase6_preparation_completion.md)。③の容量/速度・長期Base/Chat・品質達成の証拠ではない。

| report | 確認したこと |
|---|---|
| [sources.json](phase6/sources.json)、[acquisition.json](phase6/acquisition.json) | 固定revisionの条件資料・取得上限、8 filesの上流SHAとraw 2,152,539,810 bytes |
| [corpus_manifest.json](phase6/corpus_manifest.json)、[corpus_audit.json](phase6/corpus_audit.json) | 全1,803,712 raw、signature/cluster・split、全retained 1,783,193文書の本文/token/index/文字往復。manifestは作成時ラベルを保持し、監査結果はauditを正とする |
| [quality_review.json](phase6/quality_review.json) | 24 train文書の先頭最大420文字を確認。品質リスク・確認範囲を記録 |
| [wsd_resume_report.json](phase6/wsd_resume_report.json)、[evaluation_isolation.json](phase6/evaluation_isolation.json) | CUDA/BF16/math/batch 8、stable 200 vs 100+100・decay 100 vs 50+50の全state完全一致、元枝不変性とdev評価状態保全。73 GPU checks |
| [tests.xml](phase6/tests.xml)、[completion_audit.json](phase6/completion_audit.json) | 全74 tests / skip・failure・error 0、独立監査55 checks、12 checkpoints・336 snapshot files、過去report 57 filesとlock不変 |
| [preparation_failures.json](phase6/preparation_failures.json) | 初回scheme失敗・schema不足と修復。条件を緩めず失敗履歴を保持 |
| [hub_artifacts_verification.json](phase6/hub_artifacts_verification.json)、[process_completion.json](phase6/process_completion.json) | 公開25 payload照合/restored 0、launcher終了と停止確認 |
| [documentation_audit.json](phase6/documentation_audit.json)、[final_package_audit.json](phase6/final_package_audit.json) | ①②完了時点の43 Markdown / 393内部リンク、Windows/WSL 91 source filesの同期、包装監査13 checks |
| [documentation_update_20261003.json](phase6/documentation_update_20261003.json) | ①②後の文書・残りの計画更新を別監査した当時の記録。旧report/実装/config/lock/eval不変、文書リンク・CLI・WSL同期・停止境界を確認 |

大型dataは`~/jmicro-data/phase6/{raw,expanded-v2}/`、CUDA checkpoints/log/source snapshotsはLinux checkoutの`reports/phase6/preparation-20261003/cuda/`。①〜⑤のjobは終了済みで、本学習前で停止中。Git clone/Hub bundleだけで拡張data/checkpointsが揃うとは扱わない。既存snapshotと完了reportは当時の証拠として保持し、現在の文書を過去snapshotへ書き戻さない。今後の実行順は[本学習以降の計画](../docs/27_phase6_remaining_plan.md)。

## Phase 6③の高速化・容量・再開証拠

③は`a7d26e1`でcommit済み。[完了記録](../docs/29_phase6_performance_completion.md)。Flash＋compile reduce-overhead / batch 32=694,521 tokens/s、最大安定111/112 OOM。以下は①②のreportとは別の実測で、品質達成・長期Baseの証拠ではない。

| report | 確認したこと |
|---|---|
| [batch_performance_report.json](phase6/batch_performance_report.json)、[batch_choice.md](phase6/batch_choice.md)、[performance_summary.json](phase6/performance_summary.json) | 最速・容量・保存/評価込みVRAM・速度比・unique metricsのtoken台帳 |
| [performance_completion_audit.json](phase6/performance_completion_audit.json)、[performance_cold_resume_report.json](phase6/performance_cold_resume_report.json)、[performance_tests.xml](phase6/performance_tests.xml) | 独立1286 checks、空cache再開26 checks、79 tests / skip・failure・error 0 |
| [performance_failures.json](phase6/performance_failures.json)、[performance_audit_initial_failure.json](phase6/performance_audit_initial_failure.json) | 初回cache/backend・観測不足・監査のoutput数誤判定を保持 |
| [performance_documentation_audit.json](phase6/performance_documentation_audit.json) | ③完了時の文書/CLI/WSL同期・旧73 reports/lock保持と実装/report binding |
| [plan_update_20261003.json](phase6/plan_update_20261003.json) | 今回の最新計画・完了チェック・算術予算・文書同期と旧成果/コード保持の監査 |

raw logs/requests/compiled code/source snapshots/checkpointsはLinux `reports/phase6/performance-20261003-v3/`と`performance-cold-resume-20261003/`に保持する。④生成/変換と⑤長期設定凍結は完了した。今後は再開指定後に500M段階評価へ進む。

## Phase 6④⑤の検証・設定凍結と停止

④⑤は`93c7d1d`へcommit済み。[実施記録](../docs/30_phase6_readiness_execution.md)。

| report / config | 確認したこと |
|---|---|
| [generation_diagnostics.json](phase6/generation_diagnostics.json)、[expanded_dev_baseline.json](phase6/expanded_dev_baseline.json) | 固定dev400生成と拡張dev89,416文書の全文採点、BPB/時間/未達品質、本文一度採点・EOS分離 |
| [nonorm_export_parity_report.json](phase6/nonorm_export_parity_report.json)、[readiness_export_audit.json](phase6/readiness_export_audit.json) | CPU精度profileで学習済み短/1024・full/cacheの全12比較、13契約、実CLI/全119 GGUF重みの独立149 checks |
| [nonorm_precision_repair_report.json](phase6/nonorm_precision_repair_report.json)、[stock失敗](phase6/nonorm_export_stock_fp32_failure.json) | 精度修復の採否、途中/stock/CPU8設定/CUDA参照の失敗保持。GPU学習coreと重みは不変 |
| [readiness_stability_report.json](phase6/readiness_stability_report.json)、[readiness_gpu_audit.json](phase6/readiness_gpu_audit.json) | LR3候補×2,000 stable＋100独立decay、LR0.002採用、厳密50/cold25完全一致、独立106 checks |
| [readiness_precision_tests.xml](phase6/readiness_precision_tests.xml)、[readiness_gate_audit.json](phase6/readiness_gate_audit.json) | 全90 tests / skip・failure・error 0、指定範囲の6要求と停止境界の37 checks。Base品質合格ではない |
| [base_frozen.json](../configs/phase6/base_frozen.json)、[base_launch_plan.json](phase6/base_launch_plan.json) | version2のmodel/data/source/runtime、batch32/LR0.002/WSD global305,176更新、独立decay5%、保存/容量/実起動・再開CLI |
| [旧version1](../configs/phase6/base_frozen_blocked_v1.json)、[base_launch_guard_report.json](phase6/base_launch_guard_report.json) | 修復前の起動不可設定と実起動拒否をbyte保持 |
| [documentation_refresh_readiness_20261003.json](phase6/documentation_refresh_readiness_20261003.json) | ④⑤完了後の25文書・残りの計画更新。凍結条件/CLI/算術予算、内部リンク、WSL同期、旧実装/設定/証拠の保持と停止を検証 |

raw logs/checkpoints/weights/logits/snapshotsはLinux `reports/phase6/readiness-20261003/`、正式exportは同runの`export-stable-f32/`。専用CPU runtimeは`artifacts/runtime-stable-f32-v2`。Git/Hubだけでは復元できず、Windowsコードとともに引き継ぐ。現行の`launch_enabled=true`は技術gate成立で、ユーザーの再開指定まで500M以上の本学習を開始しない。


## 拡張trainの500M学習・評価

2026-10-03: 拡張trainの500M stable＋独立763更新decayと全文dev/400生成評価を完了。同一dev BPB 1.244126→1.022491、抑制greedy EOS 0/80→0/80、反復48/80→66/80。全99 tests成功。人手blind採点・test・Chat・新重みの量子化は未実施。1B前で停止。

- [学習/評価/paired CI/全checkpoint監査](phase6/base_500m_review.json)、[全80 greedy生成例](phase6/base_500m_review.md)。
- [起動前照合](phase6/base_500m_preflight.json)、[全99 tests](phase6/base_500m_tests.json)。
- [固定20件の内容点検](phase6/base_500m_content_review.json)はCodexによる定性的な確認で、blind人手採点ではない。予測BPB改善と生成退行を分け、1B前で停止する。

raw evidenceと18 checkpointsはLinux `reports/phase6/base-20261003/`へ保持する。今回の新しい重みのexport/量子化は未実施。

## 500M後の反復・EOS・データ構成の調査

- [実行中: ローカル10Bデータ整備](../docs/32_local_10b_corpus.md)。WSL保存、全件重複/heldout保護/token監査を行い学習前で停止する。全105tests成功。実10B構築・監査は未完了。
- [LSH性能のprefix probe](phase6/corpus_10b_cost_probe.json)、[実1M・全32bandsでの並列比較](phase6/corpus_10b_parallel_probe.json)。候補coverageと全代表が一致、30.004→9.135秒（3.285倍）。取り込みcheckpointを保持したexecution v3へ移行した。全10Bの監査完了ではない。
- [実ローダー利用確認の手順](../docs/32_local_10b_corpus.md#学習用ローダーでの最終利用確認)。Shard/BlockSamplerでtrain batch/mask/bytes/replayを検証する。小fixtureは成功、実10Bは全件audit・process終了待ち。
- [以前の2B/5B計画](../docs/27_phase6_remaining_plan.md#次回の一区切り-学習用データを2bへ拡張する)は10Bの実行依頼へ更新した。
- [保留したdecoder比較の計画](phase6/repetition_decoder_plan.json)、[以前の作業順序](../docs/27_phase6_remaining_plan.md#保留した案-学習済み10mモデルの生成方法を比較する)、[当時の計画の16項目照合](phase6/repetition_decoder_plan_audit.json)。同じ10Mパラメータの重みで640outputs/GPU15分上限を比較する案。監査は当時の計画を確認した記録で、現在の優先作業や実行結果ではない。
- [事前計画](phase6/repetition_diagnosis_plan.json)、[判断と比較](phase6/repetition_diagnosis_review.md)、[数値/binding/20項目監査](phase6/repetition_diagnosis_review.json)、[225既存files保持](phase6/repetition_preservation.json)、[終了・同期監査](phase6/repetition_completion_audit.json)。
- EOS教師欠落は確認されず、文書末尾予測は改善。反復は拡張131Mから多く、decayで70/80→66/80。全文の文書長と固定sample反復に大幅増加はない。短prefix/greedyと学習分布の違いを次の比較候補とし、因果未分離・精度差を残す。
- 全102 tests成功。GPU推論249.75秒、学習更新0、1B未開始。Linux raw evidenceは`reports/phase6/repetition-diagnosis-20261003/`。次回案を開始せずcommit後停止する。
`````
