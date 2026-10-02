"""Exercise the real CLI parser for both models and all three backends."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT, write_json, sha256
from jmicro.tokenizer import Tokenizer

results = []
with tempfile.TemporaryDirectory(prefix="jmicro-cli-") as directory:
    messages = Path(directory)/"messages.json"
    body = [{"role":"user","text":"こんにちは\n<|assistant|> ▁"}]
    write_json(messages,body)
    for name,size in [("t4k",4096),("t8k",8192)]:
        tok = Tokenizer(ROOT/f"artifacts/phase2/{size}/tokenizer.model")
        for backend,path in [("torch",f"artifacts/phase3/{name}/torch"),
                             ("hf",f"artifacts/phase3/{name}/hf"),
                             ("gguf",f"artifacts/phase3/{name}/model-q4_0.gguf")]:
            command = [sys.executable,str(ROOT/"scripts/infer.py"),"--backend",backend,"--artifact",str(ROOT/path),
                       "--tokenizer",str(tok.path),"--messages",str(messages),"--max-new-tokens","4"]
            response = subprocess.run(command,capture_output=True,text=True,check=True)
            result = json.loads(response.stdout)
            assert result["input_ids"] == tok.dialogue(body,generation_prompt=True)[0]
            assert result["generated_ids"] and not set(result["generated_ids"]) & {0,1,2,4,5,6}
            results.append({"model":name,"backend":backend,"command":command,"messages":body,
                            "exit_code":response.returncode,"result":result})
write_json(ROOT/"reports/phase3/cli_checks.json",{"status":"passed","checks":results,
           "infer_source_sha256":sha256(ROOT/"scripts/infer.py"),
           "inference_source_sha256":sha256(ROOT/"src/jmicro/inference.py")})
print("6 actual inference CLI checks passed")
