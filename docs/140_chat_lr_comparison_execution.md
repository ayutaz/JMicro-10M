# 低学習率SFT比較・実行履歴

2026-10-14 JST。goal「3まで進めてください」で直前の3項目を再開。[計画139](139_chat_lr_comparison_plan.md)。Base経路の既存不採用を参照し、代替案のpeak LR1e-4→3e-5を1件選定した。元10B親/fresh optimizer、native10,001,152、同TRAIN/Tokenizer/seed42/B1,899,555教師/schedule/固定paddingを維持する。LRとともに累積decoupled decayも変わることを交絡として記録した。

## 準備と凍結

accepted TRAIN41,529 targetと280sample QA最終誤り0をhash付き再利用。新教材/QAは0。元TRAIN凍結後の新DEV80/実履歴24会話59turnを独立記述し、既知3suiteも回帰へ残した。新DEVのTRAIN質問完全一致・登録Jaccard8・文字/mask/roundtrip異常0。独立人間や広い意味での独立性を保証するものではない。

固定NLLは以前の2,554targetを窓/ID/本文/EOT/bytes不変で保存し、新DEV80を追加した2,634target。TRAIN112とhistorical TRAIN112、新DEV/semantic DEV各80、RPC DEV2,250を区別する。S0=138のS1の実model/Adam/scheduler/RNG/sampler3state、同親/spec/教師量をCPU照合した。既知12suite/2,628判断は全原raw/履歴/itemsとratings一致を照合して出典付きで再利用し、新学習・独立判断と数えない。

最終t3の全4原gate・対照比反復非増加・新DEV内容のpaired95%CI下限>0だけで有資格を判定する。途中点で救済しない。全28suite/6,132判断/NLL7点は未完了。契約SHA `e9f67a41237ca04ebe5c04bae9caac7e9eb019d689ee8ecfdf84a73ed45f5986`。累積GPU33,600秒は初回比較と有資格時の独立確認の各固定枠を合計した上限で、品質の達成保証ではない。

準備中に混在Chat TEST20行も解析した不具合があった。学習・GPU評価への使用0だが、元Chat TEST未参照の主張を取り消す。faulty source/準備とDEV-only修正sourceを元hash一致で保存し、DEV-onlyの再照合を通過した。有資格後のChat最終TESTは新たな封印版が必要。元Base TESTは未解析。CPU auditのsrc bootstrap欠落は凍結source不変のobserverで補った。[incident](../reports/phase7/chat-lr-20261014/protected_split_incident.json)。失敗を消して品質合格にしない。

## 実CUDA gate

2026-10-13T15:31〜15:32Z（JST翌日）にprobe9更新と全state連続/再開16更新を実行。有限性、model/Adam/scheduler/RNG/sampler/counters/historyの完全一致、epoch/終端fixtureを通過した。25更新は検証専用、候補本学習0。候補学習見積もり2,103.545秒/3,000秒、peak allocated16,223,183,360bytes。各workerの実終端と元10B UI復帰を確認した。

11件の条件/元gate/モデル規模/教師量/費用/source/完了metadata改変を拒否するCPU確認が通過した。全評価の時間予測をdurable workerで実測中。予測は初回新greedy3,504応答＋有資格4suite×3生成seed sampling2,628応答とNLL最大261batchを含む。予測gateが通るまで本学習は開始しない。

現在は12/28内容suite・2,628/6,132判断・NLL0/7点のCPU進捗監査。第1段階の選定/準備/契約を具体化し、第2段階の技術gateを進めている。学習/全内容/最終採否/有資格分岐/納品は未完了でgoalはactive。Base/Chat未完成・未採用。旧135の終了jobを再起動していない。


全評価予測は10,732.271秒/14,400秒で通過した。親新DEVの生成/NLLは15:38:31Zに終端し元UI復帰を確認。全219判断を完了し、親の内容1/80・実履歴文脈1/24。13/28suite・2,847判断・NLL1/7点を監査した。15:39ZにS1の全B学習をdurable workerで開始。15:43:54ZにLinux PID304617/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start54912399の実生存と600更新/312,871教師を確認した。残る学習/15レビュー/NLL6点/最終採否/分岐/完了監査/納品が必要でgoalを維持する。

比較CPU入口のpaired API引数順序の不具合を実行前のsource確認で発見し、凍結sourceを保持したcompare_chat_lr_observed.pyで元APIのitems/レビュー順に接続した。原3suiteの実paired数値/CIを再計算して元selectionと全一致を確認。元rubric・絶対gate・数値学習sourceは変更していない。
