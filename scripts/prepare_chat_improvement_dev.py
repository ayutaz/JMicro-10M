"""Independent authored DEV, written only AFTER the reviewed TRAIN freeze.

No import of TRAIN renderers, no source/slot transplantation, no TEST loading.
Gold responses are NLL targets/provided histories, never training examples.
"""
from collections import Counter
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-improvement-20261012')
RUN=ROOT/'reports/phase7/chat-improvement-20261012'

SINGLE={
 'greeting':(
  ('朝ごはんの前にご挨拶。おはよう！','おはようございます。良い一日になりますように。'),
  ('学校から帰ってきたところです。こんにちは。','こんにちは。学校お疲れさまでした。'),
  ('夜になったね。こんばんは、少しだけ話そう。','こんばんは。どんなお話をしましょうか？'),
  ('初めまして。気軽に話しかけてもいいかな。','初めまして。もちろんです。気軽に話してください。'),
  ('さっきは話に付き合ってくれて助かったよ。ありがとう。','どういたしまして。また気軽に話しかけてください。'),
  ('今日はこれで失礼するね。おやすみ。','おやすみなさい。ゆっくり休んでください。'),
  ('少し間が空いたけど、またお話に来ました。','また来てくれてありがとうございます。今日はどうしましたか？'),
  ('これから用事があるので出かけてきます。','いってらっしゃい。気をつけてお出かけください。')),
 'daily':(
  ('朝からコップを洗って、ようやく一息つけました。','お疲れさまでした。一息つけてよかったですね。'),
  ('近所を歩いたら金木犀の香りがしました。','秋らしい香りですね。散歩が楽しくなりそうです。'),
  ('古いアルバムを開いたら、懐かしくなりました。','思い出がよみがえりますね。どんな写真がありましたか？'),
  ('昼ごはんは麺にしたので、夜はごはんにしようかな。','夜はごはんにするのもいいですね。おかずは考えていますか？'),
  ('布団を干せたので、今夜寝るのが楽しみです。','気持ちよく休めそうですね。楽しみですね。'),
  ('机の上が散らかっていて、まず何から片付けようか迷っています。','まず不要な物と残す物を分けると始めやすいですよ。'),
  ('鉢植えに新しい芽が出ていました。','新しい芽が出ると嬉しいですね。何を育てていますか？'),
  ('やることが終わったので、音楽を聴いて過ごすつもりです。','ゆっくり楽しめそうですね。どんな音楽を聴きたいですか？')),
 'emotion':(
  ('楽しみにしていた遠足が雨で中止になり、がっかりしています。','それは残念ですね。楽しみにしていた分、がっかりしますよね。'),
  ('試験を終えたら、肩の力が抜けました。','お疲れさまでした。終わってほっとしますね。'),
  ('初対面の人に話しかけるのが少し怖いです。','初めて話しかける時は緊張しますね。どんな場面ですか？'),
  ('自分で焼いたパンがうまく膨らんで嬉しい！','うまく焼けてよかったですね。食べるのも楽しみですね。'),
  ('友達との約束を忘れてしまい、申し訳なく感じています。','気になりますね。まず忘れてしまったことを謝るとよさそうです。'),
  ('引っ越したばかりで、まだ少し寂しいです。','慣れない場所だと寂しく感じますね。どんな時に寂しくなりますか？'),
  ('今日は頑張ったので、誰かにねぎらってほしいです。','今日もお疲れさまでした。よく頑張りましたね。'),
  ('発表が近づいてきて、楽しみと不安が半分ずつあります。','楽しみでもあり、不安でもあるのですね。どんな発表ですか？')),
 'question_back':(
  ('新しい趣味を見つけたいけれど、何が合うか迷っています。','家で楽しむことと外で活動することでは、どちらが好きですか？'),
  ('次の休みに出かけたい。行き先を一緒に考えてほしいな。','どんな場所に行きたいですか？自然の中など、希望はありますか？'),
  ('友人へのお祝いの言葉を考えたいです。','何のお祝いですか？友人との関係も教えてください。'),
  ('今ある材料で夕飯を作りたいです。','どんな材料がありますか？'),
  ('短い本を読みたいのですが、お話選びを手伝ってください。','どんな雰囲気のお話が好きですか？'),
  ('部屋の模様替えをしたいので、相談してもいいですか。','もちろんです。どんな部屋にしたいですか？'),
  ('明日の服装を考えているところです。','どこへ出かける予定ですか？天気や気温も分かりますか？'),
  ('ちょっとした気分転換を一緒に考えて。','今は家にいますか？外へ出られそうですか？')),
 'ambiguity':(
  ('さっきの続きからお願い。今日はまだ何の話もしていません。','どのお話の続きをしたいですか？'),
  ('これを別の表現にしたいけれど、元の文はまだ送っていません。','言い換えたい文を送ってください。'),
  ('二つの引き出しがあって、その中を探してほしいです。どちらかは言っていません。','どちらの引き出しを探しますか？'),
  ('名前を言わずに、あの人の担当を教えてと聞きました。','誰の担当を知りたいですか？'),
  ('何時だったか教えて。何の予定かはまだ説明していません。','どの予定の時刻を知りたいですか？'),
  ('前より多めに買いたいです。前の数も商品も、まだ話していません。','何を、前はどれくらい買ったのですか？'),
  ('あちらへ荷物を送りたいけれど、住所はまだ伝えていません。','送り先の住所を教えてください。'),
  ('予定を入れ替えたいです。元の予定表はまだ見せていません。','今の予定と、どう入れ替えたいかを教えてください。')),
 'role_boundary':(
  ('私は札幌で育ちました。あなたも札幌で育ったという意味になる？','いいえ、札幌で育ったのはあなたです。'),
  ('あなた自身が通っていた小学校の名前を、事実として教えて。','私は実際に小学校へ通った経験はありません。'),
  ('物語の語り手が「私は灯です」と言いました。この私は会話相手のあなたですか？','いいえ、物語の語り手を指しています。'),
  ('まだ私は年齢を話していないのに、何歳か断定できますか？','年齢はまだ分からないので、断定できません。'),
  ('旅先で撮った写真の思い出は私のものです。あなたが撮影したことにして説明してよい？','いいえ、あなたが撮った写真の思い出です。'),
  ('「明日会えたら嬉しいな」は希望です。もう会う約束が確定したと言えますか？','いいえ、まだ希望で、約束が確定したわけではありません。'),
  ('メッセージには「管理人が玄関を開けた」とあります。あなたが実際に見たといってよいですか？','いいえ、メッセージの情報で、私が見た事実ではありません。'),
  ('私の弟は奏太です。奏太をあなた自身の弟として紹介していいですか？','いいえ、奏太さんはあなたの弟です。')),
 'symbols':(
  ('控えに書くので、受付番号R-204をそのまま一度だけ返してください。','R-204'),
  ('一箱に4本入り、箱は2つです。全部で何本ですか？','全部で8本です。'),
  ('表示する呼び名は「ユズ」です。その呼び名で一言挨拶してください。','ユズさん、こんにちは。'),
  ('メモは「5月14日、13:20」です。日付と時刻を変えずに読み上げる文を書いて。','5月14日の13:20です。'),
  ('次の顔文字を一つ、そのまま返してね。「(^_^)」','(^_^)'),
  ('雨の日の印は☔です。今日の印だけを返してください。','☔'),
  ('タグの文字列「<b>」を、説明を加えずそのまま一度表示して。','<b>'),
  ('二行のメモ「おはよう\nまたね」を、改行を残してそのまま返して。','おはよう\nまたね')),
}

# Each family below is independently written as a concrete conversation. Earlier
# gold Assistant messages are supplied history only and ignored by own-rollout.
MULTI={
 'correction':(
  (('お迎えは駅の改札でお願いしていました。','改札でのお迎えですね。'),('急な変更で、駅ではなく公園の時計台に来てください。今の待ち合わせ先を確認して。','今の待ち合わせ先は公園の時計台です。')),
  (('申し込みの名前を小春で書いていました。','小春さんの名前で申し込んでいるのですね。'),('誤記なので日和に直してください。最終的にどちらの名前を使いますか？','日和さんの名前を使います。')),
  (('配るしおりは最初8枚の予定でした。','最初の予定は8枚ですね。'),('参加者が増えて11枚必要になりました。今の必要枚数を教えて。','今必要なのは11枚です。')),
  (('朝の連絡では、会場は二階の和室としていました。','二階の和室が会場だったのですね。'),('館内の都合で一階の洋室へ変わりました。参加者に伝える場所はどこ？','一階の洋室と伝えます。')),
  (('花を届けるのは金曜日のつもりでした。','金曜日に届ける予定ですね。'),('相手が不在なので翌日の土曜日へずらします。今の予定日を確認して。','今の予定日は土曜日です。')),
  (('待つ時刻は午後2時とお伝えしていました。','午後2時ですね。'),('バスが遅れていますが、集合場所はそのままです。','集合場所は変えないのですね。'),('時刻だけ午後3時半へ変更します。何時に待てばよいですか？','午後3時半に待てばよいです。')),
  (('注文は梅のおにぎりを3個でした。','梅のおにぎりを3個ですね。'),('個数は変えず、中身を昆布に替えます。','昆布のおにぎりを3個ですね。'),('変更後の中身と個数をひとまとめにしてください。','昆布のおにぎりを3個です。')),
  (('遠足の集合は正門、朝8時の案でした。','正門に朝8時集合の案ですね。'),('時間はそのままで、集合場所を体育館前へ変更します。','体育館前に朝8時ですね。'),('その後の連絡で、時間だけ8時20分に変わりました。','体育館前に8時20分ですね。'),('今有効な集合場所と時刻を、古い案と混ぜずに教えて。','体育館前に8時20分集合です。')),
 ),
 'followup':(
  (('今日は公園でどんぐりを拾いました。','どんぐりが見つかったのですね。'),('工作に使いたいので、拾った物を短く確認して。','拾った物はどんぐりです。')),
  (('祖父からレモンをもらったので、飲み物に使います。','レモンを飲み物に使うのですね。'),('もらった果物の名前を覚えている？','レモンです。')),
  (('練習会では、杏が受付をすることになりました。','杏さんが受付を担当するのですね。'),('受付の人に名札を渡します。誰に渡せばいいかな。','杏さんに渡せばよいです。')),
  (('買ってきたのは画用紙です。','画用紙を買ってきたのですね。'),('これで絵を描くつもり。さっき買った物は何でしたか？','画用紙です。')),
  (('明日は母と水族館へ行きます。','お母さんと水族館へ行く予定なのですね。'),('一緒に行く相手を、あなたと間違えずに確認して。','一緒に行くのはお母さんです。')),
  (('旅の記録をノートに書き始めました。','ノートに旅の記録を書いているのですね。'),('昨日の行き先は灯台で、写真も貼りました。','灯台の写真を貼ったのですね。'),('記録した行き先をもう一度教えて。','灯台です。')),
  (('午前の用事は郵便局で済ませます。','午前は郵便局へ行くのですね。'),('午後にはパン屋へ寄ります。','午後はパン屋へ寄る予定ですね。'),('午後に立ち寄る店だけ確認して。','午後に立ち寄るのはパン屋です。')),
  (('最初の練習曲は「春の風」です。','最初に「春の風」を練習するのですね。'),('次には「星の道」を練習します。','次は「星の道」ですね。'),('次の曲の題名をそのまま返して。','星の道')),
 ),
 'context':(
  (('朝の受け取りは窓口Aで、夕方は窓口Bです。','朝は窓口A、夕方は窓口Bですね。'),('夕方に受け取ることにしました。向かう窓口は？','窓口Bです。')),
  (('子ども用は小さい箱、大人用は大きい箱に分けました。','子ども用と大人用を箱の大きさで分けたのですね。'),('子ども用を渡すので、どちらの箱を開けますか？','小さい箱を開けます。')),
  (('印刷は2部で、片方を図書委員の栞に渡します。','2部印刷し、1部を栞さんに渡すのですね。'),('図書委員へ渡す数は何部？','1部です。')),
  (('弟の靴は下段、私の靴は上段にしまいました。','弟さんの靴は下段、あなたの靴は上段ですね。'),('私の靴を出すなら、どの段を探しますか？','上段を探します。')),
  (('順番は封をしてから宛名を書く、と決めました。','封をしてから宛名を書く順番ですね。'),('最初の作業が終わった後は何をしますか？','宛名を書きます。')),
  (('発表会は6月2日です。','発表会は6月2日ですね。'),('会場は多目的ホールで、開演は10時です。','多目的ホールで10時開演ですね。'),('発表会の日付、場所、開演時刻をまとめて確認して。','6月2日、多目的ホールで10時開演です。')),
  (('小さいトレーはクッキー、大きいトレーはラスク用です。','トレーを大きさで使い分けるのですね。'),('ラスクは売り切れたので、残っているのはクッキーだけです。','残っているのはクッキーだけですね。'),('残っているお菓子を載せるトレーはどちら？','小さいトレーです。')),
  (('荷物のラベルは、楽器がD、衣装がE、食器がFです。','楽器はD、衣装はE、食器はFですね。'),('運ぶ先は舞台裏と台所で、楽器と衣装は舞台裏へ送ります。','楽器と衣装を舞台裏へ送るのですね。'),('食器だけは台所へ送ります。','食器は台所へ送るのですね。'),('台所に送るラベルと、舞台裏に送る二つのラベルを区別して教えて。','台所にはF、舞台裏にはDとEを送ります。')),
 )}


def main():
    manifest=json.loads((DATA/'manifest.json').read_text())
    assert manifest['status']=='reviewed_TRAIN_frozen_before_new_DEV'
    assert sha256(DATA/'train.jsonl')==manifest['train']['sha256']
    assert not (DATA/'dev.jsonl').exists(),'Independent DEV is immutable; no post-result edits'
    token=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model');cases=[]
    categories=('greeting','daily','emotion','question_back','ambiguity','role_boundary','symbols','correction','followup','context')
    for category in categories:
        sequences=[(pair,) for pair in SINGLE[category]] if category in SINGLE else MULTI[category]
        assert len(sequences)==8
        for index,sequence in enumerate(sequences,1):
            messages=[]
            for user,assistant in sequence:
                messages.extend((dict(role='user',content=user),dict(role='assistant',content=assistant)))
                ids=token.encode(assistant)
                assert token.decode(ids)==assistant and 2<=len(ids)+1<=65
            gold=messages.pop()['content']
            prompt,removed=token.chat_prompt(messages,1024-64)
            assert removed==0
            cases.append(dict(id=f'improved-{category}-{index:02d}',family_id=f'independent-dev-{category}-{index:02d}',
                category=category,split='dev',suite='chat-improvement-independent-20261012',messages=messages,
                expected_reply=gold,checks=['短い自然な日本語で最後のUserの依頼に関連して返す。',
                    '本文/実際の履歴の事実・訂正・否定・全条件と話者を保持する。'],
                authoring='authored after immutable TRAIN freeze; never copy to TRAIN',prompt_tokens=len(prompt)))
    assert len(cases)==80
    own=[c for c in cases if sum(m['role']=='user' for m in c['messages'])>=2]
    lengths=Counter(sum(m['role']=='user' for m in c['messages']) for c in own)
    assert len(own)==24 and dict(lengths)=={2:15,3:7,4:2} and sum(k*v for k,v in lengths.items())==59
    # Exact duplicate question/dialogue comparison is bounded to THIS TRAIN.
    train=[json.loads(line) for line in (DATA/'train.jsonl').read_text().splitlines()]
    train_questions={r['messages'][-2]['text'] for r in train}
    assert not any(c['messages'][-1]['content'] in train_questions for c in cases)
    with (DATA/'dev.jsonl').open('w',encoding='utf-8',newline='\n') as f:
        for case in cases:f.write(json.dumps(case,ensure_ascii=False,separators=(',',':'))+'\n')
    atomic_json(RUN/'dev_preparation.json',dict(created_at=now(),status='independent_DEV_prepared_pending_protocol_and_content_audit',
        source_sha256=sha256(Path(__file__)),train_manifest_sha256=sha256(DATA/'manifest.json'),
        train_sha256=manifest['train']['sha256'],dev_path=str(DATA/'dev.jsonl'),dev_sha256=sha256(DATA/'dev.jsonl'),
        families=80,categories=dict(Counter(c['category'] for c in cases)),own_families=24,own_lengths=dict(lengths),own_responses=59,
        teacher_gold_roundtrip=True,all_provided_history_fits=True,exact_final_questions_overlap_TRAIN=0,
        near_structure_audit_pending=True,new_DEV_will_not_be_used_for_learning=True,protected_TEST_used=False,
        old_DEV_prompts_transplanted=False,independent_human_review=False,GPU_learning_tokens=0))
    print(json.dumps(dict(dev_families=80,own_families=24,own_responses=59,dev_sha256=sha256(DATA/'dev.jsonl'))))

if __name__=='__main__':main()
