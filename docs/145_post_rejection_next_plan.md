# 不採用結果を踏まえた次の計画

更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。

DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。

## ここからの順序

| 段階 | 成果物と具体的な進め方 | 進行条件・現在の状態 |
|---|---|---|
| 今回 | 全文書の棚卸し、現行説明更新、原文保全、リンク/Windows-WSL/Git検証 | 文書だけを実行。研究目標は未達のまま解除済み |
| 1. 根拠のある次比較 | 原proposal/trainer/全件notes/結果を対応付け、意味の循環・因果/数量誤りの未回答仮説を最大1件選ぶ | 現時点は未選定・未凍結。既存width/ScaleGrad/RDrop等を未検証と呼ばない |
| 2. 実行前契約と必要実装 | 主要変更、対照、初期化/親、TRAIN/教師/seed/decoder、全品質条件、必要CLIを固定。技術probe・科学比較・独立全pipeline・最終評価の別段階予算を示す | 有限な教師量/時間上限、全既消費の継承、評価保存枠、成功/不採用/中断条件がそろうこと |
| 3. 最小技術gateと科学比較 | 必要なCPU数式/gradient、実CUDA最大shape/finite、全state保存再開、native cache、全計時を確認。新fresh条件で比較し全raw/理由/stream/状態を保存 | CPU準備を品質とせず、閉じたprobeや条件を再起動・救済しない。原採否未達なら固定条件を閉じる |
| 4. 主比較資格 | pilotの実測を根拠に別runの教師量/時間を前向き固定し、絶対/相対/strong/cached/historicalの全guardを判定 | 部分的なEOS/文法/BPB改善だけで進めない。有資格recipeはまだない |
| 5. 独立全pipelineと全文DEV | native永続runner/reviewerの型付き接続・資格証拠を実装し、親の初期化/事前学習から独立fresh seed43を実行。fullDEV・400生成＋長文40を全件確認 | 同学習済みseed42親からsampler/生成乱数を43へ変えるだけでは独立学習にならない |
| 6. 新封印TESTとBase採用 | 最終recipe選定を封印後、新しい別artifact TESTを用意し元最終基準で全件評価。weights/Tokenizer/config/復旧・採否を保存 | 全条件合格でBase完成を通知し停止。Chat/SFT・量子化・公開は別の再開範囲 |

## 既にできたことと実装の残り

DEV専用reader/manifest/生成review接続と全文DEV部品を一から作り直す計画には戻さない。全文集計は元89416文書/42003934本文token/164344743bytesを固定し、本文一度採点・EOS別集計・各ID/token/bytes照合・440 adapterを持つ。36 CPU checksは合成例であり、資格ある実モデルの全文DEVや440内容レビューは未実行。Python open監査の範囲を明記し、native OS隔離を完了扱いにしない。

残りは資格/全pipeline証拠を検証し永続化するnative runner、locks/予算/乱数/モード保全・失敗時停止、実fullDEV/全440の保存・全内容判定、新TEST橋渡し。旧stable+decayへcheckpoint kind/lineageを偽装して渡さない。[読取り修理147](147_evaluation_boundary_repair.md)は当時の修理記録。

## 次仮説の選定で避ける混同

RDropは旧予算で未評価だった状態から、累積上限解除後に初めて科学25Mを実施し不採用になった。今は一律に「品質未評価」と呼ばない。ScaleGradの反復減少も内容一貫性を達成していない。NEFTuneは適合根拠不足で未選定であり、品質失敗の実測ではない。9層256/FFN1040と6層384/FFN832の300M構成比較は既に存在する。

単独原因・全未知手法の不可能・10M限界は確定していない。候補名、CPU fixture数、記録追加、GPU時間の消費自体をBase品質の進捗としない。根拠がない場合は未選定と明記する。

## 品質と資源の契約

DEV80の絶対条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、規定反復≤18、empty/role/Unicode失敗0。相対一貫性差≥8、paired CI95下限>0、BPB/strong/cached/historical保持も必要。最終TEST停止95%は別条件であり、DEVのEOS37/80で代替しない。総trainable9.5M〜10.1M、参照10,001,152を維持し、日本語領域・元品質を勝手に狭めたり下げたりしない。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。

ローカルGPUの累積上限は解除済み。旧technical180/total4800秒は過去の契約で、現在の残り利用可能量ではない。実験ごとの停止条件を後から延長せず、追加予算の根拠は新比較と独立全pipeline/最終評価それぞれに分けて事前に示す。研究を再開した範囲のroutine実装・保存再開を逐一再確認しない。有料cloud・大型化・公開・外部送信は別の指示が必要。

過去の元4.75B→10B枝の7657.678462524 GPU秒は、その当時のFlash/compile実測であり、親作成全体や将来独立native全pipelineの所要時間ではない。速度・教師量・入力量・評価保存を分けて見積もる。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="予算見積り停止の扱い"></a>
<a id="今回の完了条件と次の行動"></a>
<a id="優先0-評価データの境界を修理する"></a>
<a id="再開後の6段階"></a>
<a id="品質と10mの不変条件"></a>
<a id="次の仮説の選び方"></a>
<a id="独立seedと最終評価の実装上の課題"></a>
<a id="現在の到達点"></a>
