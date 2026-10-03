"""One bounded CPU reproducibility comparison; preserve all strict failures."""
from pathlib import Path
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from jmicro.experiment import ROOT,now,read_json,sha256,write_json
from phase6_performance import identity,alive


def study(output,runtime):
    output.mkdir(parents=True,exist_ok=True)
    binding={'verifier_sha256':sha256(ROOT/'scripts/verify_nonorm_export.py'),
             'runner_sha256':sha256(Path(__file__)),'runtime_sha256':sha256(runtime/'source_receipt.json'),
             'mkl_cbwr':['AUTO','AUTO,STRICT','AVX2,STRICT','COMPATIBLE'],'threads':[1,2],
             'completion':'Evaluate all 8 fixed CPU configurations using all 12 original comparisons and both actual stop fixtures; no tolerance/input/model changes, no follow-up sweep'}
    with (output/'supervisor.lock').open('a+') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (output/'binding.json').exists():assert read_json(output/'binding.json')==binding
        else:write_json(output/'binding.json',binding)
        job={'status':'running',**identity(),'binding':binding,'started_at':now()}
        rows=[]
        try:
            for mode in binding['mkl_cbwr']:
                for threads in binding['threads']:
                    name=f"{mode.lower().replace(',','-')}-t{threads}"
                    directory=output/name
                    report=directory/'nonorm_export_parity_report.json'
                    if not report.exists():
                        log=output/f'{name}.log'
                        env=dict(os.environ,MKL_CBWR=mode,MKL_DYNAMIC='FALSE',OMP_DYNAMIC='FALSE')
                        with log.open('a') as stream:
                            child=subprocess.Popen([sys.executable,str(ROOT/'scripts/verify_nonorm_export.py'),
                                '--output',str(directory),'--runtime',str(runtime),'--threads',str(threads)],
                                env=env,stdout=stream,stderr=subprocess.STDOUT)
                            job.update(stage=name,worker=identity(child.pid),log=str(log))
                            while child.poll() is None:
                                job['heartbeat_at']=now();write_json(output/'job.json',job);time.sleep(2)
                            assert child.returncode in (0,1) and report.exists()
                    value=read_json(report)
                    assert value['status'] in ('passed','failed')
                    assert len(value['comparisons'])==12 and len(value['checks'])==11, 'Incomplete comparison; inspect before retry'
                    rows.append({'name':name,'status':value['status'],'report':str(report),
                        'report_sha256':sha256(report),'binding':value['binding'],'checks':value['checks'],
                        'comparisons':value['comparisons']})
                    write_json(output/'results.json',{'status':'running','results':rows,'binding':binding})
            write_json(output/'results.json',{'status':'complete','results':rows,'binding':binding,
                'successful':[row['name'] for row in rows if row['status']=='passed'],'completed_at':now()})
            job.update(status='complete',worker=None,completed_at=now())
        except Exception as error:
            job.update(status='failed',failure=f'{type(error).__name__}: {error}',completed_at=now())
            raise
        finally:write_json(output/'job.json',job)
        print(json.dumps({'status':'complete','successful':[row['name'] for row in rows if row['status']=='passed']}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--runtime',type=Path,default=ROOT/'artifacts/runtime-precise')
    args=parser.parse_args()
    study(args.output.resolve(),args.runtime.resolve())
