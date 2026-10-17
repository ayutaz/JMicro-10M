"""CPU loopback access to completed new SFT arms; no dataset body reader."""
import argparse
import json
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import signal
import sys
import threading
from http.server import ThreadingHTTPServer
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.chat_demo import ChatEngine,make_handler
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer

CONFIG=ROOT/'configs/phase7/answer-curriculum-resource-v2-20261017.json'
CONFIG_SHA='e9172f65215fe44f2a94f5c0e9f1429175a27917b3d32b3e09c848cb318e9e46'
RUN=ROOT/'reports/phase7/chat-answer-learning-20261017/curriculum-main-resource-v2'
PARENT_SHA='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'


class Engine(ChatEngine):
    def __init__(self,arm):
        assert arm in ('C0','C1') and not torch.cuda.is_available()
        torch.set_num_threads(2);assert sha256(CONFIG)==CONFIG_SHA
        c=read_json(CONFIG);result=read_json(RUN/arm/'result.json')
        assert result['status']=='learning_complete' and result['config_sha256']==CONFIG_SHA and result['parameter_count']==10001152
        assert c['parent']['sha256']==PARENT_SHA
        value=result['checkpoint'];checkpoint=Path(value['path']);tokenizer=Path(c['tokenizer']['path'])
        assert checkpoint.parent==RUN/arm and sha256(checkpoint)==value['sha256'] and sha256(tokenizer)==c['tokenizer']['sha256']
        for name in ('src/jmicro/model.py','src/jmicro/tokenizer.py','src/jmicro/chat_evaluation.py','src/jmicro/training.py'):
            assert sha256(ROOT/name)==c['source_sha256'][name]
        state=torch.load(checkpoint,map_location='cpu',weights_only=False)
        assert state['update']==value['update'] and state['supervised_tokens']==value['Assistant_teachers'] and 1000000<=state['supervised_tokens']<=1000031
        assert state['sampler']==result['sampler'] and state['lineage']['base_checkpoint']['sha256']==PARENT_SHA
        assert state['lineage']['optimizer_policy']=='fresh' and state['implementation_sha256']==c['implementation']
        assert state['spec']['teacher_chat']['data_binding']==c['arms'][arm]['sampler_binding']
        self.tok=Tokenizer(tokenizer);self.model=JMicroModel(state['model_config'])
        self.model.load_state_dict(state['model'],strict=True);self.model.eval().requires_grad_(False)
        assert sum(p.numel() for p in self.model.parameters())==10001152 and all(bool(torch.isfinite(p).all()) for p in self.model.parameters())
        self.lock=threading.Lock();self.stopping=threading.Event()
        self.info=dict(name='JMicro-10M 回答学習 '+arm,kind='改善教材の会話モデル（試験中）' if arm=='C1' else '比較用の会話モデル（試験中）',
            arm=arm,checkpoint=str(checkpoint),checkpoint_sha256=value['sha256'],config_sha256=CONFIG_SHA,parent_sha256=PARENT_SHA,
            tokenizer_sha256=c['tokenizer']['sha256'],parameters=10001152,SFT_teacher_tokens=state['supervised_tokens'],
            device='CPU',precision='FP32 / math attention',decoding='greedy',context=1024,max_new_tokens=32,max_new_tokens_range=[8,64],
            Chat_adopted=False,Base_adopted=False,quality_status='研究用の比較。正式採用は未確定。')
        del state


def main():
    p=argparse.ArgumentParser();p.add_argument('--arm',choices=['C0','C1'],required=True);p.add_argument('--port',type=int,required=True);a=p.parse_args()
    assert 1024<=a.port<=65535
    engine=Engine(a.arm);server=ThreadingHTTPServer(('127.0.0.1',a.port),make_handler(engine))
    path=ROOT/f'reports/local/chat-answer-{a.arm}/server.json';path.parent.mkdir(parents=True,exist_ok=True)
    record=dict(status='running',started_at=now(),pid=os.getpid(),boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
        start_ticks=Path(f'/proc/{os.getpid()}/stat').read_text().split()[21],url=f'http://127.0.0.1:{a.port}',
        **engine.info,GPU_initialized=False,training_launched=False)
    def write():path.write_text(json.dumps(record,ensure_ascii=False,indent=2))
    write()
    def stop(*_):engine.stopping.set();threading.Thread(target=server.shutdown,daemon=True).start()
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    try:server.serve_forever(poll_interval=.2)
    finally:server.server_close();record.update(status='stopped',ended_at=now());write()


if __name__=='__main__':main()
