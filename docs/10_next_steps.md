# 次回のチェックリスト

最終更新: 2026-10-05 JST。[最新状態](autonomous_status.md)、[最新結果60](60_dataset_expansion_results.md)、[次回計画61](61_condition_preservation_next_plan.md)へ合わせる。現在は文書更新まで。未チェック項目は未実行の提案で、新data/GPU jobを開始する指示ではない。

## 完了済み・再実行しない

- [x] Phase0〜5の環境・Tokenizer・モデル・GPU学習器・保存再開・候補選定。
- [x] 一般Web train12,225,819,077tokens整備と主要Web総10Bの学習・全文評価。独立全件監査未完了は保持。
- [x] 元10Bの日本語Base追加評価と複数の100M/500M/1Bの教材・LR・学習量比較。
- [x] 最新物語200,000,192tokensの準備、同じ親から旧/新各追加1,000,013,824tokensの学習。
- [x] dev256/固定80/意味192/JBLiMP331/JCQA1119と全160個別内容診断、一次35/最終20checks、原gate採否。
- [x] 最新候補不採用・条件付き全文未起動を記録、local commit `afad164`、元final10B UI復帰。

## 今回の文書更新

- [x] 保存review/result/completion/report hashと実process/HTTPを読み取り確認。
- [x] status/README/docs一覧/roadmap/引継ぎ/残作業/自動runnerの現在地を最新へ統一。
- [x] 次回の目的・ゴール・比較条件・予算・終了/失敗時分岐を計画61へ保存。

リンク・数値・元証拠保持・Linux同期とlocal commitの実確認は文書更新監査`reports/phase6/documentation_update_20261005.json`へ記録する。文書のチェック印だけを検証証拠とは扱わない。

## 再開後の段階1: 保存結果の失敗診断

- [ ] 既存160生成と教材40全文を再利用して人物/数量/否定/因果/反復/末尾の問題を分類。
- [ ] 必要時だけ既存trainから32全文を抽出し、selectorで扱う欠陥と扱えない欠陥を確定。
- [ ] 固定dev/testのprefix・正解・生成文を教材へ入れない。

## 再開後の段階2: 教材準備と凍結

- [ ] 同じ取得済み翻訳sourceから従来/改善selector各約20M-tokenのwhole-doc poolを準備。
- [ ] 量・平均長・EOS密度±5%・長さ分布・実source/split/hash/共有範囲を記録。
- [ ] random40全文ずつを個別診断し、改善と候補弱例10/40以下の提案条件を確認。
- [ ] CPU累積1800秒以内。条件不成立なら学習せず報告・停止。
- [ ] 学習config/schema/source/data/参照結果と関連CPU/CUDA再開条件を凍結。

## 再開後の段階3・4: 小予算比較と判断

- [ ] actual process/boot/start ticks/GPU lock確認、元UI停止、必要な実CUDA保存再開確認。
- [ ] 元10Bから各100,007,936tokens、Web80%/short20%、共通scheduleで二枝学習。
- [ ] 同じ日本語診断/本文/生成と全160内容を採点し、原gateと実用条件を判定。
- [ ] 一次GPU累積1200秒以内。全一次条件通過時だけ候補の全文/400/長文を追加1800秒以内で評価。
- [ ] 採否・限界・次案、実state/checkpoint/raw、local commitと元10B UI復帰を確認して停止。

500M/1B追加、20B/50B、Chat、保護test、量子化/公開はこの提案の自動後続ではない。実用Base/Chatの元品質目標とraw失敗を維持する。
