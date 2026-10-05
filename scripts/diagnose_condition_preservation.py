"""Plan61 stage1: preserve existing individually reviewed failures and source evidence."""
import json
from pathlib import Path
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-preservation-20261005')
RUN=ROOT/'reports/phase6/condition-preservation-100m-20261005'

def main():
    assert sys.version_info[:3]==(3,12,7)
    started=time.monotonic()
    old=ROOT/'reports/phase6/dataset-expansion-1b-20261005'
    review=read_json(old/'review.json');assert review['status']=='passed' and all(review['checks'].values())
    source=Path('/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005')
    sample=read_json(source/'shards/samples.json');content=read_json(source/'content-review.json')
    assert len(sample['rows'])==len(content['notes'])==40 and content['samples_sha256']==sha256(source/'shards/samples.json')
    examples=[]
    groups={'reference_subject':['base-007','base-009','base-037','base-062','base-079'],
            'quantity_time':['base-051','base-052','base-055','base-057','base-059','base-060'],
            'negation_cause':['base-012','base-016','base-085','base-090','base-096'],
            'repetition':['base-005','base-031','base-067','base-072','base-092']}
    for arm,rows in review['scored_outputs'].items():
        by={r['id']:r for r in rows};assert len(by)==80 and all(r['rationale'] for r in rows)
        for tag,ids in groups.items():
            examples.extend(dict(arm=arm,diagnostic_group=tag,**by[i]) for i in ids)
    data=dict(completed_at=now(),source_review_sha256=sha256(old/'review.json'),
        source_annotations_sha256=sha256(old/'annotations.json'),all160_prior_individual_reviews_reused=True,
        source40_prior_individual_reviews_reused=True,additional32_train_inspection='not required; existing40 include specific translated-story failures',
        category_totals={a:{category:dict(count=len(selected),relevance_below2=sum(r['relevance']<2 for r in selected),
            coherence0=sum(r['coherence']==0 for r in selected)) for category in sorted({r['category'] for r in rows})
            if (selected:=[r for r in rows if r['category']==category])} for a,rows in review['scored_outputs'].items()},
        examples=examples,source_samples=sample,source_individual_notes=content,
        source_failure_examples=[dict(sample=sample['rows'][i],note=content['notes'][i]) for i in (6,7,8,14)],
        observable_exclusions=['unsupported didactic closing/generalization','same-speaker immediate self-answer',
            'repeated sentence/long clause','weak recent entity/topic link','dependent opening'],
        not_solved_by_heuristics=['world knowledge','general arithmetic','implicit reference resolution','logical truth of all sentences'],
        comparison='Same translated-source base stream; selector subset contrast with identical lengths/EOS positions. Action endings and topic/dialogue distribution may also change; not a semantic-quality causal certificate.',
        protected_test_used=False,scientific_training_tokens=0,reviewer='Codex; reuse saved individual nonblind diagnoses',
        script_sha256=sha256(Path(__file__)),CPU_seconds=time.monotonic()-started)
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    write_json(DATA/'diagnosis.json',data)
    print(json.dumps(dict(status='stage1_saved_failure_diagnosis_complete',examples=len(examples),source40_weak=sum(n['weak_example'] for n in content['notes']),scientific_training_tokens=0)))

if __name__=='__main__':main()
