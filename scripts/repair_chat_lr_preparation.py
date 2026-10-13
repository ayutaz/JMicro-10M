"""Preserve actual split incident and validate prepared DEV without TEST parsing."""
import json
from pathlib import Path
import re
from chat_lr_contract import RUN, OLD, DATA, reference, require_ref
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json


def main():
    fixed_source = ROOT / 'scripts/prepare_chat_lr.py'
    fixed = fixed_source.read_text()
    new_block = "for case in (json.loads(line) for line in require_ref(ref).read_text().splitlines()\n                                       if re.search(r'\"split\"\\s*:\\s*\"dev\"', line))}"
    old_block = "for case in (json.loads(line) for line in require_ref(ref).read_text().splitlines())}"
    assert fixed.count(new_block) == 1
    restored = fixed.replace('import math\nimport re\n', 'import math\n').replace(new_block, old_block)
    original = RUN / 'preparation_incident_v1/prepare_chat_lr.py'
    assert not original.exists()
    original.write_text(restored)
    prior = read_json(RUN / 'preparation_incident_v1/preparation.json')
    assert sha256(original) == prior['source']['sha256'], 'Original faulty source must be preserved exactly'
    old_config = read_json(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    parsed = []
    excluded = 0
    for ref in old_config['suites'].values():
        for line in require_ref(ref).read_text().splitlines():
            if not re.search(r'"split"\s*:\s*"dev"', line):
                excluded += 1
                continue
            row = json.loads(line)
            assert row['split'] == 'dev'
            parsed.append(row)
    assert len(parsed) == 240 and excluded == 20
    previous = {row['messages'][-1]['content'] for row in parsed}
    current = [json.loads(line) for line in (DATA / 'dev.jsonl').read_text().splitlines()]
    assert len(current) == 80 and not any(row['messages'][-1]['content'] in previous for row in current)
    audit = read_json(RUN / 'dev_audit.json')
    assert audit['passed'] and not audit['exact_final_question_overlap']
    assert not audit['near_Jaccard8_at_least80percent'] and not audit['surface_flags']
    assert audit['dev_sha256'] == sha256(DATA / 'dev.jsonl')
    audit.update(source=reference(original), corrected_overlap_observer=reference(Path(__file__)),
                 corrected_source=reference(fixed_source), corrected_at=now(),
                 only_DEV_objects_parsed_in_corrected_audit=True,
                 original_Chat_TEST_parsed_during_v1_preparation=True,
                 original_Chat_TEST_eligible_for_final_blind_confirmation=False,
                 required_final_TEST='fresh sealed Chat TEST after recipe selection; original Base TEST unreferenced',
                 incident=reference(RUN / 'protected_split_incident.json'))
    atomic_json(RUN / 'dev_audit.json', audit)
    prep = read_json(RUN / 'preparation.json')
    prep.update(source=reference(original), corrected_source=reference(fixed_source),
                DEV_audit=reference(RUN / 'dev_audit.json'),
                protected_split_incident=reference(RUN / 'protected_split_incident.json'),
                corrected_at=now(), original_Chat_TEST_unreferenced=False)
    atomic_json(RUN / 'preparation.json', prep)
    print('Original faulty source verified; corrected DEV-only overlap passed; actual TEST exposure retained')


if __name__ == '__main__':
    main()
