# 2026-10-12 Chat改善調査の証拠

[調査130](../../../docs/130_chat_failure_improvement_investigation.md)の静的な根拠。新しい生成・採点・学習・教材準備は含まない。

- `analysis.json`: 4条件の既存採点とraw packetを再集計。カテゴリ別、同じ最終24 IDの提供/自生成履歴、prompt/生成長、教師量、PAD率、学習中batch lossの教師重み付き平均、3周の原採点の失敗一覧。入力21ファイルのSHA256を保存する。
- `sources.json`: 読んだ公開一次資料のURL・版・適用範囲と限界。論文の全文・重み・追加データセットは保存しない。
- `verification.json`: 文書リンク、既存入力hash、原reviewとの一致、凍結source/config保全、GPU等の未実施範囲の確認。

再集計はPowerShell 7で、project rootから次を実行する。

```powershell
pwsh -NoProfile -File scripts/analyze_chat_first_failures.ps1
```

scriptは保存済みの小さい報告を読み、この調査のanalysis.jsonだけを更新する。元report、TRAIN/DEV教材、checkpointには書き込まず、ネットワーク・Python・GPUを使わない。旧採点を再採点しない。

876は4条件のjudgment数で、各80の無抑制controlは標準80と内容が一致する。自生成24familyは提供履歴のfamilyと重なる。876独立例の成功率、独立人間評価、全corpus監査として使わない。学習中lossは固定checkpointのDEV NLLではない。
