# Baseのquery依存Attention出力ゲート比較

2026-10-07。Base限定の新しい比較を定義し、モデル・trainer・評価経路のCPU検証を終えた。GPU検証・本学習・品質評価はまだ実行していない。Baseは未完成・未採用で、Chat/SFT/量子化へ進まない。

直近の同100Mのoptimizer変更は文章の一貫性を改善しなかった。一方、既存のstaged学習には文章品質が上がってWeb本文BPBが悪化する条件がある。今回は同じ教材・教師量を保ち、Attentionで読んだ情報を出力へ書き込む経路に、queryに応じた非線形の選択を加える仮説を一つ検証する。

[一次論文](https://arxiv.org/html/2505.06708)のG1/headwise gateと[著者実装](https://github.com/qiuzh20/gated_attention/blob/main/modeling_qwen3.py)は、SDPA出力にquery由来のsigmoidを掛け、その後に出力projectionを適用する。主な実験規模・初期学習・言語条件は本プロジェクトと異なる。日本語10Mでの有効性、Attention sinkの存在や解消を証明した資料として扱わない。

既存のAttention飽和診断は陰性だったため、それを理由としたQK normalization・softcap等の再試行はしない。今回の出力ゲートはsoftmax前の正規化とは別の機構である。また、既存の`gated_shared`は二回目のblock呼出しをscalar residual gateで調整するもの。今回は各blockを一回だけ呼び、各query token・headのSDPA出力を調整する。

両条件とも元10B重みから独立にコピーし、追加ゲート行列を0、Attentionの`o_proj`重みを2倍にする。初期sigmoidは1/2なので初期の予測関数を保つ。ただしAdamWの更新は元のparameterizationと同じではないため、保存済みnative CEをmatched controlへ流用しない。

| 条件 | SDPA出力に掛ける値 | 初期状態 | パラメータ数 | 新規教師量 |
|---|---|---|---:|---:|
| 新しい対照static_half | 常に1/2 | 元モデルの予測と一致 | 10,014,464 | 100M |
| query_headwise | sigmoid(query由来のhead別score) | 元モデルの予測と一致 | 10,014,464 | 100M |

両条件に同じゲート行列・projection計算・optimizer partitionを持たせる。対照の追加ゲート勾配は0で、行列は0のまま。物理パラメータ数は同じだが、候補にはゲートを学習する自由度がある。元のnative10,001,152より13,312（約0.133%）多い約10Mモデルで、exact native architectureとは区別する。元model.pyは変更していない。

同accepted2B TRAINから各Web75M・教材20M・物語5Mを、同じOriginalTrainCorpusSampler/full metadata/元body+EOS/maskで学習する。新固有教材・Tokenizer変更は0。両条件fresh AdamW/constant LR1e-5/WD.1/betas(.9,.999)/eps1e-8/clip1/seed42/batch48。新科学合計200Mを検証教師・保存済みnative CE100Mと別会計する。

CPUでは以下を確認した。

- 独立したsigmoid計算・解析微分、元parentを変えないconversion、cache・padding・causal/future isolation、モデル/Adam保存再開、静的ゲート0と候補の非ゼロ勾配、実parameter countと語彙tie。
- 元10BチェックポイントをCPUで読込み、既存TRAIN24窓の全logitsが両条件とも元と完全一致。実CPU1.304994秒、GPU0、更新0、品質生成0。128以下と誤認した初回prepareの拒否後、全24窓を変更せず元context範囲で確認した。
- 原CE・各source教師・入力digest・fullsamplerの両条件一致、両条件それぞれ連続4更新対2更新save+2更新の全model/Adam/scheduler/RNG/sampler/counters/history一致。更新途中の例外後はsave/continueを拒否し、有効checkpointから復旧できる。
- typed evaluatorが同じゲートモデルを尤度・cache・生成へ渡し、例外後に既存factoryを復帰する。実GPU評価・日本語品質を測ったものではない。

最終CPU33checks/4.93秒（モデル16＋trainer/evaluator17）。初回モデルは解析testの8次元fixtureが実32次元と合わず1failed/13pass。初回trainerは静的ゲートの検査がSwiGLU MLPの`gate_proj`まで対象にし13failed/4pass。検査を`.self_attn.gate_proj.weight`へ限定し、静的モデルの正常ロードを含むpositive controlを追加した。旧source/XMLを保持し、モデルのloader以外のASTが同じことを確認して元10B初期forward証拠を再利用した。gate関数・初期化・教師・optimizer・GPU上限・品質基準は変更していない。

現在の正本は[準備v2](../reports/phase6/base_headwise_gate_preparation_v2.json)。[元の事前案](../reports/phase6/base_headwise_gate_proposal.json)・[CPU初期parity](../reports/phase6/base_headwise_gate_parent_CPU_parity.json)も保存し、初期の誤ったloaderを現行として使わない。

次は専用の永続CUDA probe/launcher、science runner/reviewerを実装する。probe180秒以内に、両条件の実CUDA4対2+2/fullstate・fullhistory、BF16/Flash・48×1024有限forward/backward、resident90%以内のVRAM、両全32stepの速度を測る。各条件の予測は`ceil(100M * 全32step秒 / 全32step教師tokens * 1.3 + 評価・保存900秒)`。両予測の和＋実probeが事前総上限9,000秒に収まった場合だけscienceを凍結・起動する。旧FFN/MHA上限の変更や、遅いsubsetを捨てた予測は行わない。

実学習後は同DEV256/common472,055bytes、日本語192/331/1119、同greedy64の80件×両条件を全件個別に読む。新static対照・強いstaged対照の元relative条件、絶対文法56/一貫性27/適切27/EOS37以上・反復18以下・errors0、歴史Web BPB上限0.9812859519097707をすべて維持する。合格候補だけ独立学習seed/full DEV/保護TEST/採用へ進める。不合格時はこの固定headwise・初期化・親・LR・source・教師・予算条件を終了し、elementwise/別head数/gain/LR等で救済しない。

元10B WebUIはCPU作業中も継続、actual2758/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start287335、HTTP親SHA410f975d…/busy=falseを確認した。品質Baseが実際に完成したらユーザーへ通知して停止する。今回の実装・CPU成功はBase完成ではない。
