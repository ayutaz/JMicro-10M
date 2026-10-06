import sys
from pathlib import Path
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts'),str(Path(__file__).resolve().parents[1]/'src')]
from prepare_public_magpie_prose import candidate,split_family


class Codec:
    def encode(self,text):self.text=text;return [8]*len(text)
    def decode(self,ids):return self.text


def record(body):
    user=next(f'独立した物語{i}を書いてください' for i in range(100) if split_family(f'独立した物語{i}を書いてください')[1]=='train')
    return dict(id=1,conversations=[dict(role='user',content=user),dict(role='assistant',content=body)])


def test_whole_body_preserved_without_prompt_role_or_truncation():
    body='少年は小川のそばに立ちました。'+('友達と一緒に橋を渡って家へ帰りました。'*5)
    row,error=candidate(record(body),Codec(),[])
    assert error is None and row['text']==body and row['split']=='train'
    assert row['body_tokens']==len(body) and 'prompt' not in row


def test_context_only_markdown_unfinished_and_fixed_dev_overlap_refused():
    body='少年は小川のそばに立ちました。'+('友達と一緒に橋を渡って家へ帰りました。'*5)
    for text,protected in [('もちろんです。'+body,[]),('# 説明\n'+body,[]),(body[:-1],[]),(body,[body[:20]])]:
        assert candidate(record(text),Codec(),protected)[0] is None


def test_repeated_user_prompt_families_keep_reserved_split():
    user=next(f'独立した物語{i}を書いてください' for i in range(100) if split_family(f'独立した物語{i}を書いてください')[1]=='dev')
    body='少年は小川のそばに立ちました。'+('友達と一緒に橋を渡って家へ帰りました。'*5)
    r=record(body);r['conversations'][0]['content']=user
    assert candidate(r,Codec(),[])[1]=='reserved_family'
