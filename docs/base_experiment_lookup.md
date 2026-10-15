# Baseの実験結果を探す

2026-10-15別[author tiled実装readiness](../reports/phase6/forgetting-attention-fused-preparation-20261015/CPU_readiness.json):CPU26/24/22と実親FP32cache合格。閉鎖MATH sourceを変更せず、新model/cache/trainer/owned configを明示。原kernel/config保持・layoutだけtranspose・license全文/NOTICE保存、依存変更0。CUDA値/全勾配/48x1024/両armresume/cache/timingはこれからで、既消費1.244660秒を元180/4800へ継承する。新科学/GPU0の準備記録、Base未完成。

2026-10-15最新閉鎖: [key-bias MATH owned capacity](../reports/phase6/forgetting-attention-key-bias-probe-20261015/completion.json)は48x1024 CUDA OOM、GPU1.244660秒、Adam/TRAIN stream更新0。科学品質の不採用とは区別し、GPU resume/cache/32timing未実施を保持する。元referenceはCPU精度未達、key-biasはCPU精度合格だが容量未達。元technical180/総4800を全額継承し閉鎖source/形状/backend/allocator/予算を救済しない。次の[fused source assessment](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/fused_kernel_assessment.json)は一次調査のみで、導入/追加GPU/品質証拠0。

2026-10-15別runtime [key-bias CPU readiness](../reports/phase6/forgetting-attention-key-bias-preparation-20261015/CPU_readiness.json): softmax行定数を省く同数式、元precision/backend/初期gate/10M/品質を維持。17/23/16 checksと実親cache gate passed、旧runtime cache/state移行拒否。元referenceとのbitwise更新同値ではなく数式同値と元精度合格。次はowned180秒のcapacity FIRST48x1024、両arm実測総4800内資格。新科学/GPU0の準備記録、旧reference失敗は保存。

2026-10-15[実親CPU cache層別localization](../reports/phase6/forgetting-attention-preparation-20261015/CPU_cache_layer_localization.json)完了。native最終差1.4305115e-5は元基準内、forgetting reference0.0001010895は未達。初回非exact箇所は双方共通で、数値差の原因や品質の根因を確定していない。同診断を再実行せず、閉鎖referenceを保持し、次は同数式の別安定実装の価値を検討する。

2026-10-15CPU reference閉鎖: [forgetting attention](../reports/phase6/forgetting-attention-preparation-20261015/CPU_model_trainer_closeout.json)は実count10,014,516・model14/trainer19 passedだが、実親full/chunk精度0.0001010895で元許容差を満たさず科学/GPU0。品質不採用の実験と区別する。initial gate.5の両arm関数はexactだがnativeとは異なる。失敗audit source/hash/diagnostic logを保全し、閾値を緩めず同technical spanで数値差の局在化が次。数学7checksやmodel/trainer未実装は下の履歴。

2026-10-15CPU数学のみ: [forgetting-attention](../reports/phase6/forgetting-attention-preparation-20261015/proposal.json)はpre-softmax累積gate減衰の[7 checks](../reports/phase6/forgetting-attention-preparation-20261015/CPU_math.json)まで。actual model/cache/trainer/count/初期対照設計/GPU品質なし。旧post-SDPA gateは出力scalar、旧QKVはprojected featureのlagで作用位置が異なる。次案の成功や新規性の網羅証明ではない。旧next-two原proposal/config/completionとrecurrent novelty reviewは既閉鎖と再確認し、head/horizon/visit順序の救済を除外した。

2026-10-15最新閉鎖: [causal-QKV contiguous100M](../reports/phase6/causal-qkv-contiguous-science-20261015/completion.json)は全state/history・原CE対照＋宣言13,312lag座標差・全80個別notesまで確認し不採用。native10,001,152対候補10,014,464、文法61/80、一貫性1/80、完結1/80、EOS21/80、反復47/80、BPB0.998450。技術の数値一致・速度改善と文章品質を混同しない。固定lag/tap/層subset/activation/親/seed/decoder/予算を閉鎖し救済せず、次案は原proposal/trainer/resultと照合する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と全4項目goalはactive/未達。以下は当時の履歴。

2026-10-15進行: [causal-QKV contiguous science](../configs/phase6/causal_qkv_contiguous_science_20261015.json)は元referenceを保存し、新しい実装比較で同保存点からの全state/更新/history・保存済みreference0/3/38と32metrics exactを実GPU確認した後に起動。技術累計34.850105秒を元180/総4800へ継承、科学予測4291秒で同元親/原CE100M/48/42・候補10,014,464・元quality gates維持。実PID58473/start66504429、全80採否前。数式や教師/精度/予算を変える救済ではなく専用runtimeをkind/spec/lineageへ明示。reference/new両probeは閉鎖・再実行せず、同science終端を観測。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goal未達。

2026-10-15技術のみ: [causal-QKV reference](../reports/phase6/causal-qkv-probe-20261015/completion.json)は前2tokenの各projected Q/K/Vを13,312零座標で加える別機構。元SwiGLUを保持しclosed squared-ReLU/first-V/cross-map/context-token-mixingの救済ではない。層数/FFN再配分は原architecture_comparisonで既に学習済みと確認し再提案しなかった。referenceは技術合格だが科学予測8581>総4800で科学0・予算未達閉鎖。別contiguous実装は[CPU11 exact checks](../reports/phase6/causal-qkv-contiguous-preparation-20261015/CPU_equivalence.json)までで、GPU同値性・速度・品質未確認。元referenceを上書き/再launchせず、次の別CUDA gateも既消費19.769017秒を元technical180/総4800へ継承する。4項目goalの最終品質は未達。

2026-10-15最新閉鎖: [first-layer value residual100M](../reports/phase6/value-residual-science-20261015/completion.json)は元CE全stream/base config＋宣言12scalarの層間V0経路差・全state/history・全80個別notesまで確認し不採用。native10,001,152対候補10,001,164、文法58/80、一貫性1/80、完結1/80、EOS23/80、反復47/80、BPB0.998524。論文の一般的な全variantや10M規模の限界の結論に広げず、今回のV0係数/層subset/normalization/親/seed/decoder/予算を閉鎖し救済しない。次案は索引だけでなく原proposal/trainer/resultで実差分を確認する。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goal未達。以下は当時の履歴。

2026-10-15進行: [first-layer value residual科学契約](../configs/phase6/value_residual_science_20261015.json)を実親CPU parity/model21/trainer12/probe10/科学18 checksとowned GPU9.812882秒後に凍結・起動。元親/原TRAIN100M/48/42・12scalar差の10,001,164、全元quality gates保持。実PID52873/start66148908は途中値、全80内容採否前。完了GPU probeを再実行せず同science終端を観測する。下のCPU準備は当時の記録で品質合格ではない。独立fresh全pipeline/fullDEV/全440/新TEST/採用と4項目goalは未達。

2026-10-15次案: [first-layer value residual](../reports/phase6/value-residual-preparation-20261015/proposal.json)は現在層Vへ最初の層Vを零初期化scalarで加え、元mapで読む独自variant。cross-GQA map差引き、query-headwise出力gate、attentionとMLPのparallel residualの原source/resultとは変更する経路が異なる。旧index query valueは0件だが網羅性の証明にはしない。一次論文Eq5/Table4と原closed sourceを確認、先行proposal後に18＋1 CPU checksまで。実元親/trainer/GPU/品質未確認で未採用。完了CPU assayは再実行せず、全4項目goalを準備へ縮めない。

2026-10-15最新閉鎖: [cross-GQA signed-map100M](../reports/phase6/cross-gqa-map-science-20261015/completion.json)は元CE全stream/base config＋宣言した52scalar構造差・全state/history・全80個別notesまで確認し不採用。元native10,001,152対候補10,001,204、文法60/80でも一貫性2/80・完結2/80・EOS18/80・反復47/80で元gate未達。旧query-headwise output gateとは別機構だが今回の固定map/係数/normalization/親/seed/decoder/予算は閉鎖し救済しない。次案は索引だけでなく原proposal/trainer/resultで既存条件との実差分を確認する。独立fresh全pipeline/fullDEV/全440/新封印TEST/採用と4項目goalは未達。以下は当時の履歴。

2026-10-15最新閉鎖: [sentence-copy確率減衰100M](../reports/phase6/pseudo-repetition-science-20261015/completion.json)は全17,698更新/全state/対照一致・全80内容reviewまで完了し不採用。原rollout4gram ULとは正のdetach確率目標と合成全句copy入力が異なるが、今回の固定variantは反復31/80・一貫性2/80・適切完結3/80で未達。係数/decay/copy/文境界/親/seed/decoder/予算を変更して再試行しない。前のcontext likelihood/FIMも閉鎖のまま。索引の語句検索だけで新規性を判断せず、原proposal/trainer/resultsと照合して別案を1件選定する。4項目goalの独立学習/fullDEV/新TEST/採用はまだ未達。

2026-10-15追補: 最新の閉じた条件は[context likelihood100M](../reports/phase6/context-likelihood-science-20261015/completion.json)。全80 raw-bound notes・数値監査を含め不採用で、独立学習/fullDEV/新TEST/採用の資格なし。直前のfresh FIMも[不採用閉鎖](../reports/phase6/base-fim-pilot-20261015/completion.json)。どちらも固定条件の係数/親/seed/予算/decoder救済をしない。20261008索引はこの後続比較を含まない検索補助であり、原proposal/trainer/resultとの照合が必要。4項目Base goalはactiveで次の別介入を選定する。以下は文書限定だった時点の履歴。

更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。

[最新Base結果144](144_base_document_balance_results.md) / [前回Chat結果141](141_chat_lr_comparison_results.md) / [次の計画145](145_post_rejection_next_plan.md) / [今回更新146](146_documentation_followup.md)。

Baseの最新固定不採用は143/144、前回teacher-decayは123。後続Chat136/138/141も不採用。20261008索引は当時の検索補助で、144や後続Chatまでの網羅的な現行監査ではない。今回は索引生成・全corpus scan・旧GPU再評価を実行しない。次案は原proposal/trainer/結果を対応付け、検索語がないことだけで未検証と断定しない。

最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。

元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。

次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。

## 当時の資料・保存手順

現在の実状態は `autonomous_status.md` の先頭と、対象jobの実PID/boot/startを確認する。旧計画の「次は…」を、新しい実行指示と解釈しない。

過去の条件を再提案する前に、WSL native repoで `uv run --frozen --extra hub --extra data --extra ml --extra export scripts/index_base_experiments.py --query キーワード` を実行する。例: `larger_material`、`initialization`、`wikipedia`。日時付き索引 `reports/phase6/base_experiment_index_20261008.json` は小さいproposal/completion/review/active_job報告のパス、原SHA、status、閉鎖等のフラグ、要約だけを保存する。

索引は観測時点の検索補助。報告に欠ける量やstatusは推測せず、rawや1MiBを超える報告・全corpus・重みは読み込まない。省略対象はskippedへ列挙する。実行判断時には原報告を参照し、更新済みファイルや稼働中processを再確認する。採点、品質条件、過去の不採用を変更しない。

2026-10-08の参照例: `larger_material_v3_completion.json` はWeb95/story5の500M対2B準備が固定64中11弱>上限10で不採用。`base_gradient_accumulation_pilot_completion.json` は同94.16M教師の勾配蓄積比較が不採用。その後の初期化比較とteacher-decay比較も終了した。最新は結果123の累積2B teacher-decay不採用・一時停止で、次回計画は124。古い索引を最新結果の網羅的な証拠と扱わない。

生成済み索引は同名で上書きしない。新たな結果を集約する場合は日時の異なる後続索引を作り、原報告を保存する。Baseの品質・独立学習seed・fullDEV・protectedTEST・採用が揃うまで未完成。Chat/SFT/量子化はユーザーが再開するまで進めない。
