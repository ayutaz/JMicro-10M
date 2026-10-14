# 作り直す前の調査: Akebono-10M-chatとJMicro-10Mの比較

調査日: 2026-10-10 JST。今回の依頼は「参考モデルと前回の失敗を徹底的に調べ、原因を分析してから作り直したい」。公開資料・配布コードと、既存の実装・凍結設定・結果・個別notesを読み、原因の確度と再設計の判断材料を整理した。**新しい学習・推論評価・データ準備は行っていない。10M維持、Base完成時に通知して停止する境界は継続する。**

## 1. 調査の結論

前回は学習基盤が動かなかったプロジェクトではなく、**実際に学習できたが、目標とする短い日本語の自由生成に届かなかったプロジェクト**である。保存再開・長期実行・WebUIまで成立した一方、元10Bの固定greedyはEOS停止0/80、反復53/80だった。最新2Bの損失改善も一貫性の改善につながらなかった。[元10B評価](42_base_10b_quality_evaluation.md)、[最新2B結果](123_base_teacher_decay_2b_results.md)。

参考のAkebonoは会話形式を学習した別モデルで、前回のWebUIは文章の続きを出すBaseである。さらにAkebonoの公開成績自体が通常の全会話成立3/40、長会話0/12である。**「Akebonoが完成済みなので同じ構造にすれば解決する」という前提は成り立たない。** END終了168/168と、会話内容の成立は別の結果である。[公開評価要約](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/EVALUATION_SUMMARY.json)。

最も支持される説明は、教材の文章・文脈・終端と求める生成のずれ、および自己生成中に反復へ入り、その続きを高確率で出す挙動である。ただし、これらの寄与を一つずつ分離した汎化改善の証拠は不足している。データ不足、学習不足、容量限界のどれか一つへ原因を確定していない。

作り直しでは、元モデルを保存したまま実験・推論・評価の入口を整理し、変更の根拠と比較単位を揃える。10B再学習、語彙12kへの交換、SFT追加を即時に選ぶ根拠はない。**今回、新しい科学比較は選定・凍結していない。** 次の介入は[計画124](124_base_recovery_plan.md)に従い最大1件に絞り、根拠不足なら開始しない。

## 2. 調べた範囲と再現可能性

| 対象 | 固定した版・資料 | 今回の確認 |
|---|---|---|
| Windows正本 | 調査開始時HEAD `8f50c47` | status、roadmap、handoff、124/125/126、Phase5、元10B、根本原因診断、教材増量、最新2B、既存意思決定表と関連コード |
| 参考モデル | `hisakata-ai/akebono-10m-chat` revision `74b3a1739e6d16883177c6021b3c03a7d517c7fb` | README/config/runtime、モデル・Tokenizer・推論コード、評価要約、配布検証、manifest/hash、ライセンス |
| 参考Space | revision `aba003926d78f088a010192f51a28ff04e45dfab` | README/model card/runtime、ブラウザー推論・Worker・UIコード、manifest/hash、ライセンス |
| 外部一次資料 | TinyStories、MobileLLM、Chinchilla、Unlikelihood、Neural Text Degeneration、HF chat templates、2件のdataset card | 主張の適用範囲と、本プロジェクトの既存結果との対応 |

取得した公開の小ファイルは[調査資料](../reports/investigation/rebuild_20261010/README.md)、取得版・SHA256・確認結果は[機械可読証拠](../reports/investigation/rebuild_20261010/evidence.json)に保存する。公開コードは資料として保管し、実行・本体への取り込みはしていない。モデル重み・Tokenizer binary・訓練データ・ONNX/WASM binaryは取得していない。

webの取得経路では参考モデルを開けなかったが、PowerShellの直接HTTPではHub APIとrevision固定URLから取得できた。GitHubの匿名API/pageは404、既存gh認証は401 `Bad credentials`。private・移動・権限等の理由は判別できず、「repoが存在しない」とは判断しない。GitHubの最新内容・issue・remote HEADは今回確認できていない。前回の解析はユーザーが指定したWindowsのlocal checkoutと保存記録を正本として行った。

全4,947 JSONを今回再監査したわけではない。全体記録125と詳細台帳を入口に、原因判断に関係する原結果・実装を読んだ。独立全corpus監査、人間blind採点、未公開の参考モデルの学習履歴は確認済みとして扱わない。個別の起動例外やユーザーの失敗ログは未提示であり、今回の主対象は保存記録に最も明確な生成品質の失敗である。

## 3. Akebonoから実際に分かること

### 3.1 配布物と学習履歴

配布物は独自PyTorchモデル、SentencePiece、CPU FP32推論一式であり、Transformersの`AutoModel.from_pretrained`互換ではない。configでは9,965,824 parameters。重み50テンソルの元checkpointとの完全一致は配布者による検証報告であり、今回こちらで重みを読み直した結果ではない。[model card](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/README.md)、[配布検証](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/VERIFICATION.json)。

公開cardによる祖先の教材にはSimpleStories-JA、magpie-sft、Wikipedia、RealPersonaChat、ローカル教師出力、作成された架空会話、本人提供の私的会話等がある。v19はNEW320の1巡目・50更新のcheckpointと説明される。しかしこれは最後の追加段階であり、**総学習量50更新、訓練データ320件だけで完成したとは読めない**。祖先の総教師量・epoch・配合・LR・optimizer・split・sampling履歴の完全な再現レシピは配布されていない。[model card](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/README.md)。

### 3.2 公開評価の限界

| 項目 | 公開報告値 | 読み取れる範囲 |
|---|---:|---|
| 通常の全会話成立 | 3/40 | 限定された親作業の比較値。一般会話成功率ではない |
| 長会話の全会話成立 | 0/12 | 長い履歴保持が成立した証拠はない |
| END終了 | 168/168 | 終端形式は安定したが、内容正解を意味しない |
| 追加SFT LOWE1 / LOWE2 | 通常成立1/40 / 2/40 | 公開説明では正答改善なし、元v19維持 |
| 配布CPU生成一致 | 3出力 | 元demoとの同一性・可搬性の確認。能力評価ではない |

分母・採点基準・会話長・独立性がJMicroのDEV80と違うため、3/40と3/80を比較して優劣を出さない。評価要約自身もpublishableな方法説明が必要と記載している。[評価要約](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/EVALUATION_SUMMARY.json)。

### 3.3 参考にする価値がある実装

推論packageはweight/TokenizerのSHAを確認し、スクリプトの所在からファイルを読み、起動時のcwdに依存しない。履歴は生成したtoken IDsで保持する。greedy、END/EOS、token/文字/context上限を区別し、反復ペナルティや定型応答への置換はない。長すぎる会話は履歴を変えず拒否する。[chat.py](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/chat.py)。

関連Spaceは無料static配信で、ブラウザーCPU/WASMによるFP32 ONNX推論を使う。モデルページのCPU CLIとSpaceのONNX実行は別経路である。約60MBの初回読込、512tokenの履歴制限、停止理由表示等はSpaceの説明値。今回ブラウザー実生成や速度測定をしていない。[Space README](https://huggingface.co/spaces/hisakata-ai/akebono-10m-chat/blob/aba003926d78f088a010192f51a28ff04e45dfab/README.md)。

参考モデルのREADME/manifestには「公開していない」という配布前metadataが残る一方、調査時のHub APIではpublic・ungatedであった。現在の公開状態はAPI、品質・学習履歴は各原報告の範囲で読む。この不一致を重み破損の証拠にはしない。

## 4. 同じ10Mでも構成は違う

| 項目 | JMicro現在の凍結reference | Akebono配布config |
|---|---:|---:|
| 総trainable parameters | 10,001,152 | 9,965,824 |
| 語彙 | 4,096 | 12,288 |
| hidden | 256 | 256 |
| 層数 | 13 | 8 |
| FFN幅 | 640 | 768 |
| Attention | GQA 4Q/2KV | MHA 4Q/4KV |
| context | 1024 | 512 |
| Norm / 活性化 | RMSNorm / SwiGLU | RMSNorm / SwiGLU |
| RoPE layout | half-split | even/odd interleaved |
| tied embedding | あり | あり |
| Norm epsilon | 1e-6 | 1e-5 |
| 初期化 | linear/embedding std0.02 | std0.02、attention output/FFN downは0.02/√(2×layers) |
| 配布推論 | native、GPU UIはBF16/math＋KV cache | CPU FP32、各stepで全prefixを再計算 |

JMicroは[実config](../reports/phase6/base_model.json)と[凍結モデル実装](../src/jmicro/model.py)、Akebonoは[config](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/config.json)と[実装](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/modeling_japanesechat10m.py)から確認した。AkebonoのPython dataclassの既定値は配布configと異なり、実際の配布モデルはconfig.jsonを渡して構築される。既定値だけを読んで構成を推定しない。

行列shapeから計算した内訳は次のとおり。今回の計算はconfigとsourceによる算術確認で、新しいモデル生成・学習ではない。

| 部分 | JMicro | Akebono |
|---|---:|---:|
| shared embedding | 1,048,576（約10.5%） | 3,145,728（約31.6%） |
| Attentionの全行列 | 2,555,904 | 2,097,152 |
| FFNの全行列 | 6,389,760 | 4,718,592 |
| Norm | 6,912 | 4,352 |
| 合計 | 10,001,152 | 9,965,824 |

JMicroの式は`4096×256 + 13×(196608 + 491520 + 512) + 256`。Akebonoは`12288×256 + 8×(262144 + 589824 + 512) + 256`。Akebonoは語彙へ約2.10M多く使い、Transformer部分を減らしている。総sizeだけでは同等の機能容量や速度を意味しない。

語彙の増加で日本語のsequenceを短くできる可能性はあるが、圧縮率はTokenizerの訓練分布にも依存する。前回の同32文では4k→8kでbody tokensが2042→1793へ約12.2%減り、codecは両方losslessだった。Phase5の同token予算では4kが良く、近いbytes予算では8kが僅かに良かった。語彙・層数・FFN・schedule位置が交絡しており、「4kが失敗原因」「12kなら解決」とは言えない。[Phase5](23_phase5_completion.md)、[codec診断](72_root_cause_diagnostic_results.md)。

語彙12k、8層、MHA、context512、初期化を一緒に変えると、仮に良くなっても原因を特定できない。元Tokenizerを再学習したり、凍結model.pyを差し替える案は今回採用しない。構成変更を行うなら、9.5M〜10.1M内で別proposalと対照が必要である。

## 5. 会話形式・codec・lossの違い

JMicroのBase教師はBOS/body/EOSである。Tokenizerにはrole/EOTが予約され、Assistant本文＋EOT-only SFTを作るコードもあるが、**予約tokenやSFT準備が存在することはChat学習済みという意味ではない**。[Tokenizer](../src/jmicro/tokenizer.py)、[WebUI説明](43_local_webui.md)、[後続段階の実態](125_project_retrospective.md)。

Akebonoの推論はBOS/SYSTEM/body/END、USER/body/END、ASSISTANT/body/ENDを使う。ID0〜7の役割は概ね対応するが、JMicroのID7は`<|eot|>`、Akebonoは`<|end|>`。AkebonoにはさらにID8のnewlineがある。JMicroは改行などの保護文字をUTF-8 byte piecesへ写す。JMicroのID8以降をAkebonoの語彙と対応付けずにコピーできない。[Akebono Tokenizer](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/tokenizer.py)。

Akebonoのforward(labels=...)は与えられたlabelsをそのままCEへ渡す。JMicroのforward(labels=...)は内部で一位置shiftするが、実Trainerは既にshiftしたyをlogitsに直接CEで計算する。**片方のTrainerへもう片方のmodelをそのまま入れると、shiftの契約を取り違える危険がある。現在のJMicroで二重shiftが起きたという証拠はない。** 過去の実32件診断で入力/教師/マスクを確認している。[診断72](72_root_cause_diagnostic_results.md)、[Trainer](../src/jmicro/training.py)。

また、RoPE layout、QKV行列分割、layer/FFN shape、語彙の意味が違うため、同じhidden256でも互換checkpointではない。AutoModel互換やTokenizerの交換を前提にした再構築は避け、config/codec/weightの組を一つのartifactとして同定する。

## 6. 前回の失敗を系列別に読む

| 系列 | 実際の学習量・評価範囲 | 主な観察 | 判断 |
|---|---|---|---|
| 元Web10B | input10,000,007,168、教師9,978,838,479。全文DEVと400生成 | 全文BPB0.954018、固定EOS0/80、反復53/80、全400Unicode0 | Webの予測は改善、自然な短文生成は未達 |
| source-order staged | input10,600,546,304、教師10,577,786,961。DEV256/80内容 | 文法65、一貫性23、適切完結26、EOS76、反復2（各80） | 生成は改善した参考例。絶対一貫性/完結とWeb保持等で不採用 |
| fresh native sequential2B | 正確に2B教師。DEV256/80内容 | BPB1.106386、文法23、一貫性3、適切完結7、EOS20、反復27 | 最新decayの同条件対照。stagedとは履歴が違う |
| teacher-normalized decay2B | 正確に2B教師。DEV256/80内容 | BPB1.090316、文法22、一貫性3、適切完結5、EOS23、反復27、Unicode1 | BPB約1.45%改善。全固定条件未達、不採用・closed |

量の正本は[保存版126](126_model_archive.md)、品質は[元10B](42_base_10b_quality_evaluation.md)、[staged完了](../reports/phase6/source_order_condition_comparison_completion.json)、[既存意思決定表](../reports/phase6/base_learning_decision_table_20261008.json)、[最新completion](../reports/phase6/base_teacher_decay_2b_completion.json)。

原10Bの全文DEVと、後続256文書のBPBは分母が違う。表の縦方向を単純な学習曲線にしない。各枝のtokensも合算しない。stagedのほうが最新2Bより生成が良いという記述的観察は可能だが、「decayのせいで23→3に落ちた」という因果比較ではない。

## 7. 原因候補と、確定できる範囲

| 原因候補 | 支持する証拠 | 反証・限界 | 現在の判断 |
|---|---|---|---|
| BaseをChatとして期待した | 元UIは続きを生成するBase、Chat未学習。参考はrole付き会話 | Base自身の反復・不完結はこの違いだけでは説明できない | 用途の不一致は明確。全失敗の単独原因ではない |
| 教材の文脈・終端と短文生成のずれ | Web原文にメニュー/見出し/引用/未完終端、正解履歴と自由生成でEOSが異なる | 全corpus不良率未推定、source/長さ/配合が交絡 | 優先度高。因果と汎化改善は未確定 |
| 自己生成で反復を過信 | loop地点の選択確率99.66%や99.86%、EOSは極小 | 正解から別の自然な続きを出すこと自体は誤りでない | 現象を直接観察。解決する介入は未採用 |
| 文脈連結・切断への依存 | Phase5 packed overfitは単独文書再現2%、文書単位へ変えて合格 | 後続document-localでも生成未達、原context診断もscreen未達 | 一部で確認済み。packingだけで全体を説明できない |
| EOS実装バグ/二重shift | 現行コードだけを見れば疑いやすい | 実教師確認、条件例EOS、6文記憶、独立reference比較 | 主原因として支持されない |
| BF16/Flash/compile数値差 | 固定数値7checksの失敗を保存 | FP32でもoriginal/mixedの主な停止・反復件数は同じ | 未解決の技術問題。全品質問題の主因とは未実証 |
| 4k語彙/GQA/層配分 | 参考と配分が異なる、4kはtoken圧縮で不利 | 4k/8kには既存実比較、codec破壊は未確認、参考品質も低い | 未確定。構成を丸ごと交換する根拠なし |
| optimizer/更新単位 | nativeは平均約9416教師/update、packedは32768入力/update。betas等も違う | accumulation/decay/各optimizerの固定比較は不採用 | 実差はあるが、単独原因は未確定 |
| データ/学習量不足 | 一部学習曲線で損失や生成改善 | 延長で一貫性が下がる例、増量がsource/長さ/EOSを変える | 否定も確定もできない。無条件延長は支持されない |
| 10Mの容量限界 | 広い日本語生成・条件保持が未達 | train100件や6原文の記憶、staged改善、別10Mの会話終端学習 | 一般目標の達成可能性は未証明。上限到達の証明ではない |

根拠は[Phase5](23_phase5_completion.md)、[根本原因72](72_root_cause_diagnostic_results.md)、[capacity control](../reports/phase6/base_residual_capacity_control_completion.json)、[TRAIN/DEV診断](../reports/phase6/base_residual_train_dev_history_completion.json)、[LF診断](../reports/phase6/base_residual_boundary_counterfactual_completion.json)、[原context診断](../reports/phase6/base_residual_original_context_completion.json)、[更新単位の原台帳](../reports/phase6/base_learning_decision_table_20261008.json)。

## 8. 教材について、量と意味を分ける

WebのEOSは取得文書の終端で、必ずしも意味の完結ではない。既存の原文確認には、数値の途中、見出し、続くという予告、本文後の別記事見出し群で終わる例がある。文章の次token予測として学べても、短い書き出しから目的に沿って締める教師とは一致しない。これはsampleの観察で、Web全体の不良率の推定ではない。[診断72](72_root_cause_diagnostic_results.md)。

日本語物語も自動的に正しい教材ではない。既存レビューでは否定反転、対象の置換、因果欠落が見つかっている。60M→200M比較では、平均body長88.462→170.129、実物語EOS教師が約52.55%へ減った。一貫性15→9、EOS34→25（各80）となったが、source/意味品質/長さ/EOS密度が同時に変わったので「増量の効果」だけには帰せない。[増量結果60](60_dataset_expansion_results.md)。

参考モデルのSimpleStories-JAはgpt-4o-miniによる合成物語で、topic/theme等のmetadataがある。magpie-sftはcalm3でinstruction、Qwen2.5-32Bでresponseを生成した公開教材である。両方とも参考の祖先へ使われたというcardの記述から、実配合・フィルタ・消費量は復元できない。前回もSimpleStoriesを使用しており、そのdataset名を新たな未試行の解決策にはしない。[SimpleStories card](https://huggingface.co/datasets/SimpleStories/SimpleStories-JA)、[magpie card](https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0)。

再開後に教材条件を提案するなら、source名や総tokensだけでなく、原記事と抽出単位、途中切断、完結位置、否定/指示対象/因果、長さ、EOS密度、文脈、消費教師数を記録する。train-onlyの変更と評価splitを分離し、既存audit/accepted poolを再利用する。**今回は新しいpool作成や全corpus再走査をしていない。**

## 9. 学習と最適化について

同じ「LR0.002、AdamW、10M」でも学習条件は一致しない。元packed Trainerはdecayとno-decayを分け、betas=(0.9,0.95)、fused AdamW、update位置のWSDを使う。後続nativeは全parameter一group、betas=(0.9,0.999)のAdamW、教師位置cosine、document-localの教師を使う。平均教師数やpadding比も違う。[元Trainer](../src/jmicro/training.py)、[native Trainer](../scripts/base_kv_allocation_trainer.py)、[実更新台帳](../reports/phase6/base_learning_decision_table_20261008.json)。

これらの差はstagedとfreshの比較を交絡させる。全parameter decayやbeta2を「バグ」と決めつけない。nativeの少ない教師数/updateに対するdecay exposureは実際に比較され、最新2Bまで不採用だった。4microbatchの加重accumulationも94.16Mで不採用。今回この条件を新しい案として再起動しない。[蓄積結果116](116_base_gradient_accumulation_pilot_results.md)、[decay結果123](123_base_teacher_decay_2b_results.md)。

モデルの容量controlでは固定prefix以降612/612教師、全6suffix/EOSの再現に成功した。これは現在の構成と学習経路が少数例を学べる証拠で、一般生成を学ぶための教材・計算量が十分という証拠ではない。fit-gap screen不成立も「過学習なし」「十分学習済み」の証明にはならない。

## 10. 評価の問題は、学習の問題と別に直す

前回は多数の比較で損失が下がったが生成が改善しなかった。Phase5の候補選定でもBPB/速度の優位を選ぶ一方、EOS0/80・sampling Unicode2/240を未達として残した。これは100M候補選定と最終Base採用が別だからであり、採用済み良質モデルの証拠ではない。[Phase5](23_phase5_completion.md)。

後続ではBPBが良い条件を検出しやすくても、生成改善を検出するscreenとしては弱かった場面がある。teacher-decay短期screenはBPB改善と生成非退行で通ったが、一貫性は2→2、最終2Bも3→3だった。探索screenと最終品質gateを分け、次の比較では**狙う生成失敗の改善が見えたときだけ**本比較を提案する。[pilot120](120_base_teacher_decay_pilot_results.md)、[最終123](123_base_teacher_decay_2b_results.md)。

DEV80を繰り返したAI非blind採点であり、学習seedは主に一つ。document-paired CIは文書sampleの不確実性で、学習seedの再現性を保証しない。独立学習seed43、fullDEV、400＋長文40、protectedTEST、実人間blindの状態を別々に記録する。今回再採点やTEST閲覧をしていない。

64新tokensはTokenizer間で同じ文字量ではなく、END・EOSと内容的な完結も異なる。将来の比較では原固定suiteを保ちつつ、共通本文bytes/BPBと生成のdecoded bytes/文字数/context占有/停止理由を併記する。短い出力だけにして見かけの反復を減らしたり、raw失敗を表示補正で消して合格にしたりしない。[評価契約](evaluation_protocol.md)、[日本語評価監査44](44_japanese_base_evaluation_audit.md)。

## 11. 外部研究から採用できる教訓と適用限界

| 一次資料 | 研究の対象と教訓 | この10M日本語への適用 |
|---|---|---|
| [TinyStories](https://arxiv.org/abs/2305.07759) | 語彙・内容を制御した英語合成物語で10M未満でも一貫した生成を報告 | 10Mが常に不可能とは言えない。幅広い日本語や会話の成功保証ではなく、目標を物語限定へ変更しない |
| [MobileLLM](https://arxiv.org/abs/2402.14905) | 主な比較125M/350M。deep-thin・embedding共有・GQA・sharing | 構成配分を検討する根拠。10Mで13層/GQAが最適という証明ではない。sharingは本projectでも不採用比較済み |
| [Chinchilla](https://arxiv.org/abs/2203.15556) | 70M〜16B級の計算予算下でsizeと学習量を比較 | 10Mの「十分なtokens」を20×parameter等だけで断定しない。固定sizeで欲しい生成品質を測る必要がある |
| [Unlikelihood](https://arxiv.org/abs/1908.04319) | likelihoodと反復の関係、反復確率を下げる目的を検討 | 現象の説明には有用。既存sequence UL/低係数ULの不採用を無視してそのまま再提案しない |
| [Neural Text Degeneration](https://arxiv.org/abs/1904.09751) | 同じ重みでもdecode法が反復・多様性を変える | samplingや反復penaltyは推論policy。rawモデル品質の証拠と分ける。前回samplingも失敗を残した |
| [HF chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating) | 会話role/control tokensはモデルの訓練形式と一致させる | Baseに任意のChat templateを付けてもChat学習を代替しない |

研究名の列挙を改善の証拠にしない。今回の主な根拠は対象projectの実際の失敗と比較結果である。

## 12. 環境・可搬性に関して分かったこと

元環境はWSL2・RTX4090で学習・WebUIが成立したという保存証拠がある。今回GPU状態やUI livenessを再確認していないため、現在も起動しているとは保証しない。参考のCPU配布検証も既存Windows依存を用い、空環境への新規installは未検証と明記される。参考の依存を移植すればこちらのGPU学習が直る、という根拠はない。[引継ぎ](windows_handoff.md)、[参考verification](https://huggingface.co/hisakata-ai/akebono-10m-chat/blob/74b3a1739e6d16883177c6021b3c03a7d517c7fb/VERIFICATION.json)。

静的に確認できた可搬性の課題は次のとおり。

- [start_webui.ps1](../scripts/start_webui.ps1)はdistribution `Ubuntu`、Linux user `aihub_ubuntu`、Linux repoとuvのpathを固定している。別環境へcloneして起動するだけでは同じpathにならない。実際の今回の起動失敗原因かはログがないため未確定。
- Gitはcode/docsで、checkpoint・大容量dataはGit外。Hub archiveもmanual approvalが必要で、samplerとdatasetを除く。cloneや公開重み取得だけで厳密再開が成立するとは案内しない。[archive126](126_model_archive.md)。
- WSL package3.x、distributionのWSL2、Windows driver、Linux CUDA runtime、Python/uv/extrasは別の項目。historical versionを現在の環境観測へ読み替えない。
- このprojectの全Pythonは`uv run --frozen`、Python3.12.7、依存変更は`uv add`。参考のsystem Python/pip手順をこちらの手順へそのままコピーしない。今回依存sync/installや環境benchmarkはしていない。

将来runtime修復が必要になったときは、実際の例外・uv log・distribution/path・artifact取得可否を原因に対応付ける。生成品質の失敗とinstall失敗を混ぜてアーキテクチャ再設計へ進まない。

## 13. 再利用するものと、やり直さないもの

| 対象 | 方針 | 理由 |
|---|---|---|
| 元model/Tokenizer/3系列checkpoint | 凍結してreferenceを残す | 現10,001,152予算と失敗/改善の比較根拠 |
| 保存再開・sampler/digest/counters・GPU lock/ledger | 再利用する | 実CUDAの厳密再開と長期実行が成立済み |
| accepted shards/既存評価/raw・全notes | 再利用する | 全corpus再構築や旧GPU再評価は新しい原因証拠にならない |
| 実験入口とartifactの型 | 次回実装で整理する | 多数の継承Trainerと旧/new checkpoint型の違いで、recipe混同・接続誤りが起きやすい |
| Base/Chat/推論packageの表示 | 学習状態と一致させる | 後続コード・予約token・UIを能力完成と誤解しない |
| 既存不採用条件 | 元採否を保持して閉じる | 少し係数を変えた救済や、条件名を変えた再試行を防ぐ |

特にsequence UL、native teacher/KD・on-policy/hint/preference、label smoothing、confidence penalty、next-two/middle supervision、Muon/AdEMAMix/SAM、Layer Sharing、parallel residual、context/FFN/KV allocation、初期化、accumulation、teacher-decayには既存比較がある。方式一般の無効性ではなく、**各固定条件が未達・不採用だった**と読む。[全体記録125](125_project_retrospective.md)、[目的台帳](retrospective/04_objectives.md)、[構成台帳](retrospective/05_architecture.md)。

ReLU²は実装・CUDA gateが成立したが、固定予算を速度見積もりが超え、本比較は未実行でclosed。品質が劣る結果として数えない。LF・原contextの診断成立/未達も、自由生成を解決した証拠にはしない。

## 14. 作り直す場合の具体的な順序

これは次回の実装・実行に向けた提案で、今回の開始commandではない。既存品質基準、10M予算、Base-only境界を変えない。

### 段階A: 再構築の仕様を一つにする

現在のreferenceのconfig/codec/model/checkpoint/教師単位を明示し、model・loader・trainer・eval・local inferenceの小さな入口を設計する。科学sourceは別pathで維持する。元Web10B、staged、fresh2Bの型とlineageを明示し、都合のよい重みを対照へ混ぜない。

成果物は、単一のrecipe schema、artifact manifest、checkpoint型、コマンド一覧、既存コードとの対応表。CLI/CPU contractができても、新学習や品質向上ができたとは記録しない。架構をAkebonoへ交換する判断はここで自動的に行わない。

### 段階B: 次の問いを一つに絞る

優先する問いは「原文から短い続きへ展開・完結することを学ぶ教師分布と、自由生成の失敗の対応」。ただし、教材配合・文脈・終端を変更する過去比較が多数ある。次proposalには、どの例のどの失敗、どの既存比較の何が未回答かを列挙し、対照・主要変更1つ・同教師予算・同TRAIN分離・終了条件を定義する。

今回の参考資料だけでは、新しい有効な配合比率・目的係数・学習量は決定できない。したがって新介入は未選定とする。参考の非公開学習recipeを推測で埋めず、既存資料で問いを定義できなければ「根拠不足」として学習しない。既存6文・TRAIN/DEV32文・LF・原contextの再診断も既定作業にしない。

### 段階C: 必要な実装と検証を先に完成する

新条件が定義できた場合だけ、専用runner/reviewer、実パラメータ計数、x/y一位置shift、PAD/BOS/役割/EOS教師mask、document境界、全state再開、教師消費digest、学習/eval RNG隔離を接続する。nativeの独立seed/fullDEV/TEST型接続は未完成なので、旧stable+decay専用runnerへ偽装して渡さない。[準備122](122_base_native_seed_confirmation_preparation.md)。

初回はsimpleな正しい経路をreferenceとして保持し、高速化と品質介入を同時に変えない。新環境で必要な確認だけ行い、Phase0〜3や旧benchmarksを全部再実行しない。

### 段階D: 上限を固定した対照比較

[計画124](124_base_recovery_plan.md)の各25M〜100M教師という提案範囲から、検出したい差に根拠を付けて一つの予算を選ぶ。小予算で比較できないなら先にその理由を示す。GPU上限は実際のcondition/shape/backendの速度と固定eval時間から決める。元packedの約694k input tokens/sをnative教師速度へ流用しない。

探索screenはBPB低下だけで通さず、狙った一貫性・適切完結・反復等の改善と保持を事前に定義する。全80 raw内容とpaired差、各Unicode/role/empty失敗を確認する。不採用ならその一巡を閉じ、seed/係数/予算を変えて自動救済しない。

### 段階E: 最終Base確認と停止

有望条件だけ独立fresh学習seed43、fullDEV、400生成＋長文40、選定封印後のprotectedTESTへ進む。現DEV80の絶対screenは文法≥56、一貫性≥27、適切完結≥27、EOS≥37、反復≤18、文字/role/empty0。指定された相対差・CI・BPB保持・historical等の全guardも必要。最終TESTの停止95%等をDEVのEOS37/80で代用しない。

全条件を満たしたBaseができた時点で通知して停止する。会話学習、CPU/WASM配布、量子化は別の後続段階である。Akebonoの使いやすい配布方式は将来の参考に残すが、この調査から自動的にChat/配布/公開へ進まない。

## 15. 調査の完了と残った不確実性

今回完了したのは、公開参考実装の版固定取得、構造/codec/runtime/評価/由来の比較、前回の代表的な原結果と実装の照合、原因の確度と再構築順序の文書化である。根拠のhash・config算術・新文書のリンクを確認し、凍結model.pyのSHA256 `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83`を維持する。

未確認なのは、ユーザーの個別失敗ログ、GitHub remoteの現状態、参考の完全な学習recipe、同条件の独立モデル比較、今回の実環境liveness、全corpus独立監査、独立人間評価、10Mの目標品質を満たす新recipeである。これらを推測で埋めない。新しいGPU/CPU推論・診断学習、データ準備、Chat/SFT、量子化、外部公開は0。

**実務上の判断は、学習基盤を捨てて全部ゼロから書き直すことより、成立済みの基盤を再利用して教師・生成・採否の契約を揃え、品質の変更を一件ずつ検証することである。** 現レシピの未達は明確だが、Akebonoへの構造交換や追加SFTで解決する証拠はない。調査の完了はBaseの完成でも、学習再開でもない。
