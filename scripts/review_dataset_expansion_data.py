"""Save Codex's actual individual inspection of the fixed random40 full stories."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from probe_dataset_expansion_supply import DATA

NOTES=[
 (0,False,'帽子を追いかけて持ち主へ返す行動と結末がつながる。'),
 (1,False,'惑星と風の擬人化という設定の中で孤独から遊びへの展開が完結する。'),
 (2,False,'時を止める道具の発見と使用、幸福という短い幻想の結末。'),
 (3,True,'夢を描く／見るの意味が曖昧で、「ていねいな友達」の導入も不自然。'),
 (4,False,'働く村で少し遊んで再開する提案がまとまる。'),
 (5,True,'協力して食べ物を取り戻す作戦の内容がなく、追い払うことと回収のつながりが弱い。'),
 (6,True,'ミサイルと踊る幻想だが、座って回る・飛び降りる位置や行動の因果が曖昧。'),
 (7,True,'車をなくした話から恥ずかしがり屋でよいという教訓へ飛び、教訓の関連が弱い。'),
 (8,True,'花瓶の修復は追えるが、何でも粘土で直せるという結末の一般化が強い。'),
 (9,False,'なくしたおもちゃを探し、新しいものを作る行動と喜びの結末がつながる。'),
 (10,False,'二人が夢を共有して励ますという一つの場面が完結。'),
 (11,True,'「けっこう、ひまわり畑で」の導入が不自然で、友達の助けの内容も薄い。'),
 (12,False,'栗拾いから栗ごはんを作り食べる時系列が通る。'),
 (13,True,'魚を捕る海賊が助ける理由と「海賊たちはお礼に」の主体が弱い。'),
 (14,True,'年齢・健康を理由とした禁止からお手伝いで許可へ変わり、最初の条件を説明しない。'),
 (15,True,'「けれども」で始まり、前の条件が欠けた導入。飛べるようになる筋は追える。'),
 (16,False,'「お庭でお外」は冗長だが、カエルへの恐怖を母の説明と再挑戦で解く筋は通る。'),
 (17,False,'動物の速さに応じて役割を分けて木の実を取る展開が追える。'),
 (18,False,'宝の不在への怒りから周囲の美しさへの気づきへ移り、感情の変化で終わる。'),
 (19,False,'動物の料理という設定で材料、調理、食べる順序が完結。'),
 (20,False,'おもちゃを集め、友達と遊び、保管するまとまりがある。'),
 (21,True,'落選から分かち合う喜びは追えるが、「希望は結果じゃない」の教訓が曖昧。'),
 (22,False,'家族のピクニックの場面と一日の終わりが自然につながる。'),
 (23,False,'宇宙の女の子の幻想設定で地球訪問と人を元気にする結末がまとまる。'),
 (24,True,'駅への移動や家族の登場が省略され、新しい冒険で終わるため具体的な結末が弱い。'),
 (25,True,'宝物の材質・形が不明でフォトフレームへの変化が急、礼儀という教訓も筋と弱くつながる。'),
 (26,True,'持つ向きを直す解決は追えるが、一つの経験で常に安いモップを買うという一般化が強い。'),
 (27,False,'友達の登場で深い場所への恐怖が解ける短い筋。'),
 (28,False,'冬の遊びや飲み物を友達と楽しむ場面が幸福という結末へつながる。'),
 (29,False,'禁止、警備員の注意、発砲、逮捕という因果は追える。暴力を含む物語であり全教材を児童向けとは扱わない。'),
 (30,False,'庭でコインを見つけ友達に見せ、宝探しの思い出になる順序が通る。'),
 (31,False,'海辺で集めた物より共有した時間を宝物とする結末がまとまる。'),
 (32,True,'窓やドアを閉めると竜巻が入れず去るという因果は現実の説明として誤り。幻想・擬人化を含む。'),
 (33,False,'焼き上がるまで待つ条件を守り、ケーキ一切れを受け取る筋が通る。'),
 (34,False,'けがをした鳥を保護し、回復して飛び立つまでが完結。'),
 (35,True,'「じゅうぶんな森」の形容が不自然。大きな音への反省と静かな演奏は追える。'),
 (36,True,'冒頭の「やがて」に先行する出来事がなく、悪い星との戦いの具体性も弱い。'),
 (37,True,'「よい夜」が不自然で、冒険に向けた小さな一歩の具体的行動がない。'),
 (38,True,'草原が小さくなった理由がなく、新しい場所探しへ進む動機の説明が薄い。'),
 (39,False,'歌で花が咲く幻想の筋で、鳥との交流と開花の結末がまとまる。')]

def main():
    samples=read_json(DATA/'shards/samples.json')['rows'];ready=read_json(DATA/'shards/ready.json')
    assert len(samples)==len(NOTES)==40 and [r[0] for r in NOTES]==list(range(40))
    notes=[dict(sample_position=i,text_sha256=samples[i]['text_sha256'],source=samples[i]['source'],weak_example=weak,rationale=reason) for i,weak,reason in NOTES]
    result=dict(status='inspected_accepted_for_bounded_comparison',accepted_for_experiment=True,
        ready_sha256=sha256(DATA/'shards/ready.json'),manifest_sha256=sha256(DATA/'shards/manifest.json'),
        samples_sha256=sha256(DATA/'shards/samples.json'),reviewer_sha256=sha256(Path(__file__)),notes=notes,
        weak_examples=sum(r['weak_example'] for r in notes),
        comparison_interpretation='Amount plus new source/length/EOS density, not amount-only; all old stories retained',
        source_selection='Existing retained selector unchanged; new translated full-story selector32–512 tokens/2–24sentences/4gram repetition<=0.15',
        content_limit='Nonblind Codex sample diagnosis. Weak causality, translation artifacts, fantasy and violent stories remain; not factual or child-safe certification. Whole-corpus independent overlap audit incomplete.',
        original_validation_test_used=False,independent_human_certification=False,checked_at=now())
    assert ready['totals']['tokens']>=200000000
    write_json(DATA/'content-review.json',result)
    print(f"Inspected all40 whole stories;{result['weak_examples']} weak examples disclosed; bounded expanded-source comparison accepted")

if __name__=='__main__':main()
