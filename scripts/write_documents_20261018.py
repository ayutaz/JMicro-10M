"""Authored current documentation and consolidation; no research execution."""
from pathlib import Path
import json
import re
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from documentation_refresh_20261018 import ROOT, RUN, LIVING, NEW, REMOVED, page, write, catalog, read_baseline, href


CONTENT = {
'docs/autonomous_status.md': ('現在の研究と公開の状態', '''
最新のSFT試行は完了しましたが、一般会話の品質が低下したため不採用です。Base 3系列と最新SFTの重みは申請・ログイン不要で公開し、GitHubのコードはApache-2.0にしました。現在の作業は文書の更新・整理とpushです。新しい学習や評価は開始していません。

## 最新SFTの結果

元の10B Baseから64教材を483更新、250,003 Assistant教師tokenで学習しました。教材の全文再現64/64、未知値30/32に対し、質問構造の変更15/32（二項目0/16）、実会話最終9/16でした。主SFTへ進む条件に届かず、追加の主比較は行っていません。

既存7組は全て内容成立が低下し、固定100ケースのタスク成立も直前の別SFTの19/100から3/100へ低下しました。教材構成・教師量も異なる歴史的比較です。全1,973応答をCodexで非blind判定しており、独立人手評価ではありません。[全結果165](165_chat_two_attribute_diagnosis_results.md)。

## 完了したことと残る課題

- モデル・Tokenizer・学習・保存再開・評価・ローカル画面の基盤、複数のBase/SFT比較、最新候補の全件判定は完了。
- GitHubをpublicへ変更し、Apache-2.0と読みやすいREADMEを反映。Hugging Faceの4モデルの匿名取得を確認。
- 実用的な一般会話、正式Base/Chat採用、親の事前学習からの独立した全工程再現、必要な実全文DEV/全440件・新封印TESTは未達。

10Mの限界や単独の失敗原因を証明した結果ではありません。現在の追加SFTを繰り返す根拠は弱く、既存の固定条件は終了しています。[残課題と再開条件](10_next_steps.md)。

## 保存と実行状態

最終checkpointはWSLの`reports/phase7/chat-two-attribute-20261018/model/checkpoint-00000483.pt`。SHA256は`44128809acccf45fbfddcd8863a72af5a029d43a660e10b06ed73e4157aff553`です。全model/Adam/RNG/samplerはWSLに保持し、公開保存版には重み・Tokenizer・native実装を収録しています。

最新SFTの科学process/Windows workerは正常終了し、2026-10-18 02:40 UTCの記録で元Base UIの復帰を確認しました。この日時付き記録は現在のprocess生存保証ではありません。起動や停止が必要なら[運用手順](windows_handoff.md)で実状態を照合します。
'''),
'docs/03_architecture.md': ('モデル構成と学習方式', '''
JMicro-10Mは独自Tokenizerを使う日本語のdecoder-only Transformerです。最新Base/SFTの参照構成は10,001,152 parametersで、一般会話の品質は未達です。

## 構成

| 項目 | 固定した参照値 |
|---|---|
| 層数 / hidden / FFN | 13 / 256 / 640 |
| query / key-value heads | 4 / 2、head dimension 64 |
| 語彙 / context | 4096 / 1024 token |
| FFN / 正規化 | SwiGLU / RMSNorm、QK-Normなし |
| RoPE | half-split、theta 10000 |
| embedding / output | weight tying |
| 推論dropout | 0 |

実装は[src/jmicro/model.py](../src/jmicro/model.py)。共有重みにより、119 unique parameter tensorsに対してstate辞書には120 entriesがあります。公開safetensorsは共有outputの重複保存を省き、native loaderで結び直します。

## Tokenizer

語彙4096のSentencePiece unigramとprotected-byte処理を併用します。改行・タブ・文字`▁`・`<`を保護して、本文の文字と構造tokenを区別します。

| ID | 構造 |
|---|---|
| 0 / 1 / 2 / 3 | PAD / UNK / BOS / EOS |
| 4 / 5 / 6 / 7 | System / User / Assistant / EOT |

Tokenizer SHA256は`a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`。`jmicro.tokenizer.Tokenizer`を使い、raw SentencePieceや汎用AutoTokenizerだけで置き換えません。

## 学習と保存再開

Baseは本文の次token予測、Chat SFTはAssistant本文とEOTを教師とします。直前までのUser/Assistant履歴は入力であり、最新SFTでは最後のAssistantだけを教師にしています。教師を途中で切断せず、入力・教師・paddingの量を分けて記録します。

最新の64教材診断は元Base/fresh optimizer、seed42、LR1e-4、BF16/math、32×1024で483更新・250,003教師。正確な条件は[固定契約164](164_chat_two_attribute_diagnosis_execution.md)、結果は[165](165_chat_two_attribute_diagnosis_results.md)です。この終了済み条件を延長する計画はありません。

長い実験の前に最大shapeの有限逆伝播、連続実行と保存再開の全state一致、実測費用を確認します。保存はcompleted updateで行い、model、optimizer、scheduler、RNG、sampler、消費量、履歴を保持します。技術合格と品質合格は別です。[データ](../data/README.md) / [評価](evaluation_protocol.md)。

## 実装上の不変条件

日本語Base/短いChatの目標と約10Mの要件（9.5M〜10.1M）を維持します。勝手な大型化、Tokenizer/精度/decoder/親/教師量の変更、品質条件の緩和で失敗を救済しません。新しい構成変更は別の根拠・対照・契約が必要です。
'''),
'data/README.md': ('データと会話教材', '''
学習データの実体は主にWSLの`/home/aihub_ubuntu/jmicro-data`に保存しています。GitHubのコードやHugging Faceのモデル保存版だけから、全corpusや元samplerを復元できるわけではありません。

## Baseデータと会話教材

既存BaseのWeb/textbook/story poolと、後続の会話SFT教材は別の学習系列です。学習量とunique教材量を区別し、同じ文書を繰り返した教師token数を新規データ量と呼びません。

最新SFTは著作した64件の二情報回答教材です。8組の事実設定を記憶/訂正・一項目/二項目・短距離/離れた質問に展開しており、64の独立した事実設定ではありません。過去の公開会話教材と著作2,048件の混合SFTとは、教材構成と教師量が異なります。[教材点検152](../docs/152_answer_learning_diagnosis_results.md) / [教材比較結果156](../docs/156_answer_curriculum_results.md) / [最新結果165](../docs/165_chat_two_attribute_diagnosis_results.md)。

## 分離と品質確認

TRAINを確定してから評価を用意し、DEV/TESTを教師へ混ぜません。本文・教師ID・mask・非切断・source配合・サンプル順・消費量を、各runのmanifestとCPU replayで照合します。損失低下や短文選別だけを、質問に答える能力の証拠にはしません。

元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴があります。学習・GPU採点に使っていないことと、未開封であることを混同しません。将来の最終確認には新しく封印したTESTが必要です。今回の文書更新でデータ本文・TESTを開いたり再処理したりしていません。

## 公開と復元

最新モデル保存版にはデータセット・sampler・optimizer・RNGを含めていません。古いBase保存版の数値学習状態も、data/samplerなしでの厳密再開を保証しません。初期pilot/Tokenizer bundleは別のdataset保存で、[Hub取得手順](../docs/huggingface_handoff.md)を参照してください。

コードのApache-2.0を、外部教材・モデル重み・Tokenizerへ一括適用していません。元教材の出所と条件は各実験記録へ保持しています。再生成や再学習は、[当時の手順](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/ed91c002cdfe52c879e275241c58436bfef3e394/data/README.md)を読んだだけで開始しないでください。
'''),
'docs/evaluation_protocol.md': ('評価方法と結果の読み方', '''
最新SFTの全1,973応答は確認済みで、候補は不採用です。評価が完了したことと、Base/Chatの正式品質条件を満たしたことを区別します。

## 現在の評価条件

最新診断は学習前後の教材128応答、未知値32、質問構造32、16会話の実履歴48応答、計240。回帰確認は既存7組×219と公開100ケースの200応答、計1,733です。合計1,973に1,400件の新しい判定と573件の厳密な実履歴/raw判定再利用を含みます。

BF16/math、greedy、最大32生成token、抑制IDは0/1/2/4/5/6、停止はEOT7/EOS3です。各suiteの抑制なし対照も保存します。最大token到達は自然停止と数えません。自己履歴には実際のAssistant本文を入れ、空応答・誤答・壊れたUTF8も記録から消しません。

## 内容と機械的な検査

文法・関連性・文脈を0/1/2で個別に判定し、要求値が含まれることと、回答全体が成立することを区別します。停止、反復、空、役割漏れ、raw UTF8、履歴切断は別に集計します。損失や単語一致だけで内容成立を推定しません。

Codex非blind評価は独立した人手blind評価ではありません。固定DEVの件数を一般利用全体の精度と解釈せず、bootstrapの単位・seed・分母を各結果へ残します。最新の旧モデル比較は教師集合と学習量も違うため、単独要因の因果効果ではありません。

## BaseのBPBと元の品質条件

`BPB = 本文NLL総和 / (ln(2) × 採点したcanonical UTF-8 bytes総数)`。本文は一回だけ数え、EOSを別集計します。CRLF/CRをLFへ統一しU+0000を除き、他のUnicode・空白を暗黙に正規化しません。異なるTokenizerのperplexityを直接比較しません。

元Base DEV80の条件は文法≥56、一貫性≥27、適切完結≥27、EOS≥37、規定反復≤18、空/役割/Unicode失敗0。相対差・CI・BPB/strong/historical保持等も必要です。これらの一部や小集合の暗記だけを正式採用へ読み替えません。

## 固定suiteとTEST

v1の[protocol.json](../configs/evaluation/protocol.json)は80 DEV/20 TEST、64token等の元契約を保存しています。後続SFTの32token条件や、Base標準400/長文40の抑制ID差を上書きして揃えません。評価時に混在fileを開いてからfilterする旧経路へ戻さず、DEV専用manifest/readerを使います。

元TESTにはCPU解析履歴があり、新しい封印TESTが必要です。全文DEV/全440接続部品の36 CPU checksは、資格ある最新モデルの実全文評価・全内容判定の代替ではありません。独立全工程・人手blind・最終TESTの未達を保持します。[最新結果165](165_chat_two_attribute_diagnosis_results.md) / [残課題](10_next_steps.md)。
'''),
'eval/README.md': ('評価データと利用上の境界', '''
評価の現在の説明は[評価方法](../docs/evaluation_protocol.md)、最新の全件結果は[165](../docs/165_chat_two_attribute_diagnosis_results.md)へ統合しました。固定v1の[protocol](../configs/evaluation/protocol.json)は過去の契約として保持し、後続実験の生成長や抑制IDで書き換えません。

最新診断の240応答と回帰1,733応答は別の分母で、合計1,973応答を個別に確認しています。公開100ケースは、最終100回答と全200回答の集計を区別します。

TRAIN/DEV/TESTのfamily分離、専用DEV artifact、manifest、実履歴とraw bytesを保持します。旧Base TEST20 promptとChat TEST20行にはCPU解析履歴があるため、未開封とは呼べません。学習やGPU TEST採点には使っていませんが、正式な最終評価には新しい封印TESTが必要です。

今回の文書更新では評価データ本文の解析、新TEST作成、生成・再採点を行いません。ファイル名が存在することやCPU fixtureの合格を、実モデルの品質確認へ読み替えないでください。
'''),
'docs/10_next_steps.md': ('残る課題と再開の条件', '''
現在の追加SFTは、限定教材を覚えても一般会話に転用できず、継続する根拠が弱いという判断です。最新の固定条件は不採用で終了し、新しい学習は予定していません。文書の更新・統合・不要文書の削除・pushを今回の作業とします。

## 完了したもの

- [x] 10Mモデル・Tokenizer・学習・全state保存再開・評価の基盤。
- [x] 複数のBase/SFT比較、最新診断の5工程と全1,973応答の確認。
- [x] Base 3系列と最新SFTの申請不要公開、匿名の重み取得とhash照合。
- [x] GitHubのpublic化、コードのApache-2.0、入手・CPU実行手順。

## 未解決のもの

- [ ] 質問の言い換えで二項目のうち一つを落とす問題。
- [ ] 自分の誤答や古い値に固定され、訂正・継続会話に失敗する問題。
- [ ] 一般会話の内容成立、空応答、反復、UTF8破損を含む品質の保持。
- [ ] 正式Base/Chat採用、親の事前学習から独立した全工程の再現、必要な実全文DEV/全440、新封印TEST。

## 研究を再開する場合

[結果165](165_chat_two_attribute_diagnosis_results.md)には、重み・事実・履歴を固定して質問表現だけを変える64入力の診断案があります。これは未著作・未実行で、今の実行計画ではありません。10M全般の限界や単独原因を確定したわけではありません。

再開の指示があった場合は、根拠ある未回答仮説を一つ選び、対照、教師集合、量、親、decoder、品質条件、段階予算、停止条件を実行前に定めます。累積ローカルGPU時間の上限は解除済みですが、各比較の有限な契約は必要です。終了済みの条件を延長・再計時・閾値変更で救済しません。
'''),
'docs/windows_handoff.md': ('環境と保存先の引継ぎ', '''
WindowsをGitの正本、WSLを実行・大容量保存先としています。新しいPCでモデルを試すだけなら、[READMEのCPU手順](../README.md#最新モデルをcpuで試す)を使えます。元の学習の厳密再開には公開重み以外の保存物が必要です。

## ローカルの保存先

| 対象 | 場所 |
|---|---|
| Git正本 | `C:\\Users\\AiHUB\\Desktop\\japanese-tiny-llm-10m` |
| WSL実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| データ | `/home/aihub_ubuntu/jmicro-data` |
| 元Base | `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt` |
| 最新SFT | `reports/phase7/chat-two-attribute-20261018/model/checkpoint-00000483.pt` |
| Tokenizer | `artifacts/phase2/4096/tokenizer.model` |

元Base SHA256は`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、最新SFTは`44128809acccf45fbfddcd8863a72af5a029d43a660e10b06ed73e4157aff553`です。全学習stateはWSLへ、小raw・判定理由・監査記録はWindows/Gitへ保全します。

## Pythonと同期

記録された環境はWSL2/Linux disk/RTX4090、Python3.12.7とuvです。Pythonは`uv run --frozen`から実行し、必要なextraを指定します。依存は`uv sync --frozen`で復元し、既存の学習環境を文書更新のために変更しません。

WindowsとWSLを同期する時は対象を限定し、元の科学source/configのEOLとhashを保持します。WindowsのGit HEADを正とし、WSLで別の履歴を作ったり大容量重みをGitへ追加したりしません。

## 実行状態を確認する

最新SFTは正常終了し、2026-10-18 02:40 UTCの[終端観測](../reports/phase7/chat-two-attribute-20261018/terminal_observation.json)で元Base UI復帰を確認しました。PIDの記録だけで現在生存と断定せず、操作時に実PID/boot/start・HTTP・kernel lockを照合します。

[WebUI操作](43_local_webui.md)を参照し、元Baseと各SFTのモデル名・port・checkpointを区別してください。今回は起動・停止・モデル差替えを行いません。[公開モデルと復元範囲](126_model_archive.md)。
'''),
'docs/43_local_webui.md': ('ローカル画面とモデルの区別', '''
研究用のBase/SFT画面を複数用意しています。最新SFT診断の重みを、既存画面へ採用・差替えしたわけではありません。配布された最新SFTを試す場合は[READMEのCPU手順](../README.md#最新モデルをcpuで試す)を使ってください。

## 各portのモデル

| port | 対象 |
|---|---|
| 7860 | 元10B Base、文章の続きを生成 |
| 7861 | 最初のRealPersonaChat SFT |
| 7862 / 7863 | 自然な会話教材SFTの候補C1 / 対照C0、結果150 |
| 7864 / 7865 | 回答教材SFTの候補C1 / 対照C0、結果156 |
| 7866 / 7867 | 入力配置SFTの候補C1 / 対照C0、結果162 |

これらはローカル環境のport対応表です。現在の生存は保証せず、画面が動いている場合も品質採用済みとは解釈しません。ChatはCPU FP32/greedy、既定32token、16/32/64の選択です。最新64教材SFT用の追加画面はありません。

## 操作と確認

稼働時は`http://127.0.0.1:<port>`へアクセスします。「新しい会話」で履歴を消し、Enterで送信、Shift+Enterで改行します。開始前に`/api/model`で実際のモデル名・checkpointを確認してください。

```powershell
Invoke-RestMethod http://127.0.0.1:7860/api/model
```

停止中の元Baseを起動する既存の入口は`./scripts/start_webui.ps1`です。最初のChatは`./scripts/start_chat_demo.ps1`、自然会話教材のC1/C0は`./scripts/start_natural_chat_demo.ps1 -Arm C1`等を使います。後続画面の固有手順は[当時の実行結果162](162_chat_input_structure_sft_results.md)を確認し、閉じた学習runnerをUI起動に使わないでください。

短い挨拶が返せても、訂正・実履歴・継続会話の品質は未達です。7864での同文固定は[実ブラウザー確認156](156_answer_curriculum_results.md)で再現しています。入力と履歴の送信が正しくてもモデル自身が反復するため、UIの動作と内容の品質を区別します。
'''),
'docs/126_model_archive.md': ('公開モデルの保存内容と入手方法', '''
Base 3系列と最新SFTをHugging Faceでpublic・ungatedにしています。アクセス申請もログインも不要です。2026-10-18に既存Base保存先のmanual gateを解除しました。

## 保存先

| モデル | リポジトリとフォルダ |
|---|---|
| 元Base | [Base保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)の`models/web-10b` |
| source-order Base | 同保存版の`models/staged-10p6b` |
| teacher-decay Base | 同保存版の`models/teacher-decay-2b` |
| 最新二情報SFT | [SFT研究保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018)のルート |

全てnative10,001,152 parameters、語彙4096、context1024です。Base保存版の10B/10.6B/2Bは各系列の学習量であり、パラメータ数ではありません。最新SFTは一般会話の品質不採用です。

## 読み込みと保存範囲

最新SFTは`model.safetensors`、`jmicro_config.json`、`tokenizer/`、`src/`、`inspect_model.py`、出所・評価・hash一覧を含みます。[READMEのCPU実行手順](../README.md#最新モデルをcpuで試す)を使い、native loaderと専用Tokenizerを組み合わせてください。標準AutoModel/AutoTokenizer形式ではありません。

最新SFTに元checkpoint pickle、optimizer、RNG、sampler、学習データは含めていません。古いBase保存版には数値学習状態がありますが、data/samplerを含まないため元と厳密に同じ状態からの再開の代替ではありません。

## 公開の確認

最新SFTの128ファイル・41,732,706 bytesをHubのサイズとhashで照合し、全128ファイルを匿名で取得しました。Base 3系列も重み全体を匿名取得しhashを照合しています。詳細は[公開記録166](166_public_models_and_oss.md)です。

Baseの`archive_manifest.json`と`SHA256SUMS`は2026-10-09の保存revision `853d52d2323653331b610249912fbe25615615fc`に対応します。その後のREADME変更を元のhash一覧で検証しないでください。

コードのApache-2.0と、モデル重み・Tokenizer・外部データの利用条件は別です。公開設定の変更は、重み等への新たな一括ライセンス付与ではありません。
'''),
'docs/huggingface_handoff.md': ('Hugging Faceからの取得と復元', '''
モデルは[Base保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)と[最新SFT保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018)で申請・ログイン不要です。最新SFTをCPUで試す手順は[README](../README.md#最新モデルをcpuで試す)へ統合しました。

## モデルと古いpilot bundleを区別する

モデル保存版は重み・Tokenizer・実装・評価記録の保存です。学習データ全体や元samplerの復元には使えません。Base保存版とSFT保存版はフォルダ構成も異なります。[保存範囲](126_model_archive.md)。

初期pilot/Tokenizerのdataset bundleは`japanese-data-analyze/japanese-tiny-llm-10m-artifacts`、固定revisionは`0b1042979bf32899e24da30790e3ae6b239013c3`です。後続10B corpusや最新SFT教材を含むものではありません。欠損時だけ[download helper](../scripts/download_hub_artifacts.py)と[固定設定](../configs/hub/artifacts.json)で復元します。

```sh
uv run --frozen --extra hub scripts/download_hub_artifacts.py --verify-only
```

既存の正しいファイルがある環境で再取得・Tokenizer再学習を繰り返しません。取得先をproject rootにしてREADMEを上書きしないでください。元payloadの検証・配置の詳細は更新前の手順を参照します。

## Tokenizerの互換性

固定4k model SHA256は`a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`です。独自のprotected-byte契約を含むため、汎用AutoTokenizerだけで置き換えません。過去のrandom-weight exportのhashと、本学習で使った公開Tokenizerのhashを混同しないでください。
'''),
'docs/09_prior_art_and_baselines.md': ('参考モデルとの比較と文献の扱い', '''
参考モデルAkebonoは、固定revision `74b3a1739e6d16883177c6021b3c03a7d517c7fb`の重みと配布コードを照合してCPU実行しています。実parameter数9,965,824、語彙12,288、context512です。

同じ既知20問で、公式128token条件と別driverの32token条件はともに内容成立5/20、最初のJMicro SFTは4/20、当時のJMicro C1は1/20でした。全80応答を確認し、Akebonoの2条件では実ID・本文・停止が同じでした。[結果152](152_answer_learning_diagnosis_results.md)。

固有Tokenizer、対話形式、学習履歴、system文、抑制IDが異なるため、一般的な優劣や、同じ32tokenが同じ日本語長だという結論にはしません。これは固定した少数質問の非blind比較で、最新JMicro SFTとの新しい同条件比較ではありません。

初期に調べた小型モデル一覧や論文の採否は、更新前の本文と[研究総覧](125_project_retrospective.md)へ保存しています。過去の公開時期・製品情報・外部モデルrevisionを、今回再調査した現在情報として再掲しません。10Mモデル全般の不可能や容量限界は証明していません。
'''),
'docs/125_project_retrospective.md': ('研究の経過と実証できたこと', '''
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
'''),
'docs/base_experiment_lookup.md': ('BaseとChatの結果索引', '''
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
'''),
'docs/retrospective/README.md': ('固定した研究台帳の読み方', '''
このディレクトリのcoverage・experiment_records等は、元revision `2d48062f5e29f7cb4cc9a1eb4352aa304e44827c`の集合を保持した固定台帳です。後続SFTや公開の件数・hashを元の台帳へ書き戻しません。

現在までの経過は[研究総覧](../125_project_retrospective.md)、新しい結果は[最新SFT165](../165_chat_two_attribute_diagnosis_results.md)、全保存文書は[カタログ](../document_catalog.md)で補います。元台帳の詳細な分野別案内は更新前の本文へ残しています。

原キー・指標・採否・失敗・source SHAを保ち、記録数を独立実験数、重複する行のGPU秒を一意な全プロジェクト総計と扱わないでください。記録にある「次は」「実行中」「公開未承認」は、そのrevision時点の記述です。
'''),
'reports/README.md': ('結果と監査記録の入口', '''
最新の結果は`phase7/chat-two-attribute-20261018/`、公開確認は`publication/chat-sft-public-20261018-v2/`です。大容量checkpoint・optimizer・RNG・samplerはWSLに保全し、Gitには選んだ小記録・全回答・判定理由を収録しています。

| 記録 | 内容 |
|---|---|
| [最新SFT completion](phase7/chat-two-attribute-20261018/completion.json) | 5工程の完了と品質不採用を区別した要件照合 |
| [final_analysis](phase7/chat-two-attribute-20261018/final_analysis.json) | 診断240・回帰1,733・全1,973応答の集計と採否 |
| [全回答CSV](phase7/chat-two-attribute-20261018/all1973_responses.csv) | 実履歴・raw・停止・判定理由 |
| [一つ前の比較](phase7/chat-recovery-20261018/input-structure-main/completion.json) | 入力配置SFTの実行・全3,466主応答・不採用 |
| [SFT公開](publication/chat-sft-public-20261018-v2/SFT_public.json) | 128ファイルのHub hash照合と匿名重み取得 |
| [Base公開](publication/chat-sft-public-20261018-v2/Base_public.json) | 3系列の匿名重み取得・manual gate解除 |
| [GitHub公開](publication/repository-public-20261018.json) | public・Apache-2.0・匿名README/Git確認 |
| [今回の文書棚卸し](investigation/documentation-refresh-20261018/baseline.json) | 全元文書のpath/hash/分類と開始revision |

過去の完了report、source snapshot、失敗、台帳は日付時点の証拠です。現在の結果で過去の採否やhashを上書きせず、当時の相対リンクは元revisionの配置で読みます。文書更新の監査合格はモデルの品質合格ではありません。
'''),
'docs/codex_automation.md': ('実験runnerと文書更新の運用', '''
現在の依頼は全ドキュメントの更新・統合・不要文書削除とpushです。以前のSFT試行は完了・不採用で、新しい学習・評価・TEST準備を起動する範囲ではありません。GitHubとモデル公開は完了しており、今回の文書pushは明示的に依頼されています。

実験を再開する場合は[残課題と条件](10_next_steps.md)と[AGENTS](../AGENTS.md)を確認します。旧runnerは当時の契約・source・予算に結び付くため、古い「active」「continue」を今の起動指示に使いません。

WindowsのGit正本とWSLの実行コピーを区別し、Pythonはuv frozenから実行します。長い実行では実PID/boot/start・lock・ログ・completed checkpointを結び付け、観測が途切れたという理由だけで重複起動しません。文書更新では元の数値source/config/重み・データ・原評価を変更しません。

手法の成功、実験の完了、文書作業の完了は別の状態です。今回も全件カバレッジ、現在の説明、履歴保全、リンク、同期、公開pushを確認してから文書goalを完了します。
'''),
}

REDIRECTS = {
'docs/01_project_goal.md': ('プロジェクトの目標','../README.md','03_architecture.md','約10Mの日本語Baseと短いChatを調べる目標は維持しています。実験・公開は完了しましたが、実用的な会話と正式採用は未達です。'),
'docs/02_research_summary.md': ('研究結果の要約','125_project_retrospective.md','autonomous_status.md','経過と結論は研究総覧へ、現在の結果・採否は状態ページへ統合しました。最新SFTの限定課題成功を、一般会話の改善へ読み替えません。'),
'docs/04_tokenizer.md': ('Tokenizerの仕様','03_architecture.md#tokenizer','huggingface_handoff.md','語彙4096、protected-byte処理、特殊ID、固定hashはモデル構成のTokenizer節へ統合しました。取得と互換性はHub手順で説明します。'),
'docs/05_dataset.md': ('データ設計と分離','../data/README.md','evaluation_protocol.md','Base poolと会話教材、教師量とunique量、出所と復元範囲の説明をデータREADMEへ統合しました。'),
'docs/06_training_plan.md': ('学習方式と再開条件','03_architecture.md#学習と保存再開','10_next_steps.md','教師mask・保存再開・最新の実行条件はモデル構成へ統合しました。終了済みSFTの延長は予定していません。'),
'docs/07_environment.md': ('実行環境と保存先','windows_handoff.md','126_model_archive.md','Windows/WSL、Python/uv、データとcheckpointの場所、同期と復元の説明を引継ぎへ統合しました。'),
'docs/08_evaluation.md': ('評価とcheckpointの確認','evaluation_protocol.md','165_chat_two_attribute_diagnosis_results.md','BPB、内容判定、実履歴、生成長、保存再開と品質の区別は評価方法へ統合しました。'),
'docs/11_technical_research_gaps.md': ('未解決の課題','10_next_steps.md','165_chat_two_attribute_diagnosis_results.md','質問の言い換え、二情報の保持、訂正、反復と空応答、独立全工程・最終TESTの不足を一つのチェックリストへ統合しました。'),
'docs/12_training_implementation_research.md': ('学習実装の確認事項','03_architecture.md#学習と保存再開','125_project_retrospective.md','数学・最大shape・全state再開の技術確認はモデル構成へ、OOMや費用閉鎖・品質失敗の経過は研究総覧へ統合しました。'),
'docs/13_tokenizer_dialogue_data_research.md': ('対話データとTokenizer','../data/README.md','03_architecture.md#tokenizer','Assistant本文+EOT、教材の能力点検、構造tokenと本文の分離を、それぞれの主文書へ統合しました。'),
'docs/14_evaluation_deployment_research.md': ('評価とモデル配布','evaluation_protocol.md','126_model_archive.md','研究モデルの公開は完了しましたが、正式float採用・学習済み量子化品質・独立環境の最終確認は別の未達事項です。評価方法と公開手順へ説明を統合しました。'),
'docs/15_project_roadmap.md': ('現在のロードマップ','10_next_steps.md','125_project_retrospective.md','基盤・学習・評価・公開の実績は研究総覧へ、残る成果物と再開の条件はチェックリストへ統合しました。20B/50Bや大型モデルの研究を自動的に開始しません。'),
'docs/124_base_recovery_plan.md': ('Base品質改善の再開条件','10_next_steps.md','evaluation_protocol.md','Base採用・独立全工程・全文DEV/全440・新TESTは未達です。旧計画の不足を保持しつつ、現在の判断と再開条件はチェックリストへ統合しました。'),
'docs/145_post_rejection_next_plan.md': ('不採用後の課題と判断','10_next_steps.md','165_chat_two_attribute_diagnosis_results.md','後続SFTも実行・評価済みで、最新候補は不採用です。現時点では追加SFTを継続せず、再開する場合の根拠と条件をチェックリストへ統合しました。'),
}


def main():
    for name,(title,body) in CONTENT.items():
        page(name,title,body)
    for name,(title,target,second,summary) in REDIRECTS.items():
        page(name,title,f'{summary}\n\n詳しい説明は[統合先]({target})と[関連する結果・手順]({second})を参照してください。',previous=True)

    revision=read_baseline()['initial_commit']
    old=(ROOT/'AGENTS.md').read_text(encoding='utf-8-sig')
    rules=old[old.index('## Fixed model-size requirement'):]
    rules=rules.split('<!-- Historical incoming')[0].strip()
    rules=rules.split('The complete pre-refresh AGENTS progress chronology')[0].rstrip()
    rules=rules.replace('Do not automatically push or publish.', 'Push/publication requires user authorization; the current documentation push is explicitly authorized.')
    rules=rules.replace('do not automatically push or publish.', 'push/publication requires explicit user authorization, which is present for this documentation goal.')
    body=f'''# JMicro-10M development and training

## Current scope 2026-10-18

The active user goal is to update ALL documentation, consolidate overlapping explanations, delete unnecessary documents, and push the verified changes. GitHub and all four published models are already public/ungated. Original code is Apache-2.0; model weights, Tokenizer artifacts, external datasets and third-party code retain their separate conditions.

Latest diagnostic SFT: 483 updates/250003 teachers; TRAIN64 exact, unseen values30/32, structure15/32 (two fields0/16), own final9/16; public100 task3/100. All1973 reviewed. Five-step execution COMPLETE; candidate REJECTED. Formal Base/Chat adoption, independent whole pipeline, required fullDEV/all440/new sealedTEST remain unachieved. This documentation goal does not restart any research/training/evaluation or switch the UI model.

Read [current state](docs/autonomous_status.md), [remaining work](docs/10_next_steps.md), [latest fixed results](docs/165_chat_two_attribute_diagnosis_results.md), [publication](docs/166_public_models_and_oss.md), and [documentation catalog](docs/document_catalog.md). Preserve frozen scientific sources/configs/results/weights, dataset boundaries, negative decisions and all historical costs. Dated active/live/next statements are historical, not current authorization. Do not reopen a closed job or use a small memorization result as Base/Chat qualification.

The full preceding instructions and progress chronology are preserved at [the pre-refresh Git revision](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/{revision}/AGENTS.md). Documentation-maintenance summaries142/146/148 are consolidated into167 and removed from the current tree; original scientific records and their source snapshots remain intact.

{rules}
'''
    write('AGENTS.md',body)
    readme=(ROOT/'README.md').read_text(encoding='utf-8-sig')
    marker='## コードと研究記録を読む\n'
    if '全文書更新167' not in readme:
        readme=readme.replace(marker,marker+'\n文書の入口は[読む順序と主要文書](docs/README.md)、整理・統合・削除の記録は[全文書更新167](docs/167_current_state_and_documentation.md)です。\n')
    write('README.md',readme)

    numbered=[]
    for row in read_baseline()['documents']:
        if re.fullmatch(r'docs/\d+_[^/]+\.md',row['path']) and row['path'] not in REMOVED:
            numbered.append(row)
    numbered.sort(key=lambda r:int(Path(r['path']).name.split('_')[0]))
    table=['| 文書 | 内容 |','|---|---|']
    for r in numbered:
        table.append(f"| [{Path(r['path']).name}]({Path(r['path']).name}) | {r['title'].replace('|','/')} |")
    table.append('| [167](167_current_state_and_documentation.md) | 全文書の更新・統合・削除の記録 |')
    page('docs/README.md','文書を読む順序','''
最新SFTは実行・全件評価を完了し、候補は品質不採用です。Base 3系列と最新SFTの重みは申請不要で公開し、コードはApache-2.0になりました。

## まず読む文書

| 目的 | 主文書 |
|---|---|
| モデルを取得して試す | [プロジェクトREADME](../README.md) / [保存範囲](126_model_archive.md) |
| 現在の結果と公開 | [状態](autonomous_status.md) / [最新結果165](165_chat_two_attribute_diagnosis_results.md) / [公開166](166_public_models_and_oss.md) |
| 構成・Tokenizer・学習 | [モデル構成](03_architecture.md) / [データ](../data/README.md) |
| 評価の基準と限界 | [評価方法](evaluation_protocol.md) / [残課題](10_next_steps.md) |
| 環境・保存先・画面 | [引継ぎ](windows_handoff.md) / [WebUI](43_local_webui.md) |
| 過去の研究を探す | [総覧](125_project_retrospective.md) / [実験索引](base_experiment_lookup.md) / [全件カタログ](document_catalog.md) |

重複する設計・計画は主文書へ統合しました。旧入口はリンク互換性のため案内だけ残し、古い文書更新報告142/146/148は[更新記録167](167_current_state_and_documentation.md)へ統合・削除しています。日付付き実験結果、凍結契約、source snapshot、原文copy、第三者の帰属は保持しています。

## 番号付きの計画と結果

以下は現在の実行順ではありません。各文書の日付・対象・採否で読み、古い「実行中」「未公開」「次は」を現在の状態へ持ち込まないでください。

'''+ '\n'.join(table),previous=False)

    page(NEW,'最新の研究状態と全文書の整理','''
最新SFTの実行・全1,973応答の判定と品質不採用、Base 3系列/最新SFTの申請不要公開、GitHubのpublic化とApache-2.0を、現行文書へ反映しました。追加学習を繰り返す根拠は弱く、新しい研究は開始していません。

## 最新の結果

64教材の全文再現は64/64、未知値30/32、質問構造15/32（二項目0/16）、実会話最終9/16。固定100ケースのタスク成立は3/100で、旧混合教材SFTの19/100を下回りました。主SFT条件は非発動で、試行完了と品質採用を区別します。[原結果165](165_chat_two_attribute_diagnosis_results.md)。

重みは[Base保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)と[最新SFT](https://huggingface.co/japanese-data-analyze/JMicro-10M-chat-research-20261018)で公開。全4モデルの匿名取得を確認済みです。コードのApache-2.0は、モデル重みや外部データへの新たな一括許諾ではありません。[公開の証拠166](166_public_models_and_oss.md)。

## 統合と削除

構成・Tokenizer・学習を03、データをdata/README、評価をevaluation_protocol、残課題と再開条件を10、環境と保存をwindows_handoff、モデル入手を126へまとめました。旧入口14文書は短い案内へ置き換え、外部からの旧見出しリンクを保持しています。初期の長い調査本文は更新前のGit revisionで読めます。

重複する文書更新報告142/146/148は現行treeから削除し、この更新記録へ統合しました。これらは2026-10-14/17の文書棚卸し・当時の最新結果を報告する文書で、今の状態を示すものではありません。元の報告・監査JSON、当時のGit本文・hash・件数は保持しています。削除前の全文はカタログの固定revisionリンクから取得できます。

## 全件の扱い

[全件カタログ](document_catalog.md)はGit管理のMarkdown/RST/TXT等、ライセンス、source snapshot、原文copyも含みます。現在の説明は本文とリンクを更新し、凍結した科学記録・原文・ライセンスはbyte一致を確認して保持します。現在のリンク検証と、過去snapshot内で当時の配置を前提とするリンクを区別します。

更新前は1,056文書。34の現行入口を点検し、新しい主文書167を追加、保守報告3文書を削除しています。更新前の全path/hash/分類は[baseline](../reports/investigation/documentation-refresh-20261018/baseline.json)、本文・リンク・不変記録・同期の照合は[監査結果](../reports/investigation/documentation-refresh-20261018/coverage_audit.json)へ記録します。

独立全工程、必要な実全文DEV/全440、新封印TEST、正式採用は未達として残しています。この文書作業で学習、生成、TEST準備、モデル差替えは行いません。
''',previous=False)

    # Only redundant documentation-maintenance summaries are removed. Their
    # complete bytes and old references remain available at the baseline Git revision.
    for name in REMOVED:
        assert name.startswith('docs/') and name.endswith('.md')
        if (ROOT/name).exists():
            from documentation_refresh_20261018 import sha
            original=next(r for r in read_baseline()['documents'] if r['path']==name)
            assert sha(ROOT/name)==original['sha256']
            (ROOT/name).unlink()
    catalog()
    authored=set(CONTENT)|set(REDIRECTS)|{'AGENTS.md','README.md','docs/README.md','docs/document_catalog.md'}
    assert authored==LIVING, (sorted(LIVING-authored),sorted(authored-LIVING))
    print(json.dumps(dict(current_documents=len(LIVING)+1,compatibility_entries=len(REDIRECTS),removed=sorted(REMOVED))))


if __name__=='__main__':main()
