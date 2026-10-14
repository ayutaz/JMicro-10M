# 条件保持selector v2の検証・教材準備結果

2026-10-05 JST。[実行64](64_condition_selector_v2_execution.md)の四項目を、明記した**教材準備不成立の停止分岐**まで実施した。段階1・2と採否を保存し、段階3の各100Mと段階4のモデル評価/条件付き全文は未起動。学習比較を完了したとは扱わない。元の受け入れ・モデル採用条件は維持する。

## 結果と判断

| 範囲 | 対照/v1 | 候補/v2 |
|---|---:|---:|
| 開発用固定32の弱例 | 12/32 | 選別後3/19 |
| 開発用で除外した弱例 / 正しい例 | 0 / 0 | 9 / 4 |
| 新pool tokens | 20,000,072 | 20,000,072 |
| 全文数 | 71,268 | 71,268 |
| 平均body tokens | 278.631868 | 278.631868 |
| body長 min/25%/median/75%/max | 70/242/276/314/512 | 70/242/276/314/512 |
| EOS/1000tokens | 3.563387 | 3.563387 |
| body bytes | 83,690,260 | 83,216,801 |
| 未確認から固定抽出した40の弱例 | 12/40 | 14/40 |

両poolのtoken量・全文長の全並び・BOS/EOS位置は一致。共有10,232文書を明記し、独立なpoolとは主張しない。新しい40では候補の弱例14が対照12より少なくなく、10/40以下の上限も満たさない。**二つの準備gateが未達のため候補不採用**。受け入れsampleを再抽出・再採点せず、ルールを結果に合わせて再改修せず停止した。

開発32の数字はルールを作る際の診断で、未確認例への改善や全pool品質を証明しない。今回、その転移を受け入れsampleでは確認できなかった。非blind・各40という小sampleで、一般的な品質悪化や有意差を確定もしない。**科学学習0/検証0、新GPU学習・評価0**。EOSやモデル精度の変化は測っていない。

## 段階1: 別train例でのルール開発と凍結

既存v1適格trainから、過去に確認した教材と重ならない32全文をseed202610064で固定抽出した。全32に個別理由を保存し、弱例12を確認した。v2では明示された意図の直接否定、投げた物の回収なしの返却、施錠した扉の解錠なしの開扉、無限定の「二度と」の達成、説明されない能力制約の解除を追加検出した。省略されたlocative対象と末尾の具体的動作もproxyとして使用した。

開発例の弱例9を除いた一方、正しい例も4除いた。魔法の花の贈り物や悲しい結果など、意味が通る話にも動作proxyによる誤除外があり、これは結果から消していない。関連5testsで意図変更/物の回収/解錠/決意と達成の区別、正しい魔法と失敗を確認した。算術/大小・全暗黙参照・語義や世界知識を判定する能力はこのルールからは得られない。

このselectorとbuilderはlocal commit `3273e77`で固定し、その後に新poolと受け入れsampleを作った。旧結果63・旧80原文/理由・旧selector/builder/readyを変更していない。開発32を受け入れ評価へ使っていない。

## 段階2: 同source・同量・全文保持の準備

`shibatch/TinyStories-JA` revision`155b4e5842076c90e07a4934d5b68410fe21f65f`の既存翻訳trainだけを使用。共通base/family holdout/ローカル完全一致除外を引き継ぎ、既知の過去教材と開発32のhash集合152を両条件から除外した。実際の翻訳streamで除外対象127が該当し、498,939全文を選別した。旧SimpleStoriesやdev/test/固定評価生成を学習素材として混ぜていない。

v2適格供給58,421,317tokensから、全文を切らず複製せずに長さ別quotaをそろえた。builder seed202610065/sample seed202610066。各40は同じ文書slotを一度だけ無作為抽出し、全80に原文と具体的理由を保存。軽微な語形誤り・省略と中心的な意味の欠陥を区別し、架空設定・擬人化・失敗や悲しい結末自体は弱例にしない。

残った候補の例は、ドアを開けた対象が箱へ替わる参照の混乱（index16）、物を隠す役と見つける役の切替えが説明されないゲーム（23）、カメを持ち上げる道具が肩になる語義/動作の不自然さ（32）、結びへの未訳語idea混入（36）。こうした対象・役割・語義の全体を局所ルールだけで確認できない。

## 実時間と保存証拠

WSL2/Linux disk、uv Python3.12.7。12CPU workersで既存token streamをdecodeして選別し、再tokenize/新取得/主Web全走査を省いた。開発32抽出0.222122秒、抽出を含むbuilder20.160553秒、新pool証拠照合0.825141秒。Gitの末尾空行checkで新reviewerの整形を修正し、追加0.728438秒で新poolのみ再照合した。selector・教材・seed・内容理由・gateは変更していない。初回review/source/report/completionはLinux runのarchive-before-eof-fixへ保存。実装と個別診断の時間は別、CPU上限1800秒以内。

関連5testsと101準備証拠条件に成功。これは原文・hash・量・分布・source/split・固定sample・全80理由の照合であり、準備gateやモデル品質が成功した意味ではない。各100Mのconfig/runner凍結・実CUDA確認・一次/全文評価は、準備gateが不合格なので行っていない。提案設定を実行証拠にしない。

- [開発32とv1/v2比較](../reports/phase6/condition_v2_calibration_review.json)、[32原文](../reports/phase6/condition_v2_calibration.json)、[個別notes](../reports/phase6/condition_v2_calibration_notes.json)、[5tests](../reports/phase6/condition_v2_selector_tests.xml)。
- [ready/binding](../reports/phase6/condition_v2_ready.json)、[実builder job](../reports/phase6/condition_v2_prepare_job.json)、[全80原文・内容理由・準備gate](../reports/phase6/condition_v2_data_review.json)、[authored notes](../reports/phase6/condition_v2_source_notes.json)。
- [採否](../reports/phase6/condition_v2_judgment.json)、[要求別完了と元UI実確認](../reports/phase6/condition_v2_completion.json)。

Linux教材は`/home/aihub_ubuntu/jmicro-data/phase6/condition-v2-20261005/`、実行証拠は`reports/phase6/condition-v2-100m-20261005/`。両shards/index/manifest/sample、開発例、凍結selector/builder、ready/job/reviewを保存。Gitには可搬な証拠とコードを保存し、大容量shardsは別途引き継ぐ。名前の100mは学習済みを意味しない。

元final10B UIは今回は停止していない。完了確認でactual PID/boot/start_ticksとHTTP親SHA410f975d…/10,000,007,168tokens/busy=falseを照合し、その証拠をcompletionへ保存する。verified local commitと同期を終えて停止し、pushしない。

## 次の判断

ルール開発用の数字をモデル品質や新しい教材の改善と取り違えない。現条件では準備が成立しないので、同量100Mの仮説は未検証。教材増量の無効性・学習飽和・10Mの容量限界も未確定のままである。

次回案は、個別に意味を確認できる小さなwhole-doc教材で「条件保持を学ぶか」を切り分ける実験を設計すること。準備量と反復回数を独立に記録し、同source/文長/EOS・同量学習の対照を作り、未確認評価で測る。20M準備条件とは別の実験契約が必要で、今回のgateを後から書き換えて採用しない。その設計・教材・新GPUは今回開始しない。

Base/Chat未達、独立人手blind/主Web全件監査/保護test未実施、原品質目標と採用条件を保持。500M/1B延長・20B/50B/Chat/test/公開は対象外。
