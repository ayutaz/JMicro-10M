"""Atomic state files for restartable large corpus jobs."""
import json
import os
from pathlib import Path
import time


def write_json(path, value):
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+f".tmp-{os.getpid()}")
    with temporary.open("w",encoding="utf-8") as stream:
        json.dump(value,stream,ensure_ascii=False,indent=2,allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary,path)


def read_json(path):
    # The original acquisition runner predates atomic state writes. Only retry
    # transient empty/partial JSON while observing it; never restart its process.
    for attempt in range(4):
        try:
            return json.loads(Path(path).read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            if attempt==3:
                raise
            time.sleep(.05)
