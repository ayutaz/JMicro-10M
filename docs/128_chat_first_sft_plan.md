# 現在のBaseを直接SFTして会話を検証する計画

後続の実施状況: ユーザーの「5まで進めてください」で明示再開し、2026-10-10に最大3周の1条件、学習前後の全876内容確認、paired比較、結果記録を完了した。全候補がDEV screen不合格のため条件付きsampling/保持/手動5会話は省略し、報告で停止。[実行・結果129](129_chat_first_sft_execution.md)。以下の「今回は計画まで」「未実装」「学習0」は作成時点の記録であり、現在の状態ではない。

作成: 2026-10-10 JST。ユーザーの「まず現在のモデルをチャットデータで学習し、動作確認する」という方針と、その計画作成依頼に基づく。**今回は計画の文書化まで。実装・データ準備・GPU診断・学習・新しい推論評価は開始していない。**

先に現在の重みから小規模なChat候補を作り、学習前後を同じ会話で比較する。その結果から、Baseを作り直す必要性と次に直す箇所を判断する。Baseの完成を待ってからChatへ進む従来順序に対する、限定した診断実験の計画である。未採用Baseを採用済みに変更せず、この実験の成功もBase完成とは扱わない。

[調査127](127_rebuild_investigation.md)、[現在の状態](autonomous_status.md)、[元の品質目標](01_project_goal.md)、[評価契約](evaluation_protocol.md)を前提とする。Base復旧が必要と判断した後の計画は[124](124_base_recovery_plan.md)に残す。参考Akebonoの重み・構成・Tokenizerは移植しない。

## 1. 今回答える問い

現在のモデルに不足している会話形式と「ユーザーの発話に応じ、Assistantとして返答して終える」学習を追加したとき、未知の会話で関連性・文脈・停止が改善するか。

比較は **元10B Base → 同じ重みから直接SFTしたChat候補** の1条件に固定する。Dialogue mid-training、別Base系列、別教材、LR探索、構成変更を同時に加えない。停止だけの改善と、内容を伴う会話の改善を分ける。SFTが失敗しても、Baseだけが原因、10Mの容量限界、SFT全般が無効とは断定しない。

## 2. 親モデルと保全

「現在のモデル」は、引継ぎに記録された元WebUIの **web-10b系列** を指す。最新teacher-decay2Bや、比較的文章品質が良かったstaged-10p6bへ自動で置き換えない。

| 固定する項目 | 計画値・根拠 |
|---|---|
| 親checkpoint | WSL repoの `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt` |
| 親SHA256 | `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`。保存版126・引継ぎの記録 |
| 学習可能parameter数 | 10,001,152。全parameterをSFTする。モデルの大型化・LoRA追加は含めない |
| Tokenizer | 既存4096語彙、SHA256 `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318` |
| context | 1024。特殊tokenの意味・番号を維持 |
| frozen model.py | SHA256 `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83` |
| 出力先 | 新しい `reports/phase7/chat-first-sft-<実行日>/`。元runを上書きしない |
| 採用状態 | `Base_adopted=false`、`Chat_adopted=false`、`purpose=chat_first_diagnostic` を記録 |

親のhash・schema・実装一致は、実行再開後のpreflightで確認する。ここに記載したpath/hashは過去の保存記録であり、今回のWSL上の所在・稼働確認ではない。親が一致しなければ開始せず、別checkpointへの無断差し替えやmetadata偽装をしない。

BaseのAdam・schedulerを継続せず、**重みだけを引き継ぎ、新しいSFT optimizerとseedを使う**。Baseの既学習量と新しいSFT量を別々に保存する。親ファイルを変更する必要はない。元UIを保持し、GPU実験中に必要ならidle確認後に停止、実験の終端で元モデルへ戻す。今回はUIを操作しない。

## 3. 最初に使う会話教材

既存の [Chat pilot準備記録](../reports/phase7/chat_pilot_preparation.json) と [4会話の内容確認](../reports/phase7/chat_pilot_content_notes.json) を再利用する。新しい収集・全corpus再走査・Tokenizer再学習を最初の条件に加えない。

- 元教材: `nu-dialogue/real-persona-chat`、revision `28d0b6b3865b29cabc26c230a2db37cdf315e937`、CC-BY-SA-4.0。既存manifestの帰属・license bucketを保持する。
- 準備先: `/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006`。実行時に存在・manifest・TRAIN hashを確認し、同じ準備済みデータがあればbuilderを再実行しない。
- 全会話/connected familyの既存splitを維持。TRAINだけを学習し、DEV・protectedTEST・固定評価問題を混ぜない。共有話者がsplitをまたぐ可能性や、独立した意味的重複監査の未完了を明記する。
- 話者1をuser、話者2をassistantとして交互に扱う。personaを省略した既存教材をそのまま使用し、不足背景を創作しない。

| 準備済み数量 | TRAIN・1周 | DEV・学習禁止 |
|---|---:|---:|
| 会話数 | 2,688 | 150 |
| Assistant応答/学習window数 | 40,366 | 2,250 |
| Assistant本文+EOTの教師tokens | 633,185 | 35,054 |
| うちEOT教師tokens | 40,366 | 2,250 |
| windowの非PAD直列tokens（履歴を含む） | 10,189,157 | 560,873 |
| モデルへの非PAD入力tokens | 10,148,791 | 558,623 |
| context1024固定paddingを含むwindow容量 | 41,334,784 | 2,304,000 |

この数量は**準備記録**であり、実学習はまだ0。教師tokensはAssistant本文+EOTで、直列tokensは各targetの過去履歴を繰り返して含む。3周の学習は新しい3倍のデータを意味しない。実batch末尾の空行による追加paddingは別に記録する。

教材は人間同士の雑談で、instruction-following、知識の正しさ、AIとしての自己紹介を保証しない。短い相づち、自己経験、誤字、省略背景を含む。したがって最初の実験は自然な短い会話への適応を見る。訂正・否定・制約を扱う元の評価問題も残し、教材にない能力を結果から除外して合格扱いにしない。

## 4. 学習契約と1条件のrecipe

既存 [TokenizerのSFT window](../src/jmicro/tokenizer.py)、[AssistantSampler](../src/jmicro/assistant_sampler.py)、[AssistantTrainer](../src/jmicro/chat_training.py) を再利用する。

各windowで、**現在のAssistant本文と最後のEOTだけ**をloss対象にする。user/system、role token、過去のAssistant、PADは `-100` でmaskする。causal shiftは1回。現在のuser/assistant対と最後のEOTを途中で切らず、必要な場合だけ過去の完全なturnを落とす。今回の準備記録では履歴削除は0。

以下は最初の条件の提案値。GPU実測前に最適値・凍結済みconfigとは呼ばない。実行再開後、manifestと安定batchに結び付けたconfigを凍結してから本学習を始める。DEVを見ながら値を調整しない。

| 項目 | 提案値 |
|---|---|
| 学習route | direct SFT。新しい学習seed42、全parameter更新 |
| 最大量 | TRAIN 3周、**121,098 windows**、**1,899,555 Assistant教師tokens**、**30,567,471直列tokens** |
| optimizer | fresh AdamW、betas=(0.9, 0.95)、weight decay=0.01。bias/norm等の既存非decay群を維持 |
| peak LR | `1e-4`。小規模fine-tuningの初回設計値であり、最適性は未実証 |
| scheduler | 既存SFTのWSD: 更新数の冒頭5%をwarmup（最低1 update）、直列tokensの最後10%をcosine decay、最終LR `1e-5` |
| 精度/attention | CUDA/BF16、masked document、math backend、training_fast_path=false、accumulation=1 |
| batch | masked SFTで教師tokens/秒とfinite forward/backwardを実測して選ぶ。Baseの速度・batchを転用しない |
| clipping | gradient norm 1.0。finite loss/gradient/stateを確認 |
| 保存 | 250更新または5分の早い方、1周/2周到達後の最初の完了更新、3周終端、停止時 |

最大量の算術は `40,366×3=121,098`、`633,185×3=1,899,555`、`10,189,157×3=30,567,471`。最終EOT数は121,098。1周・2周のcheckpointはbatchが周境界をまたぎ得るため、名称だけで正確な1/2周と扱わず、実window数・教師量・sampler位置を記録する。最終3周は既存全windowを3回消費する契約を検証する。

単一recipeの途中checkpointを比較する。品質が悪いことを理由に4周目へ延長したり、別LR・別seed・別教材を続けて試したりしない。技術gateや予算で途中停止した場合は実消費量を残し、3周完了とは書かない。

## 5. 未実装の入口と、実行前に通すgate

既存 [run_chat_sft.py](../scripts/run_chat_sft.py) は `require_adopted_base` を必須とし、直列予算を10M/30M/100Mに限定する。既存batch probe・stage評価・保持評価にも採用済みBaseを前提とした結び付けがある。**そのまま今回の未採用Baseを渡しても実行できない。既存採用gateは変更しない。**

実行再開後に、診断目的を明示した以下の入口を新設する。以下の名前は予定で、今回作成した実行可能commandではない。

| 予定成果物 | 必要な責務 |
|---|---|
| `configs/phase7/chat_first_sft.json` | 親/Tokenizer/TRAIN/DEV/suite/source hash、量、recipe、時間上限、採点・選定規則を凍結 |
| `scripts/run_chat_first_sft.py` と `.ps1` | 未採用親を明示的に許す専用preflight、TRAIN限定、fresh optimizer、manifest由来3周予算、永続job/ledger、保存再開、終端後の停止 |
| `scripts/probe_chat_first_batch.py` | 診断親に結び付けたmasked CUDA batch証拠。probe重みは本学習へ流用しない |
| `scripts/evaluate_chat_first_sft.py` | 読み取り専用BaseとSFT checkpointを同じChat contractで評価。greedy、role control、自生成履歴、sampling、raw保存、途中再開 |
| `scripts/review_chat_first_sft.py` | 全出力に結び付いた内容採点、既存DEV screen、paired差、保持、未完了項目をまとめる。採用済みの偽証を作らない |
| 診断用Base保持adapter | 正しいweb-10b対照と同一の既存DEV/生成条件に結び付ける。別系列の結果を親対照に使わない |

中核モデル・Tokenizer・旧学習sourceを上書きせず、既存trainer/evaluatorを呼ぶadapterを優先する。親schemaが互換でない場合は互換性を先に調べ、旧checkpointの実装hashを書き換えて通さない。

実行順序は次のとおり。

1. 親、Tokenizer、既存manifest、split、source hash、特殊tokenとmask、3周算術、出力の隔離をCPUで確認する。変更に必要な検証だけを行う。
2. 実PID/boot/start・GPU lock・job・UI busyを確認。重複jobを防ぎ、必要なら元UIを一時停止する。
3. masked CUDA/BF16の有限forward/backwardと安定batchを確認し、batchに結び付いた最終configを凍結する。
4. CUDAで連続4更新と2更新→全state保存→再開2更新を比較。model/optimizer/scheduler/RNG/sampler/counters/消費列/履歴を同じ凍結条件で一致させる。gate用stateを本学習へ引き継がない。
5. 未学習BaseをChat形式で評価する。既存結果が同じ親hash・suite・dtype・decoding・history契約に完全一致するときだけ再利用し、それ以外は今回のmatched対照を作る。
6. 元親からfresh SFTを開始し、1周・2周到達checkpointと3周終端を保存する。学習を完了してからcheckpoint群を評価し、DEVを見て途中recipeを変えない。
7. 全内容を確認し、選定候補のsamplingとBase保持を確認する。結果・未達・次案を記録して停止する。

動作確認では、選定候補が得られた場合にローカルの診断用対話入口でも、挨拶・話題継続・訂正・否定・条件付き応答の5会話を最大4ターンずつ試す。CLI等の入口が足りなければ先に実装し、同じ特殊token/履歴/停止policyとraw logを使う。これは評価予算内の最大20追加応答で、固定DEVの合格件数へ足さず、主観的な手触りを採用の代用にしない。元Base UIの既定モデルは維持する。

必要なtestsは、新入口のsplit混入拒否/未採用lineage、maskと1回shift、完全EOT、3周境界、checkpoint選定、全state再開、予算/重複job停止を中心にする。既存CPU testsは実CUDA学習や品質の証拠にしない。全PythonはWSLの `uv run --frozen --extra hub --extra data --extra ml --extra export ...`、Python3.12.7で実行する。未実装のscriptを実行手順として提示しない。

## 6. 動作確認と内容評価

「ロードできる」「lossが下がる」「EOTで止まる」「会話が成立する」を別々に判定する。既存 [Chat評価](../src/jmicro/chat_evaluation.py) と [内容review](../src/jmicro/chat_review.py) の契約を維持する。

### 同じ問題で学習前後を比べる

Baseと3つのSFT checkpointを、同じDEV80、context1024、greedy、max_new_tokens64、同じBF16/mathで評価する。EOT7/EOS3を停止tokenとし、標準条件の特殊token抑制と無抑制の対照を両方残す。反復penaltyや強制改行・強制EOTは追加しない。

1モデルあたり、標準80応答、無抑制80応答、24会話familyの自生成履歴による59応答、合計219応答。4モデルで876応答。24会話は2〜4ターンで、モデル自身の返答本文を次の履歴へ戻す。既存実装はtext clientと同様にdecoded bodyを再encodeし、元token IDs/raw bytes/Unicode失敗は別に保持する。この方式をraw IDsのまま履歴へ戻す方式と混同しない。

全219応答について文法・関連性・必要な文脈を0/1/2で採点し、失敗の具体的な理由を残す。後半の成功で前半の破綻を隠さず、各会話の全turnを読む。Codex非blind採点を独立した人間blind評価と呼ばない。新しい独立DEVの獲得や未完了corpus監査は今回完了扱いにしない。

| 既存DEV screenの項目 | 維持する条件 |
|---|---|
| 内容 | 標準80の文法2かつ関連性2が56/80以上（70%） |
| 会話文脈 | 自生成履歴24familyの最終応答で文脈2が15/24以上（60%以上） |
| 自然な停止 | 標準80で76/80以上、全自生成59応答で57/59以上。EOT/EOSと上限打切りを分ける |
| 空返答 | 5%以下（標準80では4件以下、自生成59では2件以下） |
| role漏れ | 1%以下（80/59件それぞれ0件） |
| Unicode失敗 | rawで0。表示上の置換・無視で成功にしない |
| 履歴 | 固定評価では全文履歴保持。収まらない例を黙って切り捨てない |

反復件数・token/char n-gram・同文再出現、EOT/EOS内訳、無抑制での漏れ、category別成績も報告する。既存Chat screenには反復の独立した数値gateがないため、勝手に既存gateとして追加・削除したと書かない。反復が対照より増える候補は次段階へ推奨せず、停止と内容のどちらが改善したかを示す。

### checkpoint選定とsampling

選定規則は事前固定する。既存DEV screenを通ったcheckpointの中から、標準80の文法・関連性同時2の件数、24familyの文脈2件数、反復の少なさの順で選び、同率なら早いcheckpointとする。screen合格がなければ採用候補はなし。診断用に最良例を提示するときも不合格を明記する。

選定候補がある場合、Baseと候補にtemperature0.8/top_p0.9/top_k50、生成seed42/43/44を適用し、同じ219応答を各seedで比較する（追加1,314応答）。最良seedだけを示さず、全seed/全turnを読む。生成seedを変えた評価は独立した学習seedではない。family単位のpaired差・95%CIを報告し、同じfamilyをseedごとに独立した新問題として数えない。DEVでcheckpointを選んだ比較は探索的で、CIだけで最終採用や再現性を証明しない。

### Base能力の保持

採用候補とweb-10b親を、同じ既存DEV256の共通byte BPBと固定Base DEV80生成で比較する。親の保存済み結果はcheckpoint/suite/data/実装/decoding一致が確認できる場合に再利用する。別の2B/staged対照や、Chat promptでの結果をBase保持へ代用しない。

診断の保持guardはBPBの相対悪化5%以内、Base文法2の件数を減らさず、反復・空返答・role漏れ・Unicode失敗を増やさないこととする。これは本実験で新しく提案するguardで、元のBase採用基準の置き換えではない。untagged Base生成ではEOTを旧policyどおり別扱いにする。DEV256はfullDEVではなく、保持guard通過もBase完成ではない。保持に失敗した候補はChat改善があってもそのまま推奨しない。

protectedTESTは今回使用しない。独立学習seed、人間blind/採点者一致、fullDEV、最終TESTは後続の品質確認として残す。

## 7. 時間上限と停止

初回は **本学習を最大3周、全実験の累積GPU時間を最大6時間** とする。区分ごとの時間上限に先に達した場合は、その時点で停止する。6時間は速度予測ではなく資源の上限案。実測前に完了時刻を約束しない。学習だけでなくprobe・保存再開gate・Base対照・候補評価・sampling・保持をledgerへ足す。

| GPUを使う区分 | 上限案 |
|---|---:|
| masked batch/finite probe | 600秒 |
| CUDA保存再開gate | 600秒 |
| 本SFT | 3,600秒、かつTRAIN最大3周 |
| matched Chat評価・checkpoint群・sampling | 14,400秒 |
| Base保持 | 2,400秒 |
| 合計 | 21,600秒（6時間） |

不要になったsampling/保持は実行せず、不合格報告で終える。実測速度から上限内に必要な評価を完了できないと分かった場合、recipe凍結前に不足を記録する。評価件数や品質gateを減らして合格扱いにせず、追加予算を自動で確保しない。CPU実装・内容review時間はGPU秒とは別に記録する。

NaN/Inf、親/Tokenizer/source/split不一致、resume不一致、重複job、容量不足・hardware/credential blockerで停止する。OOMはprobeで切り分け、本学習を別batchへ黙って変更してresumeしない。中断時は最後の完了更新を全state保存し、同じ凍結条件と残予算内のresumeだけを認める。元weights・旧証拠を保存し、終端後にGPU lock解放と元UI復帰を記録する。

## 8. 結果から次を決める

| 結果 | 結論と次案 |
|---|---|
| 技術gate未達 | 学習・評価入口の問題を修正する段階。Chat能力や10M容量について結論しない |
| EOT/role形式だけ改善、内容や文脈が未達 | 会話形式の学習効果はある。関連性・履歴・教材の対応を失敗例から調べ、教材改善かBase復旧を別条件として計画する |
| DEV内容/文脈/停止と保持が合格し、samplingでも重大破綻なし | 現BaseからChatへ進める候補を得た。次は独立学習seed・人間blind・未使用評価で確認する計画を提示。今回はChat最終採用しない |
| Chatは改善するがBase保持に失敗 | 忘却/目的のtrade-offが未解決。混合やLR等を次案にできるが自動追加実験はしない |
| 本条件で改善なし/悪化 | この教材・recipe・親の組合せを閉じる。小規模SFTの不成功だけで作り直し必須・容量限界と断定せず、127/124に戻して次案を1件に絞る |

まずこの実験の結果と実際の会話例をユーザーへ報告して止める。mid-training、追加epoch、別Base、構成変更、量子化、公開、deploymentを自動的に始めない。後続でWebUIへ候補を追加する場合も、未採用Chat候補であることとraw失敗を表示し、元Baseへ戻せる別のモデル選択として扱う。

## 9. 完了時に残すもの

親/Tokenizer/data/suite/sourceの固定一覧、凍結config、masked batch測定、CUDA resume gate、job/PID/boot/start、GPU ledger/log、1/2/3周到達の全stateと実消費量、学習前後のraw生成と全内容notes、paired差、sampling/保持、未完了事項を保存する。`completion.json` は技術完了・学習量完了・DEV screen・保持・採用を別のfieldにする。

今回の計画作成完了と、将来のChat診断完了と、Base/Chatモデルの品質完成は別である。**現在の実Chat教師tokensは0、Base/Chat未採用、次の実行は明示的な再開待ち。**

計画作成時の静的確認: 更新した8文書のローカルリンク215件、準備manifestに基づく3周のwindow/教師/直列tokensの算術、input+EOT=seriesの計数、GPU時間上限の合計をPowerShellで確認した。frozen model.pyのSHA256は既存値と一致。これは文書の検証で、GPU実行・学習・品質評価の証拠ではない。
