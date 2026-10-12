# 文書と計画の最新化（2026-10-13）

ユーザーの「ドキュメントと計画を最新にして」に対応する文書のみの納品。基準revisionは `ed3aa292087afd9d92bf6b7ea11555e8f8a90163`。学習・教材準備・GPU診断・評価・再採点・UI操作・外部調査・push/公開を行わない。

[baseline](baseline.json)に整理前14文書と15の固定証拠のSHA256を保存した。`history/` のコピーは元bytesのまま保全し、相対リンク・コマンド・PIDは元workspaceに対する当時の記述として読む。現在の実行指示や生存証拠には使わない。

更新した文書はstatus/ロードマップ/引継ぎ/AGENTS/README/文書一覧/チェックリスト/計画135/代替Base計画124/全体記録125/reports入口。現行文書から古い学習中・不足評価の手順を除き、最新の全評価完了・不採用・停止、未実行分岐、未確認の正式品質を統一した。計画135は最新D1対照・候補教材1件、新しい未使用DEV＋既知2回帰、21セット4,599判断の未実行提案に改訂した。元の品質条件、10M、Base-onlyの停止境界は維持する。

[静的確認スクリプト](verify.ps1)は保存済みmetadataと文書を読むだけで、科学runnerを起動しない。履歴bytes、固定証拠、最終数値/分岐、提案と実績の区別、ローカルリンク、変更範囲、WSLへの文書byte同期を確認する。結果は実行後の[verification](verification.json)へ保存する。文書の確認はモデル品質の追加実証ではない。

再確認コマンドはWindowsのrepo rootで以下。文書コピーとこの納品の確認記録だけを更新する。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File reports/investigation/documentation_plan_refresh_20261013/verify.ps1
```
