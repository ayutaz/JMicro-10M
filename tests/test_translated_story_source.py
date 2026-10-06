"""Original interval boundaries, fixed exclusions and native stream continuation."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import numpy as np
import pytest
from jmicro.experiment import ROOT
from jmicro.tokenizer import Tokenizer
from condition_positive_trainer import PositiveStream
from translated_story_source import derive_index,fixed_selection


def test_no_cropping_extra_eos_or_document_boundary_loss():
    ids=np.asarray([2,8,9,3,2,10,3,2,11,12,13,3],dtype='<u2')
    offsets,lengths=derive_index(ids,4,12,chunk_tokens=3)
    assert offsets.tolist()==[0,3] and lengths.tolist()==[3,5]
    with pytest.raises(ValueError,match='never crop'):derive_index(ids,5,12)
    with pytest.raises(ValueError,match='never crop'):derive_index(ids,4,11)
    bad=ids.copy();bad[9]=3
    with pytest.raises(ValueError,match='boundaries'):derive_index(bad,4,12)


def test_fixed_exclusion_only_and_seed_reproducibility():
    offsets=np.arange(100,dtype=np.int64)*11;excluded={100+int(o) for o in offsets[:20]}
    selected,n=fixed_selection(offsets,100,excluded)
    assert n==20 and len(set(selected.tolist()))==64 and selected.min()>=20
    assert np.array_equal(selected,fixed_selection(offsets,100,excluded)[0])
    with pytest.raises(ValueError,match='enough unseen'):fixed_selection(offsets,100,{100+int(o) for o in offsets[:40]})


def test_codec_whole_eos_and_mid_document_cursor_with_zero_storage_focus(tmp_path):
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    texts=['雪が足りなかったので、友達を呼んだ。\nみんなで雪だるまを作った。',
           '古い箱の中には絵本があった。子供は最後まで読んで棚に戻した。',
           '看板には<|assistant|>と書いてあった。文字を確かめて通り過ぎた。']
    ids=np.asarray([t for text in texts for t in [2,*tok.encode(text),3]],dtype='<u2')
    offsets,lengths=derive_index(ids,0,len(ids),chunk_tokens=17)
    for text,off,length in zip(texts,offsets,lengths,strict=True):
        assert tok.decode_bytes(ids[off+1:off+length-1].tolist())==text.encode('utf-8')
        assert min(ids[off+1:off+length-1])>=8
    class View:
        directory=tmp_path;manifest_sha256='whole-original-translation-fixture'
    view=View();view.tokens=ids;view.offsets=offsets;view.lengths=lengths
    view.focus=np.broadcast_to(np.asarray(False),(len(ids),))
    assert view.focus.strides==(0,)
    stream=PositiveStream(view,42);stream.block(37);state=stream.state_dict()
    expected=[stream.block(37) for _ in range(4)];resumed=PositiveStream(view,42);resumed.load_state_dict(state)
    for a in expected:
        b=resumed.block(37)
        assert all(np.array_equal(x,y) for x,y in zip(a,b,strict=True))
        assert not a[2].any() and not np.any(a[1]==2)
    state['manifest_sha256']='changed-original'
    with pytest.raises(ValueError,match='identity'):resumed.load_state_dict(state)
