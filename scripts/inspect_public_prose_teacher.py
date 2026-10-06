"""Pin public teacher metadata anonymously; no inference or project training."""
import dataclasses
import json
import os
from pathlib import Path
import sys
os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1'
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from huggingface_hub import HfApi
from jmicro.experiment import ROOT,now,write_json


def main():
    target=ROOT/'reports/phase6/public_prose_teacher_metadata.json'
    if target.exists():raise ValueError('Preserve pinned metadata')
    info=HfApi(token=False).model_info('Qwen/Qwen3-4B-Instruct-2507',files_metadata=True,token=False)
    allowed={'config.json','generation_config.json','tokenizer.json','tokenizer_config.json','vocab.json','merges.txt','added_tokens.json','special_tokens_map.json','model.safetensors.index.json','README.md','LICENSE','LICENSE.txt'}
    files=[]
    for entry in info.siblings:
        if entry.rfilename in allowed or entry.rfilename.endswith('.safetensors'):
            lfs=dataclasses.asdict(entry.lfs) if dataclasses.is_dataclass(entry.lfs) else entry.lfs
            files.append(dict(path=entry.rfilename,bytes=entry.size,blob_id=entry.blob_id,lfs=lfs))
    result=dict(status='public_anonymous_pinned_teacher_metadata_not_recovered',repo_id=info.id,revision=info.sha,
        gated=info.gated,private=info.private,license=info.card_data.to_dict().get('license'),files=files,
        total_bytes=sum(f['bytes'] or 0 for f in files),created_at=now(),anonymous_access=True,
        model_url='https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507',teacher_precision='BF16',
        student_parameters=10001152,project_Chat_started=False,student_quantization_started=False,teacher_inference_started=False)
    if result['gated'] or result['private'] or result['license']!='apache-2.0':raise ValueError('Public Apache2 teacher required')
    write_json(target,result)
    print(json.dumps({k:result[k] for k in ('status','repo_id','revision','license','total_bytes')}))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
