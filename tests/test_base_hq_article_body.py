import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_hq_article_body import select_article


class Tokenizer:
    def encode(self,value): return [8]*len(value)


def test_only_original_contiguous_body_without_punctuation_repair():
    text='  旅の記録\r\n朝は雨だった。帰るころには青空が広がった。\r\n予約オプション:\r\nサイトの案内です。'
    result,error=select_article(text,Tokenizer(),minimum=1)
    assert error is None
    assert text.encode()[result['byte_start']:result['byte_end']]==result['text'].encode()
    assert result['text']=='旅の記録\r\n朝は雨だった。帰るころには青空が広がった。'
    assert result['removed_tail_chars']>0
    assert select_article('朝は雨だった。帰るころには青空が広がっ…',Tokenizer(),minimum=1)[0] is None


def test_oversized_whole_body_rejected_instead_of_sentence_eos_chunks():
    text='朝は雨だった。帰るころには青空が広がった。'*20
    result,error=select_article(text,Tokenizer(),minimum=1,maximum=64)
    assert result is None and error=='whole_article_token_length'


def test_reject_operations_but_keep_genuine_question_ending():
    tok=Tokenizer()
    assert select_article('会社を検索枠に入れてみてください。必要な情報をお試し機能で確認できます。',tok,minimum=1)[1]=='site_operation_body'
    text='私たちは星を眺めながら夜が更けるまで話をした。あの星の向こうには何があるのだろう？'
    result,error=select_article(text,tok,minimum=1)
    assert error is None and result['text']==text
