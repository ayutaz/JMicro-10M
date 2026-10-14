# 10Bの同条件品質評価

2026-10-04、総10,000,007,168 tokensの最終10B checkpointを、以前と同じ全文devと固定400生成で評価した。**本文BPBと反復指標は改善し、raw文字化けは0件。固定greedyの自然EOS停止は0/80のままで、意味・数量・時刻・否定の誤りも残る。**

[保存結果とCPU確認23項目](../reports/phase6/base_10b_comparison_review.json)、[固定80・自然停止9件の内容確認](../reports/phase6/base_10b_content_review.json)、[実process終了記録](../reports/phase6/base_10b_comparison_completion.json)。元の増量安全gateと最良WebのBPB改善条件に合格し、10Bを次の仕上げ比較の候補として保持する。Base/Chatの品質目標達成とは判定しない。

## 同じ評価による比較

dev89,416文書、164,344,743本文bytes、42,003,934本文tokensを一度ずつ採点。context1024/stride512/batch16、BF16/math backend、FP32のtoken別CE。BPBは小さいほど良く、EOS lossは本文BPBの分母・分子から分離した。

生成は固定dev80入力×5条件＝400出力。greedy抑制あり・なし、sampling seeds42/43/44、temperature0.8/top_p0.9、各64新規tokens上限。EOS bias・強制停止・新decoderは使わず、raw IDs/bytes/text/flagsを維持した。表の固定80は抑制ありgreedy。

| モデル | 学習input tokens | 全文BPB | 固定自然EOS | 固定反復 | 全400 raw Unicode失敗 |
|---|---:|---:|---:|---:|---:|
| 元2B | 2,000,027,648 | 0.982882 | 0/80 | 60/80 | 0/400 |
| 元5B | 5,000,003,584 | 0.964484 | 0/80 | 59/80 | 2/400 |
| Web仕上げ5.1B | 5,100,011,520 | 0.958092 | 0/80 | 57/80 | 0/400 |
| 短文仕上げ5.1B・参考 | 5,100,011,520 | 0.959011 | 13/80 | 51/80 | 2/400 |
| **新10B** | **10,000,007,168** | **0.954018** | **0/80** | **53/80** | **0/400** |

10Bの正確なBPBは0.9540184727984398。元5Bから−0.010465598（−1.085098%）、最良Web5.1Bから−0.004073508（−0.425169%）。固定反復は元5Bから6件、Web5.1Bから4件減った。全400反復は元5B122→10B112、Web121→112。空応答・役割漏出も10Bは各0/400。

自然EOSは全400では元5B5、Web5.1B13、10B9。10Bの9件はsamplingのみ（seed42:4 /43:2 /44:3）。固定greedyでは全80件がtoken上限停止であり、停止問題は解決していない。sampling停止もWebより4件少なく、EOS改善とは報告しない。

モデルは10,001,152 parameters、準備済みtrain poolは12,225,819,077 tokensのまま。今回はデータを新規収集せず既存pool内の学習量を増やした。短文枝は異なるmixtureなので純粋な学習量比較の参考に留める。stable親と減衰期間が異なる系列の単一seed観測であり、差のすべてを学習量だけの因果効果や統計的有意差とは断定しない。

## 生成内容に残る問題

10BとWeb5.1Bの同じ固定80出力を全件読み、10Bの自然停止9出力も全件確認した。これはCodexによる内容診断で、独立した人手blind採点や正答率測定ではない。

- 関連する導入が良くなった例はある。base-019ではWebの「息が止まらなくなった」から10Bの「息が切れてしまう」へ、base-016では料理を作る話から食べる話へ改善した。ただし後続の反復は残る。
- 数量・時刻の誤りは残る。base-051の3個−1個に2個を答えず、base-055の1000円−700円に300円を答えない。base-057は3個を3種類と取り違える。base-059は16時を答えず、自然停止したsampling出力も12時半と誤答した。
- 比較・否定・因果を保持しない。base-056で20度を15度より低いと述べ、base-085で甘いものを食べない姉に菓子を勧める。base-082は鍵がないのに鍵を開ければ見つかると述べ、base-090は雨が吹き込む窓を開け続ける。
- 局所的な退行もある。base-099は乾いた靴下を履く導入を不自然な脱ぐ動作へ、base-100は外出前に靴を履く導入を脱ぐへ変えた。改善件数を正答率へ換算していない。
- 元の反復指標は三回完全一致を検出する。flagがfalseでも二回の同文や言い換えの重複が残る（base-015/016/066など）。結果を見て検出条件を変更していない。
- 自然停止は完結した適切な内容を保証しない。base-011には「つづく」や縦棒、base-059には「固定リンク」が出る。base-020/seed44の短い関連文で止まる例もあるが、大半には逸脱・矛盾が残る。

## 採否と検証範囲

凍結した元条件は、両対照に対して全文BPB悪化+0.001以内、固定反復増加8件未満、全400のraw Unicode/empty/role0、生成条件一致。さらに最良WebよりBPBが小さいことを要求する。**10Bはこれらの自動条件をすべて満たした。** 原Base/Chatの文法・関連性・対話・停止品質条件は緩めていない。

関連23 CPU tests成功。初回に過去EOS設定5件のschema欠落を見つけ、元config/resultsを変更せず厳密const schemaを追加して修復した。[修復記録](../reports/phase6/base_10b_comparison_schema_repair.json)。完了reviewの23項目で、全devの有限NLL/本文一回採点/common-byte BPB、全400のraw flags、旧dev/生成key一致、元gate再計算、凍結hash、評価のRNG/mode/weights隔離、実process終了、全80と全自然停止の内容確認を検証した。

GPU時間は **786.881秒（13分7秒）**、全文376.052秒・生成409.008秒で、評価上限1,800秒以内。LinuxPID442とWindowsPID31900は終了済み。追加学習tokensは0、旧5B/5.1BをGPU再評価せず保存結果を再利用した。

raw evidenceはLinux repoの `reports/phase6/base-10b-comparison-20261004/` にjob/result、全文文書別NLL、400生成、固定80比較packet、自然停止packet、pipeline log/source snapshotを保持する。configは[専用評価設定](../configs/phase6/base_10b_comparison.json)、実行入口は `bash scripts/compare_base_10b.sh`。完了済みなのでGPU再実行しない。評価重みSHA256は `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290` で不変。

保護test、独立人手blind採点、Chat、新重みの量子化品質は未実施。独立全12.23B corpus auditの未完了も保持する。今回の依頼は品質評価までなのでreport/local commitで停止する。次回EOS仕上げを実行する場合は[既定の単一Web/短文20%比較](39_learning_scale_and_generation_plan.md)を10B親に適用する条件を整える。20B/50Bやdecoder変更を自動で始めない。
