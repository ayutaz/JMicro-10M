"""Change only Web input delivery; inherit the tested CE/KL math and grad buffers."""
from pathlib import Path
from jmicro.experiment import ROOT,read_json,sha256
from historical_parent_condition_trainer import historical_web_cursor
from resident_web_window import ResidentWebTokens
from web_kl_condition_trainer_v2 import WebKLTrainer as BaseWebKLTrainer,KIND

PREPARATION=ROOT/'reports/phase6/web_kl_resident_window_preparation.json'
_RESIDENT=None


def resident(view,cursor):
    global _RESIDENT
    p=read_json(PREPARATION)
    for path,digest in p['source_sha256'].items():
        if sha256(ROOT/path)!=digest:raise ValueError('Prepared resident input code differs')
    if _RESIDENT is None:
        _RESIDENT=ResidentWebTokens(view,cursor,73421,Path(p['cache_directory']))
    expected=p['cache']['binding']
    if (_RESIDENT.binding!=expected or _RESIDENT.binding['initial_cursor']!=cursor
            or _RESIDENT.binding['source_directory']!=str(view.directory)):
        raise ValueError('Resident actual parent window differs')
    return _RESIDENT


class WebKLTrainer(BaseWebKLTrainer):
    def __init__(self,parent,pool,original_web,positive,goals,binding,device='cuda',context=1024,batch=32,reference_batch=8):
        super().__init__(parent,pool,original_web,positive,goals,binding,device,context,batch,reference_batch)
        data=resident(original_web,historical_web_cursor(parent))
        self.sampler.streams['web'].sampler.shard=data.view(original_web)
        self.replay.stream.sampler.shard=data.view(original_web)
        self.spec.update(resident_window_manifest_sha256=data.manifest_sha256,
            resident_reader_sha256=sha256(ROOT/'scripts/resident_web_window.py'),resident_trainer_sha256=sha256(Path(__file__)))
