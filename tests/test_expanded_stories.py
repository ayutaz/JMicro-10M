from jmicro.expanded_stories import translated_candidate

class Tok:
    def encode(self,text):return [8]*min(len(text),512)

def test_whole_finished_story_keeps_original_body():
    text='花子は本を忘れて家に戻りました。机の上で本を見つけ、かばんに入れました。'
    result=translated_candidate(text,Tok())
    assert result and result['text']==text and result['sentences']==2

def test_trailing_fragment_and_repeated_sentences_are_rejected():
    assert translated_candidate('花子は本を忘れて家に戻りました。机の上には',Tok()) is None
    assert translated_candidate('花子は本を忘れて家に戻りました。花子は本を忘れて家に戻りました。',Tok()) is None

def test_translation_header_and_unclosed_quotes_are_rejected():
    assert translated_candidate('日本語訳：花子は本を忘れて家に戻りました。机の上で本を見つけました。',Tok()) is None
    assert translated_candidate('花子は「本を忘れたと気づきました。机の上で本を見つけました。',Tok()) is None
