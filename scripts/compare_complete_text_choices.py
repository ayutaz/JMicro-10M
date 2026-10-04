"""Secondary paired CPU statistics from already saved choice scores; no new inference."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.japanese_evaluation import clustered_ci
from run_complete_text_comparison import RUN,PLAN

def main():
    plan=read_json(PLAN);screen=read_json(RUN/'result.json');report={}
    sources={}
    for task in plan['evaluation']['tasks']:
        saved={}
        for arm in plan['arms']:
            path=RUN/arm/'evaluation'/(task+'.json')
            payload=read_json(path)
            saved[arm]={r['id']:r for r in payload['rows']}
            sources[str(path.relative_to(ROOT))]=sha256(path)
        baseline=saved['web'];report[task]={}
        for arm in ('short20','coherent20'):
            assert set(saved[arm])==set(baseline)
            differences=[]
            for key,a in baseline.items():
                b=saved[arm][key];family=a.get('family',key);assert family==b.get('family',key)
                differences.append({'id':key,'family':family,'difference':b['credit']-a['credit']})
            report[task][arm]=clustered_ci(differences,key='difference')
            if task=='semantics':
                groups={}
                for row in differences:groups.setdefault(row['family'],[]).append(row['id'])
                both=[]
                for family,ids in groups.items():
                    assert len(ids)==2
                    difference=int(all(saved[arm][i]['credit']==1 for i in ids))-int(all(baseline[i]['credit']==1 for i in ids))
                    both.append({'id':family,'family':family,'difference':difference})
                report[task][arm]['both_contexts_difference']=clustered_ci(both,key='difference')
    result=dict(status='complete',created_at=now(),config_sha256=sha256(PLAN),screen_result_sha256=sha256(RUN/'result.json'),
      source_sha256=sources,reviewer_source_sha256=sha256(Path(__file__)),paired_differences_from_web=report,
      additional_inference=0,additional_training_tokens=0,selection_gates_unchanged=True,
      limits='Secondary diagnostic; one training seed. Cluster paired bootstrap by existing frozen family, not evidence of practical Base quality.')
    write_json(RUN/'choice-paired-comparison.json',result)
    print(report)

if __name__=='__main__':main()
