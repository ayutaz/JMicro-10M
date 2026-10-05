"""Raw-bound, non-blind material review; a failed pool stays failed."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now

V2_WEAK={7:'湯たんぽのようにマラソンをする比喩が不自然',10:'せっかく冬の雪が降るという導入が不自然',
19:'なかなか星の夜が訪れるという導入が不自然',22:'馬の導入から人の兄妹のレースへ説明なしに移る',
24:'車の色変更で不可視になり自分を大事にする教訓へ飛ぶ',25:'にしんのようにおもちゃを探す比喩が不自然',
36:'妹が玩具を欲しがるだけで兄が嫉妬する関係が不明',37:'失ったものを最後に述べるがそれまで示していない',
42:'宝探しから失ったものへの照応が示されていない',47:'ざっくりした知恵という導入が不自然',
48:'セミナーの宣伝と未提示の参加案内',50:'カメラあり/なしの例を挙げるが実例がない',
51:'育毛製品の宣伝と使う/使わないの説明が混乱',52:'糖質制限から最後に血圧へ対象が変わる',
53:'本セミナーの未提示催しを告知する文',54:'サイト制作意図と唯一という自己宣伝',
55:'ゲーム展示告知と来場/プレゼントの宣伝',59:'チーム加入の呼びかけを含む',
61:'治療製品の宣伝',63:'ソフトウェア提供の宣伝'}
V3_WEAK={21:'ごちそうな空気という導入が不自然',35:'いっぱいいっぱいの星という数量表現が不自然',
39:'高く、妹が花を見つけるという導入の係り先がない',46:'誕生日パーティーを準備して叫んだ後に誕生日を忘れたという因果の飛躍',
51:'会社自身の制度/職場の自己PR',54:'翻訳アプリの説明に便利/役立つという推奨が重なる',
57:'接骨院の施術実績/専門性の自己宣伝',58:'ゲーム紹介から利用を勧める呼びかけを含む',
62:'アカウントの能力等の語法破綻と求人登録の誘導',63:'復旧業者への委託が最適という宣伝/誘導'}
V3_NOTES=[
'夢の村への創作として踊り/思い出へ完結。日常限定ではない。','彫刻と友人の応援の因果がある。','授業の会話と友情の話が同じ主題で完結。',
'雲と夢の小さな創作。完結する。','絵と友人の感動の短い説明。','きつねの宝探しの創作。擬人化を誤りとしない。',
'温泉で友人と過ごす気持ちを完結。','サッカーと友人の活躍をつなぐ。','星の物語を夢の動機にする。',
'りんごを友人と分ける流れ。','昔の日本への創作で花見の気持ちを完結。','収穫と人助けで共有の喜びへつなぐ。',
'果物の買物/分け合いを同じ対象で完結。','クマへの伝説の擬人化を前提に伝える意味を完結。','雨の日の歌の体験として完結。',
'話す星という幻想の中で家族の絆へつなぐ。','星の夢を聞く幻想として完結。','川での遊びと仲間の気持ちをつなぐ。',
'タヌキの迷子/帰宅の擬人化物語。','虫と人が遊ぶ幻想として完結。','夢の中の昔の子供との遊びが完結。','',
'うるおいのある声は比喩として音楽の主題を維持。','イベントの計画/準備/達成がつながる。','友人の引越しと葉の喪失の比喩がつながる。',
'話す虫と希望の創作。','小さな船で冒険する幻想として完結。','貝殻を友人へ分ける具体的な行動がある。',
'祭りの風船作りと伝統の流れ。','一人の王子が友人を得る完結。','魚の友達/パーティーの擬人化を誤りとしない。',
'魚の会話と競争を同じ場面で完結。','花冠を協力して作る心理変化がある。','嘲笑から勉強/自信への時間推移がある。',
'花選びと贈り物を同じ主題で完結。','','木の夢から友人の協力へつなぐ幻想。','火が消えて手をつなぐ因果がある。',
'歌の本心をめぐる対立と和解。抽象性は残るが嘘という比喩だけで破綻とはしない。','','実で作る夢という幻想設定内で仲直りを描く。',
'失った貝と新しい思い出を区別して完結。','楽器の世界という比喩/創作の中で音楽の主題を維持。','花/風/散歩の対象がつながる。',
'怖さから友人と波に乗る行動へつながる。','森の花と明暗を扱う教訓の幻想。','','怖い声から友人を呼び戻す行動がある。',
'過去の地域交流の催しとして生徒/来場者の行動がつながる。','団体設立と共通プラットフォームの説明が完結。',
'資金/政府/民間の役割を一つの計画として説明。','','ニュートンの言葉と発見の過程の説明。見出し語は残るが未提示画像参照ではない。',
'自己PRと志望動機のつながりを説明。個別応募書類の未提示参照ではない。','','地蔵の伝承の物語として因果を説明。',
'企業決算の数値/部門/増益理由を説明。','','','読書と表現についての一般的主張。事実の独立認証ではない。',
'監督の式典/展示を一つのニュースとして説明。','慈江道の移動/配給と閉鎖性の関係を説明。','','']

if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--revision',choices=('v2','v3'),default='v2');a=p.parse_args()
    data=Path('/home/aihub_ubuntu/jmicro-data/phase6/curriculum-strategy-20261005-'+a.revision)
    run=ROOT/('reports/phase6/curriculum-strategy-20261005-'+a.revision)
    sample=read_json(data/'sample64.json');reviews=[];weak=V2_WEAK if a.revision=='v2' else V3_WEAK
    assert len(sample)==64 and (a.revision=='v2' or len(V3_NOTES)==64)
    for i,r in enumerate(sample):
        reviews.append(dict(sample_index=i,doc_id=r['doc_id'],canonical_sha256=r['canonical_sha256'],group=r['group'],text=r['text'],
            weak=i in weak,note=weak.get(i,V3_NOTES[i] if a.revision=='v3' else '本文の主体/出来事/説明のつながりと末尾を確認。幻想や比喩のみでは誤りとせず、独立した人手認証とはしない。')))
    result=dict(created_at=now(),sample_sha256=sha256(data/'sample64.json'),documents=64,weak_documents=len(weak),
        passed=len(weak)<=10,reviews=reviews,method='Codex non-blind full64 review; not independent human certification',
        decision='Bounded strategy comparison may use v3 under unchanged10/64 threshold; fantasy/anthropomorphism and some promotions remain, not certified everyday-only material.' if a.revision=='v3' else 'Do not train this pool. One selector revision with unseen fixed sample; preserve original failed64 and source snapshot.')
    write_json(run/'content-review.json',result)
