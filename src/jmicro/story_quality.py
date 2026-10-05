"""Additional whole-story heuristics; never a semantic-quality certificate."""
import re
from jmicro.whole_short_text import whole_candidate
from jmicro.complete_units import complete_sentences

DEPENDENT = re.compile(r'^(?:次に|つぎに|すると|こうして|その時|そのあと|それから)')
AWKWARD = re.compile(r'なやましい風|ごゆっくりと時間|お菓子のお菓子|友達の友達の友達')
CONNECTOR = re.compile(r'^(?:ある日|その(?:後|ため|結果|日|人|時)|翌[日朝]|次の日|すると|そして|だから|しかし|それ(?:で|から|を|に)|やがて|ついに|最後に|結局|二人|みんな|彼[は女ら]|彼女)')
GENERIC = {'友達','仲間','笑顔','幸せ','一緒','時間','気持','物語','楽し','大切'}


def anchors(text):
    return (set(re.findall(r'(?=([一-龯]{2}))',text))-GENERIC)|set(re.findall(r'[ァ-ヶー]{2,}',text))


def improved_story(text,size):
    unit=whole_candidate(text,size,'story')
    if not unit or DEPENDENT.search(unit['text']) or AWKWARD.search(unit['text']):return None
    parts=[r[2] for r in complete_sentences(unit['text'])]
    prior=anchors(parts[0]);links=0
    for sentence in parts[1:]:
        current=anchors(sentence)
        if prior&current or CONNECTOR.search(sentence):links+=1
        prior|=current
    # Majority of transitions have an explicit entity/topic or connector.
    if links*2<len(parts)-1:return None
    unit['linked_transitions']=links
    return unit
