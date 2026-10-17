# 実行環境とデータ配置

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

Git正本はWindows、実行・大容量data/重み/samplerはWSL。Python3.12.7/uv frozen、WSL2/Linux disk/RTX4090が記録された環境。最新runの科学GPU777.297900秒を台帳へ全額加算済み。過去の高速Flash/compile速度をfresh独立native pipelineの見積りに流用しない。機器・package・PIDの値は観測時点の記録。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

## 設計・手順の保存記録

以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。

## 作成時点の資料・契約

## 実機環境

| 項目 | 確認結果 |
|---|---|
| Windows / WSL package | Windows build 26100.6584 / WSL 3.0.1.0 |
| Linux distribution / 実行方式 | Ubuntu / WSL 2、user `aihub_ubuntu` |
| GPU / Windows driver | RTX 4090、24,564 MiB / 616.92 |
| Python / Linux uv | 3.12.7 / 0.9.0 |
| PyTorch / CUDA | 2.14.1 / 13.0、lock runtime 13.0.96 |
| precision | FP32 parameters/optimizer、BF16 autocast |
| 検証 | Phase 4: CUDA/BF16 finite forward/backward・64 tests、Phase 5: 68 tests・4構成のmath厳密resume、Phase 6①②: 74 tests・73 GPU checks・WSD stable/decay全state完全一致（全skip 0） |

WSL packageの3.xとdistributionのWSL 2は別のversion。NVIDIA driverはWindows側のものを使用し、WSLへLinux display driverを追加しない。[NVIDIA公式手順](https://docs.nvidia.com/cuda/wsl-user-guide/)。Linuxのnvidia-smi表示にはツール版615.71.08もあるが、driverの観測値は616.92。

## iMacから学習PCへ切り替える境界

Phase 0〜3はM1 iMac上の履歴。コードと公開pilot/TokenizerをWindows/WSLへ引き継ぎ、Phase 4で実GPU検証を完了した。Macの仮想環境・native binaryは移していない。新規PCの復元は[引継ぎ手順](windows_handoff.md)、復元済みPCの再開は[現在の状態](autonomous_status.md)を読む。

Python実行は一時スクリプトも`uv run --frozen`。導入は`uv python install 3.12.7`、依存復元は`uv sync --frozen`、変更は`uv add`。通常のWSL実行は`--extra hub --extra data --extra ml --extra export`を付けて固定環境を保持する。

## 最大バッチの決め方

本学習では最大安定容量と最速micro batchを実測し、速度・保存/評価余裕・再開一致から設定を選ぶ。以下はPhase 4時点の履歴。Phase 4はcontext 1024、accumulation 1、eager/default SDPA、fused AdamW、CUDA allocator 94%上限で測定した。

| モデル | 最大安定micro batch | effective tokens/update | 次のOOM batch | 定常中央値 |
|---|---:|---:|---:|---:|
| T8K | 57 | 58,368 | 58 | 225,169 tokens/s |
| T4K | 64 | 65,536 | 65 | 218,411 tokens/s |

倍増と境界の中間値を探し、最大値を3×200更新、評価・保存込みで確認した。測定点の最高速度はcompile batch 8で439,656 / 448,601 tokens/s。compile経路の最大容量は未探索。最大容量と最高速度を区別し、backend/context/precision/optimizerを変える場合は新しい設定で検証する。小探索のeffective batchと更新数は別に固定する。

Phase 4の短い速度・有限値probeではdefault、math-only、compile/defaultが成功。Phase 5の厳密resumeではcompile/defaultとeager/defaultが失敗し、採用したeager/mathだけが全state一致を通過した。Flash-onlyはnon-null attention mask非対応で失敗を保持している。③ではPADなし固定長の学習専用causal経路を実装してFlashを検証済み。推論/cacheの明示maskは維持する。[Phase 4実測](21_phase4_completion.md)、[現在の速度と制約](../reports/phase5/performance_status.md)

Phase 5の選択候補T4K NoNorm / math / batch 8の学習ピークallocated VRAMは約3.866 GiB、定常約121,139 tokens/s。③の拡張shard/WSDではreference/math最大45、compiled/math最大53、compiled Flash最大111。最速のFlash＋compile reduce-overhead batch 32=694,521 tokens/sを採用した。選択設定のpeak allocatedは5.73 GiB、driver peakは7.53 GiB。最大111はdriver 23.42/23.99 GiB、112 OOM。厳密/cold再開は完全一致。[③の完了証拠](29_phase6_performance_completion.md)。以降のgateは[Phase 6計画](24_phase6_plan.md#開始前に揃える条件)で定める。

## ストレージ配置

Windowsコード正本は`C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは`/home/aihub_ubuntu/src/japanese-tiny-llm-10m`。

```text
~/src/japanese-tiny-llm-10m/
  artifacts/phase2/{4096,8192}/   公開Tokenizer
  data/phase1/processed/         固定pilot、manifest、sample
  reports/phase4/gates-20261003/ ログ、source snapshot、検証checkpoint
  reports/phase5/run-20261003-docoverfit/  実学習/評価・snapshot・checkpoint（終了済み）
  reports/phase6/preparation-20261003/    準備audit/CUDA run・12 checkpoints（終了済み）
  reports/phase6/performance-20261003-v3/  ③の測定・全state検証・source snapshots（終了済み）
  reports/phase6/performance-cold-resume-20261003/  空compiler cache再開（終了済み）
  reports/phase6/readiness-20261003/  ④⑤のGPU比較/全文評価/生成/変換・source snapshots（終了済み）
  artifacts/runtime-stable-f32-v2/  NoNorm CPU精度profileの専用native runtime（構築・検証済み）
~/jmicro-data/
  shards/{t8k-pilot,t4k-pilot}/   Phase 4〜5 pilot入力
  phase6/raw/                    固定8 Parquet・条件資料・receipt
  phase6/expanded-v2/            拡張corpus・SQLite・signatures・shards・全監査
  gpu.lock                      単一GPU job排他
```

ユーザーの約8TBストレージ計画とWSL内の実容量は別。Phase 4監査時のLinux空きは980,811,743,232 bytesだった。Phase 6①②完了時は950,875,688,960 bytes（約885.6 GiB）、VHDの上限は約1TB。8TB全体がLinuxから使えることは未確認。uv cache約19.27GB、venv約6.07GB、Phase 4成果物約1.47GBはapparent bytesで、hardlinkを重複排除していない。[実容量と予算](../reports/phase4/resource_budget.md)

Phase 6①②の拡張dataは15,431,198,093 apparent bytes、rawは別途2,152,539,810 bytes、CUDA runは1,447,634,238 apparent bytes。[測定証拠](../reports/phase6/completion_audit.json)。空き容量は各job開始時に再確認する。

## 事前tokenizeと実装済みshard

学習中のon-the-fly tokenizationを避け、公開corpusのWeb trainを共通wrapperでencodeする。会話/sharealikeはBase系列へ混ぜていない。各split一本のlittle-endian uint16 `.bin`、document index、token-byte情報、hash付きJSON manifestを保存する。現在のpilot実装は複数shard/source mixtureの大規模loaderではない。

T8K trainは18,022 docs / 6,884,183 stream tokens / 32,774,150 body bytes、T4Kは同じ文書・bytesで8,398,329 tokens。stream countはBOS/EOSを含む。固定長blockをseed/epochでshuffleし、文書を跨いでpackする。BOS targetsをmaskし、最後の不完全train blockは使用しない。dev/testは文書単位で別評価する。[データ手順](../data/README.md)

Phase 6①では同じ公開T4Kでtrain 756,087,912 stream tokens / 1,604,292 docs / 2,946,200,160 body bytesの拡張shardを作成し、dev/testを別binへ分離して全件監査した。[保存先と契約](../data/README.md#phase-6拡張corpusと全件監査)。Web 100%の単一sourceで、複数source mixtureは未実装。

50B tokensのID本体は約100GB、100Bは約200GBという算術値。二つのTokenizer版、raw、index、checkpoint、一時領域は別加算。50〜100B master corpusは未取得で、実容量を計測してから拡張する。

## benchmark済みと残る測定

synthetic/実shard、eager/compile、backend、batch、peak VRAM、data wait、評価/save時間を測定済み。③でcompiled/math/Flash容量探索も完了した。Windows volumeとLinux filesystemのI/O比較、DataLoader単体、厳密なMFUは未実施で、完了条件へ追加せず必要性が出た時の別対照とする。③の成功をPhase 4の履歴へ遡及しない。

長期予算は実測tokens/sから計算し、評価/save/compile初回/データ処理/比較runを加える。Phase 4のT8K Norm/default最大batchでは10B compute約12.34hという算術値を得たが、Phase 5の厳密resumeを通過した現候補の保証ではない。最新③のFlash＋compile batch 32の694,521 tokens/sでは500M約12分、10B約4時間の純学習算術値。全文評価・保存・cold compile・decay枝・LR調整は別計上し、⑤で長期予算をversion2へ凍結済み。[凍結設定](../configs/phase6/base_frozen.json)はLR0.002の定常693,666 tokens/s、10B純学習約4時間、全decay枝約22.2分、5回の全文dev/400生成約58.1分を別計上する。checkpoint推定347件/41,702,694,225 bytes、run上限100 GiB・最低空き200 GiB。[次回の予算](24_phase6_plan.md#暫定のcompute見積もり)。品質改善に必要な総期間の保証ではなく、20B/50B着手はロードマップの条件に従う。
