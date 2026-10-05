from pathlib import Path
import sys
import numpy as np

from jmicro.larger_material_v2 import material_units
from jmicro.nested_material_v2 import material_unit
from jmicro.tokenizer import Tokenizer
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from probe_larger_web_supply import containing_document


def test_all_intact_lead_blocks_have_original_bytes_and_one_parent_split():
    tok=Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    a="図書館では多くの本を読むことができる。静かな閲覧室があり、椅子に座って本を読める。本を借りるときには利用者のカードを窓口に出す。返却期限を確認して、期限までに本を返す。入口には開館時間を示す看板がある。"
    b="畑では季節に合わせて野菜を育てる。土を耕してから種をまき、芽が出るまで水をやる。育った野菜は収穫して家に持ち帰る。収穫した野菜を洗ってから鍋に入れ、夕食の料理を作る。畑での作業には長靴と手袋を使う。"
    text="題名\n\n"+a+"\n\n"+b+"\n\n前の話の続きは\n\n"+a
    first=material_unit(text,tok.encode(text),"web",tok)
    units=material_units(text,tok.encode(text),"web",tok)
    assert first and len(units)==2
    assert first["canonical_sha256"]==units[0]["canonical_sha256"]
    assert len({(u["split"],u["source_family"]) for u in units})==1
    for u in units:
        assert text[u["source_char_start"]:u["source_char_end"]]==u["text"]
        assert tok.decode(u["token_ids"][1:-1])==u["text"]
    whole=material_units(a,tok.encode(a),"web",tok)
    assert len(whole)==1 and whole[0]["unit_kind"]=="original-whole"
    assert material_units(text,tok.encode(text),"story",tok)==[]


def test_token_uniform_containing_record_includes_every_boundary_and_corrects_length_bias():
    records=[[2,8,3],[2,*([9]*7),3],[2,10,10,3]]
    tokens=np.asarray(sum(records,[]),dtype="<u2")
    selected={0:2,3:7,12:1}
    rates=[]
    for offset in range(len(tokens)):
        a,b=containing_document(tokens,offset,maximum_body=7)
        assert tokens[a]==2 and tokens[b]==3 and a<=offset<=b
        rates.append(selected[a]/(b-a+1))
    assert np.isclose(np.mean(rates)*len(tokens),sum(selected.values()))
    oversized=np.asarray([2,*([8]*8),3],dtype="<u2")
    assert all(containing_document(oversized,i,maximum_body=7) is None for i in range(len(oversized)))


def test_first32_keeps_later_intact_blocks_without_weakening_content_filters():
    from jmicro.larger_material_v3 import material_units as broader
    tok=Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    valid="図書館では多くの本を読むことができる。静かな閲覧室があり、椅子に座って本を読める。本を借りるときには利用者のカードを窓口に出す。返却期限を確認して、期限までに本を返す。入口には開館時間を示す看板がある。"
    text="\n\n".join(["見出し"]*5+[valid,"しかし、"+valid])
    assert material_units(text,tok.encode(text),"web",tok)==[]
    selected=broader(text,tok.encode(text),"web",tok)
    assert len(selected)==1 and selected[0]["paragraph_position"]==5
    assert text[selected[0]["source_char_start"]:selected[0]["source_char_end"]]==selected[0]["text"]
    deep="\n\n".join(["見出し"]*32+[valid])
    assert broader(deep,tok.encode(deep),"web",tok)==[]


def test_builder_worker_emits_multiple_complete_units_from_one_native_parent(monkeypatch):
    import prepare_larger_material_v3 as builder
    tok=Tokenizer(ROOT/"artifacts/phase2/4096/tokenizer.model")
    a="図書館では多くの本を読むことができる。静かな閲覧室があり、椅子に座って本を読める。本を借りるときには利用者のカードを窓口に出す。返却期限を確認して、期限までに本を返す。入口には開館時間を示す看板がある。"
    b="畑では季節に合わせて野菜を育てる。土を耕してから種をまき、芽が出るまで水をやる。育った野菜は収穫して家に持ち帰る。収穫した野菜を洗ってから鍋に入れ、夕食の料理を作る。畑での作業には長靴と手袋を使う。"
    original="題名\n\n"+a+"\n\n"+b+"\n\nこのページの続きは"
    ids=tok.encode(original); train=np.asarray([2,*ids,3],dtype="<u2")
    monkeypatch.setattr(builder.decode,"_TOK",tok)
    monkeypatch.setattr(builder.decode,"_TRAIN",train)
    monkeypatch.setattr(builder.decode,"_PIECES",[tok.decode_bytes([i]) if i!=1 else b"" for i in range(tok.vocab_size)])
    rows=builder.worker(("web",[(0,len(train)-1)]))
    assert len(rows)==2 and len({(r["source_start"],r["source_end"],r["split"]) for r in rows})==1
    assert all(original[r["source_char_start"]:r["source_char_end"]]==r["text"] for r in rows)
