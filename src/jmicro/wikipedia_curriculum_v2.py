"""One prospective lead-selector revision for extraction holes and article promises.

Reject whole units without rewriting. Previous fixed64 article families are
calibration exclusions in the builder, never a new acceptance sample.
"""
import re
from jmicro.wikipedia_curriculum import lead as original_lead

# Missing foreign/link text leaves dangling punctuation, an empty language
# field, or an acronym-only sentence prefix. These are extraction symptoms;
# proper multilingual aliases and ordinary dates must remain available.
BROKEN = re.compile(
    r'[（(]\s*[、,]|[、,]\s*[）)]|[、,]\s*[、,]|'
    r'[：:]\s*[）)]|(?:^|[。！？]\s*)[（(][A-Z]{2,8}[）)]の|'
    r'(?:は|が|を)と[\u4e00-\u9fffァ-ヺ]|(?:は|が)に位置'
)
ARTICLE_PROMISE = re.compile(r'後述|前述|上述|本項|本記事|下記|以下を参照|詳細は.+参照')


def lead(record,tok):
    unit=original_lead(record,tok)
    if unit is None or BROKEN.search(unit['text']) or ARTICLE_PROMISE.search(unit['text']):
        return None
    return dict(unit,selector_revision='2: reject whole leads with missing metadata or external article promises')
