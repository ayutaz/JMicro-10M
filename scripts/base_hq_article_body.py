"""One conservative contiguous article span; never split paragraphs into EOS units."""
import hashlib
import re

FOOTER = re.compile(
    r'^(?:脚注|出典|参考文献|関連項目|外部リンク)(?:\[編集\])?\s*$'
    r'|^(?:Recommend\b|Back Number\b|NEXT PAGE\b|WEB用語集TOP|テーマ:|ラベル:)'
    r'|引用をストック|引用するにはまずログイン|限定公開記事のため引用'
    r'|予約オプション|トリップアドバイザーは .*パートナー提携'
    r'|の管理者様、ぜひご登録|ブログのトップへ|日本ブログ村'
    r'|^All Rights Reserved\b|^デザイナー[：:]'
    r'|^Next\s*[⇒→]|^旅行くちこみサイト|^ウィーン旅行記 TOP'
    r'|^\d{4}(?:年\s*\d{1,2}月\s*\d{1,2}日(?:[月火水木金土日]曜日)?|[-/]\d{2}[-/]\d{2})\s*$', re.I)
OPERATIONS = re.compile(r'検索枠|お試し機能|画像をクリック|掲示板を復活|推奨しているブラウザ|会員登録はアプリ版')
NOTICE = re.compile(r'(?:当HP|本サイト|当サイト|本ホームページ).{0,100}(?:免責|営利目的|著作権|責任)', re.S)
TERMINAL = re.compile(r'[。！？!?．.][」』”）)〉》]*$')
ELLIPSIS = re.compile(r'(?:\.{2,}|…|⋯)[」』”）)〉》]*$')
JAPANESE = re.compile(r'[ぁ-んァ-ヶ一-龯]')
BYLINE = re.compile(r'[A-Za-z][A-Za-z ._-]{1,39}$')


def select_article(text, tokenizer, minimum=64, maximum=8192):
    """Keep original leading material and body, removing only a recognized tail.

    This is a structural candidate, not a semantic classifier or whole-corpus
    acceptance. Retain headings inside the body; an oversized article is rejected
    rather than split. Original bytes/punctuation and source family stay bound.
    """
    lines = list(text.splitlines(keepends=True)); offset = 0; cut = len(text); marker = None
    for line in lines:
        value = line.strip()
        if FOOTER.search(value):
            cut, marker = offset, value
            break
        offset += len(line)
    prefix = text[:cut]
    left = len(prefix)-len(prefix.lstrip()); right = len(prefix.rstrip())
    value = text[left:right]
    if not value: return None, 'empty_body_before_footer'
    # A short roman byline is metadata only if it follows a sentence-closed body.
    body_lines = value.splitlines(keepends=True)
    if len(body_lines)>1 and BYLINE.fullmatch(body_lines[-1].strip()):
        previous = value[:-len(body_lines[-1])].rstrip()
        if TERMINAL.search(previous) and not ELLIPSIS.search(previous):
            right = left+len(previous); value = previous
    if OPERATIONS.search(value) or NOTICE.search(value): return None, 'site_operation_body'
    tiny_words = sum(0<len(line.strip())<=4 and JAPANESE.search(line.strip()) is not None and
        not TERMINAL.search(line.strip()) for line in value.splitlines())
    if tiny_words>=12: return None, 'many_extraction_word_breaks'
    if not TERMINAL.search(value) or ELLIPSIS.search(value): return None, 'no_sentence_closed_article_body'
    if len(JAPANESE.findall(value))<16: return None, 'insufficient_Japanese_prose'
    ids = tokenizer.encode(value)
    if not minimum<=len(ids)<=maximum: return None, 'whole_article_token_length'
    raw = text.encode('utf-8'); a=len(text[:left].encode('utf-8')); b=len(text[:right].encode('utf-8'))
    if raw[a:b] != value.encode('utf-8'): raise ValueError('Contiguous original byte span changed')
    return dict(text=value,body_ids=ids,char_start=left,char_end=right,byte_start=a,byte_end=b,
        original_span_sha256=hashlib.sha256(raw[a:b]).hexdigest(),native_body_tokens=len(ids),
        original_body_UTF8_bytes=b-a,removed_prefix_chars=left,removed_tail_chars=len(text)-right,
        footer_marker=marker), None
