"""Three-source provenance accounting without modifying historical trainers."""
import json
import numpy as np
from jmicro.experiment import sha256
from jmicro.learning_curve import MilestoneMixture
from jmicro.packing_study import TeacherBudgetMixture
from amount_learning_trainer import CurveTrainer

GENRES = ("web", "story", "textbook")
TAG_MAPPING = {name:i for i,name in enumerate(GENRES)}


class ThreeSourceIndex:
    def __init__(self, view):
        detail=view.manifest["splits"]["train"];path=view.directory/"train.index.jsonl"
        assert sha256(path)==detail["index_sha256"]
        count=detail["documents"]
        self.offsets=np.empty(count,dtype=np.int64)
        self.lengths=np.empty(count,dtype=np.int32)
        self.sources=np.empty(count,dtype=np.uint8)
        offset=0;read=0
        with path.open() as stream:
            for i,line in enumerate(stream):
                row=json.loads(line)
                assert i<count and row["offset"]==offset and row["split"]=="train"
                self.offsets[i],self.lengths[i]=offset,row["body_tokens"]
                self.sources[i]=TAG_MAPPING[row["source"]]
                offset+=row["body_tokens"]+2;read+=1
        assert read==count and offset==len(view.tokens)

    def __len__(self):return len(self.offsets)

    def __getitem__(self,index):
        return dict(offset=int(self.offsets[index]),body_tokens=int(self.lengths[index]))


class ThreeSourceMixture(MilestoneMixture):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        assert np.isin(self.short.tags,list(TAG_MAPPING.values())).all()
        self.genre_teachers={g:0 for g in GENRES};self.genre_eos={g:0 for g in GENRES}

    def state_dict(self):
        return dict(super().state_dict(),genre_tag_mapping=TAG_MAPPING.copy())

    def load_state_dict(self,state):
        if state.get("genre_tag_mapping")!=TAG_MAPPING:
            raise ValueError("Three-source provenance tag mapping differs")
        if set(state["genre_teachers"])!=set(GENRES) or set(state["genre_eos"])!=set(GENRES):
            raise ValueError("Three-source provenance counters differ")
        super().load_state_dict(state)
        if sum(self.genre_eos.values())!=self.source_eos["short"]:
            raise ValueError("Three-source EOS accounting differs")

    def batch(self,size):
        consumed=self.source_teachers["short"]
        boundary=next((n for n in self.boundaries if n>consumed),None)
        if boundary is None:raise ValueError("Teacher budget exhausted")
        original=self.goals;self.goals=dict(web=0,short=boundary)
        try:
            # Call the inherited masking/cursor implementation directly. The
            # historical MilestoneMixture counts only Web/story tags.
            result=TeacherBudgetMixture.batch(self,size);y=result[1].numpy()
            for genre,tag in TAG_MAPPING.items():
                selected=self.short.last_target_tags==tag
                self.genre_teachers[genre]+=int(np.count_nonzero(selected & (y!=-100)))
                self.genre_eos[genre]+=int(np.count_nonzero(selected & (y==3)))
            assert sum(self.genre_teachers.values())==self.source_teachers["short"]
            assert sum(self.genre_eos.values())==self.source_eos["short"]
            return result
        finally:self.goals=original


class ThreeSourceTrainer(CurveTrainer):
    def __init__(self,parent,web,pool,mode,goals,binding,device="cuda"):
        super().__init__(parent,web,pool,mode,goals,binding,device)
        web_state=parent["sampler"]
        if web_state.get("kind")=="teacher-learning-curve-v1":web_state=web_state["web"]
        sampler=ThreeSourceMixture(web,pool,web_state,self.sampler.boundaries)
        if self.curve_mode=="decay":
            assert parent["sampler"]["genre_tag_mapping"]==TAG_MAPPING
            sampler.short.load_state_dict(parent["sampler"]["short"])
        self.sampler=sampler
        self.spec["genre_tag_mapping"]=TAG_MAPPING.copy()
        self._set_token_lr()
