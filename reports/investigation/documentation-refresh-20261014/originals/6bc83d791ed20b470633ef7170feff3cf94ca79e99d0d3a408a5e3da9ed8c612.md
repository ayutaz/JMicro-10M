# 文書連結依存の三条件比較：実行契約

2026-10-05 JST。「3まで進めてください」で、直前の三項目（同教材の三条件、約25M教師tokens、条件付きWeb混合100Mと日本語総合評価）を実行する。過去の結果66/67と元10B・Tokenizerは保持。

1. 結果67のcompact1000全文・55,273tokensを共通入力として、fixed（現在のblock連結）、shuffle（毎周全文の順序を変更して連結）、isolated（1文書1行、他文書の参照なし、位置は文書先頭から）を固定する。教師は全文body＋EOS。PAD/BOSを教師に数えず、他文書やChat役割を追加しない。文書順変更と遮断＋位置resetの効果を区別するが、最後の条件で遮断と位置resetの個別効果を分離したとはしない。
2. 全三条件を元final10Bから各25,000,000 **教師tokens**で実行する。valid入力・physical入力/PAD・body bytes・EOS教師・更新数・GPU時間を別記録する。LR0.0001、教師予算90%まで維持、残り10%で0.00001まで減衰。fixed/shuffleは実測済み32×1024 compiled Flash、isolatedは256×128 eager mathから実CUDA有限step/保存再開で確認する。新経路の連続4更新と2→保存→2更新を全三条件で比較し、重み/optimizer/scheduler/RNG/sampler/教師量/byte/lossの一致を学習前に要求する。学習GPU各300秒以内、全段階の累積GPU2400秒以内。
3. 共通の固定train100と結果67dev100を参照診断し、学習開始前に固定する未確認dev100を主診断とする（既知構文50/未学習構文50、過去dev原文と重ならない反転50組）。目標は単独train90%以上・新dev70%以上。fixed以外で目標を満たす条件があれば、同じ教材を使用して元10BからWeb80M＋教材20Mの教師tokensを、fixedと候補の各100Mで比較する。候補選択は新dev正答率→反転両方正答率→shuffle優先という固定順。双方のWebは同じ保存cursor、本文EOSの同予算。純粋な三条件の終端から混合を開始しない。

新終端は同じdev256 BPB、意味192/JBLiMP331/JCQA1119、固定dev80生成のEOS/反復/UTF-8と全原文の個別内容理由で評価する。短い合成教材への適応と一般日本語の品質を区別する。新条件devの正答をBase採用条件に代用しない。各条件の合否を変更せず、目標未達なら100Mは未開始と明記し、三条件の評価/採否/report/local commit/元10B UI確認まで行う。

最大科学教師tokensは75M＋200M=275M、実CUDA保存再開24更新は別の実測会計。訓練中のvalid入力カウンタはPADを除き、physical計算量は別に残す。各完了更新でoptimizer/scheduler/RNG/sampler/教師・valid入力・bytesを保存、周期checkpointとログ/PID/boot/start ticksを永続化。既存GPU jobを確認し、UIを停止してからGPU lockを取得、終了時に元UIを復帰する。checkpoint/source/data/budgetを固定し、再開は実checkpointから行う。

原の一貫性・適切完結・BPB・EOS条件を維持する。品質条件が一次で満たされた場合の全文確認は新契約の予算内で判断する。20B/50B/Chat、保護test、Tokenizer再学習、push/公開は対象外。次の追加実験を自動で始めず、確認済みlocal commitで停止する。
