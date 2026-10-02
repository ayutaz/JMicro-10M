# Hugging Face公開前のライセンス・個人情報確認

2026-10-02に公開候補を確認した。確認者はCodexであり、独立した人手監査・法的な権利クリアランスではない。集計と原fileのhashは[確認report](../reports/publication/review.json)に保存した。個人の連絡先や検出した本文そのものはreportへ転記していない。

## 結論

今回の本文は固定revisionの**既に公開されたdataset**から取得したもの。連絡先・自己紹介の検出を、それだけで新たな個人情報漏えいや違法な公開と扱わない。ユーザーからもdataset内部の既公開情報は公開対象として問題ないとの確認を得た。配布元の再配布条件・出所・変更点を維持し、こちらのiMacのユーザー名が含まれていたTokenizer metadataを除去したコピーで公開を進める。

当初は元一式の公開を保留する判断を記録したが、公開済み情報とローカル環境情報を分け、配布元のマスク処理・公開同意の根拠とユーザーの意図を確認して判断を更新した。一般的なWeb権利の留保を、今回のdatasetの再配布が禁止されているという結論に置き換えない。

## ライセンス確認

| source | 確認結果と公開時の扱い |
|---|---|
| FineWeb2 Edu Japanese | 固定READMEを再取得し、保存済みSHA-256と一致。ODC-By 1.0のdatabase licenseを保持し、hotchpotch/FineWeb2/Common Crawlへの出所表示・利用条件のリンクを添付 |
| RealPersonaChat | 固定LICENSEはCC BY-SA 4.0。出所・版・変更点・license全文を添付し、会話の派生部分は同licenseで配布 |
| 混合file、Tokenizer、metadata | source別条件をLICENSEとmanifestに保持。全本文をMIT等の単一licenseへ変更しない。公開者が持つTokenizer等の権利についての公開条件はbundleのLICENSEに明記 |

[ODC-Byの2.4・4.2・4.3](https://opendatacommons.org/licenses/by/1-0/)を確認した。databaseの共有条件を満たすことと、個々の記事のすべての著作権・プライバシー権を許諾されることは別。[Common Crawl利用条件](https://commoncrawl.org/terms-of-use)も第三者の権利・sourceの条件を維持する。これらの留保を公開bundleにも記載する。全記事の個別の権利を確認した、という保証はしない。

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)では、出所・license・変更点の表示と派生部分のShareAlike条件を保持する。privacy等の権利がすべてlicenseに含まれるとは扱わない。

[RealPersonaChatの固定README](https://github.com/nu-dialogue/real-persona-chat/blob/28d0b6b3865b29cabc26c230a2db37cdf315e937/README.md)は、公開版で話者名・その他の個人情報をマスクし、問題のある対話を除外したと説明している。[原論文3・3.1・3.3](https://aclanthology.org/2023.paclic-1.85.pdf)は、倫理委員会の承認、参加者の公開への事前同意と個人情報を開示しない条件を説明している。独自に参加者への再同意取得を行ったわけではない。

## 全件チェックの範囲

元bundle 25 files、Parquet manifestの取得23,000件（Web 20,000・会話3,000）、採用corpus 22,998件、Tokenizer sample 2,444件、4k/8k model/vocab、JSON metadataを確認した。

`scripts/audit_publication.py`でNFKCを**検査用にのみ**適用し、メール、国内/国際電話、郵便番号、番地付き住所候補、氏名/誕生日の文脈、番号・認証token候補、ローカルuser path、年齢・居住・健康文脈を走査した。card候補にはLuhnを併用する。元本文は変更していない。件数はcandidateを含む文書数であり、確定した非公開個人情報の件数ではない。

| 本文のcandidate | Web | 会話 |
|---|---:|---:|
| メール形式 | 105 | 0 |
| 国内電話形式 | 148 | 0 |
| 番地付き住所形式 | 103 | 0 |
| 誕生日の文脈 | 9 | 0 |
| 名前の文脈 | 183 | 31 |
| 健康の文脈 | 21 | 5 |
| 居住の文脈 | 576 | 253 |
| 年齢の文脈 | 777 | 57 |

Webの8カテゴリ各3件、会話の名前文脈31件と健康文脈5件の最初の該当箇所を読み、曖昧だった会話2件は全文を確認した。企業・施設の公開問い合わせ先、作品・ペットの名前、架空人物・動物の誕生日、ISBNやURL時刻等の数値誤検出を含む。会話の話者名は確認例でmaskが保持されていた。健康文脈には一般的な経験談と語の誤検出が混在する。これらを一律に危険な個人情報と判定しない。

本文のほか、Parquetにある採否・URL・source metadataと、同じ本文が残るsampleも確認した。regexは難読化した連絡先、すべての人名、複数対話からの再識別を網羅しない。全件機械走査と部分的な内容確認を、完全な匿名性の証明とは呼ばない。

## Tokenizer内部のローカル情報の修正

両modelの`trainer_spec.model_prefix`にローカルユーザー名を含むpathがあった。これは配布元datasetの情報ではなく、このiMacで追加された情報なので公開コピーから除去した。元の`artifacts/phase2/`は変更していない。

コピーは`artifacts/publication-audit/tokenizers/{4096,8192}/`に用意した。protobuf全体を比較し、変更が`trainer_spec.model_prefix`だけであること、piece table/normalizer/special IDsが同じことを確認した。各modelでgolden＋Unicode等232ケースのencode/decodeと、2会話のID/labelが元modelと一致した。コピーの10 filesを再走査し、直接連絡先・認証token・ローカルuser pathのcandidateは検出されなかった。8k vocabの通常の居住関連語は個人の住所ではない。

modelのbyte hashは変わるため、新manifestとtraining metadataへ新SHA-256を記録した。過去のPhase 2 reportとランダム重みのHF/GGUFは旧model hashに対応し、その履歴は書き換えない。旧exportを公開コピーと組み合わせる場合は、同コピーに合わせてexportし直す。以後の学習で同コピーを使う場合も、そのhashを実験入力として記録する。

## 再確認

```sh
uv run --frozen --extra data --extra ml scripts/audit_publication.py
uv run --frozen --extra hub scripts/download_hub_artifacts.py --source artifacts/hub-publication --verify-only
```

公開bundleは、元候補の本文・split・sampleを保持し、Tokenizer metadataの修正と説明資料を追加した計27 files。公開状態とWindowsの取得commandは[共有手順](huggingface_handoff.md)を参照する。
