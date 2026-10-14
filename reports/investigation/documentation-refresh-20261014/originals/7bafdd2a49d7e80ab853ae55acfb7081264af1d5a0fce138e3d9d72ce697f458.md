# 条件保持selector改修と各100M比較

2026-10-05 JST。ユーザーの「4まで進めてください」により、結果63後の四項目を再開する。旧計画61の準備失敗を再採点せず、新しい実験としてコード・データ・原文・判断を別保存する。元の受け入れ/採用条件を緩めない。

1. **選別方法の改善・検証**: 既存trainから、過去の確認教材と重ならない固定32全文を抽出する。人物の意図/否定、物の所在と回収、結論の具体性について個別理由を保存し、従来selectorと新selectorの検出・誤除外・検出できない欠陥を比較する。架空設定自体を誤りにしない。ルールと関連testsを凍結してから受け入れsampleを抽出する。
2. **教材の再確認**: 同じpinned翻訳trainから、量・文書長全並び・BOS/EOS位置が一致する各約20Mのwhole-doc poolを作る。過去の確認教材と今回の32を除き、未確認の固定random40各を同一rubricで診断する。候補弱例が対照より少なく、かつ10/40以下、量/長さ/EOS・train/whole-doc条件を満たす場合だけ学習に進む。sampleの再抽出や受け入れ結果を見た再改修はしない。準備不成立ならその理由を保存して停止する。
3. **条件成立時の同量学習**: 元final10Bの同じoptimizer/RNG/Web cursorから二枝各100,007,936tokens（3052updates、短文610updates=19,988,480、Web80,019,456）。batch32/context1024/seed42/Flash+compile、共通peak0.0001/stable2900/decay152/floor0.00001。新configで実CUDA連続対再開の全state一致を確認する。科学200,015,872と検証262,144を別記録。元UIはGPU中のみ停止しfinallyで復帰する。
4. **評価・判断**: 同じdev256/固定80greedy最大64/意味192/JBLiMP331/JCQA1119、全160個別内容理由を保存。元の一貫性+8/80かつ対応95%下限>0、EOS/反復非悪化、BPB+1%以内、実用一貫性/適切完結各27・EOS37・反復18の条件と保存Web安全条件を維持する。全一次条件通過時だけ候補の全文89416/400/長文40を実施し、原full gateで判断する。report/status/verified local commit/元10B UI確認で停止する。

CPU抽出・選別・保存は累積1800秒、CUDA確認＋科学＋一次GPU評価は累積1200秒、条件付きfullは追加1800秒。実装・個別内容診断は別会計。新取得・再tokenize・主Web全走査・Tokenizer再学習を前提にしない。候補供給と品質を実データで測り、提案を合格の証拠にしない。独立人手blindと主Web全件監査は未完了のまま。

入力sourceは結果63と同じ `shibatch/TinyStories-JA` revision `155b4e5842076c90e07a4934d5b68410fe21f65f` の既存取得済みtrain。結果63の20M poolと全80理由・凍結source/reportは保持。新学習は準備条件成立前に開始しない。500M/1B延長・20B/50B/Chat/protected test/push/公開へ自動移行しない。

開始時にWindows正本commit6908b44/clean、元10B UI actual359102とHTTP親SHA410f975d…/学習10,000,007,168/busy=falseを確認した。新data/runtimeは実装中で、実結果は以下へ追記する。

## 段階1の実証拠・selector凍結

過去の確認教材と重ならないv1適格trainから、seed202610064で固定32全文を抽出し全個別診断を保存した。弱例12/32。v2はこのうち9を除外し、正しい20のうち4も除外、残った19は弱例3/正しい16。この32はルール開発用で、独立な受け入れ評価や全コーパス品質の推定ではない。具体的な動作で結ぶ条件も変えたため、架空話や悲しい結末を含む正しい教材の誤除外がある。誤除外を隠さず、sample32の数字で準備合格としない。

明示した意図の直接否定、投げた対象の回収なしの返却、施錠した扉の解錠なしの開扉、限定されない「二度と」の達成、明示された能力制約の説明なしの解除を扱う。locativeの省略対象・具体的な末尾動作もproxyとして使う。一般的な算術/大小、全ての暗黙参照、語義や世界知識の正確さは未解決。関連5testsで最小対と正しい魔法/失敗を確認した。これから両poolを作り、未確認40各で準備を判定する。selectorはこの時点で固定し、受け入れsample後の改修はしない。

可搬証拠: [固定32](../reports/phase6/condition_v2_calibration.json)、[全32理由とv1/v2比較](../reports/phase6/condition_v2_calibration_review.json)、[authored notes](../reports/phase6/condition_v2_calibration_notes.json)、[5tests](../reports/phase6/condition_v2_selector_tests.xml)。新data `/home/aihub_ubuntu/jmicro-data/phase6/condition-v2-20261005/`、run `reports/phase6/condition-v2-100m-20261005/`へ旧実験とは別に保存。
