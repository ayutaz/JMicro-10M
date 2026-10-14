# JMicro-10M 調査・検証・学習の全体記録

2026-10-13追記: 下の全体台帳は2026-10-09までの固定revision記録。後続のChat診断・教材比較は[結果129](129_chat_first_sft_execution.md)、[結果132](132_chat_improvement_execution.md)、[最新結果136](136_chat_generalization_results.md)で実行・全評価を終え、いずれも不採用。現在は文書・計画のみの更新で追加実験は停止中。[最新計画135](135_chat_problem_solution_plan.md)、[現在の状態](autonomous_status.md)。詳細台帳の原revision・報告数を後続実験を含む全件数へ読み替えない。

記録日: 2026-10-09 JST。約10Mの日本語モデルを作る過程で、何を調べ、何を実装し、どの条件を学習・評価し、何が改善せず、何を残したかをまとめる。**Baseの品質目標は未達で、学習・研究実行は一時停止している。今回の保存作業は学習再開ではない。**

この文書は経緯と判断を読むための説明である。全保存報告の原キー・数値・失敗・採否は[詳細台帳](retrospective/README.md)、当時の計画と説明は[原文書一覧](retrospective/document_map.md)、現在の事実は[status](autonomous_status.md)を参照する。代表結果だけを全実験の代わりにせず、原記録へ戻れる形で残す。

## 1. 目的と、最後まで変えなかった条件

小さな日本語言語モデルをTokenizerからスクラッチ構築し、自然な短文生成を行うBase、その後に短い雑談を行うChatとローカル利用一式を作ることを目指した。初期contextは1024。高度な知識、長文推論、コード生成等は達成条件へ加えていない。

ユーザーは、モデルを大型化するより**10Mのサイズを維持することに優位性がある**と明示した。現モデルは10,001,152 parameters、既存予算は9.5M〜10.1M。品質改善のために30M/100Mへ切り替える方針は採用しない。同予算内の構成変更も、過去の凍結モデルを上書きせず別の比較として扱う。

日本語Baseの品質基準も維持する。小さいモデルだからという理由で基準を下げず、対象を物語だけへ無断で縮めない。未達は未達として報告する。Chat・量子化を進めてBaseの品質未達を見えにくくしない。

[AGENTS](../AGENTS.md)、[プロジェクト目的](01_project_goal.md)、[現行ロードマップ](15_project_roadmap.md)、[次回計画124](124_base_recovery_plan.md)。

## 2. 記録の範囲と読み方

今回の整理前のGit revisionは`2d48062f5e29f7cb4cc9a1eb4352aa304e44827c`。その時点で保存された全11,289ファイルをpath・bytes・Git blob SHA1で一覧化した。うちreportsは9,465ファイル、JSONは4,947件。4,815 JSON objectから原status・予算・教師量・品質指標・合否・解釈等を抽出し、残る132件も理由付きで記録した。

対象外の内訳は2MiB超16件、非object JSON22件、歴史的なsource snapshot94件。対象外も原ファイルと全file一覧に残しており、確認済み・合格として扱わない。配列の全生成文、個別採点、全更新履歴は原記録に残し、再採点していない。105原文書への一覧、XMLに保存された297 suiteの属性とfailure/error/skip node数、WSL reportsの28,228 file/symlinkのmetadataも保存した。

**記録数は独立実験数ではない。** proposal、途中job、終端result、review、completion、portable copy、snapshotが同じ実験を重複して表す。教師量・GPU時間・test数をこれらの行から単純合計しない。全実験の一意な総GPU時間や総教師量は今回新たに認証していない。

分野別台帳は検索のためのファイル名分類であり、原因や採否を自動判定したものではない。古いrunningやnext_actionは当時の記録。現実の稼働にはPID/boot/start ticksと終端記録の照合が必要である。

| 読みたい内容 | 保存先 |
|---|---|
| 全体の経緯と教訓 | この文書 |
| 個々の完了・採否 | [完了・判断一覧](retrospective/decisions.md) |
| 設定・数値・実行予算・失敗flags | [分野別詳細台帳](retrospective/README.md) |
| 初期調査・原計画・各結果説明 | [原文書一覧](retrospective/document_map.md) |
| すべてのGit保存fileの所在 | [tracked_files.tsv](retrospective/tracked_files.tsv) |
| 抽出した原キー・値・SHA256 | [experiment_records.json](retrospective/experiment_records.json) |
| 抽出しなかった報告と理由 | [exclusions.json](retrospective/exclusions.json) |
| 保存されたCPU tests等 | [verification_ledger](retrospective/verification_ledger.md) |
| Git外の重み・metrics・rawの所在 | [native_reports.tsv](retrospective/native_reports.tsv)、[引継ぎ](windows_handoff.md) |

## 3. 初期調査: 小型化・Tokenizer・学習・評価

初期にはdeep-thin Transformer、GQA、RoPE、RMSNorm、QK-Norm、SwiGLU、tied embedding、biasなし、dropout0を候補にした。語彙層が小型モデルのparameter予算を大きく使うため、4k/8k Tokenizerとモデル配分を実比較する計画にした。

MobileLLM等の小型モデル設計、TinyStories等の小規模生成、公開10M級モデル、Chinchilla等の学習量の考え方、Qwen系の構成、Mamba/Conv hybrid、Layer Sharing、Muon、SFT・蒸留、GGUF・量子化を調査した。ただし、大きい規模・英語・限定した物語での研究結果を、10Mの幅広い日本語品質の保証とは扱わなかった。研究候補と実装済み・実測済みの条件を分けた。

当時の調査の引用・採否理由は[調査要約02](02_research_summary.md)、[構成03](03_architecture.md)、[技術課題11](11_technical_research_gaps.md)、[実装研究12](12_training_implementation_research.md)、[Tokenizer/会話13](13_tokenizer_dialogue_data_research.md)、[評価/配布14](14_evaluation_deployment_research.md)、[先行例09](09_prior_art_and_baselines.md)へ保持する。これらは当時の調査記録で、将来案を現行の実行指示として扱わない。

## 4. Phase0–1: 実験契約と追跡可能なpilot

2026-10-02、M1 iMac上でリポジトリ、Python3.12.7/uv固定、schema、seed、run ID、source snapshot、input/config hash、評価splitを整備した。BaseとChatは各100入力を用意し、DEV80/保護TEST20に分離した。準備runはtokens0として記録し、code準備を学習実績と扱わない契約にした。[Phase0完了16](16_phase0_completion.md)。

データpilotはFineWeb2 Edu Japaneseの固定範囲20,000 recordsとRealPersonaChat3,000対話から構築した。取得23,000、採用22,998、canonical本文42,647,826 UTF-8 bytes。Web19,998文書、会話3,000対話で、source revision・原file/row/本文hash・除外理由・bucketを保存した。

exact/near重複、同URL、長い共有prefix等をclusterとしてsplitし、固定evalとの混入も検査した。Tokenizer sampleはtrainだけから取り出した。二回のoffline buildの6成果物がbyte一致し、23,000原recordsを復元して確認した。このpilotの全件確認と、後の12.23B Web全量の独立監査は別物である。[Phase1完了17](17_phase1_completion.md)。

Webとshare-alike会話データは別bucketで管理した。source条件の確認は、個々のWeb本文や学習済み重みの公開条件を一括認証するものではない。今回pushするものもコード・文書・保存済み小報告であり、raw corpusや学習重みの新規公開ではない。

## 5. Phase2: Tokenizerの学習と日本語・byte契約

SentencePiece Unigram＋byte fallbackで4096/8192語彙を同じtrain-only sampleから学習した。sampleは2,444文書/対話、本文4,499,689 bytes。coverage0.9995/0.999/0.995の全6候補が契約を通過し、両語彙で0.9995を採用した。

正規化、前処理golden、全sampleとpilot全22,998件のround-trip、全256 byte値、未出現Unicode、制御文字、lone surrogate・未decode bytes拒否、不正UTF-8検出を確認した。学習sampleと順序・hashを固定した再学習ではartifact一致を確認したが、別OS・別versionでの再学習一致は保証しない。移行では学習済みTokenizerを復元する。

| 語彙 | Web bytes/token | 会話 bytes/token | 会話総系列tokens | Assistant教師tokens |
|---|---:|---:|---:|---:|
| 4096 | 3.9207 | 4.4855 | 1,496,446 | 705,467 |
| 8192 | 4.7865 | 5.4406 | 1,250,640 | 581,149 |

圧縮効率が良いTokenizerが同token予算・同GPU時間・同モデル配分でも勝つとは限らないため、後のGPU比較へ渡した。[Phase2完了18](18_phase2_completion.md)。現在の4096 model SHA256は`a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`。

## 6. Phase3: モデル・cache・exportの成立

T8Kは9,772,800、T4K/QK-Normありは10,002,816 parametersを実装した。因果性、padding、full/cache、HF/native float GGUF、量子化の型・容量・数値比較をCPUで確認した。ただしPhase3の重みはランダム初期化であり、自然な日本語や学習済み量子化品質の実績ではない。[Phase3完了19](19_phase3_completion.md)。

後に選んだnative referenceは語彙4096、hidden256、13層、FFN640、4Q/2KV、head64、SwiGLU、RMSNorm、RoPE1024、tied embedding、NoQK-Norm、biasなし、dropout0。実parameter数10,001,152。構成のコードと古い輸出実験を現在の品質認定と混同しない。

## 7. Windows/WSL移行・権限・復元・長時間実行

Phase4からWindows/WSL2/Ubuntu/RTX4090へ移行した。WSL package3.xとdistributionのWSL2は別の値として確認した。GPUの利用はWindows側NVIDIA driverにも依存するため、「WSLで学習するのでWindows driverは無関係」とはしなかった。現確認済み構成はWSL3.0.1、driver616.92、uv Python3.12.7、PyTorch2.14.1+cu130、BF16。

初期には権限・OS操作・復元・runnerの観測などが進行上の問題になった。ユーザーのfull access許可と、OS昇格/再起動が必要な操作は区別した。ログに新しい行がないだけで停止とせず、実processとcounter増加、job/result、GPU lockを確認する運用へ整備した。

固定公開pilot/Tokenizerのrevision・manifest/hashを用いて復元し、Tokenizer再学習やPhase3の全再実行を移行前提にしなかった。Windows正本、WSL実行コピー、大容量dataを分離した。全Pythonはuv経由とし、system Python/pipにfallbackしないルールを固定した。

長期jobは会話が終わっても継続するよう、PID/boot/start ticks、launcher、log、checkpoint、消費教師、GPU ledgerを保存した。普通のresumeでsource/schedule/予算を変えず、学習済み親の全stateを保持する。実GPU再開gateを通過してから長期学習へ進む。[Phase4完了21](21_phase4_completion.md)、[引継ぎ](windows_handoff.md)、[自律runner](codex_automation.md)。

## 8. Phase4–5: 保存再開・overfit・smoke・100M選定

Phase4では実shard、CUDA/BF16 forward/backward、有限値、学習器・評価、全state保存再開を検証した。64 testsとhandoff7 gate、両モデルのresume一致を記録した。保存対象はmodelだけでなくoptimizer/scheduler/RNG/sampler/countersである。

Phase5ではcompile/defaultとeager/defaultの厳密resume不一致を保存して棄却し、eager/mathで一致を確保した。固定連結block overfitはtrain lossが約0.002まで下がっても文書単独再現が2%で不合格だった。文書単位windowへ修復し、元の6,000更新上限・閾値のまま再実行して合格した。元失敗runを削除していない。

最終overfitは100 train文書、NLL0.012770、teacher accuracy99.712%、16-token continuation exact100%、末尾EOS100%。smokeは10,002,432 tokensでdev BPB2.747870→1.416968。これらは学習経路の成立を示すが、未知の広い日本語品質を保証しない。

同100,007,936 tokensの比較では、T4K/NoQK-Norm/LR0.002を次の候補にした。

| 構成 | 共通DEV BPB | 共通短文BPB | 定常tokens/s | greedy EOS /80 | 反復 /80 |
|---|---:|---:|---:|---:|---:|
| T8K/QK-Norm/LR0.002 | 1.258861 | 1.650058 | 117,119 | 0 | 54 |
| T4K/QK-Norm/LR0.002 | 1.231823 | 1.591386 | 111,693 | 0 | 53 |
| T4K/NoQK-Norm/LR0.002 | 1.221443 | 1.546589 | 121,139 | 0 | 54 |
| T4K/NoQK-Norm/LR0.001 | 1.235002 | 1.618124 | 121,046 | 0 | 52 |

近いbyte予算ではT8Kが僅かに良い補助結果も残した。NoNormの選択は予算に依存し、生成停止やsampling Unicodeの問題は未達のままだった。[Phase5完了23](23_phase5_completion.md)。

## 9. Phase6基盤: データ拡張・速度・資源・変換

初期の約756M trainを準備し、WSDのstable枝/decay評価枝とCUDA全state再開を成立させた。その後一般Webを12,225,819,077 tokensまで準備した。大量の公開sourceがあることと、取得・変換・受入済みTRAINの量を分けた。[準備26](26_phase6_preparation_completion.md)、[10B corpus32](32_local_10b_corpus.md)。

Windows側への頻繁な大容量I/Oを避け、処理・学習はLinux diskに置いた。変換・保存・dedup/index照合が学習開始を遅らせたため、ユーザーの要望に従ってaccepted loader/build証拠を再利用し、巨大corpusや13GB級indexの不要な再scanを避ける方針を固定した。独立全件監査を省略した部分は未完了として残す。

性能ではreference/math、compiled/math、Flash/compile、batchを実比較した。Phase6③のcompiled Flash容量上限111に対し、最速はbatch32・694,521入力tokens/sだった。最大batch/VRAM消費と最高速度を分けた。後のnative/BF16/math/短い有効教師の系列へ、この入力速度をそのまま適用しない。[性能28](28_phase6_performance.md)、[完了29](29_phase6_performance_completion.md)。

NoNormのHF/Llama・GGUF/Llama adapterも整備し、学習済み重みをCPU精度profileで確認した。未修正stock FP32の失敗を保持した。これも最終Chatや採用済みモデルの量子化品質が完成した証拠ではない。[変換30](30_phase6_readiness_execution.md)。

## 10. 主系列5B・10Bと、EOS/反復/文字末尾

主系列はWeb中心に5B、総10,000,007,168 tokensまで学習した。元10Bの本学習GPU時間は7,657.678秒。モデル・optimizer・scheduler・RNG・sampler・metricsと終端状態を確認した。元10Bは現在のWebUIの重みであり、後の2B fresh/native比較とは別の系列である。[5B35](35_base_5b_execution.md)、[5B比較36](36_base_5b_comparison.md)、[10B学習41](41_base_10b_training.md)。

共通全文DEVの元10B BPBは0.954018473。固定greedy80のEOSは0、反復53。全400条件のEOS9件は「9独立prompt」ではなく、80prompt×5modeの中の停止である。全9件を読むと、適切な内容完結は1件だった。BPBが改善しても自然な続きを生成できていないことが明確になった。[10B品質42](42_base_10b_quality_evaluation.md)、[日本語評価46](46_japanese_base_evaluation_v2_results.md)。

5B親から従来Webと短い完結文を混ぜる条件を比べ、EOS・反復の改善は見られたがraw Unicode失敗もあり、最終採用には至らなかった。生成の途中でUTF-8 byte列が切れる問題は、表示の末尾処理とモデルのraw失敗を分離した。表示を整えてraw failureを消したことにはしない。[計画37](37_eos_repetition_utf8_improvement_plan.md)、[結果38](38_eos_5b_finish_results.md)。

## 11. 評価を日本語Base向けに拡張した理由と結果

ユーザーがWebUIを試した際、同じ語の定義を循環させ、入力場面を展開できない例が出た。このため本文BPB・EOS・機械的反復だけでは日本語品質を十分に表せないとして、評価の棚卸しを行った。[監査44](44_japanese_base_evaluation_audit.md)。

JBLiMP、JCommonsenseQA、JNLI、JCoLA、JSQuADと、否定・数量・時間・比較・照応・因果の基本意味診断を追加した。公式testを学習や選定に使わず、DEVや事前固定小sampleを用いた。長さ正規化・unigram補正・prior・多数派回答を併記し、高い採点方式だけを後から主指標へ選ばなかった。

元10Bの代表結果は以下。公式全taskの再現と独自小診断を区別する。

| 評価 | 結果 | 解釈の限界 |
|---|---:|---|
| JBLiMP sample SLOR331対 | 74.62% | train先頭2M IDsのunigram補正。公式全train頻度再現ではない |
| JCQA公式DEV1119 | 30.38% | chance20%より上だが、大半は誤答 |
| 基本意味96family/192例 | 59.38% | 両文脈正答23/96、共有template・非独立sampleの限界 |
| JNLI 0/3-shot | 14.34% / 14.59% | 回答priorに偏り、理解成立とは言えない |
| JCoLA 2-shot in/out | 74.80% / 68.47% | 多数派83.93% /73.28%より低い。MCCもほぼ0 |
| JSQuAD DEV固定100 | EM0、文字F1 12.69% | 独自文字F1・64-token生成。公式形態素F1/全体scoreではない |

文法、入力との関連、文間一貫性、適切完結を分け、全rawを個別に読む診断を追加した。Codexの非blind採点は独立した人間blind評価ではない。EOSが出た、文法が自然、正解候補の尤度が高い、という三つも同じ能力ではない。[仕様45](45_japanese_base_evaluation_v2.md)、[結果46](46_japanese_base_evaluation_v2_results.md)。

## 12. 教材配合・量・学習量を増やした比較

完結文の三条件100M、物語10%/20%、低LR、100M/500M/1Bを段階的に比較した。物語20%・低LR100Mは同LR Web対照に比べ、一貫性0→12/80、EOS0→23、反復59→22、BPB悪化約0.67%で元の相対条件を通過した。その後500M候補も研究上の比較条件を通過したが、実用品質には未達だった。[比較48](48_complete_text_10b_comparison.md)、[10%判断51](51_story10_judgment_and_next_proposal.md)、[20%判断53](53_story20_low_lr_judgment.md)。

「全ての試みが無効だった」とは言えない。一方、研究上の比較合格をBase採用と呼んではいけない。元UIを候補へ自動で差し替えなかった理由もこの区別にある。

その後は全文教材、量と長さ/EOS位置をそろえた選別、同pool500M→1B、物語59,963,449→200,000,192 tokensなどを比較した。物語増量の各追加1BではJCQA35.031→38.561%が改善した一方、一貫性15→9、適切完結20→19、EOS34→25（各80）で候補不採用だった。

| 比較 | 用意した量 | 学習の量 | 主な結果 |
|---|---|---|---|
| 旧/新物語pool | 約60M /200M | 各追加1,000,013,824 input tokens | BPB0.977155/0.977322、JCQA改善・生成不採用 |
| 同Web/story教材の学習曲線 | 500,000,785 tokens | stable2B/5B＋各20M decay教師 | BPB1.138590→1.127218、一貫性21→15、適切完結27→24 |
| 教材量の比較 | 約500M /2B、同75/20/5配合 | 各1B＋20M decay教師 | BPB1.155191/1.157868、一貫性11/14。全条件不合格 |

各行の入力tokensと教師tokens、schedule、親、DEV分母は異なる。行を横断して量だけの効果や学習曲線を作らない。source/長さ/EOS密度まで変わる比較は交絡を明示した。[全文55](55_complete_document_500m_results.md)、[量/学習57](57_matched_story_and_learning_budget_results.md)、[増量60](60_dataset_expansion_results.md)、[学習曲線原review](../reports/phase6/amount_learning_review.json)、[5B完了](../reports/phase6/improved_base_5b_completion.json)、[教材量review](../reports/phase6/textbook_quantity_comparison_review.json)。

## 13. 教材選別・供給の失敗も保存した

同source/文長/EOS位置を合わせた条件保持poolは、内容確認で準備gateに届かなかった。selector v2も別train32で開発・凍結後、未確認40各を確認したが弱例12/14で不合格だった。準備失敗分岐で停止し、未実行100Mを学習実績へ加えていない。[結果63](63_condition_preservation_preparation_results.md)、[結果65](65_condition_selector_v2_preparation_results.md)。

自然原文を増やす準備ではWeb単独の固定64に弱例18/24、混合案ではWeb供給不足を記録した。source/配分を別契約で修正した10,000原文poolは受入に達したが、同100M比較では意味診断58.333→64.583%に対し一貫性6→3、適切完結6→2、EOS30→7（各80）で不採用だった。[準備修復76](76_diverse_preparation_repair.md)、[原文結果79](79_narrative_diversity_results.md)。

教材源としてWikipedia、Livedoor、公開prose、Sarashina由来の限定teacher文、OpenJA、Tatoeba、Tanaka編集PD2008、翻訳物語・原言語物語等も調べた。アクセス可能、量が足りる、encodingが正しい、内容が適切、学習が改善する、という段階を区別した。供給量、strict encoding、固定内容gate等で閉じたsourceは、学生モデルの学習失敗ではない。

例えばWeb95/story5の500M/2B準備は固定64中弱11で上限10を超え、GPU学習へ進めなかった。Tatoeba/OpenJAは量、Tanaka編集sourceはstrict body encoding、翻訳/物語sourceは固定内容等の失敗を残す。抽出の再試行・係数変更で過去の不採用を書き換えない。[教材詳細台帳](retrospective/02_material.md)、[準備不採用](../reports/phase6/larger_material_v3_completion.json)。

## 14. 条件保持・記憶・packing・汎化の切り分け

小さな著作/合成教材で条件保持を学べるか、文書連結順序や文書単位学習が結果を変えるか、教材を増やすと未見条件へ移るかを比較した。少数例の記憶と広い日本語生成の差が大きく、trainでの成功をDEVでの一般能力と扱わなかった。[診断67](67_condition_learning_diagnostic_results.md)、[packing69](69_packing_learning_results.md)、[自然学習74](74_natural_learning_results.md)。

後続ではcondition diversity/positive/query balance/relation/transfer、mature親対fresh、historical親、source順序、早期8M対100M、story教師比率、textbook被覆などを調べた。固定比較を完了してもBaseの全品質に届かない結果を残した。生成の失敗とteacher-forced尤度の失敗を同じものとしない。

[学習・配合台帳](retrospective/03_learning.md)、[評価・条件保持台帳](retrospective/06_evaluation.md)、[完了・判断一覧](retrospective/decisions.md)に個々の原報告と採点・量・採否を保存する。

## 15. 実装や数値誤差が主原因かを調べた

根本原因診断ではBOS/body/EOS、x/yの一位置shift、PAD除外、生成時EOS抑制を確認した。二重shiftやEOS無効化を主原因とする証拠は得なかった。

元実重みのFP32でfull/causal fast、cache、独立HF referenceとlogits/CE/代表gradientを比べた。BF16対FP32、Flash対math、compiled対eagerには固定許容値を超える項目があり、**数値7失敗を失敗のまま保存した**。閾値を変えて合格にしなかった。

別契約でFP32生成を追跡するとoriginal/mixedのEOS・反復件数は主要部分が同じだった。この小標本では精度変更だけで品質問題が消える仮説を支持しなかったが、長期学習trajectoryへの影響を完全に否定していない。[根本原因72](72_root_cause_diagnostic_results.md)、[数値/gradient詳細](retrospective/04_objectives.md)。

## 16. 学習目的・teacher・最適化の比較

目的やregularizationを変える試みを多数実施した。以下は実験系列の入口であり、各固定条件の詳細・中間失敗・GPU上限・全内容採点は分野台帳から原記録を読む。方式一般の無効性を証明したものではない。

| 試み | 検証した狙い | 保存された判断の位置付け |
|---|---|---|
| sequence UL・低係数UL | 自己生成の反復を罰する | 同25M比較・gradient診断・低係数比較を完了、固定候補不採用 |
| positive anchor / outcome ranking / natural-context contrast | 条件に合う続きと不適切な続きの差を学ぶ | 各固定pilot/teacher移行/projection経路を保存、Base全合格に至らず |
| hard-body Web replay / shared-prefix loss | 苦手教師や共通prefixの損失を切り分ける | 診断・固定比較と保持結果を保存 |
| Web KL / EOS-decoupled KL | 元Web能力を保持しつつ改善する | 初期CUDA失敗・budget rejection・repair・終端比較も保存 |
| native teacher KD / on-policy teacher / hint / preference | teacher信号を小型モデルへ移す | teacher品質とstudent改善を分け、固定100M等を不採用として保存 |
| label smoothing / confidence penalty | 過信・分布を調整する | 固定100M比較を完了、候補不採用 |
| next-two-token / middle supervision | 追加予測・中間教師で学習を変える | 固定100M比較を完了、候補不採用 |
| Muon / AdEMAMix / SAM | 最適化の差を調べる | 固定100M比較を完了、候補不採用 |
| weight averaging / displacement anchor | 重み空間・親保持を調べる | 同条件比較・単一midpoint等を保存、候補不採用 |
| grouping / gradient accumulation | 同教師列で更新のまとまりを変える | 約94Mpilotを完了、候補不採用 |
| teacher-normalized weight decay | 更新あたりでなく教師量に応じた減衰へ変える | 短期BPB screen通過後2Bを完了したが、最終候補不採用 |

[目的・最適化台帳](retrospective/04_objectives.md)。初期失敗を含むcompletion以外のproposal、launch、preparation、resume、review、notesも一覧に含めた。同じ実験のportable/root/nested記録を別実験として数えない。

## 17. 10M内の構成・parameter配分・反復計算

層数/幅/FFN配分、gated layer sharing、context mixing、headwise gate、KV配分、readout adapter/output mixture、SigSoftmax、parallel residual、residual dropout/初期化等を調べた。Layer Sharingは13 unique blocksを各2回使う実100M比較まで行い、不採用だった。単なる再訪順序やgate初期値の変更を、未検証の独立した有望経路として繰り返さない判断も保存した。

ReLU²はtwo-projection FFN960を実装し、SwiGLU640と10,001,152 parametersを合わせた。CPU22 tests・実CUDA保存再開・batch80/context1024を確認したが、各300M比較の事前4時間予算を速度予測が超えたため、本比較は未実行で閉じた。これはReLU²の品質が劣るという結果ではない。

parallel residualはfresh同2Bの対照と候補を比較した。attention saturation、KV head gradient、embedding gradient等の読み取り診断も保存した。短いプロトタイプ・容量probe・CPU数値確認が成功しても、本学習や日本語品質が成功したことにはしない。

[構成03](03_architecture.md)、[構成詳細台帳](retrospective/05_architecture.md)、[ReLU²予算終了](../reports/phase6/base_relu_squared_probe_completion.json)、[反復計算再提案の判断](../reports/phase6/base_recurrent_compute_novelty_review.json)。

## 18. 直近のcapacity・TRAIN/DEV・LF・原文脈診断

現native2Bモデルの固定6原文に対するpositive controlでは、最初のCUDA再開gateが不一致で停止した。決定論設定/CUBLAS workspaceの欠落を修復し、元失敗も予算へ加えて再実行した。同BOSから6つの異なる先頭語を全て正答することは不可能なので、GPU前に全原教師の理論上限と条件付き教師を分けて記録した。

最終的に全原751/756という理論上限、固定prefix以降612/612、全6原suffixとEOSを完全再現した。診断学習252,176教師で、科学Baseへの追加学習は0。probe重みは採用していない。

TRAIN既知16と長さ対応DEV16ではteacher NLL差の事前fit-gap screenは不成立だった。ただしtopic/style・露出回数は揃わず、十分学習/過学習なしとは結論しない。TRAINの自由生成にも循環があり、未見文だけの問題という説明も支持しなかった。

同32本文の末尾LFを変える96variantではEOS確率の全体medianが0.05019→0.95490、27/32で増えた。一方DEV16のmedianは0.04772→0.31356でTRAINより弱い。marker感度を確認しただけで自由生成の改善ではない。

同TRAIN16へ原記事contextを戻す診断は本文NLLを2.64207→2.52240へ改善したが、平均文書改善0.11424で事前screen未達だった。内部段落EOSを元記事EOSと誤認せず、位置/長さ等の交絡も残した。

[6文control](../reports/phase6/base_residual_capacity_control_completion.json)、[TRAIN/DEV](../reports/phase6/base_residual_train_dev_history_completion.json)、[LF](../reports/phase6/base_residual_boundary_counterfactual_completion.json)、[原context](../reports/phase6/base_residual_original_context_completion.json)。

## 19. 最新の教師量正規化decay: 短期改善から2B不採用まで

native学習は短い有効教師の更新が多く、通常のupdate単位weight decayと教師単位の露出が異なる点に着目した。32768教師を基準にdecay-only factorを`(1 − lr×0.1)^(その更新の教師数/32768)`へ変え、Adamのgradient更新とteacher-position LRは保持した。これは学習後weight normの原因を証明したものでも、既知scaling式の公式再現でもない。

約94,160,195教師pilotはBPB1.290203→1.262247、文法28→31、一貫性2→2、適切完結3→4、EOS13→16、反復49→49（各80）。事前のBPB2%改善・非退行screenを通過し、同条件・同親・reset/reheatなしで累積2Bへ継続した。[pilot120](120_base_teacher_decay_pilot_results.md)。

追加学習1,905,839,805教師、最終212095更新、科学累積正確に2B。元native2B対照と全sampler/scheduler/counters/教師列が一致した。実CUDA連続4対2+save+2の15checks合格、検証8更新/71,464教師は別会計・重み破棄。

| 指標 | 元native2B | 正規化decay2B |
|---|---:|---:|
| 共通DEV256 BPB | 1.106386 | 1.090316 |
| 文法2 /80 | 23 | 22 |
| 関連性2 /80 | 30 | 16 |
| 一貫性2 /80 | 3 | 3 |
| 適切完結 /80 | 7 | 5 |
| EOS /80 | 20 | 23 |
| 反復 /80 | 27 | 27 |
| Unicode失敗 /80 | 0 | 1 |
| 基本意味 | 56.771% | 56.250% |
| JBLiMP | 78.852% | 80.060% |
| JCQA | 38.293% | 37.131% |

BPB約1.45%改善、paired文書差95%CI[−0.0209552,−0.0118732]。一貫性差0、率CI[−0.0375,0.0375]。全80を個別に読み、UTF-8失敗base-070も残した。元絶対6条件は全未達で、strong/cached/historical参照を含む全条件にも届かなかった。固定条件を閉じ、10B延長やseed43を始めなかった。

追加GPU26,060.094秒（約7時間14分）、pilot込み27,475.228秒。科学PID118881/Windows worker38176は終了、ledger closed。job.jsonの周期heartbeat212080と、最終result212095を混同しない。runner resultのcontent_pendingは後続completionで解消済みだが、元結果は上書きしない。[結果123](123_base_teacher_decay_2b_results.md)、[completion](../reports/phase6/base_teacher_decay_2b_completion.json)。

## 20. 最終確認・Chat・量子化の準備と、実施していないこと

独立学習seed43、fullDEV/400＋長文40、protectedTEST/最終採否の実装経路を準備した。ただし旧stable＋20M decay専用とnative方式はcheckpoint/evidence型が異なり、nativeを旧形式へ偽装して通せない。native seed factoryとCPU4 testsはあるが、その独立GPU学習・最終接続は未完成。[準備122](122_base_native_seed_confirmation_preparation.md)。

Chat側もDialog mid-training→Assistant本文＋EOT-only SFTと直接SFTの比較、masked batch probe、全219応答/own-history、複数生成seed、blind packet、評価者一致、Base retention等のコード・fixtureを準備した。これらCPU準備をChat学習や実人間評価に数えない。ユーザーのBase-only境界で、Chat/SFT/学習済み最終量子化には進んでいない。

過去の研究候補には全文DEVや400/長文評価を実施したものもあるが、最新候補の独立seed/fullDEV/protectedTEST/adoptionが完了したという意味ではない。正式採用Base/Chat、独立人間blind、独立全corpus監査、最終採用モデルの量子化品質は未達・未完了として残す。

## 21. 指標と、比較してはいけないもの

| 用語 | このプロジェクトでの意味 |
|---|---|
| 10M parameters | モデルが持つ重みの数。学習tokensやfile容量ではない |
| 用意したデータ量 | accepted TRAIN poolのtokens/文書/bytes。再利用subsetを新規量に足さない |
| 学習量 | 実際に消費した教師tokensや入力tokens。単位を明示する |
| CE入力/physical入力 | 教師以外やpaddingを含む別会計。GPU速度にも影響する |
| epoch | どのpoolをどう走査したかが定義できるときの周回。混合samplerでは比だけで厳密周回と言わない |
| BPB | 原本文byteあたりの予測損失。低いほど良い。文法や意味の成功率ではない |
| EOS停止 | ID列で停止したこと。内容が適切に完結したこととは別 |
| 反復flag | 固定アルゴリズムの診断。正常な語句再使用・意味的循環とは別に内容を読む |
| 生成seed | 同じ重みの生成乱数。独立した学習seedを代替しない |

全文DEVは89,416文書/164,344,743本文bytes/42,003,934本文tokens。最新DEV256は472,055 bytes/122,343本文tokens。分母が違うBPB、親が違う10Bと2B、配合/長さ/EOSが違う教材、teacherとpadding入力、複数modeと独立promptを混ぜない。

元固定DEV80の絶対条件は文法≥56、一貫性≥27、適切完結≥27、EOS≥37、反復≤18、empty/role/Unicode0。指定された相対比較・paired CI・BPB保持guardも必要。最終TESTの停止95%等とは別であり、DEVの値を最終採用基準へ読み替えない。[評価契約](evaluation_protocol.md)、[現行policy](../configs/phase6/base_parallel_residual_review.json)、[最終採否](../scripts/review_final_base_test.py)。

## 22. 結論: 分かったこと、分からないこと、停止の判断

成立したのは、追跡可能なデータ/Tokenizer/10Mモデル、WSLでの実学習、厳密保存再開、長期job、性能測定、日本語を複数軸で評価する経路である。物語配合等で停止・反復・一貫性が改善した研究条件もあり、すべてが無効だったわけではない。

未達なのは、広い日本語の短い続きを一貫して自然に完結する品質と、最終採用に必要な証拠である。BPBの改善が自由生成の品質へ安定してつながらず、同じ教材の学習延長や新しい教材・目的・構成も固定条件では十分な改善を出せなかった。

データ不足、学習不足、10Mの容量限界のいずれも単独原因として確定していない。6文の記憶成功は汎化の保証ではなく、小型英語物語研究も日本語の保証ではない。現方法で大幅改善を実証できていないことを、10Mの数学的な上限の証明とはしない。

ここでプロジェクトを止める判断は妥当である。停止には「これ以上改善不可能」の証明は必要なく、残る比較に時間を使う価値があるかで判断する。続ける場合も10Mを維持し、既存結果の最終見直しから有望な比較を最大1件に絞る。根拠がなければ学習せず終了し、比較が不採用なら別仮説を自動で続けない。[現在の計画124](124_base_recovery_plan.md)。現時点では一時停止であり、恒久終了や実験再開が決定したと扱わない。

## 23. 復旧・再利用のために保全するもの

最新native2B checkpointはWSL repoの`reports/phase6/base-teacher-decay-2b-20261008/latest.pt`、SHA256 `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442`。元UIの10Bは`reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt`、SHA256 `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`。どちらもGitに重みを加えていない。

Gitにはcode/config/schema/lock/eval/小report/notes/この説明と台帳がある。WSLには重み、optimizer等、metrics、raw/source snapshot、大容量dataがある。固定公開dataset bundleはpilot/Tokenizer用で、学習済み重みや12.23B shardsのbackupではない。WSLのmetadata一覧はファイルの所在を残すもので、全payloadの別媒体backupや内容hash再検証ではない。

2026-10-09に、将来の改善検討用として主要3系列を別の[研究モデル保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)へpublic / manual gatedで保存した。元WebUIの10B、source-order約10.6B、最新teacher-decay2Bのnative重み・Tokenizer・数値学習状態・実装/設定/文書/評価metadataを含む。ユーザー指定によりデータセットとsamplerは含めず、元checkpointの完全な代替や全実験の重みのbackupとはしない。全公開fileのhashと3モデルの実ダウンロードを確認済み。[詳細126](126_model_archive.md)。

再開時はWindows最新local/remote commit、AGENTS、status、計画124、引継ぎ、対象reportのhashと実processを確認する。完了したpilot/2B/10Bを再起動せず、Tokenizerや全corpusを無条件で再処理しない。Pythonは必ずuv管理3.12.7。過去の閾値と失敗を保持したまま再利用する。[保存先・復元コマンド](windows_handoff.md)。

旧状態・ロードマップ・引継ぎ・AGENTSの全原文は[状態履歴](autonomous_status_history_20261008.md)、[ロードマップ履歴](project_roadmap_history_20261008.md)、[引継ぎ履歴](windows_handoff_history_20261008.md)、[AGENTS履歴](agents_history_20261008.md)へ保持する。Phase0〜3の報告・原snapshot・実験条件を今回の説明のために変更していない。

## 24. 後続のChat診断・教材比較（2026-10-10〜13）

元WebUI10Bを未採用Baseとして識別したうえで、ユーザーの明示再開により限定Chat-first SFT128、条件回答教材比較131、first-turn/直接回答を増やす汎化比較133を実行した。Base-firstの通常順序に対する診断例外で、Base採用条件は変更していない。

| 実験 | 実行と結果 | 最終記録 |
|---|---|---|
| 128: 既存雑談の直接SFT | 3周、1,899,555 Assistant教師、全4条件876判断。停止/文法を改善したが内容17/80、文脈2/24で未達 | [129](129_chat_first_sft_execution.md)、[completion](../reports/phase7/chat-first-sft-20261010/completion.json) |
| 131: 雑談C0/条件回答C1 | 各1,899,555教師、14セット3,066判断、固定NLL7点。最終新内容11/15、文脈4/2で両方不合格 | [132](132_chat_improvement_execution.md)、[completion](../reports/phase7/chat-improvement-20261012/completion.json) |
| 133: 改訂教材D1/旧C1対照D0 | D0は一致する旧stateを再利用、新学習0。D1は1,899,562教師。14セット3,066判断/NLL7点、最終新内容16/12・文脈5/3で両方不合格 | [136](136_chat_generalization_results.md)、[completion](../reports/phase7/chat-generalization-20261013/completion.json) |

最新D1の固定TRAIN本文NLL0.001136に対し新DEV4.818918で、教材適合と未知入力への汎化が離れた。回復分岐は提供履歴・内容改善の原条件を満たさず未実行・効果未確認。保持/samplingも合格候補がなく未確認。別padding24確認は速度改善を実測したが数値gate不一致で不採用。非blind Codex判断や同じfamilyの保存点を独立確認に数えず、全raw/理由/失敗/予算を保全した。

最新133の累積GPUは失敗込み35.293分/6時間。科学completionは元10B UIの復帰と実生存を当時確認したが、今回の文書更新で再測定していない。後続Chat重みはWSLに保全し、新しく公開していない。全プロジェクトのGPU/教師量をこの表から合算する認証は行わない。

次の提案は[135](135_chat_problem_solution_plan.md)の意味構造を広げる教材recipe比較を最大1件。今回の範囲は文書・計画のみ、Base/Chat未完成・未採用で停止中。Base復旧を選ぶ場合の[124](124_base_recovery_plan.md)も未再開。容量限界、Base単独原因、学習量不足を断定せず、新条件は別の明示再開と契約を要する。
