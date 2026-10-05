"""Reconstruct inner short-slot origins from the completed deterministic sampler."""
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.experiment import read_json,write_json,sha256,now
import run_complete_document_500m as study


def main():
    assert sys.version_info[:3]==(3,12,7)
    config=study.load_config();result=read_json(study.RUN/'result.json');trained=result['trained']
    ready=read_json(Path(config['pool_ready']['path']));cursor=trained['sampler']['short']
    assert cursor['epoch']==0 and cursor['context']==1024
    # Frozen builder writes accepted whole story documents first, followed by Web.
    boundary=ready['by_source']['story']['tokens']
    order=np.random.default_rng(np.random.SeedSequence([cursor['seed'],0])).permutation(cursor['blocks'])[:cursor['position']]
    starts=order.astype(np.int64)*cursor['context']
    story=int(np.clip(boundary-starts,0,cursor['context']).sum())
    short=cursor['position']*cursor['context'];web_in_short=short-story
    assert short==trained['source_tokens']['short']==99975168
    actual_web=trained['source_tokens']['web']+web_in_short
    assert actual_web+story==result['scientific_tokens']==500006912
    payload=dict(method='Exact input-token origin reconstruction from saved epoch0 sampler and frozen story-first/Web-second packing; no corpus rescan',
                 result_sha256=sha256(study.RUN/'result.json'),pool_ready_sha256=config['pool_ready']['sha256'],sampler=cursor,
                 short_slot=dict(story=story,web=web_in_short,total=short),whole_scientific_run=dict(story=story,web=actual_web,total=500006912),
                 scientific_story_fraction=story/500006912,old_control_story_fraction=99975168/500006912,
                 short_EOS_teachers=trained['source_eos_teachers']['short'],old_story_short_EOS_teachers=1105092,
                 protected_test_used=False,checked_at=now())
    write_json(study.RUN/'source-origin-diagnosis.json',payload)
    print(json.dumps(payload),flush=True)


if __name__=='__main__':main()
