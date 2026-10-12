"""Authored TRAIN recipes for plan133. This module contains no DEV questions.

Each recipe supplies its state, answer operation and independently worded prompt.
Answers are computed from typed state before rendering, not keyword-validated.
Family identity is the authored scenario including all slot/format variants.
First-turn supervision, optional introductions and concise grounded answers.
Plan131 sources remain unchanged; this is a separately bound recipe comparison.
"""
import random


WEIGHTS=dict(daily=.30,direct=.20,correction=.15,negation=.15,context=.10,clarification=.05,speaker=.05)
NAMES=('友紀','理央','佳奈','優斗','玲奈','正人','真央','聡','優花','紗也','和也','梨沙','直樹','千尋','綾乃','誠','香織','亮介','遥香','拓也','菜月','一真','美咲','晴人')
PLACES=('図書室','工作室','音楽室','会議室','講堂','案内所','裏門','倉庫','体育館','中庭','待合室','駅前','北口','南口','西門','東門','受付','談話室','資料室','庭','売店','屋上','別館','玄関')
ITEMS=('定規','ノート','水筒','はさみ','色鉛筆','画材','時計','手袋','便箋','ペン','手帳','封筒','タオル','鉛筆','雑誌','地図','弁当','花束','切符','写真','鍵','帽子')
BORROWABLE=('手帳','タオル','鉛筆','雑誌','地図','写真','鍵','帽子')
FOODS=('ゼリー','プリン','ドーナツ','パン','まんじゅう','豆菓子','ケーキ','りんご','梨','桃','ぶどう','クッキー','おにぎり','サンドイッチ','せんべい','ヨーグルト','みかん','バナナ','いちご')
DAYS=('月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日')
ACTIONS=('片付け','読書','散歩','買い物','掃除','料理','洗濯','休憩','体操','練習','整理','準備')
TASKS=('片付け','掃除','料理','洗濯','練習','整理','準備','包装','点検','計算','記録','手入れ')
ACTIVITY_PLACES={
 '片付け':('自宅','作業室','教室'),'読書':('資料室','自宅','談話室'),
 '散歩':('公園','庭','遊歩道'),'買い物':('売店','商店','市場'),
 '掃除':('自宅','教室','玄関'),'料理':('台所','食堂','自宅'),
 '洗濯':('自宅','洗濯室'),'休憩':('休憩室','談話室','庭'),
 '体操':('広場','庭','練習室'),'練習':('練習室','教室','自宅'),
 '整理':('資料室','作業室','自宅'),'準備':('作業室','自宅','教室')}
TIMES=('七時','八時','九時','十時','十一時','十二時','十三時','十四時','十五時','十六時','十七時','十八時')
QTY=('一つ','二つ','三つ','四つ','五つ','六つ','七つ','八つ','九つ','十個','十二個','十五個')
NUMBER_NAMES=('一','二','三','四','五','六','七','八','九','十','十二','十五')
NUMBER_VALUES=(1,2,3,4,5,6,7,8,9,10,12,15)
ITEM_COUNTERS=dict(定規='本',ノート='冊',水筒='本',はさみ='本',色鉛筆='本',画材='個',時計='個',手袋='組',便箋='枚',ペン='本',手帳='冊',封筒='枚',タオル='枚',鉛筆='本',雑誌='冊',地図='枚',
    弁当='個',花束='束',切符='枚',写真='枚',鍵='本',帽子='個')
FOOD_COUNTERS=dict(バナナ='本',ぶどう='房',せんべい='枚')


def quantity(index,counter,style):
    return (str(NUMBER_VALUES[index]) if style=='arabic' else NUMBER_NAMES[index])+counter


def time_rank(value):
    return TIMES.index(value) if value in TIMES else int(value.removesuffix('時'))-7


def clock_style(value,style):
    return f'{time_rank(value)+7}時' if style=='arabic' else TIMES[time_rank(value)]
OPENERS=(
 '少し相談に乗ってもらえますか？','落ち着いて話を聞いてほしいです。','これから相談したいことがあります。',
 '短いお話をしてもよいですか？','説明をゆっくり聞いてもらえると助かります。','聞いてほしいことがあります。',
 '今から少しお話ししたいです。','相談したいので、お付き合いください。','簡単なことを尋ねてもいいですか？',
 '手短に相談させてください。','少し時間を取ってお話ししてもよいですか？','落ち着いて相談したいです。',
 '少し気になることを相談します。','お話を聞いてもらいたいです。','まず相談の内容をお伝えします。',
 'これから話す内容について相談したいです。','短い相談をしてもよいでしょうか？','一つ確認したいことがあります。',
 '気軽にお話しできると嬉しいです。','お話を聞いてくださると助かります。','少しお尋ねしたいことがあります。',
 '順番に話してもよいですか？','うまく伝えられるように少しずつ話します。','会話をしながら相談したいです。',
 '相談するためにここに来ました。','ひとまず話を聞いてもらえますか？','今日も少し相談したいです。',
 '短い質問に答えてもらいたいです。','これから話すことを確認したいです。','一緒に確認してほしいことがあります。',
 '相談を始めてもよいですか？','今からお話しするので聞いてください。')

# 24 different tasks: not 24 names for one slot substitution template.
DIRECT=(
 ('owner','{a}が{item}を預かっています。誰に聞けば{item}を受け取れますか？','a','{a}さんに聞けば受け取れます。'),
 ('destination','届け先は{place}です。荷物はどこへ持っていけばいいですか？','place','{place}へ持っていけば大丈夫です。'),
 ('meeting_time','待ち合わせの時間を{time}に決めました。何時に集合する予定ですか？','time','集合する予定は{time}です。'),
 ('weekday','休館日は{day}と案内に書かれています。休みの曜日を教えてください。','day','休館日は{day}です。'),
 ('quantity','袋に{food}を{qty}入れました。入っている数を確認したいです。','qty','袋に入っているのは{qty}です。'),
 ('first_step','{act}を済ませてから{act2}をするつもりです。最初に行うことは？','act','最初は{act}をする予定です。'),
 ('last_step','今日はまず{act}、最後に{act2}をします。最後の予定だけ教えて。','act2','最後の予定は{act2}です。'),
 ('choice','持ち物は{item}か{item2}のどちらかで、{item2}を選びました。選んだのは何？','item2','選んだ持ち物は{item2}です。'),
 ('label','箱の中身は{item}です。中身を尋ねられたら何と答えればいい？','item','箱の中身は{item}です。'),
 ('reason','{day}は休みなので、その日に{act}をします。その曜日を選んだ理由は？','休みだから','その日は休みだからです。'),
 ('name_lookup','担当表には案内係が{a}、荷物係が{b}とあります。案内係は誰ですか？','a','案内係は{a}さんです。'),
 ('location_lookup','{item}は{place}、{item2}は{place2}にあります。{item2}を探す場所は？','place2','{item2}は{place2}にあります。'),
 ('before','{time}に{act}、{time2}に{act2}をする順番です。{act2}の直前の予定は？','act','直前の予定は{act}です。'),
 ('after','予定の順序は{act}、{act2}です。{act}の次は何をしますか？','act2','次にするのは{act2}です。'),
 ('recipient','差し入れの{food}は{a}に渡す分です。誰のために用意した分ですか？','a','{a}さんのために用意した分です。'),
 ('start_place','{place}から{place2}へ移動する予定です。出発する場所を答えてください。','place','出発する場所は{place}です。'),
 ('end_place','道順は{place}から{place2}までです。到着する場所はどこですか？','place2','到着するのは{place2}です。'),
 ('container','{item}を袋に、{item2}を箱に入れました。箱に入れた物を答えて。','item2','箱に入れたのは{item2}です。'),
 ('written_number','購入メモの「{food}」の横に{qty}と書きました。この品の購入数は？','qty','購入する数は{qty}です。'),
 ('available_day','空いているのは{day}です。会うなら何曜日を提案すればよいですか？','day','{day}を提案するとよいです。'),
 ('purpose','{act}のために{place}へ行きます。そこへ行く目的は何ですか？','act','目的は{act}です。'),
 ('speaker_request','{a}が「{item}を借りたい」と言いました。借りたい物を教えて。','item','借りたい物は{item}です。'),
 ('completed','{act}はもう済み、{act2}はまだです。終わった作業はどちらですか？','act','終わったのは{act}です。'),
 ('remaining','{act}は完了し、残っている作業は{act2}です。次に取り組むものは？','act2','残っている{act2}に取り組みます。'),
)

# The current value is obtained by applying the correction event to the state.
CORRECTION=(
 ('appointment','待ち合わせは{old}です。','すみません、{new}に変更します。今の待ち合わせ場所は？','待ち合わせ場所は{new}です。','place'),
 ('arrival','到着予定を{old}と伝えました。','遅れそうなので{new}に訂正します。到着予定を確認して。','到着予定は{new}です。','time'),
 ('count','買う数は{old}にします。','数を見直して{new}にしました。いま何個買う予定？','買う予定は{new}です。','qty'),
 ('weekday','予定日は{old}とメモしました。','メモが違いました。正しくは{new}です。何曜日が正しい？','正しい予定日は{new}です。','day'),
 ('recipient','届ける相手は{old}です。','相手を取り違えました。{new}に届けます。今の相手は誰？','届ける相手は{new}さんです。','name'),
 ('item','持っていくのは{old}にします。','荷物を替えて{new}だけにします。持ち物は何ですか？','持ち物は{new}です。','item'),
 ('snack','おやつは{old}を用意します。','材料の都合で{new}に替えます。用意するおやつを教えて。','用意するおやつは{new}です。','food'),
 ('order_first','最初に{old}をする予定です。','順番を変え、最初は{new}にします。先にすることは？','先にすることは{new}です。','action'),
 ('book_storage','保管場所を{old}にしていました。','置き場所を{new}へ移しました。今はどこですか？','今の保管場所は{new}です。','place'),
 ('opening','開始は{old}と案内しました。','案内を訂正します。開始は{new}です。新しい開始時刻は？','新しい開始時刻は{new}です。','time'),
 ('reservation','席は{old}予約するつもりです。','予約数だけ{new}に直します。最終的な数を答えて。','最終的な予約数は{new}です。','qty'),
 ('closure','休みにする曜日は{old}です。','勤務表を直して{new}を休みにしました。休みは何曜日？','休みは{new}です。','day'),
 ('representative','連絡担当を{old}に頼みました。','担当が交代し{new}になりました。連絡する相手は？','連絡担当は{new}さんです。','name'),
 ('lost_item','忘れ物は{old}だと思います。','確認できました。実際は{new}でした。忘れ物は何？','忘れ物は{new}です。','item'),
 ('menu','注文は{old}でお願いします。','まだ注文前なので{new}に変更します。今の注文は？','今の注文は{new}です。','food'),
 ('last_job','最後の作業は{old}です。','最後に回す作業を{new}に替えました。最後は何をする？','最後は{new}をします。','action'),
 ('pickup','受け取りは{old}と聞きました。','店の連絡では正しくは{new}だそうです。どこで受け取る？','受け取り場所は{new}です。','place'),
 ('deadline','締め切りを{old}に設定しました。','締め切りを延ばして{new}とします。期限だけ確認したい。','新しい締め切りは{new}です。','time'),
 ('packet','袋の数を{old}と数えました。','数え直すと{new}でした。正しい袋の数は？','正しい袋の数は{new}です。','qty'),
 ('lesson','練習の曜日は{old}の予定でした。','予定表を更新し{new}に移しました。今の曜日は？','現在の練習日は{new}です。','day'),
 ('author','メモを書いたのは{old}だと思っていました。','本人に聞いたら{new}が書いたと分かりました。書いた人は？','メモを書いたのは{new}さんです。','name'),
 ('shopping','買い物メモには{old}とあります。','その品は取り消し、{new}と書き直しました。買う物は？','買う物は{new}です。','item'),
 ('gift','贈る食べ物を{old}に決めました。','相手の好みに合わせ{new}に替えました。贈る食べ物は？','贈る食べ物は{new}です。','food'),
 ('task','今日の作業は{old}です。','都合が変わり{new}をする日にしました。今の作業予定は？','今日の作業予定は{new}です。','action'),
)

# Negation tasks explicitly expose a finite permitted set, avoiding world facts.
NEGATION=(
 ('exclude','候補は{one}、{two}です。{one}は選ばないので、どちらにしますか？', 'two','選ぶのは{two}です。'),
 ('only','{one}と{two}があります。今回は{one}だけ使います。使う物を答えて。','one','今回は{one}だけ使います。'),
 ('without','持ち物は{one}、{two}、{three}から選びます。{two}と{three}は持たず、残りを持ちます。何を持つ？','one','持っていくのは{one}です。'),
 ('not_both','{one}か{two}を一つ選びます。両方は選べず、{two}も選べません。選べる物は？','one','選べるのは{one}です。'),
 ('accepted','受付が許可したのは{one}です。{two}は許可されていません。提出できるのは？','one','提出できるのは{one}です。'),
 ('remove','袋に{one}と{two}が入っています。{one}を取り出しました。残った物は何？','two','残ったのは{two}です。'),
 ('replace','{one}は使いません。代わりに{two}を使います。今回使う物を教えて。','two','今回は{two}を使います。'),
 ('forbidden','{one}は禁止で、{two}は使えます。この二つのうち使えるものは？','two','使えるものは{two}です。'),
 ('exception','{one}、{two}、{three}のうち、{three}以外は配りません。配る品は何ですか？','three','配る品は{three}です。'),
 ('cancel','注文した{one}は取り消しました。取り消していない注文は{two}です。届く品は？','two','届くのは{two}です。'),
 ('negative_fact','探し物は{one}ではありません。実際は{two}です。探している品を答えて。','two','探している品は{two}です。'),
 ('allowed_pair','{one}と{two}は使えますが、{three}は使いません。使える二つを順に答えて。','pair','使えるのは{one}と{two}です。'),
 ('leave_pair','{one}、{two}、{three}から{three}を除きます。残り二つを順に教えて。','pair','残るのは{one}と{two}です。'),
 ('avoid_question','{one}と{two}のどちらかです。{two}は避けたいので、選ぶなら何がよい？','one','{one}を選ぶとよいです。'),
 ('satisfy_both','候補は{one}と{two}。条件は「{one}ではない」「一つ選ぶ」です。答えは？','two','両方の条件を満たすのは{two}です。'),
 ('do_not_add','必要な品は{one}だけです。{two}を追加しないで準備します。準備する品は？','one','準備するのは{one}だけです。'),
 ('empty_except','箱から{one}と{two}を出し、{three}は出しませんでした。箱に残した品は？','three','箱に残したのは{three}です。'),
 ('reject_offer','{one}の提案は断り、{two}の提案を受けました。受けた提案はどちら？','two','受けたのは{two}の提案です。'),
 ('restriction_change','最初は{one}も{two}も可でしたが、今は{one}が不可です。現在使えるのは？','two','現在使えるのは{two}です。'),
 ('affirmative','{one}は選ばないのではなく、選ぶ品です。{two}は選びません。選ぶ品は？','one','選ぶ品は{one}です。'),
 ('deny_identity','{one}と{two}の札があります。正解の札は{one}ではないと分かりました。正解は？','two','正解の札は{two}です。'),
 ('keep_selected','{one}を残して{two}を外します。外す物ではなく、残す物を答えて。','one','残す物は{one}です。'),
 ('output_rule','選べるのは{one}と{two}です。{one}は禁止なので、選んだ物の名前だけ答えて。','two','{two}'),
 ('two_conditions','{one}、{two}、{three}から選びます。{one}でも{three}でもないものは何ですか？','two','条件に合うのは{two}です。'),
)

CONTEXT=(
 ('two_locations','{item}は{place}にあります。','{item2}は{place2}に置きました。','{item}の場所をもう一度教えて。','place','{item}は{place}にあります。'),
 ('two_owners','{a}が{item}を持っています。','{b}は{item2}を持っています。','{item}を持つ人は誰でしたか？','a','{item}を持つのは{a}さんです。'),
 ('time_place','集合時刻は{time}です。','場所は{place}です。','集合の時刻と場所をまとめて。','time_place','{time}に{place}へ集合します。'),
 ('person_food','{a}に{food}を渡します。','{b}には{food2}を渡します。','{a}に渡す物は何でしたか？','food','{a}さんに渡すのは{food}です。'),
 ('day_task','{day}には{act}をします。','{day2}には{act2}をします。','{day}の予定を教えて。','act','{day}の予定は{act}です。'),
 ('quantity_item','{item}を{qty}用意しました。','{item2}は{qty2}です。','{item}をいくつ用意しましたか？','qty','{item}は{qty}用意しました。'),
 ('task_order','最初に{act}をします。','その後で{act2}をする予定です。','二つの作業を順番にまとめて。','actions','{act}をしてから{act2}をします。'),
 ('who_where','{a}の待ち合わせ場所は{place}です。','{b}は{place2}で待ちます。','{a}に会うにはどこへ行けばよい？','place','{a}さんには{place}で会えます。'),
 ('loan_return','{item}は{a}に借りました。','{item2}は{b}から借りました。','{item2}は誰へ返しますか？','b','{item2}は{b}さんへ返します。'),
 ('start_end','出発地点は{place}です。','目的地を{place2}に決めました。','出発地点と目的地をまとめて。','places','{place}から{place2}へ向かいます。'),
 ('time_lookup','{act}は{time}からです。','{act2}は{time2}から始めます。','{act2}の開始時刻は？','time2','{act2}は{time2}からです。'),
 ('remember_name','担当者の名前は{a}です。','担当する仕事は{act}です。','その仕事の担当者は誰？','a','{act}の担当者は{a}さんです。'),
 ('packing','袋には{item}を入れました。','箱には{item2}を入れました。','袋に入れた物を思い出して。','item','袋に入れたのは{item}です。'),
 ('two_counts','午前には{qty}届きました。','午後は{qty2}届きました。','午後だけの数を答えてください。','qty2','午後に届いたのは{qty2}です。'),
 ('deadline_owner','提出期限は{day}です。','提出する人は{a}です。','誰が何曜日に提出する予定？','person_day','{a}さんが{day}に提出します。'),
 ('activity_place','{place}では{act}をします。','{place2}では{act2}をします。','{place2}で行うことは？','act2','{place2}では{act2}をします。'),
 ('item_destination','{item}を{place}へ運びます。','{item2}は{place2}へ運びます。','{item}の運び先を確認して。','place','{item}は{place}へ運びます。'),
 ('gift_pair','{a}への贈り物は{item}です。','渡す日は{day}です。','誰に何を渡すのかまとめて。','person_item','{a}さんに{item}を渡します。'),
 ('day_location','{day}は{place}に行きます。','{day2}は{place2}へ行きます。','{place}へ行くのは何曜日？','day','{place}へ行くのは{day}です。'),
 ('assigned_jobs','{a}が{act}を担当します。','{b}が{act2}を担当します。','{a}の仕事だけを教えて。','act','{a}さんの仕事は{act}です。'),
 ('snack_order','先に{food}を出します。','後から{food2}を出します。','最初に出す食べ物は何？','food','最初に出すのは{food}です。'),
 ('item_owner','{item}の持ち主は{a}です。','受け取り場所は{place}にします。','この品を誰に返せばいい？','a','持ち主の{a}さんに返します。'),
 ('schedule_pair','{time}に{act}をします。','{time2}には{act2}です。','最初の時刻とその作業をまとめて。','time_action','{time}に{act}をします。'),
 ('selected_route','行きは{place}を通ります。','帰りは{place2}を通る予定です。','帰りに通る場所を教えて。','place2','帰りは{place2}を通ります。'),
)

CLARIFICATION=(
 ('which_item','その品を買いたいです。','どの品を買いたいですか？','item'),
 ('which_person','あの人に伝えておいて。','誰に伝えればよいですか？','person'),
 ('which_place','そこへ行きたいです。','どこへ行きたいですか？','place'),
 ('which_date','その日に予約したいです。','何日に予約したいですか？','date'),
 ('which_time','いつもの時刻に集合しましょう。','集合する時刻を教えてください。','time'),
 ('quantity_missing','封筒を買う予定です。必要な数はまだ伝えていません。','封筒は何枚必要ですか？','quantity'),
 ('target_missing','どちらがよいか相談したいけれど、候補はまだ言っていません。','比較したい候補を教えてください。','options'),
 ('referent_missing','それを直してほしいです。まだ何を直すか説明していません。','何を直したいのか教えてください。','object'),
 ('destination_missing','荷物を届けたいのですが、届け先はまだ決めていません。','届け先はどこにしますか？','destination'),
 ('message_missing','連絡を送る文章を考えて。内容はこれから説明します。','伝えたい内容を教えてください。','content'),
 ('diet_context','食べる物を選びたいです。候補も好みもまだ話していません。','候補や食べたい物を教えてください。','choice'),
 ('meeting_missing','会う約束の時間を確認したいです。時間はまだ話していません。','約束した時刻を教えてください。','time'),
 ('lost_item','探し物を手伝って。何をなくしたかはまだ言っていません。','何をなくしましたか？','object'),
 ('name_ambiguous','同じ名字の二人がいます。どちらに渡すかはまだ決めていません。','どちらの方に渡しますか？','recipient'),
 ('count_ambiguous','一箱に入る数を知りたいです。箱の種類はまだ伝えていません。','どの種類の箱ですか？','box'),
 ('route_ambiguous','行き方を調べたいけれど、出発地も目的地も未定です。','出発地と目的地を教えてください。','route'),
 ('week_ambiguous','来週の予定をまとめて。具体的な予定はまだ伝えていません。','来週の予定を教えてください。','schedule'),
 ('borrow_ambiguous','借りた物を返したいです。誰から借りたかは話していません。','誰から借りた物ですか？','lender'),
 ('pronoun_ambiguous','二つの袋があります。「それを開けて」とだけ言いました。','どちらの袋を開けますか？','bag'),
 ('duration_missing','何分あれば終わるか知りたいです。作業の内容はまだ不明です。','どんな作業をする予定ですか？','task'),
 ('recipient_missing','贈り物の文章を考えて。相手との関係はまだ伝えていません。','誰への贈り物ですか？','recipient'),
 ('format_missing','文章を書き直してほしいです。元の文章はまだ送っていません。','書き直したい文章を送ってください。','text'),
 ('ordering_missing','二つの予定があります。順番はまだ決めていません。','どちらを先にする予定ですか？','order'),
 ('scope_missing','必要な物だけを一覧にしたいです。何の準備かはまだ不明です。','何のための準備ですか？','purpose'),
)

SPEAKER=(
 ('user_home','ここでは話す人は私です。私は{place}の近くに住んでいます。誰がそこに住んでいる？','あなたです。','user'),
 ('user_possession','私が{item}を持っています。あなたが持っていると断定してよいですか？','いいえ、持っているのはあなたです。','user'),
 ('quote_owner','{a}が「私は{item}を買いました」と言っています。買ったのは誰？','{a}さんです。','quoted_person'),
 ('proposal_fact','これは提案です。「{place}で会うのはどうでしょう」。もう決まった事実ですか？','いいえ、まだ提案です。','proposal'),
 ('user_feeling','私は今日は嬉しいです。この嬉しさは誰の気持ちとして話しましたか？','あなたの気持ちです。','user'),
 ('assistant_no_body','あなたは実際に{food}を食べた体験を持っていますか？','食べた体験はありません。','assistant_limit'),
 ('user_action','私は明日{act}をします。あなた自身の予定だと答えてよいですか？','いいえ、あなたの予定です。','user'),
 ('quote_plan','{b}の言葉は「私は{day}に出かけます」です。これは誰の予定？','{b}さんの予定です。','quoted_person'),
 ('two_speakers','{a}は{item}を、{b}は{item2}を選びました。{item2}を選んだ人は？','{b}さんです。','quoted_person'),
 ('user_preference','私は{food}が好きです。好きなのは私ですか、それともあなたですか？','あなたです。','user'),
 ('fiction_label','物語の登場人物が「私は{a}です」と言います。これはあなたの実名ですか？','いいえ、登場人物の名前です。','fiction'),
 ('suggestion_uncertain','あなたから「{act}はいかがですか」と提案されました。私がそうすると決めたことになりますか？','いいえ、決めたことにはなりません。','proposal'),
 ('user_request','私が{item}を借りたいとお願いしました。借りたいと言ったのは誰？','あなたです。','user'),
 ('quote_feeling','{a}が「嬉しい」と言い、私はまだ気持ちを話していません。嬉しいと言った人は？','{a}さんです。','quoted_person'),
 ('assistant_address','会話のためにあなたが住所を作って、本当の住所だと言えますか？','実際の住所は持っていません。','assistant_limit'),
 ('user_job','私の仕事は受付です。これは誰の仕事として伝えましたか？','あなたの仕事です。','user'),
 ('reported_not_verified','{a}が「{place}で待っている」と伝えてきました。あなたが現地で確認した事実ですか？','いいえ、{a}さんからの連絡です。','report'),
 ('future_not_past','私はこれから{act}をします。すでに終わったという意味ですか？','いいえ、これからする予定です。','future'),
 ('assistant_family','あなた自身に実際の家族がいると説明してよいですか？','実際の家族は持っていません。','assistant_limit'),
 ('user_friend','{a}は私の友人です。あなた自身の友人だと紹介してよいですか？','いいえ、あなたの友人です。','user'),
 ('hypothesis','もし{day}が休みなら{act}をしたい、と私が言いました。休みだと確定しましたか？','いいえ、まだ仮定です。','hypothesis'),
 ('quoted_request','{b}から「{item}を届けて」と頼まれました。お願いしたのは誰？','{b}さんです。','quoted_person'),
 ('user_memory','私の思い出を話しました。あなたが同じ体験をしたことになりますか？','いいえ、あなたの体験です。','user'),
 ('personal_fact_unknown','私は自分の名字をまだ伝えていません。名字を断定できますか？','まだ名字は分かりません。','unknown'),
)

DAILY=(
 ('greeting','こんにちは。少しお話ししてもいいですか？','こんにちは。どんなお話をしましょうか？'),
 ('evening','こんばんは。今日も一日が終わりました。','こんばんは。今日もお疲れさまでした。'),
 ('thanks','相談を聞いてくれてありがとう。','どういたしまして。話してくれてありがとうございます。'),
 ('tired','今日は忙しくて、少し疲れました。','お疲れさまでした。少し休めるといいですね。'),
 ('relief','気になっていた用事が終わり、ほっとしました。','無事に終わってよかったですね。'),
 ('joy','楽しみにしていた予定が決まりました。','それは楽しみですね。どんな予定ですか？'),
 ('nervous','明日初めての集まりに行くので緊張しています。','初めてだと緊張しますね。何が一番気になりますか？'),
 ('rain','雨の音を聞きながら、家でゆっくりしています。','落ち着いた時間ですね。何をして過ごしていますか？'),
 ('walk','今日は{place}の近くを散歩しました。','散歩はいかがでしたか？'),
 ('finished','やっと{act}が終わりました。','お疲れさまでした。一区切りつきましたね。'),
 ('lost','大切な{item}が見つからず、困っています。','それは困りますね。最後に見た場所は覚えていますか？'),
 ('friend','友人の{a}と久しぶりに会いました。','久しぶりに会えてよかったですね。どんな話をしましたか？'),
 ('cooking','今日は{food}を用意しました。','食事が楽しみですね。どんなふうに用意しましたか？'),
 ('weekend','週末は少しのんびりしたいです。','ゆっくりできるといいですね。何をして過ごしたいですか？'),
 ('reading','読んでいた本が面白くて、続きが楽しみです。','続きが気になりますね。どんなところが面白かったですか？'),
 ('small_success','昨日できなかったことが、今日はできました。','それは嬉しいですね。どんなことができたのですか？'),
 ('bored','今日は少し退屈しています。','何か気分転換をしてみたいですか？'),
 ('worried','明日の予定が気になって、落ち着きません。','気になりますね。どんなことが心配ですか？'),
 ('weather','今日は暖かくて過ごしやすいです。','過ごしやすい日ですね。外へ出る予定はありますか？'),
 ('preparation','{day}の予定に向けて準備しています。','準備は進んでいますか？'),
 ('hobby','最近、{act}をする時間が楽しいです。','楽しめる時間があるのはいいですね。'),
 ('farewell','そろそろ用事に戻ります。また話しましょう。','またお話ししましょう。用事が順調に進むといいですね。'),
 ('acknowledge','うまく説明できないけれど、話を聞いてほしいです。','はい。話せるところから聞かせてください。'),
 ('hope','今週は良い一週間になるといいなと思っています。','穏やかに過ごせるといいですね。楽しみな予定はありますか？'),
)

DAILY_EXPANDED=(
 'こんにちは。もちろんです。今日はどんなお話をしたいですか？',
 'こんばんは。一日お疲れさまでした。今日はどんな日でしたか？',
 'どういたしまして。話してくれてありがとうございます。また相談したいことがあれば聞かせてください。',
 '今日は忙しかったのですね。お疲れさまでした。これから少しゆっくり過ごせそうですか？',
 '気になっていた用事が無事に終わってよかったですね。少し落ち着いて過ごせそうですか？',
 '楽しみにしていた予定が決まって嬉しいですね。どんな予定なのか聞かせてください。',
 '初めての集まりは緊張しますね。どんなことが一番気になっているのか、話してみませんか？',
 '雨の音を聞きながら、家でゆっくり過ごしているのですね。今は何をして楽しんでいますか？',
 '{place}の近くを散歩したのですね。歩いていて、何か気になるものや景色はありましたか？',
 '{act}が終わって一区切りつきましたね。お疲れさまでした。これから少し休めそうですか？',
 '大切な{item}が見つからないのは困りますね。最後に見た場所や使った時のことは覚えていますか？',
 '友人の{a}さんと久しぶりに会えたのですね。どんな話をして過ごしたのか聞かせてください。',
 '今日は{food}を用意したのですね。食べるのが楽しみですね。どんなふうに用意しましたか？',
 '週末はゆっくりできるといいですね。家で休むなど、何かやってみたい過ごし方はありますか？',
 '面白い本に出会えてよかったですね。続きも楽しみですね。どんなところが気に入りましたか？',
 '昨日できなかったことが今日はできたのですね。嬉しい変化ですね。どんなことができたのでしょうか？',
 '少し退屈しているのですね。気分を変えるために、何か楽しめそうなことを一緒に考えてみますか？',
 '明日の予定が気になっているのですね。どんなことが心配なのか、話せる範囲で聞かせてください。',
 '暖かくて過ごしやすいのは嬉しいですね。今日は外へ出るなど、何かしたいことがありますか？',
 '{day}の予定に向けて準備を進めているのですね。今はどんな準備をしているところですか？',
 '最近は{act}をする時間が楽しいのですね。どんなところを楽しんでいるのか、聞かせてください。',
 'はい、またお話ししましょう。これからの用事が順調に進むといいですね。どうぞ気をつけて。',
 'はい。うまくまとめようとしなくても大丈夫です。今話せそうなところから、ゆっくり聞かせてください。',
 '良い一週間になるといいですね。穏やかに過ごすために、何か楽しみにしていることはありますか？',
)


def variables(rng):
    state={}
    for first,second,values in [('a','b',NAMES),('place','place2',PLACES),('item','item2',ITEMS),
            ('food','food2',FOODS),('day','day2',DAYS),('act','act2',ACTIONS),('time','time2',TIMES),('qty','qty2',QTY)]:
        state[first],state[second]=rng.sample(values,2)
    # Within-day schedule examples keep the first time before the second.
    state['time'],state['time2']=sorted((state['time'],state['time2']),key=TIMES.index)
    state['user_name']=rng.choice([name for name in NAMES if name not in (state['a'],state['b'])])
    state['number_style']=rng.choice(('kanji','arabic'))
    state['time']=clock_style(state['time'],state['number_style'])
    state['time2']=clock_style(state['time2'],state['number_style'])
    state['one'],state['two'],state['three']=rng.sample(ITEMS,3)
    return state


def resolved(key,state):
    if key in state:return state[key]
    operations=dict(pair=lambda:f"{state['one']}と{state['two']}",
        time_place=lambda:f"{state['time']}、{state['place']}",
        actions=lambda:f"{state['act']}、{state['act2']}",places=lambda:f"{state['place']}、{state['place2']}",
        person_day=lambda:f"{state['a']}、{state['day']}",person_item=lambda:f"{state['a']}、{state['item']}",
        time_action=lambda:f"{state['time']}、{state['act']}")
    return operations[key]() if key in operations else key


def render(category,index,variant):
    rng=random.Random(f'plan133-train-v1:{category}:{index}:{variant}')
    state=variables(rng);before=None;earlier=[]
    if category=='direct':
        name,prompt,key,full=DIRECT[index];answer=resolved(key,state)
        if name in ('quantity','written_number'):
            state['qty']=quantity(QTY.index(state['qty']),FOOD_COUNTERS.get(state['food'],'個'),state['number_style'])
            answer=resolved(key,state)
        if name in ('completed','remaining'):
            state['act'],state['act2']=rng.sample(TASKS,2);answer=resolved(key,state)
        if name=='purpose':state['place']=rng.choice(ACTIVITY_PLACES[state['act']])
        if name=='speaker_request':
            state['item']=rng.choice(BORROWABLE);answer=resolved(key,state)
    elif category=='correction':
        name,first,prompt,full,kind=CORRECTION[index]
        choices=dict(place=PLACES,time=TIMES,qty=QTY,day=DAYS,name=NAMES,item=ITEMS,food=FOODS,action=ACTIONS)[kind]
        if name in ('task','last_job'):choices=TASKS
        state['old'],state['new']=rng.sample(choices,2)
        if name in ('arrival','deadline'):
            state['old'],state['new']=sorted((state['old'],state['new']),key=TIMES.index)
        if kind=='time':
            state['old']=clock_style(state['old'],state['number_style']);state['new']=clock_style(state['new'],state['number_style'])
        if name in ('reservation','packet'):
            counter='席' if name=='reservation' else '袋'
            state['old']=quantity(QTY.index(state['old']),counter,state['number_style'])
            state['new']=quantity(QTY.index(state['new']),counter,state['number_style'])
        before=state['old'];answer=state['new']
        earlier=[dict(role='user',text=first.format(**state)),dict(role='assistant',text='承知しました。')]
    elif category=='negation':
        name,prompt,key,full=NEGATION[index];answer=resolved(key,state)
    elif category=='context':
        name,first,second,prompt,key,full=CONTEXT[index];answer=resolved(key,state)
        if name in ('assigned_jobs','remember_name','task_order','schedule_pair'):
            state['act'],state['act2']=rng.sample(TASKS,2);answer=resolved(key,state)
        if name=='activity_place':
            state['place']=rng.choice(ACTIVITY_PLACES[state['act']])
            alternatives=[p for p in ACTIVITY_PLACES[state['act2']] if p!=state['place']]
            state['place2']=rng.choice(alternatives)
        if name=='quantity_item':
            state['qty']=quantity(QTY.index(state['qty']),ITEM_COUNTERS[state['item']],state['number_style'])
            state['qty2']=quantity(QTY.index(state['qty2']),ITEM_COUNTERS[state['item2']],state['number_style'])
            answer=resolved(key,state)
        if name=='loan_return':
            state['item'],state['item2']=rng.sample(BORROWABLE,2);answer=resolved(key,state)
        earlier=[dict(role='user',text=first.format(**state)),dict(role='assistant',text='分かりました。'),
            dict(role='user',text=second.format(**state)),dict(role='assistant',text='覚えておきます。')]
    elif category in ('clarification','speaker','daily'):
        row=dict(clarification=CLARIFICATION,speaker=SPEAKER,daily=DAILY)[category][index]
        name,prompt,full=row[:3];answer=full.format(**state)
        if category=='speaker' and name=='user_request':state['item']=rng.choice(BORROWABLE)
        if category=='daily' and variant%4>=2:
            full=DAILY_EXPANDED[index];answer=full.format(**state)
        # Near variants all remain the SAME scenario family. These backgrounds
        # add turn/wording diversity, not independent semantic tasks or evidence.
        # They disclose a given name only, never the requested missing field.
        opener=OPENERS[variant%len(OPENERS)]
        earlier=[dict(role='user',text=f"私は{state['user_name']}といいます。{opener}"),
            dict(role='assistant',text='はい。お話を聞かせてください。')]
        if category=='daily':
            earlier[0]['text']=f"私は{state['user_name']}といいます。今週は{state['day']}に時間があります。{opener}"
    else:raise ValueError(category)
    if category in ('direct','negation'):
        # Additional known user identity varies the surrounding dialogue, while
        # the whole task still belongs to its original scenario family.
        earlier=[dict(role='user',text=f"私は{state['user_name']}といいます。{OPENERS[variant%len(OPENERS)]}"),
            dict(role='assistant',text='はい。どうぞ。')]
    # Introductions are optional. Most single-turn tasks begin with the actual
    # request. Multi-turn state tasks retain only relevant prior facts.
    if category in ('daily','direct','negation','clarification','speaker') and variant%5!=0:
        earlier=[]
    if category in ('correction','context'):
        # First factual turns receive supervision. Acknowledge the User's
        # facts without repeating a first-person statement as the Assistant.
        for offset in range(0,len(earlier),2):
            earlier[offset+1]['text']=('分かりました。','確認しました。',
                '承知しました。','はい、覚えておきます。')[(variant+offset)%4]
    prompt=prompt.format(**state)
    if not earlier and category!='daily':
        # A request may arrive with ordinary context in the SAME first User
        # turn. No preceding gold Assistant is needed to answer it.
        colors=('青','赤','緑','黄色','白','茶色')
        if variant%7<5:
            prompt=f"{state['day']}のメモを、{colors[(variant//7)%len(colors)]}の紙に書いています。"+prompt
    if category=='daily' and not earlier:
        # Real first-User contexts, rather than an obligatory named greeting
        # followed by a gold Assistant. These remain near family variants.
        backgrounds=('','今日は{day}です。','外は晴れています。','外は曇っています。',
            '窓の外で雨の音がしています。','今日は家で過ごしています。',
            '今は休み時間です。','少し落ち着いたところです。')
        background=backgrounds[(variant//5)%len(backgrounds)].format(**state)
        if variant%7<4:
            background=f"今日は{state['day']}です。"+background
        prompt=background+prompt
    # Authored paraphrase rules preserve facts and requested answer formats.
    # All such variants remain in their original semantic scenario family.
    if variant%3==1:
        for original,replacement in (('教えてください。','教えてもらえますか？'),
            ('答えてください。','答えてもらえますか？'),('答えて。','教えて。'),
            ('今の','現在の'),('どちらですか？','どちらになりますか？')):
            prompt=prompt.replace(original,replacement)
    elif variant%3==2:
        for original,replacement in (('予定です。','予定にしています。'),
            ('教えて。','確認したいです。'),('だけ教えて。','だけ確認したいです。')):
            prompt=prompt.replace(original,replacement)
    full=full.format(**state)
    # Natural dialogue and clarification are not expanded with an unrelated filler.
    # Explicit requested formats account for short versus fuller direct answers.
    mode=variant%4
    if category in ('direct','correction','negation','context'):
        if mode==0:
            prompt+='短い答えだけでお願いします。';body=answer+'。'
        elif mode==1:body=full
        elif mode==2:
            prompt+='確認のため、答えを一文で返してください。';body=full
        else:
            prompt+='理由も短く添えてください。'
            if category=='correction':
                body=full+f"{state['old']}から{state['new']}へ変更されたので、新しい方を使います。"
            elif category=='direct':
                explanations=dict(
                    owner='{item}を預かっているのが{a}さんだからです。',
                    destination='届け先が{place}に指定されています。',
                    meeting_time='{time}に待ち合わせると決めているからです。',
                    weekday='案内に{day}が休館日と書かれています。',
                    quantity='{food}を袋に{qty}入れたためです。',
                    first_step='{act}を済ませてから{act2}をする順番です。',
                    last_step='{act}を先に行い、{act2}を最後にする予定です。',
                    choice='{item}も候補でしたが、選んだ方は{item2}です。',
                    label='その箱には{item}が入っています。',
                    reason='{day}は休みで、{act}の時間を取れるためです。',
                    name_lookup='担当表で{a}さんを案内係としています。',
                    location_lookup='{place}にある{item}とは、置き場所が違います。',
                    before='{time}に{act}、{time2}に{act2}という順番です。',
                    after='{act}の後に{act2}をする順番だからです。',
                    recipient='{food}は{a}さんに渡すための分だからです。',
                    start_place='{place}を出て、{place2}へ向かう予定です。',
                    end_place='{place}から{place2}へ行く道順だからです。',
                    container='{item}の方は袋に入っています。',
                    written_number='購入メモで{food}の数を{qty}としています。',
                    available_day='空いている曜日が{day}だからです。',
                    purpose='{place}へ行くのは{act}をするためです。',
                    speaker_request='{a}さんが{item}を借りたいと言ったためです。',
                    completed='{act2}の方はまだ終わっていません。',
                    remaining='{act}は済んでいて、{act2}はまだだからです。')
                body=full+explanations[name].format(**state)
            elif category=='negation':
                explanations=dict(
                    exclude='{one}は選ばない条件だからです。',
                    only='{two}は今回使わないためです。',
                    without='{two}と{three}を除くと、{one}だけが残ります。',
                    not_both='{two}は選べず、一つだけ選ぶためです。',
                    accepted='{two}は受付で許可されていません。',
                    remove='{one}を取り出したからです。',
                    replace='{one}の代わりに{two}を使うためです。',
                    forbidden='{one}は禁止されているからです。',
                    exception='{one}と{two}は配らない条件だからです。',
                    cancel='{one}の注文は取り消されているためです。',
                    negative_fact='{one}ではないと分かっているからです。',
                    allowed_pair='{three}は使わない条件だからです。',
                    leave_pair='{three}を候補から除いたためです。',
                    avoid_question='{two}を避けたいとのことだからです。',
                    satisfy_both='{one}を除き、一つ選ぶ条件だからです。',
                    do_not_add='{two}を追加しない条件だからです。',
                    empty_except='{one}と{two}は箱から出したためです。',
                    reject_offer='{one}の提案は断っているためです。',
                    restriction_change='{one}は今、使えないためです。',
                    affirmative='{two}を選ばないと指定されているためです。',
                    deny_identity='{one}は正解でないと分かったためです。',
                    keep_selected='{two}を外しているためです。',
                    output_rule='{one}は禁止されているためです。',
                    two_conditions='{one}と{three}を除く条件だからです。')
                body=full+explanations[name].format(**state)
            else:
                # Specific supplied facts, not invented reasoning. Both facts
                # are explicitly requested here, keeping the response relevant.
                prompt+='最初に伝えた事実も引用して確認してください。'
                body=full+f"最初の情報は「{first.format(**state)}」です。"
    else:body=full
    if category=='negation' and name=='output_rule':
        # Preserve the name-only instruction in all format variants.
        prompt=NEGATION[index][1].format(**state);body=answer
    messages=earlier+[dict(role='user',text=prompt),dict(role='assistant',text=body)]
    return dict(doc_id=f'd1-{category}-{name}-{variant:06d}',split='train',messages=messages,
        target_message_indices=[len(messages)-1],category=category,family=f'authored-{category}-{name}',
        source='project-authored-plan133-train',license='project-authored',
        grounding=dict(operation=name,state=state,answer=answer,previous_value=before,
            full_answer=full,mode=mode,oracle='typed-state-operation-v1'),
        editing_reason='plan133 independent recipe; mostly no introduction; first factual turns receive separate selected targets')


def render_targets(category,index,variant):
    """Prefixes teach previously unsupervised first/middle factual replies.

    A prefix has one selected final Assistant, retaining the proven sampler
    contract. Prefixes and wording variants remain in the original family.
    """
    full=render(category,index,variant)
    targets=[full]
    if category in ('correction','context') and variant%4==0:
        for position in range(1,len(full['messages'])-2,2):
            record=dict(full,messages=full['messages'][:position+1],
                target_message_indices=[position],doc_id=full['doc_id']+f'-prefix{position}',
                target_kind='first_turn' if position==1 else 'middle_turn')
            targets.append(record)
    full['target_kind']='final'
    return targets


def semantic_check(record):
    """Recompute the entire rendering and state; catches state/answer/turn edits."""
    if record['source']!='project-authored-plan133-train':raise ValueError('Not an authored recipe')
    category=record['category'];doc_id=record['doc_id'].split('-prefix')[0]
    variant=int(doc_id.rsplit('-',1)[1])
    table=dict(daily=DAILY,direct=DIRECT,correction=CORRECTION,negation=NEGATION,
        context=CONTEXT,clarification=CLARIFICATION,speaker=SPEAKER)[category]
    family=record['family'];index=next(i for i,row in enumerate(table) if family==f'authored-{category}-{row[0]}')
    expected=next(r for r in render_targets(category,index,variant) if r['doc_id']==record['doc_id'])
    return all(record[key]==expected[key] for key in ('messages','grounding','target_message_indices','doc_id'))
