# 現在の状態

2026-10-17 11:38 UTC途中観測: 同resource-v2 process488265が対照C0の50万教師に到達。25万/50万の全20応答を実履歴・strict32 raw validatorで点検し、内容成立0/10→1/10。挨拶は自然になったが、訂正・多対象・話者区別・復唱は未解決。途中の有利な点へ終了点や採点を変更せず、元100万と新候補の全比較を維持する。新goal active、両腕完了・全2,628内容・実UI会話は未達。

2026-10-17 11:32 UTC更新: [回答教材SFT155](155_answer_curriculum_execution_status.md)を実行中。resource-v2 config e9172f65、実WSL488265/start87977686/同boot・Windows19704。全40技術更新と全state保存再開に合格し、対照C0本学習は102更新53,152教師を観測。次は同processのC0→C1→全2,628応答生成を観測し、全内容比較・新UI会話へ進む。時間計画は[154](154_curriculum_resource_replan.md)で元自己設定3600から各7200秒へ本学習前に明示訂正し、旧failed条件・全費用・欠けた原timingも保全。新goalはactive、4/5未完了。以下の「準備中/未起動」は以前の経過。

2026-10-17新goal: [計画151](151_answer_learning_execution_plan.md)の5までを実行中。1〜3の参考比較・教材監査・少数学習診断は完了し、4/5は未完了。[診断152](152_answer_learning_diagnosis_results.md)ではTRAIN32件の教師本文を全件再現したが、未知入力の改善は未確認。Dolly/Ayaを各120件内容点検し、完全32教師以内の確認済み31/50件と、根拠付き著作TRAIN2,048件を準備した。[比較153](153_answer_curriculum_comparison.md)の同元Base・新対照/候補各1M教師へ向け、明示alias反復の配合と全消費をCPUで計測中。今回の主SFT・新DEV80・全2,628応答・新UI会話は未実施。以下の旧計画149の完了は新goalの完了ではない。

2026-10-17確定: [計画149](149_chat_sft_next_plan.md)の教材準備→条件固定→SFT→全比較→実会話の5段階を完了した。[結果150](150_chat_natural_sft_results.md) / [全要件の完了監査](../reports/phase7/chat-natural-sft-20261017/completion.json)。両腕100万教師・各1,921更新、全2,190内容判定、7点NLL、途中40応答、UI各5会話10応答の証拠を保存した。

候補は改善未実証・正式品質未達で不採用。新DEV内容5→5/80・自己生成文脈0→0/24、内容差95%CIは−5〜+5百分点。汎化の内容と元Chatの文脈などに退行も残る。固定条件を閉じ、同runの延長や有利な途中点への選び直しは行わない。正式Base・独立全pipeline・全文DEV/440・新TEST・採用は別課題として未達のまま。

[候補7862](http://127.0.0.1:7862) / [対照7863](http://127.0.0.1:7863)。Chat既定32token、16/32/64選択。元Base7860と旧Chat7861も生存を確認。科学WSL468008/Windows31644は終了し、元Base470198/start86442058/同boot・idle HTTP・実kernel FLOCK/dxgを再確認した。[復帰観測](../reports/phase7/chat-natural-sft-20261017/restoration_observation.json)。新run所有stage wall2,487.419184秒、元UI1token診断wall0.4761091秒は別記。全stateはWSL、小raw/notes/sourceはWindows Gitへ保存する。

次の候補仮説は直接回答・実履歴参照・訂正の教師不足。許可TRAIN内の能力分布を調べ、量・品質・対照・有限予算を定めてから別比較を準備する。新学習は未起動。今回の5段階完了は正式品質の採用宣言ではない。

## 以下は過去時点の経過記録

ここから下の「最新・現在・実行中・未達」は記載時点の履歴。現在のSFT試行の完了と採否は上記および結果150を参照する。

最新: SFT対照C0と候補C1は各100万教師・1,921更新まで完了し、両腕の全学習state/全履歴の照合も合格。候補[7862](http://127.0.0.1:7862)、対照[7863](http://127.0.0.1:7863)をCPUで実起動し各10応答を保存・内容確認した。既定32token、16/32/64選択。名前に答えた成功もあるが復唱や訂正失敗は残り、品質改善・採用は未確定。GPU pipeline同468008が2,190応答の評価生成中。全内容確認はC0/newの219応答だけ完了（内容5/80、own文脈0/24）で、残り9suiteが未完了。全5段階goalはactive。原Base UIは評価終了時に復帰させる。

2026-10-17 SFT実行: ユーザーの「5まで進めてください」で[計画149](149_chat_sft_next_plan.md)の教材準備からChat実動作まで再開。短い応答の指示を受け、UI既定32token・16/32/64選択を反映済み。公開TRAINを取得・計測し、300件の個別内容確認と除外、両腕の100万教師CPU全消費、TRAIN/新DEV80＋既知4suiteの固定、6 CPU checksが完了。新しい専用CUDA gateを起動した。科学学習・2,190応答の全内容比較・新候補の実会話はこれからで、全5段階goalはactive/未達。

進捗追記: CUDA gateは24技術更新・最大32x1024逆伝播・両腕の全state保存再開に合格。frozen configはec0b61b2、専用pipeline WSL468008/start86194546/同boot・Windows31644がC0→C1→2190 rawを実行中。06:41:53ZにC0=1200更新/624,982教師まで確認。途中25万/50万のNLLと各10応答も保存・内容確認したが、復唱や条件の誤りが残る。主比較は最終100万点を維持。NVML一覧が空のため学習前に止まった最初の起動記録を保全し、別の実process/dxg/HTTP/FLOCK/空きVRAM確認で同じ科学契約の学習を開始した。全5段階はactive/未達、新候補UIは準備段階。

更新: 2026-10-17 JST。文書目標は645b3d09で完了。ユーザーがチャットSFT・動作確認へ方針を変更したため、最初のRealPersonaChat SFT済みモデルをローカルChat画面へ接続した。事前学習とSFT学習の完了、正式品質の採用未達、実際の短い会話成立を区別する。

## 現在試せるChat

[http://127.0.0.1:7861](http://127.0.0.1:7861)。元10B親からRealPersonaChatを3周、1,899,555 Assistant教師tokensでSFTしたepoch3をCPU FP32/greedyで利用する。今回の新学習/GPU利用は0。元Base UI7860はそのまま利用可能。

5会話10応答を全件確認し、EOT終了10/10・有効UTF8 10/10・履歴削除0。挨拶/食べ物の質問に短く返答する一方、入力の復唱や猫の名前を忘れる失敗が残った。[raw](../reports/phase7/chat-demo-20261017/raw.json)・[全個別notes](../reports/phase7/chat-demo-20261017/notes.json)。これは既存モデルの新しい操作確認で、旧DEV80採点の再評価・救済でも新しいblind TESTでもない。

[次のSFT計画149](149_chat_sft_next_plan.md) / [Baseの残課題145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。今回のチャット動作確認は、新しいユーザー指示に基づく。

## 完了した検証

- 第一回RDrop科学比較：元10B親/fresh Adam、同25M教師、4,420更新。全型付き状態・全履歴・元主streamを照合済み。
- 全80件の個別内容確認と原採否判定。paired一貫性差+2/80、CI95[0,.0625]、BPB3.5507%悪化で不採用。
- DEV入力の隔離と全文DEV/440 CPU接続部品。後者36 checksは合成fixtureの検証で実品質ではない。

## 未達事項

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

## 実行状態と保存

RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。

最新完了commitはcf113068。checkpoint-00004420.ptの全stateはWSLのreports/phase6/rdrop-science-20261016/、小raw/notes/receiptはGitに保全。累積台帳は技術169.2456279549515＋科学4241.304908989929＝4410.55053694488秒。これは当該継承台帳の範囲であり、プロジェクトの全歴史GPU時間の総計ではない。

## 現在の目標と次の行動

元「4まで」は未達のまま解除済み。文書目標は645b3d09で完了。現在はユーザーの指示に沿い、Baseの正式合格を待たずにチャットの実動作を確認している。同じ閉じたSFTの再学習は行わず、既存の学習済み成果物を試せる形にした。必要な次のChat学習を定義する場合は、既存SFT結果と実会話の失敗を根拠に新しい契約を作る。Baseの正式完成までの不足は計画145に保全する。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="ui保存先履歴"></a>
<a id="前回chatの完了結果"></a>
<a id="完了したことと未確認"></a>
<a id="次の判断と停止境界"></a>
