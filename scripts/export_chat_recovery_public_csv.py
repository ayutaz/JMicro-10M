"""Export all400 already-reviewed public replies; never infer or change grades."""
import csv
import json
from chat_recovery_contract import RUN,CONFIG
from answer_learning_common import read_json,ref,save,now

target=RUN/'public400_responses.csv';assert not target.exists()
completion=read_json(RUN/'completion.json');assert completion['status']=='four_requested_steps_complete'
rows=[];sources={}
for arm in ('C0','C1'):
    directory=RUN/'public100'/arm;raw=read_json(directory/'raw.json');notes=read_json(directory/'notes.json')
    assert notes['raw']==ref(directory/'raw.json') and len(raw['responses'])==len(notes['judgments'])==200
    sources[arm]=dict(raw=ref(directory/'raw.json'),notes=ref(directory/'notes.json'))
    for row,note in zip(raw['responses'],notes['judgments'],strict=True):
        assert row['id']==note['id'] and row['turn']==note['turn']
        rows.append(dict(arm=arm,case=row['id'],category=row['category'],turn=row['turn'],final=row['final'],expected=row['expected'],
            response=row['response']['text'],stop=row['response']['stop_reason'],
            **{key:note[key] for key in ('grammar','relevance','context','factual_correct','task_pass','rationale')},
            actual_history=json.dumps(row['messages'],ensure_ascii=False)))
with target.open('x',encoding='utf-8-sig',newline='') as stream:
    writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
save(RUN/'public400_export.json',dict(created_at=now(),config=ref(CONFIG),CSV=ref(target),sources=sources,rows=400,source=ref(__file__),no_generation_or_rescoring=True))
print('Exported all400 public replies with existing factual/task judgments and full actual histories')
