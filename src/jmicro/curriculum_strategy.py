"""Literal curriculum selection and a warmup fork; historical trainers unchanged."""
import hashlib
import re
from jmicro.complete_units import complete_sentences, unit_hash
from jmicro.evaluation import canonicalize_text
from jmicro.narrative_diversity import HUMAN, FANTASY
from jmicro.natural_learning import NaturalTrainer
from jmicro.whole_short_text import whole_candidate

REFERENCES=re.compile(r'画像|写真|図[123１２３表]|図の|図に|表の|上記|下記|前述|このページ|次のページ|こちら|一覧|ご提供|ご案内|ご希望|株式会社|当社|弊社|料金|価格|通販|公式サイト|続きを読む|取り扱い|詳細は|お問い合わせ')
STORY_STYLE=re.compile(r'^[ぁ-ん]{3,8}[、,。]|のように|のような|ざっくりした|時間旅行|異世界|夢が現実|おばけ|お化け|ウミウシ|にんぎょう|人形|光る玉|不思議|ちょうちょの国')
PROMOTION=re.compile(r'セミナー|当[館店]|本サイト|製品|商品|プレゼント|ご連絡|提供致|提供いた|スポンサー|出展|育毛|サプリ|頭皮|治療|医学|医療|血圧|糖質|参加者|参加する|次のとおり|例を挙げ|例として')


def select(text, size, source):
    text=canonicalize_text(text)
    unit=whole_candidate(text,size,source)
    if not unit or REFERENCES.search(text):return None
    if source=='story':
        if FANTASY.search(text) or STORY_STYLE.search(text) or not HUMAN.search(text):return None
        group='short' if size<=80 else 'narrative'
    else:
        # No genre/quote/conditional blacklist: preserve realistic language variety.
        if size<96 or PROMOTION.search(text) or len(list(complete_sentences(text)))<2:return None
        group='general'
    first=next(complete_sentences(text))[2]
    family_head=unit_hash(re.sub(r'[0-9０-９]+','N',first))
    return dict(text=text,canonical_sha256=unit_hash(text),group=group,
        family_head=family_head,sentences=unit['sentences'],repetition=unit['char4_repetition'])


def family_split(family):
    # The full parent family, rather than a name variant, determines split.
    return 'dev' if int(hashlib.sha256(family.encode()).hexdigest()[:8],16)%20==0 else 'train'


class StrategyTrainer(NaturalTrainer):
    def _set_token_lr(self):
        lr=super()._set_token_lr()
        warmup=self.pilot_binding.get('warmup_updates',0)
        if warmup:
            local=self.update-self.lineage['parent_update']
            lr*=min(1.,(local+1)/warmup)
            for group in self.optimizer.param_groups:group['lr']=lr
            self.scheduler._last_lr=[lr]*len(self.optimizer.param_groups)
        return lr
