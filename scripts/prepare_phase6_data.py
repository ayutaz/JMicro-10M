"""Run through uv; all large expansion artifacts remain in the WSL data root."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.expanded_data import main

if __name__ == "__main__":
    main()
