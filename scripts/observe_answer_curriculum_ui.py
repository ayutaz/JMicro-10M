"""Actual HTTP assets, response controls and exact CPU process identity."""
import argparse
import hashlib
from urllib.request import urlopen
from pathlib import Path
from answer_learning_common import ROOT,save,ref,read_json,now
from run_answer_curriculum_resource_v2 import CONFIG,RUN
from phase6_performance import alive,identity


def main(arm):
    target=RUN/'practical'/arm/'UI_observation.json';assert not target.exists()
    port=7864 if arm=='C1' else 7865;url=f'http://127.0.0.1:{port}'
    record_path=ROOT/f'reports/local/chat-answer-{arm}/server.json';record=read_json(record_path)
    assert record['status']=='running' and alive(record) and record['GPU_initialized'] is False
    result=read_json(RUN/arm/'result.json');assets={}
    with urlopen(url+'/api/model',timeout=5) as response:
        import json
        info=json.load(response)
    assert info['arm']==arm and info['config_sha256']==ref(CONFIG)['sha256'] and not info['busy']
    assert info['checkpoint_sha256']==result['checkpoint']['sha256'] and info['device']=='CPU' and info['max_new_tokens']==32
    for route,name in (('/','index.html'),('/app.js','app.js'),('/style.css','style.css')):
        with urlopen(url+route,timeout=5) as response:body=response.read();content_type=response.headers['Content-Type']
        local=ROOT/'webui/chat'/name;assert body==local.read_bytes()
        assets[name]=dict(source=ref(local),bytes=len(body),HTTP_content_type=content_type,sha256=hashlib.sha256(body).hexdigest())
        if name=='index.html':
            html=body.decode();assert '<option value="32" selected>' in html
            assert all(f'<option value="{n}"' in html for n in (16,32,64))
        if name=='app.js':
            script=body.decode();assert 'max_new_tokens:Number(responseLength.value)' in script
            assert "history=[...request,{role:'assistant',content:raw.text}]" in script
    save(target,dict(created_at=now(),server=ref(record_path),actual_identity=identity(record['pid']),HTTP=info,assets=assets,
        response_choices=[16,32,64],default_tokens=32,raw_assistant_history_used=True,
        browser_render_automation=False,observation_via_actual_HTTP=True,new_generation_by_this_check=False,
        protected_TEST_used=False,source=ref(__file__)))
    print('Actual CPU UI identity/HTTP/assets/default32/choices16,32,64/history handler confirmed: '+url)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('arm',choices=['C0','C1']);main(p.parse_args().arm)
