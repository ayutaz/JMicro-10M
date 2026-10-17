"""Author new DEV only after paired TRAIN freeze; carry all six old suites."""
import json
import hashlib
from collections import Counter
from prepare_chat_recovery_train_v3 import original
from answer_learning_common import ROOT,save,ref,bound,read_json,now
from jmicro.tokenizer import Tokenizer
from jmicro.data import normalized

RUN=ROOT/'reports/phase7/chat-recovery-20261018'
DATA=original.DATA
SINGLES={
'greeting':[
('おはよう。今朝も少しだけ話そう。','おはようございます。何を話しましょうか。'),
('やあ、こんにちは。初めて話しかけます。','こんにちは。よろしくお願いします。'),
('こんばんは。寝る前にひとこと挨拶に来たよ。','こんばんは。ゆっくりお休みください。'),
('聞いてもらったおかげで気持ちが軽くなった。ありがとう。','少し楽になったならよかったです。'),
('今日はもう終わり。また話すときまで、さようなら。','さようなら。またお話ししましょう。'),
('用事を済ませて帰ってきたよ。ただいま。','おかえりなさい。お疲れさまでした。'),
('初めまして。短い会話を楽しめたらうれしいです。','初めまして。よろしくお願いします。')],
'emotion':[
('初めて焼いたパンがうまく膨らんでうれしい。','うまく焼けてうれしいですね。'),
('大事にしていた鉢が割れて、悲しい気持ちです。','大切な鉢が割れると悲しいですね。'),
('明日の初出勤を思うと、少し不安なんだ。','初めては不安ですね。少しずつ慣れていきましょう。'),
('友人と仲直りできて、ようやく安心しました。','仲直りできてよかったですね。'),
('待ち望んでいた荷物が届かず、がっかりしている。','楽しみにしていた分、がっかりしますね。'),
('重い荷物を運んでくたくた。少し休みたい。','お疲れさまです。ゆっくり休んでください。'),
('練習していた曲を弾けるようになったよ。','練習の成果が出てうれしいですね。')],
'daily':[
('雨の日に部屋でできる遊びを一つだけ挙げて。','折り紙はいかがですか。'),
('帰宅すると鞄を床に置いてしまいます。片付けの工夫を一つ教えて。','鞄を置く場所を決めておきましょう。'),
('朝食の後に皿がたまります。小さく始める方法は？','まず一枚だけ洗ってみましょう。'),
('散歩を習慣にしたいけど続きません。まず何分から始めよう。','五分ほどから始めてみませんか。'),
('机がいっぱいです。まず何を片付ければいいかな。','使わない物を一つ片付けてみましょう。'),
('友人へ短いお礼を伝えたい。手伝ってくれたことへの一文を考えて。','手伝ってくれてありがとう。助かりました。'),
('寝る前につい予定を忘れます。翌朝のためにできることは？','明日の予定をメモしておきましょう。')],
'binding':[
('母は切符を買い、兄は席を探します。席を探すのは誰でしょう。','兄です。'),
('手袋は奥の箱、帽子は手前の箱です。帽子を取る箱はどちら？','手前の箱です。'),
('月曜は練習、日曜は発表です。発表する曜日を教えて。','日曜です。'),
('昨日は港へ、今日は病院へ行きました。今日の行き先は？','病院です。'),
('私が妹へ辞書を貸しました。借りた側は誰ですか。','妹さんです。'),
('飲むのは豆乳にします。牛乳は選びません。選んだ飲み物は？','豆乳です。'),
('使うのは細い筆で、太い筆は使いません。使わない方はどちら？','太い筆です。')],
'numbers':[
('二枚の紙と三枚の紙を合わせると何枚でしょう。','五枚です。'),
('六個の飴から一個食べました。残るのは何個ですか。','五個です。'),
('三冊に二冊を加えた冊数を教えてください。','五冊です。'),
('八本あった鉛筆を二本渡しました。手元には何本？','六本です。'),
('必要な皿は五枚です。数を変えずに、何枚必要か答えて。','五枚です。'),
('箱のラベルに「17」とあります。書かれた数だけ答えて。','17'),
('予定は九時からです。開始時刻をそのまま答えてください。','九時です。')],
'format':[
('注文の符号は「P-62」です。符号のみを返してください。','P-62'),
('保存した名前は「list_4」です。その名前だけ返して。','list_4'),
('表には「07:35」と書いてあります。この五文字だけを返して。','07:35'),
('選択した文字は小文字の「fox」です。その三文字だけ答えて。','fox'),
('使う印は「△」です。その印一つだけで返事をしてください。','△'),
('値は「5,240」です。コンマも含め、その表記だけ返して。','5,240'),
('合図は「雨 / 晴」です。引用符なしでそのまま返して。','雨 / 晴')],
'missing':[
('私の荷物の重さを教えて。まだ荷物の説明はしていません。','荷物の説明や重さの測定値を教えてください。'),
('二人のどちらに頼もうかな。二人の特徴はこれから話します。','それぞれどんな人か教えてください。'),
('書き直してほしい一文があります。本文はまだ送っていません。','書き直したい一文を送ってください。'),
('行きたい場所への道順を教えて。出発地も行き先もまだ秘密です。','出発地と行き先を教えてください。'),
('私が昨日選んだ色を覚えてる？この会話ではまだ色を伝えていません。','まだ色を伺っていません。何色ですか。'),
('会議の終了時刻は分かる？開始時刻も長さもまだ話していません。','まだ分かりません。開始時刻と長さを教えてください。'),
('この材料で料理を決めてほしいです。材料名は次の発言で伝えます。','材料名を教えてください。')],
'role':[
('兄が水泳を習ったという話です。習ったのはあなたでしたか。','いいえ、お兄さんです。'),
('物語の猫は船長です。あなたが本当に船長だという意味になりますか。','いいえ、物語の猫の設定です。'),
('私は明日店に行くか迷っています。もう行ったことになっていますか。','いいえ、まだ迷っている段階です。'),
('この説明では祖父が写真を撮りました。撮った人だけ答えて。','お祖父さんです。'),
('友人が私に箱を渡しました。箱を受け取ったのは誰ですか。','あなたです。'),
('あなた自身が昨夜眠った場所を実体験として教えて。','私は眠らないので、その実体験はありません。'),
('作り話と分かる形で、雲に住む鳥の短い文を一つ作って。','作り話です。雲の鳥は朝の風を待ちました。')]
}

DIALOGUES={
'followup':[
(['子猫の名前はメイ、使う器は白です。','メイという子猫で、器は白ですね。','今日は庭の落ち葉を集めました。','庭を片付けたのですね。','子猫の名前だけ確認したいです。','メイです。','夕方は絵を描くつもりです。','絵を描く予定なのですね。','子猫の情報は変えません。','先ほどの情報のままですね。','子猫の名前と器の色を二つとも教えて。'],'名前はメイ、器は白です。'),
(['作る小物は布の栞です。','布の栞ですね。','使う布は麻にしました。','麻の布を使うのですね。','何の布で栞を作る予定でしたか。'],'麻です。'),
(['私は明日の朝、植物園に行きます。','植物園へ行くのですね。','明日の行き先を思い出して教えて。'],'植物園です。'),
(['晩ご飯はカレーを温め直します。','カレーを温め直すのですね。','晩ご飯は何と伝えましたか。'],'カレーです。'),
(['家の鉢にはミントを植えました。','ミントを植えたのですね。','鉢に植えた植物の名前は？'],'ミントです。'),
(['借りている楽器はフルートです。','フルートを借りているのですね。','借りている楽器は何でしたか。'],'フルートです。'),
(['窓辺に置いた写真は祖父の写真です。','お祖父さんの写真なのですね。','写真に写っているのは誰でしょう。'],'お祖父さんです。'),
(['今週は木曜に歯医者へ行きます。','木曜に歯医者ですね。','歯医者へ行く曜日を教えて。'],'木曜です。')],
'correction':[
(['小箱の色は黄色、届ける日は金曜です。','黄色の小箱を金曜に届けるのですね。','小箱の色だけ紫へ変えます。','色は紫へ変更ですね。','今の小箱は何色ですか。','紫です。','今日は窓ガラスを磨きました。','窓がきれいになったのですね。','届ける日だけ日曜へ直します。','日曜へ変更ですね。','小箱の最新の色と届ける日を両方教えて。'],'色は紫、届ける日は日曜です。'),
(['訪ねる場所は本屋です。','本屋ですね。','本屋はやめて花屋に変えます。','花屋へ変更ですね。','今、訪ねるつもりなのはどこ？'],'花屋です。'),
(['使うリボンは赤でした。','赤のリボンですね。','青のリボンに直しました。今の色を答えて。'],'青です。'),
(['会う相手は父の予定でした。','お父さんですね。','父は来られないので母に変更します。会う相手は？'],'お母さんです。'),
(['袋は三つ必要だと伝えました。','三つですね。','数え直したら二つで足りました。今必要な袋は何個？'],'二つです。'),
(['本棚は西の壁に置く予定です。','西の壁ですね。','訂正です。東の壁に置きます。最後の位置はどちら？'],'東の壁です。'),
(['バスに乗るのは北の入口です。','北の入口ですね。','南の入口に変更し、その変更を取り消しました。最後はどこ？'],'北の入口です。'),
(['飲み物は紅茶、菓子はクッキーです。','紅茶とクッキーですね。','菓子だけケーキに変えます。飲み物はそのままです。今の組合せは？'],'紅茶とケーキです。')],
'context':[
(['姉は笛、兄は太鼓を担当します。','お姉さんが笛、お兄さんが太鼓ですね。','私は歌を担当します。','あなたは歌ですね。','太鼓を担当する人は誰でしたか。'],'お兄さんです。'),
(['小さい缶に砂糖、大きい缶に塩を入れました。','小さい缶が砂糖、大きい缶が塩ですね。','塩の缶は大きい方と小さい方のどちら？'],'大きい方です。'),
(['父は電車、母はバスで帰ります。','お父さんが電車、お母さんがバスですね。','バスを使う人だけ教えてください。'],'お母さんです。'),
(['朝は読書、昼は散歩、夜は片付けをします。','三つの予定ですね。','散歩はどの時間帯ですか。'],'昼です。'),
(['青の札を先に取り、そのあと白の札を取ります。','青のあと白ですね。','先に取る札の色はどれ？'],'青です。'),
(['図書館は無料、映画館は有料です。','図書館は無料なのですね。','お金が必要なのはどちらですか。'],'映画館です。'),
(['叔父が箱を包み、叔母が箱を届けます。','叔父さんが包み叔母さんが届けるのですね。','届ける担当の人を答えて。'],'叔母さんです。'),
(['赤い袋は弟の物で、黒い袋は姉の物です。','弟さんが赤、お姉さんが黒ですね。','姉の袋の色を教えて。'],'黒です。')]
}


def main():
    manifest=read_json(DATA/'manifest.json');assert manifest['status']=='TRAIN_frozen_before_new_DEV'
    target=RUN/'DEV_preparation.json';assert not target.exists()
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    questions=set()
    for arm in ('C0','C1'):
        for line in bound(manifest['arms'][arm]['records']).read_text().splitlines():
            row=json.loads(line)
            for index in row['target_message_indices']:questions.add(normalized(row['messages'][index-1]['text']))
    cases=[];targets=[]
    for category,entries in {**SINGLES,**DIALOGUES}.items():
        assert len(entries)==(8 if category in DIALOGUES else 7)
        for i,(text,answer) in enumerate(entries):
            texts=[text] if isinstance(text,str) else text
            messages=[dict(role='user' if j%2==0 else 'assistant',content=t) for j,t in enumerate(texts)]
            assert normalized(messages[-1]['content']) not in questions,(category,i)
            assert tok.chat_prompt(messages,992)[1]==0 and 2<=len(tok.encode(answer))+1<=32
            uid=f'recovery-unseen-{category}-{i+1:02}'
            cases.append(dict(id=uid,family_id=uid,split='dev',category=category,messages=messages,
                checks=['最後の質問へ直接答え、人物と属性・否定・最新訂正・要求した情報数を保つ。',
                        '指定形式・不足情報を守り、未提示の事実や自分の実体験を創作しない。',
                        '文法・関連性・履歴文脈を別に採点し、名詞一致や停止だけで合格にしない。']))
            targets.append(dict(id=uid,dataset='new_DEV',split='dev',messages=messages+[dict(role='assistant',content=answer)]))
    contexts=[r for r in cases if len(r['messages'])>1]
    assert len(cases)==80 and len(contexts)==24 and sum(sum(m['role']=='user' for m in r['messages']) for r in contexts)==59
    directory=DATA/'dev_suites';directory.mkdir()
    def dump(path,rows):
        with path.open('x',encoding='utf-8') as stream:
            for row in rows:stream.write(json.dumps(row,ensure_ascii=False)+'\n')
    dump(directory/'new.jsonl',cases);suites={'new':ref(directory/'new.jsonl')}
    old=read_json(CONFIG:=ROOT/'configs/phase7/answer-curriculum-resource-v2-20261017.json')
    for name,value in old['suites'].items():
        renamed='curriculum' if name=='new' else name
        destination=directory/f'{renamed}.jsonl';destination.write_bytes(bound(value).read_bytes());suites[renamed]=ref(destination)
    nll=[json.loads(line) for line in bound(old['NLL']).read_text().splitlines()];assert len(nll)==320
    for index,row in enumerate(nll):
        if row['dataset']=='new_DEV':row['dataset']='previous_new_DEV' if index<208 else 'curriculum_DEV'
    nll+=targets
    authored=[json.loads(line) for line in (DATA/'authored_TRAIN.jsonl').read_text().splitlines()]
    for family in ('name','preference','correction','quantity','owner','literal','arithmetic','missing'):
        for row in [r for r in authored if r['family']==family][:4]:
            nll.append(dict(id='transformed-'+row['doc_id'],dataset='transformed_TRAIN',split='train',messages=row['messages']))
    assert len(nll)==432;dump(DATA/'nll_fixed.jsonl',nll)
    save(DATA/'new_DEV_authored.json',dict(created_at=now(),author='Codex nonblind',targets=targets,TRAIN_manifest=ref(DATA/'manifest.json'),TRAIN_frozen_before_new_DEV=True))
    save(target,dict(created_at=now(),status='all7_DEV_suites_fixed',TRAIN_manifest=ref(DATA/'manifest.json'),TRAIN_frozen_before_new_DEV=True,
        source=ref(__file__),new_authored=ref(DATA/'new_DEV_authored.json'),suites=suites,NLL=ref(DATA/'nll_fixed.jsonl'),NLL_targets=432,
        final_suite_responses=3066,public100_responses=400,total_main_responses=3466,context_user_turn_distribution=dict(Counter(sum(m['role']=='user' for m in r['messages']) for r in contexts)),
        exact_final_question_overlap_with_TRAIN=0,semantic_ancestry_overlap_not_fully_excluded=True,old_config=ref(CONFIG),new_TEST=False,new_training_updates=0))
    print('Frozen newDEV80/24 families/59own turns; all6 old suites; NLL432; total3466 final responses',flush=True)


if __name__=='__main__':main()
