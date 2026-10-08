# Windows / WSL 引継ぎ

最終更新: 2026-10-09 JST。**学習・研究実行は一時停止。今回のモデル保存・公開は学習の再開指示ではない。** [状態](autonomous_status.md)、[結果123](123_base_teacher_decay_2b_results.md)、[計画124](124_base_recovery_plan.md)を先に読む。

## 将来確認するためのモデル保存版

[JMicro-10M-research-archive](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)へ主要3系列をpublic / gated=manualで保存済み。revision `853d52d2323653331b610249912fbe25615615fc`。native safetensors・共通Tokenizer・optimizer/scheduler/RNG等の数値状態・実装/設定/文書/評価metadataがある。データセットとsamplerは含めず、元checkpointの完全な代替ではない。[保存内容・uv読み込み手順126](126_model_archive.md)、[全公開fileのhash照合report](../reports/publication/model_archive_20261009.json)。

ユーザーの「データセットは残さなくてよい」は今回のアップロード対象から除く指定であり、既存のWSLデータを削除する指示とは扱わない。元のローカルdata/checkpointを削除・変更していない。

## 固定方針と実行範囲

10Mのサイズ維持がユーザーの優先条件。現在10,001,152 parameters、既存9.5M〜10.1Mの総parameter予算を保ち、大型化や大型モデル比較を復旧・改善の既定作業にしない。元の日本語Base品質基準を維持する。次の比較は計画124で選定する段階で、介入条件・教師予算・新configは未凍結。文書更新から学習/診断/data準備へ進まない。

## 正本と保存場所

| 項目 | 保存場所・確認済み構成 |
|---|---|
| Git正本 | Windows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`。最新local commitを引継ぎ、remoteが最新とは仮定しない |
| WSL実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| 大容量データ | `/home/aihub_ubuntu/jmicro-data`。Linux diskで処理・学習 |
| 確認済み環境 | WSL package3.0.1 / Ubuntu WSL2 / RTX4090 / Windows driver616.92 / Python3.12.7 / PyTorch2.14.1+cu130 / BF16 |
| Tokenizer | `artifacts/phase2/4096/tokenizer.model`、SHA256 `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318` |
| モデル | 10,001,152 parameters。最新2B候補、staged参考系列、元10B UIは別の重み |

WindowsのNVIDIA driverがWSL CUDAにも関係する。WSLへLinux display driverを追加しない。現在の環境変更は不要で、新PC・runtime変更時に必要な範囲だけ再確認する。学習の停止中にdriver更新やdata再構築を開始しない。

## 完了jobとUI

最新scienceは `reports/phase6/base-teacher-decay-2b-20261008/`。PID118881 / boot `4052bfc5-3850-44e4-9123-d34a9e19f36e` / start_ticks8215874は終了し、Windows worker38176はexit0。累積2B教師・212095更新、全80レビュー済み、不採用・固定条件closed。追加GPU26,060.094秒、pilot込27,475.228秒、ledger closed。**完了runを再起動しない。**

元[WebUI](http://127.0.0.1:7860)は10,000,007,168学習tokensの元10B checkpointを配信。2026-10-09 JSTの文書更新時にPID120460 / start_ticks10822295、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290` /busy=falseを再確認した。将来は `reports/local/webui/server.json` と実PID/boot/start、HTTPを再確認する。保存PIDだけで稼働を判定しない。

Windows正本でのUI操作:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
Invoke-RestMethod http://127.0.0.1:7860/api/model
```

[UI操作43](43_local_webui.md)。既に起動済みなら重複起動しない。停止中もUIは利用可能のままにする。明示的に再開されたGPU実験が必要なときだけidle確認後に停止し、終端で元モデルへ復帰する。

## Git外で必ず保全するもの

以下はWSL repo相対、またはdata root相対。Git/公開Hubだけでは学習済み状態を復元できない。

| 場所 | 内容 |
|---|---|
| `reports/phase6/base-teacher-decay-2b-20261008/` | 最新のlatest.pt、optimizer/scheduler/RNG/sampler/counters、metrics、resume gate、job/result、評価raw |
| `reports/phase6/base-teacher-decay-pilot-20261008/` | 同条件94M親、元config/source/履歴 |
| `reports/phase6/base-parallel-residual-comparison-20261007/` | 元sequential2B対照と閉じたparallel比較、重み・原レビュー |
| `reports/phase6/base-10b-20261004/` | 元UIのstable/final、特に `decay/checkpoint-00305176.pt` と再開state |
| data: `phase6/textbook-mixture-20261006/large` | 最新accepted混合2Bのstream/index/manifest/ready/source |
| data: `phase6/expanded-v2/shards` | 独立DEVとmanifest。TRAINとは分離 |
| data: `phase6/ten-billion/prepared-v2/export-001/shards` | 元12.23B Webとsplit/source履歴 |
| `artifacts/phase2/{4096,8192}/`、必要な `data/phase1/processed/` | pinned Tokenizer/pilot |
| 全旧run/data | staged参考系列・旧11B比較・失敗/採用候補・全Phase0〜5の記録。下記履歴リストも参照 |

最新latest.pt SHA256は `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442`。checkpointはGitに加えず、転送時は保存済みSHAへ照合する。移行しない通常文書更新で全重み・13GB index・全corpusを再走査しない。Gitには最新completion、全80notes、raw生成・小評価記録・終端stateを保存済み。

job.jsonの周期heartbeatは212080更新/1,999,868,016教師だが、最終result/train-result/checkpointは212095更新/正確に2B。runner resultのcontent_pendingはその後の[completion](../reports/phase6/base_teacher_decay_2b_completion.json)で解消済み。元記録を「修正」して履歴を失わない。

## 新PC・欠損時だけ行う復元

PowerShellで `wsl --version`、`wsl -l -v`、`nvidia-smi` を確認する。WSL package3.xとdistributionのWSL2は別の値。必要時のみ `scripts/setup_windows_wsl.ps1` を使い、昇格・再起動・初回Linuxユーザー作成が必要なら外部blockerを記録する。

Linux project rootで固定環境を復元する:

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
git config --local user.name yousan
git config --local user.email ka1357amnbpdr@gmail.com
```

全Pythonは `uv run --frozen --extra hub --extra data --extra ml --extra export ...`。依存変更は `uv add`。system Python/pipへ切り替えない。Mac/別OSのvenv/native binaryはコピーしない。

固定公開pilot/Tokenizerはcommit `0b1042979bf32899e24da30790e3ae6b239013c3`、manifest SHA `8072bd218be26637a51c7c11540f1c8c636392c3b1a91f805a5e317e6ca55a09`。不足時のみ次を使い、hash確認後に復元する。[詳細](huggingface_handoff.md)。

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/download_hub_artifacts.py
```

Hubには学習済み重み・12.23B shardsはない。環境変更時の証拠は新しい保存先へ記録し、既存Phaseの完了reportを上書きしない。必要時の環境取得:

```sh
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/experiment.py capture-environment --probe-torch --output reports/local/handoff/environment.json
```

## 再開時の手順

1. 最新Windows local commitとAGENTS/status/roadmap/本書/計画124を読む。
2. ユーザーが再開した範囲と10M維持の固定条件を確認する。文書更新だけならGPU/data/診断へ進まない。
3. 実process・GPU lock・job/result・有効checkpointを確認する。観測timeoutや残存lockだけで終了を決めない。
4. 最新teacher-decay pilot/2Bは完了・不採用なので復旧対象にしない。計画124の次条件選定から始める。
5. 新実験は不足command/型付き証拠接続/関連checks/予算/configを先に完成する。長期jobは全state再開gate・永続identity/ledgerを必須とする。
6. native方式の独立seed/fullDEV/TEST接続は未完成。旧stable+20M形式へ偽装しない。Base採用前にChatや量子化へ進まない。

本当に未完了のjobを復旧する場合に限り、同じ凍結条件・累積予算でvalid checkpointから再開する。歴史的なrestart commandは現在の実行指示ではない。外部公開・有料cloud・他者連絡は別途許可が必要。自動pushなし。

更新前の全引継ぎ原文と旧runの詳細リストは[引継ぎ履歴20261008](windows_handoff_history_20261008.md)。実験記録やPhase0〜3を消さず保全する。
