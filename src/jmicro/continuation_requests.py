"""Input-only planning for the original Base DEV400 and long40 policies.

No mixed suite, TEST reader, models, datasets or generation. Consumers use the
already pinned DEV80 artifact and must separately qualify their checkpoint.
"""
from collections import Counter
from dataclasses import dataclass

from jmicro.evaluation_boundary import DevSuite, load_dev_suite

POLICY = 'isolated_original_Base_DEV400_long40_requests_v1'
# Preserve legacy full-suite/long policies. The newer pilot suppresses EOT7
# additionally; do not silently apply its seven-ID policy to these requests.
LEGACY_SUPPRESS_IDS = (0, 1, 2, 4, 5, 6)
MODES = (('greedy', True, 42), ('greedy', False, 42),
         ('sampling', True, 42), ('sampling', True, 43), ('sampling', True, 44))


@dataclass(frozen=True)
class ContinuationRequest:
    stage: str
    case_id: str
    category: str
    prefix: str
    split: str
    decoding: str
    suppressed: bool
    seed: int
    max_new_tokens: int
    temperature: float | None
    top_p: float | None

    @property
    def key(self):
        return (self.stage, self.case_id, self.decoding, self.suppressed, self.seed, self.max_new_tokens)


def requests(suite):
    if not isinstance(suite, DevSuite) or len(suite.cases) != 80:
        raise ValueError('Pinned isolated DEV80 inputs required')
    standard = [ContinuationRequest('standard400', case['id'], case['category'], case['prefix'], 'dev',
                  mode, suppressed, seed, 64, .8 if mode == 'sampling' else None,
                  .9 if mode == 'sampling' else None)
                for case in suite.cases for mode, suppressed, seed in MODES]
    counts, selected = Counter(), []
    for case in suite.cases:
        if counts[case['category']] < 2:
            selected.append(case)
            counts[case['category']] += 1
    if len(selected) != 20 or len(counts) != 10 or any(n != 2 for n in counts.values()):
        raise ValueError('Original20 long prefixes: first2 per10 categories required')
    long = [ContinuationRequest('long40', case['id'], case['category'], case['prefix'], 'dev',
              'greedy', True, 42, maximum, None, None)
            for maximum in (128, 512) for case in selected]
    if len({request.key for request in standard + long}) != 440:
        raise ValueError('All440 distinct original request identities required')
    return tuple(standard + long)


def load_requests(manifest_path, manifest_sha256):
    suite = load_dev_suite(manifest_path, manifest_sha256)
    planned = requests(suite)
    return planned, dict(policy=POLICY, DEV_manifest_sha256=suite.manifest_sha256,
        DEV_cases_sha256=suite.cases_sha256, source_legacy_suite_sha256=suite.source_legacy_suite_sha256,
        evaluation_read_paths=list(suite.opened_paths), standard_requests=400, long_requests=40,
        full_suite_suppressed_ids=list(LEGACY_SUPPRESS_IDS), pilot_also_suppresses_EOT7=True,
        fixed80_equality_to_qualified_screen_must_be_checked=True,
        TEST_opened=False, model_forward_executed=False, Base_qualified=False)


def preflight_context(planned, tokenizer, maximum=1024):
    if not isinstance(planned, tuple) or len(planned) != 440 or maximum != 1024:
        raise ValueError('Original440 requests and context1024 required')
    lengths = {}
    for request in planned:
        if request.prefix not in lengths:
            lengths[request.prefix] = len(tokenizer.encode(request.prefix)) + 1
        if lengths[request.prefix] + request.max_new_tokens > maximum:
            raise ValueError('Original continuation request exceeds context; no silent prefix truncation')
    return dict(requests=440, unique_case_ids=len({r.case_id for r in planned}),
                maximum_prompt_tokens=max(lengths.values()), all_complete_prefixes_fit=True)


def validate_outputs(rows, planned, stage):
    expected = [request for request in planned if request.stage == stage]
    if stage not in ('standard400', 'long40') or len(rows) != len(expected):
        raise ValueError('All original400 or long40 outputs required')
    for row, request in zip(rows, expected):
        fields = dict(id=request.case_id, category=request.category, prefix=request.prefix,
            split='dev', decoding=request.decoding, suppressed=request.suppressed, seed=request.seed,
            max_new_tokens=request.max_new_tokens)
        if any(row.get(key) != value for key, value in fields.items()):
            raise ValueError('Actual continuation request/order/mode binding differs')
    return True
