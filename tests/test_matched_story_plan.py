from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from prepare_matched_story_pools import matched_quotas


def test_quotas_never_invent_missing_source_or_exceed_eligible_count():
    q=matched_quotas({32:100,64:100,96:100},{32:0,64:30,96:80},target=5000)
    assert q[32]==0 and q[64]<=30 and q[96]<=80
    assert sum((s+2)*n for s,n in q.items())>=5000


def test_source_exhaustion_uses_actual_common_capacity():
    q=matched_quotas({32:100,96:100},{32:3,96:4},target=100000)
    assert q=={32:3,96:4}
