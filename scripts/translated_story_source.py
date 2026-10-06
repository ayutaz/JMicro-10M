"""Read-only original translation interval; no prose/quality-based selection."""
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import read_json, sha256
from jmicro.eos_pilot import TrainView

KIND='pinned_original_TRAIN_TinyStories_JA_translation_view_v1'
REPOSITORY='shibatch/TinyStories-JA'
REVISION='155b4e5842076c90e07a4934d5b68410fe21f65f'
TOKENIZER_SHA='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'


def derive_index(tokens, begin, end, chunk_tokens=4*1024*1024):
    if (type(begin) is not int or type(end) is not int or not 0<=begin<end<=len(tokens)
            or tokens[begin]!=2 or tokens[end-1]!=3):
        raise ValueError('Whole original BOS/body/EOS interval required; never crop')
    pieces=[]; eos=0
    for start in range(begin,end,chunk_tokens):
        block=tokens[start:min(end,start+chunk_tokens)]
        pieces.append(np.flatnonzero(block==2)+start-begin)
        eos+=int(np.count_nonzero(block==3))
    offsets=np.concatenate(pieces).astype('<i8')
    lengths=np.diff(np.r_[offsets,end-begin]).astype('<i4')
    selected=tokens[begin:end]
    if (eos!=len(offsets) or np.any(lengths<3) or np.any(lengths-1>1024)
            or not np.array_equal(offsets,np.r_[0,np.cumsum(lengths)[:-1]])
            or not np.all(selected[offsets+lengths-1]==3)):
        raise ValueError('Whole native document boundaries/EOS/context disagree')
    return offsets,lengths


def fixed_selection(offsets, begin, excluded_offsets, seed=2026100693, count=64):
    excluded=np.isin(offsets+begin,np.asarray(sorted(excluded_offsets),dtype=np.int64))
    eligible=np.flatnonzero(~excluded)
    if len(eligible)<count:raise ValueError('Fixed source cannot supply enough unseen calibration documents')
    selected=np.random.default_rng(seed).choice(eligible,count,replace=False)
    return selected,int(excluded.sum())


class TranslatedStoryTrainView:
    """PositiveStream protocol; mmap bodies unchanged, zero focus uses no large array."""
    def __init__(self,path,manifest_sha256,require_accepted=True):
        self.directory=Path(path)
        if sha256(self.directory/'manifest.json')!=manifest_sha256:raise ValueError('Translation view manifest differs')
        m=self.manifest=read_json(self.directory/'manifest.json')
        if (m['kind']!=KIND or m['repository']!=REPOSITORY or m['revision']!=REVISION
                or m['documents']!=499066 or m['new_original_corpus_tokens']!=0 or m['source_text_modified']
                or m['tokenizer_sha256']!=TOKENIZER_SHA or sha256(self.directory/'document-index.npz')!=m['arrays_sha256']
                or sha256(self.directory/'content-pilot.json')!=m['pilot_sha256']):
            raise ValueError('Pinned complete original TRAIN translation provenance required')
        if require_accepted:
            review=read_json(self.directory/'content-review.json')
            if (not review['all64_read'] or not review['training_pool_accepted'] or review['weak_documents']>10
                    or review['unresolved_grammar_documents'] or review['unresolved_grounding_documents']
                    or review['manifest_sha256']!=manifest_sha256 or review['pilot_sha256']!=m['pilot_sha256']
                    or review['notes_sha256']!=sha256(self.directory/'content-notes.json')):
                raise ValueError('Accepted raw-bound fixed64 original translation review required')
        native=TrainView(m['native_pool'],m['native_manifest_sha256'])
        stream=native.directory/'train.bin';stat=stream.stat()
        if [stat.st_size,stat.st_mtime_ns]!=m['native_stream_size_and_mtime_ns']:
            raise ValueError('Immutable recorded native source stream identity differs')
        begin,end=m['native_interval']
        self.tokens=native.tokens[begin:end]; self.byte_lengths=native.byte_lengths
        with np.load(self.directory/'document-index.npz',allow_pickle=False) as arrays:
            self.offsets=arrays['offsets'].copy();self.lengths=arrays['lengths'].copy()
        if (len(self.lengths)!=499066 or self.offsets.shape!=self.lengths.shape or len(self.tokens)!=m['serialized_tokens']
                or int(self.lengths.sum())!=len(self.tokens) or np.any(self.lengths<3) or np.any(self.lengths-1>1024)
                or not np.array_equal(self.offsets,np.r_[0,np.cumsum(self.lengths)[:-1]])
                or not np.all(self.tokens[self.offsets]==2) or not np.all(self.tokens[self.offsets+self.lengths-1]==3)):
            raise ValueError('Original native complete translation boundaries differ')
        self.focus=np.broadcast_to(np.asarray(False),(len(self.tokens),))
        self.manifest_sha256=manifest_sha256
