# Phase 0 完了記録

履歴の位置付け（2026-10-03）: 本文の件数・hash・未実施・次の作業は実施当時の記録。現在は[Phase 0〜4が完了](21_phase4_completion.md)し、ユーザー指定により停止中。[最新状態](autonomous_status.md)を優先する。過去のreport・snapshotは上書きしない。

この文書とreportはPhase 0実施時点の履歴。後続のPhase 4でWindows/WSLへ移行済み。[最新計画](15_project_roadmap.md)を参照する。後続の変更で過去のsnapshot・hashを上書きしない。

実施日: 2026-10-02。対象は[フェーズ別計画のPhase 0](15_project_roadmap.md#phase-0-成功条件環境実験管理)。iMac上で開発・実験管理と評価の準備を完了した。モデル学習・4090検証の完了ではない。

## 要求と成果物

| Phase 0の要求 | 実際の成果物・証拠 |
|---|---|
| リポジトリ骨格 | `src/jmicro/`、`configs/`、`schemas/`、`scripts/`、`tests/`、`data/`、`eval/`、`reports/`、[使い方](../README.md) |
| Python/依存の固定 | [.python-version](../.python-version)、[pyproject.toml](../pyproject.toml)、[uv.lock](../uv.lock)。`uv init`、`uv add`、`uv python pin`で作成。`uv lock --check --offline`が成功 |
| run/config/artifact記録 | [experiment_schema.json](../schemas/experiment_schema.json)、[準備runツール](../src/jmicro/experiment.py)。ID・source snapshot・環境・lock/config/input hashを保存し、ledgerで改変を検出 |
| seed・モデル/学習候補 | [T8K](../configs/models/t8k.json)、[T4K](../configs/models/t4k.json)、[baseline](../configs/training/baseline.json)。seed 42とparameter予算を明示 |
| iMac環境の実記録 | [environment.json](../reports/phase0/environment.json)。macOS、arm64、Python 3.12.7、uv、インストール済み依存とlock hash。Windows対象は未検証として分離 |
| Linuxへの引継ぎ | [移行手順](windows_handoff.md)、[iMac設定](../configs/runtime/imac.json)、[Windows/WSL設定](../configs/runtime/windows_wsl.json) |
| Base/Chat評価仕様 | [evaluation_protocol.md](evaluation_protocol.md)、[protocol.json](../configs/evaluation/protocol.json)。BPB、生成条件、rubric、数値許容値、停止ID、bucketを明記 |
| 独自promptとsplit | [Base 100件](../eval/base.jsonl)、[Chat 100件](../eval/chat.jsonl)、[split manifest](../eval/split_manifest.json)。各dev 80/test 20、10 category |
| 採点ルールの確認 | [手動採点例11件](../eval/rubric_examples.json)。文法・関連性・訂正保持の0/1/2と独立した反復flagを区別 |
| 自動検証 | [validation.json](../reports/phase0/validation.json)、[完了監査](../reports/phase0/completion_audit.json)、22件のpytestが成功 |

## 実験記録の契約

準備run IDは`p0-<name>-<UTC日時>-<8桁random>`、台帳は`reports/experiments.jsonl`、snapshotは`reports/<run_id>/`。実際のcode/config/lock/eval/docsを保存するため、Git commitだけでは表せない未コミット変更も復元できる。

recordは`phase=0, kind=preparation, status=prepared`、tokens/stepsは0。構造化schemaでは準備runを学習済みと記載できない。Tokenizerの設定hashと学習済みTokenizer artifactのhashを区別し、後者とdataset入力は未作成のため`null`。Phase 2以降は実fileを入力として渡し、実hashを記録する。

検証はschemaに加え、snapshot/参照fileのchecksumと台帳のexperiment checksumを確認する。input本文の変更、sourceの変更、schemaを満たすrecordの改変、欠けた入力、run名のpath traversalをテストした。学習run/checkpoint/metricsのschemaと状態遷移はPhase 4で追加する。

## 評価基盤の確認範囲

Base/Chatの計200件は独自作成で、同一入力のexact重複、ID、category別8/2分割、familyのsplit越境、manifest hash、Chatの役割順序を検査した。Tokenizer前処理30例、BPBの算術、モデルconfigからのparameter予算も検証済み。

手動採点例はCodexが設計時に読んで採点した架空応答。第三者の人手評価・評価者一致率は未実施で、Phase 7のモデル評価で確認する。固定履歴の文脈suiteはfree-running会話の証明ではなく、後続フェーズでrolloutを追加する。

品質目標と数値許容値は未実測の初期提案。品質閾値はPhase 5までにdev/pilotで固定、量子化退行幅はfloat dev評価後に固定する。Phase 0で実装したのは評価の入力・契約・検証で、LMのloss/生成を測るrunnerは後続フェーズ。

## Windows側へ残すこと

- WSL 3.1の実導入version、distribution実行方式、driver/CUDA、RTX 4090とストレージの確認。
- `ml` extraのインストールとCUDA/BF16検証。Phase 0では依存解決/lockのみで、ML package本体は導入していない。
- モデルのCUDA forward/backward、保存再開、最大安定micro batchと実shard速度。

これらは計画どおりPhase 4のgate。iMac側のPhase 0完了には含めず、Windows環境を確認済みとは記載しない。

## 次の着手

Phase 1ではsource/subset/revisionと実際の利用条件を確認し、小corpusと会話pilotのmanifest、重複cluster、train/dev/testを作る。Phase 0の固定評価例を学習sampleへ混ぜない。データを用意した後にPhase 2の独自Tokenizerへ進む。
