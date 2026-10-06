"""Authored natural continuations and an explicit optimizer-policy fork."""
import hashlib
from jmicro.packing_study import PackingTrainer

# Each scene states a concrete action and its outcome; no QA labels or fantasy.
SCENES = [
 ('{a}は朝、公園の入口で友達を待っていた。','友達が手を振りながら歩いてきた。二人は並んで池まで散歩し、ベンチで少し休んだ。'),
 ('{a}は帰り道に、小さなパン屋へ入った。','店内には焼きたてのパンの香りが広がっていた。丸いパンを一つ買い、家でお茶と一緒に食べた。'),
 ('{a}は机の上で読みかけの本を開いた。','昨日挟んだしおりの場所から続きを読んだ。一章を読み終えると、本を閉じて棚に戻した。'),
 ('{a}は玄関を出たところで雨に気づいた。','いったん家に戻り、傘を持って出直した。傘のおかげで、服をぬらさずに駅まで歩けた。'),
 ('{a}は台所で野菜を洗った。','洗った野菜を小さく切り、鍋に入れて煮込んだ。温かいスープができ、家族と食卓を囲んだ。'),
 ('{a}は庭の土が乾いているのを見つけた。','じょうろに水を入れて、花の根元に静かに注いだ。水が土にしみ込むのを確かめ、じょうろを片づけた。'),
 ('{a}は図書館で借りた本を持って受付へ行った。','係の人に本を返し、返却が済んだことを確認した。それから新しく読みたい本を探した。'),
 ('{a}は靴の泥を落とそうと、玄関に座った。','ブラシで泥を払い、布で表面を拭いた。きれいになった靴をそろえて置き、作業を終えた。'),
 ('{a}は友達から届いた手紙を読んだ。','元気に暮らしていると分かり、うれしくなった。便せんを取り出し、近況を伝える返事を書いた。'),
 ('{a}は買い物の前に冷蔵庫を開けた。','足りないものを紙に書き、店へ持っていった。必要なものだけを買えたので、無駄な買い物をせずに済んだ。'),
 ('{a}は電車の窓から川を眺めていた。','橋を渡ると、水面が朝の光を反射した。目的の駅に着いたので、荷物を持って電車を降りた。'),
 ('{a}は落ちていた手袋を道の端で見つけた。','近くを歩く人が片方の手袋を探していた。声をかけて渡すと、その人は笑顔でお礼を言った。'),
 ('{a}は部屋の窓を開けた。','涼しい風が入り、こもっていた空気が入れ替わった。しばらくして窓を閉め、机に向かった。'),
 ('{a}は散歩から帰ると、手を洗った。','せっけんを流してタオルで拭き、食卓についた。家族が用意した昼ご飯を一緒に食べた。'),
 ('{a}は友達と夕方の待ち合わせ場所を決めた。','約束の時間より少し早く駅前へ着いた。友達も時間どおりに来たので、二人で店へ向かった。'),
 ('{a}は棚から空の箱を取り出した。','散らばっていた写真を一枚ずつ箱に入れた。机が片づき、必要な写真も探しやすくなった。'),
 ('{a}は風で飛ばされた洗濯物を庭で拾った。','汚れたので洗い直し、今度は洗濯ばさみで留めた。乾いた後に取り込み、丁寧に畳んだ。'),
 ('{a}は道を尋ねてきた人の話を聞いた。','その人が探していた郵便局は角を曲がった先にあった。行き方を伝えると、その人はお礼を言って歩き出した。'),
 ('{a}は自転車に乗る前にタイヤを確かめた。','空気が少なかったので、空気入れで補充した。十分に入ったことを確認し、公園へ出かけた。'),
 ('{a}は台所でコップを落として割ってしまった。','破片を踏まないように片づけ、床に残っていないか確かめた。掃除を終えると、新しいコップを棚から出した。'),
 ('{a}は夕食の後で皿を洗った。','泡をよく流し、水切りかごに並べた。乾いた皿を棚に戻すと、流し台もすっきりした。'),
 ('{a}は冷たい風を感じて上着を取りに戻った。','上着を着ると暖かくなり、外へ出る支度が整った。戸締まりを確かめてから出かけた。'),
 ('{a}は友達に借りた傘を持って出かけた。','待ち合わせ場所で傘を返し、助かったと伝えた。友達はうなずき、傘をかばんにしまった。'),
 ('{a}は部屋の時計が止まっていることに気づいた。','新しい電池に交換すると、針が動き始めた。正しい時刻に合わせ、時計を壁に戻した。'),
 ('{a}は夕方、洗った米を炊飯器に入れた。','水を量って加え、ふたを閉めて炊き始めた。ご飯が炊けたら、茶わんによそって家族に渡した。'),
 ('{a}は公園で小鳥の声を聞いた。','木の枝に小鳥が止まっているのを見つけた。しばらく静かに眺め、小鳥が飛び去ると散歩を続けた。'),
 ('{a}は寝る前に明日の持ち物を確かめた。','必要な書類をかばんに入れ、玄関に置いた。準備が済んだので、明かりを消して床についた。'),
 ('{a}は久しぶりに家族へ電話をかけた。','お互いの近況を話し、次に会う日を相談した。電話を切ると、会える日が楽しみになった。'),
 ('{a}は駅の階段で重そうな荷物を持つ人を見かけた。','手伝いが必要か尋ねると、その人はうなずいた。荷物を一緒に運び終えると、お礼を言われた。'),
 ('{a}は机に置いた鉛筆の先を確かめた。','先が丸くなっていたので、鉛筆削りで削った。削りくずを捨て、ノートに続きを書いた。'),
 ('{a}は休みの日に近所の川沿いを歩いた。','道ばたに咲く花を見ながら、ゆっくり橋まで進んだ。気分が落ち着いたので、来た道を戻って家に帰った。'),
 ('{a}は友達の誕生日にカードを書いた。','日頃のお礼とお祝いの言葉を添え、封筒に入れた。友達に渡すと、うれしそうに受け取ってくれた。'),
]
TRAIN_NAMES=('あおい','ひなた','みどり','なお','ゆう','まこと','はる','りょう','あきら','けん','さくら','たくみ','なつ','ふみ','まい','りん','えり','かず','ほのか','れん','智史','智也','太郎','恭子','美咲','健太','花','葵','真理','夏子','春子','大輔')
DEV_NAMES=('しおり','さとる','かえで','つばさ','すみれ','いおり','千尋','直子')
EXPANDED_NAMES=tuple(surname+name for surname in ('佐藤','鈴木','高橋','田中','伊藤','渡辺','山本','中村') for name in TRAIN_NAMES)


def material(split,count):
    names=TRAIN_NAMES if split=='train' else EXPANDED_NAMES if split=='expanded' else DEV_NAMES
    maximum=len(names)*len(SCENES)
    if not 0<count<=maximum:raise ValueError('Unique scene supply exceeded')
    records=[]
    for i in range(count):
        scene=i%len(SCENES);name=names[i//len(SCENES)]
        first,last=SCENES[scene]
        prefix=first.format(a=name)+'\n';text=prefix+last.format(a=name)
        records.append(dict(id=f'natural-{split}-{i:04d}',doc_id=f'natural-{split}-{i:04d}',split='train' if split=='expanded' else split,kind='web',
            bucket='authored-natural',scene=scene,prefix=prefix,continuation=last.format(a=name),text=text,
            canonical_sha256=hashlib.sha256(text.encode()).hexdigest(),
            provenance='Codex authored32 reviewed everyday scenes; lexical variants, not independent human certification'))
    assert len({r['text'] for r in records})==len(records)
    assert len({r['prefix'] for r in records})==len(records)
    return records


def apply_optimizer_policy(optimizer,policy):
    if policy not in ('inherit','fresh'):raise ValueError('Unknown optimizer policy')
    if policy=='fresh':optimizer.state.clear()


class NaturalTrainer(PackingTrainer):
    def __init__(self,parent,web,short,mode,goals,binding,device='cuda'):
        super().__init__(parent,web,short,mode,goals,binding,device)
        apply_optimizer_policy(self.optimizer,binding['optimizer_policy'])
        if binding['optimizer_policy']=='fresh':
            self.lineage['learning_rate_fork']['moments_weights_RNG_cursors_preserved']=False
        self.lineage.update(optimizer_policy=binding['optimizer_policy'],
            initialization=binding.get('initialization','original10B'),optimizer_reset_only_at_fork=True)
