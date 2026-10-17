"""CPU-only loopback UI for the completed input-structure arms."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import argparse
import json
from pathlib import Path
import signal
import threading
from http.server import ThreadingHTTPServer
import answer_curriculum_chat_demo as inherited
from chat_recovery_contract import CONFIG,RUN,ROOT
from answer_learning_common import sha256,read_json,now
from jmicro.chat_demo import make_handler

CONFIG_SHA='29a5fa2541f321a8de26f4f54ee98879bfc2245f232ebfe5246d09069d65f075'
inherited.CONFIG=CONFIG;inherited.CONFIG_SHA=CONFIG_SHA;inherited.RUN=RUN


class Engine(inherited.Engine):
    def __init__(self,arm):
        super().__init__(arm)
        self.info.update(name='JMicro-10M 情報配置 '+arm,
            kind='情報配置の会話モデル（研究用・未採用）' if arm=='C1' else '情報配置の対照モデル（研究用・未採用）',
            quality_status='全評価と実会話で判定する研究用モデル。正式採用は別判定。')


def main():
    p=argparse.ArgumentParser();p.add_argument('--arm',choices=['C0','C1'],required=True);p.add_argument('--port',type=int,required=True);a=p.parse_args()
    assert a.port in (7866,7867) and sha256(CONFIG)==CONFIG_SHA
    engine=Engine(a.arm);server=ThreadingHTTPServer(('127.0.0.1',a.port),make_handler(engine))
    target=ROOT/f'reports/local/chat-input-structure-{a.arm}/server.json'
    record=dict(status='running',started_at=now(),pid=os.getpid(),boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
        start_ticks=Path(f'/proc/{os.getpid()}/stat').read_text().split()[21],url=f'http://127.0.0.1:{a.port}',
        source_sha256=sha256(Path(__file__)),**engine.info,GPU_initialized=False,training_launched=False)
    def write():target.parent.mkdir(parents=True,exist_ok=True);target.write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
    write()
    def stop(*_):engine.stopping.set();threading.Thread(target=server.shutdown,daemon=True).start()
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    try:server.serve_forever(poll_interval=.2)
    finally:server.server_close();record.update(status='stopped',ended_at=now());write()


if __name__=='__main__':main()
