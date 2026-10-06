"""Cache only the already selected train Web block windows; preserve BlockSampler."""
import copy
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import time
import numpy as np
from jmicro.experiment import read_json,sha256,now
from jmicro.shards import BlockSampler
from jmicro.training import atomic_json


def selected_blocks(view,cursor,count):
    sampler=BlockSampler(view,cursor['context'],cursor['seed']);sampler.load_state_dict(cursor)
    result=[]
    while len(result)<count:
        if sampler.position==sampler.blocks:
            sampler.epoch+=1;sampler.position=0;sampler._shuffle()
        take=min(count-len(result),sampler.blocks-sampler.position)
        result.extend(sampler.order[sampler.position:sampler.position+take].tolist())
        sampler.position+=take
    return np.asarray(result,dtype='<i8')


def binding(view,cursor,count):
    if view.split!='train' or count<=0:raise ValueError('Positive train-only block window required')
    return dict(kind='resident-exact-selected-Web-window-v1',source_directory=str(view.directory),
        source_manifest_sha256=sha256(view.directory/'manifest.json'),source_tokens=len(view.tokens),
        source_stream_sha256=view.manifest['splits']['train']['stream_sha256'],initial_cursor=copy.deepcopy(cursor),
        context=cursor['context'],block_windows=count,newly_prepared_source_tokens=0,
        dtype='<u2',preserves_labels='Original BlockSampler still shifts targets and masks BOS; cache stores unchanged context+1 raw IDs')


def build(view,cursor,count,folder,workers=8,budget=180):
    expected=binding(view,cursor,count);folder=Path(folder);ready=folder/'ready.json'
    if ready.exists():
        loader=ResidentWebTokens(view,cursor,count,folder)
        return read_json(ready)
    folder.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    blocks=selected_blocks(view,cursor,count);context=cursor['context']
    temporary=folder/'windows.tmp';array=np.memmap(temporary,mode='w+',dtype='<u2',shape=(count,context+1))
    def read_block(block):
        start=int(block)*context
        return np.asarray(view.tokens[start:start+context+1]).copy()
    try:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            for start in range(0,count,2048):
                if time.monotonic()-started>budget:raise TimeoutError('Finite CPU cache budget exhausted')
                end=min(count,start+2048)
                array[start:end]=np.stack(list(executor.map(read_block,blocks[start:end])))
                atomic_json(folder/'progress.json',dict(status='building',completed_windows=end,total_windows=count,
                    elapsed_seconds=time.monotonic()-started,workers=workers,GPU_seconds=0,scientific_teacher_tokens=0))
        array.flush();del array
        temporary.replace(folder/'windows.bin');np.save(folder/'block_ids.npy',blocks,allow_pickle=False)
        record=dict(binding=expected,created_at=now(),workers=workers,CPU_elapsed_seconds=time.monotonic()-started,
            files={name:dict(sha256=sha256(folder/name),bytes=(folder/name).stat().st_size) for name in ('windows.bin','block_ids.npy')},
            GPU_seconds=0,scientific_teacher_tokens=0,
            limits='Derived duplicate storage of selected original train IDs, not new corpus. File hashes verify this cache; source integrity reuses its accepted manifest and train stream SHA, without rescanning12B.')
        atomic_json(ready,record)
        return record
    except BaseException:
        atomic_json(folder/'failure.json',dict(status='failed',elapsed_seconds=time.monotonic()-started,
            partial_cache_not_accepted=True,GPU_seconds=0,scientific_teacher_tokens=0))
        raise


class ResidentWebTokens:
    def __init__(self,view,cursor,count,folder):
        self.binding=binding(view,cursor,count);folder=Path(folder);r=read_json(folder/'ready.json')
        if r['binding']!=self.binding:raise ValueError('Cache source/cursor/shape binding differs')
        for name,detail in r['files'].items():
            path=folder/name
            if path.stat().st_size!=detail['bytes'] or sha256(path)!=detail['sha256']:
                raise ValueError('Derived cache bytes differ')
        blocks=np.load(folder/'block_ids.npy',allow_pickle=False)
        if len(blocks)!=count or not np.array_equal(blocks,selected_blocks(view,cursor,count)):
            raise ValueError('Exact parent-selected block list differs')
        self.values=np.fromfile(folder/'windows.bin',dtype='<u2').reshape(count,cursor['context']+1)
        self.values.flags.writeable=False
        self.slots={int(block):index for index,block in enumerate(blocks)}
        self.original_length=len(view.tokens);self.context=cursor['context'];self.dtype=self.values.dtype
        self.shape=(self.original_length,);self.manifest_sha256=sha256(folder/'ready.json')

    def __len__(self):return self.original_length

    def __getitem__(self,key):
        if (not isinstance(key,slice) or key.step not in (None,1) or key.start is None or key.stop is None
                or key.start%self.context or key.stop-key.start!=self.context+1):
            raise ValueError('Only original context+1 aligned BlockSampler slices allowed')
        block=key.start//self.context
        if block not in self.slots:raise ValueError('Requested block outside fixed parent window; no silent source fallback')
        return self.values[self.slots[block]]

    def view(self,original):
        wrapper=copy.copy(original);wrapper.tokens=self
        return wrapper
