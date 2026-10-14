headwise Attention出力ゲートの比較を終了し、不採用とした。品質基準を満たすBaseは未完成で、Chat・量子化・展開は開始していない。

元10Bモデルから、固定した半分ゲートとquery依存ゲートを独立に学習した。両方10,014,464パラメータ、同じ既存2B TRAIN、Web75M・教材20M・物語5Mの正確100M教師tokens、fresh AdamW/constant LR1e-5/seed42/batch48を使った。新しい教材は追加していない。固定ゲートも出力projectionを2倍にした同じ初期変換を使い、以前のnative CEをこの対照へ代用していない。

| 条件 | 今回の学習量 | BPB | 文法2 | 関連2 | 一貫性2 | 適切完結 | EOS停止 | 自動反復 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 新static_half対照 | 100M | 0.998472 | 41/80 | 27/80 | 1/80 | 2/80 | 19/80 | 45/80 |
| query_headwise候補 | 100M | 0.998350 | 40/80 | 28/80 | 1/80 | 2/80 | 17/80 | 48/80 |
| 保存済みnative CE参照 | 過去の100Mを再利用 | 0.998487 | 44/80 | 25/80 | 2/80 | 2/80 | 19/80 | 45/80 |
| 保存済みstrong staged参照 | 過去結果を再利用 | 1.133613 | 65/80 | 39/80 | 23/80 | 26/80 | 76/80 | 2/80 |

BPBは共通DEV256文書・472,055bytesで測定した。両条件のUnicode/role/empty失敗は0。候補の日本語選択式は意味192=61.4583%、JBLiMP331=77.0393%、JCQA1119=34.5398%。対照は60.9375%、77.3414%、34.7185%だった。

候補のBPB差は約−0.000123だが、一貫性の増加は0件、paired95%CIは[0,0]。EOSは2件減り、反復は3件増えた。strong参照に対する一貫性差は−22件、CIは[−0.375,−0.175]。新static・strong・保存済みnativeの全相対条件、絶対品質条件、歴史Web BPB条件のいずれも全合格には至らない。[採否記録](../reports/phase6/base_headwise_gate_comparison_review.json)に各条件を保存した。

全160件を個別に読み、raw SHA付きnotesと理由を保存した。固定優先順の過去同文採点を対照69件・候補68件で保持し、既存採点の差異22件・20件も記録した。候補には最後に新staticの同文採点を参照する。評価者は非blindのCodexで、独立人間評価ではない。[対照notes](../reports/phase6/base_headwise_gate_static_half_notes.json)、[候補notes](../reports/phase6/base_headwise_gate_query_headwise_notes.json)、[同文採点の履歴](../reports/phase6/base_headwise_gate_rating_reuse.json)を参照。

両17,698更新の有限history、model/Adam/scheduler/RNG/full sampler/counters、語彙tie、静的ゲート0を監査した。両条件・保存済みCEとの元教師/入力digest/全samplerの11条件も一致した。凍結v1 reviewerにはPT tupleとJSON listの比較、およびCPU readerのfp32/math設定をCUDA学習のbf16/flashへ直接比較する問題があった。元sourceを保持したままv2/v3評価adapterを追加し、同じ実GPU終端stateで拒否を再現し、値・学習precision・全stateを厳格に確認して受け入れた。異なるbetaと異なる学習precisionは拒否する。CPU監査でGPU学習を代用していない。

科学・自動評価のGPU占有は2,986.084726秒、own probe16.900100秒を含め3,002.984826秒（約50分）。科学6,838秒・総9,000秒上限内だった。検証86更新/500,626教師とstress49,152 backward位置は科学へ含めない。実科学9140は終了、launcher exit0、元10B WebUI10860/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start811347の実aliveとHTTP親410f975d…/busy=falseを確認した。

[終了記録](../reports/phase6/base_headwise_gate_comparison_completion.json)と107text/212,028,151bytesのmanifest、圧縮90,886,926bytes/SHA60d8ab43abd572fad75fff377792ad493579105904c8c1899e6ec7455837b5d4をWindowsへ保存して照合した。tensor/corpusはnativeで保持する。

この固定headwise・初期化・親・source・LR・教師・予算の比較を閉じる。追加のゲート形状や係数等の救済探索は行わない。今回の成熟親への100M適応という範囲を踏まえて既存比較を整理し、次の独立した根本要因を一つ定義する。品質に合格した候補だけ独立学習seed/full DEV/保護TEST/採用へ進め、Base完成時に通知して停止する。
