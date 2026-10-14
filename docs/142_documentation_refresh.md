# 全ドキュメントの最新化（142）

更新: 2026-10-14 JST。依頼「ドキュメントをすべて最新にして」に対応し、**既存311文書を棚卸しし、現行32文書の本文・実績・運用を更新した。** 日付付き計画・結果88文書と固定台帳・保存証拠191文書の計279文書は原byteを保持し、現在の説明と区別する。[全文書カタログ](document_catalog.md)は既存311＋今回追加2の全313源文書への入口。

今回の範囲は文書の更新・保全・整合確認・ローカルcommit。研究・教材準備・診断・生成評価・GPU学習・TEST利用は再開していない。Base/Chatは未完成・未採用。最新の科学結果は[141](141_chat_lr_comparison_results.md)で不採用、前の3項目の比較・条件分岐・報告・ローカル納品は完了済み。

## 更新した内容

| 対象 | 更新内容 |
|---|---|
| README・AGENTS・状態 | 現依頼を文書のみへ統一。前の結果commit89275a8/納品commit09f338eの完了とモデル品質未達を区別 |
| ロードマップ・チェックリスト・引継ぎ | 139/141の全評価・不採用・保存先・残課題を反映。古い13/28・学習中・旧UI PIDを現行説明から整理 |
| 目的・構成・Tokenizer・データ・学習・環境・評価 | native10,001,152・固定Tokenizer4096、実装済みChat trainer/document sampler/自己履歴評価、教師量・保持・原品質を反映 |
| 研究11〜14・先行例09・調査要約02 | 現在の実装・未達と当時の論文/算術例/候補を分離。外部資料の最新再調査とは呼ばない |
| data/eval/reports README | 最新の原出力・NLL・採否・分岐・事故・保存先を案内。教材実体と小metadata、DEVとTEST、CPU確認と品質を区別 |
| WebUI・Hub引継ぎ・archive説明 | 元10B UIと後続SFTを区別。公開版は2026-10-09の主要3Base系列で、最新SFT重みやdataset/samplerを公開済みにしない |
| 全体記録125・実験検索・固定台帳README | 136→138→141の後続結果への入口を追加。固定revisionの記録数・原キー・失敗・採否は保持 |
| 全文書カタログ | 全源文書を区分・掲載し、古い「次は」「未実施」「継続中」を現在の実行指示として読まない案内を追加 |

約10M予算9.5M〜10.1M、日本語Base目標、各実験の全採否条件を維持した。Phase0〜3の原報告、学習・評価・失敗・採否のJSON、config、数値source、重み・datasetを変更していない。

## 最新結果として反映した事実

低LR候補139は3,646更新/1,899,557 Assistant本文+EOT教師、全28セット/6,132判断/NLL7点×2,634 target。最終新/138/133/元旧の内容20/18/19/15 of80、自己文脈5/5/5/1 of24。新内容差+8.75ポイント、95%CI −1.25〜+18.75で原条件未達。反復・停止の退行、新自己生成Unicode失敗1も保存した。

正式Base保持、sampling、fresh学習seed43、人間blind、fullDEV、封印TEST、採用の全7分岐は候補なしで未実行・passed=false・品質未確認。非blindレビュー・CPU準備・生成seedを独立確認へ読み替えない。Base単独原因・10M容量限界は未確定。

元Chat TEST20行は以前のCPU準備で構文解析した事故があり、未参照の主張は取り消した。学習・GPU評価に使っていないが、将来の有資格Chat最終確認には新しい封印TESTが必要。元Base TESTはこの事故では解析していない。文書更新で新たにdataset/TESTを解析・採点していない。

元UIのPID/boot/start・driver・空き容量は日付付き観測で、現在/将来の生存や容量を保証しない。終了した比較を再起動しない。次のBase復旧は[124](124_base_recovery_plan.md)の未再開の別経路で、合格Baseで通知・停止の境界を維持する。

## 保全と検証の証拠

更新前Git正本は `09f338e3312f884dab84ba20a8467ff5e2011a9e`。全311文書・21,021,337 bytesの原文とSHA256を[baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)へ保存した。コピーは内容hashごとに保存し、同じ原文がある場合も各元pathから出所を追える。保全コピーは新しい源文書や独立実験として数えない。

原文の一部に既存の末尾空白があるため、保全コピーの`originals/`だけGitの末尾空白警告対象から外す。元byteを整形・修正しないための扱いで、現行文書・原品質基準・数値sourceの確認は維持する。

5件のTXTはbuild/dependency/失敗時source snapshotで、説明文書ではない。[分類と原hash](../reports/investigation/documentation-refresh-20261014/non_document_text_files.json)へ記録した。Markdown/RST以外の説明文書を勝手に除外したものではない。

[検証結果](../reports/investigation/documentation-refresh-20261014/verification.json)は、全源文書へのカタログ掲載、32現行文書の更新、279原文の不変、全保全コピーの原hash、現行リンクとWindows/WSL一致、凍結source・科学記録・前回納品commit、文書以外の変更範囲、ローカルGit保存を確認する。文書の検証をモデル品質やGPU実行の証拠へ数えない。

保存後の[commit照合記録](../reports/investigation/documentation-refresh-20261014/commit_verification.json)は、現行文書と原文保全・棚卸し・検証fileの実Git blobを照合し、結果commitを記録する。そのreceiptもローカル保存し最終HEAD・clean worktreeと照合して納品を完了する。

全313源文書から現行文書への見出しリンク14件も照合する。古いロードマップ・引継ぎの見出しを参照する固定報告を変更せず、現行文書の対応箇所へ互換anchorを設けた。[見出し参照の確認](../reports/investigation/documentation-refresh-20261014/inbound_anchor_checks.json)。原報告や固定台帳の数値・採否は不変。

前の保存一覧・completion・納品receiptは当時のGit revision/snapshotの証拠で、今回のliving文書更新に合わせて過去のhashを上書きしない。[前の結果141](141_chat_lr_comparison_results.md)の科学監査時点の「納品が別途必要」は当時の境界で、後続の89275a8/09f338e照合により前の納品は完了済み。

全Pythonは固定uv/Python3.12.7。今回の棚卸し・保全・カタログ・検証は[文書更新スクリプト](../scripts/refresh_project_documents.py)を使用し、学習・推論・dataset parserは呼び出さない。Git正本はWindows、ローカルidentityは`yousan <ka1357amnbpdr@gmail.com>`。push・外部公開は今回の範囲に含めない。
