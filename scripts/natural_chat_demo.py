"""Loopback CPU UI for a completed matched SFT arm, independent of GPU jobs."""
import argparse
import os
from pathlib import Path
import sys
os.environ['CUDA_VISIBLE_DEVICES']=''
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.natural_chat_demo import serve

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--arm',choices=('C0','C1'),required=True)
    p.add_argument('--port',type=int,required=True);a=p.parse_args()
    assert 1024<=a.port<=65535
    serve(a.arm,a.port)
