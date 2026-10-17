# 回答学習の切り分け：参考比較・教材点検・少量診断

2026-10-17。[新計画151](151_answer_learning_execution_plan.md)の段階1〜3を完了した。**段階4の改善教材による対照SFTと、段階5の未知入力・実会話比較はまだ未完了。新しい「5まで」のgoalはactive。** 前回150の完了を今回の全工程の完了へ流用しない。

## 1. 参考モデルを実際に比較した結果

Akebonoの現行公開revisionは `74b3a1739e6d16883177c6021b3c03a7d517c7fb`。配布コードを確認し、重みSHA `8eef42db4b29928086b022c1dc9d8ee0d23f74e725bdbd45fc56c28340c89771` とTokenizer SHA `b5578c547c593640cd412d66d094eaf8d8fc79eb2e9ddbacc041903f94eab63b` を照合してCPU実行した。実parameter数9,965,824、語彙12,288、context512。

生成前に固定した同じ既知DEV20問（挨拶・日常・直接回答・訂正・文脈を各4）を4条件で生成し、全80応答を内容確認した。

| CPU FP32条件 | 内容成立 /20 | 自然停止 /20 | 空応答 |
|---|---:|---:|---:|
| Akebono公式128token・160字cap | 5 | 20 | 1 |
| Akebonoを別driverで32token上限 | 5 | 20 | 1 |
| 最初のJMicro SFT・32token | 4 | 17 | 0 |
| 前回JMicro C1・32token | 1 | 15 | 0 |

Akebonoの2条件は全20問で実入力ID・生成ID・本文・stopが同一で、明示した20判定を再利用した。訂正後の人数や場所を答えた一方、薄い封筒を厚い封筒の枚数で答える、地図の担当を鍵の担当と取り違える例もあった。これは少数の既知DEV上の非blind比較で、モデル全体の優劣や因果効果を証明しない。

各モデル固有の語彙・役割形式・学習履歴・システム文・特殊ID抑制が異なる。同じ32tokenを同じ日本語長とは扱わない。配布コードの元の128設定を書き換えず、別driverの32条件を保存した。[固定質問・実行条件](../reports/phase7/chat-answer-learning-20261017/reference_execution_contract.json) / [全raw](../reports/phase7/chat-answer-learning-20261017/reference_raw.json) / [全80判定](../reports/phase7/chat-answer-learning-20261017/reference_notes.json)。

## 2. 教材の能力点検

許可TRAIN-onlyの旧inventoryをhash照合し、RPC/Magpie×教師2〜32/33〜64から各30件、計120件を前向き抽出して全件を個別分類した。

| source・長さ | 直接回答 /30 | 確認質問 /30 | 中立な助手の初回教材として採用候補 /30 |
|---|---:|---:|---:|
| RPC 2〜32 | 5 | 2 | 11 |
| RPC 33〜64 | 12 | 3 | 5 |
| Magpie 2〜32 | 6 | 24 | 24 |
| Magpie 33〜64 | 6 | 24 | 28 |

直接回答には人間の食事・家族・実体験に基づく答えも含み、助手にそのまま事実として教えてよい件数とは異なる。120件では、過去情報を明示的に再質問して答える例・明示的な訂正に追従する例は確認できなかった。単なる話題継続と区別した結果であり、全corpusに該当例が存在しない証明ではない。意味確認は直前の質問・教師と最大2往復前を表示し、全履歴のbindingを保存した。[全120判定と定義](../reports/phase7/chat-answer-learning-20261017/TRAIN_capability_review.json)。

Magpieを64教師まで広げてもこの標本では確認質問が多い。機械的な短文選別が、入力に応じた答えを教える教材の確保とは別の問題であることが分かった。

## 3. 32件のTRAIN学習診断

意味を確認した32件（直接回答6＋相槌/挨拶/確認26）を選び、全対象を完全な32教師以内に限定。元10B Base/fresh Adam/native10M/seed42/LR1e-4/同じteacher trainer・512教師更新/32×1024/BF16/mathで25万教師を前向きに固定した。実478更新・250,018教師で終了した。

| 指標 | 学習前 | 学習後 |
|---|---:|---:|
| 内容成立 /32 | 0 | 31 |
| 直接回答の内容成立 /6 | 0 | 6 |
| 自然停止 /32 | 3 | 32 |
| 教師本文との一致 /32 | 0 | 32 |
| 同じTRAINのmean NLL | 4.012774 | 0.000001103 |

全64生成を個別確認した。教師と一致したから全件を自動合格にせず、表現の不自然な1件は文法1とした。完全な小集合の対応を学べることが実証された。**これは反復したTRAIN32件の暗記診断であり、未知入力の汎化、名前の記憶・訂正の一般化、正式品質の合格ではない。** 診断重みを次の主比較の親にしない。

全478更新履歴をCPU全消費の教師batch/LR/終端samplerと照合、119 Adam state/モデル/scheduler/RNGを保存し有限性を確認した。技術確認の2更新連続と1更新＋保存＋1更新のcheckpointは、全fieldで厳密一致した。最大32×1024の受入は同じnative source/runtimeの前回実測証拠を再利用し、データ変更経路の保存再開だけを新規確認した。

最初の技術wrapperは保存用data/manifest.jsonの準備漏れで、最初の保存時に停止した（メモリ上の技術2更新、本学習0、保存state0）。旧source/config/jobを保全し、別のmanifest-packaging-v2でmanifestを事前にbindingして再確認。教材・数値条件・品質条件は変更せず、旧技術2.615431秒を全額継承した。全所有stage wallは157.818719秒。元Baseの実identity・idle HTTP・kernel FLOCKの復帰も確認した。[失敗と包装修理](../reports/phase7/chat-answer-learning-20261017/diagnostic_packaging_repair.json) / [診断の全監査・全採点](../reports/phase7/chat-answer-learning-20261017/diagnostic-manifest-v2/completion.json)。

## 4. 次のSFT教材の準備状態

直接回答を含む別候補として、LLM-jpのDolly日本語版をrevision `f8ae87df31fac05429d974264eeb35c453bde737`、JSONL SHA `4af3f1490a2e36d74cecfe44fe1c667c8324256268d9479a279031deb1e638a0` で取得した。公式説明はDatabricks DollyのDeepL訳・CC-BY-SA3.0。[公式card](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja)。

元行番号から本文JSON解析前に新DEV1,527 IDを留保し、許可TRAIN13,484行だけを解析。完結64教師以内の候補は6,318件・196,355教師で、うち本文contextがある候補2,208件。旧保護splitはmetadataのhash/MinHashだけで照合し本文を読まない。LSHの漏れやweb由来の祖先重複は除外し切ったとは主張しない。[実量](../reports/phase7/chat-answer-learning-20261017/dolly_inventory.json)。

category×長さ×本文contextの層を巡回して120件を個別確認し、採用候補57件・不採用63件。質問と無関係な人名、国籍を言語へ変える訳、与えた本文の人物や地域の取り違え、条件違反を確認した。外部の珍しい史実を一次資料で未照合のため保守的に断った例も含むため、63件すべてを事実誤りとは呼ばない。標本採用率を母集団の正答率へ換算しない。本文contextありでも27/44の採用候補に留まり、categoryだけで品質保証しない。[全120件QA](../reports/phase7/chat-answer-learning-20261017/dolly_QA_review.json)。

この状態でDolly全量を無条件に次SFTへ投入しない。既存素材で不足する直接回答/文脈参照の量と質を確保するため、CohereLabs/Aya Datasetの公開TRAINについてmetadataを確認した。公式説明は人手の新規注釈と人手編集による多言語指示応答、Apache2.0。現行revision `f9ea04583f02a8f86404ff6c58bf75fe637df8a2` はpublic/ungatedで、日本語を含む。**この時点ではAyaのデータ本体は未取得・未解析**。[公式card](https://huggingface.co/datasets/CohereLabs/aya_dataset)。Ichikaraの試したmetadata入口は401で、データや連絡先の提供・規約同意は行っていない。

次はAyaのTRAIN-only日本語候補の実量・個別内容を確認するか、Dollyの根拠付き候補subsetを追加で全件確認し、実際に成立する1件の教材recipeへ絞る。主比較の教師量/配合/LR/configはまだ未凍結。新DEV80はTRAINを確定した後に固定し、同元Baseから新対照・候補を学習して全評価・実会話へ進む。新TEST・有料クラウド・外部公開・旧閉鎖run再開は行わない。
