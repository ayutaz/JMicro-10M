# 2026-10-10 作り直し前の調査資料

[調査報告127](../../../docs/127_rebuild_investigation.md)の出典を固定するための小さい公開資料と静的確認結果。

- `reference/`: hisakata-ai/akebono-10m-chat、revision `74b3a1739e6d16883177c6021b3c03a7d517c7fb`から取得した文書・JSON・コード。`hub_metadata.json`は取得時のmain API観測で、配布前metadataと現在公開状態の違いを残す。
- `reference_space/`: 対応Space、revision `aba003926d78f088a010192f51a28ff04e45dfab`の文書・JSON・アプリコード。API観測は別ファイル。
- `evidence.json`: 取得URL、SHA256、公開manifestとの小ファイル照合、config由来のparameter計算、local根拠のSHA、取得制約、実施範囲。
- `verification.json`: 新しい文書・証拠JSONのリンク、source整合性等の確認。モデル能力を測った結果ではない。

静的確認はproject rootで `pwsh -NoProfile -File scripts/verify_rebuild_investigation.ps1` を実行する。取得資料のpublished manifest/hash、parameter算術、文書リンク・JSON・凍結sourceを検証し、evidence/verificationを更新する。ネットワークアクセス・Python・モデル実行は行わない。

参考コードは資料として保存し、実行・project実装への統合はしていない。重み、Tokenizer binary、ONNX/WASM binary、dataset本文は取得していない。原ファイルの記述・著作権表示は保持し、配布元のLICENSEおよびSpaceの第三者noticeを併置する。今回のrepo側の新たなライセンス付与や再公開は行っていない。

公開資料中の「未公開」「残る承認」等は当時の原metadataであり、このprojectの実行指示ではない。参考の能力値は配布者が報告した値で、こちらの独立評価ではない。
