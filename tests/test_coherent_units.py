from jmicro.coherent_units import acceptable_sentences, coherent_units


class CharacterTokenizer:
    def encode(self, text):
        return [8]*len(text)


def test_selector_preserves_contiguous_complete_sentences_and_drops_tail():
    text = '公園で友人と散歩しました。その後、公園のベンチで休んで帰りました。書きかけの文'
    units = list(coherent_units(text, CharacterTokenizer(), minimum=20, maximum=64))
    assert len(units)==1 and units[0]['sentences']==2
    assert text[units[0]['char_start']:units[0]['char_end']]==units[0]['text']
    assert units[0]['text'].endswith('帰りました。')


def test_dependent_openings_advertisements_loops_and_topic_jump_are_rejected():
    for pieces in (
        ['そのため、散歩しました。','その後、帰りました。'],
        ['この料理はおいしいです。','その後、帰りました。'],
        ['料理にはコツがあります。','料理のコツを見てみましょう。'],
        ['友人と散歩しました。','その後、何をしたのでしょうか?'],
        ['友人と散歩しました。','無料キャンペーンに申し込みました。'],
        ['公園で散歩しました。','公園で散歩しました。'],
        ['公園で散歩しました。','宇宙には星があります。']):
        assert not acceptable_sentences(pieces)
    assert acceptable_sentences(['公園で散歩しました。','その後、家に帰りました。'])


def test_oversized_sentence_is_not_truncated_and_single_sentence_is_not_emitted():
    tok = CharacterTokenizer()
    assert not list(coherent_units('公園で友人と散歩しました。',tok,minimum=2,maximum=64))
    assert not list(coherent_units('公園で'+('ゆっくり'*20)+'散歩しました。その後、帰りました。',tok,minimum=2,maximum=64))
