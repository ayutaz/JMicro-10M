from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from prepare_story_text import story_candidate


class CharacterTokenizer:
    def encode(self,text): return [8]*len(text)


def test_full_story_preserves_ending_and_never_truncates_to_fit():
    text='ある日、太郎は公園へ行きました。友達と一緒に遊んで、楽しい時間を過ごしました。'
    unit=story_candidate(text,CharacterTokenizer())
    assert unit and unit['text']==text and unit['sentences']==2
    assert not story_candidate(text,CharacterTokenizer(),maximum=35)


def test_incomplete_opening_trailing_fragment_cliffhanger_and_loops_are_rejected():
    tok=CharacterTokenizer()
    for text in (
        'その後、太郎は公園へ行きました。友達と楽しい時間を過ごしました。',
        '太郎は公園へ行きました。友達と楽しい時間を過ごしました。まだ途中の文',
        '太郎は公園へ行きました。友達の行方は誰もわからなかった。',
        '太郎は公園へ行きました。太郎は公園へ行きました。'):
        assert story_candidate(text,tok) is None
