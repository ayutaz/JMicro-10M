"""CPU-only80 raw responses, with official and bounded reference decoders."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
import importlib.util
import json
from pathlib import Path
import sys
import time
from urllib.request import Request,urlopen
from answer_learning_common import ROOT,RUN,DATA,PIN,save,ref,bound,read_json,now


def main():
    target=RUN/'reference_raw.json'
    assert not target.exists(),'Preserve all reference results, including partial failures'
    preparation=read_json(RUN/'reference_preparation.json')
    assert preparation['status']=='complete' and preparation['revision']==PIN
    for value in preparation['files'].values():bound(value)
    questions=read_json(bound(preparation['questions']))['questions']
    assert len(questions)==20
    directory=DATA/'reference'
    sys.path.insert(0,str(directory))
    spec=importlib.util.spec_from_file_location('akebono_official_chat',directory/'chat.py')
    official=importlib.util.module_from_spec(spec);sys.modules[spec.name]=official;spec.loader.exec_module(official)
    engine=official.Chat(directory,threads=2)
    assert engine.parameters==9965824
    models={}
    for name,port in (('JMicro_first_SFT_cap32',7861),('JMicro_C1_cap32',7862)):
        with urlopen(f'http://127.0.0.1:{port}/api/model',timeout=5) as response:models[name]=json.load(response)
        assert not models[name]['busy'] and models[name]['device']=='CPU' and models[name]['max_new_tokens']==32
    contract=dict(created_at=now(),source=ref(Path(__file__)),preparation=ref(RUN/'reference_preparation.json'),
        questions=preparation['questions'],local_models=models,reference_parameters=engine.parameters,
        reference_original_code_unchanged=True,reference_original_decoder=dict(max_tokens=128,character_cap=160),
        controlled_reference_decoder=dict(max_tokens=32,character_cap=None),
        wall_cap_each_condition=600,conditions=['Akebono_official','Akebono_cap32',*models],
        differences=['Reference vocabulary12288 vs local4096; token counts are not equal Japanese lengths',
            'Reference learned system frame vs local native chat prompt',
            'Reference original no suppression vs local suppress0,1,2,4,5,6',
            'Reference CPUFP32 and local CPUFP32, different models and training lineages',
            'Provided Assistant history is re-encoded by each tokenizer; no history removed'],
        protected_TEST_used=False,GPU_initialized=False,training_updates=0)
    save(RUN/'reference_execution_contract.json',contract)
    result=dict(status='running',contract=ref(RUN/'reference_execution_contract.json'),conditions={},created_at=now())
    save(target,result)
    try:
        for condition in contract['conditions']:
            started=time.monotonic();rows=[]
            result['conditions'][condition]=dict(status='running',responses=rows)
            for case in questions:
                assert time.monotonic()-started<600
                messages=case['messages']
                if condition.startswith('Akebono'):
                    assert all(m['role']!='system' for m in messages)
                    engine.reset()
                    engine.users=[m['content'] for m in messages[:-1] if m['role']=='user']
                    engine.bodies=[engine.tok.encode(m['content']) for m in messages[:-1] if m['role']=='assistant']
                    assert len(engine.users)==len(engine.bodies)
                    official.MAX_NEW=128 if condition=='Akebono_official' else 32
                    official.CHAR_CAP=160 if condition=='Akebono_official' else 10**9
                    prefix=engine.prefix(messages[-1]['content'])
                    assert len(prefix)+official.MAX_NEW<=512,'No context clipping permitted'
                    response=engine.send(messages[-1]['content'])
                    assert response['input_ids']==prefix and response['history']['dropped_history_turns']==0
                    assert not official.torch.cuda.is_initialized()
                    row=dict(id=case['id'],category=case['category'],messages=messages,response=response)
                else:
                    port=7861 if condition=='JMicro_first_SFT_cap32' else 7862
                    payload=json.dumps(dict(messages=messages,max_new_tokens=32),ensure_ascii=False).encode()
                    with urlopen(Request(f'http://127.0.0.1:{port}/api/chat',data=payload,
                        headers={'Content-Type':'application/json'}),timeout=min(90,600-(time.monotonic()-started))) as reply:
                        response=json.load(reply)['response']
                    assert response['max_new_tokens']==32 and response['removed_turns']==0
                    row=dict(id=case['id'],category=case['category'],messages=messages,response=response)
                rows.append(row);save(target,result)
                print(json.dumps(dict(condition=condition,id=case['id'],text=response['text'],
                    stop=response.get('stop_reason')),ensure_ascii=False),flush=True)
            result['conditions'][condition].update(status='complete',CPU_wall_seconds=time.monotonic()-started)
            assert len(rows)==20 and time.monotonic()-started<=600
            save(target,result)
        result.update(status='all80_raw_complete_pending_individual_content_notes',completed_at=now(),
            GPU_initialized=False,protected_TEST_used=False,training_updates=0)
    except BaseException as error:
        result.update(status='failed_partial_preserved',error=repr(error),observed_at=now());raise
    finally:save(target,result)


if __name__=='__main__':main()
