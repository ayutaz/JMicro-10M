# 研究の経過と実証できたこと

更新: 2026-10-18 JST。

独自Tokenizerと約10Mモデルを構築し、Baseの事前学習、複数の品質改善比較、会話SFT、実会話の確認まで実行しました。技術基盤は成立しましたが、実用的な一般会話と正式Base/Chat採用は未達です。

## 主な経過

| 段階 | 実際に確認したこと | 結果への入口 |
|---|---|---|
| Tokenizer・モデル・export | 保護byte、KV cache、保存再開、変換の基盤 | [Phase2](18_phase2_completion.md) / [Phase3](19_phase3_completion.md) |
| 元Base 10B | 実学習と同条件品質比較 | [学習41](41_base_10b_training.md) / [評価42](42_base_10b_quality_evaluation.md) |
| Baseの後続比較 | データ・目的関数・構成・EOS等を比較、資格あるrecipeは未達 | [実験検索](base_experiment_lookup.md) |
| 会話教材SFT | 公開会話・回答教材・著作対話を比較 | [結果150](150_chat_natural_sft_results.md) / [結果156](156_answer_curriculum_results.md) |
| 入力配置の比較 | 全3,466主応答・実ブラウザーも確認、候補不採用 | [結果162](162_chat_input_structure_sft_results.md) |
| 二情報回答の診断 | 教材64全文再現、未知値30/32、構造15/32、一般会話退行 | [結果165](165_chat_two_attribute_diagnosis_results.md) |
| 公開 | Base 3系列・最新SFTは申請不要、コードはApache-2.0 | [公開166](166_public_models_and_oss.md) |

## 結果の解釈

損失低下、EOS増加、表面反復の減少、短い挨拶の成功だけでは、意味の一貫性や継続会話を保証できません。最新SFTも小集合の学習と未知値への限定的な転用は確認しましたが、質問構造の変更や自分の履歴への転用が弱く、一般会話の内容成立が減りました。

評価は主に固定DEVのCodex非blind判定です。独立人手評価や10M全般の限界の証明ではありません。次の研究を始めるなら、閉じた条件の延長でなく、根拠ある未回答仮説と新しい前向き契約が必要です。[残課題](10_next_steps.md)。

## 原記録を読む

初期からの長い経過、当時の判断・数値・失敗は更新前の本文と[固定台帳](retrospective/README.md)に保持しています。古い台帳へ後続runを混ぜて件数や総GPU秒を上書きしません。全ての文書と保存原文は[カタログ](document_catalog.md)からたどれます。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/125_project_retrospective.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="1-目的と最後まで変えなかった条件"></a>
<a id="10-主系列5b10bとeos反復文字末尾"></a>
<a id="11-評価を日本語base向けに拡張した理由と結果"></a>
<a id="12-教材配合量学習量を増やした比較"></a>
<a id="13-教材選別供給の失敗も保存した"></a>
<a id="14-条件保持記憶packing汎化の切り分け"></a>
<a id="15-実装や数値誤差が主原因かを調べた"></a>
<a id="16-学習目的teacher最適化の比較"></a>
<a id="17-10m内の構成parameter配分反復計算"></a>
<a id="18-直近のcapacitytraindevlf原文脈診断"></a>
<a id="19-最新の教師量正規化decay-短期改善から2b不採用まで"></a>
<a id="2-記録の範囲と読み方"></a>
<a id="20-最終確認chat量子化の準備と実施していないこと"></a>
<a id="2026-10-09までの固定台帳"></a>
<a id="21-指標と比較してはいけないもの"></a>
<a id="22-結論-分かったこと分からないこと停止の判断"></a>
<a id="23-復旧再利用のために保全するもの"></a>
<a id="24-後続のchat診断教材比較2026-10-1013"></a>
<a id="3-初期調査-小型化tokenizer学習評価"></a>
<a id="4-phase01-実験契約と追跡可能なpilot"></a>
<a id="5-phase2-tokenizerの学習と日本語byte契約"></a>
<a id="6-phase3-モデルcacheexportの成立"></a>
<a id="7-windowswsl移行権限復元長時間実行"></a>
<a id="8-phase45-保存再開overfitsmoke100m選定"></a>
<a id="9-phase6基盤-データ拡張速度資源変換"></a>
<a id="jmicro-10m-調査検証学習の全体記録"></a>
<a id="固定revision後の比較と判断"></a>
<a id="固定台帳後の追加判断"></a>
<a id="更新前の本文契約当時の記録"></a>
<a id="設計手順の保存記録"></a>
