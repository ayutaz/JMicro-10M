# 現在の状態

最終更新: 2026-10-10 JST。**学習・GPU診断・データ準備は一時停止。Baseは未完成・未採用。モデル保存・公開と前回の文書保存は完了。今回は既存Baseを直接Chat学習して検証する計画の作成まで。**

## 最新のChat-first計画

調査後、ユーザーは「まず現在のモデルをチャットデータで学習し、動作確認する」方針を確認し、計画の作成を依頼した。[計画128](128_chat_first_sft_plan.md)に、元WebUI10Bの重みを保全し、既存TRAIN 2,688会話・40,366応答から1条件・最大3周（1,899,555 Assistant本文+EOT教師tokens）の直接SFTを行う案を記載した。学習前後のDEV80、24familyの自生成履歴、sampling、Base保持を比較し、全実験の累積GPU上限案は6時間。実測batch・最終config凍結は未実施。

これは従来のBase-first順序に対する限定診断の**計画**であり、Base採用の証拠ではない。既存SFT runnerには採用済みBaseのgateがあり、専用の未採用親診断入口が未実装。今回は文書と参照だけを更新し、実装・GPU probe・data準備・学習・新しい推論評価は0。Chat実教師tokensも0。次の実行は明示的な再開待ち。実験を再開した場合も診断結果を報告して停止し、量子化・公開・追加比較へ自動移行しない。Base復旧が必要と判断した後の[計画124](124_base_recovery_plan.md)は保持する。

## 作り直す前の調査

2026-10-10の依頼に基づき、参考のAkebono-10M-chatの公開文書・構造・推論コード・評価要約と、前回の実装・原結果を調べた。[調査127](127_rebuild_investigation.md)、[固定資料・確認結果](../reports/investigation/rebuild_20261010/README.md)。参考モデルも通常会話成立3/40・長会話0/12と報告し、前回のBaseとは用途・教材・評価単位が異なる。構成交換や追加SFTによる解決は実証されていない。

前回は学習基盤が成立した一方、短文の自由生成品質が未達。教材の文脈・終端と生成のずれ、自己生成中の過信した反復を優先して考えるが、単独原因は未確定。調査時点では新比較は未選定。その後に計画128で直接SFTの1条件を提案したが未実行・config未凍結。公開資料取得・静的分析は学習の再開ではなく、10M予算、元品質基準、元UIの保持を継続する。

## モデル保存・公開

ユーザーは将来の改善検討のため、モデルをHugging Faceへpublic / manual gatedで残すよう依頼し、データセットは不要と指定した。[保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)へ元WebUIの10B、source-order約10.6B、最新teacher-decay2Bの3系列を保存した。1,544ファイル・396,038,805 bytes、Hub revision `853d52d2323653331b610249912fbe25615615fc`。全ファイルのサイズ・リモートhash、公開設定、手動承認、匿名重み取得HTTP401を確認済み。[保存内容・読み込み手順126](126_model_archive.md)、[実施report](../reports/publication/model_archive_20261009.json)。

native重み・Tokenizer・数値学習state・実装・設定・文書・評価metadataを保存し、sampler内の文書とデータセットは除外した。元checkpointはWSLに保持する。保存版だけで元学習の厳密再開はできない。新しい学習/GPU評価/量子化は0。この公開時点では以前の詳細文書整理・README・GitHub push依頼は途中停止しており、モデル公開だけでそれらを完了とは扱わなかった。後続のGitHub保存は次節を参照する。

## 詳細記録とGitHub保存

上記の公開後、ユーザーはGitHubへ残りをすべてpushするよう明示した。[全体記録125](125_project_retrospective.md)と[詳細台帳](retrospective/README.md)に初期調査・環境構築・Tokenizer・学習/評価・改善比較・不採用・未達・保存先を整理し、READMEを人間向けの入口として更新した。台帳は整理前revision `2d48062`を固定し、4,947 JSON報告を詳細抽出4,815件と理由付き対象外132件に分ける。後続のモデル公開記録は126とpublication reportから参照する。

2026-10-09の対象は文書・記録の検証、commit、既存remoteへのpushだった。この依頼は現在の計画更新を自動pushする許可ではない。学習/データ処理/研究実行は再開せず、GitHubの反映は当該push後のremote SHAとlocal HEAD一致をもって確認した。既存の科学結果やPhase0〜3の報告・凍結sourceを上書きしない。

[文書保存の確認結果](../reports/publication/documentation_archive_20261009.json): 元報告4,815件のSHA256一致、表示180,595項目・104ページの全記録/原キーとの一致、ローカルfileリンク5,885件を確認した。11,289ファイルの保存一覧は元revisionのGit treeと一致。これは文書の検証であり、新しいGPU評価・独立corpus監査・モデル品質改善の証拠ではない。

## 最新のユーザー方針

2026-10-08: **10Mのサイズを維持することが重要であり、そこをプロジェクトの優位性とする。** 現在10,001,152 parameters、既存の約10M予算（9.5M〜10.1M）を維持する。精度改善のためにモデルを大型化する方針へ切り替えず、大型モデルとの診断比較も別の明示依頼なしに開始しない。10M内で教材・学習方法・パラメータ配分の改善を検討する。日本語Baseの目標や品質基準を勝手に縮小せず、未達は未達として扱う。今回の方針記録で学習・研究実行を再開しない。

## 限界についての判断

現レシピで学習量や設定を追加しても、文章品質の大幅改善は実証できていない。ただし10Mの容量限界に到達した証拠ではない。最新native2B、一貫性23/80の別staged系列、元WebUIを同じ重みとして扱わない。大型化へ切り替えず、再開後は10M内の変更を1つ選び、改善対象と事前の採否条件を明確にする。大幅改善を約束せず、不採用ならその条件を閉じて報告する。

## 現在地と次の行動

| 項目 | 実際の状態 |
|---|---|
| モデル | 10,001,152 parameters。10Mは重みの数 |
| Phase0〜5 | 完了。[Phase4](21_phase4_completion.md)、[Phase5](23_phase5_completion.md)の証拠を保持 |
| Phase6 Base | 元10B学習と追加比較は実施済み。品質・最終確認は未達 |
| 最新の学習 | 教師量に応じてweight decayを調整した条件で累積2,000,000,000教師、212095更新まで完了 |
| 最新の採否 | 全80個別レビューまで完了。不採用、固定条件を閉鎖 |
| 次の実行 | 明示的な再開指示を待つ。計画の更新は実行の再開ではない |
| Chat / SFT / 量子化 | 128に未採用Baseからの限定SFT診断を計画。未実装入口あり、学習0、量子化は範囲外 |
| Git | 科学結果・停止保存は `a26194c`、文書整理は `7ab2c07`、10M維持の固定は `88d4363`。今回の文書更新commitは `git log -1` で確認。自動pushなし |

[最新結果123](123_base_teacher_decay_2b_results.md)、[Chat-first計画128](128_chat_first_sft_plan.md)、[Base復旧計画124](124_base_recovery_plan.md)、[ロードマップ](15_project_roadmap.md)、[引継ぎ](windows_handoff.md)を参照する。限定Chat診断はその結果報告で停止。Base復旧を選ぶ場合は必要な証拠を満たした時点で通知・停止し、後続段階へ自動移行しない。

## 最新の同条件比較

既存2B TRAIN poolを使い、同じモデル・同じ教師列・同じ2B教師予算で比較した。データセット増量の比較ではない。BPBは共通DEV256文書・472,055 bytes・122,343本文tokens。以下の生成評価は各80件、Codexによる非blind採点であり、独立した人間の評価ではない。

| 指標 | 元native2B | 教師量正規化decay2B |
|---|---:|---:|
| BPB ↓ | 1.106386 | 1.090316 |
| 文法2 ↑ | 23 | 22 |
| 関連性2 ↑ | 30 | 16 |
| 一貫性2 ↑ | 3 | 3 |
| 適切完結 ↑ | 7 | 5 |
| EOS停止 ↑ | 20 | 23 |
| 自動反復 ↓ | 27 | 27 |
| Unicode失敗 ↓ | 0 | 1 |

BPBは約1.45%改善し、文書paired差の95%CIは[−0.0209552, −0.0118732]。一貫性差は0件、率のCI[−0.0375, 0.0375]。予測損失の改善が生成品質の改善につながったとはいえない。元絶対6条件は全未達。追加のstrong/cached/historical参照を含む全条件も合格していない。

[完了・採否JSON](../reports/phase6/base_teacher_decay_2b_completion.json)、[全80レビュー](../reports/phase6/base_teacher_decay_2b_candidate_notes.json)、[最終science結果](../reports/phase6/base-teacher-decay-2b-20261008/result.json)を正とする。結果JSONのcontent_pendingはGPU runner終了時点のラベルであり、その後のcompletionで全80レビュー完了を確認できる。旧結果を上書きしない。

## これまでに分かったことと限界

- 同500M教材の2B→5B学習ではBPB1.13859→1.12722に改善した一方、一貫性21→15、適切完結27→24、EOS40→34（各80）。[5B完了記録](../reports/phase6/improved_base_5b_completion.json)。学習量不足は否定できないが、単純延長で文章品質が改善するとは確認できていない。
- 別の約10.6B staged系列は文法65・一貫性23・適切完結26・EOS76・反復2（各80）。最新候補より生成面で良い参考例だが、履歴が違うため同条件対照ではなく、Base採用基準も未達。元WebUIの10Bとも別checkpoint。
- 固定6原文のcapacity controlでは条件付き612/612教師と全6続き・EOSを再現。[証拠](../reports/phase6/base_residual_capacity_control_completion.json)。少数例を学べることは確認できたが、汎化や一般生成の成立を意味しない。
- 実消費TRAIN16対DEV16のfit-gap screenは不成立。これは十分な学習や過学習がないことの証明ではない。[証拠](../reports/phase6/base_residual_train_dev_history_completion.json)。
- 末尾LFでEOS確率が大きく変わる小標本診断は成立したが、DEV16の効果はTRAIN16より弱い。自由生成・意味的反復の解決ではない。[証拠](../reports/phase6/base_residual_boundary_counterfactual_completion.json)。
- 原記事contextを戻すTRAIN16診断では平均本文NLL改善0.11424、CI[0.03722, 0.20033]だが事前screen未達。[証拠](../reports/phase6/base_residual_original_context_completion.json)。原文脈欠落を単独原因と断定しない。

教材量不足、学習量不足、10Mの容量限界のいずれも単独原因として確定していない。数値7失敗、独立した全corpus監査・人間blind評価の未完了も保持する。BPB、選択式正答率、文法、一貫性、停止を一つの「精度」にまとめない。

## データ量と学習量

| 区分 | 保存証拠にある量 | 注意点 |
|---|---:|---|
| 一般Web TRAIN準備 | 12,225,819,077 tokens | 公開データ総量とは別。全件独立監査済みではない |
| 短い物語準備 | 200,000,192 tokens | 他poolへの再利用分を新規量へ二重加算しない |
| 最新比較のaccepted混合pool | 約2B tokens | Web75% / textbook20% / story5%。既存pool |
| 今回のモデルの学習量 | 正確に2B supervised tokens | 先行pilot94,160,195を含む。追加は1,905,839,805 |
| 元UIモデルの学習量 | 10,000,007,168 tokens | 最新2B候補とは別系列。枝の学習量を合算しない |

teacher数、CE入力数、padding込みphysical入力数、本文bytesは別々に保存する。学習tokensとpool量の単純な比を厳密なepoch数とはしない。

## process・重み・UI

科学PID118881 / boot `4052bfc5-3850-44e4-9123-d34a9e19f36e` / start_ticks8215874は終了。Windows worker38176はexit0。追加GPU26,060.094秒、pilot込み27,475.228秒、台帳closed。最終result/checkpointは212095更新・正確に2B教師。job.jsonの最終周期heartbeat212080/1,999,868,016と混同しない。

WSL checkpoint: `/home/aihub_ubuntu/src/japanese-tiny-llm-10m/reports/phase6/base-teacher-decay-2b-20261008/latest.pt`、SHA256 `03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442`。optimizer/scheduler/RNG/sampler等も保存。重みと大型metricsはWSL、可搬評価・レビュー・小記録はGit。

元10B [WebUI](http://127.0.0.1:7860)は復帰。2026-10-09 JSTの文書更新時にPID120460とHTTPの親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290` /10,000,007,168学習tokens/busy=falseを再確認した。これは観測時点の状態であり、将来の稼働保証ではない。最新候補へ差し替えていない。[active記録](../reports/phase6/base_teacher_decay_2b_active_job.json)と[引継ぎ](windows_handoff.md)を参照。

## 保存した履歴

更新前の全原文は[状態履歴20261008](autonomous_status_history_20261008.md)へbyte一致で保存した。Phase0〜3・各凍結report/source/raw・失敗証拠は変更していない。履歴の「次は」「継続」「実行中」は当時の記録であり、現在の再開指示ではない。
