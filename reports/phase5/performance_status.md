# Phase 5: 実行環境・VRAM・速度

2026-10-03。学習はWSL 2 / UbuntuのLinux checkoutで実行する。Python 3.12.7はuv管理、RTX 4090、FP32 parameters / BF16 autocast、context 1024。Windowsはコード・Gitの正本とWSL launcherを保持する。

## 現在の100M比較

| Run | Micro batch | Backend | 定常中央値 tokens/s | 学習ピークallocated VRAM GiB |
|---|---:|---|---:|---:|
| T8K / QK-Norm / LR 0.002 | 8 | eager/math | 117,119 | 4.482 |
| T4K / QK-Norm / LR 0.002 | 8 | eager/math | 111,693 | 4.300 |
| T4K / NoQK-Norm / LR 0.002 | 8 | eager/math | 121,139 | 3.866 |

VRAM 24 GiBを最大限使う設定ではない。学習ピークはtrainerのCUDA allocated計測であり、nvidia-smiのreserved/contextを含む使用量とは異なる。速度・VRAMは各training auditのmetrics/run記録から得た実測値。生成評価中のGPU使用率やメモリ量を学習の稼働率として扱わない。

batch 8は100Mあたり12,208更新を確保する小予算の比較条件。途中でbatchやbackendを変えると凍結した対照実験の学習履歴が変わるため、この比較は設定を維持する。

## 測定済みの高速化と採用制約

[Phase 4速度report](../phase4/throughput_report.json)ではcompile/default、batch 8でT8K 439,656 / T4K 448,601 tokens/sを測定した。compile初回時間を除く短い定常測定であり、今回の100M全体をその速度で完了した証拠ではない。eager/default最大安定batchはT8K 57 / T4K 64、速度225,169 / 218,411 tokens/s。容量はallocator上限94%・3×200更新と評価/保存で確認した条件付きの値。

Phase 5ではcompile/defaultとeager/defaultが厳密な連続200 vs 100+100更新の保存再開検証で失敗した。消費列/RNG/samplerが一致してもloss/weights/optimizerが一致しないため採用しない。[失敗記録](failed_attempts.json)を保持する。eager/mathではT8K/T4K/文書overfit/NoQK-Normの4構成が全state完全一致を通過した。[再開証拠](resume_report.json)

高速化は完了していない。compiled/mathの正確な再開と速度、math backendの最大安定batchは未検証。明示的Flash-onlyはnon-null attention mask非対応で失敗しており、成功したFlash高速化とは記載しない。Phase 4のdefault最大batchをmath backendの容量保証として流用しない。

## 次の境界

今回のPhase 5比較・評価・候補選定を固定条件で完了して停止する。Phase 6をユーザーが再開した際、本学習開始前に候補構成でbackend/compile/batchを比較し、有限値・厳密な保存再開・評価/保存時のheadroom・cold start・実測速度を揃えて設定を決める。VRAMを埋めることだけを速度の達成条件にはしない。生成評価の速度も学習速度と分けて測る。
