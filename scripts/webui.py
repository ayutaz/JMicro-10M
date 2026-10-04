"""Launch the local UI through uv using the final trained checkpoint."""
import os
from pathlib import Path
import sys

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from jmicro.webui import main

if __name__ == "__main__":
    main()
