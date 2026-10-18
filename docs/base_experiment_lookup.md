# BaseとChatの結果索引

更新: 2026-10-18 JST。

現在の科学的な状態は[状態](autonomous_status.md)、最新SFTは[165](165_chat_two_attribute_diagnosis_results.md)です。Baseと後続Chat、技術検証と品質改善、候補不採用と実験完了を区別します。

| 対象 | 結果 |
|---|---|
| 元Base 10B | [42](42_base_10b_quality_evaluation.md) |
| 教師量正規化weight decay 2B | [123](123_base_teacher_decay_2b_results.md) |
| 文書長重み100M | [144](144_base_document_balance_results.md) |
| 進行長補助 / ScaleGrad / RDrop | `reports/phase6/document-progress-science-20261015/` / `scalegrad-science-20261015/` / `rdrop-science-20261016/` |
| 自然会話教材 / 回答教材SFT | [150](150_chat_natural_sft_results.md) / [156](156_answer_curriculum_results.md) |
| 対照100ケースと履歴要因 | [159](159_chat_recovery_diagnosis_results.md) |
| 入力配置SFT / 二情報SFT | [162](162_chat_input_structure_sft_results.md) / [165](165_chat_two_attribute_diagnosis_results.md) |

過去の手法名検索・全proposal/結果の固定一覧は更新前の索引と[固定台帳](retrospective/README.md)を使います。索引に語がないことを未検証や新規性の証拠にしません。保存済みの構成配分比較や閉じたprobeを、未検証の改善案として繰り返さないでください。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/base_experiment_lookup.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="baseの実験結果を探す"></a>
<a id="当時の資料保存手順"></a>
<a id="最新までの入口"></a>
<a id="設計手順の保存記録"></a>
