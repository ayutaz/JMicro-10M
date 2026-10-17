"""New80 DEV authored after actual TRAIN freeze; retain all five known suites."""
from collections import Counter
import json
from answer_learning_common import ROOT,RUN,DATA,save,ref,bound,read_json,digest,now
from prepare_answer_curriculum import DIRECTORY
from jmicro.tokenizer import Tokenizer
from jmicro.data import normalized

SINGLES={
'greeting':[
 ('ひと仕事終わりました。こんにちは。','こんにちは。お疲れさまでした。'),
 ('おはよう、まだ少し眠いけど起きたよ。','おはようございます。ゆっくり目を覚ましましょう。'),
 ('今日も話に来たよ。よろしく。','よろしくお願いします。今日は何を話しましょうか。'),
 ('こんばんは。少し雑談に付き合って。','こんばんは。何をお話ししましょうか。'),
 ('話を聞いてくれて助かった。またね。','どういたしまして。またお話ししましょう。'),
 ('そろそろ休みます。おやすみ。','おやすみなさい。ゆっくり休んでくださいね。'),
 ('ただいま。長い一日だった。','おかえりなさい。お疲れさまでした。'),
 ('初めてここに来ました。こんにちは。','こんにちは。よろしくお願いします。')],
'daily':[
 ('机の上に書類が積もった。最初に何をしよう。','必要な書類と不要な書類を分けてみませんか。'),
 ('寒い日に家でできる気晴らしを一つ挙げて。','好きな音楽を聴くのはいかがですか。'),
 ('朝の支度で忘れ物が多いんだ。工夫はある？','前の晩に持ち物を確認してまとめておきましょう。'),
 ('友達へ短いお礼を書きたい。最初の一文を考えて。','先日は手伝ってくれてありがとう。'),
 ('読書を始めたいけれど時間がない。どう始める？','一日五分だけ読む時間を作ってみませんか。'),
 ('夕飯のあと食器を片付けるのが面倒です。','まず一枚だけ洗ってみませんか。'),
 ('寝る前に明日の用意をしておきたい。何を確認する？','予定と持ち物を確認するとよさそうです。'),
 ('休日に絵を描いてみたい。何から描こうかな。','身近にあるコップを描いてみませんか。')],
'emotion':[
 ('続けていた練習の成果が出て、今日はうれしい。','努力が実ってうれしいですね。'),
 ('大切にしていたしおりをなくして悲しい。','大切な物をなくすと悲しいですね。'),
 ('頼まれたことを無事終えて安心したよ。','無事に終わってほっとしますね。'),
 ('明日は初めての発表で落ち着かない。','初めての発表は緊張しますね。深呼吸してみましょう。'),
 ('友人が約束を忘れていて、がっかりした。','楽しみにしていた分、がっかりしますね。'),
 ('長く探していた写真が見つかってうれしい。','見つかってよかったですね。'),
 ('今日は小さな失敗が続いて落ち込んでいる。','そんな日もありますね。少し休んでみませんか。'),
 ('丁寧にお礼を言ってもらえて心が温かくなった。','気持ちが伝わってうれしいですね。')],
'question_back':[
 ('図書館は月曜休み、美術館は火曜休みです。火曜に休むのはどちら？','美術館です。'),
 ('出発は八時、到着は九時半です。到着する時刻だけ答えて。','九時半です。'),
 ('南の棚に紙、北の棚には糸があります。紙はどこ？','南の棚です。'),
 ('赤い手袋は姉の物で、白い手袋は父の物です。父の手袋の色は？','白です。'),
 ('最初に宛名を書き、その後に切手を貼ります。先にする作業は？','宛名を書くことです。'),
 ('クッキーが九枚あり、三枚食べました。残りは何枚？','六枚です。'),
 ('展示の入場は無料ですが、冊子は有料です。無料なのは何？','展示への入場です。'),
 ('花壇の西側がバラで、東側がユリです。ユリがある方角は？','東側です。')],
'ambiguity':[
 ('ここを直してほしいです。直す場所はまだ示していません。','どこを直したいか教えてください。'),
 ('この言葉を訳して。言葉はこれから送ります。','訳したい言葉を送ってください。'),
 ('会場の行き方を知りたい。会場名はまだ伝えていません。','会場の名前を教えてください。'),
 ('お勧めの本を探したい。興味のある分野はまだ話していない。','どんな分野の本に興味がありますか。'),
 ('どの道を進むべき？現在地も目的地もまだ伝えていないよ。','現在地と目的地を教えてください。'),
 ('これの寸法を教えて。対象の写真や名前はまだありません。','何の寸法を知りたいか教えてください。'),
 ('二つの案を比較したい。内容はまだ説明していない。','それぞれの案の内容を教えてください。'),
 ('必要な布は二枚です。何枚必要か聞かれたらどう答える？','二枚です。')],
'role_boundary':[
 ('母が旅行した話をしています。旅行したのはあなたですか？','いいえ、旅行したのはお母さんです。'),
 ('小説の主人公の仕事は料理人です。あなたの実際の仕事になりますか？','いいえ、登場人物の仕事です。'),
 ('弟が友人に傘を渡しました。受け取った人は誰ですか？','弟さんの友人です。'),
 ('予約しようか相談しているところです。予約はもう済んでいますか？','いいえ、まだ予約は済んでいません。'),
 ('晴れたら出かけるかもしれません。外出は決定ですか？','いいえ、まだ決まっていません。'),
 ('あなたが昨日食べた夕食を、実体験として話して。','私は食事をしないので、夕食の実体験はありません。'),
 ('この写真は私の祖母が撮りました。撮影したのは誰？','あなたのお祖母さんです。'),
 ('架空の設定と断った上で、月に住む猫の一文を作って。','架空のお話です。月の猫は星を眺めていました。')],
'symbols':[
 ('使う番号は「R-73」です。番号だけを返してください。','R-73'),
 ('予定表には「16:25」とあります。その表記だけ返して。','16:25'),
 ('「vwx」を選びました。「yz」ではありません。選んだ文字列は？','vwx'),
 ('ファイル名を「memo_9」にしました。名前だけ答えて。','memo_9'),
 ('印は「◎」を使います。印だけで返事をして。','◎'),
 ('表示を「B36」から「B39」に更新しました。今の表示だけ答えて。','B39'),
 ('「右」「左」の札から「左」を外しました。残った文字は？','右'),
 ('伝票の値は「2,640」です。数字と記号をそのまま返して。','2,640')]
}

DIALOGUES={
'correction':[
 (['本は寝室に置く予定です。','寝室に置くのですね。','置き場所は寝室ではなく書斎でした。どこに置きますか？'],'書斎です。'),
 (['発送日は木曜日です。','木曜日ですね。','予定を変えて、土曜日に発送します。','土曜日に変わったのですね。','いまの発送予定日はいつ？'],'土曜日です。'),
 (['席は五つ必要です。','五つ用意するのですね。','一人欠席になったので、席は四つにします。必要な席はいくつ？'],'四つです。'),
 (['表紙は紺色にしようと思います。','紺色ですね。','やはり表紙を白色に変更しました。','白色に変更ですね。','採用した表紙の色を教えて。'],'白色です。'),
 (['会議は東館で行います。','東館ですね。','訂正です。東館は使わず、本館で行います。会議はどこ？'],'本館です。'),
 (['案内するのは小野さんです。','小野さんが案内するのですね。','担当が変わって、今は長谷川さんです。','長谷川さんが担当ですね。','現在の案内担当は誰でしょう？'],'長谷川さんです。'),
 (['買うのはバターです。','バターを買うのですね。','バターは不要でした。代わりにチーズを買います。買う物は？'],'チーズです。'),
 (['開場は十五時の予定でした。','十五時ですね。','開場が十六時半へ延期されました。','十六時半に変わったのですね。','延期後に入れるのは何時から？'],'十六時半です。')],
'followup':[
 (['次の休みには陶芸を体験したいです。','陶芸を体験したいのですね。','私が体験したいと言ったのは何？'],'陶芸です。'),
 (['店で梨を買ってきました。','梨を買ったのですね。','買ってきた果物をもう一度教えて。'],'梨です。'),
 (['作文のテーマは海です。','海について書くのですね。','締切は来週になります。','来週が締切ですね。','私の作文は何についてでしたか？'],'海です。'),
 (['昨日は台所の戸を修理しました。','台所の戸を直したのですね。','昨日どこの戸を直したと話しましたか？'],'台所の戸です。'),
 (['旅行先は水族館のある町です。','水族館のある町へ行くのですね。','移動には電車を使います。','電車で向かうのですね。','移動手段として伝えたのは何でしたか？'],'電車です。'),
 (['借りているのは園芸の本です。','園芸の本なのですね。','何についての本を借りていましたか？'],'園芸の本です。'),
 (['父への贈り物は靴下にしました。','靴下を贈るのですね。','来月、父に渡す予定です。','来月渡すのですね。','贈り物として選んだ物は何？'],'靴下です。'),
 (['休み時間にヨーグルトを食べました。','ヨーグルトを食べたのですね。','休み時間に食べた物を覚えていますか？'],'ヨーグルトです。')],
'context':[
 (['右の戸棚には皿、左の戸棚にはコップがあります。','右に皿、左にコップですね。','コップを取りたい場合、どちらの戸棚ですか？'],'左の戸棚です。'),
 (['弟は財布を、姉は切符を持っています。','弟さんが財布、お姉さんが切符ですね。','私はお弁当を持っています。','あなたはお弁当ですね。','切符を持っている人だけ教えて。'],'お姉さんです。'),
 (['先週は博物館、今週は植物園を訪れました。','今週は植物園なのですね。','今週訪れた所はどちらでしたか？'],'植物園です。'),
 (['夕方に散歩をして、午前には買い物をします。','午前に買い物、夕方に散歩ですね。','午後は家で過ごします。','午後は在宅なのですね。','買い物に行く時間帯を教えて。'],'午前です。'),
 (['届けるのは叔父で、包むのは叔母です。','叔父さんが届け、叔母さんが包むのですね。','包む作業を受け持つのは誰？'],'叔母さんです。'),
 (['黒い紐は使わず、白い紐を使います。','使うのは白い紐ですね。','使わない方の紐の色を答えて。'],'黒です。'),
 (['水曜に練習、金曜に本番です。','水曜が練習、金曜が本番ですね。','練習だけを木曜へ移しました。','練習は木曜ですね。','本番の日は変えていません。','本番は金曜のままですね。','練習と本番は、それぞれ何曜日ですか？'],'練習は木曜、本番は金曜です。'),
 (['紙の袋にはパンを入れ、布の袋にはタオルを入れました。','紙袋にパン、布袋にタオルですね。','タオルを取り出すのは何の袋から？'],'布の袋です。')]
}


def main():
    manifest=read_json(DIRECTORY/'manifest.json');assert manifest['status']=='TRAIN_frozen_before_new_DEV'
    target=RUN/'curriculum_DEV_preparation.json';assert not target.exists()
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    questions=set();histories=set()
    for arm in ('C0','C1'):
        for line in bound(manifest['arms'][arm]['records']).read_text().splitlines():
            row=json.loads(line)
            for i in row['target_message_indices']:
                questions.add(normalized(row['messages'][i-1]['text']))
                histories.add(digest(json.dumps(row['messages'][:i],ensure_ascii=False,sort_keys=True)))
    authored=[];cases=[]
    for category in ('greeting','daily','emotion','question_back','ambiguity','role_boundary','symbols','correction','followup','context'):
        entries=SINGLES.get(category,DIALOGUES.get(category));assert len(entries)==8
        for i,(prompt,answer) in enumerate(entries):
            text=[prompt] if isinstance(prompt,str) else prompt
            messages=[dict(role='user' if j%2==0 else 'assistant',content=t) for j,t in enumerate(text)]
            assert normalized(messages[-1]['content']) not in questions,(category,i)
            assert tok.chat_prompt(messages,992)[1]==0 and 2<=len(tok.encode(answer))+1<=32
            uid=f'answer-unseen-{category}-{i+1:02}'
            cases.append(dict(id=uid,family_id=uid,split='dev',category=category,messages=messages,
                checks=['入力中の対象・条件・話者に沿って、最後の質問または依頼へ自然に答える。',
                    '訂正は最新の指定を使い、推測した事実や実体験を足さない。',
                    '単語一致・停止だけでは合格にせず、文法・関連性・履歴文脈を別々に採点。']))
            authored.append(dict(id=uid,dataset='new_DEV',split='dev',messages=messages+[dict(role='assistant',content=answer)]))
    contexts=[r for r in cases if len(r['messages'])>1]
    assert len(cases)==80 and len(contexts)==24 and sum(sum(m['role']=='user' for m in r['messages']) for r in contexts)==59
    directory=DIRECTORY/'dev_suites';directory.mkdir(exist_ok=True)
    def dump(path,rows):
        assert not path.exists();path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
    dump(directory/'new.jsonl',cases);suites={'new':ref(directory/'new.jsonl')}
    old=read_json(ROOT/'configs/phase7/chat-natural-sft-20261017.json')
    for name,reference in old['suites'].items():
        renamed='previous_new' if name=='new' else name
        raw=bound(reference);rows=[json.loads(line) for line in raw.read_text().splitlines()]
        assert len(rows)==80 and all(r['split']=='dev' for r in rows)
        destination=directory/f'{renamed}.jsonl';assert not destination.exists();destination.write_bytes(raw.read_bytes())
        suites[renamed]=ref(destination)
    nll=[json.loads(line) for line in bound(old['NLL']).read_text().splitlines()]
    assert len(nll)==208
    for row in authored:nll.append(dict(row,id='new-'+row['id']))
    extra=read_json(DIRECTORY/'supplement_unique_TRAIN.json')
    for row in sorted(extra,key=lambda r:digest('answer-NLL42:'+r['doc_id']))[:32]:
        nll.append(dict(id='candidate-'+row['doc_id'],dataset='supplement_TRAIN',split='train',messages=row['messages']))
    assert len(nll)==320
    dump(DIRECTORY/'nll_fixed.jsonl',nll)
    save(DIRECTORY/'new_DEV_authored.json',dict(created_at=now(),author='Codex nonblind, not independent human',targets=authored,
        TRAIN_manifest=ref(DIRECTORY/'manifest.json'),TRAIN_frozen_before_new_DEV=True,protected_TEST_used=False))
    save(target,dict(created_at=now(),status='all6_DEV_suites_fixed',TRAIN_manifest=ref(DIRECTORY/'manifest.json'),
        TRAIN_frozen_before_new_DEV=True,new_authored=ref(DIRECTORY/'new_DEV_authored.json'),suites=suites,NLL=ref(DIRECTORY/'nll_fixed.jsonl'),
        NLL_targets=320,final_responses=2628,full_content_review_required=True,
        prompt_exact_overlap_with_TRAIN=0,semantic_ancestry_overlap_not_fully_excluded=True,
        generalization_disclosure='New wording and semantic compositions, reversed mention orders, non-TRAIN entities/objects and tasks; familiar task concepts remain',
        original_known_suites=old['suites'],protected_TEST_used=False,new_TEST_created=False,new_training_updates=0))
    print('New80 DEV plus all5 known suites frozen;2628 final responses and320 NLL targets')


if __name__=='__main__':main()
