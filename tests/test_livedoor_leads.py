from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from prepare_livedoor_leads import first_lead,family_split


def test_original_lead_is_not_repaired_or_replaced_by_later_paragraph():
    header='http://news.livedoor.com/article/detail/123/\n2012-09-01\n記事の見出し\n'
    lead='散歩の帰りに見つけたパン屋で、焼きたてのパンを買った。家に戻ると、家族と一緒に食べた。'
    assert first_lead(header+lead+'\n\n別の段落。')==lead
    assert first_lead(header+lead[:-1]+'\n\n'+lead) is None
    assert first_lead(header+'「'+lead+'\n\n'+lead) is None
    assert first_lead(header+'■'+lead+'\n\n'+lead) is None
    assert first_lead('not an article\n'+lead) is None
    assert family_split('123')==family_split('123')
    assert {family_split(str(n)) for n in range(1000)}=={'train','dev','test'}
