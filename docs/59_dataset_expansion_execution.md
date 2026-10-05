# 教材200M・各1B比較の実行

2026-10-05 JST。ユーザーが計画58の段階1〜3を再開。教材増量、旧/新各追加1B、同条件日本語・内容評価と採否判断まで進み、報告/local commit/元final10B UI復帰で停止する。20B/50B/Chat/protected test/pushは対象外。

## 段階1の実準備と比較条件の具体化

一般Web12.23Bの全走査・再処理は行わず、旧物語59,963,449 tokensを丸ごと保持し、新しい公開train日本語訳TinyStoriesを140,036,743 tokens追加した。新poolは200,000,192 tokens/1,161,923全文/822,869,721 UTF-8 bytes。追加499,066全文、旧662,857全文。翻訳元familyのhashで1%を除外し、ローカル完全一致61,995件を除外した。独立全corpus重複・評価混入監査は未完了で、主Webとの非重複を認証しない。

新sourceは`shibatch/TinyStories-JA` revision`155b4e5842076c90e07a4934d5b68410fe21f65f`、宣言license CDLA-Sharing-1.0。公開train4 JSONLだけを取得、公式validation/testは取得していない。各取得ファイルを公開LFS SHA256で検証。READMEとpin/inspection/receiptを保存した。合成教科書のmetadataも確認したが、その本文は取得・使用していない。新文章は32–512 body tokens、2–24完結文、4gram反復率0.15以下などの独立selectorで全文を選び、途中を切ってEOSを付けない。旧selectorと旧poolは変更していない。

平均body長は88.462→170.129、EOS/1000tokensは11.054→5.810で、計画58の±5%には一致しない。GPU開始前に比較の解釈を**量と新しい翻訳物語の構成・文章長・EOS密度の変更**へ具体化した。量だけの効果と呼ばない。旧60Mへの3.335周に対し、新200Mへ約0.99975周の同じ短文入力を比較する。前回110MはWebの完結文書追加だったが、今回は物語を保持し、別の公開物語を追加した条件である。

供給pin、1ファイル/10,000行診断、取得と並列変換・保存を含む準備実経過145.021秒、上限1800秒以内。新poolmanifest SHA`a33ad89783d7b9c2f65eadc96ceca06d19c1e397b0dc95852b148d408cec7b12`。seed20261005の一様reservoir40全文を個別確認し、弱例を開示する。これはCodex非blind診断で、全件の意味品質・事実正確性を保証しない。

## 段階2の固定条件

元final10B SHA`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`から二枝。旧poolと新poolに対し、各追加1,000,013,824 tokens/30,518更新、Web800,063,488/short199,950,336を一致。same tokenizer4096/model10,001,152parameters/seed42/Adam moments/RNG/Web初期cursor。両枝stable29,000/decay1,518、peak0.0001/floor0.00001。500M中間を保存するが中間は減衰前であり、学習量だけの効果として終端と比べない。科学計2,000,027,648、実CUDA保存再開262,144は別計上。

関連CPU5testsと新poolによる実CUDA stable→decay連続/再開一致を実行前条件とする。source/config/schema/pool reviewを凍結。実PID/boot/start ticks、logs、500更新ごとのcheckpoint、sampler/RNG/optimizer/scheduler/token countersを保存する。元UIはGPU中停止しwrapper finallyで復帰する。

## 段階3の評価と終了条件

両終端を同じdev256本文BPB/固定80生成/意味192/JBLiMP331/JCQA1119で比較し、全160生成を同じrubricで個別診断する。文法0破綻/1部分的・不自然/2局所的自然、関連性0条件逸脱/1部分一致/2条件保持、一貫性0矛盾・強反復/1弱い・冗長/2意味の通る展開。cap終了だけを文法0とせず、適切完結は実EOSかつ文脈に合う内容的な終わりだけ1。

原条件は一貫性の対照比+8/80以上・対応95%下限>0、反復非悪化、raw失敗0、BPB条件、保存Web対照比EOS+8等を維持。実用条件は一貫性・適切完結各27/80以上、EOS37/80以上、反復18/80以下。全一次条件通過時だけ新候補の全文89,416/生成400/長文40を実施し、親BPB+0.001以内など原全文条件を確認する。一次4800秒/条件付き全文1800秒が事前GPU上限。未達時はその結果を保存し、採用条件を緩めない。

現在は教材準備とCPU5tests完了。内容review・config凍結・GPU・評価・採否の実施結果は後続記録へ追記する。

段階2実行中: 凍結commit03346a7、hidden Windows21040/actual Linux239609/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks6902884。新poolによる実CUDA stable→decay連続/再開一致25項目成功（検証262,144は別）。対照500Mの中間を2026-10-05T07:49:44.684084Zに745.994秒で保存した。実追加500,006,912/総10,500,014,080/update320435、Web400,031,744/short99,975,168、EOS教師Web846,893/short1,105,092。中間SHA`c5658fc5891f30ebb007e58427d1453fcf9cb47687222411ae8078a0ff1344f3`を実ファイルと照合。評価を挟まず対照1Bへ継続中。新教材1Bと両終端評価・160内容・採否は未完了。元UIはGPU中停止した状態で、wrapperの復帰処理を終了後に実確認する。
