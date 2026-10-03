import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location('corpus_handoff', Path(__file__).resolve().parents[1]/'scripts/watch_corpus_10b_audit_handoff.py')
handoff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(handoff)


class HandoffGuards(unittest.TestCase):
    def test_exact_live_identity(self):
        record = dict(pid=os.getpid(), boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                      start_ticks=Path('/proc/self/stat').read_text().split()[21])
        self.assertTrue(handoff.alive(record))
        record['start_ticks'] = 'wrong'
        self.assertFalse(handoff.alive(record))

    def test_export_stage_cannot_be_interrupted(self):
        self.assertFalse(handoff.ready(Path('/does/not/exist'), {'stage': 'export'}))

    def test_completed_export_and_frozen_source_guards(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = root/'configs/phase6/corpus_10b.json'
            config.parent.mkdir(parents=True)
            config.write_text(json.dumps({'minimum_train_stream_tokens': 10_000_000_000}))
            artifact = root/'export-001'
            (artifact/'shards').mkdir(parents=True)
            split = {'train': {'tokens': 10_000_000_000}}
            built = dict(config_sha256=handoff.sha256(config), target_met=True, splits=split, artifact_directory=str(artifact))
            handoff.write_json(root/'manifest.json', built)
            handoff.write_json(artifact/'shards/manifest.json', {'splits': split})
            source = root/'frozen.txt'
            source.write_text('original')
            handoff.write_json(root/'source_snapshot.json', {'frozen.txt': handoff.sha256(source)})
            handoff.write_json(root/'execution_v3_snapshot.json', {})
            job = {'stage': 'full_independent_serial_audit'}
            with patch.object(handoff, 'ROOT', root):
                self.assertTrue(handoff.ready(root, job))
                built['splits']['train']['tokens'] -= 1
                handoff.write_json(root/'manifest.json', built)
                with self.assertRaisesRegex(ValueError, 'frozen target'):
                    handoff.ready(root, job)
                built['splits']['train']['tokens'] += 1
                handoff.write_json(root/'manifest.json', built)
                handoff.write_json(artifact/'shards/manifest.json', {'splits': {}})
                with self.assertRaisesRegex(ValueError, 'counts differ'):
                    handoff.ready(root, job)
                handoff.write_json(artifact/'shards/manifest.json', {'splits': split})
                source.write_text('changed')
                with self.assertRaisesRegex(ValueError, 'Frozen source changed'):
                    handoff.ready(root, job)
