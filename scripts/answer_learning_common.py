"""New five-stage answer-learning investigation; old experiments stay frozen."""
import hashlib
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256

RUN=ROOT/'reports/phase7/chat-answer-learning-20261017'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-answer-learning-20261017')
OLD_RUN=ROOT/'reports/phase7/chat-natural-sft-20261017'
OLD_DATA=Path('/home/aihub_ubuntu/jmicro-data/phase7/chat-natural-sft-20261017')
PIN='74b3a1739e6d16883177c6021b3c03a7d517c7fb'


def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def ref(path):
    path=Path(path)
    return dict(path=str(path),sha256=sha256(path))


def bound(value):
    path=Path(value['path'])
    assert path.is_file() and sha256(path)==value['sha256'],str(path)
    return path


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()
