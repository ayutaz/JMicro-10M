"""Prospectively fixed diagnostic:100 cases/200 actual CPU chat API responses.

Open diagnostic only, not sealed TEST or a representative population sample.
Keep the deployed checkpoint and greedy32 decoding, retain all failed replies.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[1]
RUN=ROOT/'reports/phase7/chat-quality-100-20261017'
CHECKPOINT='b5cb947c2d580e8ec4a080cfa71571a5e59baa2d24272c4229634799c913bc61'
URL='http://127.0.0.1:7864'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def read(path):return json.loads(path.read_text(encoding='utf-8-sig'))


def cases():
    rows=[]
    def add(category,text,expected,objective=False,history=None):
        rows.append(dict(id=f'{category}-{sum(r["category"]==category for r in rows)+1:02d}',category=category,
            mode='provided' if history else 'single',objective=objective,
            turns=[dict(user=text,expected=expected,objective=objective)],history=history or []))
    for text,expected in [
        ('おはようございます。これから一日を始めます。','朝の挨拶を返す。自分の生活体験は作らない。'),
        ('こんにちは。少し雑談しませんか。','挨拶か会話の申し出への自然な返答。'),
        ('こんばんは。今日の用事が終わりました。','夜の挨拶や労い。昼や朝と取り違えない。'),
        ('初めまして。よろしくお願いします。','初対面の挨拶に自然に応じる。'),
        ('話を聞いてくれて、ありがとう。','感謝を自然に受け止める。'),
        ('今日はここまでにします。また今度。','終了と別れを受け止める。新しい質問で引き止めない。'),
        ('そろそろ眠ります。おやすみなさい。','就寝の挨拶を返す。'),
        ('ただいま。家に帰ってきました。','帰宅の挨拶や報告に応じる。'),
        ('今から出かけます。いってきます。','出発の挨拶を受け止める。帰宅済みとしない。'),
        ('しばらく話せませんでしたが、また来ました。','再訪を迎える。未提供の過去の会話は作らない。')]:add('greeting',text,expected)
    for text,expected in [
        ('試験が終わって、ほっとしました。','試験後の安心への自然な反応。'),
        ('作った料理を褒めてもらえて嬉しいです。','喜びを自然に受け止める。'),
        ('楽しみにしていた催しが中止で残念です。','残念さを自然に受け止める。'),
        ('明日の面接を考えると緊張します。','緊張への自然な反応。面接済みとしない。'),
        ('今日は歩き回って疲れました。','疲れへの自然な労いや休息の提案。'),
        ('なくした鍵が見つかって安心しました。','鍵が見つかった安心を受け止める。'),
        ('本棚を片付けたら、読みかけの本が見つかりました。','片付けと本の発見に関連した反応。'),
        ('昼ご飯は作らず、昨日の残りのスープを温めました。','残りのスープを温めた報告に応じる。別の料理を作らない。'),
        ('雨だったので散歩をやめて、家で本を読みました。','屋内の読書に応じる。散歩したとは言わない。'),
        ('友達から久しぶりに便りが届き、元気が出ました。','友人の便りと喜びに関連した反応。')]:add('daily_emotion',text,expected)
    for text,expected in [
        ('私の名前は「かな」です。私の名前は何ですか。','かな。'),
        ('飼い犬の名前は「マル」です。犬の名前を教えて。','マル。'),
        ('買った果物はみかんです。何を買いましたか。','みかん。'),
        ('傘は玄関に置きました。傘はどこですか。','玄関。'),
        ('今日は木曜日です。今日は何曜日ですか。','木曜日。'),
        ('会う場所は市役所です。待ち合わせはどこですか。','市役所。'),
        ('読む本の題名は「海の道」です。題名は何ですか。','海の道。'),
        ('飲み物は牛乳ではなく水にします。何を飲みますか。','水。牛乳ではない。'),
        ('駅ではなく郵便局へ向かいます。どこへ行きますか。','郵便局。駅ではない。'),
        ('使う紙は白ではなく黄色です。紙は何色ですか。','黄色。白ではない。')]:add('direct',text,expected,True)
    for text,expected in [
        ('姉は帽子、弟は手袋を持ちます。手袋を持つのは誰ですか。','弟。姉ではない。'),
        ('赤い箱には鉛筆、青い箱には消しゴムがあります。鉛筆はどちらの箱ですか。','赤い箱。'),
        ('午前は掃除、午後は読書をします。午後にすることは何ですか。','読書。'),
        ('上の棚に茶碗、下の棚に皿を置きました。皿があるのはどちらですか。','下の棚。'),
        ('父が母に鍵を渡しました。鍵を受け取った人は誰ですか。','母。'),
        ('小さい袋は空で、大きい袋に本があります。本があるのはどちらですか。','大きい袋。'),
        ('先に手を洗い、次に食事をします。最初に何をしますか。','手を洗う。'),
        ('兄は地図、私は水筒を持ちます。地図を持つのは誰ですか。','兄。'),
        ('昨日は図書館、今日は美術館へ行きました。今日行ったのはどこですか。','美術館。'),
        ('姉は「私は紅茶を飲む」、私は「水を飲む」と言いました。紅茶を飲む人は誰ですか。','姉。ユーザーやAssistantではない。')]:add('binding',text,expected,True)
    for a,op,b,answer in [(1,'+',2,3),(2,'+',3,5),(4,'+',4,8),(6,'+',1,7),(3,'+',5,8),(5,'-',2,3),(9,'-',4,5),(7,'-',1,6),(10,'-',6,4),(8,'-',3,5)]:
        assert (a+b if op=='+' else a-b)==answer
        word='足す' if op=='+' else '引く'
        add('arithmetic',f'{a}{word}{b}はいくつですか。',f'{answer}。別の数や単位を加えない。',True)
    for text,expected in [
        ('受付番号は「L-36」です。番号だけ返してください。','L-36 のみ。説明やですを付けない。'),
        ('保存名は「memo_8」です。名前だけをそのまま返してください。','memo_8 のみ。'),
        ('合言葉は「青い空」です。かぎ括弧を付けず、合言葉だけ答えて。','青い空 のみ。'),
        ('時刻は「08:15」です。この表記だけをそのまま返してください。','08:15 のみ。'),
        ('札は「南」と「北」です。「北」だけ返してください。','北 のみ。'),
        ('使う印は「□」です。印を一つだけ返してください。','□ のみ。'),
        ('並びは「B→D→A」です。かぎ括弧を付けず、矢印も含めて並びだけ返してください。','B→D→A のみ。'),
        ('メモは「昼 / 夜」です。かぎ括弧なしで空白と斜線もそのまま返してください。','昼 / 夜 のみ。'),
        ('数値は「3,600」です。数字とコンマだけ返してください。','3,600 のみ。'),
        ('文字列は小文字の「cat」です。その三文字だけ返してください。','cat のみ。大文字に変えない。')]:add('format',text,expected,True)
    for text,expected in [
        ('おすすめの料理を決めたいです。家にある材料はまだ伝えていません。','材料を尋ねる、または材料が未提示と明示。具体的な材料を作らない。'),
        ('近い方の店を選んでほしいです。場所も候補もまだ伝えていません。','現在地や候補を尋ねる、または未提示と明示。'),
        ('予定の時刻を確認したいです。どの予定かはまだ話していません。','どの予定か尋ねる、または予定未提示と明示。'),
        ('この文章を短くしてほしいです。文章は次に送ります。','文章の送付を求める、または送付を待つ。本文を創作しない。'),
        ('友人への返事を考えたいです。友人のメッセージはまだ見せていません。','元メッセージや返したい内容を確認する。'),
        ('二つの服で迷っています。服の特徴はまだ説明していません。','候補の特徴を尋ねる、または不足情報を明示する。'),
        ('人数分の飲み物を用意したいです。人数はまだ決まっていません。','人数が未定と扱う。人数の確認や確定を促す。数字を作らない。'),
        ('いつもの人に連絡したいです。相手の名前はまだ教えていません。','相手を尋ねる、または名前の未提示を明示する。'),
        ('旅行に何日使うか相談したいです。行き先はまだ話していません。','行き先や条件を確認する。具体的な目的地や日数を断定しない。'),
        ('私が何時に到着するか分かりますか。出発時刻も移動方法もまだ伝えていません。','分からないと認める、または出発や移動条件を確認する。到着時刻を作らない。')]:add('missing_information',text,expected)
    provided=[
        ([('user','借りた本は園芸の入門書です。'),('assistant','園芸の入門書ですね。')],'何の入門書を借りましたか。','園芸。'),
        ([('user','休憩は三十分あります。'),('assistant','三十分ですね。')],'休憩は何分ですか。','三十分。'),
        ([('user','うさぎの名前はココです。'),('assistant','ココですね。'),('user','ココは人参が好きです。'),('assistant','人参が好きなのですね。')],'うさぎの名前を教えて。','ココ。'),
        ([('user','手帳は緑の袋、鍵は黒い袋にあります。'),('assistant','手帳は緑、鍵は黒ですね。')],'鍵の入った袋は何色ですか。','黒。'),
        ([('user','母は料理を作り、父は皿を洗います。'),('assistant','お母さんが料理、お父さんが皿洗いですね。')],'皿を洗う担当は誰ですか。','父。'),
        ([('user','花は赤にします。'),('assistant','赤ですね。')],'花を白に変更しました。今の色は何ですか。','白。赤ではない。'),
        ([('user','予約は火曜日です。'),('assistant','火曜日ですね。')],'予約を土曜日に訂正します。今の曜日は？','土曜日。火曜ではない。'),
        ([('user','紙は四枚必要です。'),('assistant','四枚ですね。')],'必要な数を七枚に変更しました。何枚ですか。','七枚。四枚ではない。'),
        ([('user','待ち合わせは駅です。'),('assistant','駅ですね。'),('user','公園に変更します。'),('assistant','公園へ変更ですね。')],'その変更を取り消して元へ戻します。今の場所はどこですか。','駅。公園ではない。'),
        ([('user','果物はりんご、飲み物は水です。'),('assistant','りんごと水ですね。'),('user','果物だけバナナにします。'),('assistant','バナナと水ですね。')],'飲み物だけお茶に変更します。最後の組合せを教えて。','バナナとお茶の両方。')]
    for history,text,expected in provided:add('provided_history',text,expected,True,[dict(role=r,content=t) for r,t in history])
    memories=[
        ('飼い猫','ルナ','首輪の色','緑','今日は本棚を片付けました。','明日は近所を散歩します。'),
        ('飼い犬','ポチ','首輪の色','黄色','今日は玄関を掃除しました。','夕方は家で休みます。'),
        ('読む本の題名','森の道','表紙の色','青','今日は買い物に行きました。','明日は手紙を書きます。'),
        ('合言葉','白い雲','使う印','丸','午前は部屋を片付けました。','夕方はお茶を飲みます。'),
        ('買う果物','桃','買う個数','三個','今日は図書館に寄りました。','明日は家にいます。'),
        ('買う野菜','人参','買う本数','二本','今日は写真を整理しました。','夕方に本を読みます。'),
        ('待ち合わせ場所','公民館','待ち合わせの曜日','金曜','今日は机を拭きました。','帰りは歩きます。'),
        ('借りた本の分野','地理','返却の曜日','木曜','今日は洗濯をしました。','明日は映画を見ます。'),
        ('贈る品物','手袋','贈る相手','祖母','今日は早く起きました。','夜は音楽を聴きます。'),
        ('使う道具','はさみ','道具を置く場所','引き出し','今日は窓を開けました。','午後は読書をします。')]
    for i,(field,value,other,other_value,d1,d2) in enumerate(memories,1):
        rows.append(dict(id=f'own_memory-{i:02d}',category='own_memory',mode='own',objective=True,history=[],turns=[
            dict(user=f'{field}は「{value}」です。覚えておいてください。',expected=f'{field}={value}の確認や自然な受け止め。',objective=False),
            dict(user=d1,expected='この近況を自然に受け止める。前の情報を否定しない。',objective=False),
            dict(user=f'最初に伝えた{field}は何でしたか。',expected=value,objective=True),
            dict(user=f'{other}は「{other_value}」です。',expected=f'{other}={other_value}の確認や自然な受け止め。',objective=False),
            dict(user=d2,expected='この近況を自然に受け止める。既存の情報を変えない。',objective=False),
            dict(user=f'{field}と{other}を両方教えてください。',expected=f'{value}と{other_value}の両方。属性の対応を変えない。',objective=True)]))
    corrections=[
        ('予約の曜日','月曜','木曜','予約の時刻','二時','三時'),
        ('会場','学校','図書館','参加人数','三人','五人'),
        ('封筒の色','白','青','封筒の枚数','二枚','四枚'),
        ('猫の名前','ミミ','ハナ','首輪の色','赤','緑'),
        ('本の置き場所','机','棚','本の冊数','一冊','二冊'),
        ('買う果物','りんご','梨','買う個数','二個','四個'),
        ('手紙を渡す相手','姉','兄','渡す曜日','火曜','金曜'),
        ('集合場所','北口','南口','集合時刻','十時','十一時'),
        ('糸の色','赤','黄色','糸の本数','三本','六本'),
        ('借りる本の分野','歴史','科学','返却の曜日','水曜','土曜')]
    for i,(field,old,new,other,old_other,new_other) in enumerate(corrections,1):
        rows.append(dict(id=f'own_correction-{i:02d}',category='own_correction',mode='own',objective=True,history=[],turns=[
            dict(user=f'{field}は「{old}」です。',expected=f'{old}の確認。',objective=False),
            dict(user=f'{field}を「{new}」へ変更します。',expected=f'変更後の{new}を受け止め、{old}を維持しない。',objective=False),
            dict(user=f'今の{field}を教えてください。',expected=new,objective=True),
            dict(user=f'{other}は「{old_other}」です。',expected=f'{other}={old_other}の確認。',objective=False),
            dict(user=f'{other}だけ「{new_other}」へ訂正します。',expected=f'{other}={new_other}を受け止める。最初の{field}={new}は変えない。',objective=False),
            dict(user=f'最後の{field}と{other}を両方教えてください。',expected=f'{new}と{new_other}の両方。旧値{old}/{old_other}へ戻らない。',objective=True)]))
    assert len(rows)==100 and sum(len(c['turns']) for c in rows)==200
    assert len({c['id'] for c in rows})==100
    assert sum(c['objective'] for c in rows)==70
    return rows


def prepare():
    target=RUN/'cases.json';assert not target.exists(),'Keep prepared cases immutable'
    payload=dict(created_at=now(),cases=cases(),cases_count=100,responses_count=200,
        category_count=10,objective_final_cases=70,source_sha256=sha(__file__),
        scope='Public authored diagnostic; nonrandom, no sealed TEST; no claim of training decontamination')
    save(target,payload)
    save(RUN/'protocol.json',dict(created_at=now(),cases_sha256=sha(target),checkpoint_sha256=CHECKPOINT,URL=URL,
        max_new_tokens=32,decoding='greedy',device='CPU',precision='FP32/math',max_CPU_wall_seconds=1800,
        request_timeout_seconds=60,history='all actual decoded Assistant replies; each case starts fresh',
        no_learning=True,no_TEST_or_corpus_reads=True,rubric=dict(grammar='0 broken;1 awkward;2 natural',
            relevance='0 irrelevant/wrong;1 partial;2 directly and completely responds',
            context='0 contradiction/lost facts;1 partial;2 all relevant facts/instructions retained',
            factual_correct='bool only for marked objective probes; judge requested facts independently of surface grammar',
            task_pass='grammar=relevance=context=2; numerical accuracy and format compliance separately discussed'),
        scoring='Every response receives a literal human-readable rationale from Codex nonblind; no keyword-based semantic scoring',
        primary='100 case-final outputs; also report all200 and the20 own-history probe3/final6 separately',
        restrictions='No checkpoint/decoder selection or run extension from these outcomes; no adoption claim',
        source_sha256=sha(__file__)))
    print('Prepared100 cases/200responses before inference',flush=True)


def model_info():
    with urlopen(URL+'/api/model',timeout=5) as response:value=json.load(response)
    assert value['checkpoint_sha256']==CHECKPOINT and value['decoding']=='greedy' and value['max_new_tokens']==32
    assert value['parameters']==10001152 and value['device']=='CPU'
    return value


def run():
    target=RUN/'raw.json';assert not target.exists(),'Do not overwrite full/partial actual results'
    protocol=read(RUN/'protocol.json');assert protocol['cases_sha256']==sha(RUN/'cases.json') and protocol['source_sha256']==sha(__file__)
    all_cases=read(RUN/'cases.json')['cases'];started=time.monotonic()
    report=dict(status='running',created_at=now(),protocol_sha256=sha(RUN/'protocol.json'),cases_sha256=sha(RUN/'cases.json'),
        model_before=model_info(),responses=[],actual_response_count=0,completed_cases=0,CPU_only=True)
    save(target,report)
    try:
        for case in all_cases:
            history=[dict(m) for m in case['history']]
            for turn,t in enumerate(case['turns'],1):
                assert time.monotonic()-started<1740
                history.append(dict(role='user',content=t['user']));payload=dict(messages=[dict(m) for m in history],max_new_tokens=32)
                request=Request(URL+'/api/chat',data=json.dumps(payload,ensure_ascii=False).encode('utf-8'),
                    headers={'Content-Type':'application/json'},method='POST')
                attempts=[]
                for attempt in range(20):
                    try:
                        with urlopen(request,timeout=min(60,1800-(time.monotonic()-started))) as response:answer=json.load(response)
                        break
                    except HTTPError as error:
                        body=error.read().decode('utf-8',errors='replace');attempts.append(dict(status=error.code,body=body))
                        if error.code!=409 or attempt==19:raise
                        time.sleep(.1)
                row=answer['response']
                assert row['max_new_tokens']==32 and row['generated_tokens']<=32 and row['full_history_retained'] and row['removed_turns']==0
                report['responses'].append(dict(id=case['id'],category=case['category'],mode=case['mode'],turn=turn,
                    final=turn==len(case['turns']),objective=t['objective'],expected=t['expected'],request=payload,
                    answer=answer,HTTP_conflicts=attempts))
                history.append(dict(role='assistant',content=row['text']));report['actual_response_count']+=1
                save(target,report)
            report['completed_cases']+=1;save(target,report)
            print(json.dumps(dict(completed=report['completed_cases'],responses=report['actual_response_count'],
                id=case['id'],final_reply=row['text']),ensure_ascii=False),flush=True)
        assert report['actual_response_count']==200 and report['completed_cases']==100
        report.update(status='all200_actual_responses_complete_pending_literal_review',model_after=model_info(),CPU_wall_seconds=time.monotonic()-started)
    except BaseException as error:
        report.update(status='failed_partial_preserved',error=repr(error),CPU_wall_seconds=time.monotonic()-started);raise
    finally:report['updated_at']=now();save(target,report)


def packet(start,count):
    report=read(RUN/'raw.json');assert report['status']=='all200_actual_responses_complete_pending_literal_review'
    for i,row in enumerate(report['responses'][start:start+count],start):
        print(json.dumps(dict(i=i,id=row['id'],turn=row['turn'],final=row['final'],objective=row['objective'],
            history=row['request']['messages'],expected=row['expected'],reply=row['answer']['response']['text'],
            stop=row['answer']['response']['stop_reason']),ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('mode',choices=['prepare','run','packet']);parser.add_argument('--start',type=int,default=0);parser.add_argument('--count',type=int,default=25)
    args=parser.parse_args()
    if args.mode=='prepare':prepare()
    elif args.mode=='run':run()
    else:packet(args.start,args.count)
