# データと会話教材

更新: 2026-10-18 JST。

学習データの実体は主にWSLの`/home/aihub_ubuntu/jmicro-data`に保存しています。GitHubのコードやHugging Faceのモデル保存版だけから、全corpusや元samplerを復元できるわけではありません。

## Baseデータと会話教材

既存BaseのWeb/textbook/story poolと、後続の会話SFT教材は別の学習系列です。学習量とunique教材量を区別し、同じ文書を繰り返した教師token数を新規データ量と呼びません。

最新SFTは著作した64件の二情報回答教材です。8組の事実設定を記憶/訂正・一項目/二項目・短距離/離れた質問に展開しており、64の独立した事実設定ではありません。過去の公開会話教材と著作2,048件の混合SFTとは、教材構成と教師量が異なります。[教材点検152](../docs/152_answer_learning_diagnosis_results.md) / [教材比較結果156](../docs/156_answer_curriculum_results.md) / [最新結果165](../docs/165_chat_two_attribute_diagnosis_results.md)。

## 分離と品質確認

TRAINを確定してから評価を用意し、DEV/TESTを教師へ混ぜません。本文・教師ID・mask・非切断・source配合・サンプル順・消費量を、各runのmanifestとCPU replayで照合します。損失低下や短文選別だけを、質問に答える能力の証拠にはしません。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴があります。学習・GPU採点に使っていないことと、未開封であることを混同しません。将来の最終確認には新しく封印したTESTが必要です。今回の文書更新でデータ本文・TESTを開いたり再処理したりしていません。

## 公開と復元

最新モデル保存版にはデータセット・sampler・optimizer・RNGを含めていません。古いBase保存版の数値学習状態も、data/samplerなしでの厳密再開を保証しません。初期pilot/Tokenizer bundleは別のdataset保存で、[Hub取得手順](../docs/huggingface_handoff.md)を参照してください。

コードのApache-2.0を、外部教材・モデル重み・Tokenizerへ一括適用していません。元教材の出所と条件は各実験記録へ保持しています。再生成や再学習は、[当時の手順](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/data/README.md)を読んだだけで開始しないでください。

[現在の状態](../docs/autonomous_status.md) / [最新SFT結果](../docs/165_chat_two_attribute_diagnosis_results.md) / [公開モデル](../docs/166_public_models_and_oss.md) / [文書一覧](../docs/README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/data/README.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="phase-1-pilotの再生成"></a>
<a id="phase-4の実装済みshard"></a>
<a id="phase-6拡張corpusと全件監査"></a>
<a id="データ領域"></a>
<a id="当時の資料保存手順"></a>
<a id="設計手順の保存記録"></a>
<a id="過去の検証と現在の依存lock"></a>
