"""Persist non-blind qualitative notes, kept separate from token-departure metrics."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now

RUN=ROOT/'reports/phase6/generation-transfer-20261006'
TRAIN_NOTES=[
'別の宝物探しとして展開し完結。goldとの不一致だけでは意味破綻としない。',
'空き地の導入を重ねて光る石/過去世界へ展開。長い創作としては完結。',
'かぼちゃから野菜育成へ話題を広げ完結。goldとは別展開。',
'「星たちは彼女に、昔の人々の話を聞きました」は聞く主体/格が不自然。',
'貝と過去の海の冒険へ展開し完結。日常文への一般化ではない。',
'雪だるま作りと友人の助けへ展開し完結。',
'夢を追いかける/夢を持つ/夢を叶えるの言換えが続き具体的進展が弱い。',
'まだ植えたい段階から「木が枯れてしまった」へ飛び、植えると元気になる因果も弱い。',
'空を飛ぶ夢を再述して時間の大切さへ移る。完結するが進展が乏しい。',
'友達が来て笑顔になる前の「しかし」が対立を示していない。',
'石の由来と友達との交流へ展開し完結。別の創作として許容。',
'花を見つけ育てた後に毎日育てると決める再述。大きな矛盾は確定しない。',
'「風が強くなり、風が強くなった」の局所反復と風に乗る展開。',
'ダンスと友人の短い完結。token不一致を誤りとしない。',
'星と夢の世界へ展開。幻想そのものを意味破綻としない。',
'一人遊びで悲しみ友人が助ける。理由/つながりは薄いが完結。',
'紙芝居画家から日本絵画史の一般論へ移り同一文を反復、256でも非停止。',
'既に擬人化されたクラゲの友人/ダンスを続け完結。',
'友達と遊んでいる導入の後に友達が来ないと気付き、状態変化の説明なし。',
'「その石は、友達と一緒にその石を触りました」で石が触る主体になる。',
'楽器の時間旅行能力を追加。幻想設定は別展開であり単独では誤りとしない。',
'花から友人との遊びへ移り、最後に花を大切にする理由が弱い。',
'「朝から朝」の時系列と昼食を食べ続ける反復、256でも非停止。',
'本を通じて世界へ入る同趣旨を重ねる。EOSは出るが内容の進展が弱い。',
'伝統学習から協力/友達へ移り完結。具体性は低い。',
'宝物を分け合う導入の後「そんな」を反復、256でも非停止。',
'prefixの「何か見つけた」を引用して反復、256でも非停止。',
'物語作りから友人との冒険を作り完結。明示的な破綻は確定しない。',
'木を昔の人が使った物として扱い森を守る力を追加。因果の説明が薄い。',
'光る石と友人の思い出へ展開し完結。gold不一致だけでは誤りとしない。',
'新クラス/一人の部屋から友達との遊びへ移り状態変化を説明していない。',
'自分の絵を見る→美術館に行きたいという同一展開を反復してからEOS。']

DEV_NOTES=[
'同じ治療/健康の語を反復して説明が進まない。',
'研究所の運営/研究開発を循環的に説明する。',
'勉強する上でという導入を反復して内容が進まない。',
'保湿の一般論から同趣旨の反復へ。最初の文単独では誤りを確定しない。',
'ヒゲナガガガ等の語形破綻/同じ分布説明の反復。',
'診療所前の階段/第3以降のターミナルへ根拠なく増殖する。',
'血糖値上昇抑制の同一説明を反復。',
'吉神/福徳/方位を循環的に説明する。',
'対象の説明を進めず事業主という項目を反復。',
'介護保険の一般論/見出しを反復。',
'スポールブールをゲームの世界観/ゲームに入る意味と循環定義する。',
'腰痛の原因/筋肉の緊張の反復。',
'農園から農家イベントへ移る根拠がなく同一説明を反復。',
'会社のために働くのではなく会社のために働くという対立の崩壊。',
'戦死者家族/遺体/列車の関係が崩れ同じ句を反復。',
'貸す投資家がいないという条件を売りたい投資家がいない条件へ変える。',
'prefix再述/プレイヤーのプレイヤーという循環と反復。',
'引用閉じは出るが印税/出版/手記の関係が混乱し反復。',
'税金対策には税金対策が必要/一番という同語反復。',
'放送法の規定に基づきという句を反復。',
'硝酸性窒素を処理方法と混同/酸性窒素等へ語形逸脱し反復。',
'prefixの為替情報を再述して反復。',
'パズルの世界という説明に移り反復。',
'中国/韓国/韓国と対象が重複し文化という語が反復。',
'割安の説明から割高という逆の説明へ移る/保険定義を反復。',
'料理教室のテーマを再述して反復。',
'心得を説明せず守り方という見出しを反復。',
'PEEPを血圧上昇の設定とする同一説明を反復。医学的正確性の認証ではない。',
'土器体験から森への話題逸脱/土器づくりの同義反復。',
'産後講座へは関連するが講師/講座を反復し完結しない。',
'山の中に入るという句を反復。',
'らしさ/象徴化の表層を循環的に説明し反復。']

if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    cases=read_json(RUN/'cases.json');models={a:read_json(RUN/(a+'-result.json')) for a in ('control','diverse')}
    reviews=[]
    for arm,model in models.items():
        for i,case in enumerate(cases):
            short=model['greedy64'][i];long=model['greedy256'][i]
            note=(TRAIN_NOTES[i] if arm=='diverse' else '導入から別の説明/暗記場面へ移るか同じ句を反復。'+('池への散歩へ場面が移る。' if i==30 else '')) if i<32 else DEV_NOTES[i-32]
            reviews.append(dict(arm=arm,id=case['id'],case_index=i,source=case['source'],
                prefix=case['prefix'],generated64=short['text'],generated256=long['text'],
                first_token_departure=short['first_token_departure'],first_repeated4gram=long['first_repeated_4gram'],
                diagnosis=note,semantic_first_position='earliest identifiable issue is described in prose; raw token departure is not semantic onset',
                long_stop=long['stop_reason'],new_stop_after64=short['stop_reason']!='eos' and long['stop_reason']=='eos'))
    result=dict(created_at=now(),cases_sha256=sha256(RUN/'cases.json'),
        raw_sha256={a:sha256(RUN/(a+'-result.json')) for a in models},reviews=reviews,
        review_method='Non-blind Codex qualitative diagnosis of64-token outputs and diverse extended outputs; control/dev extended recurrence additionally indicated by raw token trace. Not independent human scoring or a replacement quality suite.',
        decision='Length matters on trained narrative examples; official Web dev still fails after256. Prefer short complete curriculum with explanation/general Japanese and continuation-vs-fresh strategy; no EOS-weight-only experiment now.',
        numerical_failures72='unresolved; no new evidence requires changing frozen model/trainer numerics',
        scientific_teacher_tokens=0,protected_test_used=False)
    write_json(RUN/'review.json',result)
    write_json(ROOT/'reports/phase6/generation_transfer_review.json',result)
