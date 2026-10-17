"""Start the existing SFT model on CPU; this command never trains."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.chat_demo import serve

if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=7861)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error('Port must be between 1024 and 65535')
    serve(args.port)
