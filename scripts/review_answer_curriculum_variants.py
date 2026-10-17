"""Literal content review of all32 rendered TRAIN phrasing variants."""
from answer_learning_common import RUN,save,ref,bound,read_json,now

NOTES=[
 ('name',0,'アオイと名乗った本人への名前の再質問にアオイさんと答えている。'),
 ('name',1,'さっき伝えた名前という言い換えに、冒頭のアオイを参照している。'),
 ('name',2,'名前を尋ねる過去形の質問に、冒頭で示した名前を返している。'),
 ('name',3,'何さんと呼ぶかという依頼に、示された名前へさんを付けて答える。'),
 ('preference',0,'冒頭で紅茶が好きと述べた本人に、紅茶と直接回答している。'),
 ('preference',1,'覚えているかの問いに単に肯定せず、好きな紅茶を具体的に返す。'),
 ('preference',2,'どの飲み物だったかという質問に、名前ではなく紅茶を返す。'),
 ('preference',3,'好みを一言で尋ねられ、与えられた飲み物の紅茶を返している。'),
 ('correction',0,'6時から7時へ変更された後の集合時刻として7時を答える。'),
 ('correction',1,'7時という古い情報を使わず、訂正後の8時を答えている。'),
 ('correction',2,'8時から9時へ変更されており、後に示された9時を選ぶ。'),
 ('correction',3,'最初の9時ではなく、最後に確定した10時を返している。'),
 ('quantity',0,'青も赤も1個とされた場合で、青の問いに1個と答えている。'),
 ('quantity',1,'赤1個と混同せず、指定された青い箱の2個を返す。'),
 ('quantity',2,'青3個ではなく、質問された赤い箱の1個を返している。'),
 ('quantity',3,'青4個の情報に引かれず、赤い箱に対応する1個を答える。'),
 ('owner',0,'地図を持つカエデと区別し、鍵を持つアオイを答えている。'),
 ('owner',1,'鍵の持ち主であるカエデを選び、コハルの地図と混同しない。'),
 ('owner',2,'コハルが持つ鍵ではなく、地図を持つシオンを答えている。'),
 ('owner',3,'名前を尋ねる対象は地図なので、ツバサという持ち主を返す。'),
 ('literal',0,'指定されたりんごの一語だけを返し、説明や句点を足していない。'),
 ('literal',1,'返事を一語にという指示に従い、りんごだけを出している。'),
 ('literal',2,'説明不要という指示を守り、引用内のりんごだけを返す。'),
 ('literal',3,'指定語を尋ねる表現の違いに対しても、りんごだけを返す。'),
 ('arithmetic',0,'0個に0個を足すと0個であり、単位も問題に対応する。'),
 ('arithmetic',1,'1個の箱に0個を追加するため、合計1個という回答が正しい。'),
 ('arithmetic',2,'2個と0個を合わせると2個であり、質問に直接答えている。'),
 ('arithmetic',3,'最初の3個から追加が0個なので、合計3個と正しく答える。'),
 ('missing',0,'公園と服装しか示されておらず、約束の時刻を推測せず確認する。'),
 ('missing',1,'待ち合わせ場所から時刻は分からないため、未提供と伝えて尋ねる。'),
 ('missing',2,'予約という言い方になっても時刻の根拠はなく、推測で埋めない。'),
 ('missing',3,'会う時刻は会話で未指定であり、不足情報だけを短く確認する。')
]


def main():
    target=RUN/'curriculum_variant_QA_review.json';assert not target.exists()
    inventory=read_json(RUN/'curriculum_synthetic_inventory.json');rows=read_json(bound(inventory['variant_sample']))
    assert len(rows)==len(NOTES)==32
    notes=[]
    for row,(family,variant,reason) in zip(rows,NOTES,strict=True):
        assert (row['family'],row['variant'])==(family,variant)
        notes.append(dict(doc_id=row['doc_id'],family=family,variant=variant,accepted=True,rationale=reason))
    save(target,dict(status='all32_rendered_variants_reviewed',created_at=now(),
        inventory=ref(RUN/'curriculum_synthetic_inventory.json'),sample=inventory['variant_sample'],
        judgments=notes,authored_review_source=ref(__file__),reviewer='Codex nonblind; full32 rendered dialogues displayed',
        caveats=['All2048 rendered answers separately verified by the text-derived oracle; only32 full dialogues manually displayed',
            'Templates and values are finite; quantity/color and key/map mention positions are fixed in TRAIN',
            'This is authored synthetic TRAIN, not an independent natural conversation corpus',
            'No inference about unseen response quality or general capability follows from these checks'],
        new_training_updates=0,new_TEST_created=False))
    print('All32 content notes bound; no unseen quality claim')


if __name__=='__main__':main()
