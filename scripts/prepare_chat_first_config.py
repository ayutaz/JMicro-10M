"""Bind an existing pilot to the bounded diagnostic; never prepare new data."""
import argparse
import json
import math
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT, read_json, sha256, write_json
from jmicro.training import implementation_hashes
from chat_first_contract import PARENT_SHA, TOKENIZER_SHA, RUN, parent_state
from run_chat_first_sft import SOURCES, preflight
from probe_chat_first_batch import SOURCES as PROBE_SOURCES
from phase6_performance import alive


def prepare(final):
    directory = Path('/home/aihub_ubuntu/jmicro-data/phase7/real-persona-pilot-20261006')
    manifest = read_json(directory/'manifest.json')
    base = ROOT/'reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt'
    tok = ROOT/'artifacts/phase2/4096/tokenizer.model'
    probe_path = RUN.with_name(RUN.name+'-probe')
    batch = 8
    evidence = None
    if final:
        job = read_json(probe_path/'probe-job.json')
        assert job['status'] == 'complete' and not alive(job)
        report = read_json(probe_path/'batch-report.json')
        batch = report['selected_batch']
        evidence = dict(path=str(probe_path/'batch-report.json'), sha256=sha256(probe_path/'batch-report.json'))
    updates = math.ceil(121098/batch)
    c = dict(purpose='chat_first_diagnostic',Base_adopted=False,Chat_adopted=False,protected_test_used=False,route='direct-sft',
        parent=dict(path=str(base),sha256=PARENT_SHA), tokenizer=dict(path=str(tok),sha256=TOKENIZER_SHA),
        data_directory=str(directory),data_manifest_sha256=sha256(directory/'manifest.json'),
        train_records=dict(path=str(directory/'train.jsonl'),sha256=manifest['train_records_sha256']),
        dev_records=dict(path=str(directory/'dev.jsonl'),sha256=manifest['dev_records_sha256']),
        dialogue_binding=manifest['dialogue_binding'],series_budget=30567471,
        output=str(RUN.relative_to(ROOT)),GPU_budget_seconds=4200,training_GPU_budget_seconds=3600,resume_GPU_budget_seconds=600,
        total_experiment_GPU_budget_seconds=21600,implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        evaluation_sha256={p:sha256(ROOT/p) for p in ('eval/chat.jsonl','eval/base.jsonl','configs/evaluation/protocol.json')},
        spec=dict(seed=42,context=1024,batch=batch,accumulation=1,lr=1e-4,weight_decay=.01,warmup=max(1,math.ceil(.05*updates)),
            schedule_updates=updates,dtype='bf16',compile=False,backend='math',sampler='document',training_fast_path=False,
            scheduler='wsd',deterministic=True),
        probe_kind='sft',probe_source_sha256={p:sha256(ROOT/p) for p in PROBE_SOURCES},
        candidate_batches=[8,16,32,64],probe_warmup_updates=2,probe_measured_updates=6,probe_GPU_budget_seconds=600,
        probe_output=str(probe_path.relative_to(ROOT)),selection_policy='existing DEV screen then joint grammar/relevance, context, fewer repeats, earliest checkpoint',
        retention_policy=dict(maximum_relative_BPB_regression=.05,grammar_score2_must_not_decrease=True,failures_must_not_increase=True))
    if evidence: c['batch_evidence'] = evidence
    path = ROOT/'configs/phase7'/('chat_first_sft.json' if final else 'chat_first_probe.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():
        assert read_json(path) == c, 'Preserve frozen config; changes need a separate identified run'
    else: write_json(path,c)
    preflight(path,require_batch=final)
    state = parent_state(c)
    out = dict(status='CPU_diagnostic_preflight_passed',config=str(path),config_sha256=sha256(path),
        parent_checkpoint_sha256=PARENT_SHA,parameter_count=10001152,
        batch=batch,Assistant_teachers_budget=1899555,series_budget=30567471,Base_adopted=False,Chat_adopted=False,GPU_started=False)
    write_json(RUN.with_name(RUN.name+'-preparation')/('final_preflight.json' if final else 'initial_preflight.json'),out)
    print(json.dumps(out))


if __name__ == '__main__':
    assert sys.version_info[:3] == (3,12,7)
    parser=argparse.ArgumentParser();parser.add_argument('--final',action='store_true');prepare(parser.parse_args().final)
