"""CPU trial access to completed plan149 checkpoints; no corpus/TEST reader."""
from http.server import ThreadingHTTPServer
import json
import os
from pathlib import Path
import signal
import threading
import torch
from jmicro.chat_demo import ChatEngine,make_handler
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer

CONFIG_SHA='ec0b61b2961ef9294cb840cb86ad6f5ba291ea1c4a0213d0404e9fa87cdb464d'
PARENT_SHA='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
TOKENIZER_SHA='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'
RUN=ROOT/'reports/phase7/chat-natural-sft-20261017'


class NaturalChatEngine(ChatEngine):
    def __init__(self,arm):
        if arm not in ('C0','C1'):
            raise ValueError('Unknown trial model')
        if torch.cuda.is_available():
            raise RuntimeError('This trial UI must run with CUDA_VISIBLE_DEVICES empty')
        torch.set_num_threads(2)
        config=ROOT/'configs/phase7/chat-natural-sft-20261017.json'
        if sha256(config)!=CONFIG_SHA:
            raise ValueError('Frozen SFT config differs')
        c=read_json(config)
        result=read_json(RUN/arm/'result.json')
        if (result['status']!='learning_complete' or result['config_sha256']!=CONFIG_SHA or
                c['parent']['sha256']!=PARENT_SHA or c['tokenizer']['sha256']!=TOKENIZER_SHA or
                result['parameter_count']!=10001152):
            raise ValueError('Only completed same10M SFT checkpoints may be served')
        value=result['checkpoint']
        checkpoint=Path(value['path'])
        tokenizer=Path(c['tokenizer']['path'])
        if checkpoint.parent!=RUN/arm or sha256(checkpoint)!=value['sha256'] or sha256(tokenizer)!=TOKENIZER_SHA:
            raise ValueError('Completed checkpoint/tokenizer binding differs')
        # Read only execution metadata, source code and this completed model.
        for name in ('src/jmicro/model.py','src/jmicro/tokenizer.py','src/jmicro/chat_evaluation.py','src/jmicro/training.py'):
            if sha256(ROOT/name)!=c['source_sha256'][name]:
                raise ValueError('Frozen inference implementation differs')
        state=torch.load(checkpoint,map_location='cpu',weights_only=False)
        if (state['update']!=value['update'] or state['supervised_tokens']!=value['Assistant_teachers'] or
                not 1000000<=state['supervised_tokens']<=1000031 or state['sampler']!=result['sampler'] or
                state['lineage']['base_checkpoint']['sha256']!=PARENT_SHA or
                state['lineage']['optimizer_policy']!='fresh' or state['implementation_sha256']!=c['implementation'] or
                state['spec']['teacher_chat']['data_binding']!=c['arms'][arm]['sampler_binding']):
            raise ValueError('Checkpoint is not the frozen completed trial')
        self.tok=Tokenizer(tokenizer)
        self.model=JMicroModel(state['model_config'])
        self.model.load_state_dict(state['model'],strict=True)
        self.model.eval().requires_grad_(False)
        if sum(p.numel() for p in self.model.parameters())!=10001152 or not all(bool(torch.isfinite(p).all()) for p in self.model.parameters()):
            raise ValueError('Unexpected or nonfinite10M model')
        self.lock=threading.Lock();self.stopping=threading.Event()
        self.info=dict(name='JMicro-10M '+arm,
            kind='新しい会話モデル（試験中）' if arm=='C1' else '比較用の会話モデル（試験中）',
            arm=arm,checkpoint=str(checkpoint),checkpoint_sha256=value['sha256'],config_sha256=CONFIG_SHA,
            parent_sha256=PARENT_SHA,tokenizer_sha256=TOKENIZER_SHA,parameters=10001152,
            SFT_teacher_tokens=state['supervised_tokens'],device='CPU',precision='FP32 / math attention',
            decoding='greedy',context=1024,max_new_tokens=32,max_new_tokens_range=[8,64],
            Chat_adopted=False,Base_adopted=False,quality_status='研究用の比較。正式採用は未確定。')
        del state


def serve(arm,port):
    engine=NaturalChatEngine(arm)
    server=ThreadingHTTPServer(('127.0.0.1',port),make_handler(engine))
    record_path=ROOT/f'reports/local/chat-natural-{arm}/server.json'
    record=dict(status='running',started_at=now(),pid=os.getpid(),
        boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
        start_ticks=Path(f'/proc/{os.getpid()}/stat').read_text().split()[21],
        url=f'http://127.0.0.1:{port}',**engine.info,GPU_initialized=False,training_launched=False)
    record_path.parent.mkdir(parents=True,exist_ok=True)
    record_path.write_text(json.dumps(record,ensure_ascii=False,indent=2))
    def stop(*_):
        engine.stopping.set()
        threading.Thread(target=server.shutdown,daemon=True).start()
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    try:server.serve_forever(poll_interval=.2)
    finally:
        server.server_close();record.update(status='stopped',ended_at=now())
        record_path.write_text(json.dumps(record,ensure_ascii=False,indent=2))
