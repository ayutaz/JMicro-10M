# 完結文配合の三条件100M比較

ユーザー指定「3まで進めてください」に基づき、[計画47](47_post_evaluation_training_plan.md)と会話で整理した段階1〜3を完了した（2026-10-05 JST）。段階3は三条件の学習・評価・条件付き全文/長文評価・比較報告まで。新物語配合は正式採用条件を満たさず、Base/Chat品質目標は未達。追加500M〜1B、20B/50B、Chatは開始しない。以下の準備・起動記録は当時の履歴として保持する。

## 段階1: データとEOS処理

WSLの既存trainから固定seedのtoken位置を抽出し、Web100文書と既存短文100単位を保存した。token位置からの抽出なので文書長に偏る標本であり、全corpusの比率を推定しない。Web63/100、短文100/100が句読点等で終わる。両標本に本文special ID混入は0。Webの先頭・末尾と短文の本文をCodexが読み、広告・記事の末尾定型句、途中切断、前文への依存、意味の崩れを確認した。短文S73/S74等には内容の崩れ、S67には説明の予告で終わる例がある。句読点だけで完結性を認定しない。

`BlockSampler`の具体的なBOS/body/EOS例で、EOS教師あり・BOS教師mask・次token shiftの四条件は成功した。現行実装では文章末尾EOSが学習対象から消えている証拠はない。文書をまたぐcausal attentionと、任意block境界からの学習は現行仕様として保持する。これだけで全データのEOS意味や学習された停止能力を保証しない。

保存先: Linux `reports/phase6/complete-text-10b-100m-20261004/data-inspection/{web,short,result}.json`。全12.23Bの再走査・dedupは行っていない。

## 段階2: 完結文候補pool

最終poolの準備と限定内容確認を完了した。SimpleStories-JA trainから25,000,067 input tokens / 276,369物語 / 108,582親family、本文98,735,557 bytes、平均88.459 body tokensを82.876秒で構築した。100例をCodexで確認し、出来事・登場人物・結末が概ね保たれる一方、不自然な語（例19/26/91/98）、弱い展開、未解決の結末（例44）が残ることを記録した。全例が意味的に完結するという認定ではなく、制限を明示した小予算比較用の採用である。[標本確認](../reports/phase6/complete_text_data_review.json)。追加filter/rebuildを繰り返さず、元の品質採用gateによって学習結果を判定する。

Linux保存先は`~/jmicro-data/phase6/simple-stories-ja-20261004/shards`、manifest SHA `b89d692c6cb7580909b3cfa90fb8d277b3dfc606ac458724ccafd5c444d77f8d`。元train parquet二つだけを固定revisionから取得し、LFS SHA256とサイズを照合。38関連CPU tests成功。学習前に専用config/schemaを凍結した。

**学習前のprotocol改訂:** Web候補r2も30,235,206 tokens/636,432単位まで232.351秒で構築したが、無作為100例に意味の崩れ（例2）、前文依存（例3/15/16等）、未説明の予告（例50）を確認した。文字列規則だけで今回の完結文条件を満たすと扱わず、両Web候補を未採用として保存する。公開の[SimpleStories-JA](https://huggingface.co/datasets/SimpleStories/SimpleStories-JA/tree/d25370316dd77ec0ee4fd9db57bfe57075cf4b90)へ切り替える。作者のMIT表記とREADME hash、revision `d25370316dd77ec0ee4fd9db57bfe57075cf4b90`、train parquetのLFS SHA256/サイズを固定。公開済みの合成物語で、有料生成や認証は不要。公式validation/testは取得しない。

この変更後のCは**切り出さない物語全文、2〜8文、32〜128 body tokens**。閉じない文・括弧、前文依存、反復、クリフハンガー/超現実style等を除き、物語末尾を保持する。先頭train1000例の候補322例は平均91.66tokensで、旧32〜64 binsと同一の長さ配合として扱えない。全文の内容と完結を優先し、長さのbin一致を実験条件から外すことを結果を見る前に決めた。**Cはsource・語彙・文体・長さ・EOS密度も変わる配合全体の比較であり、一貫性だけの純粋な因果効果ではない。** B/Cのsourceごとの教師EOS数も報告する。25M〜50M pool、20%配合、同じ学習tokens/モデル/LR/評価/gateは維持する。

生成元の`generation_id`を末尾の物語番号より前でまとめ、family hash1%を補助devへ分離する。完全一致の局所重複と既存固定suiteのexact本文を除外し、補助devとtrainの親familyは分離する。既存Webとの重なり・公開benchmarksへの混入は不明で、完全独立や25M新規uniqueを主張しない。独立人手による全例の意味保証も未実施。新sourceのtoken量と、以前のWebを選別しただけの候補量を分けて記録する。

以下は未採用Web候補の準備条件と証拠を保持したもの。科学Cには上記の物語全文を使用する。

受け入れ済みWeb trainから、連続する2〜6文・32〜64 body tokensの単位を選別する。前文依存の書き出し、広告/誘導表現、説明予告、質問だけの末尾、露骨な反復を除き、文間の話題の共有または関係を示す接続を要求する。途中token切断でEOSを付けない。元記事とは別の単位末尾にEOSを付けることをmanifestへ明記する。

内容の選別は保守的な規則とCodex標本確認による実験用候補であり、全例の事実性・意味品質や独立人手認定を主張しない。原trainを再選別したsubsetで、新規source tokensは0。既存Webの重複・独立全corpus監査未完了は引き継ぐ。protected dev/testは学習へ取り込まず、補助devは既存の保護済みdevを再利用する。

長さの効果を抑えるため、旧短文の32–39/40–47/48–55/56–64 token binsの文書比率を一致させる。bin内部の完全一致ではなく、source・文体・文数も変わる比較である。候補内のexact重複のみ小さく除去し、元の25.9M文書全体の重複照合は繰り返さない。

初回候補は30,230,920 tokens/636,432単位、422,051親文書、12workers/215.570秒。無作為100例に前文依存・説明予告が残ったため、学習前に条件を修正した。初回pool・source・確認結果は保存し、採用済みとはしない。修正版は独立した`coherent-text-10b-20261004-r2`へ構築する。

## 段階3: 比較条件

| 条件 | 配合 | 各枝の追加tokens |
|---|---|---:|
| web | Web100% | 100,007,936 |
| short20 | Web80%＋既存完結短文20% | 100,007,936 |
| coherent20 | Web80%＋新候補完結文20% | 100,007,936 |

同じfinal10B（SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、update305176）のweights/Adam/RNG/Web cursorからforkする。モデル10,001,152 parameters、Tokenizer、context1024/batch32、BF16/Flash/compileを保持。親実LRは約0.000200000019であり、比較は全枝peak0.0002、stable2900＋decay152updates、floor0.00002。新しい学習率方針のforkであり、通常resumeや純粋な総学習量比較とは呼ばない。

科学合計300,023,808 input tokens。短文/新完結文は各19,988,480 tokens。各枝の終端は総10,100,015,104 tokens/update308228となる。枝同士のtokensを一モデルの累積へ足さない。新poolの実CUDA保存再開は8optimizer updates/262,144 input tokensを科学学習と別会計にし、重み・Adam・scheduler・RNG・両sampler等の連続/再開一致を確認する。

一次評価は各dev256本文BPB、固定dev80 greedy64、意味dev192、JBLiMP331対、JCommonsenseQA1,119公式dev。旧v1とv2.1を保持し、quantity助数詞等の既知制限を今回も記録する。評価仕様を結果を見て変更しない。保護testは使用しない。文法・関連性・一貫性・内容完結はモデル名を除いた240packetを単独Codexが採点し、独立人手blindとは呼ばない。

元mixture条件（EOS差8以上、反復対照以下、BPB対照比+1%以内、raw Unicode/empty/role0、句読点だけの停止なし）を保持し、提案済みの内容条件（一貫性2点が対照より8/80以上、paired95%差の下限>0）を追加する。全条件を通る最良候補のみ、必要な対照と条件付き全文dev/400・128/512評価へ進む。通らない場合は未採用と報告し、全文評価を繰り返さない。

GPU一次上限1,800秒、条件付き追加評価上限3,000秒。初回候補作成の実測によりデータ整備は数分規模。checkpoint/log/process identity/source/manifest/configを保存し、途中終了は有効checkpointから再開する。UIは学習中だけ停止して最後に元final10Bで復帰する。

比較の終了と品質合格を分ける。100Mは総10Bの約1%で、結果が弱くても学習量不足を否定しない。三条件の完了・rawと内容評価・結果保存・local commitで停止する。

## 一次比較の実測

三条件の学習・一次評価をGPU774.624秒で完了した。科学300,023,808 tokens、保存再開検証262,144 tokensは別会計。各枝の終端は総10,100,015,104 tokens/update308228。38関連CPU testsと実CUDAの全state/履歴一致、完了証拠35項目は成功した。

| 指標 | Web100% | 既存短文20% | 新物語20% |
|---|---:|---:|---:|
| dev256本文BPB | 0.980484 | 0.982015 | 0.987748 |
| 自然EOS / 80 | 0 | 3 | 24 |
| 反復 / 80 | 60 | 55 | 24 |
| raw Unicode失敗 / 80 | 0 | 0 | 0 |
| Codex文法2点 / 80 | 25 | 32 | 59 |
| Codex関連性2点 / 80 | 26 | 29 | 23 |
| Codex一貫性2点 / 80 | 0 | 1 | 10 |
| Codex適切な内容完結 / 80 | 0 | 1 | 9 |
| 学習中EOS教師数（Web / 配合source） | 211,670 / 0 | 169,362 / 424,017 | 169,362 / 221,003 |

全240出力をモデル名を除いたpacketで単独Codex採点。独立人手blindではない。新物語は一貫性差10/80、prompt paired bootstrap95%差区間[0.0625,0.2]で事前条件を通り、EOS・反復・BPB対照比+1%・raw失敗・句読点停止の一次条件も通った。BPBは対照比約+0.741%、旧全文BPBとdev256は異なる標本なので直接比べない。関連性2点は26→23へ減少し、数量・時刻・局所条件を失う例は残る。24停止のうち内容として適切な完結は9で、EOSだけを品質合格にしない。

事前に定めた条件付き全文/長文評価を新物語とWeb対照だけに行う。専用`evaluate_complete_text_full.py`/`.ps1`とconfig/schemaを凍結し、関連14CPU tests成功。原全文dev89,416/164,344,743 bytes、固定400、同じ20prefixのgreedy128/512を測る。追加学習0、GPU上限3,000秒、元raw条件と親BPB+0.001条件を保持する。一次結果・旧親・旧benchmarksの再学習や評価仕様変更は行わない。

### 日本語Base診断（保存済み一次結果）

| 指標 | Web100% | 既存短文20% | 新物語20% |
|---|---:|---:|---:|
| 基本意味192正答率 | 60.94% | 61.46% | 62.50% |
| 基本意味の両文脈正答 / 96 | 23 | 25 | 26 |
| JBLiMP331 train-sample SLOR正答率 | 74.02% | 76.13% | 75.53% |
| JCommonsenseQA dev1,119正答率 | 32.62% | 29.80% | 34.58% |

追加推論なしで保存した同一問題のcredit差をfamily単位paired bootstrapした。[CPU差の記録](../reports/phase6/complete_text_10b_choice_comparison.json)。新物語の対照差は基本意味+1.563 percentage points（95%区間−1.042〜+4.167）、JBLiMP+1.511（−1.813〜+4.532）、常識+1.966（−0.089〜+4.111）で、いずれも差の区間が0を含む。点推定上昇を理解能力の確実な改善と断定しない。既存短文の常識差は−2.815（−4.246〜−1.385）で退行が見られる。学習seed一つのdev診断であり、未実施の独立人手・test・公開Base参照を代替しない。旧quantity助数詞等の既知制限を保持し、今回の採用gateは変更していない。

### 条件付き評価の読み込み修復

初回conditional process19791は、Web全文本文と固定400の保存後、親の保存結果を`read_json(str)`へ渡す誤りで停止した。旧job/source/config/schema/log/raw結果は`conditional-full`へ保持。保存済みWebのcheckpoint hash・本文/400条件の一致・全raw ID flagsをCPU確認し、再計算せず、明示的な`reused_from`でr1へ引き継ぐ。本文BPB0.948957324851、本文評価389.088秒。失敗時点のGPU831.355秒も元3,000秒予算に含める。

`parent_results`でJSON内のpathをPathへ変換し、同じ処理を実行とCPU reviewerで共用する。実ファイルの文字列pathを読み込む回帰testを追加し、関連15CPU tests成功。科学学習・Tokenizer・scorer・dev・suite・品質gateは変更しない。新しい凍結config/schemaは`complete_text_10b_full_r1`、runは`conditional-full-r1`。Linux37818、hidden Windows33788、2026-10-04 15:01:44Z（日本時間10月5日00:01）起動。Web長文→新物語全文/400・長文へ続け、完了後にreport/local commitとUI復帰で停止する。

## 最終評価と採否

条件付き評価は2026-10-04 15:20:32Z（日本時間10月5日00:20）に完了。全文dev89,416文書 / 164,344,743 bytes / 42,003,934本文tokensを同じcontext1024/stride512で評価した。保存済みWeb全文/400は明示的に再利用し、旧失敗runのGPU831.355秒も元予算へ含めた。追加学習は0、protected testは不使用。

| 指標 | Web100%・総10.1B | 新物語20%・総10.1B |
|---|---:|---:|
| 全文本文BPB | 0.948957 | 0.955765 |
| 固定80自然EOS | 0 | 24 |
| 固定80反復 | 60 | 24 |
| 全400自然EOS | 6 | 137 |
| 全400反復 | 124 | 53 |
| 全400 raw Unicode / role / empty失敗 | 0 / 0 / 0 | 0 / 0 / 0 |

| 長文条件（各20prefix） | Web EOS / 20 | 新物語 EOS / 20 | Web平均char4反復率 | 新物語平均char4反復率 |
|---|---:|---:|---:|---:|
| 最大128tokens | 0 | 10 | 84.40% | 46.48% |
| 最大512tokens | 0 | 10 | 96.15% | 55.13% |

長文のraw UTF8失敗は全条件0。長文の追加内容採点は未実施で、10/20のEOSを意味的に適切な完結とは認定しない。一次240件のCodex診断も独立人手blindではない。

**新物語は正式採用を見送る。** 対照Web比の全文BPB悪化は+0.717%でmixture上限+1%以内、EOS・反復・raw条件も通った。しかし元final10BのBPB0.9540184727984398からは+0.001746218490803253で、既存の増量安全条件「悪化+0.001以内」を超えた。失敗項目を保持し、`candidate_passes_all_full_conditions=false`とした。理解診断の対照差の95%区間は全て0を含み、理解能力の確実な改善も主張しない。Web枝の本文BPB改善も、生成品質合格やUIへの採用とは別である。

停止・反復はデータ配合への反応を示したが、source/語彙/文体/長さ/EOS密度が同時に変わるため、意味品質だけの因果効果ではない。追加100Mは元10Bの約1%で、今回の未採用を学習量不足の否定としない。

## 完了証拠と停止境界

- [一次比較35項目](../reports/phase6/complete_text_10b_comparison_review.json)と[全文・長文43項目](../reports/phase6/complete_text_10b_full_review.json)の保存結果確認が成功。後者はcheckpoint/source/config、全文coverageとNLL、全400 raw ID、長文40件ずつのdecode/停止/反復、旧Web結果の完全再利用、変更していない採用条件を照合した。38関連CPU tests、修復後15 tests、実CUDA全state保存再開は成功済み。
- [最終結果](../reports/phase6/complete_text_10b_full_result.json)。GPU一次774.624秒＋条件付き1,956.804秒＝2,731.428秒（約45分31秒）、元合計上限4,800秒以内。データ準備・実装・内容採点時間は別。科学300,023,808と検証262,144 tokensを分け、各枝100,007,936追加・総10,100,015,104/update308228を保持する。
- Linux科学17951、旧失敗19791、修復37818は終了。raw/checkpoint/source/logは`reports/phase6/complete-text-10b-100m-20261004/`、最終評価は`conditional-full-r1/`、旧`conditional-full/`も保持する。完了jobを再起動しない。
- Web UIは元final10B SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`へ復帰。`http://127.0.0.1:7860/api/model`で総10,000,007,168 tokens / busy=falseを確認した。復帰時LinuxPID49746 / boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe / start_ticks1043870。最新identityは`reports/local/webui/server.json`を正とする。
- [要求別完了・復帰記録](../reports/phase6/complete_text_10b_comparison_completion.json)とlocal commitに保存し、段階1〜3で停止する。500M/1B、20B/50B、Chat、protected test、push/publicationは開始しない。独立人手blind、全12.23B独立監査、新sourceの広域重複・benchmark混入確認は未実施のまま保持する。
