"""Reuse complete training/screens in a fresh process with the original numerical flags."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.training import seed_all
from run_eos_complete_100m import main

if __name__ == '__main__':
    seed_all(42)
    torch.use_deterministic_algorithms(True)
    main()
