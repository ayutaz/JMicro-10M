# 実験runnerと文書更新の運用

更新: 2026-10-18 JST。

現在の依頼は全ドキュメントの更新・統合・不要文書削除とpushです。以前のSFT試行は完了・不採用で、新しい学習・評価・TEST準備を起動する範囲ではありません。GitHubとモデル公開は完了しており、今回の文書pushは明示的に依頼されています。

実験を再開する場合は[残課題と条件](10_next_steps.md)と[AGENTS](../AGENTS.md)を確認します。旧runnerは当時の契約・source・予算に結び付くため、古い「active」「continue」を今の起動指示に使いません。

WindowsのGit正本とWSLの実行コピーを区別し、Pythonはuv frozenから実行します。長い実行では実PID/boot/start・lock・ログ・completed checkpointを結び付け、観測が途切れたという理由だけで重複起動しません。文書更新では元の数値source/config/重み・データ・原評価を変更しません。

手法の成功、実験の完了、文書作業の完了は別の状態です。今回も全件カバレッジ、現在の説明、履歴保全、リンク、同期、公開pushを確認してから文書goalを完了します。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/codex_automation.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="保存と再開"></a>
<a id="保存と納品"></a>
<a id="実行範囲と完了を区別する"></a>
<a id="実行範囲と目標状態を区別する"></a>
<a id="将来の学習運用"></a>
<a id="目標状態と実行範囲"></a>
<a id="自律runnerの現在の運用"></a>
