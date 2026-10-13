"""Supply explicit src bootstrap to the frozen CPU audit; arithmetic unchanged."""
import argparse
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import audit_chat_lr as audit
from chat_lr_contract import preflight


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--training', action='store_true')
    args = p.parse_args()
    c, _, _ = preflight()
    audit.training(c) if args.training else audit.progress(c)
