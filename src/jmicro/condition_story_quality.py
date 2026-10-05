"""Conservative whole-story exclusions; sampled diagnosis, not semantic certification."""
from collections import Counter
import re
from jmicro.complete_units import complete_sentences
from jmicro.story_quality import anchors, CONNECTOR

LESSON = re.compile(r'学[びぶんべ]|教訓|ということを知|ことがわか|ことが分か')
OVERGENERAL = re.compile(r'何でも|なんでも|どんな.{0,20}でも|すべて.{0,12}(?:でき|直せ|治せ)|誰でも.{0,15}でき')
DEPENDENT = re.compile(r'^(?:こうして|だから|その結果|それから|しかし|すると|やがて)[、,]')
SPEECH = re.compile(r'([^。！？!?「」\s、]{1,16}?)(?:は|が)「[^」]+」と(?:言|答|返|叫)')

def entity_anchors(text):
    # Retain one-kanji entities (星/月/犬/本 etc.); two-kanji-only anchors lost them.
    singles = set(re.findall(r'([一-龯])(?:は|が|を|に|で|と|の)', text)) - {'心','人','日','時','気'}
    return anchors(text) | singles

def exclusion_reasons(text):
    """Only observable local defects/proxies; never certify remaining meanings."""
    sentences = [s[2] for s in complete_sentences(text)]
    reasons = []
    if len(sentences) < 2:
        return ['not_whole_multisentence']
    if DEPENDENT.search(text):
        reasons.append('dependent_opening')
    # Preserve action-based endings rather than learning unsupported general lessons.
    closing = sentences[-1] if sentences[-1] not in ('おしまい。', 'おわり。') else sentences[-2]
    if LESSON.search(closing):
        reasons.append('didactic_closing')
    if OVERGENERAL.search(closing):
        reasons.append('unbounded_closing_generalization')
    normalized = [re.sub(r'[\s、。！？!?「」]', '', s) for s in sentences]
    if len(set(normalized)) != len(normalized):
        reasons.append('repeated_sentence')
    # Detect a local same-named speaker answering their immediately preceding quote.
    previous = None
    for sentence in sentences:
        speeches = list(SPEECH.finditer(sentence))
        for speech in speeches:
            entity = speech.group(1)
            if previous == entity and re.search(r'」と(?:答|返)', speech.group()):
                reasons.append('same_speaker_self_answer')
            previous = entity
        if not speeches and len(sentence) > 80:
            previous = None
    recent = [entity_anchors(sentences[0])]
    connected = 0
    for sentence in sentences[1:]:
        current = entity_anchors(sentence)
        if current & set().union(*recent[-3:]) or CONNECTOR.search(sentence):
            connected += 1
        recent.append(current)
    if connected / (len(sentences) - 1) < .8:
        reasons.append('weak_local_entity_topic_links')
    # Long repeated clauses survive an exact-sentence check in some translations.
    clauses = [c.strip() for c in re.split(r'[、。！？!?\n]', text) if len(c.strip()) >= 12]
    if any(n >= 3 for n in Counter(clauses).values()):
        reasons.append('repeated_long_clause')
    return sorted(set(reasons))
